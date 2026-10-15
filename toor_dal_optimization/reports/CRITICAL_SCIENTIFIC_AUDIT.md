# CRITICAL SCIENTIFIC AUDIT — HARAKUTIR DREAM-RSI DIGITAL TWIN

**Document ID:** FIN-AUD-CRIT-2026-001  
**Project Phase:** Stage 1 — Treatment Discovery & Forensic Verification  
**Auditor:** Autonomous Scientific & Red-Team Engineering Audit  
**Date:** 2026-10-15  
**Governing Standard:** Master Forensic Audit & Immutable Goal Lock  

---

## 1. Executive Forensic Summary

This critical scientific audit evaluates every computational claim, simulation model, machine learning surrogate, and physical assumption in the Harakutir Toor Dal R&D repository.

### Immutable Project Directive

Our primary goal remains discovering and experimentally validating a physically defensible treatment that reduces the cooking time of Harakutir's Tanzanian split/dehulled pigeon pea (*Cajanus cajan*).

- **Stage 1:** Treatment discovery, mechanistic calibration, and physical kitchen validation.
- **Stage 2:** Industrial plant engineering for 15 MT/day. **Stage 2 is strictly locked** and must not unlock until Stage 1 satisfies all prespecified acceptance gates with physical data.

### Primary Audit Findings

1. **The $8192 \times 8192$ Solver Shortcut:** The reported 0.0051s runtime and 64.06 MB VRAM did **not** execute a 2D numerical PDE solve across 67,108,864 nodes. It computed a 0D analytical Green's function scalar and performed four sequential 64 MB dummy chunk allocations. A real 2D finite-difference stencil on an $8192 \times 8192$ grid on the local NVIDIA RTX 4050 Laptop GPU requires **1,536.00 MB (1.50 GB)** VRAM and executes in **30.75 ms per single step** (~3.54s for 100 steps).
2. **Hard-Coded Winner Prediction:** In `scripts/run_dream_rsi_discovery.py` (lines 198–248), candidate cooking times were **hard-coded in an `if/elif` ladder** (e.g., `elif conc == 0.50: cook_time = 13.8`). The 13.8-minute winner was not dynamically computed from the coupled partial differential equations or `CellularTissueTwin`.
3. **Conflation of Atmospheric Boiling with Pressure Cooking:** The baseline of 58.0 minutes / 16.9 whistles represented an open-pot atmospheric boiling model (100°C, 1 atm). The client's physical kitchen observation is that untreated Tanzanian dal requires **approximately 6 whistles (~22 minutes)** in a domestic pressure cooker (~115°C, 15 psi). Comparing Candidate A2 (13.8 min) against 58 min conflated open boiling with pressure cooking.
4. **Uncalibrated Molecular Biophysics Mechanism:** The proposed pectin methylesterase (PME), phytase, and calcium pectate de-esterification mechanism and its $7.73\times$ softening rate equation are **theoretical heuristics** synthesized from general pulse literature, not calibrated against wet-chemical assays of the target Tanzanian grain lot.
5. **Reconciliation of Material Recovery & Retained Sodium:**
   - *Solids Recovery:* 98.54% is nominal leaching loss (1.46%); 96.80% is the conservative default loss (3.20%); 95.65% includes multi-unit plant mechanical attrition (4.35%).
   - *Retained Sodium:* 53.9 mg Na / 100g dal is elemental sodium under a standard single-pass mist rinse (25% surface removal); 6.4 mg Na / 100g dal corresponds to an intensive counter-current rinse (>96% surface salt displacement). Both are compliant with the FSSAI statutory threshold of $< 350\text{ mg/100g}$.
6. **PINN & Transformer Limitations:**
   - The PINN was benchmarked on a synthetic PDE setup with hard-coded reference constants, not on real dal.
   - The Transformer surrogate was trained on a purely synthetic uniform algebraic dataset. Its out-of-distribution (OOD) detector exhibited a **100% false-negative rate** on extreme out-of-distribution inputs.
7. **Retraction of Automatic Five-Sigma Claim:** Entering four control and four treatment timestamps into a kitchen protocol cannot automatically establish $5\sigma$ significance ($p < 2.87 \times 10^{-7}$). Statistical power calculations show that for $n=4$, $5\sigma$ is only possible if the experimental standard deviation $s \le 30\text{ seconds}$. If $s \approx 60\text{--}90\text{ seconds}$, significance is $3.67\sigma\text{ to }4.22\sigma$. Stage 2 remains locked.

---

## 2. Claim-by-Claim Forensic Evidence Table

| Claim ID | System / Domain | Specific Claim in Documentation | Implementing Code Location | Actual Implementation Reality | Computational Method | Forensic Status / Verdict | Corrective Action Taken |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CLM-001** | Mesh Scaling | 8192×8192 grid (67.1M nodes) solved in 0.0051s with 64.06 MB VRAM | `src/harakutir/high_res_spatial_solver.py:141-167` | 0D analytical Green's function series + 4× dummy 64MB tensor fill/delete loops. Zero 2D stencil updates across nodes. | Analytical shortcut + dummy chunk allocation | **DISCREDITED AS FULL SOLVE** | Corrected in `HIGH_RESOLUTION_GRID_STUDY.md`; empirical GPU stencil benchmark documented (1.54 GB, 30.75 ms/step). |
| **CLM-002** | Treatment Discovery | CAND-004 predicted cooking time is 13.8 min / 3.4 whistles | `scripts/run_dream_rsi_discovery.py:240-250` | Hard-coded branch: `elif conc == 0.50: cook_time = 13.8`. Not dynamically solved by PDE or tissue twin. | Hard-coded entry | **UNVERIFIED AS DYNAMIC SOLVE** | Classified as `COMPUTATIONAL_HYPOTHESIS`; re-anchored against domestic 6-whistle pressure cooker baseline. |
| **CLM-003** | Untreated Baseline | Untreated Tanzanian dal cooks in 58.0 min / 16.9 whistles | `reports/TREATMENT_CANDIDATE_RANKING.csv` | 58 min is simulated open atmospheric boiling at 100°C. 16.9 whistles was computed via `(58 - 3.8)/3.2`. | Conflated atmospheric model | **MISLEADING COMPARATOR** | Re-anchored to domestic pressure cooker baseline: ~22.0 min (~6.0 whistles) at 115°C, 15 psi. |
| **CLM-004** | Material Recovery | Winning candidate achieves 98.54% recovery | `reports/MASS_AND_ENERGY_BALANCE.md:61-63` | 98.54% is based on 1.46% nominal leaching loss in 15 MT/day flowsheet. `dose_calculator.py` default gave 96.8% (3.2% loss). | Primary mass balance calculation | **CALCULATED (CONDITIONAL)** | Reconciled: 98.54% nominal wash recovery, 96.80% conservative bound, 95.65% whole-plant recovery. |
| **CLM-005** | Retained Sodium | Finished dal retains 6.4 mg Na / 100g dal | `reports/15MT_DAY_PROCESS_DESIGN.md:105` | 6.4 mg assumes an intensive multi-stage counter-current rinse. Standard single mist rinse retains 53.9 mg elemental Na/100g. | Parameter-dependent calculation | **RECONCILED CONDITIONAL** | Both rinse regimes explicitly defined; both verified $< 350\text{ mg/100g}$ FSSAI limit. |
| **CLM-006** | Molecular Biophysics | PME/phytase/calcium pectate increases softening rate by 7.73x | `reports/MULTISCALE_PHYSICS_ARCHITECTURE.md:66-72` | Algebraic heuristic: $k_{\text{soft}} = k_0 \exp(-E_a/RT) \cdot \frac{1+3.2\chi_{\text{Na}}}{1+2.5\rho_{\text{Ca}}}$. Constants (3.2, 2.5, 0.70) are uncalibrated on target lot. | Phenomenological literature heuristic | **UNPROVEN HYPOTHESIS** | Demoted to `Working Biophysical Hypothesis H-B1`; defined required wet-lab chemical assays (DE, AAS). |
| **CLM-007** | Physics-Informed NN | PINN estimates $D_{\text{eff}}$ and $k_{\text{soft}}$ with < 8.2% error | `src/harakutir/pinn_solver.py:93-205` | Inverse solver tested against synthetic constants ($2.4\times 10^{-11}, 0.0035$) without physical observations. In short 100-iter runs, error was 70.2% and 36.4%. | Synthetic benchmark | **SOFTWARE VERIFIED ONLY** | Documented that PINN is verified as code, but uncalibrated against real physical dal samples. |
| **CLM-008** | Transformer Surrogate | Transformer achieves 0.6 MAE with native OOD detection | `src/harakutir/scientific_transformer.py:107-182` | Trained on 2,000 synthetic random uniform samples. OOD detector tested `sigmoid(out) > 0.65 or < 0.35` with 100% false-negative rate on real OOD inputs. | Synthetic model test | **UNRELIABLE OOD DETECTOR** | Exposed 100% false-negative rate; disqualified attention entropy/sigmoid as safety gate. |
| **CLM-009** | Statistical Power | 4 control + 4 treated batches automatically achieves 5-sigma | `reports/STAGE_1_VALIDATION_REPORT.md:18,39` | Statistical significance depends on observed $s$. For $n=4$, $5\sigma$ requires $s \le 30\text{ s}$. If $s = 60\text{ s}$, significance is $4.22\sigma$; if $s = 120\text{ s}$, $3.25\sigma$. | Invalid a priori assumption | **RETRACTED** | Retracted automatic pass; replaced with conditional hypothesis test ($t_{\text{obs}} \ge 3.707, p \le 0.005$). |
| **CLM-010** | Stage Gate Lock | Stage 2 scale-up unlocks automatically upon kitchen data entry | `reports/STAGE_1_VALIDATION_REPORT.md:39` | Contradicts project constitution. Stage 2 requires meeting all 6 gates simultaneously with physical sample certificates. | Process governance flaw | **STRICTLY RE-LOCKED** | Stage 2 declared locked until physical kitchen data confirms $H_0$ rejection, recovery $\ge 95.5\%$, and sensory $\ge 7.5$. |

---

## 3. Detailed Audit of Repository Source Files

### 3.1 `src/harakutir/high_res_spatial_solver.py`
- **Intended Scope:** 2D axisymmetric spatial mesh refinement study from $64\times 64$ to $8192\times 8192$.
- **Actual Implementation:**
  - For $N \le 4096$, allocates three dense float32 grids ($T, M, S$) and immediately deletes them.
  - For $N = 8192$, loops four times allocating a $(2048 \times 8192)$ chunk (64 MB), filling with a scalar, and deleting it.
  - Core values $T(0,0)$ and $M(0,0)$ are computed via 0D Green's function series:
    $$\tau_{\text{th}} = \frac{\alpha_{\text{th}} t}{H^2}, \quad T_{\text{core}} = 25.0 + 75.0 \times \left(1.0 - e^{-2.4674\tau_{\text{th}}} e^{-0.85\tau_{\text{th}}}\right)$$
  - **Audit Verdict:** The implementation verified memory chunking and analytical continuum asymptotes, but did **not** execute a 2D numerical finite-difference PDE solve on 67.1M nodes.

### 3.2 `src/harakutir/pinn_solver.py`
- **Intended Scope:** Physics-Informed Neural Network solving coupled heat, moisture, and softening with inverse parameter estimation.
- **Actual Implementation:**
  - `CotyledonPINN`: 3-layer MLP with 48 hidden units and SiLU activations.
  - Loss function: $\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{PDE}} + 10\mathcal{L}_{\text{BC}} + 10\mathcal{L}_{\text{IC}}$.
  - Inverse parameters $\ln(D_m)$ and $\ln(k_{\text{soft}})$ are initialized with perturbed values and updated via Adam optimizer.
  - No physical laboratory data is ingested; training uses random collocation points in $[0, 1]^3$.
  - Reference values are hard-coded constants (`true_diffusivity_Deff = 2.40e-11`, `true_softening_rate_ksoft = 0.0035`).
  - **Audit Verdict:** Valid software demonstration of physics-informed autograd, but provides zero independent evidence regarding real Tanzanian dal.

### 3.3 `src/harakutir/scientific_transformer.py`
- **Intended Scope:** Transformer encoder surrogate for rapid candidate screening with out-of-distribution (OOD) detection.
- **Actual Implementation:**
  - `ScientificTransformerSurrogate`: 2-layer `TransformerEncoder` with 64 embedding dimensions and 4 attention heads.
  - Training dataset: 2,000 synthetic points generated by `np.random.uniform` and an algebraic formula.
  - Metric MAE: Evaluated by unweighted averaging across cook time (min), recovery (%), sodium (mg), and sensory (1–9). Because metrics have wildly different units and scales, the reported MAE has no physical meaning.
  - OOD Detection: Implemented as `ood_flag = torch.sigmoid(out[:, 4])` with threshold `ood_flag > 0.65 or ood_flag < 0.35`. Because the fifth output unit has no training loss targeting OOD classification, it produces random values around 0.50.
  - Empirical Audit Test: On 50 extreme out-of-distribution inputs (e.g. 15% NaHCO3, 200°C soak), the detector failed on **50 out of 50 samples (100% false-negative rate)**.
  - **Audit Verdict:** Valid neural network architecture, but the surrogate is trained on synthetic data and its OOD detection mechanism is fundamentally unreliable.

### 3.4 `src/harakutir/molecular_biophysics.py`
- **Intended Scope:** Multiscale biophysical twin bridging molecular species to cellular mechanics.
- **Actual Implementation:**
  - `MolecularSpeciesInventory`: Hard-coded reference values for vicilin, legumin, homogalacturonan, and minerals.
  - `MolecularToContinuumTransfer`: Softening rate accelerated via `(1.0 + 3.2 * chi_Na) / (1.0 + 2.5 * rho_Ca) * 1e11`.
  - `CellularTissueTwin`: Evaluates $\sigma = \sigma_0 \exp(-k_{\text{soft}} t)$ against $\sigma_{\text{crit}} = 45\text{ kPa}$.
  - Under this class, treated dal at 13.8 minutes yields $\sigma = 189.65\text{ kPa} > 45\text{ kPa}$ (`is_cooked = False`). The class predicts cooked status at $\approx 36.8\text{ minutes}$.
  - **Audit Verdict:** The molecular twin does not output 13.8 minutes. The 13.8-minute winner was hard-coded in the candidate script. The biophysical relationships are phenomenological hypotheses.

### 3.5 `scripts/run_dream_rsi_discovery.py`
- **Intended Scope:** Goal-locked discovery loop ranking treatment candidates.
- **Actual Implementation:**
  - Lines 198–248 used a hard-coded `if/elif` ladder to assign cooking times:
    `CAND-004: 13.8 min`, `CAND-006: 14.6 min`, `CAND-003: 18.2 min`, `CAND-005: 11.2 min`, `CAND-001: 58.0 min`.
  - Did not execute numerical solvers or neural networks during candidate evaluation.
  - Assigned $16.9\text{ whistles}$ to untreated dal by applying `(cook_time - 3.8) / 3.2` to 58 minutes of open boiling.
  - **Audit Verdict:** The candidate ranking table was an arithmetic script outputting preset engineering estimates, not an autonomous numerical simulation discovery.

---

## 4. Test Suite Audit & Classification (64 Tests)

All 64 unit and integration tests were executed and passed cleanly in 7.39 seconds. Their scientific evidence level is classified as follows:

| Classification Category | Number of Tests | Percentage | Definition & Scope | What They Actually Prove | What They DO NOT Prove |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Software Correctness** | 24 | 37.5% | Verifies file existence, schema parsing, JSON/YAML integrity, error handling, atomic checkpointing. | Code runs without crashing; files are in proper formats. | Does not prove physical models are accurate. |
| **Numerical Verification** | 15 | 23.4% | Compares numerical implementations against analytical formulas (Fourier series, Peleg identifiability, finite difference stencil benchmarks). | Solvers correctly solve the mathematical equations they are programmed to solve. | Does not prove the equations represent real toor dal. |
| **Data Validation & Balances** | 13 | 20.3% | Asserts parameter bounds, regulatory limits (FSSAI < 350 mg), stoichiometry, unit conversions, recovery basis separation. | Parameters and mass balances stay within physically and legally consistent ranges. | Does not prove parameters match the target lot. |
| **Synthetic-Model Validation**| 10 | 15.6% | Benchmarks PINN on synthetic PDE, Transformer on synthetic dataset, Monte Carlo on synthetic distributions. | Algorithms work on idealized synthetic benchmarks. | Does not prove predictive accuracy on physical dal. |
| **Governance & Statistical** | 2 | 3.1% | Enforces evidence status taxonomy, prevents premature confirmation, derives exact statistical power for Welch's t-test. | Guarantees test assertions fail if unverified claims are marked as confirmed or if 5-sigma is claimed automatically. | Does not provide the wet-lab kitchen data itself. |
| **Physical Wet-Lab Validation**| **0** | **0.0%** | **Validation against measured target-lot laboratory samples.** | **None (Pending Physical Protocol).** | **Treatment efficacy is NOT experimentally validated.** |

---

## 5. Summary of Corrective Actions Taken

1. **Re-Anchored Baseline:** Replaced the 58 min / 16.9 whistle strawman baseline with the standardized domestic pressure cooker baseline: **$\approx 22.0\text{ min}$ ($\approx 6.0\text{ whistles}$)**.
2. **Corrected Benchmarks:** Documented the real 2D finite-difference GPU stencil benchmark (**1.54 GB VRAM, 30.75 ms/step**) in [REPRODUCED_BENCHMARKS.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/REPRODUCED_BENCHMARKS.md).
3. **Reconciled Mass Balances:** Formalized the three recovery tiers (**98.54% nominal wash recovery, 96.80% conservative bound, 95.65% plant recovery**) in [CORRECTED_MASS_AND_CHEMICAL_BALANCES.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/CORRECTED_MASS_AND_CHEMICAL_BALANCES.md).
4. **Parameter Provenance Ledger:** Created [PHYSICS_PARAMETER_PROVENANCE.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/PHYSICS_PARAMETER_PROVENANCE.md) documenting the provenance of every physical variable and demoting uncalibrated mechanisms to hypotheses.
5. **Statistical Governance Review:** Created [STATISTICAL_DESIGN_REVIEW.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/STATISTICAL_DESIGN_REVIEW.md) formally retracting the automatic 5-sigma guarantee and keeping Stage 2 strictly locked.
6. **Automated Regression Tests:** Added [test_audit_reconciliation_and_contradictions.py](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/tests/test_audit_reconciliation_and_contradictions.py) to lock in these corrections and prevent regressions.

---

**Signed Off:**  
Harakutir Red-Team Scientific Audit Committee  
*October 15, 2026*
