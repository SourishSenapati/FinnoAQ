# HARAKUTIR TOOR DAL — STAGE 1 VALIDATION REPORT

**Document ID:** HKT-STG1-2026-001  
**Project Phase:** Stage 1 — Discovery & Experimental Proof  
**Controlling Standard:** Master Directive Part VI (Two-Stage Lock Protocol) & [`AUDIT_DIRECTIVE.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/AUDIT_DIRECTIVE.md)  
**Date:** 2026-10-14  
**Audit Status:** AUDITED & RECONCILED (See [`AUDIT_CHALLENGE_AND_DEFECT_RESOLUTIONS.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/AUDIT_CHALLENGE_AND_DEFECT_RESOLUTIONS.md))  

---

## 1. Formal Stage 1 Decision Status

$$\mathbf{STAGE\ 1\ STATUS:\ PROMISING\_UNCONFIRMED\ (STAGE\ 2\ STRICTLY\ LOCKED)}$$

### Decision Justification & Forensic Audit Compliance
1. **Computational Proposal:** Coupled multiphysics modeling, mass/energy balances, and kinetic simulations predict that Candidate A2 (CAND-004: $0.50\%$ NaHCO₃, $1.5:1$ liquor ratio, $30\text{ min}$ soak) reduces domestic pressure cooking time from **$\approx 22.0\text{ minutes}$ ($\approx 6\text{ whistles}$) down to $\approx 13.8\text{ minutes}$ ($\approx 3.4\text{ whistles}$)** with **$98.54\%$ nominal dry-solids recovery**.
2. **Out-of-Sample Empirical Literature Validation:** The model predicts cooking times of 6 independent pigeon pea cultivars from Machinjili et al. (2025) with **$< 5.0\%$ out-of-sample error** without re-tuning.
3. **Non-Negotiable Gating Principle:** Under the project constitution, **simulated Monte Carlo samples cannot substitute for physical laboratory measurements on the real physical target Tanzanian lot**. Because physical sample certificates on the target lot remain pending, awarding `PASS` would violate scientific truth.
4. **Retraction of Automatic Unlock Claim:** The prior assertion that entering 4 control and 4 treatment timestamps would "automatically establish five-sigma significance and unlock Stage 2" is **formally retracted**. Passing Stage 1 is conditional on the observed effect size ($\Delta \bar{X}$) and observed variability ($s$) satisfying the prespecified hypothesis test, alongside meeting all sensory, yield, and safety acceptance gates.

---

## 2. Predefined Stage 1 Acceptance Gate Evaluation

| Stage 1 Preregistered Acceptance Gate | Target Threshold | Modeled Candidate A2 Value | Current Empirical Status | Gate Decision |
| :--- | :--- | :--- | :--- | :--- |
| **G1: Primary Cooking Endpoint** | $\le 15.0\text{ min}$ ($\le 3.5\text{ whistles}$) | **13.8 min (3.4 whistles)** | Pending physical kitchen test | **GATED** |
| **G2: Minimum Dry-Solids Recovery**| $\ge 95.5\%$ (Target $\ge 98.0\%$) | **98.54%** ($1.46\%$ loss) | Validated in mass balance model | **PASSED (MODEL)**|
| **G3: Retained Chemical / Sodium** | $< 350.0\text{ mg Na / 100g dal}$ | **53.9 mg Na** (mist rinse) / **6.4 mg Na** (counter-current) | Reconciled across both rinse modes | **PASSED (MODEL)**|
| **G4: Sensory / Mouthfeel** | Score $\ge 7.5 / 9.0$; zero soapy note| **8.4 / 9.0 (Hedonic score)** | Tested in virtual sensory model | **PASSED (MODEL)**|
| **G5: Statistical Significance** | One-sided $p < 0.001$ ($\ge 3.0\sigma$; target $5.0\sigma$)| **Conditional on observed $s$** ($s \le 0.5\text{ min} \implies 5.06\sigma$; $s = 1.0\text{ min} \implies 4.22\sigma$)| Empirical data pending | **GATED** |
| **G6: Capital Preservation** | Zero waste on unnecessary CRO labs | **₹1.98 Lakh Preserved** | In-house protocol selected (₹50) | **PASSED** |

---

## 3. Preregistered Statistical Decision Rule for Kitchen Protocol

For the 4-arm standardized kitchen trial ($n_{\text{control}} = 4, n_{\text{treated}} = 4, df = 6$):
$$\Delta \bar{X} = \bar{X}_{\text{control}} - \bar{X}_{\text{treated}}$$
$$t_{\text{obs}} = \frac{\Delta \bar{X}}{\sqrt{\frac{s_1^2}{4} + \frac{s_2^2}{4}}}$$

- **Stage 1 `PASS` Condition:**
  1. $t_{\text{obs}} \ge 3.707$ (one-tailed $p \le 0.005$, equivalent to $\ge 3.0\sigma$ statistical standard).
  2. $\bar{X}_{\text{treated}} \le 15.0\text{ minutes}$ ($\le 3.5\text{ whistles}$).
  3. Measured dry-solids recovery $\ge 95.5\%$.
  4. Blind hedonic sensory evaluation score $\ge 7.5 / 9.0$ with zero alkaline off-flavor notes.
- **Stage 1 `FAIL` / Remediation Condition:**
  If $t_{\text{obs}} < 3.707$, or if sensory score $< 7.5$, Candidate A2 will be rejected or re-optimized, and Stage 2 will remain strictly locked.

---

## 4. Recommended Immediate Action

Execute the standardized kitchen protocol documented in [`reports/EXPERIMENTAL_PROTOCOL.md`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/EXPERIMENTAL_PROTOCOL.md). 

Upon data ingestion, the statistical engine will compute the exact empirical test statistic and gate evaluation. Stage 2 industrial scale-up remains locked until all acceptance criteria are empirically satisfied.
