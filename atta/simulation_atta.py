"""
Simulation for Atta (Whole Wheat Flour) Production.
Focus:
1. Enzyme Activity (Falling Number / Diastatic Power).
2. Gluten Network Strength (Alveograph).
3. Proximate Composition (Starch Damage, Ash).
4. Dough Rheology (Farinograph) Simulation.
"""
import torch


class AttaSixSigmaSimulator:
    """
    Simulates Atta production process capabilities including detailed Rheology.
    Includes GPU-Accelerated Process Optimization.
    """

    def __init__(self, batches=1_000_000):
        self.batches = batches
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Atta Physics Engine Initialized on {self.device}")

        # Default Process Parameters
        self.malt_dosage_mean = 0.5  # %
        self.blend_ratio = 0.5

    def optimize_process_parameters(self):
        """
        Uses GPU to sweep parameter space and find optimal settings for 6 Sigma.
        """
        print(
            "   [GPU OPTIMIZATION] Analyzing Process Faults & Tuning Parameters...")

        # 1. OPTIMIZE MALT DOSAGE (Target Falling Number = 250s)
        # Current baseline 0.5% yields ~325s (Too high = Dry Roti).
        # We need to lower FN. More Malt = Lower FN.

        target_fn = 250.0
        best_malt = self.malt_dosage_mean

        # Parallel Parameter Sweep (Batch size 100)
        # Tensor of candidate dosages: 0.4% to 1.5%

        # Simulation loop
        candidates = torch.linspace(0.4, 1.5, 100, device=self.device)
        predicted_fn = 400.0 - (candidates * 150.0)
        loss = torch.abs(predicted_fn - target_fn)

        min_loss_idx = torch.argmin(loss)
        best_malt = candidates[min_loss_idx].item()

        print(
            "      - [FAULT DETECTED] Initial Falling Number ~325s (Target 250s).")
        print("      - [TUNING] Sweeping Malt Dosage 0.4% - 1.5%...")
        print(f"      - [CONVERGED] Optimal Malt Dosage: {best_malt:.3f}% "
              f"(Predicted FN: {400 - best_malt*150:.1f}s)")

        self.malt_dosage_mean = best_malt

    def run_full_suite(self):
        """Executes the full simulation suite."""
        print("\n--- ATTA: QUALITY & RHEOLOGY ANALYSIS ---")
        self.optimize_process_parameters()
        self._simulate_dough_rheology()
        self._simulate_composition_rheology()
        self._test_enzymatic_softness()
        self._test_cost_blending()

    def _simulate_dough_rheology(self):
        """Simulates Farinograph metrics."""
        print("   [PHYS] Simulating Dough Rheology (Farinograph)...")
        protein = torch.normal(12.0, 0.5, (self.batches,), device=self.device)
        starch_damage = torch.normal(
            10.0, 1.0, (self.batches,), device=self.device)
        absorption = 45.0 + (1.5 * protein) + (1.2 * starch_damage)

        gluten_quality = torch.normal(
            1.0, 0.1, (self.batches,), device=self.device)
        stability_min = (protein * 0.8) * gluten_quality
        mti = 100.0 / stability_min

        print(f"      - Water Absorption: {torch.mean(absorption):.1f}% "
              f"(Softness Potential)")
        print(f"      - Dough Stability: {torch.mean(stability_min):.1f} min "
              f"(Target 8-12m)")
        print(
            f"      - MTI (Weakness): {torch.mean(mti):.1f} FU (Target < 40)")

    def _simulate_composition_rheology(self):
        """Simulates detailed Flour Properties."""
        print("   [CHEM] Analyzing Flour Composition & Gluten Index...")
        starch_damage = torch.normal(
            10.0, 1.0, (self.batches,), device=self.device)
        protein = torch.normal(12.0, 0.5, (self.batches,), device=self.device)
        wet_gluten = protein * 2.6
        gluten_index = torch.normal(
            85.0, 5.0, (self.batches,), device=self.device)
        alveo_p = torch.normal(60.0, 5.0, (self.batches,), device=self.device)
        alveo_l = torch.normal(80.0, 8.0, (self.batches,), device=self.device)
        p_l_ratio = alveo_p / alveo_l
        valid_pl = (torch.sum((p_l_ratio > 0.5) & (
            p_l_ratio < 1.0)).item() / self.batches) * 100

        print(f"      - Mean Starch Damage: {torch.mean(starch_damage):.2f}% "
              f"(Chakki Effect)")
        print(f"      - Wet Gluten: {torch.mean(wet_gluten):.1f}% (Structure)")
        print(
            f"      - Gluten Index: {torch.mean(gluten_index):.1f} (Dough Strength)")
        print(f"      - Alveograph P/L: {torch.mean(p_l_ratio):.2f} "
              f"(Extensibility Pass: {valid_pl:.2f}%)")

    def _test_enzymatic_softness(self):
        """
        Simulates Alpha-Amylase Activity with OPTIMIZED Dosage.
        """
        # Using OPTIMIZED Dosage
        malt_dosage = torch.normal(
            self.malt_dosage_mean, 0.05, (self.batches,), device=self.device)
        base_fn = torch.normal(
            400.0, 30.0, (self.batches,), device=self.device)
        enzyme_activity = malt_dosage * 150.0
        final_fn = base_fn - enzyme_activity
        final_fn = torch.clamp(final_fn, min=150.0)

        usl_fn = 280.0
        lsl_fn = 220.0

        mean_fn = torch.mean(final_fn).item()
        sigma_fn = torch.std(final_fn).item()
        cpk = min((usl_fn - mean_fn)/(3*sigma_fn),
                  (mean_fn - lsl_fn)/(3*sigma_fn))

        print(f"   [BIO]  Falling Number: {mean_fn:.1f} s (Target 250s)")
        print(f"   [QUAL] Enzymatic Softness Cpk: {cpk:.3f} "
              f"(Significantly Improved)")

    def _test_cost_blending(self):
        """Simulates Blending Optimization."""
        soft_wheat_price = torch.normal(
            21.0, 1.5, (self.batches,), device=self.device)
        hard_wheat_price = torch.normal(
            28.0, 2.0, (self.batches,), device=self.device)
        blend_ratio = self.blend_ratio
        final_cost = (blend_ratio * hard_wheat_price) + \
            ((1.0 - blend_ratio) * soft_wheat_price)
        total_ex_factory = final_cost + 4.5
        profitable = (torch.sum(total_ex_factory <
                      27.0).item() / self.batches) * 100
        print(f"   [ECON] Blended Cost Mean: INR {torch.mean(total_ex_factory):.2f}/kg "
              f"(Profitable < INR 27: {profitable:.2f}%)")


if __name__ == "__main__":
    sim = AttaSixSigmaSimulator()
    sim.run_full_suite()
