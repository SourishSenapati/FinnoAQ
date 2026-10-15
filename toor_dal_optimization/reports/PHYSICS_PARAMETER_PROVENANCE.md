# HARAKUTIR TOOR DAL — PHYSICS & PARAMETER PROVENANCE REGISTER

**Document ID:** HKT-PROV-2026-001  
**Audit Reference:** [`CRITICAL_SCIENTIFIC_AUDIT.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/CRITICAL_SCIENTIFIC_AUDIT.md)  
**Governing Standard:** Scientific Traceability & Epistemic Honesty Directive  
**Date:** 2026-10-15  

---

## 1. Executive Scientific Statement on Biophysical Claims

> [!IMPORTANT]
> **Fundamental Audit Rule:** A Python class that computes an output does **not** constitute a validated molecular digital twin. An algebraic equation that yields a plausible cooking time does **not** prove that the hypothesized biochemical pathway occurs in Harakutir's physical dal lot.

All molecular and biochemical mechanisms proposed in earlier reports (PME de-esterification, phytase cleavage, calcium pectate crosslinking, and monovalent ion exchange) are hereby classified as **Uncalibrated Working Biophysical Hypotheses**. They are grounded in general pulse science, but their numerical parameters have **never been calibrated on physical wet-lab measurements of the target Tanzanian pigeon pea lot**.

---

## 2. Parameter Provenance & Epistemic Classification Taxonomy

Every physical parameter used in the simulation models is categorized under one of six epistemic classifications:
1. `MEASURED_TARGET_LOT`: Directly measured on Harakutir's specific Tanzanian pigeon pea lot.
2. `MEASURED_OTHER_PIGEON_PEA`: Measured on other pigeon pea (*Cajanus cajan*) cultivars in published literature.
3. `LITERATURE_SOURCED`: Sourced from other dry legumes (beans, chickpeas, cowpeas) or standard physical handbooks.
4. `FITTED`: Calibrated by regression against independent empirical data.
5. `ASSUMED`: Engineering estimate based on heuristic physical reasoning.
6. `SYNTHETIC`: Artificial benchmark constant constructed for software testing.

---

## 3. Comprehensive Physical Parameter Ledger

| Parameter Symbol | Description | Numerical Value | Physical Units | Provenance Category | Primary Source Citation / Basis | Status / Limitation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$R$** | Cotyledon Major Radius | $3.25 \times 10^{-3}$ | $\text{m}$ (3.25 mm) | `MEASURED_TARGET_LOT` | Physical calliper measurements on Harakutir sample lot. | Verified physical geometry. |
| **$H/2$** | Cotyledon Half-Thickness | $1.30 \times 10^{-3}$ | $\text{m}$ (1.30 mm) | `MEASURED_TARGET_LOT` | Physical calliper measurements on Harakutir sample lot. | Verified physical geometry. |
| **$M_0$** | Initial Grain Moisture | $0.105$ | $\text{g H}_2\text{O / g wet dal}$ (10.5%) | `MEASURED_TARGET_LOT` | In-house moisture analyzer certificate. | Verified physical baseline. |
| **$\rho_{\text{dal}}$** | Bulk Dal Grain Density | $1350.0$ | $\text{kg/m}^3$ | `MEASURED_OTHER_PIGEON_PEA` | Goyal et al. (2010), *Int. J. Food Prop.* | Representative legume density. |
| **$\alpha_{\text{th}}$** | Thermal Diffusivity | $1.121 \times 10^{-7}$ | $\text{m}^2/\text{s}$ | `LITERATURE_SOURCED` | Singh & Goswami (2000); Sweat (1986). | Standard pulse food property. |
| **$c_{p,\text{dal}}$** | Grain Specific Heat | $1.85$ | $\text{kJ/(kg}\cdot\text{K)}$ | `LITERATURE_SOURCED` | Standard food engineering correlation. | Standard pulse property. |
| **$D_m$** | Baseline Moisture Diffusivity | $2.40 \times 10^{-11}$ | $\text{m}^2/\text{s}$ | `FITTED` | Fitted to Machinjili et al. (2025) pigeon pea hydration kinetics ($R^2 = 0.994$). | Good general cultivar fit; uncalibrated on target lot. |
| **$E_{a,\text{diff}}$** | Moisture Diffusion Activation Energy | $32,400.0$ | $\text{J/mol}$ | `LITERATURE_SOURCED` | Peleg & Saguy (1988); Sopade et al. (1992). | General legume mass transfer. |
| **$D_{\text{Na}}$** | Sodium Ion Diffusivity (25°C) | $1.25 \times 10^{-10}$ | $\text{m}^2/\text{s}$ | `LITERATURE_SOURCED` | Robinson & Stokes (2002); aqueous electrolyte handbook. | Free aqueous electrolyte value; tortuosity assumed. |
| **$DE_0$** | Initial Degree of Esterification | $0.58$ | Dimensionless ($0\text{--}1$) | `ASSUMED` | Adapted from aged navy bean literature (Liu et al., 1992). | **NOT measured on target lot.** |
| **$[\text{Ca}^{2+}]$** | Total Endogenous Calcium | $73.0$ | $\text{mg / 100g dal}$ | `MEASURED_OTHER_PIGEON_PEA` | USDA FoodData Central / ICRISAT pigeon pea database. | Cultivar average; target lot unassayed. |
| **$[\text{PA}]$** | Phytic Acid Content | $850.0$ | $\text{mg / 100g dal}$ | `MEASURED_OTHER_PIGEON_PEA` | Dahiya et al. (1982), *J. Sci. Food Agric.* | Literature estimate. |
| **$T_{d,\text{vicilin}}$** | Vicilin (7S) Denaturation Temp | $82.5$ | $^\circ\text{C}$ | `LITERATURE_SOURCED` | Marcone et al. (1998), DSC thermograms of grain globulins. | Standard legume biophysics. |
| **$T_{d,\text{legumin}}$** | Legumin (11S) Denaturation Temp | $91.0$ | $^\circ\text{C}$ | `LITERATURE_SOURCED` | Arntfield & Murray (1981), *J. Food Sci.* | Standard legume biophysics. |
| **$\sigma_0$** | Initial Cotyledon Cohesion Stress | $450.0$ | $\text{kPa}$ | `ASSUMED` | Heuristic estimate based on pea Kramer shear cell curves. | **NOT measured on target lot.** |
| **$\sigma_{\text{crit}}$** | Cooked Squash Threshold Stress | $45.0$ | $\text{kPa}$ | `ASSUMED` | Derived from 1.0 kg dead-weight tactile squash threshold. | Engineering heuristic. |
| **$k_{\text{soft,base}}$** | Baseline Softening Rate (100°C) | $0.000135$ | $\text{s}^{-1}$ | `ASSUMED` | Reverse-calculated to yield ~58 min open boiling time. | **Phenomenological assumption.** |
| **$E_{a,\text{soft}}$** | Softening Activation Energy | $85,400.0$ | $\text{J/mol}$ | `LITERATURE_SOURCED` | Taherian et al. (2011); Rao (2014) pectin beta-elimination. | Standard beta-elimination kinetics. |

---

## 4. In-Depth Audit of the 7.73x Softening Rate Equation

In [MULTISCALE_PHYSICS_ARCHITECTURE.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/MULTISCALE_PHYSICS_ARCHITECTURE.md), the mathematical transfer function is defined as:

$$k_{\text{soft}}(T, \chi_{\text{Na}}, \rho_{\text{Ca}}) = k_0 \cdot \exp\left(-\frac{E_a}{R_g T}\right) \cdot \left[ \frac{1.0 + 3.2 \cdot \chi_{\text{Na}}}{1.0 + 2.5 \cdot \rho_{\text{Ca}}} \right]$$

### 4.1 Variable-by-Variable Dissection
1. **$k_0$ (Arrhenius Pre-exponential Factor):**
   - *Units:* $\text{s}^{-1}$
   - *Value:* $1.35 \times 10^8\text{ s}^{-1}$ (when multiplying $0.0035$ by $10^{11}$ scaling factor).
   - *Provenance:* **ASSUMED**. Tuned so that at $T = 100^\circ\text{C}$, the baseline rate constant equals $0.000135\text{ s}^{-1}$.
2. **$E_a$ (Activation Energy for Middle-Lamella Solubilization):**
   - *Units:* $\text{J / mol}$
   - *Value:* $85,400\text{ J/mol}$ ($85.4\text{ kJ/mol}$).
   - *Provenance:* **LITERATURE_SOURCED**. Reflects published activation energies for non-enzymatic $\beta$-eliminative depolymerization of pectin chains at elevated temperatures ($> 90^\circ\text{C}$).
3. **$\chi_{\text{Na}}$ (Sodium Ion Displacement Fraction):**
   - *Units:* Dimensionless ($0.0 \le \chi_{\text{Na}} \le 1.0$).
   - *Formula:* $\chi_{\text{Na}} = \min(1.0, C_{\text{NaHCO}_3} / 0.50\%)$.
   - *Provenance:* **ASSUMED**. A linear saturation model assuming complete monovalent displacement occurs at $0.50\%$ w/w solution concentration. No competitive ion-exchange equilibrium isotherms ($K_{\text{ex}}$) were experimentally measured.
4. **$\rho_{\text{Ca}}$ (Residual Calcium-Pectate Crosslink Density):**
   - *Units:* Dimensionless ($0.10 \le \rho_{\text{Ca}} \le 0.75$).
   - *Formula:* $\rho_{\text{Ca}} = \max(0.10, 0.75 \cdot (1.0 - 0.70 \cdot \chi_{\text{Na}}))$.
   - *Provenance:* **ASSUMED**. Presumes that $0.50\%$ NaHCO₃ removes exactly $70\%$ of bridging calcium ions. No atomic absorption spectroscopy of bound vs. free calcium was conducted.
5. **Coefficient $3.2$ (Monovalent Acceleration Factor):**
   - *Provenance:* **ASSUMED**. A synthetic multiplier chosen so that the numerator equals $4.2$ when $\chi_{\text{Na}} = 1.0$.
6. **Coefficient $2.5$ (Divalent Retardation Factor):**
   - *Provenance:* **ASSUMED**. A synthetic multiplier chosen so that the denominator drops from $2.875$ ($\rho_{\text{Ca}} = 0.75$) down to $1.5625$ ($\rho_{\text{Ca}} = 0.225$).

### 4.2 Why the Ratio Yields Exactly 7.73:
$$\text{Untreated Multiplier } (\chi_{\text{Na}}=0, \rho_{\text{Ca}}=0.75) = \frac{1.0 + 3.2(0)}{1.0 + 2.5(0.75)} = \frac{1.0}{2.875} = 0.3478$$
$$\text{Treated Multiplier } (\chi_{\text{Na}}=1, \rho_{\text{Ca}}=0.225) = \frac{1.0 + 3.2(1.0)}{1.0 + 2.5(0.225)} = \frac{4.2}{1.5625} = 2.6880$$
$$\text{Acceleration Ratio} = \frac{2.6880}{0.3478} = \mathbf{7.7285 \approx 7.73\times}$$

**Scientific Audit Verdict:** The 7.73-fold acceleration was **constructed algebraically**, not empirically derived from target-lot kinetic observations.

---

## 5. Required Physical Wet-Lab Assays for Mechanistic Proof

To transition this mechanism from a hypothesis to demonstrated scientific fact, the following laboratory assays are mandatory:

```
[ PHYSICAL ASSAY ROADMAP FOR MECHANISTIC VALIDATION ]

1. PECTIN ESTERIFICATION ASSAY (FT-IR / Titrimetry)
   - Measure Degree of Esterification (DE) on raw Tanzanian dal vs fresh Indian benchmark.
   - Hypothesis: DE_Tanzanian <= 0.55 (PME-hydrolyzed) vs DE_Indian >= 0.68.

2. FRACTIONAL CATION EXTRACTION (AAS / ICP-OES)
   - Fraction 1: Water-soluble free Ca2+/Mg2+.
   - Fraction 2: EDTA-extractable pectate-bound Ca2+/Mg2+.
   - Fraction 3: Insoluble structural mineral fraction.
   - Hypothesis: EDTA-bound Ca is > 2.5x higher in hard Tanzanian dal.

3. TEXTURE PROFILE ANALYSIS (Kramer Shear Cell / Instron)
   - Measure peak compressive yield force (N/g) vs cooking time in 115°C pressure cooker.
   - Establish true empirical softening curve k_soft(t).
```

---

**Signed Off:**  
Harakutir Scientific Advisory & Biophysical Audit Panel  
*October 15, 2026*
