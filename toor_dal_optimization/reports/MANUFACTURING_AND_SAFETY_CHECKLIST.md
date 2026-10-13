# HARAKUTIR MANUFACTURING READINESS & FOOD-SAFETY CHECKLIST
## FSSAI Standards, HACCP Hazard Analysis, Critical Control Points (CCPs) & Factory Qualification

**Document ID:** HKT-SAF-2026-011  
**Version:** 3.0.0  
**Governing Regulation:** Food Safety and Standards (Food Products Standards and Food Additives) Regulations, 2011 (FSSAI)  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Statutory FSSAI Compliance Checklist (Dry Split Pulses)

| Regulatory Parameter | Statutory FSSAI Limit | Process Target / Achieved | Compliance Status | Verified Analytical Method |
| :--- | :--- | :--- | :--- | :--- |
| **Moisture Content** | Maximum $14.0\%$ (w.b.) | **$10.0\%$ (w.b.)** | COMPLIANT | IS:4333 (Part II) Oven Drying |
| **Water Activity ($a_w$)** | Max $0.65$ (at 25°C) | **$0.58$ (at 25°C)** | COMPLIANT | AOAC 978.18 / Rotronic Sensor |
| **Foreign Matter (Inorganic)**| Maximum $0.1\%$ by weight | **$0.0\%$** (Destoner installed) | COMPLIANT | IS:4333 (Part I) Visual Gravimetric |
| **Foreign Matter (Organic)**  | Maximum $0.75\%$ by weight | **$< 0.1\%$** | COMPLIANT | IS:4333 (Part I) Visual Gravimetric |
| **Damaged / Weeviled Grains** | Maximum $3.0\%$ by count | **$< 0.5\%$** (Optical sorter) | COMPLIANT | IS:4333 (Part III) Manual Count |
| **Uric Acid** | Maximum $100\text{ mg/kg}$ | **$< 10\text{ mg/kg}$** | COMPLIANT | Colorimetric enzymic method |
| **Aflatoxin Total (B1+B2+G1+G2)**| Maximum $15.0\text{ ppb}$ | **$< 2.0\text{ ppb}$** | COMPLIANT | HPLC with Post-Column Derivatization |
| **Aflatoxin B1** | Maximum $10.0\text{ ppb}$ | **$< 1.0\text{ ppb}$** | COMPLIANT | HPLC with Fluorescence Detection |
| **Pesticide Residues (MRLs)** | Codex / FSSAI Schedule limits| **ND (< Limit of Detection)** | COMPLIANT | GC-MS/MS & LC-MS/MS Multi-Residue |

---

## 2. HACCP Plan & Critical Control Points (CCPs)

```
[Raw Receiving] --> [Tempering] --> [IR Tunnel] --> [Dryer (CCP-1)] --> [Metal Detector (CCP-2)] --> [Packaging]
```

### CCP-1: Final Drying Moisture & Water Activity ($a_w$)
* **Hazard:** Growth of xerophilic molds (*Aspergillus flavus*, *Penicillium* spp.) and synthesis of aflatoxins during downstream retail storage if moisture exceeds $14\%$ or $a_w > 0.65$.
* **Critical Limit:** Moisture $\le 11.5\%$ w.b. and $a_w \le 0.60$ measured immediately after fluid-bed cooler.
* **Monitoring Procedure:** Hourly sampling across fluid-bed cooler discharge chute; rapid halogen moisture analyzer verification + calibrated water activity meter.
* **Corrective Action:** If moisture $> 11.5\%$, automated divert gate routes material back into tempering bypass for secondary drying pass; alert logged on SCADA.

### CCP-2: In-Line Metal Detection Post-Cooling
* **Hazard:** Metallic fragments from wear of vibratory screen decks or bucket elevator chains.
* **Critical Limit:** Zero detectable ferrous ($\ge 1.0\text{ mm}$), non-ferrous ($\ge 1.2\text{ mm}$), or stainless steel ($\ge 1.5\text{ mm}$) contamination.
* **Monitoring Procedure:** $100\%$ inline continuous interrogation via multi-frequency tunnel metal detector with automated pneumatic reject gate.
* **Corrective Action:** Immediate pneumatic rejection into locked quarantine bin; QA supervisor logs foreign body occurrence and inspects upstream machinery.

---

## 3. Factory Qualification Line Trial Acceptance Criteria

Before authorizing commercial sales, the industrial plant must complete three consecutive 8-hour qualification shifts satisfying:
1. **Continuous Line Availability:** Minimum $95\%$ uptime over 24 operating hours without mechanical jamming or belt tracking faults.
2. **Batch Cooking Parity:** Finished packed dal samples drawn every 2 hours must achieve $\le 3.5$ whistles in standardized 5L pressure cooker testing.
3. **Yield Stability:** Net finished saleable mass yield $\ge 98.0\%$ across all three shifts.
4. **Hygienic Cleaning & Changeover:** Complete CIP/dry sanitation protocol executable within $\le 90\text{ minutes}$.
