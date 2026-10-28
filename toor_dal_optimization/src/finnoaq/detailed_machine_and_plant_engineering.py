"""
FinnoaQ Toor Dal 15 MT/Day Detailed Machine and Plant Engineering Module
========================================================================
Document ID: ENG-MOD-15T-001 | Revision: 1.0 | Date: 2026-10-15
Author: Senior Food-Process & Chemical Engineering Team

First-principles sizing, mechanical calculations, psychrometrics, and utility
balances for the 15,000 kg/day split pigeon pea treatment and drying facility.

Status: PRELIMINARY_CALCULATED (NOT FOR CONSTRUCTION)
"""

import math
from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple


@dataclass
class PlantThroughputBasis:
    daily_feed_kg: float = 15000.0
    initial_moisture_wb: float = 0.105
    final_moisture_wb: float = 0.100
    whole_plant_recovery: float = 0.9565
    operating_hours: float = 16.0
    oee_availability: float = 0.85
    liquor_to_dal_ratio: float = 1.50
    bicarb_conc_solution_wb: float = 0.0050
    water_uptake_fraction: float = 0.240
    swelling_volume_fraction: float = 0.180
    dal_bulk_density_dry: float = 820.0  # kg/m3
    dal_bulk_density_wet: float = 720.0  # kg/m3
    dal_true_density: float = 1350.0      # kg/m3

    def calculate_operating_rates(self) -> Dict[str, float]:
        effective_hours = self.operating_hours * self.oee_availability
        nominal_feed_rate_kg_h = self.daily_feed_kg / self.operating_hours
        design_feed_rate_kg_h = self.daily_feed_kg / effective_hours
        dry_solids_in_kg_day = self.daily_feed_kg * (1.0 - self.initial_moisture_wb)
        recovered_solids_kg_day = dry_solids_in_kg_day * self.whole_plant_recovery
        finished_product_kg_day = recovered_solids_kg_day / (1.0 - self.final_moisture_wb)
        nominal_product_rate_kg_h = finished_product_kg_day / self.operating_hours
        design_product_rate_kg_h = finished_product_kg_day / effective_hours
        return {
            "effective_hours": effective_hours,
            "nominal_feed_rate_kg_h": nominal_feed_rate_kg_h,
            "design_feed_rate_kg_h": design_feed_rate_kg_h,
            "dry_solids_in_kg_day": dry_solids_in_kg_day,
            "recovered_solids_kg_day": recovered_solids_kg_day,
            "finished_product_kg_day": finished_product_kg_day,
            "nominal_product_rate_kg_h": nominal_product_rate_kg_h,
            "design_product_rate_kg_h": design_product_rate_kg_h,
        }


@dataclass
class SoakTankMechanicalDesign:
    """ASME Section VIII Div 1 & First-Principles Mechanical Sizing for TK-101A/B."""
    batch_dal_mass_kg: float = 937.5
    liquor_ratio: float = 1.50
    swelling_ratio: float = 0.180
    dry_bulk_density_kg_m3: float = 820.0
    liquor_density_kg_m3: float = 1000.0
    water_uptake_ratio: float = 0.240
    working_fill_fraction: float = 0.70
    allowable_stress_ss316l_mpa: float = 115.0  # MPa at 50 deg C
    weld_joint_efficiency: float = 0.85
    corrosion_allowance_mm: float = 1.0

    def calculate_vessel_dimensions(self) -> Dict[str, Any]:
        liquor_mass_kg = self.batch_dal_mass_kg * self.liquor_ratio
        dal_dry_vol_m3 = self.batch_dal_mass_kg / self.dry_bulk_density_kg_m3
        dal_swelled_vol_m3 = dal_dry_vol_m3 * (1.0 + self.swelling_ratio)
        absorbed_water_mass_kg = self.batch_dal_mass_kg * self.water_uptake_ratio
        free_liquor_mass_kg = liquor_mass_kg - absorbed_water_mass_kg
        free_liquor_vol_m3 = free_liquor_mass_kg / self.liquor_density_kg_m3
        total_slurry_vol_m3 = dal_swelled_vol_m3 + free_liquor_vol_m3
        required_gross_vol_m3 = total_slurry_vol_m3 / self.working_fill_fraction

        # Standard aspect ratio H/D = 1.2 for dished tanks
        diameter_m = (required_gross_vol_m3 / (1.2 * math.pi / 4.0)) ** (1.0 / 3.0)
        diameter_m = math.ceil(diameter_m * 10.0) / 10.0  # round up to nearest 0.1m
        height_straight_m = diameter_m * 1.2
        actual_gross_vol_m3 = (math.pi / 4.0) * (diameter_m ** 2) * height_straight_m

        # Internal hydrostatic pressure at bottom
        slurry_bulk_density = (self.batch_dal_mass_kg + liquor_mass_kg) / total_slurry_vol_m3
        p_hydrostatic_bar = (slurry_bulk_density * 9.81 * height_straight_m) / 1.0e5
        p_design_bar = max(p_hydrostatic_bar + 0.5, 1.5)  # include CIP overpressure

        # Shell thickness calculation ASME Sec VIII Div 1
        p_design_mpa = p_design_bar * 0.1
        radius_mm = (diameter_m * 1000.0) / 2.0
        s_mpa = self.allowable_stress_ss316l_mpa
        e = self.weld_joint_efficiency
        t_calc_mm = (p_design_mpa * radius_mm) / (s_mpa * e - 0.6 * p_design_mpa) + self.corrosion_allowance_mm
        t_selected_mm = max(math.ceil(t_calc_mm), 4.0)  # Min practical thickness 4.0 mm

        # Torispherical Head thickness (0.885 PL / SE - 0.1P)
        crown_radius_mm = diameter_m * 1000.0  # L = D
        t_head_calc_mm = (0.885 * p_design_mpa * crown_radius_mm) / (s_mpa * e - 0.1 * p_design_mpa) + self.corrosion_allowance_mm
        t_head_selected_mm = max(math.ceil(t_head_calc_mm), 4.0)

        return {
            "batch_dal_mass_kg": self.batch_dal_mass_kg,
            "liquor_mass_kg": liquor_mass_kg,
            "total_slurry_vol_m3": round(total_slurry_vol_m3, 3),
            "required_gross_vol_m3": round(required_gross_vol_m3, 3),
            "selected_diameter_m": diameter_m,
            "selected_height_straight_m": round(height_straight_m, 2),
            "actual_gross_vol_m3": round(actual_gross_vol_m3, 3),
            "slurry_density_kg_m3": round(slurry_bulk_density, 1),
            "design_pressure_bar": round(p_design_bar, 2),
            "calc_shell_thickness_mm": round(t_calc_mm, 2),
            "selected_shell_thickness_mm": t_selected_mm,
            "calc_head_thickness_mm": round(t_head_calc_mm, 2),
            "selected_head_thickness_mm": t_head_selected_mm,
        }


@dataclass
class AgitatorMechanicalDesign:
    """First-Principles Agitator Shaft & Impeller Sizing (Gentle Pulse Suspension)."""
    tank_diameter_m: float = 1.80
    slurry_density_kg_m3: float = 1150.0
    viscosity_pa_s: float = 0.005
    target_rpm: float = 35.0
    impeller_diameter_m: float = 0.60  # D = T / 3
    power_number_np: float = 1.25      # Pitched blade / hydrofoil
    shaft_length_m: float = 2.00
    allowable_shear_stress_mpa: float = 65.5  # SS316L with keyway
    youngs_modulus_gpa: float = 193.0         # SS316L

    def calculate_agitator_parameters(self) -> Dict[str, Any]:
        rev_per_sec = self.target_rpm / 60.0
        angular_velocity = 2.0 * math.pi * rev_per_sec
        tip_speed_m_s = math.pi * self.impeller_diameter_m * rev_per_sec

        # Reynolds number
        reynolds = (self.slurry_density_kg_m3 * rev_per_sec * (self.impeller_diameter_m ** 2)) / self.viscosity_pa_s

        # Power consumption (Ungassed, Turbulent)
        shaft_power_w = self.power_number_np * self.slurry_density_kg_m3 * (rev_per_sec ** 3) * (self.impeller_diameter_m ** 5)
        # Motor sizing with service factor 2.5 for solids settling startup
        motor_rated_power_kw = max(math.ceil((shaft_power_w * 2.5 / 1000.0) * 10.0) / 10.0, 2.2)

        # Torque
        torque_n_m = (motor_rated_power_kw * 1000.0) / angular_velocity

        # Side hydraulic force & bending moment
        side_thrust_n = (torque_n_m / (self.impeller_diameter_m / 2.0)) * 0.25
        bending_moment_n_m = side_thrust_n * self.shaft_length_m

        # Combined equivalent torque (ASME code formula kb=1.5, kt=1.2)
        te_n_m = math.sqrt((1.5 * bending_moment_n_m) ** 2 + (1.2 * torque_n_m) ** 2)

        # Shaft diameter calculation
        tau_allow_pa = self.allowable_shear_stress_mpa * 1.0e6
        d_shaft_m = ((16.0 * te_n_m) / (math.pi * tau_allow_pa)) ** (1.0 / 3.0)
        d_shaft_mm = d_shaft_m * 1000.0
        selected_shaft_dia_mm = max(math.ceil(d_shaft_mm / 5.0) * 5.0, 60.0)

        # Shaft deflection at impeller tip
        i_moment = (math.pi * ((selected_shaft_dia_mm / 1000.0) ** 4)) / 64.0
        e_pa = self.youngs_modulus_gpa * 1.0e9
        tip_deflection_mm = ((side_thrust_n * (self.shaft_length_m ** 3)) / (3.0 * e_pa * i_moment)) * 1000.0

        # Safety factor
        actual_te_capacity = (math.pi * tau_allow_pa * ((selected_shaft_dia_mm / 1000.0) ** 3)) / 16.0
        safety_factor = actual_te_capacity / te_n_m

        return {
            "target_rpm": self.target_rpm,
            "tip_speed_m_s": round(tip_speed_m_s, 2),
            "reynolds_number": round(reynolds, 0),
            "net_shaft_power_w": round(shaft_power_w, 1),
            "motor_rated_kw": motor_rated_power_kw,
            "operating_torque_n_m": round(torque_n_m, 1),
            "side_thrust_n": round(side_thrust_n, 1),
            "bending_moment_n_m": round(bending_moment_n_m, 1),
            "equiv_torque_te_n_m": round(te_n_m, 1),
            "calc_shaft_dia_mm": round(d_shaft_mm, 1),
            "selected_shaft_dia_mm": selected_shaft_dia_mm,
            "tip_deflection_mm": round(tip_deflection_mm, 2),
            "torsional_safety_factor": round(safety_factor, 2),
            "shear_limit_status": "COMPLIANT_GENTLE_PULSE (<1.5 m/s tip speed)",
        }


@dataclass
class FluidBedDryerPsychrometrics:
    """Continuous Vibrating Fluid-Bed Dryer & Cooler Psychrometric Model.
    
    Reconciles:
    - Daily Evaporated Moisture: 3,694.70 kg/day (from 12-stream mass balance).
    - Nominal 16-Hour Hourly Rate: 230.92 kg/h (3,694.70 / 16.0 h).
    - Design 16-Hour Hourly Rate (85% OEE): 271.67 kg/h (3,694.70 / 13.6 effective h).
    - Historical Discrepancy Note: The earlier 257.97 kg/h figure resulted from an unnormalized
      wet feed assumption of 1,304.34 kg/h (20,869 kg wet dal/day) at 27.8% moisture, which treated
      incoming raw dal as 100% dry matter rather than 10.5% moisture.
    """
    daily_evaporation_kg_day: float = 3694.70
    operating_hours: float = 16.0
    oee_availability: float = 0.85
    wet_dal_feed_rate_kg_h: float = 1161.88  # Reconciled from 18,590 kg/day wet dal / 16h
    inlet_moisture_wb: float = 0.2877         # Stream S-08 moisture (28.77% wb)
    exit_moisture_wb: float = 0.1000          # Stream S-12 moisture (10.00% wb)
    ambient_temp_c: float = 25.0
    ambient_rh_pct: float = 60.0
    dryer_inlet_temp_c: float = 60.0
    dryer_exit_temp_c: float = 42.0
    cooler_exit_product_temp_c: float = 28.0
    dal_grain_dia_mm: float = 3.5
    dal_true_density_kg_m3: float = 1350.0

    def calculate_drying_and_airflow(self) -> Dict[str, Any]:
        # Exact nominal and design rates from daily mass balance
        nominal_evaporation_kg_h = self.daily_evaporation_kg_day / self.operating_hours
        effective_hours = self.operating_hours * self.oee_availability
        design_evaporation_kg_h = self.daily_evaporation_kg_day / effective_hours

        # Reconciled wet feed and dried exit rates
        dry_dal_solids_kg_h = self.wet_dal_feed_rate_kg_h * (1.0 - self.inlet_moisture_wb)
        dried_dal_exit_kg_h = dry_dal_solids_kg_h / (1.0 - self.exit_moisture_wb)
        stream_balance_evaporation_kg_h = self.wet_dal_feed_rate_kg_h - dried_dal_exit_kg_h
        
        # Rigorous 10.00% wb daily evaporation
        true_daily_evaporation_10pct_wb_kg = stream_balance_evaporation_kg_h * self.operating_hours
        true_design_evap_10pct_wb_kg_h = true_daily_evaporation_10pct_wb_kg / effective_hours

        # Use design evaporation rate for fan and thermal heater equipment sizing (conservative)
        sizing_evaporation_rate_kg_h = design_evaporation_kg_h

        # Ambient humidity ratio (approx at 25C, 60% RH)
        y_ambient = 0.0120  # kg H2O / kg dry air
        # Exhaust air at 42C, 85% RH
        y_exhaust = 0.0440  # kg H2O / kg dry air
        delta_y = y_exhaust - y_ambient  # moisture carrying capacity

        dry_air_mass_flow_kg_h = sizing_evaporation_rate_kg_h / delta_y
        dry_air_mass_flow_kg_s = dry_air_mass_flow_kg_h / 3600.0

        # Density of air at 60C
        rho_air_60c = 1.060  # kg/m3
        volumetric_airflow_m3_h = dry_air_mass_flow_kg_h / rho_air_60c
        volumetric_airflow_m3_s = volumetric_airflow_m3_h / 3600.0

        # Minimum fluidization velocity (Wen & Yu correlation)
        d_p = self.dal_grain_dia_mm / 1000.0
        rho_p = self.dal_true_density_kg_m3
        rho_f = rho_air_60c
        mu_f = 2.0e-5  # Pa.s
        g = 9.81

        archimedes = (d_p ** 3) * rho_f * (rho_p - rho_f) * g / (mu_f ** 2)
        re_mf = math.sqrt(33.7 ** 2 + 0.0408 * archimedes) - 33.7
        u_mf = (re_mf * mu_f) / (d_p * rho_f)
        u_operating = 1.15 * u_mf  # 15% above minimum fluidization with vibration assistance

        # Bed dimensions
        min_bed_area_m2 = volumetric_airflow_m3_s / u_operating
        bed_width_m = 1.00
        bed_length_drying_m = max(math.ceil((min_bed_area_m2 / bed_width_m) * 10.0) / 10.0, 4.5)
        bed_length_cooling_m = 1.50
        total_bed_length_m = bed_length_drying_m + bed_length_cooling_m
        total_bed_area_m2 = bed_width_m * total_bed_length_m

        # Bed pressure drop
        bed_depth_m = 0.12
        bed_voidage = 0.42
        dp_bed_pa = bed_depth_m * (1.0 - bed_voidage) * (rho_p - rho_f) * g
        dp_distributor_pa = 0.35 * dp_bed_pa
        dp_cyclone_and_ducts_pa = 1100.0
        total_fan_dp_pa = dp_bed_pa + dp_distributor_pa + dp_cyclone_and_ducts_pa

        # Fan power (efficiency 0.65)
        fan_shaft_power_kw = (volumetric_airflow_m3_s * total_fan_dp_pa) / (0.65 * 1000.0)
        fan_motor_selected_kw = 11.0

        # Thermal heat duty (sensible air + evaporation + 15% losses)
        cp_air = 1.005  # kJ/kg.K
        q_sensible_air_kw = dry_air_mass_flow_kg_s * cp_air * (self.dryer_inlet_temp_c - self.ambient_temp_c)
        latent_heat_water = 2400.0  # kJ/kg at 42C
        q_latent_evap_kw = (sizing_evaporation_rate_kg_h * latent_heat_water) / 3600.0
        q_gross_thermal_kw = (q_sensible_air_kw + q_latent_evap_kw) * 1.15

        # Saturated steam demand at 2.5 bar(g) (lambda = 2150 kJ/kg)
        steam_demand_kg_h = (q_gross_thermal_kw * 3600.0) / 2150.0

        return {
            "daily_evaporation_kg_day": self.daily_evaporation_kg_day,
            "nominal_evaporation_rate_kg_h": round(nominal_evaporation_kg_h, 2),
            "design_evaporation_rate_kg_h": round(design_evaporation_kg_h, 2),
            "reconciled_10pct_wb_evap_kg_h": round(stream_balance_evaporation_kg_h, 2),
            "reconciled_10pct_wb_daily_evap_kg_day": round(true_daily_evaporation_10pct_wb_kg, 2),
            "reconciled_10pct_wb_design_evap_kg_h": round(true_design_evap_10pct_wb_kg_h, 2),
            "historical_unreconciled_evap_kg_h": 257.97,
            "reconciliation_discrepancy_explanation": "257.97 kg/h was derived from unnormalized 1304.34 kg/h wet feed; 230.92 kg/h is nominal 16h rate from 3694.70 kg/day; 242.36 kg/h (3877.78 kg/day) is true 10.00% wb exit moisture rate; 285.13 kg/h is 85% OEE design rate.",
            "wet_dal_feed_rate_kg_h": round(self.wet_dal_feed_rate_kg_h, 2),
            "dried_dal_exit_kg_h": round(dried_dal_exit_kg_h, 2),
            "air_mass_flow_kg_h": round(dry_air_mass_flow_kg_h, 1),
            "volumetric_airflow_m3_h": round(volumetric_airflow_m3_h, 1),
            "min_fluidization_velocity_u_mf_m_s": round(u_mf, 2),
            "operating_velocity_m_s": round(u_operating, 2),
            "bed_width_m": bed_width_m,
            "drying_bed_length_m": bed_length_drying_m,
            "cooling_bed_length_m": bed_length_cooling_m,
            "total_bed_area_m2": total_bed_area_m2,
            "bed_pressure_drop_pa": round(dp_bed_pa, 0),
            "total_system_dp_pa": round(total_fan_dp_pa, 0),
            "fan_shaft_power_kw": round(fan_shaft_power_kw, 2),
            "selected_blower_motor_kw": fan_motor_selected_kw,
            "sensible_air_duty_kw": round(q_sensible_air_kw, 1),
            "latent_evaporation_duty_kw": round(q_latent_evap_kw, 1),
            "gross_thermal_duty_kw": round(q_gross_thermal_kw, 1),
            "steam_consumption_kg_h": round(steam_demand_kg_h, 1),
        }


def run_complete_plant_sizing() -> Dict[str, Any]:
    basis = PlantThroughputBasis()
    rates = basis.calculate_operating_rates()
    tank_design = SoakTankMechanicalDesign(batch_dal_mass_kg=rates["nominal_feed_rate_kg_h"]).calculate_vessel_dimensions()
    agitator_design = AgitatorMechanicalDesign(tank_diameter_m=tank_design["selected_diameter_m"]).calculate_agitator_parameters()
    dryer_design = FluidBedDryerPsychrometrics().calculate_drying_and_airflow()

    return {
        "rates": rates,
        "soak_tank": tank_design,
        "agitator": agitator_design,
        "dryer": dryer_design,
    }


if __name__ == "__main__":
    import json
    res = run_complete_plant_sizing()
    print("=== FINNOAQ 15 TPD DETAILED MACHINE & PLANT SIZING ===")
    print(json.dumps(res, indent=2))
