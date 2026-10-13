"""
Synthetic test fixtures generator.
STRICTLY isolated under data/synthetic/.
Watermarked with dataset_kind=synthetic_test_only.
Used solely for testing computational code, GPU models, recovery, and statistics.
"""

import json
import os
from typing import List, Dict, Any
from src.harakutir.schemas import DatasetKind, ProvenanceRecord

def generate_synthetic_fixtures(out_dir: str = "data/synthetic") -> str:
    """Generate isolated synthetic fixtures for pipeline testing."""
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "synthetic_test_fixtures_only.json").replace("\\", "/")
    
    prov = {
        "source_file": "synthetic_generator",
        "record_pointer": "code_fixture",
        "source_hash": "N/A_SYNTHETIC",
        "analyst_or_device": "synthetic_test_fixture_generator",
        "raw_units": "standard_si",
        "normalized_units": "standard_si",
        "transformation_applied": "synthetic_generation_for_testing_only"
    }
    
    # 2 synthetic Tanzanian lots and 2 synthetic Indian lots for software verification
    samples = [
        {
            "sample_id": "SYN_TZ_01",
            "sample_type": "Tanzanian",
            "lot_number": "SYN_TZ_LOT_101",
            "origin_country": "Tanzania",
            "quantity_received_kg": 3.0,
            "retention_quantity_kg": 0.5,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "provenance": prov
        },
        {
            "sample_id": "SYN_TZ_02",
            "sample_type": "Tanzanian",
            "lot_number": "SYN_TZ_LOT_102",
            "origin_country": "Tanzania",
            "quantity_received_kg": 3.0,
            "retention_quantity_kg": 0.5,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "provenance": prov
        },
        {
            "sample_id": "SYN_IND_01",
            "sample_type": "Indian Benchmark",
            "lot_number": "SYN_IND_LOT_201",
            "origin_country": "India",
            "quantity_received_kg": 3.0,
            "retention_quantity_kg": 0.5,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "provenance": prov
        },
        {
            "sample_id": "SYN_IND_02",
            "sample_type": "Indian Benchmark",
            "lot_number": "SYN_IND_LOT_202",
            "origin_country": "India",
            "quantity_received_kg": 3.0,
            "retention_quantity_kg": 0.5,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "provenance": prov
        }
    ]
    
    # Synthetic physical assays
    physical = [
        {
            "sample_id": "SYN_TZ_01",
            "lot_number": "SYN_TZ_LOT_101",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "length_mm": 5.42,
            "width_mm": 4.88,
            "thickness_mm": 3.25,
            "length_width_ratio": 1.11,
            "cielab_l": 62.4,
            "cielab_a": 4.2,
            "cielab_b": 28.5,
            "thousand_grain_weight_g": 92.5,
            "bulk_density_g_ml": 0.81,
            "true_density_g_ml": 1.34,
            "broken_grain_pct": 2.1,
            "defects_pct": 1.5,
            "residual_seed_coat_pct": 1.2,
            "raw_hardness_n": 142.0,
            "provenance": prov
        },
        {
            "sample_id": "SYN_IND_01",
            "lot_number": "SYN_IND_LOT_201",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "length_mm": 5.15,
            "width_mm": 4.65,
            "thickness_mm": 3.10,
            "length_width_ratio": 1.11,
            "cielab_l": 68.1,
            "cielab_a": 3.8,
            "cielab_b": 32.1,
            "thousand_grain_weight_g": 85.0,
            "bulk_density_g_ml": 0.83,
            "true_density_g_ml": 1.36,
            "broken_grain_pct": 1.8,
            "defects_pct": 0.9,
            "residual_seed_coat_pct": 0.4,
            "raw_hardness_n": 128.0,
            "provenance": prov
        }
    ]

    # Synthetic proximate assays
    proximate = [
        {
            "sample_id": "SYN_TZ_01",
            "lot_number": "SYN_TZ_LOT_101",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "moisture_pct": 10.4,
            "protein_pct": 21.8,
            "fat_pct": 1.6,
            "crude_fibre_pct": 3.9,
            "ash_pct": 3.8,
            "total_carbohydrate_pct": 58.5,
            "total_starch_pct": 52.1,
            "analytical_method_standard": "SYNTHETIC_TEST_FIXTURE",
            "provenance": prov
        },
        {
            "sample_id": "SYN_IND_01",
            "lot_number": "SYN_IND_LOT_201",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "moisture_pct": 10.1,
            "protein_pct": 22.4,
            "fat_pct": 1.5,
            "crude_fibre_pct": 3.6,
            "ash_pct": 3.7,
            "total_carbohydrate_pct": 58.7,
            "total_starch_pct": 53.4,
            "analytical_method_standard": "SYNTHETIC_TEST_FIXTURE",
            "provenance": prov
        }
    ]

    # Synthetic hydration curves (0 to 480 min) with Peleg synthetic kinetic profile
    # Peleg formula: M(t) = M0 + t / (k1 + k2*t)
    # TZ synthetic: slower uptake (k1=3.8 min/%, k2=0.009 %^-1)
    # IND synthetic: faster uptake (k1=1.5 min/%, k2=0.008 %^-1)
    times = [0, 15, 30, 60, 120, 240, 480]
    
    def peleg_curve(m0, k1, k2):
        pts = []
        for t in times:
            if t == 0:
                m = m0
            else:
                m = m0 + t / (k1 + k2 * t)
            uptake = (m - m0) / 100.0
            pts.append({
                "time_min": float(t),
                "water_uptake_g_per_g": round(uptake, 4),
                "moisture_pct_dry_basis": round(m, 2),
                "mass_gain_pct": round(uptake * 100.0, 2),
                "swelling_capacity_ml_grain": round(0.04 + uptake * 0.05, 3)
            })
        return pts

    hydration = [
        {
            "sample_id": "SYN_TZ_01",
            "lot_number": "SYN_TZ_LOT_101",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "soaking_temperature_c": 25.0,
            "wai_g_per_g": 2.45,
            "time_points": peleg_curve(11.5, 3.8, 0.009),
            "provenance": prov
        },
        {
            "sample_id": "SYN_IND_01",
            "lot_number": "SYN_IND_LOT_201",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "soaking_temperature_c": 25.0,
            "wai_g_per_g": 2.85,
            "time_points": peleg_curve(11.2, 1.5, 0.008),
            "provenance": prov
        }
    ]

    # Synthetic cooking trials
    cooking = [
        {
            "sample_id": "SYN_TZ_01",
            "lot_number": "SYN_TZ_LOT_101",
            "trial_id": "COOK_TZ_01",
            "test_type": "Test C: Controlled Pressure",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "sample_mass_g": 50.0,
            "water_to_dal_ratio": 4.0,
            "operating_pressure_kpa": 103.0,
            "cooking_temperature_c": 121.0,
            "cooking_endpoint_time_min": 68.0,
            "observed_whistles": 6,
            "hard_core_pct": 2.0,
            "cooking_loss_pct": 14.2,
            "cooked_water_absorption_ratio": 2.15,
            "cooked_grain_swelling_ratio": 2.20,
            "final_cooked_moisture_pct": 65.4,
            "provenance": prov
        },
        {
            "sample_id": "SYN_IND_01",
            "lot_number": "SYN_IND_LOT_201",
            "trial_id": "COOK_IND_01",
            "test_type": "Test C: Controlled Pressure",
            "replicate_id": 1,
            "dataset_kind": DatasetKind.SYNTHETIC_TEST_ONLY.value,
            "watermark": "SYNTHETIC_TEST_ONLY_DO_NOT_USE_IN_REAL_REPORTS",
            "sample_mass_g": 50.0,
            "water_to_dal_ratio": 4.0,
            "operating_pressure_kpa": 103.0,
            "cooking_temperature_c": 121.0,
            "cooking_endpoint_time_min": 34.0,
            "observed_whistles": 3,
            "hard_core_pct": 0.0,
            "cooking_loss_pct": 16.5,
            "cooked_water_absorption_ratio": 2.45,
            "cooked_grain_swelling_ratio": 2.50,
            "final_cooked_moisture_pct": 69.8,
            "provenance": prov
        }
    ]

    payload = {
        "metadata": {
            "dataset_kind": "synthetic_test_only",
            "notice": "THIS IS ISOLATED SYNTHETIC DATA FOR UNIT TESTING AND ARCHITECTURE VERIFICATION ONLY. NEVER USE IN REAL SCIENTIFIC REPORTS.",
            "generated_at": "2026-10-13T19:00:00Z"
        },
        "samples": samples,
        "physical_assays": physical,
        "proximate_assays": proximate,
        "hydration_assays": hydration,
        "cooking_trials": cooking
    }

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return out_file

def assert_no_synthetic_leakage(records: List[Dict[str, Any]], context_name: str = "Real Report Dataset"):
    """
    Automated gate assertion.
    Fails immediately if any record with dataset_kind='synthetic_test_only'
    attempts to enter real analytical reports or real-data namespace.
    """
    for idx, rec in enumerate(records):
        kind = rec.get("dataset_kind")
        if kind == DatasetKind.SYNTHETIC_TEST_ONLY.value or kind == "synthetic_test_only":
            raise ValueError(
                f"CRITICAL DATA INTEGRITY VIOLATION: Synthetic test record detected in {context_name}! "
                f"Record index {idx}: {rec.get('sample_id', 'Unknown')}. "
                f"Synthetic records are strictly forbidden from entering real analysis!"
            )
        watermark = rec.get("watermark", "")
        if "SYNTHETIC" in watermark.upper():
            raise ValueError(
                f"CRITICAL DATA INTEGRITY VIOLATION: Synthetic watermark found in {context_name}! "
                f"Record index {idx}: {rec.get('sample_id', 'Unknown')}."
            )
    return True
