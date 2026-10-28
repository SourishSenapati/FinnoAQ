import http.server
import socketserver
import threading
import time
import os
import sys
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PORT = 8993
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

    os.makedirs("reports/portal_audit/refactored", exist_ok=True)

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
        page.screenshot(path="reports/portal_audit/refactored/01_full_page.png", full_page=True)
        print("Saved full page screenshot: reports/portal_audit/refactored/01_full_page.png")

        # 2. Hero screenshot (Module 1)
        hero = page.locator("#hero")
        hero.screenshot(path="reports/portal_audit/refactored/02_hero_module.png")
        print("Saved hero screenshot: reports/portal_audit/refactored/02_hero_module.png")

        # 3. Arbitrage Workstation (Module 2)
        arb = page.locator("#arbitrage")
        arb.screenshot(path="reports/portal_audit/refactored/03_arbitrage_workstation.png")
        print("Saved arbitrage screenshot: reports/portal_audit/refactored/03_arbitrage_workstation.png")

        # Test Arbitrage sensitivity buttons
        btn_30tpd = page.locator("button:has-text('30 TPD')")
        if btn_30tpd.count() > 0:
            btn_30tpd.first.click()
            time.sleep(0.2)
            print("Clicked 30 TPD button")

        btn_spread28 = page.locator("button:has-text('₹28/kg')")
        if btn_spread28.count() > 0:
            btn_spread28.first.click()
            time.sleep(0.2)
            print("Clicked ₹28/kg spread button")

        # Test CapEx tab in financial drawer
        capex_tab = page.locator("button:has-text('TAB 2 // TURNKEY CAPEX')")
        if capex_tab.count() > 0:
            capex_tab.click()
            time.sleep(0.2)
            print("Clicked CapEx tab")

        # 4. Biophysics Workbench (Module 3)
        bio = page.locator("#biophysics")
        bio.screenshot(path="reports/portal_audit/refactored/04_biophysics_viewA.png")
        print("Saved biophysics view A screenshot: reports/portal_audit/refactored/04_biophysics_viewA.png")

        # Switch to View B
        view_b_btn = page.locator("button:has-text('View B: Forensic')")
        if view_b_btn.count() > 0:
            view_b_btn.click()
            time.sleep(0.2)
            bio.screenshot(path="reports/portal_audit/refactored/04b_biophysics_viewB.png")
            print("Switched to View B and saved screenshot")

        # 5. PFD & Aspen Inspector (Module 4)
        pfd = page.locator("#pfd-aspen")
        # Click SC-101 node
        sc_btn = page.locator("button:has-text('SC-101')")
        if sc_btn.count() > 0:
            sc_btn.first.click()
            time.sleep(0.2)
            print("Clicked SC-101 PFD node")
        pfd.screenshot(path="reports/portal_audit/refactored/05_pfd_aspen.png")
        print("Saved PFD & Aspen screenshot: reports/portal_audit/refactored/05_pfd_aspen.png")

        # 6. Scaleup Roadmap (Module 5)
        roadmap = page.locator("#roadmap")
        phase3_btn = page.locator("button:has-text('Phase 3')")
        if phase3_btn.count() > 0:
            phase3_btn.click()
            time.sleep(0.2)
            print("Clicked Phase 3 in Roadmap")
        roadmap.screenshot(path="reports/portal_audit/refactored/06_roadmap.png")
        print("Saved roadmap screenshot: reports/portal_audit/refactored/06_roadmap.png")

        # 7. Miller Scoping (Module 6)
        scoping = page.locator("#scoping")
        scoping.screenshot(path="reports/portal_audit/refactored/07_miller_scoping.png")
        print("Saved miller scoping screenshot: reports/portal_audit/refactored/07_miller_scoping.png")

        # Test manifest submission
        mill_input = page.locator("input[placeholder*='Sri Balaji']")
        if mill_input.count() > 0:
            mill_input.fill("Sri Balaji Mega Pulses Pvt Ltd (Latur)")
            contact_input = page.locator("input[placeholder*='Rajesh Patil']")
            contact_input.fill("Rajesh Patil, Managing Partner")
            phone_input = page.locator("input[placeholder*='+91 98230']")
            phone_input.fill("+91 98230 45678")
            submit_btn = page.locator("button:has-text('Transmit Diagnostic')")
            submit_btn.click()
            time.sleep(0.3)
            print("Manifest submitted successfully")

        # 8. Data Room (Module 7)
        data_room = page.locator("#data-room")
        cad_tab = page.locator("button:has-text('TAB 2 // VERIFIED CAD')")
        if cad_tab.count() > 0:
            cad_tab.click()
            time.sleep(0.2)
            print("Clicked CAD tab in Data Room")
        data_room.screenshot(path="reports/portal_audit/refactored/08_data_room_cad.png")
        print("Saved data room screenshot: reports/portal_audit/refactored/08_data_room_cad.png")

        browser.close()

    httpd.shutdown()
    print("\n--- REFACTORED PORTAL AUDIT SUMMARY ---")
    print(f"Total Page Errors: {len(errors)}")
    for err in errors:
        print("ERROR:", err)
    print(f"Total Warnings: {len(warnings)}")
    for w in warnings:
        print("WARNING:", w)

if __name__ == '__main__':
    main()
