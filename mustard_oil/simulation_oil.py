"""
Simulation for Mustard Oil manufacturing.
Focus:
1. Blending economics & Pungency.
2. Oxidative Stability (Rancimat).
3. Fatty Acid Composition (Nutritional Profile involved with Heart Health).
4. Detailed Sensory & Viscosity Mimicry.
"""
import torch


class MustardOilLabSimulator:
    """
    Simulates Blending, Stability, and Full Nutritional Profile.
    """

    def __init__(self, batches=1_000_000):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        self.batches = batches
        print(f"Mustard Oil R&D Engine Initialized on {self.device}")

    def run_full_suite(self):
        """Executes the full simulation suite."""
        print("\n--- MUSTARD OIL: QUALITY & NUTRITION ANALYSIS ---")
        self._simulate_cold_press_mechanics()
        self._simulate_sensory_viscosity()
        self._simulate_fatty_acid_profile()
        self._test_pungency_aitc()
        self._simulate_rancimat()

    def _simulate_cold_press_mechanics(self):
        """
        Simulates Cold Press Extraction (Kachi Ghani).
        Physics: Friction Heat Generation vs Cooling Rate.
        Constraint: Temp < 45C (True Cold Press).
        Material: Wood/SS304 Friction Coefficient.
        """
        print("   [MACHINERY] Simulating Cold Press Extraction Physics...")

        # Machine Parameters (Wooden vs SS Ghani - User Prefers Wood/Cold Press)
        # Slow RPM for minimal heat
        rpm = torch.normal(12.0, 1.5, (self.batches,), device=self.device)
        pressure_bar = torch.normal(
            250.0, 20.0, (self.batches,), device=self.device)

        # Friction Heat Generation (Q_gen = mu * P * v)
        # Using Wooden Pestle Friction (Higher Torque, Lower Heat Transfer)
        ambient_temp = 28.0
        friction_coeff = 0.35  # Wood on Seed
        heat_gen_factor = (rpm * pressure_bar * friction_coeff) / \
            100.0  # Watts approx per unit mass flow
        cooling_capacity = 2.0  # Natural convection + Water Jacket (if any)

        exit_temp = ambient_temp + (heat_gen_factor / cooling_capacity)

        # Critical Limit: 50C (Enzyme Deactivation / Flavor Loss / Non-Cold Press)
        is_burnt = exit_temp > 50.0
        is_cold_pressed = exit_temp < 45.0

        cold_press_rate = (
            torch.sum(is_cold_pressed).item() / self.batches) * 100
        burn_rate = (torch.sum(is_burnt).item() / self.batches) * 100

        print(
            f"      - Mean Press Temperature: {torch.mean(exit_temp):.1f}C (Limit < 45C)")
        print(
            f"      - Cold Press Compliance: {cold_press_rate:.2f}% (True Kachi Ghani)")
        print(
            f"      - Burn Defect Rate: {burn_rate:.4f}% (RPM Control Vital)")

    def _simulate_sensory_viscosity(self):
        """
        Simulates Viscosity (Mouthfeel) and Nitrogen Sparging (Taste Preservation).
        """
        print("   [SENS] Simulating Mouthfeel & Taste Preservation...")

        # 1. VISCOSITY MATCHING
        # Mustard Oil Viscosity ~ 50 cP at 20C. RBO ~ 55 cP.
        # Blend (80% RBO) will be slightly thicker, which consumers perceive as "richer".
        rbo_visc = torch.normal(55.0, 2.0, (self.batches,), device=self.device)
        mustard_visc = torch.normal(
            50.0, 1.5, (self.batches,), device=self.device)

        # Arrhenius Mixing Rule: ln(mix) = x1 ln(v1) + x2 ln(v2)
        log_mix = (0.8 * torch.log(rbo_visc)) + (0.2 * torch.log(mustard_visc))
        final_visc = torch.exp(log_mix)

        # 2. NITROGEN SPARGING (Dissolved Oxygen Removal)
        # Prevents off-flavors (Peroxides) without synthetic antioxidants like TBHQ.
        initial_do = torch.normal(
            8.0, 1.0, (self.batches,), device=self.device)  # ppm Dissolved O2
        sparging_efficiency = torch.normal(
            0.95, 0.02, (self.batches,), device=self.device)  # 95% removal

        final_do = initial_do * (1.0 - sparging_efficiency)

        # Oxidative risk factor (Taste degradation)
        taste_integrity = 100.0 - (final_do * 10.0)  # Penalty for high oxygen

        print(
            f"      - Viscosity (20C): {torch.mean(final_visc):.1f} cP (Rich Mouthfeel)")
        print(
            f"      - Dissolved Oxygen: {torch.mean(final_do):.2f} ppm (Target < 0.5 ppm)")
        print(
            f"      - Taste Integrity Score: {torch.mean(taste_integrity):.1f}/100 (No Rancidity)")

    def _simulate_fatty_acid_profile(self):
        """Simulates GC-FID Analysis for Fatty Acids."""
        print("   [CHEM] Analyzing Lipid Profile (SFA/MUFA/PUFA & Erucic Acid)...")

        erucic_mustard = torch.normal(
            45.0, 2.0, (self.batches,), device=self.device)
        noise = torch.normal(0.0, 1.0, (self.batches,), device=self.device)
        final_sfa = (0.2 * 4.0) + (0.8 * 20.0) + noise
        final_mufa = (0.2 * 60.0) + (0.8 * 40.0)
        final_erucic = 0.2 * erucic_mustard
        final_oryzanol = torch.normal(
            10000.0, 500.0, (self.batches,), device=self.device) * 0.8

        safe_erucic = (torch.sum(final_erucic < 10.0).item() /
                       self.batches) * 100

        print(
            f"      - Erucic Acid: {torch.mean(final_erucic):.2f}% (Safety: {safe_erucic:.2f}%)")
        print(
            f"      - Gamma Oryzanol: {torch.mean(final_oryzanol):.0f} ppm (Natural Antioxidant)")
        print(
            f"      - Lipid Profile (SFA/MUFA): {torch.mean(final_sfa):.1f}% / {final_mufa:.1f}%")

    def _test_pungency_aitc(self):
        """Simulates AITC levels."""
        mustard_fraction = 0.20
        eo_ppm = torch.normal(
            14000.0, 500.0, (self.batches,), device=self.device)

        base_aitc = mustard_fraction * 0.5
        eo_aitc_contribution = (eo_ppm / 10000.0) * 0.25
        total_aitc_pct = base_aitc + eo_aitc_contribution

        usl = 0.50
        lsl = 0.40
        mean = torch.mean(total_aitc_pct).item()
        sigma = torch.std(total_aitc_pct).item()
        cpk = min((usl - mean)/(3*sigma), (mean - lsl)/(3*sigma))

        print(f"   [CHEM] AITC Pungency: {mean*100:.3f}% (Target 0.45%)")
        print(f"   [QUAL] Pungency Cpk: {cpk:.3f}")

    def _simulate_rancimat(self):
        """
        Simulates Induction Time (Shelf Life).
        Nitrogen Sparging extends shelf life.
        """
        # Nitrogen reduces Dissolved Oxygen (DO)
        nitrogen_sparge_efficiency = torch.normal(
            0.95, 0.02, (self.batches,), device=self.device)
        initial_do = 8.0  # ppm
        final_do = initial_do * (1.0 - nitrogen_sparge_efficiency)

        # Arrhenius eq for Oxidation
        temp = 110.0  # Rancimat Temp (Accelerated)
        base_induction = 12.0  # Hours
        # Lower DO = Higher Induction
        induction_time = base_induction / (final_do + 0.1) * 0.5

        print(f"   [PHYS] Induction Time: {torch.mean(induction_time):.2f} hours "
              f"(Shelf Life > 12M: {torch.sum(induction_time > 10.0).item()/self.batches*100:.1f}%)")


if __name__ == "__main__":
    sim = MustardOilLabSimulator()
    sim.run_full_suite()
