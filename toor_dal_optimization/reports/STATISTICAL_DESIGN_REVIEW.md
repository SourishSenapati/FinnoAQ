# FINNOAQ TOOR DAL — STATISTICAL DESIGN & GOVERNANCE REVIEW

**Document ID:** HKT-STAT-2026-001  
**Audit Reference:** [`CRITICAL_SCIENTIFIC_AUDIT.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/CRITICAL_SCIENTIFIC_AUDIT.md)  
**Governing Standard:** Two-Stage Lock Protocol & Empirical Verification Standard  
**Date:** 2026-10-15  

---

## 1. Executive Scientific Statement on Statistical Governance

> [!WARNING]
> **Formal Retraction of A Priori Five-Sigma Claim:** The assertion in earlier reports that executing a four-control and four-treatment batch trial will *"automatically establish five-sigma significance and unlock Stage 2 industrial scale-up"* is **formally retracted**. Statistical significance ($p$-value and $z/\sigma$ equivalent) cannot be guaranteed before physical observations exist.

Under the project constitution:
1. **Stage 1 (Discovery & Physical Proof) remains strictly UNCONFIRMED** until empirical timestamps on the physical target lot are ingested and statistically evaluated.
2. **Stage 2 (15 MT/Day Scale-Up & Capital Expenditure) remains STRICTLY LOCKED**.

---

## 2. Statistical Audit of the 4-Control / 4-Treatment Protocol

### 2.1 The Experimental Design
The preregistered confirmatory protocol ([`reports/EXPERIMENTAL_PROTOCOL.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/EXPERIMENTAL_PROTOCOL.md)) specifies a two-arm randomized kitchen trial:
- **Arm 1 (Control):** $n_1 = 4$ independent batches of Untreated Raw Tanzanian Toor Dal cooked under standardized pressure cooker conditions (1200W induction, Hawkins 3.0L cooker, 1:3 dal-to-water ratio).
- **Arm 2 (Candidate A2 / CAND-004):** $n_2 = 4$ independent batches of NaHCO₃-conditioned dal ($0.50\%$ w/w, $1.5:1$ ratio, $30\text{ min}$ soak, fresh mist rinse, dried to $10\%$ moisture).

### 2.2 Formal Null and Alternative Hypotheses
To eliminate p-hacking or retroactive boundary shifting, the hypothesis test is formally prespecified:
- **Null Hypothesis ($H_0$):** The conditioning treatment does not reduce mean domestic pressure cooking time by at least $5.0\text{ minutes}$ ($\ge 1.5\text{ whistles}$ reduction):
  $$H_0: \mu_{\text{control}} - \mu_{\text{treated}} \le 5.0\text{ minutes}$$
- **Alternative Hypothesis ($H_1$):** The conditioning treatment achieves a clinically meaningful reduction exceeding $5.0\text{ minutes}$:
  $$H_1: \mu_{\text{control}} - \mu_{\text{treated}} > 5.0\text{ minutes}$$

---

## 3. Statistical Power & Sample Size Derivation

### 3.1 Mathematical Derivation ($n_1 = 4, n_2 = 4, df = 6$)
In a domestic pressure cooker (~115°C, 15 psi), the untreated control is observed at $\approx 22.0\text{ minutes}$ ($\approx 6.0\text{ whistles}$). Candidate A2 is computationally predicted at $\approx 13.8\text{ minutes}$ ($\approx 3.4\text{ whistles}$).
$$\text{Expected Effect Size } \Delta \mu = \mu_{\text{control}} - \mu_{\text{treated}} = 22.0 - 13.8 = \mathbf{8.2\text{ minutes}}$$

Using Welch's two-sample $t$-statistic with pooled sample variance $s^2$:
$$SE = \sqrt{\frac{s^2}{4} + \frac{s^2}{4}} = \frac{s}{\sqrt{2}}$$
$$t_{\text{obs}} = \frac{\Delta \bar{X}}{SE} = \frac{\sqrt{2} \times 8.2}{s}$$

### 3.2 Power & Significance Table Across Realistic Kitchen Variances

| Experimental Std Dev $s$ | Standard Error $SE$ | Student's $t$ ($df=6$) | One-Tailed $p$-value | Gaussian $\sigma$ Equivalent | Statistical Decision |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$s = 0.50\text{ min}$ (30 s)** | $0.354\text{ min}$ | $t = 23.19$ | $p = 2.11 \times 10^{-7}$ | **$5.06\sigma$** | **Passes $5\sigma$ Gold Standard** |
| **$s = 0.75\text{ min}$ (45 s)** | $0.530\text{ min}$ | $t = 15.46$ | $p = 2.54 \times 10^{-6}$ | **$4.56\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 1.00\text{ min}$ (60 s)** | $0.707\text{ min}$ | $t = 11.60$ | $p = 1.24 \times 10^{-5}$ | **$4.22\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 1.50\text{ min}$ (90 s)** | $1.061\text{ min}$ | $t = 7.73$ | $p = 1.23 \times 10^{-4}$ | **$3.67\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 2.00\text{ min}$ (120 s)**| $1.414\text{ min}$ | $t = 5.80$ | $p = 5.77 \times 10^{-4}$ | **$3.25\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 2.50\text{ min}$ (150 s)**| $1.768\text{ min}$ | $t = 4.64$ | $p = 1.77 \times 10^{-3}$ | **$2.92\sigma$** | Fails $3\sigma$ Regulatory Threshold |

### 3.3 Critical Findings of Power Review:
1. **$5\sigma$ Feasibility Condition:** Achieving the Gaussian $5.0\sigma$ gold standard ($p < 2.87 \times 10^{-7}$) with $n = 4$ batches requires experimental variance to be tightly constrained to **$s \le 30\text{ seconds}$**.
2. **Realistic Kitchen Variability:** Due to domestic induction voltage fluctuations ($\pm 3\%$), pressure cooker thermal inertia differences, and operator human reaction time in noting whistle completions, realistic experimental standard deviations typically range from **$s = 60\text{ to }90\text{ seconds}$** ($1.0\text{ to }1.5\text{ minutes}$).
3. **Realistic Significance:** Under realistic kitchen conditions ($s = 1.0\text{ to }1.5\text{ min}$), the $n=4$ experiment will achieve between **$3.67\sigma\text{ and }4.22\sigma$** ($p < 0.001$). This is overwhelmingly sufficient to prove scientific efficacy, but strictly fails the $5\sigma$ requirement.
4. **Sample Size to Guarantee $5\sigma$:** If kitchen variance is $s = 1.5\text{ minutes}$, achieving $5\sigma$ ($z \ge 5.0$) requires expanding sample size to:
   $$n \ge 2 \times \left( \frac{5.0 \times 1.5}{8.2} \right)^2 \approx \mathbf{17\text{ batches per arm}}$$

---

## 4. Prespecified Decision Rules for Stage 1 Exit

To maintain scientific integrity, the test protocol is divided into two distinct sequential phases:

### Phase 1: Exploratory Kitchen Proof-of-Concept ($n = 4 + 4$)
- **Purpose:** Inexpensive screening (costing < ₹100 in materials) to estimate real-world variance ($s$), observe sensory properties, and verify that the treatment produces a substantial reduction ($\Delta \mu > 5\text{ min}$) without soapy off-flavors.
- **Stage 1 Exit Gate:**
  1. Observed reduction: $\bar{X}_{\text{control}} - \bar{X}_{\text{treated}} \ge 6.0\text{ minutes}$ ($\ge 2.0\text{ whistles}$).
  2. Observed $t$-statistic: $t_{\text{obs}} \ge 3.707$ ($p \le 0.005$, $\ge 3.0\sigma$ regulatory standard).
  3. Mean treated cooking time: $\bar{X}_{\text{treated}} \le 15.0\text{ minutes}$ ($\le 3.5\text{ whistles}$).
  4. Measured dry solids recovery: $\ge 95.50\%$.
  5. Sensory score: Blind hedonic score $\ge 7.5 / 9.0$ with zero alkaline notes.

### Phase 2: Confirmatory Five-Sigma Campaign (Conditional)
- If Phase 1 achieves $t_{\text{obs}} \ge 3.707$ but misses $5.0\sigma$ due to $s > 0.5\text{ min}$, and executive leadership demands full $5.0\sigma$ before capital commitment:
  - Expand sample size to $n = 12\text{ to }16$ batches per arm using the empirical $s$ measured in Phase 1.
  - Test across three independent imported Tanzanian lots to quantify lot-to-lot agronomic variance.

---

## 5. Industrial Stage 2 Lock Enforcement

```
[ STAGE 1 / STAGE 2 LOCK PROTOCOL ]

                      ┌──────────────────────────────────────┐
                      │ STAGE 1: CONFIRMATORY KITCHEN TRIAL  │
                      │ (n = 4 Control vs n = 4 CAND-004)    │
                      └──────────────────┬───────────────────┘
                                         │
                                         ▼
                     ┌────────────────────────────────────────┐
                     │ PHYSICAL ACCEPTANCE GATES EVALUATION   │
                     │ - p < 0.005 (t >= 3.707)               │
                     │ - Cook Time <= 15.0 min (<= 3.5 wh)    │
                     │ - Recovery >= 95.5%                    │
                     │ - Hedonic Sensory >= 7.5/9.0           │
                     │ - Zero Soapy Off-Flavor                │
                     └──────────────────┬─────────────────────┘
                                        │
                       ┌────────────────┴────────────────┐
                       │                                 │
                 ALL GATES PASSED                 ANY GATE FAILED
                       │                                 │
                       ▼                                 ▼
         ┌───────────────────────────┐     ┌───────────────────────────┐
         │ STAGE 1: PASS             │     │ STAGE 1: REMEDIATE        │
         │ - Stage 2 Formally        │     │ - Stage 2 REMAINS LOCKED  │
         │   Unlocked for Pilot Fab  │     │ - Optimize dose / rinse   │
         └───────────────────────────┘     └───────────────────────────┘
```

**Conclusion:** Stage 2 remains locked until physical certificates are registered.

---

**Signed Off:**  
FinnoaQ Statistical Audit & Governance Panel  
*October 15, 2026*
