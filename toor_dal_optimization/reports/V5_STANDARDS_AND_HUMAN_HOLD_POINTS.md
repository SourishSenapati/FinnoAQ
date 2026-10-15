# V5 STANDARDS AND HUMAN HOLD POINTS
**Document ID:** `RPT-FIN-15T-V5-SHP-001`  
**Governing Standard:** V5 Master Directive — Evidence-Locked Governance & Standards Alignment  
**Facility:** 15,000 kg/day Greenfield Imported Pigeon Pea (*Cajanus cajan*) Rapid-Cooking Plant  
**Completeness Benchmark Target:** ASD-STM-100 Internal Benchmark  
**Active Work Branch:** `v5-integrated-engineering`  
**Overall Hold Status:** **GATE G-A HOLD ACTIVE (HUMAN HOLD POINT)**  
**Date:** 2026-10-16  

---

## 1. Regulatory & Engineering Standards Applicability Matrix

The engineering baseline for the 15,000 kg/day split pigeon pea optimization facility has been designed to satisfy an integrated suite of national and international engineering codes, food safety regulations, and environmental directives.

| Engineering Domain | Governing Standard / Code | Title / Scope | Baseline Compliance Mechanism | Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| **Mechanical & Pressure** | **ASME Section VIII Div 1** | Rules for Construction of Pressure Vessels | Sizing of TK-101 dimple steam jacket ($3.0\text{ barg}$ @ $120^\circ\text{C}$) | Compliant in Design |
| **Piping & Valves** | **ASME B31.3** | Process Piping Code | SS316L/SS304 line design pressures and wall thickness schedule | Compliant in Line List |
| **Piping Flanges** | **ASME B16.5** | Pipe Flanges and Flanged Fittings | Class 150 RF sanitary flanges on all process equipment nozzles | Compliant in CAD |
| **Food Hygiene (Global)** | **EHEDG Guidelines** | Docs 8, 10, 13 (Hygienic Equipment Design) | Crevice-free welds, $Ra \le 0.8\ \mu\text{m}$, self-draining slopes | Compliant in Specs |
| **Food Safety (India)** | **FSSAI Schedule 4** | General Hygienic and Sanitary Practices | Plant layout zoning, pest barriers, potable water standards | Compliant in Plot Plan |
| **Food Safety (US/FDA)** | **US FDA 21 CFR 117** | Current Good Manufacturing Practice (cGMP) | Hazard analysis, sanitation, preventive controls for human food | Compliant in Specs |
| **Elastomers & Gaskets**| **FDA 21 CFR 177.2600**| Rubber Articles Intended for Repeated Use | Food-grade EPDM and PTFE gaskets on all tri-clamp joints | Specified in BOM |
| **Combustible Dust** | **NFPA 652 / NFPA 68** | Combustible Dust Fundamentals & Venting | Deflagration venting on DC-101, Zone 20/21 hazardous zoning | Compliant in DWG-012 |
| **Dust Explosions** | **ATEX 2014/34/EU** | Equipment for Explosive Atmospheres | Category 2D/3D explosion-proof motors and instruments | Specified in Index |
| **Electrical Safety** | **IEC 60204-1** | Safety of Machinery — Electrical Equipment | Emergency stop circuits, isolation disconnects, cable sizing | Compliant in DWG-011 |
| **Ingress Protection** | **IEC 60529** | Degrees of Protection Provided by Enclosures | IP66 for wet wash-down areas (Zone 2); IP65 for dry areas | Specified in Motor List|
| **Instrumentation** | **ISA-5.1** | Instrumentation Symbols and Identification | Standard tag bubbles, loop designations, P&ID symbol set | Compliant in P&IDs |
| **Civil & Concrete** | **IS 456 / IS 875** | Plain and Reinforced Concrete / Design Loads | Slab load capacity ($4.5\text{ t/m}^2$), wind and seismic loads | Compliant in Civil Basis |
| **Environmental (ZLD)** | **CPCB / SPCB ZLD** | Zero Liquid Discharge Guidelines | 100% recycling of evaporator distillate ($19.58\text{ m}^3\text{/d}$) | Reconciled in Aspen |
| **Technical Drawings** | **ISO 128 / ISO 7200** | Technical Drawings & Title Blocks | Standard projection, line weights, title blocks, revision tracking | Compliant in All DWGs |
| **CAD Digital Definition**| **ASME Y14.41 / STEP** | Digital Product Definition / ISO 10303 | Parametric 3D solid modeling and STEP AP214 exchange | 100% B-Rep Validated |

---

## 2. Gate G-A Hold Protocol & Scientific Integrity

### 2.1 The Gate G-A Hold Principle
The project operates under a strict anti-fabrication mandate. Computational multi-scale models, literature-derived Peleg sorption parameters, and finite-element fluid bed drying simulations provide robust thermodynamic envelopes, but **they do not constitute physical empirical verification of the commercial grain shipment**.

Therefore, the human project leadership has placed the process under **Gate G-A Hold**:
- **Commercial Lot Identification:** The target physical lot is officially registered as `PENDING_COMMERCIAL_LOT_ID`. Historical placeholder tags (e.g., `TZ-2026-IMP-001`) have been purged from the active baseline.
- **Recipe Freeze Prohibition:** No chemical pre-treatment concentration (e.g., $0.75\%\text{ NaHCO}_3$) or soaking temperature profile is released for commercial production guarantees until the arrival and laboratory qualification of the physical lot.
- **Engineering Envelope Freedom:** Equipment sizing, pump flow rates, motor powers, and heat exchanger duties have been engineered with $+20\%\text{ to }+50\%$ design margins to accommodate the full operational range ($0.50\%\text{ to }1.00\%\text{ w/w}$ dosing; $45^\circ\text{C}\text{ to }55^\circ\text{C}$ soaking; $60^\circ\text{C}\text{ to }70^\circ\text{C}$ drying).

### 2.2 Gate G-A Release Criteria (Physical Lab Verification Plan)
Gate G-A Hold shall be lifted only after completion of the following physical laboratory procedures on representative samples drawn from the incoming commercial shipment:
1. **Raw Material Characterization:**
   - Determination of moisture content via oven drying ($105^\circ\text{C}$ for 16 hours, ISO 712 / AOAC 925.10).
   - Thousand-grain weight ($1000\text{-GW}$), split-to-whole ratio, broken grain percentage, and initial grain hardness (texture analyzer compression test).
2. **Hydration Kinetics Assay:**
   - 3-point temperature soak kinetics ($45^\circ\text{C}, 50^\circ\text{C}, 55^\circ\text{C}$) in triplicate across 4 chemical concentrations ($0.0\%, 0.5\%, 0.75\%, 1.0\%\text{ NaHCO}_3$).
   - Extraction of empirical Peleg rate constants ($K_1, K_2$) for the actual lot.
3. **Cooking Tenderness Evaluation:**
   - Cooking time determination using an automated 25-pin Mattson Cooker until $80\%$ pin penetration, validated against sensory finger-press texture.
   - Confirmation of target cooking time reduction ($< 15\text{ minutes}$ in open vessel, $< 7\text{ minutes}$ in pressure cooker).
4. **Organoleptic & Quality Assessment:**
   - Turbidity of cooked dal liquor (leaching loss assessment).
   - Residual sodium concentration in cooked product (compliance with dietary sodium limits).
   - Colorimetry ($L^*, a^*, b^*$ values) to confirm zero yellow hue degradation or discoloration.

---

## 3. Greenfield Plant Human Hold Points (Gates G-B through G-E)

To maintain rigorous quality assurance throughout equipment procurement, detailed civil engineering, skid fabrication, and plant commissioning, the following mandatory Human Hold Points are established:

```
[GATE G-A: Physical Grain Lot Qualification] ◄── CURRENT ACTIVE HOLD
      │ (Requires: Physical sample delivery + Lab assay report + Recipe signoff)
      ▼
[GATE G-B: Equipment Procurement & Detailed Engineering Release]
      │ (Requires: Vendor fabrication drawings + ASME calc sheets + MTC 3.1)
      ▼
[GATE G-C: Civil Foundation & Mezzanine Structural Pouring]
      │ (Requires: Soil geotechnical bore report + Structural deflection signoff)
      ▼
[GATE G-D: Factory Acceptance Testing (FAT) & Site Delivery]
      │ (Requires: Hydrostatic test certs + Surface roughness Ra certs + ATEX certs)
      ▼
[GATE G-E: Site Acceptance Testing (SAT), Cold Water Run & FSSAI Licensing]
      │ (Requires: CIP sanitization swab test + Water batching + FSSAI audit)
      ▼
[COMMERCIAL OPERATION]
```

### 3.1 Gate G-B: Equipment Procurement & Detailed Engineering Release
- **Required Deliverables:** Vendor general arrangement drawings, detailed ASME Section VIII calculation sheets, finite element stress analysis for vibrating screen and dryer, and Material Test Certificates (EN 10204 Type 3.1) confirming SS316L metallurgy.
- **Signoff Authority:** Project Engineering Lead & Lead Mechanical Engineer.

### 3.2 Gate G-C: Civil Foundation & Mezzanine Structural Pouring
- **Required Deliverables:** Geotechnical soil investigation report confirming safe soil bearing capacity $\ge 180\text{ kN/m}^2$, certified structural reinforcement drawings, and vibration harmonic frequency calculations for the mezzanine slab.
- **Signoff Authority:** Lead Civil / Structural Engineer.

### 3.3 Gate G-D: Factory Acceptance Testing (FAT) & Site Delivery
- **Required Deliverables:** Hydrostatic pressure test reports ($1.5 \times$ design pressure on TK-101 jacket), surface profilometer certificates confirming $Ra \le 0.8\ \mu\text{m}$ on all product contact zones, ATEX / IECEx certificates for hazardous zone drives, and dye penetrant weld inspection records.
- **Signoff Authority:** Quality Assurance Superintendent & Client Project Representative.

### 3.4 Gate G-E: Site Acceptance Testing (SAT), Cold Run & FSSAI Operating License
- **Required Deliverables:** Clean-in-Place (CIP) ATP bioluminescence swab clearance, complete 24-hour continuous water run verifying thermal and pneumatic loops, formal FSSAI food business operating license, and SPCB Consent to Operate (CTO) for Zero Liquid Discharge.
- **Signoff Authority:** Plant General Manager & Regulatory Affairs Director.

---

## 4. Governance Signoff

This document establishes the binding regulatory standards and hold point protocol for the Harakutir 15 TPD greenfield engineering baseline. All modifications to the Master Data or release of hold points require formal engineering change notices (ECN) and multidisciplinary signoff.

**Approved under V5 Master Directive Governance.**  
*Hold Status: GATE G-A ACTIVE.*
