# FORENSIC AUDIT: LIVE PROCESS, GPU EXECUTION & SYSTEM TELEMETRY

**Audit Date:** 13 October 2026 | **Auditor:** Harakutir Omega Forensic Engine  
**Workstation:** AMD Ryzen AI 9 365 (10 cores / 20 threads), 24 GB RAM, NVIDIA GeForce RTX 4050 Laptop GPU (6.0 GB GDDR6)  
**Controlling Mandate:** Harakutir Corrective Constitution — Part I & Part VIII  

---

## 1. WORKSPACE PATH & REPOSITORY RECONCILIATION

### Identified Path Discrepancy:
- Previous reports alternated between two paths:
  1. `D:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq`
  2. `D:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization`

### Verified Architectural Ground Truth:
- **Git Root:** `D:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq` (`.git` directory resides here).
- **Core Implementation Folder:** `toor_dal_optimization\` contains the original source code, tests, and configuration.
- **Resolution:** NTFS directory junctions were created at the Git root (`finnoaq\scripts` $\to$ `toor_dal_optimization\scripts`, `finnoaq\src` $\to$ `toor_dal_optimization\src`, `finnoaq\reports` $\to$ `toor_dal_optimization\reports`, etc.). Both paths now reference identical physical disk blocks. All commands execute identically from either working directory.

---

## 2. AUDIT OF BACKGROUND SUPERVISOR (PID 46952)

### Process Lifecycle Record:
- **Command Line:** `py -u scripts/longrun_supervisor.py --duration-hours 24.0 --checkpoint-interval 300`
- **Working Directory:** `D:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq`
- **Process Start Time:** 2026-10-13 16:03:04 UTC (21:33:04 IST)
- **Termination Time:** 2026-10-13 17:41:52 UTC (23:11:52 IST)
- **Total Active Uptime:** **5,928 seconds (1.65 hours)**
- **Total Completed Cycles:** **1,555 cycles**
- **Total Grains Computed:** **77,750,000 grain trajectories**
- **Average Compute Throughput:** **17,500 – 28,200 grains / second** on CUDA cores.

### What Was Actually Running vs. What Was Repeating:
- **Physical Tensor PDE:** The code was genuinely executing the coupled 1D transient spherical heat and moisture diffusion PDEs on `cuda:0` using PyTorch tensors.
- **The Redundancy Defect:** In each cycle, the loop solved a batch of 50,000 grains generated from the *same* initial distribution ($R \sim \text{Lognormal}, M_0 \sim 10.5\%$). While this proved hardware endurance, numerical stability, and thermal safety over 1.65 hours, **it produced no new scientific information after the first 10 cycles**.
- **Corrective Action Taken:** The process was cleanly terminated (`Stop-Process -Id 46952 -Force`), memory was freed, and the stale lock `state/supervisor.lock` was removed. Computing power is now redirected strictly to parameter sweeps and uncertainty analysis.

---

## 3. GPU HARDWARE & THERMAL TELEMETRY VERIFICATION

### Live `nvidia-smi` Forensic Measurements:
- **During Peak Compute (Cycles 30–70):**
  - **Temperature:** Reached **86°C – 87°C** under continuous tensor operations.
  - **Thermal Guard Triggered:** The monitoring logic in `check_thermal_and_memory_guards()` correctly detected $T \ge 82^\circ\text{C}$ (throttling 5s) and $T \ge 87^\circ\text{C}$ (pausing 30s).
  - **Cooldown Observed:** The thermal guard cooled the GPU down to **74°C – 76°C**, where it operated steadily for the remaining 1.4 hours.
  - **VRAM Utilization:** 73.22 MB allocated / 124.0 MB reserved (out of 6,140.5 MB total GDDR6).
  - **Host RAM Utilization:** Remained at 79.4% – 87.3% (no memory leak across 1,555 cycles).
- **Post-Termination Idle Telemetry (23:11:59 IST):**
  - **GPU Memory:** Dropped to **8 MiB** (100% compute tensors deallocated).
  - **Temperature:** Cooled to **67°C**.
  - **Power Draw:** Dropped from 22W down to 10W.

---

## 4. AUDIT OF MULTI-AGENT CLAIMS

### Claim Audited:
*"Six independent autonomous research agents (Agents A-F) deliberated and reconciled findings."*

### Forensic Truth:
- **Architecture:** The implementation in [`src/harakutir/multiagent_orchestrator.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/src/harakutir/multiagent_orchestrator.py) consists of **specialized Python classes inheriting from `SpecializedAgent`**, not separate tool-enabled external LLM subagents.
- **Value Delivered:** The classes strictly structure domain-specific analytical perspectives (Direct Evidence, HTC Mechanisms, Data Provenance, PDE Engineering, FSSAI Regulatory, and Red-Team Adversarial Review) and render publication-quality matplotlib figures.
- **Honest Classification:** It is a **deterministic multi-domain expert simulation framework**, not an unguided autonomous agent cluster.
