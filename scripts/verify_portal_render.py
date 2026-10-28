import http.server
import socketserver
import threading
import time
import os
import sys
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PORT = 8996
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

    os.makedirs("reports/portal_audit/solidworks_3d", exist_ok=True)

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
        time.sleep(1.5)

        print("Page Title:", page.title())

        # Test SolidWorks 3D CAD Workstation
        cad_section = page.locator("#solidworks-cad")
        if cad_section.count() > 0:
            print("Found #solidworks-cad workstation")
            cad_section.screenshot(path="reports/portal_audit/solidworks_3d/01_cad_assembly.png")
            print("Saved 3D Assembly CAD screenshot")

            # Test Camera Presets
            page.locator("button:has-text('[ISO]')").click()
            time.sleep(0.3)
            page.locator("button:has-text('[FRONT]')").click()
            time.sleep(0.3)
            page.locator("button:has-text('[TOP]')").click()
            time.sleep(0.3)
            print("Camera view angle presets tested: ISO, FRONT, TOP")

            # Test Display Modes
            page.locator("button:has-text('Wireframe')").click()
            time.sleep(0.3)
            page.locator("button:has-text('Turntable')").click()
            time.sleep(0.3)
            print("Display modes tested: Wireframe & Turntable")

            # Test Model Switch to TK-101
            tk_btn = page.locator("#solidworks-cad button:has-text('TK-101A/B')")
            if tk_btn.count() > 0:
                tk_btn.first.click()
                time.sleep(1.0)
                cad_section.screenshot(path="reports/portal_audit/solidworks_3d/02_cad_tk101.png")
                print("Switched model to TK-101A/B and captured screenshot")

        browser.close()

    httpd.shutdown()
    print("\n--- SOLIDWORKS 3D CAD AUDIT SUMMARY ---")
    print(f"Total Page Errors: {len(errors)}")
    for err in errors:
        print("ERROR:", err)
    print(f"Total Warnings: {len(warnings)}")
    for w in warnings:
        print("WARNING:", w)

if __name__ == '__main__':
    main()
