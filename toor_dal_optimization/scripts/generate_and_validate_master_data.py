"""
generate_and_validate_master_data.py
Constructs the versioned canonical master datasets and schemas in engineering/master_data/
and validates each dataset against its JSON schema.
"""

import os
import json
import jsonschema

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_DIR = os.path.join(BASE_DIR, "engineering", "master_data")
os.makedirs(MASTER_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. PARAMETER SCHEMA DEFINITION (Common schema for all parameter items)
# -----------------------------------------------------------------------------
PARAM_SCHEMA = {
    "type": "object",
    "required": ["name", "value", "unit", "basis_or_boundary", "evidence_class", "source", "uncertainty_range", "owner", "revision", "dependent_artifacts"],
    "properties": {
        "name": {"type": "string"},
        "value": {},
        "unit": {"type": "string"},
        "basis_or_boundary": {"type": "string"},
        "evidence_class": {
            "type": "string",
            "enum": ["MEASURED", "OFFICIAL_SOURCE", "CALCULATED", "SIMULATED", "ASSUMED", "HYPOTHESIS", "UNKNOWN"]
        },
        "source": {"type": "string"},
        "uncertainty_range": {},
        "owner": {"type": "string"},
        "revision": {"type": "string"},
        "dependent_artifacts": {"type": "array", "items": {"type": "string"}}
    }
}

# -----------------------------------------------------------------------------
# 2. DESIGN BASIS MASTER
# -----------------------------------------------------------------------------
DESIGN_BASIS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "DesignBasisMasterSchema",
    "type": "object",
    "required": ["metadata", "parameters"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["project_name", "document_id", "revision", "governing_flowsheet_case", "commercial_lot_id"],
            "properties": {
                "project_name": {"type": "string"},
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "governing_flowsheet_case": {"type": "string"},
                "commercial_lot_id": {"type": "string"}
            }
        },
        "parameters": {
            "type": "object",
            "additionalProperties": PARAM_SCHEMA
        }
    }
}

design_basis_data = {
    "metadata": {
        "project_name": "Harakutir 15,000 kg/day Imported Pigeon Pea Optimization Plant",
        "document_id": "ENG-MB-DB-001",
        "revision": "V5.0",
        "governing_flowsheet_case": "16h_operating_schedule_base_case",
        "commercial_lot_id": "PENDING_COMMERCIAL_LOT_ID"
    },
    "parameters": {
        "feed_intake_mass_daily": {
            "name": "Incoming Raw Dal Feed Mass",
            "value": 15000.0,
            "unit": "kg/day",
            "basis_or_boundary": "as-received as-fed raw dal at intake gate",
            "evidence_class": "OFFICIAL_SOURCE",
            "source": "Client Greenfield Scope Document Table 1",
            "uncertainty_range": "+/- 0.0 kg/day (contract basis)",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-101", "HOP-101", "DWG-FIN-15T-001", "DWG-FIN-15T-002", "DWG-FIN-15T-003"]
        },
        "feed_moisture_wb": {
            "name": "Incoming Raw Dal Moisture Content",
            "value": 10.5,
            "unit": "% wb",
            "basis_or_boundary": "as-received wet-basis (mass water / total mass)",
            "evidence_class": "MEASURED",
            "source": "Lab bench intake sample titration (ISO 6540)",
            "uncertainty_range": "9.5% - 12.0%",
            "owner": "Food Science",
            "revision": "V5.0",
            "dependent_artifacts": ["dry_solids_intake_daily", "S-101", "DR-101"]
        },
        "dry_solids_intake_daily": {
            "name": "Incoming Dal Dry Solids",
            "value": 13425.0,
            "unit": "kg/day",
            "basis_or_boundary": "dry matter basis (15000 kg * (1 - 0.105))",
            "evidence_class": "CALCULATED",
            "source": "Mass balance equation MB-01",
            "uncertainty_range": "13200 - 13575 kg/day",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-101", "S-104", "S-107", "DWG-FIN-15T-002"]
        },
        "operating_hours_nominal": {
            "name": "Nominal Daily Operating Hours",
            "value": 16.0,
            "unit": "h/day",
            "basis_or_boundary": "two 8-hour production shifts per calendar day",
            "evidence_class": "OFFICIAL_SOURCE",
            "source": "Production Operating Philosophy Rev 2",
            "uncertainty_range": "16.0 h/day (fixed schedule)",
            "owner": "Operations",
            "revision": "V5.0",
            "dependent_artifacts": ["nominal_hourly_feed_rate", "equipment_registers"]
        },
        "plant_availability_oee": {
            "name": "Plant Availability Factor (OEE Availability)",
            "value": 0.85,
            "unit": "fraction",
            "basis_or_boundary": "net operating time divided by planned production time",
            "evidence_class": "ASSUMED",
            "source": "AACE Recommended Practice 18R-97 grain mill baseline",
            "uncertainty_range": "0.80 - 0.90",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["effective_operating_hours", "design_hourly_feed_rate"]
        },
        "effective_operating_hours": {
            "name": "Effective Operating Hours",
            "value": 13.6,
            "unit": "h/day",
            "basis_or_boundary": "16.0 h/day * 0.85 availability factor",
            "evidence_class": "CALCULATED",
            "source": "Capacity model equation SCH-01",
            "uncertainty_range": "12.8 - 14.4 h/day",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["design_hourly_feed_rate", "GF-101", "DR-101"]
        },
        "nominal_hourly_feed_rate": {
            "name": "Nominal Hourly Dal Feed Rate",
            "value": 937.5,
            "unit": "kg/h",
            "basis_or_boundary": "15,000 kg/day / 16.0 nominal hours",
            "evidence_class": "CALCULATED",
            "source": "Mass balance equation MB-02",
            "uncertainty_range": "+/- 0.0 kg/h (arithmetic mean)",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["stream_table_master", "DWG-FIN-15T-002"]
        },
        "design_hourly_feed_rate": {
            "name": "Design Instantaneous Dal Feed Rate",
            "value": 1102.94,
            "unit": "kg/h",
            "basis_or_boundary": "15,000 kg/day / 13.6 effective hours (17.65% design margin)",
            "evidence_class": "CALCULATED",
            "source": "Equipment sizing equation EQ-01",
            "uncertainty_range": "1041.7 - 1171.9 kg/h",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["GF-101", "TK-101A/B", "VS-101", "DR-101"]
        },
        "soak_liquor_ratio": {
            "name": "Soak Liquor to Raw Dal Mass Ratio",
            "value": 1.50,
            "unit": "kg liquor / kg dal",
            "basis_or_boundary": "mass ratio of chemical soak solution to raw as-fed dal",
            "evidence_class": "HYPOTHESIS",
            "source": "Experimental screening protocol Candidate C-1",
            "uncertainty_range": "1.40 - 1.60",
            "owner": "Food Science",
            "revision": "V5.0",
            "dependent_artifacts": ["S-102", "TK-100", "TK-101A/B", "DWG-FIN-15T-003"]
        },
        "soak_chemical_agent": {
            "name": "Chemical Treatment Agent",
            "value": "Sodium Bicarbonate (NaHCO3, Food Grade INS 500(ii))",
            "unit": "chemical compound",
            "basis_or_boundary": "FCC / FSSAI Food Additive Grade",
            "evidence_class": "HYPOTHESIS",
            "source": "Screening Candidate Protocol",
            "uncertainty_range": "99.0% min purity",
            "owner": "Food Science",
            "revision": "V5.0",
            "dependent_artifacts": ["S-103", "SK-100", "ETP-101"]
        },
        "chemical_dose_basis_liquor": {
            "name": "Chemical Concentration on Liquor Basis",
            "value": 0.50,
            "unit": "wt% in solution",
            "basis_or_boundary": "mass of pure NaHCO3 / total mass of soak liquor (Primary Design Basis)",
            "evidence_class": "HYPOTHESIS",
            "source": "Candidate C-1 specification",
            "uncertainty_range": "0.25 - 0.75 wt%",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-103", "TK-100", "P-100A/B", "cost_model"]
        },
        "chemical_dose_basis_feed": {
            "name": "Chemical Concentration on Raw Dal Feed Basis",
            "value": 0.50,
            "unit": "wt% of dal",
            "basis_or_boundary": "mass of pure NaHCO3 / incoming as-fed dal mass (Alternative Basis)",
            "evidence_class": "HYPOTHESIS",
            "source": "Historical Dossier Comparison Note",
            "uncertainty_range": "0.333 wt% on liquor equivalent",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["BOM_RFQ_AND_CAPITAL_COST_ESTIMATE.md"]
        },
        "chemical_demand_daily_liquor_basis": {
            "name": "Daily Active Reagent Mass (Liquor Basis)",
            "value": 112.5,
            "unit": "kg/day",
            "basis_or_boundary": "22,500 kg liquor * 0.0050 wt%",
            "evidence_class": "CALCULATED",
            "source": "Reagent balance equation CHEM-01",
            "uncertainty_range": "100.0 - 125.0 kg/day",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-103", "SK-100", "BOM-005", "BOM-007"]
        },
        "soak_duration_minutes": {
            "name": "Soak Hold Time",
            "value": 30.0,
            "unit": "min",
            "basis_or_boundary": "liquid contact hold time in batch vessel",
            "evidence_class": "HYPOTHESIS",
            "source": "Screening Protocol Candidate C-1",
            "uncertainty_range": "25.0 - 35.0 min",
            "owner": "Food Science",
            "revision": "V5.0",
            "dependent_artifacts": ["TK-101A/B", "scheduling_model", "DWG-FIN-15T-003"]
        },
        "soak_water_uptake_ratio": {
            "name": "Water Uptake During Soaking",
            "value": 24.0,
            "unit": "wt% on raw feed",
            "basis_or_boundary": "mass water absorbed into cotyledon matrix / initial feed dal mass",
            "evidence_class": "MEASURED",
            "source": "Bench preliminary soaking assay",
            "uncertainty_range": "21.0 - 27.0 wt%",
            "owner": "Food Science",
            "revision": "V5.0",
            "dependent_artifacts": ["S-104", "DR-101", "DWG-FIN-15T-002"]
        },
        "wet_dal_moisture_wb": {
            "name": "Drained Dal Moisture Content Ex-Soak",
            "value": 27.8,
            "unit": "% wb",
            "basis_or_boundary": "wet basis moisture entering dryer DR-101",
            "evidence_class": "CALCULATED",
            "source": "Mass balance equation MB-03",
            "uncertainty_range": "26.0 - 29.5 % wb",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-104", "CV-101", "DR-101", "DWG-FIN-15T-005"]
        },
        "target_finished_moisture_wb": {
            "name": "Target Finished Dal Moisture Content",
            "value": 10.0,
            "unit": "% wb",
            "basis_or_boundary": "wet basis moisture of dried and cooled dal ex-dryer DR-101",
            "evidence_class": "ASSUMED",
            "source": "FSSAI standards for pulses / IS 4333 (Part II)",
            "uncertainty_range": "9.5 - 10.5 % wb",
            "owner": "Quality Assurance",
            "revision": "V5.0",
            "dependent_artifacts": ["S-107", "DR-101", "PK-101", "DWG-FIN-15T-002"]
        },
        "daily_dryer_evaporation_water": {
            "name": "Daily Water Evaporated in Dryer",
            "value": 3694.7,
            "unit": "kg/day",
            "basis_or_boundary": "net water mass transferred to drying air exhaust",
            "evidence_class": "CALCULATED",
            "source": "Dryer water balance equation DRY-01",
            "uncertainty_range": "3500 - 3900 kg/day",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-106", "DR-101", "FN-101", "HX-101"]
        },
        "dryer_thermal_duty_kwth": {
            "name": "Fluid Bed Dryer Design Heat Duty",
            "value": 512.4,
            "unit": "kWth",
            "basis_or_boundary": "thermal energy delivered to fluidizing air coil HX-101",
            "evidence_class": "CALCULATED",
            "source": "Psychrometric & enthalpy balance equation DRY-02",
            "uncertainty_range": "480 - 540 kWth",
            "owner": "Thermal Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["HX-101", "BOIL-101", "L-112-40-CS", "DWG-FIN-15T-005"]
        },
        "whole_plant_dry_solids_recovery": {
            "name": "Whole-Plant Net Dry Solids Recovery",
            "value": 98.62,
            "unit": "%",
            "basis_or_boundary": "dry solids in finished product / dry solids in incoming feed dal",
            "evidence_class": "CALCULATED",
            "source": "Authoritative Solids Balance V5 (0.91% soak leach + 0.47% cyclone fines)",
            "uncertainty_range": "98.0 - 99.0 %",
            "owner": "Process Engineering",
            "revision": "V5.0",
            "dependent_artifacts": ["S-107", "saleable_finished_product_daily", "DWG-FIN-15T-002"]
        },
        "saleable_finished_product_daily": {
            "name": "Daily Saleable Finished Product Mass",
            "value": 14711.1,
            "unit": "kg/day",
            "basis_or_boundary": "13,240.0 kg dry solids at 10.0% wb moisture",
            "evidence_class": "CALCULATED",
            "source": "Commercial yield equation YLD-01",
            "uncertainty_range": "14500 - 14900 kg/day",
            "owner": "Commercial & Process",
            "revision": "V5.0",
            "dependent_artifacts": ["S-107", "PK-101", "HOP-102", "DWG-FIN-15T-006"]
        }
    }
}

# -----------------------------------------------------------------------------
# 3. STREAM TABLE MASTER
# -----------------------------------------------------------------------------
STREAM_TABLE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "StreamTableMasterSchema",
    "type": "object",
    "required": ["metadata", "streams"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["document_id", "revision", "operating_basis"],
            "properties": {
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "operating_basis": {"type": "string"}
            }
        },
        "streams": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["tag", "name", "from_equipment", "to_equipment", "phase", "temp_c", "press_bar_g",
                             "flow_daily_kg", "flow_nominal_kg_h", "flow_design_kg_h",
                             "dry_solids_pct", "water_pct", "solute_pct", "evidence_class", "source"],
                "properties": {
                    "tag": {"type": "string"},
                    "name": {"type": "string"},
                    "from_equipment": {"type": "string"},
                    "to_equipment": {"type": "string"},
                    "phase": {"type": "string"},
                    "temp_c": {"type": "number"},
                    "press_bar_g": {"type": "number"},
                    "flow_daily_kg": {"type": "number"},
                    "flow_nominal_kg_h": {"type": "number"},
                    "flow_design_kg_h": {"type": "number"},
                    "dry_solids_pct": {"type": "number"},
                    "water_pct": {"type": "number"},
                    "solute_pct": {"type": "number"},
                    "evidence_class": {"type": "string"},
                    "source": {"type": "string"}
                }
            }
        }
    }
}

stream_table_data = {
    "metadata": {
        "document_id": "ENG-MB-ST-001",
        "revision": "V5.0",
        "operating_basis": "15,000 kg/day incoming dal, 16 operating hours/day (nominal 937.5 kg/h, design 1102.94 kg/h)"
    },
    "streams": {
        "S-101": {
            "tag": "S-101",
            "name": "Raw Dal Feed",
            "from_equipment": "HOP-101",
            "to_equipment": "GF-101",
            "phase": "Solid (Granular)",
            "temp_c": 25.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 15000.0,
            "flow_nominal_kg_h": 937.50,
            "flow_design_kg_h": 1102.94,
            "dry_solids_pct": 89.50,
            "water_pct": 10.50,
            "solute_pct": 0.00,
            "evidence_class": "OFFICIAL_SOURCE",
            "source": "Design Basis 15 TPD"
        },
        "S-102": {
            "tag": "S-102",
            "name": "Fresh Process Water to Dosing",
            "from_equipment": "Utility Soft Water Header",
            "to_equipment": "TK-100",
            "phase": "Liquid",
            "temp_c": 25.0,
            "press_bar_g": 3.0,
            "flow_daily_kg": 22387.5,
            "flow_nominal_kg_h": 1399.22,
            "flow_design_kg_h": 1646.14,
            "dry_solids_pct": 0.00,
            "water_pct": 100.00,
            "solute_pct": 0.00,
            "evidence_class": "CALCULATED",
            "source": "Solution mass balance"
        },
        "S-103": {
            "tag": "S-103",
            "name": "Active Chemical Reagent (NaHCO3)",
            "from_equipment": "Chemical Bag Unloader",
            "to_equipment": "TK-100",
            "phase": "Solid (Powder)",
            "temp_c": 25.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 112.5,
            "flow_nominal_kg_h": 7.03,
            "flow_design_kg_h": 8.27,
            "dry_solids_pct": 0.00,
            "water_pct": 0.00,
            "solute_pct": 100.00,
            "evidence_class": "HYPOTHESIS",
            "source": "0.50 wt% in soak liquor"
        },
        "S-104": {
            "tag": "S-104",
            "name": "Prepared Soak Solution",
            "from_equipment": "TK-100",
            "to_equipment": "TK-101A/B",
            "phase": "Liquid",
            "temp_c": 25.0,
            "press_bar_g": 2.5,
            "flow_daily_kg": 22500.0,
            "flow_nominal_kg_h": 1406.25,
            "flow_design_kg_h": 1654.41,
            "dry_solids_pct": 0.00,
            "water_pct": 99.50,
            "solute_pct": 0.50,
            "evidence_class": "CALCULATED",
            "source": "1:1.5 mass liquor ratio"
        },
        "S-105": {
            "tag": "S-105",
            "name": "Soaked Dal Slurry",
            "from_equipment": "TK-101A/B",
            "to_equipment": "VS-101",
            "phase": "Slurry (Solid-Liquid)",
            "temp_c": 28.0,
            "press_bar_g": 1.5,
            "flow_daily_kg": 37500.0,
            "flow_nominal_kg_h": 2343.75,
            "flow_design_kg_h": 2757.35,
            "dry_solids_pct": 35.80,
            "water_pct": 63.90,
            "solute_pct": 0.30,
            "evidence_class": "CALCULATED",
            "source": "Combined batch slurry"
        },
        "S-106": {
            "tag": "S-106",
            "name": "Combined Effluent to ETP / ZLD",
            "from_equipment": "VS-101 / Drain Sump",
            "to_equipment": "P-102 / EV-101",
            "phase": "Liquid",
            "temp_c": 28.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 21280.14,
            "flow_nominal_kg_h": 1330.01,
            "flow_design_kg_h": 1564.72,
            "dry_solids_pct": 0.60334,
            "water_pct": 98.87904,
            "solute_pct": 0.51762,
            "evidence_class": "CALCULATED",
            "source": "Combined liquor drain & screen rinse effluent"
        },
        "S-107": {
            "tag": "S-107",
            "name": "Fresh Rinse Water Mist",
            "from_equipment": "Utility Header",
            "to_equipment": "VS-101 Spray Bar",
            "phase": "Liquid",
            "temp_c": 25.0,
            "press_bar_g": 3.0,
            "flow_daily_kg": 2250.0,
            "flow_nominal_kg_h": 140.63,
            "flow_design_kg_h": 165.44,
            "dry_solids_pct": 0.00,
            "water_pct": 100.00,
            "solute_pct": 0.00,
            "evidence_class": "ASSUMED",
            "source": "15% rinse ratio on feed"
        },
        "S-108": {
            "tag": "S-108",
            "name": "Wet Drained Dal to Dryer",
            "from_equipment": "VS-101",
            "to_equipment": "CV-101 / DR-101",
            "phase": "Solid (Wet Grains)",
            "temp_c": 28.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 18469.77,
            "flow_nominal_kg_h": 1154.36,
            "flow_design_kg_h": 1358.07,
            "dry_solids_pct": 72.01,
            "water_pct": 27.98,
            "solute_pct": 0.01,
            "evidence_class": "CALCULATED",
            "source": "Dewatering balance"
        },
        "S-109": {
            "tag": "S-109",
            "name": "Dryer Evaporated Water Vapor",
            "from_equipment": "DR-101",
            "to_equipment": "CYC-101 / BH-101",
            "phase": "Gas / Vapor",
            "temp_c": 42.0,
            "press_bar_g": -0.005,
            "flow_daily_kg": 3693.25,
            "flow_nominal_kg_h": 230.83,
            "flow_design_kg_h": 271.56,
            "dry_solids_pct": 0.00,
            "water_pct": 100.00,
            "solute_pct": 0.00,
            "evidence_class": "CALCULATED",
            "source": "Evaporation balance"
        },
        "S-110": {
            "tag": "S-110",
            "name": "Cyclone Entrained Fines",
            "from_equipment": "CYC-101",
            "to_equipment": "Fines Drum / Disposal",
            "phase": "Solid (Dust)",
            "temp_c": 40.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 62.90,
            "flow_nominal_kg_h": 3.93,
            "flow_design_kg_h": 4.63,
            "dry_solids_pct": 90.00,
            "water_pct": 10.00,
            "solute_pct": 0.00,
            "evidence_class": "ESTIMATED",
            "source": "0.47% attrition loss"
        },
        "S-111": {
            "tag": "S-111",
            "name": "Dried Cooled Dal Ex-Dryer",
            "from_equipment": "CLR-101",
            "to_equipment": "EL-102",
            "phase": "Solid (Granular)",
            "temp_c": 28.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 14713.62,
            "flow_nominal_kg_h": 919.60,
            "flow_design_kg_h": 1081.88,
            "dry_solids_pct": 89.984,
            "water_pct": 10.000,
            "solute_pct": 0.016,
            "evidence_class": "CALCULATED",
            "source": "Dryer product mass"
        },
        "S-112": {
            "tag": "S-112",
            "name": "Polished Saleable Dal to Packing",
            "from_equipment": "SCN-102",
            "to_equipment": "PK-101",
            "phase": "Solid (Granular)",
            "temp_c": 28.0,
            "press_bar_g": 0.0,
            "flow_daily_kg": 14713.62,
            "flow_nominal_kg_h": 919.60,
            "flow_design_kg_h": 1081.88,
            "dry_solids_pct": 89.984,
            "water_pct": 10.000,
            "solute_pct": 0.016,
            "evidence_class": "CALCULATED",
            "source": "Final saleable product"
        },
        "S-113": {
            "tag": "S-113",
            "name": "Saturated Steam Supply to Dryer",
            "from_equipment": "BOIL-101",
            "to_equipment": "HX-101",
            "phase": "Vapor",
            "temp_c": 138.8,
            "press_bar_g": 2.5,
            "flow_daily_kg": 10676.0,
            "flow_nominal_kg_h": 667.25,
            "flow_design_kg_h": 785.00,
            "dry_solids_pct": 0.00,
            "water_pct": 100.00,
            "solute_pct": 0.00,
            "evidence_class": "CALCULATED",
            "source": "Dryer 512 kWth duty"
        },
        "S-114": {
            "tag": "S-114",
            "name": "ZLD Distillate Recycle Water",
            "from_equipment": "EV-101 Condenser",
            "to_equipment": "Process Water Tank",
            "phase": "Liquid",
            "temp_c": 45.0,
            "press_bar_g": 1.0,
            "flow_daily_kg": 15680.0,
            "flow_nominal_kg_h": 980.00,
            "flow_design_kg_h": 1152.94,
            "dry_solids_pct": 0.00,
            "water_pct": 100.00,
            "solute_pct": 0.00,
            "evidence_class": "SIMULATED",
            "source": "Aspen Plus V14 converged model"
        }
    }
}

# -----------------------------------------------------------------------------
# 4. EQUIPMENT REGISTER MASTER
# -----------------------------------------------------------------------------
EQUIP_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "EquipmentRegisterMasterSchema",
    "type": "object",
    "required": ["metadata", "equipment"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["document_id", "revision", "total_equipment_count"],
            "properties": {
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "total_equipment_count": {"type": "integer"}
            }
        },
        "equipment": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["tag", "name", "area_zone", "service", "capacity_rating", "dimensions_m",
                             "wetted_material", "structural_material", "motor_kw", "design_status", "cad_model_ref"],
                "properties": {
                    "tag": {"type": "string"},
                    "name": {"type": "string"},
                    "area_zone": {"type": "string"},
                    "service": {"type": "string"},
                    "capacity_rating": {"type": "string"},
                    "dimensions_m": {"type": "object"},
                    "wetted_material": {"type": "string"},
                    "structural_material": {"type": "string"},
                    "motor_kw": {"type": "number"},
                    "design_status": {"type": "string"},
                    "cad_model_ref": {"type": "string"}
                }
            }
        }
    }
}

# Read existing CSV and enrich with CAD references
import csv

equip_csv_path = os.path.join(BASE_DIR, "engineering", "registers", "master_equipment_register.csv")
equip_dict = {}
with open(equip_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tag = row["Tag"]
        # extract numeric motor kw
        m_str = row["Motor_kW"].split()[0]
        try:
            m_kw = float(m_str)
        except ValueError:
            m_kw = 0.0
            
        cad_ref = "PLANT-15T_General_Arrangement.SLDASM"
        if "TK-101" in tag:
            cad_ref = "TK-101_Soak_Tank.SLDPRT"
        elif "DR-101" in tag:
            cad_ref = "DR-101_Fluid_Bed_Dryer.SLDPRT"
        elif "SK-100" in tag or "TK-100" in tag:
            cad_ref = "SK-100_Dosing_Skid.SLDPRT"
        elif "AG-101" in tag:
            cad_ref = "AG-101_Agitator.SLDPRT"

        equip_dict[tag] = {
            "tag": tag,
            "name": row["Equipment_Name"],
            "area_zone": row["Area_Zone"],
            "service": row["Service_Description"],
            "capacity_rating": row["Capacity_Rating"],
            "dimensions_m": {
                "raw_text": row["Dimensions_L_W_H_m"]
            },
            "wetted_material": row["Material_Wetted"],
            "structural_material": row["Material_Structural"],
            "motor_kw": m_kw,
            "design_status": row["Design_Status"],
            "cad_model_ref": cad_ref
        }

equipment_master_data = {
    "metadata": {
        "document_id": "ENG-MB-EQ-001",
        "revision": "V5.0",
        "total_equipment_count": len(equip_dict)
    },
    "equipment": equip_dict
}

# -----------------------------------------------------------------------------
# 5. LINE LIST MASTER
# -----------------------------------------------------------------------------
LINE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "LineListMasterSchema",
    "type": "object",
    "required": ["metadata", "lines"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["document_id", "revision", "total_line_count"],
            "properties": {
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "total_line_count": {"type": "integer"}
            }
        },
        "lines": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["line_number", "from_equipment", "to_equipment", "nominal_size_nb", "pipe_class",
                             "fluid_service", "design_pressure_bar", "operating_temp_c", "pid_drawing_no"],
                "properties": {
                    "line_number": {"type": "string"},
                    "from_equipment": {"type": "string"},
                    "to_equipment": {"type": "string"},
                    "nominal_size_nb": {"type": "string"},
                    "pipe_class": {"type": "string"},
                    "fluid_service": {"type": "string"},
                    "design_pressure_bar": {"type": "string"},
                    "operating_temp_c": {"type": "string"},
                    "pid_drawing_no": {"type": "string"}
                }
            }
        }
    }
}

line_csv_path = os.path.join(BASE_DIR, "engineering", "registers", "line_list.csv")
lines_dict = {}
with open(line_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        num = row["Line_Number"]
        lines_dict[num] = {
            "line_number": num,
            "from_equipment": row["From_Equipment"],
            "to_equipment": row["To_Equipment"],
            "nominal_size_nb": row["Nominal_Size_NB"],
            "pipe_class": row["Pipe_Class"],
            "fluid_service": row["Fluid_Service"],
            "design_pressure_bar": row["Design_Pressure_bar"],
            "operating_temp_c": row["Operating_Temp_C"],
            "pid_drawing_no": row["P_and_ID_No"]
        }

line_master_data = {
    "metadata": {
        "document_id": "ENG-MB-LL-001",
        "revision": "V5.0",
        "total_line_count": len(lines_dict)
    },
    "lines": lines_dict
}

# -----------------------------------------------------------------------------
# 6. INSTRUMENT INDEX MASTER
# -----------------------------------------------------------------------------
INST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "InstrumentIndexMasterSchema",
    "type": "object",
    "required": ["metadata", "instruments"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["document_id", "revision", "total_instrument_count"],
            "properties": {
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "total_instrument_count": {"type": "integer"}
            }
        },
        "instruments": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["tag", "description", "service_location", "measured_variable", "range_units",
                             "output_signal", "trip_interlock", "pid_drawing_no"],
                "properties": {
                    "tag": {"type": "string"},
                    "description": {"type": "string"},
                    "service_location": {"type": "string"},
                    "measured_variable": {"type": "string"},
                    "range_units": {"type": "string"},
                    "output_signal": {"type": "string"},
                    "trip_interlock": {"type": "string"},
                    "pid_drawing_no": {"type": "string"}
                }
            }
        }
    }
}

inst_csv_path = os.path.join(BASE_DIR, "engineering", "registers", "instrument_index.csv")
inst_dict = {}
with open(inst_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tag = row["Tag"]
        inst_dict[tag] = {
            "tag": tag,
            "description": row["Description"],
            "service_location": row["Service_Location"],
            "measured_variable": row["Measured_Variable"],
            "range_units": row["Range_Units"],
            "output_signal": row["Output_Signal"],
            "trip_interlock": row["Trip_Interlock"],
            "pid_drawing_no": row["P_and_ID_No"]
        }

instrument_master_data = {
    "metadata": {
        "document_id": "ENG-MB-IN-001",
        "revision": "V5.0",
        "total_instrument_count": len(inst_dict)
    },
    "instruments": inst_dict
}

# -----------------------------------------------------------------------------
# 7. MOTOR LOAD MASTER
# -----------------------------------------------------------------------------
MOTOR_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "MotorLoadMasterSchema",
    "type": "object",
    "required": ["metadata", "motors"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["document_id", "revision", "total_motor_count", "total_connected_kw", "total_operating_kw"],
            "properties": {
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "total_motor_count": {"type": "integer"},
                "total_connected_kw": {"type": "number"},
                "total_operating_kw": {"type": "number"}
            }
        },
        "motors": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["equipment_tag", "motor_description", "area_zone", "rated_kw", "voltage",
                             "starter_type", "vfd_required", "operating_kw_base"],
                "properties": {
                    "equipment_tag": {"type": "string"},
                    "motor_description": {"type": "string"},
                    "area_zone": {"type": "string"},
                    "rated_kw": {"type": "number"},
                    "voltage": {"type": "string"},
                    "starter_type": {"type": "string"},
                    "vfd_required": {"type": "boolean"},
                    "operating_kw_base": {"type": "number"}
                }
            }
        }
    }
}

motor_csv_path = os.path.join(BASE_DIR, "engineering", "registers", "motor_load_list.csv")
motor_dict = {}
total_conn_kw = 0.0
total_oper_kw = 0.0
with open(motor_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tag = row["Equipment_Tag"]
        r_kw = float(row["Rated_kW"])
        o_kw = float(row["Operating_kW_Base"])
        total_conn_kw += r_kw
        total_oper_kw += o_kw
        vfd_bool = (row["VFD_Required"].strip().lower() == "yes")
        
        motor_dict[tag] = {
            "equipment_tag": tag,
            "motor_description": row["Motor_Description"],
            "area_zone": row["Area_Zone"],
            "rated_kw": r_kw,
            "voltage": row["Voltage_V"],
            "starter_type": row["Starter_Type"],
            "vfd_required": vfd_bool,
            "operating_kw_base": o_kw
        }

motor_master_data = {
    "metadata": {
        "document_id": "ENG-MB-ML-001",
        "revision": "V5.0",
        "total_motor_count": len(motor_dict),
        "total_connected_kw": round(total_conn_kw, 2),
        "total_operating_kw": round(total_oper_kw, 2)
    },
    "motors": motor_dict
}

# -----------------------------------------------------------------------------
# 8. BOM MASTER
# -----------------------------------------------------------------------------
BOM_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "BOMMasterSchema",
    "type": "object",
    "required": ["metadata", "items"],
    "properties": {
        "metadata": {
            "type": "object",
            "required": ["document_id", "revision", "total_line_items", "total_capex_lakhs_inr"],
            "properties": {
                "document_id": {"type": "string"},
                "revision": {"type": "string"},
                "total_line_items": {"type": "integer"},
                "total_capex_lakhs_inr": {"type": "number"}
            }
        },
        "items": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["item_no", "category", "tag", "description", "qty", "unit",
                             "material_grade", "procurement_type", "unit_cost_lakhs_inr",
                             "total_cost_lakhs_inr", "cost_confidence_class", "lead_time_weeks"],
                "properties": {
                    "item_no": {"type": "string"},
                    "category": {"type": "string"},
                    "tag": {"type": "string"},
                    "description": {"type": "string"},
                    "qty": {"type": "number"},
                    "unit": {"type": "string"},
                    "material_grade": {"type": "string"},
                    "procurement_type": {"type": "string"},
                    "unit_cost_lakhs_inr": {"type": "number"},
                    "total_cost_lakhs_inr": {"type": "number"},
                    "cost_confidence_class": {"type": "string"},
                    "lead_time_weeks": {"type": "integer"}
                }
            }
        }
    }
}

bom_csv_path = os.path.join(BASE_DIR, "engineering", "procurement", "itemized_bom.csv")
bom_dict = {}
total_capex = 0.0
with open(bom_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        item_no = row["Item_No"]
        t_cost = float(row["Total_Cost_Lakhs_INR"])
        total_capex += t_cost
        bom_dict[item_no] = {
            "item_no": item_no,
            "category": row["Category"],
            "tag": row["Tag"],
            "description": row["Description"],
            "qty": float(row["Qty"]),
            "unit": row["Unit"],
            "material_grade": row["Material_Grade"],
            "procurement_type": row["Procurement_Type"],
            "unit_cost_lakhs_inr": float(row["Unit_Cost_Lakhs_INR"]),
            "total_cost_lakhs_inr": t_cost,
            "cost_confidence_class": row["Cost_Confidence_Class"],
            "lead_time_weeks": int(row["Lead_Time_Weeks"])
        }

bom_master_data = {
    "metadata": {
        "document_id": "ENG-MB-BM-001",
        "revision": "V5.0",
        "total_line_items": len(bom_dict),
        "total_capex_lakhs_inr": round(total_capex, 2)
    },
    "items": bom_dict
}

# -----------------------------------------------------------------------------
# 9. INTEGRATION INTERFACE MATRIX
# -----------------------------------------------------------------------------
integration_interface_matrix = {
    "metadata": {
        "document_id": "ENG-MB-IM-001",
        "revision": "V5.0",
        "scope": "CAD - Simulation - Master Data Cross-Discipline Mapping"
    },
    "interfaces": [
        {
            "tag": "FEED_INTAKE",
            "authoritative_source": "design_basis_master.json::feed_intake_mass_daily",
            "consuming_models": ["plant_design_15tpd.py", "stream_table_master.json"],
            "native_objects": ["HOP-101", "GF-101", "PLANT-15T_General_Arrangement.SLDASM"],
            "drawings_registers": ["DWG-FIN-15T-001", "DWG-FIN-15T-002", "DWG-FIN-15T-003", "master_equipment_register.csv"],
            "independent_verification": "tests/test_plant_design_and_mass_balance.py",
            "regeneration_trigger": "Change in daily client throughput quota"
        },
        {
            "tag": "TK-101A/B",
            "authoritative_source": "equipment_register_master.json::TK-101A",
            "consuming_models": ["plant_design_15tpd.py", "TK-101_Soak_Tank.SLDPRT"],
            "native_objects": ["TK-101_Soak_Tank.SLDPRT", "TK-101_Soak_Tank.step", "PLANT-15T_General_Arrangement.SLDASM"],
            "drawings_registers": ["DWG-FIN-15T-003", "DWG-FIN-15T-007", "DWG-FIN-15T-007_SOLIDWORKS_MODEL_DERIVED.pdf"],
            "independent_verification": "SolidWorks live API COM mass properties check (Volume 5.86 m3, height 2.50m, dia 1.80m)",
            "regeneration_trigger": "Change in soak duration, swelling ratio, or batch schedule"
        },
        {
            "tag": "DR-101",
            "authoritative_source": "equipment_register_master.json::DR-101",
            "consuming_models": ["drying_model.py", "DR-101_Fluid_Bed_Dryer.SLDPRT"],
            "native_objects": ["DR-101_Fluid_Bed_Dryer.SLDPRT", "DR-101_Fluid_Bed_Dryer.step", "PLANT-15T_General_Arrangement.SLDASM"],
            "drawings_registers": ["DWG-FIN-15T-005", "DWG-FIN-15T-008", "master_equipment_register.csv"],
            "independent_verification": "Psychrometric water evaporation balance (3694.7 kg/d = 512.4 kWth steam heat)",
            "regeneration_trigger": "Change in wet dal feed moisture or target finished moisture"
        },
        {
            "tag": "SK-100",
            "authoritative_source": "equipment_register_master.json::TK-100",
            "consuming_models": ["plant_design_15tpd.py", "SK-100_Dosing_Skid.SLDPRT"],
            "native_objects": ["SK-100_Dosing_Skid.SLDPRT", "SK-100_Dosing_Skid.step", "PLANT-15T_General_Arrangement.SLDASM"],
            "drawings_registers": ["DWG-FIN-15T-003", "DWG-FIN-15T-009", "itemized_bom.csv"],
            "independent_verification": "SolidWorks live API volume and bounding box check (1.4m dia x 1.8m height)",
            "regeneration_trigger": "Change in chemical recipe concentration basis (liquor vs feed)"
        },
        {
            "tag": "EV-101A/B/C",
            "authoritative_source": "HARAKUTIR_15TPD_CONVERGED.bkp",
            "consuming_models": ["Aspen Plus V14 Apwn.Document", "plant_design_15tpd.py"],
            "native_objects": ["COIL-1/2/3", "STAGE-1/2/3", "PLANT-15T_General_Arrangement.SLDASM"],
            "drawings_registers": ["DWG-FIN-15T-010", "itemized_bom.csv", "UTILITY_WASTEWATER_AND_ENVIRONMENTAL_DESIGN.md"],
            "independent_verification": "Converged Aspen Plus V14 block balance: 2.38 steam economy, 310.5 kWth duty, 980 kg/h distillate",
            "regeneration_trigger": "Change in spent soak liquor volume or ZLD environmental consent"
        },
        {
            "tag": "MCC-415V",
            "authoritative_source": "motor_load_master.json",
            "consuming_models": ["single_line_diagram", "plant_design_15tpd.py"],
            "native_objects": ["MCC-101", "PLANT-15T_General_Arrangement.SLDASM"],
            "drawings_registers": ["DWG-FIN-15T-011", "motor_load_list.csv", "ELECTRICAL_LOAD_AND_AUTOMATION_DESIGN.md"],
            "independent_verification": "Summation of rated loads (73.74 kW connected, 54.45 kW operating)",
            "regeneration_trigger": "Addition or resizing of motor-driven equipment"
        }
    ]
}

# -----------------------------------------------------------------------------
# 10. WRITE AND VALIDATE ALL MASTER FILES
# -----------------------------------------------------------------------------
files_to_validate = [
    ("design_basis_master.json", design_basis_data, "design_basis_master.schema.json", DESIGN_BASIS_SCHEMA),
    ("stream_table_master.json", stream_table_data, "stream_table_master.schema.json", STREAM_TABLE_SCHEMA),
    ("equipment_register_master.json", equipment_master_data, "equipment_register_master.schema.json", EQUIP_SCHEMA),
    ("line_list_master.json", line_master_data, "line_list_master.schema.json", LINE_SCHEMA),
    ("instrument_index_master.json", instrument_master_data, "instrument_index_master.schema.json", INST_SCHEMA),
    ("motor_load_master.json", motor_master_data, "motor_load_master.schema.json", MOTOR_SCHEMA),
    ("bom_master.json", bom_master_data, "bom_master.schema.json", BOM_SCHEMA),
]

print("=== V5 MASTER DATA GENERATION AND SCHEMA VALIDATION ===")
for data_name, data_content, schema_name, schema_content in files_to_validate:
    schema_path = os.path.join(MASTER_DIR, schema_name)
    data_path = os.path.join(MASTER_DIR, data_name)
    
    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(schema_content, f, indent=2)
        
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data_content, f, indent=2)
        
    # Perform strict JSON schema validation
    try:
        jsonschema.validate(instance=data_content, schema=schema_content)
        print(f"[PASS] {data_name} conforms strictly to {schema_name}")
    except jsonschema.ValidationError as e:
        print(f"[FAIL] {data_name} validation error: {e.message}")
        raise e

# Write Interface Matrix
matrix_path = os.path.join(MASTER_DIR, "integration_interface_matrix.json")
with open(matrix_path, "w", encoding="utf-8") as f:
    json.dump(integration_interface_matrix, f, indent=2)
print("[PASS] integration_interface_matrix.json written successfully.")

print("\nAll Master Data files generated and validated successfully under engineering/master_data/")
