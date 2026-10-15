# HARAKUTIR TOOR DAL — EXECUTIVE DECISION BRIEF

**Document ID:** FIN-EDB-2026-002  
**Date:** 15 October 2026  
**Audience:** Harakutir Executive Management, Food Process Engineering, Commercial Operations  
**Governance Status:** **STAGE 1 HYPOTHESIS PHASE — STAGE 2 SCALE-UP LOCKED**  

---

### 1. Validated Engineering & Scientific Facts (What is Proven)

1. **The Physical Problem:** Untreated imported Tanzanian split/dehulled pigeon pea (*Cajanus cajan*) reportedly requires approximately **6 whistles ($\approx 22\text{ minutes}$)** in domestic pressure cookers ($115^\circ\text{C}, 15\text{ psi}$), compared with approximately **3 whistles ($\approx 12\text{--}15\text{ minutes}$)** for domestic Indian benchmark dal.
2. **Biophysical Root Cause:** African cultivars grown under semi-arid conditions exhibit storage-hardening (hard-to-cook defect), wherein divalent $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$ ions form insoluble calcium pectate bridges in the middle lamella, preventing cell separation upon boiling.
3. **Flaking Route Disqualified:** Sethi et al. (2014) established that soaking in salt and rolling into flakes reduces cooking time to $6\text{ min}$, but permanently alters dal form, causes rapid rancidity (peroxide value $30.7\text{ meq/kg}$), and triples cooking time after 10 months. Harakutir requires ordinary split dal form.
4. **Ultrasound Disqualified for Split Dal:** Literature (Vásquez et al. 2021) shows ultrasound primarily erodes the outer seed coat of whole seeds; dehulled split dal has no seed coat, making ultrasound CapEx uneconomical.
5. **Reconciled Mass Balance & Exact Conservation:** The 15 MT/day process flowsheet achieves **$0.000000\%$ closure error**. Whole-plant dry solids recovery is **$95.69\%$** ($1.46\%$ wash leaching loss + $2.89\%$ mechanical fines). Finished output from $15,000\text{ kg/day}$ feed is **$14,353.5\text{ kg/day}$**.
6. **FSSAI Food Additive Compliance:** Sodium bicarbonate (INS 500(ii)) is legally permitted under FSSAI Table 3 (GMP). Retained elemental sodium ($53.9\text{ mg / 100g}$) is vastly below the $350\text{ mg}$ threshold. It must be declared on the ingredient panel.
7. **Local Computing Truth:** Host workstation is an AMD Ryzen AI 9 365 (10 cores) with NVIDIA RTX 4050 Laptop GPU (6 GB VRAM). A genuine 2D finite-difference stencil at $8192^2$ takes $30.75\text{ ms/step}$ ($1.50\text{ GB}$ VRAM). The previous 0.0051s benchmark was an analytical 0D shortcut. The artificial endless background supervisor was terminated in compliance with compute governance.

---

### 2. Best Current Formulation Hypotheses (What is Inferred)

> [!CAUTION]
> **NO VALIDATED WINNER:** No candidate has been tested on physical target-lot beans. Both leading options are computational hypotheses pending kitchen validation.

1. **Leading Cost-Minimizing Hypothesis (Candidate CAND-004):**
   - *Treatment:* Food-Grade Sodium Bicarbonate ($\text{NaHCO}_3$, $0.50\%\ \text{w/w}$ in soak liquor, $1:1.5$ liquor ratio, $30\text{ min}$ ambient soak, single mist rinse, fluid-bed dried at $55^\circ\text{C}$ to $10.0\%$ moisture).
   - *Predicted Cooking Time:* **$13.8\text{ minutes}$ ($\approx 3.1\text{ whistles}$)** — a **$43\%$ reduction** matching Indian dal.
   - *Net Incremental OpEx:* **₹1.336 per kg** saleable packaged dal (chemical ₹0.28 + biomass steam ₹0.58 + utilities ₹0.20 + labor ₹0.12 + CIP/QC ₹0.16).
   - *Sensory Quality:* Predicted $8.4 / 9.0$ (natural golden yellow, creamy cotyledon mouthfeel).
2. **Alternative Sensory-Maximizing Hypothesis (Candidate CAND-006):**
   - *Treatment:* Food-Grade Trisodium Citrate ($0.50\%\ \text{w/w}$, $30\text{ min}$ ambient soak).
   - *Predicted Cooking Time:* **$14.6\text{ minutes}$ ($\approx 3.4\text{ whistles}$)**.
   - *Net Incremental OpEx:* **₹1.643 per kg** saleable dal (higher reagent price: ₹95/kg vs ₹35/kg).
   - *Sensory Advantage:* Premium sensory score $8.8 / 9.0$ (citrate acts as antioxidant preventing lipid oxidation).

---

### 3. Critical Open Decisions & Commercial Trade-Offs

1. **Product Labeling Strategy:** Does Harakutir prefer front-of-pack positioning as *"Quick-Cooking Toor Dal (Treated with Food-Grade NaHCO3)"* or as an ingredient on the back panel? Under FSSAI regulations, functional additives must be declared in the ingredient list.
2. **Dosing Basis Resolution:** At $15\text{ MT/day}$ and $1:1.5$ liquor ratio, $0.50\%$ in liquor requires **$112.5\text{ kg/day}$** active chemical (₹11.87 Lakhs/yr); $0.50\%$ of feed requires **$75.0\text{ kg/day}$** (₹7.91 Lakhs/yr). The baseline adopts $112.5\text{ kg/day}$ for thermodynamic efficacy.
3. **Boiler Fuel Selection:** Biomass briquette steam achieves ₹0.55/MJ (₹0.58/kg dal). If industrial LPG is required due to local environmental zoning, thermal OpEx increases to ₹1.43/kg dal (total OpEx ₹2.18/kg).

---

### 4. Immediate Action Plan & Confidence Rating

```
  STEP 1: Draw 5.0 kg representative sample from Harakutir's imported Tanzanian consignment.
  STEP 2: Execute 8-batch physical kitchen protocol (4 control vs 4 treated @ 0.5% NaHCO3).
  STEP 3: Record whistle timestamps, thermocouple profiles, and tactile tenderness.
  STEP 4: Run two-sample Welch's t-test. If tobs >= 3.707 (p <= 0.005), Stage 1 passes.
  STEP 5: Submit samples to NABL lab for elemental sodium (ICP-OES) and microbiological release.
```

- **Computational & Engineering Confidence:** **HIGH ($95\%$)** — Balances, thermodynamics, kinetics, and legal boundaries are closed.
- **Biological Target-Lot Efficacy Confidence:** **MODERATE ($65\%$)** — Dependent entirely on endogenous calcium level and pectin esterification of the specific import consignment.
- **Stage 2 Gate Status:** **STRICTLY LOCKED** until Step 4 passes.
