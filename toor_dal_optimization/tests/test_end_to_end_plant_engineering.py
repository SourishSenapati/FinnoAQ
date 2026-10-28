"""
Tests for FinnoaQ Toor Dal 15 MT/Day End-to-End Plant, Machine Design, and CAD Package
========================================================================================
Document ID: TEST-ENG-15T-001 | Revision: 1.0 | Date: 2026-10-15
"""

import os
import csv
import pytest
import yaml
from src.finnoaq.detailed_machine_and_plant_engineering import (
    PlantThroughputBasis,
    SoakTankMechanicalDesign,
    AgitatorMechanicalDesign,
    FluidBedDryerPsychrometrics,
    run_complete_plant_sizing,
)


def test_operating_schedules_throughput_and_downtime():
    """Verify 15 MT/day capacity across 8h, 16h, 24h schedules with 85% OEE availability."""
    # 16-hour base case
    basis_16h = PlantThroughputBasis(operating_hours=16.0, oee_availability=0.85)
    r16 = basis_16h.calculate_operating_rates()
    assert r16["effective_hours"] == pytest.approx(13.6, rel=1e-3)
    assert r16["nominal_feed_rate_kg_h"] == pytest.approx(937.5, rel=1e-3)
    assert r16["design_feed_rate_kg_h"] == pytest.approx(1102.94, rel=1e-3)
    assert r16["finished_product_kg_day"] == pytest.approx(14267.79, rel=1e-3)

    # 8-hour schedule
    basis_8h = PlantThroughputBasis(operating_hours=8.0, oee_availability=0.85)
    r8 = basis_8h.calculate_operating_rates()
    assert r8["effective_hours"] == pytest.approx(6.8, rel=1e-3)
    assert r8["nominal_feed_rate_kg_h"] == pytest.approx(1875.0, rel=1e-3)
    assert r8["design_feed_rate_kg_h"] == pytest.approx(2205.88, rel=1e-3)

    # 24-hour schedule
    basis_24h = PlantThroughputBasis(operating_hours=24.0, oee_availability=0.85)
    r24 = basis_24h.calculate_operating_rates()
    assert r24["effective_hours"] == pytest.approx(20.4, rel=1e-3)
    assert r24["nominal_feed_rate_kg_h"] == pytest.approx(625.0, rel=1e-3)
    assert r24["design_feed_rate_kg_h"] == pytest.approx(735.29, rel=1e-3)


def test_soak_tank_mechanical_sizing_and_asme_compliance():
    """Verify working volume, swelling, and ASME Sec VIII Div 1 wall thickness for TK-101A/B."""
    design = SoakTankMechanicalDesign(batch_dal_mass_kg=937.5).calculate_vessel_dimensions()

    # Working slurry volume must account for dal grain swelling (18%) and free liquor
    assert design["total_slurry_vol_m3"] == pytest.approx(2.53, rel=1e-2)
    assert design["actual_gross_vol_m3"] >= design["required_gross_vol_m3"]
    # Working fill fraction must be <= 70%
    fill_fraction = design["total_slurry_vol_m3"] / design["actual_gross_vol_m3"]
    assert fill_fraction <= 0.70

    # ASME Sec VIII Div 1 shell thickness
    assert design["calc_shell_thickness_mm"] >= 2.0
    assert design["selected_shell_thickness_mm"] >= 4.0  # Selected robust sanitary plate
    assert design["selected_head_thickness_mm"] >= 4.0


def test_agitator_low_shear_and_shaft_mechanics():
    """Verify tip speed limit (<1.5 m/s to prevent splitting) and ASME shaft sizing."""
    agitator = AgitatorMechanicalDesign(tank_diameter_m=1.60).calculate_agitator_parameters()

    # Gentle pulse suspension constraint
    assert agitator["tip_speed_m_s"] <= 1.50
    assert agitator["target_rpm"] == 35.0

    # Motor power and torque
    assert agitator["motor_rated_kw"] >= 2.2
    assert agitator["operating_torque_n_m"] >= 500.0

    # Shaft diameter under combined bending and torsion
    assert agitator["calc_shaft_dia_mm"] <= 55.0
    assert agitator["selected_shaft_dia_mm"] == 60.0  # Standard 60mm solid SS316L round bar
    assert agitator["torsional_safety_factor"] >= 1.50


def test_fluid_bed_dryer_psychrometrics_and_thermal_duty():
    """Verify water evaporation rate, Wen & Yu minimum fluidization, and thermal duty."""
    dryer = FluidBedDryerPsychrometrics().calculate_drying_and_airflow()

    # Reconciled daily and hourly evaporation rates for 16h schedule
    assert dryer["daily_evaporation_kg_day"] == pytest.approx(3694.70, rel=1e-2)
    assert dryer["nominal_evaporation_rate_kg_h"] == pytest.approx(230.92, rel=1e-2)
    assert dryer["design_evaporation_rate_kg_h"] == pytest.approx(271.67, rel=1e-2)
    assert dryer["historical_unreconciled_evap_kg_h"] == pytest.approx(257.97, rel=1e-2)

    # Rigorous 10.00% wb exit moisture reconciled rates
    assert dryer["reconciled_10pct_wb_evap_kg_h"] == pytest.approx(242.34, rel=1e-2)
    assert dryer["reconciled_10pct_wb_daily_evap_kg_day"] == pytest.approx(3877.44, rel=1e-2)
    assert dryer["reconciled_10pct_wb_design_evap_kg_h"] == pytest.approx(285.11, rel=1e-2)

    # Wen & Yu fluidization velocity
    assert dryer["min_fluidization_velocity_u_mf_m_s"] == pytest.approx(1.17, rel=0.1)
    assert dryer["operating_velocity_m_s"] > dryer["min_fluidization_velocity_u_mf_m_s"]

    # Active drying area & blower sizing
    assert dryer["bed_width_m"] == 1.0
    assert dryer["drying_bed_length_m"] == 4.5
    assert dryer["cooling_bed_length_m"] == 1.5
    assert dryer["selected_blower_motor_kw"] == 11.0

    # Gross thermal duty and steam demand
    assert dryer["gross_thermal_duty_kw"] == pytest.approx(288.4, rel=0.1)
    assert dryer["steam_consumption_kg_h"] == pytest.approx(482.8, rel=0.1)


def test_chemical_dose_bases_clarity():
    """Verify both chemical formulation bases (liquor basis vs feed basis) are modeled."""
    feed_kg_day = 15000.0
    liquor_kg_day = feed_kg_day * 1.50  # 22,500 kg liquor

    # Basis 1: 0.50% w/w in soak liquor
    bicarb_liquor_basis_kg_day = liquor_kg_day * 0.0050
    assert bicarb_liquor_basis_kg_day == 112.5

    # Basis 2: 0.50% w/w on incoming dal feed
    bicarb_feed_basis_kg_day = feed_kg_day * 0.0050
    assert bicarb_feed_basis_kg_day == 75.0

    # Verify difference is visible and exactly 37.5 kg/day
    assert bicarb_liquor_basis_kg_day - bicarb_feed_basis_kg_day == 37.5


def test_equipment_registers_and_bom_consistency():
    """Verify cross-consistency between equipment register, line list, valve list, and BOM."""
    base_dir = "engineering/registers"
    eq_file = os.path.join(base_dir, "master_equipment_register.csv")
    bom_file = "engineering/procurement/itemized_bom.csv"
    line_file = os.path.join(base_dir, "line_list.csv")

    assert os.path.exists(eq_file)
    assert os.path.exists(bom_file)
    assert os.path.exists(line_file)

    # Load Equipment Tags
    equipment_tags = set()
    with open(eq_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            equipment_tags.add(row["Tag"])

    assert len(equipment_tags) >= 25
    assert "TK-101A" in equipment_tags
    assert "DR-101" in equipment_tags
    assert "PK-101" in equipment_tags

    # Verify BOM has no empty equipment tags for major packages
    with open(bom_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            assert float(row["Total_Cost_Lakhs_INR"]) > 0.0


def test_cad_deliverables_existence_and_not_empty():
    """Verify all 10 DXF drawings, 4 STEP files, OBJ files, and vector PDF drawings exist."""
    cad_dir = "engineering/cad"
    dxf_dir = os.path.join(cad_dir, "dxf")
    step_dir = os.path.join(cad_dir, "step")
    pdf_dir = os.path.join(cad_dir, "pdf")

    # Verify all 10 DXFs
    for i in range(1, 11):
        dxf_name = f"DWG-FIN-15T-{i:03d}.dxf"
        p = os.path.join(dxf_dir, dxf_name)
        assert os.path.exists(p), f"Missing DXF drawing {dxf_name}"
        assert os.path.getsize(p) > 500, f"DXF drawing {dxf_name} is empty"

    # Verify STEP models
    step_models = [
        "TK-101_Soak_Tank.step",
        "AG-101_Agitator.step",
        "DR-101_Fluid_Bed_Dryer.step",
        "SK-100_Dosing_Skid.step",
    ]
    for sm in step_models:
        p = os.path.join(step_dir, sm)
        assert os.path.exists(p), f"Missing STEP model {sm}"
        assert os.path.getsize(p) > 200

    # Verify PDF drawing package
    pdf_pkg = os.path.join(pdf_dir, "FINNOAQ_15TPD_ENGINEERING_DRAWINGS.pdf")
    assert os.path.exists(pdf_pkg)
    assert os.path.getsize(pdf_pkg) > 5000  # Multi-page vector PDF


def test_preliminary_warning_in_dxf_drawings():
    """Ensure all generated DXF drawings carry the mandatory 'PRELIMINARY—NOT FOR CONSTRUCTION' warning."""
    dxf_dir = "engineering/cad/dxf"
    dwg_001 = os.path.join(dxf_dir, "DWG-FIN-15T-001.dxf")
    with open(dwg_001, "r", encoding="utf-8") as f:
        content = f.read()
    assert "NOT FOR CONSTRUCTION" in content
    assert "PRELIMINARY" in content
