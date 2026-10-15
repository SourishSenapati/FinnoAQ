# CAD Deliverables File-by-File Truth Table & Defect Ledger

> [!IMPORTANT]
> **Audit Status:** `COMPLETE — AUDITED 15 OCTOBER 2026`  
> **Classification:** `HISTORICAL CAD INVENTORY AUDIT`  
> **Overall Assessment:** All legacy 3D STEP files lack B-Rep solid geometry (stub headers only). 7 of 10 legacy DXF drawings contain only border templates. All legacy DXFs have model space scaled down to A1 paper coordinates with `$INSUNITS` unset.  
> **Governing Status:** All CAD deliverables remain stamped **`PRELIMINARY — NOT FOR CONSTRUCTION / NOT FOR PROCUREMENT`**.

---

## 1. Master CAD Truth Table

| Deliverable Path | Stated Title & Purpose | Byte Size | Actual Inspected Content & Entities | Unit & Scaling State | Defect Severity | Maturity Category | Required Corrective Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `engineering/cad/step/TK-101_Soak_Tank.step` | 3D Solid Model of Dual Conical Soak Vessel | 1,739 B | **27 ASCII lines.** Contains only ISO-10303-21 header, `DATA; ENDSEC;`. **0 B-Rep solids, 0 faces, 0 edges.** | Unspecified (Stub Header) | **CRITICAL (DEF-CAD-01)** | `CAD_NOT_GENERATED` (Placeholder) | Re-generate using verified SolidWorks 2025 COM automation (`SldWorks.Application`) with genuine 6mm shell, dished head, and B-Rep solids. |
| `engineering/cad/step/DR-101_Fluid_Bed_Dryer.step` | 3D Solid Model of Vibrating Fluid-Bed Dryer | 1,743 B | **27 ASCII lines.** Header only. **0 B-Rep solids, 0 bodies.** | Unspecified (Stub Header) | **CRITICAL (DEF-CAD-01)** | `CAD_NOT_GENERATED` (Placeholder) | Re-generate parametric solid model in SolidWorks once drying kinetics and deck dimensions are frozen. |
| `engineering/cad/step/SK-100_Dosing_Skid.step` | 3D Solid Model of Bicarbonate Dosing Skid | 1,725 B | **27 ASCII lines.** Header only. **0 B-Rep solids.** | Unspecified (Stub Header) | **CRITICAL (DEF-CAD-01)** | `CAD_NOT_GENERATED` (Placeholder) | Re-generate structural channel frame and pump assembly in SolidWorks. |
| `engineering/cad/step/AG-101_Agitator.step` | 3D Solid Model of Low-Shear Impeller & Drive | 1,755 B | **27 ASCII lines.** Header only. **0 B-Rep solids.** | Unspecified (Stub Header) | **CRITICAL (DEF-CAD-01)** | `CAD_NOT_GENERATED` (Placeholder) | Model stepped shaft and pitched-blade hydrofoil in SolidWorks. |
| `engineering/cad/obj/TK-101_Soak_Tank.obj` | 3D Polygonal Mesh for Visualization | 5,618 B | **164 lines** (66 vertices, 96 faces). Open, infinitely thin faceted cylinder with conical bottom. No thickness, nozzles, jacket, or legs. | Unitless mesh | **MODERATE (DEF-CAD-03)** | `CONCEPTUAL_MESH` | Replace with tessellated mesh exported from true SolidWorks solid. |
| `engineering/cad/dxf/DWG-FIN-15T-001.dxf` | Plant Master Plot Plan ($52\text{ m} \times 24\text{ m}$) | 11,420 B | **35 entities** (A1 border lines + 17 schematic room/zone boxes). | Model Space scaled to A1 mm ($841 \times 594\text{ mm}$). `$INSUNITS = \text{NOT_SET}` | **HIGH (DEF-CAD-05)** | `CONCEPTUAL_SCHEMATIC` | Re-generate using `accoreconsole.exe` at **1:1 true coordinate scale** ($52,000 \times 24,000\text{ mm}$) with `$INSUNITS = 4`. |
| `engineering/cad/dxf/DWG-FIN-15T-002.dxf` | Master Process P&ID | 8,924 B | **18 entities.** Outer border, inner border, title block grid lines only. **Zero process piping or instruments.** | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Draft vector P&ID with ISA-5.1 tags using AutoCAD Plant 3D / P&ID. |
| `engineering/cad/dxf/DWG-FIN-15T-003.dxf` | Process Flow Diagram (PFD) | 8,924 B | **18 entities.** Title block border lines only. Zero process symbols. | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Synchronize with PFD vector geometry from Sheet 1 of engineering PDF. |
| `engineering/cad/dxf/DWG-FIN-15T-004.dxf` | Rotary Drum Sieve & Pre-cleaner GA | 8,924 B | **18 entities.** Title block border lines only. Zero machine geometry. | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Draft equipment GA envelope in 1:1 mm model space. |
| `engineering/cad/dxf/DWG-FIN-15T-005.dxf` | Dual Soak Tank TK-101A/B General Arrangement | 13,850 B | **55 entities.** Basic 2D outline of cylinder, cone, centerlines, and 8 rough nozzle marks. | Scaled to A1 sheet mm. `$INSUNITS = \text{NOT_SET}` | **HIGH (DEF-CAD-04)** | `CONCEPTUAL_2D_SKETCH` | Re-project associative 2D drawing from SolidWorks 3D solid with true orthographic views and section cuts. |
| `engineering/cad/dxf/DWG-FIN-15T-006.dxf` | Dewatering Rotary Screen SC-101 GA | 8,924 B | **18 entities.** Title block border lines only. Zero machine geometry. | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Draft dewatering drum GA envelope with motor and chute. |
| `engineering/cad/dxf/DWG-FIN-15T-007.dxf` | Continuous Fluid-Bed Dryer DR-101 GA | 13,110 B | **49 entities.** Two rectangular zone outlines, air duct connections, and circles. | Scaled to A1 sheet mm. `$INSUNITS = \text{NOT_SET}` | **HIGH (DEF-CAD-04)** | `CONCEPTUAL_2D_SKETCH` | Re-draft at 1:1 true scale ($14,000 \times 1,000\text{ mm}$ deck) with plenum and blower interface. |
| `engineering/cad/dxf/DWG-FIN-15T-008.dxf` | Chemical Dosing Skid SK-100 GA | 8,924 B | **18 entities.** Title block border lines only. Zero skid geometry. | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Draft skid frame, dosing tanks, and metering pump layout. |
| `engineering/cad/dxf/DWG-FIN-15T-009.dxf` | Electrical Single Line Diagram (SLD) | 8,924 B | **18 entities.** Title block border lines only. Zero electrical busbars/breakers. | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Synchronize with SLD schematic from Sheet 5 of engineering PDF. |
| `engineering/cad/dxf/DWG-FIN-15T-010.dxf` | Form-Fill-Seal Packaging Line PKG-101 GA | 8,924 B | **18 entities.** Title block border lines only. Zero line geometry. | Border only. `$INSUNITS = \text{NOT_SET}` | **CRITICAL (DEF-CAD-02)** | `EMPTY_TEMPLATE` | Draft packaging line envelope, checkweigher, and conveyor footprint. |

---

## 2. Summary of CAD Defect Types & Severity

1. **DEF-CAD-01 (Empty 3D STEP Stubs):**
   All 4 `.step` files have only 27 ASCII lines and zero topological solids. They are completely unopenable as solids in any CAD software.
2. **DEF-CAD-02 (Empty Title Block DXFs):**
   7 of 10 `.dxf` files contain exactly 18 border entities and zero machine geometry.
3. **DEF-CAD-03 (Faceted Open Mesh):**
   `TK-101_Soak_Tank.obj` is a zero-thickness polygonal mesh, not a solid body.
4. **DEF-CAD-04 (Coarse 2D Elevation Only):**
   `DWG-005` and `DWG-007` have exterior outlines only, lacking cross-sections, wall thicknesses, tolerances, and weld details.
5. **DEF-CAD-05 (Drawing Scaling & Unit Violation):**
   Model space in all legacy DXFs was scaled down to A1 paper sheet size ($841 \times 594\text{ mm}$) instead of 1:1 true scale, and `$INSUNITS` was left unset.

---

## 3. Validated Corrective Toolchain Path

Following the successful execution of **Phase 0A Disposable Smoke Tests**:
- **3D Solid Models:** Will be generated via **SOLIDWORKS 2025 SP01.2** automation (`SldWorks.Application`), producing valid STEP AP214 B-Rep solids and native `.SLDPRT` files.
- **2D Conceptual CAD:** Will be generated via **AutoCAD 2025 `accoreconsole.exe`** with **Model Space strictly at 1:1 true millimeter scale** and `$INSUNITS = 4`.
- **Drawing Presentation:** Title blocks, borders, and drawing scales will be managed in Paper Space / Layout viewports without altering the true 1:1 physical dimensions in model space.
