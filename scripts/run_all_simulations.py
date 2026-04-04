
import subprocess
import sys
import os
import time

# List of simulation scripts to run
simulations = [
    r"d:\PROJECT\FINNO PROJECTS\toor_dal\production_optimizer\rnd_simulation.py",  # Toor Dal R&D
    # Toor Dal Bench
    r"d:\PROJECT\FINNO PROJECTS\toor_dal\production_optimizer\phase2_bench.py",
    # Atta (Wheat/Cassava)
    r"d:\PROJECT\FINNO PROJECTS\atta\simulation_atta.py",
    # Sundarban Honey
    r"d:\PROJECT\FINNO PROJECTS\sundarban_honey\simulation_honey.py",
    # Mustard Honey (Diversified)
    r"d:\PROJECT\FINNO PROJECTS\mustard_honey\simulation_mustard_honey.py",
    # Ghee Bilona
    r"d:\PROJECT\FINNO PROJECTS\ghee_bilona\simulation_ghee.py",
    # Mustard Oil (Herbal)
    r"d:\PROJECT\FINNO PROJECTS\mustard_oil\simulation_oil.py"
]


def run_simulation(script_path):
    print(f"\n{'='*60}")
    print(f"RUNNING: {os.path.basename(script_path)}")
    print(f"{'='*60}")

    if not os.path.exists(script_path):
        print(f"ERROR: File not found: {script_path}")
        return

    # Use the same python interpreter
    python_exe = sys.executable

    start_time = time.time()
    try:
        # Run as subprocess to isolate environments
        result = subprocess.run(
            [python_exe, script_path],
            check=True,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path)  # Run from the script's directory
        )
        print(result.stdout)
        if result.stderr:
            print("STDERR Warning/Error:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"FAILED: {script_path}")
        print("OUTPUT:")
        print(e.stdout)
        print("ERROR:")
        print(e.stderr)

    print(f"Finished in {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    print("STARTING FULL R&D SIMULATION SUITE (GPU ACCELERATED)")
    print("Targeting: Toor Dal, Honey, Ghee, Atta, Mustard Oil")

    total_start = time.time()
    for sim in simulations:
        run_simulation(sim)

    print(
        f"\nALL SIMULATIONS COMPLETED in {time.time() - total_start:.2f} seconds.")
