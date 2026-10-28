# FINNOAQ TECHNO-ECONOMIC ANALYSIS (TEA) & COMMERCIAL MODEL
## Industrial OPEX, Turnkey CAPEX, Unit Economics & Margin Arbitrage Spread

**Document ID:** HKT-TEA-2026-012  
**Version:** 3.0.0  
**Basis:** 5.0 Tonnes/Hour Commercial Facility (30,000 Tonnes/Year Operating Basis)  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Operating Expenditure (OPEX) Breakdown

All operating cost assumptions are modeled with explicit transparent industrial rate benchmarks:

| Cost Element | Specific Consumption Basis | Industrial Unit Rate | Direct Cost (INR / kg finished dal) | Direct Cost (INR / Tonne finished dal) | Annual Expenditure (30,000 T/yr) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Thermal Energy (Natural Gas / PNG)** | $0.359\text{ MJ / kg grain}$ | $\text{INR } 0.35\text{ / MJ thermal}$ (PNG) | **INR 0.126** | **INR 126.00** | ₹37,80,000 |
| **Electrical Power** | $9.0\text{ kWh / Tonne}$ | $\text{INR } 8.50\text{ / kWh}$ (HT Industrial) | **INR 0.077** | **INR 76.50** | ₹22,95,000 |
| **Process Water (Potable Misting)** | $35\text{ Liters / Tonne}$ | $\text{INR } 0.05\text{ / Liter}$ | **INR 0.002** | **INR 1.75** | ₹52,500 |
| **Direct Operating Labor** | 2 Operators per shift (3 shifts) | $\text{INR } 28,000\text{ / operator-month}$ | **INR 0.067** | **INR 67.20** | ₹20,16,000 |
| **Routine Maintenance & Wear** | $3.5\%$ of turnkey CAPEX / year | Turnkey CAPEX amortized | **INR 0.084** | **INR 84.00** | ₹25,20,000 |
| **Milling Yield Loss (Fines 0.96%)** | $9.6\text{ kg loss / Tonne}$ | Raw dal value @ ₹78.00/kg | **INR 0.749** | **INR 748.80** | ₹2,24,64,000 |
| **TOTAL DIRECT OPERATING COST (OPEX)** | — | — | **INR 1.105 / kg** | **INR 1,104.25 / Tonne** | **₹3,31,27,500 / year** |

*Target Constraint Verification:* Direct added processing OPEX of **INR 1.11 / kg** is safely beneath the **INR 2.50 / kg commercial ceiling**.

---

## 2. Turnkey Capital Expenditure (CAPEX) Estimation

| Equipment Package Description | Scope & Capacity | Estimated Budget (INR Lakhs) |
| :--- | :--- | :--- |
| **Raw Feed Hopper, Destoner & Screw Feeder** | 6.0 T/hr vibrating hopper, magnetic separator | ₹6.5 Lakhs |
| **Continuous Tempering Screw Conveyor** | SS304 paddle misting screw with automated dosing | ₹8.5 Lakhs |
| **Catalytic Infrared Radiant Heating Tunnel** | 5.5 T/hr gas-fired catalytic IR radiant tunnel with exhaust | ₹28.0 Lakhs |
| **Continuous Vibratory Fluidized-Bed Dryer** | Counter-flow heated air deck with cooling discharge section | ₹22.0 Lakhs |
| **Cyclone Dust Collector & Baghouse Filter** | High-efficiency pulse-jet dust collector, ducting, blower | ₹6.5 Lakhs |
| **PLC / SCADA Instrumentation & Control Panel** | Siemens S7-1200 PLC, touch HMI, temperature/moisture loops | ₹5.0 Lakhs |
| **Mechanical Piping, Structural Support & Commissioning** | Turnkey installation, piping, electrical cabling, trials | ₹7.0 Lakhs |
| **TOTAL TURNKEY CAPITAL INVESTMENT (CAPEX)** | **5.0 Tonnes / Hour Complete Quick-Cooking Plant** | **₹83.50 Lakhs (INR 83.5 Lakhs)** |

---

## 3. Commercial Arbitrage & Return on Investment (ROI)

The fundamental commercial driver is the price arbitrage between imported raw Tanzanian Toor Dal and premium domestic Indian Desi Toor Dal:

* **Raw Imported Tanzanian Dal Landed Cost:** **₹78.00 / kg**
* **Direct Added Processing Cost (OPEX + Yield Loss):** **₹1.11 / kg**
* **Total Cost of Goods Sold (COGS) for FinnoaQ Dal:** **₹79.11 / kg**
* **Benchmark Wholesale Price of Indian Desi Dal:** **₹98.00 / kg**
* **Net Value Arbitrage Spread:** **INR 18.89 / kg (₹18,890 per tonne)**
* **Annual Line Capacity (20 hrs/day, 300 days/yr):** $30,000\text{ Tonnes / year}$
* **Projected Annual Gross Margin Contribution:**
  $$30,000\text{ Tonnes} \times \text{INR } 18,890\text{ / Tonne} = \mathbf{₹56.67\text{ Crores / Year}}$$
* **Payback Period:**
  $$\text{Payback} = \frac{\text{CAPEX (₹83.50 Lakhs)}}{\text{Annual Contribution (₹5,667 Lakhs)}} = \mathbf{0.015\text{ Years} \approx 5.5\text{ Days of Full Production!}}$$

**Commercial Conclusion:** Even under conservative stress-testing (reducing the arbitrage spread to ₹10.00/kg), the total capital expenditure of ₹83.5 Lakhs is paid back in less than two weeks of commercial production.
