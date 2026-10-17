// FinnoaQ 15 TPD Plant Authentic Engineering Data Model
// Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati | Academic Guidance: Dr. Archisman Ray (IIT Kharagpur)

export const PROJECT_METADATA = {
  ref: "FNQ-PR-2026-001",
  title: "15,000 kg/day Tanzanian Toor Dal Rapid-Hydration & Conditioning Plant Concept",
  leadEngineer: "Sourish Senapati",
  company: "FinnoaQ Agro-Industrial Technologies Ltd.",
  advisory: "Dr. Archisman Ray",
  institution: "Dept. of Chemical Engineering, IIT Kharagpur",
  capacity: "15,000 kg/day (15 TPD)",
  capex: "$1,482,000 (INR 12.30 Cr)",
  opex: "$0.084 / kg processed",
  irr: "28.4% (Payback: 2.3 Years)",
  governance: "ASME Sec VIII Div 1 / NFPA 68 / ISA-88 / FSSAI / IS 800",
  status: "Conceptual FEED Baseline | Gate G-A Experimental Hold Active"
};

export const EQUIPMENT_SPECS = {
  "TK-101_Soak_Tank": {
    tag: "TK-101A",
    name: "Rapid-Hydration Soak Vessel Alpha",
    category: "Hydration Battery",
    designCode: "ASME Section VIII Div 1 / IS 2825 Class 2",
    dimensions: "2,000 mm ID x 2,200 mm Tan-to-Tan x 3,630 mm OAL",
    volume: "7.5 m3 working (8.85 m3 gross)",
    emptyWeight: "3,250 kg",
    fullWeight: "8,850 kg full operating",
    moc: "AISI SS304 (Shell & Cone) / SS316L (Contact Welds)",
    operatingTemp: "55°C - 65°C controlled",
    operatingPress: "Atmospheric (Hydrostatic head 0.36 bar)",
    motorKw: "4.0 kW (IE3 Inverter-Duty)",
    scadaTag: "LIC-101A / TIC-101A / ZIC-101A",
    nozzles: [
      { tag: "N1", size: "DN80 PN16", desc: "Water Infeed Header" },
      { tag: "N2", size: "DN200 PN10", desc: "Dry Dal Solid Gravity Infeed" },
      { tag: "N3", size: "DN100 PN16", desc: "Safety Overflow to Drain" },
      { tag: "N4", size: "DN40 Sanitary", desc: "Chemical Dosing Ingress" },
      { tag: "N5", size: "DN150 ASME 150#", desc: "Bottom Slurry Dump Nozzle" },
      { tag: "N6", size: "DN50 PN16", desc: "CIP Spray Ball Connection" },
      { tag: "M1", size: "DN500 Oval", desc: "Quick-Opening Pressure Manway" }
    ],
    description: "Cylindrical vertical dished vessel with 60° steep discharge cone. Incorporates 4 anti-swirl baffles and internal orbital sanitary polish (Ra < 0.4 um) to guarantee zero grain hang-up."
  },
  "TK-101_Soak_Tank_1": {
    tag: "TK-101B",
    name: "Rapid-Hydration Soak Vessel Beta",
    category: "Hydration Battery",
    designCode: "ASME Section VIII Div 1 / IS 2825 Class 2",
    dimensions: "2,000 mm ID x 2,200 mm Tan-to-Tan x 3,630 mm OAL",
    volume: "7.5 m3 working (8.85 m3 gross)",
    emptyWeight: "3,250 kg",
    fullWeight: "8,850 kg full operating",
    moc: "AISI SS304 (Shell & Cone) / SS316L (Contact Welds)",
    operatingTemp: "55°C - 65°C controlled",
    operatingPress: "Atmospheric (Hydrostatic head 0.36 bar)",
    motorKw: "4.0 kW (IE3 Inverter-Duty)",
    scadaTag: "LIC-101B / TIC-101B / ZIC-101B",
    nozzles: [
      { tag: "N1", size: "DN80 PN16", desc: "Water Infeed Header" },
      { tag: "N2", size: "DN200 PN10", desc: "Dry Dal Solid Gravity Infeed" },
      { tag: "N3", size: "DN100 PN16", desc: "Safety Overflow to Drain" },
      { tag: "N4", size: "DN40 Sanitary", desc: "Chemical Dosing Ingress" },
      { tag: "N5", size: "DN150 ASME 150#", desc: "Bottom Slurry Dump Nozzle" },
      { tag: "N6", size: "DN50 PN16", desc: "CIP Spray Ball Connection" },
      { tag: "M1", size: "DN500 Oval", desc: "Quick-Opening Pressure Manway" }
    ],
    description: "Mirror twin of TK-101A operating in synchronized staggered cyclic batch mode to sustain continuous 1,875 kg/h slurry feed to the downstream dewatering screen."
  },
  "AG-101_Agitator": {
    tag: "AG-101A",
    name: "Low-Shear Hydrofoil Agitator Alpha",
    category: "Agitation & Mixing",
    designCode: "DIN 28161 / AGMA 6010-F97",
    dimensions: "Shaft Dia 60 mm x 2,800 mm L; Impeller Dia 800 mm",
    volume: "N/A",
    emptyWeight: "245 kg",
    fullWeight: "245 kg",
    moc: "Solid SS316L Shaft & High-Efficiency A310 Hydrofoil Blades",
    operatingTemp: "Up to 80°C",
    operatingPress: "Atmospheric",
    motorKw: "4.0 kW (415V / 50Hz / 1,440 RPM Gearmotor via VFD to 45-65 RPM)",
    scadaTag: "SIC-101A / II-101A",
    nozzles: [],
    description: "Gentle axial-flow hydrofoil impeller designed to gently suspend dense pulse grains without inducing cotyledon fracture, shear attrition, or starch release into the soak liquor."
  },
  "AG-101_Agitator_1": {
    tag: "AG-101B",
    name: "Low-Shear Hydrofoil Agitator Beta",
    category: "Agitation & Mixing",
    designCode: "DIN 28161 / AGMA 6010-F97",
    dimensions: "Shaft Dia 60 mm x 2,800 mm L; Impeller Dia 800 mm",
    volume: "N/A",
    emptyWeight: "245 kg",
    fullWeight: "245 kg",
    moc: "Solid SS316L Shaft & High-Efficiency A310 Hydrofoil Blades",
    operatingTemp: "Up to 80°C",
    operatingPress: "Atmospheric",
    motorKw: "4.0 kW (415V / 50Hz / 1,440 RPM Gearmotor via VFD to 45-65 RPM)",
    scadaTag: "SIC-101B / II-101B",
    nozzles: [],
    description: "Twin agitator unit for TK-101B ensuring uniform thermal distribution and active salt contact during conditioning cycle."
  },
  "CHU-100_Transfer_Chutes": {
    tag: "CHU-100",
    name: "Converging Gravity Slurry Chute Suite",
    category: "Solids Handling",
    designCode: "CEMA Standard 550 / Sanitary Food Handling",
    dimensions: "Dual DN150 legs merging into 400 mm x 300 mm flanged feed spool",
    volume: "N/A",
    emptyWeight: "380 kg",
    fullWeight: "620 kg operating flow",
    moc: "AISI SS304 mirror finish, 3.0 mm wall thickness",
    operatingTemp: "Ambient to 65°C",
    operatingPress: "Gravity Fall",
    motorKw: "Pneumatically Actuated Diverter Valves (6.0 bar air)",
    scadaTag: "XV-101A / XV-101B / ZSO-101",
    nozzles: [],
    description: "Engineered with a steep 52.65° incline exceeding the internal friction angle of saturated pigeon peas (38°), ensuring instantaneous, blockage-free discharge to the dewatering screen."
  },
  "SC-101_Dewatering_Screen": {
    tag: "SC-101",
    name: "High-Frequency Vibratory Dewatering Screen",
    category: "Solid-Liquid Separation",
    designCode: "ISO 2194 / FSSAI GMP",
    dimensions: "2,400 mm L x 800 mm W x 1,200 mm H",
    volume: "Dewatering Capacity: 2,500 kg/h solids + 3,500 kg/h free liquor",
    emptyWeight: "520 kg",
    fullWeight: "710 kg operating",
    moc: "SS304 contact frame, wedge-wire deck (0.5 mm aperture SS316)",
    operatingTemp: "Ambient to 65°C",
    operatingPress: "Atmospheric",
    motorKw: "2 x 1.5 kW Unbalanced Motor Exciters (3.0 kW total)",
    scadaTag: "MC-SC101 / VI-101",
    nozzles: [
      { tag: "EFF-1", size: "DN100 PN10", desc: "Effluent Drain to Evaporator Catch Tank" }
    ],
    description: "Wedge-wire linear motion screen separating 98.5% of free surface water from soaked dal, dropping surface moisture to < 18% w/w prior to dryer infeed."
  },
  "DR-101_Fluid_Bed_Dryer": {
    tag: "DR-101",
    name: "Continuous Multi-Zone Fluid Bed Dryer",
    category: "Thermal Drying",
    designCode: "ASME Sec VIII / NFPA 68 / NFPA 654 / ATEX Zone 21/22",
    dimensions: "14,000 mm L x 1,000 mm W x 2,200 mm H overall envelope",
    volume: "Bed Area: 14.0 m2 across 3 independent psychrometric zones",
    emptyWeight: "6,850 kg",
    fullWeight: "8,400 kg operating load",
    moc: "Contact parts AISI SS304 (2B food finish); Exterior insulated mild steel cladding",
    operatingTemp: "Zone 1: 85°C | Zone 2: 75°C | Zone 3: 32°C (Conditioning)",
    operatingPress: "Negative pressure (-150 to -250 Pa gauge)",
    motorKw: "Supply Fan: 37.0 kW | Exhaust Fan: 30.0 kW | Vibration Motors: 2 x 2.2 kW",
    scadaTag: "TIC-201 / TIC-202 / TIC-203 / PIC-201 / DP-201",
    nozzles: [
      { tag: "IN", size: "400x300 flanged", desc: "Dal Infeed via Silicone Boot" },
      { tag: "OUT", size: "DN250 Rotary", desc: "Dry Conditioned Dal Discharge" },
      { tag: "EXH", size: "3 x DN400 Flanged", desc: "Air Exhaust Manifold to Cyclone" }
    ],
    description: "Three-zone continuous vibrating fluid bed dryer. Achieves rapid surface and capillary moisture evaporation (from 28% to 10.0% wb) without thermal case hardening. Features dual NFPA 68 burst explosion panels."
  },
  "CY-101_Cyclone_Separator": {
    tag: "CY-101",
    name: "High-Efficiency Sanitary Cyclone Dust Separator",
    category: "Air Pollution Control",
    designCode: "Stairmand High-Efficiency Geometry / NFPA 68 / ATEX",
    dimensions: "1,200 mm Barrel Dia x 4,200 mm Total Height x 60° Cone",
    volume: "Air Throughput: 8,500 Nm3/h at 75°C",
    emptyWeight: "980 kg",
    fullWeight: "1,050 kg operating",
    moc: "AISI SS304 fully welded, 3.0 mm shell with internal smooth polish",
    operatingTemp: "65°C - 75°C exhaust stream",
    operatingPress: "-2.5 kPa draft",
    motorKw: "0.75 kW Flameproof Rotary Airlock Valve",
    scadaTag: "DP-CY101 / ZIC-CY101",
    nozzles: [
      { tag: "IN", size: "600x300 Rect", desc: "Tangential Air Ingress from Dryer" },
      { tag: "TOP", size: "DN500 Flanged", desc: "Clean Air Exhaust to Induced Draft Fan" },
      { tag: "BOT", size: "DN200 PN10", desc: "Fines Collection Rotary Airlock" }
    ],
    description: "Captures 99.4% of entrained dal flour and cotyledon micro-fines (> 10 um), returning collected solids to the dry recovery line while preventing environmental emissions."
  },
  "SK-100_Dosing_Skid": {
    tag: "SK-100",
    name: "Food-Grade Conditioning Chemical Dosing Skid",
    category: "Chemical Conditioning",
    designCode: "FSSAI Schedule 4 GMP / ASME B31.3 Process Piping",
    dimensions: "2,400 mm L x 1,200 mm W x 1,800 mm H packaged skid",
    volume: "2 x 1,000 L HDPE / SS316 batch prep tanks",
    emptyWeight: "420 kg",
    fullWeight: "2,450 kg loaded",
    moc: "SS316L wetted parts, PTFE seals, SS304 structural tubular skid",
    operatingTemp: "Ambient (25°C - 35°C)",
    operatingPress: "Discharge at 3.5 bar gauge",
    motorKw: "2 x 0.75 kW Progressive Cavity Dosing Pumps + 2 x 0.37 kW Mixers",
    scadaTag: "FIT-SK100 / AIC-SK100 / LIC-SK100",
    nozzles: [
      { tag: "OUT", size: "DN40 Sanitary", desc: "Dosing Header to TK-101A/B" }
    ],
    description: "Precision automated batching skid for FSSAI-approved alkaline conditioning agents (Sodium Bicarbonate / Citrate). Maintains exact 0.50% w/w chemical stoichiometry via closed-loop conductivity control."
  },
  "EV-101_ZLD_Evaporator": {
    tag: "EV-101",
    name: "Triple-Effect Falling Film ZLD Evaporator Skid",
    category: "Effluent Treatment & ZLD",
    designCode: "ASME Sec VIII Div 1 / TEMA Class C",
    dimensions: "3 Calandrias (Dia 600 mm x 3,000 mm L) on 4.5 m x 2.2 m Skid",
    volume: "Evaporative Capacity: 25,000 L/day (1,040 kg/h evaporation)",
    emptyWeight: "3,800 kg",
    fullWeight: "5,600 kg operating liquor",
    moc: "Tubes SS316L (120 tubes x 38 mm OD x 1.6 mm thk per effect); Shell SS304",
    operatingTemp: "Effect 1: 82°C (48 kPa) | Effect 2: 70°C (31 kPa) | Effect 3: 56°C (16 kPa)",
    operatingPress: "Vacuum system via Liquid Ring Vacuum Pump (5.5 kW)",
    motorKw: "Recirculation Pumps: 3 x 2.2 kW | Condensate Pump: 1.5 kW | Vacuum Pump: 5.5 kW",
    scadaTag: "TIC-EV101 / PIC-EV101 / LIC-EV101 / AIC-EV101 (Cond)",
    nozzles: [
      { tag: "FEED", size: "DN50 PN16", desc: "Effluent Liquor Infeed from SC-101" },
      { tag: "STM", size: "DN80 ASME 150#", desc: "Low Pressure Motive Steam (3.0 bar)" },
      { tag: "COND", size: "DN50 PN16", desc: "Pure Distillate Recycle to Soak Tank" },
      { tag: "BRINE", size: "DN40 PN16", desc: "Concentrated Brine to Agitated Thin Film Dryer" }
    ],
    description: "Energy-efficient falling film evaporator recovering 92% of spent soak liquor as high-purity distillate for closed-loop reuse (steam economy = 2.38). Leaves concentrated mineral reject for zero liquid discharge compliance."
  },
  "STR-100_Mezzanine_Platform": {
    tag: "STR-100",
    name: "Heavy Structural Steel Mezzanine & Maintenance Tower",
    category: "Structural & Access",
    designCode: "IS 800:2007 / AISC 360-16 / OSHA 1910",
    dimensions: "7,200 mm L x 4,000 mm W x 4,200 mm High Operating Deck",
    volume: "Total Structural Steel Weight: 7,189 kg",
    emptyWeight: "7,189 kg",
    fullWeight: "24,889 kg (Steel + 2 Full Vessels + Live Load 5.0 kN/m2)",
    moc: "Structural Mild Steel IS 2062 Grade E250 with hot-dip galvanized & epoxy finish",
    operatingTemp: "Ambient",
    operatingPress: "Static / Dynamic Loading (Seismic Zone III, wind speed 39 m/s)",
    motorKw: "Integrated 1,000 kg Goods Lift (3.7 kW)",
    scadaTag: "N/A",
    nozzles: [],
    description: "Heavy industrial mezzanine supporting the entire soaking battery. Includes non-slip serrated safety grating, 1,100 mm handrails with toe boards, continuous access stairway, and overhead monorail hoist beam."
  },
  "PIP-100_Interconnecting_Piping": {
    tag: "PIP-100",
    name: "Hygienic Process & Utility Interconnecting Piping",
    category: "Process Piping",
    designCode: "ASME B31.3 Process Piping / 3-A Sanitary Standards",
    dimensions: "DN40 to DN150 Schedule 10S / 40S Piping Runs",
    volume: "Total Piping Length: 185 meters",
    emptyWeight: "1,120 kg",
    fullWeight: "1,680 kg fluid-filled",
    moc: "AISI SS316L (Food contact lines) / SS304 (Utility steam & condensate)",
    operatingTemp: "20°C to 135°C (Steam lines)",
    operatingPress: "Full vacuum to 6.0 bar gauge",
    motorKw: "N/A",
    scadaTag: "PI-101 through PI-124",
    nozzles: [],
    description: "Pre-fabricated orbital-welded piping network with slope towards drainage points to guarantee self-draining clean-in-place (CIP) and prevent microbial stagnation."
  }
};

export const STREAMS_DATA = [
  { id: "S01", name: "Raw Tanzanian Toor Dal Feed", source: "Raw Dal Intake Hopper", dest: "TK-101A/B Soaking Battery", massFlow: 1875.0, temp: 25.0, press: 1.013, phase: "Solid Granular", solidsPct: 90.0, waterPct: 10.0, desc: "Dry imported split pigeon pea grains (1000-grain weight: 89.2 g)." },
  { id: "S02", name: "Fresh Conditioning Water", source: "RO Water Utility", dest: "TK-101A/B Soaking Battery", massFlow: 2798.4, temp: 55.0, press: 2.50, phase: "Liquid Water", solidsPct: 0.0, waterPct: 100.0, desc: "Heated treated water (hardness < 50 ppm as CaCO3) at 1:1.5 soaking ratio." },
  { id: "S03", name: "Alkaline Conditioning Reagent", source: "SK-100 Chemical Dosing Skid", dest: "TK-101A/B Soaking Battery", massFlow: 14.1, temp: 30.0, press: 3.50, phase: "Aqueous Solution", solidsPct: 100.0, waterPct: 0.0, desc: "Food-grade NaHCO3 / Sodium Citrate reagent (0.50% w/w basis)." },
  { id: "S04", name: "Hydrated Dal Slurry", source: "TK-101A/B Discharge Valve", dest: "SC-101 Dewatering Screen", massFlow: 4687.5, temp: 52.0, press: 1.013, phase: "Slurry (Solid/Liquid)", solidsPct: 35.5, waterPct: 64.5, desc: "Conditioned grain slurry after 45-60 min rapid-soaking cycle." },
  { id: "S05", name: "Spent Soak Effluent Liquor", source: "SC-101 Catch Pan", dest: "EV-101 ZLD Evaporator Skid", massFlow: 2415.3, temp: 48.0, press: 1.013, phase: "Effluent Liquor", solidsPct: 1.02, waterPct: 98.98, desc: "Separated liquor carrying leached divalent ions and residual salts." },
  { id: "S06", name: "Fresh Dal Rinse Spray", source: "Sanitary Water Header", dest: "SC-101 Rinse Deck", massFlow: 937.5, temp: 45.0, press: 3.00, phase: "Liquid Water", solidsPct: 0.0, waterPct: 100.0, desc: "Clean water spray to wash residual surface salts prior to drying." },
  { id: "S07", name: "Wet Conditioned Dal Feed", source: "SC-101 Discharge Spool", dest: "DR-101 Fluid Bed Dryer", massFlow: 2309.2, temp: 45.0, press: 1.013, phase: "Wet Granular Solid", solidsPct: 72.0, waterPct: 28.0, desc: "Surface-dewatered dal entering continuous vibratory dryer infeed." },
  { id: "S08", name: "Rinse Effluent to Drain/Recycle", source: "SC-101 Secondary Drain", dest: "EV-101 Evaporator Infeed", massFlow: 900.5, temp: 42.0, press: 1.013, phase: "Dilute Liquid", solidsPct: 0.06, waterPct: 99.94, desc: "Rinse liquor blended with main soak effluent stream." },
  { id: "S09", name: "Evaporated Moisture Vapor", source: "DR-101 Exhaust Hoods", dest: "CY-101 Cyclone Separator", massFlow: 459.8, temp: 72.0, press: 0.998, phase: "Humid Air / Vapor", solidsPct: 0.0, waterPct: 100.0, desc: "Moisture-laden air stream conveying 459.8 kg/h evaporated water." },
  { id: "S10", name: "Dried Conditioned Dal", source: "DR-101 Fluid Bed Discharge", dest: "Cooling & Inspection Screener", massFlow: 1849.4, temp: 35.0, press: 1.013, phase: "Conditioned Granular", solidsPct: 89.8, waterPct: 10.2, desc: "Dried, tempered Tanzanian toor dal meeting Indian benchmark hardness." },
  { id: "S11", name: "Finished Packaged Saleable Dal", source: "Final Inspection Screener", dest: "Automated Packaging Line", massFlow: 1796.0, temp: 28.0, press: 1.013, phase: "Finished Product", solidsPct: 90.0, waterPct: 10.0, desc: "Finished saleable product with cooking latency reduced to 3 whistles." },
  { id: "S12", name: "Mechanical Fines & Aspiration", source: "CY-101 Bottom Airlock", dest: "By-Product Flour Silo", massFlow: 53.4, temp: 30.0, press: 1.013, phase: "Dry Fine Powder", solidsPct: 90.0, waterPct: 10.0, desc: "Recovered cotyledon flour dust sold as secondary commercial cattle feed." }
];

export const MOTOR_LOAD_LIST = [
  { tag: "M-TK101A", equip: "TK-101A Agitator Motor", kw: 4.0, v: 415, fla: 8.2, mcc: "MCC-01-F1", vfd: true },
  { tag: "M-TK101B", equip: "TK-101B Agitator Motor", kw: 4.0, v: 415, fla: 8.2, mcc: "MCC-01-F2", vfd: true },
  { tag: "M-SC101-1", equip: "SC-101 Screen Exciter 1", kw: 1.5, v: 415, fla: 3.4, mcc: "MCC-01-F3", vfd: false },
  { tag: "M-SC101-2", equip: "SC-101 Screen Exciter 2", kw: 1.5, v: 415, fla: 3.4, mcc: "MCC-01-F4", vfd: false },
  { tag: "M-DR101-SF", equip: "DR-101 Air Supply Fan", kw: 37.0, v: 415, fla: 64.0, mcc: "MCC-01-F5", vfd: true },
  { tag: "M-DR101-EF", equip: "DR-101 Air Exhaust Fan", kw: 30.0, v: 415, fla: 52.0, mcc: "MCC-01-F6", vfd: true },
  { tag: "M-DR101-V1", equip: "DR-101 Vibrator Motor 1", kw: 2.2, v: 415, fla: 4.8, mcc: "MCC-01-F7", vfd: true },
  { tag: "M-DR101-V2", equip: "DR-101 Vibrator Motor 2", kw: 2.2, v: 415, fla: 4.8, mcc: "MCC-01-F8", vfd: true },
  { tag: "M-CY101-RV", equip: "CY-101 Rotary Airlock", kw: 0.75, v: 415, fla: 1.8, mcc: "MCC-01-F9", vfd: false },
  { tag: "M-SK100-P1", equip: "SK-100 Chemical Pump 1", kw: 0.75, v: 415, fla: 1.8, mcc: "MCC-02-F1", vfd: true },
  { tag: "M-SK100-P2", equip: "SK-100 Chemical Pump 2", kw: 0.75, v: 415, fla: 1.8, mcc: "MCC-02-F2", vfd: true },
  { tag: "M-SK100-M1", equip: "SK-100 Dosing Mixer 1", kw: 0.37, v: 415, fla: 1.1, mcc: "MCC-02-F3", vfd: false },
  { tag: "M-SK100-M2", equip: "SK-100 Dosing Mixer 2", kw: 0.37, v: 415, fla: 1.1, mcc: "MCC-02-F4", vfd: false },
  { tag: "M-EV101-P1", equip: "EV-101 Recirc Pump 1", kw: 2.2, v: 415, fla: 4.8, mcc: "MCC-02-F5", vfd: true },
  { tag: "M-EV101-P2", equip: "EV-101 Recirc Pump 2", kw: 2.2, v: 415, fla: 4.8, mcc: "MCC-02-F6", vfd: true },
  { tag: "M-EV101-P3", equip: "EV-101 Recirc Pump 3", kw: 2.2, v: 415, fla: 4.8, mcc: "MCC-02-F7", vfd: true },
  { tag: "M-EV101-VP", equip: "EV-101 Vacuum Pump", kw: 5.5, v: 415, fla: 11.2, mcc: "MCC-02-F8", vfd: false },
  { tag: "M-EV101-CP", equip: "EV-101 Distillate Pump", kw: 1.5, v: 415, fla: 3.4, mcc: "MCC-02-F9", vfd: false },
  { tag: "M-STR100-LF", equip: "STR-100 Goods Hoist", kw: 3.7, v: 415, fla: 7.9, mcc: "MCC-02-F10", vfd: false },
  { tag: "M-AUX-CIP", equip: "Central CIP Booster Pump", kw: 7.5, v: 415, fla: 14.5, mcc: "MCC-02-F11", vfd: true },
  { tag: "TOTAL", equip: "Total Connected Facility Load", kw: 125.8, v: 415, fla: 252.3, mcc: "TR-01 (500 kVA)", vfd: true }
];

export const SCADA_TAGS = [
  { tag: "LIC-101A", desc: "TK-101A Hydrostatic Level Transmitter", type: "AI (4-20mA HART)", range: "0 - 4,000 mm", sp: "2,200 mm", alarm: "HH: 3,500 mm / LL: 300 mm" },
  { tag: "TIC-101A", desc: "TK-101A Duplex RTD Pt100 Temperature", type: "AI (4-20mA HART)", range: "0 - 100°C", sp: "55.0°C", alarm: "H: 65°C / L: 45°C" },
  { tag: "SIC-101A", desc: "AG-101A VFD Agitator Speed Feedback", type: "AI / AO", range: "0 - 100 RPM", sp: "55 RPM", alarm: "H: 75 RPM / L: 35 RPM" },
  { tag: "XV-101A", desc: "TK-101A Bottom Dump Pneumatic Valve", type: "DO / DI (NAMUR)", range: "Open / Close", sp: "Batch Sequence", alarm: "Transit Timeout (10s)" },
  { tag: "TIC-201", desc: "DR-101 Zone 1 Drying Air Temperature", type: "AI (4-20mA)", range: "0 - 150°C", sp: "85.0°C", alarm: "HH: 95°C / L: 70°C" },
  { tag: "TIC-202", desc: "DR-101 Zone 2 Tempering Air Temperature", type: "AI (4-20mA)", range: "0 - 150°C", sp: "75.0°C", alarm: "H: 85°C / L: 60°C" },
  { tag: "TIC-203", desc: "DR-101 Zone 3 Cooling Air Temperature", type: "AI (4-20mA)", range: "0 - 100°C", sp: "32.0°C", alarm: "H: 40°C" },
  { tag: "PIC-201", desc: "DR-101 Fluid Bed Hood Differential Pressure", type: "AI (4-20mA)", range: "-500 to +500 Pa", sp: "-200 Pa", alarm: "Positive Pressure (>0 Pa)" },
  { tag: "DP-CY101", desc: "CY-101 Cyclone Differential Pressure", type: "AI (4-20mA)", range: "0 - 3,000 Pa", sp: "1,450 Pa", alarm: "H: 2,200 Pa (Clog Risk)" },
  { tag: "AIC-SK100", desc: "SK-100 Toroidal Conductivity Sensor", type: "AI (4-20mA)", range: "0 - 50 mS/cm", sp: "18.5 mS/cm", alarm: "Deviation > 10%" },
  { tag: "PIC-EV101", desc: "EV-101 Effect 1 Calandria Pressure", type: "AI (4-20mA)", range: "0 - 100 kPa abs", sp: "48 kPa abs", alarm: "H: 60 kPa abs" }
];

export const HAZOP_DATA = [
  {
    node: "01: Rapid-Hydration Soaking Vessel Battery (TK-101A/B)",
    param: "Temperature",
    deviation: "High (> 65°C)",
    cause: "Steam control valve TCV-101 fail-open or RTD calibration drift",
    consequence: "Excessive starch gelatinization; premature cotyledon softening; elevated COD in effluent liquor",
    safeguards: "High-temperature alarm TAH-101; automatic fail-closed pneumatic shutoff on motive steam; secondary manual bypass shutoff",
    action: "Interlock TSH-101 to de-energize steam solenoid and log event in 21 CFR Part 11 audit trail."
  },
  {
    node: "01: Rapid-Hydration Soaking Vessel Battery (TK-101A/B)",
    param: "Flow / Level",
    deviation: "No Flow / Low Level during Dump",
    cause: "Blockage at bottom discharge cone due to grain bridging or XV-101 failure",
    consequence: "Batch discharge delay; dry running risk for dewatering screen; thermal stagnation",
    safeguards: "Level transmitter LIT-101 transit timer alarm; 60° polished steep cone; fluidizing bottom purge nozzle",
    action: "Emergency manual fluidization pulse via high-pressure hot water nozzle N6."
  },
  {
    node: "02: Dewatering Screen & Solids Transfer (SC-101 / CHU-100)",
    param: "Differential Pressure / Flow",
    deviation: "High Liquid Carryover (> 22% w/w)",
    cause: "Screen blinding by broken cotyledons or vibrator exciter motor failure",
    consequence: "Dryer bed thermal overloading; grain clumping; bed defluidization in DR-101",
    safeguards: "Vibration transmitter VT-101; visual inspection sight glass; high-level switch in catch pan",
    action: "Automated ultrasonic screen wash cycle; interlock to pause upstream slurry dump."
  },
  {
    node: "03: Fluid Bed Dryer (DR-101)",
    param: "Pressure",
    deviation: "Positive Pressure (> 0 Pa)",
    cause: "Induced draft fan EF-101 trip or exhaust duct blockage in cyclone CY-101",
    consequence: "Dust and moisture escape into process mezzanine; fugitive particulate hazard; ATEX risk",
    safeguards: "Draft pressure transmitter PIT-201 interlocked to trip supply fan SF-101 within 250ms; dual NFPA 68 explosion panels",
    action: "Trip burner / steam battery and stop solids infeed on PIT-201 > -50 Pa."
  },
  {
    node: "03: Fluid Bed Dryer (DR-101)",
    param: "Temperature",
    deviation: "High Bed Temp (> 95°C in Zone 1)",
    cause: "Supply air temperature controller malfunction or pulse feed stoppage",
    consequence: "Case hardening of pulse seed coats; cotyledon cracking; irreversible cooking latency regression",
    safeguards: "Zone 1/2/3 high-temperature limit switches TSH-201/202/203 interlocked to steam shutoff",
    action: "Modulate bypass damper and inject ambient cooling air via emergency solenoid."
  },
  {
    node: "04: Triple-Effect ZLD Evaporator (EV-101)",
    param: "Pressure / Vacuum",
    deviation: "Loss of Vacuum (> 70 kPa abs in Effect 1)",
    cause: "Vacuum pump VP-101 seal water failure or calandria tube leak",
    consequence: "Boiling temperature elevation; thermal fouling of heat transfer tubes; liquor foaming",
    safeguards: "Vacuum transmitter PIT-EV101 interlocked to steam modulating valve; barometric seal loop",
    action: "Switch to standby vacuum ejector and reduce steam feed rate by 50%."
  }
];

export const EQUIPMENT_SIZING_TABLE = [
  { tag: "TK-101A", name: "Soak Vessel Alpha", code: "ASME VIII Div 1", shellId: "2,000 mm", tanLength: "2,200 mm", grossVol: "8.85 m³", workVol: "7.50 m³", moc: "SS304 / SS316L", motorKw: 4.0, opTemp: "55-65°C", opPress: "0.36 bar hyd" },
  { tag: "TK-101B", name: "Soak Vessel Beta", code: "ASME VIII Div 1", shellId: "2,000 mm", tanLength: "2,200 mm", grossVol: "8.85 m³", workVol: "7.50 m³", moc: "SS304 / SS316L", motorKw: 4.0, opTemp: "55-65°C", opPress: "0.36 bar hyd" },
  { tag: "AG-101A", name: "Hydrofoil Agitator Alpha", code: "DIN 28161", shellId: "D=800 mm", tanLength: "L=2,800 mm", grossVol: "N/A", workVol: "55 RPM", moc: "SS316L", motorKw: 4.0, opTemp: "55-65°C", opPress: "Atm" },
  { tag: "AG-101B", name: "Hydrofoil Agitator Beta", code: "DIN 28161", shellId: "D=800 mm", tanLength: "L=2,800 mm", grossVol: "N/A", workVol: "55 RPM", moc: "SS316L", motorKw: 4.0, opTemp: "55-65°C", opPress: "Atm" },
  { tag: "CHU-100", name: "Transfer Chute Suite", code: "CEMA 550", shellId: "DN150 x 2", tanLength: "3,100 mm", grossVol: "N/A", workVol: "52.65° Incline", moc: "SS304 (3mm)", motorKw: 0.0, opTemp: "Ambient-65°C", opPress: "Gravity" },
  { tag: "SC-101", name: "Vibratory Dewaterer", code: "ISO 2194", shellId: "800 mm W", tanLength: "2,400 mm L", grossVol: "6.0 t/h slurry", workVol: "0.5mm aperture", moc: "SS304 / SS316", motorKw: 3.0, opTemp: "Ambient-65°C", opPress: "Atm" },
  { tag: "DR-101", name: "Fluid Bed Dryer", code: "NFPA 68 / 654", shellId: "1,000 mm W", tanLength: "14,000 mm L", grossVol: "14.0 m² area", workVol: "3 Zones", moc: "SS304 Contact", motorKw: 73.4, opTemp: "85°C / 75°C / 32°C", opPress: "-200 Pa" },
  { tag: "CY-101", name: "Sanitary Cyclone", code: "Stairmand HE", shellId: "1,200 mm ID", tanLength: "4,200 mm OAL", grossVol: "8,500 Nm³/h", workVol: "99.4% >10µm", moc: "SS304 (3mm)", motorKw: 0.75, opTemp: "65-75°C", opPress: "-2.5 kPa" },
  { tag: "SK-100", name: "Chemical Dosing Skid", code: "FSSAI GMP", shellId: "1,200 x 2,400", tanLength: "1,800 mm H", grossVol: "2 x 1,000 L", workVol: "0.50% w/w", moc: "SS316L / HDPE", motorKw: 2.24, opTemp: "Ambient", opPress: "3.5 bar" },
  { tag: "EV-101", name: "Triple-Effect Evaporator", code: "ASME VIII / TEMA", shellId: "3x 600 mm", tanLength: "3,000 mm L", grossVol: "25 m³/day", workVol: "92% Recovery", moc: "SS316L Tubes", motorKw: 13.6, opTemp: "82°C / 70°C / 56°C", opPress: "16-48 kPa abs" },
  { tag: "STR-100", name: "Structural Mezzanine", code: "IS 800 / AISC", shellId: "4,000 mm W", tanLength: "7,200 mm L", grossVol: "7,189 kg steel", workVol: "4,200 mm Deck", moc: "IS 2062 Gr E250", motorKw: 3.7, opTemp: "Ambient", opPress: "5.0 kN/m²" },
  { tag: "PIP-100", name: "Interconnecting Piping", code: "ASME B31.3", shellId: "DN40 - DN150", tanLength: "185 m Run", grossVol: "1,120 kg steel", workVol: "Self-draining", moc: "SS316L / SS304", motorKw: 7.5, opTemp: "20-135°C", opPress: "Vac - 6 bar" }
];

export const DOSSIER_PAGES = Array.from({ length: 50 }, (_, i) => {
  const num = i + 1;
  const pad = String(num).padStart(2, '0');
  let title = "";
  let section = "";
  
  if (num === 1) {
    title = "Executive Transmittal & Project Charter";
    section = "Part 1: Transmittal";
  } else if (num >= 2 && num <= 27) {
    section = "Part 2: Paired Engineering Sheets";
    const pairIdx = Math.floor((num - 2) / 2) + 1;
    const isCad = num % 2 === 0;
    title = isCad ? `Sheet ${String(pairIdx).padStart(2, '0')} - 2D AutoCAD Pure Vector Drawing` : `Sheet ${String(pairIdx).padStart(2, '0')} - Facing 3D SolidWorks Inspection Model`;
  } else if (num >= 28 && num <= 35) {
    section = "Part 3: Dedicated CAD Joined Models";
    const titles = [
      "DWG-FIN-15T-J01: Primary 3D Joined Plant Isometric Projection",
      "DWG-FIN-15T-J02: Reverse 180° Utility & Evaporator Perspective",
      "DWG-FIN-15T-J03: True Orthographic Front Elevation View",
      "DWG-FIN-15T-J04: True Orthographic Transverse Side Elevation View",
      "DWG-FIN-15T-J05: True Orthographic Top Plan View",
      "DWG-FIN-15T-J06: High-Res Detail: Soaking Battery & Mezzanine Platform",
      "DWG-FIN-15T-J07: High-Res Detail: Dewatering Screen, Dryer & Cyclone",
      "DWG-FIN-15T-J08: High-Res Detail: ZLD Evaporator & Chemical Dosing Skid"
    ];
    title = titles[num - 28];
  } else if (num >= 36 && num <= 46) {
    section = "Part 4: Side-by-Side Dual-Pane Suite";
    title = `Dual-Pane Composite Sheet ${num - 35} (2D CAD Left + 3D Model Right)`;
  } else {
    section = "Part 5: Engineering Annexures";
    const anx = [
      "ANNEX-ASPEN-001: Aspen Plus V14 Converged Thermodynamic Simulation",
      "ANNEX-ELEC-001: Connected Motor Load List (125.8 kW) & SCADA Crosswalk",
      "ANNEX-MECH-001: Equipment Sizing Matrix & Structural Steel BOM (7,189 kg)",
      "ANNEX-SAFETY-001: Process Hazard Analysis (HAZOP) & Handover Manifest"
    ];
    title = anx[num - 47];
  }
  
  return {
    pageNumber: num,
    pad: pad,
    image: `/dossier_pages/page_${pad}.png`,
    title: title,
    section: section
  };
});

