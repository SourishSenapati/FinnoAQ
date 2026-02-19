# Ghee Bilona Project - Documentation Index

**Project Goal:** Industrialize traditional Bilona Ghee production with 6-Sigma precision.

## Key Documents

| Document                                                 | Description                                                                                | Status          |
| :------------------------------------------------------- | :----------------------------------------------------------------------------------------- | :-------------- |
| **[TECHNICAL_REPORT_GHEE.md](TECHNICAL_REPORT_GHEE.md)** | Full Simulation Report (100M Batches). Covers Yield, Maillard Reaction, and Lipid Profile. | ✅ **Released** |
| **[specifications.md](specifications.md)**               | Core Process Specifications & Yield Targets.                                               | ✅ **Released** |
| **[simulation_ghee.py](simulation_ghee.py)**             | Digital Twin Simulation Engine (Python/PyTorch).                                           | ✅ **Active**   |

## Quick Stats (Simulated)

- **Yield:** 35.31 g/L (+20% vs Traditional)
- **Optimal Temp:** 13.0°C
- **Texture:** 1.50 mm Grain Size ('Danedar')
- **Safety:** 0.00% Burn Rate (Industrial SS316)

## Economics (Per Batch)

- **Input:** 1000L Milk @ ₹35/L = ₹35,000
- **Culturing Cost:** ₹500 (Culture + Heat)
- **Output:**
  - **Ghee:** 35.3 kg @ ₹900/kg = ₹31,770
  - **Buttermilk (Chaas):** 900L @ ₹10/L = ₹9,000
- **Total Revenue:** ₹40,770
- **Gross Margin:** **16.5%** (Significantly higher than standard 5%)

## Critical Machinery Specifications

1. **Bilona Churner (Bi-directional)**:
   - **Spec:** 500L SS316, 40 RPM, Variable Frequency Drive.
   - **Critical Feature:** Glycol Jacket for 13°C Temp maintenance.
   - **Est. Cost:** ₹4.5 Lakhs.
2. **Cream Separator (Optional)**:
   - **Spec:** 1000 LPH, Self-cleaning bowl.
   - **Est. Cost:** ₹2.2 Lakhs.
3. **Ghee Boiler (Kadhai)**:
   - **Spec:** Steam Jacketed 300L with Scraper.
   - **Est. Cost:** ₹3.8 Lakhs.

---

_Maintained by Finno Digital Twin Engine_
