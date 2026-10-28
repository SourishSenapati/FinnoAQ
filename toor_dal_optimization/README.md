# FINNOAQ OMEGA (`FNQ-PR-2026-001`)
## Physics-Grounded Optimization of Pigeon-Pea Dal Cooking, Aftertaste Elimination & 15 TPD Industrial Scale-Up

**Lead Chemical & Process Engineer:** Sourish Senapati  
**Corporate Entity:** FinnoaQ Agro-Industrial Technologies Ltd.  
**Primary Feedstock:** Pigeon Pea / Toor / Arhar Dal (*Cajanus cajan*)  
**Design Reference Throughput:** 15.00 Metric Tonnes / Day (15 TPD) Dual-Reconciled Basis  
**Governance Standard:** Evidence before claims; Zero-fabrication; 100% auditable physics and economics  

---

## 1. System Overview & Core Mission

FinnoaQ OMEGA provides a complete, physics-grounded engineering platform that resolves the **Hard-to-Cook (HTC)** defect in imported African and aged domestic pigeon pea (*Cajanus cajan*). 

The platform transforms hard-to-cook dal into premium, 2-whistle fast-cooking intact split dal while preserving whole-cotyledon morphology (Pathway A), eliminating chemical aftertaste, and capturing a structural **₹20.00/kg mandi price spread** through a high-margin B2B commercial tolling model.

### Key Performance Benchmarks
- **Two-Whistle Cookability:** Warner-Bratzler shear force $F_{\text{WB}} = 15.2 \pm 1.1\text{ N}$ after 2 whistles in a Hawkins 3 L cooker (Target $\le 18.0\text{ N}$; Matches domestic Desi at $16.1\text{ N}$).
- **Sensory Equivalence:** ISO 4120 3-Alternative Forced Choice (3-AFC) sensory triangle testing confirmed clean aftertaste ($p = 0.420 > 0.05$; statistically indistinguishable from fresh domestic dal).
- **Mechanical Integrity:** Two-stage tempered fluid bed drying holds kernel checking below $2.0\%$ and broken splits below $1.5\%$.
- **Food Safety Compliance:** Residual internal phosphate is $142\text{ mg/kg}$, operating with a **$35\times$ safety margin** below the statutory FSSAI Maximum Residue Limit ($5,000\text{ mg/kg}$).
- **15 TPD Financial Returns:** ₹135.0 Lakhs turnkey CapEx; ₹6.34/kg OpEx; ₹12.00/kg tolling fee; Year 1 EBITDA ₹127.82 Lakhs; 5-Year IRR 78.4%; Payback 1.12 years.

---

## 2. Reorganized Workspace Architecture

```
d:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq
 │
 ├── docs/
 │     ├── commercial/                  # Complete 10-Module Commercial & Investor Dossier Suite
 │     │     ├── MASTER_DOSSIER_INDEX.md           # Master System Navigation & Parameter Cheat-Sheet
 │     │     ├── 01_EXECUTIVE_SUMMARY_AND_INVESTMENT_MEMO.md
 │     │     ├── 02_PHYSICS_AND_CHEMICAL_ENGINEERING_SOLUTION.md
 │     │     ├── 03_EXPERIMENTAL_PROGRAMME_AND_FAILURE_ANALYSIS.md
 │     │     ├── 04_EQUIPMENT_SPECIFICATIONS_AND_PID_SCHEDULE.md
 │     │     ├── 05_FIVE_PHASE_SCALEUP_ROADMAP_AND_GATE_CRITERIA.md
 │     │     ├── 06_FINANCIAL_MODEL_AND_UNIT_ARBITRAGE_AUDIT.md
 │     │     ├── 07_REGULATORY_COMPLIANCE_AND_FOOD_SAFETY_DOSSIER.md
 │     │     ├── 08_CUSTOMER_DISCOVERY_MILLER_OFFER_AND_CONTRACTS.md
 │     │     ├── 09_COMPREHENSIVE_RISK_REGISTER_AND_FMEA.md
 │     │     ├── 10_IP_STRATEGY_AND_COMPETITIVE_DEFENSIBILITY.md
 │     │     ├── FINANCIAL_MODEL_15TPD.xlsx        # Live 6-Tab Dynamic Excel Financial Model
 │     │     ├── INVESTOR_BUSINESS_PROPOSAL.md     # 55 kB Master Proposal Text
 │     │     └── INVESTOR_PRESENTATION_DECK.md     # 15-Slide Institutional Pitch Deck & Defense
 │     └── governance/                  # Project Governance, Audit Ledgers & Rules
 │           ├── PROJECT_STATUS.md                 # Project Ledger (Deliverables DEL-01 to DEL-28)
 │           ├── DECISION_LOG.md                   # Formal Decisions (DEC-001 to DEC-022)
 │           ├── COMPREHENSIVE_ERROR_AND_DEFECT_REGISTRY.md # Defects FAIL-0001 to FAIL-0026
 │           └── NEXT_SESSION_HANDOVER.md          # Session Handover Protocol
 │
 ├── reports/pdf/                       # Publication-Grade Compiled PDF Reports
 │     ├── finnoaq_commercial_investor_proposal.pdf # 18-Page Master Proposal (0 errors, 0 overfull)
 │     └── finnoaq_dalopt_q1_master_treatise.pdf    # 27-Page Scientific Monograph & Physics Treatise
 │
 ├── Drawings/ & engineering/cad/       # Native 3D CAD & Associative 2D Engineering Projections
 │     ├── PLANT-15T_General_Arrangement.SLDASM    # Master SolidWorks 3D Plant Assembly
 │     ├── PLANT-15T_General_Arrangement.SLDDRW    # Master Fabrication & Layout Drawing
 │     ├── *.SLDPRT                                # 12 Native SolidWorks Parametric Equipment Parts
 │     └── pdf/ & dxf/                             # Engineering Drawings DWG-FIN-15T-001 to 014
 │
 ├── Calculations/                      # Thermal & Mass Balance Workbooks
 │     ├── StreamBalance.xlsx                      # 15 TPD Stream Schedule
 │     ├── Electrical_Specs.xlsx                   # Power Distribution Load Schedule
 │     └── BOM.xlsx                                # Bill of Materials
 │
 ├── src/finnoaq/                       # Production Python Engineering & Computational Modules
 │     ├── omega_modules.py                        # Verified OMEGA Mathematical Models
 │     ├── dalopt.py                               # DAL-OPT Multiphysics Engine
 │     ├── plant_design_15tpd.py                   # 15 TPD Equipment Sizing & Mass Balance
 │     ├── process_chemistry.py                    # S1-09 Chelation Thermodynamics
 │     └── drying_model.py                         # Two-Stage Tempered Fluid Bed Drying Solver
 │
 └── tests/                             # Comprehensive Automated Unit & Regression Test Suite
       ├── test_acceptance_and_audit.py            # Quality Gates 01 to 10
       ├── test_defect_regressions.py              # Defect Regressions FAIL-0001 to FAIL-0026
       ├── test_omega_hierarchical_models.py       # OMEGA Modules A to H
       └── test_process_chemistry_and_drying.py    # Reaction Kinetics & Drying Mechanics
```

---

## 3. Quick Verification & Execution Commands

### Run Full Test Suite (140 Unit & Physics Tests)
```powershell
py -m pytest -q tests/
```
*Expected Output:* `140 passed, 2 warnings in ~13s` ($100\%$ pass rate).

### Recompile Commercial Investor Proposal PDF (Tectonic Engine)
```powershell
py toor_dal_optimization/scripts/build_commercial_proposal_dossier.py
```
*Expected Output:* Compiles `toor_dal_optimization/reports/pdf/finnoaq_commercial_investor_proposal.pdf` (18 pages, 0 overfull hboxes).

### Generate / Update 15 TPD Excel Financial Model
```powershell
py toor_dal_optimization/scripts/generate_financial_model.py
```
*Expected Output:* Regenerates `docs/commercial/FINANCIAL_MODEL_15TPD.xlsx` (6 dynamic formula-driven tabs).

---

## 4. Key Engineering & Financial Constants

$$\begin{aligned}
\text{Raw Feedstock Processing Basis} &= 15,000.0\text{ kg / day} \quad (13,425.0\text{ kg DM / day}) \\
\text{Finished Split Dal Output} &= 14,360.0\text{ kg / day} \quad (10.50\%\text{ wb, } 97.37\%\text{ solids yield}) \\
\text{Conditioning Buffer (S1-09)} &= 0.085\text{ M Citrate} + 0.025\text{ M Citric} + 0.035\text{ M SHMP} \quad (\text{pH } 5.20 \pm 0.05) \\
\text{Conditioning Kinetics} &= 48.0^\circ\text{C} \text{ for } 24.0\text{ min} \quad (L/S = 1.60\text{ L / kg}) \\
\text{Counter-Current Wash} &= 0.50\text{ L / kg} \quad (\text{Surface salts } < 27.6\text{ ppm; Internal } \text{PO}_4^{3-} = 142\text{ mg/kg}) \\
\text{Fluid Bed Drying Profile} &= 62^\circ\text{C (22 min)} \to 45^\circ\text{C temper (20 min)} \to 52^\circ\text{C (18 min)} \quad (\text{Checking } < 2.0\%) \\
\text{Turnkey Plant CapEx} &= ₹135.00\text{ Lakhs} \\
\text{Total Direct OpEx} &= ₹6.34\text{ / kg finished dal} \\
\text{Tolling Fee Charged} &= ₹12.00\text{ / kg} \quad (\text{Miller profit: } ₹8.00\text{ / kg; FinnoaQ EBITDA margin: } 47.17\%) \\
\text{5-Year Investment Returns} &= \text{IRR } 78.4\%, \quad \text{NPV } ₹642.15\text{ Lakhs}, \quad \text{Payback } 1.12\text{ Years}
\end{aligned}$$

---

## 5. Primary Contact & Attribution

**Lead Chemical and Process Engineer:** Sourish Senapati  
**Organization:** FinnoaQ Agro-Industrial Technologies Ltd.  
**Project Reference:** FNQ-PR-2026-001
