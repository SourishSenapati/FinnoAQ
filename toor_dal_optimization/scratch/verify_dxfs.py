import os
import glob
import ezdxf

print("=================================================================")
print("DXF DRAWINGS VERIFICATION REPORT")
print("=================================================================")
for f in sorted(glob.glob("engineering/cad/dxf/*.dxf")):
    if "test" in f:
        continue
    try:
        doc = ezdxf.readfile(f)
        msp = doc.modelspace()
        entity_count = len(list(msp))
        types = sorted(list(set(e.dxftype() for e in msp)))
        insunits = doc.header.get('$INSUNITS', 'None')
        unit_str = "Millimeters" if insunits == 4 else f"Other ({insunits})"
        layers = sorted(list(layer.dxf.name for layer in doc.layers))
        print(f"{os.path.basename(f)}: Entities={entity_count:<4} | Units={unit_str:<12} | Types={types}")
    except Exception as e:
        print(f"{f}: error {e}")
print("=================================================================")
