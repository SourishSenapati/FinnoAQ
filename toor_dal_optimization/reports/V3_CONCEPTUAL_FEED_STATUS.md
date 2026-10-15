# V3 Conceptual Front-End Engineering Design (FEED) Status Report
## 15,000 kg/day Incoming-Feed Toor-Dal Optimization Greenfield Plant

> [!IMPORTANT]
> **Project Engineering Phase:** `CONCEPTUAL FEED (STAGE 3)`  
> **Document Identifier:** `REP-FIN-15T-V3-FDS-001`  
> **Governing Directive:** V3 — Offline-First Professional FEED and Engineering Execution Directive  
> **Mandatory Stamping:** `CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`  
> **Experimental Gate Status:** `GATE G-A HOLD ACTIVE` (Zero physical trials authorized without client sign-off)  
> **Commercial Raw Material Lot:** `PENDING_COMMERCIAL_LOT_ID` (supplier chain-of-custody documentation pending)

---

## 1. Executive Summary & Design Governance

This Conceptual Front-End Engineering Design (FEED) establishes the technical, mechanical, spatial, and economic architecture for a greenfield 15,000 kg/day processing facility targeting imported Tanzanian split/dehulled pigeon peas (*Cajanus cajan*). 

The engineering design is developed under a **rigorous parallel decoupling philosophy**:
1. **Process Chemical Status = `HYPOTHESIS`:** The accelerated tenderness treatment (ambient steeping in dilute food-grade sodium bicarbonate) remains a scientific hypothesis until confirmed by empirical measurements on physical samples from `PENDING_COMMERCIAL_LOT_ID`.
2. **Plant Sizing = `SENSITIVITY ENVELOPES`:** Because moisture uptake, steeping duration, and solids recovery cannot be frozen without target-lot data, all major equipment, utility duties, and civil footprints are sized across **Low, Base, and High sensitivity envelopes**.
3. **Engineering Deliverables = `CONCEPTUAL GA & ARCHITECTURE`:** Native 3D B-Rep CAD models (SolidWorks 2025), 1:1 true-millimeter drawings (AutoCAD 2025), and converged utility simulations (Aspen Plus V14) represent preliminary general-arrangement envelopes. Fabrication details, weld schedules, and procurement packages remain strictly locked at **Gate Hold Point HP-PROC-01**.

---

## 2. Conceptual FEED Drawing and Model Register

All drawings and native engineering models have been produced, verified, and cataloged in the repository:

| Drawing / Model ID | Sheet Title | Type | Native Format & Tools | Model Scale / Extents | Engineering Status |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **DWG-FIN-15T-001** | Greenfield Site Plot Plan & Logistics / Hygienic Zoning | 2D Layout | AutoCAD 2025 (`.dxf` / `.dwg`) | 1:1 mm ($52.0\text{ m} \times 24.0\text{ m}$) | `COMPLETED (FEED)` |
| **DWG-FIN-15T-002** | Process Flow Diagram (PFD) & 12-Stream Balance Table | 2D PFD | AutoCAD 2025 (`.dxf`) | Formatted Layout | `COMPLETED (FEED)` |
| **DWG-FIN-15T-003** | Piping & Instrumentation Diagram: Soaking & Dewatering | 2D P&ID | AutoCAD 2025 (`.dxf`) | ISA-5.1 Symbols | `COMPLETED (FEED)` |
| **DWG-FIN-15T-004** | Piping & Instrumentation Diagram: Fluid-Bed Drying & Air | 2D P&ID | AutoCAD 2025 (`.dxf`) | ISA-5.1 Symbols | `COMPLETED (FEED)` |
| **DWG-FIN-15T-005** | Piping & Instrumentation Diagram: Cleanroom Packaging | 2D P&ID | AutoCAD 2025 (`.dxf`) | ISA-5.1 Symbols | `COMPLETED (FEED)` |
| **DWG-FIN-15T-006** | Equipment GA: $7.5\text{ m}^3$ Soak Vessel (`TK-101`) | 2D GA | AutoCAD 2025 (`.dxf`) | 1:1 mm ($2.0\text{ m} \times 2.7\text{ m}$) | `COMPLETED (FEED)` |
| **DWG-FIN-15T-007** | Equipment GA: Continuous Vibrating Fluid Bed Dryer (`DR-101`) | 2D GA | AutoCAD 2025 (`.dxf`) | 1:1 mm ($14.0\text{ m} \times 1.0\text{ m}$) | `COMPLETED (FEED)` |
| **DWG-FIN-15T-008** | Equipment GA: Dual-Tank Automated Dosing Skid (`SK-100`) | 2D GA | AutoCAD 2025 (`.dxf`) | 1:1 mm ($3.0\text{ m} \times 1.5\text{ m}$) | `COMPLETED (FEED)` |
| **DWG-FIN-15T-009** | Electrical Single Line Diagram (SLD) & Motor Control Center | 2D Electrical | AutoCAD 2025 (`.dxf`) | Formatted Layout | `COMPLETED (FEED)` |
| **DWG-FIN-15T-010** | Utility, Wastewater & 25 KLD ETP Flowsheet | 2D Utility | AutoCAD 2025 (`.dxf`) | Formatted Layout | `COMPLETED (FEED)` |
| **CAD-FIN-15T-001** | Soak Vessel Hollow Shell 3D Solid Model (`TK-101`) | 3D B-Rep | SOLIDWORKS 2025 (`.SLDPRT` / `.step`) | $\phi 2,000 \times 2,206\text{ mm}$ (6mm wall) | `COMPLETED (FEED)` |
| **CAD-FIN-15T-002** | Fluid Bed Dryer Trough & Plenum 3D Solid Model (`DR-101`) | 3D B-Rep | SOLIDWORKS 2025 (`.SLDPRT` / `.step`) | $14,000 \times 1,000 \times 1,400\text{ mm}$ | `COMPLETED (FEED)` |
| **CAD-FIN-15T-003** | Automated Dosing Skid 3D Multi-Body Assembly (`SK-100`) | 3D B-Rep | SOLIDWORKS 2025 (`.SLDPRT` / `.step`) | $3,000 \times 1,500 \times 1,150\text{ mm}$ | `COMPLETED (FEED)` |
| **CAD-FIN-15T-004** | Low-Shear Agitator & Drive Envelope 3D Solid (`AG-101`) | 3D B-Rep | SOLIDWORKS 2025 (`.SLDPRT` / `.step`) | $\phi 700 \times 2,900\text{ mm}$ sweep | `COMPLETED (FEED)` |
| **SIM-FIN-15T-001** | Aspen Plus V14 Native Water Evaporation Simulation | Process Rigor | Aspen Plus V14 (`.bkp`) | Converged 6 blocks / 10 streams | `CONVERGED (FEED)` |

---

## 3. Equipment Sizing & Sensitivity Envelopes

Because physical steeping kinetics and moisture uptake will be determined during the wet-lab trial, major equipment design parameters are bound across three operational envelopes:

```
                  +-------------------------------------------------------------+
                  |           PROCESS SENSITIVITY DESIGN ENVELOPES              |
                  +-------------------------------------------------------------+
                  | Low Scenario:   wb_wet = 25.50%  (Δwb = +15.0% points)       |
                  | Base Scenario:  wb_wet = 28.77%  (Δwb = +18.27% points)      |
                  | High Scenario:  wb_wet = 33.50%  (Δwb = +23.0% points)       |
                  +-------------------------------------------------------------+
```

| Equipment Tag & Unit Name | Design Parameter | Low Scenario (25.5% wb) | Base Design (28.77% wb) | High Scenario (33.5% wb) | Sizing Basis & Governance Rule |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **TK-101A/B**<br>Soak Vessels | Tank Working Volume<br>Cycle Batch Time<br>Operating Schedule | $4.85\text{ m}^3$<br>$3.5\text{ h}$ soak / $4.0\text{ h}$ turn<br>4 batches/day/tank | **$5.12\text{ m}^3$**<br>**$3.5\text{ h}$ soak / $4.0\text{ h}$ turn**<br>**4 batches/day/tank** | $5.65\text{ m}^3$<br>$4.5\text{ h}$ soak / $5.0\text{ h}$ turn<br>3.2 batches/day/tank | Vessel physical volume ($6.83\text{ m}^3$ gross / $7.5\text{ m}^3$ envelope) accommodates all three scenarios with $> 17\%$ freeboard. |
| **AG-101A/B**<br>Low-Shear Agitators | Impeller Type<br>Impeller Diameter<br>Motor Power | 3-blade axial hydrofoil<br>$\phi 650\text{ mm}$<br>$3.0\text{ kW}$ | **3-blade axial hydrofoil**<br>**$\phi 700\text{ mm}$**<br>**$4.0\text{ kW}$** | 3-blade axial hydrofoil<br>$\phi 750\text{ mm}$<br>$5.5\text{ kW}$ | Tip speed limited to $< 1.8\text{ m/s}$ to prevent dal cotyledon splitting and starch attrition. |
| **SC-101**<br>Vibrating Dewaterer | Screen Deck Area<br>Deck Inclination<br>Mesh Aperture | $2.00\text{ m}^2$<br>$5.0^\circ$ uphill<br>$1.0\text{ mm}$ wedge-wire | **$2.50\text{ m}^2$**<br>**$5.0^\circ$ uphill**<br>**$1.0\text{ mm}$ wedge-wire** | $3.00\text{ m}^2$<br>$6.0^\circ$ uphill<br>$1.0\text{ mm}$ wedge-wire | Sized for peak instantaneous batch discharge rate of $15.0\text{ m}^3/\text{h}$ slurry. |
| **DR-101**<br>Fluid Bed Dryer | Drying Deck Area<br>Design Evaporation<br>Air Flow Rate<br>Static Pressure | $10.5\text{ m}^2$<br>$225.1\text{ kg/h}$<br>$12,500\text{ m}^3/\text{h}$<br>$1,800\text{ Pa}$ | **$14.0\text{ m}^2$**<br>**$285.1\text{ kg/h}$**<br>**$16,100\text{ m}^3/\text{h}$**<br>**$2,200\text{ Pa}$** | $18.5\text{ m}^2$<br>$382.3\text{ kg/h}$<br>$21,000\text{ m}^3/\text{h}$<br>$2,600\text{ Pa}$ | Base length $14.0\text{ m} \times 1.0\text{ m}$ accommodates Base Design over 13.6 effective hours ($285.1\text{ kg/h}$). |
| **HE-101**<br>Steam Air Heater | Thermal Heat Duty<br>Steam Consumption | $395.0\text{ kW}$<br>$415\text{ kg/h}$ steam | **$512.4\text{ kW}$**<br>**$520\text{ kg/h}$ steam (avg)** | $685.2\text{ kW}$<br>$720\text{ kg/h}$ steam (avg) | Sized with 600 kg/h boiler capacity; high scenario requires boiler rating upgrade to 850 kg/h. |
| **SK-100**<br>Dosing Skid | Dosing Tank Size<br>Metering Pump Flow | 2× $400\text{ L}$ HDPE<br>$15.0\text{ L/h}$ diaphragm | **2× $500\text{ L}$ HDPE**<br>**$25.0\text{ L/h}$ diaphragm** | 2× $500\text{ L}$ HDPE<br>**$35.0\text{ L/h}$ diaphragm** | Sized for Basis A ($112.5\text{ kg/day}$ $NaHCO_3$) with variable-stroke stroke frequency adjustment. |
| **PK-101A/B**<br>FFS Packaging | Packaging Machine Type<br>Operating Speed<br>Cleanroom Class | 2× 10-head weighers<br>2× 25 pouches/min<br>Class 8 (100,000) | **2× 14-head weighers**<br>**2× 35 pouches/min**<br>**Class 8 (100,000)** | 2× 14-head weighers<br>2× 45 pouches/min<br>Class 8 (100,000) | Dual packaging lines provide $100\%$ redundancy for 1 kg retail and 5 kg food-service pouches. |

---

## 4. Site, Civil, and Mechanical Interface Status

### Plot Plan & Civil Foundations
- **Total Greenfield Footprint:** $52.000\text{ m} \times 24.000\text{ m} = \mathbf{1,248.00\text{ m}^2}$.
- **Pre-Engineered Building (PEB) Structure:** Clear span steel portal frames with $6.0\text{ m}$ bay spacing and $8.0\text{ m}$ clear eaves height.
- **Substructure Soil Bearing Requirement:** Minimum allowable soil bearing capacity $q_{\text{allow}} \ge 150\text{ kN/m}^2$. (Subject to geotechnical bore-log verification).
- **Floor Loading Specifications:**
  - Raw Storage Silo Bay: $50.0\text{ kN/m}^2$ reinforced raft slab.
  - Wet Processing & Dryer Hall: $25.0\text{ kN/m}^2$ with heavy anti-microbial epoxy screed ($4.0\text{ mm}$ thickness) sloped $1:50$ to stainless steel floor channels.
  - Packaging & Finished Goods Warehouse: $35.0\text{ kN/m}^2$ jointless laser-screed floor designed for 3-tier pallet racking and 2.5-ton reach trucks.

### Logistics & Hygienic Zoning Architecture
1. **Raw Receiving Zone (Brown Zone, Uncontrolled):** External truck unloading bay, silo intake, raw grain screening, dust aspiration. Negative pressure ventilation.
2. **Wet Processing & Thermal Zone (Medium Hygiene / Grey Zone):** Chemical preparation, steeping tanks, dewatering screens, fluid-bed drying. Washdown-capable walls, stainless drains.
3. **Primary Packaging Cleanroom (High Hygiene / White Zone - Class 8):** Positive pressure ($+15\text{ Pa}$), terminal HEPA filtration ($99.97\%$ @ $0.3\mu\text{m}$), 15 air changes/hour, 2-stage airlock entry with shoe-change barrier and automated hand-wash station.
4. **Finished Goods Warehouse & Dispatch (Blue Zone):** Palletized storage, shrink wrapping, dispatch dock with dock levelers.

---

## 5. Vendor Data Gaps & Technical Queries (Hold Register)

The following parameters cannot be finalized until specific vendor technical data are received during detailed engineering:

| Query ID | Equipment / Subsystem | Required Vendor Confirmation | Impact on Engineering Design | Current FEED Placeholder Assumption |
| :---: | :--- | :--- | :--- | :--- |
| **TQ-DR-01** | Fluid Bed Dryer (`DR-101`) | Manufacturer validated air velocity ($u_{\text{mf}}$ and $u_{\text{operating}}$) for Tanzanian split dal. | Determines fluidizing blower static pressure and motor kW. | Assumed $u_{\text{mf}} = 1.15\text{ m/s}$, $u_{\text{op}} = 1.45\text{ m/s}$ based on Ergun equation. |
| **TQ-DR-02** | Vibration Isolators | Dynamic spring constants ($k_x, k_y, k_z$) and transmissibility ratio ($< 5\%$). | Civil foundation mass ratio and resonance frequency check. | Foundation sized at $3.0\times$ total vibrating equipment mass ($12,000\text{ kg}$ inertia block). |
| **TQ-BL-01** | Steam Boiler (`BL-101`) | Turn-down ratio and steam dryness fraction ($x \ge 0.98$). | Steam accumulator requirement and heat exchanger surface area. | Sized for 600 kg/h IBR package boiler with internal cyclonic demister. |
| **TQ-PK-01** | Packaging Lines (`PK-101`) | Nitrogen flushing residual oxygen level ($< 1.0\% O_2$). | MAP shelf-life guarantee and nitrogen generator sizing. | Sized for PSA nitrogen generator ($12.0\text{ Nm}^3/\text{h}$ @ $99.5\%$ purity). |
| **TQ-ET-01** | Effluent Treatment (`ETP-101`) | SPCB consent-to-establish limits for BOD ($< 30\text{ mg/L}$), COD ($< 250\text{ mg/L}$), and TDS ($< 2,100\text{ mg/L}$). | Tertiary RO / MVR evaporator requirement if Zero Liquid Discharge (ZLD) is mandated. | Assumed standard surface discharge norms; ZLD requires ₹85L additional CAPEX. |

---

## 6. Professional Review Hold Points & Governance Rules

Per Directive Section "PROCESS AND EXPERIMENTAL GATES":
- **Hold Point HP-EXP-01 (Screening Authorization):** Execution of the 4-condition steeping and cooking trial is frozen until the human project sponsor provides signed experimental authorization.
- **Hold Point HP-LOT-01 (Commercial Traceability):** Experimental execution must only proceed upon physical delivery of commercial lot material verified by supplier paperwork under identifier `PENDING_COMMERCIAL_LOT_ID`.
- **Hold Point HP-PROC-01 (Procurement Release):** No purchase orders, vendor equipment fabrication, or site civil ground-breaking shall be initiated based solely on this Conceptual FEED document.
- **Hold Point HP-STAMP-01 (Engineering Stamping):** All generated drawings, models, and specifications must bear the watermark:  
  **`CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`**.
