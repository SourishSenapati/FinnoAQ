def calculate_objective(output_kg_hr, total_cost_hr, defect_prob, catastrophic_prob):
    """
    Calculates the optimization objective:
    Maximize (Output / Cost) * Reliability Factors
    """
    # Avoid division by zero
    cost_safe = total_cost_hr + 1e-6

    base_objective = output_kg_hr / cost_safe

    # Reliability Penalties
    reliability_factor = (1.0 - defect_prob) * (1.0 - catastrophic_prob)

    return base_objective * reliability_factor
