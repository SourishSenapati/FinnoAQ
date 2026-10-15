"""
V4 Master Complete Drawing Package QA & High-Resolution Image Renderer.
Renders all 12 FEED drawing PDFs and native model-derived drawings to 150 DPI PNGs,
performs automated margin and text boundary QA, and writes a structured audit log.
"""

import os
import json
import fitz # PyMuPDF

DRAWINGS = [
    ("DWG-FIN-15T-001", "engineering/cad/pdf/DWG-FIN-15T-001_PFD.pdf", "Process Flow Diagram (PFD)"),
    ("DWG-FIN-15T-002", "engineering/cad/pdf/DWG-FIN-15T-002_STREAM_TABLE.pdf", "Authoritative Stream Table & Balance Schedule"),
    ("DWG-FIN-15T-003", "engineering/cad/pdf/DWG-FIN-15T-003_PID_SOAKING.pdf", "P&ID Soaking Battery & Chemical Dosing"),
    ("DWG-FIN-15T-004", "engineering/cad/pdf/DWG-FIN-15T-004_SITE_PLOT_PLAN.pdf", "Site Master Plot Plan & Hygienic Zoning"),
    ("DWG-FIN-15T-005", "engineering/cad/pdf/DWG-FIN-15T-005_PID_DRYER.pdf", "P&ID Continuous Fluid Bed Dryer & Air Handling"),
    ("DWG-FIN-15T-006", "engineering/cad/pdf/DWG-FIN-15T-006_PID_PACKAGING.pdf", "P&ID Secondary Packaging & Cleanroom Dedusting"),
    ("DWG-FIN-15T-007", "engineering/cad/pdf/DWG-FIN-15T-007_SOAK_TANK_GA.pdf", "Equipment GA - Dal Soaking Vessel TK-101"),
    ("DWG-FIN-15T-008", "engineering/cad/pdf/DWG-FIN-15T-008_DRYER_GA.pdf", "Equipment GA - Continuous Fluid Bed Dryer DR-101"),
    ("DWG-FIN-15T-009", "engineering/cad/pdf/DWG-FIN-15T-009_DOSING_SKID_GA.pdf", "Equipment GA - Chemical Dosing Skid SK-100"),
    ("DWG-FIN-15T-010", "engineering/cad/pdf/DWG-FIN-15T-010_PID_EVAPORATOR.pdf", "P&ID Triple-Effect ZLD Wastewater Evaporator"),
    ("DWG-FIN-15T-011", "engineering/cad/pdf/DWG-FIN-15T-011_ELECTRICAL_SLD.pdf", "Electrical Single-Line Diagram & 415V MCC Distribution"),
    ("DWG-FIN-15T-012", "engineering/cad/pdf/DWG-FIN-15T-012_DUST_ZONING.pdf", "Hazardous Area Classification & Combustible Dust Zoning"),
    ("DWG-FIN-15T-007-SW", "engineering/cad/pdf/DWG-FIN-15T-007_SOLIDWORKS_MODEL_DERIVED.pdf", "SolidWorks 3D Model-Derived Drawing (TK-101)"),
]

def run_qa_and_render():
    qa_results = []
    img_dir = os.path.abspath("engineering/verification/v4/renders")
    os.makedirs(img_dir, exist_ok=True)

    for dwg_id, pdf_path, desc in DRAWINGS:
        if not os.path.exists(pdf_path):
            qa_results.append({
                "dwg": dwg_id,
                "description": desc,
                "status": "FAIL_FILE_NOT_FOUND",
                "pdf_path": pdf_path
            })
            continue

        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=150)
        png_path = os.path.join(img_dir, f"{dwg_id}_render.png")
        pix.save(png_path)

        # Text bounds analysis
        text_blocks = page.get_text("blocks")
        w_pt, h_pt = page.rect.width, page.rect.height
        margin_violations = 0
        latex_errors = 0

        for b in text_blocks:
            bx0, by0, bx1, by1, btext, bno, btype = b
            # Check for margin intrusions (within 4 pt of edge)
            if bx0 < 4 or by0 < 4 or bx1 > w_pt - 4 or by1 > h_pt - 4:
                margin_violations += 1
            # Check for broken raw LaTeX markers
            if any(marker in btext for marker in [r"\frac", r"\text", r"\Delta", r"\sim", "$$"]):
                latex_errors += 1

        status = "PASS" if (margin_violations == 0 and latex_errors == 0) else "FAIL_QA"

        qa_results.append({
            "dwg": dwg_id,
            "description": desc,
            "pdf_path": pdf_path,
            "png_render_path": png_path,
            "page_dimensions_pt": f"{w_pt:.1f} x {h_pt:.1f}",
            "render_pixel_res": f"{pix.width} x {pix.height}",
            "text_blocks_count": len(text_blocks),
            "margin_violations": margin_violations,
            "latex_syntax_errors": latex_errors,
            "visual_qa_status": status
        })

    out_json = os.path.abspath("engineering/verification/v4/v4_drawing_package_qa_report.json")
    with open(out_json, "w") as f:
        json.dump(qa_results, f, indent=2)

    print(json.dumps(qa_results, indent=2))
    return qa_results

if __name__ == "__main__":
    run_qa_and_render()
