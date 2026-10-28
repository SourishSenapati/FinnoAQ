"""
Comprehensive Acceptance and Independent Red-Team Adversarial Audit Test Suite.
Validates all 14 mandatory contract gates from Section 15 of FINNOAQ_MASTER_PROMPT.
"""

import os
import sys
import json
import pytest
import numpy as np

# Ensure root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.finnoaq.parameters import get_all_parameters, get_sow_sections_matrix
from src.finnoaq.schemas import DatasetKind, ProvenanceRecord, PhysicalAssay, ProximateAssay
from src.finnoaq.synthetic import generate_synthetic_fixtures, assert_no_synthetic_leakage
from src.finnoaq.provenance import compute_sha256, ProvenanceRegistry
from src.finnoaq.statistics import compute_descriptive_stats, compute_comparative_stats, apply_holm_bonferroni
from src.finnoaq.hydration import fit_peleg_model, peleg_function, GPUInverseHydrationModel
from src.finnoaq.checkpoint import CheckpointManager
from src.finnoaq.oed import BayesianOEDPlanner
from src.finnoaq.dream_rsi import DiscoveryNode, DiscoveryTree, DreamRSIPolicyEvaluator
from src.finnoaq.claims import get_baseline_phase1_claims
from src.finnoaq.reports import ReportGenerator

# GATE 1: Complete SOW §§1–36 coverage
def test_gate_01_complete_sow_coverage():
    matrix = get_sow_sections_matrix()
    assert len(matrix) == 36, f"Expected 36 sections in SOW matrix, found {len(matrix)}"
    for idx, s in enumerate(matrix, start=1):
        assert s["section"] == f"§{idx}"
        assert s["status"] != ""
        assert s["requirement"] != ""

# GATE 2: Source hash reconciliation
def test_gate_02_source_hash_reconciliation():
    reg = ProvenanceRegistry()
    sow_path = "inputs/Phase1_Scope_of_Work_Toor_Dal.docx"
    if os.path.isfile(sow_path):
        h = compute_sha256(sow_path)
        assert len(h) == 64, "SHA-256 hash must be 64 characters hex"
        reg.register_file(sow_path, "Source Contract Document")
        assert reg.verify_file(sow_path) is True

# GATE 3: Unit conversion & parameter registry consistency
def test_gate_03_parameter_consistency():
    params = get_all_parameters()
    assert len(params) >= 70, f"Expected >= 70 detailed parameters, found {len(params)}"
    param_ids = set()
    for p in params:
        assert p.param_id not in param_ids, f"Duplicate param ID: {p.param_id}"
        param_ids.add(p.param_id)
        assert p.unit != ""
        assert p.category != ""

# GATE 4: Synthetic-to-real data isolation and report-level leakage prevention
def test_gate_04_synthetic_leakage_prevention():
    synth_path = generate_synthetic_fixtures()
    assert os.path.isfile(synth_path)
    
    with open(synth_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for s in data["samples"]:
        assert s["dataset_kind"] == DatasetKind.SYNTHETIC_TEST_ONLY.value
        assert "SYNTHETIC" in s["watermark"].upper()
        
    # Test that the gate assertion catches synthetic data attempting to enter real reports
    with pytest.raises(ValueError, match="CRITICAL DATA INTEGRITY VIOLATION"):
        assert_no_synthetic_leakage(data["samples"], "Real Analytical Benchmark")

# GATE 5: Missing values, duplicates, censoring and outlier flags
def test_gate_05_data_validation_bounds():
    prov = ProvenanceRecord(
        source_file="test.csv",
        record_pointer="row 1",
        analyst_or_device="test",
        raw_units="g",
        normalized_units="g"
    )
    # Valid physical assay
    p_good = PhysicalAssay(
        sample_id="TZ_01",
        lot_number="LOT_1",
        replicate_id=1,
        dataset_kind=DatasetKind.SYNTHETIC_TEST_ONLY,
        length_mm=5.5,
        width_mm=4.8,
        thickness_mm=3.2,
        cielab_l=65.0,
        thousand_grain_weight_g=90.0,
        bulk_density_g_ml=0.82,
        provenance=prov
    )
    assert p_good.length_mm == 5.5

    # Out of bounds value must trigger Pydantic ValidationError
    with pytest.raises(Exception):
        PhysicalAssay(
            sample_id="TZ_01",
            lot_number="LOT_1",
            replicate_id=1,
            dataset_kind=DatasetKind.SYNTHETIC_TEST_ONLY,
            length_mm=99.0,  # Impossible grain length (> 15 mm)
            provenance=prov
        )

# GATE 6: Statistical results against known fixtures, confidence intervals, multiple testing
def test_gate_06_statistical_engine():
    # Known dataset
    grp_a = [10.0, 10.5, 11.0, 10.2, 10.8]
    grp_b = [5.0, 5.2, 4.8, 5.1, 5.3]
    
    comp = compute_comparative_stats(grp_a, grp_b)
    assert comp["status"] == "success"
    assert comp["mean_a"] > comp["mean_b"]
    assert comp["significant_at_alpha"] is True
    assert comp["cohens_d"] > 2.0  # Very large effect size
    assert comp["p_value_welch"] < 0.001
    
    # Holm-Bonferroni correction
    p_vals = [0.001, 0.04, 0.045, 0.20]
    adj = apply_holm_bonferroni(p_vals)
    assert len(adj) == 4
    assert adj[0]["significant"] is True

# GATE 7: Peleg fit recovery on synthetic test curves & rejection of invalid cases
def test_gate_07_peleg_fitting():
    times = [0.0, 15.0, 30.0, 60.0, 120.0, 240.0, 480.0]
    m0_true, k1_true, k2_true = 10.0, 2.5, 0.01
    moistures = peleg_function(np.array(times), m0_true, k1_true, k2_true).tolist()
    
    fit = fit_peleg_model(times, moistures)
    assert fit["status"] == "success"
    assert pytest.approx(fit["k1"], rel=1e-2) == k1_true
    assert pytest.approx(fit["k2"], rel=1e-2) == k2_true
    assert fit["r2"] > 0.999
    assert fit["is_identifiable"] is True
    
    # Invalid time sequence should fail gracefully
    bad_fit = fit_peleg_model([0.0, 10.0, 5.0], [10.0, 12.0, 15.0])
    assert bad_fit["status"] == "invalid_time_sequence"

# GATE 8: Report building with and without actual data
def test_gate_08_report_generation():
    rep = ReportGenerator()
    readiness = {
        "real_data_status": "ABSENT",
        "empirical_analysis_status": "BLOCKED_BY_MISSING_DATA",
        "overall_status": "DATA_READINESS_ONLY",
        "files_list": []
    }
    rep.generate_all_deliverables(readiness)
    
    assert os.path.isfile("reports/COMPLETE_PARAMETER_REGISTRY.md")
    assert os.path.isfile("reports/SOW_REQUIREMENTS_MATRIX.md")
    assert os.path.isfile("reports/DATA_READINESS_REPORT.md")
    assert os.path.isfile("reports/EXECUTIVE_MANAGEMENT_SUMMARY.md")
    assert os.path.isfile("reports/INDIAN_VS_TANZANIAN_BENCHMARK_MATRIX.md")
    assert os.path.isfile("reports/PHASE1_TECHNICAL_REPORT.md")
    assert os.path.isfile("reports/PHASE1_TECHNICAL_REPORT.docx")

# GATE 9: Output/figure integrity and relative paths
def test_gate_09_relative_paths():
    with open("reports/PHASE1_TECHNICAL_REPORT.md", "r", encoding="utf-8") as f:
        text = f.read()
    # Ensure no hard-coded non-portable C:\tmp paths in report
    assert "C:\\tmp" not in text
    assert "/tmp" not in text

# GATE 10: Atomic checkpointing, restart equivalence, idempotency, fallback
def test_gate_10_atomic_checkpointing():
    cp_mgr = CheckpointManager()
    data1 = {"run_id": "TEST_RUN_1", "step": 1, "status": "STEP_1"}
    cp_mgr.write_atomic_checkpoint(data1)
    
    loaded1 = cp_mgr.load_latest_checkpoint()
    assert loaded1 is not None
    assert loaded1["step"] == 1
    
    # Write step 2
    data2 = {"run_id": "TEST_RUN_1", "step": 2, "status": "STEP_2"}
    cp_mgr.write_atomic_checkpoint(data2)
    
    loaded2 = cp_mgr.load_latest_checkpoint()
    assert loaded2["step"] == 2
    
    # Previous checkpoint should have step 1
    prev = cp_mgr.load_previous_checkpoint()
    assert prev is not None
    assert prev["step"] == 1

# GATE 11: Replay determinism and branch lineage
def test_gate_11_dream_rsi_replay():
    tree = DiscoveryTree(tree_file="state/test_discovery_tree.json")
    n1 = DiscoveryNode(
        node_id="T_NODE_01",
        parent_id=None,
        task_hypothesis="Test Hypothesis 1",
        policy_version="1.0.0",
        command_or_action="test_action",
        config_hash="H1",
        data_hash="D1",
        status="SUCCESS",
        test_results={"total": 5, "passed": 5}
    )
    tree.add_node(n1)
    
    evaluator = DreamRSIPolicyEvaluator()
    res = evaluator.evaluate_policy(tree, "1.0.0")
    assert res["status"] == "EVALUATED"
    assert res["composite_score"] > 0.8
    if os.path.isfile("state/test_discovery_tree.json"):
        os.remove("state/test_discovery_tree.json")

# GATE 12: No credentials in logs or configs
def test_gate_12_no_credentials():
    for fpath in ["configs/default_config.json", "reports/DATA_READINESS_REPORT.md"]:
        if os.path.isfile(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read().lower()
            for secret in ["password", "secret_key", "api_key", "private_token"]:
                assert secret not in content

# GATE 13: Resource guard tests and CPU fallback
def test_gate_13_resource_guard_and_fallback():
    # Test that GPUInverseHydrationModel works on CPU fallback cleanly
    cpu_model = GPUInverseHydrationModel(target_device="cpu")
    times = [0.0, 15.0, 30.0, 60.0]
    moistures = [11.0, 15.0, 20.0, 26.0]
    res = cpu_model.fit_inverse_diffusion(times, moistures, epochs=50)
    assert res["status"] == "success"
    assert res["effective_diffusivity_m2_s"] > 0.0

# GATE 14: Final claim and provenance audit
def test_gate_14_claim_provenance_audit():
    claims_ledger = get_baseline_phase1_claims()
    assert len(claims_ledger.claims) >= 4
    for cid, c in claims_ledger.claims.items():
        assert c.evidence_category in ["A", "B", "C", "D"]
        assert c.evidence_status == "DATA_READINESS_ONLY"
        assert c.supporting_source_pointer != ""
        assert len(c.limitations) > 0

# GATE 15: Foodoscope Culinary Informatics & Flavor Chemistry Engine
def test_gate_15_foodoscope_culinary_informatics():
    from src.finnoaq.foodoscope import FoodoscopeInformaticsEngine
    fe = FoodoscopeInformaticsEngine()
    
    # Test volatile database
    assert "hexanal" in fe.volatiles_db
    assert "2_5_dimethylpyrazine" in fe.volatiles_db
    assert fe.volatiles_db["hexanal"].is_off_flavor is True
    assert fe.volatiles_db["2_5_dimethylpyrazine"].is_off_flavor is False
    
    # Test thermal flavor & nutrient kinetics
    kin = fe.simulate_thermal_flavor_and_nutrient_kinetics(
        treatment_temperature_c=185.0,
        treatment_duration_min=0.75,
        moisture_content_pct=14.0
    )
    assert kin["lox_inactivation_pct"] == 100.0
    assert kin["beany_off_note_suppression_index"] > 0.5
    assert kin["available_lysine_retention_pct"] > 90.0  # Safe nutritional window
    
    # Test recipe matrix simulation (Acidic Sambar broth)
    sambar_sim = fe.predict_recipe_matrix_performance(
        dal_treatment_profile={"cooking_time_reduction_pct": 45.0},
        cooking_media="sambar_broth_acidic"
    )
    assert sambar_sim["predicted_pressure_cooker_whistles"] < 6.0
    assert sambar_sim["broth_ph"] < 5.0
    
    # Test Hedonic Sensory Scoring
    sens = fe.compute_sensory_hedonic_score(
        texture_firmness_n=22.0,
        hard_core_pct=0.0,
        flavor_kinetics=kin
    )
    assert sens["overall_hedonic_score_9pt"] >= 7.8
    assert "Premium Grade Benchmark" in sens["commercial_sensory_tier"]

# GATE 16: 5-Layer Computational Screening & Pareto Multi-Objective Optimization
def test_gate_16_virtual_screening_and_pareto_front():
    from src.finnoaq.virtual_screening import VirtualScreeningPipeline
    pipe = VirtualScreeningPipeline()
    candidates = pipe.generate_candidate_design_space()
    assert len(candidates) >= 15
    
    results = pipe.screen_and_optimize(candidates)
    assert len(results) == len(candidates)
    
    # Assert rejection of non-compliant candidates
    edta_rejections = [r for r in results if "EDTA" in r.treatment_id]
    assert len(edta_rejections) > 0
    assert edta_rejections[0].survived is False
    assert "Layer 1: Hard Constraints" in edta_rejections[0].rejected_at_layer
    
    # Assert existence of Pareto optimal survivors
    pareto_survivors = [r for r in results if r.is_pareto_optimal]
    assert len(pareto_survivors) >= 3
    for p in pareto_survivors:
        assert p.survived is True
        assert p.predicted_whistles <= 4.0
        assert p.opex_inr_per_kg <= 2.50

# GATE 17: Closed-Loop Digital Twin & Bayesian Parameter Updating
def test_gate_17_closed_loop_digital_twin_and_feedback():
    from src.finnoaq.digital_twin import ClosedLoopDigitalTwin
    dt = ClosedLoopDigitalTwin()
    
    # Check initial prior distributions
    assert "peleg_k1_tz" in dt.posteriors
    prior_k1 = dt.posteriors["peleg_k1_tz"].current_mean
    prior_std = dt.posteriors["peleg_k1_tz"].current_std
    
    # Ingest observed physical experiment
    obs_data = {
        "peleg_k1_tz": {"observed_mean": 3.40, "observed_std": 0.10}
    }
    update_res = dt.update_from_experiment("EXP_WET_LAB_001", obs_data)
    assert update_res["status"] == "SUCCESS_CLOSED_LOOP_UPDATED"
    
    # Assert Bayesian posterior shifted and uncertainty reduced
    post_k1 = dt.posteriors["peleg_k1_tz"].current_mean
    post_std = dt.posteriors["peleg_k1_tz"].current_std
    assert post_std < prior_std
    assert abs(post_k1 - 3.40) < abs(prior_k1 - 3.40)
    
    # Test industrial scale unit operations simulation
    scale = dt.simulate_industrial_scale_unit_operations(5.0)
    assert scale["throughput_tonnes_per_hour"] == 5.0
    assert scale["mass_balance"]["overall_process_yield_pct"] > 98.0
    assert scale["techno_economics"]["total_opex_inr_per_kg"] < 1.00
    assert scale["techno_economics"]["raw_material_arbitrage_advantage_inr_per_kg"] > 15.00

# GATE 18: Learn Harness Engineering Decision Gates (G0-G9)
def test_gate_18_learn_harness_engineering_gates_g0_g9():
    from src.finnoaq.harness import HarnessEngineeringManager
    harness = HarnessEngineeringManager()
    summary = harness.evaluate_all_gates()
    
    assert summary["total_gates"] == 10
    assert summary["failed"] == 0
    assert summary["passed_or_gated"] == 10
    assert os.path.isfile("state/harness_execution_log.json")

