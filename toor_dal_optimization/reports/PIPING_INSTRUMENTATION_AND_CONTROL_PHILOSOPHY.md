# PIPING, INSTRUMENTATION, AND CONTROL PHILOSOPHY (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-009  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Piping, Process Control & Automation  

---

## 1. Process & Instrumentation Diagrams (P&IDs)

The plant's instrumentation and piping networks are documented across two primary P&ID drawings:
1. **DWG-FIN-15T-003:** Raw Feed Intake, Chemical Dosing Skid (`SK-100`), Jacketed Soaking Vessels (`TK-101A/B`), Slurry Pumps, and Vibratory Dewatering Screen (`VS-101`).
2. **DWG-FIN-15T-004:** Fluid-Bed Dryer (`DR-101`), Steam Heating Coil, Product Cooler (`CLR-101`), Air Blowers, Cyclone Separator, Baghouse, Finished Dal Elevators, and Packaging Machine (`PK-101`).

---

## 2. Piping Material Specifications

| Piping Class | Nominal Rating | Wetted Material | Joint Type | Gasket / O-Ring | Typical Services |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Class SAN-316L** | 10 bar / 120°C | Seamless SS316L (Ra < 0.8µm) | Hygienic Tri-Clamp / Orbital TIG | FDA EPDM / PTFE | Dal slurry, soak liquor, mist rinse, CIP lines |
| **Class STM-150** | 10 bar / 185°C | ASTM A106 Gr B Carbon Steel | ANSI Class 150 Flanged / Welded | Spiral Wound SS316/Graphite | Saturated steam supply ($2.5\text{ bar(g)}$), condensate return |
| **Class UTL-PVC** | 6 bar / 40°C | Schedule 40 UPVC / CPVC | Solvent Welded / Flanged | EPDM | Spent liquor to ETP, chemical acid dosing, drain headers |
| **Class AIR-GI** | 5000 Pa / 70°C| Lock-seam Galvanized Iron | Companion Flange with Neoprene | Closed-cell Neoprene gasket | Fluidizing hot air ducts, exhaust ductwork to cyclone |

---

## 3. Automated Batch Sequence Narrative

The PLC automates the alternating batch soaking sequence across `TK-101A` and `TK-101B` to feed the continuous dryer:

```mermaid
sequenceDiagram
    autonumber
    participant PLC as Siemens S7-1500 PLC
    participant GF as Gravimetric Feeder GF-101
    participant Dose as Dosing Pump P-100 & FT-102
    participant TankA as Soak Tank TK-101A
    participant Slurry as Slurry Pump P-101 & VS-101
    participant Dryer as Fluid-Bed Dryer DR-101

    Note over TankA: Batch A Sequence (60 min total)
    PLC->>Dose: Start P-100; Meter 1,406 kg 0.5% liquor via FT-102
    Dose-->>TankA: Fill liquor in 5 minutes
    PLC->>GF: Start GF-101; Meter 937.5 kg dry dal
    GF-->>TankA: Feed dal in 10 minutes
    PLC->>TankA: Start Agitator AG-101A at 35 RPM
    Note over TankA: Soak timer runs for exactly 30 minutes at 28°C
    PLC->>TankA: Open flush-bottom valve XV-105A
    PLC->>Slurry: Start Slurry Pump P-101A & Vibratory Screen VS-101
    Slurry-->>Dryer: Screen dewaters & discharges wet dal to Dryer CV-101
    PLC->>TankA: Tank empty; Initiate Tank B cycle in TK-101B
```

---

## 4. Cause-and-Effect Safety Matrix

| Initiating Cause / Transmitter | Setpoint / Condition | Automated Interlock Action | Fail-Safe State | Manual Reset Required |
| :--- | :--- | :--- | :--- | :---: |
| **LT-101A/B High-High Level** | Level $\ge 2.20\text{ m}$ ($>85\%$ volume) | Trips feed gate `XV-101` and closes liquor valve `XV-103`. | Valves spring closed | Yes |
| **FT-102 Coriolis Over-Batch** | Total mass $\ge 1,420\text{ kg}$ liquor | Instantly de-energizes dosing pump `P-100` and closes `FV-102`. | Pump stops, valve shut | No (Next batch) |
| **TT-102 Dryer Inlet High-High**| Air temperature $\ge 68.0^\circ\text{C}$ | Trips main steam shutoff valve `XV-112` and throttles `TCV-112`. | Steam valve spring closed | Yes |
| **PDT-101 Low Bed Pressure** | Differential pressure $\le 600\text{ Pa}$ | Indicates loss of fluidization; stops wet dal infeed conveyor `CV-101`. | Conveyor stops | Yes |
| **MD-101 Metal Detection** | Ferrous $\ge 1.0\text{ mm}$ / SS $\ge 1.5\text{ mm}$ | Actuates high-speed pneumatic diverter flap (500 ms stroke); fires horn. | Rejects pouch to locked bin | No |
| **E-Stop Button Depressed** | Any field E-stop station | Instantaneous Category 0 emergency stop of all motors in zone. | Hardwired safety relay open | Yes (Key reset) |
