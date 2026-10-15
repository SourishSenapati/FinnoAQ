# OPERATIONS, MAINTENANCE, AND OPERATOR TRAINING PLAN (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-016  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Operations, Maintenance & Industrial Training  

---

## 1. Standard Operating Procedures (SOP Framework)

The plant operations team executes processing shifts under six core Standard Operating Procedures:

```mermaid
graph LR
    SOP01[SOP-01: Intake & Cleaning] --> SOP02[SOP-02: Chemical Liquor Prep]
    SOP02 --> SOP03[SOP-03: Soaking Cycle TK-101]
    SOP03 --> SOP04[SOP-04: Dewater & Mist VS-101]
    SOP04 --> SOP05[SOP-05: Fluid Drying DR-101]
    SOP05 --> SOP06[SOP-06: VFFS Packaging PK-101]
```

### SOP Master Table:

| SOP Number | Procedure Title | Key Operational Controls | Quality & Safety Critical Limits |
| :--- | :--- | :--- | :--- |
| **SOP-PR-01** | Raw Grain Receiving & Destoning | Inspect incoming Tanzanian bags; start aspiration fan before elevator `EL-101` | Daily stone discharge trap inspection; pull test on magnet `MAG-101` ($>9,500\text{ Gauss}$) |
| **SOP-PR-02** | 0.50% NaHCO3 Solution Preparation | Fill tank `TK-100` with soft water; weigh FCC sodium bicarbonate on certified scale | Active bicarb concentration verified by hydrometer/titration ($0.50\% \pm 0.05\%$) |
| **SOP-PR-03** | Jacketed Vessel Soaking Cycle | Verify tank clean; meter liquor first, then charge dry dal; run agitator at 35 RPM | Soak timer exactly 30 minutes; liquor temp $28 \pm 2^\circ\text{C}$; flush bottom discharge |
| **SOP-PR-04** | Vibratory Dewatering & Mist Rinse | Inspect wedge-wire deck; verify mist spray header pressure at $3.0\text{ bar}$ | Dewatered dal moisture entering conveyor `CV-101` checked ($27.8\% \pm 1.0\%$) |
| **SOP-PR-05** | Fluid-Bed Dryer & Cooler Run | Pre-heat bed to $60^\circ\text{C}$ on steam; verify fluidizing airflow before feeding wet dal | Discharge NIR moisture $10.0\% \pm 0.5\%$; product temperature $<30^\circ\text{C}$ |
| **SOP-PR-06** | Multihead Weighing & Packaging | Calibrate checkweigher zero; challenge metal detector with Fe/NFe/SS certified wands | Pouch weight $1000 \pm 1.5\text{ g}$; hourly nitrogen flush residual oxygen check ($<2.0\%$) |

---

## 2. Sanitation Standard Operating Procedures (SSOPs)

- **SSOP-01 (Automated CIP Cycle):** Executed after every 16-hour operating shift or prior to weekend shutdown:
  1. **Pre-Rinse:** 5-minute recirculated potable water flush at 40°C dumps residual starch fines to ETP.
  2. **Caustic Wash:** 10-minute recirculation of $1.5\%$ food-grade sodium hydroxide (NaOH) wash at $65^\circ\text{C}$ through rotating spray balls in `TK-101A/B` removes organic protein films.
  3. **Intermediate Rinse:** 5-minute potable water rinse to neutral pH.
  4. **Sanitizing Rinse:** 10-minute recirculation of $0.2\%$ peracetic acid (PAA) at ambient temperature.
  5. **Final Air Blow:** Compressed air purge drains all piping dead legs dry.
- **SSOP-02 (Dry Packaging Area Sanitization):** Zone 4 is strictly dry-cleaned. No water hoses permitted. Industrial HEPA vacuums remove pulse dust from sifter `SCN-102` and weigher buckets, followed by wiping with $70\%$ isopropanol disinfectant wipes.

---

## 3. Preventive Maintenance (PM) Schedule & Spares

| Frequency | Equipment Tag | Maintenance & Inspection Task | Acceptance Tolerance |
| :--- | :--- | :--- | :--- |
| **Daily Shift** | `MD-101` | Challenge metal detector with $1.0\text{ mm}$ Fe, $1.2\text{ mm}$ NFe, $1.5\text{ mm}$ SS wands | $100\%$ detection and positive diverter reject |
| **Daily Shift** | `MAG-101` | Wipe clean magnetic grid trap and inspect for ferrous filings | Log weight of collected metal debris |
| **Weekly** | `VS-101` | Inspect SS316L wedge-wire screen for loose fasteners, blinding, or fatigue cracks | Zero mesh rupture; wire spacing $1.00 \pm 0.05\text{ mm}$ |
| **Weekly** | `AG-101A/B` | Inspect mechanical seal faces, check lubricating barrier fluid level and pressure | Zero leakage; barrier fluid pressure $>1.0\text{ bar}$ |
| **Monthly** | `FN-101 / EXH` | Check V-belt tension, grease pillow block bearings with food-grade grease (NLGI 2) | Bearing temperature rise $<35^\circ\text{C}$; vibration $<2.8\text{ mm/s}$ |
| **Quarterly** | `DR-101` | Inspect distributor deck perforated plate, clean air plenum, check coil spring dampeners | Zero distributor blockage; coil springs free of cracks |

### Critical Insurance Spares Kept in Store:
- 1 complete spare mechanical seal assembly for `AG-101A/B` (SS316L/SiC/Carbon).
- 1 set spare SS316L wedge-wire deck panels ($1.0\text{ mm}$ aperture) for `VS-101`.
- 2 sets replacement V-belts for blowers `FN-101` and `EXH-101`.
- 1 complete spare vortex slurry pump impeller and casing liner for `P-101`.
- 1 spare Coriolis mass flowmeter sensor board (`FT-102`).
- 20 nos spare pulse-jet baghouse filter bags with support cages (`BH-101`).

---

## 4. Operator Competency & Training Matrix

Prior to plant commissioning, all operations and maintenance personnel must complete a certified 40-hour training program:

| Training Module | Target Personnel | Core Learning Competencies | Assessment Method |
| :--- | :--- | :--- | :--- |
| **MOD-01: Food Hygiene & FSSAI GMP** | All Factory Staff | Personal hygiene, hand washing, zone barriers, allergen awareness, Schedule 4 | Written exam ($\ge 85\%$ pass) $+$ hygiene audit |
| **MOD-02: HACCP & CCP Monitoring** | Shift Supervisors & QA | CCP-1 metal detector challenge, CCP-2 moisture testing, deviation reporting | Practical demonstration on production line |
| **MOD-03: SCADA & Batch Automation**| Process Operators | Starting automated sequence, recipe locks, alarm acknowledgement, E-stop response | Simulated fault handling on SCADA terminal |
| **MOD-04: Chemical Handling Safety** | Wet Area Operators | Sodium bicarbonate and CIP acid/caustic handling, PPE use, eyewash station drill | Emergency response drill & PPE inspection |
| **MOD-05: Mechanical PM & Lockout** | Maintenance Technicians| Lockout/Tagout (LOTO) procedures, confined space entry in soak tanks, belt tensioning| Hands-on LOTO sign-off with safety officer |
