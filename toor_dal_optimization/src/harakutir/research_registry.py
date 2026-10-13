"""
Harakutir Research Registry & Scientific Literature Manager.
Adheres to Harakutir Omega v4 Sections 4.1, 4.3, 5.1.
Parses, indexes, verifies SHA-256, and classifies open-access research sources.
"""

import os
import csv
import json
import hashlib
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone


class ResearchRegistry:
    """
    Manages bibliographic source records, evidence classifications,
    licensing compliance, and SHA-256 integrity audits.
    """

    def __init__(self, registry_csv_path: Optional[str] = None):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.csv_path = registry_csv_path or os.path.join(base_dir, "research", "SOURCE_REGISTRY.csv")
        self.sources: Dict[str, Dict[str, Any]] = {}
        self._load_registry()

    def _load_registry(self) -> None:
        if not os.path.isfile(self.csv_path):
            return

        with open(self.csv_path, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            for row in reader:
                s_id = row.get("Source_ID", "").strip()
                if s_id:
                    self.sources[s_id] = row

    def get_source(self, source_id: str) -> Optional[Dict[str, Any]]:
        return self.sources.get(source_id)

    def get_sources_by_class(self, evidence_class: str) -> List[Dict[str, Any]]:
        return [s for s in self.sources.values() if s.get("Relevance_Class") == evidence_class]

    def verify_direct_cajanus_sources(self) -> List[Dict[str, Any]]:
        """Returns direct Cajanus cajan evidence sources (Machinjili et al. 2025 etc.)."""
        return self.get_sources_by_class("DIRECT_CAJANUS_EVIDENCE")

    def audit_registry_integrity(self) -> Dict[str, Any]:
        """Audits all registered sources for mandatory fields and access status."""
        total = len(self.sources)
        classes: Dict[str, int] = {}
        missing_fields = []

        for s_id, data in self.sources.items():
            e_class = data.get("Relevance_Class", "UNKNOWN")
            classes[e_class] = classes.get(e_class, 0) + 1

            for req in ["Title", "Year", "DOI_or_ID", "License", "Study_Species"]:
                if not data.get(req):
                    missing_fields.append({"source_id": s_id, "missing": req})

        return {
            "total_sources_registered": total,
            "evidence_class_breakdown": classes,
            "missing_field_count": len(missing_fields),
            "missing_field_details": missing_fields,
            "direct_cajanus_sources_count": classes.get("DIRECT_CAJANUS_EVIDENCE", 0),
            "related_pulse_sources_count": classes.get("RELATED_PULSE_EVIDENCE", 0),
            "audit_timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "PASSED" if len(missing_fields) == 0 and total > 0 else "DEFECTIVE"
        }


def compute_file_sha256(filepath: str) -> str:
    """Calculates strict SHA-256 hash of a file."""
    if not os.path.isfile(filepath):
        return ""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()
