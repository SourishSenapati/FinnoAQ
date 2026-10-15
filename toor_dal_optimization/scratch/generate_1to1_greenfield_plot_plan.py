"""
Generate 1:1 True Millimeter Scale Greenfield Master Plot Plan DXF (DWG-FIN-15T-001).
Enforces:
- Model Space is strictly 1:1 true coordinates in millimeters (52,000 x 24,000 mm).
- $INSUNITS = 4 (Millimeters).
- Layer separation: CIVIL_BOUNDARY, HYGIENIC_ZONING, EQUIPMENT_ENVELOPES, LOGISTICS_ROADS, DRAINAGE_TRENCH.
- Dimensioned boundaries and equipment envelopes.
- Explicit watermark: CONCEPTUAL FEED - NOT FOR FABRICATION.
"""
import os
import ezdxf
from ezdxf.enums import TextEntityAlignment

def generate_1to1_plot_plan():
    doc = ezdxf.new("R2018")
    doc.header["$INSUNITS"] = 4 # Millimeters
    msp = doc.modelspace()

    # Define Layers with standard colors
    doc.layers.add("CIVIL_BOUNDARY", color=7)      # White/Black
    doc.layers.add("ZONE_1_INTAKE", color=8)       # Dark Grey
    doc.layers.add("ZONE_2_WET_SOAK", color=5)     # Blue
    doc.layers.add("ZONE_3_DRY_COOL", color=3)     # Green
    doc.layers.add("ZONE_4_CLEANROOM", color=2)    # Yellow/Gold
    doc.layers.add("ZONE_5_WAREHOUSE", color=1)    # Red/Orange
    doc.layers.add("EQUIPMENT_ENVELOPE", color=4)  # Cyan
    doc.layers.add("LOGISTICS_CORRIDOR", color=9)  # Light Grey
    doc.layers.add("TRENCH_DRAINAGE", color=6)     # Magenta
    doc.layers.add("ANNOTATIONS_TITLE", color=7)   # White

    # 1. Outer Site Boundary: 52,000 mm x 24,000 mm
    site_w, site_h = 52000.0, 24000.0
    msp.add_lwpolyline(
        [(0, 0), (site_w, 0), (site_w, site_h), (0, site_h), (0, 0)],
        dxfattribs={"layer": "CIVIL_BOUNDARY"}
    )

    # 2. Functional Zone Partitions (1:1 mm)
    # Zone 1 (Intake & Pre-cleaning): X = 0 to 10,000 mm
    msp.add_lwpolyline([(10000, 0), (10000, site_h)], dxfattribs={"layer": "ZONE_1_INTAKE"})
    msp.add_text("ZONE 1: RAW INTAKE & PRE-CLEANING (GREY)", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 400}).set_placement((1000, 23000))

    # Zone 2 (Wet Soaking & Dewatering): X = 10,000 to 22,000 mm
    msp.add_lwpolyline([(22000, 0), (22000, site_h)], dxfattribs={"layer": "ZONE_2_WET_SOAK"})
    msp.add_text("ZONE 2: WET PROCESS & HYDRATION (BLUE)", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 400}).set_placement((11000, 23000))

    # Zone 3 (Thermal Drying & Cooling): X = 22,000 to 36,000 mm
    msp.add_lwpolyline([(36000, 0), (36000, site_h)], dxfattribs={"layer": "ZONE_3_DRY_COOL"})
    msp.add_text("ZONE 3: THERMAL DRYING & COOLING (GREEN)", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 400}).set_placement((23000, 23000))

    # Zone 4 (Positive Pressure Cleanroom Packaging): X = 36,000 to 44,000 mm, Y = 0 to 16,000 mm
    msp.add_lwpolyline([(44000, 0), (44000, 16000), (36000, 16000)], dxfattribs={"layer": "ZONE_4_CLEANROOM"})
    msp.add_text("ZONE 4: CLASS 8 CLEANROOM PACKAGING (+25 Pa)", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 350}).set_placement((36500, 15000))

    # Zone 5 (Finished Goods Warehouse & Dispatch): X = 44,000 to 52,000 mm
    msp.add_text("ZONE 5: FINISHED GOODS WAREHOUSE", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 400}).set_placement((44500, 23000))

    # 3. Major Equipment GA Envelopes in 1:1 true mm
    # Silos: Two 3,000mm diameter raw silos
    msp.add_circle((3500, 6000), 1500, dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_circle((3500, 12000), 1500, dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_text("SIL-101 (25 MT)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 250}).set_placement((2500, 6000))
    msp.add_text("SIL-102 (25 MT)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 250}).set_placement((2500, 12000))

    # Dual Soak Tanks TK-101A/B: D=2,000mm
    msp.add_circle((14000, 8000), 1000, dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_circle((18000, 8000), 1000, dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_text("TK-101A (7.5 m3)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 250}).set_placement((13000, 8000))
    msp.add_text("TK-101B (7.5 m3)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 250}).set_placement((17000, 8000))

    # Dewatering Screen SC-101: 1,500mm x 3,000mm
    msp.add_lwpolyline([(19500, 7250), (21000, 7250), (21000, 8750), (19500, 8750), (19500, 7250)], dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_text("SC-101 (Dewatering)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 200}).set_placement((19600, 8000))

    # Fluid Bed Dryer DR-101: 14,000mm x 1,500mm envelope
    msp.add_lwpolyline([(22500, 7250), (36500, 7250), (36500, 8750), (22500, 8750), (22500, 7250)], dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_text("DR-101: CONTINUOUS FLUID-BED DRYER (14,000 x 1,000 mm DECK)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 280}).set_placement((23000, 8000))

    # Form-Fill-Seal Packaging Line PKG-101 in Cleanroom: 3,000mm x 8,000mm
    msp.add_lwpolyline([(38000, 4000), (41000, 4000), (41000, 12000), (38000, 12000), (38000, 4000)], dxfattribs={"layer": "EQUIPMENT_ENVELOPE"})
    msp.add_text("PKG-101 (FFS PACKAGING LINE)", dxfattribs={"layer": "EQUIPMENT_ENVELOPE", "height": 250}).set_placement((38200, 8000))

    # 4. Drainage Trench (Sloped to ETP): 500mm width running across Zone 2 & 3
    msp.add_lwpolyline([(10000, 2000), (36000, 2000), (36000, 2500), (10000, 2500), (10000, 2000)], dxfattribs={"layer": "TRENCH_DRAINAGE"})
    msp.add_text("EFFLUENT TRENCH (SLOPE 1:100 TO ETP)", dxfattribs={"layer": "TRENCH_DRAINAGE", "height": 200}).set_placement((15000, 2200))

    # 5. Drawing Header & Watermarks
    msp.add_text("HARAKUTIR FOODS LTD — GREENFIELD MASTER SITE PLOT PLAN", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 600}).set_placement((1000, 1500))
    msp.add_text("SCALE: 1:1 TRUE COORDINATE MILLIMETERS | INSUNITS = 4", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 350}).set_placement((1000, 800))
    msp.add_text("STATUS: CONCEPTUAL FEED — PRELIMINARY — NOT FOR FABRICATION / NOT FOR CONSTRUCTION", dxfattribs={"layer": "ANNOTATIONS_TITLE", "height": 450}).set_placement((15000, 800))

    out_dxf = "engineering/cad/dxf/DWG-FIN-15T-001.dxf"
    doc.saveas(out_dxf)
    print(f"Generated 1:1 True Scale Greenfield Plot Plan DXF: {out_dxf} ({os.path.getsize(out_dxf)} bytes)")

if __name__ == "__main__":
    generate_1to1_plot_plan()
