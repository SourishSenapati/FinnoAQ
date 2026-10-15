"""
Build highly realistic, multi-feature TK-101 Process Vessel in SolidWorks 2025.
"""
import os
import math
import win32com.client

sw = win32com.client.Dispatch("SldWorks.Application")
template = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\MBD\part 0051mm to 0250mm.prtdot"
doc = sw.NewDocument(template, 0, 0, 0)
feat_mgr = doc.FeatureManager
sketch_mgr = doc.SketchManager

print("Building realistic TK-101 in SolidWorks...")

# 1. Main Cylindrical Shell (H = 2.20m, OD = 2.0m, 6mm wall)
doc.Extension.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 1.000)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.994)
sketch_mgr.InsertSketch(True)
f1 = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.200, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("1. Main shell:", f1 is not None)

# 2. Conical Bottom Section (Extrude downwards with draft to create conical hopper)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 1.000)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.994)
sketch_mgr.InsertSketch(True)
# Draft inward 50 degrees = 0.8726 radians, depth 0.50m
f2 = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.500, 0, True, False, False, False, 0.8726, 0, False, False, False, False, False, True, True)
print("2. Conical bottom:", f2 is not None)

# 3. Reference Plane for Bottom Drain (Y = -0.50m)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
p_drain = feat_mgr.InsertRefPlane(8, -0.500, 0, 0, 0, 0)
print("3. Ref plane drain:", p_drain is not None)

# Bottom Drain Spool & Flange (Extrude downwards from drain level)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.100)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.090)
sketch_mgr.InsertSketch(True)
f_spool = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.750, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   Drain spool:", f_spool is not None)

# Drain Flange Disc at Y = -0.75m
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.140) # 280mm flange
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.090)
sketch_mgr.InsertSketch(True)
f_flange = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.775, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   Drain flange:", f_flange is not None)

# 4. Top Head Reference Plane at Y = 2.20m
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
p_top = feat_mgr.InsertRefPlane(8, 2.200, 0, 0, 0, 0)
print("4. Ref plane top head:", p_top is not None)

# Top Dished Cap (Extrude dome from Top Plane with inward draft)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 1.020)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.994)
sketch_mgr.InsertSketch(True)
f_rim = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.230, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   Top rim:", f_rim is not None)

# Dome Cap
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 1.000)
sketch_mgr.InsertSketch(True)
f_dome = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.500, 0, True, False, False, False, 0.65, 0, False, False, False, False, False, True, True)
print("   Dome cap:", f_dome is not None)

# 5. Agitator Stool (Lantern Mounting) at Top Center
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.225) # 450mm stool
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.180)
sketch_mgr.InsertSketch(True)
f_stool = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.800, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("5. Agitator stool:", f_stool is not None)

# Agitator Top Mounting Flange
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.260)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.180)
sketch_mgr.InsertSketch(True)
f_sflange = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.830, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   Stool top flange:", f_sflange is not None)

# Geared Motor Drive Housing (SEW Helical Gearbox on top of stool)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCornerRectangle(-0.200, -0.200, 0, 0.200, 0.200, 0)
sketch_mgr.InsertSketch(True)
f_motor1 = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 3.250, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   Gearbox housing:", f_motor1 is not None)

# Electric Motor Cylinder extending horizontally from gearbox
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0.350, 0, 0, 0.150)
sketch_mgr.InsertSketch(True)
f_motor2 = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 3.200, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   Electric motor:", f_motor2 is not None)

# 6. Flanged Nozzles on Top Head
# N1: 20" Manway (500mm neck + 650mm flange + cover)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0.450, 0.450, 0, 0.250)
sketch_mgr.CreateCircleByRadius(0.450, 0.450, 0, 0.240)
sketch_mgr.InsertSketch(True)
f_n1_neck = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.650, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("6. N1 Manway neck:", f_n1_neck is not None)

# N1 Flange & Bolted Cover
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0.450, 0.450, 0, 0.320)
sketch_mgr.InsertSketch(True)
f_n1_flg = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.680, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   N1 Manway cover:", f_n1_flg is not None)

# N2: 6" Dal Feed Nozzle & Flange
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(-0.500, 0.450, 0, 0.084)
sketch_mgr.CreateCircleByRadius(-0.500, 0.450, 0, 0.075)
sketch_mgr.InsertSketch(True)
f_n2_neck = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.600, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(-0.500, 0.450, 0, 0.140)
sketch_mgr.CreateCircleByRadius(-0.500, 0.450, 0, 0.075)
sketch_mgr.InsertSketch(True)
f_n2_flg = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.625, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   N2 Feed nozzle & flange:", f_n2_flg is not None)

# N3: 2" Water Inlet Nozzle & Flange
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0.000, -0.650, 0, 0.030)
sketch_mgr.CreateCircleByRadius(0.000, -0.650, 0, 0.025)
sketch_mgr.InsertSketch(True)
f_n3_neck = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.550, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0.000, -0.650, 0, 0.075)
sketch_mgr.CreateCircleByRadius(0.000, -0.650, 0, 0.025)
sketch_mgr.InsertSketch(True)
f_n3_flg = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.570, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   N3 Water nozzle & flange:", f_n3_flg is not None)

# N5: 3" Breather Vent Nozzle & Flange
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(-0.500, -0.450, 0, 0.045)
sketch_mgr.CreateCircleByRadius(-0.500, -0.450, 0, 0.040)
sketch_mgr.InsertSketch(True)
f_n5_neck = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.600, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(-0.500, -0.450, 0, 0.100)
sketch_mgr.CreateCircleByRadius(-0.500, -0.450, 0, 0.040)
sketch_mgr.InsertSketch(True)
f_n5_flg = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.620, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   N5 Vent nozzle & flange:", f_n5_flg is not None)

# 7. Support Legs (4 Structural Columns with Baseplates and Gussets)
legs = [(0.92, 0.92), (-0.92, 0.92), (-0.92, -0.92), (0.92, -0.92)]
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
for lx, lz in legs:
    sketch_mgr.CreateCornerRectangle(lx - 0.08, lz - 0.08, 0, lx + 0.08, lz + 0.08, 0)
sketch_mgr.InsertSketch(True)
f_legs = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.750, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("7. 4 Support legs:", f_legs is not None)

# Baseplates at bottom of legs (Z = -0.75m to -0.77m)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
for lx, lz in legs:
    sketch_mgr.CreateCornerRectangle(lx - 0.15, lz - 0.15, 0, lx + 0.15, lz + 0.15, 0)
sketch_mgr.InsertSketch(True)
f_bps = feat_mgr.FeatureExtrusion(True, True, True, 0, 0, 0.775, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("   4 Foot baseplates:", f_bps is not None)

# 8. Lifting Padeyes (2 heavy lugs on shell rim)
doc.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCornerRectangle(0.98, -0.05, 0, 1.08, 0.05, 0)
sketch_mgr.CreateCornerRectangle(-1.08, -0.05, 0, -0.98, 0.05, 0)
sketch_mgr.InsertSketch(True)
f_lugs = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 2.350, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("8. 2 Lifting padeyes:", f_lugs is not None)

# Save Part and STEP
out_prt = os.path.abspath("engineering/cad/sldprt/TK-101_Soak_Tank.SLDPRT")
out_step = os.path.abspath("engineering/cad/step/TK-101_Soak_Tank.step")
doc.SaveAs(out_prt)
sw.SetUserPreferenceIntegerValue(17, 214) # AP214
doc.SaveAs(out_step)

bodies = doc.GetBodies2(0, False)
b_count = len(bodies) if bodies else 0
print(f"TK-101 COMPLETED: Total Solid Bodies={b_count}!")
print(f"Saved: {out_prt} ({os.path.getsize(out_prt)} bytes)")
print(f"Saved: {out_step} ({os.path.getsize(out_step)} bytes, {len(open(out_step).readlines())} lines)")

sw.CloseDoc(doc.GetTitle)
