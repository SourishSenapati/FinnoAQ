# Professional Equipment Engineering Data Sheets (Rev V3.0)
## 15,000 kg/day Incoming-Feed Toor-Dal Greenfield Processing Plant

> [!IMPORTANT]
> **Engineering Phase:** `CONCEPTUAL FRONT-END ENGINEERING DESIGN (FEED)`  
> **Document Identifier:** `EDS-FIN-15T-V3-001`  
> **Governing Standards:** ASME Sec VIII Div 1, IS 2825, API 650, TEMA C, ISA-5.1, FSSAI 2011  
> **Stamping:** `CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`  
> **Lot Identifier:** `PENDING_COMMERCIAL_LOT_ID` | **Gate Status:** `GATE G-A HOLD ACTIVE`

---

## 1. Equipment Data Sheet: TK-101A / TK-101B (Sanitary Soak Vessels)

| Parameter Category | Specification / Engineering Value | Design Standard / Compliance |
| :--- | :--- | :--- |
| **Equipment Tag / Name** | `TK-101A` / `TK-101B` (Dual Alternating Soak Vessels) | P&ID Sheet `DWG-FIN-15T-003` |
| **Quantity Installed** | 2 Units (1 Operating, 1 Filling/Discharging/CIP) | 100% Operational Duty Rotation |
| **Vessel Type & Orientation** | Vertical Cylindrical, Dished Top Head, 45° Conical Bottom | ASME Sec VIII Div 1 / IS 2825 Class 2 |
| **Vessel Dimensions** | Outside Diameter: $2,000\text{ mm}$ (Inside: $1,988\text{ mm}$)<br>Straight Shell Height: $2,200\text{ mm}$<br>Conical Bottom Height: $500\text{ mm}$<br>Top Head Crown Height: $300\text{ mm}$<br>Overall Height (incl. legs & agitator stool): $3,855\text{ mm}$ | General Arrangement `DWG-FIN-15T-006` |
| **Process Capacities** | Gross Geometric Volume: $6.83\text{ m}^3$ fluid capacity ($7.50\text{ m}^3$ envelope)<br>Working Batch Volume: $5.12\text{ m}^3$ (at 75% liquid fill level)<br>Design Operating Freeboard: $550\text{ mm}$ ($25.0\%$ vapor space) | Reconciled in `V3_BALANCE_AND_COST_RECONCILIATION.md` |
| **Operating Conditions** | Operating Fluid: Split Dal Granular Slurry in 0.50% $NaHCO_3$ liquor<br>Slurry Density: $1,150\text{ kg/m}^3$<br>Operating Pressure: Atmospheric (Static liquid head $0.27\text{ bar}$)<br>Operating Temperature: $25.0^\circ\text{C}$ to $40.0^\circ\text{C}$ (Ambient / Controlled) | Process Flow Diagram `DWG-FIN-15T-002` |
| **Mechanical Design Limits** | Internal Design Pressure: Full Vacuum (FV) to $1.50\text{ bar g}$<br>Design Temperature: $100.0^\circ\text{C}$ (Sanitary Steam/CIP sterilisation)<br>Hydrostatic Test Pressure: $2.25\text{ bar g}$ ($1.5 \times P_{\text{design}}$) | ASME Code Case 2286-1 |
| **Material of Construction (MOC)** | Shell, Heads & Conical Bottom: SS316L (ASTM A240 Gr 316L)<br>Wetted Contact Surface Finish: Electro-polished $R_a \le 0.8\mu\text{m}$ (Sanitary 3A)<br>External Shell Finish: 2B Mill finish, pickled and passivated<br>Legs & Support Structure: SS304 Schedule 40 Pipe with Base Plates | FDA 21 CFR 177 / FSSAI Schedule 4 |
| **Component Wall Thicknesses** | Cylindrical Straight Shell: $6.0\text{ mm}$ ($5.0\text{ mm}$ calc + $1.0\text{ mm}$ CA)<br>Top Dished Head: $6.0\text{ mm}$ torispherical<br>Conical Bottom: $6.0\text{ mm}$ reinforced apex<br>Corrosion Allowance: $0.0\text{ mm}$ (Food grade stainless steel) | Welded joint efficiency $E = 0.85$ (Spot X-Ray) |
| **Internal Components** | 4× Anti-Swirl Baffles: $160\text{ mm}$ width ($D/12$), SS316L 6mm plate, full seal welded with $25\text{ mm}$ stand-off gap for sanitary drainage. | Prevents deep vortexing at 55 RPM |
| **Support & Civil Interface** | 4× Tubular Support Legs ($\phi 168\text{ mm}$ SS304) with gusset pads.<br>Footplates: $350 \times 350 \times 25\text{ mm}$ with 4× M24 anchor bolts.<br>Fitted with stainless steel shear-beam electronic load cells (`WIT-101A/B`). | Foundation static operating load: $8,309\text{ kg}$<br>Hydrotest load: $9,250\text{ kg}$ |
| **Weights Summary** | Empty Tare Weight: $809.0\text{ kg}$ (Vessel shell + cone + legs)<br>Agitator Drive Weight: $320.0\text{ kg}$<br>Operating Liquid/Slurry Weight: $7,180.0\text{ kg}$<br>Total Operating Weight: $\mathbf{8,309.0\text{ kg}}$ | Civil Base Load Schedule |

### Nozzle Schedule: TK-101A/B
- **N1 (20" / 500mm):** Hinged Sanitary Manway with sight glass and safety limit switch (Top Head, 45°).
- **N2 (4" / 100mm):** Split Dal Granular Feed Inlet, ANSI 150# RF / Tri-Clamp (Top Head, 180°).
- **N3 (3" / 80mm):** Softened Process Water Supply Inlet, ANSI 150# RF (Top Head, 270°).
- **N4 (1.5" / 40mm):** Chemical Dosing Reagent Inlet, ANSI 150# RF (Top Head, 90°).
- **N5 (2" / 50mm):** CIP Rotary Spray Ball Connection, Tri-Clamp (Top Head Center).
- **N6 (3" / 80mm):** Vessel Breathing Vent with 0.22 $\mu$m PTFE Sterile Filter, Tri-Clamp (Top Head, 135°).
- **N7 (2" / 50mm):** Pressure Relief Valve / Rupture Disc Flange, ANSI 150# RF (Top Head, 225°).
- **N8 (2" / 50mm):** Guided Wave Radar Continuous Level Transmitter, ANSI 150# RF (Top Head, 315°).
- **N9 (1" / 25mm):** Duplex PT100 RTD Thermowell, ANSI 150# RF (Lower Shell, 90°).
- **N10 (6" / 150mm):** Conical Bottom Slurry Drain Nozzle with Flush Bottom Valve, ANSI 150# RF (Bottom Center).
- **N11 (3" / 80mm):** Emergency Vessel Overflow Line to ETP, ANSI 150# RF (Top Shell, 0°).

---

## 2. Equipment Data Sheet: DR-101 (Continuous Vibrating Fluid Bed Dryer)

| Parameter Category | Specification / Engineering Value | Design Standard / Compliance |
| :--- | :--- | :--- |
| **Equipment Tag / Name** | `DR-101` (Continuous Vibrating Fluid Bed Dryer & Cooler) | P&ID Sheet `DWG-FIN-15T-004` |
| **Manufacturer / Reference Type** | GEA / Buhler Industrial Sanitary Vibrating Fluid Bed Dryer | Continuous plug-flow vibratory deck |
| **Drying Deck Dimensions** | Effective Deck Length: $14,000\text{ mm}$ ($14.0\text{ m}$)<br>Effective Deck Width: $1,000\text{ mm}$ ($1.0\text{ m}$)<br>Total Active Heat Transfer Area: $\mathbf{14.00\text{ m}^2}$ | Sizing envelope derived from drying kinetics |
| **Overall Trough Dimensions** | Trough Length: $14,000\text{ mm}$ | Width: $1,500\text{ mm}$ overall<br>Lower Plenum Depth: $600\text{ mm}$ | Upper Hood Freeboard: $800\text{ mm}$<br>Overall Height (incl. springs & exhaust hoods): $2,750\text{ mm}$ | General Arrangement `DWG-FIN-15T-007` |
| **Process Throughput & Moisture** | Wet Dal Feed Rate: $18,590.0\text{ kg/day}$ ($1,161.9\text{ kg/h}$ over 16h; $1,366.9\text{ kg/h}$ des)<br>Feed Moisture Content: $28.7735\%$ wet basis ($0.404\text{ kg H2O/kg solids}$)<br>Dried Product Discharge: $14,712.22\text{ kg/day}$ ($919.5\text{ kg/h}$ nom; $1,081.8\text{ kg/h}$ des)<br>Discharge Moisture: $10.0000\%$ wet basis ($0.111\text{ kg H2O/kg solids}$)<br>Water Evaporation Duty: $\mathbf{3,877.78\text{ kg H2O/day}}$ ($\mathbf{285.13\text{ kg/h}}$ effective design rate) | Reconciled in `V3_BALANCE_AND_COST_RECONCILIATION.md` |
| **Air Handling & Psychrometrics** | Process Air Flow Rate: $16,100\text{ kg/h}$ dry air ($13,500\text{ m}^3/\text{h}$ @ 85°C)<br>Fluidizing Air Face Velocity: $1.15\text{ m/s}$ to $1.35\text{ m/s}$ ($u_{\text{op}} / u_{\text{mf}} \approx 1.25$)<br>Inlet Air Temperature: $85.0^\circ\text{C}$ (controlled via steam battery `HE-101`)<br>Exhaust Air Temperature: $60.0^\circ\text{C}$ to $65.0^\circ\text{C}$ (Wet-bulb $60.0^\circ\text{C}$)<br>Exhaust Air Relative Humidity: $82.0\%$ to $86.0\%$ RH | Aspen Plus V14 / ASME Steam Tables |
| **Thermal Energy Duty** | Net Evaporation Heat Duty: $198.33\text{ kW}$<br>Air Preheating Duty (30°C to 85°C): $247.20\text{ kW}$<br>Design Thermal Duty (with 15% system losses): $\mathbf{512.36\text{ kW}}$ ($\mathbf{440,600\text{ kcal/h}}$)<br>Steam Consumption: $520.0\text{ kg/h}$ average ($864.6\text{ kg/h}$ peak startup) @ 3.0 bar g | Sized for 600 kg/h IBR Boiler `BL-101` |
| **Vibratory Drive & Excitation** | Drive Type: Twin Unbalanced Electric Vibratory Exciter Motors (Contra-rotating)<br>Motor Rating: 2× $5.5\text{ kW}$, 415V, 50Hz, 4-Pole, IP66, Inverter Duty<br>Excitation Frequency: $16.0\text{ Hz}$ ($960\text{ RPM}$)<br>Vibration Stroke Amplitude: $\pm 3.5\text{ mm}$ to $\pm 4.0\text{ mm}$ at $45^\circ$ forward throw angle | Fluidized conveyance velocity $v_{\text{bed}} \approx 0.08\text{ m/s}$ |
| **Vibration Isolation System** | 12× Heavy-Duty Coil Spring Isolator Stations (6 pairs along trough sides)<br>Static Deflection: $35.0\text{ mm}$ | Spring Stiffness: $185\text{ N/mm}$ to $240\text{ N/mm}$<br>Dynamic Isolation Efficiency: $> 95.5\%$ transmissibility reduction to civil floor | Prevents structural building resonance |
| **Explosion Protection & Safety** | 2× Flanged Explosion Relief Panels (Rupture vents) on expansion hood roof<br>Vent Area: $0.85\text{ m}^2$ per panel | Static Burst Pressure: $0.10\text{ bar g}$ ($10\text{ kPa}$)<br>Compliant with NFPA 68 / VDI 3673 for St-1 agricultural pulse dust | Explosion vent ducted to safe outdoor roof area |
| **Materials of Construction** | Product Contact Trough & Deck: SS316L ($4.0\text{ mm}$ sheet, $R_a \le 0.8\mu\text{m}$)<br>Perforated Deck: SS316L directional Conidrur / slotted deck ($1.2\text{ mm}$ slots)<br>Lower Air Plenum: SS316L ($4.0\text{ mm}$ sheet metal)<br>Sub-frame & Structural Girders: Hot-Dip Galvanised Structural Carbon Steel | Sanitary food contact finish |
| **Weights Summary** | Vibrating Machine Tare Weight: $2,850\text{ kg}$ (Trough, plenum, deck, exciters)<br>Grain Bed Live Operating Weight: $1,450\text{ kg}$ (mean bed depth $85\text{ mm}$)<br>Total Dynamic Vibrating Weight: $\mathbf{4,300\text{ kg}}$<br>Concrete Foundation Inertia Block Mass: $13,000\text{ kg}$ ($3.0\times$ machine mass) | Civil Foundation Dynamic Schedule |

---

## 3. Equipment Data Sheet: SK-100 (Automated Chemical Dosing Skid)

| Parameter Category | Specification / Engineering Value | Design Standard / Compliance |
| :--- | :--- | :--- |
| **Equipment Tag / Name** | `SK-100` (Pre-Packaged Automated Chemical Dosing Skid) | P&ID Sheet `DWG-FIN-15T-003` |
| **Dosing Chemical Reagent** | Food-Grade Sodium Bicarbonate ($NaHCO_3$, E500ii / IS 2124)<br>Solution Concentration: $0.50\%\text{ w/w}$ (or $5.0\text{ g/L}$ in softened water)<br>Reagent Purity: $\ge 99.0\%$ Food Grade | FSSAI Food Additive Compendium |
| **Skid Dimensions & Structure** | Length: $3,000\text{ mm}$ | Width: $1,500\text{ mm}$ | Height: $1,600\text{ mm}$ overall<br>Frame Material: ISMC 150 Structural Steel Channels, Hot-Dip Galvanised ($85\mu\text{m}$)<br>Containment Bund: Integral SS304 drip tray with $50\text{ mm}$ raised bund lip ($225\text{ L}$ capacity) | General Arrangement `DWG-FIN-15T-008` |
| **Chemical Mixing Tanks** | 2 Units (`TK-103A` and `TK-103B`), each $500\text{ L}$ capacity<br>Material: UV-stabilized virgin food-grade High-Density Polyethylene (HDPE)<br>Features: Graduated visual level scale, quick-opening hinged charging hatch, low-level sensor | Dual batch preparation: 1 mixing, 1 dosing |
| **Skid Mixers (`AG-103A/B`)** | 2 Units, Top-mounted electric direct-drive mixers<br>Motor Rating: $0.37\text{ kW}$, 415V, 3-Phase, 50Hz, IP55, 280 RPM<br>Shaft & Impeller: SS316L, 3-blade marine propeller ($\phi 200\text{ mm}$) | Fast dissolving of $NaHCO_3$ powder |
| **Metering Pumps (`P-102A/B`)** | 2 Units (1 Duty, 1 Standby with automated changeover)<br>Pump Type: Positive Displacement Mechanically Actuated Diaphragm Metering Pump<br>Liquid End Material: PVDF / PTFE Diaphragm with Ceramic Double Ball Valves<br>Design Flow Capacity: $25.0\text{ L/h}$ @ $5.0\text{ bar g}$ (Operating: $7.03\text{ L/h}$ average)<br>Turn-down Ratio: $10:1$ via micrometer manual stroke + $4-20\text{ mA}$ VFD speed control | Sized for Basis A ($112.5\text{ kg/day}$ peak) |
| **Manifold & Instrumentation** | Suction Y-Strainers (SS316L, 40 mesh basket)<br>Calibration Column ($1,000\text{ mL}$ borosilicate glass with 3-way valves)<br>Bladder Pulsation Dampener ($0.5\text{ L}$ SS316L body with Viton bladder)<br>Back Pressure Valve (Set @ $1.5\text{ bar g}$) & External Pressure Relief Valve (Set @ $3.5\text{ bar g}$)<br>Electromagnetic Flowmeter (`FIT-102`, PFA lined, DN15, 4-20mA HART) | Prevents siphoning and flow pulsing |
| **Local Control Panel (`LCP-100`)** | Enclosure: SS304 IP65, front-door mounted HOA switches, run/trip indication lamps, emergency stop pushbutton, and multi-color beacon stack. | Interfaced to plant PLC via Profinet |

---

## 4. Equipment Data Sheet: AG-101A / AG-101B (Low-Shear Hydrofoil Agitators)

| Parameter Category | Specification / Engineering Value | Design Standard / Compliance |
| :--- | :--- | :--- |
| **Equipment Tag / Name** | `AG-101A` / `AG-101B` (Top-Entry Low-Shear Slurry Agitators) | Mounted on `TK-101A/B` Top Head |
| **Quantity Installed** | 2 Units (1 mounted per soak vessel) | Process Flow Diagram `DWG-FIN-15T-002` |
| **Agitator Drive Motor** | SEW-Eurodrive / Nord Helical-Bevel Geared Motor Unit<br>Motor Rating: $4.0\text{ kW}$, 415V, 3-Phase, 50Hz, IE3 Premium Efficiency, IP66<br>Operating Output Speed: $55\text{ RPM}$ (Variable speed range $30\text{ RPM}$ to $70\text{ RPM}$ via VFD)<br>Service Factor: $1.80$ continuous industrial duty | Low power dissipation ($P/V \approx 0.65\text{ kW/m}^3$) |
| **Shaft & Mounting Stool** | Solid Precision-Ground Shaft: $\phi 60.0\text{ mm}$ SS316L, Length $2,400\text{ mm}$<br>Shaft Straightness: $< 0.1\text{ mm/m}$ | Critical Speed Ratio: $N_{\text{op}} / N_{\text{crit}} < 0.60$<br>Mounting Stool: Cast ductile iron lantern stool ($\phi 450\text{ mm}$ flange ANSI 150#) | Prevents shaft whip and seal wear |
| **Shaft Sealing System** | Cartridge-type Double Mechanical Seal with food-grade sanitary water flush barrier.<br>Seal Faces: Silicon Carbide vs Carbon (Product side), Carbon vs Ceramic (Atmospheric side)<br>Barrier Fluid: Sterile demineralised water @ $1.0\text{ bar g}$ over vessel pressure | Zero batch cross-contamination |
| **Impeller Geometry & Shear** | Impeller Type: High-Efficiency 3-Blade Axial Hydrofoil (Lightnin A310 / Chemineer HE-3 type)<br>Swept Impeller Diameter: $\mathbf{\phi 700\text{ mm}}$ ($D/T = 700 / 2000 = 0.35$)<br>Impeller Tip Speed: $v_{\text{tip}} = \pi \times 0.70\text{ m} \times (55/60) = \mathbf{2.01\text{ m/s}}$ (Limited to $< 1.8\text{ m/s}$ during grain residence)<br>Flow Number: $N_q = 0.56$ | Power Number: $N_p = 0.38$<br>Pumping Rate: $Q = N_q \times N \times D^3 = 0.56 \times (55/60) \times (0.70)^3 = \mathbf{0.176\text{ m}^3\text{/s}}$ ($634\text{ m}^3\text{/h}$) | High axial turnover with minimum shear to prevent dal splitting |
