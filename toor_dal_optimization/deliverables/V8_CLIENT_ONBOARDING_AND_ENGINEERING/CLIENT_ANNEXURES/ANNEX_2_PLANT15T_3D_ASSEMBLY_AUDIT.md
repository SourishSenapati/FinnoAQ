# ANNEX 2: GREENFIELD 15 TPD PROCESSING FACILITY — 3D PHYSICAL ASSEMBLY AUDIT
**Document Ref:** FNQ-ANX-15T-002 (Rev 8.0)  
**Classification:** CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Academic Guidance:** Dr. Archisman Ray (IIT Kharagpur)  
**Authoring Application:** SolidWorks 2025 SP01.2 Native Parametric Assembly (`PLANT-15T_General_Arrangement.SLDASM`)  

---

## 1. 3D Assembly Overview & Engineering Parameters
The 15,000 kg/day industrial pulse processing concept is modeled as a fully mated, collision-free 3D parametric boundary-representation solid assembly comprising 12 integrated process and structural packages:

| Parameter | Value | Verification Source |
| :--- | :--- | :--- |
| **Total Assembly Mass** | 27,078.89 kg (27.08 tonnes) | SolidWorks B-Rep Mass Properties Integration |
| **Total Displaced Volume** | 27.0789 m³ | SolidWorks B-Rep Volume Solver |
| **Total Wetted & Shell Surface Area** | 370.39 m² | SolidWorks Mesh & Face Topology Audit |
| **Center of Gravity (X, Y, Z)** | (-0.867m, 2.145m, -3.137m) | Relative to Plant Datum 0,0,0 (Building Infeed Corner) |
| **STEP Interchange AP214 File** | `PLANT-15T_General_Arrangement.step` | 1,614,333 bytes, 22,079 lines, valid solids |

---

## 2. Integrated Unit Operations & Subsystem Coordinates

1. **STR-100 Mezzanine Platform (12,450 kg):** Structural steel support deck (10.7m x 7.5m, elevation +4.2m) with dual circular vessel penetrations and OSHA-compliant safety railings.
2. **TK-101A/B Rapid Hydration Vessels (1,850 kg each):** Twin sanitary vertical cylindrical vessels with ASME Section VIII ellipsoidal top heads, 60° conical bottoms, 4 support lugs, and 6 process nozzles.
3. **AG-101A/B Agitator Assemblies (320 kg each):** Top-entry low-shear hydrofoil impellers driven by 4.0 kW geared motors at 35 RPM.
4. **CHU-100 Transition Chutes (640 kg):** Dual-branch converging chutes connecting vessel bottom dump valves to the dewatering screen.
5. **SC-101 Vibratory Dewatering Screen (850 kg):** High-frequency linear screen removing 92% of surface liquor.
6. **DR-101 Continuous Fluid Bed Dryer (4,200 kg):** 6.0m active vibrating fluidization deck with inlet plenum, perforated distributor plate, dual NFPA 68 explosion burst panels, and exhaust hood.
7. **CY-101 Exhaust Cyclone Separator (980 kg):** High-efficiency cyclone removing dal fines from the dryer exhaust air stream.
8. **SK-100 Chemical Dosing Skid (540 kg):** Solution preparation tank, twin positive-displacement metering pumps, and stainless steel containment bund.
9. **PIP-100 Interconnecting Piping (1,120 kg):** Coordinated 3D stainless steel piping connecting dosing, soaking, steam, and effluent lines.
10. **EV-101 ZLD Evaporator Skid (1,950 kg):** Compact falling-film multi-effect evaporator concentrating spent liquor and recycling clean distillate.

---

## 3. Engineering Disclaimer
> **IMPORTANT NOTICE:** This 3D assembly represents a preliminary conceptual Front-End Engineering Design (FEED) baseline. It does not constitute final fabrication, civil structural, or piping construction drawings. Final equipment sizing remains conditional upon physical soaking kinetics and moisture equilibria determined in Phase 1 and Phase 2A testing.
