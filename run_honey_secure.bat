@echo off
REM ---------------------------------------------------
REM  FINNO HONEY - SECURE LAUNCHER
REM  Using Verified Python Environment: C:\Python313
REM ---------------------------------------------------

echo [INFO] Explicitly using Python 3.13 for Sundarban Honey...

"C:\Python313\python.exe" "sundarban_honey\simulation_honey.py"

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Simulation Failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [SUCCESS] Honey Simulation Complete.
pause
