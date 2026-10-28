"""
Unit & Integration Tests for 15 MT/Day Plant Design, Mass Balance, and Dose Calculator.
Verifies compliance with the FinnoaQ Omega Persistent Autonomous R&D Constitution.
"""

import pytest
from src.finnoaq.dose_calculator import DoseCalculator
from src.finnoaq.plant_design import PlantDesignEngine
from src.finnoaq.mass_balance import MassBalanceEngine


def test_dose_calculator_multi_basis_separation():
    calc = DoseCalculator()
    # Test 0.5% w/w solution at 1.5:1 liquor ratio
    res = calc.calculate_formulation_point(
        solution_conc_w_w_pct=0.50,
        liquor_to_grain_ratio=1.5,
        incoming_moisture_wb_pct=10.5
    )

    # 1. Solution concentration must be 0.5% w/w
    assert res["solution_concentration"]["w_w_pct"] == 0.50
    assert res["solution_concentration"]["w_v_g_per_L"] == 5.04  # 0.005 * 1008 kg/m3

    # 2. Applied treatment per incoming dal must be 0.75 kg / 100kg (since 1.5 kg liquor * 0.5% = 0.0075 kg/kg dal)
    assert res["applied_treatment"]["kg_active_per_100kg_dal"] == 0.75
    assert res["applied_treatment"]["kg_active_per_tonne_dal"] == 7.50
    assert res["applied_treatment"]["pct_of_incoming_mass"] == 0.75

    # 3. Dry solids basis must be higher than wet basis (0.75 / 0.895 = 0.838%)
    assert res["applied_treatment"]["pct_of_incoming_dry_solids"] == 0.838

    # 4. Never equate soak concentration (0.5%) with applied dose (0.75%)
    assert res["solution_concentration"]["w_w_pct"] != res["applied_treatment"]["pct_of_incoming_mass"]


def test_dose_calculator_reference_table():
    calc = DoseCalculator()
    targets = [0.10, 0.20, 0.25, 0.50, 0.75, 1.00, 2.00]
    table = calc.generate_arithmetic_reference_table(target_concentrations=targets, liquor_ratio=1.5)

    assert len(table) == 7
    # Verify monotonic increase of chemical consumption
    for i in range(len(table) - 1):
        assert table[i]["daily_chem_15_tpd_kg"] < table[i + 1]["daily_chem_15_tpd_kg"]
        assert table[i]["retained_na_mg_per_100g"] < table[i + 1]["retained_na_mg_per_100g"]


def test_plant_design_operating_schedules():
    plant = PlantDesignEngine(incoming_feed_kg_day=15000.0, plant_availability_pct=85.0, design_capacity_margin_pct=20.0)
    res = plant.model_operating_schedules(dal_dry_solids_loss_pct=3.2)

    # 1. Incoming feed basis must be 15,000 kg/day
    assert res["design_basis"]["daily_feed_kg"] == 15000.0
    assert res["design_basis"]["plant_availability_pct"] == 85.0

    schedules = res["schedules"]
    assert "8h_schedule" in schedules
    assert "16h_schedule" in schedules
    assert "24h_schedule" in schedules

    # 2. Check nominal throughput rates
    assert schedules["8h_schedule"]["nominal_incoming_feed_rate_kg_h"] == 1875.0
    assert schedules["16h_schedule"]["nominal_incoming_feed_rate_kg_h"] == 937.5
    assert schedules["24h_schedule"]["nominal_incoming_feed_rate_kg_h"] == 625.0

    # 3. Design feed rate with 85% availability and 20% margin
    # Rate = (15000 / (hours * 0.85)) * 1.20
    for h in [8, 16, 24]:
        expected = round((15000.0 / (h * 0.85)) * 1.20, 1)
        actual = schedules[f"{h}h_schedule"]["effective_design_feed_rate_kg_h"]
        assert abs(actual - expected) < 0.2

    # 4. Sizing check: 8h dryer duty must exceed 24h dryer duty
    assert schedules["8h_schedule"]["dryer_system"]["gross_thermal_duty_kw"] > schedules["24h_schedule"]["dryer_system"]["gross_thermal_duty_kw"]


def test_mass_balance_closure_and_dry_solids_recovery():
    engine = MassBalanceEngine(incoming_feed_kg=15000.0, raw_moisture_wb_pct=10.5, target_product_moisture_wb_pct=10.0)
    balance = engine.solve_complete_mass_balance(
        leaching_loss_solids_pct=2.10,
        rinsing_loss_solids_pct=0.45,
        disintegration_loss_solids_pct=0.65,
        conveying_attrition_solids_pct=0.35,
        drying_cracking_solids_pct=0.40,
        cyclone_fines_solids_pct=0.25,
        rejection_allowance_solids_pct=0.15
    )

    # 1. Total loss percentage must equal sum of loss channels
    total_loss = 2.10 + 0.45 + 0.65 + 0.35 + 0.40 + 0.25 + 0.15  # 4.35%
    ds_balance = balance["dal_dry_solids_balance"]
    assert abs(ds_balance["dal_derived_solids_loss_pct"] - total_loss) < 1e-4
    assert abs(ds_balance["dal_dry_solids_recovery_pct"] - (100.0 - total_loss)) < 1e-4

    # 2. Chemical additive must NOT be counted as dal-origin solids
    chem = balance["chemical_additive_balance"]
    assert chem["chemical_retained_in_product_kg"] > 0
    # Saleable dal solids + chemical retained = total dry solids
    total_dry_solids = ds_balance["saleable_dal_origin_dry_solids_kg"] + chem["chemical_retained_in_product_kg"]
    assert total_dry_solids > ds_balance["saleable_dal_origin_dry_solids_kg"]

    # 3. Mass balance closure must be exact (< 0.01% error)
    facility = balance["total_facility_mass_balance"]
    assert facility["mass_balance_closure_error_pct"] < 0.01
    assert facility["status"] == "VERIFIED_CLOSED (< 0.05% error)"
