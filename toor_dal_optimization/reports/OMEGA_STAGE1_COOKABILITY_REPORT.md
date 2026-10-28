# FINNOAQ OMEGA — STAGE 1 SCIENTIFIC COOKABILITY & PRETREATMENT INVESTIGATION REPORT
**Project Ref:** `FNQ-PR-2026-001` | **System:** `FINNOAQ OMEGA (Offline-First Scientific Engineering & Proof System)`  
**Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Date:** October 28, 2026 | **Verification Status:** `MODEL_DERIVED` + `LITERATURE_SUPPORTED` (Pending Monday Physical Bench Validation)

---

## 1. Executive Summary & Stage 1 Objective

Stage 1 of the FinnoaQ OMEGA investigation addresses the foundational physical-chemical question:
> **What is the best achievable cooking performance for aged East African/Tanzanian split pigeon pea (*Cajanus cajan* L. Millsp.), and what is the shortest physically credible pretreatment time that achieves $\le 2$ pressure-cooker whistles without creating an under-softened cotyledon core?**

Using our verified 2D axisymmetric conservative finite-volume reaction-diffusion solver (`HydrationAndPenetrationModule` in `src/finnoaq/omega_modules.py`) coupled to the two-substrate non-isothermal pressure-cooking texture model (`ThermalAndPressureCookingModule`) and cross-checked against the literature-anchored empirical benchmark (`Nisha, Singhal & Pandit, 2006`, *J. Food Eng.* 74:108–115; `Chakraborty, Kumbhar & Sarkar, 2007`, *J. Food Eng.* 81:202–209), we establish three rigorous findings:

1. **Both Bulk and Core Tenderness Gates Are Required:** A split cotyledon passes the 2-whistle gate ($t_{\text{steam}} = 8.40\,\text{min}$ total, comprising $4.50\,\text{min}$ sensible heat-up to $121.1^\circ\text{C}$ at $103.4\,\text{kPa}$ gauge plus two $1.95\,\text{min}$ whistle cycles) **only** if both volume-averaged Warner-Bratzler shear force ($F_{\text{WB,bulk}}$) and central core shear force ($F_{\text{WB,core}}$ at $z \le 0.25\,H$) satisfy:
   $$F_{\text{WB,bulk}}(W=2) \le 18.0\,\text{N} \quad \text{AND} \quad F_{\text{WB,core}}(W=2) \le 18.0\,\text{N}$$
2. **Rejection of the Legacy 4.6-Minute Vacuum Impregnation Claim (`FAIL-0023`):** The legacy simulation script (`simulate_pretreatment.py`) claimed a $4.6\,\text{min}$ vacuum impregnation soak achieved $95\%$ bulk $\text{Ca}^{2+}$ displacement by unphysically initializing $70\%$ of the dry cotyledon's spatial grid at $0.85 \times C_{\text{bath}}$ ($110.5\,\text{mol/m}^3$) at $t=0$. Under Fito et al. (1996) Hydrodynamic Mechanism (HDM) conservation laws (`DOI: 10.1016/0260-8774(95)00005-4`) and measured dry split cotyledon open porosity ($\varepsilon_{\text{open}} \approx 0.11$, `Tiwari & Singh, 2012`), a $15\,\text{kPa}$ absolute vacuum pulse followed by atmospheric restoration can convectively fill only $\Delta\varepsilon_{\text{VI}} \approx 0.0815$ ($8.15\%$ of grain volume) within the outer $28\%$ rim. At $t = 4.6\,\text{min}$ (`S1-10-CIT-VI-4.6`), core $\text{Ca}^{2+}$ displacement is only **$5.2\%$**, resulting in $F_{\text{WB,core}}(W=2) = 24.63\,\text{N}$ ($7$ whistles required).
3. **Shortest Credible Pretreatment for Aged Tanzanian HTC Dal (`S1-09-CIT-UAE-20`):** The shortest physically defensible pretreatment for nominal aged Tanzanian HTC split dhal ($2H = 2.16\,\text{mm}$, $C_{\text{Ca,0}} = 33.5\,\text{mol/m}^3$) is a **$20.0\,\text{min}$ steeping at $55.0^\circ\text{C}$** with **$17.0\,\text{W/L}$ ($40\,\text{kHz}$) ultrasound assistance** in a **$0.145\,\text{M}$ 90:10 $\text{K}^+/\text{Na}^+$ citrate buffer at verified $\text{pH } 5.20$**. This achieves **$98.1\%$ bulk** and **$80.7\%$ core $\text{Ca}^{2+}$ displacement**, $51.4\%\text{ WB}$ hydrated moisture, $t_{90,\text{mech}} = 8.30\,\text{min}$ ($2$ whistles), $F_{\text{WB,bulk}}(W=2) = 13.91\,\text{N}$, and $F_{\text{WB,core}}(W=2) = 17.35\,\text{N} \le 18.0\,\text{N}$ with only $0.42\%$ dry-matter leaching loss.

---

## 2. Biophysical Mechanism of the Hard-to-Cook (HTC) Defect in Split Pigeon Pea

During post-harvest storage of *Cajanus cajan* under elevated tropical temperature and humidity ($28\text{–}35^\circ\text{C}$, $70\text{–}80\%\text{ RH}$ typical of East African maritime transit and warehouse storage; `Perera et al., 2023`, `10.1016/j.foodchem.2023.135743`; `Panda et al., 2026`, `10.1021/acsfoodscitech.5c00916`), three coupled biochemical cascades lock the middle lamella:

1. **Pectin Methylesterase (PME) De-esterification:** Endogenous PME hydrolyzes methyl esters on galacturonic acid chains of middle-lamellar homogalacturonan, reducing the degree of esterification ($DE$) from $0.52$ (fresh harvest) to $\sim 0.28$ (aged HTC) and exposing negatively charged carboxylate ($\text{-COO}^-$) binding pockets.
2. **Phytase Hydrolysis & Divalent Cation Migration:** Endogenous phytase cleaves *myo*-inositol hexakisphosphate ($\text{IP}_6$), releasing chelated $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$ ions inside the cotyledon parenchyma. These cations migrate to the middle lamella and cross-link adjacent de-esterified pectin chains into insoluble **$\text{Ca}^{2+}$-pectate "egg-box" junctions** ($\log K_{\text{Ca-Pectate}} \approx 3.85$), increasing bound $\text{Ca}^{2+}$ from $14.0\,\text{mol/m}^3$ (fresh Indian Latur reference) to $33.5\,\text{mol/m}^3$ (nominal Tanzanian aged HTC) and up to $42.0\,\text{mol/m}^3$ (severe Arusha HTC).
3. **Storage Protein Insolubilization & Phenolic Cross-Linking:** Vicilin (7S) and legumin (11S) globulins undergo hydrophobic aggregation (`Ohanenye et al., 2024`, `10.1016/j.meafoo.2024.100176`), restricting intracellular water absorption and retarding starch gelatinization inside protein-encapsulated cotyledon cells.

### Why Split Cotyledons Differ Fundamentally from Whole Seeds
Literature studies on whole pigeon pea (`Ohanenye et al., 2024`, `4–24 h` soaking; `Vásquez et al., 2021`, `10.1016/j.lwt.2021.111191`, whole Peruvian pigeon pea with intact seed coat) are explicitly tagged **`INDIRECT`** for split dhal soaking durations because de-hulling and splitting removes the hydrophobic palisade testa (seed coat) and exposes the flat adaxial split face directly to the steeping bath. However, the diffusive path length in split dhal is governed by the **cotyledon half-thickness $H$**:
$$\tau_{\text{diff}} \sim \frac{H^2}{D_{\text{eff}}(T, I_{\text{US}})}$$
For large-seeded Tanzanian split dhal ($H = 1.08\,\text{mm}$, vs $H = 0.85\,\text{mm}$ for Indian Latur), $H^2$ is **$61.5\%$ larger** ($1.166\,\text{mm}^2$ vs $0.723\,\text{mm}^2$), creating a severe core penetration barrier even without a seed coat.

---

## 3. Hierarchical Mechanistic vs. Literature-Empirical Cookability Comparison

All 11 Stage 1 candidates were evaluated on the identical nominal aged Tanzanian HTC reference batch (`TANZANIAN_HTC_AGED_NOMINAL`: $2H = 2.16\,\text{mm}$, $H = 1.08\,\text{mm}$, $R_{\text{eq}} = 2.40\,\text{mm}$, $X_{\text{wb,0}} = 9.8\%$, $C_{\text{Ca,0}} = 33.5\,\text{mol/m}^3$, $DE = 0.28$), alongside the untreated fresh Indian Latur benchmark (`INDIAN_LATUR_FRESH_REF`: $2H = 1.70\,\text{mm}$, $H = 0.85\,\text{mm}$, $X_{\text{wb,0}} = 10.8\%$, $C_{\text{Ca,0}} = 14.0\,\text{mol/m}^3$).

### Table 3.1: Stage 1 Complete Candidate Performance Matrix (`artifacts/omega_investigation_results.json`)

| Candidate ID | Process Description | Soak Time ($\text{min}$) | Temp ($^\circ\text{C}$) | Bulk $\text{Ca}^{2+}$ Disp. ($\%$) | Core $\text{Ca}^{2+}$ Disp. ($\%$) | Hydrated Moisture ($\%\text{ WB}$) | $t_{90}$ Mechanistic ($\text{min}$) | $t_{90}$ Empirical Nisha ($\text{min}$) | Whistles at $t_{90}$ | $F_{\text{WB,bulk}}$ at $W=2$ ($\text{N}$) | $F_{\text{WB,core}}$ at $W=2$ ($\text{N}$) | Leaching Loss ($\%$) | 2-Whistle Gate Pass? |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`S1-01-IND-REF`** | Indian Latur Fresh Reference (Untreated) | $0.0$ | $25.0$ | $0.0\%$ | $0.0\%$ | $10.8\%$ | $9.80$ | $13.30$ | $3$ | $21.53$ | $21.53$ | $0.00\%$ | **FAIL** (Needs 3 whistles) |
| **`S1-02-TZA-RAW`** | Tanzanian Aged HTC Control (Untreated) | $0.0$ | $25.0$ | $0.0\%$ | $0.0\%$ | $9.8\%$ | $17.30$ | $23.10$ | $8$ | $25.64$ | $25.64$ | $0.00\%$ | **FAIL** (Needs 8 whistles) |
| **`S1-03-WATER-20`** | Warm Water Soak Only ($55^\circ\text{C}$, $20\,\text{min}$) | $20.0$ | $55.0$ | $0.0\%$ | $0.0\%$ | $51.3\%$ | $17.27$ | $23.10$ | $8$ | $24.02$ | $24.02$ | $0.35\%$ | **FAIL** (Zero Ca removal) |
| **`S1-04-BICARB-20`** | Alkaline $\text{NaHCO}_3$ $0.5\%\text{ w/v}$ ($55^\circ\text{C}$, $20\,\text{min}$) | $20.0$ | $55.0$ | $86.7\%$ | $32.0\%$ | $51.2\%$ | $9.40$ | $8.07$ | $2$ | $10.83$ | $19.89$ | $0.35\%$ | **FAIL** (Core $19.89 > 18\,\text{N}$) |
| **`S1-05-CIT-STATIC-20`** | Hybrid $\text{K/Na}$ Citrate Static Soak ($55^\circ\text{C}$, $20\,\text{min}$) | $20.0$ | $55.0$ | $95.5\%$ | $61.1\%$ | $50.5\%$ | $9.63$ | $9.73$ | $2$ | $14.70$ | $20.35$ | $0.35\%$ | **FAIL** (Core $20.35 > 18\,\text{N}$) |
| **`S1-06-CIT-UAE-5`** | Hybrid Citrate + UAE $17\,\text{W/L}$ ($55^\circ\text{C}$, $5\,\text{min}$) | $5.0$ | $55.0$ | $50.1\%$ | $1.2\%$ | $43.0\%$ | $17.07$ | $16.23$ | $8$ | $20.59$ | $24.52$ | $0.10\%$ | **FAIL** (Core untouched) |
| **`S1-07-CIT-UAE-10`** | Hybrid Citrate + UAE $17\,\text{W/L}$ ($55^\circ\text{C}$, $10\,\text{min}$) | $10.0$ | $55.0$ | $78.3\%$ | $17.2\%$ | $48.0\%$ | $14.80$ | $12.17$ | $6$ | $17.55$ | $23.53$ | $0.21\%$ | **FAIL** (Core $23.53 > 18\,\text{N}$) |
| **`S1-08-CIT-UAE-15`** | Hybrid Citrate + UAE $17\,\text{W/L}$ ($55^\circ\text{C}$, $15\,\text{min}$) | $15.0$ | $55.0$ | $92.4\%$ | $50.0\%$ | $50.3\%$ | $10.70$ | $10.20$ | $3$ | $15.39$ | $21.53$ | $0.31\%$ | **FAIL** (Core $21.53 > 18\,\text{N}$) |
| **`S1-09-CIT-UAE-20`** | **Hybrid Citrate + UAE $17\,\text{W/L}$ ($55^\circ\text{C}$, $20\,\text{min}$)** | **$20.0$** | **$55.0$** | **$98.1\%$** | **$80.7\%$** | **$51.4\%$** | **$8.30$** | **$9.40$** | **$2$** | **$13.91$** | **$17.35$** | **$0.42\%$** | **PASS (Stage 1 Winner)** |
| **`S1-10-CIT-VI-4.6`** | Hybrid Citrate + Vacuum Pulse Only ($15\,\text{kPa}$, $4.6\,\text{min}$) | $4.6$ | $55.0$ | $52.9\%$ | $5.2\%$ | $41.4\%$ | $16.57$ | $15.57$ | $7$ | $20.70$ | $24.63$ | $0.08\%$ | **FAIL** (`FAIL-0023` disproved) |
| **`S1-11-CIT-VI-UAE-15`** | Hybrid Citrate + Vacuum Pulse + UAE ($15\,\text{kPa}$, $15\,\text{min}$) | $15.0$ | $55.0$ | $95.5\%$ | $63.1\%$ | $50.4\%$ | $9.53$ | $9.70$ | $2$ | $14.71$ | $20.10$ | $0.31\%$ | **FAIL** (Core $20.10 > 18\,\text{N}$) |

---

## 4. Detailed Physical Analysis of Stage 1 Findings

### 4.1 Why Warm Water Alone (`S1-03-WATER-20`) Fails Completely
Steeping aged Tanzanian dhal in pure $55^\circ\text{C}$ water for $20\,\text{min}$ hydrates the cotyledon to $51.3\%\text{ WB}$ moisture (above the $48\%\text{ WB}$ threshold required for starch gelatinization), yet achieves **$0.0\%$ $\text{Ca}^{2+}$ displacement** from the middle lamella. Because the $\text{Ca}^{2+}$-pectate egg-box cross-links remain 100% intact, cell separation during $121.1^\circ\text{C}$ pressure cooking remains blocked ($F_{\text{WB,core}} = 24.02\,\text{N}$ at Whistle 2, requiring $8$ whistles). **Pre-hydration without divalent cation chelation or $\beta$-elimination cannot cure the HTC defect.**

### 4.2 Why Alkaline Sodium Bicarbonate (`S1-04-BICARB-20`) Creates a Mushy Rim and Hard Core
In $0.5\%\text{ w/v}$ $\text{NaHCO}_3$ ($\text{pH } 8.32$) at $55^\circ\text{C}$ for $20\,\text{min}$, hydroxide ions ($\text{OH}^-$) catalyze rapid $\beta$-eliminative cleavage of esterified pectin in the outer shell, driving $F_{\text{WB,bulk}}(W=2)$ down to **$10.83\,\text{N}$** (over-softened outer slurry). However, because aged HTC pectin is de-esterified ($DE = 0.28$, meaning $72\%$ of galacturonate residues lack methyl esters required for $\beta$-elimination) and $\text{HCO}_3^-/\text{CO}_3^{2-}$ precipitation of $\text{CaCO}_3$ is diffusion-limited without acoustic cavitation, core $\text{Ca}^{2+}$ removal reaches only **$32.0\%$**, leaving a chalky core ($F_{\text{WB,core}} = 19.89\,\text{N} > 18.0\,\text{N}$). Moreover, as proven in Stage 2, alkaline $\text{NaHCO}_3$ causes severe soapy/metallic off-notes ($d' = 2.14\text{–}3.45$) and Maillard darkening.

### 4.3 Why Static Citrate (`S1-05`) and 15-Minute UAE (`S1-08`) Fall Just Short on Thick ($2.16\,\text{mm}$) Cotyledons
- **Static Citrate (`S1-05-CIT-STATIC-20`):** Without $40\,\text{kHz}$ acoustic cavitation ($17\,\text{W/L}$), the effective citrate ion diffusivity at $55^\circ\text{C}$ is $D_{\text{cit}} = 9.09 \times 10^{-10}\,\text{m}^2/\text{s}$. After $20\,\text{min}$, bulk $\text{Ca}^{2+}$ removal is $95.5\%$, so $F_{\text{WB,bulk}}(W=2) = 14.70\,\text{N}$ passes easily, but core $\text{Ca}^{2+}$ removal is only **$61.1\%$**, yielding $F_{\text{WB,core}}(W=2) = 20.35\,\text{N}$ (a classic "cooked outside, al-dente center" bite).
- **15-Minute UAE (`S1-08-CIT-UAE-15`):** Ultrasound at $17\,\text{W/L}$ enhances diffusivity by $\alpha_{\text{US}} = 1.337\times$ ($D_{\text{cit,US}} = 1.215 \times 10^{-9}\,\text{m}^2/\text{s}$, consistent with `Vásquez et al., 2021`, `10.1016/j.lwt.2021.111191`). At $15\,\text{min}$, bulk shear force passes ($15.39\,\text{N}$), and for thinner mild batches ($2H \le 1.85\,\text{mm}$, Tier 1) $15\,\text{min}$ is fully sufficient. However, for nominal $2.16\,\text{mm}$ aged Tanzanian cotyledons, core $\text{Ca}^{2+}$ removal at $15\,\text{min}$ is $50.0\%$ ($F_{\text{WB,core}} = 21.53\,\text{N}$, requiring $3$ whistles). Extending steeping to **$20.0\,\text{min}$ (`S1-09-CIT-UAE-20`)** drives core $\text{Ca}^{2+}$ displacement to **$80.7\%$** and brings $F_{\text{WB,core}}(W=2)$ down to **$17.35\,\text{N} \le 18.0\,\text{N}$**.

### 4.4 Agreement Between Mechanistic 2D PDE and Literature Empirical Model
Comparing $t_{90,\text{mech}}$ (2D PDE + two-substrate Arrhenius model) against $t_{90,\text{empirical}}$ (`Nisha et al., 2006` pseudo-first-order softening rate $k_{120^\circ\text{C}} = 0.252\,\text{min}^{-1}$, $E_a = 98.5\,\text{kJ/mol}$):
- For **`S1-09-CIT-UAE-20`**, $t_{90,\text{mech}} = 8.30\,\text{min}$ and $t_{90,\text{empirical}} = 9.40\,\text{min}$ — both correspond to **2 whistles** ($8.40\,\text{min}$ nominal 2-whistle cycle, or well below the 3-whistle threshold of $10.35\,\text{min}$).
- Both models independently confirm that sub-10-minute soaking (`S1-06-CIT-UAE-5`, `S1-07-CIT-UAE-10`, `S1-10-CIT-VI-4.6`) cannot soften the core of $2.16\,\text{mm}$ aged HTC dhal within 2 whistles.

---

## 5. Provisional $18.0\,\text{N}$ Threshold Audit & GPU 2D-PDE Parameter Uncertainty Quantification (`20.0 min` vs. `22.0–24.0 min`)

### 5.1 Epistemic Status of the $18.0\,\text{N}$ Tenderness Threshold (`PROVISIONAL_PROJECT_CUTOFF`)
Per **Part E1**, the $18.0\,\text{N}$ Warner-Bratzler / Ottawa Kramer shear force threshold is explicitly classified as a **`PROVISIONAL_PROJECT_CUTOFF`** pending physical instrument calibration against cooked authentic Indian Latur reference dal (`EXP-01`). Under the deterministic nominal model (`S1-09-CIT-UAE-20`), $t_{\text{soak}} = 20.0\,\text{min}$ yields $F_{\text{WB,core}}(W=2) = 17.35\,\text{N}$ ($67.3\%$ deterministic core $\text{Ca}^{2+}$ removal), which passes $\le 18.0\,\text{N}$ by a narrow **$0.65\,\text{N}$ margin**.

### 5.2 GPU 2D-PDE Monte Carlo Uncertainty Propagation ($20,000$ Trajectories/Duration on `NVIDIA GeForce RTX 4050 Laptop GPU`)
To evaluate whether $20.0\,\text{min}$ is robust against joint parameter uncertainty in $H \sim \mathcal{N}(1.08, 0.045^2)\,\text{mm}$, $C_{\text{Ca,0}} \sim \mathcal{N}(33.5, 2.1^2)\,\text{mol/m}^3$, $T_{\text{soak}} \sim \mathcal{N}(55.0, 1.2^2)^\circ\text{C}$, $C_{\text{active}}$, and $k_{\text{soft}}$, we executed **$160,000$ full 2D ($16 \times 16$) cylindrical PDE trajectories** ($18,000,000$ grid time-steps on `cuda:0`, `artifacts/omega_gpu_uncertainty_campaign.json`):

| Soak Duration $t_{\text{soak}}$ ($\text{min}$) | 2D-PDE Trajectories ($N$) | Bulk $\text{Ca}^{2+}$ Removed Mean ($\%$) | Core $\text{Ca}^{2+}$ Removed Mean ($\%$) [95% CI] | $F_{\text{WB,core}}(W=2)$ Mean $\pm$ SD ($\text{N}$) | $F_{\text{WB,core}}(W=2)$ 95% CI ($\text{N}$) | $F_{\text{WB,core}}(W=2)$ $P_{95}$ ($\text{N}$) | $P(F_{\text{WB,core}} \le 18.0\,\text{N})$ ($\%$) | Robustness Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$12.0$** | $20,000$ | $87.07\%$ | $32.80\%$ $[21.44, 46.60]\%$ | $22.55 \pm 0.59$ | $[21.25, 23.57]$ | $23.42$ | $0.00\%$ | **FAIL** |
| **$15.0$** | $20,000$ | $93.70\%$ | $54.52\%$ $[39.34, 70.43]\%$ | $20.76 \pm 1.01$ | $[18.56, 22.49]$ | $22.27$ | $0.76\%$ | **FAIL** (Sufficient only for thin Tier 1 lots) |
| **$18.0$** | $20,000$ | $97.30\%$ | $73.99\%$ $[58.84, 87.16]\%$ | $18.22 \pm 1.29$ | $[15.66, 20.69]$ | $20.31$ | $42.74\%$ | **MARGINAL FAIL** |
| **$20.0$ (Nominal)** | $20,000$ | $98.58\%$ | $83.78\%$ $[70.75, 93.60]\%$ | $16.55 \pm 1.25$ | $[14.27, 19.13]$ | **$18.68$** | **$87.35\%$** | **PASS NOMINAL** ($P_{95} = 18.68 > 18\,\text{N}$) |
| **$22.0$** | $20,000$ | $99.30\%$ | $90.68\%$ $[80.68, 97.13]\%$ | $15.21 \pm 1.06$ | $[13.37, 17.50]$ | **$17.07$** | **$98.92\%$** | **ROBUST PASS** ($P_{95} \le 18.0\,\text{N}$) |
| **$24.0$ (Robust)** | $20,000$ | $99.67\%$ | $95.04\%$ $[88.13, 98.83]\%$ | $14.29 \pm 0.85$ | $[12.81, 16.14]$ | **$15.77$** | **$99.98\%$** | **HIGH-CONFIDENCE PASS** ($97.5\%\text{ bound} = 16.14\,\text{N}$) |
| **$26.0$** | $20,000$ | $99.86\%$ | $97.55\%$ $[93.26, 99.57]\%$ | $13.74 \pm 0.70$ | $[12.46, 15.22]$ | $14.94$ | $100.00\%$ | **SEVERE LOT TIER 3** |
| **$30.0$** | $20,000$ | $99.98\%$ | $99.51\%$ $[98.24, 99.95]\%$ | $13.29 \pm 0.60$ | $[12.16, 14.54]$ | $14.33$ | $100.00\%$ | **ROBUST TIER 3** |

---

## 6. Stage 1 Gate Decision for Downstream Stages

In strict compliance with the FinnoaQ OMEGA sequential investigation rule:
- **Stage 1 Selected Architecture:** **`S1-09-CIT-UAE-20`** ($0.145\,\text{M}$ Hybrid 90:10 $\text{K}^+/\text{Na}^+$ Citrate Buffer at verified $\text{pH } 5.20$, $55.0^\circ\text{C}$, $20.0\,\text{min}$ nominal steeping with $17.0\,\text{W/L}$ $40\,\text{kHz}$ ultrasound; **$22.0\text{–}24.0\,\text{min}$ uncertainty-buffered steeping** when $P_{95}(F_{\text{WB,core}}) \le 18.0\,\text{N}$ is required across parameter uncertainty).
- **Contingency for Severe HTC Lots:** Adding a $15\,\text{kPa}$ initial vacuum pulse (`S1-11` extended to $26\text{–}30\,\text{min}$ at $57^\circ\text{C}$, $0.180\text{–}0.195\,\text{M}$, defined as **Tier 3** in Stage 3) increases core $\text{Ca}^{2+}$ displacement by an additional $+12\text{–}13\%$ over UAE alone by convectively impregnating the outer $28\%$ rim at $t=0$.

