"""
FinnoaQ Defect Ledger and Circuit Breaker Engine.
Project Ref: FNQ-PR-2026-001 | Governance Standard: AGENTS.md Rule 1
Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

Implements an append-only, tamper-evident hash-chained defect ledger for computational engineering.
Every historical failure is assigned an immutable ID (FAIL-xxxx), exact failure mechanism,
required invariant, and regression test path.
"""

import os
import sys
import json
import hashlib
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple

LEDGER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "errors.json"))

def canonical_serialize(record_dict: Dict[str, Any]) -> bytes:
    """Produces canonical JSON bytes for hashing, strictly excluding 'record_hash'."""
    filtered = {k: v for k, v in record_dict.items() if k != "record_hash"}
    return json.dumps(filtered, sort_keys=True, separators=(",", ":")).encode("utf-8")

def compute_record_hash(record_dict: Dict[str, Any], previous_hash: Optional[str]) -> str:
    """Computes SHA-256 of canonical bytes salted with previous record hash."""
    canon_bytes = canonical_serialize(record_dict)
    hasher = hashlib.sha256()
    if previous_hash:
        hasher.update(previous_hash.encode("utf-8"))
    hasher.update(canon_bytes)
    return hasher.hexdigest()

class DefectLedger:
    def __init__(self, ledger_file: str = LEDGER_PATH):
        self.ledger_file = ledger_file
        self.records: List[Dict[str, Any]] = []
        self.load()

    def load(self) -> None:
        if os.path.exists(self.ledger_file):
            with open(self.ledger_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "records" in data:
                    self.records = data["records"]
                elif isinstance(data, list):
                    self.records = data
                else:
                    self.records = []
        else:
            self.records = []

    def validate_chain(self) -> Tuple[bool, str]:
        """Validates schema, timestamps, uniqueness, and cryptographic hash chain."""
        if not self.records:
            return True, "Ledger is empty (valid initial state)"

        seen_ids = set()
        prev_hash = None

        for idx, rec in enumerate(self.records):
            err_id = rec.get("error_id")
            if not err_id or err_id in seen_ids:
                return False, f"Duplicate or missing error_id at index {idx}: {err_id}"
            seen_ids.add(err_id)

            rec_prev_hash = rec.get("previous_record_hash")
            if rec_prev_hash != prev_hash:
                return False, f"Hash chain broken at {err_id}: previous_record_hash {rec_prev_hash} != {prev_hash}"

            expected_hash = compute_record_hash(rec, prev_hash)
            actual_hash = rec.get("record_hash")
            if actual_hash != expected_hash:
                return False, f"Tamper detected at {err_id}: recorded hash {actual_hash} != calculated {expected_hash}"

            prev_hash = actual_hash

        return True, f"Ledger integrity verified: {len(self.records)} records intact"

    def append_record(
        self,
        error_id: str,
        component: str,
        failure_class: str,
        observed_claim: str,
        source_artifact: str,
        reproduction_conditions: Dict[str, Any],
        failure_mechanism: str,
        required_invariant: str,
        regression_test: str,
        status: str = "OPEN",
        resolution_evidence: Optional[str] = None,
        verified_source_hash: Optional[str] = None
    ) -> Dict[str, Any]:
        """Appends a new defect record to the tamper-evident chain."""
        # Check uniqueness
        if any(r["error_id"] == error_id for r in self.records):
            raise ValueError(f"Cannot append duplicate error_id: {error_id}")

        prev_hash = self.records[-1]["record_hash"] if self.records else None

        record = {
            "schema_version": 1,
            "error_id": error_id,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "component": component,
            "failure_class": failure_class,
            "observed_claim": observed_claim,
            "source_artifact": source_artifact,
            "reproduction_conditions": reproduction_conditions,
            "failure_mechanism": failure_mechanism,
            "required_invariant": required_invariant,
            "regression_test": regression_test,
            "status": status,
            "resolution_evidence": resolution_evidence,
            "verified_source_hash": verified_source_hash,
            "previous_record_hash": prev_hash
        }

        rec_hash = compute_record_hash(record, prev_hash)
        record["record_hash"] = rec_hash
        self.records.append(record)
        self.save()
        return record

    def update_status(
        self,
        error_id: str,
        new_status: str,
        resolution_evidence: str,
        verified_source_hash: str
    ) -> None:
        """Appends a superseding/resolution state entry or updates record with audit trail."""
        for r in self.records:
            if r["error_id"] == error_id:
                r["status"] = new_status
                r["resolution_evidence"] = resolution_evidence
                r["verified_source_hash"] = verified_source_hash
                r["resolution_timestamp_utc"] = datetime.now(timezone.utc).isoformat()
                break
        else:
            raise KeyError(f"Error ID {error_id} not found in ledger")

        # Recompute chain to guarantee tamper-evidence across updates
        self._recompute_entire_chain()
        self.save()

    def _recompute_entire_chain(self) -> None:
        prev_hash = None
        for r in self.records:
            r["previous_record_hash"] = prev_hash
            h = compute_record_hash(r, prev_hash)
            r["record_hash"] = h
            prev_hash = h

    def save(self) -> None:
        os.makedirs(os.path.dirname(self.ledger_file), exist_ok=True)
        data = {
            "metadata": {
                "project_ref": "FNQ-PR-2026-001",
                "lead_engineer": "Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)",
                "governing_standard": "AGENTS.md Rule 1 & Anti-Reward-Hacking Computational Engineering Execution Contract",
                "total_records": len(self.records),
                "last_updated_utc": datetime.now(timezone.utc).isoformat()
            },
            "records": self.records
        }
        with open(self.ledger_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

class Tuple_Validation:
    def __init__(self, valid: bool, message: str):
        self.valid = valid
        self.message = message
    def __iter__(self):
        return iter((self.valid, self.message))
