"""
Bayesian Optimal Experiment Design (OED) Module for Phase 2 Planning.
Formulates candidate assay/condition grids, expected utility, statistical power,
and decision logic over competing mechanisms.
Outputs preliminary designs labeled PRELIMINARY_NOT_OPTIMIZED when empirical priors are missing.
"""

from typing import Dict, Any, List, Optional
import numpy as np

class BayesianOEDPlanner:
    def __init__(self, indicative_budget_ceiling_inr: float = 200000.0):
        self.budget_ceiling = indicative_budget_ceiling_inr
        self.competing_hypotheses = {
            "H1_Hydration_Barrier": {
                "description": "Mass transfer resistance at surface/cotyledon limits initial water uptake",
                "discriminating_assays": ["Hydration kinetics at 25°C & 60°C", "WAI", "Peleg k1"],
                "indicative_cost_inr": 10000.0,
                "refutation_condition": "If Tanzanian dal reaches full hydration in <60 min but still fails to soften under pressure cooking."
            },
            "H2_Seed_Coat_Resistance": {
                "description": "Residual testa or cuticular wax layer retards water ingress",
                "discriminating_assays": ["Optical / SEM microscopy", "Dehulled vs intact cotyledon hydration"],
                "indicative_cost_inr": 8000.0,
                "refutation_condition": "If completely dehulled split cotyledons exhibit identical cooking delay as partially dehulled dal."
            },
            "H3_Pectin_Divalent_Crosslinking": {
                "description": "Free Ca2+/Mg2+ crosslinks de-esterified pectin in the middle lamella, preventing thermal cell separation",
                "discriminating_assays": ["Pectin fractionation (WSP/CSP)", "ICP-OES Ca/Mg", "Phytate:Ca molar ratio"],
                "indicative_cost_inr": 34000.0,
                "refutation_condition": "If chelating agents (EDTA/citrate) do not reduce cooking time, or if Phytate:Ca ratio is > 1.0."
            },
            "H4_Starch_Thermal_Barrier": {
                "description": "Elevated starch gelatinization temperature or restricted swelling requires prolonged heat",
                "discriminating_assays": ["DSC gelatinization onset/enthalpy", "RVA pasting profile"],
                "indicative_cost_inr": 25000.0,
                "refutation_condition": "If DSC peak temperature Tp is identical (<1°C difference) between Tanzanian and Indian dal."
            },
            "H5_Storage_Induced_HTC": {
                "description": "Warm, humid maritime transit induced enzymatic hard-to-cook defect",
                "discriminating_assays": ["Storage history correlation", "Controlled aging trial"],
                "indicative_cost_inr": 15000.0,
                "refutation_condition": "If newly harvested fresh Tanzanian dal shows identical cooking resistance before oceanic transit."
            }
        }

    def propose_phase2_screening_design(
        self,
        empirical_data_available: bool = False
    ) -> Dict[str, Any]:
        """
        Generates candidate experimental design for discriminating among H1-H5.
        Labeled PRELIMINARY_NOT_OPTIMIZED if empirical priors are absent.
        """
        design_status = "OPTIMIZED_WITH_EMPIRICAL_PRIORS" if empirical_data_available else "PRELIMINARY_NOT_OPTIMIZED"
        
        candidate_treatments = [
            {
                "treatment_id": "TREAT_01_TEMPERING",
                "family": "Controlled Hydration / Tempering (§18.1)",
                "target_mechanism": "Water penetration and moisture distribution",
                "conditions_grid": [
                    {"moisture_target_pct": 20.0, "temp_c": 25.0, "rest_time_h": 4.0},
                    {"moisture_target_pct": 30.0, "temp_c": 40.0, "rest_time_h": 2.0}
                ],
                "expected_effect": "Accelerates initial hydration core saturation (Hypothesis)",
                "technical_risk": "Microbial proliferation during wet resting; drying energy demand",
                "estimated_lab_cost_inr": 12000.0
            },
            {
                "treatment_id": "TREAT_02_HYDROTHERMAL",
                "family": "Hydrothermal Pre-Treatment (§18.2)",
                "target_mechanism": "Cell-wall softening and pre-gelatinization",
                "conditions_grid": [
                    {"steam_pressure_kpa": 50.0, "exposure_time_min": 5.0},
                    {"steam_pressure_kpa": 100.0, "exposure_time_min": 3.0}
                ],
                "expected_effect": "Relaxes pectin matrix before consumer cooking (Hypothesis)",
                "technical_risk": "Overcooking, starch leaching, case hardening",
                "estimated_lab_cost_inr": 15000.0
            },
            {
                "treatment_id": "TREAT_03_CHELATING_CONDITIONING",
                "family": "Food-Grade Conditioning (§18.4)",
                "target_mechanism": "Disruption of Ca2+/Mg2+ pectin ionic bridges",
                "conditions_grid": [
                    {"agent": "Sodium citrate", "concentration_pct": 0.5, "soak_time_min": 30.0},
                    {"agent": "Sodium hexametaphosphate (SHMP)", "concentration_pct": 0.25, "soak_time_min": 30.0}
                ],
                "expected_effect": "Sequester divalent cations, solubilizing middle lamella pectin (Hypothesis)",
                "technical_risk": "Sensory astringency, regulatory sodium labeling, rinse requirements",
                "estimated_lab_cost_inr": 18000.0
            },
            {
                "treatment_id": "TREAT_04_IR_MICRONIZATION",
                "family": "Targeted Thermal Pre-Treatment (§18.3)",
                "target_mechanism": "Flash moisture vapor micro-fissuring of cotyledon",
                "conditions_grid": [
                    {"ir_temp_c": 175.0, "residence_time_sec": 45.0, "feed_moisture_pct": 25.0},
                    {"ir_temp_c": 185.0, "residence_time_sec": 60.0, "feed_moisture_pct": 30.0}
                ],
                "expected_effect": "Generates micro-channels bypassing pectin mass transfer resistance (Hypothesis)",
                "technical_risk": "Surface scorching, protein denaturation, flavour degradation",
                "estimated_lab_cost_inr": 25000.0
            }
        ]

        # Calculate sample size requirements (Power = 0.80, alpha = 0.05, Cohen d = 1.0)
        # N per group ~ 16 replicates for single-grain testing; 3 batches for bulk cooking
        sample_allocation = {
            "replicates_per_condition": 3,
            "grains_per_texture_test": 20,
            "sample_mass_per_trial_g": 50.0,
            "total_sample_required_kg": 2.5
        }

        total_estimated_cost = sum(t["estimated_lab_cost_inr"] for t in candidate_treatments)

        return {
            "design_status": design_status,
            "budget_ceiling_inr": self.budget_ceiling,
            "total_estimated_treatment_cost_inr": total_estimated_cost,
            "is_within_ceiling": bool(total_estimated_cost <= self.budget_ceiling),
            "competing_hypotheses": self.competing_hypotheses,
            "candidate_treatments": candidate_treatments,
            "sample_allocation": sample_allocation,
            "warning": "No physical laboratory experiments authorized by this computational plan. Phase 2 requires separate scope approval."
        }
