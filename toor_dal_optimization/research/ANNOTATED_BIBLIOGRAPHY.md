# ANNOTATED BIBLIOGRAPHY & SCIENTIFIC EVIDENCE REGISTER

**Project:** Harakutir Autonomous Pulse Engineering (Tanzanian Toor Dal vs Indian Benchmark)  
**Standard:** Ocean Boiling Protocol v3.0 | Harakutir Omega v4  
**Date:** October 2026  
**Scope:** Open-Access Literature, Authoritative Regulatory Compendia, and Public Datasets  

---

## 1. Direct *Cajanus cajan* Evidence

### SRC_001: Physicochemical and Cooking Properties of Six Pigeon Pea (*Cajanus cajan* L) Genotypes from Malawi
- **Citation:** Machinjili, T.T., et al. (2025). *Frontiers in Sustainable Food Systems*, 9, 1613117. DOI: [10.3389/fsufs.2025.1613117](https://doi.org/10.3389/fsufs.2025.1613117).
- **Evidence Class:** `DIRECT_CAJANUS_EVIDENCE`
- **Study Material:** Six pigeon pea genotypes grown in Malawi: *Kachangu* (ICEAP 00040), *Mwaiwathualimi* (ICEAP 00557), *Chitedze 1* (ICEAP 01514/15), *Sauma* (ICP 9145), *Mthawajuni*, and *ICPL 93026*. Tested in both whole and dehulled (cotyledon) states.
- **Key Findings & Measured Values:**
  - **Whole seed cooking time:** 97.0 to 193.0 minutes in open boiling.
  - **Dehulled split cotyledon cooking time:** 26.0 to 54.0 minutes in open boiling.
  - **Dehulling effect:** Removing the seed coat accelerated hydration and reduced cooking time by ~66% across varieties.
  - **Seed-coat thickness:** Ranged from 40 to 60 $\mu\text{m}$. Surprisingly, seed coat thickness had *no statistically significant correlation* ($p > 0.05$) with cooking time or water absorption rate.
  - **Moisture content:** 8.5% to 11.2% dry basis.
  - **Crude protein:** 19.8% to 23.4% (Kjeldahl, $N \times 6.25$).
- **Significance for Tanzanian Toor Dal Project:**
  - Confirms that Tanzanian/East African ICRISAT-derived lines (ICEAP series) exhibit inherently prolonged cotyledon cooking times (up to 54 minutes dehulled) even after dehulling.
  - Demonstrates that prolonged cooking is driven by the **cotyledon cell wall / middle lamella matrix**, not merely the presence or thickness of the seed coat.
- **Model Conversion Parameters:**
  - Baseline untreated dehulled cooking time range: $t_{\text{cook, untreated}} \in [26.0, 54.0]\text{ min}$ (mean $\approx 40.0\text{ min}$ in open boil; corresponds to $\sim 28\text{ min}$ / 6 whistles in domestic pressure cooker).
  - Rate constant: $k_{\text{soft, untreated}} \approx 0.00067\text{ s}^{-1}$.

---

## 2. Hard-to-Cook (HTC) Biochemical Mechanism Evidence

### SRC_003: Insight into Pectin-Cation-Phytate Theory of Hardening in Common Bean Varieties
- **Citation:** Wainaina, I.N., Lugumira, R., Wafulu, E.N., Kyomugasho, C., Sila, D.N., Hendrickx, M. (2022). *Food Research International*, 151, 110862. DOI: [10.1016/j.foodres.2021.110862](https://doi.org/10.1016/j.foodres.2021.110862).
- **Evidence Class:** `RELATED_PULSE_EVIDENCE` (Transfer prior from *Phaseolus vulgaris*)
- **Study Material:** Common bean varieties stored under adverse aging conditions (35°C, 80% RH).
- **Key Findings & Mechanistic Insights:**
  - Hydrolysis of phytate (inositol hexaphosphate, $\text{InsP}_6$) during warm/humid storage liberates divalent cations ($\text{Ca}^{2+}$ and $\text{Mg}^{2+}$).
  - Liberated cations migrate to the middle lamella where they cross-link de-esterified pectin chains ($DE < 50\%$).
  - Forms insoluble calcium pectate gel "egg-box" structures that resist thermal solubilization during cooking, preventing cell separation and causing the Hard-to-Cook defect.
- **Transferability Limitation:**
  - Demonstrated rigorously on common beans (*Phaseolus vulgaris*). Must be classified as a transfer prior, not direct empirical proof for *Cajanus cajan*.

### SRC_004: Microscopic Evidence for Pectin Changes in Hard-to-Cook Development
- **Citation:** Chen, D., Pham, U., Van Loey, A.V., Grauwet, T., Hendrickx, M.E. (2021). *Food Research International*, 140, 110115. DOI: [10.1016/j.foodres.2021.110115](https://doi.org/10.1016/j.foodres.2021.110115).
- **Evidence Class:** `RELATED_PULSE_EVIDENCE`
- **Key Findings:**
  - Immunocytochemical staining with LM19 and LM20 monoclonal antibodies proved un-esterified homogalacturonan accumulates specifically at cell corners and middle lamella.
  - Middle lamella fails to dissolve during cooking at 100°C in HTC beans, whereas normal beans show complete middle lamella dissolution and cell separation within 30 minutes.

### SRC_005: In Situ Cell Wall Associated Mineral Quantification in Red Haricot Beans
- **Citation:** Chen, D., Bernaerts, T., Debon, S., Oduah, C.O., Zhu, L., Wallecan, J., Hendrickx, M., Kyomugasho, C. (2023). *Food Research International*, 164, 112349. DOI: [10.1016/j.foodres.2022.112349](https://doi.org/10.1016/j.foodres.2022.112349).
- **Evidence Class:** `RELATED_PULSE_EVIDENCE`
- **Key Findings:**
  - SEM-EDS demonstrated that calcium concentration specifically within the middle lamella increases by up to 2.4× in hard-cooking beans relative to soft beans.

---

## 3. Official Regulatory & Quality Standards

### SRC_008: FSSAI Food Products Standards and Food Additives Regulations, 2011 (§2.4 Pulses)
- **Authority:** Food Safety and Standards Authority of India (FSSAI).
- **Evidence Class:** `OFFICIAL_REGULATORY_SOURCE`
- **Applicable Product Format:** Dehulled and split Toor Dal / Red Gram (*Cajanus cajan*).
- **Mandatory Release Specifications:**
  - Moisture Content: **Maximum 14.0% (m/m)**.
  - Foreign Matter: **Maximum 1.0% (m/m)** (inorganic matter $\le 0.25\%$).
  - Other Edible Grains: **Maximum 3.0% (m/m)**.
  - Damaged / Discoloured Grains: **Maximum 5.0% (m/m)**.
  - Weevilled Grains: **Maximum 3.0% (m/m)**.
  - Uric Acid: **Maximum 100 mg/kg**.
  - Total Aflatoxins ($B_1+B_2+G_1+G_2$): **Maximum 15 $\mu\text{g/kg}$ (ppb)**.
  - Food Additives: No artificial colours, mineral oil polishing, or non-permitted additives permitted.

---

## 4. Machine Learning & Meta-Exploration Frameworks

### SRC_006: Dream-RSI: Recursive Self-Improvement through Evolving Worlds
- **Citation:** Zheng, T., Wu, X., Zhang, Z., Kang, W.C., Huang, H. (2024). arXiv:2609.14858 [cs.LG].
- **Evidence Class:** `ENGINEERING_CORRELATION` (Methodology)
- **Core Concept:**
  - Uses the historical exploration DAG / tree as a replay simulator ("dreaming") to test alternative search policies offline, vastly reducing expensive online evaluation calls.
- **Implementation Classification in Harakutir:**
  - Classified explicitly as `DREAM_RSI_INSPIRED`. Uses `state/discovery_tree.json` to evaluate exploration policies against historical baselines.

---

## 5. Public Composition & Market Data

### SRC_009: FAOSTAT Agricultural Production and Trade Database
- **Citation:** Food and Agriculture Organization (FAO), 2024.
- **Evidence Class:** `OFFICIAL_STATISTICAL_DATA`
- **Findings:**
  - Tanzania produces ~250,000–320,000 MT of pigeon pea annually, with >80% exported to India.
  - Port of Dar es Salaam landed CIF price in Mumbai historically trades at a ₹15–22/kg discount against domestic Indian Desi varieties (Latur / Gulbarga).

### SRC_010: USDA FoodData Central (FDC ID: 172431)
- **Citation:** USDA Agricultural Research Service (2019). *Pigeon peas, mature seeds, raw*.
- **Evidence Class:** `GENERAL_FOOD_SCIENCE`
- **Composition Baseline:**
  - Energy: 343 kcal/100g | Protein: 21.7 g/100g | Total lipid: 1.49 g/100g | Carbohydrate: 62.78 g/100g | Calcium: 130 mg/100g | Iron: 5.23 mg/100g | Potassium: 1392 mg/100g.
  - Strictly classified as reference composition, not lot-specific assay of Harakutir Tanzanian samples.
