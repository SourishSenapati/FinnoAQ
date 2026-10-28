# EVIDENCE-BACKED REPOSITORY INVENTORY AND AUDIT PROVENANCE MANIFEST
**Document ID:** MANIFEST-FREEZE-2026-10-15  
**Version Identifier:** `AUDIT-FREEZE-20261015-V1.0`  
**Audit Timestamp:** 2026-10-15T19:05:00+05:30  
**Auditor:** Independent Process Red-Team Auditor  
**Status:** `EVIDENCE_BACKED_AUDIT` — **PRELIMINARY—NOT FOR CONSTRUCTION**  

---

## 1. Audit Summary by Evidence Status

A total of **305 project artifacts** have been audited and cryptographically hashed (SHA-256).
In accordance with Directive Rule B, all path-derived assertions have been removed. Every artifact defaults to `UNVERIFIED` unless supported by a named check, test, or forensic inspection.

| Evidence Status | File Count | Description & Quality Boundary |
| :--- | :---: | :--- |
| `CALCULATED_RECONCILED` | 3 | First-principles calculations verified by automated regression test |
| `TEST_SUITE_PASSING` | 12 | Automated pytest suite (verified passing 80/80 in 13.76s) |
| `PRE_REGISTERED_TEMPLATE` | 1 | Blank experimental logging template (zero synthetic data) |
| `PROTOCOL_READY_FOR_REVIEW`| 1 | Formal protocol for human sign-off; physical trials not started |
| `FROZEN_BASIS` | 1 | Formal engineering design basis awaiting client operational freeze |
| `AUDITED_REPORT` | 1 | Master red-team audit report |
| `PRELIMINARY_CONCEPT_GEOMETRY` | 3 | CAD drawings with vector geometry (lacks details / 1:1 scale) |
| `DEFECTIVE_HEADER_ONLY` | 4 | STEP models with empty 27-line headers (0 B-Rep solids) |
| `DEFECTIVE_PLACEHOLDER_ONLY`| 7 | DXF drawings with title block border only (0 vector symbols) |
| `DEFECTIVE_PARTIAL_MESH` | 1 | OBJ mesh missing nozzles, legs, flanges |
| `PRELIMINARY_CALCULATED` | 1 | Unreviewed preliminary engineering calculations |
| `UNVERIFIED` | 270 | Legacy documentation / scripts lacking formal evidence checks |

---

## 2. Key Verified & Reconciled Calculation Engines

| File Path | SHA-256 | Status | Named Evidence Reference | Limitations |
| :--- | :--- | :---: | :--- | :--- |
| [`data/kitchen_screening_4conditions_template.csv`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/data/kitchen_screening_4conditions_template.csv) | `ef817ba0febfa00d...` | `PRE_REGISTERED_TEMPLATE` | reports/EXPERIMENTAL_SCREENING_AND_CONFIRMATION_PROTOCOL.md | Blank logging sheet; physical screening data not yet collected |
| [`reports/EXPERIMENTAL_SCREENING_AND_CONFIRMATION_PROTOCOL.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/EXPERIMENTAL_SCREENING_AND_CONFIRMATION_PROTOCOL.md) | `109ede08b559d1ef...` | `PROTOCOL_READY_FOR_REVIEW` | Pre-registered 4-condition protocol design | Ready for human review; physical trial not yet started |
| [`reports/FORENSIC_ENGINEERING_AUDIT_AND_RECONCILIATION.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/FORENSIC_ENGINEERING_AUDIT_AND_RECONCILIATION.md) | `ce3b6d516a113e14...` | `AUDITED_REPORT` | Red-team audit document AUDIT-REP-2026-003 | Preliminary audit; awaiting bench trial results for physical gate unlocking |
| [`src/finnoaq/detailed_machine_and_plant_engineering.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/src/finnoaq/detailed_machine_and_plant_engineering.py) | `ff89f2028452d35c...` | `CALCULATED_RECONCILED` | tests/test_end_to_end_plant_engineering.py::test_fluid_bed_dryer_psychrometrics_and_thermal_duty | Preliminary sizing; empirical drying rate coefficient pending pilot validation |
| [`src/finnoaq/dose_calculator.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/src/finnoaq/dose_calculator.py) | `8b07b8ac178f7ac2...` | `CALCULATED_RECONCILED` | tests/test_plant_design_and_mass_balance.py::test_dose_calculator_multi_basis_separation | Recipe concentration pending physical kitchen titration results |
| [`src/finnoaq/mass_balance.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/src/finnoaq/mass_balance.py) | `03ff2b71e7e420e2...` | `CALCULATED_RECONCILED` | tests/test_audit_reconciliation_and_contradictions.py::test_solids_recovery_and_basis_separation | Loss fractions are preliminary engineering bounds; require target lot confirmation |

---

## 3. CAD & Fabrication Defects Register (Truth Table)

| File Path | Entity / Line Count | Status | Defect & Evidence Reference | Fabrication Limitation |
| :--- | :---: | :---: | :--- | :--- |
| [`engineering/cad/dxf/DWG-FIN-15T-001.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-001.dxf) | 26136 B | `PRELIMINARY_CONCEPT_GEOMETRY` | Forensic Inspection DEF-CAD-05 (A1 mm scaling, 35 entities) | Scaled to A1 sheet mm; INSUNITS unset; NOT FOR CONSTRUCTION |
| [`engineering/cad/dxf/DWG-FIN-15T-002.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-002.dxf) | 23422 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/dxf/DWG-FIN-15T-003.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-003.dxf) | 23419 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/dxf/DWG-FIN-15T-004.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-004.dxf) | 23419 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/dxf/DWG-FIN-15T-005.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-005.dxf) | 30624 B | `PRELIMINARY_CONCEPT_GEOMETRY` | Forensic Inspection DEF-CAD-04 & DEF-CAD-05 (55 entities) | Elevation only; lacks plan view & weld symbols; NOT FOR CONSTRUCTION |
| [`engineering/cad/dxf/DWG-FIN-15T-006.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-006.dxf) | 23425 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/dxf/DWG-FIN-15T-007.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-007.dxf) | 29108 B | `PRELIMINARY_CONCEPT_GEOMETRY` | Forensic Inspection DEF-CAD-05 (49 entities) | Elevation only; lacks structural duct support details; NOT FOR CONSTRUCTION |
| [`engineering/cad/dxf/DWG-FIN-15T-008.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-008.dxf) | 23412 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/dxf/DWG-FIN-15T-009.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-009.dxf) | 23423 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/dxf/DWG-FIN-15T-010.dxf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/dxf/DWG-FIN-15T-010.dxf) | 23417 B | `DEFECTIVE_PLACEHOLDER_ONLY` | Forensic Inspection DEF-CAD-02 (18 entities, border only) | Zero schematic/piping geometry in vector format; unusable for contractor bidding |
| [`engineering/cad/step/AG-101_Agitator.step`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/step/AG-101_Agitator.step) | 15897 B | `DEFECTIVE_HEADER_ONLY` | Forensic Inspection DEF-CAD-01 (0 B-Rep solids, 27 lines) | Empty header without solid topology; unusable for CAM/CNC |
| [`engineering/cad/step/DR-101_Fluid_Bed_Dryer.step`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/step/DR-101_Fluid_Bed_Dryer.step) | 25228 B | `DEFECTIVE_HEADER_ONLY` | Forensic Inspection DEF-CAD-01 (0 B-Rep solids, 27 lines) | Empty header without solid topology; unusable for CAM/CNC |
| [`engineering/cad/step/SK-100_Dosing_Skid.step`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/step/SK-100_Dosing_Skid.step) | 11887 B | `DEFECTIVE_HEADER_ONLY` | Forensic Inspection DEF-CAD-01 (0 B-Rep solids, 27 lines) | Empty header without solid topology; unusable for CAM/CNC |
| [`engineering/cad/step/TK-101_Soak_Tank.step`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/step/TK-101_Soak_Tank.step) | 17167 B | `DEFECTIVE_HEADER_ONLY` | Forensic Inspection DEF-CAD-01 (0 B-Rep solids, 27 lines) | Empty header without solid topology; unusable for CAM/CNC |
| [`engineering/cad/obj/TK-101_Soak_Tank.obj`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/obj/TK-101_Soak_Tank.obj) | 2935 B | `DEFECTIVE_PARTIAL_MESH` | Forensic Inspection DEF-CAD-03 (open cylinder only) | Missing flanges, legs, baffles, nozzles; crude layout use only |