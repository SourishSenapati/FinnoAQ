# DESIGN MATURITY AND GATE RELEASE MATRIX (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-019  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Quality Systems, Engineering Governance & Verification  

---

## 1. Design Maturity Classification Framework

Every engineering deliverable in the Harakutir Toor Dal repository is assigned a controlled maturity level and approval status:

| Maturity Stage Tag | Technical Definition & Scope | Permitted Commercial / Project Usage | Release Authority Required |
| :--- | :--- | :--- | :--- |
| `CONCEPT_ONLY` | Early process flow alternatives, block layouts, unverified literature analogies | Internal R&D brainstorming; hypothesis generation only | Chemical Engineering Lead |
| `PRELIMINARY_CALCULATED` | Sized from first principles; assumptions and bounds explicit; verified by unit tests | Feasibility studies; budgetary cost estimation; lab protocol design | Senior Food Process & Chemical Eng |
| `FOR_QUOTATION` | Detailed equipment datasheets, nozzle schedules, motor specs for supplier pricing | Vendor bidding; budgetary RFQ packages; RFP issuance | Project Procurement Manager |
| `FOR_ENGINEERING_REVIEW` | Packaged engineering drawings, calculation dossiers, P&IDs, civil loads | Peer review by registered professional engineers (PE / Chartered Eng) | Multi-Disciplinary Engineering Lead |
| `APPROVED_FOR_FABRICATION`| Signed drawings with fabrication tolerances, WPS/PQR, site soil data confirmed | Workshop metal cutting; vessel rolling; equipment procurement | Licensed Professional Engineer & Client Sign-Off |
| `AS_BUILT` | Red-lined drawings updated after physical installation, SAT, and commissioning | Operations, preventative maintenance, statutory factory license | Commissioning Lead & Plant Operations Head |

---

## 2. Artifact Maturity & Release Gate Register

The master matrix below maps all 20 core project reports, 10 CAD drawings, and datasets to their current maturity, owner, review requirement, missing input, and gating conditions:

| Artifact Identifier & Name | Discipline Owner | Current Maturity Level | Critical Missing Input Before Next Stage | Mandatory Release Gate |
| :--- | :--- | :---: | :--- | :---: |
| **ENG-REP-001: Execution Plan** | Project Management | `PRELIMINARY_CALCULATED` | Formal client sign-off on 16h operating schedule | **Gate G-C** |
| **ENG-REP-002: Design Basis** | Process Design | `PRELIMINARY_CALCULATED` | Soil test report (SITE-INQ-02), SPCB consent (SITE-INQ-03) | **Gate G-C** |
| **ENG-REP-003: Process Selection** | Chemical Eng | `PRELIMINARY_CALCULATED` | Kitchen trial cooking time validation on target lot | **Gate G-A** |
| **ENG-REP-004: Mass/Energy Balances** | Process Eng | `PRELIMINARY_CALCULATED` | Target lot bench water uptake & wash leaching assay | **Gate G-A** |
| **ENG-REP-005: Equipment Sizing** | Mechanical Eng | `PRELIMINARY_CALCULATED` | Pilot fluid-bed drying curve validation (100 kg batch) | **Gate G-B** |
| **ENG-REP-006: Custom Machine Dossiers**| Machine Design | `PRELIMINARY_CALCULATED` | Agitator vendor mechanical seal drawing review | **Gate G-D** |
| **ENG-REP-007: CAD Drawing Register** | CAD Lead | `PRELIMINARY_CALCULATED` | Final site plot boundary survey (SITE-INQ-01) | **Gate G-C** |
| **ENG-REP-008: Plant Layout & Zoning** | Civil / Food Safety | `PRELIMINARY_CALCULATED` | Client confirmation of container truck turning radius | **Gate G-C** |
| **ENG-REP-009: Piping & Control P&ID** | Piping / Controls | `PRELIMINARY_CALCULATED` | Control valve vendor Cv sizing data sheets | **Gate G-D** |
| **ENG-REP-010: Electrical & Automation**| Electrical Eng | `PRELIMINARY_CALCULATED` | Grid electricity board sanctioned HT kVA (SITE-INQ-04) | **Gate G-C** |
| **ENG-REP-011: Civil & Structural Basis**| Civil / Structural | `PRELIMINARY_CALCULATED` | Soil test boreholes confirming SBC $\ge 150\text{ kN/m}^2$ | **Gate G-D** |
| **ENG-REP-012: Safety & Regulatory** | Food Scientist | `PRELIMINARY_CALCULATED` | Formal legal opinion on FSSAI INS 500(ii) labeling | **Gate G-C** |
| **ENG-REP-013: Utility & Wastewater** | Environmental Eng | `PRELIMINARY_CALCULATED` | Local CETP acceptance letter / ZLD requirement | **Gate G-C** |
| **ENG-REP-014: BOM & CapEx Estimate** | Cost Estimator | `PRELIMINARY_CALCULATED` | Vendor formal competitive quotations (AACE Class 3) | **Gate G-D** |
| **ENG-REP-015: Commissioning Plan** | QA / Commissioning | `PRELIMINARY_CALCULATED` | Target lot laboratory baseline variance ($\sigma_{baseline}$) | **Gate G-A** |
| **ENG-REP-016: Operations & Training** | Plant Operations | `PRELIMINARY_CALCULATED` | Operator headcount approval by Harakutir HR | **Gate G-E** |
| **DWG-001 to 010: DXF CAD Package** | CAD Drafting | `PRELIMINARY_CALCULATED` | Licensed Civil/Structural engineer seal and signature | **Gate G-D** |
| **CAD-STEP-001 to 004: 3D Models** | 3D Mechanical | `PRELIMINARY_CALCULATED` | Vessel fabricator plate rolling tool constraints | **Gate G-D** |
