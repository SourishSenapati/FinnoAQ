<#
.SYNOPSIS
    Harakutir Autonomous R&D Supervisor Entrypoint (PowerShell)
.DESCRIPTION
    Runs, benchmarks, resumes, tests, or audits the Harakutir Toor Dal Diagnostic R&D system.
.PARAMETER Mode
    Execution mode: Run, Resume, Benchmark, Test, Audit, Ingest. Default is Run.
.EXAMPLE
    .\run.ps1 -Mode Benchmark
    .\run.ps1 -Mode Run
    .\run.ps1 -Mode Resume
    .\run.ps1 -Mode Test
    .\run.ps1 -Mode Audit
#>

param (
    [ValidateSet("Run", "Resume", "Benchmark", "Test", "Audit", "Ingest", "Simulate", "MillionSim")]
    [string]$Mode = "Run",
    
    [string]$Config = "configs/default_config.json"
)

$PythonExe = "C:\Python313\python.exe"

if (-not (Test-Path $PythonExe)) {
    Write-Warning "Python 3.13 not found at default location. Falling back to 'python' or 'py'..."
    if (Get-Command python -ErrorAction SilentlyContinue) {
        $PythonExe = "python"
    } elseif (Get-Command py -ErrorAction SilentlyContinue) {
        $PythonExe = "py"
    } else {
        Write-Error "No compatible Python interpreter found."
        exit 1
    }
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  HARAKUTIR AUTONOMOUS R&D SUPERVISOR (POWERSHELL)       " -ForegroundColor Cyan
Write-Host "  Target: Windows 11 + AMD Ryzen 9 + NVIDIA RTX 4050 GPU " -ForegroundColor Cyan
Write-Host "  Mode: $Mode                                             " -ForegroundColor Green
Write-Host "  Python: $PythonExe                                     " -ForegroundColor DarkGray
Write-Host "==========================================================" -ForegroundColor Cyan

if ($Mode -eq "Test") {
    Write-Host "[TEST] Launching pytest test suite..." -ForegroundColor Yellow
    & $PythonExe -m pytest tests/ -v
} elseif ($Mode -eq "Audit") {
    Write-Host "[AUDIT] Launching independent red-team audit..." -ForegroundColor Yellow
    & $PythonExe -m pytest tests/test_acceptance_and_audit.py -v
} elseif ($Mode -eq "Simulate" -or $Mode -eq "MillionSim") {
    Write-Host "[SIMULATE] Launching GPU Million-Experiment 5-Sigma Discovery Engine..." -ForegroundColor Magenta
    & $PythonExe scripts/run_gpu_million_scale.py
} else {
    & $PythonExe scripts/run_supervisor.py --mode $Mode --config $Config
}
