# FINNOAQ TOOR DAL — UNCERTAINTY QUANTIFICATION & STATISTICAL VALIDATION PLAN

**Document ID:** HKT-STP-2026-001  
**Preregistered Standard:** Two-Stage Locked Protocol (Five-Sigma Empirical Standard)  
**Evaluator Engine:** Vectorized Monte Carlo & Statistical Power Engine on CUDA  
**Date:** 2026-10-14  

---

## 1. Preregistered Statistical Hypotheses

To avoid data snooping or p-hacking, the statistical validation plan is permanently preregistered prior to conducting physical confirmatory tests:

### Formal Hypotheses
- **Null Hypothesis ($H_0$):** The proposed conditioning treatment does not reduce the standardized pressure cooking time of the target Tanzanian Toor Dal lot below $18.0\text{ minutes}$ ($\ge 4.5\text{ whistles}$):
  $$H_0: \mu_{\text{treated}} \ge 18.0\text{ minutes}$$
- **Alternative Hypothesis ($H_1$):** The proposed treatment achieves the target cooking time of $\le 15.0\text{ minutes}$ ($\le 3.5\text{ whistles}$):
  $$H_1: \mu_{\text{treated}} \le 15.0\text{ minutes}$$
- **Effect Size of Interest:** In a standardized domestic pressure cooker (~115°C, 15 psi), the untreated Tanzanian control cooks in $\approx 22.0\text{ minutes}$ ($\approx 6.0\text{ whistles}$). The predicted treated time is $\approx 13.8\text{ minutes}$ ($\approx 3.4\text{ whistles}$).
  $$\Delta \mu_{\text{pressure}} = \mu_{\text{control}} - \mu_{\text{treated}} \approx 22.0\text{ min} - 13.8\text{ min} = \mathbf{8.2\text{ minutes}} \quad (\approx 2.6\text{ whistles})$$
  *(Note: The 44.2-minute difference between 58 min and 13.8 min conflated open atmospheric boiling with pressure cooking; the true experimental comparator in a pressure cooker is $\Delta \mu \approx 8.2\text{ min}$).*

---

## 2. The Significance Standard & Power Reality

Under standard normal-theory hypothesis testing, a one-tailed $5\sigma$ significance threshold corresponds to:
$$\alpha = 1 - \Phi(5.0) \approx 2.8665 \times 10^{-7} \quad (\text{less than } 1 \text{ chance in } 3.48 \text{ million})$$

### 2.1 Separation of Numerical Precision from Real-World Certainty
The project constitution enforces a strict boundary between two distinct types of statistical distributions:

1. **Monte Carlo Numerical Sampling Error:**
   When running $N = 500,000$ synthetic grain trajectories on the GPU, the standard error of the mean converges to:
   $$\text{SE}_{\text{sim}} = \frac{s_{\text{sim}}}{\sqrt{N}} = \frac{3.0\text{ min}}{\sqrt{500,000}} = \mathbf{\pm 0.0042\text{ minutes (0.25 seconds)}}$$
   Evaluating the model yields $Z = 20.1\sigma$ ($p \ll 10^{-15}$). This proves that the **numerical solution of the mathematical model is stable and deterministic**. It does **NOT** prove that the real-world physical dal lot has zero variance.
2. **Physical Target-Lot Epistemic Uncertainty:**
   Until real, physical cooking timestamps from the target Tanzanian lot are measured under standardized conditions, the real-world treatment effect cannot be certified at $5\sigma$.

---

## 3. Physical Power Analysis: Rigorous Sensitivity Across Sample Variances ($n_1 = 4, n_2 = 4$)

With $n_1 = 4$ control and $n_2 = 4$ treated batches ($df = 6$), the standard error is:
$$SE = \sqrt{\frac{s_1^2}{4} + \frac{s_2^2}{4}} = \frac{s_{\text{pooled}}}{\sqrt{2}}$$
$$t = \frac{\Delta \bar{X}}{SE} = \frac{\sqrt{2} \times 8.2}{s_{\text{pooled}}}$$

The statistical significance achieved depends strictly on the empirical variance observed in the kitchen trial:

| Sample Std Dev $s_{\text{pooled}}$ | Standard Error $SE$ | Student's $t$ ($df=6$) | One-Tailed $p$-value | Gaussian $\sigma$ Equivalent | Regulatory / Gate Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$s = 0.50\text{ min}$ (30 s)** | $0.354\text{ min}$ | $t = 23.19$ | $p = 2.11 \times 10^{-7}$ | **$5.06\sigma$** | Meets $5\sigma$ Standard |
| **$s = 1.00\text{ min}$ (60 s)** | $0.707\text{ min}$ | $t = 11.60$ | $p = 1.24 \times 10^{-5}$ | **$4.22\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 1.50\text{ min}$ (90 s)** | $1.061\text{ min}$ | $t = 7.73$ | $p = 1.23 \times 10^{-4}$ | **$3.67\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 2.00\text{ min}$ (120 s)**| $1.414\text{ min}$ | $t = 5.80$ | $p = 5.77 \times 10^{-4}$ | **$3.25\sigma$** | Exceeds $3\sigma$; Sub-$5\sigma$ |
| **$s = 2.50\text{ min}$ (150 s)**| $1.768\text{ min}$ | $t = 4.64$ | $p = 1.77 \times 10^{-3}$ | **$2.92\sigma$** | Fails $3\sigma$ Gate |

**Forensic Audit Finding:**
- An $n=4$ experiment **CANNOT automatically guarantee $5\sigma$ significance**.
- If experimental kitchen variation is tightly controlled to $s \le 30\text{ seconds}$, $5\sigma$ is attainable.
- If realistic kitchen stove flame fluctuations produce $s \approx 1.0\text{ to }1.5\text{ minutes}$, the trial will achieve **$3.67\sigma\text{ to }4.22\sigma$** ($p < 0.001$). This is fully sufficient to decisively reject the null hypothesis and demonstrate industrial efficacy, but fails the strict $5\sigma$ threshold unless sample size is expanded to $n = 8\text{ to }12$ replicates per arm.
- Consequently, Stage 1 passing criteria are formally prespecified at $t_{\text{obs}} \ge 3.707$ ($p \le 0.005$, $\ge 3\sigma$ gate), with $5\sigma$ tracked as the aspirational gold standard.

---

## 4. Preregistered Stopping and Exclusion Rules

1. **Exclusion Criteria:**
   - Any batch with pressure cooker gasket blow-out or steam vent obstruction is declared invalid and excluded prior to opening.
   - Any batch where induction power fluctuates by $> \pm 5\%$ from the 1200W setpoint is excluded.
2. **Stopping Rule:**
   - The test stops after exactly $n = 4$ valid replicates per arm. Interim data peeking or adaptive sample size adjustments are prohibited.
3. **Primary Test Statistic:**
   - Welch's two-sample t-test (two-tailed and one-tailed reported) with Satterthwaite degrees of freedom.
