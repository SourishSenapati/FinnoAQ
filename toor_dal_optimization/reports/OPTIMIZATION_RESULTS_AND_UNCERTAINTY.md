# HARAKUTIR TOOR DAL — OPTIMIZATION RESULTS & UNCERTAINTY ANALYSIS

**Document ID:** FIN-OPT-UNCERT-2026-002  
**Date:** 15 October 2026  
**Governing Standard:** Master Build Directive — Phase 4 Closed-Loop Modeling & Candidate Ranking  
**Status:** **NO VALIDATED WINNER (ALL TREATED CANDIDATES ARE COMPUTATIONAL HYPOTHESES)**  

---

## 1. Governance Declaration & Non-Negotiable Verdict

> [!CAUTION]
> ### FORMAL STATUS: NO VALIDATED WINNER
> In strict compliance with the project constitution and the Master Build Directive, **there is currently NO VALIDATED WINNER** for the Harakutir Toor Dal cooking-time optimization.
>
> Although computational simulations, multiscale models, and literature heuristics identify promising formulations, **zero target-lot physical kitchen experiments have been conducted**. No prompt, passing unit test, GPU run, or synthetic surrogate can substitute for empirical evidence. Every treated candidate remains classified as a `COMPUTATIONAL_HYPOTHESIS`.
>
> **Stage 2 (15 MT/day industrial plant engineering) is strictly locked** and will not unlock until Stage 1 physical confirmatory data satisfies all acceptance gates.

---

## 2. Constrained Multi-Objective Pareto Analysis

Rather than relying on arbitrary weighting functions that can be manipulated to favor a predetermined candidate, treatment options are evaluated using **constrained Pareto optimization**:

### Hard Feasibility Constraints (Non-Negotiable Filters)
1. **Regulatory Legality (FSSAI):** Reagent must be permitted under FSSAI Table 3 (GMP) or Food Additive regulations; residual sodium must not exceed $350.0\text{ mg / 100g}$.
2. **Whole-Plant Dry Solids Recovery:** Net solids yield must be $\ge 95.5\%$ (maximum allowable leaching + mechanical loss is $4.5\%$).
3. **Sensory Threshold:** Cooked dal must not exhibit soapy taste, acid sourness, or gray discoloration (hedonic score $\ge 7.5 / 9.0$).
4. **Economic Margin:** Net incremental processing OpEx must be $\le \text{₹}2.00\text{ per kg}$ of saleable packaged dal.

### Candidate Ranking & Constraint Filter Table

| Candidate ID | Treatment Description | Reagent & Dose | Soak Time | Pred. Cook Time (min) | Pred. Whistles | Whole-Plant Recovery (%) | Retained Na (mg/100g) | Net OpEx (₹/kg) | Sensory Score | Constraint Status | Pareto Classification | Evidence Status | Stage 1 Decision |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CAND-001** | Untreated Raw Tanzanian Dal | Potable Water ($0\%$) | $0\text{ min}$ | **$22.0$** | **$6.0$** | $95.69\%$ | $0.0$ | ₹0.957 | $7.5$ | Fails cooking target | Reference Baseline | `COMPUTATIONALLY_VERIFIED` | Baseline Control |
| **CAND-004** | Nominal Sodium Bicarbonate | Food-Grade $\text{NaHCO}_3$ ($0.50\%$) | $30\text{ min}$ | **$13.8$** | **$3.1$** | $95.69\%$ | $53.9$ | ₹1.336 | $8.4$ | **Satisfies All Gates** | **Pareto Front (Lowest Cost)** | `COMPUTATIONAL_HYPOTHESIS` | **Advance to Kitchen Protocol** |
| **CAND-006** | Gourmet Sodium Citrate | Trisodium Citrate ($0.50\%$) | $30\text{ min}$ | **$14.6$** | **$3.4$** | $95.69\%$ | $17.5$ | ₹1.643 | $8.8$ | **Satisfies All Gates** | **Pareto Front (Highest Sensory)** | `COMPUTATIONAL_HYPOTHESIS` | **Advance as Strong Alt.** |
| **CAND-003** | Low-Dose Sodium Bicarbonate | Food-Grade $\text{NaHCO}_3$ ($0.25\%$) | $30\text{ min}$ | $18.2$ | $4.5$ | $95.69\%$ | $26.9$ | ₹1.202 | $8.2$ | Misses $\le 15\text{ min}$ target | Dominated by CAND-004 | `COMPUTATIONAL_HYPOTHESIS` | Retain as Screening Point |
| **CAND-002** | Plain Thermal Water Soak | Potable Water ($45^\circ\text{C}$) | $60\text{ min}$ | $20.5$ | $5.2$ | $95.69\%$ | $0.0$ | ₹1.050 | $7.0$ | Misses $\le 15\text{ min}$ target | Dominated by CAND-004 | `COMPUTATIONAL_HYPOTHESIS` | Retain as Thermal Control |
| **CAND-005** | High-Dose Sodium Bicarbonate | Food-Grade $\text{NaHCO}_3$ ($1.25\%$) | $30\text{ min}$ | $11.2$ | $2.3$ | $92.30\%$ | $118.5$ | ₹1.736 | $5.2$ | **Violates Yield & Sensory** | **REJECTED (Hard Gate)** | `COMPUTATIONAL_HYPOTHESIS` | Rejected (Saponification) |
| **CAND-008** | Acidified Citric Acid Soak | Citric Acid ($0.50\%$) | $30\text{ min}$ | $28.0$ | $7.5$ | $94.20\%$ | $0.0$ | ₹1.336 | $4.2$ | **Violates Time & Sensory** | **REJECTED (Hard Gate)** | `COMPUTATIONAL_HYPOTHESIS` | Rejected (Pectin Crosslink) |
| **CAND-009** | Enzymatic Pectinase Pretreatment | Food Pectinase ($0.10\%$) | $60\text{ min}$ | $14.2$ | $3.2$ | $94.50\%$ | $10.8$ | ₹85.96 | $7.8$ | **Violates Cost Constraint** | **REJECTED (Hard Gate)** | `COMPUTATIONAL_HYPOTHESIS` | Rejected (₹86/kg Prohibitive) |
| **CAND-010** | High-Temperature Parboiling | Steam/Water ($95^\circ\text{C}$) | $10\text{ min}$ | $16.5$ | $4.0$ | $89.50\%$ | $0.0$ | ₹1.050 | $6.0$ | **Violates Yield Constraint** | **REJECTED (Hard Gate)** | `COMPUTATIONAL_HYPOTHESIS` | Rejected (7.6% Leaching) |

---

## 3. The Leading Pareto Hypotheses

Two distinct formulation hypotheses form the Pareto-optimal frontier and advance to the physical kitchen trial:

```
                                  [ THE PARETO OPTIMAL FRONTIER ]
                                                 ▲
                    SENSORY QUALITY (1-9)        │
                                                 │       ★ CAND-006 (Sodium Citrate)
                                            8.8  │         [Score 8.8, 14.6 min, ₹1.64/kg]
                                                 │
                                            8.4  │   ★ CAND-004 (Sodium Bicarbonate)
                                                 │     [Score 8.4, 13.8 min, ₹1.34/kg]
                                                 │
                                            7.5  │ ■ CAND-001 (Untreated Baseline)
                                                 │   [Score 7.5, 22.0 min, ₹0.96/kg]
                                                 │
                                                 └──────────────────────────────────────►
                                                   0.90      1.20      1.50      1.80
                                                          NET OPEX (₹/kg Dal)
```

1. **Candidate CAND-004 (Cost-Minimizing Winner Hypothesis):**
   - *Reagent:* Food-Grade Sodium Bicarbonate ($\text{NaHCO}_3$, $0.50\%\ \text{w/w}$ in liquor, $1:1.5$ ratio, $30\text{ min}$ ambient soak).
   - *Predicted Cook Time:* $13.8\text{ minutes}$ ($\approx 3.1\text{ whistles}$), a $43\%$ reduction over baseline.
   - *Net OpEx:* **₹1.336 per kg** saleable dal (chemical ₹0.275 + biomass drying ₹0.582 + utilities ₹0.203 + labor ₹0.118 + CIP/QC ₹0.158).
   - *Sensory:* $8.4 / 9.0$ (clean, traditional yellow appearance, creamy texture).
   - *Retained Sodium:* $53.9\text{ mg Na / 100g dal}$ (84.6% margin below FSSAI threshold).

2. **Candidate CAND-006 (Sensory-Maximizing Alternative Hypothesis):**
   - *Reagent:* Food-Grade Trisodium Citrate ($\text{Na}_3\text{C}_6\text{H}_5\text{O}_7$, $0.50\%\ \text{w/w}$ in liquor, $1:1.5$ ratio, $30\text{ min}$ ambient soak).
   - *Predicted Cook Time:* $14.6\text{ minutes}$ ($\approx 3.4\text{ whistles}$).
   - *Net OpEx:* **₹1.643 per kg** saleable dal (higher reagent price: ₹95/kg vs ₹35/kg).
   - *Sensory:* $8.8 / 9.0$ (superior flavor stability; citrate acts as mild antioxidant preventing lipid oxidation).
   - *Retained Sodium:* $17.5\text{ mg Na / 100g dal}$ (95.0% margin below FSSAI threshold).

---

## 4. Parameter Sensitivity & Uncertainty Propagation

Uncertainty in key physical parameters propagates into cooking time and process economics. A Monte Carlo sensitivity analysis ($N = 10,000$ draws) across parameter uncertainty ranges reveals the primary project risks:

| Input Parameter | Nominal Value | 95% Credible Interval | Dominant Physical Impact | Cooking Time Sensitivity ($\partial t / \partial \theta$) | OpEx Sensitivity ($\partial \text{Cost} / \partial \theta$) | Action to Reduce Variance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cotyledon Half-Thickness ($H$)** | $1.30\text{ mm}$ | $[1.18, 1.45]\text{ mm}$ | Fickian diffusion time $\tau \propto H^2$ | $+3.8\text{ min / mm}$ | Neutral | Pre-screen incoming grain by thickness sieve. |
| **Initial Calcium Content ($[\text{Ca}^{2+}]$)** | $1.40\text{ mg/g}$ | $[0.95, 2.10]\text{ mg/g}$ | Degree of pectin crosslinking | $+2.4\text{ min / (mg/g)}$ | Neutral | Run rapid EDTA/AAS assay on each incoming lot. |
| **Water Uptake in Soak ($\Delta M$)** | $0.225\text{ kg/kg}$ | $[0.18, 0.28]\text{ kg/kg}$ | Water to evaporate in dryer | Neutral | **$+₹0.18\text{/kg per } 0.05\text{ kg/kg}$** | Strictly control soak time to exactly $30\text{ min}$. |
| **Biomass Steam Tariff** | ₹0.55 / MJ | $[0.40, 0.85]\text{ ₹/MJ}$ | Fluid-bed thermal drying cost | Neutral | **$+₹0.28\text{/kg per } 0.30\text{ ₹/MJ}$** | Long-term fuel briquette supply agreement. |
| **Wash Leaching Loss ($L_{\text{wash}}$)** | $1.46\%$ | $[1.10, 3.20]\%$ | Dry solids loss to effluent | Neutral | **$+₹0.22\text{/kg per } 1.0\%\ \text{loss}$** | Optimize gentle agitation and liquor drainage. |

---

## 5. Conclusion & The Next Decisive Step

Computational modeling has answered all questions that can be answered without physical beans. The theoretical formulations, mass balances, and cost boundaries are settled. 

**The single remaining dependency is the execution of the 8-batch physical kitchen trial** specified in [EXPERIMENTAL_SCREENING_AND_CONFIRMATION_PROTOCOL.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/reports/EXPERIMENTAL_SCREENING_AND_CONFIRMATION_PROTOCOL.md). Once physical timestamps and texture measurements are logged, the true statistical significance will be calculated and the winning treatment officially validated.
