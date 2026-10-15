# Verified Action and Evidence Audit Report

> [!IMPORTANT]
> **Audit Classification:** Evidence-Based Independent Action Dossier  
> **Repository Commit:** `580f627` (Branch: `no-lie-corrective-audit-20261015`)  
> **Status Taxonomy Applied:** `VERIFIED`, `CALCULATED`, `ASSUMED`, `HYPOTHESIS`, `NOT VERIFIED`  
> **Mandatory Hold Point:** Stopped at **Gate G-A**. No treatment or factory is declared validated.

---

## 1. Six-Column Evidence & Verification Action Ledger

| Claim | Stated Evidence | Verification Performed | Result & Category | Uncertainty | Next Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Test Suite Reproducibility** | 81 tests passing with exit code 0 | Synchronous `pytest -v` run executed on host Python 3.13 | **`VERIFIED`**<br>(81 passed, 0 failed in 13.63s, Exit code: 0) | Software logic only; does not validate physical biology | Keep tests in CI/CD regression suite |
| **Moisture Contradiction Resolution** | Historical $14,895.3\text{ kg/day}$ dal stream was $11.106\%$ wb, not $10.0\%$ | Re-solved mass balance with dry solids $= 13,241\text{ kg}$ at exact $10.0\%$ wb $= 14,712.22\text{ kg/day}$ | **`CALCULATED`**<br>Evaporation $= 3,877.78\text{ kg H2O/day}$ ($242.36\text{ kg/h}$ nom / $285.13\text{ kg/h}$ des) | 0.00% math error; depends on upstream hydration uptake | Re-measure true water uptake on physical dal lot |
| **Chemical Formulation Basis** | Two distinct dosage figures: $112.5\text{ kg/day}$ vs $75.0\text{ kg/day}$ | Reconciled equation basis: 0.50% in soak liquor ($112.5\text{ kg}$) vs 0.50% on raw dal ($75.0\text{ kg}$) | **`CALCULATED`**<br>Basis A (₹12.49L/yr) vs Basis B (₹8.33L/yr) formally separated | ₹4.16L/yr OpEx variance depending on route chosen | Screen 0.25% vs 0.50% in laboratory trials |
| **SolidWorks 2025 Availability** | Installed SolidWorks 2025 SP01.2 with COM automation | Discovered path, dispatched `SldWorks.Application`, created parametric part, measured volume | **`VERIFIED`**<br>`API_SMOKE_TEST_PASSED`<br>(SLDPRT 43KB, STEP AP214 11.9KB, volume error 0.00%) | Verified on host desktop session | Use for parametric conceptual equipment envelopes |
| **AutoCAD 2025 1:1 Scale Capability** | Headless batch execution via `accoreconsole.exe` | Executed `.scr` script, generated DXF with `$INSUNITS = 4` at 1:1 true mm scale | **`VERIFIED`**<br>`API_SMOKE_TEST_PASSED`<br>(DXF 121KB, 4 entities, return code 0) | Native AutoCAD verified; Plant 3D SDK requires project setup | Generate 1:1 conceptual plant layouts |
| **Aspen Plus V14 Process Simulation** | Aspen Plus V14 available for process flowsheet modeling | Dispatched `Apwn.Document` COM server; checked background PID and process suitability | **`NOT VERIFIED`**<br>`APPLICATION_LAUNCH_CONFIRMED`<br>(COM starts, but flowsheet NOT run) | Full init requires active license; Aspen lacks pulse grain biology | Use only as secondary rigor tool for steam/psychrometrics |
| **Legacy 3D STEP Model Repair** | Historical STEP models were 27-line empty stubs | Automated SolidWorks 2025 to generate watertight B-Rep solids for TK-101, DR-101, SK-100, AG-101 | **`VERIFIED`**<br>Re-imported STEP files; verified B-Rep solids (11KB–16KB, 192–254 lines) | Conceptual solid envelopes; not shop fabrication drawings | Re-run dimensional checks after physical kinetics locked |
| **1:1 Greenfield Plot Plan** | Plant layout must be drawn at 1:1 true millimeters | Generated `DWG-FIN-15T-001.dxf` at $52,000 \times 24,000\text{ mm}$ with `$INSUNITS = 4` | **`VERIFIED`**<br>(26,136 bytes, 5 distinct functional layers) | Assumed $52\text{ m} \times 24\text{ m}$ site footprint until survey provided | Obtain surveyed site boundary coordinates |
| **Target Lot `TZ-2026-IMP-001` Provenance** | Target Tanzanian split pigeon pea consignment identifier | Grepped codebase and checked procurement records | **`NOT VERIFIED`**<br>(Identified as internal synthetic placeholder string) | No commercial bill of lading, invoice, or cert exists | **Request genuine traceable commercial lot ID from user** |
| **Bicarbonate Cooking Reduction** | Candidate C4 reduces cooking time to $\le 15$ min | No wet-lab trial on target lot has been conducted | **`HYPOTHESIS`**<br>(Computational hypothesis awaiting empirical proof) | Cooking time on target lot completely unmeasured | Execute 16-batch physical trial under human authorization |
| **15 MT/Day Factory Readiness** | Turnkey processing plant is ready for construction | Equipment sizes depend on unmeasured kinetics | **`ASSUMED`**<br>(Conceptual FEED package under Low/Base/High bounds) | Plant sizing provisional ($\pm 25\%$ envelope variance) | Hold detailed engineering until Gate G-A is cleared |

---

## 2. Summary of Immediate Status & Required Human Action

1. **Software & Toolchain:** SOLIDWORKS 2025 and AutoCAD 2025 are verified and operational via Python COM automation. Legacy 27-line STEP files have been replaced with genuine B-Rep solids in `engineering/cad/step/`.
2. **Conceptual FEED:** Parallel execution dossier published in [`reports/CONCEPTUAL_FEED_WORK_PLAN_AND_SCENARIOS.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/CONCEPTUAL_FEED_WORK_PLAN_AND_SCENARIOS.md) with Low, Base, and High process sensitivity envelopes.
3. **Lot Traceability:** `TZ-2026-IMP-001` is marked as an unverified internal placeholder. The real commercial lot number and import documentation are requested.
4. **Mandatory Hold Point:** The physical screening protocol remains frozen at **Gate G-A**. No laboratory trials or experimental results will be recorded until the human lead reviews and approves the protocol.
