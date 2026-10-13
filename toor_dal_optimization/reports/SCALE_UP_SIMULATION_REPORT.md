# HARAKUTIR INDUSTRIAL SCALE-UP SIMULATION REPORT
## 5.0 Tonnes/Hour Continuous Line — Mass Balances, Thermal Duties & Unit Operations

**Document ID:** HKT-SCL-2026-010  
**Version:** 3.0.0  
**Target Industrial Capacity:** $5.0\text{ Tonnes / Hour}$ ($30,000\text{ Tonnes / Year}$)  
**Selected Technology:** Continuous Tempering + Catalytic Infrared Radiant Tunnel + Counter-Flow Fluidized-Bed Dryer  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Process Flow Diagram (PFD) & Unit Operations Sequence

```
[Raw Tanzanian Split Dal Storage Silo]
                 |
                 v
[1. Feed Hopper & Vibratory Feeder] (5,000 kg/hr, 10.5% moisture wb)
                 |
                 v
[2. Continuous Tempering Screw] <---- [Potable Misting Water] (175 kg/hr, +3.5% wb)
                 |
                 v
[3. Catalytic Infrared Tunnel] <----- [Radiant Flux @ 185°C, 45 seconds residence]
                 |                     (Flashes off 75 kg/hr surface moisture, induces micro-fissuring)
                 v
[4. Fluidized-Bed Counter-Flow Dryer] <- [Heated Drying Air @ 50°C, 1.2 m/s]
                 |                        (Evaporates 125.7 kg/hr, brings final moisture to 10.0% wb)
                 v
[5. Counter-Flow Air Cooling Bed] ---> [Cyclone & Dust Filtration] (22.5 kg/hr fines collected)
                 |
                 v
[6. Finished Quick-Cooking Dal Packing] (4,951.8 kg/hr finished saleable product)
```

---

## 2. Rigorous Mass & Energy Balances

### 2.1 Mass Balance (Basis: 1 Hour of Continuous Operation)
* **Raw Feed Inflow:** $5,000.0\text{ kg/hr}$ at $10.5\%$ moisture w.b.
  - Dry matter: $4,475.0\text{ kg/hr}$
  - Moisture: $525.0\text{ kg/hr}$
* **Tempering Water Added:** $175.0\text{ kg/hr}$ potable water ($+3.5\%$ loading)
  - Tempered mass: $5,175.0\text{ kg/hr}$ at $13.53\%$ moisture w.b.
* **Infrared Surface Evaporation:** $75.0\text{ kg/hr}$ moisture flashed off
  - Mass entering dryer: $5,100.0\text{ kg/hr}$ at $12.25\%$ moisture w.b.
* **Fluidized-Bed Evaporation:** $125.7\text{ kg/hr}$ moisture removed
  - Target moisture: $10.0\%$ w.b. ($0.111\text{ kg water / kg dry matter}$)
* **Milling Shatter & Fines Loss:** $22.5\text{ kg/hr}$ ($0.45\%$ of dry feed)
* **Saleable Finished Product Output:** **$4,951.8\text{ kg/hr}$**
* **Net Overall Process Mass Yield:** **$99.04\%$**

### 2.2 Thermal & Electrical Energy Balances
* **Sensible Heat of Grain:**
  $$\dot{Q}_{\text{sensible}} = \dot{m} C_p \Delta T = 5175 \times 1.8 \times (95 - 25) / 1000 = 652.1\text{ MJ/hr}$$
* **Latent Heat of Water Vaporization ($L_v = 2260\text{ kJ/kg}$):**
  $$\dot{Q}_{\text{latent}} = (75.0 + 125.7) \times 2260 / 1000 = 453.6\text{ MJ/hr}$$
* **Radiation & Convection Losses (Tunnel shell loss):** $60.5\text{ MJ/hr}$
* **Gross Thermal Input Duty ($\eta_{\text{thermal}} = 65\%$):**
  $$\dot{Q}_{\text{thermal, gross}} = \frac{652.1 + 453.6 + 60.5}{0.65} = \mathbf{1,794.2\text{ MJ/hr}} \quad (498.4\text{ kW}_{\text{th}})$$
* **Specific Thermal Energy Consumption:** **$0.359\text{ MJ per kg of raw grain}$**
* **Connected Electrical Load:**
  - Tempering screw drive: $3.7\text{ kW}$
  - IR conveyor belt drive: $2.2\text{ kW}$
  - Fluid bed air supply blowers: $22.0\text{ kW}$
  - Exhaust & cyclone induced-draft fan: $11.0\text{ kW}$
  - Cooling bed fan & vibratory feeder: $6.1\text{ kW}$
  - **Total Connected Electrical Load:** **$45.0\text{ kW}$** ($9.0\text{ kWh per tonne}$)

---

## 3. Scale-Up Equipment Sizing & Materials Specification

| Unit Operation | Equipment Type | Design Capacity | Key Dimensions / Sizing Basis | Material of Construction (MOC) | Instrumentation & Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tempering Unit** | Continuous paddle misting screw | $6.0\text{ T/hr}$ | $400\text{ mm}$ dia $\times 4.5\text{ m}$ length, $45\text{ RPM}$ | SS304 contact parts | Magnetic flowmeter, automated misting solenoid |
| **Infrared Tunnel**| Catalytic gas-fired IR radiant tunnel| $5.5\text{ T/hr}$ | $1.2\text{ m}$ belt width $\times 9.0\text{ m}$ active length | SS304 woven wire mesh belt | Optical pyrometer, zone PID temperature controllers |
| **Drying Section** | Continuous vibratory fluidized bed | $5.5\text{ T/hr}$ | $1.0\text{ m}$ bed width $\times 6.0\text{ m}$ length | SS304 perforated deck plate | RTD inlet/exhaust temp, bed differential pressure |
| **Air Filtration** | High-efficiency cyclone + baghouse | $7,500\text{ m}^3/\text{hr}$ | $1.2\text{ m}$ cyclone dia, reverse pulse-jet | Carbon steel / SS304 ducting | Differential pressure transmitter across bags |
