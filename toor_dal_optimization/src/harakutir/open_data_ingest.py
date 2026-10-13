"""
Harakutir Open Data Ingestion & Normalization Engine.
Adheres to Harakutir Omega v4 Section 5.
Ingests published literature datasets and official standards with strict unit normalization and data quality checks.
"""

import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from src.harakutir.schemas import DatasetKind


class OpenDataIngestionEngine:
    """
    Ingests and normalizes public food science datasets and regulatory standards.
    Guarantees strict separation between published literature and target lot observations.
    """

    def __init__(self, data_root: Optional[str] = None):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.data_root = data_root or os.path.join(base_dir, "data")
        self.lit_dir = os.path.join(self.data_root, "literature")

    def load_malawi_genotypes_dataset(self) -> Dict[str, Any]:
        """Loads and validates the 6-genotype Malawi pigeon pea dataset (Machinjili et al. 2025)."""
        file_path = os.path.join(self.lit_dir, "malawi_pigeonpea_genotypes_2025.json")
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Malawi literature dataset missing at {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Validate metadata
        meta = data.get("dataset_metadata", {})
        if meta.get("dataset_kind") != DatasetKind.PUBLISHED_LITERATURE.value:
            raise ValueError(f"Invalid dataset_kind {meta.get('dataset_kind')}; must be published_literature")

        genotypes = data.get("genotypes", [])
        if len(genotypes) != 6:
            raise ValueError(f"Expected 6 genotypes, found {len(genotypes)}")

        # Normalization and sanity checks
        normalized = []
        for g in genotypes:
            w_cook = float(g["whole_seed_cooking_time_min"])
            d_cook = float(g["dehulled_cotyledon_cooking_time_min"])
            if not (10.0 <= d_cook <= 120.0):
                raise ValueError(f"Suspicious dehulled cooking time {d_cook} min for {g['genotype_name']}")
            if not (50.0 <= w_cook <= 300.0):
                raise ValueError(f"Suspicious whole seed cooking time {w_cook} min for {g['genotype_name']}")

            entry = {
                "genotype_name": g["genotype_name"],
                "origin": g["origin"],
                "whole_seed_cooking_min": w_cook,
                "dehulled_cotyledon_cooking_min": d_cook,
                "dehulled_cooking_seconds": round(d_cook * 60.0, 1),
                "dehulling_reduction_pct": g["dehulling_reduction_pct"],
                "seed_coat_thickness_um": g["seed_coat_thickness_um"],
                "moisture_pct_dry_basis": g["moisture_pct_dry_basis"],
                "protein_pct": g["crude_protein_pct"],
                "dataset_kind": DatasetKind.PUBLISHED_LITERATURE.value
            }
            normalized.append(entry)

        return {
            "source_id": meta.get("source_id"),
            "species": meta.get("species"),
            "dataset_kind": DatasetKind.PUBLISHED_LITERATURE.value,
            "normalized_records": normalized,
            "ingest_timestamp": datetime.now(timezone.utc).isoformat()
        }

    def load_fssai_standards(self) -> Dict[str, Any]:
        """Loads and validates official FSSAI pulses regulatory standards."""
        file_path = os.path.join(self.lit_dir, "fssai_pulse_standards.json")
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"FSSAI pulse standards missing at {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        standards = data.get("standards", {})
        # Verify mandatory limits exist
        assert "moisture_max_pct" in standards
        assert standards["moisture_max_pct"]["limit"] == 14.0
        assert "total_aflatoxins_b1_b2_g1_g2_max_ppb" in standards
        assert standards["total_aflatoxins_b1_b2_g1_g2_max_ppb"]["limit"] == 15.0

        return {
            "regulatory_framework": data.get("regulatory_framework"),
            "dataset_kind": DatasetKind.OFFICIAL_STATISTICS.value,
            "standards": standards,
            "ingest_timestamp": datetime.now(timezone.utc).isoformat()
        }

    def load_peleg_literature_benchmarks(self) -> List[Dict[str, Any]]:
        """Loads Peleg kinetics literature benchmarks for comparison."""
        file_path = os.path.join(self.lit_dir, "peleg_pulse_kinetics_literature.json")
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Peleg kinetics literature missing at {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data.get("literature_constants", [])
