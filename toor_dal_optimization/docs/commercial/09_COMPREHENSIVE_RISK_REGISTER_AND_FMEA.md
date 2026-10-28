# FINNOAQ OMEGA — COMPREHENSIVE RISK REGISTER & FAILURE MODE AND EFFECTS ANALYSIS (FMEA)

**Project Reference:** FNQ-PR-2026-001  
**Lead Chemical & Process Engineer:** Sourish Senapati  
**Scope:** Multi-Domain Risk Matrix, FMEA Scoring (RPN), Quantitative Stopping Rules & Mitigation Protocols  
**Governance:** Truth Precedes Completeness; Rigorous Identification and Pre-emption of Failure Modes  

---

## 1. FMEA Methodology & Scoring Taxonomy

The Failure Mode and Effects Analysis (FMEA) quantitatively prioritizes technical, operational, regulatory, and commercial risks across the 15 TPD scale-up project.

### Scoring Scale (1 to 10)
- **Severity ($S$):** 1 = Negligible minor defect; 5 = Batch rejection / rework; 10 = Catastrophic plant failure, food safety recall, or company insolvency.
- **Occurrence ($O$):** 1 = Extremely remote ($< 0.1\%$ probability); 5 = Occasional occurrence ($2–5\%$ probability); 10 = Inevitable without control ($> 50\%$).
- **Detection ($D$):** 1 = Automated inline sensor detection with failsafe interlock; 5 = Manual offline lab testing within 4 hours; 10 = Undetectable prior to consumer usage.
- **Risk Priority Number ($\text{RPN}$):**
  $$\text{RPN} = S \times O \times D \quad (1 \le \text{RPN} \le 1,000)$$
  - High Risk: $\text{RPN} \ge 150$ (Mandates engineering design intervention before pilot)
  - Medium Risk: $80 \le \text{RPN} < 150$ (Requires strict standard operating procedures and online monitoring)
  - Low Risk: $\text{RPN} < 80$ (Acceptable under routine maintenance and plant controls)

---

## 2. Multi-Domain FMEA Risk Matrix (20 Identified Failure Modes)

| Risk ID | Domain | Failure Mode & Physical Mechanism | $S$ | $O$ | $D$ | Initial RPN | Engineering Mitigation & Failsafe Protocol | Post-Mitigation RPN |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RSK-01** | Biological | Severe HTC variation across African regions ($> 40\text{ meq Ca}^{2+}/\text{kg}$) causing under-cooking | 8 | 6 | 4 | **192** | 48-Hour Feedstock Titration; automated PLC adjustment of auger residence from 24 to 28 min | **48** ($8 \times 3 \times 2$) |
| **RSK-02** | Biological | High raw feed moisture ($> 14\%\text{ wb}$) causing mold/mycotoxin contamination | 9 | 3 | 2 | **54** | Reject lots $> 13.0\%\text{ wb}$ at intake; aflatoxin rapid lateral-flow strip test | **18** ($9 \times 1 \times 2$) |
| **RSK-03** | Chemical | Steeping pH drift above 5.4 due to basic seed ash leaching, causing white salt bloom | 7 | 5 | 3 | **105** | Online glass-electrode pH sensor; automatic citric acid dosing feedback loop to hold pH 5.20 ± 0.05 | **28** ($7 \times 2 \times 2$) |
| **RSK-04** | Chemical | Steeping temperature spike ($> 65^\circ\text{C}$) causing premature starch gelatinization and fouling | 9 | 4 | 2 | **72** | Redundant Class A RTDs; fail-closed pneumatic steam shutoff valve triggering at 50.0°C | **18** ($9 \times 1 \times 2$) |
| **RSK-05** | Chemical | Chemical residue exceedance (phosphate $> 500\text{ mg/kg}$ or surface salts $> 80\text{ ppm}$) | 9 | 4 | 5 | **180** | Counter-current spray wash ($0.50\text{ L/kg}$); in-line rinse conductivity monitor ($< 120\text{ }\mu\text{S/cm}$) | **36** ($9 \times 2 \times 2$) |
| **RSK-06** | Mechanical | Cotyledon fissuring/checking in drying due to tensile hoop stress ($> 2.4\text{ MPa}$) | 8 | 7 | 3 | **168** | Two-stage fluid bed drying with 20 min unheated tempering at 45°C; checking held $< 2.0\%$ | **32** ($8 \times 2 \times 2$) |
| **RSK-07** | Mechanical | Dewatering screen blinding due to fine fragments and starch solids | 6 | 5 | 3 | **90** | High-G elliptical motion wedge-wire screen (0.8 mm slot); automated CIP water back-pulse | **24** ($6 \times 2 \times 2$) |
| **RSK-08** | Mechanical | Fluid bed drying duct clogging or uneven air fluidization | 7 | 4 | 3 | **84** | Sanitary perforated deck design; differential pressure transmitters across bed with alarm | **28** ($7 \times 2 \times 2$) |
| **RSK-09** | Mechanical | Boiler failure or steam interruption during continuous steeping | 7 | 3 | 2 | **42** | Backup electric immersion elements (30 kW) in steep jacket; dual boiler feed pumps | **21** ($7 \times 1 \times 3$) |
| **RSK-10** | Mechanical | Membrane fouling in nanofiltration water recovery unit | 6 | 5 | 3 | **90** | Automated 4-hour forward flush; enzymatic weekly CIP wash; cartridge pre-filtration ($5\text{ }\mu\text{m}$) | **24** ($6 \times 2 \times 2$) |
| **RSK-11** | Sensory | Lingering mineral-saline or astringent aftertaste reported by consumers | 8 | 5 | 5 | **200** | ISO 4120 3-AFC sensory gating in bench phase; wash ratio enforced $\ge 0.50\text{ L/kg}$ | **40** ($8 \times 1 \times 5$) |
| **RSK-12** | Sensory | Cooking broth cloudiness or foam formation during domestic pressure cooking | 5 | 4 | 3 | **60** | Pre-cleaning aspiration removes all surface flour dust; single-pass rinse strips soluble pectins | **20** ($5 \times 2 \times 2$) |
| **RSK-13** | Sensory | Non-uniform tenderness (soft shell with hard core) within individual dal grains | 7 | 5 | 3 | **105** | Steep auger designed for plug flow (dispersion number $D/uL < 0.02$); uniform boundary layer | **28** ($7 \times 2 \times 2$) |
| **RSK-14** | Regulatory | FSSAI food inspector inspection or seizure due to unapproved additive allegation | 9 | 3 | 4 | **108** | Certified legal dossier classifying reagents under Category 14.1.4 and GMP Appendix A; lab certificates | **27** ($9 \times 1 \times 3$) |
| **RSK-15** | Regulatory | State Pollution Control Board notice on effluent discharge volume or COD | 8 | 4 | 3 | **96** | Zero Liquid Discharge (ZLD) architecture: NF recovers 85% water; solar brine evaporation | **24** ($8 \times 1 \times 3$) |
| **RSK-16** | Regulatory | AGMARK grade rejection due to excess broken percentage ($> 1.5\%$) | 7 | 5 | 2 | **70** | Tempered drying holds brokens $< 1.1\%$; high-precision optical sorter recycles splits | **21** ($7 \times 1 \times 3$) |
| **RSK-17** | Commercial | Compression of mandi price spread (African discount narrows from ₹20 to ₹12/kg) | 8 | 5 | 3 | **120** | Flexible tolling model (fee drops to ₹8/kg; cash breakeven at 18.7% capacity); proprietary retail brand | **48** ($8 \times 3 \times 2$) |
| **RSK-18** | Commercial | Partner mill backs out of Phase 3 demonstration or defaults on utility provision | 7 | 4 | 4 | **112** | 6 qualified host mills shortlisted in Phase 0 discovery; legally binding term sheet with penalties | **35** ($7 \times 1 \times 5$) |
| **RSK-19** | Commercial | CapEx budget overrun (> 20%) during turnkey equipment procurement | 6 | 5 | 3 | **90** | Fixed-price turnkey equipment contracts with liquidated damages; 10% contingency reserve | **30** ($6 \times 2 \times 2.5$) |
| **RSK-20** | Commercial | Delayed farmer or consumer adoption of conditioned dal | 7 | 4 | 5 | **140** | Blind taste-test marketing campaigns; institutional catering tie-ins (Akshaya Patra, IRCTC) | **42** ($7 \times 2 \times 3$) |

---

## 3. High-Priority Risk Mitigation Deep Dives (Pre-Empted Prior to Pilot)

### Deep Dive 1: RSK-11 — Residual Aftertaste Elimination (Initial RPN = 200)
- **Root Cause:** Surface retention of sodium citrate or unwashed polyphosphates crystallizing on the cotyledon during evaporation, leaving a salty, metallic, or astringent aftertaste on the tongue.
- **Engineered Control:**
  1. A high-efficiency counter-current spray wash ($0.50\text{ L/kg}$) stripping surface boundary-layer solutes in under 45 seconds.
  2. Inline conductivity verification ($< 120\text{ }\mu\text{S/cm}$ drain threshold).
  3. Strict ISO 4120 3-AFC panel testing with 30 panellists enforcing statistical indistinguishability ($p > 0.05$) before scaling to pilot batches.
- **Post-Mitigation RPN:** **40** (Low Risk).

### Deep Dive 2: RSK-01 — Regional Feedstock Hardness Variation (Initial RPN = 192)
- **Root Cause:** African import consignments vary widely in storage age (6 months to 3 years) and middle lamella calcium-magnesium pectate content ($15–48\text{ meq/kg}$). A single rigid soaking time will under-treat severely aged dal or over-hydrate younger dal.
- **Engineered Control:**
  1. Standardized 48-Hour Feedstock Intake Titration determining divalent cation cross-linking density.
  2. Automated PLC residence adjustment: The continuous steep auger is driven by a variable frequency drive (VFD) that adjusts residence time from 18 minutes (mild HTC) to 28 minutes (severe HTC), maintaining uniform 2-whistle tenderization ($F_{\text{WB}} \le 18.0\text{ N}$).
- **Post-Mitigation RPN:** **48** (Low Risk).

### Deep Dive 3: RSK-06 — Cotyledon Checking & Milling Breakage (Initial RPN = 168)
- **Root Cause:** Transient moisture gradients during rapid convective drying create tangential tensile hoop stresses exceeding the cotyledon parenchymal tensile strength ($2.40\text{ MPa}$), inducing longitudinal fissures and broken splits.
- **Engineered Control:**
  1. Two-Stage Fluid Bed Drying with an unheated, humidified intermediate tempering chamber ($45^\circ\text{C}$ for 20 minutes).
  2. Numerical modeling proves tempering relaxes peak tensile stress from $2.10\text{ MPa}$ to $0.40\text{ MPa}$, holding checking below $2.0\%$ and broken split generation below $1.5\%$.
- **Post-Mitigation RPN:** **32** (Low Risk).

---

### Associated Documentation

- Physics & Chemical Engineering Foundations: [02_PHYSICS_AND_CHEMICAL_ENGINEERING_SOLUTION.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/02_PHYSICS_AND_CHEMICAL_ENGINEERING_SOLUTION.md)
- Turnkey Equipment Schedule: [04_EQUIPMENT_SPECIFICATIONS_AND_PID_SCHEDULE.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/04_EQUIPMENT_SPECIFICATIONS_AND_PID_SCHEDULE.md)
- Five-Phase Scale-Up Roadmap: [05_FIVE_PHASE_SCALEUP_ROADMAP_AND_GATE_CRITERIA.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/05_FIVE_PHASE_SCALEUP_ROADMAP_AND_GATE_CRITERIA.md)
- Regulatory & Food Safety Dossier: [07_REGULATORY_COMPLIANCE_AND_FOOD_SAFETY_DOSSIER.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/07_REGULATORY_COMPLIANCE_AND_FOOD_SAFETY_DOSSIER.md)
- Customer Discovery & Pilot Contracts: [08_CUSTOMER_DISCOVERY_MILLER_OFFER_AND_CONTRACTS.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/08_CUSTOMER_DISCOVERY_MILLER_OFFER_AND_CONTRACTS.md)
