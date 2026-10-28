"""
Verification script for deterministic mass, moisture, and energy balances.
Checks reference calculations from Directive Section 5.
"""
import sys
sys.path.insert(0, '.')
from src.finnoaq.deterministic_balances import DeterministicMassBalance, wb_to_db, db_to_wb

def run_verification():
    print("=================================================================")
    print("FINNOAQ DETERMINISTIC MASS, MOISTURE & ENERGY BALANCE VERIFICATION")
    print("=================================================================")

    # Reference Case: 15,000 kg/day @ 10.5% WB, 184 kg loss
    mb = DeterministicMassBalance(15000.0, 0.105, 0.100, 184.0, 20.0)
    print(f"Feed Mass: {mb.feed_total:.2f} kg/day")
    print(f"Feed Dry Solids: {mb.feed_dry_solids:.2f} kg/day (reference: 13425.00 kg/day)")
    print(f"Feed Water: {mb.feed_water:.2f} kg/day (reference: 1575.00 kg/day)")
    print(f"Solids Loss: {mb.solids_loss:.2f} kg/day (reference: 184.00 kg/day)")
    print(f"Product Dry Solids: {mb.product_dry_solids:.2f} kg/day (reference: 13241.00 kg/day)")
    print(f"Product Total: {mb.product_total:.2f} kg/day (reference: ~14712.22 kg/day)")
    print(f"Product Water: {mb.product_water:.2f} kg/day (reference: ~1471.22 kg/day)")

    assert abs(mb.feed_dry_solids - 13425.0) < 1e-4
    assert abs(mb.feed_water - 1575.0) < 1e-4
    assert abs(mb.product_dry_solids - 13241.0) < 1e-4
    assert abs(mb.product_total - 14712.2222) < 1e-2
    assert abs(mb.product_water - 1471.2222) < 1e-2

    # Scenario B1: 28.00% WB moisture inlet
    b1 = mb.solve_scenario_b1(0.2800)
    print("\n--- Scenario B1 (True 28.00% WB Inlet) ---")
    print(f"Dryer Inlet Mass: {b1['dryer_inlet_mass_kg_day']:.2f} kg/day (ref: ~18390.28)")
    print(f"Dryer Inlet Water: {b1['dryer_inlet_water_kg_day']:.2f} kg/day (ref: ~5149.28)")
    print(f"Evaporation: {b1['evaporation_kg_day']:.2f} kg/day ({b1['evaporation_kg_h']:.2f} kg/h) (ref: ~3678.06)")
    print(f"Mathematical Closure Residual: {b1['closure_residual_kg']:.8f} kg")
    print(f"Mathematical Closure Error: {b1['closure_error_pct']:.8f} %")

    assert abs(b1['dryer_inlet_mass_kg_day'] - 18390.2778) < 1e-2
    assert abs(b1['dryer_inlet_water_kg_day'] - 5149.2778) < 1e-2
    assert abs(b1['evaporation_kg_day'] - 3678.0556) < 1e-2
    assert b1['mathematical_closure'] is True

    # Scenario B2: Reported 18,590.00 kg/day inlet
    b2 = mb.solve_scenario_b2(18590.0)
    print("\n--- Scenario B2 (Reported 18,590.00 kg/day Inlet) ---")
    print(f"Dryer Inlet Mass: {b2['dryer_inlet_mass_kg_day']:.2f} kg/day (ref: 18590.00)")
    print(f"Dryer Inlet Water: {b2['dryer_inlet_water_kg_day']:.2f} kg/day (ref: 5349.00)")
    print(f"Implied Inlet Moisture: {b2['inlet_moisture_wb'] * 100:.4f} % WB (ref: ~28.7735%)")
    print(f"Evaporation: {b2['evaporation_kg_day']:.2f} kg/day ({b2['evaporation_kg_h']:.2f} kg/h) (ref: ~3877.78)")
    print(f"Mathematical Closure Residual: {b2['closure_residual_kg']:.8f} kg")
    print(f"Mathematical Closure Error: {b2['closure_error_pct']:.8f} %")

    assert abs(b2['dryer_inlet_mass_kg_day'] - 18590.0) < 1e-4
    assert abs(b2['dryer_inlet_water_kg_day'] - 5349.0) < 1e-4
    assert abs(b2['inlet_moisture_wb'] - 0.2877353) < 1e-5
    assert abs(b2['evaporation_kg_day'] - 3877.7778) < 1e-2
    assert b2['mathematical_closure'] is True

    delta_evap = b2['evaporation_kg_day'] - b1['evaporation_kg_day']
    print(f"\nUnresolved Physical Delta (B2 - B1): {delta_evap:.2f} kg/day water ({delta_evap / 20.0:.2f} kg/h)")
    assert abs(delta_evap - 199.7222) < 1e-2

    # Thermal duties
    solids_h = mb.product_dry_solids / 20.0
    water_h = mb.product_water / 20.0
    t1 = mb.compute_thermal_drying_duty(b1['evaporation_kg_h'], solids_h, water_h)
    t2 = mb.compute_thermal_drying_duty(b2['evaporation_kg_h'], solids_h, water_h)
    print("\n--- Convective Drying Thermal Duties & Air Requirements ---")
    print(f"Scenario B1 Thermal Duty: {t1['thermal_duty_kw']:.2f} kW_th ({t1['thermal_duty_mj_h']:.2f} MJ/h)")
    print(f"Scenario B1 Air Flow: {t1['air_mass_flow_kg_h']:.2f} kg/h ({t1['air_volumetric_flow_m3_h']:.2f} m3/h)")
    print(f"Scenario B2 Thermal Duty: {t2['thermal_duty_kw']:.2f} kW_th ({t2['thermal_duty_mj_h']:.2f} MJ/h)")
    print(f"Scenario B2 Air Flow: {t2['air_mass_flow_kg_h']:.2f} kg/h ({t2['air_volumetric_flow_m3_h']:.2f} m3/h)")
    delta_kw = t2['thermal_duty_kw'] - t1['thermal_duty_kw']
    print(f"Delta Thermal Duty: {delta_kw:.2f} kW_th")

    # Competing Solids Loss Case (196.01 kg/day loss = 1.46% of raw solids)
    mb_l2 = DeterministicMassBalance(15000.0, 0.105, 0.100, 196.01, 20.0)
    b1_l2 = mb_l2.solve_scenario_b1(0.2800)
    b2_l2 = mb_l2.solve_scenario_b2(18590.0)
    print("\n--- Competing Solids Loss Case (196.01 kg/day = 1.4600%) ---")
    print(f"Product Dry Solids: {mb_l2.product_dry_solids:.2f} kg/day (vs 13241.00)")
    print(f"Scenario B1-L2 Evaporation: {b1_l2['evaporation_kg_day']:.2f} kg/day")
    print(f"Scenario B2-L2 Implied Moisture: {b2_l2['inlet_moisture_wb'] * 100:.4f} % WB")
    print(f"Scenario B2-L2 Evaporation: {b2_l2['evaporation_kg_day']:.2f} kg/day")

    print("\nALL DETERMINISTIC MASS & MOISTURE BALANCES VERIFIED SUCCESSFULLY.")

if __name__ == '__main__':
    run_verification()
