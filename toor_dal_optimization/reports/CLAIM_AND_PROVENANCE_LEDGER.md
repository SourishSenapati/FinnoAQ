# FINNOAQ CLAIM & PROVENANCE LEDGER
## Formal Root-Cause Taxonomy (Categories A–D), Scientific Claims & Data Gating Status

**Document ID:** HKT-CLM-2026-013  
**Version:** 3.0.0  
**Controlling Standard:** Sections 45 & 46 of FinnoaQ Autonomous Master Prompt  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Evidence Taxonomy & Root-Cause Categories

Every scientific conclusion and hypothesis in this investigation is classified under the SOW's formal four-category taxonomy:
* **Category A (Confirmed Differences):** Differences directly demonstrated by valid measurements or physical laboratory experiments.
* **Category B (Strongly Associated Factors):** Measured parameters that show statistically meaningful association with cooking performance.
* **Category C (Potential Mechanisms):** Scientific explanations and candidate mechanisms that require controlled experimental validation.
* **Category D (Factors Unlikely to Be Responsible):** Parameters for which available evidence does not support a meaningful role under tested conditions.

---

## 2. Master Claim Ledger

| Claim ID | Category | Claim Statement | Evidence Status | Supporting Source / Instrument Pointer | Data Integrity Limitations | Current Reviewer Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CLM-001** | **Category A** | Household pressure cooking of raw Tanzanian toor dal requires approximately 6 whistles, whereas Indian benchmark dal requires approximately 3 whistles under comparable kitchen conditions. | `DATA_READINESS_ONLY` | FinnoaQ problem statement; household baseline log in SOW Section 2 | Observational preliminary report; lacks standardized laboratory instrument calibration (calibrated Mattson / texture analyzer pending). | REVIEWED / PROBLEM STATEMENT |
| **CLM-002** | **Category C** | Slower cooking in Tanzanian toor dal is driven by middle lamella pectin de-esterification and subsequent cross-linking with divalent Ca2+/Mg2+ ions during tropical maritime transit (HTC defect). | `DATA_READINESS_ONLY` | Literature evidence [EVD-LIT-001]; Reyes-Moreno & Paredes-Lopez (1993) | Mechanism demonstrated in published legume literature; requires wet-lab chemical confirmation on FinnoaQ sample lots (SOW Section 11 & 12). | HYPOTHESIS H2 / AWAITING LAB DATA |
| **CLM-003** | **Category C** | Slower cooking is associated with reduced cotyledon water absorption rate and lower effective moisture diffusivity (Deff). | `DATA_READINESS_ONLY` | Peleg model simulation [EVD-LIT-002]; inverse diffusion solver on RTX 4050 | Parameter identifiability confirmed numerically; awaiting laboratory hydration soaking curve data (SOW Section 10). | HYPOTHESIS H1 / AWAITING LAB DATA |
| **CLM-004** | **Category C** | Catalytic infrared HTST treatment (185°C for 45 s) or monovalent salt chelation (0.5% NaHCO3) will restore quick-cooking performance to <= 3.5 whistles with acceptable texture. | `DATA_READINESS_ONLY` | Candidate design space [EVD-LIT-003, EVD-LIT-004]; Pareto frontier simulation | Predicted computationally via 5-layer screening; physical bench validation required before pilot investment. | CANDIDATE SHORTLIST / GATED BY G4 |
| **CLM-005** | **Category D** | Raw protein denaturation prior to cooking is unlikely to be the primary cause of the 3-whistle cooking delay. | `DATA_READINESS_ONLY` | Literature DSC thermograms in dry pulses; protein solubility references | Secondary contributing factor; cell wall pectin solubilization is the primary rate-limiting step in whole pulse softening. | CANDIDATE MECHANISM D / LOW PRIORITY |

---

## 3. Data Integrity & Provenance Guarantee

* **Zero Fabrication Policy:** In accordance with the project constitution, no synthetic fixture has been substituted for physical wet-lab certificates.
* **Gated Status:** All empirical claims remain strictly flagged as `DATA_READINESS_ONLY` until signed laboratory certificates are imported into `data/raw/` and verified with SHA-256 cryptographic registration.
