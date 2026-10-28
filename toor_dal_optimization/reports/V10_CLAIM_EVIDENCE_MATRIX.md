# V10 Claim & Evidence Traceability Matrix
**Project Reference:** FNQ-PR-2026-001 | Phase 1 Diagnostic R&D Proposal  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Academic Guidance:** Technical Advisory Panel  
**Client Entity:** Client Organization (53, Pathuriaghata Street, Kolkata – 700006)  
**Document Ref:** FNQ-V10-EVI-001  
**Date:** 19-10-2026  
**Git Branch:** `v10-phase1-proposal-reconciliation`  

---

## 1. Evidence Governance & Tagging Taxonomy

Under Section 0.2 and Section 4.3 of the V10 Master Directive, every statement, parameter, and numerical claim is classified into one of eight mutually exclusive evidence categories:
1. `SOURCE-DOCUMENT`: Information originating directly from the primary baseline SOW (`Phase1_Scope_of_Work_Toor_Dal.docx`) or approved project records.
2. `MEASURED`: Physical data obtained from verified instrument calibration, traceable laboratory assays, and documented sample lots.
3. `OFFICIAL-REFERENCE`: Statutory food safety standards, gazetted regulations (e.g., FSSAI, BIS), or certified reference methods (AOAC, AACC, ISO).
4. `CALCULATED`: Values derived through transparent, mathematically verified first-principles formulas from defined inputs.
5. `ASSUMED`: Unmeasured baseline engineering parameters explicitly declared for modeling or scenario planning.
6. `HYPOTHESIS`: Plausible scientific mechanism proposed for testing; unconfirmed for the specific target lot.
7. `INDICATIVE-COST`: Budgetary estimates, line-item ranges, or unquoted laboratory allowances subject to final confirmation.
8. `UNKNOWN/NOT-VERIFIED`: Required facts, sample identities, or parameters not yet received, measured, or legally verified.

---

## 2. Master Claim & Evidence Traceability Table

| Claim ID | Proposal Statement / Claim Description | Stated Value / Parameter | Evidence Class | Primary Source & Method | Uncertainty / Limitations | Client-Safe Wording in Proposal Rev V10 | Document Location |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :---: |
| **CLM-01** | Domestic cooking observation shows Tanzanian dal requires more time than Indian benchmark. | ~6 whistles vs ~3 whistles | `SOURCE-DOCUMENT` | Source SOW Table 1 & Section 1. Qualitative client report. | Whistle count is unstandardized, pressure/heat dependent, non-scientific. | "Domestic observations indicate approx. 6 pressure-cooker whistles vs 3 whistles for benchmark; serving as preliminary context only." | Section 3 |
| **CLM-02** | Phase 1 success criterion is diagnostic quality, not guaranteed cooking time reduction. | Diagnostic quality & root-cause ranking | `SOURCE-DOCUMENT` | Source SOW Section 2.3 & 33. | No treatment guarantee or commercial optimization is promised. | "Phase 1 will be considered successful if it delivers reproducible comparative evidence, an objective cooking endpoint, and ranked root causes." | Section 4 |
| **CLM-03** | Pectin–mineral interaction is one candidate mechanism among competing explanations. | Hypothesis H3 | `HYPOTHESIS` | Literature on legume hard-to-cook defect; V10 Directive §4. | Unproven for target Tanzanian lot; competing with hydration, structure, starch, etc. | "Pectin–mineral interactions represent one candidate hypothesis among ten competing mechanisms to be investigated." | Section 6 |
| **CLM-04** | Total proposed Phase 1 professional fee is ₹1,73,000 plus applicable GST. | ₹1,73,000 + GST | `SOURCE-DOCUMENT` / `INDICATIVE-COST` | Source SOW Table 39 & 40; sum of 11 analytical line items. | Taxes extra; third-party specialized lab costs coordinated within budget. | "Total proposed professional fee: ₹1,73,000 plus applicable GST at prevailing rates." | Section 14 |
| **CLM-05** | Commercial ceiling for exploratory testing is up to ₹2,00,000 plus GST. | Up to ₹2,00,000 + GST | `SOURCE-DOCUMENT` / `INDICATIVE-COST` | Source SOW Table 42 & Section 26. | Requires prior written client approval before exceeding ₹1,73,000. | "Suggested commercial ceiling up to ₹2,00,000 + GST for any approved exploratory scope variations." | Section 14 |
| **CLM-06** | Milestone invoice schedule: 40% on start, 40% on testing completion, 20% on final report. | ₹69,200 / ₹69,200 / ₹34,600 | `CALCULATED` / `SOURCE-DOCUMENT` | Source SOW Table 45; verified arithmetic: 40/40/20% of ₹1.73L. | Linked to deliverable acceptance, not experimental outcomes. | "Milestone payments: 40% (₹69,200), 40% (₹69,200), 20% (₹34,600)." | Section 14 |
| **CLM-07** | Indicative Phase 1 project duration is 20–25 business days. | 20–25 business days | `SOURCE-DOCUMENT` | Source SOW Table 44 & Section 27. | Dependent on timely sample arrival and external laboratory queue times. | "Indicative turnaround of 20–25 business days across 5 structured stages." | Section 13 |
| **CLM-08** | Required sample mass per lot is approximately 2.5–3.0 kg. | 2.5–3.0 kg / lot | `SOURCE-DOCUMENT` / `CALCULATED` | Source SOW Section 3.2; physical allocation budget: 1,750g tests + 500g retention + 300g loss. | Adequate for 1 lot in triplicates; does NOT cover multiple independent lots. | "Recommended sample quantity: 2.5–3.0 kg per lot to support full triplicates, retention, and repeat margin." | Section 7 |
| **CLM-09** | Target lot identity, variety, crop year, and commercial consignment COA. | Lot A1 / Lot B1 | `UNKNOWN/NOT-VERIFIED` | Client custody transfer; COA pending. | No physical samples received yet; cannot fabricate lot numbers or origin data. | "Pending sample dispatch and receipt of Sample Metadata Form from client." | Section 7 |
| **CLM-10** | Standard 15 MT/day conceptual raw feed contains 13,425 kg/day dry solids at 10.5% WB moisture. | 13,425.000 kg/day ds | `CALCULATED` | $15,000 \times (1 - 0.105) = 13,425.000 \text{ kg/day}$. | Baseline assumed moisture of incoming raw grain. | "15,000 kg/day raw grain at 10.5% wet-basis moisture contains 13,425 kg/day dry solids." | Annexure B |
| **CLM-11** | Stated solids loss of 184 kg/day represents 1.3706% loss, not 1.46%. | 1.3706% vs 1.4600% | `CALCULATED` | $184 / 13,425 = 1.370577\%$; $1.46\% \times 13,425 = 196.005 \text{ kg}$. | Two different assumptions in historical records; mathematically distinct. | "Solids loss of 184 kg/day represents 1.3706% of incoming dry solids; distinct from a 1.46% assumption." | Annexure B |
| **CLM-12** | Dried finished product mass at 10.0% WB moisture with 13,241 kg dry solids is 14,712.222 kg/day. | 14,712.222 kg/day | `CALCULATED` | $13,241 / (1 - 0.10) = 14,712.222 \text{ kg/day}$. | Assumes zero mechanical dusting loss in dryer. | "Dried finished product mass: 14,712.222 kg/day containing 1,471.222 kg/day water." | Annexure B |
| **CLM-13** | Scenario B1 pre-dryer mass at 28.0% WB is 18,390.278 kg/day; evaporation is 3,678.056 kg/day. | 3,678.056 kg/day evap | `CALCULATED` | $13,241 / 0.72 = 18,390.278 \text{ kg}$; $5,149.278 - 1,471.222 = 3,678.056 \text{ kg}$. | Strictly contingent on true 28.0% post-drainage moisture. | "Under Scenario B1 (28.0% WB moisture), pre-dryer mass is 18,390.28 kg/day and evaporation is 3,678.06 kg/day." | Annexure B |
| **CLM-14** | Scenario B2 pre-dryer mass of 18,590 kg/day implies 28.7735% WB; evaporation is 3,877.778 kg/day. | 3,877.778 kg/day evap | `CALCULATED` | $5,349 / 18,590 = 28.7735\%$; $5,349 - 1,471.222 = 3,877.778 \text{ kg}$. | Implies higher water retention; drying duty is +5.43% higher than B1. | "Under Scenario B2 (18,590 kg/day wet mass), implied moisture is 28.77% WB and evaporation is 3,877.78 kg/day." | Annexure B |
| **CLM-15** | Sodium content target of <= 150 mg / 100 g dry grain is a project acceptance target, not statutory limit. | $\le 150 \text{ mg/100g}$ | `ASSUMED` / Project Target | Nutritional positioning target for low-sodium commercial claims. | Not an FSSAI statutory ceiling; natural toor dal has 5–30 mg/100g. | "Project acceptance target: finished dal sodium $\le 150 \text{ mg/100g}$ dry grain to ensure neutral flavour and low-sodium positioning." | Section 11 |
| **CLM-16** | FSSAI standard for split pulses limits moisture to max 14.0% w/w and broken grains to max 5.0%. | Max 14.0% moisture, 5.0% broken | `OFFICIAL-REFERENCE` | FSSAI Food Products Standards Regulations 2011, Clause 2.4.6.15. | Mandatory legal threshold for commercial sale in India. | "FSSAI statutory standard 2.4.6.15 mandates moisture $\le 14.0\%$ and broken grains $\le 5.0\%$." | Section 11 |
| **CLM-17** | Candidate treatment formulations (bicarbonate, citrate, hydrothermal) are Phase 2 hypotheses. | Phase 2 Screening Candidates | `HYPOTHESIS` | V10 Directive §6; literature on legume softening. | Untested on target lot; cannot claim efficacy or approval in advance. | "Candidate treatment formulations are strictly proposed Phase 2 hypotheses for subsequent investigation." | Section 10 |
| **CLM-18** | Industrial 15 MT/day plant engineering design is provisional and gated. | Conceptual FEED Annexure | `ASSUMED` | V10 Directive §9; downstream scale-up pathway. | Equipment sizing and economics are provisional pending empirical data. | "The 15 MT/day plant scenario represents a provisional conceptual annexure; final engineering is gated on Phase 1/Phase 2 data." | Annexure B |

---

## 3. Pre-Response Verification Checklist (AGENTS.md & V10 Gate)

```
[Mandatory Pre-Response Verification Checklist]
1. Tool Provenance Audit:
   - Deliverables authored in Microsoft Word (.docx) and exported via Word COM (.pdf).
   - Python calculations verified via independent test scripts.
   - Zero synthetic raster graphics / zero Matplotlib-as-CAD slop.
   -> RESULT: PASS

2. Ground-Truth Data Audit:
   - No experimental results fabricated; all data points labeled PENDING SAMPLE RECEIPT.
   - All mass balance numbers verified to 3 decimal places.
   - Both Scenarios B1 and B2 explicitly presented and labeled provisional.
   -> RESULT: PASS

3. Scope & Empty Space Audit:
   - High information density; complete analytical matrices and hypothesis registers.
   - Strict separation of Phase 1 diagnostic scope from Phase 2/3/4 downstream stages.
   -> RESULT: PASS

4. Attribution Audit:
   - Executing R&D Contractor: FinnoaQ Agro-Industrial Technologies Ltd.
   - Lead Chemical & Process Engineer: Sourish Senapati (FinnoaQ)
   - Academic Guidance & Advisory: Technical Advisory Panel
   - Client Organization: Client Organization (Kolkata)
   - Obsolete/Banned Names: Zero occurrences of "The Client".
   -> RESULT: PASS
```
