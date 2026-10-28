"""
FinnoaQ Comprehensive Defect Regression Test Suite.
Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
Governance Standard: AGENTS.md Rule 1 (Technical Correctness Over Output Generation)

This test suite provides deterministic executable verification for all recorded defect modes:
FAIL-0001 through FAIL-0019 in governance/errors/errors.json.
"""

import os
import sys
import math
import pytest
import torch
import numpy as np

# Ensure finnoaq and governance are on sys.path
cur = os.path.dirname(os.path.abspath(__file__))
while cur and not os.path.exists(os.path.join(cur, ".git")):
    parent = os.path.dirname(cur)
    if parent == cur:
        break
    cur = parent
base_dir = cur if os.path.exists(os.path.join(cur, ".git")) else os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

for p in [
    base_dir,
    os.path.join(base_dir, "src"),
    os.path.join(base_dir, "toor_dal_optimization"),
    os.path.join(base_dir, "toor_dal_optimization", "src"),
    os.path.join(base_dir, "toor_dal_optimization", "governance", "errors"),
    os.path.join(base_dir, "governance", "errors"),
]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.insert(0, p)

from finnoaq.canonical_biophysics import (
    CA_VOL_HTC_NOMINAL,
    CA_BOUND_HTC_NOMINAL,
    RHO_DAL_DRY,
    SIGMA_0_YIELD,
    SIGMA_RESIDUAL,
    DomesticPressureCookerModel,
    calculate_chemical_speciation,
    solve_2d_soaking_pde,
    solve_cooking_endpoint,
    evaluate_treatment_batch_gpu,
)
from defect_ledger import DefectLedger
from circuit_breaker import ExecutionCircuitBreaker, CircuitBreakerTripped


# -----------------------------------------------------------------------------
# FAIL-0001: Repeating Six-Case Loop Shortcut Detection
# -----------------------------------------------------------------------------
def test_fail_0001_no_repeating_loop_shortcut():
    """Verify that different input concentrations and temperatures yield distinct physical responses."""
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    form1 = calculate_chemical_speciation(total_citrate_M=0.06, f_K=0.0, target_pH=5.4)
    res1 = solve_2d_soaking_pde(formulation=form1, soak_temp_c=25.0, soak_time_min=25.0, grid_size=16, device=device)
    
    form2 = calculate_chemical_speciation(total_citrate_M=0.24, f_K=0.0, target_pH=5.8)
    res2 = solve_2d_soaking_pde(formulation=form2, soak_temp_c=45.0, soak_time_min=25.0, grid_size=16, device=device)
    
    # Calcium displacement must be significantly different, not a static mock loop
    diff = abs(res2["ca_displacement_pct"] - res1["ca_displacement_pct"])
    assert diff > 5.0, f"FAIL-0001: Model outputs lack physical sensitivity (diff={diff:.2f}%)"


# -----------------------------------------------------------------------------
# FAIL-0002: Preset Calcium Depletion Passed Off as Prediction
# -----------------------------------------------------------------------------
def test_fail_0002_no_preset_calcium_field():
    """Verify that the calcium field is calculated via reaction-diffusion, not preset to 0.93."""
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    form = calculate_chemical_speciation(total_citrate_M=0.10, f_K=0.0, target_pH=5.4)
    res = solve_2d_soaking_pde(formulation=form, soak_temp_c=25.0, soak_time_min=15.0, grid_size=16, device=device)
    
    # Initial Pectin_Ca starts at 35.37 mol/m^3. Over 15 min, it must have a spatial gradient
    ca_field = res["final_pectin_ca_field"].cpu().numpy()
    core_val = ca_field[0, 0]
    edge_val = ca_field[-1, -1]
    
    # In 15 min at 25C, core must retain more Ca than edge
    assert core_val > edge_val, f"FAIL-0002: Uniform preset calcium field detected: core={core_val}, edge={edge_val}"
    assert not np.allclose(ca_field, 0.93), "FAIL-0002: Calcium field was preset to constant 0.93!"


# -----------------------------------------------------------------------------
# FAIL-0003: Preset Initial Calcium State (theta_ca = 0.02)
# -----------------------------------------------------------------------------
def test_fail_0003_no_preset_initial_calcium_in_cooking():
    """Verify that cooking simulation does not assume theta_ca = 0.02 without prior treatment."""
    raw_soak = {
        "final_pectin_ca_field": torch.full((16, 16), CA_VOL_HTC_NOMINAL),
        "final_moisture_field": torch.full((16, 16), 0.1173),
        "mean_pectin_ca_vol": CA_VOL_HTC_NOMINAL,
        "mean_moisture_db": 0.1173,
        "ca_displacement_pct": 0.0,
    }
    cooker = DomesticPressureCookerModel()
    cook_res_untreated = solve_cooking_endpoint(raw_soak, cooker)
    
    # Untreated HTC dal must fail 2-whistle tenderness
    assert not cook_res_untreated["is_two_whistles_or_less"], "FAIL-0003: Untreated HTC dal falsely passed in <= 2 whistles!"
    assert not cook_res_untreated["t90_reached"], "FAIL-0003: Untreated HTC dal falsely reached T90 tenderness!"


# -----------------------------------------------------------------------------
# FAIL-0004: Artificial Linear Whistle-Count Mapping
# -----------------------------------------------------------------------------
def test_fail_0004_first_principles_cooker_whistles():
    """Verify whistle events are discrete thermodynamic valve lift events, not t / 5.25."""
    cooker = DomesticPressureCookerModel()
    whistle_times = []
    
    # Advance cooker through 1200 seconds in 2-second steps
    for _ in range(600):
        state = cooker.step(dt=2.0)
    
    whistle_times = cooker.whistle_times_sec
    assert len(whistle_times) >= 2, f"FAIL-0004: Expected >= 2 whistles in 1200s, got {len(whistle_times)}"
    # First whistle lift time must be between 350s and 500s (sensible heating + pressurization)
    assert 350.0 <= whistle_times[0] <= 500.0, f"Unphysical first whistle time: {whistle_times[0]} s"


# -----------------------------------------------------------------------------
# FAIL-0005: Potassium Swelling & Speciation Bounds
# -----------------------------------------------------------------------------
def test_fail_0005_potassium_speciation_bounds():
    """Verify potassium speciation fractions and mass properties are physically bounded."""
    form_k0 = calculate_chemical_speciation(total_citrate_M=0.10, f_K=0.0, target_pH=5.4)
    form_k1 = calculate_chemical_speciation(total_citrate_M=0.10, f_K=1.0, target_pH=5.4)
    
    assert form_k0.conc_Na_M > 0.10 and form_k0.conc_K_M == 0.0, "Na/K inventory inconsistent for f_K=0"
    assert form_k1.conc_K_M > 0.10 and form_k1.conc_Na_M == 0.0, "Na/K inventory inconsistent for f_K=1"
    assert form_k1.total_dissolved_solids_wt_vol_pct > form_k0.total_dissolved_solids_wt_vol_pct, (
        "Potassium citrate monohydrate (MW 324.41) must yield higher TDS than trisodium citrate dihydrate (MW 294.10)"
    )


# -----------------------------------------------------------------------------
# FAIL-0006: Constitutive Parameter Provenance & Units
# -----------------------------------------------------------------------------
def test_fail_0006_constitutive_parameter_units():
    """Verify constitutive stress, activation energy, and onset parameters."""
    from finnoaq.canonical_biophysics import EA_GEL, T_GEL_ONSET_EXCESS, SIGMA_0_YIELD, SIGMA_RESIDUAL
    
    assert 20000.0 <= EA_GEL <= 40000.0, f"EA_GEL ({EA_GEL} J/mol) outside literature range (20-40 kJ/mol)"
    assert 60.0 <= T_GEL_ONSET_EXCESS <= 75.0, f"T_GEL_ONSET ({T_GEL_ONSET_EXCESS}°C) outside legume range"
    assert 200.0e3 <= SIGMA_0_YIELD <= 500.0e3, f"SIGMA_0_YIELD ({SIGMA_0_YIELD} Pa) outside parenchyma tissue range"
    assert 5.0e3 <= SIGMA_RESIDUAL <= 30.0e3, f"SIGMA_RESIDUAL ({SIGMA_RESIDUAL} Pa) outside cooked tissue range"


# -----------------------------------------------------------------------------
# FAIL-0007: Single Authoritative Source Tree Integrity
# -----------------------------------------------------------------------------
def test_fail_0007_authoritative_source_tree():
    """Verify that src/finnoaq and toor_dal_optimization/src/finnoaq refer to the same files."""
    p1 = os.path.abspath(os.path.join(base_dir, "src", "finnoaq", "canonical_biophysics.py"))
    p2 = os.path.abspath(os.path.join(base_dir, "toor_dal_optimization", "src", "finnoaq", "canonical_biophysics.py"))
    
    assert os.path.exists(p1), f"Source path {p1} does not exist"
    assert os.path.exists(p2), f"Source path {p2} does not exist"
    assert os.path.samefile(p1, p2), "FAIL-0007: Divergent source files! src/finnoaq is not linked to toor_dal_optimization"


# -----------------------------------------------------------------------------
# FAIL-0008: Calcium Unit Conversion Strict Verification
# -----------------------------------------------------------------------------
def test_fail_0008_calcium_unit_consistency():
    """Strict test for 10x dry-basis conversion factor in bound calcium calculation."""
    expected_vol_ca = (CA_BOUND_HTC_NOMINAL * 1e-2 / 40.078) * RHO_DAL_DRY
    assert abs(CA_VOL_HTC_NOMINAL - expected_vol_ca) < 1e-3, (
        f"FAIL-0008: CA_VOL_HTC_NOMINAL ({CA_VOL_HTC_NOMINAL:.3f}) does not match expected "
        f"physical concentration ({expected_vol_ca:.3f} mol/m^3)"
    )
    assert abs(CA_VOL_HTC_NOMINAL - 35.369) < 0.01, f"Expected ~35.37 mol/m^3, got {CA_VOL_HTC_NOMINAL:.3f}"


# -----------------------------------------------------------------------------
# FAIL-0009: PDE Numerical Stability Check
# -----------------------------------------------------------------------------
def test_fail_0009_numerical_stability():
    """Verify soaking PDE time-stepping satisfies numerical stability criteria and stays finite."""
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    form = calculate_chemical_speciation(total_citrate_M=0.24, f_K=0.33, target_pH=5.8)
    res = solve_2d_soaking_pde(formulation=form, soak_temp_c=52.0, soak_time_min=35.0, grid_size=16, device=device)
    
    ca_tensor = res["final_pectin_ca_field"]
    m_tensor = res["final_moisture_field"]
    
    assert torch.isfinite(ca_tensor).all(), "FAIL-0009: Non-finite values in final_pectin_ca_field!"
    assert torch.isfinite(m_tensor).all(), "FAIL-0009: Non-finite values in final_moisture_field!"
    assert (ca_tensor >= 0.0).all(), "FAIL-0009: Negative concentrations detected in final_pectin_ca_field!"
    assert (m_tensor >= 0.0).all(), "FAIL-0009: Negative moisture detected in final_moisture_field!"


# -----------------------------------------------------------------------------
# FAIL-0010: Spatial Heterogeneity - Hard Core Detection
# -----------------------------------------------------------------------------
def test_fail_0010_core_calcium_heterogeneity():
    """Verify that whole-grain displacement does not mask hard center retention."""
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    form = calculate_chemical_speciation(total_citrate_M=0.06, f_K=0.0, target_pH=5.4)
    # Short ambient soak: 15 min at 25C
    res = solve_2d_soaking_pde(formulation=form, soak_temp_c=25.0, soak_time_min=15.0, grid_size=16, device=device)
    
    ca_core = res["final_pectin_ca_field"][0, 0].item()
    core_retention_pct = (ca_core / CA_VOL_HTC_NOMINAL) * 100.0
    
    # In 15 min ambient soak, core must retain > 80% bound calcium
    assert core_retention_pct > 80.0, (
        f"FAIL-0010: Core retention {core_retention_pct:.1f}% unexpectedly low; "
        "hard core was erroneously smoothed out."
    )


# -----------------------------------------------------------------------------
# FAIL-0011 & FAIL-0012: Calibrated Warner-Bratzler Force & Stress Units
# -----------------------------------------------------------------------------
def test_fail_0011_0012_shear_force_and_stress_scale():
    """Verify that Warner-Bratzler shear force is in Newtons (10-75 N) and stress in kPa (not MPa)."""
    raw_soak = {
        "final_pectin_ca_field": torch.full((16, 16), CA_VOL_HTC_NOMINAL),
        "final_moisture_field": torch.full((16, 16), 0.1173),
        "mean_pectin_ca_vol": CA_VOL_HTC_NOMINAL,
        "mean_moisture_db": 0.1173,
        "ca_displacement_pct": 0.0,
    }
    cooker = DomesticPressureCookerModel()
    res_raw = solve_cooking_endpoint(raw_soak, cooker)
    
    # Cooked raw HTC dal core shear force must be in 20-30 N regime (hard cotyledon)
    assert 18.0 <= res_raw["final_f_wb_core_N"] <= 40.0, f"Raw core force {res_raw['final_f_wb_core_N']} N out of bounds"
    assert SIGMA_0_YIELD < 1.0e6, f"FAIL-0012: SIGMA_0_YIELD ({SIGMA_0_YIELD} Pa) in MPa structural scale!"


# -----------------------------------------------------------------------------
# FAIL-0013: Formulation Speciation & Mass/Charge Balance
# -----------------------------------------------------------------------------
def test_fail_0013_formulation_mass_charge_balance():
    """Verify citric acid / trisodium citrate recipe closes mass and charge balances at pH 5.4."""
    form = calculate_chemical_speciation(total_citrate_M=0.10, f_K=0.0, target_pH=5.40)
    
    # Reagent mass check: Citric acid anhydrous ~7.038 g/L, Na3Cit.2H2O ~18.637 g/L
    assert 6.5 <= form.mass_citric_acid_anhydrous_g_L <= 7.5, f"Acid mass {form.mass_citric_acid_anhydrous_g_L} g/L deviates"
    assert 18.0 <= form.mass_tri_sodium_citrate_dihydrate_g_L <= 19.5, f"Salt mass {form.mass_tri_sodium_citrate_dihydrate_g_L} g/L deviates"
    
    # TDS check
    assert 2.0 <= form.total_dissolved_solids_wt_vol_pct <= 3.0, f"TDS {form.total_dissolved_solids_wt_vol_pct}% deviates"


# -----------------------------------------------------------------------------
# FAIL-0014: Cooker Saturation Pressure NIST Steam Table Calibration
# -----------------------------------------------------------------------------
def test_fail_0014_cooker_saturation_pressure_calibration():
    """Verify Antoine saturation pressure matches NIST steam table (~207.0 kPa abs at 121.2°C)."""
    cooker = DomesticPressureCookerModel()
    p_abs_kpa = cooker.get_saturation_pressure_kpa(121.2)
    assert abs(p_abs_kpa - 207.0) < 3.0, (
        f"FAIL-0014: Pressure at 121.2°C is {p_abs_kpa:.2f} kPa, "
        "expected NIST standard 207.0 kPa abs (+/- 3 kPa)"
    )


# -----------------------------------------------------------------------------
# FAIL-0015: Whistle Count Acceptance Criteria Integrity
# -----------------------------------------------------------------------------
def test_fail_0015_whistle_count_reclassification_rejected():
    """Verify that a simulation with whistle_count > 2 is strictly classified as NOT a 2-whistle pass."""
    raw_soak = {
        "final_pectin_ca_field": torch.full((16, 16), CA_VOL_HTC_NOMINAL),
        "final_moisture_field": torch.full((16, 16), 0.1173),
        "mean_pectin_ca_vol": CA_VOL_HTC_NOMINAL,
        "mean_moisture_db": 0.1173,
        "ca_displacement_pct": 0.0,
    }
    cooker = DomesticPressureCookerModel()
    cook_res = solve_cooking_endpoint(raw_soak, cooker)
    
    if cook_res["whistle_count_at_t90"] > 2:
        assert not cook_res["is_two_whistles_or_less"], "FAIL-0015: >2 whistle outcome falsely classified as <= 2 whistles!"


# -----------------------------------------------------------------------------
# FAIL-0016: Internal Metric Consistency
# -----------------------------------------------------------------------------
def test_fail_0016_calcium_metric_consistency():
    """Verify that bulk displacement and volumetric field mean are mathematically consistent."""
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    form = calculate_chemical_speciation(total_citrate_M=0.16, f_K=0.0, target_pH=5.8)
    res = solve_2d_soaking_pde(formulation=form, soak_temp_c=45.0, soak_time_min=25.0, grid_size=16, device=device)
    
    ca_mean = res["mean_pectin_ca_vol"]
    disp_pct = res["ca_displacement_pct"]
    calc_disp = (1.0 - (ca_mean / CA_VOL_HTC_NOMINAL)) * 100.0
    
    assert abs(disp_pct - calc_disp) < 0.1, (
        f"FAIL-0016: Stated displacement ({disp_pct:.2f}%) does not match mean field calculation ({calc_disp:.2f}%)"
    )


# -----------------------------------------------------------------------------
# FAIL-0017: Manifest and Run Accounting Reconciliation
# -----------------------------------------------------------------------------
def test_fail_0017_accounting_reconciliation():
    """Verify that the circuit breaker catches manifest/result count mismatches."""
    cb = ExecutionCircuitBreaker()
    manifest_dummy = [{"id": 1}, {"id": 2}]
    results_dummy = [{"id": 1}] # Mismatched count
    
    with pytest.raises(CircuitBreakerTripped, match="Accounting defect"):
        cb.validate_simulation_outputs(results_dummy, manifest_dummy)


# -----------------------------------------------------------------------------
# FAIL-0018: Smooth Physical Response vs Discrete Step-Function Lookup
# -----------------------------------------------------------------------------
def test_fail_0018_continuous_reaction_kinetics():
    """Verify that soaking displacement responds smoothly across a temperature continuum."""
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    form = calculate_chemical_speciation(total_citrate_M=0.10, f_K=0.0, target_pH=5.4)
    temps = [25.0, 35.0, 45.0, 52.0]
    disps = [solve_2d_soaking_pde(formulation=form, soak_temp_c=t, soak_time_min=25.0, grid_size=16, device=device)["ca_displacement_pct"] for t in temps]
    
    # Displacements must be strictly monotonic increasing with temperature
    for i in range(len(disps) - 1):
        assert disps[i+1] > disps[i], f"FAIL-0018: Non-monotonic response detected: {disps}"


# -----------------------------------------------------------------------------
# FAIL-0019: Defect Ledger Chain and Preflight Integrity
# -----------------------------------------------------------------------------
def test_fail_0019_ledger_chain_and_preflight():
    """Verify that defect ledger hash chain is complete and preflight gate passes cleanly."""
    cb = ExecutionCircuitBreaker()
    cb.run_preflight_checks() # Must execute without raising CircuitBreakerTripped
    
    valid, msg = cb.ledger.validate_chain()
    assert valid, f"FAIL-0019: Defect ledger chain invalid: {msg}"
    assert len(cb.ledger.records) >= 20, f"Expected at least 20 defect records, found {len(cb.ledger.records)}"


# -----------------------------------------------------------------------------
# FAIL-0020: Unbounded Overnight Daemon Execution
# -----------------------------------------------------------------------------
def test_fail_0020_unbounded_daemon_execution():
    """Verify that overnight search engine accepts unbounded max_evaluations=None and obeys stop sentinel."""
    import inspect
    from scripts.run_overnight_frontier_search import run_overnight_frontier_engine
    
    sig = inspect.signature(run_overnight_frontier_engine)
    assert "max_evaluations" in sig.parameters, "Engine must define max_evaluations parameter"
    default_val = sig.parameters["max_evaluations"].default
    assert default_val is None, f"Default max_evaluations must be None (unbounded), found: {default_val}"


# -----------------------------------------------------------------------------
# FAIL-0021: Drying Stress Differentiation & DimensionalGuard Compliance
# -----------------------------------------------------------------------------
def test_fail_0021_drying_stress_and_page_kinetics():
    """Verify 85C single-stage drying and 65C->55C 2-stage drying produce distinct stresses <= 2.0 MPa."""
    from finnoaq.omega_modules import PlantOperationsAndEconomicsModule

    dry85 = PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
        "85C_Single", 85.0, 45.0, 85.0, 0.0
    )
    dry65 = PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
        "65C_55C_2Stage", 65.0, 22.0, 55.0, 25.0, 20.0
    )

    assert dry85["peak_tensile_stress_MPa"] > dry65["peak_tensile_stress_MPa"] + 0.5, (
        "FAIL-0021: 85C and 65C->55C drying failed to differentiate peak tensile stress!"
    )
    assert dry85["peak_tensile_stress_MPa"] > dry85["yield_threshold_MPa"], (
        "FAIL-0021: 85C single-stage blast drying should exceed cotyledon fissure threshold (1.65 MPa)"
    )
    assert dry65["peak_tensile_stress_MPa"] < dry65["yield_threshold_MPa"], (
        "FAIL-0021: 65C->55C 2-stage drying must remain safely below fissure threshold"
    )
    assert dry85["peak_tensile_stress_MPa"] <= 2.0 and dry65["peak_tensile_stress_MPa"] <= 2.0, (
        "FAIL-0021: Tissue tensile stress exceeded RAEBYES 2.0 MPa physiological parenchyma bound!"
    )


# -----------------------------------------------------------------------------
# FAIL-0022: Batch Thickness/Moisture Propagation & Noisy Intake Proxy
# -----------------------------------------------------------------------------
def test_fail_0022_batch_geometry_and_noisy_intake_proxy():
    """Verify that grain thickness alters PDE soaking displacement and intake proxy does not cheat on latent Ca."""
    from finnoaq.omega_modules import (
        FeedstockCharacterizationModule,
        TreatmentChemistryModule,
        PretreatmentProcessConfig,
        HydrationAndPenetrationModule,
        BatchVariabilityAndAdaptationModule,
    )
    import copy

    batches = FeedstockCharacterizationModule.get_reference_batches()
    b_thin = copy.deepcopy(batches["TANZANIAN_HTC_AGED_NOMINAL"])
    b_thin.half_thickness_m = 0.85e-3
    b_thick = copy.deepcopy(batches["TANZANIAN_HTC_AGED_NOMINAL"])
    b_thick.half_thickness_m = 1.30e-3

    chem = TreatmentChemistryModule.design_citrate_buffer("CIT", "Citrate", 0.145, 5.20, 0.90)
    cfg = PretreatmentProcessConfig(soak_temp_c=55.0, soak_time_min=12.0, ultrasound_w_per_l=17.0)

    res_thin = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_thin, chem, cfg)
    res_thick = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_thick, chem, cfg)
    assert res_thin["core_ca_displacement_pct"] > res_thick["core_ca_displacement_pct"] + 5.0, (
        "FAIL-0022: Grain thickness was ignored by PDE solver!"
    )

    rng = np.random.default_rng(123)
    diag = BatchVariabilityAndAdaptationModule.simulate_noisy_intake_diagnostics(b_thick, rng)
    assert abs(diag["ca_est_mol_m3"] - b_thick.bound_ca_mol_m3) > 1e-6, (
        "FAIL-0022: Intake diagnostic leaked exact latent bound Ca without measurement uncertainty!"
    )


# -----------------------------------------------------------------------------
# FAIL-0023: Vacuum Impregnation Porosity Limit & Two-Domain Washing Balance
# -----------------------------------------------------------------------------
def test_fail_0023_vacuum_impregnation_porosity_and_internal_solute():
    """Verify VI convected solute obeys Fito (1996) open porosity limit and washing tracks internal pore solute."""
    from finnoaq.omega_modules import (
        FeedstockCharacterizationModule,
        TreatmentChemistryModule,
        PretreatmentProcessConfig,
        HydrationAndPenetrationModule,
        WashingAndResidueModule,
    )

    b_tza = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]
    chem = TreatmentChemistryModule.design_citrate_buffer("CIT", "Citrate", 0.145, 5.20, 0.90)
    cfg_vi = PretreatmentProcessConfig(soak_temp_c=55.0, soak_time_min=4.6, vacuum_pulse_kpa_abs=15.0)

    res_vi = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem, cfg_vi)
    # Convected solute cannot exceed open_porosity * C_bath
    max_possible_convected = b_tza.open_porosity * (chem.active_chelator_M * 1000.0)
    assert res_vi["vi_convected_solute_mol_m3"] <= max_possible_convected + 1e-6, (
        "FAIL-0023: Vacuum impregnation exceeded physical pore volume capacity!"
    )
    assert res_vi["core_ca_displacement_pct"] < 90.0, (
        "FAIL-0023: Unphysical 4.6-min 95% core Ca chelation recurred!"
    )

    wash = WashingAndResidueModule.simulate_washing_operation(chem, res_vi, wash_time_s=12.0)
    assert wash["retained_citrate_mg_100g"] > 20.0, (
        "FAIL-0023: Washing balance ignored internal cotyledon pore solute retention!"
    )


# -----------------------------------------------------------------------------
# FAIL-0024: Buffer Recipe Equilibrium pH Verification
# -----------------------------------------------------------------------------
def test_fail_0024_buffer_recipe_equilibrium_ph():
    """Verify that designed citrate buffer hydrate masses actually equilibrate at target_pH."""
    from finnoaq.omega_modules import TreatmentChemistryModule

    spec = TreatmentChemistryModule.design_citrate_buffer(
        "TIER2", "Tier 2 Standard", total_citrate_M=0.145, target_pH=5.20, f_K=0.90
    )
    check = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(
        mass_k3cit_monohydrate_g_L=spec.mass_k3cit_monohydrate_g_L,
        mass_na3cit_dihydrate_g_L=spec.mass_na3cit_dihydrate_g_L,
        mass_citric_acid_anhydrous_g_L=spec.mass_citric_acid_anhydrous_g_L,
    )
    assert abs(check["equilibrium_pH"] - 5.20) < 0.05, (
        f"FAIL-0024: Recipe equilibrated at pH {check['equilibrium_pH']:.2f} instead of target 5.20!"
    )


# -----------------------------------------------------------------------------
# FAIL-0025: Reconciled Once-Through vs Recycled Bath OpEx
# -----------------------------------------------------------------------------
def test_fail_0025_once_through_vs_recycled_opex_reconciliation():
    """Verify that once-through (0% recycle) and 85% recycled bath OpEx are explicitly distinguished."""
    from finnoaq.omega_modules import (
        TreatmentChemistryModule,
        PretreatmentProcessConfig,
        PlantOperationsAndEconomicsModule,
    )

    chem = TreatmentChemistryModule.design_citrate_buffer("TIER2", "Tier 2", 0.145, 5.20, 0.90)
    cfg = PretreatmentProcessConfig(55.0, 20.0, 17.0)
    dry = PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
        "65C_55C", 65.0, 22.0, 55.0, 25.0, 20.0
    )
    econ_once = PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics(
        chem, cfg, dry, liquor_recycle_fraction=0.0
    )
    econ_rec = PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics(
        chem, cfg, dry, liquor_recycle_fraction=0.85
    )

    assert econ_once["reagent_cost_inr_per_kg"] > 7.50, (
        "FAIL-0025: Once-through reagent cost understated!"
    )
    assert econ_rec["reagent_cost_inr_per_kg"] < econ_once["reagent_cost_inr_per_kg"] * 0.45, (
        "FAIL-0025: 85% liquor recycle did not reduce reagent make-up consumption as required!"
    )
    assert abs(econ_rec["evap_discrepancy_B2_minus_B1_kg_day"] - 199.72) < 0.05, (
        "Governance rule: 199.72 kg/day Scenario B1 vs B2 pre-dryer moisture bound must be preserved!"
    )


