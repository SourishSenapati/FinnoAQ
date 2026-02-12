"""
Life Cycle Assessment (LCA) module for Toor Dal production.
Compares Carbon Footprint and Water Usage against traditional farming.
"""


class LcaAnalyzer:
    """
    Analyzes the environmental impact of the optimized Toor Dal process.
    """

    def __init__(self):
        self.carbon_baseline = 1.8  # kg CO2e/kg (Traditional)
        self.water_baseline = 4500.0  # L/kg (Traditional crop)

    def analyze_impact(self, batch_size_kg=1000):
        """
        Calculates carbon and water savings for a given batch size.
        """
        # Optimized Process (Analogue)
        # Usage: Brokens (Lower footprint allocation), Less cooking time (Consumer energy)

        carbon_optimized = 0.85  # kg CO2e/kg (Result of byproduct usage)
        # L/kg (Less irrigation required for lower grade pulses)
        water_optimized = 1200.0

        # Savings
        carbon_saved = (self.carbon_baseline -
                        carbon_optimized) * batch_size_kg
        water_saved = (self.water_baseline - water_optimized) * batch_size_kg

        print(f"--- LCA ANALYSIS (Per {batch_size_kg} kg Batch) ---")
        print(f"Carbon Reduced: {carbon_saved:.2f} kg CO2e")
        print(f"Water Conserved: {water_saved:.2f} Liters")

        return carbon_saved, water_saved


if __name__ == "__main__":
    lca = LcaAnalyzer()
    c, w = lca.analyze_impact()
    print("Impact Analysis Complete.")
