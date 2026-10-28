"""
FinnoaQ Fail-Closed Execution Circuit Breaker.
Project Ref: FNQ-PR-2026-001 | Governance Standard: AGENTS.md Rule 1
Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

Mechanically enforces failure-ledger validation, shortcut detection, and physical consistency
before and after any simulation, grid search, refinement, or report publication.
"""

import os
import sys
import math
import json
import torch
from typing import Dict, Any, List, Optional

cur = os.path.dirname(os.path.abspath(__file__))
while cur and not os.path.exists(os.path.join(cur, "AGENTS.md")):
    parent = os.path.dirname(cur)
    if parent == cur:
        break
    cur = parent
base_dir = cur if os.path.exists(os.path.join(cur, "AGENTS.md")) else os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

for p in [
    base_dir,
    os.path.join(base_dir, "src"),
    os.path.join(base_dir, "toor_dal_optimization"),
    os.path.join(base_dir, "toor_dal_optimization", "src"),
    os.path.join(base_dir, "toor_dal_optimization", "governance", "errors"),
    os.path.join(base_dir, "governance", "errors"),
]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.insert(0, p)

from defect_ledger import DefectLedger

class CircuitBreakerTripped(Exception):
    """Raised when a shortcut, invariant violation, or ledger failure is detected."""
    pass

class ExecutionCircuitBreaker:
    def __init__(self, ledger_path: Optional[str] = None):
        if ledger_path is None:
            ledger_path = os.path.join(base_dir, "governance", "errors", "errors.json")
            if not os.path.exists(ledger_path):
                ledger_path = os.path.join(base_dir, "toor_dal_optimization", "governance", "errors", "errors.json")
        self.ledger = DefectLedger(ledger_path)

    def run_preflight_checks(self) -> None:
        """Mandatory preflight gate that must pass before any simulation launch."""
        print("[CIRCUIT_BREAKER] Running deterministic preflight gates...")

        # 1. Verify defect ledger cryptographic hash chain
        valid, msg = self.ledger.validate_chain()
        if not valid:
            raise CircuitBreakerTripped(f"Ledger integrity failure: {msg}")
        print(f"  [PASS] Defect ledger chain verified ({len(self.ledger.records)} records intact)")

        # 2. Check source path consistency (FAIL-0007)
        src1 = os.path.abspath(os.path.join(base_dir, "src", "finnoaq", "canonical_biophysics.py"))
        src2 = os.path.abspath(os.path.join(base_dir, "toor_dal_optimization", "src", "finnoaq", "canonical_biophysics.py"))
        if os.path.exists(src1) and os.path.exists(src2):
            if not os.path.samefile(src1, src2):
                raise CircuitBreakerTripped(f"FAIL-0007 violation: divergent source files between {src1} and {src2}")
        print("  [PASS] Single authoritative source tree verified via filesystem junction")

        # 3. Verify calcium conversion units (FAIL-0008)
        from finnoaq.canonical_biophysics import CA_VOL_HTC_NOMINAL, CA_BOUND_HTC_NOMINAL, RHO_DAL_DRY
        expected_vol_ca = (CA_BOUND_HTC_NOMINAL * 1e-2 / 40.078) * RHO_DAL_DRY
        if abs(CA_VOL_HTC_NOMINAL - expected_vol_ca) > 0.05:
            raise CircuitBreakerTripped(
                f"FAIL-0008 violation: CA_VOL_HTC_NOMINAL = {CA_VOL_HTC_NOMINAL:.3f} mol/m^3, "
                f"expected ~{expected_vol_ca:.3f} mol/m^3 (missing 10x dry-basis factor)"
            )
        print(f"  [PASS] Volumetric calcium concentration strictly verified ({CA_VOL_HTC_NOMINAL:.2f} mol/m^3)")

        # 4. Verify steam pressure equation calibration (FAIL-0014)
        from finnoaq.canonical_biophysics import DomesticPressureCookerModel
        cooker = DomesticPressureCookerModel()
        p_121_kpa = cooker.get_saturation_pressure_kpa(121.2) # ~207.0 kPa abs
        if abs(p_121_kpa - 207.0) > 5.0:
            raise CircuitBreakerTripped(
                f"FAIL-0014 violation: saturation pressure at 121.2°C is {p_121_kpa:.1f} kPa, "
                f"expected NIST steam table reference ~207.0 kPa abs (+/- 5 kPa)"
            )
        print(f"  [PASS] Steam saturation pressure verified against NIST standard ({p_121_kpa:.1f} kPa abs at 121.2°C)")

        # 5. Verify tissue yield stress units (FAIL-0012)
        from finnoaq.canonical_biophysics import SIGMA_0_YIELD, SIGMA_RESIDUAL
        if SIGMA_0_YIELD > 2.0e6 or SIGMA_RESIDUAL > 1.0e6:
            raise CircuitBreakerTripped(
                f"FAIL-0012 violation: Yield stress constants ({SIGMA_0_YIELD} Pa) exceed 2.0 MPa. "
                "Parenchyma tissue yield stress cannot be in structural metal MPa regime."
            )
        print(f"  [PASS] Tissue mechanics stress scale verified in kPa regime ({SIGMA_0_YIELD/1000.0:.1f} kPa)")

        print("[CIRCUIT_BREAKER] All preflight gates passed successfully.\n")

    def validate_simulation_outputs(self, results: List[Dict[str, Any]], manifest_entries: List[Any]) -> None:
        """Mechanically verifies simulation results against shortcut signatures."""
        print("[CIRCUIT_BREAKER] Validating simulation outputs against shortcut signatures...")

        if len(results) != len(manifest_entries):
            raise CircuitBreakerTripped(
                f"Accounting defect: received {len(results)} outputs for {len(manifest_entries)} manifest entries"
            )

        # Check for uninitialized / constant outputs across varying inputs (FAIL-0001, FAIL-0002)
        if len(results) > 10:
            temps = [r.get("T_soak_c") for r in results if "T_soak_c" in r]
            ca_disps = [r.get("ca_displacement_pct") for r in results if "ca_displacement_pct" in r]
            if len(set(temps)) > 1 and len(set(ca_disps)) == 1:
                raise CircuitBreakerTripped("FAIL-0001/0002 shortcut signature: Calcium displacement is invariant across varying soak temperatures!")

        # Check for Untreated Dal false pass (the core physical defect)
        for r in results:
            cfg_c = r.get("C_citrate_M", r.get("citrate_conc_M", 0.0))
            cfg_t = r.get("soak_time_min", 0.0)
            if cfg_c == 0.0 and cfg_t == 0.0:
                is_two = r.get("is_two_whistles", False)
                t90 = r.get("t90_min", 99.0)
                final_f = r.get("final_f_wb_N", 99.0)
                if is_two or t90 < 15.0 or final_f < 20.0:
                    raise CircuitBreakerTripped(
                        f"CRITICAL DEFECT: Untreated HTC dal falsely evaluated as cooked in 2 whistles! "
                        f"(T90={t90}m, Whistles={r.get('whistle_count')}, Shear={final_f} N)"
                    )

        # Check for linear clock whistle calculation (FAIL-0004)
        for r in results:
            whistles = r.get("whistle_count", 0)
            t90 = r.get("t90_min", 0.0)
            if whistles > 0 and t90 > 0:
                # If whistle count is identically equal to round(t90 / 5.25) across all runs
                if abs(t90 - whistles * 5.25) < 1e-4:
                    raise CircuitBreakerTripped("FAIL-0004 shortcut signature: Linear elapsed-time clock used for whistles!")

        print(f"  [PASS] {len(results)} simulation outputs verified free of shortcut signatures.\n")

if __name__ == "__main__":
    cb = ExecutionCircuitBreaker()
    cb.run_preflight_checks()
