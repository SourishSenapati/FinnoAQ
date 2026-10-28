"""
Unit tests for DAL-OPT CLI tools (Directive Section 15)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pytest
from finnoaq.dalopt import (
    run_doctor,
    run_sources,
    run_batch_register,
    run_data_validate,
    run_plan_doe,
    run_simulate,
    run_analyze,
    run_scale,
)

def test_dalopt_doctor():
    res = run_doctor()
    assert res["status"] == "PASS"
    assert res["cuda_available"] is True
    assert "RTX 4050" in res["cuda_device"]

def test_dalopt_sources_search():
    res = run_sources("search", "citrate")
    assert res["action"] == "search"
    assert "results" in res

def test_dalopt_batch_register():
    res = run_batch_register("BATCH-TEST-001", "Maruti", 0.105, 1.05)
    assert res["status"] == "REGISTERED"
    assert "fingerprint_sha256" in res
    assert res["initial_moisture_wb"] == 0.105

def test_dalopt_data_validate():
    res = run_data_validate()
    assert res["status"] == "ALL_CONSTRAINTS_SATISFIED"

def test_dalopt_plan_doe():
    res = run_plan_doe(runs=8, seed=123)
    assert len(res["runs"]) == 8
    assert res["seed"] == 123

def test_dalopt_simulate():
    res_hyd = run_simulate("hydration", 24.0)
    assert res_hyd["moisture_wb"] > 0.105
    res_cook = run_simulate("cooking", 7.0)
    assert res_cook["shear_force_n"] < 29.58
    res_pc = run_simulate("pressure-cycle")
    assert res_pc["thermal_severity_f0"] > 12.0

def test_dalopt_analyze():
    res_tex = run_analyze("texture")
    assert res_tex["pass"] is True
    res_sen = run_analyze("sensory")
    assert res_sen["r_off_index"] == 0.164
    assert res_sen["classification"] == "PREDICTED_MINIMUM"

def test_dalopt_scale():
    res = run_scale(15000.0)
    assert res["recycle_85_opex_inr_kg"] == 6.34
    assert res["annual_savings_inr"] > 50000000.0

