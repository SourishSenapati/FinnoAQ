# Technical Proposal: Phase 1 R&D Analytical Study
**Subject:** Pulse Processing Optimization - Resolution of the Hard-to-Cook (HTC) Defect in Tanzanian Toor Dal  
**Target:** Client Product Development and Procurement Team  
**Schedule:** 7 Business Days from sample receipt  

---

## 1. Executive Summary & Commercial Framework

Tanzanian imported pigeon pea (*Cajanus cajan*) exhibits an average atmospheric cooking time of 110 minutes, compared to 35 minutes for the domestic Indian benchmark. The raw-material price differential is INR 20/kg in favor of the Tanzanian import. The objective of this study is to measure the physicochemical rate-limiting step causing this cooking deficit and establish whether an engineered process intervention can restore cooking parity at an operational cost below INR 20/kg.

The cooking-time elevation in tropical-stored legumes is termed the Hard-to-Cook (HTC) defect. The primary working hypothesis is that storage-induced phytase activity hydrolyzes endogenous phytic acid, liberating divalent cations (Ca2+ and Mg2+). These cations migrate to the middle lamella and crosslink de-esterified pectin chains, forming an insoluble calcium/magnesium-pectate gel network. This gel resists dissolution at cooking temperatures (>100 deg C) and acts as a hydraulic barrier to cotyledon water imbibition.

The Phase 1 scope tests this hypothesis against four competing mechanisms through wet chemistry, spectroscopy, texture analysis, and Physics-Informed Neural Network (PINN) kinetic parameter estimation.

---

## 2. Phase 1 Scope of Work

Testing runs in parallel on Tanzanian import lots and Indian domestic control lots.

### 2.1 Proximate Composition & Baseline Properties
* **Moisture Content:** AOAC 925.10 (vacuum oven at 105 deg C to constant weight).
* **Crude Protein:** AOAC 920.87 (Kjeldahl digestion, N x 6.25).
* **Crude Lipids:** Soxhlet extraction with petroleum ether.
* **Total Starch and Amylose Content:** Megazyme enzymatic assay (AA/AMG, AOAC 996.11) with Concanavalin A amylopectin precipitation.

### 2.2 Biochemical & Structural Defect Isolation
* **Pectin Fractionation:** Sequential extraction of water-soluble, chelator-soluble (CDTA/EDTA), and alkali-soluble pectin fractions. Quantified by m-hydroxydiphenyl assay at 520 nm.
* **Phytic Acid Quantification:** Wade reagent colorimetric assay with HPLC confirmation.
* **Divalent Cations (Ca2+, Mg2+):** Atomic Absorption Spectroscopy (AAS) following nitric/perchloric acid digestion to determine free apoplastic vs. bound pectin cations.
* **Lignin Content:** Acid detergent lignin (ADL) method to determine if seed-coat sclerification contributes to the barrier.

### 2.3 Thermodynamic & Kinetic Characterization
* **Differential Scanning Calorimetry (DSC):** Onset (To), peak (Tp), conclusion (Tc) gelatinization temperatures and enthalpy (delta-H) measured between 20 deg C and 120 deg C at 10 deg C/min.
* **Instrumental Texture Analysis:** TA.XTPlus texture analyzer with 75 mm compression platen; hardness (N), cohesiveness, and chewiness recorded after standardized cooking intervals.
* **PINN Hydration Modeling:** Numerical solution of the inverse Peleg problem:
  M(t) = M0 + t / (K1 + K2 * t)
  where K1 represents mass transfer resistance (min/%) and K2 represents capacity (%^-1).

---

## 3. Deliverables

1. Full analytical dataset across all replicates (raw data CSV + summary).
2. Standardized cooking curves (shear hardness vs. boiling duration).
3. DSC thermograms and gelatinization enthalpy tables.
4. Cause -> Evidence -> Intervention matrix evaluating the 5 candidate mechanisms.
5. Ranked preliminary process interventions for Phase 2 pilot testing.

Interventions to be evaluated include:
* **Thermal Shock / Infrared Micronization:** Rapid vapor-pressure micro-fissuring of the middle lamella.
* **Chemical Chelation Conditioning:** Pre-soaking with food-grade sodium tripolyphosphate (STPP) or sodium bicarbonate.
* **Enzymatic Depolymerization:** Controlled pectinase or cellulase application.

---

## 4. Cost Breakdown & Timeline

| Stage | Scope | Fee (INR) |
| :--- | :--- | :--- |
| **1.A** | Proximate, Starch, and Amylose Profiling | 55,000 |
| **1.B** | Cell Wall Pectin, Phytate, and AAS Mineral Analysis | 95,000 |
| **1.C** | DSC Thermal Analysis and TA.XTPlus Texture Profiling | 60,000 |
| **1.D** | PINN Hydration Kinetics and Engineering Dossier | 45,000 |
| **Total** | **Phase 1 R&D Package** | **2,55,000** |

*Taxes: Applicable GST extra at standard statutory rates. Quotation validity: 30 days.*

**Execution Timeline:**
* **Days 1-2:** Sample reception, moisture equalization, proximate analysis, and hydration logging.
* **Days 3-4:** Chemical extractions (phytate, pectin), AAS mineral analysis, and DSC scans.
* **Days 5-6:** PINN kinetic parameter estimation, texture profile analysis, and data synthesis.
* **Day 7:** Technical report submission and Phase 2 pilot recommendation.

---

## 5. Sample Requirements & Logistics

* **Domestic Indian Control:** 3.0 kg, food-grade, standard commercial split toor dal.
* **Tanzanian Import Subject:** 3.0 kg, unpolished/milled split dal from imported shipment lots.
* **Packaging:** Hermetically sealed poly-lined containers to prevent ambient moisture uptake during transit.
