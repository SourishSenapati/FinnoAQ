"""
FinnoaQ Toor Dal — Frontier Multiscale Biophysical Architecture.
Bridges:
Scale A: Molecular Species & Ion Exchange (Pectin, Ca2+, Na+, Vicilin/Legumin)
Scale B: Cellular & Middle-Lamella Cohesion (Intercellular Adhesion Stress)
Scale C: Particle-Scale Continuum Parameters (k_soft, Deff, tau_cook)
"""

import math
from typing import Dict, Any, List, Tuple


class MolecularSpeciesInventory:
    """
    Biochemical species inventory specific to Cajanus cajan (Pigeon Pea).
    """
    def __init__(self):
        self.storage_proteins = {
            "vicilin_7S": {
                "molecular_weight_kda": 150.0,
                "denaturation_temp_c": 82.5,
                "fraction_of_total_protein": 0.65
            },
            "legumin_11S": {
                "molecular_weight_kda": 320.0,
                "denaturation_temp_c": 91.0,
                "fraction_of_total_protein": 0.25
            }
        }
        self.cell_wall_polysaccharides = {
            "homogalacturonan_pectin": {
                "monomer": "D-galacturonic acid (MW 194.14 g/mol)",
                "nominal_degree_of_esterification_de": 0.58,  # Tropical transit HTC dal
                "calcium_binding_capacity_mmol_g": 0.85
            },
            "cellulose_microfibrils": {
                "crystallinity_index": 0.42,
                "fraction_cell_wall": 0.35
            }
        }
        self.minerals_and_phytate = {
            "calcium_content_mg_100g": 73.0,
            "magnesium_content_mg_100g": 115.0,
            "phytic_acid_mg_100g": 850.0,
            "phytate_to_divalent_ratio": 2.4  # In fresh dal; drops in aged HTC dal
        }


class MolecularToContinuumTransfer:
    """
    Explicit mathematical transfer functions bridging atomistic/ionic mechanisms
    to continuum macroscopic transport and softening parameters.
    """
    def __init__(
        self,
        k_soft_base: float = 0.0035,
        Ea_soft_j_mol: float = 85400.0,
        D_m_base: float = 2.40e-11
    ):
        self.k_base = k_soft_base
        self.Ea = Ea_soft_j_mol
        self.D_base = D_m_base
        self.Rg = 8.314

    def compute_effective_softening_rate(
        self,
        temperature_c: float,
        sodium_displacement_fraction: float,
        calcium_bridge_density: float
    ) -> float:
        """
        Macroscopic softening rate constant as a function of temperature (Arrhenius)
        and molecular middle-lamella calcium displacement.
        """
        T_k = temperature_c + 273.15
        arrhenius_factor = math.exp(-self.Ea / (self.Rg * T_k))
        # Calcium crosslinks strongly retard softening; Na+ displacement accelerates it
        ionic_factor = (1.0 + 3.2 * sodium_displacement_fraction) / max(0.1, 1.0 + 2.5 * calcium_bridge_density)
        return self.k_base * arrhenius_factor * ionic_factor * 1e11

    def compute_effective_diffusivity(
        self,
        temperature_c: float,
        sodium_displacement_fraction: float
    ) -> float:
        """
        Effective water diffusivity in cotyledon matrix as a function of temperature
        and middle-lamella swelling induced by monovalent ion exchange.
        """
        T_k = temperature_c + 273.15
        arrhenius_diff = math.exp(-32400.0 / (self.Rg * T_k))
        # Swelling expands intercellular micro-channels by 15-30%
        swelling_factor = 1.0 + 0.35 * sodium_displacement_fraction
        return self.D_base * arrhenius_diff * swelling_factor * 1e5


class CellularTissueTwin:
    """
    Represents split cotyledon cellular tissue mechanics and middle-lamella debonding.
    """
    def __init__(
        self,
        initial_adhesion_strength_kpa: float = 450.0,
        critical_cooking_squash_threshold_kpa: float = 45.0
    ):
        self.sigma_0 = initial_adhesion_strength_kpa
        self.sigma_crit = critical_cooking_squash_threshold_kpa

    def evaluate_tissue_softening(
        self,
        soak_treatment_conc: float,
        cooking_time_min: float,
        cooking_temp_c: float = 100.0
    ) -> Dict[str, Any]:
        """
        Evaluates tissue cohesion stress and determines whether the cooking endpoint
        has been reached (cellular separation under 1.0 kg squash force).
        """
        transfer = MolecularToContinuumTransfer()
        # Sodium displacement fraction in middle lamella
        chi_Na = min(1.0, soak_treatment_conc / 0.50)
        # Residual calcium bridge density
        rho_Ca = max(0.1, 0.75 * (1.0 - 0.70 * chi_Na))

        k_soft = transfer.compute_effective_softening_rate(cooking_temp_c, chi_Na, rho_Ca)
        Deff = transfer.compute_effective_diffusivity(cooking_temp_c, chi_Na)

        # Tissue cohesion evolution: exponential decay of intercellular middle-lamella pectin bonds
        t_sec = cooking_time_min * 60.0
        cohesion_stress = self.sigma_0 * math.exp(-k_soft * t_sec)

        is_cooked = cohesion_stress <= self.sigma_crit
        softening_progress_pct = min(100.0, (1.0 - (cohesion_stress / self.sigma_0)) * 100.0)

        # Whistle equivalent (3.8 min induction lag + ~3.2 min per whistle)
        whistles_equiv = max(0.0, (cooking_time_min - 3.8) / 3.2)

        return {
            "cooking_time_min": cooking_time_min,
            "soak_treatment_conc_pct": soak_treatment_conc,
            "molecular_calcium_bridge_density": round(rho_Ca, 3),
            "sodium_displacement_fraction": round(chi_Na, 3),
            "effective_softening_rate_ksoft": round(k_soft, 6),
            "effective_diffusivity_Deff_m2_s": round(Deff, 14),
            "intercellular_cohesion_stress_kpa": round(cohesion_stress, 2),
            "softening_progress_pct": round(softening_progress_pct, 1),
            "is_cooked_endpoint_reached": is_cooked,
            "whistles_equivalent": round(whistles_equiv, 1)
        }
