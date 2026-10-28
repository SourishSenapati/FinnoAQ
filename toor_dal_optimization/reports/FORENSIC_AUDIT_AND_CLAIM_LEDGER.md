# FINNOAQ TOOR DAL — FORENSIC AUDIT & CLAIM LEDGER

**Document ID:** FIN-AUD-LEDGER-2026-002  
**Date:** 15 October 2026  
**Governing Standard:** Master Build Directive — Toor Dal Cooking-Time Optimization & 15 MT/Day Process Design  
**Status:** FORENSIC AUDIT COMPLETED — NO PREMATURE CONFIRMATION  

---

## 1. Executive Audit Mandate

This forensic audit ledger provides an evidence-traceable, unvarnished accounting of every numeric claim, computational model, biophysical assumption, and benchmark in the FinnoaQ Toor Dal R&D repository.

### Non-Negotiable Truth Rule
No prompt, simulation, passing unit test, literature analogy, GPU run, digital twin, or large synthetic dataset can guarantee real-world success. The system must state what is known, what is inferred, what remains unknown, and exactly what physical experiment or engineering verification closes each gap. **Stage 2 (15 MT/day scale-up) is strictly locked** until Stage 1 physical kitchen validation passes.

---

## 2. Claim-by-Claim Forensic Audit Register

| Claim / Feature | Source Code Location | Evidence Type | Independent Reproduction | Finding | Severity | Correction Implemented | Regression Test | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **8192×8192 Mesh Grid Solve (67.1M nodes)** | `src/finnoaq/high_res_spatial_solver.py:141-167` | `simulation` / `shortcut` | Profiled on RTX 4050 Laptop GPU | Did **not** execute 2D PDE solve. Evaluated 0D analytical Green's function series and 4× dummy 64MB tensor loops. A real 2D stencil requires **1,536 MB (1.50 GB)** VRAM and **30.75 ms/step** (~3.38s / 100 steps). | **CRITICAL (S1)** | Discredited 0.0051s claim; added true 2D finite-difference stencil benchmark in `high_res_spatial_solver.py:benchmark_real_2d_pde_stencil`. | `test_8192_grid_memory_and_stencil_requirements` | **RESOLVED & DOCUMENTED** |
| **CAND-004 Cooking Time (13.8 min / 3.4 whistles)** | `scripts/run_dream_rsi_discovery.py:245-250` | `hypothesis` / `hard-coded` | Code inspection | Cooking time was hard-coded in an `elif conc == 0.50: cook_time = 13.8` branch. Not dynamically solved by PDE or cellular tissue twin. | **CRITICAL (S1)** | Demoted status to `COMPUTATIONAL_HYPOTHESIS`; removed premature `EXPERIMENTALLY_CONFIRMED` label. | `test_evidence_status_taxonomy_and_prohibition_of_premature_confirmation` | **CORRECTED TO HYPOTHESIS** |
| **Untreated Dal Baseline (58.0 min / 16.9 whistles)** | `reports/TREATMENT_CANDIDATE_RANKING.csv` | `simulation` / `conflated` | Analytical & literature review | 58.0 min was open atmospheric boiling at 100°C. Household client baseline is **~6 whistles (~22 min)** in a domestic pressure cooker (115°C, 15 psi). 16.9 whistles was an artificial formula `(58-3.8)/3.2`. | **MAJOR (S2)** | Re-anchored baseline comparator to domestic pressure cooker standard: ~22.0 min (~6.0 whistles). | `test_stage_c_cooking_response_raw_vs_treated` | **RE-ANCHORED** |
| **Solids Recovery Contradiction (98.54% vs 96.8%)** | `reports/MASS_AND_ENERGY_BALANCE.md` vs `src/finnoaq/dose_calculator.py:58` | `derived_from_observed` vs `published_literature` | Rigorous mass balance reconciliation | 98.54% is nominal wash leaching recovery (1.46% loss); 96.80% is conservative default in `dose_calculator.py` (3.2% loss); 95.65% is whole-plant recovery including mechanical fines (2.89% loss). | **MAJOR (S2)** | Explicitly separated all 3 recovery boundaries with stream tables in `plant_design_15tpd.py`. | `test_solids_recovery_and_basis_separation`, `test_mass_balance_closure_and_dry_solids_recovery` | **RECONCILED BY BOUNDARY** |
| **Retained Sodium Contradiction (53.9 mg vs 6.4 mg)** | `reports/15MT_DAY_PROCESS_DESIGN.md:105` | `derived_from_observed` | Stoichiometric washing balance | 53.9 mg Na/100g corresponds to standard single-pass mist rinse (25% displacement); 6.4 mg Na/100g corresponds to intensive 3-stage counter-current rinse (>96% displacement). Both comply with FSSAI (<350 mg). | **MAJOR (S2)** | Fully defined both rinse regimes and elemental sodium conversion (27.37% Na in NaHCO3). | `test_retained_sodium_chemical_vs_elemental_separation` | **RECONCILED BY RINSE REGIME** |
| **Chemical Dose Ambiguity (112.5 kg vs 75.0 kg)** | `src/finnoaq/dose_calculator.py` vs reports | `derived_from_observed` | Arithmetic stoichiometric check | At 15,000 kg/day feed and 1:1.5 liquor ratio (22,500 kg liquor), 0.50% w/w in liquor = **112.5 kg/day** active chemical. 0.50% of incoming dal feed = **75.0 kg/day**. | **MAJOR (S2)** | Kept both calculations fully visible in `PlantDesign15TPD` and config files; annual difference is ~₹3.9 Lakhs. | `test_chemical_dosing_bases_separation` | **SEPARATED & VISIBLE** |
| **Automatic 5-Sigma Guarantee** | `reports/STAGE_1_VALIDATION_REPORT.md:18,39` | `assumption` / `invalid` | Student's / Welch's t-distribution math | Mathematically impossible to guarantee 5-sigma ($p < 2.87 \times 10^{-7}$) with $n=4$ ($df=6$) unless sample variance $s \le 30\text{ seconds}$. If $s \approx 60\text{--}90\text{ s}$, significance is $3.67\sigma\text{ to }4.22\sigma$. | **CRITICAL (S1)** | Retracted automatic 5-sigma guarantee; replaced with exact conditional hypothesis test ($t_{\text{obs}} \ge 3.707, p \le 0.005$). | `test_statistical_power_and_retraction_of_automatic_five_sigma` | **RETRACTED & REPLACED** |
| **Transformer Surrogate OOD Detection Failure** | `src/finnoaq/scientific_transformer.py:175-182` | `synthetic_test_only` | 50-sample OOD perturbation benchmark | Tested `sigmoid(out[:,4]) > 0.65 or < 0.35` on 50 extreme out-of-distribution vectors (15% NaHCO3, 200°C soak). Failed on **50/50 samples (100% false-negative rate)**. | **CRITICAL (S1)** | Disqualified neural attention entropy/sigmoid as safety gate; replaced with deterministic bounds checking. | `test_transformer_surrogate_and_ood_detection` | **DISQUALIFIED AS GATE** |
| **PINN Inverse Parameter Estimation Accuracy** | `src/finnoaq/pinn_solver.py:93-205` | `synthetic_test_only` | 100-iteration autograd optimization | In short runs, parameter estimation error on synthetic data was $70.2\%$ for $D_m$ and $36.4\%$ for $k_{\text{soft}}$. The PINN has never seen physical dal data. | **MODERATE (S3)** | Tagged as synthetic demonstration; barred from engineering decisions until trained on physical wet-lab data. | `test_pinn_coupled_transport_and_inverse_estimation` | **ISOLATED TO SYNTHETIC** |
| **Molecular Biophysics 7.73x Acceleration Equation** | `reports/MULTISCALE_PHYSICS_ARCHITECTURE.md:66-72` | `published_literature` / `hypothesis` | Algebraic deconstruction | Equation $k_{\text{soft}} = k_0 e^{-E_a/RT} \frac{1+3.2\chi_{\text{Na}}}{1+2.5\rho_{\text{Ca}}}$ contains uncalibrated coefficients ($3.2, 2.5, 0.70$) that were not measured on target lot. | **MAJOR (S2)** | Demoted to `Working Biophysical Hypothesis H-B1`; created wet-lab assay roadmap (ICP-OES, FT-IR). | `test_molecular_to_continuum_biophysical_twin` | **DEMOTED TO HYPOTHESIS** |

---

## 3. Numeric Input Provenance Ledger

Every single numeric parameter utilized across the computational models, balances, and economic estimates is classified into an epistemic category:

| Parameter Symbol | Description | Value | Units | Epistemic Provenance Tag | Source / Derivation Justification | Verification Requirement to Close Gap |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\dot{m}_{\text{feed}}$ | Nominal Dal Feed Rate | 15,000.0 | kg/day | `assumption` | Client commercial target for industrial facility. | Commercial business requirement. |
| $w_{\text{feed}}$ | Raw Dal Moisture | 10.0 | % w.b. | `observed_target_lot` | Typical commercial Tanzanian import lot certificate. | Moisture meter verify per consignment. |
| $w_{\text{target}}$ | Target Packaged Moisture | 10.0 | % w.b. | `published_literature` | Standard Indian storage target to prevent mold/insects (FSSAI max 14.0%). | AOAC 925.10 hot air oven check. |
| $R_{\text{liq}}$ | Dal-to-Liquor Mass Ratio | 1.5 | kg/kg | `hypothesis` | Candidate A2 formulation ratio. | Confirmatory bench soak test. |
| $t_{\text{soak}}$ | Ambient Soaking Time | 30.0 | min | `hypothesis` | Candidate A2 formulation parameter. | Confirmatory bench soak test. |
| $T_{\text{soak}}$ | Soak Temperature | 25.0 | °C | `assumption` | Ambient factory floor condition in India. | Monitor seasonal ambient fluctuation. |
| $C_{\text{NaHCO3}}$ | Reagent Concentration | 0.50 | % w/w | `hypothesis` | Winning candidate formulation. | Wet-lab bench titration. |
| $t_{\text{cook,control}}$ | Baseline Cooking Time | 22.0 | min | `derived_from_observed` | Derived from client report of ~6 whistles in domestic pressure cooker. | Standardized thermocouple cooker run. |
| $t_{\text{cook,treated}}$ | Treated Dal Cooking Time | 13.8 | min | `hypothesis` | Predicted ~3.1 whistles for Candidate A2. | **Physical Kitchen Protocol ($n=4$).** |
| $L_{\text{wash}}$ | Nominal Leaching Loss | 1.46 | % solids | `published_literature` | Literature benchmark for short ambient pulse soaking. | Gravimetric wash water residue test. |
| $L_{\text{fines}}$ | Mechanical Fines Loss | 2.89 | % solids | `assumption` | Standard bucket elevator & fluid bed attrition. | Pilot line gravimetric collection. |
| $Y_{\text{plant}}$ | Whole-Plant Recovery | 95.69 | % solids | `derived_from_observed` | $(1 - 0.0146) \times (1 - 0.0289) = 95.69\%$. | 15 TPD commissioning mass balance. |
| $T_{\text{dry}}$ | Dryer Inlet Air Temp | 55.0 | °C | `published_literature` | Recommended max pulse drying temp (prevents protein denaturation). | Fluid bed air thermocouple. |
| $\eta_{\text{th}}$ | Dryer Thermal Efficiency | 0.65 | fraction | `assumption` | Standard insulated industrial fluid bed dryer. | Vendor performance guarantee. |
| $P_{\text{chem}}$ | Food Grade NaHCO3 Cost | 35.0 | ₹/kg | `assumption` | Current bulk chemical market quote (25 kg bags). | Formal vendor procurement quote. |
| $P_{\text{steam}}$ | Biomass Steam Cost | 0.55 | ₹/MJ | `published_literature` | Standard Indian dal mill biomass briquette boiler. | Factory utility log review. |
| $P_{\text{elec}}$ | Industrial Electricity | 8.50 | ₹/kWh | `assumption` | Commercial tariff schedule (HT industrial). | Local electricity utility bill. |
| $[\text{Na}]_{\text{retained}}$ | Retained Elemental Sodium | 53.9 | mg/100g | `derived_from_observed` | Stoichiometric calculation (single mist rinse). | ICP-OES / Flame Photometry assay. |

---

## 4. Audit Sign-Off & Governance Verdict

1. **Software Verification:** Code execution, syntax, unit test frameworks, and mass balance conservation are verified.
2. **Physical Verification:** **ZERO target-lot physical kitchen experiments have been conducted.**
3. **Status:** All treated candidates remain strictly classified as `COMPUTATIONAL_HYPOTHESIS`. No candidate is `EXPERIMENTALLY_CONFIRMED`.
4. **Stage 2 Gate:** **15 MT/day scale-up remains locked.**
