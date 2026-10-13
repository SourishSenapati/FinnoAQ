"""
Foodoscope Computational Gastronomy and Flavor Informatics Engine for Pigeon Pea (Cajanus cajan).
Grounded in Foodoscope, FlavorDB, and Indian culinary recipe matrix pairing principles.
"""

import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

@dataclass
class VolatileCompound:
    name: str
    cas_number: str
    flavor_profile: List[str]
    threshold_ppm: float
    is_off_flavor: bool
    baseline_conc_ppm: float  # Baseline concentration in raw Tanzanian dal

@dataclass
class SpicePairingIngredient:
    name: str
    culinary_role: str
    key_compounds: List[str]
    pairing_synergy_score: float  # Foodoscope negative-pairing affinity

class FoodoscopeInformaticsEngine:
    """
    Computational gastronomy and culinary informatics engine for pulse R&D.
    Models volatile aroma chemistry, nutrient retention kinetics (lysine vs Maillard),
    and recipe matrix interactions (Sambar, Tadka Dal, Dal Makhani).
    """

    def __init__(self):
        # 1. Primary volatile aroma compounds of Cajanus cajan
        self.volatiles_db: Dict[str, VolatileCompound] = {
            "hexanal": VolatileCompound(
                name="Hexanal",
                cas_number="66-25-1",
                flavor_profile=["green", "beany", "grassy", "fatty"],
                threshold_ppm=0.005,
                is_off_flavor=True,
                baseline_conc_ppm=0.450
            ),
            "1_octen_3_ol": VolatileCompound(
                name="1-Octen-3-ol",
                cas_number="3391-86-4",
                flavor_profile=["mushroom", "earthy", "musty"],
                threshold_ppm=0.001,
                is_off_flavor=True,
                baseline_conc_ppm=0.085
            ),
            "2_pentylfuran": VolatileCompound(
                name="2-Pentylfuran",
                cas_number="3777-69-3",
                flavor_profile=["green bean", "metallic", "beany"],
                threshold_ppm=0.006,
                is_off_flavor=True,
                baseline_conc_ppm=0.120
            ),
            "trans_2_nonenal": VolatileCompound(
                name="trans-2-Nonenal",
                cas_number="18829-55-5",
                flavor_profile=["cardboard", "stale", "aged fatty"],
                threshold_ppm=0.0001,
                is_off_flavor=True,
                baseline_conc_ppm=0.015  # Elevated in aged Tanzanian dal (HTC marker)
            ),
            "2_5_dimethylpyrazine": VolatileCompound(
                name="2,5-Dimethylpyrazine",
                cas_number="123-32-0",
                flavor_profile=["roasted", "nutty", "toasted", "popcorn"],
                threshold_ppm=0.080,
                is_off_flavor=False,
                baseline_conc_ppm=0.010  # Low in raw dal, generated during thermal conditioning
            ),
            "methional": VolatileCompound(
                name="Methional",
                cas_number="3268-49-3",
                flavor_profile=["cooked potato", "savory", "soupy"],
                threshold_ppm=0.0002,
                is_off_flavor=False,
                baseline_conc_ppm=0.035
            ),
            "2_methylbutanal": VolatileCompound(
                name="2-Methylbutanal",
                cas_number="96-17-3",
                flavor_profile=["malty", "nutty", "cocoa"],
                threshold_ppm=0.001,
                is_off_flavor=False,
                baseline_conc_ppm=0.025
            )
        }

        # 2. Indian Culinary Matrix Pairing (Foodoscope Spice Network)
        self.culinary_pairings: Dict[str, SpicePairingIngredient] = {
            "turmeric": SpicePairingIngredient(
                name="Curcuma longa (Turmeric)",
                culinary_role="Colorant, earthy base, antioxidant",
                key_compounds=["curcumin", "ar-turmerone", "curlone"],
                pairing_synergy_score=0.92
            ),
            "cumin": SpicePairingIngredient(
                name="Cuminum cyminum (Jeera)",
                culinary_role="Warm aromatic tempering (tadka)",
                key_compounds=["cuminaldehyde", "cymene", "terpenes"],
                pairing_synergy_score=0.88
            ),
            "mustard_seeds": SpicePairingIngredient(
                name="Brassica nigra (Rai)",
                culinary_role="Pungent nutty crackle tempering",
                key_compounds=["allyl isothiocyanate", "sinigrin"],
                pairing_synergy_score=0.85
            ),
            "asafoetida": SpicePairingIngredient(
                name="Ferula foetida (Hing)",
                culinary_role="Sulfur savory depth, antiflatulent",
                key_compounds=["sec-butyl propenyl disulfide", "ferulic acid esters"],
                pairing_synergy_score=0.95
            ),
            "curry_leaves": SpicePairingIngredient(
                name="Murraya koenigii (Kadi Patta)",
                culinary_role="Citrus-herbal fresh finish",
                key_compounds=["caryophyllene", "pinene", "koenigine"],
                pairing_synergy_score=0.90
            ),
            "tamarind": SpicePairingIngredient(
                name="Tamarindus indica (Imli / Sambar acidulant)",
                culinary_role="Acidic broth matrix (pH 3.8 - 4.5)",
                key_compounds=["tartaric acid", "furfural", "phenylacetaldehyde"],
                pairing_synergy_score=0.78  # Challenges pectin solubilization if dal is unconditioned
            ),
            "tomato": SpicePairingIngredient(
                name="Solanum lycopersicum (Tomato)",
                culinary_role="Umami acidity in Dal Tadka (pH 4.2 - 4.6)",
                key_compounds=["citric acid", "glutamic acid", "hexenal"],
                pairing_synergy_score=0.82
            )
        }

    def simulate_thermal_flavor_and_nutrient_kinetics(
        self,
        treatment_temperature_c: float,
        treatment_duration_min: float,
        moisture_content_pct: float
    ) -> Dict[str, Any]:
        """
        Simulates lipoxygenase (LOX) inactivation, off-flavor reduction,
        Maillard pyrazine generation, and available lysine retention.
        
        Kinetic constants derived from pulse processing literature (Singh et al., Food Chem):
        - LOX Inactivation: Arrhenius Ea = 65.0 kJ/mol, D_75C = 1.2 min
        - Lysine Degradation: Arrhenius Ea = 88.0 kJ/mol, k0 = 4.5e8 min^-1
        """
        temp_k = treatment_temperature_c + 273.15
        r_gas = 8.314e-3  # kJ / (mol K)

        # 1. Lipoxygenase (LOX) Inactivation Kinetics
        # Reference at 75 C (348.15 K), k_ref = ln(10) / 1.2 = 1.919 min^-1
        ea_lox = 65.0  # kJ/mol
        t_ref_lox = 348.15
        k_lox_ref = 1.919
        k_lox = k_lox_ref * math.exp(-(ea_lox / r_gas) * (1.0 / temp_k - 1.0 / t_ref_lox))
        
        # Remaining LOX activity fraction
        lox_retention = math.exp(-k_lox * treatment_duration_min)
        lox_inactivation_pct = max(0.0, min(100.0, (1.0 - lox_retention) * 100.0))

        # 2. Hexanal & 1-Octen-3-ol off-flavor stripping / suppression
        # Thermal stripping + LOX inactivation
        hexanal_loss_rate = 0.05 * (treatment_temperature_c / 100.0) ** 1.5
        residual_hexanal = self.volatiles_db["hexanal"].baseline_conc_ppm * (
            0.15 + 0.85 * lox_retention
        ) * math.exp(-hexanal_loss_rate * treatment_duration_min)

        residual_octenol = self.volatiles_db["1_octen_3_ol"].baseline_conc_ppm * (
            0.20 + 0.80 * lox_retention
        ) * math.exp(-hexanal_loss_rate * 0.8 * treatment_duration_min)

        # Beany Off-Note Suppression Index (BOSI) [0.0 = severe beany, 1.0 = zero beany off-flavor]
        base_off = (
            self.volatiles_db["hexanal"].baseline_conc_ppm
            + 1.5 * self.volatiles_db["1_octen_3_ol"].baseline_conc_ppm
        )
        curr_off = residual_hexanal + 1.5 * residual_octenol
        bosi = max(0.0, min(1.0, 1.0 - (curr_off / base_off)))

        # 3. Maillard Roasted Aroma Formation (Pyrazines)
        # Threshold thermal activation at T > 95 C with sufficient moisture
        if treatment_temperature_c > 90.0 and moisture_content_pct > 8.0:
            rate_maillard = 0.00015 * math.exp(0.055 * (treatment_temperature_c - 90.0))
            pyrazine_conc = 0.010 + rate_maillard * treatment_duration_min * (moisture_content_pct / 15.0)
        else:
            pyrazine_conc = 0.010

        # Roasted Aroma Index (RAI) [0.0 = green/raw, 1.0 = rich nutty roasted benchmark]
        target_pyrazine = 0.150  # ppm
        rai = max(0.0, min(1.0, pyrazine_conc / target_pyrazine))

        # 4. Available Lysine Retention (Nutritional Quality Preservation)
        # Lysine loss accelerates at T > 115 C
        ea_lys = 88.0  # kJ/mol
        t_ref_lys = 373.15  # 100 C
        k_lys_ref = 0.00025  # min^-1 at 100 C
        k_lys = k_lys_ref * math.exp(-(ea_lys / r_gas) * (1.0 / temp_k - 1.0 / t_ref_lys))
        
        # Moisture accelerates Maillard loss of free amino groups
        moisture_factor = (moisture_content_pct / 12.0) ** 0.8
        lysine_retention_pct = max(50.0, min(100.0, math.exp(-k_lys * moisture_factor * treatment_duration_min) * 100.0))

        return {
            "temperature_c": treatment_temperature_c,
            "duration_min": treatment_duration_min,
            "moisture_pct": moisture_content_pct,
            "lox_inactivation_pct": round(lox_inactivation_pct, 2),
            "residual_hexanal_ppm": round(residual_hexanal, 4),
            "residual_1_octen_3_ol_ppm": round(residual_octenol, 4),
            "beany_off_note_suppression_index": round(bosi, 4),
            "pyrazine_concentration_ppm": round(pyrazine_conc, 4),
            "roasted_aroma_index": round(rai, 4),
            "available_lysine_retention_pct": round(lysine_retention_pct, 2)
        }

    def predict_recipe_matrix_performance(
        self,
        dal_treatment_profile: Dict[str, Any],
        cooking_media: str = "sambar_broth_acidic"
    ) -> Dict[str, Any]:
        """
        Simulates how conditioned dal behaves in specific Indian culinary recipes
        (e.g., Sambar with Tamarind pH 4.2 vs Neutral Dal Tadka pH 6.8).
        
        Acidic media binds pectin chains and inhibits solubilization unless
        the dal has received adequate hydrothermal or mineral conditioning.
        """
        media_specs = {
            "neutral_water": {"ph": 7.0, "calcium_ppm": 20.0, "acid_delay_factor": 1.0},
            "hard_water": {"ph": 7.8, "calcium_ppm": 220.0, "acid_delay_factor": 1.35},
            "dal_tadka_tomato": {"ph": 4.8, "calcium_ppm": 45.0, "acid_delay_factor": 1.25},
            "sambar_broth_acidic": {"ph": 4.1, "calcium_ppm": 60.0, "acid_delay_factor": 1.55}
        }

        spec = media_specs.get(cooking_media, media_specs["neutral_water"])
        
        # Base cooking whistles for Tanzanian dal
        base_whistles = 6.0
        
        # Conditioning reduction effect
        conditioning_reduction = dal_treatment_profile.get("cooking_time_reduction_pct", 0.0) / 100.0
        adjusted_whistles = base_whistles * (1.0 - conditioning_reduction)
        
        # Media impact
        final_whistles = adjusted_whistles * spec["acid_delay_factor"]
        
        # Hard core defect probability
        hard_core_risk_pct = max(
            2.0,
            (final_whistles / 6.0) * 35.0 * (1.0 if spec["ph"] > 5.5 else 1.8) * (1.0 - conditioning_reduction)
        )

        return {
            "cooking_media": cooking_media,
            "broth_ph": spec["ph"],
            "calcium_hardness_ppm": spec["calcium_ppm"],
            "predicted_pressure_cooker_whistles": round(final_whistles, 1),
            "hard_core_defect_risk_pct": round(min(100.0, hard_core_risk_pct), 1),
            "culinary_texture_rating": "Acceptable Soft Disintegration" if final_whistles <= 4.0 else "Incomplete Softening / Grainy Grittiness"
        }

    def compute_sensory_hedonic_score(
        self,
        texture_firmness_n: float,
        hard_core_pct: float,
        flavor_kinetics: Dict[str, Any],
        disintegration_index: float = 0.85
    ) -> Dict[str, Any]:
        """
        Computes 9-point Hedonic Sensory Acceptance Score:
        - Texture Score (35% weight): Penalizes firmness > 25 N and hard core > 5%
        - Aroma Score (25% weight): Rewards Roasted Aroma Index (RAI), rewards BOSI
        - Appearance/Disintegration Score (20% weight): Optimal at 0.75-0.90 (creamy broth)
        - Taste & Nutritional Profile (20% weight): Penalizes lysine loss < 85%
        """
        # 1. Texture Score (1 to 9)
        # Optimal benchmark firmness: 18 - 24 N, 0% hard core
        tex_penalty = max(0.0, (texture_firmness_n - 22.0) * 0.25) + (hard_core_pct * 0.40)
        tex_score = max(1.0, min(9.0, 8.5 - tex_penalty))

        # 2. Aroma Score (1 to 9)
        bosi = flavor_kinetics.get("beany_off_note_suppression_index", 0.5)
        rai = flavor_kinetics.get("roasted_aroma_index", 0.3)
        aroma_score = max(1.0, min(9.0, 4.0 + 3.0 * bosi + 2.0 * rai))

        # 3. Disintegration & Mouthfeel Score (1 to 9)
        # Ideal disintegration index between 0.70 and 0.90
        disint_dev = abs(disintegration_index - 0.82)
        disint_score = max(1.0, min(9.0, 8.8 - disint_dev * 15.0))

        # 4. Taste & Nutritional Score (1 to 9)
        lysine_ret = flavor_kinetics.get("available_lysine_retention_pct", 95.0)
        nutr_penalty = max(0.0, (95.0 - lysine_ret) * 0.15)
        taste_score = max(1.0, min(9.0, 8.5 - nutr_penalty))

        # Overall Weighted Acceptability
        overall_score = (
            0.35 * tex_score +
            0.25 * aroma_score +
            0.20 * disint_score +
            0.20 * taste_score
        )

        return {
            "overall_hedonic_score_9pt": round(overall_score, 2),
            "texture_score": round(tex_score, 2),
            "aroma_score": round(aroma_score, 2),
            "mouthfeel_score": round(disint_score, 2),
            "taste_nutrition_score": round(taste_score, 2),
            "commercial_sensory_tier": (
                "Premium Grade Benchmark (Equivalent to Indian Desi Dal)" if overall_score >= 7.8 else
                "Standard Commercial Grade" if overall_score >= 6.5 else
                "Substandard / Sensory Rework Required"
            )
        }
