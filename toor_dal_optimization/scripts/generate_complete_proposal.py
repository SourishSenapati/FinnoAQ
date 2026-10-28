# -*- coding: utf-8 -*-
"""
V10 MASTER PROPOSAL GENERATOR (COMPLETE)
Generates: deliverables/PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.docx
Governed by: V10 Master Directive, AGENTS.md, and Phase1_Scope_of_Work_Toor_Dal.docx
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# Typography & Palette
HEX_NAVY = "1A365D"       # Deep Corporate Navy (#1A365D)
HEX_STEEL = "2B6CB0"      # Slate Accent Blue (#2B6CB0)
HEX_BODY = "2D3748"       # Dark Slate Charcoal (#2D3748)
HEX_BG_ALT = "F7FAFC"     # Subtle Grey Zebra (#F7FAFC)
HEX_BORDER = "CBD5E0"     # Border (#CBD5E0)
HEX_CALLOUT = "EDF2F7"    # Callout Background (#EDF2F7)
HEX_CALLOUT_BORDER = "3182CE"
HEX_WHITE = "FFFFFF"

COLOR_NAVY = RGBColor(26, 54, 93)
COLOR_STEEL = RGBColor(43, 108, 176)
COLOR_BODY = RGBColor(45, 55, 72)
COLOR_MUTED = RGBColor(113, 128, 150)

def set_cell_margins(cell, top=80, bottom=80, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="CBD5E0", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_header_row(row, bg_hex=HEX_NAVY):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    for cell in row.cells:
        set_cell_shading(cell, bg_hex)
        set_cell_margins(cell, top=100, bottom=100, left=110, right=110)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(8.0)
                run.font.name = "Calibri"

def make_data_row(row, is_zebra=False, font_size=7.5):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    bg = HEX_BG_ALT if is_zebra else HEX_WHITE
    for cell in row.cells:
        if is_zebra:
            set_cell_shading(cell, bg)
        set_cell_margins(cell, top=65, bottom=65, left=110, right=110)
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.size = Pt(font_size)
                run.font.name = "Calibri"
                run.font.color.rgb = COLOR_BODY

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(13)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(12.0)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_STEEL
    return p

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_BODY
    return p

def add_p(doc, text, bold_prefix=None, space_after=3):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(9.0)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(9.0)
    r.font.color.rgb = COLOR_BODY
    return p

def add_callout(doc, text, heading="SCOPE SPECIFICATION & DIAGNOSTIC DIRECTIVE"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.0)
    
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, HEX_CALLOUT)
    set_cell_margins(cell, top=90, bottom=90, left=160, right=130)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_CALLOUT_BORDER}"/>'
        f'  <w:top w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    run_h = p.add_run(f"[{heading}]\n")
    run_h.font.bold = True
    run_h.font.size = Pt(8.5)
    run_h.font.color.rgb = COLOR_NAVY
    run_h.font.name = "Calibri"
    
    run_b = p.add_run(text)
    run_b.font.size = Pt(8.0)
    run_b.font.italic = True
    run_b.font.color.rgb = COLOR_BODY
    run_b.font.name = "Calibri"
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(3)

def setup_page_header_footer(doc):
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)
        
        # Header
        hdr = s.header
        p_hdr = hdr.paragraphs[0]
        p_hdr.text = "FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES  |  TECHNICAL & COMMERCIAL PROPOSAL  |  REV V10"
        p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_hdr.paragraph_format.space_after = Pt(4)
        for r in p_hdr.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_MUTED
            
        # Footer
        ftr = s.footer
        p_ftr = ftr.paragraphs[0]
        p_ftr.text = "CONFIDENTIAL  —  PREPARED FOR Client Organization (KOLKATA)  |  REF: FNQ-PR-2026-001"
        p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p_ftr.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_MUTED

print("Base setup verified in generate_complete_proposal.py")
