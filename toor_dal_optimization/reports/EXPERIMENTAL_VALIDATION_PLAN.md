# FINNOAQ TOOR DAL — EXPERIMENTAL VALIDATION & PREREGISTERED LAB PROTOCOL

**Document ID:** HKT-EXP-2026-001  
**Protocol Standard:** Preregistered Randomized Block Confirmatory Study  
**Objective:** Provide Definitive Physical Evidence to Transition from Class B to Class A  
**Estimated Physical Execution Cost:** ₹50 – ₹100 (In-house Kitchen Protocol) vs ₹1,98,000 (Commercial CRO Lab)

---

## 1. Preregistered Study Design & Hypotheses

This experimental protocol is preregistered to prevent p-hacking, outcome switching, or post-hoc rationalization.

### Formal Statistical Hypotheses
- **Primary Null Hypothesis ($H_0$):** The 0.50% NaHCO₃ conditioning treatment does not reduce the standardized pressure cooking time of the target Tanzanian Toor Dal lot below $25.0\text{ minutes}$ ($\ge 5.0\text{ whistles}$):
  $$H_0: \mu_{\text{treated}} \ge 25.0\text{ min}$$
- **Alternative Hypothesis ($H_1$):** The treatment achieves the target cooking time of $\le 15.0\text{ minutes}$ ($\le 3.5\text{ whistles}$):
  $$H_1: \mu_{\text{treated}} \le 15.0\text{ min}$$
- **Decision Significance Criterion:** One-tailed Student's t-test / Welch's t-test at $\alpha = 2.87 \times 10^{-7}$ ($5\sigma$) with $n = 4$ independent replicate batches per treatment arm.

---

## 2. Four-Arm Randomized Block Design

The experiment evaluates four distinct physical treatment arms using samples from the target Tanzanian dal lot:

| Treatment Arm | Formulation & Conditioning Procedure | Water Ratio | Duration & Temperature | Post-Treatment Handling | Sample Size ($n$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Arm 1: Untreated Control** | Plain potable / DI water soak (Reference) | 1.5 : 1 | 30 min @ 25°C | Drained on screen, dried at 45°C | $n = 4$ batches |
| **Arm 2: Low-Dose NaHCO₃** | 0.25% w/w Food Grade NaHCO₃ solution | 1.5 : 1 | 30 min @ 25°C | Drained, 10s mist rinse, dried at 45°C | $n = 4$ batches |
| **Arm 3: Nominal Winner** | **0.50% w/w Food Grade NaHCO₃ solution** | **1.5 : 1** | **30 min @ 25°C** | **Drained, 10s mist rinse, dried at 45°C** | **$n = 4$ batches** |
| **Arm 4: Citrate Alternative**| 0.50% w/w Food Grade Sodium Citrate | 1.5 : 1 | 30 min @ 25°C | Drained, 10s mist rinse, dried at 45°C | $n = 4$ batches |

---

## 3. Standardized In-House Cooking Assay Protocol

To eliminate operator subjectivity and thermal variance across domestic stoves:

```
┌────────────────────────────────────────────────────────────────────────┐
│               STANDARDIZED PHYSICAL COOKING PROTOCOL                   │
├────────────────────┬───────────────────────────────────────────────────┤
│ Parameter          │ Standardized Experimental Setting                 │
├────────────────────┼───────────────────────────────────────────────────┤
│ Pressure Cooker    │ Hawkins Classic 3.0 L or Prestige Deluxe 3.0 L    │
│ Pressure Regulator │ Standard weighted vent weight calibrated to       │
│                    │ 1.0 kg/cm² gauge (15 psi / 103–115 kPa).          │
│ Heating Source     │ Induction Cooktop set to exactly 1200 Watts       │
│                    │ (eliminates gas pressure fluctuations).           │
│ Charge Mass        │ 100.0 ± 0.1 grams dried dal per pot.              │
│ Cooking Water      │ 300.0 ± 1.0 grams potable water (Liquor ratio 3:1)│
│ Ambient Water Temp │ 25.0 ± 1.0 °C.                                    │
└────────────────────┴───────────────────────────────────────────────────┘
```

### Step-by-Step Test Execution
1. **Charge:** Place $100.0\text{ g}$ of prepared dal and $300.0\text{ g}$ of water into the cooker. Lock the lid with gasket inspected and vent tube clear.
2. **Induction Heating:** Place cooker on 1200W induction burner; start digital stopwatch ($t = 0$).
3. **Thermal Induction Lag:** Record timestamp $t_{\text{steam}}$ when continuous steam emerges from the vent tube (typical 3.8 to 4.5 min). Place vent weight regulator on the vent pipe.
4. **Whistle Logging:** Record the exact stopwatch timestamp of every pressure release whistle ($W_1, W_2, W_3, \dots$).
5. **Cooking Endpoint:**
   - For Treated Arms: Extinguish heat at Whistle 3.5 (or 15.0 min elapsed).
   - For Control Arm: Extinguish heat at Whistle 6.0 (or when full softening occurs).
6. **Depressurization:** Allow exactly 5.0 minutes of natural cooling; gently lift vent weight to confirm depressurization before opening.
7. **Glass Plate Squash Test:** Take 10 representative cotyledons from the pot center. Place between two glass microscope slides and apply 1.0 kg dead weight. If 10/10 cotyledons spread into a smooth paste with zero hard white core, mark as **FULLY COOKED**.

---

## 4. Techno-Economic Capital Preservation: ₹50 vs ₹1,98,000

| Evaluation Option | Description | Direct Cost (INR) | Turnaround Time | Strategic Value to FinnoaQ |
| :--- | :--- | :--- | :--- | :--- |
| **Option A: Commercial CRO Lab** | Send samples to external commercial analytical laboratory for routine texture analysis and proximate testing. | **₹1,73,000 – ₹1,98,000** | 20 – 30 business days | High cost; yields standard charts without process engineering integration. |
| **Option B: In-House Kitchen Protocol (RECOMMENDED)** | Execute the preregistered 4-arm standardized pressure cooker protocol using existing kitchen equipment and food-grade reagents. | **₹50 – ₹100** | **2 – 3 days** | **Preserves ~₹1.98 Lakh in capital** for pilot equipment fabrication or GPU upgrades; yields immediate physical verification. |

**Recommendation:** Proceed immediately with Option B.
