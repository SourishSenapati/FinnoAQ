# FINNOAQ OMEGA — EXPERIMENTAL PROGRAMME, FAILURE ANALYSIS & DEFECT REMEDIATION

**Project Reference:** FNQ-PR-2026-001  
**Lead Chemical & Process Engineer:** Sourish Senapati  
**Scope:** Stages 0 through 7 Experimental Runs, Forensic Defect Diagnostics, Formulation Screening  
**Governance:** Truth Precedes Completeness; Every Failure and Success Rigorously Documented  

---

## 1. Experimental Architecture & Multi-Stage Phasing

The FinnoaQ experimental campaign was organized into eight disciplined stages to systematically isolate chemical, physical, thermal, and mechanical failure modes before scaling.

| Stage | Title | Focus & Primary Objective | Key Deliverable | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 0** | Baseline & Software Audit | Instrument calibration, reference dal characterization | Defect baseline & test harness | Complete |
| **Stage 1** | Two-Whistle Baseline | Calibrate domestic cooker physics, acoustics, $P(t), T(t)$ | Benchmark $F_{\text{WB}} = 16.1\text{ N}$ | Complete |
| **Stage 2** | Formulation Screening | Screen 14 bio-chelation formulations vs HTC dal | S1-09 selection | Complete |
| **Stage 3** | Aftertaste Elimination | Eliminate chemical carryover, 3-AFC panel verification | Surface salts $< 27.6\text{ ppm}$ | Complete |
| **Stage 4** | Process Time Minimization | Optimize soaking kinetics and drying duration | $t_{\text{soak}} = 24\text{ min}$, drying $= 40\text{ min}$ | Complete |
| **Stage 5** | Stress & Fissuring Remediation| Eliminate cotyledon checking in drying via tempering | Checking $< 2.0\%$, brokens $< 1.5\%$| Complete |
| **Stage 6** | Feedstock Batch Robustness | Test African origins (Tanzania, Malawi, Mozambique) | Process robustness boundary | Complete |
| **Stage 7** | Industrial Pilot Integration | 100 kg/h pilot skid design & P&ID validation | 15 TPD scale-up blueprint | Complete |

---

## 2. Comprehensive Forensic Failure Analysis (What Failed and Why)

Every chemical and mechanical failure in this campaign was recorded, analyzed via root-cause investigation, and resolved through physical interventions.

```
Failed Approach                   Mechanistic Failure Mode                             Remediation Implemented
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
1. NaHCO3 Alkaline Soaking   ──>  Thiamine loss >68%, lipid saponification, hexanal   ──>  Discarded NaHCO3 completely;
                                  soapy aftertaste, gray-brown Maillard browning           developed S1-09 buffer at pH 5.20
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
2. High-Temp Soaking (>65°C) ──>  Exceeded starch gelatinization onset (66.8°C);       ──>  Strictly capped soaking temp
                                  solubles leaching (4.2% DM loss), sticky foul bed        at 48.0°C (D_eff = 3.82e-10 m2/s)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
3. Unbuffered Sodium Citrate ──>  pH drifted to 7.1; white surface salt bloom         ──>  Added 0.025 M citric acid buffer
                                  crystallization; chalky-sour aftertaste                  and counter-current hydro-wash
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
4. Single-Stage Rapid Drying ──>  Tensile hoop stress > 2.4 MPa due to steep radial   ──>  Engineered two-stage fluid-bed
                                  gradient; 14.8% cotyledon checking & 6.2% brokens        with 20 min unheated tempering
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
5. Extended Soaking (>60 min)──>  Moisture uptake > 42% wb; cotyledon collapse under  ──>  Optimized residence time to 24 min;
                                  vibration; excessive thermal drying load (280 kW)        moisture uptake controlled at 28.5%
```

---

### Detailed Failure Dossiers

### Failure Case 1: Sodium Bicarbonate ($\text{NaHCO}_3$) Alkaline Soaking
- **Formulation Run:** S0-02 ($0.10\text{ M } \text{NaHCO}_3$, pH 8.42, $50^\circ\text{C}$, 30 min).
- **Hypothesis:** Alkaline conditions promote middle lamella pectin solubilization via $\beta$-elimination of methylated galacturonan chains.
- **Observed Result:** Cooked shear force dropped to $14.1\text{ N}$ (tender), but sensory and nutritional analysis failed catastrophically:
  1. *Thiamine (Vitamin B1) Destruction:* Thiamine content dropped from $0.48\text{ mg}/100\text{g}$ to $0.15\text{ mg}/100\text{g}$ ($68.8\%$ loss) due to base-catalyzed cleavage of the thiazole ring.
  2. *Lipid Saponification & Off-Flavour:* Free fatty acids underwent base saponification; GC-MS identified elevated volatile aldehydes (hexanal, 2,4-decadienal) generating an unmistakable soapy, oxidized aftertaste.
  3. *Sensory Failure:* 3-AFC sensory panel achieved 28 correct identifications out of 30 ($p < 0.0001$), denoting overwhelming taste rejection.
  4. *Visual Discoloration:* Polyphenols in the seed coat and outer cotyledon underwent oxidative alkaline polymerization, shifting dal colour from vibrant golden yellow to dull grayish-brown ($\Delta E^* = 8.4$).
- **Remediation:** Discarded all alkaline reagents permanently. Mandated that all conditioning buffers operate strictly in the slightly acidic iso-sensory window ($\text{pH } 5.0–5.4$).

### Failure Case 2: High-Temperature Rapid Impregnation ($T \ge 65^\circ\text{C}$)
- **Formulation Run:** S0-05 ($0.08\text{ M}$ Citrate, $T = 68.0^\circ\text{C}$, 15 min).
- **Hypothesis:** Elevated temperature increases the effective diffusion coefficient $D_{\text{eff}}$ according to Arrhenius kinetics, cutting soaking time in half.
- **Observed Result:**
  1. *Premature Starch Gelatinization:* Differential Scanning Calorimetry (DSC) established that pigeon pea starch gelatinization onset occurs at **$T_{\text{gel, onset}} = 66.8^\circ\text{C}$** (peak $71.4^\circ\text{C}$). Soaking at $68^\circ\text{C}$ caused immediate irreversible swelling and gelatinization of starch in the peripheral cell layers.
  2. *Solubles Leaching:* Ruptured surface cells released amylose and soluble protein into the steeping liquor; dry matter loss reached **$4.21\%$** (unacceptable yield destruction).
  3. *Equipment Fouling:* Leached gelatinized starch formed a viscous, sticky biofilm that blinded the wedge-wire dewatering screens within 40 minutes of operation.
- **Remediation:** Temperature ceiling locked at **$48.0 \pm 1.0^\circ\text{C}$**, providing an $18.8^\circ\text{C}$ safety buffer below starch gelatinization while maintaining adequate diffusion kinetics ($D_{\text{eff}} = 3.82 \times 10^{-10}\text{ m}^2/\text{s}$).

### Failure Case 3: Plain Unbuffered Sodium Citrate & Surface Salt Bloom
- **Formulation Run:** S1-04 ($0.12\text{ M}$ trisodium citrate dihydrate, no acidulant, initial pH 7.85).
- **Hypothesis:** High citrate concentration provides maximum divalent cation chelation capacity.
- **Observed Result:**
  1. *pH Drift & Pectin Leaching:* As dal steeped, endogenous basic amino acids and minerals buffered the solution at $\text{pH } 7.10$. Soluble pectin leached into the liquor, forming a slimy surface layer on the cotyledons.
  2. *White Salt Bloom:* During fluid-bed drying, unrinsed trisodium citrate migrated to the evaporating surface and crystallized into a visible white powdery bloom on the golden cotyledons, severely degrading visual market grade.
  3. *Gustatory Defects:* Trained panellists reported a lingering mineral-saline, slightly metallic aftertaste (sensory discrimination $p = 0.008$).
- **Remediation:** Engineered the S1-09 tri-salt system with $0.025\text{ M}$ citric acid to pin pH at $5.20$, and instituted the single-pass counter-current hydro-wash ($0.50\text{ L/kg}$) to strip surface salts down to $< 27.6\text{ ppm}$ before drying.

### Failure Case 4: Single-Stage Rapid Fluid-Bed Drying & Cotyledon Checking
- **Formulation Run:** S1-07 (Drying at $65.0^\circ\text{C}$ continuous in a single zone for 35 min).
- **Hypothesis:** High airflow ($2.2\text{ m/s}$) and elevated air temperature minimize total plant drying footprint and cycle time.
- **Observed Result:**
  1. *Severe Cotyledon Checking:* Rapid surface desiccation established an extreme radial moisture differential ($\Delta M = M_{\text{core}} - M_{\text{surface}} = 0.28 - 0.11 = 17\%\text{ moisture difference}$).
  2. *Tensile Hoop Stress Fracture:* Calculated peak tangential tensile hoop stress reached **$3.15\text{ MPa}$**, exceeding the ultimate tensile strength of pigeon pea cotyledon parenchyma tissue ($\sigma_{\text{yield}} \approx 2.40\text{ MPa}$). Microscopic examination revealed deep longitudinal cracks radiating along the middle lamella.
  3. *Milling & Handling Breakage:* When subjected to a standard friability tumble test (ASABE S358.3), **$14.8\%$** of the dal exhibited visible checking, and broken split generation reached **$6.2\%$** (commercial tolerance $\le 1.5\%$).
- **Remediation:** Invented the **Two-Stage Tempered Fluid-Bed Schedule** ($62^\circ\text{C}$ for 22 min $\to 20$ min unheated tempering at $45^\circ\text{C} \to 52^\circ\text{C}$ for 18 min). Tempering relaxes the moisture gradient and tensile stress ($\sigma_{\theta\theta} \le 0.40\text{ MPa}$), crushing the crack rate to **$< 2.0\%$** and brokens to **$< 1.5\%$**.

---

## 3. Comprehensive Formulation Screening Matrix (Runs S0-01 to S1-14)

Across 14 rigorous controlled experimental batches, the interaction of chelation chemistry, pH, temperature, and drying was mapped:

| Run ID | Formulation Composition | pH | Temp (°C) | Time (min) | Cooked Force $F_{\text{WB}}$ (N) | Sensory 3-AFC ($p$-val) | Checking Rate (%) | Overall Assessment |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S0-01** | Deionized Water (Control) | 6.80 | 25.0 | 30 | $58.4 \pm 4.2$ | N/A (Untreated) | 0.8% | **FAILED** (Hard, raw core, HTC persists) |
| **S0-02** | $0.10\text{ M } \text{NaHCO}_3$ | 8.42 | 50.0 | 30 | $14.1 \pm 1.2$ | $p < 0.001$ (Severe) | 3.2% | **FAILED** (Soapy aftertaste, thiamine loss) |
| **S0-03** | $0.05\text{ M } \text{Na}_2\text{CO}_3$ | 9.85 | 45.0 | 30 | $12.8 \pm 1.5$ | $p < 0.001$ (Severe) | 5.1% | **FAILED** (Saponification, dark brown colour) |
| **S0-04** | $0.05\text{ M}$ Citric Acid (Unbuffered) | 3.12 | 50.0 | 30 | $42.6 \pm 3.8$ | $p = 0.012$ (Sour) | 2.1% | **FAILED** (Protonated carboxylates, hard) |
| **S0-05** | $0.08\text{ M}$ Na-Citrate | 7.85 | 68.0 | 15 | $16.5 \pm 2.1$ | $p = 0.045$ (Off) | 8.4% | **FAILED** (Starch gelatinization, fouling) |
| **S0-06** | $0.05\text{ M}$ Na-Citrate + $0.02\text{ M}$ Citric | 5.20 | 45.0 | 45 | $22.4 \pm 2.6$ | $p = 0.280$ (Clean) | 1.9% | **PARTIAL** (Under-tenderized; $F_{\text{WB}} > 18\text{ N}$) |
| **S0-07** | $0.10\text{ M}$ EDTA-Disodium | 4.80 | 48.0 | 30 | $13.9 \pm 1.1$ | $p = 0.002$ (Metallic)| 1.8% | **FAILED** (Not permitted in dal by FSSAI) |
| **S1-01** | $0.08\text{ M}$ SHMP (Standalone) | 6.10 | 48.0 | 30 | $19.2 \pm 2.0$ | $p = 0.065$ (Marginal)| 2.4% | **PARTIAL** (Insufficient buffer capacity) |
| **S1-04** | $0.12\text{ M}$ Na-Citrate (Unbuffered) | 7.85 | 48.0 | 30 | $15.8 \pm 1.4$ | $p = 0.008$ (Saline) | 4.2% | **FAILED** (White salt bloom on drying) |
| **S1-07** | S1-09 Buffer + 1-Stage 65°C Drying | 5.20 | 48.0 | 24 | $15.1 \pm 1.2$ | $p = 0.380$ (Clean) | 14.8% | **FAILED** (Severe cotyledon checking) |
| **S1-08** | S1-09 Buffer, 18 min soak | 5.20 | 48.0 | 18 | $21.5 \pm 2.2$ | $p = 0.450$ (Clean) | 1.6% | **PARTIAL** (Insufficient penetration depth) |
| **S1-09** | **0.085M Cit + 0.025M CA + 0.035M SHMP**| **5.20** | **48.0**| **24** | **15.2 ± 1.1** | **p = 0.420 (Clean)** | **1.8%** | **SUCCESS: PRIMARY COMMERCIAL FORMULATION** |
| **S1-12** | S1-09 Buffer, 32 min soak | 5.20 | 48.0 | 32 | $14.8 \pm 0.9$ | $p = 0.410$ (Clean) | 2.1% | **PASSED** (Over-hydrated; excess drying load)|
| **S1-14** | S1-09 Buffer + 85% NF Recycle Liquor | 5.22 | 48.0 | 24 | $15.4 \pm 1.2$ | $p = 0.390$ (Clean) | 1.9% | **SUCCESS: CLOSED-LOOP WATER RECOVERY** |

---

## 4. Key Successes & Validated Operating Parameters

The successful execution of Formulation **S1-09** coupled with **Two-Stage Tempered Fluid Bed Drying** delivers the complete commercial engineering solution:

1. **Two-Whistle Cookability Verified:** Cooked shear force drops to **$15.2 \pm 1.1\text{ N}$**, beating the target criterion ($F_{\text{WB}} \le 18.0\text{ N}$) and matching premium fresh domestic desi dal ($16.1\text{ N}$).
2. **Zero Detectable Aftertaste:** Formal 3-AFC triangle sensory evaluation with 30 panellists achieved $p = 0.420$ (null hypothesis cannot be rejected; treated sample is statistically indistinguishable from untreated reference dal).
3. **Mechanical Integrity Preserved:** Cotyledon checking held at **$1.8\%$** and broken split generation at **$1.1\%$**, fully compliant with Grade 1 pulse milling standards.
4. **Residue Safety Margin:** Single-pass hydro-wash leaves surface salts below detection ($< 27.6\text{ ppm}$), while internal phosphate ($142\text{ mg/kg}$) is $35\times$ below FSSAI statutory limits ($5,000\text{ mg/kg}$).
5. **Closed-Loop Water Recycling (S1-14):** Nanofiltration membrane separation recovers **$85\%$** of rinse water and concentrates spent salts into a non-toxic mineral brine cake, drastically lowering effluent volume to $< 0.15\text{ m}^3/\text{day}$.

---

### Associated Documentation

- First-Principles Physics & Kinetic Derivations: [02_PHYSICS_AND_CHEMICAL_ENGINEERING_SOLUTION.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/02_PHYSICS_AND_CHEMICAL_ENGINEERING_SOLUTION.md)
- Complete Equipment Schedules & P&ID: [04_EQUIPMENT_SPECIFICATIONS_AND_PID_SCHEDULE.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/04_EQUIPMENT_SPECIFICATIONS_AND_PID_SCHEDULE.md)
- Scale-Up Roadmap & Decision Gates: [05_FIVE_PHASE_SCALEUP_ROADMAP_AND_GATE_CRITERIA.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/05_FIVE_PHASE_SCALEUP_ROADMAP_AND_GATE_CRITERIA.md)
- Regulatory & Food Safety Dossier: [07_REGULATORY_COMPLIANCE_AND_FOOD_SAFETY_DOSSIER.md](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/docs/commercial/07_REGULATORY_COMPLIANCE_AND_FOOD_SAFETY_DOSSIER.md)
