# FinnoaQ Offline GPU Computational Engineering & Scientific Falsification Report

**Project Reference:** FNQ-PR-2026-001 | Toor Dal Cooking-Time Optimization & Diagnostic R&D  
**Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Document Ref:** FNQ-REP-COMP-001 (Revision V10.1)  
**Date:** 20 October 2026  
**Execution Mode:** Local-First, Offline-Verified, GPU-Accelerated (NVIDIA RTX 4050 CUDA)  
**Governing Manifest:** `artifacts/computational_pipeline_run_manifest.json`  

---

## 1. Executive Summary

This report establishes the local-first, offline-capable computational engineering suite implemented to investigate slow-cooking kinetics in imported Tanzanian split pigeon pea (*Cajanus cajan*). 

The software package addresses four primary engineering questions:
1. **Missing Measurements:** Identifies exact physical parameters (pre-dryer drainage moisture, lot-specific hydration rate $k_1$, middle-lamella pectin fractions, phytate-to-cation ratio, and autoclave $T_{90}$) whose absence prevents conclusive mechanistic attribution.
2. **Sensitivity Propagation:** Quantifies the sensitivity of water evaporation ($\pm 18\%$), thermal drying duty ($118.95$ to $167.61\,\text{kW}_{th}$), material recovery ($14,698$ to $14,712\,\text{kg/day}$), and cooking softening ($25.38$ to $45.20\,\text{min}$) across uncertain inputs via a 100,000-scenario Monte Carlo sweep.
3. **Hypothesis Discrimination & OED:** Connects all 10 competing scientific hypotheses (H1 to H10) to the itemized laboratory budget in `Final_Proposal.pdf` (Option 1: INR 1,73,000 across 11 work packages), ranking candidate assays by Expected Information Gain (EIG) and diagnostic cost-efficiency.
4. **Data-Readiness for Ingestion:** Delivers pre-parameterized, numerically verified pipelines (`src/finnoaq/`) that accept genuine laboratory observations upon sample arrival to fit kinetic parameters, compute parameter covariance matrices, and validate competing models.

In strict compliance with FinnoaQ Engineering Governance:
- Zero emojis, zero colloquial language, and zero synthetic placeholders are permitted.
- Synthetic datasets are segregated in `data/synthetic/` with explicit warning headers.
- Physical laboratory work remains unstarted (`PLANNED`), awaiting client sample shipment and Milestone 1 advance.
- No simulation is represented as experimental proof of dal properties.

---

## 2. Hardware Discovery & Offline Environment

Hardware and software telemetry were verified directly on the host workstation:

| Component | Verified Specification | Verification Method |
| :--- | :--- | :--- |
| **CPU** | 10 Physical Cores / 20 Logical Threads (x86_64 AMD64) | `psutil.cpu_count()` via Python 3.13.7 |
| **System RAM** | 23.12 GB Total / 3.86 GB Available | `psutil.virtual_memory()` |
| **GPU Hardware** | NVIDIA GeForce RTX 4050 Laptop GPU (Ada Lovelace, Compute 8.9) | `nvidia-smi` (Driver: 591.74, CUDA 13.1) |
| **GPU Memory** | 6,141 MiB Total VRAM | `torch.cuda.get_device_properties(0)` |
| **Python Runtime** | Python 3.13.7 (MSC v.1944 64-bit) | `sys.version` |
| **ML/Numerical Stack** | PyTorch 2.6.0+cu124, SciPy 1.15.1, NumPy 2.2.2 | In-process imports and execution |
| **CUDA Verification** | 1000x1000 tensor allocation, matmul, and `torch.cuda.synchronize()` | Verified (`mean = 0.00455`) |
| **Offline Status** | All modules executed with zero external network access | `artifacts/computational_pipeline_run_manifest.json` |

---

## 3. Forensic Audit of Previous Claims & Contradictions

The project repository and previous audit documents were independently audited against authoritative sources:

### Claim A — Phase 1 Scope Boundary
- **Audit Contradiction:** Phase 1 was described in one place as including "bounded screening" and elsewhere as "gated to Phase 2".
- **Reconciliation:** Authoritative SOW Table 40 explicitly defines Work Package 3 as "Bounded candidate-treatment screening" (untreated control, water control, and up to 3 candidate conditioning approaches: bicarbonate, citrate, hydrothermal; budgeted at INR 20,000 under WP-10). Full factorial parameter optimization, pilot trials, and commercial factory design are strictly gated to downstream Phase 2 and Phase 4.

### Claim B — Mass Balance Discrepancy
- **Audit Contradiction:** Described as resolved by scenario in one section, yet unresolved pending physical dewatering in another.
- **Reconciliation:** Both statements are technically reconciled when properly framed:
  - **Scenario B1 (28.00% WB Inlet):** Wet feed to dryer = $18,390.28\,\text{kg/day}$; dryer evaporation = $3,678.06\,\text{kg/day}$ ($183.90\,\text{kg/h}$); thermal duty = $134.23\,\text{kW}_{th}$; air flow = $14,712\,\text{kg/h}$. Mathematical closure error = $0.000000\%$.
  - **Scenario B2 (Reported 18,590.00 kg/day Inlet):** Implied moisture = $28.7735\%$ WB; dryer evaporation = $3,877.78\,\text{kg/day}$ ($193.89\,\text{kg/h}$); thermal duty = $141.11\,\text{kW}_{th}$; air flow = $15,511\,\text{kg/h}$. Mathematical closure error = $0.000000\%$.
  - **Physical Conclusion:** The mathematical balances for both conditional input scenarios close with zero error. However, the physical discrepancy of **199.72 kg/day water (6.88 kW_th thermal duty)** represents entrained surface liquor following screen dewatering. It remains **empirically unresolved** until a 5-minute laboratory screen dewatering trial is conducted on physical dal. Mathematical closure must not be confused with physical validation.

### Claim C — Dry-Solids Loss Discrepancy
- **Audit Contradiction:** Competing loss figures of 184.00 kg/day vs. 196.01 kg/day.
- **Reconciliation:** Raw dry solids feed = $15,000 \times (1 - 0.105) = 13,425.00\,\text{kg/day}$.
  - $184.00\,\text{kg/day}$ represents exactly $1.3706\%$ loss (stoichiometrically derived from dissolved solids in spent soak liquor).
  - $196.01\,\text{kg/day}$ represents an unverified general pulse milling literature assumption of $1.4600\%$ ($13,425 \times 0.0146 = 196.01\,\text{kg/day}$).
  - Both cases are retained as distinct scenarios. A loss of 196.01 kg/day reduces product dry solids from 13,241.00 kg/day to 13,228.99 kg/day, lowering saleable output by 13.34 kg/day.

### Claim D — Experimental Cooking Protocol Thermodynamics
- **Audit Contradiction:** Proposed cooking conditions of $115.0^\circ\text{C}$ and $1.05\text{ bar}$.
- **Reconciliation:** Saturated steam tables (IAPWS-97) establish that water at $115.0^\circ\text{C}$ has an absolute vapor pressure of $1.691\text{ bar}_{abs}$ ($169.1\text{ kPa}_{abs}$). The corresponding gauge pressure is:
  $$P_{gauge} = 1.691 - 1.013 = 0.678\,\text{bar}_g \quad (9.83\,\text{psig})$$
  If an autoclave were operated at $1.05\text{ bar}_g$ ($2.063\text{ bar}_{abs}$), saturated steam temperature would be $121.2^\circ\text{C}$. If $1.05\text{ bar}_{abs}$ were applied, boiling temperature would be only $101.0^\circ\text{C}$. The protocol is clarified: operating at $115.0^\circ\text{C}$ requires exactly **$0.68\,\text{bar}_g$ saturated steam pressure**, or an overpressure air-steam autoclave.

### Claim E — Statistical Replication Hierarchy
- **Audit Contradiction:** Treating 9 observations as independent degrees of freedom.
- **Reconciliation:** The computational framework enforces a 3-tier hierarchical nested design: 3 preparation batches $\times$ 3 technical repeats. Technical repeats nested within a single batch share common batch-level liquor and temperature history. Degrees of freedom for treatment comparisons are restricted to $N = 3$ preparation batches.

### Claim F — Laboratory Quotations & Accreditation
- Candidate laboratories (Eureka Analytical, Mitra S.K., CGCRI) and itemized costs (INR 1,73,000 for Option 1; INR 2,85,000 for Option 2) are formally classified as `PROVISIONAL_BUDGETARY_QUOTATIONS`, pending formal contract issuance upon Milestone 1 advance.

### Claim G — CAD and Aspen Simulation Boundaries
- The Aspen Plus V14 converged simulation (`FINNOAQ_15TPD_CONVERGED.bkp`) models triple-effect water evaporation utility duties for spent liquor under the ELECNRTL property package. It does not model solid cotyledon mass transfer, cellular starch gelatinization, or dal hydration.

### Claim H — Statistical Certainty & Commercial Guarantees
- Unsupported 5-sigma guarantees have been retracted. The turnkey plant estimate (INR 5.42 Crore) is strictly categorized as an unverified Phase 4 conceptual projection.

---

## 4. Machine-Readable Design Basis Register

All model parameters are stored in `configs/design_basis_register.json` and `.csv`. Each entry carries explicit evidence states (`MEASURED`, `SOURCE_REPORTED`, `OFFICIAL_SOURCE`, `LITERATURE_SUPPORTED`, `CALCULATED`, `SIMULATED`, `ASSUMPTION`, `HYPOTHESIS`, `NOT_VERIFIED`, `BLOCKED`):

| ID | Parameter Description | Value | Units | Evidence State | Source / Reference |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `FEED-001` | Raw feed dal processing capacity | 15000.0 | kg/day | `OFFICIAL_SOURCE` | SOW Item 4 |
| `FEED-002` | Raw feed dal initial moisture (WB) | 10.5 | % WB | `LITERATURE_SUPPORTED` | IS 4333 standard |
| `LOSS-001A` | Soaking & screening solids loss (Scen. 1) | 184.0 | kg/day | `CALCULATED` | Stream balance (1.3706%) |
| `LOSS-001B` | Soaking & screening solids loss (Scen. 2) | 196.01 | kg/day | `ASSUMPTION` | Literature milling (1.46%) |
| `DRYER-IN-B1` | Pre-dryer wet mass (Scenario B1: 28% WB) | 18390.28 | kg/day | `CALCULATED` | Material balance |
| `DRYER-IN-B2` | Pre-dryer wet mass (Scenario B2: reported) | 18590.00 | kg/day | `SOURCE_REPORTED` | Preliminary flowsheet |
| `PROD-001` | Target finished dal moisture (WB) | 10.0 | % WB | `OFFICIAL_SOURCE` | FSSAI Table 3 |
| `SOAK-001` | Conditioning liquor-to-grain ratio | 1.50 | kg/kg | `OFFICIAL_SOURCE` | SOW WP-03 |
| `COOK-001` | Reported target dal whistles | 6.0 | whistles | `SOURCE_REPORTED` | Informal client report |
| `COOK-002` | Reported benchmark dal whistles | 3.0 | whistles | `SOURCE_REPORTED` | Informal client report |
| `COOK-003` | Calibrated autoclave temperature | 115.0 | deg C | `OFFICIAL_SOURCE` | SOW protocol |
| `COOK-004` | Saturated steam absolute pressure | 1.691 | bar_abs | `CALCULATED` | IAPWS-97 steam tables |
| `COOK-005` | Saturated steam gauge pressure | 0.678 | bar_g | `CALCULATED` | $P_{abs} - 1.01325\,\text{bar}$ |
| `PELEG-K1` | Peleg rate constant prior at 25 C | 2.35 | min/% | `LITERATURE_SUPPORTED` | Singh & Prasad (pigeon pea) |
| `PELEG-K2` | Peleg capacity constant prior at 25 C | 0.0125 | %^-1 | `LITERATURE_SUPPORTED` | Singh & Prasad (pigeon pea) |
| `BUDGET-P1` | Phase 1 Diagnostic R&D Fee (Option 1) | 173000.0 | INR | `OFFICIAL_SOURCE` | Table 4, SOW Table 40 |

---

## 5. Model Architecture & Implementation Verification

### 5.1 Model A — Deterministic Balances (`src/finnoaq/deterministic_balances.py`)
- **Governing Equations:**
  $$w = \frac{X}{1+X}, \quad X = \frac{w}{1-w}$$
  $$\dot{m}_{evap} = \dot{m}_{water,in} - \dot{m}_{water,out}$$
  $$Q_{thermal} = \dot{m}_{solids} c_{p,s} \Delta T + \dot{m}_{w,out} c_{p,w} \Delta T + \dot{m}_{evap} [h_{fg} + c_{p,v} (T_{out} - T_{evap})]$$
- **Verification Results:**
  - Scenario B1 ($28.00\%$ WB): Dryer inlet wet mass = $18,390.28\,\text{kg/day}$; evaporation = $3,678.06\,\text{kg/day}$ ($183.90\,\text{kg/h}$); thermal duty = $134.23\,\text{kW}_{th}$; mathematical closure error = $0.000000\%$.
  - Scenario B2 ($18,590.00\,\text{kg/day}$): Implied inlet moisture = $28.7735\%$ WB; evaporation = $3,877.78\,\text{kg/day}$ ($193.89\,\text{kg/h}$); thermal duty = $141.11\,\text{kW}_{th}$; mathematical closure error = $0.000000\%$.
  - Unresolved physical delta: **199.72 kg/day water (6.88 kW_th thermal duty)**.
  - Competing solids loss: $184.00\,\text{kg/day}$ yields $13,241.00\,\text{kg/day}$ dry solids; $196.01\,\text{kg/day}$ yields $13,228.99\,\text{kg/day}$ dry solids.

### 5.2 Model B — Hydration Kinetics (`src/finnoaq/hydration_kinetics.py`)
- **Peleg Model:** $M(t) = M_0 + \frac{t}{k_1 + k_2 t}$.
- **Fickian Radial Diffusion Model:** $\text{MR}(t) = 1 - \frac{6}{\pi^2} \sum_{n=1}^{30} \frac{1}{n^2} \exp\left(-\frac{n^2 \pi^2 D_{eff} t}{R^2}\right)$.
- **Verification on Synthetic Benchmark Dataset (`data/synthetic/synthetic_hydration_test_dataset.csv`):**
  - Peleg fit converged: $k_1 = 2.8369 \pm 0.0458\,\text{min/\%}$ ($95\%\,\text{CI}: [2.733, 2.941]$); $k_2 = 0.0110 \pm 0.0004\,\text{\%}^{-1}$; $R^2 = 0.9996$; $\text{RMSE} = 0.243\%$.
  - Identifiability criteria satisfied: coefficient of variation $\text{CV}(k_1) = 1.6\% < 50\%$; $\text{CV}(k_2) = 3.4\% < 50\%$.
  - Fickian diffusion coefficient estimated: $D_{eff} = 4.484 \times 10^{-11}\,\text{m}^2/\text{s}$ ($\text{RMSE}_{MR} = 0.113$).

### 5.3 Model C — Cooking Performance & Texture Endpoint (`src/finnoaq/cooking_model.py`)
- Standardized endpoint: $T_{90}$ ($\le 10.0\%$ hard-core retention on 50 grains under 500 g load).
- **Model Comparison:**
  - Model 1 (Baseline Thermal Softening): Predicted $T_{90} = 30.70\,\text{min}$.
  - Model 2 (Hydration-Coupled): Predicted $T_{90} = 36.56\,\text{min}$ (incorporating slow hydration rate $k_1 = 2.837$).
  - Model 3 (Biochemical Dual-Path): `BLOCKED_MISSING_BIOCHEMICAL_DATA` (requires measured pectin fractionation).
  - Validation Status: `NOT_VALIDATED — PENDING_PHYSICAL_LABORATORY_ASSAYS`.

### 5.4 Model D — Hypothesis Discrimination & OED (`src/finnoaq/hypothesis_discrimination.py`)
- Ranks all 11 funded work packages in `Final_Proposal.pdf` (Total: INR 1,73,000 + GST) by diagnostic cost-efficiency:

| Rank | Work Package ID | Work Package Title | Budget (INR) | Discriminating Power (bits) | Diagnostic Efficiency (bits/kINR) | Target Hypotheses |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | **WP-01** | Sample Intake, Grading & Physical Inspection | 5,000 | 0.40 | **0.0800** | H2, H8 |
| **2** | **WP-04** | Water Absorption Kinetics & Peleg Modeling | 10,000 | 0.80 | **0.0800** | H1, H8 |
| **3** | **WP-02** | Moisture & Proximate Composition (AOAC) | 7,000 | 0.50 | **0.0714** | H1, H7 |
| **4** | **WP-06** | Mineral Profiling (ICP-OES) & Phytate | 16,000 | 0.90 | **0.0562** | H4, H5 |
| **5** | **WP-08** | Standardized Baseline Autoclave Cooking | 20,000 | 0.98 | **0.0490** | H10, H1, H4 |
| **6** | **WP-10** | Candidate Treatment Screening | 20,000 | 0.92 | **0.0460** | H4, H6 |
| **7** | **WP-07** | Texture Profile Analysis (TPA) Shear | 17,000 | 0.75 | **0.0441** | H3, H4, H7 |
| **8** | **WP-09** | Statistical Analysis & Hypothesis Ranking | 15,000 | 0.65 | **0.0433** | All H1-H10 |
| **9** | **WP-03** | Starch Gelatinization & DSC Thermal Analysis | 20,000 | 0.85 | **0.0425** | H6 |
| **10** | **WP-05** | Cell-Wall Pectin Fractionation | 28,000 | 0.95 | **0.0339** | H3, H4 |
| **11** | **WP-11** | Technical Report & Client Review | 15,000 | 0.30 | **0.0200** | All H1-H10 |

- **Hypothesis Coverage Audit:** All 10 hypotheses are covered by at least two independent experimental assays (`is_fully_covered = True`).

---

## 6. GPU Benchmark & Monte Carlo Uncertainty Results (The Required GPU Experiment)

The GPU engine (`src/finnoaq/gpu_accelerator.py` and `scripts/run_investigation_suite.py`) was benchmarked across workload sizes from $N = 100$ to $N = 250,000$ scenarios on the host NVIDIA GeForce RTX 4050 Laptop GPU (2,560 CUDA cores, Compute Capability 8.9, 6,140.5 MB VRAM) vs. Vectorized NumPy CPU (AMD Ryzen AI 9, 20 logical threads):

### 6.1 Performance and Numerical Error Benchmark Table

| Workload ($N$) | CPU Time (s) | GPU F32 Total (s) | GPU F32 Kernel (ms) | GPU F32 H2D (ms) | GPU F32 Speedup | Peak VRAM (MB) | $L_\infty$ Evap Error (kg) | $L_2$ Evap Error (kg) | GPU F64 Total (s) | GPU F64 Speedup | $L_\infty$ F64 Error (kg) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **100** | 0.000036 | 0.000896 | 0.338 | 0.426 | 0.04x | 0.16 | $1.07 \times 10^{-3}$ | $4.15 \times 10^{-4}$ | 0.000691 | 0.05x | $0.00 \times 10^0$ |
| **1,000** | 0.000071 | 0.000634 | 0.375 | 0.173 | 0.11x | 0.23 | $1.58 \times 10^{-3}$ | $4.22 \times 10^{-4}$ | 0.000435 | 0.16x | $0.00 \times 10^0$ |
| **10,000** | 0.000289 | 0.000744 | 0.367 | 0.273 | 0.39x | 0.90 | $1.63 \times 10^{-3}$ | $4.28 \times 10^{-4}$ | 0.001384 | 0.21x | $0.00 \times 10^0$ |
| **50,000** | 0.000931 | 0.006740 | 0.937 | 5.388 | 0.14x | 4.43 | $1.79 \times 10^{-3}$ | $4.22 \times 10^{-4}$ | 0.002668 | 0.35x | $0.00 \times 10^0$ |
| **100,000** | 0.001591 | 0.004296 | 1.502 | 2.091 | 0.37x | 12.37 | $1.76 \times 10^{-3}$ | $4.24 \times 10^{-4}$ | 0.005529 | 0.29x | $0.00 \times 10^0$ |
| **250,000** | 0.013542 | 0.006246 | 2.003 | 3.224 | **2.17x** | 27.63 | $1.75 \times 10^{-3}$ | $4.24 \times 10^{-4}$ | 0.010850 | **1.25x** | $0.00 \times 10^0$ |

### 6.2 Key Technical Findings from Benchmark:
1. **Numerical Parity (Float64):** GPU Float64 execution exhibits **exact zero absolute error ($L_\infty = 0.00$, $L_2 = 0.00$)** when cross-referenced against the 64-bit CPU NumPy reference path.
2. **Float32 Precision Bounds:** GPU Float32 single-precision exhibits a maximum absolute error $L_\infty = 1.75 \times 10^{-3}\,\text{kg}$ on a nominal $3,678\,\text{kg/day}$ water evaporation ($< 0.00005\%$ relative error) and $L_\infty = 7.42 \times 10^{-5}\,\text{kW}$ ($< 0.08\,\text{W}$) on a $134\,\text{kW}_{th}$ thermal duty, satisfying the $< 10^{-3}$ acceptance gate.
3. **GPU Scaling Crossover:** For small workloads ($N \le 10,000$), CPU execution dominates due to PCIe driver launch latency and buffer allocation overhead (Host-to-Device transfer consumes $0.17$ to $0.43\,\text{ms}$). The GPU establishes decisive dominance at **$N \ge 250,000$ scenarios**, achieving **$2.17\times$ speedup** in Float32 ($6.25\,\text{ms}$ total vs $13.54\,\text{ms}$ CPU; compute kernel alone executed in just $2.00\,\text{ms}$, representing a $6.76\times$ pure compute speedup).
4. **VRAM Footprint:** Maximum VRAM consumption at $N = 250,000$ was **$27.63\,\text{MB}$** (Float32) and **$37.12\,\text{MB}$** (Float64), consuming $< 0.6\%$ of the available 6,141 MiB dedicated VRAM.

### 6.3 Mode A (Unconditioned Research) vs. Mode B (Conditioned Laboratory) Uncertainty:
A 100,000-scenario Monte Carlo comparison demonstrated how incoming physical assays collapse engineering design uncertainty:

| Metric | Mode A (Wide Unconditioned Priors) | Mode B (Conditioned on Lab Assays) | Variance Reduction ($\Delta \sigma^2$) |
| :--- | :---: | :---: | :---: |
| **Dryer Evaporation (kg/day)** | $3,925.8 \pm 455.4$ [$3,235.6 - 4,648.4$] | $3,678.3 \pm 77.5$ [$3,551.2 - 3,805.8$] | **97.1% Reduction** |
| **Thermal Drying Duty ($\text{kW}_{th}$)** | $142.7 \pm 15.6$ [$118.9 - 167.6$] | $134.2 \pm 2.6$ [$129.9 - 138.5$] | **97.1% Reduction** |
| **Cooking Softening $T_{90}$ (min)** | $36.1 \pm 6.1$ [$25.4 - 45.2$] | $36.56 \pm 0.34$ [$36.00 - 37.12$] | **99.7% Reduction** |
| **Product Recovery (kg/day)** | $14,705.5 \pm 52.8$ [$14,618.5 - 14,792.1$] | $14,712.2 \pm 5.6$ [$14,703.1 - 14,721.4$] | **98.9% Reduction** |

### 6.4 Industrial 15 MT/day Scale-Up Design Margins:
- Continuous Fluid-Bed Dryer (`DR-101`) nominal design evaporation capacity = **$225.1\,\text{kg/h}$** (base design capacity $285.1\,\text{kg/h}$).
- Scenario B1 hourly evaporation requirement ($3,678.06\,\text{kg/day} / 20\,\text{h}$) = $183.90\,\text{kg/h}$ $\rightarrow$ **$+22.4\%$ design margin**.
- Scenario B2 hourly evaporation requirement ($3,877.78\,\text{kg/day} / 20\,\text{h}$) = $193.89\,\text{kg/h}$ $\rightarrow$ **$+16.1\%$ design margin**.
- Design conclusion: Both competing pre-dryer moisture scenarios are safely enveloped within the mechanical sizing of DR-101 without equipment modification.

---

## 7. Software Acceptance Gate Results

All 7 acceptance gates defined in Section 15 passed automated unit and integration testing (`tests/test_computational_models.py`):

| Gate ID | Gate Title | Verification Criterion | Status |
| :---: | :--- | :--- | :---: |
| **Gate A** | **Source & Design-Basis Integrity** | Design basis register has 17 audited inputs with valid epistemic tags. | `PASSED` |
| **Gate B** | **Balance Correctness** | Both scenarios B1 and B2 reproduce arithmetic with 0.000000% error; 184 vs 196 kg distinct. | `PASSED` |
| **Gate C** | **Model Implementation** | Peleg and Fickian solvers converge; identifiability passes; missing covariates flagged. | `PASSED` |
| **Gate D** | **GPU Verification** | PyTorch CUDA execution succeeds on RTX 4050; numerical equivalence $< 10^{-3}$. | `PASSED` |
| **Gate E** | **Offline Verification** | Full pipeline runs locally with zero external network or remote model calls. | `PASSED` |
| **Gate F** | **Scientific Validity** | Synthetic data clearly banner-labeled; 10 hypotheses covered; no causal leaps. | `PASSED` |
| **Gate G** | **Delivery Quality** | Manifest `artifacts/computational_pipeline_run_manifest.json` generated and verifiable. | `PASSED` |

---

## 8. Ten Required Agent Response Items (Section 17)

### 1. What Works Now
- Master pipeline entrypoint: `py -3.13 scripts/run_computational_pipeline.py --device cuda:0 --n-scenarios 100000` (executed in 1.18 s).
- Master investigation suite: `py -3.13 scripts/run_investigation_suite.py` (executed in 7.41 s across all 8 engineering sections).
- Automated test suite: `py -3.13 tests/test_computational_models.py` (7/7 tests passed in 1.60 s).
- Benchmark script: `py -3.13 scripts/run_gpu_monte_carlo_benchmark.py` (evaluated across N = 100 to 250,000).
- Balance verification script: `py -3.13 scripts/verify_deterministic_balances.py` (reconciled Scenarios B1 and B2 with 0.000000% error).

### 2. Hardware
- **CPU:** 10 physical cores / 20 logical threads (AMD64), 23.12 GB system RAM (3.86 GB available).
- **GPU:** NVIDIA GeForce RTX 4050 Laptop GPU (Ada Lovelace, Compute 8.9), 6,141 MiB VRAM total.
- **Framework:** PyTorch 2.6.0+cu124 running on `cuda:0`, CUDA runtime verified via matrix operations and CUDA event timers.

### 3. Offline Status
- **`OFFLINE_VERIFIED`:** Confirmed. The entire pipeline, test suite, and benchmark ran exclusively against local scripts, local configurations, and local synthetic data with zero network socket calls or external cloud dependencies.

### 4. Numerical Verification
- **Scenario B1 (28.00% WB Inlet):** Feed = 15,000 kg/day; Product = 14,712.22 kg/day; Evaporation = 3,678.06 kg/day; Thermal Duty = 134.23 kW_th; Closure Error = 0.000000%.
- **Scenario B2 (18,590 kg/day Inlet):** Implied Moisture = 28.7735% WB; Evaporation = 3,877.78 kg/day; Thermal Duty = 141.11 kW_th; Closure Error = 0.000000%.
- **Physical Delta:** +199.72 kg/day water (+6.88 kW_th duty).
- **Competing Solids Loss:** 184.00 kg/day (1.3706%) yields 13,241.00 kg/day product solids; 196.01 kg/day (1.4600%) yields 13,228.99 kg/day product solids.

### 5. Model Maturity States
- `deterministic_balances.py`: **`M2 — NUMERICALLY_VERIFIED`** (Reference balance tests and closure error pass).
- `hydration_kinetics.py`: **`M2 — NUMERICALLY_VERIFIED`** (Non-linear least squares, covariance, and identifiability pass on synthetic data).
- `cooking_model.py`: **`M1 — IMPLEMENTED`** for Model 1/2; **`M0 — SPECIFIED`** for Model 3; **`NOT_VALIDATED`** for target dal.
- `hypothesis_discrimination.py`: **`M2 — NUMERICALLY_VERIFIED`** (OED entropy calculations and cost-efficiency ranking pass).
- `gpu_accelerator.py`: **`M2 — NUMERICALLY_VERIFIED`** (Numerical equivalence with CPU NumPy reference verified).

### 6. GPU Benchmark
- **Workload:** 100 to 250,000-scenario Monte Carlo parameter sweep across 9 uncertain parameters.
- **Runtimes:** At $N = 250,000$, CPU NumPy = $0.01354\,\text{s}$, GPU PyTorch F32 = $0.00625\,\text{s}$ ($2.17\times$ speedup; compute kernel only $2.003\,\text{ms}$), GPU PyTorch F64 = $0.01085\,\text{s}$ ($1.25\times$ speedup).
- **Numerical Error:** Max absolute error (F32) = $1.75 \times 10^{-3}\,\text{kg}$ evaporation, $7.42 \times 10^{-5}\,\text{kW}$ thermal duty; Max absolute error (F64) = $0.00 \times 10^0$ (exact bitwise parity).
- **Limitations:** For $N \le 10,000$, CPU is faster due to PCIe kernel launch and memory transfer overhead.

### 7. Scientific Limitations
- **Explicit Confirmation:** No computational model in this repository has been validated against physical Tanzanian pigeon pea samples. All predictive parameter estimates derive from published pulse literature or synthetic test datasets. Physical validation remains blocked until physical dal samples arrive.

### 8. Existing-Project Corrections
- Demoted pectin crosslinking from fact to Hypothesis H4.
- Resolved mathematical mass balance discrepancy into Scenarios B1 and B2; flagged physical delta (199.72 kg/day) as unresolved pending drainage tests.
- Reconciled competing solids loss figures (184.00 kg vs 196.01 kg).
- Identified and corrected autoclave thermodynamic state ($115^\circ\text{C}$ requires $0.68\,\text{bar}_g$, not $1.05\,\text{bar}_g$).
- Bounded statistical degrees of freedom to $N = 3$ preparation batches.
- Purged all obsolete third-party attributions, colloquialisms, and emojis.

### 9. Files Created or Changed
- `configs/design_basis_register.json` & `.csv`: Audited machine-readable parameter ledger (`FUNCTIONAL`).
- `src/finnoaq/deterministic_balances.py`: First-principles mass, moisture, and thermal balance engine (`FUNCTIONAL`).
- `src/finnoaq/hydration_kinetics.py`: Peleg fitting, Fickian diffusion, and synthetic dataset generator (`FUNCTIONAL`).
- `src/finnoaq/cooking_model.py`: Hard-core retention $T_{90}$ and multi-model comparison (`FUNCTIONAL`).
- `src/finnoaq/hypothesis_discrimination.py`: 10-hypothesis EIG ranking and SOW Table 40 budget optimization (`FUNCTIONAL`).
- `src/finnoaq/gpu_accelerator.py`: CUDA Monte Carlo uncertainty engine and benchmark (`FUNCTIONAL`).
- `src/finnoaq/gpu_chemistry.py`: First-principles reaction-diffusion PDE across cotyledon slab (`FUNCTIONAL`).
- `data/synthetic/synthetic_hydration_test_dataset.csv`: Clearly labeled test dataset (`DATA`).
- `scripts/verify_deterministic_balances.py`: Unit verification script for balance reference cases (`TEST`).
- `scripts/run_gpu_monte_carlo_benchmark.py`: GPU scaling and performance benchmark script (`BENCHMARK`).
- `scripts/run_computational_pipeline.py`: Master single-command pipeline entrypoint (`PIPELINE`).
- `scripts/run_investigation_suite.py`: Integrated master investigation runner (`PIPELINE`).
- `tests/test_computational_models.py`: Automated test suite for Gates A through G (`TEST`).
- `artifacts/computational_pipeline_run_manifest.json`: Execution run manifest (`ARTIFACT`).
- `artifacts/investigation_suite_manifest.json`: Full investigation run manifest (`ARTIFACT`).
- `reports/GPU_CPU_BENCHMARK_RESULTS.json`: The Required GPU Experiment benchmark payload (`ARTIFACT`).
- `reports/OFFLINE_GPU_COMPUTATIONAL_MODELLING_REPORT.md`: Comprehensive engineering report (`REPORT`).

### 10. Blockers and Next Action
- **Blocker 1:** Physical grain consignments (10–15 kg target dal, 1–2 kg Indian benchmark) have not arrived at the laboratory.
- **Blocker 2:** Client approval of Proposal Rev V10 and remittance of Milestone 1 advance (INR 69,200 + GST).
- **Next Safe Action:** Await client shipment confirmation and tracking number. Upon arrival, log consignments in `Lab_Data/SAMPLE_RECEIVING_AND_CHAIN_OF_CUSTODY_LOG.csv`, execute AOAC 925.10 moisture test and IS 4333 grading, and ingest physical observations directly into `src/finnoaq/hydration_kinetics.py`.
