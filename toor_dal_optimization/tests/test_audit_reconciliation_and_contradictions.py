"""
FinnoaQ Toor Dal — Automated Regression & Audit Reconciliation Tests.
Verifies compliance with the Critical Scientific Audit Directive.
Guards against numerical contradictions, unverified claims, and premature stage unlocking.
"""

import os
import csv
import math
import pytest
import numpy as np
import scipy.stats as stats

try:
    import torch
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

from src.finnoaq.dose_calculator import DoseCalculator
from src.finnoaq.mass_balance import MassBalanceEngine
from src.finnoaq.high_res_spatial_solver import HighResSpatialSolver


def test_8192_grid_memory_and_stencil_requirements():
    """
    Guards against the discredited claim that an 8192x8192 float32 grid requires 64 MB.
    Verifies that a single full float32 grid of 8192x8192 elements strictly requires 256 MiB.
    """
    N = 8192
    bytes_per_field = N * N * 4  # float32 = 4 bytes
    mebibytes = bytes_per_field / (1024 * 1024)
    assert mebibytes == 256.0, f"Single float32 grid must be exactly 256 MiB, got {mebibytes}"

    solver = HighResSpatialSolver()
    if HAS_TORCH and torch.cuda.is_available():
        res = solver.benchmark_real_2d_pde_stencil(N=8192, steps=2)
        assert res["status"] == "COMPLETED_REAL_PDE_BENCHMARK"
        # Stencil state buffers (T, M, T_new) must strictly exceed 1,000 MB
        assert res["peak_vram_mb"] >= 1000.0, f"Real 8192x8192 PDE stencil must allocate >= 1000 MB, got {res['peak_vram_mb']} MB"


def test_solids_recovery_and_basis_separation():
    """
    Reconciles the three recovery figures (98.54% vs 96.80% vs 95.65%)
    and asserts strict basis separation.
    """
    calc = DoseCalculator()
    
    # Tier 1: Nominal process leaching loss = 1.46% -> Recovery = 98.54%
    f_nom = calc.calculate_formulation_point(
        solution_conc_w_w_pct=0.50,
        liquor_to_grain_ratio=1.5,
        dal_dry_solids_loss_pct=1.46
    )
    rec_nom = f_nom["recovery_and_yield"]["dal_dry_solids_recovery_pct"]
    assert abs(rec_nom - 98.54) < 0.01

    # Tier 2: Conservative screening default = 3.20% -> Recovery = 96.80%
    f_cons = calc.calculate_formulation_point(
        solution_conc_w_w_pct=0.50,
        liquor_to_grain_ratio=1.5,
        dal_dry_solids_loss_pct=3.20
    )
    rec_cons = f_cons["recovery_and_yield"]["dal_dry_solids_recovery_pct"]
    assert abs(rec_cons - 96.80) < 0.01

    # Tier 3: Whole-plant mass balance with mechanical attrition (4.35% loss -> 95.65% recovery)
    mb = MassBalanceEngine(incoming_feed_kg=15000.0)
    bal = mb.solve_complete_mass_balance(
        leaching_loss_solids_pct=2.10,
        rinsing_loss_solids_pct=0.45,
        disintegration_loss_solids_pct=0.65,
        conveying_attrition_solids_pct=0.35,
        drying_cracking_solids_pct=0.40,
        cyclone_fines_solids_pct=0.25,
        rejection_allowance_solids_pct=0.15
    )
    rec_plant = bal["dal_dry_solids_balance"]["dal_dry_solids_recovery_pct"]
    assert abs(rec_plant - 95.65) < 0.01

    # All tiers must exceed the Stage 1 threshold of 95.50%
    assert rec_nom >= 95.50
    assert rec_cons >= 95.50
    assert rec_plant >= 95.50


def test_retained_sodium_chemical_vs_elemental_separation():
    """
    Verifies that retained chemical (NaHCO3) and elemental sodium (Na)
    are strictly separated with proper molecular weight conversion.
    """
    calc = DoseCalculator()
    res = calc.calculate_formulation_point(
        solution_conc_w_w_pct=0.50,
        liquor_to_grain_ratio=1.5,
        absorption_fraction_of_liquor=0.35,
        rinsing_washout_fraction=0.25
    )

    ret = res["retention_and_carryover"]
    retained_chem_mg_100g = ret["retained_additive_mg_per_100g"]
    retained_na_mg_100g = ret["retained_sodium_mg_per_100g"]

    # Molecular weight ratio check: Na (22.990) / NaHCO3 (84.007) = 0.273667
    expected_na = retained_chem_mg_100g * (22.990 / 84.007)
    assert abs(retained_na_mg_100g - expected_na) < 0.05
    assert abs(retained_na_mg_100g - 53.88) < 0.1

    # Must comply with FSSAI low-sodium (< 120 mg/100g) and statutory (< 350 mg/100g)
    assert retained_na_mg_100g < 120.0
    assert retained_na_mg_100g < 350.0


def test_evidence_status_taxonomy_and_prohibition_of_premature_confirmation():
    """
    Guards against assigning EXPERIMENTALLY_CONFIRMED status before
    physical target-lot wet-lab certificates exist.
    """
    csv_path = "reports/TREATMENT_CANDIDATE_RANKING.csv"
    assert os.path.isfile(csv_path), "Treatment ranking CSV must exist"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        candidates = list(reader)

    assert len(candidates) >= 10
    valid_statuses = {
        "UNVERIFIED_IMPLEMENTATION",
        "COMPUTATIONAL_HYPOTHESIS",
        "COMPUTATIONALLY_VERIFIED",
        "INDEPENDENTLY_MODEL_VALIDATED",
        "EXPERIMENTALLY_CONFIRMED"
    }

    for c in candidates:
        cid = c["candidate_id"]
        status = c["evidence_status"]
        assert status in valid_statuses, f"Candidate {cid} has invalid status {status}"
        # STRICT RULE: No candidate may be marked EXPERIMENTALLY_CONFIRMED yet
        assert status != "EXPERIMENTALLY_CONFIRMED", (
            f"Candidate {cid} illegally marked EXPERIMENTALLY_CONFIRMED without physical wet-lab data!"
        )

    # Winning candidate CAND-004 must be marked COMPUTATIONAL_HYPOTHESIS
    cand_004 = next(c for c in candidates if c["candidate_id"] == "CAND-004")
    assert cand_004["evidence_status"] == "COMPUTATIONAL_HYPOTHESIS"


def test_statistical_power_and_retraction_of_automatic_five_sigma():
    """
    Guards against the unscientific claim that 4 batches automatically guarantees 5-sigma.
    Proves that for n=4 with Delta_mu = 8.2 min, significance is conditional on variance s.
    """
    delta_mu = 8.2  # Pressure cooker effect size: 22.0 min control - 13.8 min treated
    n = 4
    df = 2 * n - 2  # 6 degrees of freedom

    # If s = 1.0 min:
    s_realistic = 1.0
    se_realistic = np.sqrt(s_realistic**2 / n + s_realistic**2 / n)
    t_realistic = delta_mu / se_realistic
    p_realistic = 1.0 - stats.t.cdf(t_realistic, df=df)
    sigma_realistic = stats.norm.ppf(1.0 - p_realistic)

    # Significance must be sub-5-sigma for realistic kitchen variance
    assert sigma_realistic < 5.0, f"Expected sub-5-sigma for s=1.0 min, got {sigma_realistic:.2f}"
    assert sigma_realistic >= 3.0, "Must still satisfy regulatory 3-sigma gate"

    # Only when variance is tightly controlled to s <= 0.50 min (30 s) is 5-sigma reached
    s_tight = 0.50
    se_tight = np.sqrt(s_tight**2 / n + s_tight**2 / n)
    t_tight = delta_mu / se_tight
    p_tight = 1.0 - stats.t.cdf(t_tight, df=df)
    sigma_tight = stats.norm.ppf(1.0 - p_tight)
    assert sigma_tight >= 5.0, f"Expected >= 5.0 sigma for s=0.50 min, got {sigma_tight:.2f}"


def test_dryer_moisture_contradiction_reconciliation():
    """
    Independently verifies and reconciles the critical drying moisture contradiction:
    1. 15,000 kg/day feed dal at 10.5% moisture contains exactly 13,425 kg/day dry solids.
    2. At 95.65% net whole-plant recovery, saleable dry solids = 12,841.01 kg/day.
       At 10.0% final moisture, saleable product = 14,267.79 kg/day.
    3. Traces historical contradiction: 13,241.0 kg solids + 1,654.3 kg water = 14,895.3 kg dal,
       which has moisture 1,654.3 / 14,895.3 = 11.106% wb, NOT 10.00%.
    4. Proves that at true 10.00% exit moisture, 13,241.0 kg dry solids gives:
       Total exit mass = 13,241.0 / 0.90 = 14,712.22 kg/day.
       Water in exit dal = 1,471.22 kg/day.
       Daily evaporation from 5,349.0 kg water = 5,349.0 - 1,471.22 = 3,877.78 kg H2O/day.
       Nominal 16h rate = 242.36 kg/h; Design 85% OEE rate (13.6h) = 285.13 kg/h.
    """
    feed_dal_kg = 15000.0
    feed_moisture_wb = 0.105
    feed_dry_solids = feed_dal_kg * (1.0 - feed_moisture_wb)
    assert feed_dry_solids == 13425.0

    # Whole-plant 95.65% recovery
    net_recovery = 0.9565
    saleable_solids = feed_dry_solids * net_recovery
    assert abs(saleable_solids - 12841.01) < 0.05

    target_moisture_wb = 0.100
    saleable_total_dal = saleable_solids / (1.0 - target_moisture_wb)
    assert abs(saleable_total_dal - 14267.79) < 0.05
    saleable_water = saleable_total_dal * target_moisture_wb
    assert abs(saleable_water - 1426.78) < 0.05

    # Forensic audit of reported flawed stream
    reported_solids = 13241.0
    reported_water = 1654.30
    reported_total = reported_solids + reported_water  # 14,895.30 kg
    actual_reported_moisture = reported_water / reported_total
    # Assert that the reported stream was in reality 11.11% moisture, NOT 10.0%
    assert abs(actual_reported_moisture - 0.11106) < 1e-4
    assert actual_reported_moisture != pytest.approx(0.100, abs=1e-3)

    # Reconciled true 10.00% wet-basis stream
    true_dryer_exit_total = reported_solids / (1.0 - target_moisture_wb)
    assert abs(true_dryer_exit_total - 14712.22) < 0.05
    true_dryer_exit_water = true_dryer_exit_total * target_moisture_wb
    assert abs(true_dryer_exit_water - 1471.22) < 0.05

    # True evaporation
    wet_dal_water_entering = 5349.0
    true_daily_evaporation = wet_dal_water_entering - true_dryer_exit_water
    assert abs(true_daily_evaporation - 3877.78) < 0.05

    # Hourly rates
    nominal_16h_evap_rate = true_daily_evaporation / 16.0
    assert abs(nominal_16h_evap_rate - 242.36) < 0.05
    design_13_6h_evap_rate = true_daily_evaporation / (16.0 * 0.85)
    assert abs(design_13_6h_evap_rate - 285.13) < 0.05

