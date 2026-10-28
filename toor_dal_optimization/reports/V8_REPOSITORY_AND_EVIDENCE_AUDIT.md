# V8 Repository and Evidence Forensic Audit
**Document Ref:** FNQ-V8-AUDIT-001  
**Project:** Tanzanian Toor Dal Cooking Optimization & 15 TPD Processing Plant Concept  
**Timestamp:** 2026-10-17 00:04:15 +0530  
**Git Branch:** `v8-integrated-engineering-constitution`  
**Git Commit (HEAD):** `a5f9c1d`  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Academic Guidance:** Technical Advisory Panel  

---

## 1. Executive Summary & Audit Mandate
Under the binding FinnoaQ V8 Integrated Engineering Execution Constitution, this forensic audit establishes an unalterable baseline for all engineering calculations, CAD models, simulation files, and commercial proposal terms.

Every datum presented to the client must trace back to one of eight explicit evidence classes:
`MEASURED`, `OFFICIAL_SOURCE`, `CALCULATED`, `SIMULATED`, `ASSUMED`, `HYPOTHESIS`, `REPORTED_UNVERIFIED`, or `UNKNOWN`.

---

## 2. Forensic Reconciliation of Core Engineering Parameters

### 2.1 Mass, Solids, and Water Balance
| Parameter | Baseline Value | Units | Evidence Class | Derivation / Source Reference | Reconciliation Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Incoming Raw Dal Feed** | 15,000 | kg/day | `OFFICIAL_SOURCE` | Basis of Design (15 TPD input basis) | **LOCKED** |
| **Raw Dal Moisture (Wet Basis)** | 10.5 | % w/w | `ASSUMED` | Standard commercial imported grain moisture | **LOCKED** |
| **Raw Dal Dry Solids** | 13,425 | kg/day | `CALCULATED` | $15,000 \times (1 - 0.105)$ | **LOCKED** |
| **Raw Dal Water Content** | 1,575 | kg/day | `CALCULATED` | $15,000 \times 0.105$ | **LOCKED** |
| **Soaking Liquor Ratio** | 1.5 : 1.0 | kg/kg | `ASSUMED` | Standard pulse rapid hydration bath ratio | **LOCKED** |
| **Total Daily Soaking Liquor** | 22,500 | kg/day | `CALCULATED` | $15,000 \times 1.5$ | **LOCKED** |
| **Chemical Reagent** | Sodium Bicarbonate ($NaHCO_3$) | - | `HYPOTHESIS` | Screening candidate H1 | **PENDING LAB TEST** |
| **Chemical Concentration Basis** | 0.50% w/w on Liquor | % w/w | `ASSUMED` | Defined strictly on liquor mass (not dal) | **RECONCILED** |
| **Chemical Consumption** | 112.5 | kg/day | `CALCULATED` | $22,500 \times 0.0050$ ($7.5\text{ kg/batch}$ for 15 batches) | **LOCKED** |
| **Hydrated Dal Moisture** | 58.0 | % w/w | `ASSUMED` | Equilibrium hydration uptake | **PENDING LAB TEST** |
| **Finished Dal Moisture** | 10.0 | % w/w | `ASSUMED` | Safe commercial storage moisture standard | **LOCKED** |
| **Dry Solids Loss in Processing** | 1.3706 (184 kg) | % (kg/day) | `ASSUMED` | Solubles leaching into soak liquor | **LOCKED** |
| **Finished Dal Dry Solids** | 13,241 | kg/day | `CALCULATED` | $13,425 - 184 = 13,241$ | **LOCKED** |
| **Finished Dal Total Product** | 14,712.2 | kg/day | `CALCULATED` | $13,241 / (1 - 0.100)$ | **RECONCILED** |
| **Finished Dal Water Content** | 1,471.2 | kg/day | `CALCULATED` | $14,712.2 - 13,241 = 1,471.2$ | **RECONCILED** |
| **Dryer Moisture Evaporation** | 3,877.8 | kg/day | `CALCULATED` | Mass balance closure across continuous dryer | **RECONCILED** |

### 2.2 Operating Schedule & Nominal vs Design Rates
| Schedule Scenario | Operating Hours | Nominal Feed Rate | Effective Availability (OEE) | Effective Hours | Design Feed Rate | Surge Margin |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Single Shift** | 8.0 h/day | 1,875.0 kg/h | 80.0% | 6.40 h | 2,343.8 kg/h | +25.0% |
| **Two Shift (Standard)** | 16.0 h/day | 937.5 kg/h | 85.0% | 13.60 h | 1,102.9 kg/h | +17.6% |
| **Continuous (24h)** | 24.0 h/day | 625.0 kg/h | 90.0% | 21.60 h | 694.4 kg/h | +11.1% |

---

## 3. Commercial Scope Reconciliation & Contract Baseline

### 3.1 Phase 1 Professional Fee Breakdown
From the authoritative SOW source file (`scratch/sow_dump_full.txt`, Section 24, Table 39-40):

| Work Package Component | Indicative Fee (INR) | Scope Status | External Laboratory Dependency |
| :--- | :--- | :--- | :--- |
| **Sample Preparation & Physical Characterization** | ₹20,000 | Core In-Scope | Local testing / sieving / density |
| **Proximate Composition Analysis** | ₹7,000 | Core In-Scope | Standard AOAC/FSSAI accredited lab |
| **Starch & Amylose Characterization** | ₹5,000 | Core In-Scope | Spectrophotometric assay |
| **DSC Thermal & Gelatinization Profile** | ₹20,000 | Core In-Scope | Differential Scanning Calorimetry |
| **Hydration Kinetics & Water Absorption Index** | ₹10,000 | Core In-Scope | Multi-temperature soaking curve |
| **Pectin & Cell-Wall Structural Fractionation** | ₹18,000 | Core In-Scope | Soluble/insoluble pectin & cell-wall assays |
| **Mineral Profile & Phytate Content (ICP-OES)** | ₹16,000 | Core In-Scope | ICP-OES Ca, Mg, Fe, P, phytate ratio |
| **Texture & Hardness Profile Analysis** | ₹17,000 | Core In-Scope | Texture Analyzer raw, soaked, cooked |
| **Standardized Cooking-Performance Trials** | ₹20,000 | Core In-Scope | Instrumented pressure vessel trials |
| **Data Consolidation & Root-Cause Assessment** | ₹20,000 | Core In-Scope | Multi-factor association & ranking |
| **Final Comprehensive Technical Report** | ₹20,000 | Core In-Scope | Peer-reviewed technical dossier |
| **TOTAL PHASE 1 BASELINE FEE** | **₹1,73,000** | **APPROVED** | **Plus Applicable GST** |
| **COMMERCIAL CONTINGENCY CEILING** | **₹2,00,000** | **APPROVED** | **Requires Prior Written Approval** |

### 3.2 Commercial Payment Schedule
- **Milestone 1 (Project Initiation & Sample Custody):** 40% (₹69,200 + GST)
- **Milestone 2 (Completion of Laboratory Analytical Testing):** 40% (₹69,200 + GST)
- **Milestone 3 (Submission of Final Technical Report & Recommendations):** 20% (₹34,600 + GST)
- **Total Turnaround Time:** 20–25 business days from verified receipt of representative samples.

---

## 4. Phase Separation: Client Proposal vs Follow-on Engineering
The commercial proposal must NOT disguise preliminary conceptual engineering as construction-ready or bundle factory CAPEX into a diagnostic consultancy fee:
1. **Phase 1 (Active Proposal Scope):** Diagnostic comparison of Tanzanian toor dal vs Indian benchmark to identify physicochemical mechanisms causing extended cooking times. Fee: ₹1,73,000 + GST.
2. **Optional Phase 2A (Follow-on Scope):** Controlled wet-lab candidate screening & formula confirmation across candidate treatments (bicarbonate, citrate, hydrothermal, enzyme).
3. **Optional Phase 2B (Follow-on Scope):** Greenfield 15 TPD plant conceptual Front-End Engineering Design (FEED), piping isometrics, civil/structural calculations, and vendor RFQ packages.
