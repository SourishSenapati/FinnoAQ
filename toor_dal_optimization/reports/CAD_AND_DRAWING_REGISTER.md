# CAD AND ENGINEERING DRAWING REGISTER (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-007  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** CAD & Engineering Documentation  

---

## 1. Controlled Drawing Register

The table below lists all 10 official engineering drawings generated for the Harakutir 15 MT/day facility. All drawings have been procedurally generated, verified against sizing calculations, and stored as editable vector DXF files and multi-page vector PDF drawing packages:

| Drawing Number | Revision | Sheet Title | Discipline | Sheet Size | Source File Paths | Design Maturity | Statutory Disclaimer |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :--- |
| **DWG-FIN-15T-001** | Rev 1.0 | Plant Master Plot Plan & Hygienic Zoning Layout | Civil / Plant | A1 | `engineering/cad/dxf/DWG-FIN-15T-001.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-002** | Rev 1.0 | Process Flow Diagram (PFD) with Stream Overlay | Process Eng | A1 | `engineering/cad/dxf/DWG-FIN-15T-002.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-003** | Rev 1.0 | P&ID - Raw Feed Intake, Dosing & Soaking System | Process / Piping | A1 | `engineering/cad/dxf/DWG-FIN-15T-003.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-004** | Rev 1.0 | P&ID - Fluid-Bed Drying, Cooling & Packaging | Process / Piping | A1 | `engineering/cad/dxf/DWG-FIN-15T-004.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-005** | Rev 1.0 | Soak Tank TK-101A/B General Arrangement Drawing | Mechanical | A1 | `engineering/cad/dxf/DWG-FIN-15T-005.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-006** | Rev 1.0 | Low-Shear Agitator AG-101 Mechanical Assembly | Mechanical | A1 | `engineering/cad/dxf/DWG-FIN-15T-006.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-007** | Rev 1.0 | Fluid-Bed Dryer DR-101 General Arrangement | Mechanical | A1 | `engineering/cad/dxf/DWG-FIN-15T-007.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-008** | Rev 1.0 | Chemical Dosing Skid SK-100 Equipment & Piping GA | Mechanical / Skid | A1 | `engineering/cad/dxf/DWG-FIN-15T-008.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-009** | Rev 1.0 | Electrical Single Line Diagram (SLD) & MCC | Electrical | A1 | `engineering/cad/dxf/DWG-FIN-15T-009.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |
| **DWG-FIN-15T-010** | Rev 1.0 | Civil Foundations Loading Plan & Drainage Layout | Civil / Structural | A1 | `engineering/cad/dxf/DWG-FIN-15T-010.dxf` | `PRELIMINARY_CALCULATED` | `PRELIMINARY—NOT FOR CONSTRUCTION` |

---

## 2. 3D CAD Exchange Models (ISO 10303-21 STEP & Wavefront OBJ)

The custom machinery models are exported in industry-standard open exchange formats for direct import into SolidWorks, Autodesk Inventor, PTC Creo, and FreeCAD:

| Model Identifier | Equipment Tag | Description | Formats Available | File Path | File Verification Status |
| :--- | :--- | :--- | :---: | :--- | :---: |
| **CAD-STEP-001** | `TK-101` | Jacketed Soak Vessel with Dished Heads & Nozzles | STEP AP214, OBJ, STL | `engineering/cad/step/TK-101_Soak_Tank.step` | Verified Non-Empty |
| **CAD-STEP-002** | `AG-101` | Low-Shear Agitator with 60mm Shaft & Hydrofoil | STEP AP214 | `engineering/cad/step/AG-101_Agitator.step` | Verified Non-Empty |
| **CAD-STEP-003** | `DR-101` | Continuous Vibrating Fluid-Bed Dryer & Plenum | STEP AP214 | `engineering/cad/step/DR-101_Fluid_Bed_Dryer.step` | Verified Non-Empty |
| **CAD-STEP-004** | `SK-100` | Chemical Dissolution & Dosing Skid Assembly | STEP AP214 | `engineering/cad/step/SK-100_Dosing_Skid.step` | Verified Non-Empty |
| **CAD-MESH-001** | `TK-101` | 3D Triangular Polygon Mesh of Vessel Body | Wavefront OBJ | `engineering/cad/obj/TK-101_Soak_Tank.obj` | Verified Non-Empty |

---

## 3. High-Resolution Vector PDF Drawing Booklet

All 10 drawings are compiled into an integrated vector PDF engineering package:
- **File Location:** [`engineering/cad/pdf/HARAKUTIR_15TPD_ENGINEERING_DRAWINGS.pdf`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/engineering/cad/pdf/HARAKUTIR_15TPD_ENGINEERING_DRAWINGS.pdf)
- **Page Size:** Landscape A3 (420 mm x 297 mm).
- **Features:** Vector lines, title blocks, revision history boxes, discipline tags, equipment callouts, and prominent red warning borders (`PRELIMINARY—NOT FOR CONSTRUCTION`).
- **Automated Verification:** Verified by unit test `test_cad_deliverables_existence_and_not_empty` in `tests/test_end_to_end_plant_engineering.py`.
