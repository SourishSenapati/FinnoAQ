"""
Generate V5 Cryptographic Checksum Manifest.
Computes SHA-256 hashes and file metadata for all authoritative V5 FEED engineering deliverables.
"""

import os
import hashlib
import json
from datetime import datetime, timezone

WORKSPACE_ROOT = r"d:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization"

def compute_sha256(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def scan_file(rel_path: str):
    full_path = os.path.join(WORKSPACE_ROOT, rel_path)
    if not os.path.exists(full_path):
        return None
    stat = os.stat(full_path)
    return {
        "relative_path": rel_path.replace("\\", "/"),
        "sha256": compute_sha256(full_path),
        "size_bytes": stat.st_size,
        "last_modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
    }

def build_manifest():
    manifest = {
        "manifest_metadata": {
            "title": "V5 Master Cryptographic Checksum Manifest",
            "standard": "V5 Master Directive Section 1(E) Cryptographic Lock",
            "generated_timestamp": datetime.now(timezone.utc).isoformat(),
            "target_plant": "15,000 kg/day Greenfield Imported Pigeon Pea Optimization Facility",
            "git_branch": "v5-integrated-engineering",
            "hash_algorithm": "SHA-256",
            "gate_status": "GATE G-A HOLD ACTIVE"
        },
        "master_data": [],
        "native_cad_models": [],
        "step_models": [],
        "vector_drawings_pdf": [],
        "vector_drawings_dxf": [],
        "simulation_models": [],
        "v5_verification_and_tools": [],
        "v5_reports": []
    }

    # 1. Master Data
    master_data_dir = os.path.join(WORKSPACE_ROOT, "engineering", "master_data")
    if os.path.exists(master_data_dir):
        for fname in sorted(os.listdir(master_data_dir)):
            if fname.endswith(".json"):
                info = scan_file(os.path.join("engineering", "master_data", fname))
                if info:
                    manifest["master_data"].append(info)

    # 2. Native CAD models
    cad_files = [
        os.path.join("engineering", "cad", "native", "PLANT-15T_General_Arrangement.SLDASM"),
        os.path.join("engineering", "cad", "sldprt", "TK-101_Soak_Tank.SLDPRT"),
        os.path.join("engineering", "cad", "sldprt", "DR-101_Fluid_Bed_Dryer.SLDPRT"),
        os.path.join("engineering", "cad", "sldprt", "SK-100_Dosing_Skid.SLDPRT"),
        os.path.join("engineering", "cad", "sldprt", "AG-101_Agitator.SLDPRT"),
    ]
    for rel in cad_files:
        info = scan_file(rel)
        if info:
            manifest["native_cad_models"].append(info)

    # 3. STEP models
    step_dir = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "step")
    if os.path.exists(step_dir):
        for fname in sorted(os.listdir(step_dir)):
            if fname.endswith(".step"):
                info = scan_file(os.path.join("engineering", "cad", "step", fname))
                if info:
                    manifest["step_models"].append(info)

    # 4. Drawing PDFs
    pdf_dir = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "pdf")
    if os.path.exists(pdf_dir):
        for fname in sorted(os.listdir(pdf_dir)):
            if fname.startswith("DWG-FIN-15T-") and fname.endswith(".pdf"):
                info = scan_file(os.path.join("engineering", "cad", "pdf", fname))
                if info:
                    manifest["vector_drawings_pdf"].append(info)

    # 5. Drawing DXFs
    dxf_dir = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "dxf")
    if os.path.exists(dxf_dir):
        for fname in sorted(os.listdir(dxf_dir)):
            if fname.startswith("DWG-FIN-15T-") and fname.endswith(".dxf"):
                info = scan_file(os.path.join("engineering", "cad", "dxf", fname))
                if info:
                    manifest["vector_drawings_dxf"].append(info)

    # 6. Simulation models
    sim_files = [
        os.path.join("engineering", "aspen", "HARAKUTIR_15TPD_CONVERGED.bkp"),
        os.path.join("data", "stream_tables_15tpd.json")
    ]
    for rel in sim_files:
        info = scan_file(rel)
        if info:
            manifest["simulation_models"].append(info)

    # 7. Verification & Tools
    tool_files = [
        os.path.join("engineering", "verification", "v5", "v5_toolchain_inventory.json"),
        os.path.join("engineering", "verification", "v5", "v5_integration_acceptance_report.json"),
        os.path.join("scripts", "v5_integration_checker.py"),
        os.path.join("scripts", "generate_and_validate_master_data.py")
    ]
    for rel in tool_files:
        info = scan_file(rel)
        if info:
            manifest["v5_verification_and_tools"].append(info)

    # 8. V5 Reports
    v5_reports = [
        os.path.join("reports", "V5_BASELINE_AND_INTEGRATION_PLAN.md"),
        os.path.join("reports", "V5_ENGINEERING_ACCEPTANCE_REPORT.md"),
        os.path.join("reports", "V5_DRAWING_QA_REPORT.md"),
        os.path.join("reports", "V5_BALANCE_AND_ECONOMICS_REPORT.md"),
        os.path.join("reports", "V5_CAD_GEOMETRY_AND_NATIVE_MODEL_AUDIT.md"),
        os.path.join("reports", "V5_STANDARDS_AND_HUMAN_HOLD_POINTS.md"),
        os.path.join("reports", "V5_CROSS_DISCIPLINE_DESIGN_REVIEWS.md"),
        os.path.join("NEW_CHAT_HANDOVER_DIRECTIVE.md")
    ]
    for rel in v5_reports:
        info = scan_file(rel)
        if info:
            manifest["v5_reports"].append(info)

    total_files = sum(len(manifest[k]) for k in manifest if k != "manifest_metadata")
    manifest["manifest_metadata"]["total_locked_files"] = total_files

    out_path = os.path.join(WORKSPACE_ROOT, "engineering", "verification", "v5", "v5_final_checksum_manifest.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Cryptographic manifest generated successfully at: {out_path}")
    print(f"Total locked artifacts: {total_files}")
    for section, items in manifest.items():
        if section != "manifest_metadata":
            print(f"  - {section}: {len(items)} files")

if __name__ == "__main__":
    build_manifest()
