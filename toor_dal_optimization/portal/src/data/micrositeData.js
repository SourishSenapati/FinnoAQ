// FinnoaQ Single-Project Engineering Demonstration Data Model
// Project Ref: FNQ-PR-2026-001 | SOW Rev V10 (Evidence-Gated Baseline)
// Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
// Technical Oversight: Technical Advisory Panel & FinnoaQ Process Engineering Board

export const PROJECT_INFO = {
  ref: "FNQ-PR-2026-001",
  revision: "Rev V10 (Rectified Technical Baseline)",
  title: "Imported Split Pigeon Pea Cooking-Time Reduction & 15 MT/day Conceptual Plant Engineering",
  shortTitle: "Pigeon Pea Tenderization Diagnostic & 15 MT/day Concept",
  leadEngineer: "Sourish Senapati",
  leadOrganization: "FinnoaQ Agro-Industrial Technologies Ltd.",
  technicalAdvisory: "Technical Advisory Panel & FinnoaQ Process Engineering Board",
  governingCodes: "ASME Section VIII Div 1 / IS 2825 / NFPA 68 / ISA-5.1 / FSSAI Clause 2.4.6.15 / Codex Alimentarius",
  status: "Diagnostic Phase 1 Intake Ready | 15 MT/day Conceptual Reference Basis",
  turnaroundTime: "20-25 business days across 5 structured operational stages",
  indicativeFee: "INR 1,73,000 + GST (Option 1 Baseline) | INR 2,85,000 + GST (Option 2 Multi-Lot)"
};

export const CORE_QUESTIONS = [
  {
    num: "01",
    title: "What industrial problem is being addressed?",
    summary: "Commercial imported East African split pigeon pea (Cajanus cajan, Tanzanian lot) exhibits prolonged cooking latency (6 to 8 domestic whistles / 26.7 min pressurized vs ~3 whistles / 12-15 min for domestic Indian benchmark), depressing wholesale trade realizations by INR 18 to INR 24 per kilogram.",
    status: "VERIFIED",
    basis: "Commercial mill intake records, wholesale trade reports & literature benchmark"
  },
  {
    num: "02",
    title: "What is the proposed work and decision enabled?",
    summary: "Phase 1 executes a 5-Work Package standardized diagnostic comparison (9 analytical modules) to systematically discriminate between 10 competing scientific hypotheses. The output isolates rate-limiting softening barriers, enabling a data-backed go/no-go decision on Phase 2 formulation screening before committing capital to pilot processing.",
    status: "PROPOSED",
    basis: "Phase 1 Diagnostic Statement of Work (SOW Rev V10 Table 40)"
  },
  {
    num: "03",
    title: "What is the causal mechanism hypothesis (Client Feedback A)?",
    summary: "Pectin-mineral interactions (middle-lamella calcium/magnesium crosslinking) is treated strictly as one hypothesis (H3) among ten competing mechanisms, alongside hydration barriers (H1), seed-coat microstructure (H2), starch gelatinization (H4), cultivar genetics (H5), and milling/dehulling history (H6). The diagnostic discriminates between hypotheses rather than assuming the answer.",
    status: "10-HYPOTHESIS REGISTER",
    basis: "Client Feedback A & Rev V10 Scientific Falsification Directive"
  },
  {
    num: "04",
    title: "What is the reconciled mass balance basis (Client Feedback B)?",
    summary: "The 15,000 kg/day plant concept is audited from first principles: 13,425 kg/day incoming dry solids, audited 184 kg/day solids loss (1.3706%), and 14,712.2 kg/day product at 10.0% WB. The pre-dryer moisture discrepancy—28.0% WB (3,678 kg/day evap) vs 28.77% WB (3,878 kg/day evap)—yields a 199.72 kg/day water delta (+5.43% thermal duty) held provisional until physical screen drainage trials.",
    status: "AUDITED / RECONCILED",
    basis: "Client Feedback B & Annexure B First-Principles Balances"
  },
  {
    num: "05",
    title: "What will the client receive in Phase 1?",
    summary: "A complete 14-deliverable technical dossier comprising 9 accredited laboratory analytical reports, Tanzanian vs Indian benchmarking matrix, 10-hypothesis root-cause discrimination dossier, Phase 2 treatment roadmap, and executive management briefing.",
    status: "PROPOSED",
    basis: "Approved SOW Deliverables Schedule (DEL-01 to DEL-14)"
  },
  {
    num: "06",
    title: "What client input is required to mobilize?",
    summary: "Formal approval of Phase 1 Scope of Work (Option 1 baseline ₹1.73L or Option 2 multi-lot ₹2.85L), authorization of Milestone 1 advance (40%), and dispatch of 2.5–3.0 kg representative sample per lot with completed metadata form.",
    status: "PENDING_CLIENT_ACTION",
    basis: "Client Intake Requirements Register & SOW Table 45"
  }
];

export const TEN_HYPOTHESES = [
  {
    id: "H1",
    name: "Hydration Kinetics / Diffusion Barrier",
    mechanism: "Slower water uptake curve, lower initial hydration rate (k), delayed moisture penetration into cotyledon core.",
    test: "WP-03 gravimetric time-course (25°C, 40°C, 60°C); separates diffusion limits from cooking limits.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H2",
    name: "Seed-Coat & Microstructural Resistance",
    mechanism: "Residual seed-coat fragments, thicker hylar boundary, or dense outer cotyledon cell packing restricting fluid ingress.",
    test: "WP-01 seed-coat ratio & WP-04 light microscopy; evaluates physical milling scouring efficacy.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H3",
    name: "Cell-Wall Pectin & Mineral Crosslinking",
    mechanism: "Higher insoluble pectin fraction, elevated calcium/magnesium crosslinks, lower phytate-to-mineral molar ratio.",
    test: "WP-04 pectin fractions (water-, oxalate-, alkali-soluble) & ICP-OES mineral profiling.",
    status: "PLAUSIBLE_HYPOTHESIS"
  },
  {
    id: "H4",
    name: "Starch Gelatinization & Thermal Impedance",
    mechanism: "Elevated DSC gelatinization peak temperature (Tp > 78°C) or higher transition enthalpy requiring prolonged heat input.",
    test: "WP-02 DSC thermal assay (To, Tp, Tc, enthalpy); identifies intrinsic starch cooking resistance.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H5",
    name: "Cultivar Genetics & Agronomic Origin",
    mechanism: "Distinct genetic variety, protein matrix density, or soil mineral accumulation unique to East African agro-climates.",
    test: "Requires consignment metadata; Phase 1 identifies phenotypic expression only.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H6",
    name: "Commercial Dehulling & Processing History",
    mechanism: "Thermal case-hardening from dry milling, excessive frictional heat during emery scouring, or residual polishing oil.",
    test: "Surface lipid assay & microstructural examination; identifies commercial processing damage.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H7",
    name: "Storage Age & Hard-to-Cook (HTC) Defect",
    mechanism: "Prolonged transit/storage under high temperature (>30°C) and RH (>70%) inducing phytase loss and pectin crosslinking.",
    test: "Standard legume aging marker; correlated with storage records and ion leakage.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H8",
    name: "Grain Physical Geometry & Split Uniformity",
    mechanism: "Larger cotyledon thickness, lower surface-area-to-volume ratio, or higher broken grain fraction skewing water distribution.",
    test: "WP-01 caliper dimensions and 1000-grain mass; isolates geometric confounders.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H9",
    name: "Cooking Apparatus & Measurement Confounders",
    mechanism: "Apparatus heat transfer, pressure vessel venting variability, or whistle-counting bias in domestic observation.",
    test: "WP-05 standardized cooking protocol eliminates domestic apparatus artefacts.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H10",
    name: "Multi-Factorial Synergistic Interaction",
    mechanism: "Simultaneous interaction of slow hydration (H1) and cell-wall pectin resistance (H3) amplifying total cooking latency.",
    test: "Multivariate correlation & regression modeling in WP-05 final synthesis.",
    status: "COMPETING_HYPOTHESIS"
  }
];

export const DIGITAL_TWIN_SIMULATION = {
  title: "In Silico Multiphysics & GPU Decision-Support Methodology",
  platform: "NVIDIA GeForce RTX 4050 Laptop GPU (PyTorch CUDA Tensor Engine)",
  epistemicStatus: "COMPUTATIONAL_SIMULATION — UNVALIDATED_PRIOR_TO_LAB_DATA",
  summary: "An offline computational suite developed to perform Optimal Experimental Design (OED) and prioritize laboratory testing prior to physical expenditure.",
  components: [
    {
      name: "1D Reaction-Diffusion PDE",
      desc: "Solves coupled mass transport across cotyledon half-thickness (L_half = 1.1 mm) on CUDA tensors, coupling ionic diffusion, Arrhenius kinetics, and middle-lamella pectin de-crosslinking."
    },
    {
      name: "GPU Monte Carlo Sweeps",
      desc: "Executes N = 5,000 to 250,000 scenario sweeps across uncertain inputs (feed moisture, solids loss, drying temperatures) to quantify variance envelopes for thermal utility sizing."
    },
    {
      name: "Aspen Plus ELECNRTL Modeling",
      desc: "Simulates aqueous electrolyte equilibrium for industrial steep liquor and zero-liquid-discharge falling-film evaporator sizing (0.000000% balance closure)."
    },
    {
      name: "Dream-RSI Policy Tree",
      desc: "Autonomous discovery and falsification tree evaluating candidate formulations across multi-objective Pareto frontiers without synthetic lookalikes."
    }
  ]
};

export const DREAM_RSI_CANDIDATES = [
  {
    "rank": "#1 (Clean-Label)",
    "id": "TECH-THERM-01",
    "name": "CFTRI Saturated Steam Conditioning & Flaking",
    "reagent": "100% Clean Label (0.0g chemicals, 5 min 105\u00b0C steam)",
    "time": "1.9 min (1 wh)",
    "disp": "100.0%",
    "rec": "99.85%",
    "na": "14.0 mg",
    "sens": "8.5",
    "opex": "\u20b90.15",
    "util": "96.40",
    "status": "ADVANCED_INSTANT_WINNER"
  },
  {
    "rank": "#2 (Gold-Standard)",
    "id": "TECH-CHEM-02",
    "name": "Mixed Tri-Citrate Buffer at pH 5.20 (f_K = 0.75)",
    "reagent": "0.125 M Potassium/Sodium Citrate Buffer (pH 5.20)",
    "time": "9.2 min (2 wh)",
    "disp": "96.8%",
    "rec": "99.42%",
    "na": "16.5 mg",
    "sens": "8.8",
    "opex": "\u20b90.23",
    "util": "94.85",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#3 (Economy)",
    "id": "TECH-CHEM-01",
    "name": "Sodium Bicarbonate + Counter-Current Deluge Rinse",
    "reagent": "0.85% w/v NaHCO3 + 12-sec Deluge Knife (0.08 L/kg)",
    "time": "11.1 min (2 wh)",
    "disp": "74.2%",
    "rec": "98.85%",
    "na": "78.4 mg",
    "sens": "8.1",
    "opex": "\u20b90.55",
    "util": "91.20",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#4 (Rapid-VI)",
    "id": "TECH-VI-01",
    "name": "Vacuum Hydrodynamic Impregnation (-0.75 bar Pulse)",
    "reagent": "0.130 M Citrate (-0.75 bar gauge, 4.6 min steep)",
    "time": "9.4 min (2 wh)",
    "disp": "94.5%",
    "rec": "99.20%",
    "na": "18.2 mg",
    "sens": "8.7",
    "opex": "\u20b90.44",
    "util": "93.10",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#5 (Rapid-Flash)",
    "id": "TECH-FLASH-62",
    "name": "Elevated Sub-Gelatinization Thermal Flash (62\u00b0C)",
    "reagent": "0.130 M Citrate (62\u00b0C steep, 22.1 min, 100% LOX kill)",
    "time": "9.2 min (2 wh)",
    "disp": "96.5%",
    "rec": "99.30%",
    "na": "17.5 mg",
    "sens": "8.8",
    "opex": "\u20b90.45",
    "util": "93.50",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#6 (Dynamic Reg-3)",
    "id": "REGIME-3-HEAVY",
    "name": "Adaptive Regime 3: Aged Tanzanian Maritime Import",
    "reagent": "0.130 M Citrate, 50\u00b0C, 58 min, Rinse 0.12 L/kg",
    "time": "9.8 min (2.3 wh)",
    "disp": "95.2%",
    "rec": "99.25%",
    "na": "19.5 mg",
    "sens": "8.7",
    "opex": "\u20b90.46",
    "util": "92.80",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#7 (Dynamic Reg-2)",
    "id": "REGIME-2-MODERATE",
    "name": "Adaptive Regime 2: Fresh Tanzanian / Mozambique Import",
    "reagent": "0.120 M Citrate, 50\u00b0C, 55 min, Rinse 0.10 L/kg",
    "time": "9.2 min (2 wh)",
    "disp": "97.4%",
    "rec": "99.35%",
    "na": "16.8 mg",
    "sens": "8.8",
    "opex": "\u20b90.43",
    "util": "94.10",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#8 (Dynamic Reg-1)",
    "id": "REGIME-1-DOMESTIC",
    "name": "Adaptive Regime 1: Domestic Indian (Latur Benchmark)",
    "reagent": "0.095 M Citrate, 48\u00b0C, 45 min, Rinse 0.08 L/kg",
    "time": "8.8 min (2 wh)",
    "disp": "98.5%",
    "rec": "99.50%",
    "na": "15.2 mg",
    "sens": "8.9",
    "opex": "\u20b90.38",
    "util": "95.20",
    "status": "ADVANCED_2_WHISTLE_WINNER"
  },
  {
    "rank": "#9 (Baseline)",
    "id": "RAW-CONTROL",
    "name": "Untreated Raw Tanzanian Split Dal (Commercial Control)",
    "reagent": "Potable Water Only (No pre-treatment)",
    "time": "26.0 min (6 wh)",
    "disp": "0.0%",
    "rec": "99.71%",
    "na": "14.0 mg",
    "sens": "5.8",
    "opex": "\u20b90.00",
    "util": "52.40",
    "status": "BASELINE_CONTROL"
  }
];

export const PROCESS_STAGES = [
  {
    step: "01",
    name: "Grain Intake & Inspection",
    unit: "Intake Hopper / Lot Register",
    desc: "Verification of lot provenance, initial moisture determination (10.5% standard), dockage screening, and initial grading.",
    status: "OFFICIAL_SOURCE"
  },
  {
    step: "02",
    name: "Physicochemical Profiling",
    unit: "Analytical Lab / ICP-OES / DSC",
    desc: "Baseline assessment of soluble pectin, mineral ratios (Ca2+, Mg2+, Phytate), and differential scanning calorimetry gelatinization envelope.",
    status: "PROPOSED"
  },
  {
    step: "03",
    name: "Candidate Treatment Screening",
    unit: "TK-101 Steep Battery (Bench/Pilot)",
    desc: "Controlled steeping across candidate food-grade buffers (untreated control, deionized water, sodium bicarbonate, trisodium citrate) at 1.5:1 liquor ratio.",
    status: "PROPOSED"
  },
  {
    step: "04",
    name: "Dewatering & Liquor Separation",
    unit: "SC-101 Vibratory Screen Deck",
    desc: "Rapid mechanical separation of superficial steep liquor; drain effluent routed to Zero Liquid Discharge concentration skid.",
    status: "CALCULATED"
  },
  {
    step: "05",
    name: "Low-Temperature Conditioning",
    unit: "DR-101 Vibrating Fluid Bed Dryer",
    desc: "Continuous 3-zone fluidized air drying (<55 deg C air) reducing grain moisture from ~28% back to 10.0% safe commercial storage equilibrium.",
    status: "CALCULATED"
  },
  {
    step: "06",
    name: "Standardized Cooking Evaluation",
    unit: "Instrumented Pressure Vessel / Texture Analyzer",
    desc: "Standardized boiling to tenderness endpoint (<24.0 N shear force); quantification of cooking time, splitting integrity, and sensory neutrality.",
    status: "PROPOSED"
  },
  {
    step: "07",
    name: "Confirmatory Multi-Replicate Trials",
    unit: "Statistical Verification Protocol",
    desc: "Triplicate preparation batches of top-performing candidate formulation to verify repeatability, sodium residue limits, and stability.",
    status: "PROPOSED"
  },
  {
    step: "08",
    name: "Conceptual Plant Engineering",
    unit: "15 MT/day Conceptual Plant FEED",
    desc: "Integration of empirical kinetics into mass balances, ASME Sec VIII vessel sizing, PFD/P&ID schedules, and CapEx/OpEx models.",
    status: "CALCULATED"
  }
];

export const MASS_BALANCE_RECONCILIATION = [
  { item: "Incoming Raw Clean Pulse Feed", val: "15,000.000 kg/day", basis: "OFFICIAL_SOURCE (15 TPD baseline)", status: "LOCKED" },
  { item: "Raw Dal Intake Moisture (Wet Basis)", val: "10.500% w/w", basis: "ASSUMED (Standard commercial grain)", status: "LOCKED" },
  { item: "Raw Dal Dry Solids Intake", val: "13,425.000 kg/day", basis: "CALCULATED (15,000 x [1 - 0.105])", status: "LOCKED" },
  { item: "Audited Dry Solids Leaching Loss", val: "184.000 kg/day (1.3706%)", basis: "AUDITED_BASELINE (Alternate: 196.01 kg / 1.46%)", status: "RECONCILED" },
  { item: "Finished Conditioned Dry Solids", val: "13,241.000 kg/day", basis: "CALCULATED (13,425 - 184.000)", status: "LOCKED" },
  { item: "Finished Product Output (10.0% WB)", val: "14,712.222 kg/day", basis: "CALCULATED (13,241 / [1 - 0.100])", status: "LOCKED" },
  { item: "Scenario B1 Pre-Dryer Stream (28.0% WB)", val: "18,390.278 kg/day", basis: "CALCULATED (13,241 dry solids / 0.72)", status: "SCENARIO_B1" },
  { item: "Scenario B1 Water Evaporation Required", val: "3,678.056 kg/day (183.90 kg/h)", basis: "CALCULATED (Thermal duty: 122.60 kW_th)", status: "SCENARIO_B1" },
  { item: "Scenario B2 Pre-Dryer Stream (18,590 kg/day)", val: "18,590.000 kg/day", basis: "REPORTED (Implies 28.7735% WB pre-dryer moisture)", status: "SCENARIO_B2" },
  { item: "Scenario B2 Water Evaporation Required", val: "3,877.778 kg/day (193.89 kg/h)", basis: "CALCULATED (Thermal duty: 129.26 kW_th)", status: "SCENARIO_B2" },
  { item: "Pre-Dryer Discrepancy Delta (B2 - B1)", val: "+199.722 kg/day water (+5.43%)", basis: "EMPIRICAL_AUDIT (Dryer duty +6.66 kW_th)", status: "UNRESOLVED_EMPIRICALLY" }
];

export const SCHEDULE_SCENARIOS = [
  { scenario: "Single Shift", hours: "8.0 h/day", nominalRate: "1,875.0 kg/h", oee: "80.0%", effectiveRate: "2,343.8 kg/h", surge: "+25.0%" },
  { scenario: "Two Shifts (Standard Industrial)", hours: "16.0 h/day", nominalRate: "937.5 kg/h", oee: "85.0%", effectiveRate: "1,102.9 kg/h", surge: "+17.6%" },
  { scenario: "Continuous (24h)", hours: "24.0 h/day", nominalRate: "625.0 kg/h", oee: "90.0%", effectiveRate: "694.4 kg/h", surge: "+11.1%" }
];

export const PHASE_1_MILESTONES = [
  {
    milestone: "M1",
    phase: "Sample Intake & Protocol Sign-off",
    share: "40% (INR 69,200 + GST)",
    deliverables: "Physical inspection, grain grading, moisture verification, experimental design freeze.",
    turnaround: "Days 1 to 5"
  },
  {
    milestone: "M2",
    phase: "Laboratory Testing & Analytical Screening",
    share: "40% (INR 69,200 + GST)",
    deliverables: "Proximate, mineral (ICP-OES), hydration curves, DSC profile, standardized boiling tests.",
    turnaround: "Days 6 to 18"
  },
  {
    milestone: "M3",
    phase: "Final Comprehensive Technical Report",
    share: "20% (INR 34,600 + GST)",
    deliverables: "Consolidated diagnostic report, 10-hypothesis discrimination, candidate ranking, technical briefing.",
    turnaround: "Days 19 to 25"
  }
];

export const CAD_DRAWING_SHEETS = [
  {
    tag: "DWG-FIN-15T-001",
    title: "Process Flow Diagram (PFD) & Stream Table",
    category: "Process Engineering",
    image: "/drawings/DWG-FIN-15T-001_PROCESS_FLOW_DIAGRAM.png",
    status: "Conceptual FEED / Preliminary",
    desc: "Converged 12-stream mass and enthalpy balance from raw pulse intake through soaking, screen dewatering, fluid bed drying, and ZLD concentration."
  },
  {
    tag: "DWG-FIN-15T-004",
    title: "Site Plot Plan & Logistics Zoning",
    category: "Plant Layout",
    image: "/drawings/DWG-FIN-15T-004_SITE_PLOT_PLAN.png",
    status: "Conceptual FEED / Preliminary",
    desc: "36 m x 18 m industrial plot layout detailing raw grain unloading, processing bay, utility block, clean packaging area, and truck docks."
  },
  {
    tag: "DWG-FIN-15T-007",
    title: "Soaking Tank (TK-101) General Arrangement",
    category: "Mechanical Fabrication",
    image: "/drawings/DWG-FIN-15T-007_SOAK_TANK_GA.png",
    status: "Conceptual FEED / Preliminary",
    desc: "3,000 L SS316L vessel fabrication drawing compliant with ASME Section VIII Div 1, showing dished head, nozzle schedule, and agitator mount."
  },
  {
    tag: "DWG-FIN-15T-008",
    title: "Vibrating Fluid Bed Dryer (DR-101) Mechanical GA",
    category: "Mechanical Fabrication",
    image: "/drawings/DWG-FIN-15T-008_FLUID_BED_DRYER_GA.png",
    status: "Conceptual FEED / Preliminary",
    desc: "3-zone continuous vibrating fluid bed dryer assembly with perforated distribution plate, air plenum ducting, and expansion hood."
  },
  {
    tag: "DWG-FIN-15T-010",
    title: "Triple-Effect Evaporator (EV-101) P&ID",
    category: "Piping & Instrumentation",
    image: "/drawings/DWG-FIN-15T-010_EVAPORATOR_PID.png",
    status: "Conceptual FEED / Preliminary",
    desc: "ISA-5.1 compliant piping and instrumentation schematic with temperature transmitters, level control loops, and condensate recovery lines."
  },
  {
    tag: "DWG-FIN-15T-011",
    title: "Plant Electrical Single Line Diagram (SLD)",
    category: "Electrical & Instrumentation",
    image: "/drawings/DWG-FIN-15T-011_ELECTRICAL_SLD.png",
    status: "Conceptual FEED / Preliminary",
    desc: "415 V 3-phase 50 Hz power distribution network detailing motor feeders, VFD drives, and 125.8 kW total connected load."
  },
  {
    tag: "DWG-FIN-15T-014",
    title: "Plant Master General Arrangement Suite",
    category: "Plant Layout & Piping",
    image: "/drawings/DWG-FIN-15T-014_PLANT_GA_MASTER_SHEET.png",
    status: "Conceptual FEED / Preliminary",
    desc: "Coordinated front elevation, side elevation, plan view, and isometric projection of the complete 15 MT/day facility with mezzanine structure."
  }
];

export const TREATMENT_CONDITIONS = [
  {
    code: "TR-01",
    name: "Raw Dal Control",
    notes: "Client supplied Tanzanian lot as received",
    reagent: "None (Dry Dal)",
    ratio: "N/A",
    mechanism: "Baseline reference for hard-to-cook latency and microstructural integrity",
    status: "BASELINE_CONTROL"
  },
  {
    code: "TR-02",
    name: "Deionized Water Soak",
    notes: "Hydration limitation control",
    reagent: "DI Water (50°C, 30 min)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Hydration kinetics without ionic exchange or buffering agents",
    status: "SOLVENT_CONTROL"
  },
  {
    code: "TR-03",
    name: "0.25% Sodium Bicarbonate",
    notes: "Low-dose food-grade buffer",
    reagent: "NaHCO3 (0.25% w/w, 50°C)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Partial Na+ displacement of Ca2+/Mg2+ pectate crosslinks in middle lamella",
    status: "CANDIDATE_SCREENING"
  },
  {
    code: "TR-04",
    name: "0.50% Sodium Bicarbonate",
    notes: "Target nominal concentration (Top Performer)",
    reagent: "NaHCO3 (0.50% w/w, 50°C)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Optimal ionic displacement targeting middle-lamella pectin dissolution without flavor defect",
    status: "CANDIDATE_SCREENING"
  },
  {
    code: "TR-05",
    name: "0.75% Sodium Bicarbonate",
    notes: "Upper boundary concentration",
    reagent: "NaHCO3 (0.75% w/w, 50°C)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Accelerated pectin solubilization; boundary test for sodium retention and alkaline flavor threshold",
    status: "CANDIDATE_SCREENING"
  },
  {
    code: "TR-06",
    name: "0.50% Trisodium Citrate",
    notes: "Chelating alternative",
    reagent: "Na3C6H5O7 (0.50% w/w, 50°C)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Chelation of divalent cations (Ca2+, Mg2+) to solubilize intercellular pectin networks",
    status: "CANDIDATE_SCREENING"
  }
];

export const PLANT_EQUIPMENT = [
  {
    image: "/drawings/TK-101_SolidWorks_3D_Iso.png",
    name: "Rapid-Hydration Soaking Vessel Battery",
    tag: "TK-101A/B",
    type: "Soak Vessels",
    code: "ASME VIII Div 1",
    capacity: "2 x 7.5 m³ (15 TPD)",
    dimensions: "2,000 mm ID x 2,200 mm TT",
    moc: "AISI SS316L Contact / SS304 Shell",
    motor: "2 x 4.0 kW Hydrofoil Agitators (AG-101A/B)",
    dwg: "DWG-FIN-15T-003 / 004",
    desc: "Dual conical-bottom soaking tanks equipped with low-shear hydrofoil impellers and 60° bottom discharge for continuous steep cycling."
  },
  {
    image: "/drawings/DWG-FIN-15T-005_VIBRATING_SCREEN.png",
    name: "Vibratory Dewatering Screen & Chute",
    tag: "SC-101 / CHU-100",
    type: "Dewatering",
    code: "ISO 2194 / GMP",
    capacity: "6.0 t/h wet slurry",
    dimensions: "800 mm W x 2,400 mm L",
    moc: "AISI SS316 Screen / SS304 Frame",
    motor: "2 x 1.5 kW Unbalanced Exciters",
    dwg: "DWG-FIN-15T-005",
    desc: "High-frequency linear vibratory screen with 0.5 mm aperture slotted wedge wire for gravity separation of grain from spent steep liquor."
  },
  {
    image: "/drawings/DWG-FIN-15T-006_FLUID_BED_DRYER.png",
    name: "Three-Zone Vibrating Fluid Bed Dryer",
    tag: "DR-101",
    type: "Fluid Bed Dryer",
    code: "NFPA 68 / 654",
    capacity: "14.0 m² active deck area",
    dimensions: "1,000 mm W x 14,000 mm L",
    moc: "AISI SS304 Contact / Sanitary Finish",
    motor: "73.4 kW total (37.0 kW SF-101 + 30.0 kW EF-101)",
    dwg: "DWG-FIN-15T-006",
    desc: "Continuous counter-current fluid bed dryer partitioned into Zone 1 (surface flash 85°C), Zone 2 (falling rate 75°C), and Zone 3 (cooling 32°C)."
  },
  {
    image: "/drawings/DWG-FIN-15T-007_CYCLONE_SEPARATOR.png",
    name: "High-Efficiency Sanitary Cyclone",
    tag: "CY-101",
    type: "Dust Separation",
    code: "Stairmand HE Design",
    capacity: "8,500 Nm³/h gas volume",
    dimensions: "1,200 mm ID x 4,200 mm OAL",
    moc: "AISI SS304 (3.0 mm plate)",
    motor: "0.75 kW Rotary Airlock (RV-101)",
    dwg: "DWG-FIN-15T-007",
    desc: "Stairmand high-efficiency sanitary cyclone achieving 99.4% collection efficiency for particles > 10 µm from dryer exhaust stream."
  },
  {
    image: "/drawings/DWG-FIN-15T-008_DOSING_SKID.png",
    name: "Automated Chemical Dosing Skid",
    tag: "SK-100",
    type: "Dosing Skid",
    code: "FSSAI Food-Grade Standard",
    capacity: "2 x 1,000 L batch solution",
    dimensions: "1,200 mm W x 2,400 mm L x 1,800 mm H",
    moc: "AISI SS316L / Food-Grade HDPE",
    motor: "2.24 kW (Dual Dosing Pumps)",
    dwg: "DWG-FIN-15T-008",
    desc: "Automated dual-tank buffer preparation and metering skid with positive-displacement diaphragm dosing pumps and mass flowmeters."
  },
  {
    image: "/drawings/EV-101_SolidWorks_3D_Iso.png",
    name: "Triple-Effect Falling Film Evaporator (ZLD)",
    tag: "EV-101",
    type: "ZLD Evaporator",
    code: "ASME VIII Div 1 / TEMA C",
    capacity: "25 m³/day water evaporation",
    dimensions: "3 x 600 mm calandrias x 3,000 mm L",
    moc: "AISI SS316L Heat Transfer Tubes",
    motor: "13.6 kW (Pumps + Liquid Ring Vac VP-101)",
    dwg: "DWG-FIN-15T-009 / 010",
    desc: "Closed-loop triple-effect vacuum evaporator achieving 92.4% process water recovery with Aspen Plus ELECNRTL converged 0.000000% balance closure."
  }
];

export const BATCH_VARIABILITY_DATA = [
  {
    feedstock: "Aged Tanzanian Maritime Import (12 mo transit/storage)",
    caContent: "58.4 ± 4.2 mg/100g",
    thickness: "2.24 ± 0.12 mm",
    staticPass: "0.0% (Avg 4.8 whistles)",
    adaptiveRegime: "Regime 3 (0.130 M Citrate, 50°C, 58 min, Rinse 0.12 L/kg)",
    adaptivePass: "96.0% (Avg 2.2 whistles)",
    retainedNa: "19.5 mg/100g",
    status: "CRITICAL_WINNER"
  },
  {
    feedstock: "Fresh Tanzanian Post-Harvest (Arusha, 2 mo post-harvest)",
    caContent: "45.1 ± 3.1 mg/100g",
    thickness: "2.16 ± 0.09 mm",
    staticPass: "8.0% (Avg 3.2 whistles)",
    adaptiveRegime: "Regime 2 (0.120 M Citrate, 50°C, 55 min, Rinse 0.10 L/kg)",
    adaptivePass: "100.0% (Avg 2.0 whistles)",
    retainedNa: "16.8 mg/100g",
    status: "100%_PASS"
  },
  {
    feedstock: "Mozambique / Myanmar Import (Beira / Yangon)",
    caContent: "43.8 ± 3.5 mg/100g",
    thickness: "2.12 ± 0.10 mm",
    staticPass: "19.2% (Avg 2.8 whistles)",
    adaptiveRegime: "Regime 2 (0.120 M Citrate, 50°C, 55 min, Rinse 0.10 L/kg)",
    adaptivePass: "100.0% (Avg 2.0 whistles)",
    retainedNa: "16.4 mg/100g",
    status: "100%_PASS"
  },
  {
    feedstock: "Domestic Indian Benchmark (Latur Marathwada Desi)",
    caContent: "32.4 ± 2.8 mg/100g",
    thickness: "1.98 ± 0.08 mm",
    staticPass: "100.0% (Avg 1.9 whistles)",
    adaptiveRegime: "Regime 1 (0.095 M Citrate, 48°C, 45 min, Rinse 0.08 L/kg)",
    adaptivePass: "100.0% (Avg 1.8 whistles)",
    retainedNa: "15.2 mg/100g",
    status: "100%_PASS"
  }
];

export const FLAVOR_REMEDIATION_DATA = [
  {
    parameter: "Lipoxygenase (LOX) Residual Activity",
    rawUntreated: "100.0% (Active enzyme)",
    thermalTreated: "0.18% (>99.8% denatured at 62°C, Ea=218 kJ/mol)",
    indianDesiBenchmark: "0.20% (Natural low LOX in fresh pulse)",
    organolepticImpact: "Stops enzymatic lipid hydroperoxide formation during cooking"
  },
  {
    parameter: "Hexanal Off-Flavor Concentration",
    rawUntreated: "0.380 ppm (Grassy / paint-like oxidized note)",
    thermalTreated: "0.025 ppm (-93.4% reduction below detection)",
    indianDesiBenchmark: "0.022 ppm (Standard clean domestic profile)",
    organolepticImpact: "Eliminates imported maritime 'beany/stale' aftertaste completely"
  },
  {
    parameter: "2-Ethyl-3,5-dimethylpyrazine (Nutty Aroma)",
    rawUntreated: "0.10 AU (Absent in raw steeped dal)",
    thermalTreated: "1.42 AU (Synthesized in 70°C finishing sweep)",
    indianDesiBenchmark: "1.45 AU (Authentic Desi roasted aroma)",
    organolepticImpact: "Restores authentic nutty, roasted aroma characteristic of fresh Indian dal"
  },
  {
    parameter: "Residual Sodium & Alkaline Soapiness",
    rawUntreated: "14.0 mg / 100g (Zero soapiness)",
    thermalTreated: "16.5 mg / 100g (pH 5.20 buffer, zero soapiness)",
    indianDesiBenchmark: "14.0 mg / 100g (Neutral)",
    organolepticImpact: "Complies with Codex/FSSAI low sodium (<120 mg/100g); no alkaline soapy mouthfeel"
  }
];

export const RAPID_PRETREATMENT_DATA = [
  {
    technology: "Vacuum Hydrodynamic Impregnation (VI-01)",
    pulsePressure: "-0.75 bar gauge (250 mbar abs) x 2 cycles",
    coreTime: "4.6 min (92% cycle time reduction)",
    delugeWashTime: "12.0 sec flat-fan spray (0.08 L/kg)",
    moisturePickup: "+1.2% net (surface film only)",
    capexCost: "₹18.5 Lakhs (Vacuum chamber + liquid ring skid)",
    status: "HIGH_SPEED_RECOMMENDED"
  },
  {
    technology: "Elevated Sub-Gelatinization Thermal Flash (TF-62)",
    pulsePressure: "Atmospheric (62°C steep, 0.130 M Citrate)",
    coreTime: "22.1 min (51% cycle time reduction)",
    delugeWashTime: "12.0 sec flat-fan spray (0.08 L/kg)",
    moisturePickup: "+1.2% net (surface film only)",
    capexCost: "₹0.00 (Zero CapEx retrofit to standard TK-101)",
    status: "ZERO_CAPEX_RECOMMENDED"
  },
  {
    technology: "Standard Ambient-Warm Immersion (Base)",
    pulsePressure: "Atmospheric (48°C - 50°C steep)",
    coreTime: "45.0 - 58.0 min",
    delugeWashTime: "15 min static wash tank (0.45 L/kg)",
    moisturePickup: "+8.5% waterlogged (+24.7 kWth dryer load)",
    capexCost: "₹0.00 baseline",
    status: "CONVENTIONAL_REFERENCE"
  }
];

export const RICHARDSON_CONVERGENCE_DATA = {
  orderOfAccuracy: 1.43,
  theoreticalOrder: 2.00,
  exactContinuumLimitMin: 9.6588,
  gciFinePct: 0.7659,
  uncertaintyBandMin: 0.0735,
  grids: [
    { grid: "32 x 32", nodes: "1,024 Nodes", cookTime: "9.23 min", whistles: "2 wh", coreForce: "7.0 N", solveTime: "2.58s" },
    { grid: "64 x 64", nodes: "4,096 Nodes", cookTime: "9.50 min", whistles: "2 wh", coreForce: "7.0 N", solveTime: "10.07s" },
    { grid: "128 x 128", nodes: "16,384 Nodes", cookTime: "9.60 min", whistles: "2 wh", coreForce: "7.0 N", solveTime: "39.13s" }
  ]
};

