"""
FinnoaQ Engineering Workspace — Deterministic Mass, Moisture, and Energy Balance Engine.
Project Reference: FNQ-PR-2026-001 | Toor Dal Cooking-Time Optimization
Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

This module implements first-principles mass, moisture, solids recovery, and thermal energy balances.
It strictly distinguishes:
1. Mathematical closure (conservation of mass: delta < 1e-9) from empirical validation.
2. Wet-basis moisture fraction (w) from dry-basis moisture ratio (X = w / (1 - w)).
3. Competing solids-loss assumptions: 184.00 kg/day (1.3706%) vs 196.01 kg/day (1.4600%).
4. Competing dryer-inlet scenarios: Scenario B1 (28.00% WB) vs Scenario B2 (18,590 kg/day, 28.7735% WB).
"""

import math
from typing import Dict, Any, Tuple, Optional

def wb_to_db(w: float) -> float:
    """Converts wet-basis moisture fraction w to dry-basis ratio X = w / (1 - w)."""
    if not (0.0 <= w < 1.0):
        raise ValueError(f"Wet-basis moisture fraction must be in [0.0, 1.0), got {w}")
    return w / (1.0 - w)

def db_to_wb(X: float) -> float:
    """Converts dry-basis moisture ratio X to wet-basis fraction w = X / (1 + X)."""
    if X < 0.0:
        raise ValueError(f"Dry-basis moisture ratio must be non-negative, got {X}")
    return X / (1.0 + X)

class DeterministicMassBalance:
    """
    Rigorous multi-stream material and moisture balance for 15,000 kg/day Toor Dal plant.
    """
    def __init__(
        self,
        raw_feed_kg_day: float = 15000.0,
        raw_moisture_wb: float = 0.105,
        target_product_moisture_wb: float = 0.100,
        solids_loss_kg_day: float = 184.0,
        operating_hours: float = 20.0
    ):
        if raw_feed_kg_day <= 0.0:
            raise ValueError("Raw feed mass must be strictly positive.")
        if not (0.0 < raw_moisture_wb < 1.0):
            raise ValueError("Raw feed moisture fraction must be between 0.0 and 1.0.")
        if not (0.0 < target_product_moisture_wb < 1.0):
            raise ValueError("Target product moisture fraction must be between 0.0 and 1.0.")
        if solids_loss_kg_day < 0.0:
            raise ValueError("Solids loss cannot be negative.")
        if operating_hours <= 0.0:
            raise ValueError("Operating hours must be strictly positive.")

        self.feed_total = raw_feed_kg_day
        self.w_in = raw_moisture_wb
        self.w_out = target_product_moisture_wb
        self.solids_loss = solids_loss_kg_day
        self.hours = operating_hours

        # Feed dry solids & water
        self.feed_dry_solids = self.feed_total * (1.0 - self.w_in)
        self.feed_water = self.feed_total * self.w_in

        if self.solids_loss > self.feed_dry_solids:
            raise ValueError(f"Solids loss ({self.solids_loss}) exceeds raw dry solids ({self.feed_dry_solids})")

        # Remaining dry solids to finished product
        self.product_dry_solids = self.feed_dry_solids - self.solids_loss

        # Finished product mass at target moisture
        # product_total = product_dry_solids / (1.0 - w_out)
        self.product_total = self.product_dry_solids / (1.0 - self.w_out)
        self.product_water = self.product_total * self.w_out

    def solve_scenario_b1(self, dryer_inlet_moisture_wb: float = 0.2800) -> Dict[str, Any]:
        """
        Scenario B1: Exactly 28.00% wet-basis moisture entering fluid bed dryer.
        Dryer-inlet wet mass is calculated directly from remaining dry solids.
        """
        if not (0.0 < dryer_inlet_moisture_wb < 1.0):
            raise ValueError("Dryer inlet moisture must be between 0.0 and 1.0")
        
        inlet_wb = dryer_inlet_moisture_wb
        dryer_inlet_total = self.product_dry_solids / (1.0 - inlet_wb)
        dryer_inlet_water = dryer_inlet_total * inlet_wb

        evaporation_kg_day = dryer_inlet_water - self.product_water
        evaporation_kg_h = evaporation_kg_day / self.hours

        # Mathematical closure across dryer
        mass_in = dryer_inlet_total
        mass_out = self.product_total + evaporation_kg_day
        closure_residual = abs(mass_in - mass_out)
        closure_error_pct = (closure_residual / mass_in) * 100.0

        return {
            'scenario_id': 'SCENARIO_B1_28_PCT_WB',
            'inlet_moisture_wb': inlet_wb,
            'inlet_moisture_db': wb_to_db(inlet_wb),
            'dryer_inlet_mass_kg_day': dryer_inlet_total,
            'dryer_inlet_dry_solids_kg_day': self.product_dry_solids,
            'dryer_inlet_water_kg_day': dryer_inlet_water,
            'product_total_kg_day': self.product_total,
            'product_dry_solids_kg_day': self.product_dry_solids,
            'product_water_kg_day': self.product_water,
            'evaporation_kg_day': evaporation_kg_day,
            'evaporation_kg_h': evaporation_kg_h,
            'closure_residual_kg': closure_residual,
            'closure_error_pct': closure_error_pct,
            'mathematical_closure': bool(closure_error_pct < 1e-6),
            'empirical_status': 'UNRESOLVED_EMPIRICALLY_AWAITING_DRAINAGE_TEST'
        }

    def solve_scenario_b2(self, reported_dryer_inlet_mass_kg_day: float = 18590.0) -> Dict[str, Any]:
        """
        Scenario B2: Reported dryer inlet mass of 18,590.00 kg/day.
        With 13,241.00 kg/day dry solids, implied moisture is 28.7735% wet basis.
        """
        dryer_inlet_total = reported_dryer_inlet_mass_kg_day
        if dryer_inlet_total <= self.product_dry_solids:
            raise ValueError(f"Reported dryer mass ({dryer_inlet_total}) must exceed dry solids ({self.product_dry_solids})")

        dryer_inlet_water = dryer_inlet_total - self.product_dry_solids
        implied_inlet_wb = dryer_inlet_water / dryer_inlet_total

        evaporation_kg_day = dryer_inlet_water - self.product_water
        evaporation_kg_h = evaporation_kg_day / self.hours

        mass_in = dryer_inlet_total
        mass_out = self.product_total + evaporation_kg_day
        closure_residual = abs(mass_in - mass_out)
        closure_error_pct = (closure_residual / mass_in) * 100.0

        return {
            'scenario_id': 'SCENARIO_B2_18590_KG_DAY',
            'inlet_moisture_wb': implied_inlet_wb,
            'inlet_moisture_db': wb_to_db(implied_inlet_wb),
            'dryer_inlet_mass_kg_day': dryer_inlet_total,
            'dryer_inlet_dry_solids_kg_day': self.product_dry_solids,
            'dryer_inlet_water_kg_day': dryer_inlet_water,
            'product_total_kg_day': self.product_total,
            'product_dry_solids_kg_day': self.product_dry_solids,
            'product_water_kg_day': self.product_water,
            'evaporation_kg_day': evaporation_kg_day,
            'evaporation_kg_h': evaporation_kg_h,
            'closure_residual_kg': closure_residual,
            'closure_error_pct': closure_error_pct,
            'mathematical_closure': bool(closure_error_pct < 1e-6),
            'empirical_status': 'UNRESOLVED_EMPIRICALLY_AWAITING_DRAINAGE_TEST'
        }

    def compute_thermal_drying_duty(
        self,
        evaporation_kg_h: float,
        product_dry_solids_kg_h: float,
        product_water_kg_h: float,
        t_feed_c: float = 25.0,
        t_product_out_c: float = 45.0,
        t_air_in_c: float = 65.0,
        t_air_out_c: float = 45.0,
        ambient_humidity_kg_kg: float = 0.012,
        cp_dry_grain: float = 1.60,      # kJ/(kg K)
        cp_liquid_water: float = 4.184,  # kJ/(kg K)
        cp_vapor: float = 1.88,          # kJ/(kg K)
        cp_dry_air: float = 1.005        # kJ/(kg K)
    ) -> Dict[str, Any]:
        """
        Calculates thermal duty and air flow requirements for convective fluid-bed drying.
        """
        # Latent heat of vaporization at product evaporation temperature (~40 C)
        # Regnault formula: h_fg = 2501.3 - 2.361 * T (kJ/kg)
        t_evap_c = 40.0
        h_fg = 2501.3 - 2.361 * t_evap_c  # ~2406.86 kJ/kg

        # Sensible heat to raise product dry solids:
        q_solids_kj_h = product_dry_solids_kg_h * cp_dry_grain * (t_product_out_c - t_feed_c)

        # Sensible heat to raise retained water:
        q_retained_water_kj_h = product_water_kg_h * cp_liquid_water * (t_product_out_c - t_feed_c)

        # Heat of vaporization:
        q_evap_kj_h = evaporation_kg_h * (cp_liquid_water * (t_evap_c - t_feed_c) + h_fg + cp_vapor * (t_air_out_c - t_evap_c))

        # Total process thermal duty (kJ/h and kW_th):
        q_process_kj_h = q_solids_kj_h + q_retained_water_kj_h + q_evap_kj_h
        thermal_duty_kw = q_process_kj_h / 3600.0

        # Required drying air mass flow rate:
        # Moisture pick-up in air: delta_Y = Y_out - Y_in (assumed 0.0125 kg water / kg dry air)
        delta_y = 0.0125
        air_mass_flow_kg_h = evaporation_kg_h / delta_y
        air_density_kg_m3 = 1.128  # at 40 C average
        air_volumetric_m3_h = air_mass_flow_kg_h / air_density_kg_m3

        return {
            'thermal_duty_kw': thermal_duty_kw,
            'thermal_duty_mj_h': q_process_kj_h / 1000.0,
            'latent_heat_evap_kj_kg': h_fg,
            'evaporation_kg_h': evaporation_kg_h,
            'air_mass_flow_kg_h': air_mass_flow_kg_h,
            'air_volumetric_flow_m3_h': air_volumetric_m3_h
        }
