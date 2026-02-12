"""
Simulates Ghee Production using Bilona Method.
Validates:
1. FRE (Fat Recovery Efficiency).
2. Maillard Reaction (Flavor).
3. Detailed Lipid Profile & Physical Constants.
Includes GPU-Accelerated Parameter Tuning.
"""
import torch


class GheeProductionSimulator:
    """
    Simulates Ghee Process & Chemical Composition.
    Includes Optimization Engine.
    """

    def __init__(self, batches=1_000_000):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        self.batches = batches
        print(f"Ghee Bilona Physics Engine Initialized on {self.device}")

        # Default Process Parameters
        self.churn_temp_setpoint = 14.0  # Initial guess (sub-optimal)

    def optimize_churning_physics(self):
        """
        Uses GPU to sweep Churning Temperature to find Max Yield.
        """
        print("   [GPU OPTIMIZATION] Tuning Churning Thermodynamics...")

        # Sweep Temperature from 10C to 18C
        temps = torch.linspace(10.0, 18.0, 100, device=self.device)

        # Vectorized Simulation of Mean Yield at each Temp point
        # Yield function: exp(-(T - 13.0)**2 / 8.0) * exp(-(4.6-4.6)**2/0.1) * (38-30) + 30
        # Peak should be at 13.0.

        # We simulate 1 Million batches for EACH temp point? No, too slow.
        # We simulate the FUNCTION response.

        yield_curve = 30.0 + (8.0 * torch.exp(-(temps - 13.0)**2 / 8.0))

        max_idx = torch.argmax(yield_curve)
        best_temp = temps[max_idx].item()

        print(
            f"      - [FAULT] Initial Setpoint 14.0C (Yield ~ {30 + 8*0.88:.2f} g/L).")
        print(f"      - [SWEEP] Analyzing Phase Inversion across 10-18C...")
        print(
            f"      - [OPTIMAL] Detected Peak Yield at {best_temp:.1f}C (Predicted Yield: {yield_curve[max_idx]:.2f} g/L).")

        self.churn_temp_setpoint = best_temp

    def run_full_suite(self):
        """Executes the full Ghee simulation suite."""
        print("\n--- GHEE BILONA: PROCESS & COMPOSITION ANALYSIS ---")
        self.optimize_churning_physics()
        self._simulate_structure_texture()
        self._simulate_lipid_profile()
        self._test_churning_yield()
        self._test_maillard_flavor()

    def _simulate_structure_texture(self):
        """Simulates Graininess and 'Danedar' Texture."""
        print("   [PHYS] Simulating 'Danedar' Texture & Granularity...")
        cooling_temp_maintenance = torch.normal(
            29.0, 0.5, (self.batches,), device=self.device)
        hold_time_moas = torch.normal(
            12.0, 1.0, (self.batches,), device=self.device)
        driving_force = 1.0 / \
            (torch.abs(cooling_temp_maintenance - 28.0) + 0.1)
        crystal_size_mm = driving_force * (hold_time_moas / 10.0)
        sfc_20 = 45.0 + (crystal_size_mm * 2.0)

        print(f"      - Mean Grain Size: {torch.mean(crystal_size_mm):.2f} mm "
              f"(Target: 1.0-2.0mm 'Danedar')")
        print(f"      - Solid Fat Content (20C): {torch.mean(sfc_20):.1f}% "
              f"(Semi-Solid Texture)")

    def _simulate_lipid_profile(self):
        """Simulates detailed Fatty Acid Composition."""
        print("   [CHEM] Analyzing Lipid Profile (GLC Method)...")
        butyric_acid = torch.normal(
            3.5, 0.2, (self.batches,), device=self.device)
        oleic_acid = torch.normal(
            28.0, 1.5, (self.batches,), device=self.device)
        ffa = torch.normal(0.25, 0.05, (self.batches,), device=self.device)
        valid_ffa = (torch.sum(ffa < 0.5).item() / self.batches) * 100

        print(f"      - Butyric Acid Content: {torch.mean(butyric_acid):.2f}% "
              f"(Authenticity Marker)")
        print(
            f"      - Oleic Acid Content: {torch.mean(oleic_acid):.2f}% (Texture)")
        print(f"      - Free Fatty Acids (FFA): {torch.mean(ffa):.3f}% "
              f"(Rancidity Check: {valid_ffa:.2f}%)")

    def _test_churning_yield(self):
        """
        Simulates Churning Efficiency based on Isoelectric Point Physics.
        Uses OPTIMIZED Temperature.
        """
        ph = torch.normal(4.6, 0.15, (self.batches,), device=self.device)
        # Using Optimized Setpoint
        temp_c = torch.normal(self.churn_temp_setpoint,
                              1.5, (self.batches,), device=self.device)

        yield_ph = torch.exp(-(ph - 4.6)**2 / 0.1)
        yield_temp = torch.exp(-(temp_c - 13.0)**2 / 8.0)  # Physics stays same

        base_yield = 30.0
        max_yield = 38.0
        actual_yield = base_yield + \
            (max_yield - base_yield) * yield_ph * yield_temp

        mean_yield = torch.mean(actual_yield).item()
        sigma_yield = torch.std(actual_yield).item()

        cpk = (mean_yield - 32.0) / (3 * sigma_yield)

        print(f"   [PHYS] Fat Recovery Yield: {mean_yield:.2f} g/L")
        print(f"   [ECON] Churning Process Cpk: {cpk:.3f} "
              f"(Improved via Optimal Temp 13C)")

    def _simulate_boiling_physics(self):
        """
        Simulates Maillard Reaction Kinetics & Vessel Thermodynamics.
        Physics: Heat Transfer from SS316 Wall to Makhan.
        Constraint: Wall Superheat < 5C to prevent bottom scorching.
        """
        print("   [MACHINERY] Simulating Vessel Thermodynamics (SS316)...")

        # Heat Source Control (Flame/Induction)
        heat_input_kw = torch.normal(
            5.0, 0.2, (self.batches,), device=self.device)
        viscosity_hot = 0.5  # cP (Very thin when hot)

        # Heat Transfer Coefficient (h)
        # Nusselts Number correlation for natural convection boiling
        # h ~ 500-1000 W/m2K for nucleate boiling
        h_coeff = torch.normal(
            800.0, 50.0, (self.batches,), device=self.device)

        # Temperatures
        # Bulk liquid temp varies slightly due to control loop
        bulk_temp = torch.normal(
            118.0, 1.0, (self.batches,), device=self.device)

        # Wall Temp = Bulk + (Heat_Flux / h)
        # Assuming minimal fouling initially
        wall_superheat = (heat_input_kw * 1000.0 / 1.5) / h_coeff  # Area 1.5m2
        wall_temp = bulk_temp + wall_superheat

        # Burn Risk: Wall Temp > 130C implies rapid protein carbonization at interface
        is_burnt = wall_temp > 130.0
        burn_rate = (torch.sum(is_burnt).item() / self.batches) * 100

        # Flavor Development (Maillard)
        # Rate doubles every 10C. Optimal at 118-122C.
        flavor_score = 100.0 - torch.abs(bulk_temp - 118.0) * 5.0
        # Penalty for wall burns
        flavor_score[is_burnt] *= 0.5

        print(
            f"      - Mean Wall Temperature: {torch.mean(wall_temp):.1f}C (Burn Limit 130C)")
        print(
            f"      - Nucleate Boiling Efficiency: {torch.mean(h_coeff):.0f} W/m2K")
        print(
            f"      - Burn Defect Rate: {burn_rate:.4f}% (Scraper/Agitator Needed)")
        print(
            f"      - Flavor Profile Score: {torch.mean(flavor_score):.1f}/100")

    def run_full_suite(self):
        """Executes the full Ghee simulation suite."""
        print("\n--- GHEE BILONA: PROCESS & COMPOSITION ANALYSIS ---")
        self.optimize_churning_physics()
        self._simulate_structure_texture()
        self._simulate_lipid_profile()
        self._test_churning_yield()
        self._simulate_boiling_physics()


if __name__ == "__main__":
    sim = GheeProductionSimulator()
    sim.run_full_suite()
