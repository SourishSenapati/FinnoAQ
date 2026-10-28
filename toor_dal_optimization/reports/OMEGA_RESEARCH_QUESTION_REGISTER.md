# FINNOAQ OMEGA — COMPLETE 35-QUESTION SCIENTIFIC & ENGINEERING REGISTER
**Project Ref:** `FNQ-PR-2026-001` | **System:** `FINNOAQ OMEGA (Offline-First Scientific Engineering & Proof System)`  
**Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Generated UTC:** `2026-10-27T23:02:34.322520+00:00` | **Machine-Readable Artifact:** `evidence_vault/claims/question_register_35.json`

---

## Summary Table of All 35 Mandatory Questions (Part L)

| ID | Question | Evidence Class | Key Numerical Result | Next Action |
| :---: | :--- | :--- | :--- | :--- |
| **Q01** | What exact cooker protocol defines the two-whistle target? | `PROTOCOL_SPECIFICATION_AND_CALCULATED` | Whistle 1 = 6.45 min; Whistle 2 = 8.40 min; Whistle 3 = 10.35 min; T_sat = 121.1 C at 103.4 kPa gauge. | Execute EXP-01 baseline calibration logging stopwatch time to Whistle 1, 2, and 3 on 5 replicates. |
| **Q02** | What is the baseline distribution of cooking time and tenderness? | `LITERATURE_SUPPORTED_AND_MODEL_DERIVED` | Indian Reference: 3 whistles (9.8-13.3 min); Aged Tanzanian HTC: 7-9 whistles (17.3-23.1 min). | Measure N=5 baseline replicates of Indian Latur and Tanzanian raw controls in EXP-01. |
| **Q03** | Which treatment methods have directly relevant pigeon-pea evidence? | `LITERATURE_SUPPORTED (DIRECT_AND_INDIRECT_SEPARATED)` | 8 DIRECT split pigeon-pea sources and 3 INDIRECT whole-seed/bean sources cataloged. | Run EXP-01 Pots 1-5 to directly validate 55 C citrate + 17 W/L UAE on split dhal. |
| **Q04** | What is the shortest defensible pretreatment time? | `MODEL_DERIVED_WITH_UNCERTAINTY_BOUNDS` | 15-18 min (Tier 1 Mild), 20 min nominal / 24 min robust (Tier 2 Standard), 26-30 min (Tier 3 Severe). Sub-10-min claims (4.6 min VI) are falsified. | Test t = 15, 20, 24, 28 min steeping in EXP-01. |
| **Q05** | Which mechanisms control treatment penetration and core softening? | `LITERATURE_SUPPORTED_AND_MODEL_DERIVED` | Sobol total-order variance indices on F_WB,core: Steeping_Time_t S_T = 0.6304, Native_Bound_Ca S_T = 0.1136, Half_Thickness_H S_T = 0.0986, Steeping_Temp_T S_T = 0.0829, Citrate_Molarity_C S_T = 0.0807. | Sectioned outer-vs-core EDTA/ICP-OES calcium assay in EXP-01. |
| **Q06** | Which assumptions in the existing model are identifiable from available data? | `STRUCTURAL_IDENTIFIABILITY_AUDIT` | 19/27 parameters independently identifiable from literature/thermodynamics; 8/27 require paired multi-duration/multi-thickness wet-lab calibration. | Include 2 sieve fractions x 4 soak times in Phase 1 WP-03/WP-04 calibration. |
| **Q07** | What aftertaste defects actually occur? | `LITERATURE_SUPPORTED` | NaHCO3 (S2-02): soapy R_off = 1.104, d' = 2.14 (FAIL). Acid quench (S2-03): hexanal = 73.9 ppb, d' = 2.71 (FAIL). S2-10-WINNER: R_off = 0.164, hexanal = 44.5 ppb, d' = 0.22. | Execute descriptive sensory profiling (QDA) alongside triangle testing in EXP-05. |
| **Q08** | Which treatment variables contribute to those defects? | `MODEL_DERIVED_AND_LITERATURE_SUPPORTED` | Shifting from 100% K-Citrate (S2-06) to 90:10 K/Na Citrate (S2-10) lowers R_off from 0.183 (d'=0.25) to 0.164 (d'=0.22) while keeping added Na at only 3.4 mg/100g. | Compare S2-02 (NaHCO3), S2-06 (100% K-Cit), and S2-10 (90:10 K/Na Cit) in Matrix A unspiced blind tasting. |
| **Q09** | What fraction of the defect can be attributed to treatment carryover or other measured contributors? | `MODEL_DERIVED_DECOMPOSITION` | S2-02 (NaHCO3): 78% exogenous chemical / 22% endogenous volatile. S2-10 (pH 5.20 Citrate + 12s spray): 42% sub-threshold ion carryover / 58% residual storage volatile. | Pair GC-MS hexanal/1-octen-3-ol + ICP-OES K/Na/citrate with descriptive sensory scores in EXP-05. |
| **Q10** | Which intervention reduces the measured defect? | `MODEL_DERIVED_AND_LITERATURE_SUPPORTED` | Reduces predicted Thurstonian d' from 3.45 (unwashed NaHCO3) and 2.14 (washed NaHCO3) to 0.22 (S2-10-WINNER). | Validate in EXP-01/EXP-02/EXP-05. |
| **Q11** | Can the aftertaste be made nondetectable under a defined sensory protocol? | `PREDICTED_MINIMUM (AWAITING_PHYSICAL_ISO_4120_TRIANGLE_TEST)` | Model prediction: d' = 0.22 (predicted correct triangle selection rate = 35.1% vs 33.3% chance). Physical test status: NOT_STARTED. | Execute N=24 blind ISO 4120 triangle test in EXP-05. |
| **Q12** | How close is each candidate to the Indian sensory reference? | `MODEL_DERIVED_RANKING (TOST_EQUIVALENCE_PENDING)` | S2-10-WINNER d' = 0.22 vs S2-02 (NaHCO3) d' = 2.14; TOST equivalence margin Delta = +/-0.75 points (N=72 consumers). | Execute EXP-05 N=72 consumer TOST trial on Matrix A (unspiced) and Matrix B (standardized tadka). |
| **Q13** | Which analytical measurements predict meaningful sensory differences? | `LITERATURE_SUPPORTED` | Target analytical gates: Cooked pH in [5.75, 6.35], surface film residue < 50 ppm, added Na < 15 mg/100g, cooked hexanal < 55 ppb. | Run pH, conductivity, ICP-OES, and SPME-GC-MS assays in EXP-02 and EXP-05. |
| **Q14** | What is the minimum tested rinse duration that satisfies the specified requirements? | `MODEL_DERIVED (REQUIRES_EXP_02_CONFIRMATION)` | t_spray = 12.0 s at 0.50 L/kg -> 23.3 ppm surface film residue (98.7% film removal). | Execute EXP-02 comparing 0 s, 6 s, 12 s, and 25 s spray wash conductivity and surface stickiness. |
| **Q15** | What is the full wash/dewatering residence time? | `CALCULATED_ENGINEERING_DESIGN` | Active spray exposure = 12.0 s (0.20 min); Full WSH-102 station residence time = 4.00 min (240.0 s). | Verify dewatering moisture at t = 1, 2, 3.3 min air-knife drainage in EXP-02. |
| **Q16** | How much moisture, water, energy, and yield are affected by washing? | `CALCULATED_MASS_AND_ENERGY_BALANCE` | 12s spray wash: 0.50 L/kg water (7,526 L/d), +0.08% solids loss, removes 98.7% surface film; saves 0.70 L/kg water and ~18 kW_th dryer load vs 30s immersion rinse. | Measure wet cake moisture before and after air-knife dewatering in EXP-02. |
| **Q17** | Which feedstock attributes predict cooking outcome? | `LITERATURE_SUPPORTED_AND_SOBOL_VERIFIED` | Feedstock variance contributors at fixed process conditions: Bound Ca2+ (48.2% of feedstock variance), Half-thickness H (41.8%), Initial moisture & porosity (10.0%). | Measure H, X_wb, WAI_3min, and EDTA-bound Ca2+ across 10 independent lots in EXP-04. |
| **Q18** | Which attributes predict aftertaste, if any? | `LITERATURE_SUPPORTED_AND_MODEL_DERIVED` | Over-treating thin mild lots (H = 0.88 mm) in Tier 3 (0.185 M) increases internal pore citrate from 109.7 to 148.5 mg/100g (R_off rises from 0.164 to 0.228). | Include free fatty acid / hexanal intake screening in EXP-04/EXP-05. |
| **Q19** | Can those attributes be measured reliably at intake? | `MODEL_DERIVED_ERROR_ANALYSIS (PROPOSED_DIAGNOSTIC_NOT_YET_FIELD_PROVEN)` | Direct H & X_wb: high reliability (<3% CV). Noisy WAI_3min proxy for Ca2+: 76.0% raw tier accuracy; requires uncertainty-buffered cutoffs (ADAPTIVE_ROBUST_P95) + 15-min pilot pressure-cook confirmation for borderline/unfamiliar shipments. | Evaluate repeatability and predictive R^2 of the 5-min WAI_3min assay across 10 real lots in EXP-04. |
| **Q20** | How often must the recipe change between batches? | `OPERATIONAL_ANALYSIS_AND_SIMULATION` | 1 recipe adjustment per 15-25 MT container lot (<= 1 changeover per 20 h operating day, taking ~15 min via automated dosing skid SK-100). | Verify intra-lot vs inter-lot variance in EXP-04. |
| **Q21** | What happens outside the validated batch domain? | `GOVERNANCE_AND_CONTROL_POLICY` | 4.7% OOD flag rate across simulated import distribution; routing OOD lots + buffered cutoffs reduces P95 core force from 20.34 N to 17.68 N. | Test extreme aged/thick cotyledon sieve fraction (>2.5 mm) in EXP-04. |
| **Q22** | Which parts of the toor-dal model transfer to other dal species? | `MECHANISTIC_TRANSFERABILITY_AUDIT` | 4/8 model sub-blocks share universal physics/thermodynamics; 4/8 require species-specific parameter tables. | Maintain separate species parameter cards in Module G. |
| **Q23** | What needs to be calibrated separately for each species? | `MODEL_DERIVED_AND_LITERATURE_SUPPORTED` | Chana (24 min -> 19.85 N FAIL, needs 28-30 min); Moong (12 min -> 14.03 N, 1 wh); Urad (18 min -> 13.83 N, 1 wh); Masoor (12 min -> 13.46 N, 1 wh). | Execute separate Phase 2 species-extension bench trials after Toor Dal validation. |
| **Q24** | What limits the complete production cycle? | `CALCULATED_PROCESS_SCHEDULING` | Active processing residence = 103.0 min (Tier 2) to 107.0 min (Robust 24m Tier 2); Gate-to-gate elapsed time = 118.0-122.0 min; Dryer + Tempering = 67.0 min (bottleneck). | Verify drying curve and tempering relaxation time in EXP-03. |
| **Q25** | Does the full process meet the 15 TPD design basis? | `INDEPENDENTLY_REPRODUCED_MASS_BALANCE` | Basis I (15,000 kg/d raw feed) -> 14,884.8 kg/d prime out. Basis II (15,000 kg/d prime out) -> 15,116.1 kg/d raw feed (755.8 kg/h). | Validate pilot throughput and turnaround drainage times in Stage 4 pilot run. |
| **Q26** | Are all material and energy balances consistent? | `INDEPENDENTLY_REPRODUCED_CALCULATION` | Dry solids closure error = 0.000000%; Evaporative delta (B2 - B1) = +199.72 kg/day. | Measure drained wet cake moisture in EXP-02. |
| **Q27** | Are reagent consumption and costs reconciled? | `INDEPENDENTLY_REPRODUCED_CALCULATION` | Once-Through: 880.91 kg/d (₹8.62/kg reagent, ₹11.65/kg total). 85% Recycle: 371.29 kg/d (₹3.63/kg reagent, ₹6.34/kg total). | Obtain formal vendor quotes for 10 MT/month bulk food-grade K3Cit·H2O and H3Cit in India and run 5-cycle reuse test in EXP-02. |
| **Q28** | What are the important food-safety and regulatory requirements? | `OFFICIAL_REGULATORY_SOURCE` | FSSAI max moisture = 14.0% WB; INS 330/331/332 permitted under GMP with mandatory ingredient declaration for conditioned dal. | Verify total plate count (TPC) and yeast/mold across 5 consecutive bath reuse cycles in EXP-02. |
| **Q29** | Which claims are supported by calculations and literature alone? | `INDEPENDENTLY_REPRODUCED_AND_LITERATURE_SUPPORTED` | 6 core mathematical, thermodynamic, and falsification conclusions established from first principles and literature. | Proceed to laboratory verification of material-dependent kinetic claims (Q30). |
| **Q30** | Which require laboratory measurements? | `REQUIRES_LABORATORY_MEASUREMENT` | 8 material-specific claims gated on bench laboratory measurements (Est. budget ₹31,500 across EXP-01 to EXP-04). | Execute EXP-01 (Monday Bench Trial) immediately upon sample receipt. |
| **Q31** | Which require sensory panels? | `REQUIRES_HUMAN_SENSORY_PANEL` | N = 24 trained assessors (ISO 4120 triangle test) + N = 72 naive consumers (ISO 11136 TOST equivalence test). | Commission accredited sensory laboratory for EXP-05 after EXP-01/02 pass. |
| **Q32** | Which require pilot or plant validation? | `REQUIRES_PILOT_OR_PLANT_VALIDATION` | 5 scale-up engineering phenomena requiring 100-500 kg/h pilot verification prior to 15 TPD CapEx commitment. | Execute 100 kg pilot trial after bench and sensory gates pass. |
| **Q33** | What experiment would most efficiently reduce the remaining uncertainty? | `BAYESIAN_VOI_RANKED_EXPERIMENT` | Reduces Stage 1/2 feasibility uncertainty by >75% for ₹3,500 in 1 day. | Execute EXP-01 following docs/specifications/MONDAY_BENCH_TRIAL_PROTOCOL.md. |
| **Q34** | What evidence is necessary before stating a commercial guarantee? | `GOVERNANCE_ACCEPTANCE_CRITERION` | 5 mandatory physical validation certificates required prior to commercial guarantee. | Complete Phase 1 diagnostic and bench validation (EXP-01 to EXP-05). |
| **Q35** | Which claims on the website need correction, downgrading, or removal? | `VERIFIED_PORTAL_REMEDIATION` | 6/6 legacy overclaims corrected and verified in compiled `toor_dal_optimization/portal/dist/` bundle. | Run `finnoaq website check` as part of final pre-response verification. |

---

## Detailed Question-by-Question Provenance & Analysis

### Q01: What exact cooker protocol defines the two-whistle target?
- **Current Scientific Answer:** 5.0 L Hawkins Classic deadweight-valve aluminium pressure cooker operating at 103.4 kPa gauge (204.7 kPa abs, saturated steam T = 121.1 C) on a 1.40 kW regulated LPG/induction heat input with 100.0 g split dhal + 350.0 mL potable water (1:3.5 w/w). Sensible heat-up to pressure lock takes 4.50 min (270 s), and each whistle cycle takes 1.95 min (117 s), making a 2-whistle cycle exactly 8.40 min (504 s) of active heating followed by 2.0 min off-heat depressurization before texture testing.
- **Evidence Classification:** `PROTOCOL_SPECIFICATION_AND_CALCULATED`
- **Evidence References:** `SRC-PIGEON-08 (10.1016/j.jfoodeng.2005.05.054)`, `docs/specifications/MONDAY_BENCH_TRIAL_PROTOCOL.md`
- **Model & Code Component:** `ThermalAndPressureCookingModule.solve_pressure_cooking_softening`
- **Verified Numerical Result:** Whistle 1 = 6.45 min; Whistle 2 = 8.40 min; Whistle 3 = 10.35 min; T_sat = 121.1 C at 103.4 kPa gauge.
- **Confidence & Uncertainty:** Burner power variance (+/-10%) shifts 2-whistle elapsed time by +/-0.55 min; thermocouple/pressure logging eliminates ambiguity.
- **Limitations:** A whistle is cooker-geometry and heat-input dependent; all two-whistle claims apply strictly to this standardized 1:3.5, 1.4 kW, 103.4 kPa protocol.
- **Downstream Decisions Enabled:** Locks Stage 1 acceptance gate at t90 <= 8.40 min and F_WB,core(W=2) <= 18.0 N.
- **Required Next Action:** Execute EXP-01 baseline calibration logging stopwatch time to Whistle 1, 2, and 3 on 5 replicates.

### Q02: What is the baseline distribution of cooking time and tenderness?
- **Current Scientific Answer:** Untreated Fresh Indian Latur Reference: t90_mech = 9.80 +/- 0.65 min (t90_emp = 13.30 min, 3 whistles), F_WB,core(W=2) = 21.53 +/- 1.15 N, F_WB,core(W=3) = 15.80 +/- 0.95 N. Untreated Aged Tanzanian HTC Control: t90_mech = 17.30 +/- 1.45 min (t90_emp = 23.10 min, 8 whistles), F_WB,core(W=2) = 25.64 +/- 1.50 N. Across East African dehulled genotypes (Machinjili et al., 2025), open-boiling cooking time spans 26.0 to 54.0 min.
- **Evidence Classification:** `LITERATURE_SUPPORTED_AND_MODEL_DERIVED`
- **Evidence References:** `SRC-PIGEON-07 (10.3389/fsufs.2025.1613117)`, `SRC-PIGEON-08 (10.1016/j.jfoodeng.2005.05.054)`
- **Model & Code Component:** `FeedstockCharacterizationModule & ThermalAndPressureCookingModule`
- **Verified Numerical Result:** Indian Reference: 3 whistles (9.8-13.3 min); Aged Tanzanian HTC: 7-9 whistles (17.3-23.1 min).
- **Confidence & Uncertainty:** High literature confidence on range; specific client lot requires physical baseline measurement.
- **Limitations:** No wet-lab texture data measured on client's specific physical bag yet.
- **Downstream Decisions Enabled:** Establishes that even fresh untreated Indian dhal takes ~3 whistles under un-soaked cooking, making a 2-whistle target on aged Tanzanian dhal an ambitious conditioning upgrade.
- **Required Next Action:** Measure N=5 baseline replicates of Indian Latur and Tanzanian raw controls in EXP-01.

### Q03: Which treatment methods have directly relevant pigeon-pea evidence?
- **Current Scientific Answer:** Directly evidenced on Cajanus cajan splits: (1) Warm water soaking + steam precooking/flaking (Chakraborty et al., 2007, 10.1016/j.jfoodeng.2006.10.019 — DIRECT); (2) NaHCO3 alkaline soaking/cooking texture kinetics (Nisha et al., 2006, 10.1016/j.jfoodeng.2005.05.054 & 10.1016/j.foodchem.2003.08.004 — DIRECT); (3) Dehulling + water hydration across East African genotypes (Machinjili et al., 2025 — DIRECT); (4) Divalent cation Ca2+/Mg2+ vs phytin-P chelation stoichiometry in split dhal (Narasimha & Desikachar, 1978 — DIRECT). Indirectly evidenced on whole pigeon pea seeds: (5) 40 kHz Ultrasound (17 & 43 W/L) + NaHCO3 (Vasquez et al., 2021, 10.1016/j.lwt.2021.111191 — INDIRECT whole seed at 27 C); (6) NaHCO3 protein digestibility/structure (Ohanenye et al., 2024 — INDIRECT whole seed). Hybrid K/Na Citrate at pH 5.20 + 55 C UAE combines these mechanisms and requires direct bench confirmation.
- **Evidence Classification:** `LITERATURE_SUPPORTED (DIRECT_AND_INDIRECT_SEPARATED)`
- **Evidence References:** `SRC-ANCHOR-01`, `SRC-ANCHOR-02`, `SRC-ANCHOR-03`, `SRC-PIGEON-07`, `SRC-PIGEON-08`, `SRC-PIGEON-09`
- **Model & Code Component:** `OfflineEvidenceIndex.search_sources(direct_only=True)`
- **Verified Numerical Result:** 8 DIRECT split pigeon-pea sources and 3 INDIRECT whole-seed/bean sources cataloged.
- **Confidence & Uncertainty:** Bibliographic provenance 100% verified via Crossref and OpenAlex.
- **Limitations:** Vasquez et al. (2021) tested ultrasound with NaHCO3 at 27 C on whole seeds, not citrate at 55 C on splits.
- **Downstream Decisions Enabled:** Mandates EXP-01 paired factorial comparison (Static Citrate vs UAE Citrate vs NaHCO3).
- **Required Next Action:** Run EXP-01 Pots 1-5 to directly validate 55 C citrate + 17 W/L UAE on split dhal.

### Q04: What is the shortest defensible pretreatment time?
- **Current Scientific Answer:** For nominal aged Tanzanian split dhal (2H = 2.16 mm, C_Ca,0 = 33.5 mol/m^3) under 0.145 M K/Na Citrate (pH 5.20, 55 C, 17 W/L UAE): 20.0 min is the shortest nominal time whose point estimate passes Whistle 2 core tenderness (F_WB,core = 17.35 N <= 18.0 N), while 24.0 min is the shortest robust uncertainty-buffered time whose 95th-percentile prediction bound passes (P95 = 17.52 N <= 18.0 N). For mild/thin lots (Tier 1, 2H <= 1.92 mm), 15.0-18.0 min suffices; for severe bold Arusha lots (Tier 3, 2H = 2.44 mm), 26.0-30.0 min with a 15 kPa vacuum pulse is required.
- **Evidence Classification:** `MODEL_DERIVED_WITH_UNCERTAINTY_BOUNDS`
- **Evidence References:** `SRC-ANCHOR-03`, `SRC-PIGEON-08`, `artifacts/omega_gpu_uncertainty_campaign.json`
- **Model & Code Component:** `HydrationAndPenetrationModule & GPU Uncertainty Campaign`
- **Verified Numerical Result:** 15-18 min (Tier 1 Mild), 20 min nominal / 24 min robust (Tier 2 Standard), 26-30 min (Tier 3 Severe). Sub-10-min claims (4.6 min VI) are falsified.
- **Confidence & Uncertainty:** At t = 20.0 min, P(F_WB,core <= 18 N) = 71.4%; at t = 24.0 min, P(F_WB,core <= 18 N) = 96.8%.
- **Limitations:** Depends on effective internal citrate diffusivity D_cit(55C, UAE) = 1.215e-9 m^2/s.
- **Downstream Decisions Enabled:** Sets standard SOP steeping range to 20-24 min (Tier 2) rather than promising <10 min.
- **Required Next Action:** Test t = 15, 20, 24, 28 min steeping in EXP-01.

### Q05: Which mechanisms control treatment penetration and core softening?
- **Current Scientific Answer:** Core softening is controlled by a sequential reaction-diffusion cascade across the cotyledon half-thickness H: (1) Fickian + cavitation-enhanced pore diffusion of HCit2-/Cit3- and co-diffusing K+/Na+ cations (tau_diff ~ H^2 / D_cit,eff); (2) thermodynamic ligand exchange displacing Ca2+ from middle-lamellar low-DE homogalacturonan egg-box junctions (log K_CaCit = 4.68 > log K_CaPectate = 3.85); and (3) subsequent 121.1 C pressure-cooking thermal dissolution of Ca-depleted middle-lamellar pectin coupled with intracellular starch gelatinization.
- **Evidence Classification:** `LITERATURE_SUPPORTED_AND_MODEL_DERIVED`
- **Evidence References:** `SRC-ANCHOR-04 (10.1016/j.foodchem.2023.135743)`, `SRC-CHEM-14 (NIST SRD 46)`, `SRC-PIGEON-10`
- **Model & Code Component:** `HydrationAndPenetrationModule & ThermalAndPressureCookingModule`
- **Verified Numerical Result:** Sobol total-order variance indices on F_WB,core: Steeping_Time_t S_T = 0.6304, Native_Bound_Ca S_T = 0.1136, Half_Thickness_H S_T = 0.0986, Steeping_Temp_T S_T = 0.0829, Citrate_Molarity_C S_T = 0.0807.
- **Confidence & Uncertainty:** High mechanistic consensus across legume literature.
- **Limitations:** Internal Donnan potential of negatively charged cell walls is lumped into effective diffusivity D_cit,eff.
- **Downstream Decisions Enabled:** Explains why 90:10 K+/Na+ (higher K+ Stokes mobility) outperforms 100% Na+ in reaching the core (17.35 N vs 18.85 N).
- **Required Next Action:** Sectioned outer-vs-core EDTA/ICP-OES calcium assay in EXP-01.

### Q06: Which assumptions in the existing model are identifiable from available data?
- **Current Scientific Answer:** Independently identifiable from existing literature/thermodynamics: (1) Citric/carbonic acid pKa and Ca/Mg stability constants (NIST SRD 46); (2) Grain geometry H, R_eq, and open porosity epsilon_open (Baryeh & Mangope, 2002); (3) Pure-water Peleg/Fickian diffusivity D_w(T) (Swami et al., 2013); (4) Thin-layer Page drying k(T), n (Shepherd & Bhardwaj, 1988). Jointly identifiable (collinear from a single cook endpoint): internal citrate diffusivity D_cit,ref and second-order chelation rate constant k_chel. Unidentifiable without new target-lot experiments: exact initial bound Ca2+ of a specific shipment without ICP-OES/WAI calibration, and human hedonic equivalence score.
- **Evidence Classification:** `STRUCTURAL_IDENTIFIABILITY_AUDIT`
- **Evidence References:** `reports/OMEGA_PARAMETER_REGISTER.md`, `evidence_vault/parameters/parameter_register.json`
- **Model & Code Component:** `scripts/build_evidence_vault.py::build_parameter_register`
- **Verified Numerical Result:** 19/27 parameters independently identifiable from literature/thermodynamics; 8/27 require paired multi-duration/multi-thickness wet-lab calibration.
- **Confidence & Uncertainty:** Documented parameter-by-parameter in parameter_register.json.
- **Limitations:** Breaking D_cit vs k_chel collinearity requires soaking two thickness sieve fractions (1.8 mm vs 2.4 mm) across 4 time points.
- **Downstream Decisions Enabled:** Prevents over-interpreting single-point cooking agreement as proof of unique internal rate parameters.
- **Required Next Action:** Include 2 sieve fractions x 4 soak times in Phase 1 WP-03/WP-04 calibration.

### Q07: What aftertaste defects actually occur?
- **Current Scientific Answer:** Three distinct sensory defects occur depending on chemistry and feedstock age: (1) Alkaline/soapy/flat mouthfeel from residual HCO3-/CO32- and fatty-acid saponification when NaHCO3 is used (pH > 8.0); (2) Bitter/metallic or sour/tart note if K3Cit/H3Cit is used at excessive molarity (>0.22 M), unwashed surface film, or over-acidified pH (<4.7); and (3) Endogenous grassy/beany/stale oxidized note (hexanal, 1-octen-3-ol, (E)-2-nonenal) inherent to aged maritime-stored East African pigeon pea.
- **Evidence Classification:** `LITERATURE_SUPPORTED`
- **Evidence References:** `SRC-FLAV-16 (Roland et al., 2017)`, `SRC-FLAV-17 (Keast & Breslin, 2002)`, `Khrisanapant et al. (2019)`
- **Model & Code Component:** `SensoryAndFlavourModule.evaluate_sensory_and_flavour`
- **Verified Numerical Result:** NaHCO3 (S2-02): soapy R_off = 1.104, d' = 2.14 (FAIL). Acid quench (S2-03): hexanal = 73.9 ppb, d' = 2.71 (FAIL). S2-10-WINNER: R_off = 0.164, hexanal = 44.5 ppb, d' = 0.22.
- **Confidence & Uncertainty:** Qualitative defect taxonomy is well established in pulse sensory science; quantitative intensity on client lot requires descriptive panel.
- **Limitations:** Model estimates chemical/volatile proxies, not direct human descriptors.
- **Downstream Decisions Enabled:** Separates exogenous chemical carryover control (washing + pH 5.20) from endogenous volatile control (55 C LOX suppression + ultrasonic degassing).
- **Required Next Action:** Execute descriptive sensory profiling (QDA) alongside triangle testing in EXP-05.

### Q08: Which treatment variables contribute to those defects?
- **Current Scientific Answer:** Bath pH (>7.5 triggers alkaline soapiness; <4.7 triggers sourness and vicilin curdling; 6.5-7.2 maximizes LOX lipid oxidation), bath molarity C_bath (governs internal pore solute loading), K+:Na+ cation ratio (100% K+ increases bitter/metallic note; 90:10 K+/Na+ masks trace K+ bitterness via sub-threshold Na+ receptor interaction), steeping temperature/ultrasound (controls LOX denaturation and volatile degassing), and post-soak spray-wash exposure time/water ratio (controls external surface film stripping).
- **Evidence Classification:** `MODEL_DERIVED_AND_LITERATURE_SUPPORTED`
- **Evidence References:** `SRC-FLAV-16`, `SRC-FLAV-17`, `SRC-CHEM-14`
- **Model & Code Component:** `TreatmentChemistryModule, WashingAndResidueModule & SensoryAndFlavourModule`
- **Verified Numerical Result:** Shifting from 100% K-Citrate (S2-06) to 90:10 K/Na Citrate (S2-10) lowers R_off from 0.183 (d'=0.25) to 0.164 (d'=0.22) while keeping added Na at only 3.4 mg/100g.
- **Confidence & Uncertainty:** High thermodynamic certainty on pH/ion concentrations; moderate uncertainty on taste-mixture suppression factor.
- **Limitations:** Interaction with household spice tempering (tadka) masks low-level off-notes; unspiced Matrix A is required for stringent detection.
- **Downstream Decisions Enabled:** Fixes Tier 2 composition at 0.145 M, pH 5.20, 90:10 K/Na ratio.
- **Required Next Action:** Compare S2-02 (NaHCO3), S2-06 (100% K-Cit), and S2-10 (90:10 K/Na Cit) in Matrix A unspiced blind tasting.

### Q09: What fraction of the defect can be attributed to treatment carryover or other measured contributors?
- **Current Scientific Answer:** In alkaline NaHCO3 treatment (S2-02), ~78% of total sensory divergence (d' = 2.14) originates from exogenous bicarbonate/carbonate alkaline carryover (R_off = 1.104) and ~22% from endogenous grassy volatiles. Conversely, in washed pH 5.20 90:10 K/Na Citrate (S2-10-WINNER, total d' = 0.22), exogenous reagent carryover is reduced to 16.4% of threshold (contributing ~42% of the tiny residual d'), while endogenous storage volatiles (44.5 ppb hexanal vs 38.0 ppb Indian baseline) account for the remaining ~58%.
- **Evidence Classification:** `MODEL_DERIVED_DECOMPOSITION`
- **Evidence References:** `SRC-FLAV-16`, `SRC-FLAV-17`, `artifacts/omega_investigation_results.json`
- **Model & Code Component:** `SensoryAndFlavourModule.evaluate_sensory_and_flavour`
- **Verified Numerical Result:** S2-02 (NaHCO3): 78% exogenous chemical / 22% endogenous volatile. S2-10 (pH 5.20 Citrate + 12s spray): 42% sub-threshold ion carryover / 58% residual storage volatile.
- **Confidence & Uncertainty:** Model-derived variance partitioning (+/-15%); requires analytical + sensory regression to confirm empirically.
- **Limitations:** Assumes additive orthogonal psychophysical combination of taste and retronasal aroma.
- **Downstream Decisions Enabled:** Shows that once pH 5.20 citrate + 12s spray wash is adopted, any remaining subtle difference vs Indian Latur dal is driven by native/storage seed volatiles rather than chemical residue.
- **Required Next Action:** Pair GC-MS hexanal/1-octen-3-ol + ICP-OES K/Na/citrate with descriptive sensory scores in EXP-05.

### Q10: Which intervention reduces the measured defect?
- **Current Scientific Answer:** Four coupled interventions minimize total sensory defect without losing 2-whistle softening: (1) Replace alkaline NaHCO3 with pH 5.20 buffered citrate (eliminating saponification and carbonate bitterness); (2) Use a 90:10 K+:Na+ molar ratio (eliminating pure-potassium metallic note while keeping core diffusion fast); (3) Steep at 55.0 C under 17 W/L 40 kHz ultrasound at pH 5.20 (inactivating ~78% of LOX and stripping free volatile aldehydes); and (4) Apply a 12.0 s dual-fan high-pressure (2.5 bar, 0.50 L/kg) potable water spray wash (stripping 98.7% of external adhering surface liquor film).
- **Evidence Classification:** `MODEL_DERIVED_AND_LITERATURE_SUPPORTED`
- **Evidence References:** `SRC-ANCHOR-02`, `SRC-FLAV-16`, `SRC-FLAV-17`
- **Model & Code Component:** `WashingAndResidueModule & SensoryAndFlavourModule`
- **Verified Numerical Result:** Reduces predicted Thurstonian d' from 3.45 (unwashed NaHCO3) and 2.14 (washed NaHCO3) to 0.22 (S2-10-WINNER).
- **Confidence & Uncertainty:** 95% CI on d' for S2-10-WINNER: [0.15, 0.35].
- **Limitations:** Classified as PREDICTED_MINIMUM until physical panel testing.
- **Downstream Decisions Enabled:** Locks Stage 2 process configuration to S2-10-WINNER.
- **Required Next Action:** Validate in EXP-01/EXP-02/EXP-05.

### Q11: Can the aftertaste be made nondetectable under a defined sensory protocol?
- **Current Scientific Answer:** PROVISIONAL / HYPOTHESIS (PREDICTED_MINIMUM): Our mass-transfer and psychophysical model predicts that S2-10-WINNER achieves a cooked-slurry off-taste ratio of R_off = 0.164 (d' = 0.22 < 0.50), which is consistent with sensory nondetection. However, per Part A2 governance rules, SENSORY_NONDETECTION can only be established physically when a trained panel (N >= 24, ISO 4120:2021 triangle test, alpha = 0.05, power >= 0.80 against d' = 1.0) shows no statistically significant detection of chemical aftertaste in unspiced Matrix A slurry.
- **Evidence Classification:** `PREDICTED_MINIMUM (AWAITING_PHYSICAL_ISO_4120_TRIANGLE_TEST)`
- **Evidence References:** `SRC-STAT-18 (Bi & Meyners, 2012)`, `ISO 4120:2021`
- **Model & Code Component:** `SensoryAndFlavourModule.design_iso_tost_equivalence_study`
- **Verified Numerical Result:** Model prediction: d' = 0.22 (predicted correct triangle selection rate = 35.1% vs 33.3% chance). Physical test status: NOT_STARTED.
- **Confidence & Uncertainty:** High confidence in sub-threshold ion levels; moderate uncertainty on trace astringency.
- **Limitations:** Cannot claim SENSORY_NONDETECTION as an accomplished fact prior to executing the N=24 blind triangle test.
- **Downstream Decisions Enabled:** Sets the Stage 2 gate status of S2-10-WINNER to 'Aftertaste reduced in model (PREDICTED_MINIMUM)'.
- **Required Next Action:** Execute N=24 blind ISO 4120 triangle test in EXP-05.

### Q12: How close is each candidate to the Indian sensory reference?
- **Current Scientific Answer:** In the biophysical/chemical model, relative to fresh Indian Latur reference dal (d' = 0.00 baseline, cooked hexanal ~38.0 ppb): S2-10-WINNER (90:10 K/Na Citrate pH 5.20 + 12s spray wash) is closest at d' = 0.22 (hexanal 44.5 ppb, R_off = 0.164), followed by S2-04 (100% Na-Citrate, d' = 0.19 but FAILS 2-whistle core tenderness at 18.85 N), S2-06 (100% K-Citrate + 12s spray, d' = 0.25), S2-07 (Unwashed 90:10 Citrate, d' = 0.44), S2-02 (Washed NaHCO3, d' = 2.14), S2-03 (NaHCO3 + Acid Quench, d' = 2.71), and S2-01 (Unwashed NaHCO3, d' = 3.45). Formal INDIAN_REFERENCE_EQUIVALENCE requires the N=72 ISO 11136:2014 TOST 90% CI for (mu_FinnoaQ - mu_IndianRef) to lie entirely within [-0.75, +0.75] hedonic points.
- **Evidence Classification:** `MODEL_DERIVED_RANKING (TOST_EQUIVALENCE_PENDING)`
- **Evidence References:** `SRC-ANCHOR-06 (ISO 11136:2014)`, `SRC-STAT-18 (Bi & Meyners, 2012)`
- **Model & Code Component:** `SensoryAndFlavourModule`
- **Verified Numerical Result:** S2-10-WINNER d' = 0.22 vs S2-02 (NaHCO3) d' = 2.14; TOST equivalence margin Delta = +/-0.75 points (N=72 consumers).
- **Confidence & Uncertainty:** Ranking between citrate and bicarbonate is robust; exact hedonic difference requires consumer panel.
- **Limitations:** Zero human hedonic ratings exist yet; legacy 8.8/9.0 numbers were purged.
- **Downstream Decisions Enabled:** Selects S2-10-WINNER as the sole candidate advancing to the N=72 consumer TOST panel.
- **Required Next Action:** Execute EXP-05 N=72 consumer TOST trial on Matrix A (unspiced) and Matrix B (standardized tadka).

### Q13: Which analytical measurements predict meaningful sensory differences?
- **Current Scientific Answer:** (1) Cooked-slurry pH and titratable alkalinity (predicts soapy/flat defect when pH > 6.75); (2) Rinse-water electrical conductivity and dried-grain ICP-OES elemental K+, Na+, and enzymatic/HPLC citrate (predicts salty/bitter/metallic/sour carryover); (3) Headspace SPME-GC-MS hexanal, (E)-2-nonenal, and 1-octen-3-ol (predicts grassy/beany oxidation defect); and (4) CIE L*a*b* tristimulus colorimetry (predicts alkaline polyphenol darkening when b*/L* ratio shifts).
- **Evidence Classification:** `LITERATURE_SUPPORTED`
- **Evidence References:** `SRC-FLAV-16 (Roland et al., 2017)`, `Khrisanapant et al. (2019)`
- **Model & Code Component:** `WashingAndResidueModule & SensoryAndFlavourModule`
- **Verified Numerical Result:** Target analytical gates: Cooked pH in [5.75, 6.35], surface film residue < 50 ppm, added Na < 15 mg/100g, cooked hexanal < 55 ppb.
- **Confidence & Uncertainty:** Analytical methods have <5% RSD when properly calibrated with internal standards.
- **Limitations:** Sub-detection-limit analytics do not automatically guarantee absence of trace retronasal off-notes.
- **Downstream Decisions Enabled:** Defines the exact analytical QC release panel for Stage 2 validation.
- **Required Next Action:** Run pH, conductivity, ICP-OES, and SPME-GC-MS assays in EXP-02 and EXP-05.

### Q14: What is the minimum tested rinse duration that satisfies the specified requirements?
- **Current Scientific Answer:** In our model sweep across 0, 6, 12, 20, 30, and 60 s spray/rinse durations, a 12.0-second high-pressure (2.5 bar) dual-fan spray wash using 0.50 L/kg potable water is the minimum duration that strips >98.5% of the external adhering surface liquor film (reducing surface film residue from 1,755.6 ppm to 23.3 ppm < 50 ppm dryer-fouling/bloom ceiling). A 6.0 s spray leaves ~198 ppm surface film (risking sticky FBD distributor plate fouling), while extending spray beyond 15-20 s yields diminishing returns (<2% additional total solute removal because internal pore citrate is diffusion-limited with tau_diff ~ 960 s) and wastes water.
- **Evidence Classification:** `MODEL_DERIVED (REQUIRES_EXP_02_CONFIRMATION)`
- **Evidence References:** `artifacts/omega_investigation_results.json::stage2_aftertaste_and_washing`
- **Model & Code Component:** `WashingAndResidueModule.simulate_washing_operation`
- **Verified Numerical Result:** t_spray = 12.0 s at 0.50 L/kg -> 23.3 ppm surface film residue (98.7% film removal).
- **Confidence & Uncertainty:** For k_wash in [0.22, 0.50] s^-1, required spray exposure for <50 ppm film is 12.0 s (95% CI: [8.5, 16.5] s).
- **Limitations:** Not yet physically tested across nozzle pressures; requires bench spray-wash trial.
- **Downstream Decisions Enabled:** Specifies a 12-15 s active spray zone on the vibratory dewatering deck.
- **Required Next Action:** Execute EXP-02 comparing 0 s, 6 s, 12 s, and 25 s spray wash conductivity and surface stickiness.

### Q15: What is the full wash/dewatering residence time?
- **Current Scientific Answer:** The full wash and dewatering unit operation (WSH-102) has a total grain residence time of 4.0 minutes (240.0 seconds), comprising: (a) 0.5 min (30 s) initial free-liquor gravity drainage over the 500 um wedge-wire recycle screen (recovering 85% of free bath liquor to SK-100); (b) 0.2 min (12.0 s) active high-pressure dual-fan potable water spray washing (0.50 L/kg); and (c) 3.3 min (198 s) vibratory transport under high-velocity air-knife dewatering hoods to strip surface water down to 28.0% WB (Scenario B1) - 28.7735% WB (Scenario B2) prior to dryer entry.
- **Evidence Classification:** `CALCULATED_ENGINEERING_DESIGN`
- **Evidence References:** `reports/OMEGA_STAGE4_PLANT_CYCLE_AND_ECONOMICS.md`, `docs/specifications/15TPD_FACTORY_SOP_AND_RECIPES.md`
- **Model & Code Component:** `PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics`
- **Verified Numerical Result:** Active spray exposure = 12.0 s (0.20 min); Full WSH-102 station residence time = 4.00 min (240.0 s).
- **Confidence & Uncertainty:** Deck transport velocity (0.01 m/s over 2.4 m deck) is mechanically fixed by exciter frequency.
- **Limitations:** Previously conflated in legacy reports; now strictly separated in all schedules and balances.
- **Downstream Decisions Enabled:** Included as the full 4.0 min step in the 103.0 min nominal single-lot residence time.
- **Required Next Action:** Verify dewatering moisture at t = 1, 2, 3.3 min air-knife drainage in EXP-02.

### Q16: How much moisture, water, energy, and yield are affected by washing?
- **Current Scientific Answer:** Compared to no-wash draining (S2-07), the 12.0 s spray wash (S2-10-WINNER at 0.50 L/kg): (1) consumes 7,526.3 L/day potable wash water at 15 TPD (₹0.045/kg water+ETP cost); (2) adds 0.08% additional dry-solids leaching loss (total net loss 0.35-0.42%); (3) adds +0.35% WB surface moisture prior to the air-knife, which is stripped back to 28.0-28.77% WB on the dewatering deck (+6.8 kW_th marginal dryer load if un-stripped, vs +24.7 kW_th in a 30 s static immersion rinse S2-08); and (4) prevents 1,755 ppm surface citrate caramelization/fouling on the 65 C dryer bed.
- **Evidence Classification:** `CALCULATED_MASS_AND_ENERGY_BALANCE`
- **Evidence References:** `artifacts/omega_investigation_results.json::stage2_aftertaste_and_washing & stage4_plant_and_sensitivity`
- **Model & Code Component:** `WashingAndResidueModule & PlantOperationsAndEconomicsModule`
- **Verified Numerical Result:** 12s spray wash: 0.50 L/kg water (7,526 L/d), +0.08% solids loss, removes 98.7% surface film; saves 0.70 L/kg water and ~18 kW_th dryer load vs 30s immersion rinse.
- **Confidence & Uncertainty:** Dryer inlet moisture uncertainty bounded by Scenario B1 (28.0% WB, 3,654.42 kg/d evap) vs Scenario B2 (28.7735% WB, 3,854.14 kg/d evap, +199.72 kg/d delta).
- **Limitations:** Exact screen drainage efficiency depends on air-knife slot velocity and bed depth.
- **Downstream Decisions Enabled:** Selects 12s spray + air-knife deck over static immersion rinsing.
- **Required Next Action:** Measure wet cake moisture before and after air-knife dewatering in EXP-02.

### Q17: Which feedstock attributes predict cooking outcome?
- **Current Scientific Answer:** The two primary feedstock attributes predicting Whistle-2 core tenderness F_WB,core are: (1) Native middle-lamellar bound divalent calcium density C_Ca,0 (Sobol S_T = 0.1136, driven by storage age/temperature/RH phytase + PME activity) and (2) Cotyledon half-thickness H (Sobol S_T = 0.0986, driven by cultivar/seed size, which scales diffusive penetration time as H^2). Secondary attributes are pectin degree of esterification DE, initial moisture X_wb,0, and open porosity epsilon_open. Together, C_Ca,0 and H combine into the mechanistic HTC Severity Index S_HTC = C_Ca,0 * (H / 1.0 mm)^1.35 (R^2 = 0.91 with fixed-recipe F_WB,core).
- **Evidence Classification:** `LITERATURE_SUPPORTED_AND_SOBOL_VERIFIED`
- **Evidence References:** `SRC-PIGEON-07 (Machinjili et al., 2025)`, `SRC-PIGEON-09 (Narasimha & Desikachar, 1978)`, `SRC-ANCHOR-04`
- **Model & Code Component:** `GlobalSensitivityAnalyzer.compute_sobol_indices & BatchVariabilityAndAdaptivePolicyModule`
- **Verified Numerical Result:** Feedstock variance contributors at fixed process conditions: Bound Ca2+ (48.2% of feedstock variance), Half-thickness H (41.8%), Initial moisture & porosity (10.0%).
- **Confidence & Uncertainty:** High physical confidence on H^2 diffusion scaling and Ca-pectate stoichiometry.
- **Limitations:** Country of origin and sea-transit days are contextual correlates, NOT direct deterministic predictors.
- **Downstream Decisions Enabled:** Requires intake diagnostics to measure both geometry (H) and hydration/swelling proxy for bound Ca2+ (WAI_3min).
- **Required Next Action:** Measure H, X_wb, WAI_3min, and EDTA-bound Ca2+ across 10 independent lots in EXP-04.

### Q18: Which attributes predict aftertaste, if any?
- **Current Scientific Answer:** (1) Endogenous grassy/beany off-notes in cooked dal are predicted by feedstock storage lipid peroxidation state (free fatty acid acid value, peroxide value, initial headspace hexanal, and native LOX activity, which increase with storage duration at >28 C); (2) Exogenous chemical aftertaste is weakly sensitive to grain open porosity epsilon_open and surface-to-volume ratio (1/H), because thinner, more porous cotyledons imbibe slightly more bath liquor per unit mass (+12-18% internal pore citrate in thin Tier 1 grains if over-steeped in Tier 2/3 baths).
- **Evidence Classification:** `LITERATURE_SUPPORTED_AND_MODEL_DERIVED`
- **Evidence References:** `SRC-FLAV-16 (Roland et al., 2017)`, `Khrisanapant et al. (2019)`
- **Model & Code Component:** `SensoryAndFlavourModule & WashingAndResidueModule`
- **Verified Numerical Result:** Over-treating thin mild lots (H = 0.88 mm) in Tier 3 (0.185 M) increases internal pore citrate from 109.7 to 148.5 mg/100g (R_off rises from 0.164 to 0.228).
- **Confidence & Uncertainty:** Moderate confidence; requires multi-lot sensory correlation.
- **Limitations:** Rancid lots with extreme peroxide value (>15 meq O2/kg oil) cannot be fully deodorized by aqueous citrate steeping alone.
- **Downstream Decisions Enabled:** Motivates Tier 1 Mild (0.105 M, 15-18 min) for thin/mild lots to avoid unnecessary reagent uptake, plus an intake peroxide/odor rejection gate.
- **Required Next Action:** Include free fatty acid / hexanal intake screening in EXP-04/EXP-05.

### Q19: Can those attributes be measured reliably at intake?
- **Current Scientific Answer:** Geometry (half-thickness H via 30-grain digital micrometer, SD = 0.035 mm, <2 min) and initial moisture (capacitive dielectric analyzer, SD = 0.35% WB, <1 min) are directly and reliably measurable at the receiving dock. By contrast, bound Ca2+ cannot be directly measured in 5 minutes; the proposed 3-minute 95 C boiling Water Absorption Index (WAI_3min, SD = 1.15%) + leachate conductivity assay is an INDIRECT noisy proxy (yielding 76.0% exact 3-tier classification accuracy and 14.0% false-under-treatment unless uncertainty-buffered thresholds are used).
- **Evidence Classification:** `MODEL_DERIVED_ERROR_ANALYSIS (PROPOSED_DIAGNOSTIC_NOT_YET_FIELD_PROVEN)`
- **Evidence References:** `reports/OMEGA_STAGE3_BATCH_ADAPTATION_REPORT.md`
- **Model & Code Component:** `BatchVariabilityAndAdaptivePolicyModule.evaluate_noisy_intake_diagnostic`
- **Verified Numerical Result:** Direct H & X_wb: high reliability (<3% CV). Noisy WAI_3min proxy for Ca2+: 76.0% raw tier accuracy; requires uncertainty-buffered cutoffs (ADAPTIVE_ROBUST_P95) + 15-min pilot pressure-cook confirmation for borderline/unfamiliar shipments.
- **Confidence & Uncertainty:** Explicitly modeled with realistic measurement noise; zero oracle leakage (FAIL-0022 fixed).
- **Limitations:** The 5-minute WAI_3min proxy is a proposed diagnostic to be calibrated in EXP-04, not a proven industrial sensor.
- **Downstream Decisions Enabled:** Mandates a two-stage intake protocol: 5-min WAI_3min + caliper screen, plus a 15-min laboratory pressure-cook verification on every new container lot (20-25 MT) before full-plant routing.
- **Required Next Action:** Evaluate repeatability and predictive R^2 of the 5-min WAI_3min assay across 10 real lots in EXP-04.

### Q20: How often must the recipe change between batches?
- **Current Scientific Answer:** Because commercial imported pigeon pea arrives in homogeneous 20-25 MT shipping container lots (or 15-30 MT warehouse blends) and plant capacity is 15 MT/day, recipe tier switching occurs at most ONCE per day (or once per 1.3-1.7 operating days per container lot), NOT continuously every 20 minutes. Under our 3-tier adaptive policy across simulated import strata: ~29% of lots run on Tier 1 Mild, ~45% on Tier 2 Standard, and ~26% on Tier 3 Intensive (including 4.7% OOD lots).
- **Evidence Classification:** `OPERATIONAL_ANALYSIS_AND_SIMULATION`
- **Evidence References:** `reports/OMEGA_STAGE3_BATCH_ADAPTATION_REPORT.md`, `docs/specifications/15TPD_FACTORY_SOP_AND_RECIPES.md`
- **Model & Code Component:** `BatchVariabilityAndAdaptivePolicyModule`
- **Verified Numerical Result:** 1 recipe adjustment per 15-25 MT container lot (<= 1 changeover per 20 h operating day, taking ~15 min via automated dosing skid SK-100).
- **Confidence & Uncertainty:** High operational feasibility when lots are blended in a 20 MT intake homogenization silo.
- **Limitations:** If unblended small bags from mixed farms are fed without homogenization, intra-day variability increases.
- **Downstream Decisions Enabled:** Includes a 20 MT raw-grain homogenization surge bin ahead of UAE-101A/B so recipe setpoints remain constant throughout a shift.
- **Required Next Action:** Verify intra-lot vs inter-lot variance in EXP-04.

### Q21: What happens outside the validated batch domain?
- **Current Scientific Answer:** Incoming lots triggering Out-of-Domain (OOD) flags (observed half-thickness H_obs > 1.32 mm [full split > 2.64 mm], initial moisture X_wb < 8.2% WB, estimated bound Ca > 45.0 mol/m^3, or rancid peroxide/odor failure — estimated at 4.7% of imports) are automatically quarantined from standard continuous processing. They are routed to a mandatory laboratory pilot pressure-cook test: if curable by extended Tier 3 conditioning (30 min steep at 57 C, 0.185 M citrate + 15 kPa vacuum pulse), they are processed in dedicated campaign batches; if refractory or rancid, they are rejected or diverted to dry-milled dal flour (besan/dhalia).
- **Evidence Classification:** `GOVERNANCE_AND_CONTROL_POLICY`
- **Evidence References:** `reports/OMEGA_STAGE3_BATCH_ADAPTATION_REPORT.md`
- **Model & Code Component:** `BatchVariabilityAndAdaptivePolicyModule.evaluate_noisy_intake_diagnostic`
- **Verified Numerical Result:** 4.7% OOD flag rate across simulated import distribution; routing OOD lots + buffered cutoffs reduces P95 core force from 20.34 N to 17.68 N.
- **Confidence & Uncertainty:** Prevents silent quality failures on extreme Arusha/Dodoma old-crop shipments.
- **Limitations:** Quarantine routing adds 30 min steeping residence (+6 min over Tier 2), slightly reducing hourly steeping throughput from 750 to ~640 kg/h during OOD campaigns.
- **Downstream Decisions Enabled:** Enforces hard OOD circuit-breaker bounds in factory intake SOP.
- **Required Next Action:** Test extreme aged/thick cotyledon sieve fraction (>2.5 mm) in EXP-04.

### Q22: Which parts of the toor-dal model transfer to other dal species?
- **Current Scientific Answer:** Transferable mathematical structure: (1) 2D axisymmetric conservative Fickian/cavitation diffusion PDE geometry; (2) NIST multi-protic citric acid / carbonate speciation and Davies activity thermodynamics; (3) Two-compartment surface-film vs internal-pore washing equations; and (4) Biot-number shrinkage stress framework. Non-transferable (cannot be copied blindly): species-specific diffusivity D_w(T), bound Ca2+/pectin content, starch gelatinization temperature T_gel, mucilage rheology, and target whistle count.
- **Evidence Classification:** `MECHANISTIC_TRANSFERABILITY_AUDIT`
- **Evidence References:** `SRC-ANCHOR-04 (Perera et al., 2023)`, `reports/OMEGA_STAGE3_BATCH_ADAPTATION_REPORT.md`
- **Model & Code Component:** `BatchVariabilityAndAdaptivePolicyModule.get_multi_species_profiles`
- **Verified Numerical Result:** 4/8 model sub-blocks share universal physics/thermodynamics; 4/8 require species-specific parameter tables.
- **Confidence & Uncertainty:** High scientific confidence; prevents false universal-recipe claims.
- **Limitations:** All non-Cajanus cajan simulations carry `requires_separate_physical_validation = True`.
- **Downstream Decisions Enabled:** Prohibits using the 20-min Toor Tier 2 recipe on Moong, Masoor, Urad, or Chana dal.
- **Required Next Action:** Maintain separate species parameter cards in Module G.

### Q23: What needs to be calibrated separately for each species?
- **Current Scientific Answer:** (1) Chana Dal (Cicer arietinum, 2H = 2.70 mm): high thickness (H^2 is 56% larger than Toor) + high amylose starch (~32%) requires calibrating D_cit(T), DSC gelatinization enthalpy, and extended 28-30 min Tier 3 soaking (20-min Toor soak fails at 19.85 N). (2) Moong Dal (Vigna radiata, 2H = 1.44 mm) & Masoor Dal (Lens culinaris, 2H = 1.30 mm): thin lens geometry and low bound Ca2+ (14-16.5 mol/m^3) require calibrating sloughing/leaching limits for short 8-12 min Tier 1 soaking (1-whistle target). (3) Urad Dal (Vigna mungo, 2H = 1.76 mm): soluble arabinogalactan mucilage hydration and batter-foaming viscosity as a function of citrate ionic strength must be calibrated separately.
- **Evidence Classification:** `MODEL_DERIVED_AND_LITERATURE_SUPPORTED`
- **Evidence References:** `reports/OMEGA_STAGE3_BATCH_ADAPTATION_REPORT.md`, `artifacts/omega_investigation_results.json::stage3_batch_variability.other_dal_species_screening`
- **Model & Code Component:** `BatchVariabilityAndAdaptivePolicyModule`
- **Verified Numerical Result:** Chana (24 min -> 19.85 N FAIL, needs 28-30 min); Moong (12 min -> 14.03 N, 1 wh); Urad (18 min -> 13.83 N, 1 wh); Masoor (12 min -> 13.46 N, 1 wh).
- **Confidence & Uncertainty:** Preliminary screening estimates only; zero wet-lab data on non-toor species in this project.
- **Limitations:** Strictly labeled PROVISIONAL_SCREENING.
- **Downstream Decisions Enabled:** Sequestered from Phase 1 Toor Dal commercial deliverables.
- **Required Next Action:** Execute separate Phase 2 species-extension bench trials after Toor Dal validation.

### Q24: What limits the complete production cycle?
- **Current Scientific Answer:** Across the 11-step industrial route, the primary unit-operation residence-time bottleneck is Step 8: Two-Stage Fluidized-Bed Drying & Adiabatic Tempering (67.0 min total = 22.0 min Zone 1 at 65 C + 20.0 min plug-flow tempering column + 25.0 min Zone 2 at 55 C), representing 65.0% of the 103.0 min processing residence time (or 56.8% of the 118.0 min gate-to-gate batch elapsed time including 15.0 min intake/routing). Pretreatment steeping (20.0-24.0 min + 4.0 min turn-around drain/fill) is de-bottlenecked via two staggered 600 L ultrasonic vessels (UAE-101A/B) discharging every 12-14 min onto the continuous dewatering and drying line.
- **Evidence Classification:** `CALCULATED_PROCESS_SCHEDULING`
- **Evidence References:** `reports/OMEGA_STAGE4_PLANT_CYCLE_AND_ECONOMICS.md`
- **Model & Code Component:** `PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics`
- **Verified Numerical Result:** Active processing residence = 103.0 min (Tier 2) to 107.0 min (Robust 24m Tier 2); Gate-to-gate elapsed time = 118.0-122.0 min; Dryer + Tempering = 67.0 min (bottleneck).
- **Confidence & Uncertainty:** Attempting to shorten the 67.0 min drying + tempering bottleneck by blasting at 85 C (42.0 min) violates the 1.65 MPa tissue yield stress (1.85 MPa) and spikes breakage from 0.35% to 3.19%.
- **Limitations:** Continuous 750 kg/h output requires FBD-103 active bed holdup of 588 kg and TMP-104 tempering silo holdup of 250 kg.
- **Downstream Decisions Enabled:** Sizes FBD-103 and TMP-104 for the full 67.0 min low-stress schedule.
- **Required Next Action:** Verify drying curve and tempering relaxation time in EXP-03.

### Q25: Does the full process meet the 15 TPD design basis?
- **Current Scientific Answer:** YES, when properly sized for yield losses (Part H2 reconciliation): (a) On a 15,000.0 kg/day Raw Feed Basis (750.0 kg/h raw in over 20.0 h/day + 4.0 h CIP), net prime whole-split output after 0.35% net dry-solids leaching and 0.35% broken-grain screening is 14,884.8 kg/day (plus 52.1 kg/day second-grade broken splits). (b) On a 15,000.0 kg/day Net Saleable Prime Output Basis, feeding 15,116.1 kg/day (755.8 kg/h raw dal over 20.0 h/day) into the two staggered 378 kg batch steeping vessels (discharging every 30.0 min per vessel = 15.0 min line cadence) delivers exactly 15,000.0 kg/day of prime packaged dal.
- **Evidence Classification:** `INDEPENDENTLY_REPRODUCED_MASS_BALANCE`
- **Evidence References:** `reports/OMEGA_STAGE4_PLANT_CYCLE_AND_ECONOMICS.md`
- **Model & Code Component:** `PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics`
- **Verified Numerical Result:** Basis I (15,000 kg/d raw feed) -> 14,884.8 kg/d prime out. Basis II (15,000 kg/d prime out) -> 15,116.1 kg/d raw feed (755.8 kg/h).
- **Confidence & Uncertainty:** Exact arithmetic conservation verified to <1e-6% closure error.
- **Limitations:** Assumes 90% OEE during the 20.0 h active operating window (4.0 h daily CIP/maintenance reserve).
- **Downstream Decisions Enabled:** Sizes feed elevators, dosing skids, and dryer blowers for 755.8 kg/h nominal (833 kg/h surge capacity).
- **Required Next Action:** Validate pilot throughput and turnaround drainage times in Stage 4 pilot run.

### Q26: Are all material and energy balances consistent?
- **Current Scientific Answer:** YES. Every stream (raw dry solids, raw moisture, fresh makeup water, recycled steep liquor, sanitary bleed purge, spray wash water, drained wash effluent, Scenario B1 vs B2 dryer water evaporation, leached dry solids, retained buffer ions, broken splits, and finished product moisture) closes with 0.000000% conservation error. The pre-dryer moisture discrepancy between Scenario B1 (28.0% WB -> 3,654.42 kg/day evap) and Scenario B2 (28.7735% WB -> 3,854.14 kg/day evap, +199.72 kg/day water delta, +6.66 kW_th dryer duty) is explicitly preserved across all tables.
- **Evidence Classification:** `INDEPENDENTLY_REPRODUCED_CALCULATION`
- **Evidence References:** `reports/OMEGA_STAGE4_PLANT_CYCLE_AND_ECONOMICS.md`, `tests/test_defect_regressions.py`
- **Model & Code Component:** `PlantOperationsAndEconomicsModule & scripts/handoff.py`
- **Verified Numerical Result:** Dry solids closure error = 0.000000%; Evaporative delta (B2 - B1) = +199.72 kg/day.
- **Confidence & Uncertainty:** Mathematical identity verified by automated pytest suite.
- **Limitations:** Empirical resolution of Scenario B1 vs B2 requires physical dewatering screen measurement.
- **Downstream Decisions Enabled:** Sizes FBD-103 steam heater for Scenario B2 + safety margin (195 kW_th installed).
- **Required Next Action:** Measure drained wet cake moisture in EXP-02.

### Q27: Are reagent consumption and costs reconciled?
- **Current Scientific Answer:** YES (FAIL-0025 fixed). We explicitly separate and reconcile: (1) Once-Through Mode (0% liquor recycle): 22,579 L/day fresh bath requires 569.01 kg/d K3Cit·H2O + 57.32 kg/d Na3Cit·2H2O + 254.58 kg/d Citric Acid = 880.91 kg/day total reagents, costing ₹8.62/kg dal (Total OpEx = ₹11.65/kg). (2) 85% Bleed-and-Feed Recycled Bath Mode (selected industrial design): 85% of drained free liquor is filtered (50 um wedge-wire + UV) and recycled, while fresh makeup (6,649.5 L/d) + chelation replenishment consumes 239.83 kg/d K3Cit·H2O + 24.16 kg/d Na3Cit·2H2O + 107.30 kg/d Citric Acid = 371.29 kg/day total reagents, costing ₹3.63/kg dal (Total OpEx = ₹6.34/kg dal = ₹95,065/day). The unsubstantiated legacy ₹0.42/kg claim is permanently retracted.
- **Evidence Classification:** `INDEPENDENTLY_REPRODUCED_CALCULATION`
- **Evidence References:** `governance/errors/errors.json::FAIL-0025`, `reports/OMEGA_STAGE4_PLANT_CYCLE_AND_ECONOMICS.md`
- **Model & Code Component:** `PlantOperationsAndEconomicsModule.evaluate_15tpd_plant_balance_and_economics`
- **Verified Numerical Result:** Once-Through: 880.91 kg/d (₹8.62/kg reagent, ₹11.65/kg total). 85% Recycle: 371.29 kg/d (₹3.63/kg reagent, ₹6.34/kg total).
- **Confidence & Uncertainty:** Bulk food-grade citrate price sensitivity (+/-12%) shifts total OpEx between ₹5.72/kg and ₹7.15/kg.
- **Limitations:** Assumes 85% recycle loop operates for 5-6 cycles before 15% steady-state bleed controls dissolved solids (<3.2% TDS).
- **Downstream Decisions Enabled:** Replaces contradictory numbers in 15TPD_FACTORY_SOP_AND_RECIPES.md and portal micrositeData.js.
- **Required Next Action:** Obtain formal vendor quotes for 10 MT/month bulk food-grade K3Cit·H2O and H3Cit in India and run 5-cycle reuse test in EXP-02.

### Q28: What are the important food-safety and regulatory requirements?
- **Current Scientific Answer:** Under FSSAI (Food Products Standards and Food Additives) Regulations, 2011 (Regulation 2.4.6.15 for Dehusked Split Arhar/Toor Dal and Appendix A GMP Table): (1) Finished moisture must be <= 14.0% WB (FinnoaQ target <= 11.75% WB); (2) Citric Acid (INS 330), Trisodium Citrate (INS 331iii), Tripotassium Citrate (INS 332ii), and Sodium Bicarbonate (INS 500ii) are permitted GMP food additives; (3) Crucial Labeling Distinction: because ~109.7 mg/100g citrate and ~52 mg/100g K+ remain inside internal cotyledon pores to exert a technical softening effect during household cooking, the product CANNOT be sold as untreated raw commodity dal claiming 'zero retained additive'; it must declare 'Conditioned with Acidity Regulators / Sequestrants (INS 332ii, INS 331iii, INS 330)' on the ingredient label; and (4) Recycled bath liquor at 55 C requires 50 um filtration, UV-C irradiation, 15% continuous sanitary bleed, and daily 4-hour CIP sanitization to prevent thermophilic spore (Bacillus) growth.
- **Evidence Classification:** `OFFICIAL_REGULATORY_SOURCE`
- **Evidence References:** `SRC-REG-19 (FSSAI 2011 Regulations)`, `evidence_vault/regulations/fssai_and_iso_standards.json`
- **Model & Code Component:** `scripts/build_evidence_vault.py::build_regulations_vault`
- **Verified Numerical Result:** FSSAI max moisture = 14.0% WB; INS 330/331/332 permitted under GMP with mandatory ingredient declaration for conditioned dal.
- **Confidence & Uncertainty:** Directly verified against FSSAI regulatory framework.
- **Limitations:** If a client demands 100% clean-label zero-ingredient declaration, only hydrothermal steam conditioning/flaking (Chakraborty et al., 2007) qualifies.
- **Downstream Decisions Enabled:** Mandates transparent ingredient labeling in SOP and HACCP microbial controls on the 85% recycle loop.
- **Required Next Action:** Verify total plate count (TPC) and yeast/mold across 5 consecutive bath reuse cycles in EXP-02.

### Q29: Which claims are supported by calculations and literature alone?
- **Current Scientific Answer:** Supported by calculations and literature without requiring new target-lot wet-lab proof: (1) Exact multi-protic buffer pH stoichiometry in pure water (pH 5.20 for 25.20/2.54/11.28 kg recipe vs pH 6.78 for legacy SOP, FAIL-0024); (2) Falsification of the 4.6-min Vacuum Impregnation claim via Fito (1996) porosity conservation bounds (FAIL-0023); (3) Falsification of the uncoupled 25 C drying stress script and plum citation (FAIL-0021); (4) Reconciliation of once-through (₹8.62/kg) vs 85% recycled (₹3.63/kg) reagent mass and cost balances (FAIL-0025); (5) Existence of large genotype and storage-induced cooking-time variance in East African pigeon pea (26-54 min open boiling, Machinjili et al., 2025); and (6) Mathematical conservation of mass and energy across the 15 TPD flowsheets.
- **Evidence Classification:** `INDEPENDENTLY_REPRODUCED_AND_LITERATURE_SUPPORTED`
- **Evidence References:** `SRC-CHEM-14`, `SRC-VI-15`, `SRC-PIGEON-07`, `SRC-PIGEON-11`, `governance/errors/errors.json`
- **Model & Code Component:** `TreatmentChemistryModule, HydrationAndPenetrationModule, PlantOperationsAndEconomicsModule`
- **Verified Numerical Result:** 6 core mathematical, thermodynamic, and falsification conclusions established from first principles and literature.
- **Confidence & Uncertainty:** 100% reproducible offline via `py -m pytest` and `finnoaq validate`.
- **Limitations:** Calculations prove internal consistency and falsify impossible shortcuts, but do not replace physical product testing.
- **Downstream Decisions Enabled:** Forms the verified Gate 0 / Gate 1 baseline of the OMEGA dossier.
- **Required Next Action:** Proceed to laboratory verification of material-dependent kinetic claims (Q30).

### Q30: Which require laboratory measurements?
- **Current Scientific Answer:** Require laboratory bench measurements (EXP-01, EXP-02, EXP-03, EXP-04): (1) Exact Whistle-2 bulk and core Warner-Bratzler shear force (F_WB,bulk, F_WB,core) of the client's specific Tanzanian lot after 20 min vs 24 min steeping in Pot 4; (2) Calibration of the provisional 18.0 N tenderness threshold against 3-whistle cooked authentic Indian Latur reference dal; (3) Actual bath pH shift caused by dhal solids buffering at 55 C; (4) Actual surface film and internal pore citrate/K+/Na+ retention after a 12 s spray wash; (5) Actual LOX inactivation % and headspace hexanal ppb (SPME-GC-MS); (6) Dewatering screen exit moisture (resolving Scenario B1 28.0% WB vs Scenario B2 28.7735% WB); (7) Fissured/broken grain % after 65 C -> 20m temper -> 55 C drying; and (8) Predictive R^2 of the 5-min WAI_3min intake proxy against EDTA-titrated bound Ca2+ across >=10 commercial lots.
- **Evidence Classification:** `REQUIRES_LABORATORY_MEASUREMENT`
- **Evidence References:** `reports/OMEGA_PHYSICAL_VALIDATION_PLAN.md`
- **Model & Code Component:** `EXP-01 through EXP-04 protocols`
- **Verified Numerical Result:** 8 material-specific claims gated on bench laboratory measurements (Est. budget ₹31,500 across EXP-01 to EXP-04).
- **Confidence & Uncertainty:** Currently held as MODEL_DERIVED hypotheses with quantified 95% prediction intervals.
- **Limitations:** Cannot be upgraded to MEASURED without physical grain samples and wet-lab execution.
- **Downstream Decisions Enabled:** Gates Phase 2 formulation freeze on EXP-01/02/03/04 completion.
- **Required Next Action:** Execute EXP-01 (Monday Bench Trial) immediately upon sample receipt.

### Q31: Which require sensory panels?
- **Current Scientific Answer:** Require human sensory panel testing (EXP-05): (1) Demonstrating SENSORY_NONDETECTION of chemical aftertaste in unspiced pressure-cooked dal slurry (Matrix A) requires a blinded, randomized ISO 4120:2021 Triangle Test with N >= 24 trained/screened panelists; and (2) Demonstrating INDIAN_REFERENCE_EQUIVALENCE in overall liking, aroma, flavour, and mouthfeel against authentic Indian Latur reference dal requires a blinded, 6-sequence Williams Latin Square ISO 11136:2014 Consumer Hedonic Test with N >= 72 regular toor-dal consumers analyzed via Two One-Sided Tests (TOST, Delta = +/-0.75 points on a 9-point scale, alpha = 0.05, power >= 0.90) in both Matrix A (unspiced) and Matrix B (standardized tadka).
- **Evidence Classification:** `REQUIRES_HUMAN_SENSORY_PANEL`
- **Evidence References:** `SRC-ANCHOR-06 (ISO 11136:2014)`, `SRC-STAT-18 (Bi & Meyners, 2012)`
- **Model & Code Component:** `SensoryAndFlavourModule.design_iso_tost_equivalence_study`
- **Verified Numerical Result:** N = 24 trained assessors (ISO 4120 triangle test) + N = 72 naive consumers (ISO 11136 TOST equivalence test).
- **Confidence & Uncertainty:** Statistical power >= 90% at sigma_w = 1.35 and Delta = 0.75.
- **Limitations:** Analytical residue or GC-MS measurements CANNOT substitute for human sensory panel proof.
- **Downstream Decisions Enabled:** Prohibits marketing claims of 'zero aftertaste' or 'identical to Indian Latur dal' until EXP-05 passes.
- **Required Next Action:** Commission accredited sensory laboratory for EXP-05 after EXP-01/02 pass.

### Q32: Which require pilot or plant validation?
- **Current Scientific Answer:** Require Stage 4 pilot/plant validation (100-500 kg/h continuous skid trial): (1) Acoustic cavitation uniformity and standing-wave attenuation across a 600 L jacketed vessel loaded with 375 kg dhal; (2) Continuous vibratory wedge-wire dewatering moisture (Scenario B1 vs B2) and nozzle clogging/overlapping over multi-hour runs; (3) Plug-flow mass-flow discharge without bridging in the 20-minute adiabatic tempering column (TMP-104); (4) Dissolved solids (TDS), protein foaming, and microbiological stability across 5-10 consecutive cycles of 85% steeping liquor recycling; and (5) Steady-state 755.8 kg/h raw feed -> 750.0 kg/h net prime packaged dal throughput and utility consumption.
- **Evidence Classification:** `REQUIRES_PILOT_OR_PLANT_VALIDATION`
- **Evidence References:** `reports/OMEGA_STAGE4_PLANT_CYCLE_AND_ECONOMICS.md`, `reports/OMEGA_PHYSICAL_VALIDATION_PLAN.md`
- **Model & Code Component:** `PlantOperationsAndEconomicsModule`
- **Verified Numerical Result:** 5 scale-up engineering phenomena requiring 100-500 kg/h pilot verification prior to 15 TPD CapEx commitment.
- **Confidence & Uncertainty:** Bench trials (EXP-01 to EXP-04) cannot capture 3D bed compaction or multi-hour recycle fouling.
- **Limitations:** Conceptual FEED drawings (DWG-FIN-15T-001 to 014) and mass balances are design calculations, not commissioned plant receipts.
- **Downstream Decisions Enabled:** Gates Phase 4 equipment fabrication on Phase 3 pilot validation.
- **Required Next Action:** Execute 100 kg pilot trial after bench and sensory gates pass.

### Q33: What experiment would most efficiently reduce the remaining uncertainty?
- **Current Scientific Answer:** EXP-01 (The Turnkey 1-Day Monday Bench Cookability, pH 5.20 Verification & Core-vs-Bulk Shear Trial, Cost ₹3,500, Duration 6 hours) provides the highest Value of Information (VoI) per Rupee and hour. By testing 5 pots in parallel (Pot 1 Untreated Tanzanian Control, Pot 2 55 C Water Control, Pot 3 0.5% NaHCO3 Control, Pot 4 Corrected pH 5.20 90:10 K/Na Citrate + 40 kHz UAE sampled at 15, 20, and 24 min, and Pot 5 Indian Latur Reference), it simultaneously tests the core Stage 1 hypothesis (<= 2 whistles), calibrates the 18.0 N threshold against Indian reference dal, verifies bath pH 5.20 at 55 C, and performs an immediate blind triangle taste screen on the washed cooked slurry.
- **Evidence Classification:** `BAYESIAN_VOI_RANKED_EXPERIMENT`
- **Evidence References:** `reports/OMEGA_PHYSICAL_VALIDATION_PLAN.md`, `docs/specifications/MONDAY_BENCH_TRIAL_PROTOCOL.md`
- **Model & Code Component:** `ExperimentDesignAndValidationModule`
- **Verified Numerical Result:** Reduces Stage 1/2 feasibility uncertainty by >75% for ₹3,500 in 1 day.
- **Confidence & Uncertainty:** Includes both positive/negative controls and falsification criteria.
- **Limitations:** Requires 3.0 kg authentic aged Tanzanian split dhal and 1.0 kg fresh Indian Latur reference dhal.
- **Downstream Decisions Enabled:** Immediate go/no-go gate for all downstream experiments (EXP-02 to EXP-05).
- **Required Next Action:** Execute EXP-01 following docs/specifications/MONDAY_BENCH_TRIAL_PROTOCOL.md.

### Q34: What evidence is necessary before stating a commercial guarantee?
- **Current Scientific Answer:** Before FinnoaQ can issue a legally and scientifically binding commercial performance guarantee for a 15 TPD plant, five cumulative evidence gates must transition from MODEL_DERIVED to MEASURED: (1) EXP-01/03 confirmation that treated dhal achieves <= 2 whistles and <0.5% dryer breakage with 95% confidence; (2) EXP-05 accredited sensory certificate proving ISO 4120 aftertaste nondetection (N=24) and ISO 11136 TOST equivalence (N=72, 90% CI within [-0.75, +0.75]) against Indian reference dal; (3) EXP-04 multi-lot validation across >=10 independent commercial shipments demonstrating >=95% pass rate under the uncertainty-buffered adaptive intake policy; (4) 6-month accelerated (40 C / 75% RH) and real-time shelf-life stability certificates confirming no secondary re-hardening or rancidity; and (5) A continuous 72-hour pilot/demonstration run verifying 85% liquor recycle hygiene, effluent COD/TDS compliance, and ₹6.34/kg (+/-15%) operating cost.
- **Evidence Classification:** `GOVERNANCE_ACCEPTANCE_CRITERION`
- **Evidence References:** `AGENTS.md`, `reports/OMEGA_FINAL_VERIFICATION_REPORT.md`
- **Model & Code Component:** `Gate 0-4 Sequential Evidence Framework`
- **Verified Numerical Result:** 5 mandatory physical validation certificates required prior to commercial guarantee.
- **Confidence & Uncertainty:** Zero exceptions permitted under AGENTS.md Rule 1.
- **Limitations:** Until all 5 certificates are on file, all performance figures must be presented as calibrated engineering predictions.
- **Downstream Decisions Enabled:** Governs commercial contract warranty terms for Phase 3/4.
- **Required Next Action:** Complete Phase 1 diagnostic and bench validation (EXP-01 to EXP-05).

### Q35: Which claims on the website need correction, downgrading, or removal?
- **Current Scientific Answer:** Six legacy website claims in `toor_dal_optimization/portal/src/data/micrositeData.js` were audited and corrected/downgraded: (1) Removed fabricated consumer hedonic scores (`8.8`, `8.7`, `8.9`) -> replaced with model-predicted `d'=0.22 (TOST Pending)` (`FAIL-0023`); (2) Removed `TECH-VI-01` (4.6-min Vacuum Impregnation) from the winner list -> downgraded to `FALSIFIED_BY_OMEGA_FAIL_0023 (5.2% Core Ca, 7 wh)`; (3) Corrected unsubstantiated `₹0.23/kg` and `₹0.43/kg` OpEx claims -> replaced with audited `₹6.34/kg (85% Recycle)` vs `₹11.65/kg (Once-Through)` (`FAIL-0025`); (4) Corrected legacy Tier 2 citrate recipe -> updated to exact pH 5.20 stoichiometry (`25.20 kg K3Cit·H2O + 2.54 kg Na3Cit·2H2O + 11.28 kg Citric Acid / 1000L`, `FAIL-0024`); (5) Corrected `DR-101` dryer description from `85 C / 75 C` (`FAIL-0021`) -> updated to Two-Stage `65 C (22m) -> 20m Tempering -> 55 C (25m)` keeping stress at `0.71 MPa < 1.65 MPa`; and (6) Downgraded Stage 3 `100.0%` oracle pass rates (`FAIL-0022`) -> replaced with honest `SIMULATION_CONDITIONAL` noisy intake proxy results (`78.0% baseline / 96.2% uncertainty-buffered robust policy`).
- **Evidence Classification:** `VERIFIED_PORTAL_REMEDIATION`
- **Evidence References:** `toor_dal_optimization/portal/src/data/micrositeData.js`, `governance/errors/errors.json::FAIL-0021..0026`
- **Model & Code Component:** `finnoaq website check`
- **Verified Numerical Result:** 6/6 legacy overclaims corrected and verified in compiled `toor_dal_optimization/portal/dist/` bundle.
- **Confidence & Uncertainty:** Verified automatically by `finnoaq website check` CLI subcommand.
- **Limitations:** Portal must be re-verified whenever simulation artifacts are updated.
- **Downstream Decisions Enabled:** Ensures public-facing client portal strictly obeys the evidence ledger.
- **Required Next Action:** Run `finnoaq website check` as part of final pre-response verification.

