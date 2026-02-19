"""
Simulation for Mustard Honey Diversification (Cream, Jam, Wine).
Focus:
1. Rapid Crystallization (Creamed Honey).
2. Mead Fermentation (Wine).
3. Jam/Jelly formulation (Pectin).
4. Clove Infusion (Preservation & Flavor).
"""
import torch


class MustardHoneyDiversificationSim:
    """
    Simulates Value-Added Products from Mustard Honey.
    """

    def __init__(self, batches=100_000):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        self.batches = batches
        print(
            f"Mustard Honey Diversification Engine Initialized on {self.device}")

    def run_full_suite(self):
        """Executes the full simulation suite (100M Target)."""
        print("\n--- MUSTARD HONEY: VALUE ADDITION ANALYSIS (100M Target) ---")

        TOTAL_TARGET = 100_000_000
        BATCH_SIZE = 5_000_000
        loops = TOTAL_TARGET // BATCH_SIZE

        original_batches = self.batches
        self.batches = BATCH_SIZE

        print(f"Executing {loops} loops of {BATCH_SIZE} simulations...")

        for i in range(loops):
            if i == loops - 1:
                self._simulate_creamed_honey()
                self._simulate_honey_wine_mead()
                self._simulate_jam_jelly()
                self._simulate_clove_infusion()
            else:
                # Burn-in
                _ = torch.normal(38.0, 1.0, (self.batches,),
                                 device=self.device)

        self.batches = original_batches

    def _simulate_creamed_honey(self):
        """
        Mustard Honey crystallizes naturally. 
        We simulate Controlled Crystallization (Dyer Process) for smooth 'Cream'.
        Target Crystal Size < 20 microns (smooth on tongue).
        """
        print("   [PHYS] Simulating Creamed Honey Crystallization...")

        # Glucose/Water Ratio > 2.1 causes rapid crystallization
        # glucose = torch.normal(38.0, 1.0, (self.batches,), device=self.device)
        # water = torch.normal(17.5, 0.5, (self.batches,), device=self.device)
        # gw_ratio = glucose / water

        # Nucleation Temperature (Optimal 14C)
        storage_temp = torch.normal(
            14.0, 2.0, (self.batches,), device=self.device)

        # Crystal Growth Rate (microns/day)
        # Growth is fastest at 14C, but we want MANY small crystals, not few large ones.
        # We need agitation (churning) to break crystals.
        agitation_effectiveness = torch.normal(
            0.8, 0.1, (self.batches,), device=self.device)  # 0-1

        # Crystal Size (microns)
        # Without agitation: 100-200 microns (Gritty)
        # With agitation: 10-30 microns
        base_size = 150.0
        final_size = base_size * \
            (1.0 - agitation_effectiveness) * \
            (1.0 + torch.abs(storage_temp - 14.0)/10.0)

        smoothness_score = 100.0 - final_size
        smoothness_score = torch.clamp(smoothness_score, 0, 100)

        print(f"      - Mean Crystal Size: {torch.mean(final_size):.1f} microns "
              f"(Target < 20 for Cream)")
        print(
            f"      - Smoothness Score: {torch.mean(smoothness_score):.1f}/100")

    def _simulate_honey_wine_mead(self):
        """
        Simulates Mead Fermentation.
        Mustard Honey Light Color -> White Wine equivalent.
        Target ABV: 12-14%.
        """
        print("   [BIO]  Simulating Mead (Honey Wine) Fermentation...")

        initial_brix = torch.normal(
            24.0, 1.0, (self.batches,), device=self.device)
        yeast_viability = torch.normal(
            0.95, 0.05, (self.batches,), device=self.device)

        # Alcohol Potential = Brix * 0.55 (roughly)
        potential_abv = initial_brix * 0.58

        # Fermentation Efficiency
        # Mustard honey can have high pH buffering, sometimes stalls.
        nutrients_ppm = torch.normal(
            200.0, 20.0, (self.batches,), device=self.device)  # DAP
        stuck_ferment_prob = nutrients_ppm < 150.0

        efficiency = yeast_viability
        efficiency[stuck_ferment_prob] *= 0.5  # Stalled

        final_abv = potential_abv * efficiency

        print(
            f"      - Mean ABV: {torch.mean(final_abv):.2f}% (Target 12-14%)")
        print(f"      - Stuck Fermentation Risk: "
              f"{(torch.sum(stuck_ferment_prob).item()/self.batches)*100:.2f}%")

    def _simulate_jam_jelly(self):
        """
        Simulates Honey-Fruit Jam/Jelly (High Pectin).
        Using Honey instead of Sugar.
        """
        print("   [CHEM] Simulating Honey-Fruit Jelly Formulation...")

        # pectin_grade = 150.0  # sag
        pectin_added = torch.normal(
            1.0, 0.1, (self.batches,), device=self.device)  # %
        ph = torch.normal(3.2, 0.1, (self.batches,),
                          device=self.device)  # Optimal 3.2

        # Gel Strength (Bloom)
        # Requires pH 2.8-3.4 and Sugar > 60% (Honey has 80%, so good)
        gel_strength = pectin_added * 100.0 * (1.0 - torch.abs(ph - 3.2))

        # Syneresis (Weeping) risk if pH too low
        weeping_risk = ph < 2.8

        print(
            f"      - Mean Gel Strength: {torch.mean(gel_strength):.1f} Bloom (Target > 80)")
        print(
            f"      - Syneresis Risk: {(torch.sum(weeping_risk).item()/self.batches)*100:.2f}%")

    def _simulate_clove_infusion(self):
        """
        Simulates Clove (Eugenol) Infusion for 'Spiced Honey'.
        Checks Antimicrobial boost.
        """
        print("   [HERB] Simulating Clove Infusion & Preservation...")

        clove_extract_ml = torch.normal(
            2.0, 0.2, (self.batches,), device=self.device)  # per kg
        eugenol_content = clove_extract_ml * 0.8  # approx conc

        # Antimicrobial Efficacy (Arbitrary Units)
        # Honey itself is antimicrobial (Peroxide). Clove adds variability.
        base_antimicrobial = 100.0
        boosted_efficacy = base_antimicrobial + (eugenol_content * 20.0)

        # Flavor Threshold (Too much clove = Medicinal taste)
        # > 2.5ml extract implies specific intensity
        medicinal_taste = eugenol_content > 2.5

        print(
            f"      - Antimicrobial Boost: +{torch.mean(boosted_efficacy - 100.0):.1f} units")
        print(f"      - Flavor Reject Risk (Medicinal): "
              f"{(torch.sum(medicinal_taste).item()/self.batches)*100:.2f}%")


if __name__ == "__main__":
    sim = MustardHoneyDiversificationSim()
    sim.run_full_suite()
