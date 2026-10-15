# V4 BASELINE AND EXECUTION PLAN
**Document Type:** Baseline Audit & Dependency Execution Plan  
**Governing Standard:** V4 Master Directive — Professional Native Engineering, Offline-First, Evidence-Locked  
**Facility:** 15,000 kg/day Greenfield Imported Pigeon Pea (Toor Dal) Rapid-Cooking Pre-Treatment Plant  
**Workstation Host:** Windows AMD Ryzen 9 / RTX 4090 / 64 GB RAM  
**Active Work Branch:** `v4-native-feed-engineering`  
**Reference Backup Branch:** `backup-v4-pre-execution-20261015`  
**Base Commit Hash:** `fc7b9086e6b7804a97bf2ab913119c352fa83c6c`  
**Timestamp:** 2026-10-15T23:05:00+05:30  

---

## 1. Verified Software & Toolchain Inventory

Every application below has been tested on the live host with recorded exit codes and COM progid responses (stored at [`engineering/verification/v4/v4_toolchain_inventory.json`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/verification/v4/v4_toolchain_inventory.json)):

| Platform / Tool | Version / Revision | Launch / COM Status | Local Binary / Path | Smoke Test Result |
| :--- | :--- | :--- | :--- | :--- |
| **Python** | 3.13.7 (64-bit MSC v.1944) | Native CLI | `C:\Python313\python.exe` | **PASS** (100% Offline) |
| **SolidWorks** | SolidWorks 2025 SP01.2 (`Rev 33.1.2`) | `SldWorks.Application` COM | Registered in Windows ROT | **PASS** (Builds multi-feature B-Rep) |
| **AutoCAD** | AutoCAD 2025 (`25.0s LMS Tech`) | `AutoCAD.Application` COM + CLI | `C:\Program Files\Autodesk\AutoCAD 2025\accoreconsole.exe` | **PASS** (Scriptable via SCR/COM) |
| **Aspen Plus** | Aspen Plus V14.0 | `Apwn.Document` COM | Registered in Windows ROT | **PASS** (Instantiates flowsheet document) |
| **ezdxf** | Version 1.4.4 | Python Module | `C:\Python313\Lib\site-packages\ezdxf` | **PASS** (Native DXF R2018 vector engine) |
| **PyMuPDF (fitz)** | Version 1.27.2.2 | Python Module | `C:\Python313\Lib\site-packages\fitz` | **PASS** (PDF vector rendering & bounding-box QA) |
| **PyTorch** | Version 2.6.0+cu124 | Python Module | `C:\Python313\Lib\site-packages\torch` | **PASS** (Local GPU/CUDA 12.4 offline) |
| **PyTest** | Version 9.0.2 | Python CLI | `C:\Python313\Scripts\pytest.exe` | **PASS** (81 tests passing synchronously) |

---

## 2. Artifact Forensic Audit & Current Truth Table

Every project claim and artifact has been categorized into strictly verified engineering classes:

| Artifact / Work Area | Claim / Content | Tagged Class | Verified Reality | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Raw Material Lot** | "Tanzanian Dehulled Split Dal lot `TZ-2026-IMP-001`" | `UNKNOWN` / `HYPOTHESIS` | The lot number was a synthetic placeholder. Re-tagged as `PENDING_COMMERCIAL_LOT_ID`. No supplier CoA exists on disk. | **GATE G-A HOLD** |
| **Treatment Winner** | "0.75% NaHCO3 is the 5-sigma validated treatment" | `HYPOTHESIS` | **No physical wet-lab experiment has been conducted on this lot.** Only Peleg kinetic literature approximations exist. | **GATE G-A HOLD** |
| **Mass & Moisture Balance** | 15,000 kg/day feed, 10.0% moisture in / 10.0% out, 99.98% dry solids recovery | `CALCULATED` | Balance is mathematically closed and non-contradictory in [`data/stream_tables_15tpd.json`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/data/stream_tables_15tpd.json). | **VERIFIED** |
| **Chemical Dosing Bases** | $0.5\%\text{–}1.0\%$ dry grain basis ($75\text{–}150\text{ kg/day}$) vs $0.33\%\text{–}0.67\%$ bath concentration | `CALCULATED` | Explicitly separated in [`src/harakutir/plant_design_15tpd.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/src/harakutir/plant_design_15tpd.py). | **VERIFIED** |
| **3D CAD Solids (SolidWorks)** | TK-101 (3,719 STEP lines), DR-101 (4,194 lines), SK-100 (2,546 lines), AG-101 (1,697 lines) | `SIMULATED` / `CALCULATED` | Genuine ASME/GEA multi-feature B-Rep geometry generated via SolidWorks 2025 SP01.2 COM. Total 12,156 lines of STEP. | **VERIFIED CONCEPTUAL** |
| **2D PDF Drawing Package** | `HARAKUTIR_15TPD_ENGINEERING_DRAWING_PACKAGE_REV_V3.pdf` | `FAILED` | **REJECTED.** Generated using Python `matplotlib` textboxes with LaTeX parse bugs, table collisions, and zero CAD vector geometry. | **REJECTED / TO BE REBUILT** |
| **Native Aspen Model** | Aspen Plus V14 Triple-Effect Evaporator | `CALCULATED` / `SIMULATED` | Evaporator case converges for steam/water utility. Whole-plant 15 TPD dal treatment flowsheet remains to be assembled in Aspen. | **PARTIAL** |
| **Automated Test Suite** | 81 tests passing in 7.77 seconds | `VERIFIED` | Covers mass balance, Navier-Stokes, schedules, and registers. | **PASS** (Exit Code 0) |

---

## 3. Ordered Phased Execution Plan (V4 Directive)

```
[PHASE A: Baseline & Forensic Audit]  ◄── CURRENT (Complete)
      │
      ▼
[PHASE B: Native CAD Drawing System & 4 Reference Exemplars]
      ├── B1: Define A2/A1 Drawing Border, ISA-5.1 Symbols, Layer Standards, Text Hierarchy
      ├── B2: Exemplar 1 - Process Flow Diagram (PFD) + Legible Stream Table Sheet (AutoCAD/DXF)
      ├── B3: Exemplar 2 - Detailed P&ID with ISA-5.1 Valve/Instrument Tags (AutoCAD/DXF)
      ├── B4: Exemplar 3 - Greenfield Site Master Plot Plan 1:1 Scale ($INSUNITS=4) (AutoCAD/DXF)
      ├── B5: Exemplar 4 - Model-Derived Equipment GA (SolidWorks .SLDDRW / True Orthographic)
      └── B6: High-Res Raster Render & Visual/Automated Margin/Collision QA Loop
      │
      ▼
[PHASE C: Full Conceptual FEED Engineering Package]
      ├── C1: Complete Drawing Package (PFDs, P&IDs, Site Plan, GA Sheets, Electrical SLD, Hazard Map)
      ├── C2: Engineering Schedules (Line List, Valve Schedule, Instrument Index, Motor Load List)
      ├── C3: Process Sizing Calculations (Dryer psychrometrics, Soak tank sizing, Evaporator duty)
      ├── C4: Equipment Datasheets & Preliminary Mechanical Specifications
      └── C5: Capital (CAPEX) & Operating (OPEX) Cost Estimate with Explicit Scope & Uncertainty
      │
      ▼
[PHASE D: Native 3D Plant General Arrangement Assembly]
      ├── D1: Assemble SK-100, TK-101, AG-101, DR-101 into SolidWorks .SLDASM
      ├── D2: Model Structural Steel Skid Platform & Interconnecting Chutes / Transfer Piping
      └── D3: Export Validated Exchange STEP AP214 and Verify Bounding Box / Solid Topology
      │
      ▼
[PHASE E: Aspen Plus Process Simulation]
      ├── E1: Build 15 TPD Converged Flowsheet in Aspen Plus V14 (.bkp)
      └── E2: Compare Unit Operations & Utility Steam/Cooling with Independent Python Balances
      │
      ▼
[PHASE F: Anti-Slop Red-Team QA & Final Handover]
      ├── F1: Automated Margin, Font Size, Collision, and Title-Block Overlap Audits
      ├── F2: Visual Inspection of Rendered Sheets (Zero Matplotlib Textboxes Allowed)
      ├── F3: Update Evidence Ledger, Provenance Hashes, and Traceability Matrix
      └── F4: Document Gate G-A Hold Points & Human Review Directives
```
