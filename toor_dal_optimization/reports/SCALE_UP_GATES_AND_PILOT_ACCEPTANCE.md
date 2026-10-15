# HARAKUTIR TOOR DAL — SCALE-UP GATES & PILOT ACCEPTANCE CRITERIA

**Document ID:** FIN-GAT-PILOT-2026-002  
**Date:** 15 October 2026  
**Governing Standard:** Master Build Directive — Scale-Up Evidence Chain & Engineering Gates  
**Status:** **GATES G0 PASSED; GATES G1 THROUGH G5 FORMALLY LOCKED**  

---

## 1. Governance Architecture: The 6 Engineering Gates

To prevent capital misallocation, premature commercial promises, and regulatory non-compliance, all scale-up activities are strictly controlled by a sequential 6-gate engineering governance framework:

```
  [ GATE G0 ] ──► [ GATE G1 ] ──► [ GATE G2 ] ──► [ GATE G3 ] ──► [ GATE G4 ] ──► [ GATE G5 ]
  Computational    Target-Lot      Confirmatory    100 kg Pilot    Regulatory &     15 MT/Day
   Feasibility      Kitchen         Replication     Continuous      Food-Safety    Commercial
  & Code Audit     Screening      & Re-Drying Run   Operations       Sign-Off      Commissioning
   (PASSED)        (CURRENT)       (LOCKED)         (LOCKED)        (LOCKED)        (LOCKED)
```

**Non-Negotiable Rule:** A gate cannot be bypassed. Passing unit tests or simulation scores cannot unlock physical gates. Each gate requires signed physical assay certificates and empirical data before advancing.

---

## 2. Gate-by-Gate Acceptance Criteria & Evidence Deliverables

| Gate ID & Title | Objective & Scope | Required Test Samples & Batch Scale | Quantitative Acceptance Criteria | Required Physical Deliverables & Certificates | Gate Decision & Unlock Authority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GATE G0:** Computational Feasibility & Red-Team Audit | Forensic code audit, mass/energy balance closure, profiler ground truth, literature review. | Entire repository codebase & benchmarks | • Mass conservation error $< 1e-4\%$.<br>• Zero hard-coded outcomes in candidate loop.<br>• Retraction of automatic 5-sigma guarantee.<br>• Test suite passing $100\%$. | • [FORENSIC_AUDIT_AND_CLAIM_LEDGER.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/FORENSIC_AUDIT_AND_CLAIM_LEDGER.md)<br>• [LITERATURE_AND_REGULATORY_REGISTER.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/LITERATURE_AND_REGULATORY_REGISTER.md)<br>• 72 passing regression tests. | **PASSED.** Unlocks Gate G1 physical kitchen screening. |
| **GATE G1:** Target-Lot Bench Kitchen Screening | Rapid laboratory evaluation of 7 candidate interventions against untreated control. | $n = 2$ batches per candidate ($100\text{ g}$ dal per run); $5.0\text{ kg}$ total grain | • Mean cooking time $\le 16.0\text{ min}$ ($\le 4.0\text{ whistles}$).<br>• Initial tenderness score $\ge 1.5 / 2.0$.<br>• Sensory acceptability $\ge 7.0 / 9.0$.<br>• No severe soapy, alkaline, or sour defects. | • Kitchen data capture sheet with thermocouple logs.<br>• Whistle interval logs.<br>• Sensory panel evaluation sheets.<br>• Screening ranking report. | **CURRENT ACTIVE GATE.** Must pass before Gate G2. |
| **GATE G2:** Confirmatory Replication & Re-Drying Run | Formal statistical confirmation of top candidate ($0.50\%\ \text{NaHCO}_3$) on re-dried, shelf-stable dal. | $n = 4$ independent process replicates control vs $n = 4$ treated; dried to $10.0\%$ moisture | • Welch's t-test: $t_{\text{obs}} \ge 3.707$ ($p \le 0.005$).<br>• Cook time $\le 15.0\text{ min}$ ($\le 3.5\text{ whistles}$).<br>• Dried moisture $10.0 \pm 0.5\%$, $a_w \le 0.65$.<br>• Sensory score $\ge 7.5 / 9.0$.<br>• 30-day conditioned cooking retention. | • Statistical significance report.<br>• AOAC moisture oven test certificates.<br>• Water activity meter logs.<br>• Tactile firmness extrusion data. | **LOCKED.** Unlocks Gate G3 pilot trials upon sign-off. |
| **GATE G3:** Representative Pilot Line Run (100 kg) | Integrated demonstration through all unit operations (soaking, draining, rinsing, fluid bed drying). | $100.0\text{ kg}$ pilot batch (100 kg feed, $150\text{ kg}$ liquor, pilot fluid bed dryer) | • True dry solids recovery $\ge 95.5\%$.<br>• Wash leaching loss $\le 2.0\%$.<br>• Final packaged moisture $10.0 \pm 0.3\%$.<br>• Retained sodium $< 100\text{ mg / 100g}$.<br>• No grain breakage/fines increase $> 2.0\%$. | • Pilot mass & energy balance sheet.<br>• Effluent composite sample analysis (TDS, COD, pH).<br>• Pilot dryer air temperature & moisture logs.<br>• NABL gravimetric recovery certificate. | **LOCKED.** Unlocks Gate G4 regulatory submissions. |
| **GATE G4:** Food Safety & Regulatory Clearance | Verification of statutory compliance under FSSAI standards and environmental regulations. | Representative packaged pilot samples & effluent aliquots | • FSSAI Food Additive compliance (INS 500(ii) Table 3 GMP).<br>• NABL test report: Retained elemental $\text{Na} < 350\text{ mg/100g}$.<br>• Standard plate count $< 10^4\text{ CFU/g}$, Coliforms absent.<br>• SPPCB effluent compliance consent. | • Accredited NABL test certificates.<br>• Legal food regulatory counsel opinion letter.<br>• Approved packaging artwork & nutrition label.<br>• Environmental discharge permit draft. | **LOCKED.** Unlocks Gate G5 commercial procurement. |
| **GATE G5:** 15 MT/Day Commercial Commissioning | Detailed engineering, equipment procurement, installation, and commissioning qualification. | Full commercial scale ($15,000\text{ kg/day}$ feed rate over $16\text{ h}$) | • Sustained capacity: $937.5\text{ kg/h}$ feed ($1,268\text{ kg/h}$ design peak).<br>• Packaged output $\ge 14,350\text{ kg/day}$ at $10.0\%$ moisture.<br>• Specific thermal duty $\le 1.15\text{ MJ/kg dal}$.<br>• Zero safety or environmental excursions over 72h continuous run. | • Performance guarantee test run certificate.<br>• Factory Acceptance Test (FAT) sign-offs.<br>• P&ID as-built drawings.<br>• Standard Operating Procedures (SOPs). | **LOCKED.** Unlocked only by Client Steering Committee. |

---

## 3. Pilot Unit Operation Requirements (Gate G3)

When Gate G2 passes, a representative pilot campaign ($100\text{ kg}$ batch) must validate the continuous unit operations:

1. **Pilot Soaking Vessel:** $250\text{ L}$ stainless steel vessel equipped with $1.0\text{ mm}$ false-bottom wedge-wire screen. Evaluate gravity draining time and verify liquor hold-up in the cotyledon bed.
2. **Pilot Rinsing Rig:** Calibrated spray nozzle bar operating at $2.0\text{ bar}$. Measure washout fraction ($25\%$ target) and effluent chemical recovery.
3. **Pilot Fluid Bed Dryer:** Continuous or batch fluid bed dryer operating with air at $55.0^\circ\text{C}$. Measure drying kinetics curve (Page model fitting), bed pressure drop, and verify exit product moisture ($10.0 \pm 0.3\%$).
4. **Cooling & Packaging Check:** Verify product temperature discharges below $30^\circ\text{C}$ before packing into $1.0\text{ kg}$ retail bags.

---

## 4. Current Governance Status Declaration

- **Gates G0:** **PASSED.**
- **Gates G1 through G5:** **STRICTLY LOCKED.**
- **Commercial Engineering Status:** 15 MT/day process design calculations, stream tables, and economic models are fully developed for planning purposes, but **operational performance, costs, and product claims remain strictly provisional** until Gate G3 pilot-scale mass/energy data and Gate G4 regulatory clearances are obtained.
