# Process Hazard and Operability (HAZOP) Study Dossier
## 15,000 kg/day Incoming-Feed Toor-Dal Greenfield Processing Plant

> [!IMPORTANT]
> **Engineering Phase:** `CONCEPTUAL FRONT-END ENGINEERING DESIGN (FEED)`  
> **Document Identifier:** `HAZ-FIN-15T-V3-001`  
> **Governing Standards:** IEC 61882 (HAZOP Application Guide), IEC 61508 / IEC 61511 (Functional Safety / SIL), NFPA 68 / 69  
> **Stamping:** `CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR PROCUREMENT`  
> **Risk Matrix Applied:** 5×5 Severity / Likelihood Risk Ranking with As Low As Reasonably Practicable (ALARP) criteria.

---

## 1. Study Scope, Nodes & Methodology

The Process Hazard and Operability (HAZOP) study systematically interrogates all process, mechanical, thermal, and electrical operations in the 15 MT/day facility to identify potential plant vulnerabilities, operator safety hazards, product quality deviations, and environmental exceedances before detailed engineering freeze.

### Process Nodes Interrogated
- **Node 1:** Chemical Reagent Preparation & Automated Metering (`SK-100` $\rightarrow$ `TK-101A/B`)
- **Node 2:** Grain Receiving, Ambient Steeping & Low-Shear Agitation (`TK-101A/B`, `AG-101A/B`, `SC-101`)
- **Node 3:** Fluid-Bed Thermal Drying, Blower Air Handling & Dust Recovery (`DR-101`, `HE-101`, `BL-101`, `CY-101`)
- **Node 4:** Cleanroom Grain Storage, Nitrogen Flushing & Primary Packaging (`PK-101A/B`, `MD-101`)

---

## 2. Master HAZOP Risk Assessment Matrix

### NODE 1: Chemical Reagent Preparation & Automated Dosing (`SK-100` $\rightarrow$ `TK-101A/B`)
**Design Intent:** Continuously prepare and meter $0.50\%\text{ w/w}$ food-grade sodium bicarbonate ($NaHCO_3$) liquor at $7.03\text{ L/h}$ to $25.0\text{ L/h}$ at ambient temperature ($25^\circ\text{C}$ to $35^\circ\text{C}$) and $1.5\text{ bar g}$.

| Deviation (Guide Word + Parameter) | Credible Causes | Consequences / Hazards | Existing Safeguards | Risk Rank (S×L) | Recommended Actions & Interlocks |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **NO FLOW** | • Dosing tank `TK-103` empty.<br>• Suction strainer blocked.<br>• Metering pump `P-102` motor trip.<br>• Discharge line valve closed. | • Dal steeped in water only without alkaline reagent.<br>• Calcium pectate cleavage fails; cooking time target ($\le 15\text{ min}$) missed.<br>• Commercial batch rejection. | • Tank low level switch `LALL-103`.<br>• Pump running indication on SCADA.<br>• Inline pH transmitter `pHIT-101` in soak vessel. | **Medium (3×3 = 9)** | **Interlock I-04:** Automated batch filling paused if `pHIT-101` does not reach $\ge 7.8$ within 10 minutes of liquor charging. Automated switchover to standby pump `P-102B`. |
| **MORE FLOW** | • Stroke length misadjusted.<br>• Diaphragm rupture leaking forward.<br>• Siphoning through discharge line due to negative head. | • Over-concentration of $NaHCO_3$ ($> 1.0\%$).<br>• Chemical leaching of dal protein; soapy off-flavor; alkaline residue ($pH > 8.8$).<br>• FSSAI additive non-compliance. | • Back pressure valve `BPV-101` set @ $1.5\text{ bar g}$ prevents siphoning.<br>• High pH alarm `pHAH-101` on vessel. | **High (4×2 = 8)** | **Interlock I-01:** High pH cut-off (`pH > 8.5`) immediately trips metering pump `P-102` and alarms on SCADA. Calibrated volumetric cylinder verification mandatory per shift. |
| **MORE PRESSURE** | • Discharge valve closed against running positive displacement pump.<br>• Line blocked with un-dissolved chemical cake. | • Excessive pressure buildup ($> 6\text{ bar}$).<br>• Bursting of tubing; chemical spray onto operator eyes/skin.<br>• Pump diaphragm failure. | • Integral pump internal spring relief valve.<br>• Local pressure gauge with diaphragm seal. | **Medium (3×2 = 6)** | **Recommendation:** Install external pressure relief valve `PRV-102` set @ $3.5\text{ bar g}$ on pump discharge manifold with return line piped back into `TK-103`. |
| **CONTAMINATION** | • Operator adds non-food grade chemical or incorrect bag.<br>• Biological growth in standing water during shutdown. | • Toxic contamination of food-grade product.<br>• Microbial proliferation in pulse batch.<br>• Severe legal/regulatory liability. | • Distinct barcoded chemical storage bay.<br>• Batch log sign-off sheet.<br>• Daily sanitization drain SOP. | **Critical (5×1 = 5)** | **Quality Control Gate:** Dual-operator sign-off and barcode scanning required prior to dumping chemical sacks into `TK-103`. Complete drain and hot water rinse mandatory if idle $> 24\text{ hours}$. |

---

### NODE 2: Grain Receiving, Ambient Steeping & Agitation (`TK-101A/B`, `AG-101A/B`)
**Design Intent:** Steep $3,750\text{ kg}$ dal with $5,625\text{ kg}$ liquor per batch ($1:1.5$ ratio) for $3.5\text{ hours}$ under gentle axial hydrofoil agitation ($55\text{ RPM}$, tip speed $< 1.8\text{ m/s}$) to achieve $+18.27\%$ moisture uptake without physical cotyledon damage.

| Deviation | Credible Causes | Consequences | Existing Safeguards | Risk Rank | Recommended Actions & Interlocks |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **MORE LEVEL** | • Level transmitter `LT-101` calibration drift.<br>• Water feed valve `XV-101` fails open.<br>• Operator double-batches slurry. | • Slurry overflow from top head manway.<br>• Flooding of wet processing hall floor ($> 8\text{ m}^3$ liquid).<br>• Structural overload of support legs. | • Guided wave radar continuous level `LIT-101`.<br>• 3" overflow nozzle `N11` piped to floor drain trench. | **Medium (3×3 = 9)** | **Interlock I-01 (SIL-1):** Independent hardwired high-high vibrating fork level switch `LAHH-101` shuts off water valve `XV-101` and closes inlet feed gates independently of PLC. |
| **LESS AGITATION / NO FLOW** | • Agitator `AG-101` geared motor mechanical jam.<br>• VFD trip or loss of electrical power.<br>• Shaft shear pin failure. | • Dal grains settle to conical bottom, forming compacted plug.<br>• Non-uniform chemical diffusion; un-soaked core.<br>• Choking of bottom discharge valve `XV-103`. | • Motor thermal overload trip alarm.<br>• Zero-speed sensor switch on agitator shaft. | **Medium (3×3 = 9)** | **Interlock I-02:** If agitator zero-speed sensor trips during active soak cycle, trigger audible floor alarm and pause batch timer. Provide manual emergency air-sparge connection at vessel bottom cone. |
| **MORE SHEAR / SPEED** | • VFD frequency erroneously set to maximum ($70\text{ Hz} / 75\text{ RPM}$).<br>• Wrong impeller type installed during maintenance. | • High shear stress on soaked cotyledons.<br>• Dal breakage, fracturing, and starch slurry attrition ($> 5\%$ yield loss).<br>• High COD load in effluent. | • VFD speed parameter password protected.<br>• Low-shear 3-blade hydrofoil impeller design ($N_p \approx 0.38$). | **High (3×4 = 12)** | **Software Clamp:** Lock maximum VFD output frequency in drive firmware to $55\text{ RPM}$ ($v_{\text{tip}} \le 1.8\text{ m/s}$). Measure broken dal percentage in laboratory screening trial. |
| **LEAK / SPILL** | • Flush bottom valve `XV-103` seal wear.<br>• Bottom drain pipe gasket blowout. | • Premature loss of steep liquor during 3.5h cycle.<br>• Incomplete hydration; slippery floor hazard. | • Visual inspection port.<br>• SS floor drainage trench surrounding vessel base. | **Low (2×2 = 4)** | **Maintenance SOP:** Replace flush bottom diaphragm sleeve at 6-month preventive maintenance intervals. |

---

### NODE 3: Continuous Vibrating Fluid Bed Drying & Air Handling (`DR-101`, `HE-101`, `BL-101`)
**Design Intent:** Continuously fluidize and dry $18,590\text{ kg/day}$ moist dal from $28.77\%$ wb to $10.0\%$ wb at $85^\circ\text{C}$ air temperature with $14\text{ m}^2$ active deck area and safe dust aspiration.

| Deviation | Credible Causes | Consequences | Existing Safeguards | Risk Rank | Recommended Actions & Interlocks |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **MORE TEMPERATURE** | • Steam control valve `TCV-101` fails fully open.<br>• Temperature transmitter `TT-101` fails low.<br>• Air blower `BL-101` trips while steam remains on. | • Air temperature exceeds $105^\circ\text{C}$.<br>• Dal case hardening, protein denaturation, yellow-to-brown color degradation.<br>• Potential smoldering pulse dust fire. | • Dual RTD temperature transmitters (`TT-101A/B`).<br>• High temperature alarm `TAH-101` on SCADA screen. | **Critical (4×2 = 8)** | **Interlock I-03 (SIL-2):** Independent high-high temperature switch `TAHH-101` (set @ $95^\circ\text{C}$) slams emergency steam shutoff valve `XV-201` closed within 1.0 second. Blower trip interlocked to cut steam immediately. |
| **LESS AIR FLOW** | • Blower intake air filter clogged with dust.<br>• Fan belt slippage / motor overload trip.<br>• Inlet guide vane damper stuck closed. | • Loss of bed fluidization.<br>• Wet dal collapses onto deck plate, blocking perforations and burning.<br>• Massive production outage. | • Differential pressure transmitter across deck `PDIT-101`.<br>• Blower motor current monitor on MCC. | **High (3×3 = 9)** | **Interlock I-05:** Low differential pressure `PDAL-101` ($< 400\text{ Pa}$) triggers wet dal feed shutoff gate within 5 seconds to prevent deck bed choking. |
| **DUST EXPLOSION** | • Dry fine pulse dust ($< 75\mu\text{m}$) accumulated in freeboard / cyclone.<br>• Static electric spark from ungrounded vibrating trough.<br>• Tramp metal foreign object creating frictional spark. | • Secondary agricultural pulse dust deflagration ($K_{st} \approx 60-110\text{ bar}\cdot\text{m/s}$).<br>• Severe structural rupture of dryer hood; personnel injury. | • Continuous equipotential bonding straps across all isolators.<br>• Inline magnetic separator at wet grain intake. | **Severe (5×1 = 5)** | **NFPA 68 Compliance:** Dual calibrated burst panels `EV-101A/B` (burst pressure $0.10\text{ bar g}$) installed on dryer expansion hood, vented outdoors via zero-backpressure ductwork. All electrical equipment rated ATEX Zone 22. |

---

### NODE 4: Cleanroom Storage, High-Speed Packaging & Metal Detection (`PK-101A/B`, `MD-101`)
**Design Intent:** Package $14,267.8\text{ kg/day}$ dried dal at $10.0\%$ moisture into $1\text{ kg}$ and $5\text{ kg}$ sealed nitrogen-flushed laminated pouches in Class 8 cleanroom with $100\%$ inline metal detection.

| Deviation | Credible Causes | Consequences | Existing Safeguards | Risk Rank | Recommended Actions & Interlocks |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **LESS NITROGEN PURGE** | • Nitrogen generator membrane failure.<br>• N2 supply solenoid valve stuck closed.<br>• Pouch forming tube gas nozzle misaligned. | • Residual oxygen in pouch exceeds $1.0\% O_2$.<br>• Lipid oxidation, rancidity, pest/weevil egg hatching during commercial shelf-life. | • Nitrogen pressure switch `PAL-108`.<br>• Inline oxygen sensor on N2 supply header. | **High (3×3 = 9)** | **Quality Interlock:** Inline oxygen analyzer (`AIT-108`) alarms if $O_2 > 0.8\%$ in supply stream. Pouch quality check: benchtop headspace $O_2$ test on 3 pouches per hour. |
| **METAL CONTAMINATION** | • Broken screen wire from dewaterer `SC-101`.<br>• Screw or bolt loosened from conveyor bucket.<br>• Foreign metallic object from incoming farm lot. | • Metal shard packaged in retail product.<br>• Consumer safety hazard; catastrophic product recall and brand destruction. | • Rare-earth magnetic trap (10,000 Gauss) on surge hopper intake.<br>• High-sensitivity inline metal detector `MD-101`. | **Critical (5×1 = 5)** | **Mandatory Action:** Metal detector `MD-101` equipped with automated pneumatic flapper reject bin and fail-safe reject confirmation sensor. Sensitivity verified: Ferrous $\phi 1.0\text{ mm}$, Non-Ferrous $\phi 1.5\text{ mm}$, SS316 $\phi 2.0\text{ mm}$. |
| **LOSS OF CLEANROOM PRESSURE** | • HVAC AHU blower belt snap.<br>• Airlock doors propped open simultaneously.<br>• HEPA filter gasket leakage. | • Cleanroom positive pressure drops below $+15\text{ Pa}$.<br>• Ingress of airborne mold spores, insect pests, and warehouse dust. | • Differential pressure indicator across airlock.<br>• Interlocked airlock doors (cannot open together). | **Medium (3×2 = 6)** | **Interlock:** Magnehelic differential pressure transmitter `PDIT-105` alarms on SCADA if cleanroom pressure $< +10\text{ Pa}$ for $> 30\text{ seconds}$. |

---

## 3. Summary of Safety Integrity Level (SIL) Action Items

The HAZOP study identified five safety-critical loops requiring functional safety certification under IEC 61511:

1. **SIL-2 Loop SIF-01 (Dryer Thermal Runaway):**  
   Sensor: `TT-101A/B` (1oo2 voting) $\rightarrow$ Safety PLC Logic $\rightarrow$ Final Element: Emergency Steam Shutoff Valve `XV-201` (Fail-Closed, closure time $< 1.0\text{ s}$).
2. **SIL-1 Loop SIF-02 (Soak Vessel Overfill):**  
   Sensor: High-High Level Switch `LAHH-101` $\rightarrow$ Interposing Safety Relay $\rightarrow$ Water Feed Valve `XV-101` & Chemical Dosing Valve `XV-102`.
3. **SIL-1 Loop SIF-03 (Bed Choking & Defluidization):**  
   Sensor: Differential Pressure `PDIT-101` $\rightarrow$ PLC Logic $\rightarrow$ Wet Dal Rotary Airlock Feeder motor cut-off.
4. **SIL-1 Loop SIF-04 (Foreign Metal Rejection):**  
   Sensor: Coil Detector `MD-101` $\rightarrow$ Fast-acting Pneumatic Diverter Gate (response time $< 150\text{ ms}$) $\rightarrow$ Sealed Lockable Reject Bin.
5. **Passive Safeguard (Dust Deflagration):**  
   `EV-101A/B` Explosion Relief Vents certified per NFPA 68 with certified burst pressure test certificates filed in the plant statutory dossier.
