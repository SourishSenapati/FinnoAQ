import http.server
import socketserver
import threading
import time
import os
import sys
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PORT = 8995
DIRECTORY = 'toor_dal_optimization/portal/dist'

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

def main():
    httpd = socketserver.TCPServer(('127.0.0.1', PORT), QuietHandler)
    t = threading.Thread(target=httpd.serve_forever)
    t.daemon = True
    t.start()
    print(f"HTTP Server started at http://127.0.0.1:{PORT}")

    os.makedirs("reports/portal_audit/v11_3d", exist_ok=True)

    errors = []
    warnings = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 900})
        
        page.on('console', lambda msg: 
                errors.append(f"[{msg.type}] {msg.text}") if msg.type == 'error' 
                else (warnings.append(f"[{msg.type}] {msg.text}") if msg.type == 'warning' else None))
        page.on('pageerror', lambda err: errors.append(f"[PAGE ERROR] {err}"))

        page.goto(f"http://127.0.0.1:{PORT}", wait_until='networkidle')
        time.sleep(1.0)

        print("Page Title:", page.title())
        headline = page.locator("h1").text_content()
        print("Hero Headline:", headline.strip().replace("\n", " "))

        # 1. Full page screenshot
        page.screenshot(path="reports/portal_audit/v11_3d/01_full_page.png", full_page=True)

        # 2. Hero screenshot with 3D model
        hero = page.locator("#hero")
        hero.screenshot(path="reports/portal_audit/v11_3d/02_hero_with_3d.png")

        # Test Hotspot Click
        hotspots = page.locator("#hero button:has-text('+')")
        if hotspots.count() > 0:
            hotspots.first.click()
            time.sleep(0.2)
            print("Hero 3D Hotspot (+) clicked successfully")

        # 3. Arbitrage Workstation
        arb = page.locator("#arbitrage")
        arb.screenshot(path="reports/portal_audit/v11_3d/03_arbitrage.png")

        # 4. Biophysics with Before/After Split Comparator
        bio = page.locator("#biophysics")
        bio.screenshot(path="reports/portal_audit/v11_3d/04_biophysics_split_comparator.png")

        # 5. PFD & Aspen with 3D CAD Render
        pfd = page.locator("#pfd-aspen")
        # Click TK-101A/B
        tk_btn = page.locator("button:has-text('TK-101A/B')")
        if tk_btn.count() > 0:
            tk_btn.first.click()
            time.sleep(0.2)
        pfd.screenshot(path="reports/portal_audit/v11_3d/05_pfd_with_3d_render.png")
        print("PFD 3D CAD Render inspected")

        # 6. Data Room with Lightbox
        data_room = page.locator("#data-room")
        cad_tab = page.locator("button:has-text('TAB 2 // VERIFIED CAD')")
        if cad_tab.count() > 0:
            cad_tab.click()
            time.sleep(0.2)
            # Click thumbnail to open lightbox
            thumb = page.locator("#data-room .cursor-zoom-in")
            if thumb.count() > 0:
                thumb.first.click()
                time.sleep(0.2)
                print("CAD Lightbox opened successfully")
                page.screenshot(path="reports/portal_audit/v11_3d/06_cad_lightbox.png")
                # Close lightbox
                close_btn = page.locator("button:has-text('✕ Close')")
                if close_btn.count() > 0:
                    close_btn.click()
                    time.sleep(0.2)
                    print("CAD Lightbox closed successfully")

        browser.close()

    httpd.shutdown()
    print("\n--- V11 3D PORTAL AUDIT SUMMARY ---")
    print(f"Total Page Errors: {len(errors)}")
    for err in errors:
        print("ERROR:", err)
    print(f"Total Warnings: {len(warnings)}")
    for w in warnings:
        print("WARNING:", w)

if __name__ == '__main__':
    main()
