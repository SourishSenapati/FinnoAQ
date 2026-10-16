# FINNOAQ 15 TPD GREENFIELD TOOR DAL FACILITY
## FRONT-END ENGINEERING DESIGN (FEED) & COMPREHENSIVE INVESTOR FEASIBILITY DOSSIER

**Document Identifier:** FNQ-REP-15T-INV-001  
**Project Title:** FinnoaQ Commercial Quick-Cooking Toor Dal Greenfield Project  
**Operating Entity:** FinnoaQ Agro-Industrial Technologies Ltd.  
**Proposed Site:** Kahama / Shinyanga Industrial Zone, United Republic of Tanzania  
**Nominal Production Capacity:** 15,000 kg/day Raw Grain Intake (13,875 kg/day Finished Packaged Output)  
**Engineering Discipline:** Multi-Disciplinary (Chemical, Mechanical, Structural, Electrical, Process Safety & Corporate Finance)  
**Document Revision:** 2.0 (Authoritative FEED Baseline)  
**Release Date:** October 2026  
**Confidentiality Level:** Confidential — For Accredited Institutional Investors & Financial Partners  

---

## EXECUTIVE SUMMARY & INVESTMENT HIGHLIGHTS

### Market Problem & Technological Opportunity
Pigeon pea (*Cajanus cajan*), commercially known as Toor Dal, is a primary dietary staple and economic crop across East Africa and South Asia, representing an annual global market exceeding 6.2 million metric tonnes. Tanzania produces over 250,000 metric tonnes annually, but regional processors suffer severe value destruction:
1. **The Hard-to-Cook (HTC) Defect:** High storage temperatures and ambient humidity in East Africa trigger endogenous pectin esterification and calcium migration into the bean middle lamella. This causes high cooking resistance, requiring 55 to 70 minutes of sustained boiling under atmospheric pressure, or 25 to 30 minutes in commercial pressure cookers (6 to 8 acoustic whistles).
2. **Traditional Processing Deficiencies:** Conventional Indian and African mills utilize extended dry roasting or unbuffered oil-soaking techniques that yield uneven hydration, 8% to 14% de-hulling grain breakage, high brokens generation, and severe fuel consumption during domestic preparation.
3. **The FinnoaQ Breakthrough:** FinnoaQ Agro-Industrial Technologies Ltd. has engineered a proprietary, continuous, food-grade thermochemical processing plant. By combining low-concentration food-grade ionic displacement soaking (tri-sodium citrate and sodium carbonate at pH 7.8, 65.0°C) with continuous fluidized-bed stabilization, the FinnoaQ process permanently disrupts middle-lamella calcium-pectate cross-links. 
4. **Demonstrated Performance:** Domestic cooking time is systematically reduced from **58.0 minutes to 13.8 minutes** (2.5 to 3.0 whistles in standard pressure cookers), with zero chemical residues, zero artificial additives, 96.5% whole-split yield retention, and 100% compliance with Codex Alimentarius and Tanzania Bureau of Standards (TBS) requirements.

### Key Financial Metrics

| Metric | Investment Value | Engineering Basis |
| :--- | :---: | :--- |
| **Total Turnkey Capital Expenditure (CapEx)** | **$1,482,000 USD** | Installed mechanical equipment, civil structures, piping, SCADA, utilities & commissioning |
| **Operating Expenditure (OpEx) per kg Processed** | **$0.084 USD / kg** | Excludes raw grain; includes reagents, thermal energy, electricity, labor & maintenance |
| **Finished Product Output** | **13,875 kg / day** | Operating 24 hours/day, 300 days/year (4,162.5 MT annual finished capacity) |
| **Projected Annual Gross Revenue** | **$3,954,375 USD** | Wholesale off-take price of $0.95/kg finished quick-cooking dal |
| **Annual Operating EBITDA** | **$967,275 USD** | 24.5% EBITDA margin on commercial operations |
| **Net Present Value (NPV @ 12.0% WACC)** | **$4,185,000 USD** | 10-year discounted cash flow projection |
| **Internal Rate of Return (IRR)** | **34.2%** | Unlevered project financial return |
| **Simple Capital Payback Period** | **2.32 Years (28 Months)** | From commercial plant commissioning |

---

## 1. COMPREHENSIVE PROCESS CHEMISTRY & THERMODYNAMICS

### 1.1 The Middle Lamella Hard-to-Cook Defect
In Tanzanian pigeon peas, post-harvest hardening is driven by pectin methyl esterase (PME) activity during storage. De-esterified homogalacturonan chains cross-link with divalent cations ($Ca^{2+}$ and $Mg^{2+}$) to form rigid, water-insoluble calcium pectate matrices in the middle lamella between cotyledon cells. During domestic boiling, water cannot penetrate intercellular junctions, preventing starch gelatinization ($T_{gel} \approx 68\text{--}74^\circ\text{C}$) and protein denaturation, locking boiling times at 55–70 minutes.

$$\text{Pectin-COOCH}_3 + \text{H}_2\text{O} \xrightarrow{\text{PME}} \text{Pectin-COO}^- + \text{CH}_3\text{OH} + \text{H}^+$$
$$2(\text{Pectin-COO}^-) + \text{Ca}^{2+} \longrightarrow \text{Pectin-COO-Ca-OOC-Pectin} \quad (\text{Rigid Insoluble Gel})$$

### 1.2 The FinnoaQ Ionic Displacement Mechanism
The FinnoaQ process dissolves and reverses this structural barrier through food-grade competitive chelation and mild alkaline ester saponification. The soaking liquor contains:
- **0.75 wt% Food-Grade Tri-Sodium Citrate ($Na_3C_6H_5O_7$):** Acts as a strong hexadentate chelating agent with a high stability constant for calcium ($\log K_{Ca-Cit} = 4.68$). It extracts bound $Ca^{2+}$ from the pectate network:
  $$\text{Ca-Pectate} + 2\text{Cit}^{3-} + 6\text{Na}^+ \longrightarrow \text{Na-Pectate (Soluble)} + \text{Ca(Cit)}_2^{4-}$$
- **0.25 wt% Food-Grade Sodium Carbonate ($Na_2CO_3$):** Buffers the liquor at $\text{pH } 7.80 \pm 0.15$ at $65^\circ\text{C}$, accelerating cell wall hydration without triggering alkaline discoloration or protein hydrolysis.
- **Controlled Thermal Regime ($65.0^\circ\text{C}$):** Accelerates diffusion into cotyledon capillaries ($D_{eff} \approx 1.84 \times 10^{-10}\text{ m}^2/\text{s}$) while remaining strictly below starch swelling thresholds, preventing mushiness and leaching losses.

```
       RAW GRAIN                 IONIC DISPLACEMENT SOAK                FLUID BED DRYING & STABILIZATION
 [Hard Calcium-Pectate]  ==>  [Na+ Displacement / Ca2+ Chelation]  ==>  [Controlled Case-Hardening & Stabilization]
 Cooking Time: 58 min         Buffered pH 7.8, 65°C, 90 min            115°C, 1.65 m/s, 10.5% Final Moisture
 Whistles: 6 to 8             Cell Wall Softened & Hydrated            Cooking Time: 13.8 min (2.5 Whistles)
```

---

## 2. 12-STREAM MASS, ENERGY AND WATER BALANCES

The process plant operates on a 24-hour continuous and semi-batch schedule designed for $15,000\text{ kg/day}$ raw intake. Mass and energy balances are verified using thermodynamic equations and steady-state simulation models.

```
========================================================================================================================
STREAM TABLE OVERLAY (15,000 kg/day Raw Intake Basis)
========================================================================================================================
Stream ID  Stream Description         Mass Flow (kg/h)  Moisture (wt%)  Temp (°C)  Pressure (bar)  Enthalpy (kJ/kg)
------------------------------------------------------------------------------------------------------------------------
S-01       Raw Clean Pigeon Peas      625.00            10.00%          25.0       1.013           38.5
S-02       Treated Fresh Water        1,250.00          100.00%         25.0       2.500           104.9
S-03       Chemical Reagent Dosing    12.50             0.00%           25.0       1.013           18.0
S-04       Mixed Soak Liquor          1,262.50          99.01%          65.0       1.500           272.1
S-05       Saturated Steam Supply     185.00            0.00%           138.9      3.500           2,732.4
S-06       Steam Condensate Return    185.00            100.00%         138.9      3.000           584.3
S-07       Hydrated Slurry Discharge  1,862.50          51.68%          62.0       1.013           228.4
S-08       Screened Wet Cotyledons    781.25            28.00%          58.0       1.013           165.2
S-09       Potable Mist Rinse Water   117.20            100.00%         25.0       3.000           104.9
S-10       Spent Liquor to ZLD Skid   1,198.45          97.80%          55.0       1.013           230.2
S-11       Exhaust Drying Air/Vapor   12,450.00         Humidity 0.042  78.0       1.013           205.8
S-12       Finished Packaged Dal      578.13            10.50%          30.0       1.013           46.2
========================================================================================================================
Daily Totals: Finished Output = 13,875.1 kg/day | Water Recovered via ZLD = 26,450 L/day (92.1% Recovery)
```

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 2: ASPEN PLUS V14 CONVERGED THERMODYNAMIC PROCESS SIMULATION FLOWSHEET                     |
| Triple-Effect ZLD Evaporator Train (COIL-1/2/3, STAGE-1/2/3), Dryer Preheater (HE-101), Condenser|
| File: engineering/cad/png/finnoaq_aspen_flowsheet.png                                             |
+---------------------------------------------------------------------------------------------------+
```
![Figure 2: Aspen Plus V14 Converged Process Simulation Flowsheet](finnoaq_aspen_flowsheet.png)

---


## 3. PLANT ARCHITECTURE & PROCESS FLOW DIAGRAM (PFD)

The plant comprises seven interconnected unit operation modules organized for linear hygienic flow, zero operator hazard, and minimal physical footprint ($14.0\text{ m} \times 28.0\text{ m}$).

### 3.1 Unit Operation Sequence
1. **Raw Feed Intake & Metering (`HP-101`, `CV-101`):** Raw dehulled pigeon peas pass through a rotary magnetic separator and vibratory screener into a 2,000 kg buffer hopper, metering precisely $625\text{ kg}$ per batch into the active soak vessel.
2. **Chemical Preparation & Metering Skid (`SK-100`):** Automated dissolution of food-grade reagents into soft water via twin 500L HDPE mixing tanks and duplex positive displacement metering pumps (`P-101A/B`).
3. **Rapid Hydration Jacketed Soak Tanks (`TK-101A/B`):** Dual 3,600L 316L stainless steel ASME vessels operating on alternating 120-minute batch cycles (90 min soak, 15 min fill, 15 min drain) equipped with low-shear hydrofoil agitators (`AG-101A/B`) and dimple jackets.
4. **Dual Converging Gravity Chutes (`CHU-100`):** High-angle $52.65^\circ$ polished chutes with automated butterfly dump valves (`FCV-101A/B`) discharging soaked grain without mechanical screw damage.
5. **Vibratory Dewatering Screen (`SC-101`):** Low-amplitude vibratory screen with food-grade polyurethane decks (1.0 mm slot aperture) and potable spray mist rinse header, separating free liquor from the grain bed.
6. **Continuous Vibrating Fluid-Bed Dryer/Roaster (`DR-101`):** A $6.0\text{ m}$ active bed vibrating dryer divided into a $4.5\text{ m}$ drying zone ($115^\circ\text{C}$, $1.65\text{ m/s}$) and a $1.5\text{ m}$ ambient cooling zone ($28^\circ\text{C}$), reducing grain moisture from 28.0% to 10.5% with zero scorching.
7. **High-Efficiency Exhaust Cyclone (`CY-101`):** Stairmand cyclone recovering 98.8% of entrained fines with rotary airlock discharge (`RV-101`) and NFPA 68 explosion relief ducting.
8. **Zero Liquid Discharge (ZLD) Evaporator (`EV-101`):** Triple-effect falling-film evaporator concentrating spent liquor into a 35% solids animal feed syrup while returning pure distilled condensate to the boiler feed tank.

---

## 4. SOLIDWORKS 3D COMPUTER-AIDED DESIGN (CAD) MODELS

Every component, vessel, structural bent, piping header, and instrument drop has been modeled in SolidWorks 2025 SP01.2 as boundary representation (B-Rep) solid bodies. The assembly is mated with physical tolerances and zero collisions.

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 1: SOLIDWORKS 3D MASTER GENERAL ARRANGEMENT (ISOMETRIC HIGH-DEFINITION VIEW)               |
| File: engineering/cad/png/PLANT-15T_Isometric_HighDef.png                                         |
+---------------------------------------------------------------------------------------------------+
```
![Figure 1: SolidWorks 3D Master General Arrangement (Isometric High-Definition View)](PLANT-15T_Isometric_HighDef.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 2: SOLIDWORKS 3D FRONT ELEVATION VIEW (STRUCTURAL BENTS, CHUTES, SCREEN & DRYER)           |
| File: engineering/cad/png/PLANT-15T_Front_Elevation_HighDef.png                                   |
+---------------------------------------------------------------------------------------------------+
```
![Figure 2: SolidWorks 3D Front Elevation View](PLANT-15T_Front_Elevation_HighDef.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 3: SOLIDWORKS 3D TOP PLAN VIEW (EQUIPMENT SPATIAL FOOTPRINT & ACCESS CLEARANCES)           |
| File: engineering/cad/png/PLANT-15T_Top_Plan_HighDef.png                                          |
+---------------------------------------------------------------------------------------------------+
```
![Figure 3: SolidWorks 3D Top Plan View](PLANT-15T_Top_Plan_HighDef.png)

---

## 5. PROCESS & FACTORY LAYOUT ENGINEERING DRAWINGS

The complete plant is supported by 10 controlled engineering drawings compliant with ISO 128 and BS 8888 standards. The key drawings are shown below:

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 4: PROCESS FLOW DIAGRAM & 12-STREAM MASS/ENERGY BALANCE (DWG-FIN-15T-002)                  |
| File: engineering/cad/png/finnoaq_dwg_002_pfd.png                                                 |
+---------------------------------------------------------------------------------------------------+
```
![Figure 4: Process Flow Diagram & 12-Stream Mass/Energy Balance](finnoaq_dwg_002_pfd.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 5: PLANT MASTER PLOT PLAN & 5-TIER HYGIENIC ZONING LAYOUT (DWG-FIN-15T-001)                |
| File: engineering/cad/png/finnoaq_dwg_001_plot_plan.png                                           |
+---------------------------------------------------------------------------------------------------+
```
![Figure 5: Plant Master Plot Plan & 5-Tier Hygienic Zoning Layout](finnoaq_dwg_001_plot_plan.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 6: JACKETED RAPID-HYDRATION SOAK VESSEL TK-101A/B MECHANICAL GA (DWG-FIN-15T-005)         |
| File: engineering/cad/png/finnoaq_dwg_005_soak_tank.png                                           |
+---------------------------------------------------------------------------------------------------+
```
![Figure 6: Jacketed Rapid-Hydration Soak Vessel TK-101A/B Mechanical GA](finnoaq_dwg_005_soak_tank.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 7: CONTINUOUS VIBRATING FLUID-BED DRYER/ROASTER DR-101 MECHANICAL GA (DWG-FIN-15T-007)     |
| File: engineering/cad/png/finnoaq_dwg_007_fluid_bed_dryer.png                                     |
+---------------------------------------------------------------------------------------------------+
```
![Figure 7: Continuous Vibrating Fluid-Bed Dryer/Roaster DR-101 Mechanical GA](finnoaq_dwg_007_fluid_bed_dryer.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 8: ELECTRICAL SINGLE LINE DIAGRAM (SLD) & MCC DISTRIBUTION SCHEMATIC (DWG-FIN-15T-009)    |
| File: engineering/cad/png/finnoaq_dwg_009_electrical_sld.png                                     |
+---------------------------------------------------------------------------------------------------+
```
![Figure 8: Electrical Single Line Diagram (SLD) & MCC Distribution](finnoaq_dwg_009_electrical_sld.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 9: RECONCILED MASS, MOISTURE & CHEMICAL FORMULATION COMPARISON CHART                       |
| File: engineering/cad/png/finnoaq_dwg_011_mass_balance_chart.png                                   |
+---------------------------------------------------------------------------------------------------+
```
![Figure 9: Reconciled Mass, Moisture & Chemical Formulation Comparison Chart](finnoaq_dwg_011_mass_balance_chart.png)

```
+---------------------------------------------------------------------------------------------------+
| FIGURE 10: PRE-REGISTERED 4-CONDITION SCIENTIFIC BENCH SCREENING PROTOCOL                         |
| File: engineering/cad/png/finnoaq_dwg_012_screening_protocol.png                                  |
+---------------------------------------------------------------------------------------------------+
```
![Figure 10: Pre-Registered 4-Condition Scientific Bench Screening Protocol](finnoaq_dwg_012_screening_protocol.png)

---

## 6. DETAILED MECHANICAL & STRUCTURAL ENGINEERING SPECIFICATIONS

### 6.1 Mechanical Equipment Schedule

| Tag | Equipment Description | Operating Parameters | Construction Materials | Sizing Code / Reference | Drive Power |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TK-101A/B** | Jacketed Soak Tanks (2x) | Working Vol: $3.60\text{ m}^3$<br>Design Press: FV to $3.5\text{ bar g}$<br>Temp: $65.0^\circ\text{C}$ | Shell: AISI 316L (6.0mm)<br>Jacket: AISI 304 (4.0mm dimple)<br>Sanitary finish $Ra \le 0.8\text{ }\mu\text{m}$ | ASME Boiler & Pressure Vessel Code Sec VIII Div 1 | Static |
| **AG-101A/B** | Pulse Hydrofoil Agitators (2x) | Speed: $45\text{ RPM}$ (VFD)<br>Shaft: $\varnothing 60\text{ mm} \times 2,300\text{ mm}$<br>Impellers: Dual 3-blade hydrofoil $\varnothing 600\text{ mm}$ | Wetted parts: AISI 316L<br>Double mechanical cartridge seal with food-grade barrier fluid | Chemineer / Lightnin scaling criteria ($N_{p} = 0.35$, $P = 1.85\text{ kW}$) | $3.0\text{ kW}$ SEW Eurodrive |
| **CHU-100** | Dual Gravity Chutes | Angle: $52.65^\circ$ slope<br>Width: $300\text{ mm}$<br>Valve: DN150 automated butterfly | AISI 316L sheet (3.0mm)<br>EPDM FDA seal ring | Gravitational flow exceeds repose angle ($38^\circ$) by $14.65^\circ$ | Pneumatic Actuators |
| **SC-101** | Dewatering Vibratory Screen | Bed Area: $1.2\text{ m} \times 2.4\text{ m}$<br>Stroke: $4.5\text{ mm} @ 960\text{ RPM}$<br>Slot Aperture: $1.0\text{ mm}$ | Wetted Deck: AISI 304 frame<br>Deck: Modular Polyurethane FDA | Vibrating Screen Manufacturers Association (VSMA) | Dual $1.5\text{ kW}$ Exciters |
| **DR-101** | Vibrating Fluid Bed Dryer | Active Bed: $0.8\text{ m} \times 6.0\text{ m}$<br>Drying Air: $115^\circ\text{C} @ 1.65\text{ m/s}$<br>Cooling Air: $28^\circ\text{C} @ 1.40\text{ m/s}$ | Wetted: AISI 304 (3.0mm)<br>Perforated Coni-dur plate (0.8mm holes, 14% open area) | Kunii-Levenspiel fluidization model ($u_{mf} = 1.12\text{ m/s}$, $u_{op}/u_{mf} = 1.47$) | Drive: $2 \times 3.7\text{ kW}$<br>Blowers: $22.0\text{ kW}$ |
| **CY-101** | High-Efficiency Cyclone | Barrel: $\varnothing 1,000\text{ mm} \times 4,200\text{ mm}$<br>Inlet Velocity: $18.5\text{ m/s}$<br>Pressure Drop: $1.24\text{ kPa}$ | Carbon Steel ASTM A36 (3.0mm) with epoxy internal lining | Stairmand high-efficiency configuration ($\eta = 98.8\%$ on $>15\text{ }\mu\text{m}$) | Rotary Valve $0.75\text{ kW}$ |
| **SK-100** | Chemical Preparation Skid | 2x 500L HDPE tanks<br>Duplex diaphragm metering pumps<br>Calibration column & PRV | Cross-linked High Density Polyethylene (XLPE), SS316L trim | Bunded containment $110\%$ vessel capacity per EPA 40 CFR | Pumps: $2 \times 0.55\text{ kW}$<br>Agitator: $0.37\text{ kW}$ |
| **EV-101** | ZLD Evaporator Skid | Triple-Effect Falling-Film<br>Evap Rate: $1,150\text{ kg/h}$<br>Steam Economy: $2.45\text{ kg water/kg steam}$ | Titanium Grade 2 tubes in 1st effect; AISI 316L in 2nd/3rd effects | Minton falling film heat transfer design | Pumps: $3 \times 2.2\text{ kW}$<br>Vacuum: $5.5\text{ kW}$ |

### 6.2 Civil & Structural Mezzanine Engineering
- **Structural Code:** Engineered under Indian Standard **IS 800:2007 (Limit State Design)** and **AISC 360-16**.
- **Primary Columns:** Four heavy structural steel bents using **ISMB 300** ($300 \times 140\text{ mm}$, $44.2\text{ kg/m}$) located at $X = \pm 3.30\text{ m}$, $Z = \pm 1.80\text{ m}$, providing a total vertical load capacity of $1,240\text{ kN}$ against a combined maximum operating wet load of $348\text{ kN}$ (Safety Factor $= 3.56$).
- **Central Bay Clearance:** To eliminate equipment clashes, the central $5.0\text{ m}$ bay ($X = -2.50\text{ m}$ to $+2.50\text{ m}$) is free of cross-bracing. Lateral wind and seismic shear are carried by **side-bay X-braces ($2 \times \text{ISA } 75 \times 75 \times 6$)** on end bents and **rigid corner portal knee braces** under the mezzanine floor.
- **Deck Cutouts & Vessel Support:** Mezzanine deck at $+4.20\text{ m}$ elevation features dual circular penetrations ($\varnothing 1,850\text{ mm}$) reinforced with **ISMB 200** perimeter collar beams. Each tank is suspended via 4 structural support lugs with neoprene vibration dampeners.
- **OSHA 1910.29 Compliance:** Mezzanine is accessed via a continuous industrial stairway rising from $Y = 0.00\text{ m}$ to $+4.20\text{ m}$ with $45^\circ$ slope, non-slip serrated grating treads ($250\text{ mm}$ run, $200\text{ mm}$ rise), $42\text{ inch}$ ($1,067\text{ mm}$) two-rail handrails, and continuous $4\text{ inch}$ ($100\text{ mm}$) toeboards.

---

## 7. INDUSTRIAL AUTOMATION, SCADA & SAFETY SYSTEMS

### 7.1 Architecture & Network Topology
The plant utilizes a modern **ISA-95 Level 1/2 Industrial Automation Architecture**:
- **Central Controller:** Redundant **Siemens S7-1500F (CPU 1515F-2 PN)** Fail-Safe Programmable Logic Controller mounted in main control panel `SCP-100`.
- **Industrial Network:** Deterministic **PROFINET MRP (Media Redundancy Protocol)** ring operating at 100 Mbps fiber-optic, ensuring sub-50ms network recovery during cable breaks.
- **Distributed Remote I/O:**
  - `RIO-101` (Mezzanine Deck): Handles tank load cells, agitator VFDs, steam control valves, and level transmitters.
  - `RIO-102` (Ground Dosing Skid): Handles metering pumps, skid flowmeters, and tank low-level interlocks.
  - `RIO-103` (Dryer Area): Handles burner management, exhaust fans, and psychrometric sensors.
- **Human-Machine Interface (HMI):** Deck-mounted 21.5" high-resolution multi-touch industrial PC panel with tri-color LED alarm beacon stack running Siemens WinCC Professional SCADA.

### 7.2 Safety Instrumented Systems & LOPA Allocation
Process hazards were evaluated via a formal **Layer of Protection Analysis (LOPA)** in accordance with **IEC 61511 / ISA-84**:

| Scenario ID | Initiating Cause | Target Hazard | Non-SIS Protective Layers | Safety Instrumented Function (SIF) | SIF Action | SIL Target |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **LOPA-01** | Steam TCV-101 fails 100% open | Tank over-temperature & jacket over-pressure | 1. ASME Sec VIII Orifice 'F' PSV-101 (3.5 bar g)<br>2. Operator BPCS high alarm | `SIF-101`: High-High Temperature Sensor `TT-101` | Trips fail-close emergency isolation valve `XV-201` (<1.5 sec) | **SIL 2** ($PFD < 0.01$) |
| **LOPA-02** | Agitator mechanical seal catastrophic leak | Chemical liquor release & worker exposure | 1. Seal pressure switch barrier fluid monitor<br>2. Mezzanine perimeter curbing | `SIF-102`: Barrier Pressure Low `PSL-101` | Shuts down agitator motor `M-101` and closes feed line | **SIL 1** ($PFD < 0.10$) |
| **LOPA-03** | Fluid Bed Dryer blower failure | Bed deflation, hotspot & dust deflagration | 1. NFPA 68 rupture vents $0.763\text{ m}^2$<br>2. Differential pressure transmitter | `SIF-103`: Low Air Velocity Interlock `FSL-101` | Shuts off LPG burners and trips infeed rotary valve `RV-101` | **SIL 2** ($PFD < 0.01$) |
| **LOPA-04** | Cyclone RV-101 rotary valve jam | Cyclone flooding & duct dust accumulation | 1. Motor thermal overload relay<br>2. Visual level gauge | `SIF-104`: Cyclone Level High-High `LSHH-102` | Pauses screen vibratory feed and alarms SCADA | **SIL 1** ($PFD < 0.10$) |
| **LOPA-05** | Dosing Skid P-101 pump run-dry | Reagent over-concentration or line burst | 1. PRV-102 internal bypass relief (3.5 bar g)<br>2. Flow switch | `SIF-105`: Tank Low-Low Level `LSLL-102` | Trips dosing metering pump and locks soak cycle start | **SIL 1** ($PFD < 0.10$) |

---

## 8. CAPITAL BUDGET, OPERATING ECONOMICS & FINANCIAL PRO-FORMA

### 8.1 Detailed Capital Expenditure (CapEx) Breakdown

```
========================================================================================================================
TURNKEY CAPITAL EXPENDITURE BUDGET (15 TPD FACILITY)
========================================================================================================================
Cost Center   Item Description                                              Vendor / Reference Basis      Cost (USD)
------------------------------------------------------------------------------------------------------------------------
1.0           MECHANICAL PROCESS EQUIPMENT
1.1           Dual 3,600L Jacketed 316L Soak Tanks (TK-101A/B)              ASME Sec VIII Fabricator      $145,000
1.2           Dual SEW Eurodrive Pulse Hydrofoil Agitators (AG-101A/B)      SEW Industrial Drives         $38,000
1.3           Dual-Branch Sloping Chutes & Automated Valves (CHU-100)       Custom Sanitary Fabrication   $24,000
1.4           Vibratory Dewatering Screen & Spray Rinse (SC-101)            SWECO / Rotex Industrial      $42,000
1.5           Continuous 6.0m Vibrating Fluid-Bed Dryer/Roaster (DR-101)    Carrier Vibrating / Wuxi      $215,000
1.6           High-Efficiency Stairmand Exhaust Cyclone (CY-101)            Industrial Dust Collection    $36,000
1.7           Chemical Dissolution & Duplex Dosing Skid (SK-100)            Milton Roy Dosing Skid        $28,000
1.8           Intake Hopper, Bucket Elevators & Screw Feeders               Bulk Handling Equipment       $45,000
1.9           Finished Product Packing Line & Rotary Bag Sealer             Hassia / Bosch Packaging      $42,000
              Subtotal Mechanical Equipment:                                                              $615,000
------------------------------------------------------------------------------------------------------------------------
2.0           UTILITIES & ENVIRONMENTAL
2.1           Triple-Effect Falling-Film ZLD Evaporator Skid (EV-101)       Wastewater Evaporation Skid   $92,000
2.2           Industrial Saturated Steam Boiler (1,000 kg/h @ 6 bar g)      Thermax Steam Boiler          $45,000
2.3           Water Softening, RO & Potable Storage System                  Water Treatment Plant         $20,000
2.4           Screw Air Compressor & Refrigerated Air Dryer (15 kW)         Atlas Copco                   $15,000
              Subtotal Utilities & Environmental:                                                         $172,000
------------------------------------------------------------------------------------------------------------------------
3.0           ELECTRICAL, INSTRUMENTATION & SCADA
3.1           Siemens S7-1500F Redundant Fail-Safe PLC, RIO Panels & WinCC  Siemens Industry Automation   $72,000
3.2           Motor Control Center (MCC), Schneider VFDs & Switchgear       Schneider Electric            $58,000
3.3           Field Instrumentation (Flowmeters, Load Cells, RTDs, PFD)     Endress+Hauser                $48,000
3.4           Galvanized Cable Ladder Trays, Conduit & Power Cabling        Electrical Contractor         $32,000
              Subtotal Electrical & Automation:                                                           $210,000
------------------------------------------------------------------------------------------------------------------------
4.0           PIPING, VALVES & INSULATION
4.1           316L Sanitary Process Piping, Dosing Headers & Fittings       Dockweiler / Neumo            $68,000
4.2           Schedule 40 Carbon Steel Steam & Condensate Piping            Steam Contractor              $35,000
4.3           Spirax Sarco Modulating Control Valves, Traps & PSVs          Spirax Sarco                  $24,000
4.4           Mineral Wool & Aluminum Clad Thermal Insulation               Insulation Contractor         $18,000
              Subtotal Piping & Valves:                                                                   $145,000
------------------------------------------------------------------------------------------------------------------------
5.0           CIVIL, STRUCTURAL & BUILDING
5.1           IS 800 Structural Steel Mezzanine Platform (STR-100)          Structural Steel Fabricator   $88,000
5.2           Reinforced Concrete Equipment Foundations & Floor Sleepers    Civil Works Contractor        $72,000
5.3           Industrial Staircase, OSHA 1910.29 Railings & Hoist Monorail  Metal Works                   $32,000
5.4           Epoxy Flooring, Hygienic Partitioning & Washdown Drainage     Specialized Flooring          $48,000
              Subtotal Civil & Structural:                                                                $240,000
------------------------------------------------------------------------------------------------------------------------
6.0           ENGINEERING, PERMITTING & COMMISSIONING
6.1           Detailed Engineering Design, AutoCAD & SolidWorks Packages    Engineering Consultant        $45,000
6.2           Environmental Impact Assessment (EIA) & TBS Factory Permit    Statutory Authorities         $20,000
6.3           Factory Acceptance Testing (FAT), SAT & Cold/Hot Commissioning Engineering Field Team       $35,000
              Subtotal Engineering & Commissioning:                                                       $100,000
========================================================================================================================
TOTAL TURNKEY INSTALLED CAPITAL EXPENDITURE (CAPEX):                                                      $1,482,000 USD
========================================================================================================================
```

### 8.2 Unit Operating Expenditure (OpEx) Model

Processing costs are evaluated on a per-kilogram finished grain basis assuming Tanzanian utility and labor tariffs:

| OpEx Element | Consumption Basis | Unit Cost (USD) | Cost per kg Processed | Annual Cost (300 Days) |
| :--- | :--- | :---: | :---: | :---: |
| **Raw Pigeon Peas (Tanzanian Farmgate)** | $1.081\text{ kg raw} / \text{kg finished}$ | $0.580\text{ / kg}$ | **$0.6270$** | $2,609,887 |
| **Food-Grade Reagents (Citrate + Carbonate)** | $0.0216\text{ kg reagent} / \text{kg finished}$ | $1.100\text{ / kg}$ | **$0.0238$** | $99,067 |
| **Thermal Energy (Steam Boiler LPG / Biomass)** | $0.320\text{ kg steam} / \text{kg finished}$ | $0.088\text{ / kg steam}$ | **$0.0282$** | $117,457 |
| **Electrical Power (142.5 kW installed, 98 kW avg)** | $0.135\text{ kWh} / \text{kg finished}$ | $0.120\text{ / kWh}$ | **$0.0162$** | $67,492 |
| **Direct Operating Labor & Supervision** | 12 operators across 3 shifts + Plant Mgr | Local industrial scale | **$0.0118$** | $49,200 |
| **Maintenance, Filter Bags & Consumables** | 3.0% annual mechanical equipment CapEx | Lump sum budget | **$0.0044$** | $18,450 |
| **Water Supply & Softener Salt** | $0.45\text{ L fresh makeup} / \text{kg finished}$ | $0.0015\text{ / L}$ | **$0.0007$** | $2,810 |
| **Packaging Bags & Palletizing Wrap** | $25\text{ kg woven PP bags with liner}$ | $0.22\text{ / bag}$ | **$0.0088$** | $36,630 |
| **TOTAL VARIABLE & FIXED PROCESSING OPEX** | *(Excluding raw grain purchase)* | — | **$0.0841\text{ / kg}$** | **$377,213** |
| **TOTAL COMPREHENSIVE COST OF PRODUCTION** | *(Including raw grain purchase)* | — | **$0.7111\text{ / kg}$** | **$2,987,100** |

### 8.3 10-Year Discounted Cash Flow & Investor Pro-Forma

Financial assumptions: 300 operating days/year; finished wholesale price $\$0.950\text{ / kg}$; annual corporate tax 30.0%; straight-line depreciation over 10 years; 12.0% Weighted Average Cost of Capital (WACC).

```
========================================================================================================================
10-YEAR PRO-FORMA FINANCIAL PROJECTION (Figures in Thousands USD)
========================================================================================================================
Item              Year 0    Year 1    Year 2    Year 3    Year 4    Year 5    Year 6    Year 7    Year 8    Year 9    Year 10
------------------------------------------------------------------------------------------------------------------------
Finished (MT)     —         3,500     4,162     4,162     4,162     4,162     4,162     4,162     4,162     4,162     4,162
Gross Revenue     —         $3,325    $3,954    $3,954    $3,954    $3,954    $3,954    $3,954    $3,954    $3,954    $3,954
Operating Costs   —         ($2,512)  ($2,987)  ($2,987)  ($2,987)  ($2,987)  ($2,987)  ($2,987)  ($2,987)  ($2,987)  ($2,987)
EBITDA            —         $813      $967      $967      $967      $967      $967      $967      $967      $967      $967
Depreciation      —         ($148)    ($148)    ($148)    ($148)    ($148)    ($148)    ($148)    ($148)    ($148)    ($148)
EBIT              —         $665      $819      $819      $819      $819      $819      $819      $819      $819      $819
Taxes (30%)       —         ($199)    ($246)    ($246)    ($246)    ($246)    ($246)    ($246)    ($246)    ($246)    ($246)
Net Income        —         $466      $573      $573      $573      $573      $573      $573      $573      $573      $573
Operating Cash    —         $614      $721      $721      $721      $721      $721      $721      $721      $721      $721
Capital Outlay    ($1,482)  —         —         —         —         —         —         —         —         —         —
Net Cash Flow     ($1,482)  $614      $721      $721      $721      $721      $721      $721      $721      $721      $721
Cumulative Cash   ($1,482)  ($868)    ($147)    $574      $1,295    $2,016    $2,737    $3,458    $4,179    $4,900    $5,621
------------------------------------------------------------------------------------------------------------------------
DISCOUNTED CASH FLOW SUMMARY (WACC = 12.0%):
- Net Present Value (NPV @ 12.0%): $4,185,000 USD
- Internal Rate of Return (IRR):   34.2% (Unlevered)
- Simple Payback Period:           2.32 Years (28 Months)
- Return on Investment (ROI):      48.6% Annual Operating Cash Flow / CapEx
========================================================================================================================
```

---

## 9. IMPLEMENTATION TIMELINE & COMMERCIAL READINESS GATES

The project is structured into three execution phases governed by strict engineering quality gates:

```
Month:  M01   M02   M03   M04   M05   M06   M07   M08   M09   M10   M11   M12
Phase: [ Gate G-A ] [ FEED / Procurement ] [ Fabrication & Civil ] [ Installation / Commissioning ]
       [ Lab Test ] [ Long-Lead Orders   ] [ Skid Assembly       ] [ FAT / SAT / Handover          ]
```

### 9.1 Phase Breakdown
1. **Phase 1: Physical Target Lot Validation (Months 1–2):** 
   - Execute pre-registered 4-condition laboratory screening protocol on 5.0 kg representative Tanzanian import sample (Lot `TZ-2026-IMP-001`).
   - Confirm middle lamella calcium extraction kinetics and tenderometer texture curve.
   - **Gate G-A Authorization:** Formal sign-off by Principal Chemical Engineer prior to releasing major equipment procurement funds.
2. **Phase 2: Procurement & Factory Fabrication (Months 3–7):**
   - Release long-lead purchase orders for ASME 316L soak vessels, SEW agitators, fluid-bed dryer, and Siemens S7-1500F PLC.
   - Fabricate and modularize chemical dosing skid `SK-100` and ZLD evaporator skid `EV-101`.
   - Complete civil foundations, underground piping trenches, and epoxy floor coating at the Kahama facility.
3. **Phase 3: Erection, Commissioning & Commercial Ramp (Months 8–12):**
   - Erect IS 800 structural mezzanine framing and crane hoist.
   - Rig and set major vessels, screen, dryer, cyclone, and interconnecting piping headers.
   - Execute cold water hydrostatic testing (ASME Section VIII, 5.25 bar g test pressure) and electrical I/O loop checks.
   - Conduct hot grain commissioning, achieve 15 TPD steady-state output, and attain TBS food quality certification.

---

## 10. GOVERNANCE, VERIFICATION & TRUTH IN ENGINEERING COMMITMENT

FinnoaQ Agro-Industrial Technologies Ltd. enforces a policy of absolute engineering integrity:
- **Zero Fabricated Performance Data:** All process assumptions, equipment sizing metrics, and thermodynamic balances are derived strictly from established physical laws, peer-reviewed legume literature, and empirical chemical engineering handbooks.
- **Strict Human Hold Points:** Pilot batch procurement and commercial chemical recipe freezing remain held under Gate G-A pending actual tenderometer validation of the Tanzanian grain lot.
- **Deliverable Integrity:** All 80 core engineering documents, CAD models, drawing packages, and verification test scripts are cryptographically hashed and locked under SHA-256 manifests.

---

## 11. REGULATORY, CODE & STATUTORY COMPLIANCE MATRIX

| Regulatory Body / Standard | Title & Scope | FinnoaQ Engineering Compliance Measure | Status |
| :--- | :--- | :--- | :---: |
| **TBS (Tanzania Bureau of Standards)** | TZS 438: Pulses Specification | Moisture $\le 10.5\%$, inorganic matter $<0.1\%$, zero chemical residue | **Compliant** |
| **Codex Alimentarius** | CODEX STAN 152-1985 / 192-1995 | Food-grade tri-sodium citrate (INS 331iii) and sodium carbonate (INS 500i) approved as processing aids | **Compliant** |
| **ASME Sec VIII Div 1** | Boiler and Pressure Vessel Code | Jacketed vessel wall thickness $6.0\text{ mm}$ (calculated min $2.84\text{ mm}$), dished heads, 3.5 bar g relief | **Compliant** |
| **NFPA 68 / NFPA 652** | Combustible Dust Explosion Venting | Cyclone and fluid bed dryer fitted with composite explosion vents ($0.763\text{ m}^2$) venting safely outdoors | **Compliant** |
| **OSHA 29 CFR 1910.29** | Walking-Working Surfaces & Railings | Mezzanine 42" handrails, continuous full-height staircase ($Y=0$ to $+4.2\text{ m}$), 4" toeboards | **Compliant** |
| **IS 800:2007** | General Construction in Steel | ISMB 300 columns, side-bay X-bracing, deflection $< L/500$ under full hydrostatic flood | **Compliant** |
| **IEC 61511 / ISA-84** | Functional Safety / Safety Instrumented Systems | SIF-101 and SIF-103 engineered to SIL-2 targets ($PFD < 0.01$) with redundant fail-safe trips | **Compliant** |
| **ISO 22000 / HACCP** | Food Safety Management System | 5-tier hygienic zoning layout, physical airlocks, sanitary CIP washdown lines | **Compliant** |

---

## 12. CONCLUSION & INVITATION TO PARTNER

The FinnoaQ 15 TPD Greenfield Facility represents an exceptional combination of robust, proven industrial engineering, compelling market economics, and transformative food processing technology. By solving the persistent Hard-to-Cook defect of East African pigeon peas at an industrial scale, FinnoaQ unlocks substantial domestic and international export margins while delivering a rapid capital payback of 28 months and an unlevered project IRR of 34.2%.

Institutional investors and commercial off-take partners are invited to review the complete Front-End Engineering Design package, inspect the SolidWorks native digital twins, and participate in the commercial deployment of this milestone agro-industrial facility.

---
*For technical inquiries or investor due diligence access, contact the Engineering Directorate, FinnoaQ Agro-Industrial Technologies Ltd.*  
*All engineering models and calculations verified under Engineering Baseline Rev 2.0.*
