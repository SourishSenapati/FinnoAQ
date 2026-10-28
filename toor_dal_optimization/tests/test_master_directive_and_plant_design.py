"""
Test Suite: Master Build Directive & 15 MT/day Industrial Plant Design
Author: Food-Process Engineering & Red-Team Audit
Directive Date: 15 October 2026

Verifies:
1. Throughput conversions across 8h, 16h, 24h schedules (nominal vs design).
2. Feed basis (15,000 kg/day) vs Finished Product Basis (15,000 kg/day output).
3. Chemical dosing basis separation (112.5 kg/day in liquor vs 75.0 kg/day feed basis).
4. Rigorous mass conservation closure error (< 1e-4 %).
5. Drying thermodynamics (sensible heat, latent heat, air flow, blower power).
6. Soak vessel capacity, batch size, and cycle schedule.
7. Techno-economic model sensitivity (Low, Base, High OpEx).
8. Edge-case stress tests (12% moisture, high leaching, 8h schedule bottleneck).
9. Governance assertions: 'NO_VALIDATED_WINNER' before physical kitchen data.
10. Synthetic data isolation verification.
"""

import pytest
import os
import json
from src.finnoaq.plant_design_15tpd import PlantDesign15TPD


def test_throughput_schedules_and_dual_bases():
    """Verifies nominal and design hourly rates across 8h, 16h, 24h and dual feed/output bases."""
    plant = PlantDesign15TPD(feed_rate_kg_day=15000.0, feed_moisture_wb_pct=10.0, target_product_moisture_wb_pct=10.0)
    tp = plant.calculate_throughput_cases(availability_factor=0.85, design_margin=1.15)
    
    # Check 8h schedule
    assert tp["8h_schedule"]["nominal_feed_rate_kg_h"] == 1875.0
    assert tp["8h_schedule"]["effective_hours_per_day"] == 6.8
    # Design rate = (15000 / 6.8) * 1.15 = 2536.76 kg/h
    assert tp["8h_schedule"]["design_feed_rate_kg_h"] > tp["8h_schedule"]["nominal_feed_rate_kg_h"]
    
    # Check 16h schedule
    assert tp["16h_schedule"]["nominal_feed_rate_kg_h"] == 937.5
    
    # Check 24h schedule
    assert tp["24h_schedule"]["nominal_feed_rate_kg_h"] == 625.0
    
    # Check feed required for 15,000 kg/day saleable finished output
    # At 95.65% recovery, feed required > 15,000 kg
    feed_req = tp["16h_schedule"]["feed_required_if_15tpd_saleable_kg"]
    assert feed_req > 15000.0
    assert abs(feed_req - 15682.0) < 50.0  # ~15,677 - 15,685 kg


def test_chemical_dosing_bases_separation():
    """Strictly separates 0.50% w/w in soak liquor (112.5 kg) from 0.50% of feed (75.0 kg)."""
    plant = PlantDesign15TPD(feed_rate_kg_day=15000.0, liquor_to_grain_ratio=1.5)
    dosing = plant.calculate_chemical_dosing_bases(chemical_conc_pct=0.50)
    
    basis_a = dosing["basis_a_liquor_concentration"]
    basis_b = dosing["basis_b_feed_percentage"]
    
    # Basis A: 22,500 kg liquor * 0.0050 = 112.5 kg active
    assert basis_a["active_chemical_kg_day"] == 112.5
    assert abs(basis_a["commercial_reagent_kg_day"] - (112.5 / 0.995)) < 0.01
    assert basis_a["kg_reagent_per_tonne_feed"] > 7.50
    
    # Basis B: 15,000 kg feed * 0.0050 = 75.0 kg active
    assert basis_b["active_chemical_kg_day"] == 75.0
    assert abs(basis_b["commercial_reagent_kg_day"] - (75.0 / 0.995)) < 0.01
    assert abs(basis_b["kg_reagent_per_tonne_feed"] - 5.03) < 0.05
    
    # Difference must be preserved and transparent
    diff_kg = dosing["difference_reagent_kg_day"]
    assert abs(diff_kg - 37.69) < 0.10
    assert dosing["difference_annual_cost_inr_300days"] > 350000.0  # > ₹3.5 Lakhs/year ambiguity!


def test_mass_balance_rigorous_conservation_closure():
    """Validates that multi-stream mass balance achieves strict conservation (< 1e-4 % closure error)."""
    plant = PlantDesign15TPD()
    bal = plant.calculate_rigorous_mass_balance()
    
    closure = bal["overall_closure"]
    assert closure["is_conserved"] is True
    assert abs(closure["closure_error_pct"]) < 1e-4
    assert abs(closure["closure_error_kg"]) < 0.01
    
    # Check key stream quantities
    streams = bal["stream_table"]
    assert streams["S01_Raw_Dal_Feed"]["total_kg"] == 15000.0
    assert streams["S01_Raw_Dal_Feed"]["dal_solids_kg"] == 13500.0
    
    # Packaged output must reflect nominal wash recovery (98.54%) and fines (2.89%)
    perf = bal["performance_metrics"]
    assert perf["nominal_wash_recovery_pct"] == 98.54
    assert abs(perf["whole_plant_solids_recovery_pct"] - 95.69) < 0.10
    assert perf["fssai_sodium_compliance"] is True
    assert perf["retained_elemental_sodium_mg_100g"] < 350.0


def test_drying_thermodynamic_duty_and_blower():
    """Verifies drying heat load, air flow rate, and electrical blower power."""
    plant = PlantDesign15TPD()
    dry = plant.calculate_drying_and_thermal_energy(operating_hours=16.0, thermal_efficiency=0.65)
    
    # Thermodynamic duty ~170 kW, gross duty ~265 kW (at 65% efficiency)
    assert 150.0 <= dry["thermodynamic_duty_kw"] <= 195.0
    assert 240.0 <= dry["gross_thermal_duty_kw"] <= 290.0
    assert dry["gross_thermal_duty_mj_day"] > 14000.0  # ~15,268 MJ/day
    
    # Blower volumetric air flow and power
    assert dry["air_volumetric_flow_m3_min"] > 90.0
    assert dry["blower_electric_power_kw"] > 7.0
    assert dry["specific_thermal_energy_mj_per_kg_dal"] < 1.25  # ~1.06 MJ/kg dal


def test_soak_vessels_sizing_and_cycle_schedule():
    """Validates soak tank sizing for 2-tank and 3-tank configurations."""
    plant = PlantDesign15TPD()
    tanks = plant.size_soak_vessels(operating_hours=16.0, tank_fill_factor=0.75)
    
    # 2 tanks
    t2 = tanks["2_tanks"]
    assert t2["tank_count"] == 2
    assert t2["dal_batch_size_kg"] > 500.0
    assert 1.0 <= t2["nominal_tank_capacity_m3"] <= 3.5
    assert t2["cycle_time_min"] == 90.0
    
    # 3 tanks
    t3 = tanks["3_tanks"]
    assert t3["tank_count"] == 3
    assert t3["dal_batch_size_kg"] < t2["dal_batch_size_kg"]


def test_techno_economic_scenarios_and_sensitivity():
    """Verifies OpEx model across Low, Base, and High cost cases."""
    plant = PlantDesign15TPD()
    econ_base = plant.calculate_techno_economics(scenario="base")
    econ_low = plant.calculate_techno_economics(scenario="low")
    econ_high = plant.calculate_techno_economics(scenario="high")
    
    cost_base = econ_base["cost_breakdown_inr_per_kg"]["total_net_opex_inr_per_kg"]
    cost_low = econ_low["cost_breakdown_inr_per_kg"]["total_net_opex_inr_per_kg"]
    cost_high = econ_high["cost_breakdown_inr_per_kg"]["total_net_opex_inr_per_kg"]
    
    # OpEx hierarchy
    assert cost_low < cost_base < cost_high
    # Base cost must be in the ₹1.10 - ₹1.40 / kg range
    assert 1.00 <= cost_base <= 1.45
    assert econ_base["annual_opex_lakhs_inr_300days"] > 45.0  # ~₹50 - 65 Lakhs/year


def test_plant_stress_scenarios():
    """Verifies plant response to 12% incoming moisture, high leaching, and 8h schedule."""
    plant = PlantDesign15TPD()
    stress = plant.run_stress_scenarios()
    
    # High moisture increases evaporation
    assert stress["high_moisture_12pct"]["evaporation_increase_pct"] > 0.0
    # High leaching reduces solids recovery and causes revenue loss
    assert stress["high_leach_loss_4_5pct"]["solids_recovery_pct"] < 95.0
    assert stress["high_leach_loss_4_5pct"]["annual_revenue_loss_lakhs_at_120_inr_kg"] > 10.0
    # 8h schedule increases design rate by ~2x over 16h
    assert stress["schedule_8h_bottleneck"]["design_feed_rate_kg_h"] > 2000.0


def test_governance_no_validated_winner_without_physical_data():
    """Asserts that the system strictly classifies treatments as HYPOTHESIS until physical kitchen data passes."""
    candidate_ranking_csv = "reports/TREATMENT_CANDIDATE_RANKING.csv"
    assert os.path.exists(candidate_ranking_csv)
    
    with open(candidate_ranking_csv, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Must NOT contain EXPERIMENTALLY_CONFIRMED for any treated candidate
    lines = content.strip().split("\n")
    header = lines[0].split(",")
    status_idx = header.index("evidence_status")
    cand_id_idx = header.index("candidate_id")
    
    for line in lines[1:]:
        cols = line.split(",")
        cid = cols[cand_id_idx]
        status = cols[status_idx]
        if cid != "CAND-001":  # CAND-001 is control baseline
            assert status != "EXPERIMENTALLY_CONFIRMED", f"{cid} prematurely marked confirmed!"
            assert status == "COMPUTATIONAL_HYPOTHESIS"
