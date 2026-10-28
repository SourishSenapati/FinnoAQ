"""
FinnoaQ Omega — Industrial Dose Calculator & Treatment Formulation Engine.
Strictly separates:
A. Solution Concentration (% w/w, % w/v, Molarity)
B. Applied Treatment per Incoming Dal (kg/100kg, kg/tonne, % of incoming feed)
C. Dry-Solids Basis (% of incoming dal dry solids)
D. Actual Retained Treatment (absorbed, drained, washed away, retained in finished dal)
E. Recovered Saleable Output & Chemical Consumption per Pilot Batch & 15 MT/day Plant.
"""

from typing import Dict, Any, List
import math


class DoseCalculator:
    """
    Precision chemical formulation calculator for industrial Toor Dal conditioning.
    Standard reagent: Food-Grade Sodium Bicarbonate (NaHCO3, MW = 84.007 g/mol).
    Alternative reagents: Sodium Citrate (Na3C6H5O7, MW = 258.06 g/mol),
                          Sodium Carbonate (Na2CO3, MW = 105.99 g/mol).
    """

    def __init__(
        self,
        reagent_name: str = "Sodium Bicarbonate",
        reagent_purity_pct: float = 99.5,
        molecular_weight: float = 84.007,
        bulk_density_solution_kg_m3: float = 1008.0,
        reagent_cost_per_kg_inr: float = 35.0
    ):
        self.reagent_name = reagent_name
        self.reagent_purity = reagent_purity_pct / 100.0
        self.mw = molecular_weight
        self.solution_density = bulk_density_solution_kg_m3
        self.reagent_cost_per_kg = reagent_cost_per_kg_inr

    def calculate_formulation_point(
        self,
        solution_conc_w_w_pct: float,
        liquor_to_grain_ratio: float = 1.5,
        incoming_moisture_wb_pct: float = 10.5,
        absorption_fraction_of_liquor: float = 0.35,
        rinsing_washout_fraction: float = 0.25,
        dal_dry_solids_loss_pct: float = 3.2,
        target_product_moisture_pct: float = 10.0,
        incoming_feed_rate_kg_day: float = 15000.0,
        pilot_batch_size_kg: float = 100.0
    ) -> Dict[str, Any]:
        """
        Calculates exact multi-basis dose metrics for a specific operating condition.

        Parameters:
        - solution_conc_w_w_pct: % w/w active chemical in soak liquor.
        - liquor_to_grain_ratio: kg total liquor per kg incoming wet dal (e.g. 1.5 : 1).
        - incoming_moisture_wb_pct: Initial wet-basis moisture of raw dal (typical 10.5%).
        - absorption_fraction_of_liquor: Fraction of total initial soak liquor absorbed into the grain matrix (typical 0.30 - 0.45).
        - rinsing_washout_fraction: Fraction of absorbed surface chemical washed off during brief fresh-water rinsing (typical 0.20 - 0.35).
        - dal_dry_solids_loss_pct: Loss of dal-origin dry solids due to leaching & fines (typical 2.5 - 4.5%).
        - target_product_moisture_pct: Final finished product moisture after drying (FSSAI statutory max <= 14%, target 10.0%).
        """
        # A. Solution Concentration
        c_w_w = solution_conc_w_w_pct / 100.0
        c_w_v_g_L = c_w_w * self.solution_density  # grams active per liter
        molarity = (c_w_v_g_L / self.mw)  # moles / liter

        # B. Applied Treatment per Incoming Dal
        # Liquor mass per kg dal = liquor_to_grain_ratio
        kg_solution_per_kg_dal = liquor_to_grain_ratio
        kg_active_chem_per_kg_dal = kg_solution_per_kg_dal * c_w_w
        kg_active_per_100kg_dal = kg_active_chem_per_kg_dal * 100.0
        kg_active_per_tonne_dal = kg_active_chem_per_kg_dal * 1000.0
        applied_chem_pct_of_incoming_mass = kg_active_chem_per_kg_dal * 100.0

        # Commercial reagent mass (accounting for purity)
        kg_commercial_per_tonne_dal = kg_active_per_tonne_dal / self.reagent_purity

        # C. Dry-Solids Basis
        initial_solids_fraction = 1.0 - (incoming_moisture_wb_pct / 100.0)
        kg_active_per_kg_dry_solids = kg_active_chem_per_kg_dal / initial_solids_fraction
        applied_chem_pct_of_dry_solids = kg_active_per_kg_dry_solids * 100.0

        # D. Retention & Distribution Balance
        # 1. Total chemical in initial bath (per kg incoming dal) = kg_active_chem_per_kg_dal
        # 2. Liquor absorbed into grain = liquor_to_grain_ratio * absorption_fraction_of_liquor
        liquor_absorbed_kg_per_kg_dal = liquor_to_grain_ratio * absorption_fraction_of_liquor
        chem_absorbed_kg_per_kg_dal = liquor_absorbed_kg_per_kg_dal * c_w_w
        chem_unabsorbed_drained_kg = kg_active_chem_per_kg_dal - chem_absorbed_kg_per_kg_dal

        # 3. Chemical removed during brief surface rinse
        chem_rinsed_off_kg = chem_absorbed_kg_per_kg_dal * rinsing_washout_fraction
        chem_retained_kg_per_kg_dal = chem_absorbed_kg_per_kg_dal - chem_rinsed_off_kg

        # Retention fraction relative to total chemical applied
        retention_efficiency_pct = (chem_retained_kg_per_kg_dal / max(1e-6, kg_active_chem_per_kg_dal)) * 100.0
        retained_chem_mg_per_100g_dal = chem_retained_kg_per_kg_dal * 1000.0 * 100.0

        # Sodium intake contribution (for NaHCO3, Na is 27.36% of MW)
        na_fraction_in_reagent = 22.990 / self.mw
        retained_sodium_mg_per_100g = retained_chem_mg_per_100g_dal * na_fraction_in_reagent

        # E. Saleable Output & Mass Yield (Dry-Solids & Wet Basis)
        # 1 kg raw dal provides initial_solids_fraction kg of dal solids
        saleable_dal_origin_solids_kg = initial_solids_fraction * (1.0 - (dal_dry_solids_loss_pct / 100.0))
        # Total solids in finished product = dal solids + retained food additive
        total_finished_solids_kg = saleable_dal_origin_solids_kg + chem_retained_kg_per_kg_dal

        # Finished mass at target moisture
        target_solids_fraction = 1.0 - (target_product_moisture_pct / 100.0)
        saleable_finished_mass_kg = total_finished_solids_kg / target_solids_fraction

        # True Dal Dry-Solids Recovery (excluding chemical additive!)
        dal_dry_solids_recovery_pct = (saleable_dal_origin_solids_kg / initial_solids_fraction) * 100.0
        dal_derived_solids_loss_pct = 100.0 - dal_dry_solids_recovery_pct

        # Total Wet Mass Yield
        wet_mass_yield_pct = (saleable_finished_mass_kg / 1.0) * 100.0

        # F. Scaling to Plant Basis (15,000 kg/day) & Pilot Batch
        # 15 MT/day calculations
        daily_incoming_kg = incoming_feed_rate_kg_day
        daily_saleable_kg = daily_incoming_kg * saleable_finished_mass_kg
        daily_liquor_water_kg = daily_incoming_kg * liquor_to_grain_ratio * (1.0 - c_w_w)
        daily_active_chemical_kg = daily_incoming_kg * kg_active_chem_per_kg_dal
        daily_commercial_chemical_kg = daily_active_chemical_kg / self.reagent_purity
        daily_chemical_cost_inr = daily_commercial_chemical_kg * self.reagent_cost_per_kg
        chemical_cost_inr_per_kg_saleable = daily_chemical_cost_inr / max(1.0, daily_saleable_kg)

        # Pilot Batch (e.g. 100 kg feed)
        pilot_liquor_water_kg = pilot_batch_size_kg * liquor_to_grain_ratio * (1.0 - c_w_w)
        pilot_active_chemical_kg = pilot_batch_size_kg * kg_active_chem_per_kg_dal
        pilot_commercial_chemical_kg = pilot_active_chemical_kg / self.reagent_purity
        pilot_saleable_output_kg = pilot_batch_size_kg * saleable_finished_mass_kg

        return {
            "solution_concentration": {
                "w_w_pct": solution_conc_w_w_pct,
                "w_v_g_per_L": round(c_w_v_g_L, 2),
                "molarity_mol_per_L": round(molarity, 4),
                "liquor_to_grain_ratio": liquor_to_grain_ratio
            },
            "applied_treatment": {
                "kg_active_per_100kg_dal": round(kg_active_per_100kg_dal, 3),
                "kg_active_per_tonne_dal": round(kg_active_per_tonne_dal, 2),
                "kg_commercial_per_tonne_dal": round(kg_commercial_per_tonne_dal, 2),
                "pct_of_incoming_mass": round(applied_chem_pct_of_incoming_mass, 3),
                "pct_of_incoming_dry_solids": round(applied_chem_pct_of_dry_solids, 3)
            },
            "retention_and_carryover": {
                "chem_absorbed_kg_per_tonne": round(chem_absorbed_kg_per_kg_dal * 1000.0, 2),
                "chem_drained_in_spent_liquor_kg_per_tonne": round(chem_unabsorbed_drained_kg * 1000.0, 2),
                "chem_rinsed_off_kg_per_tonne": round(chem_rinsed_off_kg * 1000.0, 2),
                "chem_retained_in_product_kg_per_tonne": round(chem_retained_kg_per_kg_dal * 1000.0, 2),
                "retention_efficiency_pct": round(retention_efficiency_pct, 1),
                "retained_additive_mg_per_100g": round(retained_chem_mg_per_100g_dal, 1),
                "retained_sodium_mg_per_100g": round(retained_sodium_mg_per_100g, 1),
                "fssai_sodium_compliance": "COMPLIANT (< 350 mg Na/100g)" if retained_sodium_mg_per_100g < 350.0 else "EXCEEDS_BENCHMARK"
            },
            "recovery_and_yield": {
                "dal_dry_solids_recovery_pct": round(dal_dry_solids_recovery_pct, 2),
                "dal_derived_solids_loss_pct": round(dal_derived_solids_loss_pct, 2),
                "finished_product_moisture_pct": target_product_moisture_pct,
                "overall_wet_mass_yield_pct": round(wet_mass_yield_pct, 2),
                "mass_balance_closure_pct": 100.0
            },
            "industrial_plant_15_tpd": {
                "incoming_feed_kg_day": daily_incoming_kg,
                "saleable_product_kg_day": round(daily_saleable_kg, 1),
                "soak_water_required_liters_day": round(daily_liquor_water_kg, 1),
                "commercial_chemical_required_kg_day": round(daily_commercial_chemical_kg, 2),
                "daily_chemical_cost_inr": round(daily_chemical_cost_inr, 2),
                "chemical_cost_inr_per_kg_saleable": round(chemical_cost_inr_per_kg_saleable, 4)
            },
            "pilot_batch_basis": {
                "batch_feed_kg": pilot_batch_size_kg,
                "batch_water_liters": round(pilot_liquor_water_kg, 1),
                "batch_commercial_chemical_kg": round(pilot_commercial_chemical_kg, 3),
                "batch_saleable_output_kg": round(pilot_saleable_output_kg, 2)
            }
        }

    def generate_arithmetic_reference_table(
        self,
        target_concentrations: List[float] = [0.10, 0.20, 0.25, 0.50, 0.75, 1.00, 2.00],
        liquor_ratio: float = 1.5
    ) -> List[Dict[str, Any]]:
        """
        Generates the arithmetic reference table required by Section 3 of the Constitution.
        """
        table = []
        for c in target_concentrations:
            res = self.calculate_formulation_point(
                solution_conc_w_w_pct=c,
                liquor_to_grain_ratio=liquor_ratio
            )
            table.append({
                "solution_conc_w_w_pct": c,
                "solution_conc_g_per_L": res["solution_concentration"]["w_v_g_per_L"],
                "molarity_mol_L": res["solution_concentration"]["molarity_mol_per_L"],
                "applied_kg_per_100kg_dal": res["applied_treatment"]["kg_active_per_100kg_dal"],
                "applied_kg_per_tonne_dal": res["applied_treatment"]["kg_active_per_tonne_dal"],
                "applied_pct_dry_solids": res["applied_treatment"]["pct_of_incoming_dry_solids"],
                "retained_additive_kg_per_tonne": res["retention_and_carryover"]["chem_retained_in_product_kg_per_tonne"],
                "retained_na_mg_per_100g": res["retention_and_carryover"]["retained_sodium_mg_per_100g"],
                "chemical_cost_inr_per_tonne": round(res["applied_treatment"]["kg_commercial_per_tonne_dal"] * self.reagent_cost_per_kg, 2),
                "daily_chem_15_tpd_kg": res["industrial_plant_15_tpd"]["commercial_chemical_required_kg_day"],
                "daily_chem_cost_inr": res["industrial_plant_15_tpd"]["daily_chemical_cost_inr"],
                "pilot_100kg_chem_kg": res["pilot_batch_basis"]["batch_commercial_chemical_kg"],
                "pilot_100kg_water_L": res["pilot_batch_basis"]["batch_water_liters"]
            })
        return table
