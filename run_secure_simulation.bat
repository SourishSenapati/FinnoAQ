@echo off
REM ---------------------------------------------------
REM  FINNO PROJECTS - SECURE LAUNCHER
REM  Using Verified Python Environment: C:\Python313
REM ---------------------------------------------------

echo [INFO] Explicitly using Python 3.13...
"C:\Python313\python.exe" "toor_dal\verify_all_modules.py"

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Environment Validation Failed!
    echo Your default 'python' might be 3.11, which lacks torch.
    echo This script forces 3.13.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [SUCCESS] Environment Verified. Launching Optimization...
echo.

"C:\Python313\python.exe" -m toor_dal.production_optimizer.main_optimizer

echo.
echo [INFO] Simulation Complete.
pause
