# Piping Material Specifications (PMS) & Valve Schedule (Rev V3.0)
## 15,000 kg/day Incoming-Feed Toor-Dal Greenfield Processing Plant

> [!IMPORTANT]
> **Engineering Phase:** `CONCEPTUAL FRONT-END ENGINEERING DESIGN (FEED)`  
> **Document Identifier:** `PMS-FIN-15T-V3-001`  
> **Governing Standards:** ASME B31.3 (Process Piping), ASME BPE (Bioprocessing Equipment), ASTM A270, ASTM A312, IS 1239  
> **Stamping:** `CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`

---

## 1. Master Piping Class Summary

| Piping Class Code | Service Description | Design Pressure | Design Temp | Pipe Material | Flange Rating & Facing | Gasket Material |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **`1S1`** | Food Contact Slurry, Dal & Steep Liquor | Full Vacuum to 3.0 bar g | -10°C to 100°C | ASTM A270 SS316L Sanitary Tube ($R_a \le 0.8\mu\text{m}$) | ASME BPE Tri-Clamp / Class 150 Sanitary | USP Class VI EPDM / PTFE Envelope |
| **`1C1`** | Utility Saturated Steam & High-Pressure Condensate | 10.0 bar g | -10°C to 185°C | ASTM A106 Gr B Seamless Carbon Steel Sch 40 | ASME B16.5 Class 150 RF | Spiral Wound SS304 with Graphite filler |
| **`1W1`** | Softened Process Water & Low-Pressure CIP Rinse | 6.0 bar g | 0°C to 65°C | ASTM A312 TP304 Welded Stainless Steel Sch 10S | ASME B16.5 Class 150 FF | Compressed Non-Asbestos Fiber (CNAF) 2mm |
| **`1E1`** | Concentrated Reagent Dosing ($NaHCO_3$) | 5.0 bar g | 0°C to 50°C | PVDF (Polyvinylidene Fluoride) / SS316L Sch 40 | DIN / ANSI Class 150 Flat Face | Virgin PTFE Solid Gaskets |
| **`1D1`** | Spent Liquor Effluent & Gravity CIP Drainage | Atmospheric (Gravity) | 0°C to 80°C | Schedule 10S SS304 / Heavy-Duty HDPE PE100 | Class 150 Stub Ends with Backing Rings | EPDM Full Face Gaskets |
| **`1A1`** | Instrument & Utility Plant Air (Dry & Oil-Free) | 8.0 bar g | -10°C to 50°C | Seamless Copper Tube / Polyurethane tubing | Threaded BSPT / Swagelok Compression | NBR / Brass O-Rings |

---

## 2. Detailed Class Specification: Class `1S1` (Food-Grade Sanitary SS316L)

### Scope
Covers all product-contact piping for raw dal feed, steeping slurry, chemical soak liquor, and wet dal slurry between intake hopper `HP-101`, soak tanks `TK-101A/B`, and dewatering screen `SC-101`.

- **Piping Sizes:** 1.5" (DN40), 2.0" (DN50), 3.0" (DN80), 4.0" (DN100), 6.0" (DN150).
- **Tubing Specification:** ASTM A270 SS316L, Seamless / Longitudinal Welded, Bright Annealed.
- **Internal Surface Roughness:** $R_a \le 0.8\mu\text{m}$ ($32\mu\text{in}$), orbital welded with argon purge.
- **Fittings:** Long-radius sanitary 90° and 45° elbows ($R = 1.5D$), concentric reducers, equal tees conforming to ASME BPE.
- **Joints:** Sanitary Tri-Clamp ferrule ends conforming to ISO 2852 / ASME BPE with heavy-duty 2-segment 304SS clamps.
- **Branch Connections:** Pulled sanitary tees with orbital butt-welds; zero dead-legs ($L/D \le 1.5$).

### Valve Specifications for Class `1S1`
1. **Sanitary Butterfly Valves (`BFV-1S1`):**
   - Type: Hygienic wafer/flanged butterfly valve, encapsulated silicone or EPDM seat.
   - Body & Disc: ASTM A351 CF3M (SS316L), mirror polished disc ($R_a \le 0.4\mu\text{m}$).
   - Actuation: Pneumatic single-acting spring-return actuator with top-mounted control box (AS-i / 24V DC solenoid).
   - Fail-Safe Position: Fail Closed (FC).
2. **Flush Bottom Tank Outlet Diaphragm Valves (`FBV-1S1`):**
   - Type: Conical bottom tank zero-deadleg flush bottom diaphragm valve.
   - Body: Solid forged SS316L body matching tank cone profile.
   - Diaphragm: Two-piece PTFE face with EPDM backing cushion.
   - Rating: ANSI Class 150# RF, pneumatically actuated with manual emergency override handwheel.

---

## 3. Detailed Class Specification: Class `1C1` (Utility Saturated Steam)

### Scope
Covers utility saturated steam piping from 600 kg/h IBR boiler `BL-101` to fluid bed dryer steam coil `HE-101` and CIP heat exchangers.

- **Design Limits:** $10.0\text{ bar g}$ @ $185.0^\circ\text{C}$ (Indian Boiler Regulations compliant).
- **Pipe Specification:** ASTM A106 Grade B, Seamless Carbon Steel, Schedule 40.
- **Fittings:** ASTM A234 Grade WPB, Seamless Butt-Weld, ASME B16.9.
- **Flanges:** ASTM A105 Forged Carbon Steel, Class 150 Raised Face (RF) Weld Neck, ASME B16.5.
- **Steam Traps:** Inverted bucket type (Armstrong) / Thermodynamic disc traps with integrated SS strainers and blowdown valves.
- **Thermal Insulation:** Pre-formed mineral wool sections ($50\text{ mm}$ thickness, density $100\text{ kg/m}^3$) clad with $24\text{ SWG}$ corrugated aluminum sheet with moisture barrier.

### Valve Specifications for Class `1C1`
1. **Steam Isolation Gate Valves (`GV-1C1`):**
   - Type: Outside Screw & Yoke (OS&Y), Rising Stem, Bolted Bonnet Gate Valve.
   - Body & Bonnet: ASTM A216 Gr WCB Cast Steel, Class 150 RF.
   - Trim: 13% Chromium Steel (API Trim 8) with Stellite 6 hard-faced seats.
2. **Steam Temperature Control Valve (`TCV-101`):**
   - Type: Single-seated globe control valve with pneumatic diaphragm actuator and digital electro-pneumatic smart positioner (4-20mA HART).
   - Characteristic: Equal Percentage for precise temperature control across turn-down.

---

## 4. Master Valve Schedule & Tagging Matrix

| Valve Tag | P&ID Sheet | Service | Line Size | Class | Valve Type | Actuation | Fail-Safe | Interlock |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`XV-101`** | `DWG-003` | Softened Water Supply to TK-101A | 3" (80mm) | `1W1` | Sanitary Butterfly | Pneumatic Spring | Fail Closed (FC) | High Level LAHH-101 |
| **`XV-102`** | `DWG-003` | Chemical Dosing to TK-101A | 1.5" (40mm) | `1E1` | Sanitary Diaphragm | Pneumatic Spring | Fail Closed (FC) | High Level LAHH-101 |
| **`XV-103`** | `DWG-003` | Tank TK-101A Slurry Bottom Drain | 6" (150mm) | `1S1` | Flush Bottom Diaphragm | Pneumatic Spring | Fail Closed (FC) | Low Level LALL-101 |
| **`XV-104`** | `DWG-003` | Softened Water Supply to TK-101B | 3" (80mm) | `1W1` | Sanitary Butterfly | Pneumatic Spring | Fail Closed (FC) | High Level LAHH-102 |
| **`XV-105`** | `DWG-003` | Chemical Dosing to TK-101B | 1.5" (40mm) | `1E1` | Sanitary Diaphragm | Pneumatic Spring | Fail Closed (FC) | High Level LAHH-102 |
| **`XV-106`** | `DWG-003` | Tank TK-101B Slurry Bottom Drain | 6" (150mm) | `1S1` | Flush Bottom Diaphragm | Pneumatic Spring | Fail Closed (FC) | Low Level LALL-102 |
| **`TCV-101`** | `DWG-004` | Steam Supply to Dryer Heater HE-101 | 2.5" (65mm) | `1C1` | Globe Control Valve | Pneumatic Diaphragm | Fail Closed (FC) | High Temp TAHH-101 |
| **`PRV-101`** | `DWG-003` | Vessel TK-101A Overpressure Relief | 2" (50mm) | `1S1` | Spring Loaded Sanitary | Self-Actuated | Relieve @ 1.5 bar g | Overpressure Safety |
| **`PRV-102`** | `DWG-003` | Dosing Pump Discharge Safety Loop | 0.75" (20mm) | `1E1` | Diaphragm Relief Valve | Self-Actuated | Relieve @ 3.5 bar g | Skid Pump Safety |
| **`BPV-101`** | `DWG-003` | Dosing Line Anti-Siphoning | 0.5" (15mm) | `1E1` | Back Pressure Valve | Spring Diaphragm | Set @ 1.5 bar g | Anti-Siphon Protection |
