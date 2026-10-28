# CONDITIONAL ASSAY DECISION TREE: DECISION-GATED LAB SPENDING

**Project:** FinnoaQ Toor Dal Diagnostic R&D (Phase 1)  
**Objective:** Provide a formal logical decision tree that blocks unnecessary analytical spending.  
**Principle:** An expensive laboratory assay is authorized ONLY if a low-cost screening assay yields an ambiguous result.  

---

## 1. THE LOGICAL DECISION FLOW

```mermaid
graph TD
    START[Start: In-House Screening Tier 1] --> STEP1[Assay A2: Gravimetric Hydration Curve]

    STEP1 -->|Tanzanian Hydration < 70% of Indian| H_SLOW[Hydration Impeded]
    STEP1 -->|Tanzanian Hydration >= 85% of Indian| H_NORM[Hydration Normal: Cotyledon Permeable]

    H_SLOW --> COND_PORO[Conditional Test: Microscopy / Porosity]
    H_NORM --> STEP2[Assay A3: Ion-Exchange Bicarbonate Cook Test]

    STEP2 -->|Baking Soda Soak Cuts Cook Time to ~3 Whistles| CA_CONFIRMED[ROOT CAUSE CONFIRMED: Calcium-Pectate Cement]
    STEP2 -->|Baking Soda Soak Fails to Soften Grain| CA_REJECTED[Hypothesis H1 Rejected]

    CA_CONFIRMED --> STOP_SUCCESS[HALT LAB SPENDING: Problem Solved for ₹50]
    
    CA_REJECTED --> STEP3[Conditional Test: DSC Starch Gelatinization]
    STEP3 -->|Onset Temp > 75°C| STARCH_DEFECT[Starch Gelatinization Delay Confirmed]
    STEP3 -->|Onset Temp ~ 68°C| PROTEIN_MATRIX[Investigate Protein-Matrix Hydrophobicity]

    CA_CONFIRMED --> TIER2_OPTIONAL{Is Accredited Certificate Legally Required?}
    TIER2_OPTIONAL -->|No| SAVE_CAPITAL[Save 100% Capital for Hardware]
    TIER2_OPTIONAL -->|Yes| ACCRED_MIN[Order Minimal Moisture + ICP-OES: ₹4,500]
```

---

## 2. CONDITIONAL TRIGGER GATES

### Trigger 1: Hydration Divergence
- **Test:** In-house gravimetric water absorption curve ($M(t)$ at 25°C).
- **Trigger Condition:** If the 4-hour water uptake of Tanzanian dal is within 15% of the Indian benchmark, **IMMEDIATELY CANCEL all outsourced porosity, seed-coat, and SEM microscopy assays (Saving: ₹30,000)**.
- **Scientific Rationale:** If water physically enters the cotyledon, structural pores are open.

### Trigger 2: Ion-Exchange Softening Response
- **Test:** 0.75% Sodium bicarbonate ($\text{NaHCO}_3$) soak followed by boiling.
- **Trigger Condition:** If the pre-treated Tanzanian dal softens in $\le 25\text{ minutes}$ (or $\le 3.5\text{ whistles}$), **IMMEDIATELY CANCEL all outsourced pectin fractionation and HPLC phytic acid assays (Saving: ₹34,000)**.
- **Scientific Rationale:** Cleaving the ionic crosslinks with monovalent $\text{Na}^+$ proves that divalent pectate crosslinking was the sole bottleneck.

### Trigger 3: Failure of Ion-Exchange
- **Trigger Condition:** If and only if the bicarbonate-treated dal still takes $> 45\text{ minutes}$ to soften, authorize:
  1. *Differential Scanning Calorimetry (DSC)* for starch gelatinization enthalpy (Cost: ~₹5,000).
  2. *SDS-PAGE Cotyledon Protein Profiling* (Cost: ~₹6,000).
- **Status:** Currently **BLOCKED / DEFERRED** pending Tier 1 results.
