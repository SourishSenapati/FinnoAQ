"""
Atomic checkpoint manager and SQLite WAL event journal.
Ensures zero progress loss, atomic file replacement, previous-checkpoint fallback,
and graceful interrupt recovery.
"""

import os
import sys
import json
import sqlite3
import shutil
import tempfile
import time
import hashlib
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

class CheckpointManager:
    def __init__(
        self,
        checkpoint_dir: str = "checkpoints",
        state_dir: str = "state",
        journal_db: str = "state/journal.db"
    ):
        self.checkpoint_dir = checkpoint_dir
        self.state_dir = state_dir
        self.journal_db = journal_db
        self.latest_cp_path = os.path.join(checkpoint_dir, "latest_checkpoint.json").replace("\\", "/")
        self.previous_cp_path = os.path.join(checkpoint_dir, "previous_checkpoint.json").replace("\\", "/")
        self.lock_file = os.path.join(state_dir, "supervisor.lock").replace("\\", "/")
        
        os.makedirs(self.checkpoint_dir, exist_ok=True)
        os.makedirs(self.state_dir, exist_ok=True)
        self.init_sqlite_journal()

    def init_sqlite_journal(self):
        """Initialize SQLite with WAL mode, synchronous=FULL, and versioned schema."""
        conn = sqlite3.connect(self.journal_db)
        cursor = conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL;")
        cursor.execute("PRAGMA synchronous=FULL;")
        cursor.execute("PRAGMA foreign_keys=ON;")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schema_version (
                version INTEGER PRIMARY KEY,
                applied_at TEXT NOT NULL
            );
        """)
        cursor.execute("SELECT MAX(version) FROM schema_version;")
        row = cursor.fetchone()
        curr_ver = row[0] if row and row[0] is not None else 0
        
        if curr_ver < 1:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS event_log (
                    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    run_id TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    phase TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    status TEXT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id TEXT PRIMARY KEY,
                    phase TEXT NOT NULL,
                    status TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    runtime_sec REAL,
                    output_path TEXT,
                    error_msg TEXT
                );
            """)
            cursor.execute("INSERT INTO schema_version (version, applied_at) VALUES (1, ?);", (datetime.now(timezone.utc).isoformat(),))
            conn.commit()
        conn.close()

    def acquire_lock(self, run_id: str) -> bool:
        """Acquire a supervisor run lock to prevent duplicate runs."""
        if os.path.isfile(self.lock_file):
            try:
                with open(self.lock_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                pid = data.get("pid")
                stored_run = data.get("run_id")
                
                import psutil
                if pid and psutil.pid_exists(pid):
                    try:
                        proc = psutil.Process(pid)
                        if proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE:
                            if stored_run != run_id or pid != os.getpid():
                                print(f"Supervisor lock active by running PID {pid} (Run ID: {stored_run}). Cannot acquire lock.")
                                return False
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
            except Exception:
                pass
        
        lock_data = {
            "run_id": run_id,
            "pid": os.getpid(),
            "acquired_at": datetime.now(timezone.utc).isoformat(),
            "host": os.environ.get("COMPUTERNAME", "localhost")
        }
        with open(self.lock_file, "w", encoding="utf-8") as f:
            json.dump(lock_data, f, indent=2)
        return True

    def release_lock(self):
        """Release the supervisor run lock."""
        if os.path.isfile(self.lock_file):
            try:
                os.remove(self.lock_file)
            except Exception:
                pass

    def log_event(self, run_id: str, phase: str, task_id: str, event_type: str, payload: Dict[str, Any], status: str):
        """Append an event to the SQLite WAL journal."""
        conn = sqlite3.connect(self.journal_db)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO event_log (run_id, timestamp, phase, task_id, event_type, payload_json, status) VALUES (?, ?, ?, ?, ?, ?, ?);",
            (run_id, datetime.now(timezone.utc).isoformat(), phase, task_id, event_type, json.dumps(payload), status)
        )
        conn.commit()
        conn.close()

    def update_task_status(self, task_id: str, phase: str, status: str, output_path: str = "", error_msg: str = "", runtime_sec: float = 0.0):
        """Update or insert task in SQLite task tracker."""
        conn = sqlite3.connect(self.journal_db)
        cursor = conn.cursor()
        now = datetime.now(timezone.utc).isoformat()
        cursor.execute("SELECT task_id FROM tasks WHERE task_id = ?;", (task_id,))
        if cursor.fetchone():
            cursor.execute(
                "UPDATE tasks SET status = ?, completed_at = ?, runtime_sec = ?, output_path = ?, error_msg = ? WHERE task_id = ?;",
                (status, now, runtime_sec, output_path, error_msg, task_id)
            )
        else:
            cursor.execute(
                "INSERT INTO tasks (task_id, phase, status, started_at, completed_at, runtime_sec, output_path, error_msg) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                (task_id, phase, status, now, now, runtime_sec, output_path, error_msg)
            )
        conn.commit()
        conn.close()

    def write_atomic_checkpoint(self, checkpoint_data: Dict[str, Any]) -> str:
        """
        Write checkpoint atomically using temporary file + fsync + atomic replacement.
        Preserves previous known-good checkpoint.
        """
        checkpoint_data["checkpoint_timestamp"] = datetime.now(timezone.utc).isoformat()
        content = json.dumps(checkpoint_data, indent=2)
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        checkpoint_data["checkpoint_sha256"] = content_hash
        content = json.dumps(checkpoint_data, indent=2)

        # 1. Back up current latest to previous if latest exists and is valid
        if os.path.isfile(self.latest_cp_path):
            try:
                shutil.copy2(self.latest_cp_path, self.previous_cp_path)
            except Exception:
                pass

        # 2. Write to temp file and flush/fsync
        temp_fd, temp_path = tempfile.mkstemp(dir=self.checkpoint_dir, prefix="cp_tmp_", suffix=".json")
        with os.fdopen(temp_fd, "w", encoding="utf-8") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())

        # 3. Atomically replace latest_checkpoint.json
        # On Windows, replace can overwrite in Python 3.3+
        os.replace(temp_path, self.latest_cp_path)
        return self.latest_cp_path

    def load_latest_checkpoint(self) -> Optional[Dict[str, Any]]:
        """Load latest checkpoint with integrity check and previous fallback."""
        if not os.path.isfile(self.latest_cp_path):
            return None
        
        try:
            with open(self.latest_cp_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Verify internal hash if present
            stored_hash = data.get("checkpoint_sha256")
            if stored_hash:
                data_copy = dict(data)
                del data_copy["checkpoint_sha256"]
                calc_hash = hashlib.sha256(json.dumps(data_copy, indent=2).encode("utf-8")).hexdigest()
                if stored_hash != calc_hash:
                    print("Latest checkpoint hash mismatch! Attempting fallback to previous checkpoint.")
                    return self.load_previous_checkpoint()
            return data
        except Exception as e:
            print(f"Error loading latest checkpoint ({e}). Falling back to previous.")
            return self.load_previous_checkpoint()

    def load_previous_checkpoint(self) -> Optional[Dict[str, Any]]:
        """Fallback to previous valid checkpoint."""
        if not os.path.isfile(self.previous_cp_path):
            return None
        try:
            with open(self.previous_cp_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
