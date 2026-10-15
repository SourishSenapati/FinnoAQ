"""
Disposable Aspen Plus V14 Smoke Test & Suitability Assessment.
Verifies Aspen Plus V14 executable paths, COM ProgID (Apwn.Document),
tests non-blocking COM initialization, and evaluates suitability for dal hydration and drying.
"""
import os
import sys
import json

def run_aspen_smoke_test():
    result = {
        "tool": "Aspen Plus / aspenONE V14",
        "progid": "Apwn.Document",
        "hysys_progid": "HYSYS.Application",
        "aspen_exe": r"D:\Engineering Software\ASPENONE64bit\Aspen Plus V14.0\GUI\Xeq\AspenPlus.exe",
        "hysys_exe": r"D:\Engineering Software\ASPENONE64bit\Aspen HYSYS V14.0\AspenHysys.exe",
        "path_found": False,
        "com_registered": False,
        "hysys_registered": False,
        "launch_confirmed": False,
        "license_status": "UNKNOWN",
        "smoke_test_passed": False,
        "error": None,
        "suitability_matrix": {
            "pure_water_evaporation_flash": "SUITABLE (Rigorous steam tables & psychrometrics)",
            "heat_exchanger_steam_coil_edr": "SUITABLE (Aspen EDR sizing for finned-tube battery)",
            "bulk_mass_energy_balance": "SUITABLE (Standard Flash/Mixer blocks)",
            "grain_hydration_pectin_kinetics": "UNSUITABLE (Aspen lacks biological grain swelling models; custom model required)",
            "soak_calcium_leaching": "UNSUITABLE (Requires empirical target-lot kinetic calibration)"
        }
    }

    if os.path.exists(result["aspen_exe"]):
        result["path_found"] = True
    print(f"Aspen Plus V14 executable found: {result['path_found']} ({result['aspen_exe']})")

    # Check Registry for ProgID
    import winreg
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "Apwn.Document"):
            result["com_registered"] = True
    except Exception:
        pass
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "HYSYS.Application"):
            result["hysys_registered"] = True
    except Exception:
        pass

    print(f"COM ProgIDs registered: Apwn.Document={result['com_registered']}, HYSYS.Application={result['hysys_registered']}")

    # Attempt COM Dispatch
    try:
        import win32com.client
        print("Attempting to instantiate Apwn.Document via win32com...")
        # Note: Aspen Plus can take 10-20 seconds to load license and GUI engine
        aspen_app = win32com.client.Dispatch("Apwn.Document")
        print("Apwn.Document dispatched successfully!")
        result["launch_confirmed"] = True
        
        # Check version if available
        try:
            ver = aspen_app.Version
            print(f"Aspen Plus COM Version: {ver}")
            result["version"] = str(ver)
        except Exception:
            result["version"] = "V14.0"

        # Check license / ready state
        try:
            # Apwn.Document.Visible
            aspen_app.Visible = False
            result["license_status"] = "ACTIVE_OR_RUNNING"
            result["smoke_test_passed"] = True
            print("Aspen Plus COM interface is responsive!")
        except Exception as le:
            result["license_status"] = f"DISPATCHED_BUT_CHECK_FAILED: {le}"

        # Close/Release
        try:
            aspen_app.Quit()
        except Exception:
            pass

    except Exception as e:
        result["error"] = str(e)
        print(f"Aspen COM Dispatch result: {e}")
        # Even if headless launch fails due to interactive license prompt, path & registration are proven
        if result["path_found"] and result["com_registered"]:
            result["license_status"] = "INSTALLED_REQUIRES_INTERACTIVE_OR_NETWORK_LICENSE"

    return result

if __name__ == "__main__":
    res = run_aspen_smoke_test()
    print("RESULT_JSON:", json.dumps(res, indent=2))
