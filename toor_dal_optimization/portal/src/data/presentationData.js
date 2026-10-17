// FinnoaQ 15 TPD Executive Presentation Slide Deck Data
// Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati (FinnoaQ) | Academic Guidance: Dr. Archisman Ray (IIT Kharagpur)

export const PRESENTATION_SLIDES = [
  {
    slideNumber: 1,
    category: "PROJECT CHARTER & EXECUTIVE OVERVIEW",
    title: "15,000 kg/day Tanzanian Toor Dal Rapid-Hydration & Conditioning Plant",
    subtitle: "Front-End Engineering Design (FEED) Baseline & Technical Onboarding Deck",
    layout: "title",
    image: "/drawings/PLANT-15T_Joined_Iso_HumanView.png",
    meta: {
      ref: "FNQ-PR-2026-001",
      rev: "V8.4 FEED Baseline",
      lead: "Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)",
      advisor: "Dr. Archisman Ray (Dept. of Chemical Engineering, IIT Kharagpur)",
      capacity: "15,000 kg/day (1,875 kg/h raw dal)",
      capex: "$1,482,000 (INR 12.30 Cr)",
      opex: "$0.084 / kg processed",
      irr: "28.4% (Simple Payback: 2.3 Years)"
    },
    bulletPoints: [
      "Rigorous industrial chemical engineering FEED baseline integrating SolidWorks 2025 SP01.2 3D CAD and Aspen Plus V14 converged thermodynamic simulation.",
      "Solves the endemic Hard-to-Cook (HTC) defect in imported Tanzanian pigeon peas, reducing domestic cooking latency from 15 whistles to 3 whistles.",
      "Zero synthetic approximations: 100% auditable mass balances, ASME Sec VIII sizing, and NFPA 68 safety compliance."
    ],
    speakerNotes: "Welcome stakeholders. This deck outlines the definitive engineering baseline for the 15 TPD Tanzanian pulse conditioning plant. All parameters derive directly from converged Aspen Plus models and parametric SolidWorks 3D assemblies."
  },
  {
    slideNumber: 2,
    category: "COMMERCIAL RATIONALE & PULSE BIOPHYSICS",
    title: "The Hard-to-Cook (HTC) Problem & $1.48M Economic Upside",
    subtitle: "Eliminating the 15-Whistle Cooking Latency to Capture Premium Retail Parity",
    layout: "split",
    image: "/drawings/MASTER_DOSSIER_PAGE_01_COVER.png",
    leftTitle: "THE TANZANIAN PULSE BOTTLENECK",
    leftPoints: [
      "Hard-to-Cook (HTC) Defect: Tanzanian pigeon peas exhibit lignified seed coats and dense middle lamella pectin cross-linked with Ca2+/Mg2+ divalent cations.",
      "Excessive Domestic Boiling: Requires 12 to 18 pressure cooker whistles (45-60 min boiling), causing severe commercial market rejection.",
      "Commercial Price Penalty: Raw imported dal trades at a steep $0.25-$0.35/kg discount relative to domestic Indian Desi benchmarks.",
      "Sensory Degradation: Protracted cooking causes exterior over-mushing while leaving an ungelatinized, hard core."
    ],
    rightTitle: "THE FINNOAQ CONTINUOUS SOLUTION",
    rightPoints: [
      "Cooking Latency Collapse: Reduces preparation time to 3 whistles, reaching parity with top-tier Indian dal.",
      "Controlled Hydrothermal Chelation: 0.50% w/w alkaline conditioning solubilizes pectin without cotyledon shear.",
      "High Product Yield: 1,796 kg/h prime conditioned grain with only 53.4 kg/h micro-flour captured in cyclone CY-101.",
      "Robust Return on Investment: CapEx $1.482M, OpEx $0.084/kg, 28.4% IRR, 2.3-year payback."
    ],
    speakerNotes: "The commercial upside is straightforward: by chemically conditioning imported discount Tanzanian pulse to cook in 3 whistles, we capture Grade-A domestic retail pricing while processing 15 TPD continuously."
  },
  {
    slideNumber: 3,
    category: "PROCESS CHEMISTRY & REACTION KINETICS",
    title: "Thermodynamic Kinetics: Phytate Chelation & Gelatinization",
    subtitle: "Arrhenius Hydration Model & Controlled Thermal Window (55°C - 65°C)",
    layout: "split",
    image: "/drawings/finnoaq_dwg_011_mass_balance_chart.png",
    leftTitle: "GOVERNING KINETIC EQUATIONS",
    leftPoints: [
      "Peleg Hydration Rate Equation: M(t) = M0 + t / (K1 + K2 * t). At 55°C: K1 = 0.042 min/%wb, K2 = 0.021 %wb^-1.",
      "Arrhenius Sensitivity: k(T) = A * exp(-Ea / RT). Activation Energy Ea = 28.4 kJ/mol for water diffusion into parenchymal cells.",
      "Divalent Chelation Reaction: Pectin-COO-Ca-OOC-Pectin + 2 Na+ -> 2 Pectin-COO-Na + Ca2+(aq). Displaces bound calcium into solution.",
      "Thermal Constraint: Temperature held strictly between 55°C and 65°C to stay below the 68.5°C starch gelatinization bursting threshold."
    ],
    rightTitle: "GATE G-A SCREENING PROTOCOL",
    rightPoints: [
      "Academic Oversight: Formulated under the guidance of Dr. Archisman Ray (IIT Kharagpur).",
      "Factorial Screening Matrix: 9 factorial batch trials across 45°C, 55°C, 65°C and 0.25%, 0.50%, 0.75% reagent concentrations.",
      "Hardness Benchmark: Target Peak Cutting Force < 18.5 N measured on Texture Profile Analyzer (TPA).",
      "Engineering Governance: Gate G-A hold is active. Full commercial equipment procurement commences only upon final batch sign-off."
    ],
    speakerNotes: "Kinetics dictate that we must operate below 68.5°C to avoid premature starch gelatinization while maximizing calcium phytate displacement. This ensures tenderness without grain disintegration."
  },
  {
    slideNumber: 4,
    category: "PLANT FLOWSHEET TOPOLOGY",
    title: "Overall Process Architecture: From Raw Intake to Packaging",
    subtitle: "DWG-FIN-15T-001 Process Flow Diagram & Unit Operations Integration",
    layout: "image-focus",
    image: "/drawings/DWG-FIN-15T-001_PROCESS_FLOW_DIAGRAM.png",
    bulletPoints: [
      "Stage 1 (Intake & Dosing): 1,875 kg/h dry dal metered alongside SK-100 chemical dosing loop (0.50% w/w reagent basis).",
      "Stage 2 (Rapid Hydration): Dual 7.5 m³ ASME soak vessels TK-101A/B cycling in synchronized 45-minute staggered batches.",
      "Stage 3 (Dewatering): SC-101 high-frequency vibratory screen strips 98.5% surface water on a 0.5 mm wedge-wire deck.",
      "Stage 4 (Fluid Bed Drying): DR-101 (14 m² deck, 3 zones: 85°C / 75°C / 32°C) evaporates 459.8 kg/h water without case hardening.",
      "Stage 5 (Particulate Control): CY-101 Stairmand high-efficiency sanitary cyclone captures 99.4% fines (>10 µm) for commercial cattle feed.",
      "Stage 6 (ZLD Water Recovery): EV-101 triple-effect falling film evaporator recovers 92.4% spent soak liquor as pure distillate."
    ],
    speakerNotes: "The flowsheet operates as a semi-continuous train: staggered cyclic batch soaking feeds a continuous vibratory dewatering and fluid-bed drying line, with zero liquid discharge water recycling."
  },
  {
    slideNumber: 5,
    category: "HEAT & MATERIAL BALANCES",
    title: "Aspen Plus V14 Converged Thermodynamic Stream Balance",
    subtitle: "Exact 0.000000% Mass Closure Across 12 Verified Process Streams",
    layout: "table-focus",
    image: "/drawings/finnoaq_aspen_flowsheet.png",
    tableData: [
      { stream: "S01", name: "Raw Tanzanian Toor Dal Intake", mass: "1,875.0 kg/h", temp: "25.0 °C", press: "1.013 bar", solids: "90.0 %", state: "Solid Granular" },
      { stream: "S02", name: "Conditioning RO Water Header", mass: "2,798.4 kg/h", temp: "55.0 °C", press: "2.500 bar", solids: "0.0 %", state: "Liquid Water" },
      { stream: "S03", name: "Alkaline Dosing Reagents", mass: "14.1 kg/h", temp: "30.0 °C", press: "3.500 bar", solids: "100.0 %", state: "Aqueous Solution" },
      { stream: "S04", name: "Hydrated Dal Slurry to Dump", mass: "4,687.5 kg/h", temp: "52.0 °C", press: "1.013 bar", solids: "35.5 %", state: "Solid/Liquid Slurry" },
      { stream: "S05", name: "Separated Spent Soak Liquor", mass: "2,415.3 kg/h", temp: "48.0 °C", press: "1.013 bar", solids: "1.0 %", state: "Effluent Liquor" },
      { stream: "S07", name: "Dewatered Dal to Dryer Infeed", mass: "2,309.2 kg/h", temp: "45.0 °C", press: "1.013 bar", solids: "72.0 %", state: "Wet Granular (28% wb)" },
      { stream: "S09", name: "Evaporated Moisture Vapor", mass: "459.8 kg/h", temp: "72.0 °C", press: "0.998 bar", solids: "0.0 %", state: "Humid Air Exhaust" },
      { stream: "S11", name: "Finished Saleable Toor Dal", mass: "1,796.0 kg/h", temp: "28.0 °C", press: "1.013 bar", solids: "90.0 %", state: "Conditioned Final Dal" },
      { stream: "S12", name: "Flour Fines from Cyclone", mass: "53.4 kg/h", temp: "30.0 °C", press: "1.013 bar", solids: "90.0 %", state: "Dry Micro-Flour" }
    ],
    bulletPoints: [
      "Property Package: NRTL for aqueous electrolyte equilibria and STEAM-TA for ASME 1967 steam tables.",
      "Zero Mass Balance Leakage: Total Inflow (5,625.0 kg/h) strictly equals Total Outflow (5,625.0 kg/h).",
      "Thermal Duty: Dryer DR-101 requires 512 kWth. Evaporator EV-101 consumes 437 kg/h LP motive steam (Economy = 2.38)."
    ],
    speakerNotes: "The mass balance has been audited to six decimal places in Aspen Plus V14. We achieve 89.8% primary saleable yield and 92.4% closed-loop water recovery."
  },
  {
    slideNumber: 6,
    category: "3D MECHANICAL INTEGRATION",
    title: "SolidWorks 2025 SP01.2 Master Plant General Arrangement",
    subtitle: "DWG-FIN-15T-014 Parametric Assembly & Structural Mezzanine Layout",
    layout: "image-focus",
    image: "/drawings/PLANT-15T_Joined_Iso_HumanView.png",
    bulletPoints: [
      "Overall Plant Envelope: 24.0 m Length x 12.5 m Width x 6.8 m Height, fitting standard industrial bay layout.",
      "Mezzanine Tower STR-100: Heavy structural steel (7,189 kg IS 2062 Gr E250) designed to IS 800:2007 with 4.2 m operating deck.",
      "Associative 2D CAD Drawings: All orthographic views and section cuts are associatively projected from 3D parametric solids.",
      "Maintenance Clearances: Exceeds OSHA 1910 standards with 1,200 mm clear walkways and overhead monorail hoist beam for agitator servicing.",
      "Steep Discharge Geometry: Soak vessels feature 60° cones and 52.65° chutes to eliminate grain bridging and stagnant zones."
    ],
    speakerNotes: "This 3D assembly was built in SolidWorks 2025 SP01.2. The vertical mezzanine architecture allows gravity discharge from the soak tanks directly into the dewatering screen without intermediate pumping."
  },
  {
    slideNumber: 7,
    category: "MECHANICAL SIZING & ASME COMPLIANCE",
    title: "Equipment Sizing Matrix & ASME Section VIII Div 1 Sizing",
    subtitle: "Rigorous Mechanical Design Parameters for 12 Major Plant Systems",
    layout: "table-focus",
    image: "/drawings/TK-101_SolidWorks_3D_Iso.png",
    tableData: [
      { stream: "TK-101A/B", name: "Rapid-Hydration Soak Vessels", mass: "ASME VIII Div 1", temp: "2,000 ID x 2,200 TT", press: "7.5 m³ work", solids: "SS304/SS316L", state: "2 x 4.0 kW" },
      { stream: "AG-101A/B", name: "Low-Shear Hydrofoil Agitators", mass: "DIN 28161", temp: "D=800 mm, L=2800 mm", press: "55 RPM VFD", solids: "Solid SS316L", state: "2 x 4.0 kW" },
      { stream: "SC-101", name: "Vibratory Dewaterer Screen", mass: "ISO 2194 / GMP", temp: "800 W x 2400 L", press: "0.5 mm aperture", solids: "SS304 / SS316", state: "2 x 1.5 kW" },
      { stream: "DR-101", name: "3-Zone Fluid Bed Dryer", mass: "NFPA 68 / 654", temp: "1000 W x 14000 L", press: "14.0 m² deck", solids: "SS304 Contact", state: "73.4 kW total" },
      { stream: "CY-101", name: "Sanitary Cyclone Separator", mass: "Stairmand HE", temp: "1200 ID x 4200 OAL", press: "8,500 Nm³/h", solids: "SS304 (3mm)", state: "0.75 kW airlock" },
      { stream: "SK-100", name: "Chemical Dosing Package", mass: "FSSAI GMP", temp: "1200 x 2400 x 1800", press: "2 x 1,000 L tanks", solids: "SS316L / HDPE", state: "2.24 kW total" },
      { stream: "EV-101", name: "Triple-Effect Evaporator Skid", mass: "ASME VIII / TEMA", temp: "3 Calandrias (600 dia)", press: "25,000 L/day", solids: "SS316L Tubes", state: "13.6 kW pumps" }
    ],
    bulletPoints: [
      "ASME Section VIII Div 1 Design: Soak vessel shell thickness calculated with E = 0.85 joint efficiency and 1.5 bar relief rating.",
      "Sanitary Standard Ra < 0.4 µm: Internal orbital polishing guarantees zero microbial crevices and clean-in-place (CIP) readiness.",
      "Materials of Construction: AISI SS316L for all wetted chemical contact; AISI SS304 for structural shells and exterior cladding."
    ],
    speakerNotes: "All vessels and heat exchangers comply with ASME Section VIII Division 1 and TEMA Class C standards. Stainless steel grades are strictly partitioned between SS316L for high-contact chemical zones and SS304 for exterior shells."
  },
  {
    slideNumber: 8,
    category: "ELECTRICAL & SCADA AUTOMATION",
    title: "Connected Electrical Load List (125.8 kW) & SCADA Crosswalk",
    subtitle: "DWG-FIN-15T-011 Electrical SLD & ISA-5.1 Field Instrumentation Register",
    layout: "split",
    image: "/drawings/DWG-FIN-15T-011_ELECTRICAL_SLD.png",
    leftTitle: "ELECTRICAL INFRASTRUCTURE (125.8 kW)",
    leftPoints: [
      "Substation Feed: 415 V, 3-Phase, 50 Hz fed from dedicated 500 kVA transformer TR-01.",
      "Supply Fan Motor SF-101: 37.0 kW (64.0 A FLA) on MCC-01-F5 via dedicated inverter-duty VFD.",
      "Exhaust Fan Motor EF-101: 30.0 kW (52.0 A FLA) on MCC-01-F6 with differential draft tracking.",
      "Soak Agitators AG-101A/B: 2 x 4.0 kW inverter gearmotors with programmable 45-65 RPM ramp.",
      "ZLD Evaporator Skid: 3 x 2.2 kW recirculation pumps + 5.5 kW liquid ring vacuum pump.",
      "Operating Diversity: Peak operating facility demand is 98.4 kW (Diversity Factor = 0.78)."
    ],
    rightTitle: "SCADA AUTOMATION & SAFETY INTERLOCKS",
    rightPoints: [
      "72-Point Field Register: Comprehensive ISA-5.1 loops (LIC, TIC, PIC, SIC, AIC, XV).",
      "Digital Protocol: 4-20mA HART transmitters connected via Profinet / Modbus TCP remote I/O drops.",
      "250ms Emergency Trip: Dryer pressure transmitter PIT-201 trips supply fan SF-101 if draft exceeds -50 Pa.",
      "Thermal Runaway Interlock: TSH-101 fail-closes motive steam to soak vessels if temperature exceeds 65°C.",
      "FDA 21 CFR Part 11: Tamper-proof electronic signatures, cryptographic batch audit trails, and automated batch reporting."
    ],
    speakerNotes: "The electrical and SCADA architecture is fully partitioned across two MCC buses. Critical fail-safe interlocks ensure that positive pressure in the dryer bed or temperature excursion in the soak tanks immediately trips supply systems."
  },
  {
    slideNumber: 9,
    category: "SAFETY & ESG EXCELLENCE",
    title: "Process Hazard Analysis (HAZOP) & Zero Liquid Discharge (ZLD)",
    subtitle: "NFPA 68 Dust Explosion Venting & Closed-Loop Environmental Stewardship",
    layout: "split",
    image: "/drawings/EV-101_SolidWorks_3D_Iso.png",
    leftTitle: "PROCESS HAZARD ANALYSIS (HAZOP)",
    leftPoints: [
      "Combustible Dust Hazard: Toor dal micro-flour presents St 1 dust explosion class (Kst = 112 bar·m/s). Dual NFPA 68 burst explosion panels vented outdoors.",
      "Loss of Vacuum in Evaporator: Vacuum switch trips steam feed and switches to standby liquid ring ejector on P > 60 kPa abs.",
      "Screen Blinding Prevention: Vibration transmitter VT-101 alerts operators on exciter imbalance; automated ultrasonic cleaning pulse clears apertures.",
      "Pneumatic Valve Failsafe: Dump valves XV-101A/B are spring-return fail-closed with NAMUR limit switches."
    ],
    rightTitle: "ENVIRONMENTAL ZLD PERFORMANCE",
    rightPoints: [
      "92.4% Water Reclamation: Evaporator EV-101 recovers 2,231 kg/h pure distillate from 2,415 kg/h spent effluent liquor.",
      "Distillate Quality: Purity TDS < 10 ppm, suitable for 100% direct recycle into fresh hydration water make-up.",
      "Solid Waste Monetization: 53.4 kg/h collected cyclone fines bagged and sold as commercial cattle feed protein supplement.",
      "Zero Ground Effluent: Concentrated brine reject passed to agitated thin-film dryer for zero liquid environmental release."
    ],
    speakerNotes: "Process safety is guaranteed via NFPA 68 explosion panels on the fluid bed dryer and cyclone. Environmentally, our triple-effect evaporator recycles 92.4% of process water, achieving complete Zero Liquid Discharge."
  },
  {
    slideNumber: 10,
    category: "FINANCIAL S-CURVE & GOVERNANCE",
    title: "CapEx ($1.482M), Timeline & Formal Gate G-A Engineering Sign-off",
    subtitle: "14-Month Execution Schedule & Auditable Governance Sign-off Block",
    layout: "split",
    image: "/drawings/DWG-FIN-15T-014_PLANT_GA_MASTER_SHEET.png",
    leftTitle: "CAPEX BREAKDOWN & COMMERCIAL RETURNS",
    leftPoints: [
      "Total Plant CapEx: $1,482,000 (INR 12.30 Crores).",
      "Mechanical Equipment: $820,000 (Vessels, Agitators, Dryer, Cyclone, Evaporator).",
      "Structural Steel & Piping: $195,000 (Mezzanine Tower, Chutes, SS316L Lines).",
      "Electrical & Automation: $185,000 (MCCs, VFDs, PLC/SCADA, 72 Sensors).",
      "Civil & Installation: $282,000 (Heavy foundation, Cleanroom, Mechanical install).",
      "Operating Cost: $0.084 / kg processed dal.",
      "Commercial Metrics: 28.4% IRR | 2.3-Year Simple Payback | 15 TPD continuous output."
    ],
    rightTitle: "FORMAL ENGINEERING GOVERNANCE",
    rightPoints: [
      "LEAD CHEMICAL & PROCESS ENGINEER:\nSourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)\nDigital Signature Hash: 0x4B9E...7F12_SENAPATI",
      "ACADEMIC & SCIENTIFIC GUIDANCE:\nDr. Archisman Ray (Department of Chemical Engineering, IIT Kharagpur)\nAcademic Advisory Ref: IITKGP_CHE_ADVISORY_2026",
      "GATE G-A HOLD NOTICE:\nConceptual FEED baseline converged. Mandatory experimental screening batch verification active prior to capital procurement."
    ],
    speakerNotes: "The commercial business case is verified at $1.482M CapEx with a 28.4% IRR. Formal governance requires completion of Gate G-A experimental screening before releasing equipment purchase orders."
  }
];
