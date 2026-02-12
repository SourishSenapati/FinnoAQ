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

    def analyze_impact(self, batch_size_kg=1000, actual_cooking_time=15.0):
        """
        Calculates carbon and water savings based on process + consumer behavior.
        Now includes 'Cradle-to-Plate' logic (Cooking Energy).
        """
        # 1. Production Phase Savings (Cradle-to-Gate)
        # Using Broken Dal (Byproduct) instead of Prime -> Lower allocation.
        carbon_production_optimized = 0.85  # kg CO2e/kg
        water_optimized = 1200.0  # L/kg

        carbon_saved_production = (
            self.carbon_baseline - carbon_production_optimized) * batch_size_kg
        water_saved = (self.water_baseline - water_optimized) * batch_size_kg

        # 2. Consumer Phase Savings (Gate-to-Plate)
        # Faster cooking = Less LPG/Electricity.
        baseline_cooking_time = 45.0  # Traditional Toor Dal (mins)
        time_saved_min = max(0, baseline_cooking_time - actual_cooking_time)

        # Energy Model: LPG Burner ~0.2 kg/hr consumption
        lpg_saved_kg = (time_saved_min / 60.0) * 0.2 * batch_size_kg
        co2_from_lpg = lpg_saved_kg * 3.0  # 1kg LPG = 3kg CO2 approx

        total_carbon_saved = carbon_saved_production + co2_from_lpg

        print(f"--- LCA IMPACT REPORT (Batch: {batch_size_kg} kg) ---")
        print(
            f"   [Cradle-to-Gate] Production CO2 Saved: {carbon_saved_production:.2f} kg")
        print(
            f"   [Gate-to-Plate]  Cooking Gas Saved:    {lpg_saved_kg:.2f} kg LPG "
            f"({co2_from_lpg:.2f} kg CO2)")
        print(
            f"   [TOTAL]          NET CARBON REDUCTION: {total_carbon_saved:.2f} kg CO2e")
        print(
            f"   [WATER]          Water Conserved:      {water_saved:.0f} Liters")

        return total_carbon_saved, water_saved


if __name__ == "__main__":
    lca = LcaAnalyzer()
    c, w = lca.analyze_impact()
    print("Impact Analysis Complete.")
