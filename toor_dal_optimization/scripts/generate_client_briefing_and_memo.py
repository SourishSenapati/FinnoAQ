# -*- coding: utf-8 -*-
"""
Generates Executive Decision Summary and Client Cover Memo for Proposal Rev V10.
"""

import os
import win32com.client
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

HEX_NAVY = "1A365D"
HEX_STEEL = "2B6CB0"
HEX_BODY = "2D3748"
HEX_CALLOUT = "EDF2F7"
HEX_CALLOUT_BORDER = "3182CE"

COLOR_NAVY = RGBColor(26, 54, 93)
COLOR_STEEL = RGBColor(43, 108, 176)
COLOR_BODY = RGBColor(45, 55, 72)
COLOR_MUTED = RGBColor(113, 128, 150)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'  <w:top w:w="{top}" w:type="dxa"/>'
        f'  <w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'  <w:left w:w="{left}" w:type="dxa"/>'
        f'  <w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="CBD5E0", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_cover_memo():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        
    p_pre = doc.add_paragraph()
    r = p_pre.add_run("FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD.\n")
    r.font.bold = True
    r.font.size = Pt(11.0)
    r.font.color.rgb = COLOR_STEEL
    
    r2 = p_pre.add_run("FORMAL TRANSMITTAL MEMORANDUM & COVER LETTER\n")
    r2.font.bold = True
    r2.font.size = Pt(15.0)
    r2.font.color.rgb = COLOR_NAVY
    
    tbl = doc.add_table(rows=5, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl)
    tbl.columns[0].width = Inches(1.8)
    tbl.columns[1].width = Inches(5.0)
    
    memo_hdr = [
        ("TO:", "Technical Advisory Panel, CEO & Director, Client Organization (Kolkata)"),
        ("FROM:", "Sourish Senapati, Lead Chemical & Process Engineer, FinnoaQ"),
        ("ACADEMIC ADVISORY:", "Technical Advisory Panel, Department of Chemical Engineering, IIT Kharagpur"),
        ("DATE / REF:", "19 October 2026 | Ref: FNQ-PR-2026-001"),
        ("SUBJECT:", "Submission of Phase 1 Scope of Work & Commercial Proposal Rev V10 (Toor Dal Diagnostic Study)")
    ]
    for idx, (lbl, val) in enumerate(memo_hdr):
        row = tbl.rows[idx]
        row.cells[0].paragraphs[0].text = lbl
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[0].paragraphs[0].runs[0].font.size = Pt(8.5)
        row.cells[1].paragraphs[0].text = val
        row.cells[1].paragraphs[0].runs[0].font.size = Pt(8.5)
        set_cell_margins(row.cells[0], top=60, bottom=60, left=80, right=80)
        set_cell_margins(row.cells[1], top=60, bottom=60, left=80, right=80)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(4)
    p.add_run("Dear Dr. Ray,\n\n"
              "We are pleased to formally submit our revised, evidence-gated Phase 1 Scope of Work and Technical-Commercial Proposal (Revision V10) "
              "for the comparative diagnostic study of imported Tanzanian split toor dal versus an Indian benchmark.\n\n"
              "This proposal strictly adheres to the baseline scope, commercial terms, and operational boundaries defined in the primary project SOW, "
              "while correcting previous scientific and numerical discrepancies. Specifically, Revision V10:\n\n"
              "1. Preserves Diagnostic Scope Boundaries: Confirms that Phase 1 is strictly a diagnostic R&D investigation to establish empirical ground truth, "
              "isolate rate-limiting softening barriers, and discriminate across 10 competing scientific hypotheses. Treatment development (Phase 2) and industrial "
              "plant FEED (Phase 4) are formally bounded as gated downstream stages.\n\n"
              "2. Reconciles First-Principles Mass Balances: Independently resolves the pre-dryer moisture and solids-loss contradictions in the provisional 15 MT/day "
              "processing scenario, documenting both Scenario B1 (true 28.0% WB; 3,678 kg/day evap) and Scenario B2 (18,590 kg/day wet stream; 28.77% WB; 3,878 kg/day evap) "
              "and confirming that industrial sizing remains provisional pending empirical Phase 1 laboratory data.\n\n"
              "3. Segregates Chemical Reagents & Dosing: Separates sodium bicarbonate (INS 500(ii)), sodium carbonate (INS 500(i)), trisodium citrate (INS 331(iii)), "
              "and hydrothermal conditioning with exact solution and grain-basis dosing specifications, labeling all candidate formulations as untested Phase 2 research hypotheses.\n\n"
              "4. Confirms Commercial Baseline: Fully validates the indicative professional fee of ₹1,73,000 + applicable GST (ceiling up to ₹2,00,000 + GST), "
              "the 20–25 business day timeline, and the 40% / 40% / 20% milestone schedule.\n\n"
              "To initiate project mobilization, Client Organization is requested to review Section 18 of the proposal, confirm selection of Option 1 (Baseline ₹1.73L) "
              "or Option 2 (Multi-Lot Variation ₹2.85L), and dispatch the requisite 2.5–3.0 kg sample consignments accompanied by the enclosed Metadata Form.\n\n"
              "We thank you for the opportunity to partner on this foundational R&D initiative.\n\n"
              "Sincerely,\n\n"
              "Sourish Senapati\n"
              "Lead Chemical & Process Engineer\n"
              "FinnoaQ Agro-Industrial Technologies Ltd.")
    
    out_docx = r"deliverables\CLIENT_COVER_MEMORANDUM.docx"
    doc.save(out_docx)
    print(f"Saved cover memo DOCX: {out_docx}")
    
    # Save text version
    with open(r"deliverables\CLIENT_COVER_MEMORANDUM.txt", "w", encoding="utf-8") as f:
        f.write(p_pre.text + "\n" + p.text)
    print("Saved cover memo TXT.")

def main():
    build_cover_memo()
    
    # Export to PDF via Word COM
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        in_p = os.path.abspath(r"deliverables\CLIENT_COVER_MEMORANDUM.docx")
        out_p = os.path.abspath(r"deliverables\CLIENT_COVER_MEMORANDUM.pdf")
        d = word.Documents.Open(in_p)
        d.SaveAs(out_p, FileFormat=17)
        d.Close(False)
        print(f"Saved cover memo PDF: {out_p}")
    finally:
        word.Quit()

if __name__ == "__main__":
    main()
