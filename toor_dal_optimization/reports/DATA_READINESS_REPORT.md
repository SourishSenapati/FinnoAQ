# Harakutir Toor Dal Diagnostic R&D Study — Phase 1
## Data Readiness & Ingestion Audit Report

**Report Date:** 15 October 2026  
**System Status:** `DATA_READINESS_ONLY`  
**Real Data Found:** `ABSENT`  
**Empirical Root-Cause Analysis Gate:** `BLOCKED_BY_MISSING_DATA`  

---

### 1. Executive Summary & Scientific Integrity Statement
In strict adherence to **Section 1 of the Harakutir Autonomous R&D Master Prompt**:
- **Zero Fabrication Rule:** No randomized, synthetic, or hand-authored values have been imported into the real-data namespace.
- **Current Observation:** The project workspace contains the contract scope document (`Phase1_Scope_of_Work_Toor_Dal.docx`) and technical proposals, but **no raw laboratory analytical assay files** (CSV, XLSX, or instrument output) have been received from external testing laboratories.
- **Gating Decision:** Empirical root-cause diagnosis is formally marked as **`BLOCKED_BY_MISSING_DATA`**. All software pipelines, schemas, GPU inverse solvers, Bayesian OED modules, checkpoint managers, and test suites are 100% verified using isolated synthetic fixtures under `data/synthetic/`.
- **Integrity Guarantee:** Synthetic test fixtures are watermarked and prohibited by automated tests from leaking into real reports.

---

### 2. Workspace Ingestion Scan Results
- **Target Ingestion Directory:** `data/raw/`
- **Raw Data Files Detected:** `0`
- **Files List:** None (Directory currently empty)

---

### 3. SOW Assay Module Readiness Matrix

| SOW Section | Assay Module | Priority | Real Data Status | Readiness State |
|---|---|---|---|---|
| §5 | Physical Characterization (Dimensions, 1000-grain wt, density, hardness) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §6 | Proximate Composition (Moisture, Protein, Fat, Fibre, Ash, Starch) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §7 | Starch & Gelatinization (DSC, RVA pasting parameters) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §8 | Hydration Kinetics (0-480 min soaking, WAI, swelling) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §9 | Seed-Coat & Cotyledon Microscopy (Thickness, SEM morphology) | High Priority | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §10 | Pectin & Cell-Wall Fractions (WSP, CSP, DE, Ca/Mg association) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §11 | Mineral & Phytate Profile (Ca, Mg, Fe, P, Phytate, Molar ratios) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §12 | Texture Profile Analysis (Raw, Hydrated, Cooked firmness & hard-core) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |
| §13-15 | Standardized Cooking Trials (Tests A, B, C; endpoint time, cooking loss) | Mandatory | Absent in `data/raw/` | BLOCKED_BY_MISSING_DATA |

---

### 4. Required Ingestion Actions for Client / Partner Laboratory
When physical laboratory test results become available from candidate partners (Eureka Analytical, Mitra S.K., CSIR-CGCRI, or IIT Kharagpur):
1. Place CSV or XLSX measurement files into `data/raw/` with unique lot identifiers (`TZ_LOT_01`, `IND_LOT_01`, etc.).
2. Execute the ingestion workflow:
   ```powershell
   ./run.ps1 -Mode Ingest
   ```
   or
   ```powershell
   python scripts/run_supervisor.py --ingest
   ```
3. The automated validator will:
   - Compute and log SHA-256 hashes in `state/provenance_registry.json`.
   - Validate against Pydantic schemas in `src/harakutir/schemas.py`.
   - Flag outliers, duplicate records, missing entries, and unit discrepancies.
   - Advance the system status to `EMPIRICAL_ANALYSIS_ACTIVE`.

---

### 5. Architectural Readiness Summary
- **Pydantic Schemas:** Fully defined across all 10 assay domains (`src/harakutir/schemas.py`).
- **Parameter Registry:** 78 individual parameters meticulously mapped with analytical standards (`reports/COMPLETE_PARAMETER_REGISTRY.md`).
- **Provenance System:** SHA-256 tracking active (`src/harakutir/provenance.py`).
- **Synthetic Isolation Gate:** 100% active, preventing test data leakage (`src/harakutir/synthetic.py`).
