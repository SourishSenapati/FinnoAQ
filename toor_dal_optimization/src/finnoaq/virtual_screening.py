"""
Five-Layer Computational Screening and Multi-Objective Pareto Optimization Engine.
Eliminates unfeasible, unsafe, and economically unviable pulse processing candidates
prior to laboratory and pilot expenditure.
"""

import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import numpy as np

from src.finnoaq.foodoscope import FoodoscopeInformaticsEngine

@dataclass
class CandidateTreatment:
    treatment_id: str
    family_name: str
    description: str
    conditioning_agent: str
    temperature_c: float
    duration_min: float
    moisture_added_pct: float
    drying_temperature_c: float
    estimated_opex_inr_per_kg: float
    estimated_capex_lakhs: float
    fssai_compliant: bool
    requires_additive_approval: bool
    uncertainty_level: str  # "LOW", "MEDIUM", "HIGH"

@dataclass
class ScreeningResult:
    treatment_id: str
    survived: bool
    rejected_at_layer: Optional[str]
    rejection_reason: Optional[str]
    predicted_whistles: float
    cooking_time_reduction_pct: float
    predicted_firmness_n: float
    sensory_hedonic_score: float
    available_lysine_retention_pct: float
    opex_inr_per_kg: float
    process_yield_pct: float
    robustness_score: float
    is_pareto_optimal: bool = False

class VirtualScreeningPipeline:
    """
    5-Layer Hierarchical Screening and Pareto Multi-Objective Optimization.
    """

    def __init__(self):
        self.foodoscope = FoodoscopeInformaticsEngine()

    def generate_candidate_design_space(self) -> List[CandidateTreatment]:
        """
        Generates structured candidate space across the 8 technical families
        outlined in the Master Prompt and SOW.
        """
        candidates: List[CandidateTreatment] = []
        
        # Family 1: Thermal & Tempering Optimization
        for temp in [60.0, 75.0, 90.0, 110.0, 140.0]:
            for dur in [15.0, 30.0, 60.0]:
                cid = f"F1_THERMAL_T{int(temp)}_D{int(dur)}"
                candidates.append(CandidateTreatment(
                    treatment_id=cid,
                    family_name="Thermal & Tempering Optimization",
                    description=f"Controlled convective thermal conditioning at {temp}C for {dur} min",
                    conditioning_agent="None (Dry/Tempered Air)",
                    temperature_c=temp,
                    duration_min=dur,
                    moisture_added_pct=2.0,
                    drying_temperature_c=55.0,
                    estimated_opex_inr_per_kg=0.35 + (temp / 100.0) * 0.25,
                    estimated_capex_lakhs=4.5,
                    fssai_compliant=True,
                    requires_additive_approval=False,
                    uncertainty_level="LOW"
                ))

        # Family 2: Moisture Conditioning & Controlled Hydration
        for soak_time in [20.0, 45.0, 90.0, 180.0]:
            for soak_temp in [25.0, 45.0, 65.0]:
                cid = f"F2_HYDRATION_S{int(soak_time)}_T{int(soak_temp)}"
                candidates.append(CandidateTreatment(
                    treatment_id=cid,
                    family_name="Moisture Conditioning & Controlled Hydration",
                    description=f"Controlled hydration at {soak_temp}C for {soak_time} min followed by gentle drying",
                    conditioning_agent="Potable Water",
                    temperature_c=soak_temp,
                    duration_min=soak_time,
                    moisture_added_pct=15.0 + soak_time * 0.1,
                    drying_temperature_c=50.0,
                    estimated_opex_inr_per_kg=0.60 + (soak_temp / 50.0) * 0.30,
                    estimated_capex_lakhs=6.0,
                    fssai_compliant=True,
                    requires_additive_approval=False,
                    uncertainty_level="LOW"
                ))

        # Family 3: Mineral Chelation & Salt Conditioning
        for salt, opex_base, approved in [
            ("Sodium Bicarbonate (NaHCO3, 0.5%)", 0.45, True),
            ("Sodium Tripolyphosphate (STPP, 0.3%)", 0.65, True),
            ("Potassium Carbonate (K2CO3, 0.4%)", 0.55, True),
            ("EDTA Chelator (Prohibited for Raw Pulses)", 0.40, False),  # Test rejection gate
            ("Citric Acid / Sodium Citrate Buffer (0.5%)", 0.70, True)
        ]:
            for temp in [40.0, 60.0]:
                cid = f"F3_MINERAL_{salt[:4].replace(' ', '_').upper()}_T{int(temp)}"
                candidates.append(CandidateTreatment(
                    treatment_id=cid,
                    family_name="Mineral Chelation & Salt Conditioning",
                    description=f"Mineral conditioning using {salt} at {temp}C",
                    conditioning_agent=salt,
                    temperature_c=temp,
                    duration_min=30.0,
                    moisture_added_pct=12.0,
                    drying_temperature_c=50.0,
                    estimated_opex_inr_per_kg=opex_base,
                    estimated_capex_lakhs=5.0,
                    fssai_compliant=approved,
                    requires_additive_approval=not approved,
                    uncertainty_level="MEDIUM"
                ))

        # Family 4: High-Temperature Short-Time (HTST) Micronization / Infrared
        for ir_temp in [120.0, 150.0, 185.0, 240.0]:  # 240C triggers scorching rejection
            for ir_sec in [30.0, 60.0, 90.0]:
                cid = f"F4_IR_MICRON_T{int(ir_temp)}_S{int(ir_sec)}"
                candidates.append(CandidateTreatment(
                    treatment_id=cid,
                    family_name="Infrared Micronization & HTST",
                    description=f"Catalytic infrared radiant conditioning at {ir_temp}C for {ir_sec} seconds",
                    conditioning_agent="Radiant Infrared Flux",
                    temperature_c=ir_temp,
                    duration_min=ir_sec / 60.0,
                    moisture_added_pct=4.0,  # Pre-tempered
                    drying_temperature_c=45.0,
                    estimated_opex_inr_per_kg=0.85 + (ir_temp / 200.0) * 0.40,
                    estimated_capex_lakhs=18.0,
                    fssai_compliant=True,
                    requires_additive_approval=False,
                    uncertainty_level="MEDIUM"
                ))

        # Family 5: Ultrasonic & Cavitation Pre-treatment
        for freq in [28.0, 40.0]:
            cid = f"F5_ULTRASONIC_{int(freq)}KHZ"
            candidates.append(CandidateTreatment(
                treatment_id=cid,
                family_name="Ultrasonic & Acoustic Cavitation",
                description=f"Sonication at {freq} kHz to induce micro-porosity in middle lamella",
                conditioning_agent="Potable Water + Acoustic Field",
                temperature_c=40.0,
                duration_min=20.0,
                moisture_added_pct=14.0,
                drying_temperature_c=50.0,
                estimated_opex_inr_per_kg=1.40,
                estimated_capex_lakhs=22.0,
                fssai_compliant=True,
                requires_additive_approval=False,
                uncertainty_level="HIGH"  # Ideal target for OED exploration
            ))

        # Family 6: Vacuum Hydration & De-aeration
        candidates.append(CandidateTreatment(
            treatment_id="F6_VACUUM_HYDRATION_01",
            family_name="Vacuum Hydration & Pressure Cycling",
            description="Pulsed vacuum infiltration (-0.08 MPa) to accelerate interstitial hydration",
            conditioning_agent="Potable Water under Vacuum",
            temperature_c=45.0,
            duration_min=15.0,
            moisture_added_pct=16.0,
            drying_temperature_c=50.0,
            estimated_opex_inr_per_kg=0.95,
            estimated_capex_lakhs=14.0,
            fssai_compliant=True,
            requires_additive_approval=False,
            uncertainty_level="MEDIUM"
        ))

        # Family 7: Controlled Enzymatic Conditioning (Pectinase / Cellulase)
        for dose in [0.05, 0.15, 0.50]:
            cid = f"F7_ENZYME_PECTINASE_D{int(dose*100)}"
            candidates.append(CandidateTreatment(
                treatment_id=cid,
                family_name="Enzymatic Biocatalytic Conditioning",
                description=f"Targeted pectin lyase / polygalacturonase incubation at {dose}% dose",
                conditioning_agent="Food-Grade Pectinase",
                temperature_c=50.0,
                duration_min=45.0,
                moisture_added_pct=18.0,
                drying_temperature_c=50.0,
                estimated_opex_inr_per_kg=1.80 + dose * 2.0,
                estimated_capex_lakhs=8.0,
                fssai_compliant=True,
                requires_additive_approval=False,
                uncertainty_level="HIGH"
            ))

        # Family 8: Superheated Steam & Controlled Flash Expansion
        for steam_p in [0.15, 0.30, 0.65]:  # 0.65 MPa triggers pressure safety limit
            cid = f"F8_STEAM_FLASH_P{int(steam_p*100)}"
            candidates.append(CandidateTreatment(
                treatment_id=cid,
                family_name="Superheated Steam & Flash Conditioning",
                description=f"Saturated steam conditioning at {steam_p} MPa followed by rapid de-pressurization",
                conditioning_agent="Culinary Steam",
                temperature_c=120.0 + steam_p * 50.0,
                duration_min=3.0,
                moisture_added_pct=6.0,
                drying_temperature_c=50.0,
                estimated_opex_inr_per_kg=1.10,
                estimated_capex_lakhs=25.0,
                fssai_compliant=True,
                requires_additive_approval=False,
                uncertainty_level="MEDIUM"
            ))

        return candidates

    def screen_and_optimize(
        self,
        candidates: Optional[List[CandidateTreatment]] = None
    ) -> List[ScreeningResult]:
        """
        Executes 5-layer computational screening and Pareto multi-objective ranking.
        """
        if candidates is None:
            candidates = self.generate_candidate_design_space()

        results: List[ScreeningResult] = []

        for cand in candidates:
            # -----------------------------------------------------------------
            # LAYER 1: Hard Constraints Screening
            # -----------------------------------------------------------------
            if not cand.fssai_compliant:
                results.append(ScreeningResult(
                    treatment_id=cand.treatment_id,
                    survived=False,
                    rejected_at_layer="Layer 1: Hard Constraints",
                    rejection_reason=f"Prohibited food additive / regulatory non-compliance: {cand.conditioning_agent}",
                    predicted_whistles=6.0,
                    cooking_time_reduction_pct=0.0,
                    predicted_firmness_n=32.0,
                    sensory_hedonic_score=1.0,
                    available_lysine_retention_pct=95.0,
                    opex_inr_per_kg=cand.estimated_opex_inr_per_kg,
                    process_yield_pct=98.0,
                    robustness_score=0.0
                ))
                continue

            if cand.temperature_c > 220.0:
                results.append(ScreeningResult(
                    treatment_id=cand.treatment_id,
                    survived=False,
                    rejected_at_layer="Layer 1: Hard Constraints",
                    rejection_reason=f"Thermal threshold breach: {cand.temperature_c}C causes severe grain scorching and pyrolysis",
                    predicted_whistles=6.0,
                    cooking_time_reduction_pct=0.0,
                    predicted_firmness_n=35.0,
                    sensory_hedonic_score=1.0,
                    available_lysine_retention_pct=40.0,
                    opex_inr_per_kg=cand.estimated_opex_inr_per_kg,
                    process_yield_pct=85.0,
                    robustness_score=0.0
                ))
                continue

            # Pressure vessel limit for atmospheric mill retrofits
            if cand.family_name == "Superheated Steam & Flash Conditioning" and cand.temperature_c > 150.0:
                results.append(ScreeningResult(
                    treatment_id=cand.treatment_id,
                    survived=False,
                    rejected_at_layer="Layer 1: Hard Constraints",
                    rejection_reason="Excessive steam pressure (> 0.5 MPa) exceeds mill safety design envelope",
                    predicted_whistles=6.0,
                    cooking_time_reduction_pct=0.0,
                    predicted_firmness_n=25.0,
                    sensory_hedonic_score=5.0,
                    available_lysine_retention_pct=80.0,
                    opex_inr_per_kg=cand.estimated_opex_inr_per_kg,
                    process_yield_pct=94.0,
                    robustness_score=0.0
                ))
                continue

            # -----------------------------------------------------------------
            # LAYER 2: Scientific & Transport Bounds Screening
            # -----------------------------------------------------------------
            # Saturated holding capacity constraint: moisture added must not exceed 35% without slurry formation
            if cand.moisture_added_pct > 30.0:
                results.append(ScreeningResult(
                    treatment_id=cand.treatment_id,
                    survived=False,
                    rejected_at_layer="Layer 2: Transport & Material Bounds",
                    rejection_reason=f"Moisture loading ({cand.moisture_added_pct}%) exceeds cotyledon holding capacity, causing slurry formation",
                    predicted_whistles=5.0,
                    cooking_time_reduction_pct=15.0,
                    predicted_firmness_n=18.0,
                    sensory_hedonic_score=4.0,
                    available_lysine_retention_pct=90.0,
                    opex_inr_per_kg=cand.estimated_opex_inr_per_kg,
                    process_yield_pct=82.0,
                    robustness_score=0.1
                ))
                continue

            # -----------------------------------------------------------------
            # LAYER 3: Soft Predictive Screening (Cooking, Flavor & Sensory)
            # -----------------------------------------------------------------
            # Calculate cooking time reduction based on mechanism:
            # Baseline whistles for Tanzanian dal = 6.0
            reduction_factor = 0.0
            if "IR_MICRON" in cand.treatment_id:
                # Rapid fissuring + starch pre-gelatinization
                reduction_factor = min(0.55, 0.15 + (cand.temperature_c / 185.0) * 0.35)
            elif "MINERAL" in cand.treatment_id:
                # Pectin de-esterification / Na+ exchange displacing Ca2+
                reduction_factor = 0.45
            elif "HYDRATION" in cand.treatment_id:
                # Controlled pre-swelling
                reduction_factor = min(0.40, 0.10 + (cand.duration_min / 90.0) * 0.25)
            elif "ULTRASONIC" in cand.treatment_id:
                reduction_factor = 0.38
            elif "ENZYME" in cand.treatment_id:
                reduction_factor = 0.48
            elif "STEAM" in cand.treatment_id:
                reduction_factor = 0.42
            else:
                reduction_factor = 0.15

            predicted_whistles = max(2.5, round(6.0 * (1.0 - reduction_factor), 1))
            cooking_time_red_pct = round(reduction_factor * 100.0, 1)

            # Texture firmness after standard cooking:
            # Firmness decreases proportionally to cooking ease (Benchmark Indian dal = 20-22 N)
            predicted_firmness = max(18.0, round(34.0 - reduction_factor * 26.0, 1))

            # Simulate volatile flavor kinetics and nutrient retention via Foodoscope
            flavor_kinetics = self.foodoscope.simulate_thermal_flavor_and_nutrient_kinetics(
                treatment_temperature_c=cand.temperature_c,
                treatment_duration_min=cand.duration_min,
                moisture_content_pct=12.0 + cand.moisture_added_pct
            )

            # Available Lysine Retention
            lysine_ret = flavor_kinetics["available_lysine_retention_pct"]
            if lysine_ret < 82.0:
                results.append(ScreeningResult(
                    treatment_id=cand.treatment_id,
                    survived=False,
                    rejected_at_layer="Layer 3: Predictive Nutritional Integrity",
                    rejection_reason=f"Severe available lysine loss (retention {lysine_ret}% < 82% target threshold)",
                    predicted_whistles=predicted_whistles,
                    cooking_time_reduction_pct=cooking_time_red_pct,
                    predicted_firmness_n=predicted_firmness,
                    sensory_hedonic_score=5.5,
                    available_lysine_retention_pct=lysine_ret,
                    opex_inr_per_kg=cand.estimated_opex_inr_per_kg,
                    process_yield_pct=96.0,
                    robustness_score=0.2
                ))
                continue

            # Sensory Hedonic Score
            sensory = self.foodoscope.compute_sensory_hedonic_score(
                texture_firmness_n=predicted_firmness,
                hard_core_pct=max(0.0, (predicted_whistles - 3.2) * 5.0),
                flavor_kinetics=flavor_kinetics
            )
            hedonic_score = sensory["overall_hedonic_score_9pt"]

            # -----------------------------------------------------------------
            # LAYER 4: Techno-Economic & Manufacturing Screening
            # -----------------------------------------------------------------
            # OPEX limit: commercial ceiling is INR 2.50 per kg
            if cand.estimated_opex_inr_per_kg > 2.50:
                results.append(ScreeningResult(
                    treatment_id=cand.treatment_id,
                    survived=False,
                    rejected_at_layer="Layer 4: Techno-Economics",
                    rejection_reason=f"OPEX (INR {cand.estimated_opex_inr_per_kg:.2f}/kg) exceeds commercial feasibility threshold (INR 2.50/kg)",
                    predicted_whistles=predicted_whistles,
                    cooking_time_reduction_pct=cooking_time_red_pct,
                    predicted_firmness_n=predicted_firmness,
                    sensory_hedonic_score=hedonic_score,
                    available_lysine_retention_pct=lysine_ret,
                    opex_inr_per_kg=cand.estimated_opex_inr_per_kg,
                    process_yield_pct=98.0,
                    robustness_score=0.4
                ))
                continue

            # Process yield: fines / broken grain loss during conditioning & drying
            loss_pct = 0.5 + (cand.moisture_added_pct * 0.05) + (cand.temperature_c > 120.0) * 0.8
            yield_pct = round(100.0 - loss_pct, 2)

            # -----------------------------------------------------------------
            # LAYER 5: Robustness Across Lot Variations
            # -----------------------------------------------------------------
            # Uncertainty awareness: high uncertainty does not automatically reject if high gain!
            robustness = 0.85
            if cand.uncertainty_level == "HIGH":
                robustness = 0.65  # Flagged for OED targeted physical testing
            elif cand.uncertainty_level == "LOW":
                robustness = 0.95

            # SURVIVED ALL 5 LAYERS
            results.append(ScreeningResult(
                treatment_id=cand.treatment_id,
                survived=True,
                rejected_at_layer=None,
                rejection_reason=None,
                predicted_whistles=predicted_whistles,
                cooking_time_reduction_pct=cooking_time_red_pct,
                predicted_firmness_n=predicted_firmness,
                sensory_hedonic_score=hedonic_score,
                available_lysine_retention_pct=lysine_ret,
                opex_inr_per_kg=round(cand.estimated_opex_inr_per_kg, 2),
                process_yield_pct=yield_pct,
                robustness_score=robustness
            ))

        # ---------------------------------------------------------------------
        # MULTI-OBJECTIVE PARETO OPTIMIZATION ON SURVIVORS
        # Objectives:
        # 1. Minimize predicted_whistles (lower is better)
        # 2. Maximize sensory_hedonic_score (higher is better)
        # 3. Minimize opex_inr_per_kg (lower is better)
        # 4. Maximize available_lysine_retention_pct (higher is better)
        # ---------------------------------------------------------------------
        survivors = [r for r in results if r.survived]
        for s in survivors:
            is_dominated = False
            for other in survivors:
                if other.treatment_id == s.treatment_id:
                    continue
                # other dominates s if other is <= on min objectives and >= on max objectives, and strictly better on at least one
                better_or_equal = (
                    other.predicted_whistles <= s.predicted_whistles and
                    other.sensory_hedonic_score >= s.sensory_hedonic_score and
                    other.opex_inr_per_kg <= s.opex_inr_per_kg and
                    other.available_lysine_retention_pct >= s.available_lysine_retention_pct
                )
                strictly_better = (
                    other.predicted_whistles < s.predicted_whistles or
                    other.sensory_hedonic_score > s.sensory_hedonic_score or
                    other.opex_inr_per_kg < s.opex_inr_per_kg or
                    other.available_lysine_retention_pct > s.available_lysine_retention_pct
                )
                if better_or_equal and strictly_better:
                    is_dominated = True
                    break
            s.is_pareto_optimal = not is_dominated

        return results
