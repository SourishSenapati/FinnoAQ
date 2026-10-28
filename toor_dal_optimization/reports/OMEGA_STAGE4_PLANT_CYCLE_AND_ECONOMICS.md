# FINNOAQ OMEGA — STAGE 4 COMPLETE 15 TPD INDUSTRIAL PLANT CYCLE, DRYING STRESS, MASS/ENERGY BALANCE & ECONOMICS
**Project Ref:** `FNQ-PR-2026-001` | **System:** `FINNOAQ OMEGA (Offline-First Scientific Engineering & Proof System)`  
**Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Date:** October 28, 2026 | **Verification Status:** `MODEL_DERIVED` + `LITERATURE_SUPPORTED` (Pending Pilot Screen-Drainage & Dryer Breakage Trial)

---

## 1. Executive Summary & Stage 4 Objectives

Stage 4 integrates the validated Stage 1/2/3 process (`0.145 M 90:10 K/Na Citrate at pH 5.20, 55°C 20 min UAE 17 W/L, 12 s Dual-Fan High-Pressure Spray Wash`) into a complete **15 Metric Tonne per Day (15 TPD / $15,000\,\text{kg/day}$ finished dhal, $20\,\text{h/day}$ active operation $= 750\,\text{kg/h}$)** industrial manufacturing plant (`PlantOperationsAndEconomicsModule` in `src/finnoaq/omega_modules.py`).

### Key Stage 4 Engineering Findings & Defect Remediations
1. **Remediation of Defect `FAIL-0021` (Temperature-Coupled Drying Stress & Fissuring):**
   - The legacy script (`simulate_drying_cycle.py`) computed an identical `1.18 MPa` tensile stress and `0.3%` breakage for both $85^\circ\text{C}$ single-stage blast drying and $65^\circ\text{C} \to 55^\circ\text{C}$ two-stage drying because it failed to couple Page drying rate $k(T)$ to internal moisture diffusivity $D_{\text{eff}}(T)$, divided $k$ by $60^1$ instead of $60^n$, violated the repo's own `<= 2.0 MPa` tissue stress guard (`2.4 MPa`), and cited a plum drying paper (`Goyal et al., 2007`).
   - Using true pigeon-pea convective drying parameters (`Chakraborty et al., 2007`, `10.1016/j.jfoodeng.2006.10.019`; `Kashaninejad et al., 2007`) and temperature-coupled Biot-number moisture gradients in `PlantOperationsAndEconomicsModule`, we prove that **$85^\circ\text{C}$ single-stage blast drying (`D1`) generates a peak surface tensile stress of $\sigma_{\text{max}} = 1.850\,\text{MPa}$**, exceeding the cotyledon viscoelastic yield threshold ($\sigma_{\text{yield}} = 1.65\,\text{MPa}$, stress-to-yield ratio **$1.121\times$**) and causing **$3.19\%$ broken/fissured grain loss**.
   - Conversely, our **Two-Stage Step-Down Fluidized-Bed Drying with 20-Minute Tempering (`D4`: $65^\circ\text{C}$ for $22\,\text{min} \to 20\,\text{min}$ adiabatic tempering $\to 55^\circ\text{C}$ for $25\,\text{min}$, $67.0\,\text{min}$ total schedule)** caps peak tensile stress at **$\sigma_{\text{max}} = 0.711\,\text{MPa}$** ($0.431 \times \sigma_{\text{yield}}$), collapses the core-to-surface moisture gradient during tempering to $\Delta X_{\text{db}} = 0.0016\,\text{kg/kg}$, and limits breakage to the mechanical handling baseline (**$0.35\%$**).
2. **Remediation of Defect `FAIL-0025` (Once-Through vs. 85% Recycled Bath Mass & OpEx Reconciliation):**
   - The legacy SOP (`15TPD_FACTORY_SOP_AND_RECIPES.md`) listed once-through daily reagent masses ($899.4\,\text{kg/day}$ citrate salts $\approx \text{₹}9.49/\text{kg}$ dal) while simultaneously claiming a reagent OpEx of `₹0.42/kg dal` (an impossible $22\times$ contradiction).
   - We explicitly model and report both operating modes side-by-side:
     - **Mode A (Once-Through Bath, $0\%$ Liquor Recycle):** Consumes $880.9\,\text{kg/day}$ total reagents ($\text{₹}8.62/\text{kg}$ reagent cost, **$\text{₹}11.65/\text{kg}$ total OpEx**). Economically unviable for commodity toor dal.
     - **Mode B (85% Bleed-and-Feed Recycled Bath via $50\,\mu\text{m}$ Wedge-Wire Filtration + Conductivity/pH Dosing):** Recovers $85\%$ of free drained steeping liquor while compensating for $0.18\,\text{L/kg}$ grain imbibition/carryover and $15\%$ sanitary bleed. Reduces daily reagent consumption to **$371.3\,\text{kg/day}$** ($239.83\,\text{kg}$ $\text{K}_3\text{Cit}\cdot\text{H}_2\text{O} + 24.16\,\text{kg}$ $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O} + 107.30\,\text{kg}$ Citric Acid), yielding a realistic, fully audited **Reagent Cost of $\text{₹}3.63/\text{kg}$** and **Total Plant OpEx of $\text{₹}6.34/\text{kg}$ finished dal** ($\text{₹}95,065/\text{day}$).
3. **Preservation of the $+199.72\,\text{kg/day}$ Pre-Dryer Moisture Bound (`Scenario B1` vs. `Scenario B2`):**
   - In strict compliance with `DECISION_LOG.md`, both pre-dryer dewatered moisture bounds are preserved: **Scenario B1 ($28.0\%\text{ WB}$)** requires **$3,654.42\,\text{kg/day}$** water evaporation, whereas **Scenario B2 ($28.7735\%\text{ WB}$)** requires **$3,854.14\,\text{kg/day}$** evaporation (an exact **$\Delta m_{\text{evap}} = +199.72\,\text{kg/day}$** difference). Both scenarios use our conservative thermal sizing envelope ($195\,\text{kW}_{\text{th}}$ peak dryer capacity).

---

## 2. Convective Drying Regimes & Stress-Crack Comparison (`FAIL-0021` Fixed)

### Table 2.1: 15 TPD Convective Drying Schedule & Thermo-Mechanical Stress Matrix (`artifacts/omega_investigation_results.json`)

| Drying Regime ID | Stage 1 Temp & Time | Tempering Time ($\text{min}$) | Stage 2 Temp & Time | Total Schedule ($\text{min}$) | Final Moisture ($\%\text{ WB}$) | Core-Surface $\Delta X_{\text{db}}$ ($\text{kg/kg}$) | Peak Tensile Stress $\sigma_{\text{max}}$ ($\text{MPa}$) | Tissue Yield Limit $\sigma_{\text{yield}}$ ($\text{MPa}$) | Stress / Yield Ratio | Broken Grain Loss ($\%$) | Mechanical Integrity Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`D1_85C_Single_Stage_Blast`** | $85^\circ\text{C}$ ($42\,\text{min}$) | $0.0$ | $85^\circ\text{C}$ ($0\,\text{min}$) | $42.0$ | $7.19\%$ (Over-dried) | $0.0431$ | **$1.850\,\text{MPa}$** | $1.65\,\text{MPa}$ | **$1.121\times$** | **$3.19\%$** | **`CRITICAL_FISSURING_EXCEEDS_YIELD`** |
| **`D2_75C_Single_Stage`** | $75^\circ\text{C}$ ($46\,\text{min}$) | $0.0$ | $75^\circ\text{C}$ ($0\,\text{min}$) | $46.0$ | $17.70\%$ (Under-dried) | $0.0811$ | $1.136\,\text{MPa}$ | $1.65\,\text{MPa}$ | $0.688\times$ | $0.35\%$ | Unsafe moisture ($>12\%\text{ WB}$ mold risk) |
| **`D3_65C_55C_No_Temper`** | $65^\circ\text{C}$ ($22\,\text{min}$) | $0.0$ | $55^\circ\text{C}$ ($26\,\text{min}$) | $48.0$ | $11.54\%$ | $0.0637$ | $0.711\,\text{MPa}$ | $1.65\,\text{MPa}$ | $0.431\times$ | $0.35\%$ | High residual gradient ($\Delta X_{\text{db}} = 0.064$) |
| **`D4_65C_55C_With_20min_Temper`** | **$65^\circ\text{C}$ ($22\,\text{min}$)** | **$20.0$** | **$55^\circ\text{C}$ ($25\,\text{min}$)** | **$67.0$** | **$11.75\%$** | **$0.0016$** | **$0.711\,\text{MPa}$** | **$1.65\,\text{MPa}$** | **$0.431\times$** | **$0.35\%$** | **`SAFE_BELOW_YIELD` (Selected Winner)** |

---

## 3. Complete 15 TPD Mass, Water, Energy & Economic Balance (`FAIL-0025` Fixed)

### Table 3.1: Audited 15 TPD Material, Utility & OpEx Comparison (`artifacts/omega_investigation_results.json`)

| Process Parameter / Cost Element | Mode A: Once-Through Bath ($0\%$ Liquor Recycle) | Mode B: Bleed-and-Feed Recycled Bath ($85\%$ Liquor Recycle — Selected) | Basis & Engineering Provenance |
| :--- | :---: | :---: | :--- |
| **Finished Product Output ($10.0\text{–}11.75\%\text{ WB}$)** | $15,000.0\,\text{kg/day}$ | **$15,000.0\,\text{kg/day}$** | $750.0\,\text{kg/h}$ over $20.0\,\text{h/day}$ active run ($4\,\text{h}$ CIP) |
| **Raw Untreated Dal Input ($9.8\%\text{ WB}$)** | $15,052.7\,\text{kg/day}$ | **$15,052.7\,\text{kg/day}$** | Accounts for $0.35\%$ net dry-matter leaching/fines offset by retained buffer ions |
| **Total Bath Circulation Volume** | $22,579.0\,\text{L/day}$ | **$22,579.0\,\text{L/day}$** | $1.50\,\text{L/kg}$ solid-to-liquid steeping ratio |
| **Fresh Makeup Bath Water Required** | $22,579.0\,\text{L/day}$ | **$6,649.5\,\text{L/day}$** | $85\%$ of drained free liquor recycled via $50\,\mu\text{m}$ wedge-wire + UV loop |
| **High-Pressure Spray Wash Water ($12\,\text{s}$)** | $7,526.3\,\text{L/day}$ | **$7,526.3\,\text{L/day}$** | $0.50\,\text{L/kg}$ potable RO water at $2.5\,\text{bar}$ dual-fan spray |
| **Dryer Water Evaporation (`Scenario B1`, $28.0\%\text{ WB}$)** | $3,654.42\,\text{kg/day}$ | **$3,654.42\,\text{kg/day}$** | Vibratory air-knife dewatering screen achieves $28.00\%\text{ WB}$ |
| **Dryer Water Evaporation (`Scenario B2`, $28.7735\%\text{ WB}$)** | $3,854.14\,\text{kg/day}$ | **$3,854.14\,\text{kg/day}$** | Conservative screen drainage bound ($+199.72\,\text{kg/day}$ higher evaporation) |
| **Daily $\text{K}_3\text{Cit}\cdot\text{H}_2\text{O}$ Consumption ($\text{₹}165/\text{kg}$)** | $569.01\,\text{kg/day}$ | **$239.83\,\text{kg/day}$** | Replenishes grain pore uptake + $\text{Ca}^{2+}$ chelation depletion + $15\%$ bleed |
| **Daily $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O}$ Consumption ($\text{₹}130/\text{kg}$)** | $57.32\,\text{kg/day}$ | **$24.16\,\text{kg/day}$** | $10\,\text{mol}\%$ sodium co-cation balance |
| **Daily Anhydrous Citric Acid Consumption ($\text{₹}110/\text{kg}$)** | $254.58\,\text{kg/day}$ | **$107.30\,\text{kg/day}$** | Maintains verified bath $\text{pH } 5.20 \pm 0.05$ |
| **1. Chemical Reagent Cost ($\text{₹/kg}$ dal)** | $\text{₹}8.62/\text{kg}$ | **$\text{₹}3.63/\text{kg}$** | $57.9\%$ savings via $85\%$ bleed-and-feed recycle (`FAIL-0025` resolved) |
| **2. Thermal Energy Cost ($\text{₹/kg}$ dal)** | $\text{₹}1.84/\text{kg}$ | **$\text{₹}1.58/\text{kg}$** | Steep heating ($55^\circ\text{C}$) + 2-stage FBD drying (biomass/PNG steam at $\text{₹}4.2/\text{kWh}_{\text{th}}$) |
| **3. Electrical Power Cost ($\text{₹/kg}$ dal)** | $\text{₹}0.28/\text{kg}$ | **$\text{₹}0.28/\text{kg}$** | $19.2\,\text{kW}$ $40\,\text{kHz}$ ultrasound + FBD blowers + pumps ($\text{₹}8.5/\text{kWh}_{\text{e}}$) |
| **4. Water & ETP Effluent Cost ($\text{₹/kg}$ dal)** | $\text{₹}0.13/\text{kg}$ | **$\text{₹}0.06/\text{kg}$** | Process water + biodegradable citrate ETP treatment |
| **5. Direct Labor, QA & Packaging ($\text{₹/kg}$ dal)** | $\text{₹}0.63/\text{kg}$ | **$\text{₹}0.63/\text{kg}$** | 3-shift plant operators + receiving dock QA technician |
| **6. Broken Grain Downgrade Penalty ($\text{₹/kg}$ dal)** | $\text{₹}0.15/\text{kg}$ | **$\text{₹}0.15/\text{kg}$** | $0.35\%$ breakage downgraded by $\text{₹}42/\text{kg}$ (vs $\text{₹}1.34/\text{kg}$ penalty at $85^\circ\text{C}$!) |
| **TOTAL MANUFACTURING OPEX ($\text{₹/kg}$ finished dal)** | **$\text{₹}11.65/\text{kg}$** | **$\text{₹}6.34/\text{kg}$** | **Economically viable within the $\text{₹}18\text{–}28/\text{kg}$ Indian-vs-Tanzanian arbitrage spread** |
| **TOTAL DAILY OPERATING COST ($\text{₹/day}$)** | $\text{₹}174,807/\text{day}$ | **$\text{₹}95,065/\text{day}$** | Saves $\text{₹}79,742/\text{day}$ ($\text{₹}2.39\,\text{Crore/year}$ over $300$ operating days) |

### Table 3.2: Dual-Basis 15 TPD Throughput & Yield Reconciliation (**Part H2** — `artifacts/omega_gpu_uncertainty_campaign.json`)

| Mass Balance Stream / Metric | **Basis I: $15,000.0\,\text{kg/day}$ Raw Feed Input Basis** | **Basis II: $15,000.0\,\text{kg/day}$ Net Saleable Prime Output Basis** | Conservation Notes |
| :--- | :---: | :---: | :--- |
| **Raw Untreated Dal Input ($9.80\%\text{ WB}$)** | **$15,000.0\,\text{kg/day}$** ($750.0\,\text{kg/h}$) | **$15,116.1\,\text{kg/day}$** ($755.81\,\text{kg/h}$) | $20.0\,\text{h/day}$ active run + $4.0\,\text{h/day}$ CIP |
| **Raw Dry Solids Input ($0\%\text{ WB}$)** | $13,530.0\,\text{kg/day}$ | $13,634.7\,\text{kg/day}$ | Exact dry-matter baseline |
| **Gross Leached Dry Solids ($0.42\%$)** | $-56.83\,\text{kg/day}$ | $-57.27\,\text{kg/day}$ | Soluble sugars/albumins into steep + wash water |
| **Retained Buffer Ions in Pores ($+0.07\%$)** | $+9.47\,\text{kg/day}$ | $+9.54\,\text{kg/day}$ | Internal pore $\text{K}^+/\text{Na}^+/\text{Citrate}$ ($+0.35\%$ net dry loss) |
| **Conditioned Dry Solids Exiting Dryer** | $13,482.65\,\text{kg/day}$ | $13,587.0\,\text{kg/day}$ | Zero dry-matter closure error |
| **Screened Broken Splits ($0.35\%$ Breakage)** | $-52.49\,\text{kg/day}$ | $-52.68\,\text{kg/day}$ | Sold as Grade-B dal flour/besan ($\text{₹}42/\text{kg}$ downgrade) |
| **Net Saleable Prime Whole Splits Output** | **$14,884.8\,\text{kg/day}$** | **$15,000.0\,\text{kg/day}$** | Reconciles raw-input vs net-prime-output basis |

---

## 4. Complete 11-Step Industrial Route, Residence Time & Bottleneck Schedule (**Part H1**)

Per **Part H1**, the complete 11-step industrial manufacturing route is modeled below. For a single grain parcel traversing the continuous/semi-continuous line, the **active processing residence time is $103.0\,\text{min}$** ($107.0\,\text{min}$ under the uncertainty-buffered $24\,\text{min}$ Tier 2 policy) and the **gate-to-gate batch elapsed time is $118.0\text{–}122.0\,\text{min}$**:

| Step # | Unit Operation (`Part H1` Mandatory Step) | Active Grain Residence ($\text{min}$) | Turnaround / Off-Line Overlap ($\text{min}$) | Equipment Sizing & Parallelization for $755.8\,\text{kg/h}$ Raw In ($15.0\,\text{TPD}$ Prime Out) | Bottleneck Status |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | **Raw Material Intake & QC** | $5.0\,\text{min}$ (per $20\,\text{MT}$ lot) |Parallel with silo discharge | Receiving pit + $20\,\text{MT}$ homogenization silo (`SIL-100`) | Non-bottleneck (1 lot/day) |
| **2** | **Cleaning, Grading & De-Stoning** | $6.0\,\text{min}$ | Continuous inline | Aspirator + gravity de-stoner + $1.8/2.2\,\text{mm}$ rotary sieve (`CLN-100`) | Non-bottleneck ($1,000\,\text{kg/h}$ rated) |
| **3** | **Batch Testing & Adaptive Routing** | $4.0\,\text{min}$ | Parallel at dock | $\text{WAI}_{3\text{min}}$ + caliper + dielectric moisture -> `Tier 1 / 2 / 3 / OOD` | Non-bottleneck (sets shift recipe) |
| **4** | **Reagent Preparation & Dosing** | Inline ($0.0\,\text{min}$ grain delay) | $15\,\text{min}$ makeup per shift | Jacketed $1,500\,\text{L}$ mixing tank + automated pH/EC dosing skid (`SK-100`) | Non-bottleneck |
| **5** | **Pretreatment / Ultrasonic Soaking (`UAE-101 A/B`)** | **$20.0\,\text{min}$** ($24.0\,\text{min}$ Robust) | $+3.0\,\text{min}$ fill | Two staggered $600\,\text{L}$ ($378\,\text{kg}$ dal + $567\,\text{L}$ liquor) $40\,\text{kHz}$ ($17\,\text{W/L}$) vessels | De-bottlenecked via staggered pair |
| **6** | **Draining & $85\%$ Liquid Recovery** | **$0.5\,\text{min}$** ($30\,\text{s}$) | $+1.0\,\text{min}$ vessel drain | $500\,\mu\text{m}$ wedge-wire primary drain + $50\,\mu\text{m}$ bag filter + UV recycle loop | Non-bottleneck |
| **7** | **Washing / Surface-Residue Removal (`WSH-102A`)** | **$0.2\,\text{min}$** ($12.0\,\text{s}$ active spray) | Continuous on deck | Dual-fan $2.5\,\text{bar}$ potable RO water spray header ($0.50\,\text{L/kg}$) | Non-bottleneck |
| **8** | **Air-Knife Dewatering (`WSH-102B`)** | **$3.3\,\text{min}$** ($198\,\text{s}$) | Continuous on deck | Vibratory 20-mesh stainless deck + high-velocity air knives ($4.0\,\text{min}$ total `WSH-102`) | Non-bottleneck |
| **9** | **Two-Stage Drying & Tempering (`FBD-103` / `TMP-104`)** | **$67.0\,\text{min}$** ($22\,\text{m}$ $65^\circ\text{C} + 20\,\text{m}$ temper $+ 25\,\text{m}$ $55^\circ\text{C}$) | Continuous plug-flow | 2-zone vibrating fluidized bed ($588\,\text{kg}$ holdup) + insulated tempering silo ($252\,\text{kg}$ holdup) | **Primary Residence-Time Bottleneck ($65.0\%$)** |
| **10** | **Cooling, Optical Screening & Packaging (`PKG-105`)** | **$12.0\,\text{min}$** | Continuous inline | Counter-current cooler ($<32^\circ\text{C}$) + $0.35\%$ broken screen + $\text{N}_2$-flush FFS packager | Non-bottleneck |
| **11** | **Cleaning, Turnaround & Daily CIP Maintenance** | $0.0\,\text{min}$ (off-shift) | **$240.0\,\text{min/day}$ ($4.0\,\text{h}$)** | Automated caustic/citric CIP sanitization of `UAE-101 A/B`, `SK-100`, and `WSH-102` | Scheduled in $20\,\text{h}$ work / $4\,\text{h}$ CIP day |
| **TOTAL** | **Active Processing Residence / Gate-to-Gate** | **$103.0\,\text{min}$** ($107.0\,\text{m}$ Robust) | **$118.0\text{–}122.0\,\text{min}$ Gate-to-Gate** | Delivers **$15,000.0\,\text{kg/day}$ net saleable prime whole splits** ($750.0\,\text{kg/h}$ prime output) | 100% Mass & Energy Conservation |

---

## 5. Global Sensitivity Analysis (Sobol / Saltelli-Jansen Variance Decomposition)

We executed a 224-run Quasi-Monte Carlo Sobol variance decomposition (`GlobalSensitivityAnalyzer.compute_sobol_indices`, $N_{\text{base}} = 32$, $d = 5$ parameters) directly on the full 2D conservative soaking PDE + non-isothermal pressure-cooking solver to rank which biophysical and operating parameters control **Whistle-2 Core Shear Force ($F_{\text{WB,core}}$)**:

### Table 5.1: Sobol First-Order ($S_1$) and Total-Order ($S_T$) Sensitivity Indices (`artifacts/omega_investigation_results.json`)

| Parameter Name | Parameter Range Explored | First-Order Index $S_1$ | Total-Order Index $S_T$ | Physical & Process Control Implication |
| :--- | :---: | :---: | :---: | :--- |
| **`Steeping_Time_t`** | $8.0 \to 28.0\,\text{min}$ | **$0.4937$** | **$0.6304$** | **Dominant Process Control Variable ($63.0\%$ of total variance).** Directly controls Fourier number $\text{Fo} = D_{\text{cit}} t / H^2$ for core $\text{Ca}^{2+}$ removal. |
| **`Native_Bound_Ca`** | $20.0 \to 44.0\,\text{mol/m}^3$ | **$0.1136$** | **$0.1136$** | **Primary Feedstock Biochemical Disturbance ($11.4\%$ of variance).** Dictates initial middle-lamellar egg-box cross-link density; motivates our 5-minute intake proxy test. |
| **`Half_Thickness_H`** | $0.90 \to 1.28\,\text{mm}$ | $0.0000$ (nonlinear) | **$0.0986$** | **Strong Nonlinear Interaction ($S_T = 9.9\%$).** Acts multiplicatively with steeping time via $t / H^2$; thick grains fail rapidly when $t < 18\,\text{min}$. |
| **`Steeping_Temp_T`** | $40.0 \to 60.0^\circ\text{C}$ | $0.0538$ | **$0.0829$** | **Moderate Arrhenius Driver ($8.3\%$ of variance).** Must be tightly controlled at $55.0 \pm 1.5^\circ\text{C}$ (below $62^\circ\text{C}$ starch onset). |
| **`Citrate_Molarity_C`** | $0.08 \to 0.20\,\text{M}$ | $0.0000$ (plateau) | **$0.0807$** | **Threshold Saturation Effect ($8.1\%$ of variance).** Below $0.11\,\text{M}$ chelation is stoichiometrically starved; above $0.145\,\text{M}$ diffusion into the core is rate-limiting rather than bath molarity. |

