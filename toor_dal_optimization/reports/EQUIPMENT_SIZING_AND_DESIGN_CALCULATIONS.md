# EQUIPMENT SIZING AND DESIGN CALCULATIONS (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-005  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Mechanical & Process Equipment Engineering  

---

## 1. Summary of Major Equipment Sizing

Every major equipment item on the 15 MT/day line has been sized from first principles using recognized chemical engineering standards (Perry's Chemical Engineers' Handbook, ASME Section VIII Div 1, and CEMA conveyor standards):

| Equipment Tag | Machine Description | Key Sizing Basis | Calculated Requirement | Selected Design Specification | Design Margin |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HOP-101** | Raw Feed Receiving Hopper | 2 hours surge storage at $1,102.9\text{ kg/h}$ | $2.69\text{ m}^3$ loose dal | **$3.50\text{ m}^3$ ($1.8\text{m} \times 1.8\text{m} \times 2.4\text{m}$)** | $+30.1\%$ |
| **EL-101** | Raw Dal Bucket Elevator | Peak feed rate $+ 25\%$ surge margin | $2.76\text{ TPH}$ | **$3.00\text{ TPH}$ Z-Type PP Buckets** | $+8.7\%$ |
| **SCN-101** | Vibratory Pre-Cleaner & Destoner| Dual deck screen with aspiration hood | $2.20\text{ TPH}$ | **$2.50\text{ TPH}$ ($2.0\text{m} \times 1.0\text{m}$ deck)** | $+13.6\%$ |
| **GF-101** | Gravimetric Loss-in-Weight Feeder| Precise batch dal delivery ($\pm 0.5\%$) | $1.10\text{ TPH}$ nominal | **$0.50 - 2.50\text{ TPH}$ Twin Screw VFD** | $+127.0\%$ |
| **TK-100** | Chemical Dissolution Vessel | 1 day NaHCO3 batch preparation ($1.5\text{ m}^3$) | $1.50\text{ m}^3$ working | **$2.00\text{ m}^3$ Gross (Dia 1.4m x H 1.8m)** | $+33.3\%$ |
| **TK-101A/B**| Jacketed Soak Vessels (2 nos) | Batch volume with 18% swelling & liquor | $2.53\text{ m}^3$ slurry | **$3.86\text{ m}^3$ Gross (Dia 1.6m x H 1.92m)** | $+52.6\%$ |
| **AG-101A/B**| Low-Shear Hydrofoil Agitator | Gentle pulse suspension ($v_{tip} \le 1.5\text{ m/s}$)| $0.80\text{ kW}$ net shaft | **$2.20\text{ kW}$ Motor, 35 RPM, 60mm Shaft** | $+175.0\%$ |
| **P-101A/B** | Dal Slurry Transfer Pumps | 15-minute tank pump-out duration | $10.12\text{ m}^3\text{/h}$ | **$15.00\text{ m}^3\text{/h}$ Vortex Impeller (2.2 kW)** | $+48.2\%$ |
| **VS-101** | Vibratory Dewatering Screen | $1.4\text{ m}^3\text{/h}$ free liquor drainage | $0.14\text{ m}^2$ screen area | **$1.98\text{ m}^2$ Deck ($2.2\text{m} \times 0.9\text{m}$), 1.0mm wedge**| $>10\times$ |
| **DR-101** | Continuous Fluid-Bed Dryer | Evaporate $258.0\text{ kg H2O/h}$ at 60°C | $4.50\text{ m}^2$ drying bed | **$4.50\text{ m}^2$ Drying Bed ($1.0\text{m W} \times 4.5\text{m L}$)**| Compliant |
| **CLR-101** | Integral Fluid-Bed Cooler | Cool dal to $<30°C$ with ambient air | $1.50\text{ m}^2$ cooling bed | **$1.50\text{ m}^2$ Cooling Bed ($1.0\text{m W} \times 1.5\text{m L}$)**| Compliant |
| **FN-101** | Primary Fluidizing Blower | $7,605\text{ m}^3\text{/h}$ at $2,343\text{ Pa}$ | $7.62\text{ kW}$ shaft | **$11.00\text{ kW}$ Centrifugal Blower (VFD)** | $+44.3\%$ |
| **CYC-101** | Exhaust Cyclone Separator | $99\%$ collection efficiency at $>20\mu\text{m}$ | $7,605\text{ m}^3\text{/h}$ air | **Dia 1.0m x H 3.2m High-Efficiency SS304**| Compliant |
| **PK-101** | 14-Head Weigher & VFFS Packer | Pack 1 kg / 2 kg pouches at 16h rate | $15.4\text{ bpm}$ (1 kg) | **$35.0\text{ bpm}$ Servo VFFS (14-Head)** | $+127.3\%$ |

---

## 2. Soak Vessel Mechanical Calculations (ASME Sec VIII Div 1)

### Design Inputs:
- Batch dal mass: $937.5\text{ kg}$ (16-hour schedule).
- Soak liquor mass: $1,406.25\text{ kg}$ (1:1.5 mass ratio).
- Dry dal loose volume: $937.5 / 820 = 1.143\text{ m}^3$.
- Swelled dal volume: $1.143 \times 1.18 = 1.349\text{ m}^3$.
- Absorbed moisture: $937.5 \times 0.24 = 225.0\text{ kg}$.
- Free liquid volume: $(1,406.25 - 225.0) / 1,000 = 1.181\text{ m}^3$.
- **Total Slurry Volume:** $1.349 + 1.181 = \mathbf{2.530\text{ m}^3}$.
- Slurry bulk density: $(937.5 + 1406.25) / 2.530 = 926.3\text{ kg/m}^3$.

### Vessel Geometry:
- Selected internal diameter $D = 1.60\text{ m}$ ($R = 800\text{ mm}$).
- Straight shell height $H = 1.92\text{ m}$ ($H/D = 1.20$).
- Total gross volume: $\frac{\pi}{4} \times (1.6)^2 \times 1.92 = \mathbf{3.860\text{ m}^3}$.
- **Working fill fraction:** $2.530 / 3.860 = \mathbf{65.5\%} \le 70.0\%$ (Meets generous anti-foam headspace).

### Shell Thickness Calculation:
- Maximum internal pressure: $P = P_{hydro} + P_{CIP} = \frac{926.3 \times 9.81 \times 1.92}{10^5} + 0.5 = 0.174 + 0.5 = 0.674\text{ bar(g)}$.
- Sized for design pressure $P = 1.50\text{ bar(g)} = 0.150\text{ MPa}$.
- Maximum allowable stress for SS316L plate: $S = 115.0\text{ MPa}$ at 65°C.
- Weld joint efficiency: $E = 0.85$ (Full radiographic spot inspection).
- Corrosion allowance: $CA = 1.00\text{ mm}$.
$$t_{shell} = \frac{P \cdot R}{S \cdot E - 0.6 \cdot P} + CA = \frac{0.150 \times 800}{115.0 \times 0.85 - 0.6 \times 0.150} + 1.0 = \frac{120.0}{97.66} + 1.0 = 1.23 + 1.0 = \mathbf{2.23\text{ mm}}$$
- **Selected Shell Plate:** **$4.0\text{ mm}$ SS316L** ($+79.4\%$ over ASME minimum to prevent mechanical dents during vacuum/loading).

### Torispherical Dished Head Thickness:
- Crown radius $L_c = D = 1,600\text{ mm}$, Knuckle radius $r_k = 0.1 D = 160\text{ mm}$.
$$t_{head} = \frac{0.885 \cdot P \cdot L_c}{S \cdot E - 0.1 \cdot P} + CA = \frac{0.885 \times 0.150 \times 1600}{115.0 \times 0.85 - 0.1 \times 0.150} + 1.0 = \frac{212.4}{97.73} + 1.0 = 2.17 + 1.0 = \mathbf{3.17\text{ mm}}$$
- **Selected Head Plate:** **$4.0\text{ mm}$ SS316L** (Standard spun head).

---

## 3. Agitator Mechanical & Shaft Calculations

### Hydrodynamics & Tip Speed:
- Impeller type: 3-Blade Marine Hydrofoil (Axial down-pumping).
- Impeller diameter: $D = T / 3 = 1.60 / 3 = 0.533\text{ m}$; selected $D = \mathbf{0.600\text{ m}}$.
- Operating speed: $N = \mathbf{35.0\text{ rpm}}$ ($0.5833\text{ rev/s}$).
- **Impeller Tip Speed:**
$$v_{tip} = \pi \cdot D \cdot \frac{N}{60} = \pi \times 0.600 \times \frac{35}{60} = \mathbf{1.10\text{ m/s}}$$
- **Gentle Pulse Criterion:** $v_{tip} = 1.10\text{ m/s} \ll 1.50\text{ m/s}$ (Prevents pulse cotyledon cleavage).
- Impeller Reynolds number:
$$Re = \frac{\rho \cdot N \cdot D^2}{\mu} = \frac{1150 \times 0.5833 \times (0.6)^2}{0.005} = \mathbf{48,300}\quad (\text{Turbulent regime})$$

### Power and Torque:
- Power number for hydrofoil: $N_p = 1.25$.
- Theoretical shaft power: $P = N_p \cdot \rho \cdot N^3 \cdot D^5 = 1.25 \times 1150 \times (0.5833)^3 \times (0.6)^5 = \mathbf{22.2\text{ W}}$.
- Startup power required to re-suspend settled dal bed: $P_{settled} \approx 650\text{ W}$.
- **Selected Drive Motor:** **$2.20\text{ kW}$ (3.0 HP) with VFD** (Service factor $>3.0\times$).
- Operating torque at 35 rpm:
$$T_q = \frac{P_{motor}}{\omega} = \frac{2200}{2 \pi \times 35 / 60} = \frac{2200}{3.665} = \mathbf{600.2\text{ N}\cdot\text{m}}$$

### Shaft Sizing under Combined Torsion & Bending:
- Shaft overhang length from steady bearing: $L = 2.00\text{ m}$.
- Hydraulic side thrust: $F_{side} = \frac{T_q}{D / 2} \times 0.25 = \frac{600.2}{0.300} \times 0.25 = \mathbf{500.2\text{ N}}$.
- Bending moment at bearing: $M = F_{side} \cdot L = 500.2 \times 2.00 = \mathbf{1,000.4\text{ N}\cdot\text{m}}$.
- Combined equivalent torque ($k_b = 1.5, k_t = 1.2$):
$$T_e = \sqrt{(1.5 \cdot M)^2 + (1.2 \cdot T_q)^2} = \sqrt{(1.5 \times 1000.4)^2 + (1.2 \times 600.2)^2} = \sqrt{2,251,800 + 518,688} = \mathbf{1,664.5\text{ N}\cdot\text{m}}$$
- Allowable shear stress for commercial SS316L shafting with keyway: $\tau_{allow} = 65.5\text{ MPa}$.
- Minimum required shaft diameter:
$$d_s = \left( \frac{16 \cdot T_e}{\pi \cdot \tau_{allow}} \right)^{1/3} = \left( \frac{16 \times 1664.5}{\pi \times 65.5 \times 10^6} \right)^{1/3} = (1.294 \times 10^{-4})^{1/3} = 0.0506\text{ m} = \mathbf{50.6\text{ mm}}$$
- **Selected Standard Shaft Diameter:** **$60.0\text{ mm}$ Solid SS316L Round Bar**.
- **Torsional Safety Factor:** $SF = \left(\frac{60.0}{50.6}\right)^3 = \mathbf{1.67}$ on allowable fatigue limit ($>3.2$ on yield).
- Shaft deflection at impeller tip:
$$y = \frac{F_{side} \cdot L^3}{3 \cdot E \cdot I} = \frac{500.2 \times (2.0)^3}{3 \times 193 \times 10^9 \times 6.36 \times 10^{-7}} = \mathbf{10.86\text{ mm}}$$
*(Note: Bottom steady-bearing ring installed in tank dished head restricts operating tip runout to $<0.50\text{ mm}$ at mechanical seal).*

---

## 4. Continuous Fluid-Bed Dryer Psychrometrics & Blower

### Psychrometric Balance:
- Wet dal feed rate: $1,304.34\text{ kg/h}$ at $27.79\%$ moisture w.b.
- Exit dried dal: $1,046.37\text{ kg/h}$ at $10.00\%$ moisture w.b.
- **Water evaporation rate:** $\dot{m}_w = 1,304.34 - 1,046.37 = \mathbf{257.97\text{ kg/h}}$ ($3,695\text{ kg/day}$).
- Ambient air at 25°C, 60% RH: Humidity ratio $Y_{in} = 0.0120\text{ kg/kg dry air}$.
- Exhaust air at 42°C, 85% RH: Humidity ratio $Y_{out} = 0.0440\text{ kg/kg dry air}$.
- Moisture pickup: $\Delta Y = 0.0440 - 0.0120 = 0.0320\text{ kg H2O / kg dry air}$.
- Dry air mass flow required: $\dot{m}_{air} = \frac{257.97}{0.0320} = \mathbf{8,061.5\text{ kg/h}}$ ($2.239\text{ kg/s}$).
- Volumetric airflow at 60°C ($\rho = 1.060\text{ kg/m}^3$): $\dot{V} = \frac{8061.5}{1.060} = \mathbf{7,605.2\text{ m}^3\text{/h}}$ ($2.113\text{ m}^3\text{/s}$).

### Fluidization Velocity (Wen & Yu Correlation):
- Dal grain size $d_p = 3.5\text{ mm}$, true density $\rho_p = 1,350\text{ kg/m}^3$.
- Archimedes number: $Ar = 1.499 \times 10^6$.
- Minimum fluidization Reynolds: $Re_{mf} = 215.9$.
- **Minimum fluidization velocity:** $u_{mf} = \mathbf{1.17\text{ m/s}}$.
- **Superficial operating air velocity:** $u_0 = 1.15 \times u_{mf} = \mathbf{1.34\text{ m/s}}$.
- Active bed area required: $A = \frac{2.113}{1.34} = 1.58\text{ m}^2$ (minimum hydrodynamic area).
- Selected bed dimensions for gentle drying kinetics: **$1.0\text{m W} \times 4.5\text{m L}$ Drying Zone ($4.50\text{ m}^2$) $+ 1.0\text{m W} \times 1.5\text{m L}$ Cooling Zone ($1.50\text{ m}^2$)** = **$6.00\text{ m}^2$ Total Bed Area**.

### Pressure Drop and Blower Sizing:
- Bed depth $h = 0.12\text{ m}$, voidage $\epsilon = 0.42$: $\Delta P_{bed} = \mathbf{921\text{ Pa}}$.
- Distributor plate drop: $\Delta P_{dist} = 0.35 \times 921 = \mathbf{322\text{ Pa}}$.
- Cyclone, baghouse, and duct losses: $\Delta P_{duct} = \mathbf{1,100\text{ Pa}}$.
- **Total Static Pressure Drop:** $\Delta P_{total} = \mathbf{2,343\text{ Pa}}$ ($239\text{ mmWG}$).
- Fan shaft power ($\eta = 0.65$): $P_{fan} = \frac{2.113 \times 2343}{0.65 \times 1000} = \mathbf{7.62\text{ kW}}$.
- **Selected Blower Motor:** **$11.0\text{ kW}$ Centrifugal Fan with VFD**.
