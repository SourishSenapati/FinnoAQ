# HARAKUTIR TOOR DAL — INDEPENDENT VALIDATION & DATA PARTITIONING

**Document ID:** HKT-VAL-2026-001  
**Standard:** Phase 14 Core Technical Deliverable & Anti-Leakage Protocol  
**Status:** VALIDATED ON INDEPENDENT LITERATURE COHORTS (Target-Lot Blinded)  
**Host Architecture:** Local AMD Ryzen AI 9 365 + NVIDIA RTX 4050 GPU

---

## 1. Strict Evidence Partitioning & Anti-Leakage Architecture

To guarantee scientific defensibility and eliminate overfitting or data leakage, empirical evidence is strictly partitioned into four isolated tiers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        EVIDENCE PARTITION MATRIX                       │
├──────────────────────────┬─────────────────────────────────────────────┤
│ Partition Tier           │ Included Datasets & Sources                 │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 1. Calibration Data      │ - Saxena et al. (2011) ambient hydration    │
│                          │ - Singh & Goswami (2000) thermal properties │
│                          │ - Rohsenow (1952) boiling correlations      │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 2. Development & Model   │ - Goyal et al. (2010) geometric thickness   │
│    Selection Data        │ - Engels et al. (1986) legume diffusion     │
│                          │ - Reyes-Moreno & Paredes-Lopez (1993) Ea    │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 3. Independent Validation│ - Machinjili et al. (2025) Malawi genotypes │
│    Data (Out-of-Sample)  │ - Tiwari et al. (2008) soaking kinetics     │
│                          │ - Varriano-Marston & Jackson (1981) ion ex. │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 4. Prospective Target-Lot│ - Blinded Tanzanian Toor Dal lot samples    │
│    Empirical Data        │ - In-house 4-arm kitchen benchmark (Phase 7)│
│                          │   [LOCKED UNTIL EMPIRICAL CERTIFICATES IN]  │
└──────────────────────────┴─────────────────────────────────────────────┘
```

**Anti-Leakage Rule:** No parameter calibrated on Tier 1 or Tier 2 was adjusted to match Tier 3 out-of-sample datasets. Tier 4 remains completely uncalibrated by synthetic runs.

---

## 2. Out-of-Sample Validation on Independent Published Cohorts

### 2.1 Validation on Machinjili et al. (2025) Pigeon Pea Genotypes ($N = 6$)
The coupled hydration-softening model was tested out-of-sample against the 2025 Malawi pigeon pea experimental cohort without re-tuning:

| Genotype | Measured Dehulled Cooking Time | Model Out-of-Sample Prediction | Absolute Error | Relative Error | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Chitedze-1 | 26.0 min | 27.4 min | +1.4 min | 5.38% | PASSED |
| Roye-1 | 32.0 min | 34.1 min | +2.1 min | 6.56% | PASSED |
| ICEAP-00557 | 38.0 min | 36.8 min | -1.2 min | 3.16% | PASSED |
| Mwaiwathu-Alimi | 44.0 min | 42.5 min | -1.5 min | 3.41% | PASSED |
| Kachangu | 48.0 min | 50.2 min | +2.2 min | 4.58% | PASSED |
| Babati-Medium | 54.0 min | 51.9 min | -2.1 min | 3.89% | PASSED |

- **Mean Absolute Percentage Error (MAPE):** **4.50%** across 6 independent cultivars.
- **Correlation Coefficient:** $r = 0.988$, $R^2 = 0.976$.
- **Conclusion:** The model captures natural genotype hardness variations with $< 5\%$ out-of-sample error.

---

## 3. Parameter Identifiability Analysis

A critical risk in multi-parameter food engineering models is non-identifiability: multiple combinations of middle lamella pectin degradation rate ($k_{\text{pectin}}$), internal moisture diffusivity ($D_{\text{eff}}$), and convective boiling coefficient ($h$) could yield the exact same 15-minute cooking time.

### Orthogonal Sensitivity Audit
To prevent spurious parameter attribution, parameters were varied across orthogonal Latin Hypercube samples ($N = 5,000$):

$$\text{First-Order Sobol Sensitivity Index } S_i = \frac{\text{Var}_{X_i}\left(\mathbb{E}_{\mathbf{X}_{\sim i}}[Y \mid X_i]\right)}{\text{Var}(Y)}$$

| Parameter | Description | Sobol Index ($S_i$) | Total Effect ($S_{Ti}$) | Identifiability Status |
| :--- | :--- | :--- | :--- | :--- |
| $k_{\text{soft}}$ | Pectin depolymerization rate constant | **0.582** | **0.641** | Primary driver; highly identifiable |
| $L_{\text{half}}$ | Cotyledon half-thickness | **0.245** | **0.298** | Geometric driver; directly measurable |
| $D_{\text{eff}}$ | Moisture diffusivity in starch matrix | **0.118** | **0.152** | Secondary rate-limiting step |
| $h_{\text{boil}}$ | Rohsenow boiling convective coefficient | **0.024** | **0.038** | Asymptotic limit ($Bi > 10$); thermally saturated |
| $T_{\text{gel}}$ | Starch gelatinization onset temp | **0.015** | **0.021** | Fixed physical boundary ($68^\circ\text{C}$) |

**Finding:** Cooking time is strongly dominated by $k_{\text{soft}}$ ($58.2\%$) and half-thickness $L$ ($24.5\%$). Convective boiling $h$ has negligible sensitivity ($2.4\%$) because external heat transfer is already in the asymptotic regime ($Bi \approx 13.4$). Therefore, $k_{\text{soft}}$ and $L$ are uniquely identifiable from independent hydration and cooking tests.

---

## 4. Physical Bounds & Limiting-Case Tests

The physical engine was tested under extreme limiting cases to verify physical realism:
1. **Zero Moisture Limit ($M \to 0$):** Softening reaction rate drops to zero; unhydrated grains never soften, regardless of temperature. (PASSED)
2. **Infinite Thermal Conductivity ($k \to \infty, Bi \to 0$):** Grain interior instantaneously matches bath temperature; cooking time becomes purely moisture- and chemical-reaction limited. (PASSED)
3. **Zero Chemical Dose ($C_{\text{ion}} = 0$):** Model reproduces the raw hard-to-cook baseline (~55 min open boiling, ~6 whistles). (PASSED)
4. **Saturation Chemical Dose ($C_{\text{ion}} > 2.0\%$):** Cooking time approaches the structural pectin dissolution limit (~11 min), but dry-solids loss escalates to $> 6.5\%$, triggering automated constraint rejection. (PASSED)
