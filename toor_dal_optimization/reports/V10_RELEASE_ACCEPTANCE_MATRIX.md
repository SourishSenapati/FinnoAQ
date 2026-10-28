# V10 Final Release Acceptance & Verification Matrix
**Project Reference:** FNQ-PR-2026-001 | Phase 1 Diagnostic R&D Proposal  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Academic Guidance:** Technical Advisory Panel  
**Client Entity:** Client Organization (53, Pathuriaghata Street, Kolkata – 700006)  
**Document Ref:** FNQ-V10-ACC-001  
**Date:** 19-10-2026  
**Git Branch:** `v10-phase1-proposal-reconciliation`  

---

## 1. Executive Release Disposition: PASS
All mandatory verification gates under the **V10 Master Directive** and **AGENTS.md** governance have been fully executed and verified through independent calculation, automated unit tests, and page-by-page visual document inspection. Zero synthetic data, zero premature causal assertions, zero chemical conflations, and zero unverified commercial guarantees exist in the released deliverables.

```
========================================================================================
FINAL RELEASE ACCEPTANCE SUMMARY
========================================================================================
Gate 0: Repository Protection & Source SOW Inventory          -> STATUS: PASS
Gate 1: Scientific & Review Findings (A through F) Audit       -> STATUS: PASS
Gate 2: 36-Section & 14-Deliverable Content Traceability      -> STATUS: PASS
Gate 3: Editable Client Proposal Authoring (DOCX)             -> STATUS: PASS
Gate 4: Independent Numerical & Regulatory Audit (Unit Tests) -> STATUS: PASS
Gate 5: Word COM PDF Export & 14-Page Visual QA Inspection   -> STATUS: PASS
Gate 6: Final Release Handover Package Sign-Off               -> STATUS: PASS
========================================================================================
```

---

## 2. Review Findings Audit & Objective Verification Matrix

| Review Finding | Governing Requirement | Verification Evidence / Check Description | Final Status | Document Location |
| :---: | :--- | :--- | :---: | :--- |
| **Finding A** | Causal mechanisms must remain hypotheses; no assumed root causes. | Purged all "modeled de-esterification" claims; established 10-Hypothesis Register (H1–H10); evidence language ladder enforced. | **PASS** | Proposal Section 6 & `V10_REVIEW_FINDINGS_AND_CHANGELOG.md` |
| **Finding B** | Independent moisture & mass-balance audit; reconcile Scenarios B1 and B2. | Derived from first principles: 15,000 kg/day @ 10.5% WB = 13,425 kg dry solids; audited solids loss (184 kg = 1.3706% vs 1.46% = 196.005 kg); derived final product (14,712.222 kg @ 10% WB); reconciled Scenario B1 (18,390.28 kg pre-dryer, 3,678.06 kg evap) vs Scenario B2 (18,590.00 kg pre-dryer, 28.77% WB, 3,877.78 kg evap, +5.43% drying duty). Status: `UNRESOLVED — SCENARIOS SHOWN`. | **PASS** | Proposal Annexure B & `V10_TECHNICAL_RECONCILIATION.md` |
| **Finding C** | Exact treatment formulations; zero chemical conflation. | Separated NaHCO₃, Na₂CO₃, Trisodium Citrate, Citrate Buffer, and Hydrothermal steeping; defined bath w/w % vs applied grain dose %; pH, wash, dry to 10% WB, 7-day conditioning; labeled `PHASE 2 CANDIDATE — NOT TESTED`. | **PASS** | Proposal Section 10 & `V10_TREATMENT_CANDIDATE_REGISTER.csv` |
| **Finding D** | Distinguish experimental units; audit sample mass budget. | Separated Independent Lots >> Independent Batches >> Technical Repeats >> Subsamples; audited mass allocation (1,750g tests + 500g retention + 300g buffer = 2,550g total); proved 2.5–3.0 kg allocation covers 1 lot in triplicates; provided commercial Options 1 (Baseline ₹1.73L) vs Option 2 (Multi-Lot ₹2.85L); zero five-sigma claims. | **PASS** | Proposal Section 7 & `V10_SAMPLE_AND_REPLICATE_PLAN.csv` |
| **Finding E** | Food safety & regulatory separation; product category definition. | Defined FSSAI Category 2.4.6.15 (Dehulled Split Pulses); separated mandatory FSSAI limits (moisture max 14%, broken max 5%) from Project Acceptance Targets (sodium <= 150 mg/100g, fines <= 2.0%, moisture 10.0% +- 0.5%, aw < 0.60); prohibited tasting uncharacterized lab samples. | **PASS** | Proposal Section 11 & `V10_CLAIM_EVIDENCE_MATRIX.md` |
| **Finding F** | 15 MT/day industrial plant remains provisional. | Separated Phase 1 diagnostic scope from Phase 2/3/4; maintained 15 MT/day plant strictly as provisional conceptual Annexure B; final equipment sizing and economics held gated on empirical bench/pilot data. | **PASS** | Proposal Annexure B & `V10_SCOPE_AND_COMMERCIAL_RECONCILIATION.md` |

---

## 3. Deliverable-by-Deliverable Inventory & Cryptographic Hashes

```
========================================================================================================================
FINAL HANDOVER DELIVERABLE MANIFEST (Branch: v10-phase1-proposal-reconciliation)
========================================================================================================================
Deliverable File Path                                                Size (Bytes)   Status   SHA-256 Cryptographic Hash
------------------------------------------------------------------------------------------------------------------------
deliverables/PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.docx     60,127         PASS     6489c510df3e4d0808ede91041108029cb2fb2b258eccda17e84fdd8b8298f6c
deliverables/PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.pdf     499,170         PASS     2720e0e7142d79e97ea5a311e799e2752e7158b8901043089a5cfebcea6c57de
reports/V10_SOURCE_INVENTORY_AND_PRECEDENCE.md                         8,990         PASS     2aa33afa233ec646d13dd38d0deff4fe12980df2226f4bcdda7f164e3629991a
reports/V10_REVIEW_FINDINGS_AND_CHANGELOG.md                          13,495         PASS     72635eb34e739613013fbd51391274ea23f42e57869c6301d76d4db4b11d4a02
reports/V10_TECHNICAL_RECONCILIATION.md                               11,349         PASS     1564d70ae0cf0e5c794792a22899d6de4b65e3b8ecd394d4b0a7e77bd631f4e8
reports/V10_SCOPE_AND_COMMERCIAL_RECONCILIATION.md                    11,404         PASS     842dba3efabe0737b74544ca6b5b8e4fa181cfe8086372769f12715308a60e44
reports/V10_CLAIM_EVIDENCE_MATRIX.md                                  10,499         PASS     964095be758674f5b558d14c56f78948d3a773683ffb8f793ed40673108e5b98
reports/V10_SOURCE_SOW_TRACEABILITY_MATRIX.md                          8,291         PASS     e6bd45bfe7baa0a7c44dcff0f1ee576ad33f2679d3cf50f61e381bddc272d03d
data/V10_TREATMENT_CANDIDATE_REGISTER.csv                              6,153         PASS     cad98b6fc42394fae1791b873fe215583bb6f94acb3d8608177f18b5cd5717a3
data/V10_SAMPLE_AND_REPLICATE_PLAN.csv                                 2,906         PASS     50e3c8f7eb7b68890f05a91fed0170f89b7b6243533610cd690cf60881182b9c
reports/V10_RELEASE_ACCEPTANCE_MATRIX.md                                [This File]   PASS     [Current Release Sign-off]
========================================================================================================================
```

---

## 4. Visual Document QA Audit (PDF Inspection Report)
- **Renderer Used:** Microsoft Word 2016 COM Automation (Native Windows Word Engine) to PDF; PyMuPDF (1.25.x) for high-resolution 150 DPI page extraction.
- **Total Rendered Page Count:** 14 pages (consistent with Word layout calculation).
- **Inspection Summary:**
  - Page 01: Metadata block, Section 1 Executive Summary, executive table. Zero clipping.
  - Page 02: Mandatory scope callout box, Section 2 Background, whistle context qualification, Section 3 Objectives, Section 4 Phase Architecture table.
  - Page 03: Phase exclusions, Section 5 Work Packages table, Section 6 10-Hypothesis introduction.
  - Page 04: Section 6 10-Hypothesis Register table (H1–H10), Evidence Language Ladder callout box, Section 7 Sample Requirements introduction.
  - Page 05: Section 7 Sample Allocation Budget table (2,550 g per lot vs 2.5–3.0 kg allocation), Options 1 and 2 commercial definitions, Section 8 Investigation introduction.
  - Page 06: Section 8 Technical Investigation Matrix (MOD-01 to MOD-09), Section 9 Experimental Design & Replication Hierarchy.
  - Page 07: Section 9 Standardized Cooking Protocol, Section 10 Future Treatment Candidate Register table (TRT-00 to TRT-06).
  - Page 08: Section 10 Concentration basis note, Section 11 Food Safety & Regulatory table, Section 12 Key Deliverables introduction.
  - Page 09: Section 12 Key Deliverables table (DEL-01 to DEL-14), 23-section final report structure, Section 13 Timeline table (Stages 1–5).
  - Page 10: Section 14 Indicative Cost Structure table (₹1,73,000 line items), Commercial notes, Payment Schedule table (40/40/20%).
  - Page 11: Section 15 Risk Management, Section 16 Confidentiality & Data Ownership, Section 17 Downstream Roadmap, Section 18 Project Acceptance Signature Block.
  - Page 12: Annexure A (Candidate Laboratory Partners: Eureka, Mitra SK, CGCRI, IIT KGP), Annexure B (15 MT/day Derivation & Pre-Dryer Scenarios B1 vs B2).
  - Page 13: Annexure B Equipment Sizing table, Annexure C (Printable Sample Custody & Metadata Form), Annexure D (References).
  - Page 14: Annexure E (Source SOW 36-Section Traceability & Concordance Matrix).
- **Defects Detected & Resolved:** Fixed table row index bounds, eliminated "five-sigma" phrase from body text, added distinct Sodium Carbonate row. Zero blank or clipped pages.

---

## 5. One Precise Next Human Action
**Action for Client Leadership (Technical Advisory Panel, Client Organization):**
Review and endorse Section 18 of the client proposal `deliverables/PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.docx` (or `.pdf`), confirming selection of **Option 1 (Baseline Scoped Study at ₹1,73,000 + GST)** or **Option 2 (Multi-Lot Expanded Study at ₹2,85,000 + GST)**, and issue sample dispatch tracking details with the enclosed Annexure C Metadata Form to initiate project mobilization.
