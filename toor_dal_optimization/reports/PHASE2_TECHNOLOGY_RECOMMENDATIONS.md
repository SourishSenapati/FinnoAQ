# Harakutir Phase 2 Technology Recommendations & Candidate Matrices

**Date:** 15 October 2026  
**Governing SOW Section:** Section 18 (Candidate Technology Families)  
**Status:** `PRELIMINARY_NOT_OPTIMIZED`  

---

### 1. Overview & Scope Boundaries
In strict accordance with SOW Section 18 and Section 32:
- Phase 1 is a **diagnostic study** to identify root causes and rate-limiting bottlenecks.
- Commercial optimization, full pilot production, and shelf-life validation are **excluded from Phase 1**.
- The technologies detailed below are **candidate interventions** whose final selection is contingent on the empirical root cause diagnosed from laboratory data.

---

### 2. Candidate Technology Families (§18)
#### Controlled Hydration / Tempering (§18.1) (ID: `TREAT_01_TEMPERING`)
- **Target Mechanism:** Water penetration and moisture distribution
- **Hypothesized Effect:** Accelerates initial hydration core saturation (Hypothesis)
- **Technical & Quality Risks:** Microbial proliferation during wet resting; drying energy demand
- **Estimated Preliminary Lab Screening Cost:** ₹12,000.00
- **Candidate Conditions Grid:**
  ```json
  [
  {
    "moisture_target_pct": 20.0,
    "temp_c": 25.0,
    "rest_time_h": 4.0
  },
  {
    "moisture_target_pct": 30.0,
    "temp_c": 40.0,
    "rest_time_h": 2.0
  }
]
  ```

#### Hydrothermal Pre-Treatment (§18.2) (ID: `TREAT_02_HYDROTHERMAL`)
- **Target Mechanism:** Cell-wall softening and pre-gelatinization
- **Hypothesized Effect:** Relaxes pectin matrix before consumer cooking (Hypothesis)
- **Technical & Quality Risks:** Overcooking, starch leaching, case hardening
- **Estimated Preliminary Lab Screening Cost:** ₹15,000.00
- **Candidate Conditions Grid:**
  ```json
  [
  {
    "steam_pressure_kpa": 50.0,
    "exposure_time_min": 5.0
  },
  {
    "steam_pressure_kpa": 100.0,
    "exposure_time_min": 3.0
  }
]
  ```

#### Food-Grade Conditioning (§18.4) (ID: `TREAT_03_CHELATING_CONDITIONING`)
- **Target Mechanism:** Disruption of Ca2+/Mg2+ pectin ionic bridges
- **Hypothesized Effect:** Sequester divalent cations, solubilizing middle lamella pectin (Hypothesis)
- **Technical & Quality Risks:** Sensory astringency, regulatory sodium labeling, rinse requirements
- **Estimated Preliminary Lab Screening Cost:** ₹18,000.00
- **Candidate Conditions Grid:**
  ```json
  [
  {
    "agent": "Sodium citrate",
    "concentration_pct": 0.5,
    "soak_time_min": 30.0
  },
  {
    "agent": "Sodium hexametaphosphate (SHMP)",
    "concentration_pct": 0.25,
    "soak_time_min": 30.0
  }
]
  ```

#### Targeted Thermal Pre-Treatment (§18.3) (ID: `TREAT_04_IR_MICRONIZATION`)
- **Target Mechanism:** Flash moisture vapor micro-fissuring of cotyledon
- **Hypothesized Effect:** Generates micro-channels bypassing pectin mass transfer resistance (Hypothesis)
- **Technical & Quality Risks:** Surface scorching, protein denaturation, flavour degradation
- **Estimated Preliminary Lab Screening Cost:** ₹25,000.00
- **Candidate Conditions Grid:**
  ```json
  [
  {
    "ir_temp_c": 175.0,
    "residence_time_sec": 45.0,
    "feed_moisture_pct": 25.0
  },
  {
    "ir_temp_c": 185.0,
    "residence_time_sec": 60.0,
    "feed_moisture_pct": 30.0
  }
]
  ```

---

### 3. Competing Hypotheses & Refutation Signals

#### `H1_Hydration_Barrier`: Mass transfer resistance at surface/cotyledon limits initial water uptake
- **Discriminating Assays:** Hydration kinetics at 25°C & 60°C, WAI, Peleg k1
- **Indicative Analytical Cost:** ₹10,000.00
- **Refutation Condition:** If Tanzanian dal reaches full hydration in <60 min but still fails to soften under pressure cooking.

#### `H2_Seed_Coat_Resistance`: Residual testa or cuticular wax layer retards water ingress
- **Discriminating Assays:** Optical / SEM microscopy, Dehulled vs intact cotyledon hydration
- **Indicative Analytical Cost:** ₹8,000.00
- **Refutation Condition:** If completely dehulled split cotyledons exhibit identical cooking delay as partially dehulled dal.

#### `H3_Pectin_Divalent_Crosslinking`: Free Ca2+/Mg2+ crosslinks de-esterified pectin in the middle lamella, preventing thermal cell separation
- **Discriminating Assays:** Pectin fractionation (WSP/CSP), ICP-OES Ca/Mg, Phytate:Ca molar ratio
- **Indicative Analytical Cost:** ₹34,000.00
- **Refutation Condition:** If chelating agents (EDTA/citrate) do not reduce cooking time, or if Phytate:Ca ratio is > 1.0.

#### `H4_Starch_Thermal_Barrier`: Elevated starch gelatinization temperature or restricted swelling requires prolonged heat
- **Discriminating Assays:** DSC gelatinization onset/enthalpy, RVA pasting profile
- **Indicative Analytical Cost:** ₹25,000.00
- **Refutation Condition:** If DSC peak temperature Tp is identical (<1°C difference) between Tanzanian and Indian dal.

#### `H5_Storage_Induced_HTC`: Warm, humid maritime transit induced enzymatic hard-to-cook defect
- **Discriminating Assays:** Storage history correlation, Controlled aging trial
- **Indicative Analytical Cost:** ₹15,000.00
- **Refutation Condition:** If newly harvested fresh Tanzanian dal shows identical cooking resistance before oceanic transit.
