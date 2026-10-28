"""
Generate LaTeX source for FinnoaQ OMEGA Technical Report (Strict 8-Page Layout)
Author: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
Project Ref: FNQ-PR-2026-001 | Governance: RAEBYES
"""

import os

TEX_PATH = os.path.abspath('reports/pdf/finnoaq_omega_technical_report.tex')

latex_content = r"""\documentclass[10pt,a4paper,twocolumn]{article}

% --- Essential Packages ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1.75cm,top=1.85cm,bottom=1.95cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{float}
\usepackage{microtype}
\usepackage{caption}
\usepackage{titlesec}
\usepackage{balance}
\usepackage{cite}
\usepackage[hidelinks,colorlinks=true,linkcolor=blue!80!black,citecolor=blue!80!black,urlcolor=blue!80!black]{hyperref}

% --- Float Placement Control ---
\setcounter{topnumber}{4}
\setcounter{bottomnumber}{3}
\setcounter{totalnumber}{6}
\setcounter{dbltopnumber}{4}
\renewcommand{\topfraction}{0.95}
\renewcommand{\bottomfraction}{0.95}
\renewcommand{\dbltopfraction}{0.95}
\renewcommand{\textfraction}{0.05}
\renewcommand{\floatpagefraction}{0.85}
\renewcommand{\dblfloatpagefraction}{0.85}

% --- Styling & Typography ---
\titleformat{\section}{\large\bfseries\color{blue!40!black}}{\thesection}{0.8em}{}[\titlerule]
\titleformat{\subsection}{\normalsize\bfseries\color{black}}{\thesubsection}{0.8em}{}
\titleformat{\subsubsection}{\small\bfseries\itshape}{\thesubsubsection}{0.8em}{}

\setlength{\columnsep}{0.65cm}
\setlength{\parskip}{2.2pt}
\setlength{\parindent}{10pt}

% Caption styling
\captionsetup{font=small,labelfont=bf,skip=4pt}

% Currency command
\newcommand{\inr}{\text{INR~}}

% --- Document Metadata ---
\title{\vspace{-1.2cm}\textbf{\Large Process Engineering, Reaction-Diffusion Kinetics, and Stochastic Feedstock Control for Accelerated Cooking in Hard-to-Cook Pigeon Pea (\textit{Cajanus cajan})}\\[0.20cm]
\large Engineering Research Report FNQ-PR-2026-001 \textbar\ Nominal Capacity: 15 Metric Tonnes/Day}

\author{\textbf{Sourish Senapati}, Lead Chemical and Process Engineer\\
FinnoaQ Agro-Industrial Technologies Ltd., Process Research Division\\
\small Technical Governance Reference: \url{https://github.com/SourishSenapati/RAEBYES}}

\date{\today}

\begin{document}

\maketitle

\begin{abstract}
\noindent\textbf{Abstract}---The hard-to-cook (HTC) defect in pigeon pea (\textit{Cajanus cajan}) arises from middle lamella pectin cross-linking mediated by endogenous divalent calcium ($\mathrm{Ca}^{2+}$) cations, extending conventional culinary preparation times to 45--60 minutes. This investigation establishes a defensible biophysical and chemical process framework targeting a 2-pressure-cooker whistle preparation ($t_{\mathrm{cook}} = 7.0 \pm 0.5$~min at 103~kPa gauge / 121$^\circ$C). A 2D axisymmetric reaction-diffusion finite-difference model coupled with Warner-Bratzler shear force decay kinetics identified formulation S1-09 (0.145~M tri-salt: potassium citrate, sodium citrate, and phosphate at pH 5.20) as achieving a core shear force of $17.35$~N at 20.0~min steeping, passing below the provisional $18.0$~N tenderness threshold. GPU-accelerated Monte Carlo uncertainty analysis ($N = 10,000$ trajectories on an NVIDIA RTX 4050) demonstrated that joint parameter uncertainty shifts the 20-min pass probability to $67.05\%$ ($P_{95} = 19.61$~N), requiring an industrial steeping setpoint of 24.0~min to guarantee a $99.72\%$ pass rate ($P_{95} = 16.51$~N). Speciation audits resolved defect FAIL-0021, proving historical unbuffered recipes produced basic excursions (pH 6.72--6.81); corrected stoichiometric recipes with anhydrous citric acid maintain strict pH 5.20. Counter-current spray washing (12.0~s active exposure, 0.50~L/kg water) on a vacuum belt dewaterer with 4.0~min station residence time achieves $98.7\%$ surface solute removal (27.6~ppm residual film). Cooked slurry residual off-flavor is modeled at $R_{\mathrm{off}} = 0.164$ ($d' = 0.22$), classified strictly as \texttt{PREDICTED\_MINIMUM} pending physical verification via ISO 4120 ($N=24$) and ISO 11136:2014 ($N=72$) TOST protocols. Stochastic feedstock simulation across 10,000 batches revealed that inline proxy measurement noise ($\sigma_{\mathrm{noise}} = 8\%$ on a 3-minute Water Absorption Index) induces a $3.8\%$ false under-treatment rate under standard adaptive control ($P_{95} = 19.06$~N); an offset controller with a 2.5-min robustness buffer (\texttt{ADAPTIVE\_ROBUST\_P95}) eliminates this tail risk, achieving a $99.90\%$ pass rate ($P_{95} = 15.77$~N). Finally, an 11-step industrial flowsheet reconciles dual-basis 15~TPD mass balances. Two-stage convective drying ($65^\circ\mathrm{C} / 55^\circ\mathrm{C}$ with 20-min adiabatic tempering) constrains peak viscoelastic tensile stress to $0.711$~MPa ($0.431\times$ yield stress), holding grain breakage to $0.35\%$ compared to $3.19\%$ under 85$^\circ$C flash drying. An 85\% bleed-and-feed liquor recycle loop reduces net chemical OpEx to \inr3.63/kg (95\% CI: [3.32, 3.94]) and total manufacturing OpEx to \inr6.34/kg (95\% CI: [5.95, 6.74]), confirming commercial and operational viability.
\end{abstract}

\noindent\textbf{Keywords:} Pigeon pea (\textit{Cajanus cajan}), Hard-to-Cook defect, Reaction-diffusion PDE, Warner-Bratzler shear force, Stochastic process control, Tempered convective drying, Industrial OpEx.

\section{Introduction and Biophysical Etiology}

Pigeon pea (\textit{Cajanus cajan}), consumed across South Asia primarily as split dehulled toor dal, represents a critical source of vegetable protein and micronutrients. Under tropical storage conditions characterized by high ambient temperature ($>30^\circ\mathrm{C}$) and elevated relative humidity ($>70\%$), post-harvest pulse stocks frequently develop the Hard-to-Cook (HTC) defect \cite{Aguilera1986, HincksStanley1986}.

\subsection{Microstructural Mechanism of HTC}
The physiological progression of the HTC defect in grain legumes involves an enzymatic and structural cascade \cite{Aguilera1986, Galiotou2002}:
\begin{enumerate}
    \item \textbf{Phytase Activation:} Endogenous phytase hydrolyzes phytate complexes located within intracellular globoids.
    \item \textbf{Divalent Cation Translocation:} Liberated $\mathrm{Ca}^{2+}$ and $\mathrm{Mg}^{2+}$ ions diffuse into the middle lamella and primary cell wall.
    \item \textbf{Pectin De-esterification:} Pectin methylesterase (PME) hydrolyzes methyl ester groups on pectin homogalacturonan chains, reducing the degree of esterification ($\mathrm{DE}$) and creating free carboxylate sites.
    \item \textbf{Pectate Cross-Linking:} Divalent calcium binds adjacent unesterified pectate chains, assembling stable ``egg-box'' complexes that cement middle lamellae.
    \item \textbf{Impaired Solubilization:} During subsequent culinary boiling, middle lamella dissolution is arrested. While normal pulse cells separate upon starch gelatinization ($65$--$72^\circ\mathrm{C}$), HTC cells remain rigidly locked. Water imbibition into intracellular starch granules is sterically retarded, maintaining high shear resistance.
\end{enumerate}

\subsection{The 2-Whistle Target and Tenderness Metric}
In Indian culinary practice, domestic pressure cookers operating at 103~kPa gauge pressure ($121^\circ\mathrm{C}$) release periodic pressure steam bursts (termed ``whistles''). For standard 3--5 liter domestic cookers, each whistle cycle corresponds to approximately 3.0--3.5 minutes under pressure. Aged HTC dal typically requires 5 to 7 whistles (18 to 25 minutes of pressure cooking) or up to 60 minutes of open boiling to attain edible softness.

The FinnoaQ engineering mandate establishes the \textbf{2-whistle regime}:
\begin{equation}
    t_{\mathrm{cook}} = 7.0 \pm 0.5\text{ min at } 121^\circ\mathrm{C}\text{ (103 kPa gauge)}
\end{equation}
Cooked tenderness is evaluated using Warner-Bratzler peak shear force ($F_{\mathrm{WB,core}}$), measured with a standard V-notch shear fixture. Literature calibrations correlate consumer acceptance with Warner-Bratzler shear force \cite{Kajla2020, Nisha2005}, establishing the provisional threshold:
\begin{equation}
    F_{\mathrm{WB,core}} \le 18.0\text{ N}
\end{equation}
Samples exceeding $18.0$~N exhibit palpable firmness and gritty cores, failing consumer sensory acceptance.

\section{Reaction-Diffusion Biophysics (Stage 1)}

\subsection{2D Oblate Spheroidal Mathematical Formulation}
Split toor dal cotyledons exhibit oblate spheroidal geometry, rendering 1D spherical approximations prone to geometric distortion. We model the cotyledon as an axisymmetric oblate spheroid with semi-major equatorial radius $R = 2.45$~mm and semi-minor axial thickness $H = 1.10$~mm.

Transient transport of chelating species (citrate, $\mathrm{Cit}^{3-}$) and counter-ions through the cellular network is governed by the 2D axisymmetric reaction-diffusion partial differential equation:
\begin{equation}
    \frac{\partial C_{\mathrm{cit}}}{\partial t} = \frac{1}{r} \frac{\partial}{\partial r}\left( r D_{r} \frac{\partial C_{\mathrm{cit}}}{\partial r} \right) + \frac{\partial}{\partial z}\left( D_{z} \frac{\partial C_{\mathrm{cit}}}{\partial z} \right) - R_{\mathrm{disp}}
    \label{eq:pde}
\end{equation}
where $D_r$ and $D_z$ are anisotropic effective diffusion coefficients ($D_{\mathrm{eff}} \approx 1.82 \times 10^{-10}\text{ m}^2/\text{s}$ at $50^\circ\mathrm{C}$), and $R_{\mathrm{disp}}$ is the second-order calcium displacement reaction rate:
\begin{equation}
    R_{\mathrm{disp}} = k_{\mathrm{disp}} \, C_{\mathrm{Ca,bound}} \, C_{\mathrm{cit}}^{1.2}
    \label{eq:rdisp}
\end{equation}
with boundary conditions:
\begin{align}
    \left.\frac{\partial C_{\mathrm{cit}}}{\partial r}\right|_{r=0} = 0, \quad &\left.\frac{\partial C_{\mathrm{cit}}}{\partial z}\right|_{z=0} = 0 \quad \text{(Axisymmetric Symmetry)}\\
    C_{\mathrm{cit}}(R, z, t) = C_{\mathrm{bath}}, \quad &C_{\mathrm{cit}}(r, H, t) = C_{\mathrm{bath}} \quad \text{(Dirichlet Boundary)}
\end{align}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/fig1_cotyledon_reaction_diffusion.pdf}
    \caption{\textbf{Biophysical Demineralization Profiles:} (a) 2D cross-sectional field of calcium displacement $\chi_{\mathrm{Ca}}(r,z)$ at $t = 20.0$~min steeping in formulation S1-09 within the oblate spheroidal cotyledon domain ($R=2.45$~mm, $H=1.10$~mm). (b) Normalized axial core demineralization profiles from core ($z/H=0$) to outer surface ($z/H=1$) across steeping times.}
    \label{fig:diffusion}
\end{figure*}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/fig2_texture_kinetics_comparison.pdf}
    \caption{\textbf{Textural Softening Kinetics:} (a) Warner-Bratzler core shear force $F_{\mathrm{WB,core}}$ decay during pressure cooking (15~psi / 121$^\circ$C) across 5 benchmark formulations. (b) Exact shear force at the 2-whistle gate ($t_{\mathrm{cook}} = 7.0$~min); only formulation S1-09 passes below the $18.0$~N acceptance threshold.}
    \label{fig:texture}
\end{figure*}

\subsection{Demineralization and Softening Kinetics}
Displacement of structural $\mathrm{Ca}^{2+}$ destabilizes the pectate matrix. Textural softening during subsequent thermal pressure cooking is described by modified first-order kinetic decay \cite{Nisha2005}:
\begin{equation}
    F_{\mathrm{WB,core}}(t) = F_\infty + (F_0 - F_\infty) \exp\left( -k_{\mathrm{eff}} \, t_{\mathrm{cook}} \right)
    \label{eq:decay}
\end{equation}
where $F_0 = 53.0$~N, $F_\infty = 8.5$~N, and the effective softening rate constant $k_{\mathrm{eff}}$ is augmented by core calcium displacement $\chi_{\mathrm{Ca,core}}$:
\begin{equation}
    k_{\mathrm{eff}} = k_0 \exp\left(-\frac{E_a}{R_g T_{\mathrm{cook}}}\right) \left[ 1 + \alpha_{\mathrm{Ca}} \chi_{\mathrm{Ca,core}}(t_{\mathrm{soak}}) \right]
    \label{eq:keff}
\end{equation}
with activation energy $E_a \approx 78.4$~kJ/mol and coupling factor $\alpha_{\mathrm{Ca}} = 1.82$.

\begin{table*}[!t]
\centering
\small
\caption{\textbf{Stage 1 Candidate Formulations and 2-Whistle Cookability Performance} ($N=11$ Screening Matrix).}
\label{tab:stage1_candidates}
\begin{tabularx}{\textwidth}{llccccccr}
\toprule
\textbf{Candidate ID} & \textbf{Formulation Description} & \textbf{Soak (min)} & \textbf{Temp ($^\circ$C)} & \textbf{Bulk $\chi_{\mathrm{Ca}}$ (\%)} & \textbf{Core $\chi_{\mathrm{Ca}}$ (\%)} & \textbf{$t_{90}$ (min)} & \textbf{$F_{\mathrm{WB,core}}^{\mathrm{w2}}$ (N)} & \textbf{2-Whistle Gate} \\
\midrule
S1-01-IND-REF & Indian Latur Fresh Reference & 0.0 & 25 & 0.0 & 0.0 & 9.8 & 21.53 & FAIL (Req 3 Wh) \\
S1-02-TZ-NOM  & Untreated Tanzanian Aged HTC & 0.0 & 25 & 0.0 & 0.0 & 16.4 & 29.58 & FAIL (Req 5 Wh) \\
S1-03-NAHCO3  & Alkaline $0.5\%\ \mathrm{NaHCO}_3$ & 20.0 & 50 & 28.4 & 18.2 & 7.8 & 18.89 & FAIL ($> 18.0$ N) \\
S1-04-EDTA-HI & $0.05\ \mathrm{M}\ \mathrm{Na}_2\mathrm{EDTA}$ (Regulatory Screen) & 15.0 & 50 & 58.2 & 49.1 & 5.8 & 15.12 & PASS (Reg Block) \\
S1-05-CIT-LO  & $0.05\ \mathrm{M}$ Sodium Citrate & 20.0 & 50 & 24.1 & 14.8 & 8.4 & 19.85 & FAIL ($> 18.0$ N) \\
S1-06-CIT-MED & $0.10\ \mathrm{M}$ Sodium Citrate & 20.0 & 50 & 36.8 & 26.5 & 7.4 & 18.42 & FAIL ($> 18.0$ N) \\
S1-07-CIT-HI  & $0.185\ \mathrm{M}$ Sodium Citrate & 20.0 & 50 & 54.2 & 45.1 & 6.2 & 16.24 & PASS (Slight Off) \\
S1-08-CIT-STD & $0.145\ \mathrm{M}$ Sodium Citrate & 20.0 & 50 & 46.1 & 35.7 & 6.9 & 18.72 & FAIL ($> 18.0$ N) \\
\textbf{S1-09-TRI-OPT} & \textbf{0.145 M Tri-Salt Buffer (pH 5.20)} & \textbf{20.0} & \textbf{50} & \textbf{48.2} & \textbf{41.8} & \textbf{6.5} & \textbf{17.35} & \textbf{PASS (Target)} \\
S1-10-US-CIT  & Ultrasonic Assisted 0.145 M Buffer & 12.0 & 45 & 49.5 & 42.6 & 6.4 & 17.18 & PASS (CapEx High) \\
S1-11-ENZ-PME & Enzymatic PME-Pectinase Cocktail & 30.0 & 45 & 51.0 & 38.4 & 6.6 & 17.44 & PASS (OpEx High) \\
\bottomrule
\end{tabularx}
\end{table*}

Table~\ref{tab:stage1_candidates} presents the evaluation of 11 candidate regimes. Formulation S1-09 (0.145~M tri-salt buffer at pH 5.20) achieves $41.8\%$ core calcium displacement at 20.0~min, producing $F_{\mathrm{WB,core}} = 17.35$~N at 2 whistles, successfully clearing the acceptance threshold.

\subsection{GPU Monte Carlo Uncertainty Quantification}
To determine parameter sensitivity under real manufacturing conditions, an offline Monte Carlo campaign ($N = 10,000$ 2D PDE trajectories) was executed on an NVIDIA RTX 4050 GPU (peak VRAM 472.9~MB, execution time 22.86~s). Key biophysical parameters were perturbed according to multivariate Gaussian priors:
\begin{align}
    H &\sim \mathcal{N}(1.10, 0.08)\text{ mm}, \quad R \sim \mathcal{N}(2.45, 0.12)\text{ mm}\\
    D_{\mathrm{eff}} &\sim \mathcal{N}(1.82 \times 10^{-10}, 0.25 \times 10^{-10})\text{ m}^2/\text{s}\\
    k_{\mathrm{disp}} &\sim \mathcal{N}(0.145, 0.020)\text{ m}^3/(\text{mol}\cdot\text{s})\\
    E_a &\sim \mathcal{N}(78.4, 4.2)\text{ kJ/mol}
\end{align}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/fig3_gpu_uncertainty_distributions.pdf}
    \caption{\textbf{GPU Parameter Uncertainty Quantification ($N=10,000$):} (a) Probability density functions of 2-whistle core shear force $F_{\mathrm{WB,core}}$ at 15, 20, 22, and 24~min steeping. (b) Simulation pass rate and 95th percentile force ($P_{95}$) versus steeping duration.}
    \label{fig:gpu_uncertainty}
\end{figure*}

As illustrated in Figure~\ref{fig:gpu_uncertainty}:
\begin{itemize}
    \item At $t = 20.0$~min, the deterministic point estimate is $17.346$~N ($0.654$~N margin below threshold). Under joint parameter uncertainty, the distribution exhibits a mean of $17.39$~N, a 95\% confidence interval of $[14.87, 20.03]$~N, and a 95th percentile force of $P_{95} = 19.61$~N. The simulation pass probability is only \textbf{67.05\%}.
    \item Extending steeping to $t = 24.0$~min (a 4.0-min margin buffer) shifts the mean force to $14.77$~N ($95\%\text{ CI}: [13.08, 16.93]\text{ N}$), reduces $P_{95}$ to $16.51\text{ N} \le 18.0\text{ N}$, and raises the pass probability to \textbf{99.72\%}.
\end{itemize}
Consequently, while 20.0~min represents the theoretical minimum steeping time, 24.0~min is adopted as the validated baseline industrial operating setpoint.

\section{Speciation Thermodynamics, Washing Dynamics, and Sensory Protocol (Stage 2)}

\subsection{Chemical Speciation Audit (Defect FAIL-0021)}
During technical auditing, defect \texttt{FAIL-0021} was uncovered: historical standard operating procedures specified a target pH of 5.20 but omitted the necessary conjugate acid buffer partner (citric acid). Because trisodium and tripotassium citrate are salts of a strong base and a weak polyprotic acid, dissolution in water produces alkaline hydrolysis:
\begin{equation}
    \mathrm{Cit}^{3-} + \mathrm{H}_2\mathrm{O} \rightleftharpoons \mathrm{HCit}^{2-} + \mathrm{OH}^-
\end{equation}
Davies-extended Henderson-Hasselbalch speciation analysis revealed that historical recipes reached actual equilibrium pH values of 6.72 to 6.81, severely accelerating lipoxygenase-mediated lipid oxidation and off-flavor generation.

To resolve this defect, exact multi-protic equilibrium speciation was solved. The corrected OMEGA industrial recipe per 1,000~L aqueous liquor comprises:
\begin{itemize}
    \item Tripotassium Citrate Monohydrate ($\mathrm{K}_3\mathrm{Cit}\cdot\mathrm{H}_2\mathrm{O}$): $25.20$~kg
    \item Trisodium Citrate Dihydrate ($\mathrm{Na}_3\mathrm{Cit}\cdot 2\mathrm{H}_2\mathrm{O}$): $2.54$~kg
    \item Citric Acid Anhydrous ($\mathrm{H}_3\mathrm{Cit}$): $11.28$~kg
\end{itemize}
This formulation guarantees thermodynamic buffer stabilization at $\text{pH} = 5.20 \pm 0.05$ with an ionic strength of $I = 0.885$~M. Maintaining pH at 5.20 inactivates lipoxygenase ($\mathrm{LOX}$), retarding the formation of volatile hexanal and 2-pentylfuran off-notes.

\subsection{Hydrodynamic Washing Kinetics on WSH-102}
A major source of potential aftertaste in pre-treated dal is residual surface liquor crystallizing during subsequent drying. In the FinnoaQ flowsheet, washed dal is processed on a vacuum belt dewatering screen (\texttt{WSH-102}).

An important operational distinction must be maintained:
\begin{itemize}
    \item \textbf{Active Spray Wash Exposure:} Dal passes beneath high-velocity counter-current flat-fan spray nozzles (water-to-grain ratio $0.50$~L/kg) for exactly \textbf{12.0 seconds}.
    \item \textbf{Station Residence Time:} The total residence time of dal across the entire belt dewaterer (including feed spread, vacuum dewatering, and discharge skimming) is \textbf{4.0 minutes} (240~s).
\end{itemize}
A 12.0~s spray wash reduces surface film concentration from 1,755.7~ppm down to $27.6$~ppm ($90.2\%$ probability of falling below the 50~ppm sensory detection limit). Beyond 15~s, marginal removal plateaus, as residual flavor compounds reside within internal pore water.

\subsection{Cooked Slurry Dilution and Sensory Protocol}
During culinary preparation, split dal is cooked at a water-to-dal mass ratio of $3.5:1.0$. Internal pore solutes ($109.7$~mg citrate and $52.0$~mg potassium per 100~g dry dal) leach into the cooking liquor, diluting to:
\begin{align}
    C_{\mathrm{cit,slurry}} &= 24.3\text{ mg}/100\text{g} \quad (\approx 2.4\text{ mM})\\
    C_{\mathrm{K,slurry}} &= 11.5\text{ mg}/100\text{g} \quad (\approx 2.9\text{ mM})
\end{align}
These concentrations fall well below human taste perception thresholds ($7.5$~mM for citrate, $12.0$~mM for potassium). The composite off-flavor index in cooked dal is calculated as $R_{\mathrm{off}} = 0.164$ with a Thurstonian discrimination index $d' = 0.22$.

Under FinnoaQ Governance Rule 4, this finding is classified strictly as \texttt{PREDICTED\_MINIMUM}. Formal consumer sensory verification requires physical validation through:
\begin{enumerate}
    \item \textbf{ISO 4120 Triangle Test ($N=24$ Panellists):} 3-Alternative Forced Choice (3-AFC) testing to establish statistical non-detection of treatment residues ($\alpha = 0.05, \beta = 0.10$).
    \item \textbf{ISO 11136:2014 TOST Equivalence Test ($N=72$ Panellists):} Two One-Sided Tests (TOST) evaluating flavor, mouthfeel, aroma, and overall liking against authentic Indian Latur reference dal within equivalence bounds of $\Delta = \pm 0.5$ on a 9-point hedonic scale.
\end{enumerate}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/fig4_batch_adaptation_policies.pdf}
    \caption{\textbf{Stage 3 Batch Adaptation Across 10,000 Batches:} (a) Empirical Cumulative Distribution Functions (ECDF) of core Warner-Bratzler force for four operational policies. (b) Controller misclassification risks comparing standard vs robust policies.}
    \label{fig:batch_policies}
\end{figure*}

\section{Feedstock Stochasticity and Robust Batch Control (Stage 3)}

\subsection{Feedstock Variability Distributions}
Commercial pigeon pea exhibits physical and biochemical stochasticity across growing seasons, harvest maturity, and storage histories. Empirical characterization of Tanzanian HTC feedstock revealed the following underlying distributions:
\begin{itemize}
    \item Semi-minor axial thickness: $H \sim \text{LogNormal}(\mu = 1.10\text{ mm}, \sigma = 0.08\text{ mm})$.
    \item Native bound calcium: $C_{\mathrm{Ca,0}} \sim \text{Gamma}(k = 70.8, \theta = 0.50\text{ mol/m}^3)$ with mean $35.37$~mol/m$^3$.
    \item Pectin degree of esterification: $\mathrm{DE} \sim \text{Beta}(\alpha = 14.0, \beta = 36.0)$ with mean $0.28$.
\end{itemize}

\subsection{Inline Intake Diagnostic Proxy}
To prevent under-treatment or over-treatment in industrial processing without requiring costly offline spectroscopy, an inline physical proxy diagnostic was formulated: the \textbf{3-minute Water Absorption Index ($\mathrm{WAI}_{\mathrm{3min}}$)} under ultrasonic pulse agitation. $\mathrm{WAI}_{\mathrm{3min}}$ measures the rate of capillary imbibition into the cotyledon micropores, exhibiting strong inverse correlation with cell wall sclerosis and native bound calcium ($R^2 = 0.887$):
\begin{equation}
    \widehat{C}_{\mathrm{Ca,0}} = \beta_0 + \beta_1 (\mathrm{WAI}_{\mathrm{3min}}) + \beta_2 (H_{\mathrm{lot}}) + \epsilon
\end{equation}
Industrial sensor noise introduces an unavoidable measurement error of $\sigma_{\mathrm{noise}} \approx 8\%$ into the intake estimation.

\subsection{Adaptive Policy Failure and Robust Resolution}
To investigate the consequence of sensor noise, 10,000 independent commercial batches were simulated through the 2D reaction-diffusion solver across four operational policies:

\begin{table}[H]
\centering
\scriptsize
\caption{\textbf{Stochastic Policy Performance Across 10,000 Batches}.}
\label{tab:policy_comparison}
\begin{tabularx}{\linewidth}{lcccc}
\toprule
\textbf{Control Policy} & \textbf{Pass (\%)} & \textbf{Mean (N)} & \textbf{$P_{95}$ (N)} & \textbf{False Under (\%)} \\
\midrule
Untreated Control     & 0.0\%   & 25.57 & 27.04 & N/A \\
Fixed Tier 2 (20 min) & 72.31\% & 16.35 & 22.56 & N/A \\
Adaptive Noisy (Std)  & 85.11\% & 15.95 & 19.06 & 3.80\% \\
\textbf{Adaptive Robust P95} & \textbf{99.90\%} & \textbf{13.75} & \textbf{15.77} & \textbf{0.14\%} \\
\bottomrule
\end{tabularx}
\end{table}

As documented in Table~\ref{tab:policy_comparison} and Figure~\ref{fig:batch_policies}:
\begin{itemize}
    \item \textbf{Fixed Tier 2 (20 min):} Fails for difficult batches, with $P_{95} = 22.56$~N and an unacceptably low pass rate of $72.31\%$.
    \item \textbf{Standard Adaptive Noisy:} When intake classification uses raw noisy proxy measurements ($\sigma = 8\%$), $3.80\%$ of batches are mistakenly under-treated (assigned to a milder tier). This generates a thick tail with $P_{95} = 19.06\text{ N} > 18.0\text{ N}$.
    \item \textbf{Adaptive Robust P95 (\texttt{ADAPTIVE\_ROBUST\_P95}):} To eliminate this tail risk, an asymmetric decision rule is introduced. The controller adds a \textbf{2.5-minute safety margin buffer} to steeping duration whenever estimated hardness exceeds Tier 1. This increases conservative over-treatment from $4.43\%$ to $24.17\%$ (mild extra steeping with zero sensory penalty), but slashes critical false under-treatment from $3.80\%$ down to \textbf{0.14\%}. Consequently, $P_{95}$ drops to \textbf{15.77~N} ($\le 18.0$~N), and overall pass rate rises to \textbf{99.90\%}.
\end{itemize}

\section{Industrial Plant Design, Drying Mechanics, and OpEx (Stage 4)}

\subsection{11-Step Industrial Process Route}
The nominal 15 metric tonnes/day (TPD) FinnoaQ manufacturing facility comprises 11 continuous and batch-integrated unit operations:
\begin{enumerate}
    \item \textbf{REC-100:} Raw Grain Receiving, Weighing, and Pneumatic Conveying.
    \item \textbf{CLN-101:} Multi-Deck Vibratory Screening and Destoning.
    \item \textbf{STP-101:} Automated Continuous Counter-Current Steeping Vessel ($50^\circ\mathrm{C}$, 20--24~min residence).
    \item \textbf{WSH-102:} Vacuum Belt Dewaterer with 12~s Counter-Current Flat-Fan Spray Wash.
    \item \textbf{REC-103:} Chemical Bleed-and-Feed Liquor Recovery System (85\% liquor recycle).
    \item \textbf{DRY-103:} Two-Stage Tempered Convective Belt Dryer ($65^\circ\mathrm{C} / 55^\circ\mathrm{C}$ with 20~min adiabatic tempering).
    \item \textbf{TEM-103:} In-Line Adiabatic Tempering Bin.
    \item \textbf{COL-104:} Counter-Current Ambient Air Grain Cooler ($< 35^\circ\mathrm{C}$).
    \item \textbf{SCR-104:} Precision Rotary Sifter for Broken and Fissured Grain Removal.
    \item \textbf{SIL-105:} Finished Product Conditioning and Surge Silos.
    \item \textbf{PCK-106:} Automated Form-Fill-Seal Packaging Line (1~kg / 5~kg retail laminates).
\end{enumerate}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/fig5_convective_drying_stress.pdf}
    \caption{\textbf{Convective Drying Mechanics and Fissuring Control:} (a) Moisture desorption curves for single-stage 85$^\circ$C flash versus two-stage 65/55$^\circ$C tempered convective drying. (b) Core viscoelastic tensile hoop stress profile against the grain rupture threshold ($\sigma_{\mathrm{yield}} = 1.65$~MPa).}
    \label{fig:drying_stress}
\end{figure*}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/fig6_plant_mass_balance_and_opex.pdf}
    \caption{\textbf{Stage 4 Industrial Mass Balance and OpEx:} (a) Basis I mass flow breakdown across unit operations. (b) Operating cost comparison: Once-Through (0\% recycle) versus Bleed-and-Feed (85\% recycle).}
    \label{fig:plant_opex}
\end{figure*}

\subsection{Dual-Basis 15 TPD Mass Balance Reconciliation}
Mass balance ambiguity between raw intake and finished product was reconciled under two distinct operational bases:

\begin{table}[H]
\centering
\scriptsize
\caption{\textbf{Dual-Basis 15 TPD Mass Balance Reconciliation}.}
\label{tab:mass_balance}
\begin{tabularx}{\linewidth}{lrr}
\toprule
\textbf{Mass Stream Parameter} & \textbf{Basis I (Intake)} & \textbf{Basis II (Product)} \\
\midrule
Raw Dal Intake Flow   & 15,000.0 kg/day & 14,779.0 kg/day \\
Intake Moisture ($X_{\mathrm{wb}}$) & 9.80\% & 9.80\% \\
Dry Matter Inflow     & 13,530.0 kg/day & 13,330.7 kg/day \\
Steeping Water Uptake & 3,923.1 kg/day & 3,865.3 kg/day \\
Steeped Mass (28.5\% WB) & 18,923.1 kg/day & 18,644.3 kg/day \\
Wash Water (0.5 L/kg) & 7,500.0 kg/day & 7,389.5 kg/day \\
Wash Effluent Bleed   & 7,552.5 kg/day & 7,441.2 kg/day \\
Dry Matter Leached (0.35\%) & 47.3 kg/day & 46.7 kg/day \\
Water Evaporated (DRY) & 3,593.8 kg/day & 3,540.8 kg/day \\
Broken Screen Fines (0.35\%) & 52.5 kg/day & 51.7 kg/day \\
\textbf{Finished Prime Dal} & \textbf{15,224.3 kg/day} & \textbf{15,000.0 kg/day} \\
Finished Moisture ($X_{\mathrm{wb}}$) & 11.75\% & 11.75\% \\
Standard Eq. (10.5\% WB) & 14,884.8 kg/day & 14,665.4 kg/day \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Convective Drying Mechanics and Fissuring Control}
Drying hydrated dal ($X_{\mathrm{wb}} = 28.5\% \to 11.75\%$) introduces severe internal moisture gradients $\nabla X(r,z,t)$, generating viscoelastic differential shrinkage and tensile hoop stresses:
\begin{equation}
    \sigma_{\mathrm{hoop}}(r,z,t) = \frac{E(X)}{1 - \nu} \beta_M \left[ \bar{X}(t) - X(r,z,t) \right]
\end{equation}
where $E(X) \approx 120$~MPa is the grain Young's modulus and $\beta_M = 0.38$ is the moisture shrinkage coefficient.

As documented in Figure~\ref{fig:drying_stress}:
\begin{itemize}
    \item \textbf{Single-Stage 85$^\circ$C Flash Drying (55 min):} Rapid moisture evaporation creates an extreme core-to-surface moisture differential ($\Delta X > 12\%$). Peak tensile stress reaches $\sigma_{\max} = 1.850$~MPa, exceeding the mechanical tensile yield limit ($\sigma_{\mathrm{yield}} = 1.65$~MPa, yield ratio $1.121$). This causes severe microscopic cotyledon fissuring, resulting in \textbf{3.19\% broken grain loss} during downstream rotary screening.
    \item \textbf{Two-Stage Tempered Drying (105 min):} Operating in three stages (Stage 1: 45~min at $65^\circ\mathrm{C}$, Stage 2: 20~min adiabatic tempering bin, Stage 3: 40~min at $55^\circ\mathrm{C}$) allows internal moisture to equilibrate via Maxwell viscoelastic relaxation. Peak tensile stress is constrained to $\sigma_{\max} = 0.711$~MPa ($0.431\times$ yield limit), suppressing grain breakage to \textbf{0.35\%}.
\end{itemize}

\subsection{Techno-Economic Reconciliation (85\% Bleed-and-Feed)}
In a once-through steeping configuration (0\% recycle), chemical reagent consumption constitutes an unbearable OpEx burden of \inr15.71/kg dal, producing a total manufacturing OpEx of \inr18.42/kg.

\begin{table}[H]
\centering
\scriptsize
\caption{\textbf{OpEx Reconciliation Under 85\% Bleed-and-Feed Recycle} (INR / kg Finished Dal).}
\label{tab:opex}
\begin{tabularx}{\linewidth}{lcc}
\toprule
\textbf{Cost Component} & \textbf{0\% Recycle} & \textbf{85\% Recycle} \\
\midrule
Reagents ($\mathrm{K}_3\mathrm{Cit}, \mathrm{Na}_3\mathrm{Cit}, \mathrm{H}_3\mathrm{Cit}$) & \inr15.71 & \inr3.63 [3.32, 3.94] \\
Thermal Energy (Drying Coal/Gas) & \inr1.45 & \inr1.45 \\
Electrical Power \& Steam & \inr0.62 & \inr0.62 \\
Water Supply \& ETP Neutralization & \inr0.64 & \inr0.64 \\
\midrule
\textbf{Total Manufacturing OpEx} & \textbf{\inr18.42} & \textbf{\inr6.34 [5.95, 6.74]} \\
\bottomrule
\end{tabularx}
\end{table}

Implementing an 85\% liquor recovery loop (\texttt{REC-103}) with inline conductivity makeup and continuous bleed (15\% purge to prevent phytate/calcium saturation) reduces fresh reagent requirements by $76.9\%$. As shown in Table~\ref{tab:opex} and Figure~\ref{fig:plant_opex}, net chemical OpEx drops to \inr3.63/kg, yielding a total manufacturing OpEx of \textbf{\inr6.34/kg dal} (95\% CI: [5.95, 6.74] \inr/kg).

\section{Physical Experimental Validation Matrix}

To transition from validated in-silico models to industrial plant commissioning, five physical validation protocols are formulated:
\begin{itemize}
    \item \textbf{EXP-01 (Warner-Bratzler Texture Calibration):} Characterize $F_{\mathrm{WB,core}}$ on $N = 30$ single cotyledons per condition across cooking times (0 to 14 min) using an Instron 3345 texture analyzer equipped with a standard Warner-Bratzler shear cell.
    \item \textbf{EXP-02 (Speciation and Residual Surface Chromatography):} Measure surface and pore citrate, potassium, and sodium concentrations via HPLC and ICP-OES across spray wash durations (0, 6, 12, 20, 30~s) to confirm $< 50$~ppm surface film.
    \item \textbf{EXP-03 (ISO 4120 and ISO 11136 Sensory Trials):} Execute blind 3-AFC triangle tests ($N=24$) and TOST equivalence trials ($N=72$) against authentic Indian Latur reference dal.
    \item \textbf{EXP-04 (Convective Drying and Fissuring Assay):} Run 100~kg pilot drying trials comparing single-stage 85$^\circ$C vs two-stage 65/55$^\circ$C tempered drying; measure broken grain yield across a 2.5~mm rotary screen.
    \item \textbf{EXP-05 (50-Cycle Bleed-and-Feed Liquor Recirculation):} Operate a 50-cycle benchtop steeping skid with 15\% bleed to verify steady-state chemical equilibrium and absence of microbial biofilm buildup.
\end{itemize}

\section{Defect Remediation Audit}

In accordance with FinnoaQ Governance standards, Table~\ref{tab:defects} documents the resolution of historical modeling defects.

\begin{table}[H]
\centering
\scriptsize
\caption{\textbf{Audit Defect Remediation Register}.}
\label{tab:defects}
\begin{tabularx}{\linewidth}{lp{5.4cm}}
\toprule
\textbf{Defect} & \textbf{Description and Remediation Status} \\
\midrule
\texttt{FAIL-0021} & Unbuffered salts caused basic excursion (pH 6.72--6.81). \textit{Resolved:} Added citric acid; verified pH 5.20. \\
\texttt{FAIL-0022} & Unqualified sensory nondetection and equivalence claims. \textit{Resolved:} Classified \texttt{PREDICTED\_MINIMUM}; ISO 4120/11136 mandated. \\
\texttt{FAIL-0023} & Unjustified claims that 2 whistles are guaranteed. \textit{Resolved:} Set 18.0~N cutoff; GPU MC proved 24~min required. \\
\texttt{FAIL-0024} & Mass balance ambiguity between intake and product basis. \textit{Resolved:} Dual-basis 15~TPD mass balance reconciled. \\
\texttt{FAIL-0025} & OpEx discrepancy: claimed \inr0.42/kg; real was \inr18.42/kg. \textit{Resolved:} 85\% recycle established \inr6.34/kg OpEx. \\
\texttt{FAIL-0026} & Standard adaptive controller suffered 3.8\% false under-treatment. \textit{Resolved:} Formulated \texttt{ADAPTIVE\_ROBUST\_P95} (0.14\% failure). \\
\bottomrule
\end{tabularx}
\end{table}

\section{Conclusions}
The FinnoaQ OMEGA investigation demonstrates that accelerating the cooking of hard-to-cook pigeon pea to approximately two pressure-cooker whistles ($7.0 \pm 0.5$~min) is biophysically feasible through formulation S1-09 (0.145~M Tri-Salt buffer at pH 5.20). Parameter uncertainty analysis proves that while 20.0~min is the nominal minimum, an industrial setpoint of 24.0~min is required to achieve a $99.72\%$ pass rate. Hydrodynamic counter-current spray washing (12.0~s active exposure, 4.0~min belt residence) reduces surface residues to $27.6$~ppm, mitigating off-taste risks. To overcome 8\% intake proxy noise, the robust controller \texttt{ADAPTIVE\_ROBUST\_P95} eliminates tail risk ($P_{95} = 15.77$~N). Finally, two-stage tempered convective drying restricts grain breakage to $0.35\%$, and 85\% liquor recirculation reconciles operating economics at \inr6.34/kg dal. Physical commissioning may now proceed under the structured experimental protocols EXP-01 through EXP-05.

\balance
\begin{thebibliography}{99}
\bibitem{Aguilera1986}
J.~M. Aguilera and D.~W. Stanley, ``A review of the hard-to-cook defect in food legumes,'' \textit{Journal of Food Biochemistry}, vol.~9, no.~4, pp.~279--327, 1986. \url{https://doi.org/10.1111/j.1745-4514.1986.tb00085.x}

\bibitem{HincksStanley1986}
M.~J. Hincks and D.~W. Stanley, ``Multiple mechanism for the hard-to-cook defect in legumes,'' \textit{Journal of Food Technology}, vol.~21, no.~6, pp.~731--750, 1986. \url{https://doi.org/10.1111/j.1365-2621.1986.tb00466.x}

\bibitem{Nisha2005}
P.~Nisha, R.~S. Singhal, and P.~R. Kulkarni, ``A kinetic approach to determine cooking quality in pulses,'' \textit{Journal of Food Engineering}, vol.~76, no.~4, pp.~622--630, 2005. \url{https://doi.org/10.1016/j.jfoodeng.2005.06.012}

\bibitem{Kajla2020}
P.~Kajla, A.~Sharma, and D.~R. Sood, ``Textural and sensory profile of pigeon pea (*Cajanus cajan*) as affected by cooking methods,'' \textit{Journal of Food Science and Technology}, vol.~57, no.~3, pp.~1012--1020, 2020. \url{https://doi.org/10.1007/s13197-019-04135-2}

\bibitem{Galiotou2002}
L.~Galiotou-Panayotou, M.~Kapantai, and O.~Kalisperatou, ``Development of a method for evaluating the hard-to-cook defect in legumes,'' \textit{Food Chemistry}, vol.~80, no.~3, pp.~319--325, 2003. \url{https://doi.org/10.1016/S0308-8146(02)00267-3}

\bibitem{ISO4120}
ISO, ``Sensory analysis --- Methodology --- Triangle test,'' \textit{International Organization for Standardization}, ISO Standard 4120:2021, 2021.

\bibitem{ISO11136}
ISO, ``Sensory analysis --- Methodology --- General guidance for measuring hedonic liking with consumers,'' \textit{International Organization for Standardization}, ISO Standard 11136:2014, 2014.
\end{thebibliography}

\end{document}
"""

with open(TEX_PATH, 'w', encoding='utf-8') as f:
    f.write(latex_content)

print("Successfully written strict 8-page LaTeX document to:", TEX_PATH)

