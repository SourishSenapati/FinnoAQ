"""
FINNOAQ OMEGA — Comprehensive Hierarchical Model & Verification Test Suite
==========================================================================
Project Ref: FNQ-PR-2026-001
Lead Chemical and Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

Verifies:
  1. Offline Evidence Vault integrity, provenance hashes, and retrieval index
  2. Modules A through H physical conservation, unit consistency, and boundary limits
  3. Numerical PDE grid convergence (12x12 vs 24x24)
  4. Sobol / Saltelli Global Sensitivity Analysis against analytical benchmark
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parent.parent
if ROOT.name == "toor_dal_optimization":
    ROOT = ROOT.parent

for p in [
    str(ROOT),
    str(ROOT / "src"),
    str(ROOT / "evidence_vault" / "index"),
    str(ROOT / "governance" / "errors"),
]:
    if p not in sys.path:
        sys.path.insert(0, p)

from finnoaq.omega_modules import (
    BatchVariabilityAndAdaptationModule,
    FeedstockCharacterizationModule,
    GlobalSensitivityAnalyzer,
    HydrationAndPenetrationModule,
    PlantOperationsAndEconomicsModule,
    PretreatmentProcessConfig,
    SensoryAndFlavourModule,
    ThermalAndPressureCookingModule,
    TreatmentChemistryModule,
    WashingAndResidueModule,
)
from offline_retrieval_index import OfflineEvidenceIndex


def test_evidence_vault_integrity_and_retrieval():
    """Verify offline Evidence Vault loads without network access and enforces direct vs indirect tagging."""
    idx = OfflineEvidenceIndex(ROOT / "evidence_vault")
    assert len(idx.sources) >= 20
    assert len(idx.parameters) >= 25
    assert idx.provenance["network_independent_execution_ready"] is True

    # Vásquez et al. (2021) studied whole seeds -> must be tagged INDIRECT
    vasquez = idx.search_sources(keyword="10.1016/j.lwt.2021.111191")
    assert len(vasquez) == 1
    assert vasquez[0]["applicability_to_split_toor_dal"].startswith("INDIRECT")

    # Machinjili et al. (2025) studied East African dehulled split genotypes -> DIRECT
    machinjili = idx.search_sources(keyword="10.3389/fsufs.2025.1613117")
    assert len(machinjili) == 1
    assert machinjili[0]["applicability_to_split_toor_dal"].startswith("DIRECT")


def test_module_a_feedstock_and_species_boundaries():
    """Verify reference batches and secondary dal species require separate validation."""
    refs = FeedstockCharacterizationModule.get_reference_batches()
    assert "INDIAN_LATUR_FRESH" in refs
    assert "TANZANIAN_HTC_AGED_NOMINAL" in refs
    assert refs["TANZANIAN_HTC_AGED_NOMINAL"].bound_ca_mol_m3 > refs["INDIAN_LATUR_FRESH"].bound_ca_mol_m3

    others = FeedstockCharacterizationModule.get_other_dal_species_profiles()
    for key, spec in others.items():
        assert spec.requires_separate_species_validation is True, f"{key} must require separate validation"
        assert spec.evidence_tag == "INDIRECT_SPECIES_EXTENSION"


def test_module_b_empirical_vs_pde_and_grid_convergence():
    """Verify Peleg/Weibull hydration bounds and 2D PDE grid convergence (12x12 vs 24x24)."""
    b_tza = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]
    chem = TreatmentChemistryModule.design_citrate_buffer("CIT", "Citrate", 0.145, 5.20, 0.90)
    cfg = PretreatmentProcessConfig(soak_temp_c=55.0, soak_time_min=18.0, ultrasound_w_per_l=17.0)

    emp = HydrationAndPenetrationModule.predict_empirical_peleg_weibull(b_tza, 55.0, 18.0, chem.ionic_strength_M)
    assert 0.20 <= emp["moisture_peleg_wb"] <= 0.55
    assert 0.20 <= emp["moisture_weibull_wb"] <= 0.55

    pde_12 = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem, cfg, grid_size=12)
    pde_24 = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem, cfg, grid_size=24)

    # Grid convergence: volume-averaged Ca displacement between 12x12 and 24x24 must agree within 4%
    assert abs(pde_12["ca_displacement_pct"] - pde_24["ca_displacement_pct"]) < 4.0


def test_module_c_untreated_vs_treated_two_whistle_criterion():
    """Verify untreated aged Tanzanian dal fails 2 whistles (4-5 whistles) while conditioned dal passes in <=2 whistles."""
    b_tza = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]
    water = TreatmentChemistryModule.design_pure_water()
    cfg_none = PretreatmentProcessConfig(soak_temp_c=25.0, soak_time_min=0.0)
    soak_raw = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, water, cfg_none)
    cook_raw = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak_raw)

    assert cook_raw["whistle_count_at_t90"] >= 4
    assert cook_raw["is_two_whistles_or_less"] is False

    chem_opt = TreatmentChemistryModule.design_citrate_buffer("OPT", "Optimal K/Na Citrate", 0.145, 5.20, 0.90)
    cfg_opt = PretreatmentProcessConfig(soak_temp_c=55.0, soak_time_min=20.0, ultrasound_w_per_l=17.0)
    soak_opt = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem_opt, cfg_opt)
    cook_opt = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak_opt)

    assert cook_opt["whistle_count_at_t90"] <= 2
    assert cook_opt["f_wb_core_at_whistle_2_N"] <= 18.0
    assert cook_opt["is_two_whistles_or_less"] is True


def test_module_d_historical_sop_ph_audit():
    """Verify Module D detects the historical SOP Tier 2 pH 6.76 mismatch and designs true pH 5.20 buffer."""
    # Historical SOP recipe: 33.8 g/L K3Cit.H2O + 3.7 g/L Na3Cit.2H2O + 2.5 g/L H3Cit
    old_sop = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(
        mass_k3cit_monohydrate_g_L=33.8,
        mass_na3cit_dihydrate_g_L=3.7,
        mass_citric_acid_anhydrous_g_L=2.5,
        use_activity_correction=False,
    )
    assert old_sop["equilibrium_pH"] > 6.50, "Historical SOP recipe must be flagged as pH ~6.76, not 5.20"

    # Corrected recipe for pH 5.20
    corrected = TreatmentChemistryModule.design_citrate_buffer("NEW", "Corrected Tier 2", 0.145, 5.20, 0.90)
    verify_new = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(
        mass_k3cit_monohydrate_g_L=corrected.mass_k3cit_monohydrate_g_L,
        mass_na3cit_dihydrate_g_L=corrected.mass_na3cit_dihydrate_g_L,
        mass_citric_acid_anhydrous_g_L=corrected.mass_citric_acid_anhydrous_g_L,
        use_activity_correction=False,
    )
    assert abs(verify_new["equilibrium_pH"] - 5.20) < 0.02


def test_module_e_and_f_washing_and_tost_sensory_design():
    """Verify spray washing reduces surface residue monotonically and TOST study is properly powered."""
    b_tza = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]
    chem = TreatmentChemistryModule.design_citrate_buffer("CIT", "Citrate", 0.145, 5.20, 0.90)
    cfg = PretreatmentProcessConfig(55.0, 20.0, 17.0)
    soak = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem, cfg)

    w0 = WashingAndResidueModule.simulate_washing_operation(chem, soak, wash_mode="NO_WASH")
    w12 = WashingAndResidueModule.simulate_washing_operation(chem, soak, wash_time_s=12.0)
    assert w12["residual_surface_film_ppm"] < w0["residual_surface_film_ppm"] * 0.05

    sens = SensoryAndFlavourModule.evaluate_flavour_and_sensory_risk(b_tza, chem, cfg, w12)
    assert sens["sub_threshold_aftertaste_pass"] is True
    assert sens["evidence_tag"] == "MODEL_DERIVED_REQUIRES_SENSORY_PANEL"

    tost = SensoryAndFlavourModule.design_iso_tost_equivalence_study()
    assert tost["minimum_consumers_required"] >= 72
    assert tost["minimum_consumers_required"] % 6 == 0


def test_sobol_global_sensitivity_analytical_benchmark():
    """Verify GlobalSensitivityAnalyzer against analytical linear function Y = 3*X1 + 1*X2 + 0*X3."""
    def linear_fn(x):
        return 3.0 * x[0] + 1.0 * x[1] + 0.0 * x[2]

    res = GlobalSensitivityAnalyzer.compute_sobol_indices(
        linear_fn,
        param_names=["X1", "X2", "X3"],
        bounds=[(0.0, 1.0), (0.0, 1.0), (0.0, 1.0)],
        n_base=256,
    )
    # Theoretical variance shares: 3^2 / (3^2 + 1^2) = 0.90 for X1, 0.10 for X2, 0.0 for X3
    assert abs(res["first_order_S1"]["X1"] - 0.90) < 0.06
    assert abs(res["first_order_S1"]["X2"] - 0.10) < 0.06
    assert res["total_order_ST"]["X3"] < 0.02


def test_omega_cli_and_claim_question_registers():
    """Verify the 14-field Claim-Provenance Ledger, 35-Question Register, and unified OMEGA CLI."""
    from finnoaq.omega_cli import cmd_audit, cmd_claims_audit, cmd_plant_audit, cmd_validate

    audit_res = cmd_audit()
    assert audit_res["status"] == "PASS"
    assert audit_res["claims_registered"] >= 14
    assert audit_res["questions_registered"] == 35

    claims_res = cmd_claims_audit()
    assert claims_res["status"] == "PASS"
    assert claims_res["claims_with_all_14_fields"] == claims_res["total_claims"]

    plant_res = cmd_plant_audit()
    assert plant_res["status"] == "PASS"
    assert abs(plant_res["bleed_feed_85pct_recycle"]["evap_discrepancy_B2_minus_B1_kg_day"] - 199.72) < 0.05

    val_res = cmd_validate()
    assert val_res["status"] == "PASS"


def test_gpu_uncertainty_and_robust_adaptive_p95():
    """Verify the RTX 4050 GPU 2D-PDE campaign artifact and the P95 <= 18.0 N robust adaptive policy."""
    import json
    gpu_path = ROOT / "artifacts" / "omega_gpu_uncertainty_campaign.json"
    assert gpu_path.exists()
    data = json.loads(gpu_path.read_text(encoding="utf-8"))

    assert "NVIDIA" in data["metadata"]["compute_device"]
    assert data["metadata"]["total_2d_pde_and_mc_trajectories"] >= 500000

    # Verify Stage 1 uncertainty bounds at 20 min vs 24 min
    s1 = data["stage1_uncertainty_quantification"]["margin_audit_20min_vs_24min"]
    assert s1["mc_24min_p95_N"] <= 18.0
    assert s1["mc_24min_prob_pass_pct"] > s1["mc_20min_prob_pass_pct"]

    # Verify Stage 3 robust policy resolves the P95 > 18.0 N mismatch
    policies = {p["policy_id"]: p for p in data["stage3_robust_policy_comparison"]["policies_comparison"]}
    assert policies["ADAPTIVE_NOISY_STANDARD"]["f_wb_core_p95_N"] > 18.0
    assert policies["ADAPTIVE_ROBUST_P95"]["f_wb_core_p95_N"] <= 18.0
    assert policies["ADAPTIVE_ROBUST_P95"]["pass_rate_le_18N_pct"] >= 95.0


