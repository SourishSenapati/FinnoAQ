// FinnoaQ Single-Project Engineering Demonstration Data Model
// Project Ref: FNQ-PR-2026-001 | SOW Rev V11 (FINNOAQ OMEGA Verified Baseline)
// Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
// Technical Oversight: Technical Advisory Panel & FinnoaQ Process Engineering Board

export const PROJECT_INFO = {
  ref: "FNQ-PR-2026-001",
  revision: "Rev V11 — FINNOAQ OMEGA Verified Baseline (Audited & Reconciled)",
  title: "Imported Split Pigeon Pea Cooking-Time Reduction & 15 MT/day Conceptual Plant Engineering",
  shortTitle: "Pigeon Pea Tenderization Diagnostic & 15 MT/day Concept",
  leadEngineer: "Sourish Senapati",
  leadOrganization: "FinnoaQ Agro-Industrial Technologies Ltd.",
  technicalAdvisory: "Technical Advisory Panel & FinnoaQ Process Engineering Board",
  governingCodes: "ASME Section VIII Div 1 / IS 2825 / NFPA 68 / ISA-5.1 / FSSAI Compendium INS 330-332 / ISO 11136:2014",
  status: "FINNOAQ OMEGA Verified In Silico Baseline | Pending Monday Physical Bench Trial",
  turnaroundTime: "20-25 business days across 5 structured operational stages",
  indicativeFee: "INR 1,73,000 + GST (Option 1 Baseline) | INR 2,85,000 + GST (Option 2 Multi-Lot)"
};

export const CORE_QUESTIONS = [
  {
    num: "01",
    title: "What industrial problem is being addressed?",
    summary: "Commercial imported East African split pigeon pea (Cajanus cajan, Tanzanian lot) exhibits prolonged cooking latency (8 domestic whistles / 17.3–23.1 min pressurized vs 3 whistles / 9.8–13.3 min for domestic Indian benchmark), depressing wholesale trade realizations by INR 18 to INR 24 per kilogram.",
    status: "VERIFIED",
    basis: "Commercial mill intake records, wholesale trade reports & literature benchmark"
  },
  {
    num: "02",
    title: "What is the proposed work and decision enabled?",
    summary: "Phase 1 executes a 5-Work Package standardized diagnostic comparison and the Monday Bench Trial Protocol (EXP-01 to EXP-05) to falsify or confirm our Stage 1–4 OMEGA mechanistic predictions before committing capital to 15 TPD equipment.",
    status: "PROPOSED",
    basis: "Phase 1 Diagnostic Statement of Work & OMEGA Physical Validation Plan"
  },
  {
    num: "03",
    title: "What is the causal mechanism hypothesis (Client Feedback A)?",
    summary: "Middle-lamellar Ca2+/Mg2+-pectate egg-box cross-linking formed via storage PME de-esterification and phytase hydrolysis (H3/H7) coupled with cotyledon half-thickness diffusion path H^2 (H1/H8) governs core softening. All 10 hypotheses remain tracked in the diagnostic register.",
    status: "10-HYPOTHESIS REGISTER",
    basis: "Perera et al. (2023), Panda et al. (2026) & 2D Conservative Reaction-Diffusion PDE"
  },
  {
    num: "04",
    title: "What is the reconciled mass & OpEx balance basis (Client Feedback B & FAIL-0025)?",
    summary: "At 15,000 kg/day finished output, 85% bleed-and-feed bath liquor recycling reduces reagent usage from 880.9 kg/day (₹8.62/kg once-through) to 371.3 kg/day (₹3.63/kg reagent, ₹6.34/kg total plant OpEx). The pre-dryer moisture delta—Scenario B1 (28.0% WB, 3,654.42 kg/d evap) vs Scenario B2 (28.7735% WB, 3,854.14 kg/d evap)—preserves the exact +199.72 kg/day evaporative bound.",
    status: "AUDITED / RECONCILED",
    basis: "OMEGA Stage 4 Plant Balance (FAIL-0025 Fixed) & Annexure B First-Principles Balances"
  },
  {
    num: "05",
    title: "What will the client receive in Phase 1?",
    summary: "A complete 12-deliverable OMEGA scientific engineering package, 22-source offline evidence vault, 42-test verified Python simulation suite, corrected pH 5.20 SOP/Bench recipes, and ISO 11136:2014 TOST sensory study protocol.",
    status: "DELIVERED_IN_SILICO",
    basis: "FINNOAQ OMEGA Deliverables Schedule"
  },
  {
    num: "06",
    title: "What physical validation is required next?",
    summary: "Execute EXP-01 (Monday Bench Trial on Pot 1–5 with corrected pH 5.20 citrate buffer: 18.90g K3Cit·H2O + 1.90g Na3Cit·2H2O + 8.46g Citric Acid per 750 mL) and EXP-05 (N=72 ISO 11136:2014 consumer TOST equivalence panel).",
    status: "PENDING_BENCH_TRIAL",
    basis: "OMEGA Ranked Physical Validation Plan (reports/OMEGA_PHYSICAL_VALIDATION_PLAN.md)"
  }
];

export const TEN_HYPOTHESES = [
  {
    id: "H1",
    name: "Hydration Kinetics / Diffusion Barrier",
    mechanism: "Slower water and chelator transport across thicker split cotyledons (tau ~ H^2 / D_eff).",
    test: "WP-03 gravimetric time-course & 2D axisymmetric PDE verification.",
    status: "COUPLED_DRIVER (Sobol S_T = 0.630 for Time)"
  },
  {
    id: "H2",
    name: "Seed-Coat & Microstructural Resistance",
    mechanism: "Removed in split dhal (making whole-seed literature INDIRECT), leaving dense parenchyma porosity (epsilon = 0.11).",
    test: "WP-01 seed-coat ratio & pycnometric open porosity assay (Fito et al., 1996).",
    status: "BOUNDED_BY_POROSITY"
  },
  {
    id: "H3",
    name: "Cell-Wall Pectin & Mineral Crosslinking",
    mechanism: "Insoluble Ca2+-pectate egg-box junctions (33.5 mol/m^3 in aged Tanzanian vs 14.0 mol/m^3 in fresh Indian Latur).",
    test: "WP-04 pectin fractionation, FTIR DE assay & EDTA/ICP-OES mineral profiling.",
    status: "PRIMARY_BIOCHEMICAL_DRIVER (Sobol S_T = 0.114)"
  },
  {
    id: "H4",
    name: "Starch Gelatinization & Thermal Impedance",
    mechanism: "Intracellular starch gelatinization (To=65°C, Tp=76°C) is physically restricted until middle-lamellar pectin softens.",
    test: "WP-02 DSC thermal assay (To, Tp, Tc, enthalpy).",
    status: "SECONDARY_COUPLED_SUBSTRATE"
  },
  {
    id: "H5",
    name: "Cultivar Genetics & Agronomic Origin",
    mechanism: "Bold East African cultivars (ICEAP 00040, 2H = 2.16-2.44 mm) have 61.5% larger H^2 than Indian Latur Desi (2H = 1.70 mm).",
    test: "30-grain digital caliper thickness & 1000-grain weight at receiving dock.",
    status: "NONLINEAR_GEOMETRIC_DRIVER (Sobol S_T = 0.099)"
  },
  {
    id: "H6",
    name: "Commercial Dehulling & Processing History",
    mechanism: "Thermal case-hardening from excessive drying temperatures (>80°C) or residual milling oil.",
    test: "Surface lipid assay & stereomicroscope fissure inspection.",
    status: "COMPETING_HYPOTHESIS"
  },
  {
    id: "H7",
    name: "Storage Age & Hard-to-Cook (HTC) Defect",
    mechanism: "Prolonged transit/storage (>30°C, >75% RH) activating PME de-esterification (DE -> 0.28) and phytase Ca2+ release.",
    test: "3-minute boiling Water Absorption Index (WAI_3min) & leachate conductivity proxy.",
    status: "PRIMARY_AGING_MECHANISM"
  },
  {
    id: "H8",
    name: "Grain Physical Geometry & Split Uniformity",
    mechanism: "Larger cotyledon half-thickness H directly delays core Ca2+ displacement even when outer bulk is soft.",
    test: "Core vs bulk Warner-Bratzler shear force (F_WB,core <= 18.0 N gate).",
    status: "VERIFIED_IN_STAGE_1"
  },
  {
    id: "H9",
    name: "Cooking Apparatus & Measurement Confounders",
    mechanism: "Standardized 121.1°C (103.4 kPa gauge) pressure-cooker whistle timeline (4.5 min heat-up + 1.95 min/whistle).",
    test: "WP-05 standardized pressure-cooking & Warner-Bratzler shear fixture.",
    status: "STANDARDIZED"
  },
  {
    id: "H10",
    name: "Multi-Factorial Synergistic Interaction",
    mechanism: "Multiplicative interaction between bound Ca2+ and H^1.35 encapsulated in HTC Severity Index S_HTC.",
    test: "Stage 3 150-batch Monte Carlo & Sobol Global Sensitivity Analysis.",
    status: "MODEL_DERIVED_VERIFIED"
  }
];

export const DIGITAL_TWIN_SIMULATION = {
  title: "FINNOAQ OMEGA Hierarchical Multiphysics & Statistical Proof System",
  platform: "AMD Ryzen AI 9 365 (20 Threads) + NVIDIA GeForce RTX 4050 Laptop GPU (CUDA 12.4)",
  epistemicStatus: "MODEL_DERIVED + LITERATURE_SUPPORTED (Pending Monday Physical Bench Validation)",
  summary: "An 8-module offline-first scientific computing suite (src/finnoaq/omega_modules.py) verified by 42 automated pytest regression and conservation checks.",
  components: [
    {
      name: "2D Axisymmetric Conservative Reaction-Diffusion PDE (Module B)",
      desc: "Solves simultaneous water hydration, pH-speciated Citrate/HCO3 diffusion, ultrasound cavitation enhancement (17 W/L), Fito (1996) vacuum impregnation porosity bounds, and competitive Ca2+-pectate chelation across (r, z)."
    },
    {
      name: "Two-Substrate Pressure Cooking & Core Shear Solver (Module C)",
      desc: "Couples middle-lamellar pectin dissolution and starch gelatinization at 121.1°C against the Literature Nisha et al. (2006) benchmark, enforcing both F_WB,bulk <= 18.0 N and F_WB,core <= 18.0 N at Whistle 2."
    },
    {
      name: "Multi-Protic Electroneutrality & Washing Film/Pore Solver (Modules D, E, F)",
      desc: "Computes exact Davies-corrected pH 5.20 hydrate stoichiometry (fixing FAIL-0024), separates 12 s external spray film stripping from internal pore retention (fixing FAIL-0023), and designs the N=72 ISO 11136:2014 TOST sensory trial."
    },
    {
      name: "Noisy Intake Adaptive Policy & Coupled Drying Stress (Modules G, H)",
      desc: "Simulates 150-batch Monte Carlo adaptation using noisy 5-min receiving dock proxies (fixing FAIL-0022), models temperature-coupled drying stress (fixing FAIL-0021), and reconciles 85% recycled bath OpEx at ₹6.34/kg (fixing FAIL-0025)."
    }
  ]
};

export const DREAM_RSI_CANDIDATES = [
  {
    "rank": "#1 (Stage 1/2 Winner)",
    "id": "S1-09 / S2-10",
    "name": "90:10 K/Na Citrate (pH 5.20) + 17 W/L UAE (20 min) + 12s Spray Wash",
    "reagent": "0.145 M K/Na Citrate (25.20 kg K3Cit·H2O + 2.54 kg Na3Cit·2H2O + 11.28 kg H3Cit / 1000L)",
    "time": "8.3 min (2 wh)",
    "disp": "98.1% bulk / 80.7% core",
    "rec": "99.58%",
    "na": "3.4 mg/100g",
    "sens": "d'=0.22 (TOST Pending)",
    "opex": "₹6.34/kg (85% Rec.)",
    "util": "96.80",
    "status": "OMEGA_VERIFIED_WINNER"
  },
  {
    "rank": "#2 (Tier 1 Mild)",
    "id": "ADAPT-TIER-1",
    "name": "Adaptive Tier 1 Mild Conditioning (52°C, 15 min UAE)",
    "reagent": "0.105 M K/Na Citrate pH 5.30 (18.85 kg K3Cit + 1.90 kg Na3Cit + 7.77 kg H3Cit / 1000L)",
    "time": "8.1 min (2 wh on Mild Lots)",
    "disp": "96.4% bulk / 82.1% core",
    "rec": "99.69%",
    "na": "2.6 mg/100g",
    "sens": "d'=0.17 (TOST Pending)",
    "opex": "₹5.32/kg (85% Rec.)",
    "util": "95.40",
    "status": "ADAPTIVE_MILD_TIER"
  },
  {
    "rank": "#3 (Tier 3 Severe)",
    "id": "ADAPT-TIER-3",
    "name": "Adaptive Tier 3 Severe HTC Conditioning (57°C, 26 min UAE + 15 kPa VI)",
    "reagent": "0.185 M K/Na Citrate pH 5.20 (32.15 kg K3Cit + 3.24 kg Na3Cit + 14.39 kg H3Cit / 1000L)",
    "time": "8.4 min (2 wh on Severe Lots)",
    "disp": "98.8% bulk / 81.4% core",
    "rec": "99.48%",
    "na": "4.2 mg/100g",
    "sens": "d'=0.27 (TOST Pending)",
    "opex": "₹7.45/kg (85% Rec.)",
    "util": "93.90",
    "status": "ADAPTIVE_SEVERE_TIER"
  },
  {
    "rank": "#4 (100% K-Citrate)",
    "id": "S2-06",
    "name": "100% Potassium Citrate Buffer (0.145 M, pH 5.20) + 12s Spray Wash",
    "reagent": "0.145 M K-Citrate Only (pH 5.20, Zero Added Sodium)",
    "time": "8.2 min (2 wh)",
    "disp": "98.3% bulk / 81.9% core",
    "rec": "99.58%",
    "na": "0.0 mg added",
    "sens": "d'=0.25 (TOST Pending)",
    "opex": "₹6.58/kg (85% Rec.)",
    "util": "94.10",
    "status": "ZERO_SODIUM_ALTERNATIVE"
  },
  {
    "rank": "#5 (Static Citrate)",
    "id": "S1-05",
    "name": "Static Hybrid K/Na Citrate Soak Without Ultrasound (55°C, 20 min)",
    "reagent": "0.145 M K/Na Citrate (pH 5.20, No Ultrasound)",
    "time": "9.6 min (Bulk Pass, Core 20.35 N)",
    "disp": "95.5% bulk / 61.1% core",
    "rec": "99.65%",
    "na": "3.4 mg/100g",
    "sens": "d'=0.22 (Hard Core)",
    "opex": "₹6.06/kg",
    "util": "74.20",
    "status": "FAILS_CORE_SHEAR_GATE"
  },
  {
    "rank": "#6 (100% Na-Citrate)",
    "id": "S2-04",
    "name": "100% Sodium Citrate Buffer (0.145 M, pH 5.20) + 17 W/L UAE (20 min)",
    "reagent": "0.145 M Na3Cit/Citric Buffer (Lower Na+ Stokes Mobility)",
    "time": "9.1 min (Core 18.85 N > 18 N)",
    "disp": "96.2% bulk / 74.8% core",
    "rec": "99.58%",
    "na": "32.5 mg/100g",
    "sens": "d'=0.19 (Hard Core)",
    "opex": "₹5.18/kg",
    "util": "76.50",
    "status": "FAILS_CORE_SHEAR_GATE"
  },
  {
    "rank": "#7 (Alkaline Soda)",
    "id": "S1-04 / S2-02",
    "name": "0.50% w/v Sodium Bicarbonate (pH 8.32, 55°C, 20 min) + 12s Spray Wash",
    "reagent": "0.50% NaHCO3 (Unbuffered Alkaline beta-Elimination)",
    "time": "9.4 min (Bulk 10.8N, Core 19.9N)",
    "disp": "86.7% bulk / 32.0% core",
    "rec": "99.65%",
    "na": "19.3 mg/100g",
    "sens": "d'=2.14 (SOAPY FAIL)",
    "opex": "₹2.95/kg",
    "util": "48.10",
    "status": "REJECTED_SOAPY_AND_HARD_CORE"
  },
  {
    "rank": "#8 (Falsified 4.6m VI)",
    "id": "S1-10 (FAIL-0023)",
    "name": "Legacy 4.6-Min Vacuum Impregnation Shortcut (Falsified by Fito 1996 HDM)",
    "reagent": "0.145 M Citrate (15 kPa Vacuum Pulse, 4.6 min steep)",
    "time": "16.6 min (7 wh, Core 24.63 N)",
    "disp": "52.9% bulk / 5.2% core",
    "rec": "99.92%",
    "na": "1.8 mg/100g",
    "sens": "Unacceptable Hard Core",
    "opex": "N/A (Falsified)",
    "util": "28.40",
    "status": "FALSIFIED_BY_OMEGA_FAIL_0023"
  },
  {
    "rank": "#9 (Baseline Control)",
    "id": "S1-02-TZA-RAW",
    "name": "Untreated Raw Tanzanian Aged HTC Split Dal (Commercial Control)",
    "reagent": "None (Untreated Aged Import, 2H = 2.16 mm, Ca = 33.5 mol/m^3)",
    "time": "17.3–23.1 min (8 wh)",
    "disp": "0.0% bulk / 0.0% core",
    "rec": "100.00%",
    "na": "0.0 mg added",
    "sens": "Grassy Hexanal >115 ppb",
    "opex": "₹0.00/kg",
    "util": "22.00",
    "status": "BASELINE_HTC_CONTROL"
  }
];

export const PROCESS_STAGES = [
  {
    step: "01",
    name: "5-Min Receiving Dock Intake Diagnostic",
    unit: "Intake Hopper / QA Bench",
    desc: "30-grain caliper half-thickness H, capacitive moisture X_wb, and 3-min 95°C boiling WAI_3min proxy to compute S_HTC and assign Tier 1, Tier 2, Tier 3, or OOD Hold.",
    status: "MODEL_DERIVED"
  },
  {
    step: "02",
    name: "pH 5.20 Hybrid Citrate Buffer Preparation",
    unit: "SK-100 Dosing & Recycle Skid",
    desc: "Exact multi-protic electroneutrality recipe (25.20 kg K3Cit·H2O + 2.54 kg Na3Cit·2H2O + 11.28 kg Citric Acid per 1000 L for Tier 2 at verified pH 5.20) with 85% filtered liquor recycle.",
    status: "CALCULATED"
  },
  {
    step: "03",
    name: "Ultrasonic Assisted Steeping (20 min)",
    unit: "UAE-101A/B Staggered Vessels",
    desc: "20.0 min steeping at 55.0°C with 17.0 W/L (40 kHz) cavitation, achieving 98.1% bulk and 80.7% core Ca2+ displacement and 78% LOX inactivation.",
    status: "MODEL_DERIVED"
  },
  {
    step: "04",
    name: "12-Second Dual-Fan Spray Wash & Dewatering",
    unit: "WSH-102 Vibratory Wedge-Wire Deck",
    desc: "12.0 s high-pressure (2.5 bar, 0.50 L/kg) flat-fan spray stripping 98.7% of surface film residue (to 23.3 ppm) followed by air-knife dewatering to 28.0–28.77% WB.",
    status: "CALCULATED"
  },
  {
    step: "05",
    name: "Two-Stage Fluidized Drying & 20-Min Tempering",
    unit: "FBD-103 & TMP-104 Tempering Silo",
    desc: "Stage 1 (65°C, 22 min) -> Adiabatic Tempering (20 min) -> Stage 2 (55°C, 25 min), keeping peak tensile stress at 0.71 MPa (< 1.65 MPa yield) and breakage at 0.35%.",
    status: "CALCULATED"
  },
  {
    step: "06",
    name: "Standardized 2-Whistle Quality Verification",
    unit: "Instrumented Pressure Cooker / Texture Analyzer",
    desc: "Verification that both bulk shear force (13.91 N) and core shear force (17.35 N) pass <= 18.0 N at Whistle 2 (8.40 min total steam cycle).",
    status: "PROPOSED"
  },
  {
    step: "07",
    name: "ISO 11136:2014 Consumer TOST Equivalence",
    unit: "Sensory Evaluation Booths (N=72)",
    desc: "Two One-Sided Tests (TOST) on unspiced slurry (Matrix A) and tempered Tadka (Matrix B) verifying 90% CI within [-0.75, +0.75] of Indian Latur reference.",
    status: "PROPOSED"
  },
  {
    step: "08",
    name: "Ambient Cooling & Nitrogen Packaging",
    unit: "PKG-105 Cooler & Sorter",
    desc: "12.0 min counter-current cooling (<32°C), optical sorting, and packaging at 15,000 kg/day (750 kg/h, 103.0 min total single-lot residence time).",
    status: "CALCULATED"
  }
];

export const MASS_BALANCE_RECONCILIATION = [
  { item: "Finished Conditioned Dal Output (11.75% WB)", val: "15,000.000 kg/day (750.0 kg/h)", basis: "OFFICIAL_SOURCE (15 TPD commercial target)", status: "LOCKED" },
  { item: "Raw Untreated Dal Input (9.8% WB)", val: "15,052.684 kg/day", basis: "CALCULATED (Accounts for 0.35% net dry-matter loss)", status: "LOCKED" },
  { item: "Total Steeping Bath Circulation (1.5 L/kg)", val: "22,579.027 L/day", basis: "CALCULATED (85% recycled via 50 um wedge-wire + UV)", status: "RECONCILED" },
  { item: "Fresh Makeup Bath Water (85% Recycle Mode)", val: "6,649.523 L/day", basis: "CALCULATED (Replenishes 0.18 L/kg grain uptake + 15% bleed)", status: "LOCKED" },
  { item: "Dual-Fan High-Pressure Spray Wash Water (0.5 L/kg)", val: "7,526.342 L/day", basis: "CALCULATED (12.0 s spray at 2.5 bar gauge)", status: "LOCKED" },
  { item: "Daily Reagents (85% Recycle Mode, pH 5.20)", val: "239.83 kg K3Cit + 24.16 kg Na3Cit + 107.30 kg H3Cit", basis: "CALCULATED (371.29 kg/d total vs 880.91 kg/d once-through)", status: "RECONCILED" },
  { item: "Scenario B1 Water Evaporation (28.0% WB Screen)", val: "3,654.420 kg/day", basis: "CALCULATED (Vibratory air-knife dewatering design base)", status: "SCENARIO_B1" },
  { item: "Scenario B2 Water Evaporation (28.7735% WB Screen)", val: "3,854.140 kg/day", basis: "REPORTED (Conservative drainage bound)", status: "SCENARIO_B2" },
  { item: "Pre-Dryer Discrepancy Delta (B2 - B1)", val: "+199.720 kg/day water (+5.47%)", basis: "EMPIRICAL_AUDIT (Preserved until EXP-02 pilot trial)", status: "UNRESOLVED_EMPIRICALLY" },
  { item: "Audited Total Manufacturing OpEx (85% Recycle)", val: "₹6.34 / kg dal (₹95,065 / day)", basis: "CALCULATED (₹3.63 reagent + ₹1.58 thermal + ₹1.13 other)", status: "RECONCILED" },
  { item: "Audited Total Manufacturing OpEx (0% Once-Through)", val: "₹11.65 / kg dal (₹174,807 / day)", basis: "CALCULATED (Fixes FAIL-0025 contradiction)", status: "REFERENCE_ONLY" }
];

export const SCHEDULE_SCENARIOS = [
  { scenario: "Single Shift", hours: "8.0 h/day", nominalRate: "1,875.0 kg/h", oee: "80.0%", effectiveRate: "2,343.8 kg/h", surge: "+25.0%" },
  { scenario: "Two Shifts", hours: "16.0 h/day", nominalRate: "937.5 kg/h", oee: "85.0%", effectiveRate: "1,102.9 kg/h", surge: "+17.6%" },
  { scenario: "Three Shifts + 4h CIP (Selected 15 TPD Design)", hours: "20.0 h/day", nominalRate: "750.0 kg/h", oee: "90.0%", effectiveRate: "833.3 kg/h", surge: "+11.1%" }
];

export const PHASE_1_MILESTONES = [
  {
    milestone: "EXP-01 & 02",
    phase: "Monday Bench Cookability, pH 5.20 Verification & Spray-Wash Trial",
    share: "INR 7,500 Est. Lab Budget (2 Days)",
    deliverables: "Falsify/confirm <= 2 whistles & F_WB,core <= 18.0 N on Pot 4; resolve Scenario B1 vs B2 dewatering moisture.",
    turnaround: "Days 1 to 2"
  },
  {
    milestone: "EXP-03 & 04",
    phase: "Two-Stage Drying Fissure Trial & 10-Lot WAI_3min Intake Calibration",
    share: "INR 24,000 Est. Lab Budget (6 Days)",
    deliverables: "Confirm <0.5% breakage under 65°C->20m temper->55°C vs 85°C blast; calibrate 5-min intake proxy across 10 lots.",
    turnaround: "Days 3 to 8"
  },
  {
    milestone: "EXP-05",
    phase: "ISO 11136:2014 Consumer TOST Sensory Panel (N=72) & GC-MS Hexanal",
    share: "INR 85,000 Accredited Sensory Lab (5 Days)",
    deliverables: "Definitive TOST equivalence CI within [-0.75, +0.75] on Matrix A (unspiced) & Matrix B (Tadka) + triangle test.",
    turnaround: "Days 9 to 14"
  }
];

export const CAD_DRAWING_SHEETS = [
  {
    tag: "DWG-FIN-15T-001",
    title: "Process Flow Diagram (PFD) & Stream Table",
    category: "Process Engineering",
    image: "/drawings/DWG-FIN-15T-001_PROCESS_FLOW_DIAGRAM.png",
    status: "Conceptual FEED / Preliminary",
    desc: "Converged 12-stream mass and enthalpy balance from raw pulse intake through soaking, screen dewatering, fluid bed drying, and 85% bleed-and-feed recycle."
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
    desc: "SS316L ultrasonic steeping vessel fabrication drawing compliant with ASME Section VIII Div 1, showing 40 kHz transducer banks and nozzle schedule."
  },
  {
    tag: "DWG-FIN-15T-008",
    title: "Vibrating Fluid Bed Dryer (DR-101) Mechanical GA",
    category: "Mechanical Fabrication",
    image: "/drawings/DWG-FIN-15T-008_FLUID_BED_DRYER_GA.png",
    status: "Conceptual FEED / Preliminary",
    desc: "Two-stage continuous vibrating fluid bed dryer assembly (65°C Zone 1 / 20-min Tempering / 55°C Zone 2) keeping stress <= 0.71 MPa."
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
    desc: "415 V 3-phase 50 Hz power distribution network detailing motor feeders, 19.2 kW 40 kHz ultrasonic generators, VFD drives, and connected load."
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
    code: "POT-01",
    name: "Untreated Aged Tanzanian HTC Control (S1-02)",
    notes: "Baseline hard-to-cook reference (2H = 2.16 mm)",
    reagent: "None (Dry Raw Dal)",
    ratio: "N/A",
    mechanism: "Intact Ca2+-pectate egg-box cross-links (33.5 mol/m^3); requires 8 whistles (F_WB,core = 25.64 N at W=2)",
    status: "BASELINE_CONTROL"
  },
  {
    code: "POT-02",
    name: "Warm Deionized Water Soak Only (S1-03)",
    notes: "Hydration-only control (55°C, 20 min)",
    reagent: "DI Water Only (55°C, 20 min)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Hydrates grain to 51.3% WB but achieves 0.0% Ca2+ displacement; fails at 8 whistles (F_WB,core = 24.02 N)",
    status: "SOLVENT_CONTROL"
  },
  {
    code: "POT-03",
    name: "0.50% w/v Sodium Bicarbonate (S1-04 / S2-02)",
    notes: "Alkaline beta-elimination control (pH 8.32)",
    reagent: "NaHCO3 (5.0 g/L, 55°C, 20 min)",
    ratio: "1.5:1 liquor-to-grain",
    mechanism: "Mushy outer rim (10.83 N) but hard core (19.89 N, 32% core Ca removal) and detectable soapy off-note (d' = 2.14)",
    status: "REJECTED_ALKALINE"
  },
  {
    code: "POT-04",
    name: "OMEGA Corrected Hybrid K/Na Citrate + UAE (S1-09 / S2-10)",
    notes: "Stage 1 & Stage 2 Verified Winner (pH 5.20)",
    reagent: "0.145 M 90:10 K/Na Citrate (25.20g K3Cit + 2.54g Na3Cit + 11.28g H3Cit / L, 55°C, 20 min + 17 W/L UAE)",
    ratio: "1.5:1 liquor-to-grain + 0.5 L/kg 12s spray wash",
    mechanism: "98.1% bulk & 80.7% core Ca2+ chelation; passes 2 whistles (F_WB,core = 17.35 N) with sub-threshold d' = 0.22",
    status: "OMEGA_WINNER"
  },
  {
    code: "POT-05",
    name: "Tier 3 Intensive Citrate + Vacuum Pulse + UAE",
    notes: "For severe bold Arusha HTC lots (2H >= 2.35 mm)",
    reagent: "0.185 M 90:10 K/Na Citrate (pH 5.20, 57°C, 26 min + 15 kPa Vacuum Pulse + 17 W/L UAE)",
    ratio: "1.5:1 liquor-to-grain + 0.5 L/kg 12s spray wash",
    mechanism: "Fito (1996) outer-rim pore impregnation + acoustic cavitation rescues severe HTC lots to <= 2 whistles",
    status: "SEVERE_HTC_TIER_3"
  },
  {
    code: "IND-REF",
    name: "Authentic Fresh Indian Latur Desi Benchmark (S1-01)",
    notes: "Sensory & texture reference target (2H = 1.70 mm)",
    reagent: "None (Fresh Domestic Harvest)",
    ratio: "Cooked to native t90 (3 whistles)",
    mechanism: "Low native bound Ca2+ (14.0 mol/m^3, DE = 0.52); target benchmark for ISO 11136:2014 TOST equivalence",
    status: "INDIAN_BENCHMARK"
  }
];

export const PLANT_EQUIPMENT = [
  {
    image: "/drawings/TK-101_SolidWorks_3D_Iso.png",
    name: "Staggered Ultrasonic Steeping Vessels",
    tag: "UAE-101A/B",
    type: "Ultrasonic Steep Vessels",
    code: "ASME VIII Div 1",
    capacity: "2 x 600 L Working (375 kg dal + 562.5 L bath each)",
    dimensions: "1,050 mm ID x 1,400 mm TT",
    moc: "AISI SS316L Contact / SS304 Jacket",
    motor: "19.2 kW Total 40 kHz Ultrasonic Transducers (17 W/L) + 2 x 1.5 kW Agitators",
    dwg: "DWG-FIN-15T-007",
    desc: "Two staggered SS316L jacketed steeping vessels operating on a 20.0 min soak + 4.0 min drain/fill cycle to feed 750 kg/h continuously."
  },
  {
    image: "/drawings/DWG-FIN-15T-005_VIBRATING_SCREEN.png",
    name: "Dual-Fan High-Pressure Spray Wash & Air-Knife Deck",
    tag: "WSH-102",
    type: "Spray Wash & Dewatering",
    code: "ISO 2194 / GMP",
    capacity: "750 kg/h dry-basis throughput (4.0 min residence)",
    dimensions: "1,200 mm W x 2,400 mm L",
    moc: "AISI SS316L 20-Mesh Wedge-Wire",
    motor: "2 x 1.5 kW Vibratory Exciters + 5.5 kW Air Knife Blower",
    dwg: "DWG-FIN-15T-005",
    desc: "12.0 s dual-fan high-pressure (2.5 bar, 0.50 L/kg) potable water spray stripping 98.7% of surface film (to 23.3 ppm), followed by air-knife dewatering."
  },
  {
    image: "/drawings/DWG-FIN-15T-006_FLUID_BED_DRYER.png",
    name: "Two-Stage Vibrating Fluid Bed Dryer & Tempering Column",
    tag: "FBD-103 / TMP-104",
    type: "Two-Stage Dryer + Tempering",
    code: "NFPA 68 / 654",
    capacity: "575 kg FBD holdup + 250 kg Tempering Silo (67.0 min total)",
    dimensions: "1,000 mm W x 12,000 mm L + 800 mm ID Tempering Column",
    moc: "AISI SS304 Sanitary Contact",
    motor: "48.5 kW Blowers & Exciters + 195 kW_th Steam Air Heaters",
    dwg: "DWG-FIN-15T-008",
    desc: "Zone 1 (65°C, 22 min) -> Insulated Plug-Flow Tempering Silo (20 min, relaxing delta-X to 0.0016) -> Zone 2 (55°C, 25 min), capping stress at 0.71 MPa (<1.65 MPa yield, 0.35% breakage)."
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
    name: "85% Bleed-and-Feed Liquor Filtration & pH 5.20 Dosing Skid",
    tag: "SK-100",
    type: "Recycle & Dosing Skid",
    code: "FSSAI Food-Grade Standard",
    capacity: "22,579 L/day circulation (85% recycle, 15% sanitary bleed)",
    dimensions: "1,200 mm W x 2,400 mm L x 1,800 mm H",
    moc: "AISI SS316L / 50 um Wedge-Wire + UV-C Sterilizer",
    motor: "3.5 kW Filtration, UV & Diaphragm Dosing Pumps",
    dwg: "DWG-FIN-15T-008",
    desc: "Recovers 85% of drained steeping liquor via 50 um filtration and inline pH/conductivity replenishment (saving ₹5.31/kg in reagent OpEx)."
  },
  {
    image: "/drawings/EV-101_SolidWorks_3D_Iso.png",
    name: "Ambient Counter-Current Cooler & Optical Sorter",
    tag: "PKG-105",
    type: "Cooling & Packaging",
    code: "ISO 22000 / FSSAI GMP",
    capacity: "750 kg/h (12.0 min residence time)",
    dimensions: "1,000 mm W x 4,500 mm L",
    moc: "AISI SS304 Food Contact",
    motor: "7.5 kW Cooling Fan + Bichromatic Optical Sorter",
    dwg: "DWG-FIN-15T-014",
    desc: "Cools conditioned dhal from 55°C to <32°C prior to optical sorting and moisture-barrier packaging."
  }
];

export const BATCH_VARIABILITY_DATA = [
  {
    feedstock: "Severe Bold Arusha/Dodoma Aged HTC (20% of Import Lots)",
    caContent: "36.0 – 44.0 mol/m³",
    thickness: "2.25 – 2.52 mm",
    staticPass: "0.0% Untreated | 16.7% in Fixed Tier 2",
    adaptiveRegime: "Tier 3 Intensive (0.185 M, pH 5.20, 57°C, 26 min + 15 kPa VI) + OOD Hold (4.7%)",
    adaptivePass: "78.0% Overall (89.3% with OOD Quarantine Routing)",
    retainedNa: "4.2 mg/100g",
    status: "RESCUED_BY_TIER_3"
  },
  {
    feedstock: "Nominal Aged Tanzanian Maritime Import (55% of Import Lots)",
    caContent: "28.0 – 36.0 mol/m³",
    thickness: "2.04 – 2.26 mm",
    staticPass: "0.0% Untreated (8 whistles)",
    adaptiveRegime: "Tier 2 Standard (0.145 M, pH 5.20, 55°C, 20 min + 17 W/L UAE)",
    adaptivePass: "84.5% (Mean Core Shear 16.34 N <= 18.0 N)",
    retainedNa: "3.4 mg/100g",
    status: "STANDARD_TIER_2"
  },
  {
    feedstock: "Early-Season Moderate Tanzanian / Mozambique (25% of Import Lots)",
    caContent: "16.0 – 28.0 mol/m³",
    thickness: "1.76 – 2.04 mm",
    staticPass: "0.0% Untreated (5 whistles)",
    adaptiveRegime: "Tier 1 Mild (0.105 M, pH 5.30, 52°C, 15 min + 17 W/L UAE)",
    adaptivePass: "93.2% (Saves 27.6% reagent vs Fixed Tier 2)",
    retainedNa: "2.6 mg/100g",
    status: "REAGENT_SAVING_TIER_1"
  },
  {
    feedstock: "Multi-Species Extension: Chana, Moong, Urad, Masoor Dals",
    caContent: "14.0 – 38.0 mol/m³",
    thickness: "1.30 mm (Masoor) to 2.70 mm (Chana)",
    staticPass: "Chana fails 20m soak (19.85 N); Moong/Masoor over-soften",
    adaptiveRegime: "Moong/Masoor: 12 min Tier 1 (1 wh) | Urad: 18 min | Chana: 28-30 min Tier 3",
    adaptivePass: "Requires Separate Physical Validation per Species",
    retainedNa: "2.5 – 4.1 mg/100g",
    status: "SEPARATE_VALIDATION_REQUIRED"
  }
];

export const FLAVOR_REMEDIATION_DATA = [
  {
    parameter: "Steeping Bath Equilibrium pH (FAIL-0024 Fixed)",
    rawUntreated: "pH 6.45 (Native aqueous slurry)",
    thermalTreated: "Verified pH 5.20 ± 0.05 (Corrected 25.20/2.54/11.28 kg recipe; legacy SOP was pH 6.78)",
    indianDesiBenchmark: "pH 6.10 – 6.35 (Cooked native broth)",
    organolepticImpact: "Prevents both alkaline soapiness (pH > 7.5) and vicilin isoelectric curdling (pI 4.6)"
  },
  {
    parameter: "Lipoxygenase (LOX) Activity & Hexanal Off-Note",
    rawUntreated: "100.0% LOX | >115 ppb Hexanal (Grassy/beany storage note)",
    thermalTreated: "22.0% Residual LOX (78% inactivated at pH 5.20, 55°C) | 44.5 ppb Hexanal",
    indianDesiBenchmark: "~38.0 ppb Hexanal (Fresh domestic Latur baseline)",
    organolepticImpact: "Suppresses grassy lipid oxidation during steeping; ultrasonic degassing strips volatiles"
  },
  {
    parameter: "Surface Film vs Internal Pore Residue (FAIL-0023 Fixed)",
    rawUntreated: "0 ppm exogenous reagent",
    thermalTreated: "23.3 ppm Surface Film (98.7% stripped in 12s spray) | 109.7 mg/100g internal pore citrate",
    indianDesiBenchmark: "180–260 mg/100g native seed citrate",
    organolepticImpact: "Cooked 1:3.5 slurry off-taste ratio R_off = 0.164 (16.4% of human threshold, d' = 0.22)"
  },
  {
    parameter: "Residual Sodium & ISO 11136:2014 TOST Sensory Status",
    rawUntreated: "Native baseline (~12 mg/100g)",
    thermalTreated: "+3.4 mg/100g added Na (89.5% lower than 100% Na-Citrate) | +52.0 mg/100g added K",
    indianDesiBenchmark: "Target Equivalence Margin Delta = ±0.75 hedonic points (N=72 consumers)",
    organolepticImpact: "Sub-threshold model prediction (d'=0.22); human hedonic parity PENDING EXP-05 TOST panel"
  }
];

export const RAPID_PRETREATMENT_DATA = [
  {
    technology: "OMEGA Winner: 40 kHz Ultrasound (17 W/L) + pH 5.20 Hybrid Citrate (S1-09)",
    pulsePressure: "Atmospheric + 17.0 W/L Acoustic Cavitation (55°C)",
    coreTime: "20.0 min steep (98.1% bulk / 80.7% core Ca2+ removal, F_WB,core = 17.35 N)",
    delugeWashTime: "12.0 sec dual-fan spray (0.50 L/kg, 23.3 ppm surface film)",
    moisturePickup: "51.4% WB hydrated -> 28.0% WB after air-knife screen",
    capexCost: "Standard 2 x 600 L Ultrasonic Steep Battery (UAE-101A/B)",
    status: "OMEGA_STAGE_1_2_WINNER"
  },
  {
    technology: "Tier 3 Booster: 15 kPa Vacuum Pulse + 17 W/L UAE (ADAPT-TIER-3)",
    pulsePressure: "15.0 kPa abs initial vacuum pulse + 17.0 W/L UAE (57°C)",
    coreTime: "26.0 min steep (Rescues bold 2.44 mm Arusha severe HTC lots to <= 2 whistles)",
    delugeWashTime: "12.0 sec dual-fan spray (0.50 L/kg)",
    moisturePickup: "+8.15% outer-rim pore filling at t=0 (Fito 1996 HDM limit)",
    capexCost: "Liquid-ring vacuum manifold engaged only on Tier 3 lots (25% of batches)",
    status: "SEVERE_HTC_BOOSTER"
  },
  {
    technology: "Legacy 4.6-Min Vacuum Impregnation Shortcut (S1-10 — Falsified)",
    pulsePressure: "15.0 kPa abs vacuum pulse only (No time for core diffusion)",
    coreTime: "4.6 min steep -> FAILS (Only 5.2% core Ca2+ removal, F_WB,core = 24.63 N, 7 wh)",
    delugeWashTime: "12.0 sec spray",
    moisturePickup: "Limited by dry cotyledon open porosity epsilon = 0.11 (FAIL-0023)",
    capexCost: "Rejected — Legacy script unphysically pre-filled 70% of grain at t=0",
    status: "REJECTED_BY_PHYSICS"
  }
];

export const RICHARDSON_CONVERGENCE_DATA = {
  orderOfAccuracy: 1.94,
  theoreticalOrder: 2.00,
  exactContinuumLimitMin: 8.30,
  gciFinePct: 0.62,
  uncertaintyBandMin: 0.08,
  grids: [
    { grid: "10 x 10 (Fast Sobol)", nodes: "100 FVM Cells", cookTime: "8.35 min", whistles: "2 wh", coreForce: "17.42 N", solveTime: "0.042s" },
    { grid: "14 x 14 (Standard)", nodes: "196 FVM Cells", cookTime: "8.30 min", whistles: "2 wh", coreForce: "17.35 N", solveTime: "0.094s" },
    { grid: "28 x 28 (Fine Reference)", nodes: "784 FVM Cells", cookTime: "8.28 min", whistles: "2 wh", coreForce: "17.31 N", solveTime: "0.610s" }
  ]
};

export const GOVERNANCE_TELEMETRY = {
  pythonVersion: "3.13.7",
  torchCuda: "PyTorch 2.6.0+cu124 | CPU 2D PDE: 93.7 ms/eval (Beats GPU for N<=256)",
  gpuDevice: "AMD Ryzen AI 9 365 (20 Threads) + NVIDIA RTX 4050 Laptop GPU",
  fanLimits: "Offline-First Execution Mode Active (Zero Live Network Dependency in Solvers)",
  thermalEnvelope: "Full 4-Stage OMEGA Investigation + 224-Run Sobol Completed in 51.14 s",
  massBalanceClosure: "0.000000% Error | Reconciled 85% Recycle OpEx: ₹6.34/kg (vs ₹11.65/kg Once-Through)",
  handoffStatus: "VALIDATED (42/42 Pytest Suite + Hash-Chained Defect Ledger Intact)",
  defectCoverage: "25 Defect Records (FAIL-0001 to FAIL-0025), 42/42 Automated Tests Passed (100%)",
  codeSplitting: "Vite Chunking: vendor-three + core OMEGA telemetry"
};

export const DEFECT_REGISTRY_HIGHLIGHTS = [
  {
    code: "FAIL-0001",
    subsystem: "Physical Balances",
    defect: "Unbalanced 15 TPD Mass Balance & Phantom Recovery",
    cause: "Dry matter leached omitted from downstream dryer feed, violating conservation laws.",
    fix: "Derived strict closed-loop dry matter balance across steeping, washing, and drying.",
    status: "CLOSED / VERIFIED"
  },
  {
    code: "FAIL-0003",
    subsystem: "Thermal Sizing",
    defect: "Pre-Dryer Evaporation Discrepancy (Scenario B1 vs B2)",
    cause: "Discrepancy between 28.0% WB screen moisture (3,654.42 kg/d evap) and 28.7735% WB moisture (3,854.14 kg/d evap).",
    fix: "Preserved exact +199.72 kg/d water delta (+5.47% evaporative load) until EXP-02 screen drainage trial.",
    status: "PROVISIONALLY_BOUND"
  },
  {
    code: "FAIL-0021",
    subsystem: "Drying Mechanics",
    defect: "Uncoupled 25°C Drying Diffusivity, 60^n Unit Bug & Plum Citation",
    cause: "simulate_drying_cycle.py predicted identical 1.18 MPa stress at 85°C and 65°C, violated 2.0 MPa guard (2.4 MPa), and cited Goyal (2007) plum drying.",
    fix: "Coupled D_eff(T) and Page k(T) in Module H: proved 85°C causes 1.85 MPa fissuring (3.19% broken) vs 0.71 MPa (0.35% broken) for 65°C->20m temper->55°C.",
    status: "CLOSED / VERIFIED"
  },
  {
    code: "FAIL-0022",
    subsystem: "Stage 1/3 Consistency",
    defect: "Citrate Stage 1 Failure (19.3 N) vs Stage 2 Winner & Stage 3 Oracle Leakage",
    cause: "simulate_feedstock_variability.py failed Citrate in Stage 1, omitted grain thickness in Stage 3, and leaked true bound Ca2+ into adaptive selector.",
    fix: "Unified 2D PDE proves 20 min UAE + pH 5.20 Citrate passes Stage 1 (17.35 N <= 18 N); built noisy 5-min WAI_3min intake classifier (76.0% accuracy).",
    status: "CLOSED / VERIFIED"
  },
  {
    code: "FAIL-0023",
    subsystem: "Transport & Sensory",
    defect: "Unphysical 70% Vacuum Pre-Fill (4.6m Claim), Wash Hardcoding & Fake 8.8 Hedonics",
    cause: "simulate_pretreatment.py pre-filled 70% of dry grain at t=0 (violating epsilon=0.11), ignored internal pore solute, and fabricated 8.8/9.0 hedonic scores.",
    fix: "Enforced Fito (1996) HDM limit (proving 4.6m VI fails at 24.63 N), modeled surface film vs internal pore washing, and designed N=72 ISO 11136 TOST study.",
    status: "CLOSED / VERIFIED"
  },
  {
    code: "FAIL-0024",
    subsystem: "Buffer Stoichiometry",
    defect: "SOP Tier 2 & Bench Pot 4 Claimed pH 5.20 But Equilibrated at pH 6.78 & 5.91",
    cause: "Historical recipes used 33.8 kg K3Cit·H2O + 3.7 kg Na3Cit·2H2O + only 2.5 kg Citric Acid per 1000 L, leaving LOX active at pH 6.78.",
    fix: "Solved exact multi-protic electroneutrality in Module D: 25.20 kg K3Cit·H2O + 2.54 kg Na3Cit·2H2O + 11.28 kg Citric Acid locks pH at 5.20.",
    status: "CLOSED / VERIFIED"
  },
  {
    code: "FAIL-0025",
    subsystem: "Plant Economics",
    defect: "Unreconciled Once-Through Reagent Mass (899 kg/d = ₹9.49/kg) vs Claimed ₹0.42/kg OpEx",
    cause: "15TPD_FACTORY_SOP_AND_RECIPES.md listed once-through daily salt consumption without bath recycling while claiming ₹0.42/kg reagent cost.",
    fix: "Reconciled both modes in Module H: Once-Through = ₹8.62/kg reagent (₹11.65/kg total) vs 85% Bleed-and-Feed Recycle = ₹3.63/kg reagent (₹6.34/kg total OpEx).",
    status: "CLOSED / VERIFIED"
  }
];

export const THERMAL_DUTY_DELTA_AUDIT = [
  {
    scenario: "Scenario B1 (Design Base — Vibratory Air-Knife Screen)",
    screenMoisture: "28.00% Wet Basis",
    dryerInletWater: "5,149.28 kg/day",
    evaporationLoad: "3,654.42 kg/day",
    dryerThermalDuty: "142.8 kWth",
    impact: "Standard sizing baseline for Two-Stage 65°C / 55°C Fluidized Bed Dryer"
  },
  {
    scenario: "Scenario B2 (Conservative Screen Drainage Bound)",
    screenMoisture: "28.7735% Wet Basis",
    dryerInletWater: "5,349.00 kg/day",
    evaporationLoad: "3,854.14 kg/day",
    dryerThermalDuty: "150.5 kWth",
    impact: "+199.72 kg/d water delta (+5.47% evaporative load increase)"
  },
  {
    scenario: "Reconciliation Strategy (EXP-02)",
    screenMoisture: "Monday Bench & Pilot Screen Trial",
    dryerInletWater: "Dynamic 5,149 – 5,349 kg/day",
    evaporationLoad: "Dynamic 3,654.42 – 3,854.14 kg/day",
    dryerThermalDuty: "FBD-103 heater sized at 195 kWth peak capacity",
    impact: "Zero process bottleneck risk; steam valve modulated to dewatering screen exit moisture"
  }
];
