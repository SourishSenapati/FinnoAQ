"""
V4 Master Final Checksum Manifest Generator.
Computes SHA-256 hashes for all V4 conceptual FEED engineering deliverables.
"""

import os
import hashlib
import json

TARGET_FILES = [
    # 12 CAD DXFs
    "engineering/cad/dxf/DWG-FIN-15T-001.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-002.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-003.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-004.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-005.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-006.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-007.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-008.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-009.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-010.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-011.dxf",
    "engineering/cad/dxf/DWG-FIN-15T-012.dxf",

    # 12 CAD PDFs + SolidWorks Model-Derived
    "engineering/cad/pdf/DWG-FIN-15T-001_PFD.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-002_STREAM_TABLE.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-003_PID_SOAKING.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-004_SITE_PLOT_PLAN.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-005_PID_DRYER.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-006_PID_PACKAGING.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-007_SOAK_TANK_GA.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-007_SOLIDWORKS_MODEL_DERIVED.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-008_DRYER_GA.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-009_DOSING_SKID_GA.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-010_PID_EVAPORATOR.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-011_ELECTRICAL_SLD.pdf",
    "engineering/cad/pdf/DWG-FIN-15T-012_DUST_ZONING.pdf",

    # 3D SolidWorks Master Assembly & Parts
    "engineering/cad/native/PLANT-15T_General_Arrangement.SLDASM",
    "engineering/cad/sldprt/TK-101_Soak_Tank.SLDPRT",
    "engineering/cad/sldprt/AG-101_Agitator.SLDPRT",
    "engineering/cad/sldprt/SK-100_Dosing_Skid.SLDPRT",
    "engineering/cad/sldprt/DR-101_Fluid_Bed_Dryer.SLDPRT",

    # 3D Neutral STEP AP214 Files
    "engineering/cad/step/PLANT-15T_General_Arrangement.step",
    "engineering/cad/step/TK-101_Soak_Tank.step",
    "engineering/cad/step/AG-101_Agitator.step",
    "engineering/cad/step/SK-100_Dosing_Skid.step",
    "engineering/cad/step/DR-101_Fluid_Bed_Dryer.step",

    # Aspen Plus V14 Simulation
    "engineering/aspen/HARAKUTIR_15TPD_CONVERGED.bkp",

    # Verification Audits & Reports
    "engineering/verification/v4/v4_drawing_package_qa_report.json",
    "engineering/verification/v4/v4_solidworks_master_assembly_audit.json",
    "engineering/verification/v4/v4_aspen_process_simulation_audit.json",
    "reports/V4_BASELINE_AND_EXECUTION_PLAN.md",
    "reports/V4_DRAWING_QA_REPORT.md",
    "reports/V4_CAD_GEOMETRY_AND_NATIVE_MODEL_AUDIT.md",
    "reports/V4_BALANCE_AND_ECONOMICS_REPORT.md",
    "reports/V4_STANDARDS_AND_HUMAN_HOLD_POINTS.md",
    "reports/V4_ENGINEERING_ACCEPTANCE_REPORT.md",
]

def generate_manifest():
    manifest = {
        "manifest_version": "V4.0_FINAL",
        "timestamp_iso": "2026-10-15T23:59:59+05:30",
        "governing_directive": "V4 MASTER DIRECTIVE — PROFESSIONAL NATIVE ENGINEERING, OFFLINE-FIRST, EVIDENCE-LOCKED",
        "gate_status": "GATE G-A HOLD STRICTLY ACTIVE",
        "commercial_lot_id": "PENDING_COMMERCIAL_LOT_ID",
        "total_files": 0,
        "files": []
    }

    for rel_path in TARGET_FILES:
        full_path = os.path.abspath(rel_path)
        if not os.path.exists(full_path):
            manifest["files"].append({
                "relative_path": rel_path,
                "status": "FILE_NOT_FOUND"
            })
            continue

        sha256 = hashlib.sha256()
        with open(full_path, "rb") as f:
            while chunk := f.read(65536):
                sha256.update(chunk)

        size_bytes = os.path.getsize(full_path)
        manifest["files"].append({
            "relative_path": rel_path,
            "size_bytes": size_bytes,
            "sha256": sha256.hexdigest(),
            "status": "VERIFIED_LOCKED"
        })

    manifest["total_files"] = len([f for f in manifest["files"] if f.get("status") == "VERIFIED_LOCKED"])
    out_path = os.path.abspath("engineering/verification/v4/v4_final_checksum_manifest.json")
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Computed SHA-256 checksums for {manifest['total_files']} files -> {out_path}")
    return manifest

if __name__ == "__main__":
    generate_manifest()
