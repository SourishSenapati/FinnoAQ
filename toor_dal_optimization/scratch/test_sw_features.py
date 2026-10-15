"""
Test SolidWorks COM API for creating Reference Planes, Revolves, and Extrusions.
"""
import win32com.client

sw = win32com.client.Dispatch("SldWorks.Application")
template = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\MBD\part 0051mm to 0250mm.prtdot"
doc = sw.NewDocument(template, 0, 0, 0)
feat_mgr = doc.FeatureManager
sketch_mgr = doc.SketchManager

# 1. Create a Reference Plane at offset 2.200m from Top Plane
doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
ref_plane_top = feat_mgr.InsertRefPlane(8, 2.200, 0, 0, 0, 0) # 8 = Distance
print("Ref plane top created:", ref_plane_top is not None)

# 2. Create a Reference Plane at offset -0.500m (downwards) from Top Plane
doc.SelectByID("Top Plane", "PLANE", 0, 0, 0)
ref_plane_bottom = feat_mgr.InsertRefPlane(8 | 2, 0.500, 0, 0, 0, 0) # Flip direction
print("Ref plane bottom created:", ref_plane_bottom is not None)

# Test extruding on the new plane!
doc.SelectByID("Plane1", "PLANE", 0, 0, 0)
sketch_mgr.InsertSketch(True)
sketch_mgr.CreateCircleByRadius(0, 0, 0, 0.5)
sketch_mgr.InsertSketch(True)
f = feat_mgr.FeatureExtrusion(True, False, False, 0, 0, 0.3, 0, False, False, False, False, 0, 0, False, False, False, False, False, True, True)
print("Extrude on Plane1 created:", f is not None)

# Test Revolve:
# Draw a closed triangle and an axis on Front Plane
doc.SelectByID("Front Plane", "PLANE", 0, 0, 0)
sketch_mgr.InsertSketch(True)
axis = sketch_mgr.CreateCenterLine(0, 0, 0, 0, 1.0, 0)
sketch_mgr.CreateLine(0.1, 0.2, 0, 0.4, 0.2, 0)
sketch_mgr.CreateLine(0.4, 0.2, 0, 0.1, 0.8, 0)
sketch_mgr.CreateLine(0.1, 0.8, 0, 0.1, 0.2, 0)
sketch_mgr.InsertSketch(True)

# Select sketch and axis
doc.SelectByID("Sketch2", "SKETCH", 0, 0, 0)
doc.SelectByID("Line1@Sketch2", "SKETCHSEGMENT", 0, 0, 0, True) # Mark 16 or 0 for axis
rev = feat_mgr.FeatureRevolve2(True, True, False, False, False, False, 0, 0, 6.2831853, 0, False, False, 0.01, 0.01, 0, 0, 0, True, True, True)
print("FeatureRevolve2 created:", rev is not None)

bodies = doc.GetBodies2(0, False)
print("Bodies in doc:", len(bodies) if bodies else 0)

sw.CloseDoc(doc.GetTitle)
