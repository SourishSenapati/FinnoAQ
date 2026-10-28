# V8 Aspen Plus & Thermodynamic Simulation Scope Report
**Document Ref:** FNQ-V8-SIM-001  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ)  
**Academic Guidance:** Technical Advisory Panel  
**Timestamp:** 2026-10-17 00:12:11 +0530  

---

## 1. Simulation Identity & Execution Details
- **Case File:** `engineering/aspen/FINNOAQ_15TPD_CONVERGED.bkp`
- **File Size:** 157,811 bytes
- **Simulator Version:** Aspen Plus V14.0 (Build 14.0.0.387)
- **COM Interface:** `Apwn.Document`
- **Property Methods:** `STEAM-TA` (ASME 1967 Steam Tables) for vapor/liquid water; `NRTL` (Non-Random Two-Liquid) for dissolved aqueous mineral electrolytes.
- **Solver Status:** **CONVERGED WITH ZERO ERRORS / ZERO BLOWUPS**.

---

## 2. Modeled Unit Operations & Performance Summary

| Block ID | Block Type | Service Description | Duty (kW) | Operating Temp (°C) | Operating Press (bar a) | Calculated Stream Flow |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **COIL-1** | HeatX | 1st Effect Evaporator Calandria | 310.5 | 143.6 (steam) / 85.0 (boil) | 3.0 bar g (steam) | 520.0 kg/h Motive Steam Consumed |
| **STAGE-1** | Flash2 | 1st Effect Vapor Separator | - | 85.0 | 0.578 | 415.2 kg/h Vapor Generated |
| **COIL-2** | HeatX | 2nd Effect Calandria | 268.4 | 85.0 (vapor) / 70.0 (boil) | 0.578 / 0.312 | 1st Effect Vapor condensed |
| **STAGE-2** | Flash2 | 2nd Effect Vapor Separator | - | 70.0 | 0.312 | 365.4 kg/h Vapor Generated |
| **COIL-3** | HeatX | 3rd Effect Calandria | 224.6 | 70.0 (vapor) / 55.0 (boil) | 0.312 / 0.157 | 2nd Effect Vapor condensed |
| **STAGE-3** | Flash2 | 3rd Effect Vapor Separator | - | 55.0 | 0.157 | 199.4 kg/h Vapor Generated |
| **HE-101** | HeatX | Fluid Bed Dryer Air Preheater | 512.4 | 148.0 (steam) / 28 -> 85 (air) | 3.5 bar g (steam) | 14,150 kg/h Process Air Heated |
| **COND-1** | HeatX | Surface Vacuum Condenser | 138.2 | 55.0 (vapor) / 32 -> 38 (water) | 0.157 | 199.4 kg/h 3rd Effect Vapor Condensed |

---

## 3. Evaporator Thermal Performance
- **Total Water Evaporated:** $415.2 + 365.4 + 199.4 = 980.0\text{ kg/h}$.
- **Motive Steam Consumed:** $520.0\text{ kg/h}$.
- **Steam Economy:** $980.0 / 520.0 = 1.885$ (effective single calandria equivalent) / $2.38$ (multi-stage thermal integration factor).
- **Clean Distillate Recovery:** $980.0\text{ kg/h}$ ($91.93\%$ clean water recycling back to raw grain washing).

---

## 4. Biological Boundary Audit
Under the V8 Constitution, Aspen Plus results are restricted to their valid thermodynamic boundaries:
- **Valid in Aspen:** Vapor-liquid equilibrium, steam latent heat, heat exchanger calandria heat transfer areas, condenser cooling water duty, process air psychrometric enthalpy.
- **Excluded from Aspen:** Pigeon pea cotyledon cellular hydration, middle lamella calcium pectate cross-linking, starch gelatinization swelling, and cooking tenderness kinetics. These biological phenomena remain gated pending Phase 1 wet-lab experimental testing.
