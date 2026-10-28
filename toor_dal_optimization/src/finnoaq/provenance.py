"""
Data provenance registry and cryptographic hash verifier.
Guarantees source traceability for every assay record and deliverable.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Dict, Any, Optional

def compute_sha256(filepath: str) -> str:
    """Compute SHA-256 hash of a file."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
    return sha256.hexdigest().upper()

class ProvenanceRegistry:
    def __init__(self, registry_file: str = "state/provenance_registry.json"):
        self.registry_file = registry_file
        self.records: Dict[str, Any] = {}
        self.load()

    def load(self):
        if os.path.isfile(self.registry_file):
            try:
                with open(self.registry_file, "r", encoding="utf-8") as f:
                    self.records = json.load(f)
            except Exception:
                self.records = {}
        else:
            self.records = {}

    def save(self):
        os.makedirs(os.path.dirname(self.registry_file), exist_ok=True)
        with open(self.registry_file, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=2)

    def register_file(self, filepath: str, category: str, notes: Optional[str] = None) -> Dict[str, Any]:
        h = compute_sha256(filepath)
        size = os.path.getsize(filepath)
        norm_path = os.path.normpath(filepath).replace("\\", "/")
        rec = {
            "filepath": norm_path,
            "filename": os.path.basename(filepath),
            "sha256": h,
            "size_bytes": size,
            "category": category,
            "registered_at": datetime.now(timezone.utc).isoformat(),
            "notes": notes or ""
        }
        self.records[norm_path] = rec
        self.save()
        return rec

    def verify_file(self, filepath: str) -> bool:
        norm_path = os.path.normpath(filepath).replace("\\", "/")
        if norm_path not in self.records:
            return False
        current_hash = compute_sha256(filepath)
        return current_hash == self.records[norm_path]["sha256"]
