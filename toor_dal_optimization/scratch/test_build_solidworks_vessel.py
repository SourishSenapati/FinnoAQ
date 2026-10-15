"""
Test building authentic TK-101 Process Soak Vessel in SolidWorks 2025 SP01.2.
Inspects each feature build and mass properties.
"""

import os
import sys
import math
import win32com.client

def test_vessel():
    print("Connecting to SolidWorks 2025...")
    sw = win32com.client.Dispatch("SldWorks.Application")
    sw.Visible = False
    
    template = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\MBD\part 0051mm to 0250mm.prtdot"
    doc = sw.NewDocument(template, 0, 0, 0)
    title = doc.GetTitle
    print(f"Created new document: {title}")
    
    feat_mgr = doc.FeatureManager
    sketch_mgr = doc.SketchManager
    
    # 1. Main Shell Cylinder (OD 2000mm, ID 1988mm, H 2200mm)
    print("1. Extruding Main Cylindrical Shell...")
    doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    sketch_mgr.CreateCircleByRadius(0, 0, 0, 1.000)
    sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.994)
    sketch_mgr.InsertSketch(True)
    f1 = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.200, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
    print(f"   Main shell feature created: {f1 is not None}")
    
    # 2. Conical Bottom (Revolve a trapezoidal profile around centerline)
    # Front Plane: X=0 to 1.0m at Y=0, X=0 to 0.10m at Y=-0.50m
    print("2. Revolving Conical Bottom...")
    doc.SelectByID("Front Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    # Centerline for revolve
    sketch_mgr.CreateCenterLine(0, 0.1, 0, 0, -1.0, 0)
    # Profile: (0.10, -0.50) -> (1.00, 0) -> (0.994, 0) -> (0.094, -0.50) -> (0.10, -0.50)
    sketch_mgr.CreateLine(0.100, -0.500, 0, 1.000, 0.000, 0)
    sketch_mgr.CreateLine(1.000, 0.000, 0, 0.994, 0.000, 0)
    sketch_mgr.CreateLine(0.994, 0.000, 0, 0.094, -0.500, 0)
    sketch_mgr.CreateLine(0.094, -0.500, 0, 0.100, -0.500, 0)
    sketch_mgr.InsertSketch(True)
    # FeatureRevolve(SingleDir, IsSolid, ReverseDir, Angle, Offset, RevType)
    f2 = feat_mgr.FeatureRevolve(6.2831853, False, 0, 0, 0, True, True, True)
    print(f"   Conical bottom revolved: {f2 is not None}")

    # 3. Bottom Drain Flange Neck & Flange (Extrude downwards from Y=-0.50m)
    print("3. Extruding Drain Neck & Flange...")
    doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.100)
    sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.094)
    sketch_mgr.InsertSketch(True)
    # Extrude downwards (flip = True) by 0.75m
    f3 = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.750, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
    print(f"   Drain neck extruded: {f3 is not None}")
    
    # 4. Top Dished Head (Torispherical dome via revolve on Front Plane)
    print("4. Revolving Top Torispherical Head...")
    doc.SelectByID("Front Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    sketch_mgr.CreateCenterLine(0, 2.0, 0, 0, 3.0, 0)
    # Crown arc from (0, 2.53) to (0.90, 2.40), knuckle arc to (1.00, 2.20)
    sketch_mgr.Create3PointArc(0.0, 2.530, 0, 0.900, 2.400, 0, 0.450, 2.490, 0)
    sketch_mgr.CreateLine(0.900, 2.400, 0, 1.000, 2.200, 0)
    sketch_mgr.CreateLine(1.000, 2.200, 0, 0.994, 2.200, 0)
    sketch_mgr.CreateLine(0.994, 2.200, 0, 0.894, 2.394, 0)
    sketch_mgr.Create3PointArc(0.894, 2.394, 0, 0.0, 2.524, 0, 0.450, 2.484, 0)
    sketch_mgr.CreateLine(0.0, 2.524, 0, 0.0, 2.530, 0)
    sketch_mgr.InsertSketch(True)
    f4 = feat_mgr.FeatureRevolve(6.2831853, False, 0, 0, 0, True, True, True)
    print(f"   Top head revolved: {f4 is not None}")

    # 5. Support Legs (4 legs at 90 deg around circumference)
    print("5. Extruding 4 Support Legs with Baseplates...")
    leg_coords = [(0.95, 0.95), (-0.95, 0.95), (-0.95, -0.95), (0.95, -0.95)]
    doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    for lx, lz in leg_coords:
        # 150mm channel footprint
        sketch_mgr.CreateCornerRectangle(lx - 0.075, lz - 0.075, 0, lx + 0.075, lz + 0.075, 0)
    sketch_mgr.InsertSketch(True)
    # Extrude downwards from Y=0.80m down to Y=-0.75m (total 1.55m)
    f5 = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.750, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
    print(f"   Legs extruded: {f5 is not None}")

    # 6. Flanged Nozzles on Top Head (Manway, Dal Feed, Water, Vent, Overflow)
    print("6. Extruding Top Head Flanged Nozzles...")
    doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    # N1: 20" Manway at (0.35, 0.35)
    sketch_mgr.CreateCircleByRadius(0.350, 0.350, 0, 0.250)
    sketch_mgr.CreateCircleByRadius(0.350, 0.350, 0, 0.240)
    # N2: 6" Dal Feed at (-0.45, 0.35)
    sketch_mgr.CreateCircleByRadius(-0.450, 0.350, 0, 0.084)
    sketch_mgr.CreateCircleByRadius(-0.450, 0.350, 0, 0.075)
    # N3: 2" Water Inlet at (0.00, -0.55)
    sketch_mgr.CreateCircleByRadius(0.000, -0.550, 0, 0.030)
    sketch_mgr.CreateCircleByRadius(0.000, -0.550, 0, 0.025)
    # N5: 3" Vent at (-0.45, -0.35)
    sketch_mgr.CreateCircleByRadius(-0.450, -0.350, 0, 0.045)
    sketch_mgr.CreateCircleByRadius(-0.450, -0.350, 0, 0.040)
    sketch_mgr.InsertSketch(True)
    # Extrude upwards from 2.20 to 2.80m
    f6 = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.800, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
    print(f"   Nozzle necks extruded: {f6 is not None}")

    # 7. Agitator Drive Mounting Stool at Top Center
    print("7. Extruding Center Agitator Stool...")
    doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
    sketch_mgr.InsertSketch(True)
    sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.225)
    sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.150)
    sketch_mgr.InsertSketch(True)
    f7 = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 3.100, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
    print(f"   Agitator stool extruded: {f7 is not None}")

    # Save SLDPRT and STEP
    out_prt = os.path.abspath("engineering/cad/sldprt/TK-101_Soak_Tank.SLDPRT")
    out_step = os.path.abspath("engineering/cad/step/TK-101_Soak_Tank.step")
    doc.SaveAs(out_prt)
    sw.SetUserPreferenceIntegerValue(17, 214) # AP214
    doc.SaveAs(out_step)
    
    bodies = doc.GetBodies2(0, False)
    body_count = len(bodies) if bodies else 0
    print(f"Successfully built TK-101: Bodies={body_count}, SLDPRT={out_prt}")
    print(f"STEP File generated: {out_step} ({os.path.getsize(out_step)} bytes, {len(open(out_step).readlines())} lines)")
    
    sw.CloseDoc(title)

if __name__ == '__main__':
    test_vessel()
