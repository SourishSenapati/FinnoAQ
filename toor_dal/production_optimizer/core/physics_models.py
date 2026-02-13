import torch
from .config import (
    SPECIFIC_HEAT_PULSE_KJ_KG_C,
    ACTIVATION_ENERGY_J_MOL,
    FREQUENCY_FACTOR_A,
    GAS_CONSTANT_J_MOL_K,
    HEAT_CONVERSION_EFFICIENCY,
    CONVECTION_COEFF_W_M2K,
    CASING_AREA_M2
)


def calculate_temp_rise_convection(power_watts, time_sec, mass_kg, ambient_temp_k, device):
    """
    Calculates temperature rise considering convection cooling.
    Delta T = (eta * P / (h * A)) * (1 - exp(-h * A * t / (m * Cp)))
    """
    # Unused arguments kept for API consistency
    _ = ambient_temp_k
    _ = device

    # Constants as tensors for broadcasting if needed, or scalars
    cp_j_kg_k = SPECIFIC_HEAT_PULSE_KJ_KG_C * 1000.0

    # h * A
    hA = CONVECTION_COEFF_W_M2K * CASING_AREA_M2

    # Exponent term: -hAt / mCp
    exponent = -(hA * time_sec) / (mass_kg * cp_j_kg_k)
    exp_term = torch.exp(exponent)

    # Steady state temp rise: eta * P / hA
    max_delta_t = (HEAT_CONVERSION_EFFICIENCY * power_watts) / hA

    delta_t = max_delta_t * (1.0 - exp_term)

    return delta_t


def calculate_arrhenius_denaturation_phys(temp_k, time_sec, device):
    """
    Calculates protein denaturation using strict Arrhenius kinetics.
    k = A * exp(-Ea / RT)
    P = 1 - exp(-k * t)
    """
    # Avoid div by zero in temp (unlikely in K)
    _ = device

    # k value
    # -Ea / RT
    exponent = -ACTIVATION_ENERGY_J_MOL / (GAS_CONSTANT_J_MOL_K * temp_k)
    k = FREQUENCY_FACTOR_A * torch.exp(exponent)

    # Probability
    # P = 1 - exp(-k * t)
    denaturation_prob = 1.0 - torch.exp(-k * time_sec)

    # Clip to 0-1 just in case
    return torch.clamp(denaturation_prob, 0.0, 1.0)
