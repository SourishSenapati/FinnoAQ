# FINNOAQ SYSTEM RESUME & OPERATIONAL RUNBOOK
## Explicit Commands, Recovery Procedures, Hardware Benchmarks & Audit Protocols

**Document ID:** HKT-RUN-2026-014  
**Version:** 3.0.0  
**Target Shell:** PowerShell (Windows 11)  
**Python Runtime:** `C:\Python313\python.exe`  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Verified Operational Commands

All commands have been verified on the local Ryzen 9 + NVIDIA GeForce RTX 4050 workstation:

### 1.1 Full Autonomous Pipeline Execution
Runs the complete 10-phase autonomous cycle (probe, parameter extraction, data readiness, GPU diffusion PDE, Bayesian OED, Dream-RSI replay, 5-layer screening, Foodoscope digital twin, Harness gates, and deliverables):
```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 -Mode Run
# Equivalent direct Python command:
C:\Python313\python.exe scripts/run_supervisor.py --mode Run
```

### 1.2 Idempotent Checkpoint Resume
Safely reconciles `checkpoints/latest_checkpoint.json` and SQLite WAL event log in `state/journal.db`, continuing execution from the last committed phase:
```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 -Mode Resume
# Equivalent direct Python command:
C:\Python313\python.exe scripts/run_supervisor.py --mode Resume
```

### 1.3 Hardware Discovery & Offline GPU Benchmark Probe
Probes Ryzen 9 CPU, RAM, and detects NVIDIA GeForce RTX 4050 Laptop GPU, executing test matrix multiplication and VRAM allocation checks:
```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 -Mode Benchmark
# Equivalent direct Python command:
C:\Python313\python.exe scripts/run_supervisor.py --mode Benchmark
```

### 1.4 Comprehensive Acceptance Test Suite (18 Gates)
Executes all 18 automated contract gates, including synthetic data isolation, Peleg non-linear fitting, Foodoscope culinary kinetics, GPU inverse diffusion, and Harness decision gates:
```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 -Mode Test
# Equivalent direct Pytest command:
C:\Python313\python.exe -m pytest tests/test_acceptance_and_audit.py -v
```

### 1.5 Independent Red-Team Adversarial Audit
Runs the independent automated auditor, verifying that zero synthetic rows have leaked into real reports and evaluating all 18 contract gates:
```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 -Mode Audit
# Equivalent direct Python command:
C:\Python313\python.exe scripts/generate_audit_report.py
```

### 1.6 Wet Laboratory Data Ingestion Scan
Scans `inputs/` and `data/raw/` for newly arrived signed laboratory certificates, generating a refreshed data readiness report:
```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 -Mode Ingest
# Equivalent direct Python command:
C:\Python313\python.exe scripts/run_supervisor.py --mode Ingest
```

---

## 2. Checkpoint Recovery Architecture

1. **State Manifest:** The system snapshot is saved atomically in `checkpoints/latest_checkpoint.json` with SHA-256 integrity hash.
2. **Durability Engine:** Every discrete state transition is recorded in SQLite database `state/journal.db` using Write-Ahead Logging (`journal_mode=WAL`) and `synchronous=FULL`.
3. **Atomic Replacement:** Checkpoints are written to a `.tmp` file, flushed with `fsync`, and atomically renamed to prevent corruption during unexpected shutdowns or power loss.
4. **Fallback Mechanism:** If the latest checkpoint file is ever damaged or truncated, the supervisor automatically loads `checkpoints/previous_checkpoint.json`.
