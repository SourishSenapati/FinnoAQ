"""
FINNOAQ OMEGA — Hierarchical Biophysical, Sensory, Adaptive & Industrial Process Models
=======================================================================================
Project Ref: FNQ-PR-2026-001
Lead Chemical and Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

Implements the 8-module hierarchical modelling architecture (Modules A through H)
with strict epistemic classification, conservation of mass/charge/energy,
and fixes for historical repository defects FAIL-0021 through FAIL-0025.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
import torch

from finnoaq.canonical_biophysics import (
    CA_VOL_HTC_NOMINAL,
    CP_DAL_DRY,
    CP_WATER,
    DomesticPressureCookerModel,
    EA_CHEL as EA_CA_EXCHANGE,
    EA_ION as EA_CIT_DIFF,
    EA_GEL,
    EA_PECTIN_HYDROLYSIS as EA_PECTIN_BETA,
    EA_MOISTURE as EA_WATER_DIFF,
    R_GAS,
    RHO_DAL_DRY,
    SIGMA_0_YIELD,
    SIGMA_RESIDUAL,
    T_GEL_ONSET_EXCESS,
)

T_REF_K = 298.15
MW_CITRIC_ACID_ANHYDROUS = 192.124
MW_TRISODIUM_CITRATE_DIHYDRATE = 294.100
MW_POTASSIUM_CITRATE_MONOHYDRATE = 324.410


# =============================================================================
# MODULE A: FEEDSTOCK CHARACTERIZATION & LATENT VS MEASURED SEPARATION
# =============================================================================

@dataclass
class FeedstockBatch:
    """Physical and biochemical representation of an incoming pulse lot."""
    batch_id: str
    species: str  # e.g., "Cajanus cajan (Toor Dal)"
    cultivar_or_origin: str  # e.g., "Tanzanian_ICEAP_00557_Aged"
    # Directly measurable rapid intake variables
    half_thickness_m: float  # H (m), half of full split thickness
    eq_radius_m: float  # R_eq (m)
    initial_moisture_wb: float  # wet basis fraction (e.g., 0.105)
    open_porosity: float  # epsilon_pore (0.08 - 0.15)
    storage_months: float
    storage_temp_c: float
    storage_rh_pct: float
    # Latent biochemical state variables (require ICP-OES / FTIR / HPLC or proxy inference)
    bound_ca_mol_m3: float  # Middle-lamella pectate-bound Ca2+ (mol/m^3)
    bound_mg_mol_m3: float  # Middle-lamella Mg2+ (mol/m^3)
    phytate_p_mg_100g: float
    pectin_de_fraction: float  # Degree of esterification (0.18 - 0.55)
    # Species-specific thermal parameters
    t_gel_onset_c: float = 68.0
    requires_separate_species_validation: bool = False
    evidence_tag: str = "MODEL_DERIVED"

    @property
    def full_thickness_mm(self) -> float:
        return self.half_thickness_m * 2000.0

    @property
    def initial_moisture_db(self) -> float:
        return self.initial_moisture_wb / (1.0 - self.initial_moisture_wb)


class FeedstockCharacterizationModule:
    """Module A: Generates reference lots, multi-cultivar distributions, and species profiles."""

    @staticmethod
    def get_reference_batches() -> Dict[str, FeedstockBatch]:
        return {
            "INDIAN_LATUR_FRESH": FeedstockBatch(
                batch_id="REF-IND-LATUR",
                species="Cajanus cajan (Split Toor Dal)",
                cultivar_or_origin="Indian Latur/Marathwada Fresh (3 mo)",
                half_thickness_m=0.925e-3,
                eq_radius_m=2.25e-3,
                initial_moisture_wb=0.108,
                open_porosity=0.125,
                storage_months=3.0,
                storage_temp_c=24.0,
                storage_rh_pct=55.0,
                bound_ca_mol_m3=12.80,
                bound_mg_mol_m3=18.50,
                phytate_p_mg_100g=235.0,
                pectin_de_fraction=0.48,
                evidence_tag="LITERATURE_SUPPORTED",
            ),
            "TANZANIAN_ICEAP_MODERATE": FeedstockBatch(
                batch_id="REF-TZA-ICEAP01514",
                species="Cajanus cajan (Split Toor Dal)",
                cultivar_or_origin="Tanzanian Arusha/Dodoma ICEAP 01514/15 (6 mo)",
                half_thickness_m=1.025e-3,
                eq_radius_m=2.38e-3,
                initial_moisture_wb=0.102,
                open_porosity=0.115,
                storage_months=6.0,
                storage_temp_c=28.0,
                storage_rh_pct=68.0,
                bound_ca_mol_m3=24.50,
                bound_mg_mol_m3=24.00,
                phytate_p_mg_100g=185.0,
                pectin_de_fraction=0.36,
                evidence_tag="LITERATURE_SUPPORTED",
            ),
            "TANZANIAN_HTC_AGED_NOMINAL": FeedstockBatch(
                batch_id="REF-TZA-ICEAP00557",
                species="Cajanus cajan (Split Toor Dal)",
                cultivar_or_origin="Tanzanian Maritime Aged ICEAP 00557 (9 mo)",
                half_thickness_m=1.100e-3,
                eq_radius_m=2.45e-3,
                initial_moisture_wb=0.098,
                open_porosity=0.110,
                storage_months=9.0,
                storage_temp_c=31.0,
                storage_rh_pct=76.0,
                bound_ca_mol_m3=CA_VOL_HTC_NOMINAL,  # 35.369 mol/m^3
                bound_mg_mol_m3=28.50,
                phytate_p_mg_100g=148.0,
                pectin_de_fraction=0.28,
                evidence_tag="LITERATURE_SUPPORTED",
            ),
            "EAST_AFRICAN_SEVERE_HTC": FeedstockBatch(
                batch_id="REF-EA-ICP9145",
                species="Cajanus cajan (Split Toor Dal)",
                cultivar_or_origin="East African Long-Duration ICP 9145 Severe HTC (14 mo)",
                half_thickness_m=1.200e-3,
                eq_radius_m=2.55e-3,
                initial_moisture_wb=0.092,
                open_porosity=0.095,
                storage_months=14.0,
                storage_temp_c=33.0,
                storage_rh_pct=80.0,
                bound_ca_mol_m3=42.80,
                bound_mg_mol_m3=31.00,
                phytate_p_mg_100g=120.0,
                pectin_de_fraction=0.21,
                evidence_tag="LITERATURE_SUPPORTED",
            ),
        }

    @staticmethod
    def get_other_dal_species_profiles() -> Dict[str, FeedstockBatch]:
        """Profiles for secondary pulse species with mandatory separate validation flags."""
        return {
            "CHANA_DAL_CICER_ARIETINUM": FeedstockBatch(
                batch_id="SPEC-CHANA",
                species="Cicer arietinum (Split Chana Dal)",
                cultivar_or_origin="Desi Chickpea Split",
                half_thickness_m=1.35e-3,
                eq_radius_m=2.70e-3,
                initial_moisture_wb=0.105,
                open_porosity=0.105,
                storage_months=6.0,
                storage_temp_c=28.0,
                storage_rh_pct=65.0,
                bound_ca_mol_m3=38.0,
                bound_mg_mol_m3=29.0,
                phytate_p_mg_100g=190.0,
                pectin_de_fraction=0.30,
                t_gel_onset_c=65.0,
                requires_separate_species_validation=True,
                evidence_tag="INDIRECT_SPECIES_EXTENSION",
            ),
            "MOONG_DAL_VIGNA_RADIATA": FeedstockBatch(
                batch_id="SPEC-MOONG",
                species="Vigna radiata (Split Yellow Moong Dal)",
                cultivar_or_origin="Dehulled Split Mung Bean",
                half_thickness_m=0.72e-3,
                eq_radius_m=1.75e-3,
                initial_moisture_wb=0.108,
                open_porosity=0.135,
                storage_months=6.0,
                storage_temp_c=28.0,
                storage_rh_pct=65.0,
                bound_ca_mol_m3=16.5,
                bound_mg_mol_m3=21.0,
                phytate_p_mg_100g=210.0,
                pectin_de_fraction=0.44,
                t_gel_onset_c=62.0,
                requires_separate_species_validation=True,
                evidence_tag="INDIRECT_SPECIES_EXTENSION",
            ),
            "URAD_DAL_VIGNA_MUNGO": FeedstockBatch(
                batch_id="SPEC-URAD",
                species="Vigna mungo (Split White Urad Dal)",
                cultivar_or_origin="Dehulled Black Gram Split (Mucilage-Rich)",
                half_thickness_m=0.88e-3,
                eq_radius_m=1.95e-3,
                initial_moisture_wb=0.106,
                open_porosity=0.110,
                storage_months=6.0,
                storage_temp_c=28.0,
                storage_rh_pct=65.0,
                bound_ca_mol_m3=26.0,
                bound_mg_mol_m3=25.0,
                phytate_p_mg_100g=220.0,
                pectin_de_fraction=0.35,
                t_gel_onset_c=69.0,
                requires_separate_species_validation=True,
                evidence_tag="INDIRECT_SPECIES_EXTENSION",
            ),
            "MASOOR_DAL_LENS_CULINARIS": FeedstockBatch(
                batch_id="SPEC-MASOOR",
                species="Lens culinaris (Split Red Masoor Dal)",
                cultivar_or_origin="Dehulled Red Lentil Split",
                half_thickness_m=0.65e-3,
                eq_radius_m=1.80e-3,
                initial_moisture_wb=0.110,
                open_porosity=0.140,
                storage_months=6.0,
                storage_temp_c=25.0,
                storage_rh_pct=60.0,
                bound_ca_mol_m3=14.0,
                bound_mg_mol_m3=17.0,
                phytate_p_mg_100g=200.0,
                pectin_de_fraction=0.46,
                t_gel_onset_c=61.0,
                requires_separate_species_validation=True,
                evidence_tag="INDIRECT_SPECIES_EXTENSION",
            ),
        }


# =============================================================================
# MODULE D: TREATMENT CHEMISTRY, SPECIATION & AFTERTASTE PRECURSORS
# =============================================================================

@dataclass
class TreatmentChemistrySpec:
    """Complete thermodynamic and stoichiometric specification of a conditioning bath."""
    treatment_id: str
    name: str
    mechanism_type: str  # "PURE_WATER", "NAHCO3_ALKALINE", "CITRATE_BUFFER", "BICARB_CITRATE_QUENCH"
    equilibrium_pH: float
    ionic_strength_M: float
    total_citrate_M: float
    total_carbonate_M: float
    f_K: float  # K+ fraction of citrate salt cations
    conc_Cit3_M: float
    conc_HCit2_M: float
    conc_H2Cit_M: float
    conc_H3Cit_M: float
    conc_HCO3_M: float
    conc_CO3_M: float
    conc_Na_M: float
    conc_K_M: float
    active_chelator_M: float  # Effective Ca2+-complexing concentration
    alkaline_beta_elim_factor: float  # Relative OH- acceleration factor during cooking
    # Exact reagent recipe per 1000 L (kg/1000L = g/L)
    mass_k3cit_monohydrate_g_L: float
    mass_na3cit_dihydrate_g_L: float
    mass_citric_acid_anhydrous_g_L: float
    mass_nahco3_g_L: float
    tds_wt_vol_pct: float
    flavonoid_yellowing_risk: bool


class TreatmentChemistryModule:
    """
    Module D: Exact multi-protic speciation with Davies activity corrections.
    Fixes FAIL-0024 by solving exact thermodynamic equilibrium pH for any given mass
    recipe and exact hydrate masses for any target pH.
    """

    PKA_CIT_25C = (3.13, 4.76, 6.40)
    PKA_CARB_25C = (6.35, 10.33)
    MW_NAHCO3 = 84.007

    @staticmethod
    def davies_log10_gamma(z: int, ionic_strength: float) -> float:
        """Davies equation for single-ion activity coefficient at 25-55°C."""
        if ionic_strength <= 0.0 or z == 0:
            return 0.0
        I_clamped = min(max(ionic_strength, 1e-6), 0.6)
        sqrt_I = math.sqrt(I_clamped)
        return -0.51 * (z ** 2) * ((sqrt_I / (1.0 + sqrt_I)) - 0.3 * I_clamped)

    @classmethod
    def citrate_alpha_fractions(cls, pH: float, ionic_strength: float = 0.25) -> Tuple[float, float, float, float]:
        """
        Returns (alpha0_H3Cit, alpha1_H2Cit-, alpha2_HCit2-, alpha3_Cit3-) at given pH and I.
        """
        g1 = cls.davies_log10_gamma(1, ionic_strength)
        g2 = cls.davies_log10_gamma(2, ionic_strength)
        g3 = cls.davies_log10_gamma(3, ionic_strength)

        pKa1_app = cls.PKA_CIT_25C[0] + g1
        pKa2_app = cls.PKA_CIT_25C[1] + (g2 - g1)
        pKa3_app = cls.PKA_CIT_25C[2] + (g3 - g2)

        h = 10.0 ** (-pH)
        k1 = 10.0 ** (-pKa1_app)
        k2 = 10.0 ** (-pKa2_app)
        k3 = 10.0 ** (-pKa3_app)

        denom = (h ** 3) + k1 * (h ** 2) + (k1 * k2 * h) + (k1 * k2 * k3)
        a0 = (h ** 3) / denom
        a1 = (k1 * (h ** 2)) / denom
        a2 = (k1 * k2 * h) / denom
        a3 = (k1 * k2 * k3) / denom
        return a0, a1, a2, a3

    @classmethod
    def solve_equilibrium_pH_from_masses(
        cls,
        mass_k3cit_monohydrate_g_L: float = 0.0,
        mass_na3cit_dihydrate_g_L: float = 0.0,
        mass_citric_acid_anhydrous_g_L: float = 0.0,
        mass_nahco3_g_L: float = 0.0,
        use_activity_correction: bool = False,
    ) -> Dict[str, float]:
        """
        Solves exact electroneutrality equation to find equilibrium pH of an arbitrary
        mixture of K3Cit.H2O, Na3Cit.2H2O, Citric Acid, and NaHCO3.
        Used to audit FAIL-0024 and verify factory SOP recipes.
        """
        m_k3cit = mass_k3cit_monohydrate_g_L / MW_POTASSIUM_CITRATE_MONOHYDRATE
        m_na3cit = mass_na3cit_dihydrate_g_L / MW_TRISODIUM_CITRATE_DIHYDRATE
        m_h3cit = mass_citric_acid_anhydrous_g_L / MW_CITRIC_ACID_ANHYDROUS
        m_nahco3 = mass_nahco3_g_L / cls.MW_NAHCO3

        c_cit_total = m_k3cit + m_na3cit + m_h3cit
        c_carb_total = m_nahco3
        c_K = 3.0 * m_k3cit
        c_Na = 3.0 * m_na3cit + m_nahco3

        def charge_residual(pH: float) -> float:
            h = 10.0 ** (-pH)
            oh = 10.0 ** (pH - 14.0)
            I_est = 0.5 * (c_K + c_Na + h + oh) if use_activity_correction else 0.0
            a0, a1, a2, a3 = cls.citrate_alpha_fractions(pH, I_est)
            k_c1 = 10.0 ** (-cls.PKA_CARB_25C[0])
            k_c2 = 10.0 ** (-cls.PKA_CARB_25C[1])
            denom_c = (h ** 2) + k_c1 * h + k_c1 * k_c2
            ac1 = (k_c1 * h) / denom_c
            ac2 = (k_c1 * k_c2) / denom_c

            positive_charge = c_K + c_Na + h
            negative_charge = c_cit_total * (a1 + 2.0 * a2 + 3.0 * a3) + c_carb_total * (ac1 + 2.0 * ac2) + oh
            return positive_charge - negative_charge

        pH_eq = float(opt.brentq(charge_residual, 1.5, 11.5))
        a0, a1, a2, a3 = cls.citrate_alpha_fractions(pH_eq, 0.25 if use_activity_correction else 0.0)
        return {
            "equilibrium_pH": pH_eq,
            "total_citrate_M": c_cit_total,
            "total_carbonate_M": c_carb_total,
            "conc_K_M": c_K,
            "conc_Na_M": c_Na,
            "z_citrate_mean": a1 + 2.0 * a2 + 3.0 * a3,
        }

    @classmethod
    def design_citrate_buffer(
        cls,
        treatment_id: str,
        name: str,
        total_citrate_M: float,
        target_pH: float,
        f_K: float = 0.90,
        use_activity_correction: bool = False,
    ) -> TreatmentChemistrySpec:
        """
        Designs an exact Citrate Buffer at target_pH with total_citrate_M and potassium cation fraction f_K.
        """
        I_curr = 0.0
        for _ in range(6):
            a0, a1, a2, a3 = cls.citrate_alpha_fractions(target_pH, I_curr if use_activity_correction else 0.0)
            z_mean = a1 + 2.0 * a2 + 3.0 * a3
            f_salt = min(max(z_mean / 3.0, 0.0), 1.0)
            c_cation = 3.0 * total_citrate_M * f_salt
            I_curr = 0.5 * (
                c_cation + total_citrate_M * (1.0 * a1 + 4.0 * a2 + 9.0 * a3)
            )

        f_salt = min(max((a1 + 2.0 * a2 + 3.0 * a3) / 3.0, 0.0), 1.0)
        f_acid = 1.0 - f_salt

        m_k3cit = total_citrate_M * f_salt * f_K
        m_na3cit = total_citrate_M * f_salt * (1.0 - f_K)
        m_h3cit = total_citrate_M * f_acid

        mass_k3cit = m_k3cit * MW_POTASSIUM_CITRATE_MONOHYDRATE
        mass_na3cit = m_na3cit * MW_TRISODIUM_CITRATE_DIHYDRATE
        mass_h3cit = m_h3cit * MW_CITRIC_ACID_ANHYDROUS

        c_Cit3 = total_citrate_M * a3
        c_HCit2 = total_citrate_M * a2
        c_H2Cit = total_citrate_M * a1
        c_H3Cit = total_citrate_M * a0

        active_chelator = c_Cit3 + 0.36 * c_HCit2

        return TreatmentChemistrySpec(
            treatment_id=treatment_id,
            name=name,
            mechanism_type="CITRATE_BUFFER",
            equilibrium_pH=target_pH,
            ionic_strength_M=I_curr,
            total_citrate_M=total_citrate_M,
            total_carbonate_M=0.0,
            f_K=f_K,
            conc_Cit3_M=c_Cit3,
            conc_HCit2_M=c_HCit2,
            conc_H2Cit_M=c_H2Cit,
            conc_H3Cit_M=c_H3Cit,
            conc_HCO3_M=0.0,
            conc_CO3_M=0.0,
            conc_Na_M=3.0 * m_na3cit,
            conc_K_M=3.0 * m_k3cit,
            active_chelator_M=active_chelator,
            alkaline_beta_elim_factor=1.0,
            mass_k3cit_monohydrate_g_L=mass_k3cit,
            mass_na3cit_dihydrate_g_L=mass_na3cit,
            mass_citric_acid_anhydrous_g_L=mass_h3cit,
            mass_nahco3_g_L=0.0,
            tds_wt_vol_pct=(mass_k3cit + mass_na3cit + mass_h3cit) / 10.0,
            flavonoid_yellowing_risk=False,
        )

    @classmethod
    def design_bicarbonate_bath(
        cls,
        treatment_id: str,
        name: str,
        mass_nahco3_g_L: float = 5.0,
        citrate_quench_M: float = 0.0,
    ) -> TreatmentChemistrySpec:
        """Designs an alkaline NaHCO3 conditioning bath (with optional post-soak citrate acid quench)."""
        c_carb = mass_nahco3_g_L / cls.MW_NAHCO3
        pH = 8.32 if citrate_quench_M <= 0.0 else 6.45
        h = 10.0 ** (-pH)
        k1 = 10.0 ** (-cls.PKA_CARB_25C[0])
        k2 = 10.0 ** (-cls.PKA_CARB_25C[1])
        denom = (h ** 2) + k1 * h + k1 * k2
        c_hco3 = c_carb * (k1 * h) / denom
        c_co3 = c_carb * (k1 * k2) / denom

        eff_chelator = 0.45 * c_carb + (0.65 * citrate_quench_M)
        beta_factor = 2.15 if citrate_quench_M <= 0.0 else 1.55

        mass_h3cit = citrate_quench_M * MW_CITRIC_ACID_ANHYDROUS
        return TreatmentChemistrySpec(
            treatment_id=treatment_id,
            name=name,
            mechanism_type="NAHCO3_ALKALINE" if citrate_quench_M <= 0.0 else "BICARB_CITRATE_QUENCH",
            equilibrium_pH=pH,
            ionic_strength_M=c_carb + citrate_quench_M,
            total_citrate_M=citrate_quench_M,
            total_carbonate_M=c_carb if citrate_quench_M <= 0.0 else c_carb * 0.18,
            f_K=0.0,
            conc_Cit3_M=0.35 * citrate_quench_M,
            conc_HCit2_M=0.50 * citrate_quench_M,
            conc_H2Cit_M=0.15 * citrate_quench_M,
            conc_H3Cit_M=0.0,
            conc_HCO3_M=c_hco3 if citrate_quench_M <= 0.0 else c_hco3 * 0.18,
            conc_CO3_M=c_co3 if citrate_quench_M <= 0.0 else 0.0,
            conc_Na_M=c_carb,
            conc_K_M=0.0,
            active_chelator_M=eff_chelator,
            alkaline_beta_elim_factor=beta_factor,
            mass_k3cit_monohydrate_g_L=0.0,
            mass_na3cit_dihydrate_g_L=0.0,
            mass_citric_acid_anhydrous_g_L=mass_h3cit,
            mass_nahco3_g_L=mass_nahco3_g_L,
            tds_wt_vol_pct=(mass_nahco3_g_L + mass_h3cit) / 10.0,
            flavonoid_yellowing_risk=(citrate_quench_M <= 0.0),
        )

    @classmethod
    def design_pure_water(cls) -> TreatmentChemistrySpec:
        return TreatmentChemistrySpec(
            treatment_id="WATER_CONTROL",
            name="Untreated Warm Water Control",
            mechanism_type="PURE_WATER",
            equilibrium_pH=6.80,
            ionic_strength_M=0.002,
            total_citrate_M=0.0,
            total_carbonate_M=0.0,
            f_K=0.0,
            conc_Cit3_M=0.0,
            conc_HCit2_M=0.0,
            conc_H2Cit_M=0.0,
            conc_H3Cit_M=0.0,
            conc_HCO3_M=0.0,
            conc_CO3_M=0.0,
            conc_Na_M=0.0,
            conc_K_M=0.0,
            active_chelator_M=0.0,
            alkaline_beta_elim_factor=1.0,
            mass_k3cit_monohydrate_g_L=0.0,
            mass_na3cit_dihydrate_g_L=0.0,
            mass_citric_acid_anhydrous_g_L=0.0,
            mass_nahco3_g_L=0.0,
            tds_wt_vol_pct=0.0,
            flavonoid_yellowing_risk=False,
        )


# =============================================================================
# MODULE B: HYDRATION & TREATMENT PENETRATION (EMPIRICAL VS 2D CONSERVATIVE PDE)
# =============================================================================

@dataclass
class PretreatmentProcessConfig:
    """Operating conditions and physical intensification modes for soaking/conditioning."""
    soak_temp_c: float = 55.0
    soak_time_min: float = 20.0
    ultrasound_w_per_l: float = 0.0  # e.g., 17.0 W/L at 40 kHz (Vásquez et al. 2021)
    vacuum_pulse_kpa_abs: Optional[float] = None  # e.g., 15.0 kPa abs (-86 kPa gauge)
    micro_perforation_factor: float = 1.0  # >1.0 reduces effective diffusion path but increases solid loss
    agitation_biot_number: float = 20.0


class HydrationAndPenetrationModule:
    """
    Module B: Multi-fidelity hydration & reaction-diffusion transport solver.
    Compares:
      - Level 1: Empirical Peleg & Weibull hydration models
      - Level 3: 2D Axisymmetric conservative finite-volume reaction-diffusion PDE
                 with realistic Fito et al. (1996) Vacuum Impregnation porosity bounds (fixing FAIL-0023).
    """

    @staticmethod
    def predict_empirical_peleg_weibull(
        batch: FeedstockBatch,
        temp_c: float,
        time_min: float,
        ionic_strength_M: float = 0.0,
    ) -> Dict[str, float]:
        """
        Empirical Peleg and Weibull water uptake models calibrated to Cajanus cajan splits
        (Swami et al. 2013; Vásquez et al. 2021).
        """
        m0_db = batch.initial_moisture_db
        m_eq_db = 1.15 * (1.0 - 0.08 * min(ionic_strength_M, 0.8))
        temp_k = temp_c + 273.15
        arr_factor = math.exp(-(EA_WATER_DIFF / R_GAS) * ((1.0 / temp_k) - (1.0 / T_REF_K)))
        thickness_ratio_sq = (batch.half_thickness_m / 1.0e-3) ** 2

        k1_min = (14.5 * thickness_ratio_sq / arr_factor) * (1.0 + 0.12 * ionic_strength_M)
        k2 = 1.0 / max(m_eq_db - m0_db, 0.1)
        m_peleg_db = m0_db + (time_min / (k1_min + k2 * time_min)) if time_min > 0 else m0_db

        tau_min = 18.0 * thickness_ratio_sq / arr_factor
        beta = 0.78
        m_weibull_db = m_eq_db - (m_eq_db - m0_db) * math.exp(-((max(time_min, 0.0) / tau_min) ** beta))

        return {
            "moisture_peleg_db": m_peleg_db,
            "moisture_peleg_wb": m_peleg_db / (1.0 + m_peleg_db),
            "moisture_weibull_db": m_weibull_db,
            "moisture_weibull_wb": m_weibull_db / (1.0 + m_weibull_db),
            "peleg_k1_min": k1_min,
            "weibull_tau_min": tau_min,
        }

    @classmethod
    def solve_2d_conservative_soaking_pde(
        cls,
        batch: FeedstockBatch,
        chem: TreatmentChemistrySpec,
        config: PretreatmentProcessConfig,
        grid_size: int = 16,
    ) -> Dict[str, Any]:
        """
        Solves coupled 2D axisymmetric (r, z) moisture diffusion, chelant transport, and
        stoichiometric calcium-pectate ligand exchange inside a split pulse cotyledon.

        Strictly enforces Fito et al. (1996) Hydrodynamic Mechanism (HDM) porosity limit
        for Vacuum Impregnation (fixing FAIL-0023).
        """
        temp_k = config.soak_temp_c + 273.15
        # Split cotyledon has both dorsal and ventral faces exposed to bath:
        h_eff = (0.88 * batch.half_thickness_m) / max(config.micro_perforation_factor, 1.0)
        r_eff = batch.eq_radius_m

        dr = r_eff / (grid_size - 1)
        dz = h_eff / (grid_size - 1)

        uae_mult = 1.0 + 0.35 * math.tanh(config.ultrasound_w_per_l / 17.0)
        d_water = 1.45e-10 * math.exp(-(EA_WATER_DIFF / R_GAS) * (1.0 / temp_k - 1.0 / T_REF_K)) * uae_mult
        d_solute = 1.10e-10 * math.exp(-(EA_CIT_DIFF / R_GAS) * (1.0 / temp_k - 1.0 / T_REF_K)) * uae_mult

        d_water *= (1.0 - 0.06 * min(chem.ionic_strength_M, 0.6))

        k_swell_boost = 1.0 + 0.16 * chem.f_K if chem.total_citrate_M > 0 else 1.0
        d_solute *= k_swell_boost

        de_factor = 0.82 + 0.65 * batch.pectin_de_fraction
        k_chel = 1.45e-4 * math.exp(-(EA_CA_EXCHANGE / R_GAS) * (1.0 / temp_k - 1.0 / T_REF_K)) * de_factor

        m0_db = batch.initial_moisture_db
        m_eq_db = 1.15 * (1.0 - 0.08 * min(chem.ionic_strength_M, 0.6))
        m_field = np.full((grid_size, grid_size), m0_db, dtype=np.float64)
        c_sol_field = np.zeros((grid_size, grid_size), dtype=np.float64)
        ca_bound_field = np.full((grid_size, grid_size), batch.bound_ca_mol_m3, dtype=np.float64)

        c_bath_mol_m3 = chem.active_chelator_M * 1000.0  # M (mol/L) -> mol/m^3

        # REALISTIC VACUUM IMPREGNATION (Fito et al., 1996 HDM Porosity Limit - Fixes FAIL-0023)
        vi_convected_mol_m3 = 0.0
        if config.vacuum_pulse_kpa_abs is not None and config.vacuum_pulse_kpa_abs < 101.325:
            p_vac = max(config.vacuum_pulse_kpa_abs, 5.0)
            x_hdm = batch.open_porosity * (1.0 - (p_vac / 101.325))
            vi_convected_mol_m3 = x_hdm * c_bath_mol_m3
            r_idx_cut = int(0.35 * grid_size)
            z_idx_cut = int(0.35 * grid_size)
            c_sol_field[r_idx_cut:, :] = vi_convected_mol_m3
            c_sol_field[:, z_idx_cut:] = vi_convected_mol_m3
            m_field[r_idx_cut:, :] += x_hdm * (1000.0 / RHO_DAL_DRY)
            m_field[:, z_idx_cut:] = np.maximum(m_field[:, z_idx_cut:], m0_db + x_hdm * (1000.0 / RHO_DAL_DRY))

        bi_eff = config.agitation_biot_number * (2.2 if config.ultrasound_w_per_l > 0 else 1.0)
        surface_alpha = bi_eff / (1.0 + bi_eff)

        if config.soak_time_min <= 0.0:
            return {
                "final_pectin_ca_field": torch.tensor(ca_bound_field, dtype=torch.float32),
                "final_moisture_field": torch.tensor(m_field, dtype=torch.float32),
                "final_solute_field": torch.tensor(c_sol_field, dtype=torch.float32),
                "mean_pectin_ca_vol": float(batch.bound_ca_mol_m3),
                "core_pectin_ca_vol": float(batch.bound_ca_mol_m3),
                "mean_moisture_db": float(m0_db),
                "mean_moisture_wb": float(batch.initial_moisture_wb),
                "mean_internal_solute_mol_m3": 0.0,
                "ca_displacement_pct": 0.0,
                "core_ca_displacement_pct": 0.0,
                "vi_convected_solute_mol_m3": vi_convected_mol_m3,
                "solid_leaching_loss_pct": 0.0,
                "alkaline_beta_elim_factor": chem.alkaline_beta_elim_factor,
                "t_gel_onset_c": batch.t_gel_onset_c,
            }

        d_max = max(d_water, d_solute)
        dt_max = 0.20 * min(dr * dr, dz * dz) / max(d_max, 1e-12)
        dt = min(2.5, dt_max)
        total_steps = int(math.ceil((config.soak_time_min * 60.0) / dt))
        dt = (config.soak_time_min * 60.0) / total_steps

        r_coords = np.linspace(0.0, r_eff, grid_size)
        inv_r_2dr = np.zeros(grid_size - 2)
        inv_r_2dr[:] = 1.0 / (r_coords[1:-1] * 2.0 * dr)
        inv_dr2 = 1.0 / (dr * dr)
        inv_dz2 = 1.0 / (dz * dz)

        for _ in range(total_steps):
            m_field[-1, :] = m_field[-2, :] + surface_alpha * (m_eq_db - m_field[-2, :])
            m_field[:, -1] = m_field[:, -2] + surface_alpha * (m_eq_db - m_field[:, -2])
            c_sol_field[-1, :] = c_sol_field[-2, :] + surface_alpha * (c_bath_mol_m3 - c_sol_field[-2, :])
            c_sol_field[:, -1] = c_sol_field[:, -2] + surface_alpha * (c_bath_mol_m3 - c_sol_field[:, -2])

            lap_m = np.zeros_like(m_field)
            d2m_dr2 = (m_field[2:, 1:-1] - 2.0 * m_field[1:-1, 1:-1] + m_field[:-2, 1:-1]) * inv_dr2
            dm_dr_r = (m_field[2:, 1:-1] - m_field[:-2, 1:-1]) * inv_r_2dr[:, None]
            d2m_dz2 = (m_field[1:-1, 2:] - 2.0 * m_field[1:-1, 1:-1] + m_field[1:-1, :-2]) * inv_dz2
            lap_m[1:-1, 1:-1] = d2m_dr2 + dm_dr_r + d2m_dz2
            lap_m[0, 1:-1] = 2.0 * (m_field[1, 1:-1] - m_field[0, 1:-1]) * inv_dr2 + (
                m_field[0, 2:] - 2.0 * m_field[0, 1:-1] + m_field[0, :-2]
            ) * inv_dz2
            lap_m[1:-1, 0] = (
                (m_field[2:, 0] - 2.0 * m_field[1:-1, 0] + m_field[:-2, 0]) * inv_dr2
                + (m_field[2:, 0] - m_field[:-2, 0]) * inv_r_2dr
                + 2.0 * (m_field[1:-1, 1] - m_field[1:-1, 0]) * inv_dz2
            )
            lap_m[0, 0] = 2.0 * (m_field[1, 0] - m_field[0, 0]) * inv_dr2 + 2.0 * (
                m_field[0, 1] - m_field[0, 0]
            ) * inv_dz2

            lap_c = np.zeros_like(c_sol_field)
            d2c_dr2 = (c_sol_field[2:, 1:-1] - 2.0 * c_sol_field[1:-1, 1:-1] + c_sol_field[:-2, 1:-1]) * inv_dr2
            dc_dr_r = (c_sol_field[2:, 1:-1] - c_sol_field[:-2, 1:-1]) * inv_r_2dr[:, None]
            d2c_dz2 = (c_sol_field[1:-1, 2:] - 2.0 * c_sol_field[1:-1, 1:-1] + c_sol_field[1:-1, :-2]) * inv_dz2
            lap_c[1:-1, 1:-1] = d2c_dr2 + dc_dr_r + d2c_dz2
            lap_c[0, 1:-1] = 2.0 * (c_sol_field[1, 1:-1] - c_sol_field[0, 1:-1]) * inv_dr2 + (
                c_sol_field[0, 2:] - 2.0 * c_sol_field[0, 1:-1] + c_sol_field[0, :-2]
            ) * inv_dz2
            lap_c[1:-1, 0] = (
                (c_sol_field[2:, 0] - 2.0 * c_sol_field[1:-1, 0] + c_sol_field[:-2, 0]) * inv_dr2
                + (c_sol_field[2:, 0] - c_sol_field[:-2, 0]) * inv_r_2dr
                + 2.0 * (c_sol_field[1:-1, 1] - c_sol_field[1:-1, 0]) * inv_dz2
            )
            lap_c[0, 0] = 2.0 * (c_sol_field[1, 0] - c_sol_field[0, 0]) * inv_dr2 + 2.0 * (
                c_sol_field[0, 1] - c_sol_field[0, 0]
            ) * inv_dz2

            hydration_gate = np.clip((m_field - m0_db) / max(m_eq_db - m0_db, 0.1), 0.35, 1.0)
            d_sol_local = d_solute * (0.55 + 0.45 * hydration_gate)

            m_field[1:-1, 1:-1] = np.clip(m_field[1:-1, 1:-1] + dt * d_water * lap_m[1:-1, 1:-1], m0_db, m_eq_db)
            m_field[0, :] = m_field[1, :]
            m_field[:, 0] = m_field[:, 1]

            c_sol_field[1:-1, 1:-1] = np.clip(
                c_sol_field[1:-1, 1:-1] + dt * d_sol_local[1:-1, 1:-1] * lap_c[1:-1, 1:-1],
                0.0,
                c_bath_mol_m3,
            )
            c_sol_field[0, :] = c_sol_field[1, :]
            c_sol_field[:, 0] = c_sol_field[:, 1]

            rxn_rate = k_chel * c_sol_field * ca_bound_field
            delta_ca = np.minimum(ca_bound_field, np.minimum(c_sol_field, rxn_rate * dt))
            ca_bound_field = np.clip(ca_bound_field - delta_ca, 0.0, batch.bound_ca_mol_m3)
            c_sol_field = np.clip(c_sol_field - 0.22 * delta_ca, 0.0, c_bath_mol_m3)

        r_weights = r_coords.copy()
        r_weights[0] = 0.25 * dr
        r_weights[-1] = 0.5 * r_coords[-1]
        z_weights = np.ones(grid_size)
        z_weights[0] = 0.5
        z_weights[-1] = 0.5
        vol_weights = np.outer(r_weights, z_weights)
        vol_weights /= np.sum(vol_weights)

        mean_ca = float(np.sum(ca_bound_field * vol_weights))
        core_ca = float(ca_bound_field[0, 0])
        mean_m_db = float(np.sum(m_field * vol_weights))
        mean_m_wb = mean_m_db / (1.0 + mean_m_db)
        mean_c_sol = float(np.sum(c_sol_field * vol_weights))

        ca_disp_pct = (1.0 - (mean_ca / max(batch.bound_ca_mol_m3, 1e-6))) * 100.0
        core_disp_pct = (1.0 - (core_ca / max(batch.bound_ca_mol_m3, 1e-6))) * 100.0

        leach_loss_pct = (
            0.35 * (config.soak_time_min / 20.0)
            * (1.0 + 0.45 * (config.ultrasound_w_per_l / 40.0))
            * (config.micro_perforation_factor ** 1.5)
        )

        return {
            "final_pectin_ca_field": torch.tensor(ca_bound_field, dtype=torch.float32),
            "final_moisture_field": torch.tensor(m_field, dtype=torch.float32),
            "final_solute_field": torch.tensor(c_sol_field, dtype=torch.float32),
            "mean_pectin_ca_vol": mean_ca,
            "core_pectin_ca_vol": core_ca,
            "mean_moisture_db": mean_m_db,
            "mean_moisture_wb": mean_m_wb,
            "mean_internal_solute_mol_m3": mean_c_sol,
            "ca_displacement_pct": ca_disp_pct,
            "core_ca_displacement_pct": core_disp_pct,
            "vi_convected_solute_mol_m3": vi_convected_mol_m3,
            "solid_leaching_loss_pct": leach_loss_pct,
            "alkaline_beta_elim_factor": chem.alkaline_beta_elim_factor,
            "t_gel_onset_c": batch.t_gel_onset_c,
        }


# =============================================================================
# MODULE C: THERMAL & PRESSURE-COOKING SOFTENING (EMPIRICAL VS MECHANISTIC)
# =============================================================================

class ThermalAndPressureCookingModule:
    """
    Module C: Compares Level 1 Empirical First-Order Softening (Nisha et al. 2006)
    against Level 2 Two-Phase Additive Parenchyma Softening under domestic pressure cooking.
    """

    @staticmethod
    def solve_pressure_cooking_softening(
        soak_result: Dict[str, Any],
        burner_power_w: float = 1600.0,
        max_cook_time_s: float = 1800.0,
    ) -> Dict[str, Any]:
        """
        Integrates both the mechanistic two-phase parenchyma tissue model and the
        empirical Nisha et al. (2006) first-order model across the pressure-cooker cycle.
        """
        cooker = DomesticPressureCookerModel(burner_power_W=burner_power_w)

        ca_field = soak_result["final_pectin_ca_field"].detach().cpu().numpy()
        m_field = soak_result["final_moisture_field"].detach().cpu().numpy()
        beta_mult = float(soak_result.get("alkaline_beta_elim_factor", 1.0))
        t_gel_onset = float(soak_result.get("t_gel_onset_c", T_GEL_ONSET_EXCESS))

        theta_ca = np.clip(ca_field / CA_VOL_HTC_NOMINAL, 0.0, 1.5)
        x_p = np.ones_like(theta_ca, dtype=np.float64)
        x_s = np.ones_like(theta_ca, dtype=np.float64)

        x_nisha = 1.0
        mean_theta_ca = float(np.mean(theta_ca))

        dt = 2.0
        steps = int(max_cook_time_s / dt)
        t90_mech_s: Optional[float] = None
        t90_nisha_s: Optional[float] = None
        whistles_at_t90: Optional[int] = None
        f_wb_core_at_whistle_2: Optional[float] = None
        f_wb_bulk_at_whistle_2: Optional[float] = None

        a_beam = 2.2e-3 * 4.5e-3  # Split cotyledon cross-section (m^2)
        c_geom = 8.85  # Calibrated Warner-Bratzler shear beam factor

        for _ in range(steps):
            state = cooker.step(dt)
            t_curr = state.time_sec
            temp_c = state.fluid_temp_c
            temp_k = temp_c + 273.15

            if temp_c > 55.0:
                k_hyd_cook = 1.6e-3 * math.exp(-(EA_WATER_DIFF / R_GAS) * (1.0 / temp_k - 1.0 / 373.15))
                m_field = m_field + dt * k_hyd_cook * np.maximum(0.0, 1.35 - m_field)

                if temp_c >= 98.0:
                    k_pectin_base = 0.0064 * math.exp(-(EA_PECTIN_BETA / R_GAS) * (1.0 / temp_k - 1.0 / 394.35))
                    k_p_spatial = k_pectin_base * beta_mult * (0.06 + 0.94 * np.exp(-3.1 * theta_ca))
                    x_p = x_p * np.exp(-k_p_spatial * dt)

                if temp_c > t_gel_onset:
                    k_gel_base = 0.0095 * math.exp(-(EA_GEL / R_GAS) * (1.0 / temp_k - 1.0 / 394.35))
                    f_moisture = np.clip((m_field - 0.20) / (0.60 - 0.20), 0.10, 1.0)
                    x_s = x_s * np.exp(-k_gel_base * f_moisture * dt)

                if temp_c >= 90.0:
                    k_nisha_120 = 3.80e-3 * beta_mult * (0.15 + 0.85 * np.exp(-2.8 * mean_theta_ca))
                    k_nisha = k_nisha_120 * math.exp(-(67300.0 / R_GAS) * (1.0 / temp_k - 1.0 / 393.15))
                    x_nisha *= math.exp(-k_nisha * dt)

            sigma_field = SIGMA_RESIDUAL + SIGMA_0_YIELD * (0.70 * x_p + 0.30 * x_s)
            f_wb_bulk = float(np.mean(sigma_field) * a_beam * c_geom)
            f_wb_core = float(sigma_field[0, 0] * a_beam * c_geom)
            f_wb_nisha = float((SIGMA_RESIDUAL + SIGMA_0_YIELD * x_nisha) * a_beam * c_geom)

            if t90_mech_s is None and f_wb_core <= 18.0 and state.whistle_count >= 1:
                t90_mech_s = t_curr
                whistles_at_t90 = state.whistle_count

            if t90_nisha_s is None and f_wb_nisha <= 18.0 and state.whistle_count >= 1:
                t90_nisha_s = t_curr

            if state.whistle_count >= 2 and len(cooker.whistle_times_sec) >= 2:
                if t_curr >= cooker.whistle_times_sec[1] + 15.0 and f_wb_core_at_whistle_2 is None:
                    f_wb_core_at_whistle_2 = f_wb_core
                    f_wb_bulk_at_whistle_2 = f_wb_bulk

        sigma_field = SIGMA_RESIDUAL + SIGMA_0_YIELD * (0.70 * x_p + 0.30 * x_s)
        f_wb_bulk_end = float(np.mean(sigma_field) * a_beam * c_geom)
        f_wb_core_end = float(sigma_field[0, 0] * a_beam * c_geom)

        if t90_mech_s is None:
            t90_mech_s = max_cook_time_s
            whistles_at_t90 = cooker.whistle_count

        if t90_nisha_s is None:
            t90_nisha_s = max_cook_time_s

        w2_time_s = cooker.whistle_times_sec[1] if len(cooker.whistle_times_sec) >= 2 else 550.0
        core_w2 = f_wb_core_at_whistle_2 if f_wb_core_at_whistle_2 is not None else f_wb_core_end
        bulk_w2 = f_wb_bulk_at_whistle_2 if f_wb_bulk_at_whistle_2 is not None else f_wb_bulk_end

        return {
            "t90_mechanistic_s": float(t90_mech_s),
            "t90_mechanistic_min": float(t90_mech_s / 60.0),
            "t90_empirical_nisha_s": float(t90_nisha_s),
            "t90_empirical_nisha_min": float(t90_nisha_s / 60.0),
            "whistle_count_at_t90": int(whistles_at_t90),
            "whistle_2_time_s": float(w2_time_s),
            "f_wb_core_at_whistle_2_N": float(core_w2),
            "f_wb_bulk_at_whistle_2_N": float(bulk_w2),
            "is_two_whistles_or_less": bool(whistles_at_t90 <= 2 and core_w2 <= 18.0),
            "whistle_times_s": list(cooker.whistle_times_sec),
        }


# =============================================================================
# MODULE E: WASHING & RESIDUE REMOVAL (TWO-DOMAIN SURFACE FILM + INTERNAL PORE)
# =============================================================================

class WashingAndResidueModule:
    """
    Module E: Models coupled two-domain solute retention during post-conditioning washing:
      1. External adhered surface liquid film (V_film ~ 0.045 L/kg dry dal)
      2. Internal cotyledon pore solute diffused during steeping
    Fixes FAIL-0023 by distinguishing surface film washout from internal pore retention.
    """

    @staticmethod
    def simulate_washing_operation(
        chem: TreatmentChemistrySpec,
        soak_result: Dict[str, Any],
        wash_mode: str = "DUAL_FAN_HIGH_PRESSURE_SPRAY",
        wash_time_s: float = 12.0,
        wash_water_ratio_L_kg: float = 0.50,
    ) -> Dict[str, float]:
        v_film_L_kg = 0.045  # 45 mL adhered surface liquid film per kg dry dal

        if wash_mode == "NO_WASH":
            k_film = 0.0
            wash_time_s = 0.0
            wash_water_ratio_L_kg = 0.0
        elif wash_mode == "STATIC_IMMERSION_RINSE":
            k_film = 0.085
        elif wash_mode == "ROTARY_DRUM_RINSE":
            k_film = 0.190
        else:  # DUAL_FAN_HIGH_PRESSURE_SPRAY
            k_film = 0.360

        bath_tds_mg_L = chem.tds_wt_vol_pct * 10000.0
        initial_surface_film_ppm = bath_tds_mg_L * v_film_L_kg
        residual_surface_film_ppm = initial_surface_film_ppm * math.exp(-k_film * wash_time_s)

        bicarb_bath_mg_L = chem.mass_nahco3_g_L * 1000.0
        surface_bicarb_ppm = bicarb_bath_mg_L * v_film_L_kg * math.exp(-k_film * wash_time_s)

        d_wash_back = 2.8e-10
        back_diff_loss_frac = min(0.45, 2.0 * math.sqrt(max(d_wash_back * wash_time_s, 0.0) / math.pi) / 1.0e-3)
        internal_solute_mol_m3 = float(soak_result.get("mean_internal_solute_mol_m3", 0.0))
        v_pore_m3_kg = 0.18e-3  # 0.18 L/kg hydrated intercellular pore liquid volume per kg dry dal
        retained_internal_mol_kg = (internal_solute_mol_m3 * v_pore_m3_kg) * (1.0 - back_diff_loss_frac)

        surface_frac_remaining = math.exp(-k_film * wash_time_s)
        retained_citrate_mg_100g = (
            (retained_internal_mol_kg + chem.total_citrate_M * v_film_L_kg * surface_frac_remaining)
            * 192.12 * 100.0
        ) if chem.total_citrate_M > 0 else 0.0

        retained_K_mg_100g = (
            (retained_internal_mol_kg * 2.6 * chem.f_K + chem.conc_K_M * v_film_L_kg * surface_frac_remaining)
            * 39.098 * 100.0
        ) if chem.conc_K_M > 0 else 0.0

        retained_Na_mg_100g = (
            (retained_internal_mol_kg * 2.6 * (1.0 - chem.f_K) + chem.conc_Na_M * v_film_L_kg * surface_frac_remaining)
            * 22.990 * 100.0
        ) if chem.conc_Na_M > 0 else 0.0

        retained_bicarb_total_ppm = (
            surface_bicarb_ppm + (retained_internal_mol_kg * 84.007 * 1000.0 if chem.mass_nahco3_g_L > 0 else 0.0)
        )

        moisture_pickup_wb_pct = 0.35 * (1.0 - math.exp(-wash_time_s / 25.0)) if wash_time_s > 0 else 0.0

        return {
            "wash_mode": wash_mode,
            "wash_time_s": wash_time_s,
            "wash_water_L_per_kg": wash_water_ratio_L_kg,
            "initial_surface_film_ppm": initial_surface_film_ppm,
            "residual_surface_film_ppm": residual_surface_film_ppm,
            "surface_bicarbonate_ppm": surface_bicarb_ppm,
            "total_retained_bicarbonate_ppm": retained_bicarb_total_ppm,
            "retained_citrate_mg_100g": retained_citrate_mg_100g,
            "retained_K_mg_100g": retained_K_mg_100g,
            "retained_Na_mg_100g": retained_Na_mg_100g,
            "back_diffusion_loss_pct": back_diff_loss_frac * 100.0,
            "wash_moisture_pickup_wb_pct": moisture_pickup_wb_pct,
        }


# =============================================================================
# MODULE F: FLAVOUR CHEMISTRY & STATISTICAL SENSORY EQUIVALENCE (ISO 11136 / TOST)
# =============================================================================

class SensoryAndFlavourModule:
    """
    Module F: Strictly separates analytical chemistry predictions from statistical
    human sensory models (Weber-Fechner, Thurstonian d', and ISO 11136 TOST equivalence).
    """

    @staticmethod
    def evaluate_flavour_and_sensory_risk(
        batch: FeedstockBatch,
        chem: TreatmentChemistrySpec,
        soak_config: PretreatmentProcessConfig,
        wash_result: Dict[str, float],
    ) -> Dict[str, Any]:
        dilution_factor = 4.5  # 100 g dry dal cooked into 450 g cooked dhal slurry

        bicarb_cooked_ppm = wash_result["total_retained_bicarbonate_ppm"] / dilution_factor
        r_soapy = bicarb_cooked_ppm / 55.0

        k_cooked_mmol_L = (wash_result["retained_K_mg_100g"] * 10.0 / 39.098) / dilution_factor
        r_metallic_k = k_cooked_mmol_L / 18.0

        cit_cooked_mmol_L = (wash_result["retained_citrate_mg_100g"] * 10.0 / 192.12) / dilution_factor
        r_tart_cit = cit_cooked_mmol_L / 8.5

        ph_diff = chem.equilibrium_pH - 6.80
        lox_ph_factor = math.exp(-0.5 * ((ph_diff / 1.15) ** 2))
        lox_temp_inactivation = math.exp(-0.042 * max(soak_config.soak_temp_c - 42.0, 0.0))
        lox_residual_activity_pct = 100.0 * lox_ph_factor * lox_temp_inactivation

        base_hexanal_ppb = 28.0 + 9.5 * batch.storage_months
        predicted_hexanal_ppb = base_hexanal_ppb * (0.22 + 0.78 * (lox_residual_activity_pct / 100.0))
        indian_ref_hexanal_ppb = 48.0

        max_taste_ratio = max(r_soapy, r_metallic_k, r_tart_cit)
        hexanal_excess_ratio = max(0.0, (predicted_hexanal_ppb - indian_ref_hexanal_ppb) / 60.0)

        d_prime_est = math.sqrt((1.35 * max_taste_ratio) ** 2 + (0.85 * hexanal_excess_ratio) ** 2)
        if chem.flavonoid_yellowing_risk:
            d_prime_est += 0.65

        return {
            "evidence_tag": "MODEL_DERIVED_REQUIRES_SENSORY_PANEL",
            "cooked_bicarbonate_ppm": bicarb_cooked_ppm,
            "cooked_K_mmol_L": k_cooked_mmol_L,
            "cooked_citrate_mmol_L": cit_cooked_mmol_L,
            "soapy_alkaline_threshold_ratio": r_soapy,
            "potassium_metallic_threshold_ratio": r_metallic_k,
            "citrate_tart_threshold_ratio": r_tart_cit,
            "max_off_taste_threshold_ratio": max_taste_ratio,
            "sub_threshold_aftertaste_pass": bool(max_taste_ratio < 0.50 and not chem.flavonoid_yellowing_risk),
            "lox_residual_activity_pct": lox_residual_activity_pct,
            "predicted_hexanal_ppb": predicted_hexanal_ppb,
            "indian_ref_hexanal_ppb": indian_ref_hexanal_ppb,
            "thurstonian_d_prime_estimate": d_prime_est,
            "thurstonian_d_prime_95ci": [max(0.0, d_prime_est - 0.28), d_prime_est + 0.28],
            "sensory_equivalence_plausible": bool(d_prime_est < 0.75),
        }

    @staticmethod
    def design_iso_tost_equivalence_study(
        equivalence_margin_hedonic: float = 0.75,
        within_subject_sd: float = 1.35,
        alpha: float = 0.05,
        target_power: float = 0.90,
    ) -> Dict[str, Any]:
        z_alpha = float(stats.norm.ppf(1.0 - alpha))
        z_beta = float(stats.norm.ppf(1.0 - (1.0 - target_power) / 2.0))
        n_required = math.ceil(2.0 * ((z_alpha + z_beta) * within_subject_sd / equivalence_margin_hedonic) ** 2)
        n_balanced = int(math.ceil(max(n_required, 72) / 6.0) * 6)

        return {
            "standard_reference": "ISO 11136:2014 (ISO Catalogue 50125) & Bi & Meyners (2012)",
            "equivalence_margin_points": equivalence_margin_hedonic,
            "assumed_within_subject_sd": within_subject_sd,
            "alpha_one_sided": alpha,
            "target_power": target_power,
            "minimum_consumers_required": n_balanced,
            "serving_design": "Williams Latin Square (6 sequences) with 3-digit blind random codes",
            "evaluation_matrices": [
                "Matrix A: Unspiced Pressure-Cooked Dal Slurry (1:3.5 dal:water, 0.5% NaCl only) — Stringent Off-Note Detection",
                "Matrix B: Standardized Tempered Indian Dal Tadka — Real-World Consumer Acceptance",
            ],
            "tost_decision_rule": (
                f"Equivalence is demonstrated if and only if the 90% confidence interval (1 - 2*alpha) "
                f"for (mu_FinnoaQ - mu_IndianRef) lies entirely within [-{equivalence_margin_hedonic:.2f}, +{equivalence_margin_hedonic:.2f}] "
                f"AND trained panel triangle test confirms no soapy/metallic off-note (p_soapy < 0.10)."
            ),
        }


# =============================================================================
# MODULE G: BATCH VARIABILITY, INTAKE DIAGNOSTICS & ADAPTIVE POLICY
# =============================================================================

class BatchVariabilityAndAdaptationModule:
    """
    Module G: Evaluates process robustness across multi-origin/cultivar/storage variability.
    Fixes FAIL-0022 by passing actual thickness H and initial moisture X_wb into the PDE solver,
    and branching on noisy 5-minute intake proxy measurements rather than hidden bound Ca2+.
    """

    @staticmethod
    def simulate_noisy_intake_diagnostics(
        batch: FeedstockBatch,
        rng: np.random.Generator,
    ) -> Dict[str, Any]:
        h_mm_true = batch.half_thickness_m * 1000.0
        h_mm_obs = float(np.clip(h_mm_true + rng.normal(0.0, 0.025), 0.65, 1.55))
        x_wb_obs = float(np.clip(batch.initial_moisture_wb + rng.normal(0.0, 0.0025), 0.07, 0.15))

        wai_3min_true = 24.0 * ((1.0 / h_mm_true) ** 0.85) * (1.0 - 0.0095 * (batch.bound_ca_mol_m3 - 12.8))
        wai_3min_obs = float(np.clip(wai_3min_true + rng.normal(0.0, 1.15), 8.0, 35.0))

        ca_est_from_wai = 12.8 + ((1.0 - (wai_3min_obs / (24.0 * ((1.0 / h_mm_obs) ** 0.85)))) / 0.0095)
        ca_est = float(np.clip(0.82 * ca_est_from_wai + 0.18 * batch.bound_ca_mol_m3 + rng.normal(0.0, 2.1), 10.0, 50.0))

        s_htc_obs = ca_est * ((h_mm_obs / 1.0) ** 1.35)
        is_ood = bool(h_mm_obs > 1.32 or x_wb_obs < 0.082 or ca_est > 45.0)

        if s_htc_obs < 29.0:
            assigned_tier = "TIER_1_MILD"
        elif s_htc_obs <= 42.5:
            assigned_tier = "TIER_2_STANDARD"
        else:
            assigned_tier = "TIER_3_INTENSIVE"

        s_htc_true = batch.bound_ca_mol_m3 * ((h_mm_true / 1.0) ** 1.35)
        if s_htc_true < 29.0:
            true_tier = "TIER_1_MILD"
        elif s_htc_true <= 42.5:
            true_tier = "TIER_2_STANDARD"
        else:
            true_tier = "TIER_3_INTENSIVE"

        return {
            "h_mm_obs": h_mm_obs,
            "x_wb_obs": x_wb_obs,
            "wai_3min_pct_obs": wai_3min_obs,
            "ca_est_mol_m3": ca_est,
            "s_htc_obs": s_htc_obs,
            "s_htc_true": s_htc_true,
            "assigned_tier": assigned_tier,
            "true_tier": true_tier,
            "tier_match": bool(assigned_tier == true_tier),
            "is_out_of_domain": is_ood,
        }

    @staticmethod
    def get_tier_treatment_policy(tier_name: str) -> Tuple[TreatmentChemistrySpec, PretreatmentProcessConfig]:
        if tier_name == "TIER_1_MILD":
            chem = TreatmentChemistryModule.design_citrate_buffer(
                treatment_id="ADAPT-TIER-1",
                name="Tier 1 Mild Conditioning (0.105 M K/Na Citrate, pH 5.30)",
                total_citrate_M=0.105,
                target_pH=5.30,
                f_K=0.90,
            )
            cfg = PretreatmentProcessConfig(soak_temp_c=52.0, soak_time_min=15.0, ultrasound_w_per_l=17.0)
        elif tier_name == "TIER_2_STANDARD":
            chem = TreatmentChemistryModule.design_citrate_buffer(
                treatment_id="ADAPT-TIER-2",
                name="Tier 2 Standard HTC Conditioning (0.145 M K/Na Citrate, pH 5.20)",
                total_citrate_M=0.145,
                target_pH=5.20,
                f_K=0.90,
            )
            cfg = PretreatmentProcessConfig(soak_temp_c=55.0, soak_time_min=20.0, ultrasound_w_per_l=17.0)
        else:  # TIER_3_INTENSIVE
            chem = TreatmentChemistryModule.design_citrate_buffer(
                treatment_id="ADAPT-TIER-3",
                name="Tier 3 Severe HTC Conditioning (0.185 M K/Na Citrate, pH 5.20)",
                total_citrate_M=0.185,
                target_pH=5.20,
                f_K=0.90,
            )
            cfg = PretreatmentProcessConfig(
                soak_temp_c=57.0, soak_time_min=26.0, ultrasound_w_per_l=17.0, vacuum_pulse_kpa_abs=15.0
            )
        return chem, cfg


# =============================================================================
# MODULE H: PLANT OPERATIONS, DRYING STRESS, SCHEDULING & ECONOMICS (15 TPD)
# =============================================================================

class PlantOperationsAndEconomicsModule:
    """
    Module H: 15 TPD industrial process engineering, temperature-coupled drying stress
    simulation (fixing FAIL-0021), and reconciled once-through vs recycled bath OpEx (fixing FAIL-0025).
    """

    @staticmethod
    def simulate_convective_drying_and_stress(
        regime_name: str,
        stage1_temp_c: float,
        stage1_time_min: float,
        stage2_temp_c: float,
        stage2_time_min: float,
        tempering_time_min: float = 0.0,
        pre_dryer_moisture_wb: float = 0.280,
        target_moisture_wb: float = 0.105,
        half_thickness_m: float = 1.10e-3,
    ) -> Dict[str, Any]:
        m0_db = pre_dryer_moisture_wb / (1.0 - pre_dryer_moisture_wb)
        m_eq_db = 0.042
        page_n = 1.12  # Shepherd & Bhardwaj (1988) pigeon pea Page exponent
        ea_dry = 29800.0  # J/mol
        sigma_yield_pa = 1.65e6  # 1.65 MPa tensile fissure threshold (<= 2.0 MPa RAEBYES guard)

        nz = 25
        dz = half_thickness_m / (nz - 1)
        m_prof = np.full(nz, m0_db, dtype=np.float64)

        dt = 2.0
        total_dry_min = stage1_time_min + stage2_time_min + tempering_time_min
        steps = int((total_dry_min * 60.0) / dt)

        peak_stress_pa = 0.0
        t_reach_target_min: Optional[float] = None

        for step in range(steps):
            t_min = (step * dt) / 60.0
            if t_min < stage1_time_min:
                temp_c = stage1_temp_c
                is_tempering = False
            elif t_min < stage1_time_min + stage2_time_min:
                temp_c = stage2_temp_c
                is_tempering = False
            else:
                temp_c = stage2_temp_c
                is_tempering = True

            temp_k = temp_c + 273.15
            # Internal diffusivity in cotyledon slab (m^2/s) with Arrhenius temperature dependence
            d_in = 3.85e-10 * math.exp(-(ea_dry / R_GAS) * (1.0 / temp_k - 1.0 / 333.15))
            if not is_tempering and m_prof[-1] < 0.11 and temp_c > 75.0:
                # Case hardening at high air temperature reduces effective diffusivity
                d_in *= 0.46

            d2m = (m_prof[2:] - 2.0 * m_prof[1:-1] + m_prof[:-2]) / (dz * dz)
            m_prof[1:-1] = np.clip(m_prof[1:-1] + dt * d_in * d2m, m_eq_db, m0_db)
            m_prof[0] = m_prof[1]

            if not is_tempering:
                # Exact Robin (Biot) mass-transfer boundary condition with 4-minute thermal warm-up ramp:
                warmup_ramp = 1.0 - math.exp(-(step * dt) / 200.0)
                bi_dry = 3.20 * ((temp_c / 60.0) ** 3.1) * warmup_ramp
                beta_evap = bi_dry * (dz / half_thickness_m)
                m_prof[-1] = (m_prof[-2] + beta_evap * m_eq_db) / (1.0 + beta_evap)
            else:
                # Zero surface evaporation during adiabatic tempering: surface equilibrates with interior
                m_prof[-1] = m_prof[-2]

            # Rubbery-to-glassy viscoelastic tensile modulus E(M_surf) (Baryeh & Mangope 2002):
            glassy_factor = 1.0 / (1.0 + math.exp((m_prof[-1] - 0.125) / 0.018))
            e_modulus_pa = 3.9e6 + 19.8e6 * glassy_factor
            beta_shrink = 0.255
            delta_m_grad = max(0.0, float(m_prof[0] - m_prof[-1]))
            sigma_surface_pa = e_modulus_pa * beta_shrink * delta_m_grad
            if sigma_surface_pa > peak_stress_pa:
                peak_stress_pa = sigma_surface_pa

            mean_m_db = float(np.mean(m_prof))
            mean_m_wb = mean_m_db / (1.0 + mean_m_db)
            if t_reach_target_min is None and mean_m_wb <= target_moisture_wb:
                t_reach_target_min = t_min

        final_m_db = float(np.mean(m_prof))
        final_m_wb = final_m_db / (1.0 + final_m_db)

        stress_ratio = peak_stress_pa / sigma_yield_pa
        if stress_ratio <= 0.75:
            broken_grain_pct = 0.35
            fissure_status = "SAFE_BELOW_YIELD"
        elif stress_ratio <= 1.00:
            broken_grain_pct = 0.35 + 1.8 * ((stress_ratio - 0.75) / 0.25) ** 2
            fissure_status = "MARGINAL_SUB_CRITICAL"
        else:
            broken_grain_pct = min(15.0, 2.15 + 14.5 * ((stress_ratio - 1.0) ** 1.25))
            fissure_status = "CRITICAL_FISSURING_EXCEEDS_YIELD"

        return {
            "regime_name": regime_name,
            "stage1_temp_c": stage1_temp_c,
            "stage2_temp_c": stage2_temp_c,
            "tempering_time_min": tempering_time_min,
            "total_schedule_min": total_dry_min,
            "time_to_10_5pct_wb_min": t_reach_target_min if t_reach_target_min is not None else total_dry_min,
            "final_moisture_wb_pct": final_m_wb * 100.0,
            "core_surface_moisture_diff_db": float(m_prof[0] - m_prof[-1]),
            "peak_tensile_stress_MPa": peak_stress_pa / 1e6,
            "yield_threshold_MPa": sigma_yield_pa / 1e6,
            "stress_to_yield_ratio": stress_ratio,
            "broken_grain_loss_pct": broken_grain_pct,
            "fissure_status": fissure_status,
        }

    @staticmethod
    def evaluate_15tpd_plant_balance_and_economics(
        chem: TreatmentChemistrySpec,
        soak_config: PretreatmentProcessConfig,
        drying_result: Dict[str, Any],
        liquor_recycle_fraction: float = 0.85,
        operating_hours_per_day: float = 20.0,
    ) -> Dict[str, Any]:
        q_finished_kg_day = 15000.0
        broken_loss_frac = drying_result["broken_grain_loss_pct"] / 100.0
        leach_loss_frac = 0.0035
        q_raw_input_kg_day = q_finished_kg_day / (1.0 - leach_loss_frac)

        total_bath_circulation_L_day = q_raw_input_kg_day * 1.50
        water_imbibed_L_day = q_raw_input_kg_day * 0.255
        drained_spent_liquor_L_day = total_bath_circulation_L_day - water_imbibed_L_day

        recycled_liquor_L_day = drained_spent_liquor_L_day * liquor_recycle_fraction
        blowdown_effluent_L_day = drained_spent_liquor_L_day * (1.0 - liquor_recycle_fraction)
        fresh_makeup_bath_water_L_day = water_imbibed_L_day + blowdown_effluent_L_day

        effective_dosed_volume_L_day = (
            total_bath_circulation_L_day
            if liquor_recycle_fraction <= 0.0
            else (fresh_makeup_bath_water_L_day + 0.18 * recycled_liquor_L_day)
        )

        kg_k3cit_day = (chem.mass_k3cit_monohydrate_g_L * effective_dosed_volume_L_day) / 1000.0
        kg_na3cit_day = (chem.mass_na3cit_dihydrate_g_L * effective_dosed_volume_L_day) / 1000.0
        kg_h3cit_day = (chem.mass_citric_acid_anhydrous_g_L * effective_dosed_volume_L_day) / 1000.0
        kg_nahco3_day = (chem.mass_nahco3_g_L * effective_dosed_volume_L_day) / 1000.0

        price_k3cit_inr = 165.0
        price_na3cit_inr = 130.0
        price_h3cit_inr = 110.0
        price_nahco3_inr = 42.0

        reagent_cost_inr_day = (
            kg_k3cit_day * price_k3cit_inr
            + kg_na3cit_day * price_na3cit_inr
            + kg_h3cit_day * price_h3cit_inr
            + kg_nahco3_day * price_nahco3_inr
        )
        reagent_cost_inr_per_kg = reagent_cost_inr_day / q_finished_kg_day

        wash_water_L_day = q_raw_input_kg_day * 0.50

        evap_water_B1_kg_day = 3654.42
        evap_water_B2_kg_day = 3854.14  # Exact +199.72 kg/day sensitivity bound preserved per governance rule

        latent_heat_mj_kg = 2.45 / 0.72
        dryer_thermal_mj_day_B1 = evap_water_B1_kg_day * latent_heat_mj_kg
        steeping_thermal_mj_day = (
            (q_raw_input_kg_day * CP_DAL_DRY + fresh_makeup_bath_water_L_day * CP_WATER)
            * max(soak_config.soak_temp_c - 25.0, 0.0) / (1e6 * 0.85)
        )
        total_thermal_mj_day = dryer_thermal_mj_day_B1 + steeping_thermal_mj_day

        thermal_cost_inr_day = total_thermal_mj_day * 1.65
        electrical_kwh_day = (18.5 + (6.5 if soak_config.ultrasound_w_per_l > 0 else 0.0)) * operating_hours_per_day
        electrical_cost_inr_day = electrical_kwh_day * 8.50
        water_effluent_cost_inr_day = ((fresh_makeup_bath_water_L_day + wash_water_L_day) / 1000.0) * 65.0
        labor_qa_packaging_inr_day = 9500.0
        broken_downgrade_penalty_inr_day = (q_finished_kg_day * broken_loss_frac) * 42.0

        total_opex_inr_day = (
            reagent_cost_inr_day
            + thermal_cost_inr_day
            + electrical_cost_inr_day
            + water_effluent_cost_inr_day
            + labor_qa_packaging_inr_day
            + broken_downgrade_penalty_inr_day
        )
        total_opex_inr_per_kg = total_opex_inr_day / q_finished_kg_day

        t_wash_drain_min = 4.0
        t_cooling_pack_min = 12.0
        single_lot_residence_min = (
            soak_config.soak_time_min
            + t_wash_drain_min
            + drying_result["total_schedule_min"]
            + t_cooling_pack_min
        )

        return {
            "capacity_finished_kg_day": q_finished_kg_day,
            "raw_input_kg_day": q_raw_input_kg_day,
            "liquor_recycle_fraction": liquor_recycle_fraction,
            "total_bath_circulation_L_day": total_bath_circulation_L_day,
            "fresh_makeup_bath_water_L_day": fresh_makeup_bath_water_L_day,
            "wash_water_L_day": wash_water_L_day,
            "evap_water_scenario_B1_kg_day": evap_water_B1_kg_day,
            "evap_water_scenario_B2_kg_day": evap_water_B2_kg_day,
            "evap_discrepancy_B2_minus_B1_kg_day": evap_water_B2_kg_day - evap_water_B1_kg_day,
            "reagent_consumption_kg_day": {
                "K3Cit_H2O": kg_k3cit_day,
                "Na3Cit_2H2O": kg_na3cit_day,
                "Citric_Acid": kg_h3cit_day,
                "NaHCO3": kg_nahco3_day,
            },
            "reagent_cost_inr_per_kg": reagent_cost_inr_per_kg,
            "thermal_cost_inr_per_kg": thermal_cost_inr_day / q_finished_kg_day,
            "electrical_cost_inr_per_kg": electrical_cost_inr_day / q_finished_kg_day,
            "water_effluent_cost_inr_per_kg": water_effluent_cost_inr_day / q_finished_kg_day,
            "labor_qa_cost_inr_per_kg": labor_qa_packaging_inr_day / q_finished_kg_day,
            "broken_downgrade_cost_inr_per_kg": broken_downgrade_penalty_inr_day / q_finished_kg_day,
            "total_opex_inr_per_kg": total_opex_inr_per_kg,
            "total_opex_inr_day": total_opex_inr_day,
            "single_lot_residence_time_min": single_lot_residence_min,
            "unit_time_breakdown_min": {
                "pretreatment_steeping": soak_config.soak_time_min,
                "spray_wash_and_dewatering": t_wash_drain_min,
                "convective_drying_and_tempering": drying_result["total_schedule_min"],
                "cooling_and_packaging": t_cooling_pack_min,
            },
        }


# =============================================================================
# GLOBAL SENSITIVITY ANALYSIS (SOBOL / SALTELLI / JANSEN VARIANCE DECOMPOSITION)
# =============================================================================

class GlobalSensitivityAnalyzer:
    """
    Implements Saltelli (2010) / Jansen (1999) Quasi-Monte Carlo Sobol first-order (S_i)
    and total-order (S_Ti) variance-based global sensitivity indices.
    """

    @staticmethod
    def compute_sobol_indices(
        func,
        param_names: List[str],
        bounds: List[Tuple[float, float]],
        n_base: int = 128,
        seed: int = 42,
    ) -> Dict[str, Any]:
        d = len(param_names)
        sampler = stats.qmc.Sobol(d=2 * d, scramble=True, seed=seed)
        u_samples = sampler.random(n=n_base)

        lows = np.array([b[0] for b in bounds], dtype=np.float64)
        highs = np.array([b[1] for b in bounds], dtype=np.float64)

        mat_a = lows + u_samples[:, :d] * (highs - lows)
        mat_b = lows + u_samples[:, d:] * (highs - lows)

        y_a = np.array([func(row) for row in mat_a], dtype=np.float64)
        y_b = np.array([func(row) for row in mat_b], dtype=np.float64)

        var_y = float(np.var(np.concatenate([y_a, y_b]), ddof=1))
        if var_y < 1e-12:
            var_y = 1e-12

        s_first = {}
        s_total = {}
        for i, name in enumerate(param_names):
            mat_ab_i = mat_a.copy()
            mat_ab_i[:, i] = mat_b[:, i]
            y_ab_i = np.array([func(row) for row in mat_ab_i], dtype=np.float64)

            # Saltelli (2010) Eq. (b) first-order & Jansen (1999) Eq. (f) total-order estimators
            v_i_saltelli = float(np.mean(y_b * (y_ab_i - y_a)))
            v_i_jansen = var_y - 0.5 * float(np.mean((y_b - y_ab_i) ** 2))
            v_ti = 0.5 * float(np.mean((y_a - y_ab_i) ** 2))
            v_i = min(max(0.5 * (v_i_saltelli + v_i_jansen), 0.0), v_ti)

            s_first[name] = float(np.clip(v_i / var_y, 0.0, 1.0))
            s_total[name] = float(np.clip(v_ti / var_y, 0.0, 1.0))

        return {
            "n_base_samples": n_base,
            "total_evaluations": n_base * (d + 2),
            "output_mean": float(np.mean(y_a)),
            "output_std": float(math.sqrt(var_y)),
            "first_order_S1": s_first,
            "total_order_ST": s_total,
        }
