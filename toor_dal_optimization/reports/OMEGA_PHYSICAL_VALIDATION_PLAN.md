# FINNOAQ OMEGA — RANKED EXPERIMENTAL DESIGN & PHYSICAL VALIDATION PLAN
**Project Ref:** FNQ-PR-2026-001 | **Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Epistemic Status:** `EXPERIMENTAL_VALIDATION_PROTOCOL` (Zero wet-lab results fabricated; designed to convert `MODEL_DERIVED` and `HYPOTHETICAL` claims into `DIRECTLY_MEASURED` evidence)

---

## 1. Prioritization Philosophy: Expected Value of Information (EVOI) per Unit Cost & Time

Every computational prediction in the FinnoaQ OMEGA digital twin depends on physical parameters whose true values on the client's incoming East African (*Cajanus cajan*) shipments must be verified empirically. Below, physical validation experiments are ranked strictly by **Expected Value of Information (EVOI) per Rupee and per Hour**, ensuring the highest-risk assumptions are tested first before committing capital to 15 TPD plant equipment.

| EVOI Rank | Experiment ID & Title | Primary Model / Claim Tested | Estimated Cost (INR) | Turnaround Time | Go / No-Go Decision Gate |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **#1** | **EXP-01:** Buffer Stoichiometry pH Verification & 5-Min Intake Proxy Calibration | `Module D` (`FAIL-0024` fix) & `Module A/G` Intake Diagnostics | ₹2,500 | **2 Hours** | Buffer equilibrates at $\text{pH } 5.20 \pm 0.05$; $\text{WAI}_{3\text{min}}$ repeatability $\text{CV} < 5\%$. |
| **#2** | **EXP-02:** Two-Sieve Multi-Duration Steeping & Whistle-2 Core Shear Trial | `Module B` ($D_{\text{cit}}$ vs $k_{\text{chel}}$ identifiability) & `Module C` ($\le 2$ whistles) | ₹12,000 | **1 Day** | Whistle-2 core shear force $F_{\text{WB,core}} \le 18.0\,\text{N}$ and $0\%$ opaque chalky center after 15–20 min UAE soak. |
| **#3** | **EXP-03:** Spray-Wash Conductivity Curve & Dewatering Screen Moisture Trial | `Module E` surface washout & `Module H` Scenario B1 vs B2 ($+199.72\,\text{kg/day}$) | ₹15,000 | **1 Day** | Surface rinse conductivity $< 350\,\mu\text{S/cm}$ at $12\,\text{s}$; resolves $28.0\%$ vs $28.77\%\,\text{wb}$ drained moisture. |
| **#4** | **EXP-04:** ISO 11136:2014 Consumer TOST Sensory Equivalence & Triangle Panel | `Module F` Indian Reference Flavour Equivalence & Zero Aftertaste | ₹45,000 | **3 Days** | $90\%$ CI of $(\mu_{\text{FinnoaQ}} - \mu_{\text{IndianRef}})$ within $[-0.75, +0.75]$ on 9-point scale ($N=72$). |
| **#5** | **EXP-05:** Two-Stage 65°C→55°C Drying Fissure & 10-Cycle 85% Bath Recycle Trial | `Module H` (`FAIL-0021` & `FAIL-0025` fixes) | ₹65,000 | **5 Days** | Broken grain loss $< 0.8\%$; 10-cycle recycled bath maintains $\le 2$-whistle cookability without microbial spoilage. |

---

## 2. Detailed Experimental Protocols, Controls & Statistical Decision Rules

### EXP-01: Buffer Stoichiometry pH Verification & Rapid Intake Proxy Calibration
* **Hypothesis Tested:** Dissolution of $26.07\,\text{g/L}$ $\text{K}_3\text{Cit}\cdot\text{H}_2\text{O} + 2.63\,\text{g/L}$ $\text{Na}_3\text{Cit}\cdot 2\text{H}_2\text{O} + 10.69\,\text{g/L}$ Anhydrous Citric Acid yields $\text{pH } 5.20 \pm 0.05$ at $25^\circ\text{C}\text{--}55^\circ\text{C}$ (correcting the legacy SOP recipe that equilibrated at $\text{pH } 6.76$).
* **Measurements Required:**
  1. Prepare $1.00\,\text{L}$ of the corrected OMEGA Tier 2 buffer and $1.00\,\text{L}$ of the legacy SOP recipe in deionized and municipal tap water ($50\text{--}150\,\text{ppm}$ hardness). Measure pH with a 2-point calibrated glass electrode ($\text{pH } 4.01$ and $7.00$ NIST buffers) at $25^\circ\text{C}$ and $55^\circ\text{C}$.
  2. Sample $N = 50$ split cotyledons from 3 commercial lots (Indian Latur fresh, Tanzanian Arusha/Dodoma, Tanzanian aged maritime). Measure full split thickness $2H$ via digital micrometer ($\pm 0.01\,\text{mm}$), initial moisture $X_{\text{wb}}$ via halogen moisture analyzer, and 3-minute $55^\circ\text{C}$ warm water gravimetric swelling index ($\text{WAI}_{3\text{min}}$).
  3. Digest $5.0\,\text{g}$ ground subsamples via $\text{HNO}_3/\text{H}_2\text{O}_2$ microwave digestion for ICP-OES total and alcohol-insoluble-solid (AIS) bound $\text{Ca}^{2+}/\text{Mg}^{2+}$.
* **Success / Falsification Rule:** If measured pH deviates from $5.20$ by $>0.08$ units, adjust ionic-strength activity coefficient parameter in `Module D`. Fit empirical regression $\hat{C}_{\text{Ca}} = f(H_{\text{obs}}, \text{WAI}_{3\text{min}}, \sigma_{\text{leach}})$ and verify $R^2 \ge 0.75$.

### EXP-02: Two-Sieve Multi-Duration Steeping & Whistle-2 Core Shear Trial (Breaking $D_{\text{cit}}$ vs. $k_{\text{chel}}$ Collinearity)
* **Hypothesis Tested:** Ultrasonic cavitation ($40\,\text{kHz}$, $17\,\text{W/L}$) at $55^\circ\text{C}$ in $0.145\,\text{M}$ K/Na Citrate ($\text{pH } 5.20$) reduces required steeping time from $40\text{--}45\,\text{min}$ (static) to **$15\text{--}20\,\text{min}$**, achieving $F_{\text{WB,core}} \le 18.0\,\text{N}$ at Whistle 2 ($t \approx 9.0\,\text{min}$). Furthermore, Vacuum Impregnation alone at $4.6\,\text{min}$ **fails** to soften the core (`FAIL-0023` proof).
* **Experimental Design (Full Factorial $2 \times 2 \times 5$ with $n = 3$ replicates = 60 runs):**
  * **Factor A (Sieve Thickness Fraction):** Thin splits ($2H = 1.80 \pm 0.10\,\text{mm}$) vs. Thick splits ($2H = 2.30 \pm 0.10\,\text{mm}$). *Why two thicknesses?* Diffusion time scales with $H^2$ whereas local ligand exchange $k_{\text{chel}}$ is independent of $H$; measuring both thicknesses simultaneously makes $D_{\text{cit}}$ and $k_{\text{chel}}$ uniquely identifiable!
  * **Factor B (Intensification Mode):** Static warm bath ($0\,\text{W/L}$) vs. Ultrasonic bath ($40\,\text{kHz}$, $17\,\text{W/L}$ calorimetrically calibrated) + a separate Vacuum Pulse arm ($15\,\text{kPa abs}$ for $2\,\text{min}$ + $2.6\,\text{min}$ vs $13\,\text{min}$ atmospheric restoration).
  * **Factor C (Steeping Duration):** $5, 10, 15, 20, 30\,\text{min}$ at $55^\circ\text{C}$.
* **Response Variables:**
  1. Gravimetric moisture uptake $M(t)$ ($\text{kg/kg db}$).
  2. Sectioned outer-rim vs. inner-core bound $\text{Ca}^{2+}$ via ICP-OES at $t = 10$ and $20\,\text{min}$.
  3. Domestic pressure cooking (Hawkins Classic 3L on calibrated $1,400\,\text{W}$ induction burner, stopped after Whistle 2): Warner-Bratzler / Ottawa Kramer peak shear force $F_{\text{WB,bulk}}$ and micro-puncture core force $F_{\text{WB,core}}$ ($\text{N}$), plus razor bisection chalky-core incidence ($\%$).

### EXP-03: Spray-Wash Conductivity Washout & Pre-Dryer Dewatering Screen Moisture Trial
* **Hypothesis Tested:** A 12-second dual-fan flat-spray rinse ($2.5\,\text{bar}$, $0.50\,\text{L/kg}$) strips $>98\%$ of external surface film salts without leaching internal pore citrate, and resolves the **Scenario B1 ($28.00\%\,\text{wb}$) vs. Scenario B2 ($28.7735\%\,\text{wb}$)** pre-dryer moisture discrepancy.
* **Protocol:**
  1. Steep $5.0\,\text{kg}$ batches of Tanzanian dal for $20\,\text{min}$ at $55^\circ\text{C}$, discharge onto a $1.5\,\text{mm}$ wedge-wire vibrating screen ($50\,\text{Hz}$, $3\,\text{mm}$ amplitude), and spray-rinse for $t_{\text{wash}} \in \{0, 5, 10, 12, 15, 25\}\,\text{s}$.
  2. Measure drained dal total moisture content via oven drying ($105^\circ\text{C}$ for $16\,\text{h}$, $n = 6$ replicates) at $30, 60,$ and $120\,\text{s}$ screen residence time to establish the exact pre-dryer moisture entering `DR-101`.
  3. Measure surface-rinse leachate electrical conductivity ($\mu\text{S/cm}$), surface pH, and dry-grain retained $\text{Na}^+$, $\text{K}^+$ (flame photometry / ICP-OES), and citrate (HPLC-UV).

### EXP-04: Consumer Sensory Equivalence (ISO 11136:2014 TOST) & Trained Triangle Panel
* **Hypothesis Tested:** Conditioned + 12-s spray-washed Tanzanian toor dal is sensorially equivalent to authentic Indian Latur reference dal within $\Delta_{\text{eq}} = \pm 0.75$ hedonic scale points and exhibits zero detectable soapy/metallic off-taste.
* **Protocol (Per ISO 11136:2014 / Catalogue 50125 & Bi & Meyners 2012):**
  1. **Phase 4A — Trained Panel Triangle Discrimination Test ($N = 24$ trained assessors):** Compare Unspiced Boiled Slurry ($1:3.5$ dal:water, $0.5\%$ $\text{NaCl}$ only) of (i) Rinsed $\text{NaHCO}_3$ Tier 1, (ii) Rinsed 90:10 K/Na Citrate Tier 2, and (iii) Unwashed 90:10 K/Na Citrate against Indian Reference Dal to quantify Thurstonian $d'$ and off-taste recognition frequency.
  2. **Phase 4B — Consumer Hedonic TOST Equivalence Study ($N = 72$ regular Indian toor dal consumers, 12 replications of 6-sequence Williams Latin Square):**
     * **Samples (Blind 3-Digit Codes):** Sample `418` (Authentic Indian Latur Reference), Sample `705` (FinnoaQ Tier 2 Conditioned Tanzanian Dal), Sample `293` (Untreated Tanzanian Dal cooked for 2 whistles — negative control).
     * **Statistical Decision Rule (Two One-Sided Tests at $\alpha = 0.05$):** Reject non-equivalence and declare **Verified Sensory Equivalence** if and only if:
       $$T_{\text{lower}} = \frac{(\bar{Y}_{\text{FinnoaQ}} - \bar{Y}_{\text{Indian}}) - (-0.75)}{s_d / \sqrt{N}} > t_{0.95, N-1} \quad \text{AND} \quad T_{\text{upper}} = \frac{0.75 - (\bar{Y}_{\text{FinnoaQ}} - \bar{Y}_{\text{Indian}})}{s_d / \sqrt{N}} > t_{0.95, N-1}$$

### EXP-05: Pilot Two-Stage Drying Stress Cracking & 85% Bath Recycle Longevity Trial
* **Hypothesis Tested:** Two-stage convective drying ($65^\circ\text{C}$ for $22\,\text{min} \rightarrow 55^\circ\text{C}$ for $25\,\text{min} + 20\,\text{min}$ adiabatic tempering) maintains broken/fissured grain loss $< 0.8\%$ (vs $>4.5\%$ under $85^\circ\text{C}$ single-stage drying), and $85\%$ micro-filtered bath recycling operates stably over 10 consecutive cycles.
* **Protocol:**
  1. Dry paired $10\,\text{kg}$ conditioned lots under Regime D1 ($85^\circ\text{C}$ single-stage) vs. Regime D4 ($65^\circ\text{C} \rightarrow 55^\circ\text{C} + 20\,\text{min}$ tempering). Quantify hairline stress fissures via stereomicroscopy ($N=200$ grains) and mechanical breakage after pneumatic conveying / bucket-elevator drop testing.
  2. Execute 10 sequential steeping cycles with $85\%$ liquor recovery through a $10\,\mu\text{m}$ polypropylene bag filter + $15\%$ blowdown + stoichiometric make-up dosing. Monitor bath free $[\text{Cit}^{3-}]$, chelated $[\text{CaCit}^-]$, total dissolved solids (Brix/conductivity), saponin foam height, and total aerobic plate count (CFU/mL) at $55^\circ\text{C}$.

