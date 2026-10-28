# Experimental Design & Cooking Test Protocol

**Project Reference:** FNQ-PR-2026-001 | Phase 1 Diagnostic R&D Study  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Document Ref:** FNQ-REP-EXP-001  
**Date:** 20 October 2026  
**Governing Standard:** Section 5 (Criticism C), Section 6 (Criticism D), and Section 7 (Standardized Cooking)  

---

## 1. Executive Summary & Experimental Philosophy

The objective of this protocol is to replace unstandardized household observations (e.g. pressure cooker "whistle counts") with an **instrumented, reproducible, mathematically closed experimental methodology**. Under workspace governance:
- **No experimental data may be fabricated or simulated.** Planned tests must remain explicitly designated as `PLANNED` until physical execution.
- Experimental replication must be strictly partitioned across **independent source lots, independent treatment batches, and technical replicates**.
- Chemical treatment screening belongs to **gated Phase 2**; Phase 1 remains focused on comparative diagnostic characterization between the Tanzanian target and domestic Indian benchmark.

---

## 2. Three-Tier Replication Architecture (Finding D)

To ensure statistical validity and prevent false claims of precision, all experimental work is designed across three nested replication tiers:

```text
========================================================================================================
EXPERIMENTAL REPLICATION HIERARCHY
========================================================================================================
Level                   Definition & Scope                          Minimum Size    Statistical Purpose
--------------------------------------------------------------------------------------------------------
Tier 1: Source Lots     Commercially independent consignments,      2 Lots (Opt 1)  Quantifies natural agricultural
                        seasons, or import shipments.               4 Lots (Opt 2)  and maritime transit variance.
Tier 2: Prep Batches    Independently prepared aliquots of grain    3 Batches       Quantifies soaking, draining,
                        undergoing an experimental step separately. per lot         and preparation variance.
Tier 3: Tech Repeats    Repeated instrumental measurements or       3 Repeats       Quantifies analytical tool and
                        sensor readings from the same batch.        per batch       operator measurement error.
--------------------------------------------------------------------------------------------------------
Total Observations      3 batches x 3 repeats = 9 measurements per analytical parameter per lot.
========================================================================================================
```

---

## 3. Sample Allocation Budget (2.5–3.0 kg per Lot)

The standard commercial consignment sample of **2,500 g to 3,000 g per lot** is allocated across the diagnostic work packages:

| Module ID | Analytical Activity & Replicate Structure | Mass Allocation (g) | Allocation Basis & Standard Reference |
| :---: | :--- | :---: | :--- |
| **MOD-01** | Physical & Grain Geometry (Dimensions, 1000-grain mass, bulk density, visual defects) | 200 g | Non-destructive; grains inspected per IS 4333 (Part 1). |
| **MOD-02** | Proximate Composition (Moisture, protein, crude fat, crude fiber, total ash) | 150 g | Finely ground sample; AOAC 925.10, 990.03, 920.39. |
| **MOD-03** | Starch Fractionation & Thermal Profiling (Amylose/amylopectin, DSC gelatinization) | 100 g | Defatted starch extract; DSC run in triplicate ($10\text{ mg}$ pans). |
| **MOD-04** | Hydration & Swelling Kinetics (25°C, 40°C, 60°C time-course; Peleg rate modeling) | 300 g | 3 temperatures x 3 independent batches x 25 g. |
| **MOD-05** | Pectin & Middle Lamella Chemistry (Water-, oxalate-, alkali-soluble fractions, DE) | 150 g | Alcohol-insoluble residue (AIR) preparation; m-hydroxydiphenyl assay. |
| **MOD-06** | Mineral & Phytate Profiling (ICP-OES Ca, Mg, P, K; enzymatic phytate assay) | 150 g | Acid digestion; ICP-OES in triplicate. |
| **MOD-07** | Texture & Grain Hardness (Raw grain compression, soaked grain shear firmness) | 200 g | Texture Profile Analysis (TPA) on 50 grains per batch. |
| **MOD-08** | Standardized Instrumented Cooking Performance (Autoclave cooking curve; hard-core assay) | 600 g | 6 time points x 3 batches x 30 g aliquots. |
| **MOD-09** | Confounder Evaluation (Deionized water vs. 300 ppm hard water comparative cooking) | 200 g | Paired cooking comparison under standardized heat input. |
| **MOD-10** | Sealed Quality Control & Chain-of-Custody Archival Reserve | 550 g | Hermetically sealed, nitrogen-flushed, stored at 4°C for re-testing. |
| **TOTAL** | **Total Scoped Mass Budget per Sample Consignment** | **2,700 g (2.7 kg)** | **Fits comfortably within 2.5–3.0 kg sample brief.** |

---

## 4. Standardized Cooking Performance Protocol

### 4.1 De-Coupling from Whistle Counts
Household cooker "whistles" fluctuate widely based on cooker capacity (3L vs 5L), burner heat flux, fill ratio, venting spring tension, and atmospheric pressure. This protocol replaces whistle counts with an **objective, instrumented cooking curve**:

### 4.2 Standardized Apparatus & Operating Parameters
1. **Cooking Chamber:** Calibrated, temperature-controlled laboratory autoclave / pressurized reaction vessel.
2. **Temperature & Pressure:** Maintained at exactly **$115.0 \pm 0.5^\circ\text{C}$** and **$105 \pm 2\text{ kPa}$ ($1.05\text{ bar} / 15.2\text{ psi}$)**.
3. **Liquor Ratio:** Exactly **1:4 (w/w)** grain-to-liquid ratio (25.0 g dry dal in 100.0 g liquid).
4. **Cooking Liquid:** Grade 1 Demineralized Water (electrical conductivity $< 0.1\ \mu\text{S/cm}$, pH $6.8 \pm 0.2$).
5. **Thermocouple Logging:** Calibrated Type-K thermocouple immersed in central grain bed; logged at 1.0 Hz to confirm time-to-temperature ($t_{\text{ramp}} \le 3.0\text{ min}$).

### 4.3 Time-Course Sampling & Hard-Core Determination
- Aliquots are cooked at intervals: **10, 15, 20, 25, 30, and 35 minutes**.
- At each interval, the vessel is rapidly decompressed and cooled via cold water jacket within 45 seconds.
- Grains are drained for 60 seconds on a 1.0 mm stainless steel wire mesh screen.
- **Objective Tenderness Endpoint:** 50 individual cooked grains are compressed between two parallel optically polished glass plates under a standardized static load of **$500\text{ g}$ ($4.90\text{ N}$) for 10 seconds** (adapted from Narasimha & Desikachar, 1978).
- **Hard-Core Index ($I_{\text{hc}}$):**
  $$I_{\text{hc}} = \frac{N_{\text{hard}}}{N_{\text{total}}} \times 100\%$$
  where $N_{\text{hard}}$ is the number of grains retaining an opaque, ungelatinized chalky core.
- **Cooking Time ($T_{90}$):** Defined as the exact cooking duration at which $\ge 90.0\%$ of grains achieve complete softness ($I_{\text{hc}} \le 10.0\%$).

---

## 5. Candidate Treatment Screening Formulations (Gated Phase 2 Protocol)

If Phase 1 diagnostics indicate that cell wall calcification (H4/H5) or hydration resistance (H1) is present, the following chemically distinct treatment protocols are formally pre-specified for Phase 2 approval:

| Treatment ID | Reagent System | Chemical Formula & Purity | Concentration Basis | Liquor:Grain Ratio | Temp & Duration | Target pH | Rinsing & Drying Protocol |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **TRT-00 (Control)** | Untreated Control | Raw intact split dal | N/A (None) | None | Ambient | Natural | No processing; tested as received. |
| **TRT-01 (Water Control)** | Pure Water Soak | Demineralized $\text{H}_2\text{O}$ | Pure water | 1.5:1 (w/w) | 25°C, 30 min | 6.8 | 5 min drain; dry at 50°C to 10.0% WB. |
| **TRT-02 (Bicarbonate)** | Sodium Bicarbonate | $\text{NaHCO}_3$ (Food Grade, 99.5%) | 0.50% w/w relative to dry dal solids | 1.5:1 (w/w) | 25°C, 30 min | 8.2–8.4 | 5 min drain; 2x fresh water wash; dry at 50°C to 10.0% WB. |
| **TRT-03 (Citrate Buffer)** | Sodium Citrate System | Trisodium citrate + citric acid | 0.05 M citrate buffer (Food Grade) | 1.5:1 (w/w) | 25°C, 30 min | 5.5 | 5 min drain; 2x fresh water wash; dry at 50°C to 10.0% WB. |
| **TRT-04 (Carbonate)** | Sodium Carbonate | $\text{Na}_2\text{CO}_3$ (Food Grade, 99.0%) | 0.25% w/w relative to dry dal solids | 1.5:1 (w/w) | 25°C, 20 min | 10.2 | 5 min drain; intensive 3x rinse; dry at 50°C to 10.0% WB. |
| **TRT-05 (Hydrothermal)** | Thermal Conditioning | Demineralized $\text{H}_2\text{O}$ | Pure water | 2.0:1 (w/w) | 85°C, 10 min | 6.8 | Rapid quench in cold water; dry at 50°C to 10.0% WB. |

**Important Distinction:** Trisodium citrate ($\text{Na}_3\text{C}_6\text{H}_5\text{O}_7$) is a calcium-chelating buffering agent acting at slightly acidic pH ($5.5$), whereas sodium carbonate ($\text{Na}_2\text{CO}_3$) is an alkaline saponifying agent acting at $\text{pH} > 10.0$. They are chemically distinct and must never be conflated.

---

## 6. Statistical Hypothesis Testing & Decision Limits

1. **Comparison Test:** Welch’s two-sample $t$-test (robust against unequal variances) comparing $T_{90}$ of Tanzanian vs. Indian lots:
   $$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$
2. **Significance Threshold:** $\alpha = 0.01$ ($99\%$ confidence).
3. **Power Analysis Limitations:** With $n=3$ independent preparation batches, the test has statistical power $1 - \beta \ge 0.80$ only for large effect sizes ($\Delta \ge 2.5\sigma$). If cooking differences are subtle ($\le 2\text{ min}$), expanded replication ($n \ge 6$) will be triggered before drawing conclusions.
4. **Data Exclusion Policy:** No outlier may be excluded without documented instrument error, seal leakage, or temperature excursion during the run. All exclusions must be recorded in `docs/experiments/EXPERIMENT_REGISTER.xlsx`.
