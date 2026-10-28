# FINNOAQ OMEGA — STAGE 2 AFTERTASTE MINIMIZATION, FLAVOUR EQUIVALENCE & WASHING STUDY
**Project Ref:** `FNQ-PR-2026-001` | **System:** `FINNOAQ OMEGA (Offline-First Scientific Engineering & Proof System)`  
**Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Date:** October 28, 2026 | **Verification Status:** `MODEL_DERIVED` + `LITERATURE_SUPPORTED` (Sensory Hedonics `NOT_VERIFIED` — Pending ISO 11136:2014 Consumer Panel)

---

## 1. Executive Summary & Stage 2 Objectives

Stage 2 of the FinnoaQ OMEGA investigation answers two coupled chemical-engineering and sensory science questions without sacrificing the Stage 1 two-whistle cookability benefit:
1. **How do we eliminate the detectable soapy/alkaline/metallic aftertaste of chemically treated dal while minimizing post-soak washing time and water consumption?**
2. **How do we suppress grassy/beany lipid-oxidation off-notes in aged East African pigeon pea so that its flavour approaches authentic Indian reference toor dal under a statistically rigorous consumer equivalence test (`ISO 11136:2014`)?**

### Key Scientific & Engineering Findings
1. **Correction of Two Legacy Repository Defects (`FAIL-0023` & `FAIL-0024`):**
   - **Defect `FAIL-0023` (Surface Film vs. Internal Pore Solute Retention):** The legacy script (`simulate_pretreatment.py`) hardcoded `"10.0 seconds"` spray wash and `"45.0 ppm"` residual solute while ignoring internal cotyledon pore solute retention, and fabricated fake consumer hedonic ratings (`8.8/9.0`). In reality, while a $12.0\,\text{s}$ dual-fan high-pressure spray wash ($0.50\,\text{L/kg}$) strips **$98.7\%$ of the external adhering liquid film** (reducing surface film residue from $1755.6\,\text{ppm}$ to **$23.3\,\text{ppm}$**), the internal open pores ($\varepsilon_{\text{hydrated}} \approx 0.18\,\text{L/kg}$) retain dissolved citrate and potassium/sodium ions that equilibrate into the cooking water ($1:3.5$ dal-to-water slurry).
   - **Defect `FAIL-0024` (Buffer Stoichiometry & pH Drift):** The legacy SOP Tier 2 recipe ($33.8\,\text{kg}$ $\text{K}_3\text{Cit}\cdot\text{H}_2\text{O} + 3.7\,\text{kg}$ $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O} + 2.5\,\text{kg}$ anhydrous citric acid per $1000\,\text{L}$) claimed $\text{pH } 5.20$, but exact multi-protic electroneutrality calculation ($\text{p}K_{a1}=3.13, \text{p}K_{a2}=4.76, \text{p}K_{a3}=6.40$ with Davies activity correction $I \approx 0.48\,\text{M}$) proves that ratio equilibrates at **$\text{pH } 6.78$** (and Bench Pot 4 at **$\text{pH } 5.91$**). At $\text{pH } 6.78$, soybean/legume Type-1 Lipoxygenase (`LOX-1`, optimum $\text{pH } 6.5\text{–}7.0$) remains maximally active during warm steeping! We corrected the Tier 2 stoichiometry to **$25.20\,\text{kg}$ $\text{K}_3\text{Cit}\cdot\text{H}_2\text{O} + 2.54\,\text{kg}$ $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O} + 11.28\,\text{kg}$ anhydrous citric acid per $1000\,\text{L}$**, which rigorously locks bath pH at **$\text{pH } 5.20$**.
2. **Why `S2-10-WINNER` (90:10 $\text{K}^+/\text{Na}^+$ Citrate at Verified $\text{pH } 5.20$ + $12\,\text{s}$ Dual-Fan Spray Wash) Wins Stage 2:**
   - Even after accounting for internal pore solute equilibration into the cooked dal slurry, the maximum off-taste threshold ratio in the cooked slurry is **$R_{\text{off}} = 0.164$** ($16.4\%$ of the human sensory detection threshold, yielding a Thurstonian discrimination index **$d' = 0.22 \ll 1.0$**).
   - By contrast, $0.5\%\text{ NaHCO}_3$ (`S2-02`) leaves carbonate/bicarbonate alkaline soapy residue above threshold even after high-pressure spray washing ($R_{\text{off}} = 1.104$, $d' = 2.14$), and an acidic citric-acid quench after $\text{NaHCO}_3$ (`S2-03`) re-protonates $\text{CO}_2$ while cooling/acidifying the outer shell in a way that fails to suppress hexanal ($73.9\,\text{ppb}$, $d' = 2.71$).
   - Crucially, **100% $\text{Na}_3\text{Cit}$ (`S2-04`) fails the 2-whistle core tenderness gate** ($F_{\text{WB,core}} = 18.85\,\text{N} > 18.0\,\text{N}$) because $\text{Na}^+$ has a larger hydrated Stokes radius ($3.58\,\text{\AA}$) and lower ionic mobility ($D_{\text{Na}^+} = 1.33 \times 10^{-9}\,\text{m}^2/\text{s}$) than $\text{K}^+$ ($r_{\text{Stokes}} = 2.32\,\text{\AA}$, $D_{\text{K}^+} = 1.96 \times 10^{-9}\,\text{m}^2/\text{s}$). Replacing $90\%$ of $\text{Na}^+$ with $\text{K}^+$ accelerates electro-neutral co-diffusion of $\text{HCit}^{2-}/\text{Cit}^{3-}$ into the cotyledon core ($F_{\text{WB,core}} = 17.35\,\text{N}$) while simultaneously reducing finished-product sodium by $89.5\%$ ($3.4\,\text{mg Na}/100\text{ g}$ vs $32.5\,\text{mg Na}/100\text{ g}$).

---

## 2. Exact Multi-Protic Buffer Stoichiometry Audit (`FAIL-0024` Remediation)

To prevent both alkaline saponification ($\text{pH} > 7.5$) and isoelectric protein precipitation of pigeon pea 7S vicilin ($\text{pI} \approx 4.5\text{–}4.7$), the steeping bath must operate strictly at **$\text{pH } 5.20 \pm 0.05$**. At $\text{pH } 5.20$:
- Divalent $\text{HCit}^{2-}$ ($62.4\%$) and trivalent $\text{Cit}^{3-}$ ($31.8\%$) dominate over $\text{H}_2\text{Cit}^-$ ($5.8\%$), providing high $\text{Ca}^{2+}$-chelation capacity ($\log K_{\text{Ca-Cit}} = 4.68$).
- Cotyledon pH remains $0.5\text{–}0.7$ units above the vicilin isoelectric point, preventing acid-curdling of storage proteins (`Miano, Pereira & Augusto, 2018`, `10.1016/j.foodres.2017.12.036`).
- Lipoxygenase (`LOX`) activity (optimum $\text{pH } 6.8$) is suppressed by $78\%$ during $55^\circ\text{C}$ steeping (`Roland et al., 2017`, `10.1094/CCHEM-06-16-0161-FI`; `10.3390/foods10123140`).

### Table 2.1: Historical vs. OMEGA-Corrected Buffer Recipes (`artifacts/omega_investigation_results.json`)

| Recipe Identifier | Historical Claimed pH | Actual Equilibrium pH of Historical Recipe | Corrected $\text{K}_3\text{Cit}\cdot\text{H}_2\text{O}$ ($\text{kg}/1000\,\text{L}$) | Corrected $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O}$ ($\text{kg}/1000\,\text{L}$) | Corrected Anhydrous Citric Acid ($\text{kg}/1000\,\text{L}$) | Verified Equilibrium pH |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`TIER_1_MILD` ($0.105\,\text{M}$)** | $5.20$ | **$6.81$** (Defect) | **$18.85\,\text{kg}$** | **$1.90\,\text{kg}$** | **$7.77\,\text{kg}$** | **$5.30$** |
| **`TIER_2_STANDARD` ($0.145\,\text{M}$)** | $5.20$ | **$6.78$** (Defect) | **$25.20\,\text{kg}$** | **$2.54\,\text{kg}$** | **$11.28\,\text{kg}$** | **$5.20$** |
| **`TIER_3_INTENSIVE` ($0.185\,\text{M}$)** | $5.20$ | **$6.72$** (Defect) | **$32.15\,\text{kg}$** | **$3.24\,\text{kg}$** | **$14.39\,\text{kg}$** | **$5.20$** |
| **`BENCH_POT4` ($750\,\text{mL}$ Bath)** | $5.20$ | **$5.91$** (Defect) | **$18.90\,\text{g}$** | **$1.90\,\text{g}$** | **$8.46\,\text{g}$** | **$5.20$** |

---

## 3. Complete Stage 2 Chemistry & Washing Trade-Off Matrix

We evaluated 10 combinations of treatment chemistry and post-soak washing operations (`WashingAndResidueModule` & `SensoryAndFlavourModule` in `src/finnoaq/omega_modules.py`). Each case tracks:
1. **External Surface Liquid Film Residue ($\text{ppm}$):** Solute remaining in the adhering surface liquid film ($\delta_{\text{film}} \approx 18\,\text{mL/kg}$) after convective mass transfer during washing.
2. **Total Retained Solutes in Dried Grain ($\text{mg}/100\text{ g}$):** Sum of unwashed surface film plus internal hydrated open-pore solute ($\varepsilon_{\text{hydrated}} \approx 0.18\,\text{L/kg}$), which diffuses out only fractionally during short surface sprays ($t_{\text{wash}} = 12\text{–}30\,\text{s} \ll \tau_{\text{diff,internal}} \approx 960\,\text{s}$).
3. **Cooked Slurry Off-Taste Threshold Ratio ($R_{\text{off}}$) & Thurstonian $d'$:** Computed after cooking $1\text{ part}$ dal in $3.5\text{ parts}$ water ($4.5\times$ dilution) against human detection thresholds ($\text{HCO}_3^-/\text{CO}_3^{2-}$ soapy/alkaline threshold $180\,\text{ppm}$; $\text{K}^+$ bitter-metallic threshold $650\,\text{ppm}$ in legume matrix; $\text{Citrate}$ sour/tart threshold at $\text{pH } 5.8$ cooked slurry $1600\,\text{ppm}$).
4. **Residual LOX Activity ($\%$) & Predicted Hexanal ($\text{ppb}$):** Coupled thermal + pH inactivation of lipoxygenase during steeping and its effect on linoleic/linolenic hydroperoxide breakdown into grassy hexanal (`Khrisanapant et al., 2019`, `10.1016/j.foodchem.2019.02.126`).

### Table 3.1: Stage 2 Chemistry & Washing Performance Matrix (`artifacts/omega_investigation_results.json`)

| Case ID | Treatment Chemistry | Wash Mode | Wash Time ($\text{s}$) | Wash Water ($\text{L/kg}$) | Surface Film Residue ($\text{ppm}$) | Retained Citrate ($\text{mg}/100\text{g}$) | Retained $\text{K}$ ($\text{mg}/100\text{g}$) | Retained $\text{Na}$ ($\text{mg}/100\text{g}$) | Max Off-Taste Ratio $R_{\text{off}}$ | Residual LOX ($\%$) | Predicted Hexanal ($\text{ppb}$) | Thurstonian $d'$ | Sub-Threshold Aftertaste? | $F_{\text{WB,core}}$ ($W=2$, $\text{N}$) | 2-Whistle Pass? |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`S2-01`** | $0.5\%\text{ NaHCO}_3$ ($\text{pH } 8.32$) | `NO_WASH` | $0.0$ | $0.00$ | $225.0$ | $0.0$ | $0.0$ | $26.7$ | $2.077$ | $24.2\%$ | $46.4$ | $3.45$ | **FAIL** (Strong soapy) | $17.51$ | PASS |
| **`S2-02`** | $0.5\%\text{ NaHCO}_3$ ($\text{pH } 8.32$) | `DUAL_FAN_HIGH_PRESSURE_SPRAY` | $12.0$ | $0.50$ | $3.0$ | $0.0$ | $0.0$ | $19.3$ | $1.104$ | $24.2\%$ | $46.4$ | $2.14$ | **FAIL** (Pore $\text{HCO}_3^-$) | $17.51$ | PASS |
| **`S2-03`** | $0.5\%\text{ NaHCO}_3$ + $0.03\,\text{M}$ Citric Quench | `DUAL_FAN_HIGH_PRESSURE_SPRAY` | $12.0$ | $0.50$ | $6.4$ | $112.3$ | $0.0$ | $34.9$ | $1.990$ | $55.3\%$ | $73.9$ | $2.71$ | **FAIL** (High hexanal) | $15.21$ | PASS |
| **`S2-04`** | $100\%\text{ Na-Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$) | `DUAL_FAN_HIGH_PRESSURE_SPRAY` | $12.0$ | $0.50$ | $21.9$ | $104.8$ | $0.0$ | $32.5$ | $0.143$ | $22.0\%$ | $44.5$ | $0.19$ | PASS | **$18.85$** | **FAIL** |
| **`S2-05`** | $100\%\text{ K-Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$) | `NO_WASH` | $0.0$ | $0.00$ | $1767.4$ | $241.5$ | $107.0$ | $0.0$ | $0.338$ | $22.0\%$ | $44.5$ | $0.46$ | PASS (Surface sticky) | $17.19$ | PASS |
| **`S2-06`** | $100\%\text{ K-Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$) | `DUAL_FAN_HIGH_PRESSURE_SPRAY` | $12.0$ | $0.50$ | $23.5$ | $110.2$ | $58.0$ | $0.0$ | $0.183$ | $22.0\%$ | $44.5$ | $0.25$ | PASS | $17.19$ | PASS |
| **`S2-07`** | $90:10\text{ K/Na Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$) | `NO_WASH` | $0.0$ | $0.00$ | $1755.6$ | $240.9$ | $96.0$ | $6.3$ | $0.328$ | $22.0\%$ | $44.5$ | $0.44$ | PASS (Dryer fouling) | $17.35$ | PASS |
| **`S2-08`** | $90:10\text{ K/Na Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$) | `STATIC_IMMERSION_RINSE` | $30.0$ | $1.20$ | $137.1$ | $113.4$ | $52.6$ | $3.4$ | $0.166$ | $22.0\%$ | $44.5$ | $0.22$ | PASS (Excess water) | $17.35$ | PASS |
| **`S2-09`** | $90:10\text{ K/Na Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$) | `ROTARY_DRUM_RINSE` | $20.0$ | $0.80$ | $39.3$ | $108.6$ | $51.3$ | $3.4$ | $0.162$ | $22.0\%$ | $44.5$ | $0.22$ | PASS | $17.35$ | PASS |
| **`S2-10-WINNER`** | **$90:10\text{ K/Na Citrate}$ ($0.145\,\text{M}, \text{pH } 5.20$)** | **`DUAL_FAN_HIGH_PRESSURE_SPRAY`** | **$12.0$** | **$0.50$** | **$23.3$** | **$109.7$** | **$52.0$** | **$3.4$** | **$0.164$** | **$22.0\%$** | **$44.5$** | **$0.22$** | **PASS (Optimal)** | **$17.35$** | **PASS** |

---

## 4. Mechanistic Insights into Washing, Residue Removal & Flavour Remediation

### 4.1 Why $12\,\text{s}$ Dual-Fan High-Pressure Spray Washing (`S2-10-WINNER`) Beats Immersion & Rotary Drum Rinsing
1. **Surface Film Stripping Efficiency ($98.7\%$ removal in $12\,\text{s}$):** Impinging fan-jet nozzles ($2.5\,\text{bar}$ gauge) on a vibrating dewatering wedge-wire deck achieve a high external film mass-transfer coefficient ($k_{\text{wash}} \approx 0.36\,\text{s}^{-1}$), stripping the adhering $1755.6\,\text{ppm}$ surface liquor film down to **$23.3\,\text{ppm}$** using only **$0.50\,\text{L/kg}$** of potable water in **$12.0\,\text{s}$** ($60\%$ less wash time than static immersion `S2-08` and $58\%$ less water).
2. **Why `NO_WASH` (`S2-05`, `S2-07`) Is Unacceptable Despite Sub-Threshold Taste:** Even though unwashed $90:10$ citrate (`S2-07`) has $R_{\text{off}} = 0.328 < 1.0$, leaving $1755.6\,\text{ppm}$ of free citrate salt on the wet grain surface causes **hygroscopic stickiness and caramelization/fouling on the $65^\circ\text{C}$ fluidized-bed dryer distributor plate** and leaves a visible chalky bloom on the dried split dhal. The $12\,\text{s}$ spray wash eliminates surface bloom and dryer fouling completely.
3. **Why $90:10\text{ K}^+/\text{Na}^+$ (`S2-10-WINNER`) Is Superior to $100\%\text{ K}^+$ (`S2-06`):** Including $10\%$ sodium citrate reduces the potassium concentration in the cooked slurry by $10.3\%$ ($52.0\,\text{mg}/100\text{g}$ vs $58.0\,\text{mg}/100\text{g}$, well inside the native pigeon pea potassium baseline of $\sim 1390\,\text{mg}/100\text{g}$ dry weight) and lowers the off-taste ratio from $0.183$ ($d'=0.25$) to $0.164$ ($d'=0.22$) because sub-threshold $\text{Na}^+$ masks trace metallic notes of $\text{K}^+$ on bitter/salt taste receptors (`Keast & Breslin, 2003`), while keeping core shear force at $17.35\,\text{N} \le 18.0\,\text{N}$.

### 4.2 Deodorization of Beany/Grassy Off-Notes in Aged East African Pigeon Pea
Aged East African pigeon pea accumulates grassy aldehydes (primarily **hexanal**, **$(E)$-2-nonenal**, and **1-octen-3-ol**) formed by lipoxygenase (`LOX`)-catalyzed peroxidation of polyunsaturated fatty acids (`Khrisanapant et al., 2019`). In `S2-10-WINNER`:
- Operating the steeping bath at verified **$\text{pH } 5.20$ and $55.0^\circ\text{C}$** with $0.145\,\text{M}$ citrate chelates trace pro-oxidant $\text{Fe}^{2+}/\text{Cu}^{2+}$ cofactors and denatures $78.0\%$ of endogenous `LOX` activity ($22.0\%$ residual activity vs $55.3\%$ in cold quench `S2-03`).
- Ultrasonic cavitation degassing ($17\,\text{W/L}$) plus warm steeping strips volatile free hexanal into the bleed liquor, reducing predicted cooked-slurry hexanal from $>115\,\text{ppb}$ (untreated aged Tanzanian dal) to **$44.5\,\text{ppb}$**, approaching the fresh Indian Latur reference baseline ($\sim 38\,\text{ppb}$).

### 4.3 Strict Separation of Active Spray Exposure (`12.0 s`) vs. Full Wash/Dewatering Station Residence (`4.0 min`) & GPU Uncertainty Sweep
Per **Part F2**, we strictly separate the active nozzle exposure time from the total station residence time on the vibratory wedge-wire deck (`WSH-102`):
- **Active Spray Exposure Time:** **$12.0\,\text{s}$** ($0.20\,\text{min}$) under dual-fan $2.5\,\text{bar}$ nozzles at $0.50\,\text{L/kg}$ potable water.
- **Full Wash & Dewatering Station Residence Time:** **$4.00\,\text{min}$** ($240.0\,\text{s}$), comprising $0.50\,\text{min}$ ($30\,\text{s}$) initial free-liquor gravity drainage over the $500\,\mu\text{m}$ recycle screen, $0.20\,\text{min}$ ($12\,\text{s}$) active spray rinse, and $3.30\,\text{min}$ ($198\,\text{s}$) vibratory transport under high-velocity air-knife dewatering hoods to reach $28.0\%\text{–}28.7735\%\text{ WB}$ pre-dryer moisture.

#### Table 4.1: GPU 100,000-Trajectory Spray-Duration & Threshold Uncertainty Sweep (`artifacts/omega_gpu_uncertainty_campaign.json`)

| Active Spray Time ($\text{s}$) | Full WSH-102 Residence ($\text{min}$) | Surface Film Mean ($\text{ppm}$) | Surface Film $P_{95}$ ($\text{ppm}$) | $P(\text{Film} < 50\,\text{ppm})$ ($\%$) | Off-Taste Ratio $R_{\text{off}}$ Mean [95% CI] | Thurstonian $d'$ Mean | Epistemic Classification |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$0.0$** | $3.5$ | $1755.7$ | $2141.3$ | $0.00\%$ | $0.402$ $[0.294, 0.555]$ | $0.54$ | `PREDICTED_MINIMUM` (Fails dryer fouling ceiling) |
| **$6.0$** | $4.0$ | $211.4$ | $337.9$ | $0.00\%$ | $0.213$ $[0.153, 0.297]$ | $0.29$ | `PREDICTED_MINIMUM` (Exceeds $50\,\text{ppm}$ bloom limit) |
| **$12.0$ (Nominal)** | **$4.0$** | **$27.6$** | **$61.4$** | **$90.20\%$** | **$0.190$** $[0.136, 0.265]$ | **$0.26$** | **`PREDICTED_MINIMUM` (Selected Nominal)** |
| **$15.0$ (Robust)** | **$4.0$** | **$10.3$** | **$26.3$** | **$99.44\%$** | **$0.187$** $[0.134, 0.262]$ | **$0.25$** | **`PREDICTED_MINIMUM` (99.4% < 50 ppm film)** |
| **$20.0$** | $4.0$ | $2.1$ | $6.4$ | $100.00\%$ | $0.186$ $[0.133, 0.260]$ | $0.25$ | `PREDICTED_MINIMUM` (Diminishing returns) |
| **$30.0$** | $4.0$ | $0.1$ | $0.4$ | $100.00\%$ | $0.185$ $[0.132, 0.259]$ | $0.25$ | `PREDICTED_MINIMUM` (Excess water/effluent) |

---

## 5. Mandatory Operational Definitions & ISO 11136:2014 Statistical Equivalence Study Design

### 5.1 Three Mandatory Stage 2 Operational Classifications (**Part F1**)
1. **`PREDICTED_MINIMUM`:** The lowest residual solute or off-taste concentration ratio ($R_{\text{off}} = 0.164$ deterministic / $0.190$ MC mean, $d' = 0.22\text{–}0.26$) estimated by our coupled mass-transfer and psychophysical model. **Current Status of `S2-10-WINNER`: `ACHIEVED_IN_MODEL` (`PREDICTED_MINIMUM`).**
2. **`SENSORY_NONDETECTION`:** No statistically significant difference between treated and untreated reference samples under a blind **ISO 4120:2021 Triangle Test** ($N \ge 24$ trained assessors, $\alpha = 0.05$, power $1-\beta \ge 0.80$ against $d' = 1.0$). **Current Status: `NOT_VERIFIED` (Requires physical `EXP-05`).**
3. **`INDIAN_REFERENCE_EQUIVALENCE`:** The $90\%$ confidence interval for the mean hedonic difference $(\mu_{\text{FinnoaQ}} - \mu_{\text{IndianRef}})$ lies entirely within $[-\Delta, +\Delta] = [-0.75, +0.75]$ on the 9-point hedonic scale under **ISO 11136:2014 Two One-Sided Tests (TOST)** ($N \ge 72$ regular consumers). **Current Status: `NOT_VERIFIED` (Requires physical `EXP-05`).**

In accordance with **Section 7.6** and **Section 11** of the FinnoaQ OMEGA mission rules, we **explicitly prohibit claiming consumer sensory equivalence as an accomplished fact** before human panel testing is executed. All legacy fabricated hedonic scores (`8.8/9.0`) have been purged (`FAIL-0023`). Instead, `SensoryAndFlavourModule.design_iso_tost_equivalence_study()` specifies the exact physical protocol required to convert our sensory status from `MODEL_DERIVED` / `NOT_VERIFIED` to `MEASURED`:

### Table 5.1: ISO 11136:2014 Two One-Sided Tests (TOST) Sensory Equivalence Specification

| Parameter | Specification | Scientific Justification & Source |
| :--- | :--- | :--- |
| **Governing Standard** | **ISO 11136:2014** (`ISO Catalogue 50125`) & **ISO 4120:2021** (Triangle Test) | International standard for measuring consumer hedonic degree of liking in a controlled sensory booth area (`Bi & Meyners, 2012`, *Food Qual. Prefer.*). |
| **Reference Benchmark** | Authentic unpolished Indian Latur/Akola Toor Dal cooked to its native $t_{90}$ ($3$ whistles) | Prevents artificial penalization of the Indian control for under-cooking while testing FinnoaQ Tanzanian dal cooked for **2 whistles**. |
| **Evaluation Matrices** | **Matrix A:** Unspiced Pressure-Cooked Dal Slurry ($1:3.5$ dal:water, $0.5\%\text{ NaCl}$ only)<br>**Matrix B:** Standardized Tempered Indian Dal Tadka | Matrix A prevents cumin/garlic/hing tempering from masking subtle soapy, sour, or metallic off-notes; Matrix B validates real-world household acceptance. |
| **Hedonic Scale & Margin ($\Delta$)** | 9-point hedonic scale ($1=$ dislike extremely to $9=$ like extremely); Equivalence margin **$\Delta = \pm 0.75$ scale points** | Standard sensory equivalence bound for staple foods (`Meyners, 2012`). |
| **Statistical Power & Sample Size** | One-sided $\alpha = 0.05$ ($90\%$ TOST confidence interval), Power $1-\beta = 0.90$, within-subject $\sigma_w = 1.35 \implies$ **$N = 72$ regular toor-dal consumers** | Balanced **Williams Latin Square ($6$ sequences)** with 3-digit random blind codes and $3\,\text{min}$ unsalted cracker + warm water palate-cleansing intervals. |
| **Dual Acceptance Criterion** | 1. $90\%\text{ CI}$ of $(\mu_{\text{FinnoaQ}} - \mu_{\text{IndianRef}}) \subset [-0.75, +0.75]$ in both Matrix A and Matrix B.<br>2. Trained panel ($N=24$) ISO 4120 triangle test confirms soapy/metallic off-note incidence $p_{\text{soapy}} < 0.10$. | Guarantees both consumer hedonic parity and absence of detectable chemical reagent aftertaste. |

