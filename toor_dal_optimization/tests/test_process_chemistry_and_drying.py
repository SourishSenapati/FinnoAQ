"""
Unit tests for FinnoaQ Sequential Process Chemistry Engine & Pulse Fluid-Bed Drying Model.
Governing Standard: FinnoaQ Omega Persistent Autonomous R&D Constitution.
"""

import pytest
from src.finnoaq.process_chemistry import SequentialProcessChemistryEngine
from src.finnoaq.drying_model import PulseFluidBedDryingModel
from src.finnoaq.gpu_continuous_engine import ContinuousGPUEngine


def test_stage_a_ambient_soaking_calcium_displacement():
    engine = SequentialProcessChemistryEngine(num_nodes=15)
    
    # 1. Raw water soak (0.0% NaHCO3)
    res_water = engine.simulate_stage_a_soaking(solution_conc_w_w=0.0, soak_time_minutes=30.0)
    assert res_water["calcium_displacement_pct"] == 0.0
    assert res_water["mean_theta_solubility"] == 0.10
    assert res_water["dal_dry_solids_leach_pct"] < 1.0

    # 2. Treated soak (0.50% NaHCO3)
    res_treated = engine.simulate_stage_a_soaking(solution_conc_w_w=0.50, soak_time_minutes=30.0)
    assert res_treated["calcium_displacement_pct"] > 60.0
    assert res_treated["mean_theta_solubility"] > 0.65
    assert res_treated["dal_dry_solids_leach_pct"] < 2.0


def test_stage_b_rinsing_and_drainage():
    engine = SequentialProcessChemistryEngine(num_nodes=15)
    stage_a = engine.simulate_stage_a_soaking(solution_conc_w_w=0.50, soak_time_minutes=30.0)
    stage_b = engine.simulate_stage_b_rinsing_and_drainage(stage_a, rinse_water_ratio=0.50)

    assert stage_b["retained_na_mg_100g_post_rinse"] < stage_a["retained_na_mg_100g_pre_rinse"]
    assert stage_b["retained_na_mg_100g_post_rinse"] <= 100.0
    assert stage_b["total_pre_cook_loss_pct"] < 3.0


def test_stage_c_cooking_response_raw_vs_treated():
    engine = SequentialProcessChemistryEngine(num_nodes=15)
    
    # Raw untreated
    raw_res = engine.execute_complete_treatment_pathway(solution_conc_w_w=0.0)
    assert raw_res["stage_c_cooking"]["cooking_time_minutes"] > 45.0
    assert raw_res["stage_c_cooking"]["pressure_cooker_whistles"] > 10.0

    # 0.50% Treated
    treated_res = engine.execute_complete_treatment_pathway(solution_conc_w_w=0.50)
    assert treated_res["stage_c_cooking"]["cooking_time_minutes"] <= 15.0
    assert treated_res["stage_c_cooking"]["dal_dry_solids_recovery_pct"] >= 95.5
    assert treated_res["stage_c_cooking"]["retained_na_mg_100g"] <= 100.0


def test_fluid_bed_drying_model():
    dm = PulseFluidBedDryingModel()
    res = dm.simulate_drying_process(
        incoming_grain_mass_kg=15000.0,
        initial_moisture_wb=0.52,
        target_moisture_wb=0.105,
        stage1_air_temp_c=65.0,
        stage2_air_temp_c=52.0
    )

    assert res["final_state"]["shelf_stable"] is True
    assert res["final_state"]["moisture_wb_pct"] == 10.5
    assert res["stability_and_quality"]["premature_gelatinization_detected"] is False
    assert "NEGLIGIBLE" in res["stability_and_quality"]["retrogradation_re_hardening_risk"]
    assert res["stability_and_quality"]["case_hardening_status"] == "ACCEPTABLE_UNIFORM"
    assert 2.5 <= res["thermal_and_energy"]["specific_energy_consumption_mj_kg_water"] <= 4.5


def test_gpu_continuous_engine_batch():
    gpu = ContinuousGPUEngine()
    res = gpu.execute_simulation_batch(batch_size=1000, solution_conc_w_w=0.50)
    assert res["mean_cooking_time_min"] <= 15.0
    assert res["dal_dry_solids_recovery_pct"] >= 95.5
    assert res["retained_na_mg_100g"] <= 100.0
    assert res["fraction_under_15min"] == 100.0
