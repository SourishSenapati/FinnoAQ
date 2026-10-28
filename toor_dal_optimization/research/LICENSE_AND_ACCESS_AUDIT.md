# LICENSE AND DATA ACCESS AUDIT

**Project:** FinnoaQ Autonomous Pulse Engineering  
**Standard:** Ocean Boiling Protocol v3.0 | FinnoaQ Omega v4  
**Date:** October 2026  

---

## 1. Compliance and Permitted Reuse Register

| Source / Resource | Publisher / Repository | Governing License / Terms | Permitted Reuse in Computational System | Commercial Reuse Status | Quarantine or Isolation Mandate |
|---|---|---|---|---|---|
| **Frontiers in Sustainable Food Systems** (Machinjili et al., 2025) | Frontiers Media SA | Creative Commons Attribution 4.0 International (CC-BY 4.0) | Unrestricted computational ingestion, adaptation, derivative creation with attribution. | Permitted under CC-BY 4.0 terms with citation. | None. Ingested into `data/literature/`. |
| **PMC Articles** (PMC5336460) | PubMed Central / NLM | Open Access / Public Health Service | Text mining, research reference, citation permitted. | Subject to underlying author copyright; research reference only. | General context only. |
| **Elsevier Food Research International** (Wainaina 2022, Chen 2021, Chen 2023) | Elsevier B.V. | Subscription / Author Copyright | Abstract, metadata, and author-summarized constants extracted under Fair Dealing / Scientific Citation. | Raw publisher PDFs not redistributed. Only atomic scientific claims and parameters catalogued. | Full text raw spreadsheets not scraped or distributed. |
| **FSSAI Food Product Standards 2011** | Government of India | Public Domain / Indian Government Gazette | Full legal text freely usable for regulatory compliance verification. | Legally binding public standard for commercial food release in India. | None. Official regulatory baseline. |
| **FAOSTAT Database** | Food and Agriculture Organization (UN) | Creative Commons Attribution-NonCommercial-ShareAlike 3.0 IGO (CC BY-NC-SA 3.0 IGO) | Data mining and statistical analysis permitted with attribution. | Aggregated statistical reference for market context. Specific pricing quotes must be verified independently. | None. Context only. |
| **USDA FoodData Central** | USDA ARS | Public Domain (U.S. Government Work) | Fully open for commercial and scientific computation without restriction. | Freely usable for nutrient baseline profiling. | Reference data only; not target lot assay. |
| **Dream-RSI** (arXiv:2609.14858) | arXiv / GitHub (`zhengkid/Dream-RSI`) | MIT / Apache 2.0 Open Source | Algorithmic concept re-implemented as `DREAM_RSI_INSPIRED`. | Permitted. | Custom replay harness marked as `DREAM_RSI_INSPIRED`. |
| **Learn Harness Engineering** | WalkingLabs | Educational Open Access | Architectural patterns (G0-G9 gates, anti-loop rules) adapted. | Permitted. | Architectural specification. |

---

## 2. Anti-Leakage & Data Governance Boundary Guarantees

1. **Synthetic Data Quarantine:** Synthetic fixtures created for software benchmarks are watermarked with `"dataset_kind": "synthetic_test_only"` and restricted exclusively to `data/synthetic/`. They are blocked by automated gate tests from entering empirical reporting.
2. **Literature Isolation:** Literature datasets from other varieties or species (e.g. Malawi pigeon pea or common beans) are tagged with `"dataset_kind": "published_literature"` and cannot be presented as physical assays of FinnoaQ's commercial lot.
3. **Target Lot Empirical Status:** Wet-lab assays on the specific Tanzanian commercial dal lot remain categorized as **`DATA_READINESS_ONLY`** until physical certified test reports from an accredited NABL/FSSAI laboratory are uploaded.
