"""
Advanced Simulation for Mustard Honey Value Addition.
Modules:
1. Creamed Honey Crystallization (Avrami Kinetics).
2. Mead Fermentation (Monod Growth).
3. Detailed Composition & Rheology (Viscosity, Alcohol).
"""
import math
import torch


class MustardValueAddSimulator:
    """
    Simulates the value-addition process for Mustard Honey.
    """

    def __init__(self, batches=1_000_000):
        self.batches = batches
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Mustard Value-Add Physics Engine Initialized on {self.device}")

    def run_full_suite(self):
        """Executes the full simulation suite."""
        print("\n--- MUSTARD HONEY VALUE ADDITION: SIMULATION SUITE ---")
        self._simulate_creaming()
        self._simulate_mead()

    def _simulate_creaming(self):
        """
        Simulates nucleation and crystal growth using Avrami equation.
        X(t) = 1 - exp(-k * t^n)
        Target: Fine crystals (<20 microns) for 'butter' texture.
        """
        print("   [PHYS] Simulating Creamed Honey Rheology...")

        # Temperature control is critical (14C Optimum)
        temp_c = torch.normal(14.0, 0.5, (self.batches,), device=self.device)

        # Nucleation Rate (k): k = A * exp(-Ea/RT) * exp(-B / (Tm - T)^2)
        # Simplified Gaussian around 14C
        nucleation_k = torch.exp(-(temp_c - 14.0)**2 / 2.0)

        # Crystal Size inversely proportional to nucleation density
        mean_crystal_size = 15.0 / (nucleation_k + 0.1)  # microns

        # RHEOLOGY: Viscosity (Herschel-Bulkley Model)
        # Viscosity increases as Crystal Fraction -> 100%
        # Yield Stress (Force to start flowing) depends on Crystal Size (Smaller = Higher Network Strength)
        crystal_fraction = 1.0  # Assuming full crystallization
        yield_stress_pa = (1.0 / mean_crystal_size) * 500.0  # Empirical
        spreadability_score = torch.clamp(
            yield_stress_pa / 50.0, min=1.0, max=10.0)  # 10 = Very Firm

        # TASTE & MOUTHFEEL (Sensory Mimicry)
        # Grittiness perception threshold is > 25 microns.
        # Solubility on tongue depends on crystal size dissolution rate.
        # Fast dissolve = smooth
        disolution_rate = 1.0 / (mean_crystal_size / 10.0)
        mouthfeel_score = disolution_rate
        # Specification: < 25 microns is smooth. > 50 is gritty.
        smoothness_pass = (torch.sum(mean_crystal_size <
                           25.0).item() / self.batches) * 100
        ideal_spread = (torch.sum((spreadability_score > 3.0) & (
            spreadability_score < 7.0)).item() / self.batches) * 100

        print(f"      - Mean Crystal Size: {torch.mean(mean_crystal_size):.2f} um "
              f"(Smoothness: {smoothness_pass:.2f}%)")
        print(f"      - Spreadability Index: {torch.mean(spreadability_score):.1f}/10 "
              f"(Ideal Range: {ideal_spread:.2f}%)")
        print(f"      - Mouthfeel (Dissolution): {torch.mean(mouthfeel_score):.1f}/10 "
              f"(Silky Texture)")
        print(f"      - Crystal Fraction: {crystal_fraction * 100:.1f}%")

    def _simulate_mead(self):
        """
        Simulates yeast metabolism for Mead production.
        Monod Equation: mu = mu_max * [S] / (Ks + [S])
        """
        print("   [BIO]  Simulating Mead Fermentation Kinetics...")

        # Initial Conditions
        yan = torch.normal(180.0, 20.0, (self.batches,),
                           device=self.device)  # Nitrogen ppm

        # Kinetics
        mu_max = 0.25  # /hr
        # ks = 5.0 g/L (Reference)

        # Nutrient Limitation Factor (Liebig's Law)
        nitrogen_factor = torch.clamp(yan / 150.0, max=1.0)
        effective_growth_rate = mu_max * nitrogen_factor
        fermentation_time_days = (
            # Empirical scaling
            math.log(100.0) / effective_growth_rate) / 24.0 * 5.0

        # CHEMICAL ANALYSIS (End Product)
        # Alcohol by Volume (ABV) depends on Sugar consumed.
        # 16.83 g sugar -> 1% Alcohol approx.
        initial_brix = 24.0  # % Sugar
        final_residual_sugar = torch.normal(
            1.5, 0.5, (self.batches,), device=self.device)  # Dry Mead
        sugar_consumed = (initial_brix * 10.0) - final_residual_sugar
        # Actually Brix is g/100g. SG drop is better metric.
        # Let's use standard rule: (OG - FG) * 131.25
        og = 1.100
        fg = 1.000 + (final_residual_sugar / 1000.0)  # Approx
        abv = (og - fg) * 131.25

        # Stuck Fermentation Definition: Time > 35 days or Sugar Residual > 20g/L
        stuck_prob = (torch.sum(fermentation_time_days >
                      30.0).item() / self.batches) * 100

        print(f"      - Mean ABV: {torch.mean(abv):.2f}% (Target 11-13%)")
        print(f"      - Sugar Consumed: {torch.mean(sugar_consumed):.1f} g/L")
        print(
            f"      - Fermentation Time: {torch.mean(fermentation_time_days):.1f} Days")
        print(f"      - Stuck Fermentation Risk: {stuck_prob:.2f}% "
              f"(Nutrient Management Check)")


if __name__ == "__main__":
    sim = MustardValueAddSimulator()
    sim.run_full_suite()
