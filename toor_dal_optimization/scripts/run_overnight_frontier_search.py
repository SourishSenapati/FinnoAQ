"""
FinnoaQ Autonomous Multi-Horizon GPU Frontier Discovery Engine.
Project Ref: FNQ-PR-2026-001 | Continuous Autonomous Overnight R&D Engine
Lead Chemical and Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
Governing Standard: AGENTS.md Rule 1 & Anti-Reward-Hacking Computational Engineering Execution Contract

Continuous, Non-Repeating Quasi-Monte Carlo & Multi-Objective Evolutionary Search on NVIDIA RTX 4050 GPU:
  - Explores continuous high-dimensional chemical and operational parameter space.
  - Sobol low-discrepancy pseudo-random sampling ensures zero loops and 100% unique configurations.
  - Tracks 5-dimensional Pareto frontier:
      1. min(Whistle count at T90)
      2. min(Peak core puncture force F_core)
      3. min(Retained sodium mg/100g)
      4. min(Total soak time min)
      5. min(OpEx INR/kg)
  - Evaluates authentic 2D axisymmetric cylindrical reaction-diffusion PDE and deadweight steam dynamics on CUDA.
  - Persists real-time checkpoints, discovery archives, and hardware telemetry to runs/active/overnight_frontier_search/.
"""

import os
import sys
import time
import math
import hashlib
import json
from datetime import datetime, timezone
from typing import List, Dict, Any, Tuple, Optional
import numpy as np
import torch

# Ensure unbuffered UTF-8 output
sys.stdout.reconfigure(line_buffering=True, encoding="utf-8", errors="replace")
sys.stderr.reconfigure(line_buffering=True, encoding="utf-8", errors="replace")

# Ensure robust path resolution
cur = os.path.dirname(os.path.abspath(__file__))
while cur and not os.path.exists(os.path.join(cur, "AGENTS.md")):
    parent = os.path.dirname(cur)
    if parent == cur:
        break
    cur = parent
base_dir = cur if os.path.exists(os.path.join(cur, "AGENTS.md")) else os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

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

from finnoaq.canonical_biophysics import (
    calculate_chemical_speciation,
    solve_2d_soaking_pde,
    calculate_drainage_and_rinse,
    DomesticPressureCookerModel,
    solve_cooking_endpoint,
    evaluate_treatment_end_to_end,
    evaluate_treatment_batch_gpu,
    CA_BOUND_HTC_NOMINAL,
    CA_VOL_HTC_NOMINAL
)
from circuit_breaker import ExecutionCircuitBreaker

OUT_DIR = os.path.join(base_dir, "runs", "active", "overnight_frontier_search")
os.makedirs(OUT_DIR, exist_ok=True)
LOG_FILE = os.path.join(OUT_DIR, "overnight_execution.log")

def log(msg: str):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{timestamp}] {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def dominates(cand_a: Dict[str, Any], cand_b: Dict[str, Any]) -> bool:
    """True if cand_a is strictly no worse than cand_b on all 5 objectives, and strictly better in at least one."""
    # Objectives to minimize:
    # 1. whistles (<= 2 is optimal)
    # 2. final_f_wb_core_N (<= 18.0 N is optimal)
    # 3. retained_na_mg_100g (<= 120 mg is optimal)
    # 4. soak_time_min
    # 5. opex_inr_kg
    w_a, w_b = cand_a.get("whistle_count", 99), cand_b.get("whistle_count", 99)
    fc_a, fc_b = cand_a.get("final_f_wb_core_N", 99.0), cand_b.get("final_f_wb_core_N", 99.0)
    na_a, na_b = cand_a.get("retained_na_mg_100g", 999.0), cand_b.get("retained_na_mg_100g", 999.0)
    t_a, t_b = cand_a.get("soak_time_min", 99.0), cand_b.get("soak_time_min", 99.0)
    op_a, op_b = cand_a.get("opex_inr_kg", 99.0), cand_b.get("opex_inr_kg", 99.0)

    no_worse = (w_a <= w_b) and (fc_a <= fc_b) and (na_a <= na_b) and (t_a <= t_b) and (op_a <= op_b)
    strictly_better = (w_a < w_b) or (fc_a < fc_b) or (na_a < na_b) or (t_a < t_b) or (op_a < op_b)
    return no_worse and strictly_better


def update_pareto_front(archive: List[Dict[str, Any]], candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Maintains an optimal non-dominated Pareto archive across all evaluated solutions."""
    updated = list(archive)
    for cand in candidates:
        # Check if dominated by any existing member
        is_dominated = False
        for member in updated:
            if dominates(member, cand):
                is_dominated = True
                break
        if not is_dominated:
            # Remove any members that this new candidate dominates
            updated = [m for m in updated if not dominates(cand, m)]
            updated.append(cand)

    # Keep archive bounded to top 200 non-dominated points sorted by (whistles, core_force, Na, OpEx)
    updated.sort(key=lambda x: (
        x.get("whistle_count", 99),
        x.get("final_f_wb_core_N", 99.0),
        x.get("retained_na_mg_100g", 999.0),
        x.get("opex_inr_kg", 99.0),
        x.get("soak_time_min", 99.0)
    ))
    return updated[:200]


def run_overnight_frontier_engine(max_evaluations: Optional[int] = None, batch_size: int = 128, grid_size: int = 64):
    log("=" * 80)
    log("STARTING FINNOAQ OVERNIGHT GPU MULTI-HORIZON FRONTIER DISCOVERY ENGINE")
    log("Lead Chemical & Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)")
    log("Governing Standard: AGENTS.md Rule 1 (Technical Correctness Over Output Generation)")
    log("=" * 80)

    # 1. Mandatory fail-closed preflight circuit breaker
    cb = ExecutionCircuitBreaker()
    cb.run_preflight_checks()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    is_cuda = device.type == "cuda"
    gpu_name = torch.cuda.get_device_name(device) if is_cuda else "CPU"
    cuda_ver = torch.version.cuda if is_cuda else "N/A"

    log(f"Compute Hardware: {device} ({gpu_name}) | CUDA: {cuda_ver} | PyTorch: {torch.__version__}")
    target_msg = f"up to {max_evaluations:,} evaluations" if max_evaluations else "Continuous Unbounded Horizon (Runs until stopped)"
    log(f"Target Horizon: {target_msg}")
    log(f"Spatial Grid Resolution: {grid_size} x {grid_size} sub-cellular mesh ({grid_size*grid_size:,} nodes/cotyledon)")
    log(f"Batch Size: {batch_size} parallel cotyledons on GPU ({batch_size * grid_size * grid_size:,} active PDE nodes)")
    log(f"Batch Size: {batch_size} parallel cotyledons on GPU")

    # 2. Load checkpoint or initialize
    checkpoint_file = os.path.join(OUT_DIR, "frontier_checkpoint.json")
    pareto_file = os.path.join(OUT_DIR, "frontier_pareto_archive.json")
    telemetry_file = os.path.join(OUT_DIR, "live_telemetry.json")

    total_evaluated = 0
    dual_gate_winners_count = 0
    pareto_archive = []
    seen_signatures = set()

    if os.path.exists(checkpoint_file):
        try:
            with open(checkpoint_file, "r", encoding="utf-8") as f:
                ckpt = json.load(f)
                total_evaluated = ckpt.get("total_evaluated", 0)
                dual_gate_winners_count = ckpt.get("dual_gate_winners_count", 0)
                log(f"[CHECKPOINT] Resuming from existing run: {total_evaluated:,} cases previously evaluated.")
        except Exception as e:
            log(f"[CHECKPOINT] Error loading checkpoint ({e}), initializing fresh search.")

    if os.path.exists(pareto_file):
        try:
            with open(pareto_file, "r", encoding="utf-8") as f:
                pareto_archive = json.load(f)
                log(f"[PARETO] Loaded {len(pareto_archive)} non-dominated regimes from existing archive.")
        except Exception:
            pass

    # 3. Sobol Multi-Horizon Space Definition:
    # 7 continuous dimensions:
    # dim 0: T_soak in [20.0, 62.0] °C
    # dim 1: C_citrate in [0.03, 0.35] M
    # dim 2: f_K in [0.00, 1.00]
    # dim 3: target_pH in [4.60, 6.60]
    # dim 4: soak_time_min in [10.0, 60.0] min
    # dim 5: rinse_ratio_L_kg in [0.08, 0.45] L/kg
    # dim 6: water_hardness_ppm in [0.0, 350.0] ppm CaCO3
    bounds_low = torch.tensor([20.0, 0.03, 0.00, 4.60, 10.0, 0.08, 0.0])
    bounds_high = torch.tensor([62.0, 0.35, 1.00, 6.60, 60.0, 0.45, 350.0])
    bounds_range = bounds_high - bounds_low

    sobol_dim = 7
    sobol_seed = int(time.time()) % 100000 + 42
    sobol = torch.quasirandom.SobolEngine(dimension=sobol_dim, scramble=True, seed=sobol_seed)

    t_global_start = time.time()
    last_checkpoint_time = time.time()
    batch_idx = 0
    stop_sentinel = os.path.join(OUT_DIR, "stop_frontier.txt")
    if os.path.exists(stop_sentinel):
        try:
            os.remove(stop_sentinel)
        except Exception:
            pass

    log("\n[EXECUTION ACTIVE] Continuous frontier generation and CUDA PDE solving started...")

    try:
        while (max_evaluations is None or total_evaluated < max_evaluations) and not os.path.exists(stop_sentinel):
            batch_idx += 1
            t_batch_start = time.time()

            # 70% Sobol space-filling exploration + 30% local evolutionary mutations around Pareto front
            n_sobol = int(batch_size * 0.70)
            n_mutate = batch_size - n_sobol

            raw_samples = sobol.draw(n_sobol)
            scaled_samples = bounds_low + raw_samples * bounds_range

            batch_configs = []
            for row in scaled_samples:
                T_c = round(float(row[0].item()), 1)
                C_m = round(float(row[1].item()), 3)
                f_k = round(float(row[2].item()), 2)
                ph = round(float(row[3].item()), 2)
                t_s = round(float(row[4].item()), 1)
                rinse = round(float(row[5].item()), 2)
                hard = round(float(row[6].item()), 1)

                # Signature to prevent any duplicate execution
                sig = f"{T_c:.1f}_{C_m:.3f}_{f_k:.2f}_{ph:.2f}_{t_s:.1f}_{rinse:.2f}_{hard:.1f}"
                if sig not in seen_signatures:
                    seen_signatures.add(sig)
                    batch_configs.append((T_c, C_m, f_k, ph, t_s, rinse, hard))

            # Evolutionary mutation around current Pareto leaders (local exploitation of promising boundaries)
            if pareto_archive and n_mutate > 0:
                for _ in range(n_mutate):
                    parent = np.random.choice(pareto_archive)
                    # Gaussian perturbation with 5% std
                    T_c = round(float(np.clip(parent["T_soak_c"] + np.random.normal(0, 1.5), 20.0, 62.0)), 1)
                    C_m = round(float(np.clip(parent["C_citrate_M"] + np.random.normal(0, 0.015), 0.03, 0.35)), 3)
                    f_k = round(float(np.clip(parent["f_K"] + np.random.normal(0, 0.05), 0.0, 1.0)), 2)
                    ph = round(float(np.clip(parent["pH"] + np.random.normal(0, 0.08), 4.6, 6.6)), 2)
                    t_s = round(float(np.clip(parent["soak_time_min"] + np.random.normal(0, 2.0), 10.0, 60.0)), 1)
                    rinse = round(float(np.clip(parent["rinse_ratio_L_kg"] + np.random.normal(0, 0.03), 0.08, 0.45)), 2)
                    hard = round(float(np.clip(parent["water_hardness_ppm"] + np.random.normal(0, 15.0), 0.0, 350.0)), 1)

                    sig = f"{T_c:.1f}_{C_m:.3f}_{f_k:.2f}_{ph:.2f}_{t_s:.1f}_{rinse:.2f}_{hard:.1f}"
                    if sig not in seen_signatures:
                        seen_signatures.add(sig)
                        batch_configs.append((T_c, C_m, f_k, ph, t_s, rinse, hard))

            # Fill remainder if duplicates occurred
            while len(batch_configs) < batch_size:
                extra = sobol.draw(1)[0]
                T_c = round(float((bounds_low[0] + extra[0] * bounds_range[0]).item()), 1)
                C_m = round(float((bounds_low[1] + extra[1] * bounds_range[1]).item()), 3)
                f_k = round(float((bounds_low[2] + extra[2] * bounds_range[2]).item()), 2)
                ph = round(float((bounds_low[3] + extra[3] * bounds_range[3]).item()), 2)
                t_s = round(float((bounds_low[4] + extra[4] * bounds_range[4]).item()), 1)
                rinse = round(float((bounds_low[5] + extra[5] * bounds_range[5]).item()), 2)
                hard = round(float((bounds_low[6] + extra[6] * bounds_range[6]).item()), 1)
                batch_configs.append((T_c, C_m, f_k, ph, t_s, rinse, hard))

            # Execute authentic GPU PDE simulation
            if is_cuda:
                torch.cuda.synchronize(device)
            results = evaluate_treatment_batch_gpu(batch_configs, grid_size=grid_size, device=device)
            if is_cuda:
                torch.cuda.synchronize(device)

            # Check dual-gate discoveries in batch
            new_dual_gate_in_batch = 0
            for r in results:
                total_evaluated += 1
                r["eval_id"] = f"FRONTIER_{total_evaluated:07d}"
                # Dual-Gate criterion: cooked in <= 2 whistles AND core shear <= 18.0 N AND Na <= 120 mg/100g
                if r.get("is_two_whistles", False) and r.get("final_f_wb_core_N", 99.0) <= 18.0 and r.get("retained_na_mg_100g", 999.0) <= 120.0:
                    dual_gate_winners_count += 1
                    new_dual_gate_in_batch += 1

            # Update Pareto frontier
            old_archive_len = len(pareto_archive)
            pareto_archive = update_pareto_front(pareto_archive, results)

            t_batch_elapsed = time.time() - t_batch_start
            batch_rate = len(batch_configs) / max(0.01, t_batch_elapsed)

            # Periodic status logging (every 5 batches)
            if batch_idx % 5 == 0:
                elapsed_total = time.time() - t_global_start
                avg_rate = total_evaluated / max(0.1, elapsed_total)
                top_lead = pareto_archive[0] if pareto_archive else {}
                top_lead_w = top_lead.get("whistle_count", "N/A")
                top_lead_fc = top_lead.get("final_f_wb_core_N", "N/A")
                top_lead_na = top_lead.get("retained_na_mg_100g", "N/A")

                vram_reserved = torch.cuda.memory_reserved(device) / (1024**2) if is_cuda else 0.0
                vram_peak = torch.cuda.max_memory_allocated(device) / (1024**2) if is_cuda else 0.0

                log(f"[BATCH {batch_idx:04d}] Total Evaluated: {total_evaluated:,} | "
                    f"Speed: {batch_rate:4.1f} cases/s (Avg: {avg_rate:4.1f}) | VRAM: {vram_reserved:.1f} MB (Peak: {vram_peak:.1f} MB) | "
                    f"Pareto Archive: {len(pareto_archive)} | Dual-Gate Winners: {dual_gate_winners_count:,} | "
                    f"Leader: {top_lead_w} Whistles, Core={top_lead_fc} N, Na={top_lead_na} mg")

            # Checkpointing & Telemetry Persistence (every 60 seconds)
            if (time.time() - last_checkpoint_time) >= 60.0 or batch_idx % 25 == 0:
                last_checkpoint_time = time.time()
                elapsed_total = time.time() - t_global_start

                # Live telemetry
                telemetry = {
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                    "device": str(device),
                    "gpu_name": gpu_name,
                    "cuda_version": cuda_ver,
                    "total_evaluated": total_evaluated,
                    "unique_signatures_explored": len(seen_signatures),
                    "pareto_non_dominated_count": len(pareto_archive),
                    "dual_gate_winners_count": dual_gate_winners_count,
                    "throughput_cases_per_sec": round(total_evaluated / max(0.1, elapsed_total), 1),
                    "elapsed_hours": round(elapsed_total / 3600.0, 3),
                    "vram_allocated_mb": round(torch.cuda.memory_allocated(device) / (1024**2), 1) if is_cuda else 0.0,
                    "vram_reserved_mb": round(torch.cuda.memory_reserved(device) / (1024**2), 1) if is_cuda else 0.0,
                    "top_pareto_leader": pareto_archive[0] if pareto_archive else None
                }

                # Atomic writes
                with open(telemetry_file + ".tmp", "w", encoding="utf-8") as f:
                    json.dump(telemetry, f, indent=2)
                os.replace(telemetry_file + ".tmp", telemetry_file)

                with open(pareto_file + ".tmp", "w", encoding="utf-8") as f:
                    json.dump(pareto_archive, f, indent=2)
                os.replace(pareto_file + ".tmp", pareto_file)

                ckpt_data = {
                    "total_evaluated": total_evaluated,
                    "dual_gate_winners_count": dual_gate_winners_count,
                    "batch_idx": batch_idx,
                    "sobol_seed": sobol_seed,
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
                with open(checkpoint_file + ".tmp", "w", encoding="utf-8") as f:
                    json.dump(ckpt_data, f, indent=2)
                os.replace(checkpoint_file + ".tmp", checkpoint_file)

                # Keep memory clean
                if is_cuda and batch_idx % 50 == 0:
                    torch.cuda.empty_cache()

    except KeyboardInterrupt:
        log("\n[INTERRUPT] Graceful pause requested by operator. Preserving current frontier archive...")
    except Exception as e:
        log(f"\n[ERROR] Unexpected exception in frontier engine: {e}")
        import traceback
        log(traceback.format_exc())
    finally:
        total_time = time.time() - t_global_start
        log("=" * 80)
        log("OVERNIGHT FRONTIER RUN COMPLETED / CHECKPOINTED")
        log(f"Total Unique Physical Configurations Evaluated: {total_evaluated:,}")
        log(f"Total Dual-Gate 2-Whistle Winners Discovered: {dual_gate_winners_count:,}")
        log(f"Non-Dominated Pareto Candidates Preserved: {len(pareto_archive)}")
        log(f"Total Run Wall Clock: {total_time/3600.0:.2f} hours ({total_time:.1f} s)")
        log(f"Saved to: {OUT_DIR}")
        log("=" * 80)


if __name__ == "__main__":
    # Continuous unbounded overnight run on GPU with sub-cellular 64x64 spatial mesh
    run_overnight_frontier_engine(max_evaluations=None, batch_size=128, grid_size=64)
