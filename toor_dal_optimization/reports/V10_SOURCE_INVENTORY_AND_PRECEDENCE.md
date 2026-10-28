# V10 Source Inventory, Document Precedence & Forensic Baseline
**Project Reference:** FNQ-PR-2026-001 / Phase 1 Diagnostic R&D Proposal  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Academic Guidance:** Technical Advisory Panel  
**Client Entity:** Client Organization (53, Pathuriaghata Street, Kolkata – 700006, West Bengal, India)  
**Document Ref:** FNQ-V10-INV-001  
**Date:** 19-10-2026  
**Git Branch:** `v10-phase1-proposal-reconciliation`  
**Base Commit (HEAD):** `20cecb1` (v8-integrated-engineering-constitution)  

---

## 1. Executive Summary & Gate 0 Disposition
This document inventories all active and historical project files, establishes rigorous source precedence, records cryptographic SHA-256 hashes, reconciles party identities, and sets the factual baseline for the **V10 Master Directive**. 

Under **Section 0 and Section 1 of the V10 Master Directive**, the primary scope baseline for Phase 1 is the 22-page document `Phase1_Scope_of_Work_Toor_Dal.docx` (36 numbered sections, 48 structured tables, ₹1,73,000 + GST indicative professional fee, 20–25 business day schedule, 40/40/20 milestone schedule). Prior AI iterations that prematurely declared causal mechanisms, simulated 15 MT/day plant designs, conflated chemical reagents, or mixed contradictory moisture/solids bases are categorized as **Level 9 (Untrusted / Prior AI Output)** and are replaced by independent first-principles derivations.

---

## 2. Document Precedence Hierarchy
Under Section 1.3 of the Directive, all claims, parameters, and commercial figures adhere to this strict hierarchy:

| Level | Document Class / Source Type | Authority Status | Usage in V10 Package |
| :---: | :--- | :--- | :--- |
| **Level 1** | Explicitly Approved Client Agreement / Signed Contract | Highest Authority | None currently signed; document issued as proposal for client approval. |
| **Level 2** | Original Phase 1 SOW (`Phase1_Scope_of_Work_Toor_Dal.docx`) | Primary Baseline | Controls Phase 1 diagnostic scope, 14 deliverables, ₹1,73,000 fee, 20–25 day timeline, and testing matrix. |
| **Level 3** | Traceable Raw Lab Data, COAs, Calibration Certificates | Ground Truth | Currently `PENDING CLIENT RECEIPT` — no target lot has been sampled or tested yet. |
| **Level 4** | Official Standards & Statutory Regulations (FSSAI Compendium, BIS) | Statutory Truth | Authoritative for food additive permissions and standard product definitions; distinguished from project targets. |
| **Level 5** | Verified Third-Party Quotations / Accreditations | Confirmed Commercial | Eureka Analytical, Mitra S.K., CGCRI, IIT KGP are candidate facilities to be quoted; not confirmed vendors. |
| **Level 6** | Peer-Reviewed Literature & Technical Handbooks | Scientific Reference | Contextual evidence for mechanisms/methods; cannot substitute for target lot measurements. |
| **Level 7** | Traceable Internal Engineering Calculations | Verified Model | Independent moisture/mass balance audit reconciling Scenarios B1 and B2; fee and sample mass arithmetic. |
| **Level 8** | Explicit Project Hypotheses & Working Assumptions | Provisional | 10 competing hypotheses (H1–H10); provisional 15 MT/day industrial plant scenario. |
| **Level 9** | Prior AI Reports / Unverified Script Outputs | Untrusted Baseline | Audited and corrected; all synthetic assertions, five-sigma claims, and premature causal conclusions purged. |

---

## 3. Comprehensive Repository Inventory & Cryptographic Hashes

| File Path | Size (Bytes) | Last Modified | SHA-256 Cryptographic Hash | Precedence Level | Description & Role |
| :--- | :---: | :---: | :--- | :---: | :--- |
| `toor_dal_optimization/inputs/Phase1_Scope_of_Work_Toor_Dal.docx` | 44,287 | 2026-10-11 00:49:16 | `a4474b10353f98eef1833a6af865169444bc9e6dd4faaf9d32fc18ce13a485e6` | **Level 2** | Primary Source Baseline (22 pages, 36 sections, 48 tables). |
| `toor_dal_optimization/backup_v10/Phase1_Scope_of_Work_Toor_Dal_ORIGINAL_BACKUP.docx` | 44,287 | 2026-10-19 13:39:13 | `a4474b10353f98eef1833a6af865169444bc9e6dd4faaf9d32fc18ce13a485e6` | **Level 2 (Backup)** | Immutable dated backup of the original source document. |
| `toor_dal_optimization/inputs/Toor_Dal_Quick_Cooking_RD_Master_Technical_Scope.docx` | 40,643 | 2026-09-21 13:47:09 | `6b7bb876f1528096f626cd6cb039a772132b345d655755b873912513f0ed8ecb` | **Level 2 (Reference)** | Early technical scope draft (65 paragraphs, 11 tables). |
| `toor_dal_optimization/inputs/FINNOAQ_MASTER_PROMPT.txt` | 54,072 | 2026-10-16 14:31:28 | `a309c875a08212ea6c1d5c41e59ca6ea11a8cdc5282be2708a1caf68a560e940` | **Level 8** | Contextual prompt instructions and historical directives. |
| `AGENTS.md` | 4,609 | 2026-10-16 23:33:20 | `805bb6cf85cc684f205619635d0cc99669490d10cade05730d64836ae096690f` | **Workspace Law** | Workspace Governance, Anti-Fraud Directive, Attribution Rules. |
| `toor_dal_optimization/output/client_proposal_v6/CLIENT_PROJECT_PROPOSAL.docx` | 3,191,727 | 2026-10-16 22:46:32 | `e7e3a64ac7ac259babea04732bc5ee982e93462b7bfeaeed5f55e8b5adbc4269` | **Level 9** | Historical V6 Proposal Draft (contained premature plant designs). |
| `toor_dal_optimization/output/client_proposal_v6/CLIENT_PROJECT_PROPOSAL.pdf` | 1,610,824 | 2026-10-16 22:46:45 | `94ac5a1d18e74a2e83fca5fcee4f5f6b445c26c7a1dd956e3dcbac087ec33b54` | **Level 9** | Historical V6 Rendered PDF. |
| `toor_dal_optimization/deliverables/V8_CLIENT_ONBOARDING_AND_ENGINEERING/CLIENT_PROJECT_PROPOSAL.docx` | 46,467 | 2026-10-17 04:28:17 | `cf5acfaa4b12285b06054e451c822bf27fe1b44aeac6892fae1c280386bde46c` | **Level 9** | V8 Proposal Draft (reconciled commercial terms, but needed V10 corrections). |
| `toor_dal_optimization/reports/V8_BALANCE_AND_COST_RECONCILIATION.md` | 3,440 | 2026-10-17 00:12:11 | `75ec4309830277cd87ad7af4c48fc5079a243401a622c9703e884525ca5ef7bc` | **Level 7** | V8 Mass & Energy Balance Audit. |
| `toor_dal_optimization/reports/V8_COMMERCIAL_APPROVAL_CHECKLIST.md` | 1,965 | 2026-10-17 00:14:31 | `2cea3dd1dfec7c8a76c3049a7db2b875592bd560478151452fd25e68b941d1fb` | **Level 7** | Commercial checklist baseline. |
| `toor_dal_optimization/scratch/source_sow_rendered.pdf` | 239,944 | 2026-10-19 13:45:43 | `2d46e31ff73db64627d351be8c28731d17e945c79bfcf6e9e4215f9b4c09d57a` | **Level 2 (Rendered)** | Microsoft Word COM automation render of original SOW (22 pages). |

---

## 4. Identity Reconciliation & Governance Audit

### 4.1 Client vs. Contractor Roles
- **Client Organization:** **Client Organization** (53, Pathuriaghata Street, Kolkata – 700006, West Bengal, India). Represented by Technical Advisory Panel.
- **Executing Contractor / R&D Consultancy:** **FinnoaQ Agro-Industrial Technologies Ltd.**
- **Lead Chemical & Process Engineer:** Sourish Senapati (FinnoaQ).
- **Academic Guidance / Research Advisory:** Technical Advisory Panel.

### 4.2 Prohibited Nomenclature & Quality Rule
- Under `AGENTS.md`, any misspelling of the client organization as `"The Client"` (with an intrusive 'n') is an obsolete typo and is strictly prohibited across all documents.
- Client identity is strictly preserved as **Client Organization**.
- No legal suffixes or corporate entities are invented.

---

## 5. Scope Boundary Demarcation (Phases 1 through 4)

1. **Phase 1 (Current Proposal Offering):** Comparative Diagnostic R&D Study.
   - Core Objective: Standardized baseline comparison between Tanzanian imported split toor dal and Indian benchmark; objective cooking measurement; root-cause discrimination across 10 competing hypotheses.
   - Budget: ₹1,73,000 + applicable GST (commercial ceiling up to ₹2,00,000 + GST).
   - Indicative Timeline: 20–25 business days.
   - Status: Proposed for client review and commissioning.
2. **Phase 2 (Future Separately Approved Stage):** Treatment Development & Mechanistic Validation.
   - Controlled laboratory screening of chemical/physical interventions; dose-response, pH, dewatering, storage stability, sensory, and kinetics.
   - Status: Gated future work; candidate treatments presented solely as research hypotheses.
3. **Phase 3 (Future Industrial Scale-Up):** Pilot Production & Shelf-Life Validation.
   - Pilot-scale runs, process validation, microbial safety hold times, packaging trials, empirical effluent load.
   - Status: Out of scope for Phase 1.
4. **Phase 4 (Future Plant Execution):** 15,000 kg/day Plant Design & FEED.
   - Detailed mechanical engineering, PFD/P&ID freeze, equipment procurement, plant construction.
   - Status: Out of scope for Phase 1; included only as a provisional downstream conceptual scenario.

---

## 6. Gate 0 Acceptance Status: PASS
- All source documents protected, inventoried, and cryptographically hashed.
- Working branch `v10-phase1-proposal-reconciliation` created and verified.
- Precedence hierarchy locked.
- Baseline ready for Stage 1 Scientific and Commercial Audits.
