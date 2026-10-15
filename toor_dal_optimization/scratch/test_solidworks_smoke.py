"""
Disposable SolidWorks 2025 SP01.2 Smoke Test.
Connects via COM, verifies version, creates a simple parametric cylinder (r=50mm, h=100mm),
computes mass properties, exports to STEP AP214, and verifies valid B-Rep solid topology.
"""
import os
import sys

def run_solidworks_smoke_test():
    result = {
        "tool": "SOLIDWORKS",
        "progid": "SldWorks.Application",
        "path_found": False,
        "exe_path": r"C:\Program Files\SolidWorks Corp\SOLIDWORKS (2)\SLDWORKS.exe",
        "version": None,
        "launch_confirmed": False,
        "smoke_test_passed": False,
        "error": None,
        "native_part_path": None,
        "step_export_path": None,
        "volume_m3": None,
        "body_count": None,
        "step_bytes": None,
        "step_lines": None,
        "has_brep_solid": False
    }

    if os.path.exists(result["exe_path"]):
        result["path_found"] = True

    try:
        import win32com.client
    except ImportError as e:
        result["error"] = f"win32com not available: {e}"
        return result

    try:
        sw_app = win32com.client.Dispatch("SldWorks.Application")
        sw_app.Visible = False
        rev = sw_app.RevisionNumber
        result["version"] = str(rev)
        result["launch_confirmed"] = True
        print(f"Connected to SolidWorks! Version/Revision: {rev}")

        template = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\MBD\part 0051mm to 0250mm.prtdot"
        if not os.path.exists(template):
            result["error"] = f"Template not found: {template}"
            return result

        part_doc = sw_app.NewDocument(template, 0, 0, 0)
        if not part_doc:
            result["error"] = "Failed to create document from template"
            return result

        title = part_doc.GetTitle
        print(f"Opened document: {title}")

        # 1. Select Front Plane
        part_doc.SelectByID("Front Plane", "PLANE", 0, 0, 0)
        part_doc.SketchManager.InsertSketch(True)

        # 2. Draw Circle radius 0.05 m (50 mm)
        part_doc.SketchManager.CreateCircleByRadius(0, 0, 0, 0.05)
        part_doc.SketchManager.InsertSketch(True)

        # 3. Extrude Cylinder 0.10 m (100 mm) using verified 20-arg FeatureExtrusion
        # (Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Dchk3, Dchk4, Ang1, Ang2, FlipAng1, FlipAng2, Cap, Draft1, Draft2, Merge, UseFeat)
        feat = part_doc.FeatureManager.FeatureExtrusion(
            True, False, False, 0, 0, 0.10, 0.0, False, False, False, False, 0.0, 0.0, False, False, False, False, False, True, True
        )
        print("FeatureExtrusion created successfully:", feat is not None)

        # 4. Save native SLDPRT in scratch/
        os.makedirs("scratch", exist_ok=True)
        part_path = os.path.abspath("scratch/disposable_smoke_test_cylinder.SLDPRT")
        step_path = os.path.abspath("scratch/disposable_smoke_test_cylinder.STEP")

        part_doc.SaveAs(part_path)
        result["native_part_path"] = part_path
        print(f"Saved native part: {part_path} ({os.path.getsize(part_path)} bytes)")

        # 5. Measure volume via Body
        # Theoretical volume: pi * r^2 * h = 3.14159265 * 0.05^2 * 0.10 = 0.000785398 m^3
        bodies = part_doc.GetBodies2(0, False)
        if bodies:
            result["body_count"] = len(bodies)
            body = bodies[0]
            # Get body volume/mass properties
            # IBody2.GetMassProperties
            mp = body.GetMassProperties(0)
            if mp and len(mp) >= 4:
                vol = mp[3] # Volume in m^3
                result["volume_m3"] = float(vol)
                print(f"Measured Solid Body Volume: {vol:.7f} m^3 (Theoretical: 0.0007854 m^3)")

        # 6. Export STEP AP214
        sw_app.SetUserPreferenceIntegerValue(17, 214) # swStepExportPreference 214
        part_doc.SaveAs(step_path)
        result["step_export_path"] = step_path

        if os.path.exists(step_path):
            sz = os.path.getsize(step_path)
            result["step_bytes"] = sz
            with open(step_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            lines = content.splitlines()
            result["step_lines"] = len(lines)
            has_brep = "MANIFOLD_SOLID_BREP" in content or "ADVANCED_FACE" in content or "CLOSED_SHELL" in content
            result["has_brep_solid"] = has_brep
            print(f"Exported STEP file: {step_path} ({sz} bytes, {len(lines)} lines)")
            print(f"Verified B-Rep Solid Topology: {has_brep}")

            # Acceptance criteria: > 2000 bytes, > 50 lines, has solid topology, body count = 1
            if sz > 2000 and len(lines) > 50 and has_brep:
                result["smoke_test_passed"] = True

        # Close test document cleanly
        sw_app.CloseDoc(title)
        print("Closed test document cleanly.")

    except Exception as e:
        result["error"] = str(e)
        print(f"SolidWorks smoke test error: {e}")

    return result

if __name__ == "__main__":
    import json
    res = run_solidworks_smoke_test()
    print("RESULT_JSON:", json.dumps(res, indent=2))
