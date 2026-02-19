"""
Machinery Energy & Cost Simulation Module.
Defines energy consumption curves for Lab vs Industrial scale.
"""


def simulate_grinding_energy(scale="lab", throughput_kg_hr=5.0):
    """
    Calculates KWh/kg based on Bond's Work Index.
    Multigrain is harder than pure Wheat.

    Work Index (Average):
    - Wheat: 12 kWh/ton
    - Maize: 15 kWh/ton
    - Soybean: 14 kWh/ton

    Energy (kW) = 1.1 * throughput * (10 / sqrt(P80) - 10 / sqrt(F80)) * Wi
    Simplified:
    Lab Scale Efficiency: 30% (Small motors, belt loss)
    Industrial Efficiency: 85% (Direct drive, optimized)
    """
    base_kwh_ton = 14.0  # Multigrain average

    if scale == "lab":
        eff = 0.30
        power_usage = throughput_kg_hr * (base_kwh_ton / 1000.0) / eff
        # Lab mills run constantly even when idle
        idle_load = 0.5
        total_kw = max(power_usage, idle_load)

    else:
        eff = 0.85
        # Industrial economy of scale
        power_usage = throughput_kg_hr * (base_kwh_ton / 1000.0) / eff
        total_kw = power_usage * 1.05  # +5% for conveying/sifting

    cost_per_unit = 12.0  # INR/kWh Industrial

    return {
        "energy_kwh_kg": total_kw / throughput_kg_hr,
        "cost_inr_kg": (total_kw / throughput_kg_hr) * cost_per_unit,
        "power_draw_kw": total_kw
    }
