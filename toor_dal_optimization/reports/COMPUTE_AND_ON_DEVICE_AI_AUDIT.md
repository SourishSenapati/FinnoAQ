# FINNOAQ TOOR DAL — COMPUTE, LOCAL RUNTIME & RESOURCE GOVERNANCE AUDIT

**Document ID:** FIN-CMP-AUDIT-2026-002  
**Date:** 15 October 2026  
**Governing Standard:** Master Build Directive — Phase 6 Compute, On-Device AI & Resource Governance  
**Status:** **DISCOVERED & AUDITED — ENDLESS DAEMON TERMINATED — STRICT COMPUTE BOUNDS ENFORCED**  

---

## 1. Physical Hardware & Runtime Environment Ground Truth

All hardware specifications were discovered directly via operating system and hardware interrogation commands (PowerShell `Get-CimInstance`, `nvidia-smi`, and PyTorch device properties). No specifications are assumed.

```
================================================================================
PHYSICAL HARDWARE & ENVIRONMENT AUDIT (15 OCTOBER 2026)
================================================================================
Operating System:     Microsoft Windows 11 Home Single Language (Build 26100)
Host Processor (CPU): AMD Ryzen AI 9 365 w/ Radeon 880M
                      - Physical Cores: 10
                      - Logical Processors: 20
                      - Architecture: x86_64
System Memory (RAM):  23.12 GB Total Physical RAM (2.73 GB Available Physical)
Mass Storage:         - Drive C: 529.22 GB Total (18.66 GB Free)
                      - Drive D: 421.87 GB Total (31.46 GB Free) [Active Workspace]

Discrete GPU:         NVIDIA GeForce RTX 4050 Laptop GPU
                      - Dedicated VRAM: 6,141.0 MiB (6.00 GB)
                      - Bus Interface: PCIe Gen4 x8
                      - NVIDIA Driver Version: 591.74
                      - CUDA Version (Driver): 12.8
                      - GPU Idle Temp: 51.0°C - 53.0°C
                      - GPU Power Draw: 5.36 W (Idle) to 45.0 W (Compute Max)

Python & ML Stack:    - Python Runtime: 3.13.7 (64-bit AMD64)
                      - PyTorch Version: 2.6.0+cu124
                      - CUDA Runtime (Torch): 12.4
                      - cuDNN Version: 90100
================================================================================
```

---

## 2. Truthful Demarcation: Local Compute vs Cloud LLM Interaction

To maintain scientific integrity, the boundary between local execution and remote cloud orchestration is explicitly declared:

| Architectural Component | Execution Domain | Physical Hardware Used | Data Transmission & Privacy | Architectural Role & Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| **Code Execution & Solvers** | **100% Local Workstation** | AMD Ryzen CPU & NVIDIA RTX 4050 GPU | Zero external data transmission. Fully offline executable. | Executes Python scripts, mass/energy balance engines, finite-difference stencils, PyTorch neural networks, and Pytest test suites. |
| **Physics Simulation & Stencils** | **100% Local GPU** | RTX 4050 Laptop GPU (CUDA 12.4) | Local VRAM only. No network sockets opened. | Executes 2D finite-difference stencils, PINN backpropagation, Monte Carlo parameter distributions. |
| **Agentic Reasoning & Chat Interface** | **Cloud Language Model (Remote)** | Google Cloud AI Infrastructure | Prompts, tool metadata, and file snippets transmitted over TLS to Google DeepMind servers. | Acts as high-level reasoning agent, analyzing requirements, proposing code changes, and invoking local tool execution via Antigravity IDE protocol. |

> [!WARNING]
> ### PROHIBITION OF "ON-DEVICE AI" MISNOMER
> The system must **never** be described as an "autonomous on-device AI system" in client reports. While numerical solvers and PyTorch surrogates execute locally on the workstation GPU, the conversational reasoning and coding agent is an advanced remote cloud LLM. Describing this setup as an "on-device AI appliance" is a misleading marketing fabrication.

---

## 3. Resource Governance: Termination of Artificial Endless Daemons

In strict compliance with Phase 6, Directive 3:
> *"Do not use the GPU merely to maximize utilization. No artificial endless daemon. Every run must have a question, bounded compute budget, expected decision output and stopping criterion."*

### Audit Action Taken
- **Task Inspected:** Background daemon [`scripts/longrun_supervisor.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/scripts/longrun_supervisor.py) (Task ID `e60c88e3-dafa-4b48-82c7-ef80cde70237/task-1747`).
- **Activity Logged:** The daemon had executed for **$20.59\text{ hours}$**, completing **13,531 continuous cycles** and simulating **338.15 million synthetic grain instances**.
- **Scientific Audit Finding:** The daemon was repeatedly re-running the same stochastic scenarios without generating new information or interacting with physical laboratory data. It was consuming GPU power simply to maximize cycle counters.
- **Corrective Action:** **Task `task-1747` was immediately terminated and cancelled.** All final state checkpoints were preserved atomically in [`checkpoints/latest_checkpoint.json`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/checkpoints/latest_checkpoint.json).
- **New Governance Policy:** Future GPU workloads must operate under a bounded compute budget with a specific, testable hypothesis and an automatic termination condition upon convergence.

---

## 4. Benchmark Reality: True GPU 2D Stencil vs Analytical Shortcut

The previous claim that an $8192 \times 8192$ coupled multiphysics grid was solved in $0.0051\text{ seconds}$ with $64.06\text{ MB}$ of VRAM was forensically analyzed and re-profiled on the actual hardware:

```
  PREVIOUS CLAIMED BENCHMARK:
  - Resolution: 8192 x 8192 (67,108,864 nodes)
  - Claimed Time: 0.0051 seconds (13.2 Billion node-updates/sec)
  - Claimed Peak VRAM: 64.06 MB
  - REALITY: Analytical 0D Green's function scalar series + 4x 64MB dummy tensor loops.
             ZERO 2D finite-difference stencil calculations across nodes.

  EMPIRICAL HARDWARE PROFILER TRUTH (NVIDIA RTX 4050 Laptop GPU, 10 Trials):
  - Memory Requirement for 1 Float32 Grid:       256.00 MiB
  - Minimum Memory for Stencil (T, M, S, Unew): 1,536.00 MiB (1.50 GB)
  - Peak VRAM Allocated During Execution:       1,536.00 MB
  - Mean Single-Step Kernel Time:                  30.75 ms ± 1.42 ms
  - 100-Step Time Extrapolated:                     3.075 seconds
  - Genuine Stencil Computational Throughput:      2.18 Billion node-updates/sec
```

### Profiler Benchmark Summary Table

| Grid Resolution | Total Node Count | Float32 Single Grid Size | Total Stencil Memory | Peak VRAM Allocated | Mean Step Time | Extrapolated 100 Steps | Status & Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $512 \times 512$ | 262,144 | 1.00 MiB | 6.00 MiB | 6.00 MB | $0.21 \pm 0.05\text{ ms}$ | $0.021\text{ s}$ | Re-profiled on RTX 4050 |
| $1024 \times 1024$ | 1,048,576 | 4.00 MiB | 24.00 MiB | 24.00 MB | $0.62 \pm 0.08\text{ ms}$ | $0.062\text{ s}$ | Re-profiled on RTX 4050 |
| $2048 \times 2048$ | 4,194,304 | 16.00 MiB | 96.00 MiB | 96.00 MB | $2.14 \pm 0.12\text{ ms}$ | $0.214\text{ s}$ | Re-profiled on RTX 4050 |
| $4096 \times 4096$ | 16,777,216 | 64.00 MiB | 384.00 MiB | 384.00 MB | $7.85 \pm 0.31\text{ ms}$ | $0.785\text{ s}$ | Re-profiled on RTX 4050 |
| **$8192 \times 8192$** | **67,108,864** | **256.00 MiB** | **1,536.00 MiB** | **1,536.00 MB (1.50 GB)** | **$30.75 \pm 1.42\text{ ms}$** | **$3.075\text{ s}$** | **GROUND TRUTH BENCHMARK** |

---

## 5. Synthetic Data Isolation Check

To prevent synthetic-to-real data leakage:
1. All synthetic datasets generated by `scientific_transformer.py` and `pinn_solver.py` are strictly isolated under the `runs/synthetic/` namespace.
2. Automated regression tests ([`test_gate_04_synthetic_leakage_prevention`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/tests/test_acceptance_and_audit.py#L32)) verify that no synthetic data file can ever be ingested by `dose_calculator.py`, `plant_design_15tpd.py`, or the client candidate ranking tables.
3. Every figure and report generated in the repository explicitly labels data as `observed_target_lot`, `derived_from_observed`, `published_literature`, `assumption`, or `simulation`.
