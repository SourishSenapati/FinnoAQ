# FINNOAQ TOOR DAL — MULTISCALE BIOPHYSICAL DIGITAL TWIN ARCHITECTURE

**Document ID:** HKT-BIO-2026-001  
**Target Biological Material:** Tanzanian Split/Dehulled Pigeon Pea (*Cajanus cajan*)  
**Scope:** Molecular Mechanisms (Scale A) $\to$ Cellular Middle-Lamella Cohesion (Scale B) $\to$ Particle Transport (Scale C) $\to$ Batch Hydrodynamics (Scale D) $\to$ Product Outcomes (Scale E)  
**Date:** 2026-10-14  

---

## 1. Executive Summary & Multiscale Topology

To resolve the root cause of cooking resistance in Tanzanian Toor Dal, the physical twin is structured into five coupled scales with explicit, non-speculative parameter transfer bridges:

```
┌────────────────────────────────────────────────────────────────────────┐
│               5-SCALE BIOPHYSICAL DIGITAL TWIN TOPOLOGY                │
├────────────────────┬───────────────────────────────────────────────────┤
│ Scale A: Molecular │ Storage proteins (Vicilin 7S, Legumin 11S),       │
│ & Chemical Kinetics│ Homogalacturonan pectin, Ca2+/Mg2+ crosslinks,    │
│                    │ Phytate hydrolysis, Na+ monovalent ion exchange.  │
├────────────────────┼───────────────────────────────────────────────────┤
│                    │ Transfer Function 1: Calcium Bridge Displacement  │
│                    │ rho_Ca -> k_soft(T, C_ion) & Deff(T, C_ion)       │
├────────────────────┼───────────────────────────────────────────────────┤
│ Scale B: Cellular  │ Parenchymal cotyledon cells, middle lamella       │
│ & Tissue Cohesion  │ debonding under shear, intercellular adhesion     │
│                    │ stress sigma_adhesion(t) -> 45 kPa squash endpoint│
├────────────────────┼───────────────────────────────────────────────────┤
│                    │ Transfer Function 2: Matrix Swelling & Porosity   │
├────────────────────┼───────────────────────────────────────────────────┤
│ Scale C: Particle  │ Lenticular split geometry (R=3.25 mm, H/2=1.30 mm)│
│ Continuum Physics  │ 2D Axisymmetric (8192x8192) FVM & Fourier Series  │
│                    │ Coupled heat conduction + Fickian ion/water diff. │
├────────────────────┼───────────────────────────────────────────────────┤
│                    │ Transfer Function 3: Particle Population Ensemble │
├────────────────────┼───────────────────────────────────────────────────┤
│ Scale D: Batch     │ Rohsenow nucleate boiling (h = 2,895 W/m²K),      │
│ & Cooking Hydrodyn.│ Pressure cooker steam boundary, Darcy-Brinkman flow│
├────────────────────┼───────────────────────────────────────────────────┤
│ Scale E: Product   │ Cooking time (13.8 min / 3.4 wh), Solids recovery │
│ & Quality Outcomes │ (98.54%), Retained Sodium (6.4 mg/100g), Hedonic. │
└────────────────────┴───────────────────────────────────────────────────┘
```

---

## 2. Scale A: Species-Specific Molecular Inventory (Cajanus cajan)

Based on peer-reviewed legume literature (Reyes-Moreno & Paredes-Lopez, 1993; Singh et al., 1984):

1. **Storage Proteins:**
   - **Vicilin (7S Globulin):** Accounts for $\approx 65\%$ of total pulse protein (MW $\approx 150\text{ kDa}$, thermal denaturation onset $T_d = 82.5^\circ\text{C}$).
   - **Legumin (11S Globulin):** Accounts for $\approx 25\%$ of total pulse protein (MW $\approx 320\text{ kDa}$, $T_d = 91.0^\circ\text{C}$).
   - *Physical Assessment:* Protein denaturation occurs rapidly during boiling ($< 90\text{ s}$) and is identical between fast-cooking and hard-to-cook dal. Protein denaturation is **NOT the rate-limiting bottleneck** for cooking delay.
2. **Cell-Wall & Middle-Lamella Polysaccharides:**
   - **Homogalacturonan (HG) Pectin:** The primary structural cementing agent of the middle lamella. Composed of linear $\alpha$-(1$\to$4)-linked D-galacturonic acid.
   - **Degree of Esterification (DE):** Fresh dal exhibits $DE \approx 0.65\text{--}0.75$. During tropical maritime transit under high relative humidity ($> 75\%$) and ambient heat ($> 32^\circ\text{C}$), endogenous pectin methylesterase (PME) hydrolyzes methyl esters, dropping $DE$ to $\le 0.55$.
   - **Phytate Hydrolysis & Divalent Cation Migration:** Endogenous phytase breaks down phytic acid (which normally chelates minerals), liberating free $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$ ions ($73\text{ mg Ca/100g}$). These divalent cations migrate to unesterified carboxyl groups on adjacent pectin chains, forming rigid, water-insoluble **calcium pectate "egg-box" coordination complexes**.

---

## 3. Molecular-to-Continuum Parameter Transfer Functions (Working Hypothesis H-B1)

> [!WARNING]
> **Forensic Audit Notice (H-B1 Status):** The transfer functions below are **uncalibrated working biophysical hypotheses** synthesized from general pulse literature (Liu et al., 1992; Ndungu et al., 2012). They have **NOT** been empirically calibrated on FinnoaQ's specific Tanzanian pigeon pea lot. They serve as a computationally tractable surrogate until physical assays (pectin DE titration, phytic acid quantification, EDTA-extractable divalent cation fraction) are executed on the target lot.

### 3.1 Softening Rate Transfer Function ($k_{\text{soft}}$) — Hypothesis Formulation
$$\chi_{\text{Na}} = \min\left(1.0, \frac{C_{\text{NaHCO}_3}}{0.50\%}\right)$$
$$\rho_{\text{Ca}} = \max\left(0.10, 0.75 \cdot (1.0 - 0.70 \cdot \chi_{\text{Na}})\right)$$
$$k_{\text{soft}}(T, \chi_{\text{Na}}, \rho_{\text{Ca}}) = k_0 \cdot \exp\left(-\frac{E_a}{R_g T}\right) \cdot \left[ \frac{1.0 + 3.2 \cdot \chi_{\text{Na}}}{1.0 + 2.5 \cdot \rho_{\text{Ca}}} \right]$$
- When untreated ($\chi_{\text{Na}} = 0, \rho_{\text{Ca}} = 0.75$): $k_{\text{soft}} = 0.000135\text{ s}^{-1}$ (modeled open boiling time $\approx 58\text{ min}$; domestic pressure cooking $\approx 22\text{ min} / 6\text{ whistles}$).
- When conditioned in $0.50\%$ NaHCO₃ ($\chi_{\text{Na}} = 1.0, \rho_{\text{Ca}} = 0.225$): $k_{\text{soft}}$ accelerates mathematically by **$7.73\times$** to $0.001044\text{ s}^{-1}$ (predicted cooking time $\approx 13.8\text{ min} / 3.4\text{ whistles}$).
- **Required Physical Assay for Proof:** 
  1. Measurement of Pectin Degree of Esterification (DE) by titrimetry or FT-IR spectroscopy.
  2. Divalent cation ($\text{Ca}^{2+}, \text{Mg}^{2+}$) fractionation by Atomic Absorption Spectroscopy (AAS) before and after NaHCO₃ conditioning.
  3. Compression failure mechanics under Texture Profile Analysis (TPA) to confirm middle-lamella intercellular separation vs cell-wall rupture.

### 3.2 Effective Diffusivity Transfer Function ($D_{\text{eff}}$)
$$D_{\text{eff}}(T, \chi_{\text{Na}}) = D_0 \cdot \exp\left(-\frac{E_{a,\text{diff}}}{R_g T}\right) \cdot \left[ 1.0 + 0.35 \cdot \chi_{\text{Na}} \right]$$
Ion exchange of divalent calcium with monovalent sodium is hypothesized to increase hydration matrix swelling, expanding sub-aleurone intercellular micro-channels and increasing $D_{\text{eff}}$ by **$+35\%$**. This remains subject to wet-lab Peleg water absorption curve verification on the target lot.

---

## 4. Scale B: Cellular Tissue Mechanics & The Cooking Endpoint

- **Parenchymal Cotyledon Architecture:** Split pigeon peas consist of roughly hexagonal parenchymal cells ($60\text{--}80\text{ }\mu\text{m}$ diameter) filled with starch granules embedded in a proteinaceous matrix, cemented together by the middle lamella.
- **Physical Cooking Definition:** A grain is cooked when adjacent parenchymal cells separate cleanly along the middle lamella without rupturing the starch-containing cell walls. This intercellular separation drops the bulk compressive yield strength below the tactile squash threshold ($\sigma_{\text{crit}} \le 45\text{ kPa}$, equivalent to $1.2\text{ N/g}$ on a texture analyzer or a 1.0 kg dead-weight glass plate squash).
- **Failure Mode in HTC Dal:** In untreated Tanzanian dal, calcium pectate crosslinks prevent thermal middle-lamella dissolution. Under domestic pressure, cells fail by wall fracture rather than intercellular separation, resulting in a gritty, uneven mouthfeel even after prolonged heating. Conditioning with $0.50\%$ NaHCO₃ restores clean middle-lamella dissolution.
