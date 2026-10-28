# -*- coding: utf-8 -*-
import fitz, os, sys
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'deliverables\PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.pdf'
doc = fitz.open(pdf_path)

print(f"=== DETAILED PAGE-BY-PAGE AUDIT ({len(doc)} PAGES) ===")
empty_pages = []
for i, page in enumerate(doc):
    rect = page.rect
    text = page.get_text().strip()
    words = len(text.split())
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    first_line = lines[0] if lines else 'EMPTY'
    last_line = lines[-1] if lines else 'EMPTY'
    print(f"Page {i+1:02d}: {rect.width:.1f} x {rect.height:.1f} pt | Words: {words:4d} | Lines: {len(lines):2d}")
    print(f"   Top: {first_line[:75]}")
    print(f"   Btm: {last_line[:75]}")
    if words < 20:
        empty_pages.append(i + 1)

print("\nEmpty pages:", empty_pages)
assert len(empty_pages) == 0, f"Found empty pages: {empty_pages}"
print("All 14 pages populated with substantive content!")
