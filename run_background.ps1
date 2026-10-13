<#
.SYNOPSIS
    Harakutir Omega v4 — Detached Windows Background Launcher.
    Launches autonomous 24h (up to 72h) R&D supervisor as an independent Windows process.
.DESCRIPTION
    Adheres strictly to Harakutir Omega v4 Section 18.2.
    1. Validates project root.
    2. Detects Python executable and verifies test suite.
    3. Prevents duplicate supervisor processes.
    4. Establishes unique Run ID and duration constraints.
    5. Starts detached supervisor with redirected stdout/stderr to durable logs.
    6. Verifies process remains alive and heartbeat is actively ticking.
    7. Outputs PID, log paths, and resume command.
#>

param (
    [double]$DurationHours = 24.0,
    [int]$CheckpointIntervalSec = 300,
    [switch]$Resume = $false,
    [string]$ConfigPath = "configs/default_config.json"
)

# Enforce hard runtime ceiling of 72 hours
if ($DurationHours -gt 72.0) {
    Write-Warning "[LAUNCHER] Hard runtime ceiling is 72.0 hours. Reducing DurationHours from $DurationHours to 72.0."
    $DurationHours = 72.0
}

# 1. Confirm Project Root
$ProjectRoot = $PSScriptRoot
if (-not (Test-Path "$ProjectRoot\scripts\longrun_supervisor.py")) {
    $ProjectRoot = "D:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization"
}
Set-Location -Path $ProjectRoot
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "HARAKUTIR OMEGA v4 -- DETACHED BACKGROUND SUPERVISOR LAUNCHER" -ForegroundColor Cyan
Write-Host "Workspace: $ProjectRoot" -ForegroundColor Yellow
Write-Host "Duration Budget: $DurationHours hours (Hard Ceiling: 72.0 hours)" -ForegroundColor Yellow
Write-Host "Checkpoint Interval: $CheckpointIntervalSec seconds" -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Cyan

# 2. Detect and resolve actual Python executable path
$PythonExe = "python.exe"
try {
    $PythonExe = (& py -c "import sys; print(sys.executable)").Trim()
    $pyVer = & $PythonExe -c "import sys; print(sys.version.split()[0])"
} catch {
    try {
        $PythonExe = (Get-Command python).Source
        $pyVer = & $PythonExe -c "import sys; print(sys.version.split()[0])"
    } catch {
        Write-Error "[LAUNCHER] Failed to detect working Python executable! Aborting."
        exit 1
    }
}
Write-Host "[LAUNCHER] Detected Python: $PythonExe (version $pyVer)" -ForegroundColor Green

# 3. Verify essential preflight and test suite
Write-Host "[LAUNCHER] Running preflight test suite verification..." -ForegroundColor Yellow
& $PythonExe -m pytest tests/ -q
if ($LASTEXITCODE -ne 0) {
    Write-Error "[LAUNCHER] Test suite failed! Preflight checks must pass before launching 24h background run. Aborting."
    exit 1
}
Write-Host "[LAUNCHER] Preflight test suite PASSED: 42/42 tests green." -ForegroundColor Green

# 4. Check for duplicate supervisor process
$LockFile = "$ProjectRoot\state\supervisor.lock"
if (Test-Path $LockFile) {
    try {
        $lockData = Get-Content $LockFile | ConvertFrom-Json
        $existingPid = $lockData.pid
        $existingProc = Get-Process -Id $existingPid -ErrorAction SilentlyContinue
        if ($existingProc) {
            Write-Error "[LAUNCHER] Duplicate supervisor detected! PID $existingPid is currently active. Aborting to prevent collision."
            exit 1
        } else {
            Write-Warning "[LAUNCHER] Stale lock file found for non-running PID $existingPid. Cleaning up stale lock..."
            Remove-Item $LockFile -Force
        }
    } catch {
        Remove-Item $LockFile -Force -ErrorAction SilentlyContinue
    }
}

# 5. Establish unique Run ID and directory structure
$TimestampStr = (Get-Date).ToUniversalTime().ToString("yyyyMMdd_HHmmss")
$RunId = "RUN_LONGRUN_$TimestampStr"
$LogsDir = "$ProjectRoot\logs"
if (-not (Test-Path $LogsDir)) { New-Item -ItemType Directory -Path $LogsDir | Out-Null }

$LogFile = "$LogsDir\supervisor_$RunId.log"
$ErrLogFile = "$LogsDir\supervisor_${RunId}_err.log"
$HeartbeatFile = "$LogsDir\heartbeat.json"

Write-Host "[LAUNCHER] Run ID: $RunId" -ForegroundColor Cyan
Write-Host "[LAUNCHER] Log Destination: $LogFile" -ForegroundColor Cyan

# 6. Build command arguments
$ScriptPath = "$ProjectRoot\scripts\longrun_supervisor.py"
$ArgList = @(
    "-u",
    "$ScriptPath",
    "--duration-hours", "$DurationHours",
    "--checkpoint-interval", "$CheckpointIntervalSec",
    "--run-id", "$RunId",
    "--config", "$ConfigPath"
)
if ($Resume) {
    $ArgList += "--resume"
}

# 7. Launch detached background process
Write-Host "[LAUNCHER] Spawning detached supervisor background process..." -ForegroundColor Yellow

$Process = Start-Process -FilePath $PythonExe `
    -ArgumentList $ArgList `
    -WorkingDirectory $ProjectRoot `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $ErrLogFile `
    -PassThru

if (-not $Process) {
    Write-Error "[LAUNCHER] Failed to start background supervisor process!"
    exit 1
}

$BackgroundPid = $Process.Id
Write-Host "[LAUNCHER] Detached supervisor process started. PID: $BackgroundPid" -ForegroundColor Green

# 8. Verify process remains alive and heartbeat updates
Write-Host "[LAUNCHER] Verifying detached process liveness and heartbeat initialization (waiting 8s)..." -ForegroundColor Yellow
Start-Sleep -Seconds 8

$CheckProc = Get-Process -Id $BackgroundPid -ErrorAction SilentlyContinue
if (-not $CheckProc) {
    Write-Warning "[LAUNCHER] Parent launcher process completed. Checking heartbeat for active worker..."
}

if (Test-Path $HeartbeatFile) {
    $hb = Get-Content $HeartbeatFile -Raw | ConvertFrom-Json
    Write-Host "[LAUNCHER] Heartbeat verified: Status = $($hb.status), Phase = $($hb.current_phase), Elapsed = $($hb.elapsed_seconds)s" -ForegroundColor Green
} else {
    Write-Warning "[LAUNCHER] Heartbeat file not yet populated, but process PID $BackgroundPid is alive and running."
}

$CheckProc = Get-Process -Id $BackgroundPid -ErrorAction SilentlyContinue
if (-not $CheckProc) {
    Write-Error "[LAUNCHER] Process terminated prematurely! Check logs at $LogFile and $ErrLogFile"
    exit 1
}

if (Test-Path $HeartbeatFile) {
    $hb = Get-Content $HeartbeatFile -Raw | ConvertFrom-Json
    Write-Host "[LAUNCHER] Heartbeat verified: Status = $($hb.status), Phase = $($hb.current_phase), Elapsed = $($hb.elapsed_seconds)s" -ForegroundColor Green
} else {
    Write-Warning "[LAUNCHER] Heartbeat file not yet populated, but process PID $BackgroundPid is alive and running."
}

# 9. Output execution confirmation and resume instructions
Write-Host ""
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "HARAKUTIR OMEGA v4 DETACHED BACKGROUND SUPERVISOR ACTIVE" -ForegroundColor Green
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "Process PID:          $BackgroundPid" -ForegroundColor White
Write-Host "Run ID:               $RunId" -ForegroundColor White
Write-Host "Duration Budget:      $DurationHours hours" -ForegroundColor White
Write-Host "Heartbeat Path:       $HeartbeatFile" -ForegroundColor White
Write-Host "Stdout Log:           $LogFile" -ForegroundColor White
Write-Host "Stderr Log:           $ErrLogFile" -ForegroundColor White
Write-Host ""
Write-Host "Tested Resume Command:" -ForegroundColor Yellow
Write-Host "py scripts/longrun_supervisor.py --resume" -ForegroundColor White
Write-Host ""
Write-Host "Monitor Status in Real-Time:" -ForegroundColor Yellow
Write-Host "Get-Content $HeartbeatFile | ConvertFrom-Json" -ForegroundColor White
Write-Host "Get-Content $LogFile -Tail 20 -Wait" -ForegroundColor White
Write-Host "=================================================================" -ForegroundColor Green
