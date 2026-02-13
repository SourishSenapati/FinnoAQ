"""
Cost Model Module
Contains functions for calculating total process cost and effective output.
"""
import torch
from .config import (
    ELECTRICITY_RATE_INR_KWH,
    LABOR_COST_INR_HR_BASE,
    RAW_MATERIAL_COST_INR_KG,
    RND_AMORTIZATION_YEARS,
    ANNUAL_OPERATING_HOURS,
    DEFECT_PENALTY_MULTIPLIER
)


def calculate_total_cost(
    capex,
    power_kw,
    throughput_kg_hr,
    defect_rate,
    rnd_cost,
    maintenance_rate_hr,
    params=None
):
    """
    Calculates the Total Cost per Hour with Sensitivity Overrides.
    """
    # defaults
    d_elec_rate = ELECTRICITY_RATE_INR_KWH
    d_mat_cost = RAW_MATERIAL_COST_INR_KG

    # overrides
    if params:
        elec_rate = params.get('electricity_rate', d_elec_rate)
        mat_cost = params.get('material_cost', d_mat_cost)
    else:
        elec_rate = d_elec_rate
        mat_cost = d_mat_cost

    # 1. Energy
    energy_cost_hr = power_kw * elec_rate

    # 2. Material
    material_cost_hr = throughput_kg_hr * mat_cost

    # 3. Labor
    labor_cost_hr = LABOR_COST_INR_HR_BASE + (throughput_kg_hr * 0.1)

    # 4. Depreciation
    total_lifecycle_hours = RND_AMORTIZATION_YEARS * ANNUAL_OPERATING_HOURS
    depreciation_hr = capex / total_lifecycle_hours

    # 5. R&D
    rnd_amortized_hr = rnd_cost / total_lifecycle_hours

    # 6. Maint (passed)

    # 7. Defect (Uses mat_cost)
    defect_cost_hr = throughput_kg_hr * defect_rate * \
        mat_cost * DEFECT_PENALTY_MULTIPLIER

    total_cost_hr = (
        energy_cost_hr +
        material_cost_hr +
        labor_cost_hr +
        depreciation_hr +
        rnd_amortized_hr +
        maintenance_rate_hr +
        defect_cost_hr
    )

    return total_cost_hr


def calculate_effective_output(throughput_nominal, defect_rate, downtime_rate):
    """
    Effective Output = Throughput * (1 - Defect) * (1 - Downtime)
    """
    effective_output = throughput_nominal * \
        (1.0 - defect_rate) * (1.0 - downtime_rate)
    return torch.clamp(effective_output, min=0.0)
