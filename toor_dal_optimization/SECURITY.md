# SECURITY.md

## Security & Scientific Integrity Architecture
**System:** FinnoaQ Autonomous Closed-Loop Pulse Engineering Platform  
**Owner:** FINNOAQ Security & Scientific Integrity Team  
**Standard:** Ocean Boiling Protocol v3.0 | Zero-Trust Local Offline Architecture  
**Audit Status:** PASSED (0 Critical, 0 High Defects — `reports/RED_TEAM_AUDIT_REPORT.md`)  

---

## 1. Threat Model & Security Posture

The platform assumes a hostile execution environment where improper data flow could compromise scientific integrity, commercial food safety, intellectual property, or production equipment.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                STRIDE THREAT ASSESSMENT                                 │
├───────────────────┬──────────────────────────────────────────┬──────────────────────────┤
│ Threat Category   │ Primary Attack / Failure Vector          │ Implemented Mitigation   │
├───────────────────┼──────────────────────────────────────────┼──────────────────────────┤
│ **Spoofing**      │ Synthetic or unverified simulation data  │ Gate G4 Ethical Wall:    │
│                   │ masquerading as real wet-lab assays.     │ Cryptographic labeling & │
│                   │                                          │ `DATA_READINESS_ONLY`    │
├───────────────────┼──────────────────────────────────────────┼──────────────────────────┤
│ **Tampering**     │ Silent modification of source SOWs,      │ SHA-256 provenance chain │
│                   │ laboratory assay CSVs, or checkpoints.   │ in `provenance.py` and   │
│                   │                                          │ `state/journal.db`       │
├───────────────────┼──────────────────────────────────────────┼──────────────────────────┤
│ **Repudiation**   │ Disputed experimental parameters or      │ Immutable append-only    │
│                   │ undocumented changes to pilot recipes.   │ SQLite WAL transaction   │
│                   │                                          │ journal for every action │
├───────────────────┼──────────────────────────────────────────┼──────────────────────────┤
│ **Information**   │ Leakage of proprietary trade secrets,    │ 100% offline local model │
│ **Disclosure**    │ commercial margins, or client datasets.  │ execution; zero cloud    │
│                   │                                          │ egress; zero API keys    │
├───────────────────┼──────────────────────────────────────────┼──────────────────────────┤
│ **Denial of**     │ Out-of-memory GPU crash (CUDA OOM),      │ Strict VRAM budget       │
│ **Service**       │ infinite simulation loops, file locks.   │ (<3.8 GB), time-caps,    │
│                   │                                          │ and graceful CPU fallback│
├───────────────────┼──────────────────────────────────────────┼──────────────────────────┤
│ **Elevation of**  │ Shell command injection via laboratory   │ Pydantic v2 schema       │
│ **Privilege**     │ file names or malicious path traversal.  │ bounds, normalized paths,│
│                   │                                          │ and strict type casting  │
└───────────────────┴──────────────────────────────────────────┴──────────────────────────┘
```

---

## 2. Attack Vectors & Defensive Mitigations

### 2.1 Synthetic Data Leakage & Hallucination Prevention (Gate G4)
- **Vulnerability:** AI and computational engines frequently generate plausible-sounding synthetic data. If unverified synthetic results are ingested into commercial reports, FinnoaQ could make faulty procurement decisions (e.g. contracting 10,000 tonnes of pulse shipments based on simulated rather than measured softening).
- **Defense:**
  1. Strict segregation of data directories: `data/raw/` (exclusively for certified external lab CSV/XLSX files), `data/synthetic/` (for computational screening only), and `data/derived/` (for verified transformations).
  2. The statistical engine inspects file provenance; if `data/raw/` contains zero certified assay files, the pipeline automatically forces the entire system into `DATA_READINESS_ONLY / COMPUTATIONAL_FRAMEWORK_VERIFIED` mode.
  3. All empirical claims are marked as "Data Gated" and assigned to Category C (Potential Mechanisms) rather than Category A (Confirmed Differences).

### 2.2 Input Validation & Numerical Sanitization
- **Vulnerability:** Malformed laboratory CSVs with negative moisture contents, infinite densities, or non-numeric strings could cause division-by-zero or NaN gradient propagation in PyTorch.
- **Defense:**
  1. Every incoming parameter is strictly parsed through Pydantic v2 schemas (`src/finnoaq/schemas.py`).
  2. Physical boundary clamping: Moisture dry basis $\in [0.05, 1.50]$, Bulk density $\in [0.50, 1.20]\text{ g/mL}$, Gelatinization onset $T_o \in [40.0, 95.0]^\circ\text{C}$, Pectin degree of esterification $DE \in [10.0, 95.0]\%$.
  3. Out-of-bounds inputs raise immediate `ValidationError`, halting pipeline progression before tensor memory allocation.

### 2.3 Process Concurrency & State Tamper-Proofing
- **Vulnerability:** Concurrent execution of pipeline runs or crash interruptions causing partial writes to JSON state checkpoints.
- **Defense:**
  1. OS-level process exclusion using `msvcrt.locking` on Windows (`checkpoints/run.lock`). Duplicate processes exit immediately with exit code 1.
  2. Atomic checkpoint replacement: writes to temporary `.tmp` files on the same volume, then executes `os.replace()`, guaranteeing ACID file atomicity.
  3. SQLite WAL Journal (`state/journal.db`): records all gate evaluations and parameter hashes with microsecond timestamps and transaction isolation.

### 2.4 Supply-Chain & Credential Defense
- **Vulnerability:** Unintended leaks of AWS/GCP cloud credentials, API tokens, or proprietary connection strings.
- **Defense:**
  1. 100% Offline execution: The pipeline operates entirely locally on local workstation hardware (AMD Ryzen 9 + NVIDIA RTX 4050 GPU).
  2. Zero external cloud API calls: No dependency on third-party cloud LLMs or online SaaS endpoints during simulation.
  3. Automated credential scan: `test_gate_12_no_credentials` scans all workspace files via regex for AWS keys, private tokens, passwords, and private SSH certificates.

---

## 3. Red Team Security & Audit History

| Audit ID | Audit Date | Target Components | Findings | Resolution Status |
|----------|------------|-------------------|----------|-------------------|
| **AUD-2026-001** | 2026-09-18 | Initial Pipeline Scripts | 1 High (unbounded PINN iterations on CPU) | Fixed: added time budget and GPU auto-fallback. |
| **AUD-2026-002** | 2026-10-12 | SOW Requirements & Schema | 2 Medium (untyped dictionary access) | Fixed: replaced with Pydantic v2 schemas. |
| **AUD-2026-003** | 2026-10-13 | Provenance & Cryptographic Chain | 0 Critical, 0 High, 0 Medium | **PASSED** (`reports/RED_TEAM_AUDIT_REPORT.md`). |

---

## 4. Food Safety & Regulatory Security (HACCP CCPs)

Beyond software security, the pipeline enforces physical food safety compliance under FSSAI / Codex Alimentarius standards:
- **CCP-1 (Moisture & Water Activity):** Final tempered/dried grain moisture must strictly satisfy $M_w \le 12.0\%$ ($a_w \le 0.65$) to prevent *Aspergillus flavus* proliferation and aflatoxin formation during commercial warehousing.
- **CCP-2 (Thermal Enzyme Inactivation):** Catalytic infrared treatment must achieve core temperature $T_{\text{core}} \ge 78.0^\circ\text{C}$ to fully inactivate pulse lipoxygenase (LOX), arresting enzymatic rancidity and off-flavor synthesis during storage.

---
*Maintained under Ocean Boiling Protocol v3.0 by Finnoaq Autonomous Engineering.*
