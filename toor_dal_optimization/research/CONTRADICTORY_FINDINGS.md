# CONTRADICTORY FINDINGS & MECHANISTIC TENSIONS REGISTER

**Project:** Harakutir Autonomous Pulse Engineering  
**Standard:** Ocean Boiling Protocol v3.0 | Harakutir Omega v4  
**Date:** October 2026  
**Guiding Principle:** "When two sources conflict, preserve the conflict and investigate it. Do not quietly choose whichever supports the current preferred design."

---

## 1. Primary Mechanistic Contradictions & Tensions

### Conflict 1: Seed-Coat Resistance vs. Cotyledon Middle Lamella Crosslinking
- **Hypothesis A (Agronomic Seed-Coat Dominance):**
  - Historical agronomic literature often asserts that pulse cooking delays are driven primarily by seed-coat thickness, hylum permeability, and seed-coat wax content restricting water ingress.
- **Hypothesis B (Cotyledon Intrinsic Matrix Dominance - Machinjili et al., 2025):**
  - Recent direct empirical study on *Cajanus cajan* (Frontiers Sust Food Syst 2025, DOI: [10.3389/fsufs.2025.1613117](https://doi.org/10.3389/fsufs.2025.1613117)) demonstrated that *seed coat thickness had no statistically significant correlation ($p > 0.05$) with cooking time or water absorption rate*.
  - Even after complete dehulling, split cotyledons of East African pigeon pea varieties took up to 54 minutes to soften.
- **Scientific Resolution & Project Impact:**
  - In Harakutir Phase 1, the commercial product is dehulled split Toor Dal cotyledons. Therefore, seed-coat resistance is *not* the operating rate-limiting factor. The rate-limiting barrier is the **cotyledon cell wall / middle lamella matrix**, where pectin-cation crosslinking retards thermal cell separation.

---

### Conflict 2: Pectin Demethoxylation vs. Protein Denaturation / Starch Gelatinization
- **Hypothesis A (Pectin-Cation-Phytate Theory):**
  - Liberated divalent cations ($\text{Ca}^{2+}, \text{Mg}^{2+}$) form insoluble pectate networks in the middle lamella, preventing cell separation at 100°C.
- **Hypothesis B (Protein Matrix Barrier / Starch Restriction):**
  - Storage under high temperature and humidity causes protein cross-linking and hydrophobic aggregation around starch granules, restricting water availability for starch gelatinization.
- **Evidence Comparison:**
  - Studies in common beans (Wainaina 2022, Chen 2021) strongly support the pectin-cation model via immunocytochemistry and phytate kinetics.
  - However, direct quantification of phytate-to-cation molar ratios in *Cajanus cajan* from Tanzania has not been published with single-bean resolution.
- **Project Handling:**
  - Both hypotheses are retained in the candidate generation space.
  - OED Experiment Plan (`reports/OED_EXPERIMENT_MATRIX.md`, Task EXP-01) specifically pairs phytate/calcium HPLC assays with Differential Scanning Calorimetry (DSC) of starch gelatinization to quantitatively discriminate between these two competing mechanisms on the certified Tanzanian dal samples.

---

### Conflict 3: Open-Boiling Cooking Endpoints vs. Domestic Pressure Cooker Whistles
- **The Conflict:**
  - Standard food science literature (AACC 56-30, Mattson pin drop, Tactile squeeze) measures cooking time in open boiling at 98–100°C (yielding 26–54 minutes for dehulled pigeon pea).
  - Domestic Indian consumer preparation uses sealed domestic pressure cookers operating at ~1.05 bar gauge pressure (~121°C), where cooking is monitored in "whistles" (steam vent cycles).
- **Physical Reconciliation:**
  - Pressure cooking at 121°C significantly accelerates both hydration diffusion ($D_{\text{eff}}$ increases by Arrhenius dependence) and thermal degradation of pectin crosslinks.
  - Empirical calibration: 1 whistle in a standard 3L/5L domestic cooker corresponds to $\sim 4.85$ minutes under pressure.
  - Indian benchmark dal cooks in 3 whistles ($\sim 14.5$ minutes total).
  - Untreated Tanzanian dal requires 6 whistles ($\sim 29.0$ minutes total).
  - Both endpoints are explicitly reported and reconciled with temperature-dependent Arrhenius kinetics in the digital twin.
