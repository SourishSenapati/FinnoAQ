# FINNOAQ PROTOTYPE ASSESSMENT TEMPLATE
## Physical Prototype Validation Scorecard, Critical-to-Quality (CTQ) Acceptance Rules & Go/No-Go Decision Gate

**Document ID:** HKT-PTA-2026-009  
**Version:** 3.0.0  
**Controlling Stage:** Stage 06 / Gate G5 (Prototype Release)  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Prototype Identification & Metadata

* **Prototype Batch ID:** `PROTO_TZ_EXP_[RUN_NUMBER]`
* **Technology Family:** `[Family 2 / Family 3 / Family 4 / Family 7]`
* **Conditioning Description:** `[Specify exact time, temperature, moisture added, and drying profile]`
* **Raw Material Lot Pointer:** `[Lot ID, Tanzanian Import Port, Harvest Date]`
* **Date of Preparation:** `YYYY-MM-DD`
* **Lead Laboratory Technician:** `[Assigned Scientist Name]`

---

## 2. Critical-to-Quality (CTQ) Evaluation Scorecard

| CTQ Parameter | Target Acceptance Threshold | Mandatory Hard Gate? | Measured Value | Measurement Instrument | Verification Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Whistle Count (Standard 5L Cooker)** | **$\le 3.5$ Whistles** | YES (CRITICAL) | `[____]` Whistles | Calibrated 5L Cooker (1:4 ratio) | `[PASS / FAIL]` |
| **Objective Cooking Time (Mattson)** | **$\le 20.0$ Minutes** | YES (CRITICAL) | `[____]` Minutes | Automated Mattson 80% Drop | `[PASS / FAIL]` |
| **Cooked Texture Firmness** | **$20.0 - 24.0$ Newtons** | YES (CRITICAL) | `[____]` N | Texture Profile Analyzer (TA.XT) | `[PASS / FAIL]` |
| **Hard-Core Defect Incidence** | **$0.0\%$ (Zero grains)** | YES (CRITICAL) | `[____]` % | Glass-plate squash test (100 grains) | `[PASS / FAIL]` |
| **Finished Moisture Content** | **$9.5\% - 11.0\%$ w.b.** | YES (FSSAI) | `[____]` % | Mettler Toledo Moisture Analyzer | `[PASS / FAIL]` |
| **Finished Water Activity ($a_w$)** | **$\le 0.60$ at 25°C** | YES (FSSAI) | `[____]` $a_w$ | Rotronic Aw Thermocon | `[PASS / FAIL]` |
| **Hedonic Sensory Score (Overall)** | **$\ge 7.8 / 9.0$** | NO (SCORING) | `[____]` / 9.0 | Trained Indian Sensory Panel | `[PASS / FAIL]` |
| **Beany Off-Note Index (BOSI)** | **$\ge 0.70$** | NO (SCORING) | `[____]` index | GC-MS volatile hexanal assay | `[PASS / FAIL]` |
| **Available Lysine Retention** | **$\ge 90.0\%$** | YES (QUALITY) | `[____]` % | AOAC 975.44 Fluorodinitrobenzene | `[PASS / FAIL]` |
| **Net Conditioning Yield** | **$\ge 98.0\%$** | NO (ECONOMIC) | `[____]` % | Analytical mass balance | `[PASS / FAIL]` |

---

## 3. Culinary Matrix Performance Check

* **Neutral Distilled Water (pH 7.0):** Whistles: `[____]`, Hard Core: `[____]%`
* **Hard Water (200 ppm Ca2+, pH 7.8):** Whistles: `[____]`, Hard Core: `[____]%`
* **Acidic Sambar Broth (pH 4.1, Tamarind Extract):** Whistles: `[____]`, Hard Core: `[____]%`

---

## 4. Formal Stage Gate G5 Go/No-Go Disposition

* **Total Hard Gate Failures:** `[ 0 / >0 ]`
* **Model Error Deviation:** $| \text{Predicted Whistles} - \text{Measured Whistles} | = [ \_\_\_\_ ]$
* **Closed-Loop Ingestion Event:** `[ Recorded in state/journal.db ]`
* **Formal Decision Verdict:**
  - `[ ] GO — ADVANCE TO SCALE-UP SIMULATION (STAGE 07)`
  - `[ ] REVISE — MINOR PARAMETER RE-TUNING REQUIRED`
  - `[ ] NO-GO — CANDIDATE REJECTED; TRIGGER BAYESIAN POSTERIOR UPDATE`

* **Signatures:**  
  *Technical Reviewer:* _______________________  
  *FinnoaQ Project Sponsor:* _______________________  
  *Date:* _______________________
