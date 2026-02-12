# MASTER FORMULATION & PROCESS GUIDE: FINNO PROJECTS

_Technical Specifications for Six Sigma Manufacturing_

This document reveals the exact compositions, process parameters, and scientific logic used in the Digital Twin simulations to achieve consistent, high-fidelity results. **All parameters are derived from valid food physics (e.g., Avrami equation, Arrhenius kinetics).**

---

## 1. TOOR DAL ANALOGUE (Reconstituted Legume)

**Goal:** Create a uniform, quick-cooking dal with natural texture using plant proteins and starches.

### A. Raw Material Composition (% w/w)

| Ingredient              | Composition | Function                                                 |
| :---------------------- | :---------- | :------------------------------------------------------- |
| **Pea Protein Isolate** | **23.5%**   | Primary protein source (Amino acid profile matching).    |
| **Native Corn Starch**  | **65.0%**   | Structural filler (Provides bulk density & texture).     |
| **Sodium Alginate**     | **1.2%**    | Gelling Agent (Reacts with Calcium).                     |
| **Calcium Lactate**     | **0.6%**    | Cross-linking Agent (Creates "Skin" via Spherification). |
| **Turmeric Extract**    | **0.1%**    | Natural Color (Curcumin).                                |
| **Water**               | **Balance** | Hydration medium for extrusion dough.                    |

### B. Process Physics (The "How")

1.  **Mixing:** High-shear blending of dry powders. Hydrate with water to form a dough (35% moisture).
2.  **Extrusion:**
    - **Temp:** **85°C** (Partial Gelatinization).
    - **Die Pressure:** **40 Bar** (Expands starch for porosity).
    - **Cutter Speed:** 1500 RPM (Creates uniform 3mm shape).
3.  **Cross-Linking (Gelation):** Extruded dal falls into a **Calcium Bath (0.6%)** for **30 seconds**. This forms the "skin" (alginate shell) that holds shape during cooking.
4.  **Drying:**
    - **Temp:** **55°C** (Low heat preserves protein).
    - **Target Moisture:** **10.0%** (Shelf stable).
    - **PID Control:** Maintained within ±0.1% via adaptive feedback loop.

---

## 2. SUNDARBAN HONEY (Raw & Tech-Processed)

**Goal:** Reduce moisture without heating (preserving enzymes/flavor) and prevent fermentation.

### A. Critical Parameters

| Parameter           | Value       | Scientific Reason                                           |
| :------------------ | :---------- | :---------------------------------------------------------- |
| **Target Moisture** | **19.0%**   | <20% inhibits osmotic yeast growth.                         |
| **Process Temp**    | **38°C**    | Body temp of bees. >40°C destroys Diastase enzyme.          |
| **Vacuum Pressure** | **0.1 Bar** | Lowers boiling point of water to <35°C (Flash Evaporation). |

### B. Process Logic

1.  **Filtration:** 200-micron mesh (removes bee parts, keeps pollen).
2.  **Vacuum Dehydration:** Honey flows over thin-film evaporator plates under vacuum.
    - **Fick's Diffusion:** Moisture diffuses out rapidly due to pressure differential.
    - **Time:** Approx **7-8 hours** per batch to drop from 24% to 19%.
3.  **HMF Control:** Arrhenius kinetics ensure HMF accumulation is < 0.2 mg/kg/hr at 38°C. Total HMF stays < 10 mg/kg (Export Grade).

---

## 3. MUSTARD HONEY (Value-Added)

**Goal:** Controlled crystallization (Creamed Honey) and Fermentation (Mead).

### A. Creamed Honey (Controlled Crystallization)

- **Seed Honey:** **10%** Finely crystallized honey (Starter).
- **Mixing Temp:** **14°C** (Optimum Nucleation Zone - Standard Gaussian peak).
- **Agitation:** Slow shear (30 RPM) for 24 hours. Breaks large crystals, promotes millions of tiny ones (<25 microns).
- **Result:** Smooth, spreadable "butter" texture.

### B. Mead (Honey Wine)

- **Must:** Dilute honey to **24 Brix** (SG 1.100).
- **Yeast:** _Saccharomyces cerevisiae_ (Wine Strain).
- **Nutrient (YAN):** **180 ppm** (Add DAP/Fermaid-K if natural pollen is low).
- **Temp:** **18°C** (Cool ferment preserves volatile aromatics).
- **Time:** **14-30 Days**. Target ABV **12-13%**.

---

## 4. GHEE BILONA (Cultured & Churned)

**Goal:** Maximize Fat Recovery (FRE) and authentic flavor profile.

### A. Composition

- **Butterfat:** >99.5%
- **Flavor Compounds:** Diacetyl (Buttery), Lactones (Creamy), free Butyric Acid.

### B. Process Physics

1.  **Culturing (Dahi):** Milk fermented at **42°C** for 6 hours (pH drops to **4.6**).
    - _Physics:_ Isoelectric point of Casein (4.6) releases fat globules from protein matrix.
2.  **Churning (Bilona):**
    - **Temp:** **13°C** (Critical). Fat solidifies slightly, clumping efficiency maximizes.
    - **Yield:** **35 g/L** fat recovery (vs 30 g/L at wrong temp).
3.  **Boiling (Ghee Making):**
    - **Temp:** **118°C** (Maillard Reaction Peak).
    - **Time:** **15 mins**. Browns milk solids (Lactose + Amino Acids) -> Nutty flavor.

---

## 5. ATTA (Bio-Enzymatic Whole Wheat)

**Goal:** Soft roti for 12+ hours using natural enzymes.

### A. Blending Formulation

- **Hard Wheat (High Protein):** **50%** (Provides Strength/Elasticity).
- **Soft Wheat (Low Protein):** **50%** (Provides Extensibility/Cost reduction).
- **Malted Wheat Flour:** **0.5%** (The "Secret Ingredient").

### B. Enzymatic Action

1.  **Malted Flour:** Source of **Alpha-Amylase** enzyme.
2.  **Logic:** Amylase breaks down damaged starch into dextrins (sugars) during dough resting.
3.  **Effect:**
    - **Falling Number:** Drops from 400s (Hard) to **250s** (Optimal).
    - **Softness:** Dextrins hold water, keeping roti soft.
    - **Browning:** Extra sugars improve roasting color (Maillard).

---

## 6. MUSTARD OIL (Herbal Blend)

**Goal:** Cost reduction (~50% of pure mustard) with improved stability and retained pungency.

### A. Blending Formulation (% v/v)

| Ingredient                     | Ratio        | Function                                              |
| :----------------------------- | :----------- | :---------------------------------------------------- |
| **Rice Bran Oil (RBO)**        | **80%**      | Cost base, Neutral carrier, Gamma Oryzanol rich.      |
| **Mustard Oil (Kacchi Ghani)** | **20%**      | Authentic flavor top-note, Natural color.             |
| **Essential Oil (Mustard)**    | **1400 ppm** | **AITC Booster**. Restores pungency to "Pure" levels. |
| **Clove Extract**              | **200 ppm**  | Antioxidant (Eugenol).                                |
| **Turmeric Extract**           | **100 ppm**  | Antioxidant (Curcumin) + Color stability.             |

### B. Quality Parameters

1.  **Pungency (AITC):** Target **0.45%** (Matches pure mustard oil). Achieved by 1400 ppm EO addition.
2.  **Nutrition:** Erucic Acid drops from ~45% (Unsafe) to **<10%** (Heart Safe) due to dilution.
3.  **Shelf Life:** Clove + Turmeric provide synergistic oxidative stability (**Induction Time > 6 hours**).
