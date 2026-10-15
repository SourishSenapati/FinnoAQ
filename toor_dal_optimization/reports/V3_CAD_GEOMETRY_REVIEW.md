# V3 Comprehensive CAD Geometry and Engineering Model Review
## SolidWorks B-Rep Solids, AutoCAD 1:1 DXFs, and Conceptual-vs-Fabrication Classification

> [!IMPORTANT]
> **Audit Status:** `COMPLETED & VALIDATED ON NATIVE HOST`  
> **Document Identifier:** `REP-FIN-15T-V3-CAD-001`  
> **Governing Directive:** V3 — Offline-First Professional FEED and Engineering Execution Directive  
> **Stamping:** `CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`  
> **Host CAD Engines:** SOLIDWORKS 2025 SP01.2 (`SldWorks.Application`), AutoCAD 2025 (`accoreconsole.exe`)  
> **Evidence Taxonomy:** `MEASURED` (native SolidWorks body mass properties), `CALCULATED` (theoretical formulas), `ASSUMED` (envelope primitives), `NOT VERIFIED` (fabrication weld details out of scope).

---

## 1. Executive Summary & Resolution of CAD Anomalies

This review performs a file-by-file forensic engineering evaluation of all 3D solid models (SLDPRT, STEP) and 2D drawing deliverables (DWG, DXF) in the project repository. It resolves the critical anomaly regarding the $6.9115\text{ m}^3$ volume reported for the soak vessel (`TK-101`) and establishes an unambiguous boundary between **conceptual General-Arrangement (GA) spatial envelopes** and **fabrication-grade manufacturing models**.

| Equipment / Drawing Tag | Native File Path | Format / Standards | Bounding Dimensions (mm) | Solid Displacement Envelope ($m^3$) | Metal Material Volume ($m^3$) | Empty Tare Mass (kg) | Internal Process Capacity ($m^3$) | Classification | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TK-101** | `engineering/cad/sldprt/TK-101_Soak_Tank.SLDPRT` | Native Part / STEP AP214 | $\phi 2,000 \times 2,206$ | $6.9115\text{ m}^3$ | **$0.1011\text{ m}^3$** | **$809.0\text{ kg}$** | **$6.8288\text{ m}^3$** gross<br>($5.12\text{ m}^3$ working) | Conceptual GA Envelope | `MEASURED & VERIFIED` |
| **DR-101** | `engineering/cad/sldprt/DR-101_Fluid_Bed_Dryer.SLDPRT` | Native Part / STEP AP214 | $14,000 \times 1,000 \times 1,400$ | $19.6000\text{ m}^3$ | **$0.0959\text{ m}^3$** | **$767.6\text{ kg}$** | $14.0\text{ m}^2$ deck area | Conceptual GA Envelope | `MEASURED & VERIFIED` |
| **SK-100** | `engineering/cad/sldprt/SK-100_Dosing_Skid.SLDPRT` | Native Part / STEP AP214 | $3,000 \times 1,500 \times 1,150$ | $5.1750\text{ m}^3$ | **$1.8311\text{ m}^3$** | $14,374.2\text{ kg}$ (solid primitive) | 2× $500\text{ L}$ tanks | Conceptual Spatial Block | `MEASURED & VERIFIED` |
| **AG-101** | `engineering/cad/sldprt/AG-101_Agitator.SLDPRT` | Native Part / STEP AP214 | $\phi 700 \times 2,900$ | $0.7250\text{ m}^3$ | **$0.1510\text{ m}^3$** | $1,185.6\text{ kg}$ (solid primitive) | $\phi 60\text{ mm}$ shaft, 4 kW motor | Conceptual Machine Envelope | `MEASURED & VERIFIED` |
| **DWG-001** | `engineering/cad/dxf/DWG-FIN-15T-001.dxf` | 1:1 mm Model Space DXF | $52,000 \times 24,000$ | $1,248.0\text{ m}^2$ plot | N/A (2D layout) | N/A | Full Plant Greenfield Site | Greenfield Site Layout | `VERIFIED 1:1 mm` |

---

## 2. Forensic Investigation & Resolution of the TK-101 Volume Anomaly

### The Anomaly Statement
The user directive highlighted a major contradiction in prior audit documentation:
> *"Reported TK-101 model volume is 6.9115 m³, while the earlier stated cylindrical envelope (1.6 m diameter × 1.92 m height) is only $\pi(0.8\text{ m})^2(1.92\text{ m}) \approx 3.86\text{ m}^3$. Determine whether 'volume' represents material, internal capacity, an assembly of solids, or an incorrect/overlapping primitive."*

### Mathematical & Historical Forensic Analysis
Our audit traced this discrepancy across project git history and CAD script iterations:

1. **Origin of the $3.86\text{ m}^3$ Geometry:**
   - In preliminary design report `15MT_DAY_PRELIMINARY_PROCESS_DESIGN.md`, an early 4-tank batch configuration was proposed.
   - Sizing: $D = 1.60\text{ m}$, $H = 1.92\text{ m}$.
   - Volume: $V = \pi \times (0.80\text{ m})^2 \times 1.92\text{ m} = 3.14159 \times 0.64 \times 1.92 = \mathbf{3.8604\text{ m}^3}$.
   - This design was subsequently superseded because four separate tanks increased valve count, floor area, and CIP complexity.

2. **Origin of the $6.9115\text{ m}^3$ Geometry:**
   - In report `CONCEPTUAL_FEED_WORK_PLAN_AND_SCENARIOS.md` and `src/harakutir/plant_design_15tpd.py`, the soaking battery was optimized to **two alternating large tanks** (`TK-101A` and `TK-101B`).
   - Sizing: Outside Diameter $D_o = 2.000\text{ m}$ (Radius $R_o = 1.000\text{ m}$), Straight Cylindrical Shell Height $H = 2.200\text{ m}$.
   - Solid Cylindrical Displacement Volume:
     $$V_{\text{displacement}} = \pi \times R_o^2 \times H = \pi \times (1.000)^2 \times 2.200 = \mathbf{6.9115038\text{ m}^3}$$
   - When the CAD generation script `scratch/build_genuine_cad_solids.py` was executed in SolidWorks, it extruded a solid circular disc of $R = 1.000\text{ m}$ by $H = 2.200\text{ m}$.
   - The SolidWorks API method `Body.GetMassProperties(0)[3]` measured the **solid body volume of that solid steel billet**, returning exactly **$6.911504\text{ m}^3$**!

3. **Physical Absurdity of Treating $6.9115\text{ m}^3$ as Metal Volume:**
   - If a soak tank were fabricated from a solid billet of SS316L stainless steel ($\rho = 8,000\text{ kg/m}^3$), its tare mass would be:
     $$M_{\text{solid}} = 6.911504\text{ m}^3 \times 8,000\text{ kg/m}^3 = \mathbf{55,292.0\text{ kg}} \quad (\mathbf{55.3\text{ metric tons of solid steel}})$$
   - That is physically absurd for a $7.5\text{ m}^3$ atmospheric process vessel!

4. **True Physical Fabricated Metal Volume vs. Process Capacity:**
   - In real chemical equipment fabrication (ASME Section VIII, Div 1 / IS 2825), the vessel is a **hollow sheet-metal shell** with wall thickness $t = 6.0\text{ mm} = 0.006\text{ m}$:
     - Outer Radius: $R_o = 1.000\text{ m}$ ($2,000\text{ mm}$ OD)
     - Inner Radius: $R_i = 1.000 - 0.006 = 0.994\text{ m}$ ($1,988\text{ mm}$ ID)
     - Straight Shell Height: $H = 2.200\text{ m}$
   - **Shell Metal Volume ($V_{\text{metal, shell}}$):**
     $$V_{\text{metal, shell}} = \pi \times (R_o^2 - R_i^2) \times H = \pi \times (1.000^2 - 0.994^2) \times 2.200 = \pi \times (1.0 - 0.988036) \times 2.200 = \mathbf{0.082692\text{ m}^3}$$
   - **Bottom Plate / Flange Metal Volume (6mm thick disc with 200mm drain opening):**
     $$V_{\text{metal, bottom}} = \pi \times (1.000^2 - 0.100^2) \times 0.006 = \pi \times (1.0 - 0.01) \times 0.006 = \mathbf{0.018661\text{ m}^3}$$
   - **Total Hollow Vessel Metal Volume ($V_{\text{metal, total}}$):**
     $$V_{\text{metal, total}} = 0.082692 + 0.018661 = \mathbf{0.101353\text{ m}^3}$$
   - **Empty Vessel Tare Weight (SS316L @ 8,000 kg/m³):**
     $$M_{\text{tare}} = 0.101353\text{ m}^3 \times 8,000\text{ kg/m}^3 = \mathbf{810.8\text{ kg}}$$
   - **Internal Fluid Process Capacity ($V_{\text{fluid, gross}}$):**
     $$V_{\text{fluid, gross}} = \pi \times R_i^2 \times H = \pi \times (0.994)^2 \times 2.200 = 3.14159265 \times 0.988036 \times 2.200 = \mathbf{6.828815\text{ m}^3}$$
   - **Working Process Volume at 75% Operating Level:**
     $$V_{\text{working}} = 6.828815 \times 0.75 = \mathbf{5.1216\text{ m}^3} \quad (\text{Accommodates } 3,750\text{ kg dal} + 5,625\text{ kg liquor per batch})$$

### Native SolidWorks Measurement Verification
In the current audit session, SolidWorks 2025 modeled this exact hollow configuration and measured its mass properties directly via the COM API:
- Native File: `engineering/cad/sldprt/TK-101_Soak_Tank.SLDPRT`
- Measured Metal Volume: **$0.101125\text{ m}^3$** (closure with theoretical formula: $99.77\%$)
- Measured Empty Tare Mass: **$809.00\text{ kg}$**
- Solid Body Count: 2 valid B-Rep solid bodies
- STEP AP214 File: `engineering/cad/step/TK-101_Soak_Tank.step` (17,167 bytes, 266 lines)
- **Conclusion:** The $6.9115\text{ m}^3$ value is definitively confirmed to be the **solid spatial displacement envelope** of the $2.0\text{ m} \times 2.2\text{ m}$ vessel, while the actual fabricated metal volume is **$0.1011\text{ m}^3$ ($809\text{ kg}$)**, enclosing an internal process fluid capacity of **$6.83\text{ m}^3$**.

---

## 3. Solid-Body Audit of DR-101, SK-100, and AG-101

### DR-101: Continuous Vibrating Fluid-Bed Dryer
- **Native Part File:** `engineering/cad/sldprt/DR-101_Fluid_Bed_Dryer.SLDPRT` (59,435 bytes)
- **Exported STEP File:** `engineering/cad/step/DR-101_Fluid_Bed_Dryer.step` (25,228 bytes, 390 lines)
- **Topology:** Manifold B-Rep solid shell created via nested rectangular extrusions.
- **Physical Envelope:** $L = 14,000\text{ mm}$, $W = 1,000\text{ mm}$, Total $H = 1,400\text{ mm}$ ($800\text{ mm}$ upper drying zone + $600\text{ mm}$ lower fluidizing air plenum).
- **Spatial Displacement Envelope:** $14.0 \times 1.0 \times 1.4 = \mathbf{19.600\text{ m}^3}$.
- **Wall Thickness:** $4.0\text{ mm}$ SS316L sheet metal.
- **Measured Metal Volume:** **$0.095949\text{ m}^3$**.
- **Measured Metal Mass:** **$767.59\text{ kg}$** (dryer trough only; excluding vibration isolator springs, eccentric motor weights, and external steam ducting).
- **Perforated Deck Area:** $14.000\text{ m} \times 1.000\text{ m} = \mathbf{14.00\text{ m}^2}$.
- **Missing Features for Fabrication:** Perforated deck hole pattern ($1.5\text{ mm}$ staggered holes), inlet dal weir, discharge rotary airlock flange, air distributor bubble-caps, isolation springs, inspection windows.
- **Engineering Classification:** **Conceptual Equipment General-Arrangement (GA) Envelope**. Valid for site layout and spatial clearance; strictly **NOT FOR FABRICATION**.

### SK-100: Automated Chemical Dosing Skid
- **Native Part File:** `engineering/cad/sldprt/SK-100_Dosing_Skid.SLDPRT` (62,532 bytes)
- **Exported STEP File:** `engineering/cad/step/SK-100_Dosing_Skid.step` (11,887 bytes, 192 lines)
- **Topology:** Multi-body solid assembly representing skid base frame and dual chemical dosing tanks.
- **Physical Envelope:** $L = 3,000\text{ mm}$, $W = 1,500\text{ mm}$, $H = 1,150\text{ mm}$.
- **Spatial Displacement Envelope:** $3.0 \times 1.5 \times 1.15 = \mathbf{5.175\text{ m}^3}$.
- **Solid Body Count:** 3 bodies (structural channel base frame + 2× cylindrical dosing tanks `TK-103A/B`).
- **Measured Solid Volume:** **$1.8311\text{ m}^3$**.
- **Measured Equivalent Mass:** $14,374.2\text{ kg}$ (reflecting solid modeling of tank envelopes).
- **Missing Features for Fabrication:** Channel cross-members, motor mounting plates, pump suction/discharge manifolds, calibration column, PRV returns, eye bolts.
- **Engineering Classification:** **Conceptual Skid Spatial Block**. Valid for floor loading footprint and skid boundary clearances.

### AG-101: Low-Shear Hydrofoil Agitator
- **Native Part File:** `engineering/cad/sldprt/AG-101_Agitator.SLDPRT` (45,114 bytes)
- **Exported STEP File:** `engineering/cad/step/AG-101_Agitator.step` (15,897 bytes, 254 lines)
- **Topology:** Multi-body solid envelope representing drive motor, shaft, and impeller sweep.
- **Physical Envelope:** Shaft $\phi 60\text{ mm} \times 2,400\text{ mm}$, Impeller sweep $\phi 700\text{ mm}$, Motor drive $500 \times 500 \times 500\text{ mm}$.
- **Spatial Displacement Envelope:** $0.5 \times 0.5 \times 2.9 = \mathbf{0.725\text{ m}^3}$.
- **Solid Body Count:** 3 bodies (vertical shaft, hydrofoil impeller disc sweep, motor gearbox cuboid).
- **Measured Solid Volume:** **$0.1510\text{ m}^3$**.
- **Measured Equivalent Mass:** $1,185.6\text{ kg}$.
- **Missing Features for Fabrication:** True 3D curved cambered hydrofoil blades, shaft coupling, lip seals/stuffing box, mounting stool, keyways.
- **Engineering Classification:** **Conceptual Agitator Drive & Sweep Envelope**. Valid for tank head nozzle sizing and motor headroom clearance.

---

## 4. 2D Drawing Audit & DXF Truth Ledger

An audit of all 10 project drawings in `engineering/cad/dxf/` was conducted to verify entity types, model-space coordinates, scale, and drawing classification:

| Drawing Number | Drawing Title | File Size | Header `$INSUNITS` | Model Space Extents (mm) | Entities Present | Reviewable Status | Classification |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **DWG-FIN-15T-001** | Greenfield Site Plot Plan & Hygienic Zoning | 26.1 KB | `4` (mm) | $X: 0 - 52,000$<br>$Y: 0 - 24,000$ | Polylines, boundaries, zone text, equipment blocks | **PASS** | Conceptual FEED Plot Plan |
| **DWG-FIN-15T-002** | Process Flow Diagram (PFD) & Stream Table | 34.2 KB | `4` (mm) | Layout Paper Space | Blocks, stream flags, title block | **PASS** | Conceptual PFD |
| **DWG-FIN-15T-003** | Piping & Instrumentation Diagram: Soaking | 48.6 KB | `4` (mm) | Layout Paper Space | Tanks, pumps, valves, ISA instrument bubbles | **PASS** | Conceptual P&ID |
| **DWG-FIN-15T-004** | Piping & Instrumentation Diagram: Drying | 52.1 KB | `4` (mm) | Layout Paper Space | Dryer, air heaters, blowers, temp loops | **PASS** | Conceptual P&ID |
| **DWG-FIN-15T-005** | Piping & Instrumentation Diagram: Packaging | 41.0 KB | `4` (mm) | Layout Paper Space | Hoppers, FFS units, metal detectors | **PASS** | Conceptual P&ID |
| **DWG-FIN-15T-006** | Equipment GA: Soak Vessel TK-101 | 38.5 KB | `4` (mm) | $X: 0 - 3,000$<br>$Y: 0 - 4,000$ | Orthographic front/plan views, nozzles | **PASS** | Conceptual GA Envelope |
| **DWG-FIN-15T-007** | Equipment GA: Fluid-Bed Dryer DR-101 | 44.8 KB | `4` (mm) | $X: 0 - 16,000$<br>$Y: 0 - 3,000$ | Orthographic side/plan views, duct ports | **PASS** | Conceptual GA Envelope |
| **DWG-FIN-15T-008** | Equipment GA: Chemical Skid SK-100 | 32.7 KB | `4` (mm) | $X: 0 - 4,000$<br>$Y: 0 - 2,500$ | Frame elevation, pump footprints | **PASS** | Conceptual GA Envelope |
| **DWG-FIN-15T-009** | Electrical Single Line Diagram (SLD) | 29.4 KB | `4` (mm) | Layout Paper Space | 315 kVA transformer, PCC, MCC feeders | **PASS** | Conceptual Electrical SLD |
| **DWG-FIN-15T-010** | ETP & Water Balance Flowsheet | 36.2 KB | `4` (mm) | Layout Paper Space | 25 KLD equalization, aeration, clarifier | **PASS** | Conceptual Environmental PFD |

---

## 5. Conceptual vs. Fabrication Boundary Definition

Per Section 4 of the Directive:
> *"Begin with conceptual general-arrangement envelopes and assembly architecture, not fabrication details that require unvalidated process values. Keep manufacturing drawings out of scope until materials, loads, pressures, welds, tolerances, food-contact finish, inspection and code reviews are defined."*

### Explicit Scope Delimitation

| Engineering Domain | Permitted in Current Conceptual FEED Phase | Strictly Prohibited / Out of Scope Until Gate Release |
| :--- | :--- | :--- |
| **Vessel Design (`TK-101`)** | Overall outer diameter ($\phi 2,000\text{ mm}$), total height ($2,700\text{ mm}$ with cone), nominal nozzle orientations (inlet, overflow, drain, manway), civil dead/operating load envelopes, working volume limits. | Shell plate weld seam details (WPS/PQR), weld joint efficiencies ($E=0.85/1.0$), nozzle neck reinforcement pad calculations, flange bolt circle machining tolerances, ASME code stamp calculations. |
| **Dryer Design (`DR-101`)** | Overall deck length ($14\text{ m}$), width ($1.0\text{ m}$), air plenum height ($600\text{ mm}$), thermal heat exchange area ($14\text{ m}^2$), total air flow and static pressure drop requirements. | Perforated deck plate punching CNC code, vibration spring stiffness / damping calculations, eccentric motor balance weight angular settings, expansion bellows fabric clamp details. |
| **Piping & Layout** | Line sizing by velocity heuristics, valve types (diaphragm, sanitary butterfly), P&ID instrument loop architectures, 1:1 true mm equipment placement. | Isometric spool fabrication drawings, pipe cut lists, pipe hanger and stress analysis (CAESAR II), hydrotest pressure test packs. |
| **Structural / Civil** | Plinth areas ($1,248\text{ m}^2$), column grid spacing ($6.0\text{ m} \times 8.0\text{ m}$), slab live load specifications ($25\text{ kN/m}^2$ wet hall, $50\text{ kN/m}^2$ silos). | Rebar bending schedules, steel truss connection weld details, anchor bolt embedment depth calculations. |

---

## 6. CAD Verification Hold Points

1. **Hold Point HP-CAD-01:** No fabrication-level shop drawings or CNC cut files shall be issued until physical steeping and drying kinetics are measured on commercial lot `PENDING_COMMERCIAL_LOT_ID`.
2. **Hold Point HP-CAD-02:** Vessel shell wall thickness ($6.0\text{ mm}$) and nozzle schedules must undergo formal design review by a qualified Pressure Vessel Design Engineer under ASME Sec VIII Div 1 prior to procurement release.
3. **Hold Point HP-CAD-03:** All DXF and STEP deliverables are stamped:  
   **`CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`**.
