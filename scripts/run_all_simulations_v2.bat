@echo off

echo =========================================================================
echo MULTIGRAIN ATTA SIMULATION - 100 MILLION ITERATIONS (6-SIGMA)
echo =========================================================================
cd /d "d:\PROJECT\FINNO PROJECTS\atta\multigrain_engine"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to navigate to Atta engine directory.
    exit /b %errorlevel%
)
py main_multigrain_sim.py > "d:\PROJECT\FINNO PROJECTS\atta\SIMULATION_LOG.txt" 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Multigrain Atta Simulation Failed! Check SIMULATION_LOG.txt.
) else (
    echo [SUCCESS] Multigrain Atta Simulation Complete. Output saved.
)

echo.
echo =========================================================================
echo MUSTARD OIL SIMULATION - 100 MILLION ITERATIONS (6-SIGMA)
echo =========================================================================
cd /d "d:\PROJECT\FINNO PROJECTS\mustard_oil"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to navigate to Oil simulation directory.
    exit /b %errorlevel%
)
py simulation_oil.py > "d:\PROJECT\FINNO PROJECTS\mustard_oil\SIMULATION_LOG.txt" 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Mustard Oil Simulation Failed! Check SIMULATION_LOG.txt.
) else ( 
    echo [SUCCESS] Mustard Oil Simulation Complete. Output saved.
)

echo.
echo [DONE] All Simulations Completed. Logs generated.
echo Press any key to exit...
pause >nul
