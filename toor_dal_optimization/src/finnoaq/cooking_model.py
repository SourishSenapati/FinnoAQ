"""
FinnoaQ Engineering Workspace — Cooking Performance and Texture Endpoint Modeling.
Project Reference: FNQ-PR-2026-001 | Toor Dal Cooking-Time Optimization
Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

This module implements:
1. Separation of hydration state, starch gelatinization, cell wall softening, and chemical effects.
2. Standardized calibrated laboratory autoclave endpoint T90 (<= 10.0% hard-core retention under 500 g load).
3. Explicit segregation of informal household whistle counts as SOURCE_REPORTED uncalibrated observations.
4. Model comparison: Baseline Covariates vs Hydration-Only vs Richer Mechanistic Candidate Model.
5. Explicit NOT_VALIDATED status for Tanzanian target dal until real physical assay data are logged.
"""

import numpy as np
from typing import Dict, Any, List, Optional

class CookingPerformanceModel:
    """
    Evaluates cooking time, tenderness kinetics, and hard-core retention.
    """
    def __init__(self):
        self.whistle_to_min_heuristic = {
            'target_reported_whistles': 6.0,
            'benchmark_reported_whistles': 3.0,
            'whistle_evidence_state': 'SOURCE_REPORTED_UNCALIBRATED',
            'warning': 'Household whistle counts are discontinuous, uncalibrated, and must NOT be used as lab time.'
        }

    def hard_core_retention(
        self,
        t_cooking_min: np.ndarray,
        k_softening: float,
        h0: float = 100.0
    ) -> np.ndarray:
        """
        Models percentage of cooked grains retaining an ungelatinized opaque central hard-core:
        H(t) = H0 * exp(- k_softening * t)
        Endpoint T90 is the time when H(t) <= 10.0%.
        """
        t = np.asarray(t_cooking_min, dtype=np.float64)
        if k_softening <= 0.0:
            raise ValueError("Softening rate constant k_softening must be strictly positive.")
        h_t = h0 * np.exp(- k_softening * t)
        return np.clip(h_t, 0.0, 100.0)

    def calculate_t90(self, k_softening: float, h0: float = 100.0, target_threshold: float = 10.0) -> float:
        """Calculates exact time to achieve T90 endpoint (H(t) <= target_threshold)."""
        if k_softening <= 0.0:
            return float('inf')
        return float(np.log(h0 / target_threshold) / k_softening)

    def evaluate_models(
        self,
        moisture_initial_wb: float = 0.105,
        water_absorption_rate_k1: Optional[float] = None,
        pectin_solubilization_ratio: Optional[float] = None,
        cooking_temp_c: float = 115.0,
        autoclave_gauge_pressure_bar: float = 0.678
    ) -> Dict[str, Any]:
        """
        Compares three candidate cooking models:
        1. Model 1 (Baseline Covariate): Dependent only on initial moisture and temperature.
        2. Model 2 (Hydration-Coupled): Softening rate driven by water diffusion rate (k1).
        3. Model 3 (Mechanistic Dual-Path): Coupled hydration + cell-wall pectin softening.
        """
        # Thermodynamic validation of autoclave state:
        # Saturated steam at 115 C has absolute pressure 1.691 bar, gauge pressure 0.678 bar.
        is_thermo_consistent = bool(abs(autoclave_gauge_pressure_bar - 0.678) < 0.15)

        # Baseline Model 1 (Empirical thermal baseline)
        # Assumes base rate k0 ~ 0.075 min^-1 at 115 C for typical pigeon pea
        k0_base = 0.075 * (cooking_temp_c / 115.0)
        t90_model1 = self.calculate_t90(k0_base)

        # Hydration-Coupled Model 2
        if water_absorption_rate_k1 is not None and water_absorption_rate_k1 > 0:
            # Slower absorption (higher k1) reduces softening rate
            # Reference k1_ref = 2.0 min/%
            k_soft_m2 = k0_base * (2.0 / water_absorption_rate_k1) ** 0.5
            t90_model2 = self.calculate_t90(k_soft_m2)
            model2_status = "CALCULATED_FROM_KINETICS"
        else:
            k_soft_m2 = None
            t90_model2 = None
            model2_status = "BLOCKED_MISSING_HYDRATION_DATA"

        # Mechanistic Model 3 (Hydration + Pectin solubilization)
        if (water_absorption_rate_k1 is not None and water_absorption_rate_k1 > 0 and
            pectin_solubilization_ratio is not None):
            # pectin_solubilization_ratio in [0.0, 1.0]
            k_soft_m3 = k0_base * (2.0 / water_absorption_rate_k1) ** 0.5 * (1.0 + 0.60 * pectin_solubilization_ratio)
            t90_model3 = self.calculate_t90(k_soft_m3)
            model3_status = "CALCULATED_FROM_ASSAYS"
        else:
            k_soft_m3 = None
            t90_model3 = None
            model3_status = "BLOCKED_MISSING_BIOCHEMICAL_DATA"

        return {
            'cooking_temperature_c': cooking_temp_c,
            'autoclave_gauge_pressure_bar': autoclave_gauge_pressure_bar,
            'thermodynamic_state_consistent': is_thermo_consistent,
            'source_reported_observations': self.whistle_to_min_heuristic,
            'model1_baseline_thermal': {
                'description': 'Pure thermal softening without biochemical covariates',
                'k_softening_min^-1': round(k0_base, 4),
                'predicted_t90_min': round(t90_model1, 2),
                'maturity_state': 'M2 — NUMERICALLY_VERIFIED'
            },
            'model2_hydration_coupled': {
                'description': 'Softening coupled to water absorption rate (k1)',
                'status': model2_status,
                'k_softening_min^-1': round(k_soft_m2, 4) if k_soft_m2 else None,
                'predicted_t90_min': round(t90_model2, 2) if t90_model2 else None,
                'maturity_state': 'M1 — IMPLEMENTED' if t90_model2 else 'M0 — SPECIFIED'
            },
            'model3_mechanistic_biochemical': {
                'description': 'Coupled hydration diffusion and pectin middle lamella solubilization',
                'status': model3_status,
                'k_softening_min^-1': round(k_soft_m3, 4) if k_soft_m3 else None,
                'predicted_t90_min': round(t90_model3, 2) if t90_model3 else None,
                'maturity_state': 'M0 — SPECIFIED'
            },
            'target_dal_validation_status': 'NOT_VALIDATED — PENDING_PHYSICAL_LABORATORY_ASSAYS'
        }
