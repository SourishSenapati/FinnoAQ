"""
FINNOAQ OMEGA — Master Offline Scientific Investigation & Benchmark Runner
==========================================================================
Project Ref: FNQ-PR-2026-001
Lead Chemical and Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

Executes strictly in staged scientific order:
  - Hardware & Solver Benchmark (CPU vs RTX 4050 CUDA GPU)
  - Historical Recipe & Defect Audit (FAIL-0021 through FAIL-0025)
  - Stage 1: Cookability & Shortest Credible Pretreatment
  - Stage 2: Aftertaste Elimination, Washing & Indian Flavour Equivalence (ISO 11136 TOST)
  - Stage 3: Batch Variability (500-Lot Monte Carlo), Noisy 5-Min Intake Diagnostics & Other Dals
  - Stage 4: 15 TPD Plant Cycle, Drying Stress, Reconciled OpEx & Sobol Global Sensitivity
"""

from __future__ import annotations

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch

_RESOLVED_PARENT = Path(__file__).resolve().parent.parent
ROOT = _RESOLVED_PARENT.parent if _RESOLVED_PARENT.name == "toor_dal_optimization" else _RESOLVED_PARENT

for p in [str(ROOT), str(ROOT / "src"), str(ROOT / "governance" / "errors")]:
    if p not in sys.path:
        sys.path.insert(0, p)

from circuit_breaker import ExecutionCircuitBreaker
from finnoaq.canonical_biophysics import evaluate_treatment_batch_gpu
from finnoaq.omega_modules import (
    BatchVariabilityAndAdaptationModule,
    FeedstockBatch,
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


def run_hardware_benchmark() -> Dict[str, Any]:
    """Benchmarks representative workloads on CPU vs RTX 4050 CUDA GPU."""
    has_cuda = torch.cuda.is_available()
    gpu_name = torch.cuda.get_device_name(0) if has_cuda else "NONE"

    # Workload 1: Single-lot 2D PDE integration (16x16 grid, 20 min soak) on CPU
    b_tza = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]
    chem = TreatmentChemistryModule.design_citrate_buffer("BENCH", "Bench", 0.145, 5.20, 0.90)
    cfg = PretreatmentProcessConfig(55.0, 20.0, 17.0)

    t0 = time.perf_counter()
    for _ in range(10):
        HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem, cfg, grid_size=16)
    cpu_10_lots_ms = (time.perf_counter() - t0) * 1000.0

    # Workload 2: Vectorized 256-lot batch evaluation on CPU vs GPU
    params_256 = [(55.0, 0.145, 0.90, 5.20, 20.0, 0.50, 50.0, 105.0) for _ in range(256)]
    t0 = time.perf_counter()
    evaluate_treatment_batch_gpu(params_256, grid_size=16, device=torch.device("cpu"))
    batch_cpu_ms = (time.perf_counter() - t0) * 1000.0

    batch_gpu_ms = None
    if has_cuda:
        # Warmup CUDA kernels
        evaluate_treatment_batch_gpu(params_256[:16], grid_size=16, device=torch.device("cuda:0"))
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        evaluate_treatment_batch_gpu(params_256, grid_size=16, device=torch.device("cuda:0"))
        torch.cuda.synchronize()
        batch_gpu_ms = (time.perf_counter() - t0) * 1000.0

    return {
        "cpu_model": "AMD Ryzen AI 9 365 w/ Radeon 880M (20 logical threads)",
        "gpu_model": gpu_name,
        "cuda_available": has_cuda,
        "single_lot_2d_pde_cpu_ms_per_eval": round(cpu_10_lots_ms / 10.0, 2),
        "vectorized_256_batch_cpu_ms": round(batch_cpu_ms, 2),
        "vectorized_256_batch_gpu_ms": round(batch_gpu_ms, 2) if batch_gpu_ms is not None else None,
        "gpu_speedup_factor_256_batch": round(batch_cpu_ms / batch_gpu_ms, 2) if batch_gpu_ms else None,
    }


def run_recipe_stoichiometry_audit() -> Dict[str, Any]:
    """Audits historical SOP and Monday Bench Trial recipes vs corrected OMEGA recipes (FAIL-0024)."""
    old_sop_tier1 = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(21.6, 2.4, 1.5, 0.0)
    old_sop_tier2 = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(33.8, 3.7, 2.5, 0.0)
    old_sop_tier3 = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(42.5, 4.6, 3.5, 0.0)
    old_bench_pot4 = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(0.0, 30.0, 7.333, 0.0)
    old_bench_kitchen = TreatmentChemistryModule.solve_equilibrium_pH_from_masses(0.0, 0.0, 21.333, 24.0)

    new_tier1 = TreatmentChemistryModule.design_citrate_buffer("TIER1", "Tier 1 Mild (0.105 M, pH 5.30)", 0.105, 5.30, 0.90)
    new_tier2 = TreatmentChemistryModule.design_citrate_buffer("TIER2", "Tier 2 Standard (0.145 M, pH 5.20)", 0.145, 5.20, 0.90)
    new_tier3 = TreatmentChemistryModule.design_citrate_buffer("TIER3", "Tier 3 Intensive (0.185 M, pH 5.20)", 0.185, 5.20, 0.90)
    new_bench_pot4 = TreatmentChemistryModule.design_citrate_buffer("POT4", "Bench Pot 4 (0.145 M, pH 5.20, 90:10 K:Na)", 0.145, 5.20, 0.90)

    return {
        "historical_recipes_audit": {
            "SOP_Tier1_claimed_pH_5.20_actual_pH": round(old_sop_tier1["equilibrium_pH"], 2),
            "SOP_Tier2_claimed_pH_5.20_actual_pH": round(old_sop_tier2["equilibrium_pH"], 2),
            "SOP_Tier3_claimed_pH_5.20_actual_pH": round(old_sop_tier3["equilibrium_pH"], 2),
            "Bench_Pot4_claimed_pH_5.20_actual_pH": round(old_bench_pot4["equilibrium_pH"], 2),
            "Bench_Kitchen_claimed_pH_5.20_actual_pH": round(old_bench_kitchen["equilibrium_pH"], 2),
        },
        "corrected_omega_recipes_per_1000L": {
            "TIER_1_MILD_0.105M_pH_5.30": {
                "K3Cit_H2O_kg": round(new_tier1.mass_k3cit_monohydrate_g_L, 2),
                "Na3Cit_2H2O_kg": round(new_tier1.mass_na3cit_dihydrate_g_L, 2),
                "Citric_Acid_Anhydrous_kg": round(new_tier1.mass_citric_acid_anhydrous_g_L, 2),
                "verified_pH": round(new_tier1.equilibrium_pH, 2),
            },
            "TIER_2_STANDARD_0.145M_pH_5.20": {
                "K3Cit_H2O_kg": round(new_tier2.mass_k3cit_monohydrate_g_L, 2),
                "Na3Cit_2H2O_kg": round(new_tier2.mass_na3cit_dihydrate_g_L, 2),
                "Citric_Acid_Anhydrous_kg": round(new_tier2.mass_citric_acid_anhydrous_g_L, 2),
                "verified_pH": round(new_tier2.equilibrium_pH, 2),
            },
            "TIER_3_INTENSIVE_0.185M_pH_5.20": {
                "K3Cit_H2O_kg": round(new_tier3.mass_k3cit_monohydrate_g_L, 2),
                "Na3Cit_2H2O_kg": round(new_tier3.mass_na3cit_dihydrate_g_L, 2),
                "Citric_Acid_Anhydrous_kg": round(new_tier3.mass_citric_acid_anhydrous_g_L, 2),
                "verified_pH": round(new_tier3.equilibrium_pH, 2),
            },
            "BENCH_POT4_750mL_GRAMS": {
                "K3Cit_H2O_g_per_750mL": round(new_bench_pot4.mass_k3cit_monohydrate_g_L * 0.75, 2),
                "Na3Cit_2H2O_g_per_750mL": round(new_bench_pot4.mass_na3cit_dihydrate_g_L * 0.75, 2),
                "Citric_Acid_Anhydrous_g_per_750mL": round(new_bench_pot4.mass_citric_acid_anhydrous_g_L * 0.75, 2),
                "verified_pH": round(new_bench_pot4.equilibrium_pH, 2),
            },
        },
    }


def run_stage1_cookability_study() -> List[Dict[str, Any]]:
    """Stage 1: Evaluates cooking performance and identifies shortest credible pretreatment."""
    refs = FeedstockCharacterizationModule.get_reference_batches()
    b_ind = refs["INDIAN_LATUR_FRESH"]
    b_tza = refs["TANZANIAN_HTC_AGED_NOMINAL"]

    water = TreatmentChemistryModule.design_pure_water()
    bicarb = TreatmentChemistryModule.design_bicarbonate_bath("BICARB", "0.5% NaHCO3 Alkaline (pH 8.32)", 5.0)
    cit_opt = TreatmentChemistryModule.design_citrate_buffer("CIT-OPT", "0.145 M K/Na Citrate (90:10, pH 5.20)", 0.145, 5.20, 0.90)

    candidates = [
        ("S1-01-IND-REF", "Indian Latur Fresh Reference (Untreated)", b_ind, water, PretreatmentProcessConfig(25.0, 0.0)),
        ("S1-02-TZA-RAW", "Tanzanian Aged HTC Control (Untreated)", b_tza, water, PretreatmentProcessConfig(25.0, 0.0)),
        ("S1-03-WATER-20", "Warm Water Soak Only (55°C, 20 min)", b_tza, water, PretreatmentProcessConfig(55.0, 20.0)),
        ("S1-04-BICARB-20", "Alkaline NaHCO3 0.5% w/v (55°C, 20 min)", b_tza, bicarb, PretreatmentProcessConfig(55.0, 20.0)),
        ("S1-05-CIT-STATIC-20", "Hybrid K/Na Citrate Static Soak (55°C, 20 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 20.0, 0.0)),
        ("S1-06-CIT-UAE-5", "Hybrid Citrate + Ultrasound 17 W/L (55°C, 5 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 5.0, 17.0)),
        ("S1-07-CIT-UAE-10", "Hybrid Citrate + Ultrasound 17 W/L (55°C, 10 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 10.0, 17.0)),
        ("S1-08-CIT-UAE-15", "Hybrid Citrate + Ultrasound 17 W/L (55°C, 15 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 15.0, 17.0)),
        ("S1-09-CIT-UAE-20", "Hybrid Citrate + Ultrasound 17 W/L (55°C, 20 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 20.0, 17.0)),
        ("S1-10-CIT-VI-4.6", "Hybrid Citrate + Vacuum Pulse Only (15 kPa, 4.6 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 4.6, 0.0, 15.0)),
        ("S1-11-CIT-VI-UAE-15", "Hybrid Citrate + Vacuum Pulse + UAE (15 kPa, 15 min)", b_tza, cit_opt, PretreatmentProcessConfig(55.0, 15.0, 17.0, 15.0)),
    ]

    results = []
    for cid, label, batch, chem, cfg in candidates:
        soak = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(batch, chem, cfg)
        cook = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak)
        results.append({
            "candidate_id": cid,
            "description": label,
            "soak_time_min": cfg.soak_time_min,
            "soak_temp_c": cfg.soak_temp_c,
            "bulk_ca_disp_pct": round(soak["ca_displacement_pct"], 1),
            "core_ca_disp_pct": round(soak["core_ca_displacement_pct"], 1),
            "hydrated_moisture_wb_pct": round(soak["mean_moisture_wb"] * 100.0, 1),
            "t90_mechanistic_min": round(cook["t90_mechanistic_min"], 2),
            "t90_empirical_nisha_min": round(cook["t90_empirical_nisha_min"], 2),
            "whistles_at_t90": cook["whistle_count_at_t90"],
            "f_wb_bulk_w2_N": round(cook["f_wb_bulk_at_whistle_2_N"], 2),
            "f_wb_core_w2_N": round(cook["f_wb_core_at_whistle_2_N"], 2),
            "passes_two_whistle_gate": cook["is_two_whistles_or_less"],
            "solid_leaching_loss_pct": round(soak["solid_leaching_loss_pct"], 2),
        })
    return results


def run_stage2_aftertaste_and_washing_study() -> Dict[str, Any]:
    """Stage 2: Evaluates aftertaste precursors, washing regimes, and ISO 11136 TOST equivalence."""
    b_tza = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]
    cfg_20 = PretreatmentProcessConfig(55.0, 20.0, 17.0)

    chem_bicarb = TreatmentChemistryModule.design_bicarbonate_bath("BICARB", "0.5% NaHCO3 (pH 8.32)", 5.0)
    chem_quench = TreatmentChemistryModule.design_bicarbonate_bath("QUENCH", "0.5% NaHCO3 + 0.03M Citric Acid Quench", 5.0, 0.03)
    chem_na_cit = TreatmentChemistryModule.design_citrate_buffer("NA-CIT", "100% Na-Citrate Buffer (0.145 M, pH 5.20)", 0.145, 5.20, 0.0)
    chem_k_cit = TreatmentChemistryModule.design_citrate_buffer("K-CIT", "100% K-Citrate Buffer (0.145 M, pH 5.20)", 0.145, 5.20, 1.0)
    chem_hyb = TreatmentChemistryModule.design_citrate_buffer("HYB-CIT", "90:10 K/Na Hybrid Citrate (0.145 M, pH 5.20)", 0.145, 5.20, 0.90)

    matrix_results = []
    cases = [
        ("S2-01", chem_bicarb, "NO_WASH", 0.0, 0.0),
        ("S2-02", chem_bicarb, "DUAL_FAN_HIGH_PRESSURE_SPRAY", 12.0, 0.50),
        ("S2-03", chem_quench, "DUAL_FAN_HIGH_PRESSURE_SPRAY", 12.0, 0.50),
        ("S2-04", chem_na_cit, "DUAL_FAN_HIGH_PRESSURE_SPRAY", 12.0, 0.50),
        ("S2-05", chem_k_cit, "NO_WASH", 0.0, 0.0),
        ("S2-06", chem_k_cit, "DUAL_FAN_HIGH_PRESSURE_SPRAY", 12.0, 0.50),
        ("S2-07", chem_hyb, "NO_WASH", 0.0, 0.0),
        ("S2-08", chem_hyb, "STATIC_IMMERSION_RINSE", 30.0, 1.20),
        ("S2-09", chem_hyb, "ROTARY_DRUM_RINSE", 20.0, 0.80),
        ("S2-10-WINNER", chem_hyb, "DUAL_FAN_HIGH_PRESSURE_SPRAY", 12.0, 0.50),
    ]

    for cid, chem, w_mode, w_time, w_ratio in cases:
        soak = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b_tza, chem, cfg_20)
        cook = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak)
        wash = WashingAndResidueModule.simulate_washing_operation(chem, soak, w_mode, w_time, w_ratio)
        sens = SensoryAndFlavourModule.evaluate_flavour_and_sensory_risk(b_tza, chem, cfg_20, wash)
        matrix_results.append({
            "case_id": cid,
            "chemistry": chem.name,
            "wash_mode": w_mode,
            "wash_time_s": w_time,
            "wash_water_L_kg": w_ratio,
            "surface_film_residue_ppm": round(wash["residual_surface_film_ppm"], 1),
            "retained_citrate_mg_100g": round(wash["retained_citrate_mg_100g"], 1),
            "retained_K_mg_100g": round(wash["retained_K_mg_100g"], 1),
            "retained_Na_mg_100g": round(wash["retained_Na_mg_100g"], 1),
            "max_off_taste_ratio": round(sens["max_off_taste_threshold_ratio"], 3),
            "lox_residual_pct": round(sens["lox_residual_activity_pct"], 1),
            "predicted_hexanal_ppb": round(sens["predicted_hexanal_ppb"], 1),
            "thurstonian_d_prime": round(sens["thurstonian_d_prime_estimate"], 2),
            "sub_threshold_aftertaste_pass": sens["sub_threshold_aftertaste_pass"],
            "f_wb_core_w2_N": round(cook["f_wb_core_at_whistle_2_N"], 2),
            "passes_two_whistle_gate": cook["is_two_whistles_or_less"],
        })

    return {
        "washing_and_chemistry_matrix": matrix_results,
        "iso_11136_tost_study_design": SensoryAndFlavourModule.design_iso_tost_equivalence_study(),
    }


def run_stage3_batch_variability_and_species_study(n_batches: int = 300) -> Dict[str, Any]:
    """
    Stage 3: Evaluates 300 diverse incoming batches (varying thickness H, moisture X_wb,
    storage history, and bound Ca2+) under:
      1. Untreated Control
      2. Fixed Single-Tier Policy (Tier 2 applied blindly to all lots)
      3. Noisy 5-Minute Intake Proxy Adaptive Policy (Tier 1 / Tier 2 / Tier 3 assigned from noisy intake test)
    Also evaluates Multi-Species Extension profiles.
    """
    rng = np.random.default_rng(20261028)
    batches: List[FeedstockBatch] = []

    for i in range(n_batches):
        # Sample across 3 realistic import strata: 25% Mild/Moderate, 55% Nominal Aged HTC, 20% Severe HTC
        u = rng.random()
        if u < 0.25:
            origin = "Tanzanian_ICEAP_01514_Moderate"
            h_m = float(np.clip(rng.normal(0.96e-3, 0.05e-3), 0.82e-3, 1.12e-3))
            ca = float(np.clip(rng.normal(23.5, 2.8), 16.0, 30.0))
            de = float(np.clip(rng.normal(0.38, 0.04), 0.25, 0.48))
            months = float(rng.uniform(4.0, 7.0))
        elif u < 0.80:
            origin = "Tanzanian_ICEAP_00557_Aged"
            h_m = float(np.clip(rng.normal(1.09e-3, 0.06e-3), 0.92e-3, 1.25e-3))
            ca = float(np.clip(rng.normal(34.5, 3.2), 26.0, 41.0))
            de = float(np.clip(rng.normal(0.29, 0.04), 0.20, 0.38))
            months = float(rng.uniform(7.0, 11.0))
        else:
            origin = "East_African_ICP_9145_Severe"
            h_m = float(np.clip(rng.normal(1.18e-3, 0.06e-3), 1.05e-3, 1.36e-3))
            ca = float(np.clip(rng.normal(41.0, 3.0), 35.0, 47.5))
            de = float(np.clip(rng.normal(0.23, 0.03), 0.18, 0.30))
            months = float(rng.uniform(11.0, 15.0))

        x_wb = float(np.clip(rng.normal(0.101, 0.008), 0.080, 0.125))
        batches.append(
            FeedstockBatch(
                batch_id=f"LOT-{i+1:03d}",
                species="Cajanus cajan",
                cultivar_or_origin=origin,
                half_thickness_m=h_m,
                eq_radius_m=h_m * 2.22,
                initial_moisture_wb=x_wb,
                open_porosity=0.112,
                storage_months=months,
                storage_temp_c=30.0,
                storage_rh_pct=74.0,
                bound_ca_mol_m3=ca,
                bound_mg_mol_m3=26.0,
                phytate_p_mg_100g=160.0,
                pectin_de_fraction=de,
            )
        )

    chem_t2, cfg_t2 = BatchVariabilityAndAdaptationModule.get_tier_treatment_policy("TIER_2_STANDARD")

    fixed_pass_count = 0
    adaptive_pass_count = 0
    tier_matches = 0
    under_treated = 0
    over_treated = 0
    ood_count = 0

    fixed_core_forces = []
    adaptive_core_forces = []
    tier_counts = {"TIER_1_MILD": 0, "TIER_2_STANDARD": 0, "TIER_3_INTENSIVE": 0}

    tier_order = {"TIER_1_MILD": 1, "TIER_2_STANDARD": 2, "TIER_3_INTENSIVE": 3}

    for b in batches:
        # 1. Fixed Tier 2 evaluation (grid_size=12 for fast 300-lot PDE sweep)
        soak_fix = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b, chem_t2, cfg_t2, grid_size=12)
        cook_fix = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak_fix)
        fixed_core_forces.append(cook_fix["f_wb_core_at_whistle_2_N"])
        if cook_fix["is_two_whistles_or_less"]:
            fixed_pass_count += 1

        # 2. Noisy 5-Minute Intake Diagnostic + Adaptive Tier Policy
        diag = BatchVariabilityAndAdaptationModule.simulate_noisy_intake_diagnostics(b, rng)
        assigned = diag["assigned_tier"]
        true_t = diag["true_tier"]
        tier_counts[assigned] += 1
        if diag["is_out_of_domain"]:
            ood_count += 1
        if assigned == true_t:
            tier_matches += 1
        elif tier_order[assigned] < tier_order[true_t]:
            under_treated += 1
        else:
            over_treated += 1

        chem_ad, cfg_ad = BatchVariabilityAndAdaptationModule.get_tier_treatment_policy(assigned)
        soak_ad = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b, chem_ad, cfg_ad, grid_size=12)
        cook_ad = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak_ad)
        adaptive_core_forces.append(cook_ad["f_wb_core_at_whistle_2_N"])
        if cook_ad["is_two_whistles_or_less"]:
            adaptive_pass_count += 1

    # Evaluate secondary dal species
    species_results = []
    for sp_key, sp_batch in FeedstockCharacterizationModule.get_other_dal_species_profiles().items():
        # Select appropriate soak duration by thickness
        soak_min = 12.0 if sp_batch.half_thickness_m < 0.85e-3 else (24.0 if sp_batch.half_thickness_m > 1.20e-3 else 18.0)
        cfg_sp = PretreatmentProcessConfig(55.0, soak_min, 17.0)
        soak_sp = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(sp_batch, chem_t2, cfg_sp, grid_size=14)
        cook_sp = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(soak_sp)
        species_results.append({
            "species_key": sp_key,
            "species_name": sp_batch.species,
            "full_thickness_mm": round(sp_batch.full_thickness_mm, 2),
            "bound_ca_mol_m3": sp_batch.bound_ca_mol_m3,
            "recommended_soak_min": soak_min,
            "core_ca_disp_pct": round(soak_sp["core_ca_displacement_pct"], 1),
            "whistles_at_t90": cook_sp["whistle_count_at_t90"],
            "f_wb_core_w2_N": round(cook_sp["f_wb_core_at_whistle_2_N"], 2),
            "requires_separate_physical_validation": sp_batch.requires_separate_species_validation,
        })

    return {
        "n_batches_evaluated": n_batches,
        "fixed_tier2_pass_rate_pct": round(100.0 * fixed_pass_count / n_batches, 1),
        "fixed_tier2_core_force_mean_N": round(float(np.mean(fixed_core_forces)), 2),
        "fixed_tier2_core_force_p95_N": round(float(np.percentile(fixed_core_forces, 95)), 2),
        "noisy_adaptive_pass_rate_pct": round(100.0 * adaptive_pass_count / n_batches, 1),
        "noisy_adaptive_core_force_mean_N": round(float(np.mean(adaptive_core_forces)), 2),
        "noisy_adaptive_core_force_p95_N": round(float(np.percentile(adaptive_core_forces, 95)), 2),
        "intake_classifier_accuracy_pct": round(100.0 * tier_matches / n_batches, 1),
        "false_under_treatment_rate_pct": round(100.0 * under_treated / n_batches, 1),
        "false_over_treatment_rate_pct": round(100.0 * over_treated / n_batches, 1),
        "out_of_domain_flagged_pct": round(100.0 * ood_count / n_batches, 1),
        "assigned_tier_distribution": tier_counts,
        "other_dal_species_screening": species_results,
    }


def run_stage4_plant_and_sobol_study() -> Dict[str, Any]:
    """Stage 4: Evaluates 15 TPD drying schedules, once-through vs recycled OpEx, and Sobol sensitivity."""
    dry_regimes = [
        PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
            "D1_85C_Single_Stage_Blast", 85.0, 42.0, 85.0, 0.0, 0.0
        ),
        PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
            "D2_75C_Single_Stage", 75.0, 46.0, 75.0, 0.0, 0.0
        ),
        PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
            "D3_65C_55C_Two_Stage_No_Temper", 65.0, 22.0, 55.0, 26.0, 0.0
        ),
        PlantOperationsAndEconomicsModule.simulate_convective_drying_and_stress(
            "D4_65C_55C_Two_Stage_With_20min_Temper", 65.0, 22.0, 55.0, 25.0, 20.0
        ),
    ]

    chem_t2 = TreatmentChemistryModule.design_citrate_buffer("TIER2", "Tier 2 Standard", 0.145, 5.20, 0.90)
    cfg_t2 = PretreatmentProcessConfig(55.0, 20.0, 17.0)

    econ_once_through = PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics(
        chem_t2, cfg_t2, dry_regimes[3], liquor_recycle_fraction=0.0
    )
    econ_85_recycle = PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics(
        chem_t2, cfg_t2, dry_regimes[3], liquor_recycle_fraction=0.85
    )

    # Global Sensitivity Analysis (Sobol S1 and ST) on Whistle-2 Core Shear Force F_WB_core
    # Varying 5 key biophysical/process parameters:
    #   [0] half_thickness_m (0.90e-3 to 1.28e-3 m)
    #   [1] bound_ca_mol_m3 (20.0 to 44.0 mol/m^3)
    #   [2] soak_time_min (8.0 to 28.0 min)
    #   [3] total_citrate_M (0.08 to 0.20 M)
    #   [4] soak_temp_c (40.0 to 60.0 C)
    b_base = FeedstockCharacterizationModule.get_reference_batches()["TANZANIAN_HTC_AGED_NOMINAL"]

    def sobol_eval_fn(x: np.ndarray) -> float:
        b = FeedstockBatch(
            batch_id="SOBOL",
            species="Cajanus cajan",
            cultivar_or_origin="Sobol_Sample",
            half_thickness_m=float(x[0]),
            eq_radius_m=float(x[0] * 2.22),
            initial_moisture_wb=0.10,
            open_porosity=0.11,
            storage_months=9.0,
            storage_temp_c=30.0,
            storage_rh_pct=75.0,
            bound_ca_mol_m3=float(x[1]),
            bound_mg_mol_m3=26.0,
            phytate_p_mg_100g=150.0,
            pectin_de_fraction=0.28,
        )
        ch = TreatmentChemistryModule.design_citrate_buffer("S", "S", float(x[3]), 5.20, 0.90)
        cf = PretreatmentProcessConfig(soak_temp_c=float(x[4]), soak_time_min=float(x[2]), ultrasound_w_per_l=17.0)
        sk = HydrationAndPenetrationModule.solve_2d_conservative_soaking_pde(b, ch, cf, grid_size=10)
        ck = ThermalAndPressureCookingModule.solve_pressure_cooking_softening(sk)
        return float(ck["f_wb_core_at_whistle_2_N"])

    sobol_res = GlobalSensitivityAnalyzer.compute_sobol_indices(
        sobol_eval_fn,
        param_names=[
            "Half_Thickness_H",
            "Native_Bound_Ca",
            "Steeping_Time_t",
            "Citrate_Molarity_C",
            "Steeping_Temp_T",
        ],
        bounds=[
            (0.90e-3, 1.28e-3),
            (20.0, 44.0),
            (8.0, 28.0),
            (0.08, 0.20),
            (40.0, 60.0),
        ],
        n_base=32,  # 32 * (5 + 2) = 224 full 2D PDE + pressure cooker evaluations
    )

    return {
        "drying_regimes_comparison": dry_regimes,
        "economics_once_through_0pct_recycle": econ_once_through,
        "economics_bleed_feed_85pct_recycle": econ_85_recycle,
        "sobol_global_sensitivity_f_wb_core": sobol_res,
    }


def main() -> None:
    cb = ExecutionCircuitBreaker()
    cb.run_preflight_checks()

    t_start = time.perf_counter()
    hw = run_hardware_benchmark()
    recipe_audit = run_recipe_stoichiometry_audit()
    s1 = run_stage1_cookability_study()
    s2 = run_stage2_aftertaste_and_washing_study()
    s3 = run_stage3_batch_variability_and_species_study(n_batches=150)
    s4 = run_stage4_plant_and_sobol_study()
    elapsed_s = time.perf_counter() - t_start

    out = {
        "metadata": {
            "project_ref": "FNQ-PR-2026-001",
            "lead_engineer": "Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)",
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "total_execution_time_s": round(elapsed_s, 2),
        },
        "hardware_benchmark": hw,
        "recipe_stoichiometry_audit": recipe_audit,
        "stage1_cookability": s1,
        "stage2_aftertaste_and_washing": s2,
        "stage3_batch_variability": s3,
        "stage4_plant_and_sensitivity": s4,
    }

    art_dir = ROOT / "artifacts"
    art_dir.mkdir(parents=True, exist_ok=True)
    out_path = art_dir / "omega_investigation_results.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[OK] Completed FINNOAQ OMEGA full investigation in {elapsed_s:.2f} s -> {out_path}")


if __name__ == "__main__":
    main()
