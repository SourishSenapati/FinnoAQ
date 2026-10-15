# CUSTOM MACHINE DESIGN DOSSIERS (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-006  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Custom Machine & Mechanical Design  

---

## 1. Machine Dossier 1: Jacketed Soak & Contact Tank (`TK-101A/B`)

### 1.1 Duty Statement & Operating Envelope
- **Equipment Tag:** `TK-101A` and `TK-101B` (2 identical parallel vessels).
- **Service:** Batch contacting of dry Tanzanian split pigeon pea with 0.50% w/w sodium bicarbonate liquor at 1:1.5 mass ratio for exactly 30 minutes at 28°C.
- **Batch Cycle Timing:** 15 min dry feed & liquor filling $\rightarrow$ 30 min gentle soak $\rightarrow$ 15 min slurry pump-out $\rightarrow$ 60 min total cycle per tank (alternating sequence ensures continuous line flow).
- **Capacity:** $937.5\text{ kg}$ dal $+ 1,406.3\text{ kg}$ liquor = $2,343.8\text{ kg}$ total batch mass ($2.53\text{ m}^3$ working slurry). Gross vessel volume: $3.86\text{ m}^3$ (fill fraction $65.5\%$).

### 1.2 Mechanical Construction & Materials
- **Design Code:** ASME Section VIII Div 1 (Unfired Pressure Vessels) + EHEDG Doc 8 (Hygienic Equipment Design).
- **Shell:** Internal Diameter $1,600\text{ mm}$, Straight Height $1,920\text{ mm}$, Plate Thickness $4.0\text{ mm}$ SS316L.
- **Heads:** Deep torispherical dished top and bottom heads ($4.0\text{ mm}$ SS316L plate).
- **Jacket:** External SS304 dimple jacket on straight shell ($2.5\text{ bar(g)}$ rating, $1.5\text{ m}^3\text{/h}$ hot/cold water circulation).
- **Surface Finish:** All internal food-contact surfaces mechanically ground and electropolished to $Ra \le 0.8\mu\text{m}$ (Mirror finish, sanitary grade).
- **Support:** 4 nos $100\text{ mm}$ NB Schedule 40 SS304 pipe legs with adjustable stainless leveling footplates and neoprene vibration pads.

### 1.3 Nozzle Schedule (`TK-101A/B`)
- **N1 (DN50 Tri-Clamp):** Dal Grain Feed Chute (from `GF-101`).
- **N2 (DN32 Tri-Clamp):** 0.5% NaHCO3 Chemical Liquor Inlet (from `P-100`).
- **N3 (DN80 Flush Bottom):** Slurry Discharge Port with pneumatic flush-bottom seat valve (zero dead leg).
- **N4 (DN50 Tri-Clamp):** Dual 360° rotating CIP spray ball supply header.
- **N5 (DN50 Flanged):** Sanitary tank breather vent with $0.2\mu\text{m}$ hydrophobic PTFE filter.
- **N6 (DN40 Flanged):** Non-contact radar level transmitter (`LT-101`).
- **N7 (DN25 Tri-Clamp):** Sanitary thermowell with RTD Pt100 (`TT-101`).
- **N8 (DN25 Tri-Clamp):** Retractable sanitary glass electrode pH transmitter (`pHT-101`).

---

## 2. Machine Dossier 2: Low-Shear Hydrofoil Agitator (`AG-101A/B`)

### 2.1 Duty Statement & Fluid Mechanics
- **Equipment Tag:** `AG-101A` and `AG-101B`.
- **Service:** Uniform suspension of split dal cotyledons in chemical liquor without mechanical fracturing, cleavage, or erosion of edges.
- **Impeller Type:** High-efficiency 3-blade axial marine hydrofoil (laser-profiled blades).
- **Impeller Diameter:** $D = 600\text{ mm}$ ($D/T = 0.375$).
- **Operating Speed:** $35.0\text{ rpm}$ ($v_{tip} = 1.10\text{ m/s}$, strictly below the $1.50\text{ m/s}$ pulse damage threshold).
- **Motor & Drive:** $2.20\text{ kW}$ (3.0 HP), 415V, 3-phase, 50 Hz, TEFC IP66 motor coupled to an inline helical gearbox (Ratio 41:1, Output torque $600.2\text{ N}\cdot\text{m}$, Service Factor 2.8).

### 2.2 Shaft & Mechanical Seal Engineering
- **Shaft Material:** Solid round bar SS316L, Diameter $\mathbf{60.0\text{ mm}}$, Overhang Length $2,000\text{ mm}$.
- **Torsional Equivalent Moment:** $T_e = 1,664.5\text{ N}\cdot\text{m}$ (ASME shaft design formula, safety factor $SF = 1.67$ on fatigue, $>3.2$ on yield).
- **Mechanical Seal:** Top-entry dry-running sanitary mechanical seal with food-grade carbon/silicon carbide faces and EPDM FDA O-rings.
- **Internal Steady Bearing:** Bottom tripod spider with food-grade Virgin PTFE/PEEK bushing located in dished head apex restricts tip deflection to $<0.50\text{ mm}$.

---

## 3. Machine Dossier 3: Continuous Vibrating Fluid-Bed Dryer (`DR-101 / CLR-101`)

### 3.1 Duty Statement & Thermal Performance
- **Equipment Tag:** `DR-101` (Drying Zone) and `CLR-101` (Cooling Zone).
- **Service:** Continuous gentle dehydration of soaked Tanzanian split dal from $27.79\%$ to $10.00\%$ moisture (w.b.) at a throughput of $1,304.3\text{ kg/h}$ wet feed ($1,046.4\text{ kg/h}$ dried product).
- **Water Evaporation Capacity:** $257.97\text{ kg H2O/h}$ ($3,695\text{ kg/day}$).
- **Gross Heat Load:** $288.4\text{ kW}$ (Steam consumption $482.8\text{ kg/h}$ at $2.5\text{ bar(g)}$ saturated).
- **Operating Temperatures:** Inlet Air $60.0^\circ\text{C}$, Exhaust Air $42.0^\circ\text{C}$, Exit Grain $<30.0^\circ\text{C}$.

### 3.2 Mechanical Sizing & Fluidization Geometry
- **Bed Dimensions:** Width $1,000\text{ mm}$, Drying Length $4,500\text{ mm}$, Cooling Length $1,500\text{ mm}$ (Total active bed area $\mathbf{6.00\text{ m}^2}$).
- **Distributor Plate:** $2.5\text{ mm}$ SS316L perforated plate with $1.5\text{ mm}$ round holes at $5.0\text{ mm}$ triangular pitch ($8.2\%$ free open area), directional airflow louvers prevent dal backflow.
- **Fluidizing Air Flow:** $7,605\text{ m}^3\text{/h}$ primary heated air ($u = 1.34\text{ m/s}$ superficial velocity, $u_{mf} = 1.17\text{ m/s}$) $+ 2,500\text{ m}^3\text{/h}$ filtered cooling air.
- **Vibration Drive:** Dual self-synchronizing unbalanced vibratory motors ($2 \times 1.50\text{ kW}$, 960 rpm) mounted at 45° attack angle impart gentle micro-hop conveying motion ($0.05\text{ m/s}$ bed travel speed).
- **Casing & Insulation:** SS316L wetted trough, SS304 external cladding with $50\text{ mm}$ high-density rockwool insulation ($k = 0.038\text{ W/m}\cdot\text{K}$) limits exterior skin temperature to $<40^\circ\text{C}$.
- **Vibration Isolation:** 8 nos heavy-duty coil springs isolate $96\%$ of dynamic vibratory loads from the building floor slab.

---

## 4. Machine Dossier 4: Vibratory Dewatering Screen Deck (`VS-101`)

### 4.1 Duty Statement & Solids Recovery
- **Equipment Tag:** `VS-101`.
- **Service:** High-speed separation of soaked dal grains from spent chemical liquor following batch dump from `TK-101A/B`.
- **Feed Rate:** $2,343.8\text{ kg}$ slurry dumped over 10 minutes ($14.0\text{ TPH}$ instantaneous hydraulic surge).
- **Screen Media:** SS316L profiled wedge-wire deck, slot aperture $\mathbf{1.00\text{ mm}}$, width $900\text{ mm}$, length $2,200\text{ mm}$ (Deck area $1.98\text{ m}^2$).
- **Integrated Spray Header:** 6 nos flat-fan sanitary spray nozzles delivering potable mist rinse ($2,250\text{ kg/day}$, $0.15:1$ water-to-dal ratio) to wash off surface sodium bicarbonate film before dal enters the dryer.
- **Drive:** Dual counter-rotating vibratory motors ($2 \times 0.75\text{ kW}$, 1440 rpm) producing linear conveying motion at 5° uphill incline to maximize dewatering drainage time.
- **Fines Retention:** Dal grain thickness is $2.2\text{ mm} > 1.0\text{ mm}$ slot; screen guarantees $>99.75\%$ retention of whole and split grains.
