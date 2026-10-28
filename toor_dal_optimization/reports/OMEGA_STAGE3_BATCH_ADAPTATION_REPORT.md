# FINNOAQ OMEGA — STAGE 3 BATCH VARIABILITY, NOISY INTAKE ADAPTATION & MULTI-SPECIES EXTENSION REPORT
**Project Ref:** `FNQ-PR-2026-001` | **System:** `FINNOAQ OMEGA (Offline-First Scientific Engineering & Proof System)`  
**Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Date:** October 28, 2026 | **Verification Status:** `MODEL_DERIVED` + `LITERATURE_SUPPORTED` (Pending Multi-Lot Physical Intake Calibration)

---

## 1. Executive Summary & Stage 3 Objectives

Stage 3 of the FinnoaQ OMEGA investigation evaluates how the validated Stage 1/Stage 2 process (`90:10 K/Na Citrate Buffer at pH 5.20 + 17 W/L UAE + 12 s Dual-Fan Spray Wash`) performs across **genuine industrial feedstock variability** (growing region, cultivar seed size, post-harvest storage age/temperature/humidity, initial moisture, and middle-lamellar bound $\text{Ca}^{2+}$) and answers two critical questions:

1. **Can a realistic, noisy 5-minute factory intake diagnostic test classify incoming pigeon pea shipments into adaptive treatment tiers (`Tier 1 Mild`, `Tier 2 Standard`, `Tier 3 Intensive`) without cheating by reading ground-truth bound $\text{Ca}^{2+}$ directly?**
2. **How does the biophysical reaction-diffusion mechanism extend to other commercially important Indian split pulses (`Chana Dal`, `Moong Dal`, `Urad Dal`, and `Masoor Dal`), and what separate species-specific validation is required?**

### Key Stage 3 Findings
1. **Remediation of Defect `FAIL-0022` (Oracle Leakage & Missing Geometry Coupling):**
   - The legacy script (`simulate_feedstock_variability.py`) omitted `thickness_mm` and `moisture_wb_pct` from its Stage 3 solver call and used exact ground-truth bound $\text{Ca}^{2+}$ inside the adaptive selector ("oracle leakage"), falsely claiming $100\%$ classification accuracy and $100\%$ pass rate.
   - In `BatchVariabilityAndAdaptivePolicyModule` (`src/finnoaq/omega_modules.py`), our 5-minute rapid intake diagnostic uses **only noisy physical measurements** achievable at a receiving dock:
     - Digital micrometer caliper thickness ($N=30$ split cotyledons, measurement noise $\sigma_H = 0.035\,\text{mm}$).
     - Capacitive moisture meter ($\sigma_{X} = 0.35\%\text{ WB}$).
     - $3.0\,\text{min}$ boiling-water gravimetric Water Absorption Index ($\text{WAI}_{3\text{min}}$ at $95^\circ\text{C}$, noise $\sigma_{\text{WAI}} = 1.15\%$) plus leachate electrical conductivity / turbidity proxy ($\sigma_{\text{Ca,proxy}} = 2.1\,\text{mol/m}^3$).
2. **Monte Carlo Comparison Across $N = 150$ Stratified Import Batches (`artifacts/omega_investigation_results.json`):**
   - **Untreated Control:** $0.0\%$ pass rate at 2 whistles across all Tanzanian/East African import strata ($F_{\text{WB,core}}$ mean $= 25.4\,\text{N}$, $6\text{–}9$ whistles required).
   - **Fixed Single-Tier Policy (Tier 2 applied blindly to all 150 lots):** Achieves **$76.7\%$ two-whistle pass rate** (mean $F_{\text{WB,core}} = 16.40\,\text{N}$, 95th percentile $P_{95} = 20.84\,\text{N}$), failing on thick, severely aged Arusha/Dodoma lots ($2H > 2.25\,\text{mm}$, $C_{\text{Ca,0}} > 36\,\text{mol/m}^3$) while over-treating mild/fresh lots.
   - **Noisy 5-Minute Intake Proxy Adaptive Policy (`Tier 1` / `Tier 2` / `Tier 3`):** Achieves **$76.0\%$ tier-classification accuracy** against the true underlying biophysical severity index ($S_{\text{HTC}} = C_{\text{Ca,0}} \cdot (H / 1.0\,\text{mm})^{1.35}$), with a **$14.0\%$ false-under-treatment rate**, **$10.0\%$ false-over-treatment rate**, and **$4.7\%$ Out-of-Domain (OOD) quarantine flag rate** for extreme lots ($H > 1.32\,\text{mm}$, $X_{\text{wb}} < 8.2\%$, or $\hat{C}_{\text{Ca}} > 45\,\text{mol/m}^3$). It improves the overall 2-whistle pass rate to **$78.0\%$** (and **$89.3\%$** when OOD-flagged lots are routed to Tier 3 + extended $30\,\text{min}$ soak), reduces 95th-percentile core shear force to **$20.34\,\text{N}$**, and saves $27.6\%$ reagent on the $44/150$ batches assigned to `Tier 1 Mild`.

---

## 2. Reference Cultivar & Storage-History Characterization (`Module A`)

Five canonical reference profiles were parameterized from published literature (`Tiwari & Singh, 2012`; `Nisha et al., 2006`; `Perera et al., 2023`; `Ohanenye et al., 2024`) to anchor the 150-batch Monte Carlo distribution:

### Table 2.1: Canonical Pigeon Pea Reference Profiles (`FeedstockCharacterizationModule`)

| Profile ID | Origin & Cultivar Type | Full Split Thickness $2H$ ($\text{mm}$) | Half-Thickness $H$ ($\text{mm}$) | Initial Moisture ($\%\text{ WB}$) | Storage History | Bound $\text{Ca}^{2+}$ ($\text{mol/m}^3$) | Pectin $DE$ Fraction | Native Whistles ($t_{90}$) |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **`INDIAN_LATUR_FRESH_REF`** | Maharashtra (Latur/Akola) Small-Seeded *Desi* | $1.70$ | $0.85$ | $10.8\%$ | $2\,\text{mo}$ at $25^\circ\text{C}, 55\%\text{ RH}$ | $14.0$ | $0.52$ | $3\text{ whistles}$ ($9.8\,\text{min}$) |
| **`INDIAN_MP_MODERATE`** | Madhya Pradesh Medium-Seeded | $1.88$ | $0.94$ | $10.2\%$ | $5\,\text{mo}$ at $28^\circ\text{C}, 62\%\text{ RH}$ | $21.5$ | $0.42$ | $5\text{ whistles}$ ($12.9\,\text{min}$) |
| **`TANZANIAN_MODERATE_FRESH`** | Tanzania (`ICEAP 00040` / Babati) Early Shipment | $1.96$ | $0.98$ | $10.4\%$ | $4\,\text{mo}$ at $27^\circ\text{C}, 65\%\text{ RH}$ | $23.5$ | $0.38$ | $5\text{ whistles}$ ($13.8\,\text{min}$) |
| **`TANZANIAN_HTC_AGED_NOMINAL`** | Tanzania (`ICEAP 00040`) Aged Maritime Lot | $2.16$ | $1.08$ | $9.8\%$ | $9\,\text{mo}$ at $31^\circ\text{C}, 76\%\text{ RH}$ | $33.5$ | $0.28$ | $8\text{ whistles}$ ($17.3\,\text{min}$) |
| **`TANZANIAN_SEVERE_ARUSHA_HTC`** | Arusha/Dodoma Bold Late-Season Aged Lot | $2.44$ | $1.22$ | $8.9\%$ | $14\,\text{mo}$ at $33^\circ\text{C}, 80\%\text{ RH}$ | $42.0$ | $0.21$ | $9\text{ whistles}$ ($20.6\,\text{min}$) |

---

## 3. Adaptive Intake Diagnostic & 3-Tier Policy Architecture (`Module G`)

### 3.1 The 5-Minute Receiving Dock Diagnostic Protocol
For every incoming $20\text{–}25\,\text{MT}$ container lot, QA executes a $5.0\,\text{min}$ rapid test before charging the soaking surge hopper:
1. **Caliper Half-Thickness ($\hat{H}$):** Measure 30 randomly sampled split cotyledons with a digital micrometer ($\hat{H} = H_{\text{true}} + \epsilon_H$, $\sigma_H = 0.035\,\text{mm}$).
2. **Dielectric Moisture ($\hat{X}_{\text{wb}}$):** Measure $250\,\text{g}$ sample in a calibrated capacitive moisture analyzer ($\sigma_X = 0.35\%\text{ WB}$).
3. **3-Minute Thermal Water Absorption Index ($\widehat{\text{WAI}}_{3\text{min}}$) & Leachate Proxy:** Immerse $50.0\,\text{g}$ split dhal in $250\,\text{mL}$ boiling deionized water ($95^\circ\text{C}$) for $180\,\text{s}$, drain $30\,\text{s}$ on a 20-mesh screen, and weigh mass gain ($\widehat{\text{WAI}}_{3\text{min}} = \frac{m_{\text{wet}} - 50.0}{50.0} \times 100\%$). Because $\text{Ca}^{2+}$-pectate cross-linking restricts cell-wall swelling and middle-lamellar water transport, $\text{WAI}_{3\text{min}}$ is inversely correlated with both $H^{0.85}$ and $C_{\text{Ca,0}}$:
   $$\text{WAI}_{3\text{min,true}} = 24.0 \left(\frac{1.0\,\text{mm}}{H_{\text{mm}}}\right)^{0.85} \left[1 - 0.0095 \left(C_{\text{Ca,0}} - 12.8\right)\right]$$
   Inverting $\widehat{\text{WAI}}_{3\text{min}}$ alongside leachate conductivity yields the noisy bound-calcium estimate $\hat{C}_{\text{Ca}}$ ($\sigma \approx 2.1\,\text{mol/m}^3$) and the observed **HTC Severity Index**:
   $$\hat{S}_{\text{HTC}} = \hat{C}_{\text{Ca}} \cdot \left(\frac{\hat{H}}{1.0\,\text{mm}}\right)^{1.35}$$

### 3.2 Adaptive Tier Assignment Rules & Verified Recipes

| Assigned Tier | Severity Index Trigger ($\hat{S}_{\text{HTC}}$) | Citrate Molarity & Verified pH | Verified Recipe per $1000\,\text{L}$ Water ($\text{K}_3\text{Cit}\cdot\text{H}_2\text{O}$ / $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O}$ / Citric Acid) | Operating Conditions ($T_{\text{soak}}, t_{\text{soak}}, I_{\text{US}}, P_{\text{vac}}$) | Lot Distribution ($N=150$) |
| :--- | :---: | :---: | :--- | :--- | :---: |
| **`TIER_1_MILD`** | $\hat{S}_{\text{HTC}} < 29.0$ | $0.105\,\text{M}$, $\text{pH } 5.30$ | $18.85\,\text{kg}$ / $1.90\,\text{kg}$ / $7.77\,\text{kg}$ | $52.0^\circ\text{C}$, $15.0\,\text{min}$, $17\,\text{W/L}$ UAE, Atmospheric | $44\text{ lots}$ ($29.3\%$) |
| **`TIER_2_STANDARD`** | $29.0 \le \hat{S}_{\text{HTC}} \le 42.5$ | $0.145\,\text{M}$, $\text{pH } 5.20$ | $25.20\,\text{kg}$ / $2.54\,\text{kg}$ / $11.28\,\text{kg}$ | $55.0^\circ\text{C}$, $20.0\,\text{min}$, $17\,\text{W/L}$ UAE, Atmospheric | $68\text{ lots}$ ($45.3\%$) |
| **`TIER_3_INTENSIVE`** | $\hat{S}_{\text{HTC}} > 42.5$ | $0.185\,\text{M}$, $\text{pH } 5.20$ | $32.15\,\text{kg}$ / $3.24\,\text{kg}$ / $14.39\,\text{kg}$ | $57.0^\circ\text{C}$, $26.0\,\text{min}$, $17\,\text{W/L}$ UAE + $15\,\text{kPa}$ Vacuum Pulse | $38\text{ lots}$ ($25.3\%$) |
| **`OOD_QUARANTINE`** | $\hat{H} > 1.32\,\text{mm}$ or $\hat{X}_{\text{wb}} < 8.2\%$ or $\hat{C}_{\text{Ca}} > 45.0$ | Hold for Lab Pilot Cook | Route to Tier 3 + $30\,\text{min}$ soak or blend $50:50$ with Tier 1 lot | Flagged automatically by intake software | $7\text{ lots}$ ($4.7\%$) |

---

## 4. Monte Carlo Robustness & Error-Rate Evaluation ($N = 150$ Batches)

### Table 4.1: Fixed Single-Tier vs. Noisy Adaptive Policy Performance (`artifacts/omega_investigation_results.json`)

| Metric | Untreated Control | Fixed Single-Tier Policy (`TIER_2` on All Lots) | Noisy 5-Min Intake Proxy Adaptive Policy | Engineering Interpretation |
| :--- | :---: | :---: | :---: | :--- |
| **Batches Evaluated ($N$)** | $150$ | $150$ | $150$ | Stratified across Moderate ($25\%$), Nominal Aged ($55\%$), and Severe HTC ($20\%$) imports |
| **2-Whistle Pass Rate ($F_{\text{WB,core}} \le 18.0\,\text{N}$)** | $0.0\%$ | $76.7\%$ | **$78.0\%$** ($89.3\%$ with OOD hold) | Adaptive policy rescues severe HTC lots via Tier 3 ($26\,\text{min}$ + VI) while avoiding oracle leakage |
| **Mean Core Shear Force at Whistle 2 ($\text{N}$)** | $25.41\,\text{N}$ | $16.40\,\text{N}$ | **$16.34\,\text{N}$** | Comfortably below the $18.0\,\text{N}$ tenderness gate |
| **95th Percentile ($P_{95}$) Core Shear Force ($\text{N}$)** | $28.15\,\text{N}$ | $20.84\,\text{N}$ | **$20.34\,\text{N}$** | Tail risk reduced by $0.50\,\text{N}$ despite realistic intake sensor noise |
| **Intake Classifier Accuracy ($\%$)** | N/A | N/A | **$76.0\%$** | Honest noisy proxy accuracy (vs fake $100\%$ in legacy `FAIL-0022`) |
| **False Under-Treatment Rate ($\%$)** | N/A | $20.0\%$ (Severe lots in Tier 2) | **$14.0\%$** | Borderline Tier 2/3 or Tier 1/2 lots misclassified one tier lower due to $\sigma_{\text{WAI}}$ noise |
| **False Over-Treatment Rate ($\%$)** | N/A | $25.0\%$ (Mild lots in Tier 2) | **$10.0\%$** | Borderline lots assigned one tier higher; causes $+0.12\%$ leaching loss but zero sensory failure |
| **Out-of-Domain (OOD) Flagged Lots ($\%$)** | N/A | $0.0\%$ (Unmonitored) | **$4.7\%$** ($7/150$ lots) | Extreme Arusha lots ($2H > 2.64\,\text{mm}$) caught before entering standard soaking |

### 4.2 Diagnosis and Resolution of the Baseline $P_{95} = 20.34\,\text{N}$ ($> 18.0\,\text{N}$) Mismatch (`ADAPTIVE_ROBUST_P95` Policy)
Per **Part G2**, we audited why the baseline noisy adaptive policy (`ADAPTIVE_NOISY_STANDARD`) exhibits a 95th-percentile core shear force of **$P_{95} = 20.34\,\text{N}$** ($> 18.0\,\text{N}$) on the 150-batch CPU sample (and $19.06\,\text{N}$ across $10,000$ 2D-PDE GPU batches):
1. **Mathematical Identity:** By definition, the 95th percentile ($P_{95}$) is exceeded by $5\%$ of all batches. Therefore, **any policy whose overall pass rate is $< 95\%$** (such as `ADAPTIVE_NOISY_STANDARD` at $78.0\%$ CPU / $85.11\%$ GPU pass rate, where $14.9\text{–}22.0\%$ of batches exceed $18.0\,\text{N}$) **must mathematically have $P_{95}(F_{\text{WB,core}}) > 18.0\,\text{N}$**!
2. **Physical Root Cause:** In `ADAPTIVE_NOISY_STANDARD`, using unbuffered intake severity cutoffs ($[28.0, 42.0]$) under $\text{WAI}_{3\text{min}}$ measurement noise ($\sigma_{\text{WAI}} = 1.15\%$) causes false-under-treatment of borderline severe batches (e.g., a true Tier 3 batch with $S_{\text{HTC}} = 43.2$ misclassified as Tier 2 and steeped for only $20.0\,\text{min}$), compounded by the narrow $0.65\,\text{N}$ nominal margin at $20.0\,\text{min}$.
3. **Engineering Solution (`ADAPTIVE_ROBUST_P95`):** We designed and verified an **Uncertainty-Buffered Robust Adaptive Policy (`ADAPTIVE_ROBUST_P95`)** across **$N = 10,000$ full 2D-PDE batches on `NVIDIA GeForce RTX 4050 Laptop GPU`** (`artifacts/omega_gpu_uncertainty_campaign.json`):
   - **Conservative Intake Cutoffs:** Shift severity thresholds downward by $\sim 1.28\,\sigma_{\text{proxy}}$ from $[28.0, 42.0]$ to **$[24.0, 35.5]$**, asymmetrically penalizing false-under-treatment over conservative over-treatment.
   - **Uncertainty-Buffered Steeping Durations:** Increase tier soak times from $[15, 20, 26]\,\text{min}$ to **$[18, 24, 30]\,\text{min}$** (plus $34\,\text{min}$ at $57^\circ\text{C}$, $0.195\,\text{M}$ for OOD-flagged lots).

#### Table 4.2: GPU 10,000-Batch 2D-PDE Policy Comparison (`artifacts/omega_gpu_uncertainty_campaign.json` — All Pass Rates `SIMULATION_CONDITIONAL`)

| Policy Identifier | Batches ($N$) | Simulation-Conditional Pass Rate ($\le 18.0\,\text{N}$) | Mean $F_{\text{WB,core}}$ $\pm$ SD ($\text{N}$) | Median $F_{\text{WB,core}}$ ($\text{N}$) | $P_{90}$ $F_{\text{WB,core}}$ ($\text{N}$) | **$P_{95}$ $F_{\text{WB,core}}$ ($\text{N}$)** | $P_{99}$ $F_{\text{WB,core}}$ ($\text{N}$) | False Under-Treatment ($\%$) | Conservative Over-Treatment ($\%$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`UNTREATED_CONTROL`** | $10,000$ | $0.00\%$ | $25.57 \pm 1.42$ | $26.16$ | $26.90$ | **$27.04$** | $27.22$ | N/A | N/A |
| **`FIXED_TIER2_20MIN`** | $10,000$ | $72.31\%$ | $16.35 \pm 3.08$ | $15.61$ | $21.13$ | **$22.56$** | $23.79$ | $24.80\%$ | $40.00\%$ |
| **`ADAPTIVE_NOISY_STANDARD`** | $10,000$ | $85.11\%$ ($78.0\%$ CPU) | $15.95 \pm 1.81$ | $15.69$ | $18.43$ | **$19.06$** ($20.34$ CPU) | $20.48$ | $3.80\%$ ($14.0\%$ CPU) | $4.43\%$ |
| **`ADAPTIVE_ROBUST_P95`** | **$10,000$** | **$99.90\%$** | **$13.75 \pm 0.89$** | **$13.29$** | **$15.24$** | **$15.77 \le 18.0\,\text{N}$** | **$16.64 \le 18.0\,\text{N}$** | **$0.14\%$** | **$24.17\%$** |

> **Governance Label:** Every pass rate in Tables 4.1 and 4.2 is strictly **`SIMULATION_CONDITIONAL`** (conditional on synthetic batch distributions and noisy $\text{WAI}_{3\text{min}}$ proxy parameters) until calibrated across $\ge 10$ physical commercial shipments in `EXP-04`.

---

## 5. Multi-Species Extension Screening (`Chana`, `Moong`, `Urad`, `Masoor`)

In compliance with **Section 9** of the FinnoaQ OMEGA instructions, we evaluated four additional commercially important Indian split pulse species in `BatchVariabilityAndAdaptivePolicyModule` using species-specific cotyledon geometry and cell-wall calcium/pectin parameters. **Crucial Epistemic Rule:** None of these species may be deployed commercially using the Toor Dal recipe without separate physical validation, because their starch gelatinization temperatures, mucilage content, and seed geometry differ substantially from *Cajanus cajan*.

### Table 5.1: Multi-Species Mechanistic Screening Results (`artifacts/omega_investigation_results.json`)

| Species Key | Botanical & Common Name | Split Cotyledon Thickness $2H$ ($\text{mm}$) | Native Bound $\text{Ca}^{2+}$ ($\text{mol/m}^3$) | Recommended Soak Time at $55^\circ\text{C}$ ($\text{min}$) | Predicted Core $\text{Ca}^{2+}$ Disp. ($\%$) | Predicted Whistles ($t_{90}$) | Predicted $F_{\text{WB,core}}$ at $W=2$ ($\text{N}$) | Species-Specific Biophysical Risks & Validation Requirements |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`CHANA_DAL`** | *Cicer arietinum* (Split Chickpea / Chana Dal) | $2.70\,\text{mm}$ ($H=1.35\,\text{mm}$) | $38.0$ | $24.0\,\text{min}$ (needs Tier 3 $28\text{–}30\,\text{min}$) | $67.2\%$ | $2\text{–}3$ | **$19.85\,\text{N}$** (Borderline at $W=2$) | **High thickness ($H^2$ is $56\%$ larger than Toor) + high amylose starch ($32\%$).** Requires $28\text{–}30\,\text{min}$ Tier 3 steeping + separate DSC gelatinization validation. |
| **`MOONG_DAL`** | *Vigna radiata* (Split Yellow Moong Dal) | $1.44\,\text{mm}$ ($H=0.72\,\text{mm}$) | $16.5$ | **$12.0\,\text{min}$** (Tier 1 Mild) | $91.5\%$ | **$1$** | **$14.03\,\text{N}$** | **Fast-hydrating thin cotyledon.** Applying Toor Tier 2 ($20\,\text{min}$) causes structural sloughing and $>1.5\%$ solid leaching loss. Must cap at $10\text{–}12\,\text{min}$ Tier 1. |
| **`URAD_DAL`** | *Vigna mungo* (Split White Urad Dal) | $1.76\,\text{mm}$ ($H=0.88\,\text{mm}$) | $26.0$ | **$18.0\,\text{min}$** (Tier 1/2) | $96.3\%$ | **$1$** | **$13.83\,\text{N}$** | **Contains soluble arabinogalactan mucilage Matrix.** Citrate chelation accelerates softening ($1\text{ whistle}$), but mucilage viscosity must be validated for idli/dosa batter leavening vs cooked dal use. |
| **`MASOOR_DAL`** | *Lens culinaris* (Split Red Lentil / Masoor Dal) | $1.30\,\text{mm}$ ($H=0.65\,\text{mm}$) | $14.0$ | **$12.0\,\text{min}$** (Tier 1 Mild) | $96.0\%$ | **$1$** | **$13.46\,\text{N}$** | **Extremely thin lens geometry ($H=0.65\,\text{mm}$).** Naturally cooks in $1\text{–}2$ whistles; requires only mild $8\text{–}12\,\text{min}$ conditioning for aged lots to prevent mushy disintegration. |

