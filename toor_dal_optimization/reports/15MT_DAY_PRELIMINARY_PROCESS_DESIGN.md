# FINNOAQ TOOR DAL — 15 MT/DAY PRELIMINARY PROCESS DESIGN

**Document ID:** FIN-ENG-15TPD-2026-002  
**Date:** 15 October 2026  
**Governing Standard:** Master Build Directive — Phase 5 Preliminary Industrial Engineering  
**Status:** **PRELIMINARY ENGINEERING MODEL (STAGE 2 LOCKED PENDING STAGE 1 VALIDATION)**  

---

## 1. Design Basis & Governance Notice

> [!IMPORTANT]
> ### STAGE 2 LOCK NOTICE
> This process design represents a preliminary, vendor-independent engineering calculation for a 15,000 kg/day Toor Dal conditioning plant. **Equipment procurement, civil works, and commercial guarantees are strictly locked** until Stage 1 physical kitchen validation passes and representative pilot trials are signed off.

### Dual Basis Clarification
- **Basis 1 (Incoming Feed Basis - Standard Case):** $15,000\text{ kg/day}$ of incoming raw, dry dehulled Tanzanian dal at $10.0\%\ \text{w.b.}$ moisture. At whole-plant recovery of $95.69\%$, finished saleable packaged dal output is **$14,353.5\text{ kg/day}$**.
- **Basis 2 (Finished Product Basis - Alternate Case):** If the client requires exactly $15,000\text{ kg/day}$ of saleable packaged dal, the required incoming raw dal feed rate is **$15,677.2\text{ kg/day}$**.

---

## 2. Operating Schedules: 8h, 16h, and 24h Scenarios

Processing rates depend heavily on daily operating hours. To properly size equipment, both nominal average rates and design rates (accounting for availability $\eta = 0.85$ and engineering design margin $1.15\times$) are calculated:

| Operating Schedule | Productive Hours/Day | Availability Factor | Effective Hours/Day | Nominal Feed Rate (kg/h) | Nominal Packaged Output (kg/h) | **Design Feed Rate (kg/h)** | **Design Output Rate (kg/h)** | Evaluation & Recommendation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Case 1: 1-Shift (8h)** | 8.0 h | 0.85 | 6.8 h | 1,875.0 kg/h | 1,794.2 kg/h | **2,536.8 kg/h** | **2,427.6 kg/h** | Requires massive dryer and tanks; creates bottleneck; uneconomical CapEx. |
| **Case 2: 2-Shift (16h)** | 16.0 h | 0.85 | 13.6 h | 937.5 kg/h | 897.1 kg/h | **1,268.4 kg/h** | **1,213.8 kg/h** | **RECOMMENDED BASE CASE.** Optimal balance of capital cost, footprint, and operating labor. |
| **Case 3: 3-Shift (24h)** | 24.0 h | 0.85 | 20.4 h | 625.0 kg/h | 598.1 kg/h | **845.6 kg/h** | **809.2 kg/h** | Lowest equipment footprint; requires 24/7 continuous shift coverage and night maintenance. |

---

## 3. Vendor-Independent Block Flow Diagram (BFD)

```
                            [ RAW UNTREATED DAL INTAKE (15,000 kg/day) ]
                                                 │
                                                 ▼
                                     [ SCREENING & WEIGHING ]
                                     (Removal of fines/stones)
                                                 │
                    ┌────────────────────────────┴───────────────────────────┐
                    │                                                        │
                    ▼ [EMERGENCY BYPASS ROUTE]                               ▼ [CONDITIONING ROUTE]
          [ UNTREATED DAL STORAGE ]                                 [ BATCH SOAK VESSELS (2x) ]
          (Direct packing if required)                     ◄─────── (0.50% NaHCO3, 1:1.5 ratio, 30 min)
                                                                    ▲        │
                                   [ CHEMICAL PREPARATION SKID ] ───┘        ▼
                                   (Liquor dosing: 112.5 kg/day NaHCO3) [ SPENT LIQUOR DRAINAGE ]
                                                                             │        │
                                                                             │        ▼
                                                                             │  [ TO WWTP EFFLUENT ]
                                                                             ▼
                                                                [ FRESH WATER MIST RINSER ]
                                                                (Single-pass spray: 7,500 L/day)
                                                                             │
                                                                             ▼
                                                                [ FLUID BED DRYER (55°C) ]
                                                                (Thermal Duty: 265 kW gross)
                                                                             │
                                                                             ▼
                                                                [ FLUID BED COOLER (28°C) ]
                                                                (Prevents sweating in packaging)
                                                                             │
                                                                             ▼
                                                                [ QUALITY & WATER ACTIVITY QC ]
                                                                (Moisture 10.0%, Aw <= 0.65)
                                                                             │
                                                                             ▼
                                                                [ METAL DETECTOR & BAGGING ]
                                                                (14,353.5 kg/day Packaged Dal)
```

---

## 4. Major Equipment Sizing & Specifications

### 4.1 Soak Vessels (Tanks T-101A / T-101B)
- **Configuration:** 2 parallel stainless steel (SS304) jacketed soaking vessels operating in staggered batch cycles.
- **Operating Schedule (16h basis):** Total cycle time = $90\text{ minutes}$ ($1.5\text{ h}$). Batches per tank per day = $10.7$ (~11 batches).
- **Batch Charge:**
  - Raw Dal per batch: $703.1\text{ kg}$.
  - Soak Liquor per batch: $1,054.7\text{ kg}$ ($1,049.4\text{ kg}$ water + $5.3\text{ kg}$ $\text{NaHCO}_3$).
- **Volumetric Sizing:**
  - Dal bulk volume ($850\text{ kg/m}^3$): $0.83\text{ m}^3$.
  - Free supernatant liquor volume: $0.72\text{ m}^3$.
  - Slurry working volume: $1.55\text{ m}^3$.
  - Design Fill Factor: $75\%$.
  - **Nominal Vessel Capacity:** **$2.50\text{ m}^3$ ($2,500\text{ L}$)** per tank.
- **Vessel Features:** Conical bottom with pneumatic slide gate; wedge-wire false bottom screen ($1.0\text{ mm}$ slots) for gravity liquor drainage; low-speed sweep agitator ($15\text{ RPM}$) with PTFE scrapers to prevent grain shear.

### 4.2 Continuous Vibrating Fluid Bed Dryer (D-201)
- **Type:** Continuous vibrating fluid bed dryer with air recirculation and economizer coil.
- **Feed Rate to Dryer:** $1,280\text{ kg/h}$ wet rinsed dal ($26.5\%\ \text{w.b.}$ moisture).
- **Product Discharge:** $925\text{ kg/h}$ dried dal ($10.0\%\ \text{w.b.}$ moisture).
- **Water Evaporation Rate:** $230.9\text{ kg water / h}$ ($3,695\text{ kg/day}$).
- **Thermal Sizing:**
  - Thermodynamic Duty: $172.3\text{ kW}$.
  - Gross Thermal Heat Input (at $\eta = 65\%$): **$265.1\text{ kW}$ ($15,268\text{ MJ/day}$)**.
  - Drying Air Temperature: $55.0^\circ\text{C}$ (strictly limited to prevent starch gelatinization).
  - Volumetric Air Flow: **$103.7\text{ m}^3\text{/min}$ ($6,220\text{ m}^3\text{/h}$)**.
  - Fluidization Blower Motor: **$11.0\text{ kW}$** IE3 high-efficiency motor.
- **Bed Dimensions:** Effective deck length $6.0\text{ m}$, width $0.65\text{ m}$ (active bed area $3.9\text{ m}^2$).

### 4.3 Integrated Fluid Bed Cooler (C-202)
- **Purpose:** Dal discharging at $50^\circ\text{C}$ must be cooled to $< 30^\circ\text{C}$ prior to packaging. Hot packaging causes moisture migration to bag surfaces ("sweating"), resulting in rapid fungal proliferation.
- **Air Flow:** $45.0\text{ m}^3\text{/min}$ ambient filtered air ($25^\circ\text{C}$).
- **Blower Motor:** $4.0\text{ kW}$.

---

## 5. Process Control Philosophy & Instrumentation

```
  [ PARAMETER ]              [ SENSOR / ACTUATOR ]              [ CONTROL RANGE ]          [ INTERLOCK / ACTION ]
  Dosing Liquor Concentration  Inline Conductivity Meter (AT-101)  0.50% ± 0.02% w/w          Auto-trim NaHCO3 dosing pump
  Soaking Bath Temperature     RTD PT100 (TT-101)                 25.0°C ± 2.0°C             Alarm if > 32°C (prevents leaching)
  Soak Duration Timer          PLC Automated Sequence             30.0 min ± 30 sec          Auto-open drain valve at 30 min
  Dryer Bed Temperature        Multi-point RTD (TT-201..204)      52.0°C - 55.0°C            Modulate steam control valve
  Exhaust Air Humidity         RH Transmitter (HT-201)            80% - 85% RH               Adjust exhaust damper
  Finished Product Moisture    NIR Online Moisture Meter (MT-301) 10.0% ± 0.3% w.b.          Divert to recycle if > 10.5%
```

---

## 6. HACCP Food-Safety Hazard Analysis

| Process Step | Potential Hazard | Preventive Control Measure | Critical Limit | Monitoring & Corrective Action |
| :--- | :--- | :--- | :--- | :--- |
| **Chemical Storage & Dosing** | Inadvertent contamination with non-food chemical | Procurement strictly restricted to Food Chemicals Codex / IS 2124 Food-Grade $\text{NaHCO}_3$. Dedicated dry store with lock. | Certificate of Analysis per batch. | Reject lot if non-food-grade. Visual check per bag. |
| **Soaking Stage (Wet Residence)** | Microbial proliferation (*Bacillus cereus*, coliforms) during warm/wet hold | Strict limitation of soak time to $30\text{ minutes}$; vessel cleaning and sanitization cycle every 8 hours. | Soak time $\le 45\text{ min}$; liquor temp $\le 30^\circ\text{C}$. | Automatic timer dump. If soaked dal is stalled $> 90\text{ min}$, divert to discard. |
| **Fluid Bed Drying** | Incomplete drying causing subsequent mold growth (*Aspergillus flavus* / aflatoxins) | Continuous online NIR moisture measurement + laboratory oven moisture confirmation per shift. | Product moisture $\le 10.5\%\ \text{w.b.}$, $a_w \le 0.65$. | Auto-divert off-spec dal back to dryer feed. |
| **Cooling & Packaging** | Condensation in plastic packaging | Fluid bed cooling to $< 30^\circ\text{C}$ prior to bagging; laminated barrier film. | Dal exit temp $\le 30.0^\circ\text{C}$. | High-temp interlock on bagging conveyor. |
| **Final Product Inspection** | Ferrous/non-ferrous metal fragments from handling equipment | Tunnel metal detector integrated on final packaging conveyor belt. | Fe $1.5\text{ mm}$, Non-Fe $2.0\text{ mm}$, SS $2.5\text{ mm}$. | Automatic pneumatic reject arm. |

---

## 7. Staged Scale-Up Execution Plan

```
  [ GATE G0: COMPUTATIONAL BASELINE ] (COMPLETED & AUDITED)
  Multi-physics modeling, mass balances, solver benchmarks, code audit.
                   │
                   ▼
  [ GATE G1: TARGET-LOT KITCHEN SCREENING ] (CURRENT PRIORITY)
  8-batch domestic pressure cooker protocol on physical Tanzanian import lot.
                   │
                   ▼
  [ GATE G2: CONFIRMATORY REPLICATION & DRY SHELF LIFE ]
  Independent replication (n=4), re-drying to 10% moisture, 60-day storage test.
                   │
                   ▼
  [ GATE G3: PILOT LINE RUN (100 kg BATCH) ]
  Validation on representative pilot soaker, dewatering screen, and fluid bed dryer.
                   │
                   ▼
  [ GATE G4: REGULATORY & FOOD-SAFETY SIGN-OFF ]
  FSSAI label clearance, NABL lab certificates (residual sodium, microbiology).
                   │
                   ▼
  [ GATE G5: 15 MT/DAY PROCUREMENT & COMMISSIONING ]
  Detailed engineering, P&ID freeze, vendor selection, erection, commissioning.
```
