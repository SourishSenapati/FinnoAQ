# Harakutir Phase 1 Toor Dal Study — Complete Parameter Registry

**Generated:** 13 October 2026  
**Document Control:** Controlling Source `Phase1_Scope_of_Work_Toor_Dal.docx`  
**Total Parameters Registered:** `100`  

---

## 1. Parameter Summary by Category

| Category | Parameter Count | Priority | Governing SOW Section |
|---|---|---|---|
| Physical Characterization | 19 | Mandatory | §5 |
| Proximate Chemical Composition | 7 | Mandatory | §6 |
| Starch & Gelatinization | 13 | Mandatory | §7 |
| Hydration Kinetics | 15 | Mandatory | §8 |
| Structural Investigation | 7 | High | §9 |
| Pectin & Cell Wall | 8 | Mandatory | §10 |
| Minerals & Phytate | 7 | Mandatory | §11 |
| Hardness & Texture Analysis | 8 | Mandatory | §12.1 |
| Standardized Cooking Study | 9 | Mandatory | §14, §15 |
| Traceability & Metadata | 4 | Mandatory | §3, §30 |
| Commercial Governance | 3 | Mandatory | §24, §28 |

---

## 2. Complete Meticulous Parameter Inventory

| Param ID | Category | Parameter Name | Symbol | Unit | Data Type | Method / Equipment | Replicates | Priority |
|---|---|---|---|---|---|---|---|---|
| `PHYS_01` | Physical Characterization | **Grain Colour (CIELAB L*)** | `L*` | dimensionless (0-100) | `float` | Spectrophotometer / HunterLab colorimeter (HunterLab ColorFlex / Minolta CR-400) | n=5 | Mandatory |
| `PHYS_02` | Physical Characterization | **Grain Colour (CIELAB a*)** | `a*` | dimensionless | `float` | Spectrophotometer (HunterLab ColorFlex) | n=5 | Mandatory |
| `PHYS_03` | Physical Characterization | **Grain Colour (CIELAB b*)** | `b*` | dimensionless | `float` | Spectrophotometer (HunterLab ColorFlex) | n=5 | Mandatory |
| `PHYS_04` | Physical Characterization | **Visual Uniformity** | `U_vis` | % | `float` | Visual inspection & digital image analysis (Flatbed scanner / high-resolution image analysis system) | n=3 | Mandatory |
| `PHYS_05` | Physical Characterization | **Grain Length** | `L` | mm | `float` | Digital vernier calipers / ImageJ image analysis (Mitutoyo Digital Caliper (0.01 mm) / stereomicroscope) | n=50 | Mandatory |
| `PHYS_06` | Physical Characterization | **Grain Width** | `W` | mm | `float` | Digital vernier calipers / Image analysis (Digital Caliper (0.01 mm)) | n=50 | Mandatory |
| `PHYS_07` | Physical Characterization | **Grain Thickness** | `T` | mm | `float` | Digital vernier calipers / Image analysis (Digital Caliper (0.01 mm)) | n=50 | Mandatory |
| `PHYS_08` | Physical Characterization | **Length-to-Width Ratio** | `L/W` | ratio | `float` | Calculated ratio L / W (Software calculation) | n=50 | Mandatory |
| `PHYS_09` | Physical Characterization | **Size Distribution (>5.0 mm fraction)** | `SD_50` | % w/w | `float` | Mechanical sieve shaker IS 4333 (Part 1) (Ro-Tap Sieve Shaker with certified ASTM/ISO sieves) | n=3 | Mandatory |
| `PHYS_10` | Physical Characterization | **Size Distribution (4.0 - 5.0 mm fraction)** | `SD_40` | % w/w | `float` | Mechanical sieve shaker (Ro-Tap Sieve Shaker) | n=3 | Mandatory |
| `PHYS_11` | Physical Characterization | **Size Distribution (<4.0 mm fraction)** | `SD_sub40` | % w/w | `float` | Mechanical sieve shaker (Ro-Tap Sieve Shaker) | n=3 | Mandatory |
| `PHYS_12` | Physical Characterization | **1000-Grain Weight** | `W_1000` | g | `float` | Counting 1000 sound grains and weighing to 0.01 g (IS 4333 Part 4) (Analytical balance (0.001 g) / Seed counter) | n=3 | Mandatory |
| `PHYS_13` | Physical Characterization | **Bulk Density** | `rho_b` | g/mL | `float` | Standard 250 mL graduated cylinder free-fall tapping (Bulk density apparatus / graduated cylinder) | n=3 | Mandatory |
| `PHYS_14` | Physical Characterization | **True Density** | `rho_t` | g/mL | `float` | Helium gas pycnometry / liquid displacement (toluene) (Gas Pycnometer / pycnometer bottle) | n=3 | High |
| `PHYS_15` | Physical Characterization | **Broken Grain Percentage** | `P_broken` | % w/w | `float` | Manual sorting & gravimetric determination IS 4333 (Analytical balance (0.01 g)) | n=3 | Mandatory |
| `PHYS_16` | Physical Characterization | **Visible Defects Percentage** | `P_defects` | % w/w | `float` | Manual visual grading under illuminated magnifier (Illuminated inspection table, analytical balance) | n=3 | Mandatory |
| `PHYS_17` | Physical Characterization | **Surface Characteristics / Crack Density** | `D_cracks` | cracks / mm² | `float` | Stereomicroscopy with darkfield illumination (Stereomicroscope with digital camera) | n=30 | High |
| `PHYS_18` | Physical Characterization | **Residual Seed-Coat Adherence** | `P_seedcoat` | % surface area | `float` | Digital image analysis of dehulled split cotyledons (Image analysis workstation) | n=50 | Mandatory |
| `PHYS_19` | Physical Characterization | **Raw Grain Hardness** | `H_raw` | N | `float` | Compression test at 1.0 mm/s with flat cylindrical probe (Texture Analyzer (e.g. TA.XT Plus) with 50 kg load cell) | n=20 | Mandatory |
| `PROX_01` | Proximate Chemical Composition | **Moisture Content** | `M_c` | % w/w | `float` | Air oven drying at 105°C to constant weight (AOAC 925.10 / IS 4333 Part 2) (Forced-air drying oven, desiccator, analytical balance) | n=3 | Mandatory |
| `PROX_02` | Proximate Chemical Composition | **Crude Protein** | `CP` | % w/w (dry basis) | `float` | Kjeldahl digestion & distillation (N x 6.25, AOAC 979.09) or Dumas combustion (Kjeldahl digestion/distillation unit / Elementar Dumas analyzer) | n=3 | Mandatory |
| `PROX_03` | Proximate Chemical Composition | **Crude Fat** | `EE` | % w/w (dry basis) | `float` | Soxhlet solvent extraction with petroleum ether (AOAC 920.39) (Soxhlet extraction apparatus / automated solvent extractor) | n=3 | Mandatory |
| `PROX_04` | Proximate Chemical Composition | **Crude Fibre** | `CF` | % w/w (dry basis) | `float` | Sequential acid/alkali digestion (Weende method, AOAC 962.09 / IS 10226) (Fibretec cold/hot extraction unit, muffle furnace) | n=3 | Mandatory |
| `PROX_05` | Proximate Chemical Composition | **Total Ash** | `Ash` | % w/w (dry basis) | `float` | Muffle furnace dry ashing at 550°C (AOAC 923.03) (Muffle furnace, silica crucibles, desiccator) | n=3 | Mandatory |
| `PROX_06` | Proximate Chemical Composition | **Total Carbohydrate** | `CHO` | % w/w (dry basis) | `float` | Mathematical calculation by difference (FAO Food Energy Methods) (Software calculation) | n=3 | Mandatory |
| `PROX_07` | Proximate Chemical Composition | **Total Starch** | `Starch_tot` | % w/w (dry basis) | `float` | Enzymatic hydrolysis (alpha-amylase/amyloglucosidase, AOAC 996.11 / Megazyme) (UV-Vis Spectrophotometer, thermostatted water bath) | n=3 | Mandatory |
| `STR_01` | Starch & Gelatinization | **Amylose Content** | `Amylose` | % of total starch | `float` | Iodine colorimetric assay (ISO 6647 / Juliano 1971) or Concanavalin A precipitation (UV-Vis Spectrophotometer (620 nm)) | n=3 | Mandatory |
| `STR_02` | Starch & Gelatinization | **Amylopectin Content** | `Amylopectin` | % of total starch | `float` | Calculated: 100 - Amylose % (Software calculation) | n=3 | Mandatory |
| `STR_03` | Starch & Gelatinization | **Amylose/Amylopectin Ratio** | `Amy/Amp` | ratio | `float` | Calculated ratio (Software calculation) | n=3 | Mandatory |
| `STR_04` | Starch & Gelatinization | **DSC Onset Gelatinization Temp** | `T_o` | °C | `float` | Differential Scanning Calorimetry (DSC, starch:water 1:3, 10°C/min) (PerkinElmer / TA Instruments DSC 250) | n=3 | Mandatory |
| `STR_05` | Starch & Gelatinization | **DSC Peak Gelatinization Temp** | `T_p` | °C | `float` | DSC thermogram peak analysis (TA Instruments DSC 250) | n=3 | Mandatory |
| `STR_06` | Starch & Gelatinization | **DSC Final/Conclusion Gelatinization Temp** | `T_c` | °C | `float` | DSC thermogram return to baseline (TA Instruments DSC 250) | n=3 | Mandatory |
| `STR_07` | Starch & Gelatinization | **Gelatinization Temperature Range** | `Delta_T` | °C | `float` | Calculated difference (Software calculation) | n=3 | Mandatory |
| `STR_08` | Starch & Gelatinization | **Gelatinization Enthalpy** | `Delta_H` | J/g dry starch | `float` | Integration of endothermic DSC peak area (TA Instruments DSC analysis software) | n=3 | Mandatory |
| `STR_09` | Starch & Gelatinization | **RVA Pasting Temperature** | `T_paste` | °C | `float` | Rapid Visco Analyzer (AACC 76-21.01 standard profile) (Perten RVA 4500) | n=3 | High |
| `STR_10` | Starch & Gelatinization | **RVA Peak Viscosity** | `V_peak` | cP or RVU | `float` | RVA pasting curve peak (Perten RVA 4500) | n=3 | High |
| `STR_11` | Starch & Gelatinization | **RVA Breakdown Viscosity** | `V_break` | cP or RVU | `float` | RVA difference calculation (Perten RVA 4500) | n=3 | High |
| `STR_12` | Starch & Gelatinization | **RVA Final Viscosity** | `V_final` | cP or RVU | `float` | RVA end-point reading (Perten RVA 4500) | n=3 | High |
| `STR_13` | Starch & Gelatinization | **RVA Setback Viscosity** | `V_setback` | cP or RVU | `float` | RVA difference calculation (Perten RVA 4500) | n=3 | High |
| `HYD_01` | Hydration Kinetics | **Water Uptake at 0 min** | `W_0` | g H2O / g dry solids | `float` | Gravimetric determination at t = 0 min (Analytical balance (0.001 g)) | n=3 | Mandatory |
| `HYD_02` | Hydration Kinetics | **Water Uptake at 15 min** | `W_15` | g H2O / g dry solids | `float` | Blotted surface gravimetric weighing (Analytical balance (0.001 g), timer) | n=3 | Mandatory |
| `HYD_03` | Hydration Kinetics | **Water Uptake at 30 min** | `W_30` | g H2O / g dry solids | `float` | Gravimetric weighing (Analytical balance (0.001 g)) | n=3 | Mandatory |
| `HYD_04` | Hydration Kinetics | **Water Uptake at 60 min** | `W_60` | g H2O / g dry solids | `float` | Gravimetric weighing (Analytical balance (0.001 g)) | n=3 | Mandatory |
| `HYD_05` | Hydration Kinetics | **Water Uptake at 120 min** | `W_120` | g H2O / g dry solids | `float` | Gravimetric weighing (Analytical balance (0.001 g)) | n=3 | Mandatory |
| `HYD_06` | Hydration Kinetics | **Water Uptake at 240 min** | `W_240` | g H2O / g dry solids | `float` | Gravimetric weighing (Analytical balance (0.001 g)) | n=3 | Mandatory |
| `HYD_07` | Hydration Kinetics | **Water Uptake at 480 min** | `W_480` | g H2O / g dry solids | `float` | Gravimetric weighing (Analytical balance (0.001 g)) | n=3 | Mandatory |
| `HYD_08` | Hydration Kinetics | **Water Absorption Index (WAI)** | `WAI` | g gel / g dry sample | `float` | Suspension hydration, centrifugation at 3000 x g (Anderson 1969) (Centrifuge, analytical balance) | n=3 | Mandatory |
| `HYD_09` | Hydration Kinetics | **Grain Mass Increase (Swelling %)** | `Delta_M_pct` | % | `float` | Gravimetric calculation (Software calculation) | n=3 | Mandatory |
| `HYD_10` | Hydration Kinetics | **Grain Volume Increase** | `Delta_V_pct` | % | `float` | Liquid displacement in 100 mL toluene / water (Graduated cylinder / pycnometer) | n=3 | Mandatory |
| `HYD_11` | Hydration Kinetics | **Swelling Capacity** | `SC` | mL / grain or mL / 100g | `float` | Volumetric displacement calculation (Graduated cylinder) | n=3 | Mandatory |
| `HYD_12` | Hydration Kinetics | **Peleg Rate Constant** | `k_1` | min / % | `float` | Non-linear least squares fit to M(t) = M_0 + t/(k_1 + k_2*t) (SciPy curve_fit / GPU PyTorch inverse model) | n=3 | Mandatory |
| `HYD_13` | Hydration Kinetics | **Peleg Capacity Constant** | `k_2` | %^-1 | `float` | Non-linear least squares fit to Peleg equation (SciPy curve_fit / GPU PyTorch inverse model) | n=3 | Mandatory |
| `HYD_14` | Hydration Kinetics | **Equilibrium Moisture Content** | `M_e` | % dry basis | `float` | Calculated from Peleg parameters (Software calculation) | n=3 | Mandatory |
| `HYD_15` | Hydration Kinetics | **Initial Hydration Rate** | `r_0` | % / min | `float` | Calculated from Peleg parameter k_1 (Software calculation) | n=3 | Mandatory |
| `STRC_01` | Structural Investigation | **Seed-Coat Thickness** | `Th_sc` | µm | `float` | Cross-sectional optical microscopy / Scanning Electron Microscopy (SEM) (FEI / Zeiss SEM or Olympus BX53 Optical Microscope) | n=10 | High |
| `STRC_02` | Structural Investigation | **Surface Morphology & Micropores** | `Morph_surf` | qualitative / score (1-5) | `int` | High-magnification SEM imaging (1000x - 5000x) (Scanning Electron Microscope) | n=5 | High |
| `STRC_03` | Structural Investigation | **Cotyledon Cell Wall Thickness** | `Th_cw` | µm | `float` | Transmission Electron Microscopy (TEM) or high-res SEM cross section (SEM / TEM) | n=10 | High |
| `STRC_04` | Structural Investigation | **Intercellular Void Fraction** | `phi_void` | % | `float` | Binarized SEM image thresholding (ImageJ void area fraction) (Digital image processing workstation) | n=5 | High |
| `STRC_05` | Structural Investigation | **Cellular Compactness Score** | `S_compact` | score (1-5) | `int` | Expert microscopist rating of SEM cross-sections (Microscopy workstation) | n=3 | Medium |
| `STRC_06` | Structural Investigation | **Post-Hydration Cell Separation Index** | `I_sep_hyd` | % separated cells | `float` | Optical microscopy of soaked cotyledon macerate (Optical microscope) | n=3 | High |
| `STRC_07` | Structural Investigation | **Post-Cooking Disintegration Index** | `I_disint_ck` | % detached cells | `float` | Microscopic examination of cooked dal puree (Optical microscope) | n=3 | High |
| `PEC_01` | Pectin & Cell Wall | **Total Pectin Content** | `Pec_tot` | % w/w dry basis | `float` | m-Hydroxydiphenyl colorimetric method (Blumenkrantz & Asboe-Hansen 1973) (UV-Vis Spectrophotometer (520 nm)) | n=3 | Mandatory |
| `PEC_02` | Pectin & Cell Wall | **Water-Soluble Pectin (WSP)** | `Pec_WSP` | % of total pectin | `float` | Sequential extraction with distilled water at 20°C, spectrophotometric assay (UV-Vis Spectrophotometer) | n=3 | Mandatory |
| `PEC_03` | Pectin & Cell Wall | **Chelator-Soluble Pectin (CSP)** | `Pec_CSP` | % of total pectin | `float` | Extraction with 0.05 M CDTA / sodium hexametaphosphate at pH 6.5 (UV-Vis Spectrophotometer) | n=3 | Mandatory |
| `PEC_04` | Pectin & Cell Wall | **Alkali-Soluble Pectin / Protopectin (ASP)** | `Pec_ASP` | % of total pectin | `float` | Extraction with 0.05 M Na2CO3 or 0.1 M NaOH (UV-Vis Spectrophotometer) | n=3 | Mandatory |
| `PEC_05` | Pectin & Cell Wall | **Pectin Degree of Esterification** | `DE` | % | `float` | FTIR spectroscopy (peak ratio 1740/1630 cm^-1) or titration (FTIR Spectrometer / automatic titrator) | n=3 | Mandatory |
| `PEC_06` | Pectin & Cell Wall | **Pectin-Associated Calcium** | `Ca_pec` | mg Ca / g pectin | `float` | Microwave digestion of CSP extract followed by ICP-OES (PerkinElmer Avio 500 ICP-OES) | n=3 | Mandatory |
| `PEC_07` | Pectin & Cell Wall | **Pectin-Associated Magnesium** | `Mg_pec` | mg Mg / g pectin | `float` | Microwave digestion of CSP extract followed by ICP-OES (PerkinElmer Avio 500 ICP-OES) | n=3 | Mandatory |
| `PEC_08` | Pectin & Cell Wall | **Cell-Wall Structural Integrity Index** | `I_cw_integ` | score (1-10) | `float` | Calculated composite index (Software calculation) | n=3 | High |
| `MIN_01` | Minerals & Phytate | **Total Calcium** | `Ca_tot` | mg / 100g (dry basis) | `float` | Microwave acid digestion (HNO3/H2O2) followed by ICP-OES (AOAC 2011.14) (PerkinElmer Avio 500 ICP-OES) | n=3 | Mandatory |
| `MIN_02` | Minerals & Phytate | **Total Magnesium** | `Mg_tot` | mg / 100g (dry basis) | `float` | Microwave digestion followed by ICP-OES (AOAC 2011.14) (PerkinElmer Avio 500 ICP-OES) | n=3 | Mandatory |
| `MIN_03` | Minerals & Phytate | **Total Iron** | `Fe_tot` | mg / 100g (dry basis) | `float` | ICP-OES (AOAC 2011.14) (PerkinElmer Avio 500 ICP-OES) | n=3 | Mandatory |
| `MIN_04` | Minerals & Phytate | **Total Phosphorus** | `P_tot` | mg / 100g (dry basis) | `float` | Vanadomolybdophosphoric acid colorimetry / ICP-OES (ICP-OES / Spectrophotometer) | n=3 | Mandatory |
| `MIN_05` | Minerals & Phytate | **Phytic Acid / Phytate** | `Phytate` | mg / 100g (dry basis) | `float` | Anion-exchange Wade reagent spectrophotometry (Latta & Eskin 1980 / Megazyme K-PHYT) or HPLC (UV-Vis Spectrophotometer (500 nm) / HPLC) | n=3 | Mandatory |
| `MIN_06` | Minerals & Phytate | **Phytate-to-Calcium Molar Ratio** | `MR_Phy_Ca` | mol / mol | `float` | Calculated stoichiometric ratio (Software calculation) | n=3 | Mandatory |
| `MIN_07` | Minerals & Phytate | **Phytate-to-(Ca+Mg) Molar Ratio** | `MR_Phy_CaMg` | mol / mol | `float` | Calculated stoichiometric ratio (Software calculation) | n=3 | Mandatory |
| `TEX_01` | Hardness & Texture Analysis | **Raw Grain Breaking Force** | `F_break_raw` | N | `float` | Single-grain compression test (knife edge / cylinder probe) (Texture Analyzer (TA.XT Plus)) | n=20 | Mandatory |
| `TEX_02` | Hardness & Texture Analysis | **Raw Grain Deformation at Fracture** | `Def_fract_raw` | mm | `float` | Texture analyzer displacement curve (Texture Analyzer) | n=20 | Mandatory |
| `TEX_03` | Hardness & Texture Analysis | **Hydrated Grain Firmness** | `F_firm_hyd` | N | `float` | Compression to 50% strain at 1.0 mm/s (Texture Analyzer with 36 mm cylinder probe) | n=20 | Mandatory |
| `TEX_04` | Hardness & Texture Analysis | **Hydrated Softening Index** | `SI_hyd` | % | `float` | Calculated percentage reduction (Software calculation) | n=20 | Mandatory |
| `TEX_05` | Hardness & Texture Analysis | **Cooked Dal Firmness** | `F_firm_ck` | N | `float` | Ottawa cell extrusion or single-grain compression to 70% strain (Texture Analyzer with Ottawa Texture Cell / Kramer Shear Cell) | n=5 | Mandatory |
| `TEX_06` | Hardness & Texture Analysis | **Cooked Dal Softness / Work of Shear** | `W_shear_ck` | N · s | `float` | Area under texture curve during Kramer/Ottawa extrusion (Texture Analyzer software) | n=5 | Mandatory |
| `TEX_07` | Hardness & Texture Analysis | **Hard-Core Percentage** | `P_hardcore` | % | `float` | Glass plate compression of 50 individual cooked grains (Two parallel glass plates with 1 kg standardized weight) | n=3 | Mandatory |
| `TEX_08` | Hardness & Texture Analysis | **Degree of Disintegration** | `P_disint` | % | `float` | Sieve separation (2.0 mm sieve) of stirred cooked broth (Standard sieve, analytical balance) | n=3 | Mandatory |
| `COOK_01` | Standardized Cooking Study | **Cooking Endpoint Time (Test A: No-Soak)** | `t_cook_A` | min | `float` | Instrumented pressure vessel with periodic glass plate endpoint checks (Instrumented pressure cooker / Mattson bean cooker with data logger) | n=3 | Mandatory |
| `COOK_02` | Standardized Cooking Study | **Cooking Endpoint Time (Test B: Standardized Soak)** | `t_cook_B` | min | `float` | Instrumented pressure vessel with data logging (Instrumented pressure vessel) | n=3 | Mandatory |
| `COOK_03` | Standardized Cooking Study | **Cooking Endpoint Time (Test C: Controlled Pressure)** | `t_cook_C` | min | `float` | Controlled laboratory autoclave / instrumented pressure vessel (Autoclave / pressure vessel with pressure transmitter and thermocouple) | n=3 | Mandatory |
| `COOK_04` | Standardized Cooking Study | **Pressure-Cooker Whistle Count (Reference Observation)** | `N_whistles` | whistles | `int` | Standard household 3L pressure cooker whistle observation (Standard domestic pressure cooker) | n=3 | Mandatory |
| `COOK_05` | Standardized Cooking Study | **Cooking Loss (Solids Leaching)** | `CL` | % dry solids lost | `float` | Gravimetric oven drying of cooking broth aliquot at 105°C (Drying oven, analytical balance) | n=3 | Mandatory |
| `COOK_06` | Standardized Cooking Study | **Cooked Water Absorption Ratio** | `WAR_ck` | g absorbed / g dry dal | `float` | Gravimetric weighing of drained cooked grains (Analytical balance) | n=3 | Mandatory |
| `COOK_07` | Standardized Cooking Study | **Cooked Grain Swelling Ratio** | `SR_ck` | ratio (v/v) | `float` | Volumetric displacement in graduated cylinder (Graduated cylinder) | n=3 | Mandatory |
| `COOK_08` | Standardized Cooking Study | **Final Cooked Moisture Content** | `M_cooked` | % w/w | `float` | Oven drying at 105°C (AOAC 925.10) (Drying oven, desiccator, analytical balance) | n=3 | Mandatory |
| `COOK_09` | Standardized Cooking Study | **Cooking Broth Turbidity / Total Soluble Solids** | `TSS_broth` | °Brix or OD_600 | `float` | Digital refractometer / UV-Vis Spectrophotometer at 600 nm (Digital Refractometer / Spectrophotometer) | n=3 | High |
| `META_01` | Traceability & Metadata | **Sample Identifier** | `Sample_ID` | string | `string` | Laboratory LIMS accessioning (LIMS / database) | n=1 | Mandatory |
| `META_02` | Traceability & Metadata | **Lot / Batch Number** | `Lot_ID` | string | `string` | Supplier manifest verification (Documentation) | n=1 | Mandatory |
| `META_03` | Traceability & Metadata | **Sample Quantity Received** | `Q_recv` | kg | `float` | Calibrated bench scale weighing (Bench scale (0.1 g)) | n=1 | Mandatory |
| `META_04` | Traceability & Metadata | **Retention Sample Quantity** | `Q_ret` | kg | `float` | Bench scale weighing and sealed pouch storage (Bench scale, heat sealer) | n=1 | Mandatory |
| `META_05` | Commercial Governance | **Indicative Professional Fee** | `Fee_prof` | INR | `float` | Contract reference (Ledger) | n=1 | Mandatory |
| `META_06` | Commercial Governance | **Commercial Working Ceiling** | `Ceiling_comm` | INR | `float` | Contract reference (Ledger) | n=1 | Mandatory |
| `META_07` | Commercial Governance | **Indicative Turnaround Timeline** | `Time_turnaround` | business days | `string` | Project schedule (Project management Gantt) | n=1 | Mandatory |

---

## 3. Scientific Purpose & Analytical Protocols per Parameter

### `PHYS_01`: Grain Colour (CIELAB L*)
- **Governing SOW Section:** §5
- **Scientific Purpose:** Quantify lightness of cotyledon surface to detect aging/storage oxidation
- **Analytical Standard:** Spectrophotometer / HunterLab colorimeter
- **Laboratory Equipment:** HunterLab ColorFlex / Minolta CR-400
- **Sampling & Replicates:** Per lot (Replicates: 5)
- **Operational Units:** `dimensionless (0-100)` (Data Type: `float`)

### `PHYS_02`: Grain Colour (CIELAB a*)
- **Governing SOW Section:** §5
- **Scientific Purpose:** Quantify red/green chromaticity coordinate
- **Analytical Standard:** Spectrophotometer
- **Laboratory Equipment:** HunterLab ColorFlex
- **Sampling & Replicates:** Per lot (Replicates: 5)
- **Operational Units:** `dimensionless` (Data Type: `float`)

### `PHYS_03`: Grain Colour (CIELAB b*)
- **Governing SOW Section:** §5
- **Scientific Purpose:** Quantify yellow/blue chromaticity coordinate (carotenoid pigmentation)
- **Analytical Standard:** Spectrophotometer
- **Laboratory Equipment:** HunterLab ColorFlex
- **Sampling & Replicates:** Per lot (Replicates: 5)
- **Operational Units:** `dimensionless` (Data Type: `float`)

### `PHYS_04`: Visual Uniformity
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine visual homogeneity and defect fraction
- **Analytical Standard:** Visual inspection & digital image analysis
- **Laboratory Equipment:** Flatbed scanner / high-resolution image analysis system
- **Sampling & Replicates:** Per lot (100 grains) (Replicates: 3)
- **Operational Units:** `%` (Data Type: `float`)

### `PHYS_05`: Grain Length
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine major axis dimension affecting surface-area-to-volume ratio
- **Analytical Standard:** Digital vernier calipers / ImageJ image analysis
- **Laboratory Equipment:** Mitutoyo Digital Caliper (0.01 mm) / stereomicroscope
- **Sampling & Replicates:** Per lot (50 grains) (Replicates: 50)
- **Operational Units:** `mm` (Data Type: `float`)

### `PHYS_06`: Grain Width
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine intermediate axis dimension
- **Analytical Standard:** Digital vernier calipers / Image analysis
- **Laboratory Equipment:** Digital Caliper (0.01 mm)
- **Sampling & Replicates:** Per lot (50 grains) (Replicates: 50)
- **Operational Units:** `mm` (Data Type: `float`)

### `PHYS_07`: Grain Thickness
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine minor axis dimension governing 1D water diffusion distance
- **Analytical Standard:** Digital vernier calipers / Image analysis
- **Laboratory Equipment:** Digital Caliper (0.01 mm)
- **Sampling & Replicates:** Per lot (50 grains) (Replicates: 50)
- **Operational Units:** `mm` (Data Type: `float`)

### `PHYS_08`: Length-to-Width Ratio
- **Governing SOW Section:** §5
- **Scientific Purpose:** Assess grain shape sphericity / elongation
- **Analytical Standard:** Calculated ratio L / W
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 50)
- **Operational Units:** `ratio` (Data Type: `float`)

### `PHYS_09`: Size Distribution (>5.0 mm fraction)
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine particle size uniformity and fraction of large grains
- **Analytical Standard:** Mechanical sieve shaker IS 4333 (Part 1)
- **Laboratory Equipment:** Ro-Tap Sieve Shaker with certified ASTM/ISO sieves
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `PHYS_10`: Size Distribution (4.0 - 5.0 mm fraction)
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine medium grain fraction
- **Analytical Standard:** Mechanical sieve shaker
- **Laboratory Equipment:** Ro-Tap Sieve Shaker
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `PHYS_11`: Size Distribution (<4.0 mm fraction)
- **Governing SOW Section:** §5
- **Scientific Purpose:** Determine fine/undersized grain fraction
- **Analytical Standard:** Mechanical sieve shaker
- **Laboratory Equipment:** Ro-Tap Sieve Shaker
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `PHYS_12`: 1000-Grain Weight
- **Governing SOW Section:** §5
- **Scientific Purpose:** Standard seed density index and commercial grain boldness indicator
- **Analytical Standard:** Counting 1000 sound grains and weighing to 0.01 g (IS 4333 Part 4)
- **Laboratory Equipment:** Analytical balance (0.001 g) / Seed counter
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `g` (Data Type: `float`)

### `PHYS_13`: Bulk Density
- **Governing SOW Section:** §5
- **Scientific Purpose:** Measure packing density and inter-granular porosity
- **Analytical Standard:** Standard 250 mL graduated cylinder free-fall tapping
- **Laboratory Equipment:** Bulk density apparatus / graduated cylinder
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `g/mL` (Data Type: `float`)

### `PHYS_14`: True Density
- **Governing SOW Section:** §5
- **Scientific Purpose:** Measure true cotyledon cellular density without inter-granular voids
- **Analytical Standard:** Helium gas pycnometry / liquid displacement (toluene)
- **Laboratory Equipment:** Gas Pycnometer / pycnometer bottle
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `g/mL` (Data Type: `float`)

### `PHYS_15`: Broken Grain Percentage
- **Governing SOW Section:** §5
- **Scientific Purpose:** Quantify milling defect and brokens that hydrate abnormally fast
- **Analytical Standard:** Manual sorting & gravimetric determination IS 4333
- **Laboratory Equipment:** Analytical balance (0.01 g)
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `PHYS_16`: Visible Defects Percentage
- **Governing SOW Section:** §5
- **Scientific Purpose:** Quantify insect damage, discolouration, chalky grains, fungal spots
- **Analytical Standard:** Manual visual grading under illuminated magnifier
- **Laboratory Equipment:** Illuminated inspection table, analytical balance
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `PHYS_17`: Surface Characteristics / Crack Density
- **Governing SOW Section:** §5
- **Scientific Purpose:** Identify micro-cracks from harvesting, dehulling, or thermal drying
- **Analytical Standard:** Stereomicroscopy with darkfield illumination
- **Laboratory Equipment:** Stereomicroscope with digital camera
- **Sampling & Replicates:** Per lot (30 grains) (Replicates: 30)
- **Operational Units:** `cracks / mm²` (Data Type: `float`)

### `PHYS_18`: Residual Seed-Coat Adherence
- **Governing SOW Section:** §5
- **Scientific Purpose:** Measure degree of dehulling; residual seed coat acts as hydrophobic barrier
- **Analytical Standard:** Digital image analysis of dehulled split cotyledons
- **Laboratory Equipment:** Image analysis workstation
- **Sampling & Replicates:** Per lot (50 grains) (Replicates: 50)
- **Operational Units:** `% surface area` (Data Type: `float`)

### `PHYS_19`: Raw Grain Hardness
- **Governing SOW Section:** §5, §12
- **Scientific Purpose:** Measure peak force to fracture intact dry cotyledon
- **Analytical Standard:** Compression test at 1.0 mm/s with flat cylindrical probe
- **Laboratory Equipment:** Texture Analyzer (e.g. TA.XT Plus) with 50 kg load cell
- **Sampling & Replicates:** Per lot (20 grains) (Replicates: 20)
- **Operational Units:** `N` (Data Type: `float`)

### `PROX_01`: Moisture Content
- **Governing SOW Section:** §6
- **Scientific Purpose:** Determine baseline free and bound moisture influencing storage stability
- **Analytical Standard:** Air oven drying at 105°C to constant weight (AOAC 925.10 / IS 4333 Part 2)
- **Laboratory Equipment:** Forced-air drying oven, desiccator, analytical balance
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `PROX_02`: Crude Protein
- **Governing SOW Section:** §6
- **Scientific Purpose:** Determine protein content (storage globulins, vicilins) and potential matrix barrier
- **Analytical Standard:** Kjeldahl digestion & distillation (N x 6.25, AOAC 979.09) or Dumas combustion
- **Laboratory Equipment:** Kjeldahl digestion/distillation unit / Elementar Dumas analyzer
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w (dry basis)` (Data Type: `float`)

### `PROX_03`: Crude Fat
- **Governing SOW Section:** §6
- **Scientific Purpose:** Quantify ether-extractable lipid fraction affecting surface hydrophobicity
- **Analytical Standard:** Soxhlet solvent extraction with petroleum ether (AOAC 920.39)
- **Laboratory Equipment:** Soxhlet extraction apparatus / automated solvent extractor
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w (dry basis)` (Data Type: `float`)

### `PROX_04`: Crude Fibre
- **Governing SOW Section:** §6
- **Scientific Purpose:** Quantify acid- and alkali-insoluble structural polysaccharides (cellulose, lignin)
- **Analytical Standard:** Sequential acid/alkali digestion (Weende method, AOAC 962.09 / IS 10226)
- **Laboratory Equipment:** Fibretec cold/hot extraction unit, muffle furnace
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w (dry basis)` (Data Type: `float`)

### `PROX_05`: Total Ash
- **Governing SOW Section:** §6
- **Scientific Purpose:** Measure total inorganic mineral matter
- **Analytical Standard:** Muffle furnace dry ashing at 550°C (AOAC 923.03)
- **Laboratory Equipment:** Muffle furnace, silica crucibles, desiccator
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w (dry basis)` (Data Type: `float`)

### `PROX_06`: Total Carbohydrate
- **Governing SOW Section:** §6
- **Scientific Purpose:** Total carbohydrate by difference: 100 - (Protein + Fat + Fibre + Ash)
- **Analytical Standard:** Mathematical calculation by difference (FAO Food Energy Methods)
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w (dry basis)` (Data Type: `float`)

### `PROX_07`: Total Starch
- **Governing SOW Section:** §6, §7
- **Scientific Purpose:** Directly quantify digestible starch fraction undergoing gelatinization
- **Analytical Standard:** Enzymatic hydrolysis (alpha-amylase/amyloglucosidase, AOAC 996.11 / Megazyme)
- **Laboratory Equipment:** UV-Vis Spectrophotometer, thermostatted water bath
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w (dry basis)` (Data Type: `float`)

### `STR_01`: Amylose Content
- **Governing SOW Section:** §7
- **Scientific Purpose:** Determine linear polysaccharide fraction governing retrogradation and gelatinization
- **Analytical Standard:** Iodine colorimetric assay (ISO 6647 / Juliano 1971) or Concanavalin A precipitation
- **Laboratory Equipment:** UV-Vis Spectrophotometer (620 nm)
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% of total starch` (Data Type: `float`)

### `STR_02`: Amylopectin Content
- **Governing SOW Section:** §7
- **Scientific Purpose:** Branched crystalline starch fraction governing crystalline melting
- **Analytical Standard:** Calculated: 100 - Amylose %
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% of total starch` (Data Type: `float`)

### `STR_03`: Amylose/Amylopectin Ratio
- **Governing SOW Section:** §7
- **Scientific Purpose:** Starch structural ratio
- **Analytical Standard:** Calculated ratio
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `ratio` (Data Type: `float`)

### `STR_04`: DSC Onset Gelatinization Temp
- **Governing SOW Section:** §7
- **Scientific Purpose:** Temperature where starch crystalline melting begins in excess water
- **Analytical Standard:** Differential Scanning Calorimetry (DSC, starch:water 1:3, 10°C/min)
- **Laboratory Equipment:** PerkinElmer / TA Instruments DSC 250
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `°C` (Data Type: `float`)

### `STR_05`: DSC Peak Gelatinization Temp
- **Governing SOW Section:** §7
- **Scientific Purpose:** Temperature of maximum heat absorption during gelatinization
- **Analytical Standard:** DSC thermogram peak analysis
- **Laboratory Equipment:** TA Instruments DSC 250
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `°C` (Data Type: `float`)

### `STR_06`: DSC Final/Conclusion Gelatinization Temp
- **Governing SOW Section:** §7
- **Scientific Purpose:** Temperature at completion of starch crystalline gelatinization
- **Analytical Standard:** DSC thermogram return to baseline
- **Laboratory Equipment:** TA Instruments DSC 250
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `°C` (Data Type: `float`)

### `STR_07`: Gelatinization Temperature Range
- **Governing SOW Section:** §7
- **Scientific Purpose:** Width of gelatinization transition: Delta_T = T_c - T_o
- **Analytical Standard:** Calculated difference
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `°C` (Data Type: `float`)

### `STR_08`: Gelatinization Enthalpy
- **Governing SOW Section:** §7
- **Scientific Purpose:** Energy required to melt starch crystallites; reflects double-helix crystallinity
- **Analytical Standard:** Integration of endothermic DSC peak area
- **Laboratory Equipment:** TA Instruments DSC analysis software
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `J/g dry starch` (Data Type: `float`)

### `STR_09`: RVA Pasting Temperature
- **Governing SOW Section:** §7
- **Scientific Purpose:** Temperature at which viscosity first begins to rise above baseline in RVA
- **Analytical Standard:** Rapid Visco Analyzer (AACC 76-21.01 standard profile)
- **Laboratory Equipment:** Perten RVA 4500
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `°C` (Data Type: `float`)

### `STR_10`: RVA Peak Viscosity
- **Governing SOW Section:** §7
- **Scientific Purpose:** Maximum viscosity reached during heating / swelling cycle
- **Analytical Standard:** RVA pasting curve peak
- **Laboratory Equipment:** Perten RVA 4500
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `cP or RVU` (Data Type: `float`)

### `STR_11`: RVA Breakdown Viscosity
- **Governing SOW Section:** §7
- **Scientific Purpose:** Disruption of swollen starch granules under shear: Peak - Trough
- **Analytical Standard:** RVA difference calculation
- **Laboratory Equipment:** Perten RVA 4500
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `cP or RVU` (Data Type: `float`)

### `STR_12`: RVA Final Viscosity
- **Governing SOW Section:** §7
- **Scientific Purpose:** Viscosity after cooling to 50°C; reflects retrogradation capacity
- **Analytical Standard:** RVA end-point reading
- **Laboratory Equipment:** Perten RVA 4500
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `cP or RVU` (Data Type: `float`)

### `STR_13`: RVA Setback Viscosity
- **Governing SOW Section:** §7
- **Scientific Purpose:** Tendency of amylose to reassociate into a gel network: Final - Trough
- **Analytical Standard:** RVA difference calculation
- **Laboratory Equipment:** Perten RVA 4500
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `cP or RVU` (Data Type: `float`)

### `HYD_01`: Water Uptake at 0 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Baseline unsoaked moisture level
- **Analytical Standard:** Gravimetric determination at t = 0 min
- **Laboratory Equipment:** Analytical balance (0.001 g)
- **Sampling & Replicates:** Controlled soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_02`: Water Uptake at 15 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Initial rapid capillary and surface hydration uptake
- **Analytical Standard:** Blotted surface gravimetric weighing
- **Laboratory Equipment:** Analytical balance (0.001 g), timer
- **Sampling & Replicates:** Soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_03`: Water Uptake at 30 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Early stage water penetration into outer cotyledon cell layers
- **Analytical Standard:** Gravimetric weighing
- **Laboratory Equipment:** Analytical balance (0.001 g)
- **Sampling & Replicates:** Soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_04`: Water Uptake at 60 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Transient diffusion regime
- **Analytical Standard:** Gravimetric weighing
- **Laboratory Equipment:** Analytical balance (0.001 g)
- **Sampling & Replicates:** Soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_05`: Water Uptake at 120 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Intermediate hydration plateau approach
- **Analytical Standard:** Gravimetric weighing
- **Laboratory Equipment:** Analytical balance (0.001 g)
- **Sampling & Replicates:** Soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_06`: Water Uptake at 240 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Late stage hydration approaching saturation
- **Analytical Standard:** Gravimetric weighing
- **Laboratory Equipment:** Analytical balance (0.001 g)
- **Sampling & Replicates:** Soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_07`: Water Uptake at 480 min
- **Governing SOW Section:** §8
- **Scientific Purpose:** Full equilibrium saturation level
- **Analytical Standard:** Gravimetric weighing
- **Laboratory Equipment:** Analytical balance (0.001 g)
- **Sampling & Replicates:** Soaking at 25°C (Replicates: 3)
- **Operational Units:** `g H2O / g dry solids` (Data Type: `float`)

### `HYD_08`: Water Absorption Index (WAI)
- **Governing SOW Section:** §8
- **Scientific Purpose:** Ability of dal flour/cotyledon particles to swell and bind water after centrifugation
- **Analytical Standard:** Suspension hydration, centrifugation at 3000 x g (Anderson 1969)
- **Laboratory Equipment:** Centrifuge, analytical balance
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `g gel / g dry sample` (Data Type: `float`)

### `HYD_09`: Grain Mass Increase (Swelling %)
- **Governing SOW Section:** §8
- **Scientific Purpose:** Percentage weight gain relative to dry weight: (M_t - M_0)/M_0 * 100
- **Analytical Standard:** Gravimetric calculation
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Time points 0-480 min (Replicates: 3)
- **Operational Units:** `%` (Data Type: `float`)

### `HYD_10`: Grain Volume Increase
- **Governing SOW Section:** §8
- **Scientific Purpose:** Volumetric expansion of cotyledons upon full hydration
- **Analytical Standard:** Liquid displacement in 100 mL toluene / water
- **Laboratory Equipment:** Graduated cylinder / pycnometer
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `%` (Data Type: `float`)

### `HYD_11`: Swelling Capacity
- **Governing SOW Section:** §8
- **Scientific Purpose:** Absolute volume increase per grain: (V_soaked - V_dry) / N_grains
- **Analytical Standard:** Volumetric displacement calculation
- **Laboratory Equipment:** Graduated cylinder
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mL / grain or mL / 100g` (Data Type: `float`)

### `HYD_12`: Peleg Rate Constant
- **Governing SOW Section:** §8
- **Scientific Purpose:** Inverse of initial hydration rate; primary parameter reflecting water mass transfer resistance
- **Analytical Standard:** Non-linear least squares fit to M(t) = M_0 + t/(k_1 + k_2*t)
- **Laboratory Equipment:** SciPy curve_fit / GPU PyTorch inverse model
- **Sampling & Replicates:** Per hydration curve (Replicates: 3)
- **Operational Units:** `min / %` (Data Type: `float`)

### `HYD_13`: Peleg Capacity Constant
- **Governing SOW Section:** §8
- **Scientific Purpose:** Inverse of maximum water absorption capacity increment: 1/k_2 = Delta_M_max
- **Analytical Standard:** Non-linear least squares fit to Peleg equation
- **Laboratory Equipment:** SciPy curve_fit / GPU PyTorch inverse model
- **Sampling & Replicates:** Per hydration curve (Replicates: 3)
- **Operational Units:** `%^-1` (Data Type: `float`)

### `HYD_14`: Equilibrium Moisture Content
- **Governing SOW Section:** §8
- **Scientific Purpose:** Asymptotic moisture saturation: M_e = M_0 + 1/k_2
- **Analytical Standard:** Calculated from Peleg parameters
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per hydration curve (Replicates: 3)
- **Operational Units:** `% dry basis` (Data Type: `float`)

### `HYD_15`: Initial Hydration Rate
- **Governing SOW Section:** §8
- **Scientific Purpose:** Instantaneous water ingress velocity at t = 0: r_0 = 1/k_1
- **Analytical Standard:** Calculated from Peleg parameter k_1
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per hydration curve (Replicates: 3)
- **Operational Units:** `% / min` (Data Type: `float`)

### `STRC_01`: Seed-Coat Thickness
- **Governing SOW Section:** §9
- **Scientific Purpose:** Determine thickness of testa layers (cuticle, palisade macrosclereids, hourglass cells)
- **Analytical Standard:** Cross-sectional optical microscopy / Scanning Electron Microscopy (SEM)
- **Laboratory Equipment:** FEI / Zeiss SEM or Olympus BX53 Optical Microscope
- **Sampling & Replicates:** Per lot (10 grains) (Replicates: 10)
- **Operational Units:** `µm` (Data Type: `float`)

### `STRC_02`: Surface Morphology & Micropores
- **Governing SOW Section:** §9
- **Scientific Purpose:** Determine surface waxiness, micropore occlusion, and cuticle smoothness
- **Analytical Standard:** High-magnification SEM imaging (1000x - 5000x)
- **Laboratory Equipment:** Scanning Electron Microscope
- **Sampling & Replicates:** Per lot (5 grains) (Replicates: 5)
- **Operational Units:** `qualitative / score (1-5)` (Data Type: `int`)

### `STRC_03`: Cotyledon Cell Wall Thickness
- **Governing SOW Section:** §9, §10
- **Scientific Purpose:** Quantify thickness of parenchyma cell walls and middle lamella
- **Analytical Standard:** Transmission Electron Microscopy (TEM) or high-res SEM cross section
- **Laboratory Equipment:** SEM / TEM
- **Sampling & Replicates:** Per lot (10 cells) (Replicates: 10)
- **Operational Units:** `µm` (Data Type: `float`)

### `STRC_04`: Intercellular Void Fraction
- **Governing SOW Section:** §9
- **Scientific Purpose:** Quantify cotyledon compactness and packing porosity that facilitates water routing
- **Analytical Standard:** Binarized SEM image thresholding (ImageJ void area fraction)
- **Laboratory Equipment:** Digital image processing workstation
- **Sampling & Replicates:** Per lot (5 fields) (Replicates: 5)
- **Operational Units:** `%` (Data Type: `float`)

### `STRC_05`: Cellular Compactness Score
- **Governing SOW Section:** §9
- **Scientific Purpose:** Qualitative grading of starch granule packing within parenchyma cells
- **Analytical Standard:** Expert microscopist rating of SEM cross-sections
- **Laboratory Equipment:** Microscopy workstation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `score (1-5)` (Data Type: `int`)

### `STRC_06`: Post-Hydration Cell Separation Index
- **Governing SOW Section:** §9
- **Scientific Purpose:** Determine whether middle lamella swells and permits cell separation during cold soaking
- **Analytical Standard:** Optical microscopy of soaked cotyledon macerate
- **Laboratory Equipment:** Optical microscope
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% separated cells` (Data Type: `float`)

### `STRC_07`: Post-Cooking Disintegration Index
- **Governing SOW Section:** §9
- **Scientific Purpose:** Measure cell separation vs cell rupture after standardized cooking
- **Analytical Standard:** Microscopic examination of cooked dal puree
- **Laboratory Equipment:** Optical microscope
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% detached cells` (Data Type: `float`)

### `PEC_01`: Total Pectin Content
- **Governing SOW Section:** §10
- **Scientific Purpose:** Measure total galacturonan polymers in the cell wall and middle lamella
- **Analytical Standard:** m-Hydroxydiphenyl colorimetric method (Blumenkrantz & Asboe-Hansen 1973)
- **Laboratory Equipment:** UV-Vis Spectrophotometer (520 nm)
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% w/w dry basis` (Data Type: `float`)

### `PEC_02`: Water-Soluble Pectin (WSP)
- **Governing SOW Section:** §10
- **Scientific Purpose:** Free, uncrosslinked, high-ester pectin soluble in neutral water
- **Analytical Standard:** Sequential extraction with distilled water at 20°C, spectrophotometric assay
- **Laboratory Equipment:** UV-Vis Spectrophotometer
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% of total pectin` (Data Type: `float`)

### `PEC_03`: Chelator-Soluble Pectin (CSP)
- **Governing SOW Section:** §10
- **Scientific Purpose:** Pectin ionic crosslinked with divalent cations (Ca²⁺/Mg²⁺) in the egg-box middle lamella
- **Analytical Standard:** Extraction with 0.05 M CDTA / sodium hexametaphosphate at pH 6.5
- **Laboratory Equipment:** UV-Vis Spectrophotometer
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% of total pectin` (Data Type: `float`)

### `PEC_04`: Alkali-Soluble Pectin / Protopectin (ASP)
- **Governing SOW Section:** §10
- **Scientific Purpose:** Covalently bound protopectin anchored to hemicellulose/cellulose matrix
- **Analytical Standard:** Extraction with 0.05 M Na2CO3 or 0.1 M NaOH
- **Laboratory Equipment:** UV-Vis Spectrophotometer
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `% of total pectin` (Data Type: `float`)

### `PEC_05`: Pectin Degree of Esterification
- **Governing SOW Section:** §10
- **Scientific Purpose:** Percentage of galacturonic acid carboxyl groups esterified with methyl esters; low DE (<50%) enables Ca crosslinking
- **Analytical Standard:** FTIR spectroscopy (peak ratio 1740/1630 cm^-1) or titration
- **Laboratory Equipment:** FTIR Spectrometer / automatic titrator
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `%` (Data Type: `float`)

### `PEC_06`: Pectin-Associated Calcium
- **Governing SOW Section:** §10
- **Scientific Purpose:** Quantify calcium bound within the isolated pectin / CSP fraction
- **Analytical Standard:** Microwave digestion of CSP extract followed by ICP-OES
- **Laboratory Equipment:** PerkinElmer Avio 500 ICP-OES
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg Ca / g pectin` (Data Type: `float`)

### `PEC_07`: Pectin-Associated Magnesium
- **Governing SOW Section:** §10
- **Scientific Purpose:** Quantify magnesium bound within the pectin / CSP fraction
- **Analytical Standard:** Microwave digestion of CSP extract followed by ICP-OES
- **Laboratory Equipment:** PerkinElmer Avio 500 ICP-OES
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg Mg / g pectin` (Data Type: `float`)

### `PEC_08`: Cell-Wall Structural Integrity Index
- **Governing SOW Section:** §10
- **Scientific Purpose:** Composite metric combining CSP fraction, DE, and divalent crosslinking
- **Analytical Standard:** Calculated composite index
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `score (1-10)` (Data Type: `float`)

### `MIN_01`: Total Calcium
- **Governing SOW Section:** §11
- **Scientific Purpose:** Quantify total calcium pool available for pectin crosslinking upon liberation from phytate
- **Analytical Standard:** Microwave acid digestion (HNO3/H2O2) followed by ICP-OES (AOAC 2011.14)
- **Laboratory Equipment:** PerkinElmer Avio 500 ICP-OES
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg / 100g (dry basis)` (Data Type: `float`)

### `MIN_02`: Total Magnesium
- **Governing SOW Section:** §11
- **Scientific Purpose:** Quantify total magnesium pool contributing to ionic bridge formation
- **Analytical Standard:** Microwave digestion followed by ICP-OES (AOAC 2011.14)
- **Laboratory Equipment:** PerkinElmer Avio 500 ICP-OES
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg / 100g (dry basis)` (Data Type: `float`)

### `MIN_03`: Total Iron
- **Governing SOW Section:** §11
- **Scientific Purpose:** Nutritional trace mineral and secondary trivalent crosslinker
- **Analytical Standard:** ICP-OES (AOAC 2011.14)
- **Laboratory Equipment:** PerkinElmer Avio 500 ICP-OES
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg / 100g (dry basis)` (Data Type: `float`)

### `MIN_04`: Total Phosphorus
- **Governing SOW Section:** §11
- **Scientific Purpose:** Determine total phosphorus (phytate-P + inorganic-P + phospholipid-P)
- **Analytical Standard:** Vanadomolybdophosphoric acid colorimetry / ICP-OES
- **Laboratory Equipment:** ICP-OES / Spectrophotometer
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg / 100g (dry basis)` (Data Type: `float`)

### `MIN_05`: Phytic Acid / Phytate
- **Governing SOW Section:** §11
- **Scientific Purpose:** Myo-inositol hexakisphosphate; primary natural chelator holding Ca/Mg in soluble/chelated state
- **Analytical Standard:** Anion-exchange Wade reagent spectrophotometry (Latta & Eskin 1980 / Megazyme K-PHYT) or HPLC
- **Laboratory Equipment:** UV-Vis Spectrophotometer (500 nm) / HPLC
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mg / 100g (dry basis)` (Data Type: `float`)

### `MIN_06`: Phytate-to-Calcium Molar Ratio
- **Governing SOW Section:** §11
- **Scientific Purpose:** Stoichiometric ratio: [Phytate/660.04] / [Ca/40.08]; values < 0.2 indicate calcium excess over chelation capacity
- **Analytical Standard:** Calculated stoichiometric ratio
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mol / mol` (Data Type: `float`)

### `MIN_07`: Phytate-to-(Ca+Mg) Molar Ratio
- **Governing SOW Section:** §11
- **Scientific Purpose:** Overall cation chelation balance: [Phytate/660.04] / [Ca/40.08 + Mg/24.31]
- **Analytical Standard:** Calculated stoichiometric ratio
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `mol / mol` (Data Type: `float`)

### `TEX_01`: Raw Grain Breaking Force
- **Governing SOW Section:** §12.1
- **Scientific Purpose:** Force to initiate fracture in dry cotyledon
- **Analytical Standard:** Single-grain compression test (knife edge / cylinder probe)
- **Laboratory Equipment:** Texture Analyzer (TA.XT Plus)
- **Sampling & Replicates:** Per lot (20 grains) (Replicates: 20)
- **Operational Units:** `N` (Data Type: `float`)

### `TEX_02`: Raw Grain Deformation at Fracture
- **Governing SOW Section:** §12.1
- **Scientific Purpose:** Brittleness / ductility of raw cotyledon
- **Analytical Standard:** Texture analyzer displacement curve
- **Laboratory Equipment:** Texture Analyzer
- **Sampling & Replicates:** Per lot (20 grains) (Replicates: 20)
- **Operational Units:** `mm` (Data Type: `float`)

### `TEX_03`: Hydrated Grain Firmness
- **Governing SOW Section:** §12.2
- **Scientific Purpose:** Peak compression force after standardized soaking (e.g. 120 min)
- **Analytical Standard:** Compression to 50% strain at 1.0 mm/s
- **Laboratory Equipment:** Texture Analyzer with 36 mm cylinder probe
- **Sampling & Replicates:** Per lot (20 grains) (Replicates: 20)
- **Operational Units:** `N` (Data Type: `float`)

### `TEX_04`: Hydrated Softening Index
- **Governing SOW Section:** §12.2
- **Scientific Purpose:** Relative reduction in hardness upon soaking: (F_raw - F_hyd)/F_raw * 100
- **Analytical Standard:** Calculated percentage reduction
- **Laboratory Equipment:** Software calculation
- **Sampling & Replicates:** Per lot (Replicates: 20)
- **Operational Units:** `%` (Data Type: `float`)

### `TEX_05`: Cooked Dal Firmness
- **Governing SOW Section:** §12.3
- **Scientific Purpose:** Residual firmness after standardized cooking cycle
- **Analytical Standard:** Ottawa cell extrusion or single-grain compression to 70% strain
- **Laboratory Equipment:** Texture Analyzer with Ottawa Texture Cell / Kramer Shear Cell
- **Sampling & Replicates:** Per cooked batch (20 grains / 30g batch) (Replicates: 5)
- **Operational Units:** `N` (Data Type: `float`)

### `TEX_06`: Cooked Dal Softness / Work of Shear
- **Governing SOW Section:** §12.3
- **Scientific Purpose:** Total mechanical work required to extrude / mash cooked dal
- **Analytical Standard:** Area under texture curve during Kramer/Ottawa extrusion
- **Laboratory Equipment:** Texture Analyzer software
- **Sampling & Replicates:** Per cooked batch (Replicates: 5)
- **Operational Units:** `N · s` (Data Type: `float`)

### `TEX_07`: Hard-Core Percentage
- **Governing SOW Section:** §12.3, §15
- **Scientific Purpose:** Percentage of cooked grains retaining an unsoftened / opaque white central core under glass plate compression (Mattson cooker test)
- **Analytical Standard:** Glass plate compression of 50 individual cooked grains
- **Laboratory Equipment:** Two parallel glass plates with 1 kg standardized weight
- **Sampling & Replicates:** Per cooked batch (50 grains) (Replicates: 3)
- **Operational Units:** `%` (Data Type: `float`)

### `TEX_08`: Degree of Disintegration
- **Governing SOW Section:** §12.3, §15
- **Scientific Purpose:** Percentage of grains that break down into smooth dal puree upon standard gentle stirring
- **Analytical Standard:** Sieve separation (2.0 mm sieve) of stirred cooked broth
- **Laboratory Equipment:** Standard sieve, analytical balance
- **Sampling & Replicates:** Per cooked batch (Replicates: 3)
- **Operational Units:** `%` (Data Type: `float`)

### `COOK_01`: Cooking Endpoint Time (Test A: No-Soak)
- **Governing SOW Section:** §14, §15
- **Scientific Purpose:** Time required to reach fully cooked endpoint without prior soaking
- **Analytical Standard:** Instrumented pressure vessel with periodic glass plate endpoint checks
- **Laboratory Equipment:** Instrumented pressure cooker / Mattson bean cooker with data logger
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `min` (Data Type: `float`)

### `COOK_02`: Cooking Endpoint Time (Test B: Standardized Soak)
- **Governing SOW Section:** §14, §15
- **Scientific Purpose:** Time to reach cooked endpoint after standardized 60 min soaking at 25°C
- **Analytical Standard:** Instrumented pressure vessel with data logging
- **Laboratory Equipment:** Instrumented pressure vessel
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `min` (Data Type: `float`)

### `COOK_03`: Cooking Endpoint Time (Test C: Controlled Pressure)
- **Governing SOW Section:** §14, §15
- **Scientific Purpose:** Time to reach cooked endpoint under 103 kPa gauge pressure (121°C)
- **Analytical Standard:** Controlled laboratory autoclave / instrumented pressure vessel
- **Laboratory Equipment:** Autoclave / pressure vessel with pressure transmitter and thermocouple
- **Sampling & Replicates:** Per lot (Replicates: 3)
- **Operational Units:** `min` (Data Type: `float`)

### `COOK_04`: Pressure-Cooker Whistle Count (Reference Observation)
- **Governing SOW Section:** §1, §13, §15
- **Scientific Purpose:** Household reference count recorded as operational context alongside scientific endpoints
- **Analytical Standard:** Standard household 3L pressure cooker whistle observation
- **Laboratory Equipment:** Standard domestic pressure cooker
- **Sampling & Replicates:** Per trial (Replicates: 3)
- **Operational Units:** `whistles` (Data Type: `int`)

### `COOK_05`: Cooking Loss (Solids Leaching)
- **Governing SOW Section:** §15
- **Scientific Purpose:** Percentage of dry matter leached into cooking water broth
- **Analytical Standard:** Gravimetric oven drying of cooking broth aliquot at 105°C
- **Laboratory Equipment:** Drying oven, analytical balance
- **Sampling & Replicates:** Per cooked trial (Replicates: 3)
- **Operational Units:** `% dry solids lost` (Data Type: `float`)

### `COOK_06`: Cooked Water Absorption Ratio
- **Governing SOW Section:** §15
- **Scientific Purpose:** Total water uptake during the entire cooking cycle
- **Analytical Standard:** Gravimetric weighing of drained cooked grains
- **Laboratory Equipment:** Analytical balance
- **Sampling & Replicates:** Per cooked trial (Replicates: 3)
- **Operational Units:** `g absorbed / g dry dal` (Data Type: `float`)

### `COOK_07`: Cooked Grain Swelling Ratio
- **Governing SOW Section:** §15
- **Scientific Purpose:** Volumetric expansion from raw dry grain to cooked state: V_cooked / V_raw
- **Analytical Standard:** Volumetric displacement in graduated cylinder
- **Laboratory Equipment:** Graduated cylinder
- **Sampling & Replicates:** Per cooked trial (Replicates: 3)
- **Operational Units:** `ratio (v/v)` (Data Type: `float`)

### `COOK_08`: Final Cooked Moisture Content
- **Governing SOW Section:** §15
- **Scientific Purpose:** Moisture content of cooked dal cotyledons at the defined sensory/firmness endpoint
- **Analytical Standard:** Oven drying at 105°C (AOAC 925.10)
- **Laboratory Equipment:** Drying oven, desiccator, analytical balance
- **Sampling & Replicates:** Per cooked trial (Replicates: 3)
- **Operational Units:** `% w/w` (Data Type: `float`)

### `COOK_09`: Cooking Broth Turbidity / Total Soluble Solids
- **Governing SOW Section:** §15
- **Scientific Purpose:** Degree of starch and protein dispersion in the supernatant cooking liquid
- **Analytical Standard:** Digital refractometer / UV-Vis Spectrophotometer at 600 nm
- **Laboratory Equipment:** Digital Refractometer / Spectrophotometer
- **Sampling & Replicates:** Per cooked trial (Replicates: 3)
- **Operational Units:** `°Brix or OD_600` (Data Type: `float`)

### `META_01`: Sample Identifier
- **Governing SOW Section:** §3, §30
- **Scientific Purpose:** Unique tracking code for sample type (Sample A: Tanzanian, Sample B: Indian)
- **Analytical Standard:** Laboratory LIMS accessioning
- **Laboratory Equipment:** LIMS / database
- **Sampling & Replicates:** At receipt (Replicates: 1)
- **Operational Units:** `string` (Data Type: `string`)

### `META_02`: Lot / Batch Number
- **Governing SOW Section:** §3, §30
- **Scientific Purpose:** Independent commercial lot identifier (minimum 2 independent lots per sample type)
- **Analytical Standard:** Supplier manifest verification
- **Laboratory Equipment:** Documentation
- **Sampling & Replicates:** Per lot (Replicates: 1)
- **Operational Units:** `string` (Data Type: `string`)

### `META_03`: Sample Quantity Received
- **Governing SOW Section:** §3
- **Scientific Purpose:** Quantity of sample received (recommended 2.5 - 3.0 kg per lot)
- **Analytical Standard:** Calibrated bench scale weighing
- **Laboratory Equipment:** Bench scale (0.1 g)
- **Sampling & Replicates:** At receipt (Replicates: 1)
- **Operational Units:** `kg` (Data Type: `float`)

### `META_04`: Retention Sample Quantity
- **Governing SOW Section:** §30
- **Scientific Purpose:** Quantity set aside in sealed, documented retention archive before testing begins
- **Analytical Standard:** Bench scale weighing and sealed pouch storage
- **Laboratory Equipment:** Bench scale, heat sealer
- **Sampling & Replicates:** At receipt (Replicates: 1)
- **Operational Units:** `kg` (Data Type: `float`)

### `META_05`: Indicative Professional Fee
- **Governing SOW Section:** §24, §28
- **Scientific Purpose:** Indicative Phase 1 fee in source proposal: ₹1,73,000 + applicable GST
- **Analytical Standard:** Contract reference
- **Laboratory Equipment:** Ledger
- **Sampling & Replicates:** Project scope (Replicates: 1)
- **Operational Units:** `INR` (Data Type: `float`)

### `META_06`: Commercial Working Ceiling
- **Governing SOW Section:** §26
- **Scientific Purpose:** Working expenditure ceiling: ₹2,00,000 + applicable GST (extra requires written client approval)
- **Analytical Standard:** Contract reference
- **Laboratory Equipment:** Ledger
- **Sampling & Replicates:** Project scope (Replicates: 1)
- **Operational Units:** `INR` (Data Type: `float`)

### `META_07`: Indicative Turnaround Timeline
- **Governing SOW Section:** §27
- **Scientific Purpose:** Indicative project timeline: 20-25 business days across 5 analytical stages
- **Analytical Standard:** Project schedule
- **Laboratory Equipment:** Project management Gantt
- **Sampling & Replicates:** Project scope (Replicates: 1)
- **Operational Units:** `business days` (Data Type: `string`)
