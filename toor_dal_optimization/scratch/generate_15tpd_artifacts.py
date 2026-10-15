import json
import yaml
import os
import sys
sys.path.insert(0, os.path.abspath("."))
from src.harakutir.plant_design_15tpd import PlantDesign15TPD

def generate_artifacts():
    os.makedirs("data", exist_ok=True)
    os.makedirs("configs", exist_ok=True)
    
    plant = PlantDesign15TPD()
    
    # 1. Stream table & balances
    bal = plant.calculate_rigorous_mass_balance()
    tp = plant.calculate_throughput_cases()
    chem = plant.calculate_chemical_dosing_bases()
    dry = plant.calculate_drying_and_thermal_energy()
    tanks = plant.size_soak_vessels()
    econ_base = plant.calculate_techno_economics(scenario="base")
    econ_low = plant.calculate_techno_economics(scenario="low")
    econ_high = plant.calculate_techno_economics(scenario="high")
    stress = plant.run_stress_scenarios()
    
    data_bundle = {
        "metadata": {
            "title": "15 MT/day Toor Dal Industrial Stream Tables & Equipment Balances",
            "date": "2026-10-15",
            "status": "PRELIMINARY_DESIGN_CALCULATION",
            "governing_standard": "Master Build Directive 15 Oct 2026",
            "nominal_feed_rate_kg_day": 15000.0,
            "feed_moisture_wb_pct": 10.0,
            "target_moisture_wb_pct": 10.0,
            "stage_status": "STAGE_2_LOCKED_PENDING_STAGE_1_PHYSICAL_CONFIRMATION"
        },
        "throughput_schedules": tp,
        "chemical_dosing_bases": chem,
        "stream_table": bal["stream_table"],
        "overall_closure": bal["overall_closure"],
        "performance_metrics": bal["performance_metrics"],
        "drying_and_thermal_energy": dry,
        "soak_vessel_sizing": tanks,
        "economics": {
            "base_case": econ_base,
            "low_case": econ_low,
            "high_case": econ_high
        },
        "stress_scenarios": stress
    }
    
    with open("data/stream_tables_15tpd.json", "w", encoding="utf-8") as f:
        json.dump(data_bundle, f, indent=2)
    print("Generated data/stream_tables_15tpd.json successfully.")

    # 2. Config YAML
    config_15tpd = {
        "plant_design_15tpd": {
            "basis": {
                "incoming_feed_rate_kg_day": 15000.0,
                "incoming_feed_moisture_wb_pct": 10.0,
                "target_product_moisture_wb_pct": 10.0,
                "solids_recovery_nominal_wash_pct": 98.54,
                "solids_recovery_whole_plant_pct": 95.69,
                "finished_saleable_output_kg_day": round(bal["performance_metrics"]["packaged_saleable_output_kg_day"], 1),
                "feed_required_if_15tpd_finished_kg": round(tp["16h_schedule"]["feed_required_if_15tpd_saleable_kg"], 1)
            },
            "operating_schedules": {
                "case_8h": {"hours": 8, "nom_feed_kg_h": 1875.0, "design_feed_kg_h": 2536.8},
                "case_16h": {"hours": 16, "nom_feed_kg_h": 937.5, "design_feed_kg_h": 1268.4},
                "case_24h": {"hours": 24, "nom_feed_kg_h": 625.0, "design_feed_kg_h": 845.6}
            },
            "dosing": {
                "reagent": "Food-Grade Sodium Bicarbonate (NaHCO3)",
                "purity_pct": 99.5,
                "liquor_ratio": 1.5,
                "concentration_pct_in_liquor": 0.50,
                "daily_active_kg_liquor_basis": 112.5,
                "daily_active_kg_feed_basis": 75.0,
                "commercial_reagent_kg_day_liquor_basis": 113.07,
                "commercial_reagent_kg_day_feed_basis": 75.38
            },
            "equipment": {
                "soak_tanks": {
                    "count_recommended": 2,
                    "working_volume_m3": 1.99,
                    "nominal_capacity_m3": 2.65,
                    "material": "SS304 Food-Contact",
                    "cycle_time_min": 90.0
                },
                "fluid_bed_dryer": {
                    "drying_temperature_c": 55.0,
                    "thermal_duty_gross_kw": 265.1,
                    "thermal_energy_mj_day": 15268.1,
                    "blower_air_flow_m3_min": 103.7,
                    "blower_power_kw": 8.6,
                    "thermal_efficiency": 0.65
                }
            },
            "economics": {
                "reagent_cost_inr_per_kg": 35.0,
                "thermal_cost_biomass_inr_per_mj": 0.55,
                "thermal_cost_lpg_inr_per_mj": 1.35,
                "electricity_cost_inr_per_kwh": 8.50,
                "fresh_water_inr_per_kl": 30.0,
                "wwtp_treatment_inr_per_kl": 40.0,
                "base_net_opex_inr_per_kg_dal": round(econ_base["cost_breakdown_inr_per_kg"]["total_net_opex_inr_per_kg"], 4),
                "low_net_opex_inr_per_kg_dal": round(econ_low["cost_breakdown_inr_per_kg"]["total_net_opex_inr_per_kg"], 4),
                "high_net_opex_inr_per_kg_dal": round(econ_high["cost_breakdown_inr_per_kg"]["total_net_opex_inr_per_kg"], 4)
            }
        }
    }
    
    with open("configs/process_15tpd_design.yaml", "w", encoding="utf-8") as f:
        yaml.dump(config_15tpd, f, sort_keys=False)
    print("Generated configs/process_15tpd_design.yaml successfully.")

if __name__ == "__main__":
    generate_artifacts()
