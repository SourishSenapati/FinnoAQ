# Diagnostic Hypothesis & Discriminating Test Matrix

**Project Reference:** FNQ-PR-2026-001 | Phase 1 Diagnostic R&D Study  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Document Ref:** FNQ-REP-HYP-001  
**Date:** 20 October 2026  
**Governing Standard:** Section 3 (Criticism A) — Multi-Hypothesis Scientific Architecture  

---

## 1. Executive Summary & Epistemic Grounding

The observed slow-cooking behavior of Tanzanian split pigeon pea (*Cajanus cajan*)—preliminarily reported by the client as requiring ~6 domestic pressure cooker whistles compared to ~3 whistles for domestic Indian dal—is a preliminary observation, not proof of a specific molecular defect. 

Under the workspace governance laws, **pectin de-esterification and calcium crosslinking must compete alongside alternative physical, anatomical, biochemical, genetic, and post-harvest mechanisms**. No single mechanism may be declared the root cause without target-lot diagnostic data. Null findings (e.g. failure to discriminate between mechanisms under standardized tests) are valid scientific outcomes.

---

## 2. Comprehensive 10-Hypothesis Register

| Hypothesis ID | Candidate Mechanism | Observable Predictions & Discriminating Test | Primary Measurement & Expected Direction | Discriminating Power & Confounders | Epistemic Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **H1** | **Hydration Kinetics & Diffusion Barriers** | Cotyledon cell walls restrict water imbibition. Cold/ambient water uptake rate is significantly depressed in target dal. | Water absorption curve ($M_t$ vs. $t$ at 25°C, 40°C, 60°C); Peleg rate constant $k_1$. If true: $k_1$ is significantly higher (slower uptake). | High. Confounded if soaking water reaches full equilibrium ($M_{\infty}$) without softening cooking time. | `HYPOTHESIS` |
| **H2** | **Grain Geometry & Seed Coat Residue** | Cotyledon thickness, aspect ratio, or residual hydrophobic seed coat/hilum remnants impede moisture and heat penetration. | Micrometer caliper 3D axes ($L, W, T$); 1000-grain mass; residual seed coat gravimetric percentage. If true: $T$ is larger, or residual testa $> 0.5\%$. | Moderate. Physical measurement distinguishes geometric resistance from chemical resistance. | `HYPOTHESIS` |
| **H3** | **Cotyledon Cellular Microstructure** | Compact, non-porous cellular packing in cotyledon parenchyma impedes thermal swelling and cell separation. | Scanning Electron Microscopy (SEM) of fractured cotyledon cross-sections; bulk porosity; dye penetration depth. If true: reduced intercellular voids. | High. Directly visualizes parenchyma compaction and middle lamella thickness. | `HYPOTHESIS` |
| **H4** | **Pectin Demethylation & Divalent Crosslinking** | Pectin methylesterase (PME) de-esterifies pectin during storage; unesterified carboxyls form insoluble calcium/magnesium pectates in middle lamella. | Fractionation into water-soluble, oxalate-soluble, and alkali-soluble pectin; degree of esterification (DE); titratable carboxyl groups. If true: oxalate-soluble fraction elevated, DE depressed. | High. The classical hard-to-cook (HTC) biochemical model. Validated only if oxalate/chelator reverses cooking resistance. | `HYPOTHESIS` |
| **H5** | **Phytate Hydrolysis & Mineral Redistribution** | Endogenous phytase hydrolyzes phytate during warm/humid transit, liberating free divalent cations ($\text{Ca}^{2+}, \text{Mg}^{2+}$) that migrate to cell walls. | Total and free phytic acid content; ICP-OES elemental analysis of Ca, Mg, P, K; Phytate:Ca and Phytate:Mg molar ratios. If true: free phytate $< 0.4\%$ or Phytate:Ca $< 0.20$. | High. Explains why middle lamella becomes calcified during storage. | `HYPOTHESIS` |
| **H6** | **Starch Gelatinization & Amylose Shifts** | Starch granules require elevated thermal energy to swell and gelatinize, or higher amylose content retards paste formation. | Differential Scanning Calorimetry (DSC: $T_o, T_p, T_c, \Delta H_{\text{gel}}$); Rapid Visco Analyzer (RVA) pasting profile; apparent amylose content. If true: $T_p > 78^\circ\text{C}$ or $\Delta H > 12\text{ J/g}$. | Moderate. Distinguishes whether cooking delay originates in starch granules vs. cell wall matrix. | `HYPOTHESIS` |
| **H7** | **Protein Denaturation & Storage Insoluble Matrix** | Storage-induced protein crosslinking, hydrophobic aggregation, or sulfur-bridge formation creates an impenetrable protein-starch complex. | Protein solubility profile in water, salt, and SDS buffers; proximate crude protein ($N \times 6.25$); free sulfhydryl groups. If true: water-soluble protein fraction markedly depressed. | Moderate. High storage temperatures ($>35^\circ\text{C}$) often drive protein crosslinking. | `HYPOTHESIS` |
| **H8** | **Genotypic / Cultivar Inherent Differences** | Tanzanian agricultural cultivars inherently possess thicker cell walls, higher lignin/fiber, or lower thermal conductivity than Indian cultivars. | Multi-lot agronomic provenance tracking; neutral detergent fiber (NDF), acid detergent fiber (ADF), lignin content; comparative botanical pedigree. If true: lignin $> 1.8\%$. | Moderate. Requires testing multiple independent imported consignments from different growing zones. | `HYPOTHESIS` |
| **H9** | **Tropical Maritime Transit & Aging Exposure** | Prolonged containerized ocean transit across the Indian Ocean (high temperature and humidity $>30^\circ\text{C}, >75\%\ \text{RH}$) triggered accelerated aging. | Accelerated aging simulation on fresh Indian control; lipid auto-oxidation (peroxide value, free fatty acids); grain moisture history. If true: target dal has high FFA ($> 15\text{ mg KOH/100g}$). | High. Reconciles why fresh harvest Tanzanian dal may cook normally, while commercial imported lots cook slowly. | `HYPOTHESIS` |
| **H10** | **Cooking Measurement & Water Hardness Confounders** | Client cooking difference is partially an artifact of domestic cooker volume, fill ratio, heat input rate, or local Kolkata tap water hardness. | Standardized laboratory cooker at controlled temperature ($115^\circ\text{C}, 15\text{ psi}$) and heating rate; comparative cooking in deionized ($0\text{ ppm}$) vs. hard ($300\text{ ppm Ca}^{2+}$) water. | Critical Control. Must be evaluated first to ensure the defect is genuine and not an operational artifact. | `HYPOTHESIS` |

---

## 3. Discriminating Logic & Decision Rules

```text
========================================================================================================
EVIDENCE-BASED DECISION LOGIC MATRIX FOR PHASE 1 DIAGNOSTICS
========================================================================================================
Diagnostic Finding                                              Inference / Outcome
--------------------------------------------------------------------------------------------------------
Target dal cooks in ~3 whistles in DI water, but ~6 in tap water Confounder H10 confirmed; local water hardness is the primary driver.
Target dal hydration rate (k1) matches Indian benchmark         Hydration barrier H1 ruled out; delay resides in middle lamella or starch.
Oxalate-soluble pectin is elevated; Phytate:Ca ratio is low     Calcium-pectate crosslinking H4/H5 supported; chelators indicated for Phase 2.
DSC gelatinization temperature Tp is identical between lots     Starch barrier H6 ruled out; starch gelatinization is normal.
All 10 tests show no significant difference between lots        Domestic artifact H10 confirmed; target grain is inherently normal.
Target dal displays elevated FFA and reduced soluble protein    Transit aging H9 and protein matrix H7 supported; storage conditions implicated.
========================================================================================================
```

---

## 4. Null Findings as Valid Deliverables

Under Section 3.3 of the directive, the final technical assessment will state what the evidence actually establishes:
1. If the standardized laboratory cooker reproduces no cooking time discrepancy between Tanzanian and Indian lots under controlled heat flux and demineralized water, **Hypothesis H10 is confirmed and the target material is vindicated**.
2. If differences in mineral content or water uptake exist but do not correlate with tenderness kinetics, **the report will explicitly state that the measured difference does not constitute the root cause**.
3. Under no circumstances will the report claim that "pectin crosslinking has been definitively proven" unless fractionation assays demonstrate statistically significant elevated pectate binding.
