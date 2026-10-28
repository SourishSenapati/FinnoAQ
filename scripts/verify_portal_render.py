import http.server
import socketserver
import threading
import time
import os
import sys
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PORT = 8991
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

    os.makedirs("reports/portal_audit", exist_ok=True)

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
        page.screenshot(path="reports/portal_audit/react_01_full_page.png", full_page=True)
        print("Saved full page screenshot: reports/portal_audit/react_01_full_page.png")

        # 2. Hero screenshot
        hero = page.locator("#architecture")
        hero.screenshot(path="reports/portal_audit/react_02_hero_command.png")
        print("Saved hero screenshot: reports/portal_audit/react_02_hero_command.png")

        # 3. Pipeline screenshot
        pipe = page.locator("#pipeline")
        pipe.screenshot(path="reports/portal_audit/react_03_execution_pipeline.png")
        print("Saved pipeline screenshot: reports/portal_audit/react_03_execution_pipeline.png")

        # 4. Comparator screenshot
        comp = page.locator("#comparator")
        comp.screenshot(path="reports/portal_audit/react_04_before_after_comparator.png")
        print("Saved comparator screenshot: reports/portal_audit/react_04_before_after_comparator.png")

        # 5. Bento Guarantees screenshot
        bento = page.locator("#guarantees")
        bento.screenshot(path="reports/portal_audit/react_05_bento_guarantees.png")
        print("Saved bento screenshot: reports/portal_audit/react_05_bento_guarantees.png")

        # 6. Benchmark Matrix screenshot
        bench = page.locator("#benchmarks")
        bench.screenshot(path="reports/portal_audit/react_06_benchmark_matrix.png")
        print("Saved benchmark screenshot: reports/portal_audit/react_06_benchmark_matrix.png")

        # 7. SDK Playground screenshot
        sdk = page.locator("#playground")
        sdk.screenshot(path="reports/portal_audit/react_07_sdk_playground.png")
        print("Saved playground screenshot: reports/portal_audit/react_07_sdk_playground.png")

        # Test interactive buttons
        # Test Fault Injection Toggle
        fault_btn = page.locator("button:has-text('Inject Simulated Fault')")
        if fault_btn.count() > 0:
            fault_btn.click()
            time.sleep(0.3)
            print("Fault button clicked! New text:", page.locator("#guarantees button").first.text_content())

        # Test Comparator Run Simulation
        sim_btn = page.locator("button:has-text('▶ Run Simulation')")
        if sim_btn.count() > 0:
            sim_btn.click()
            print("Run Simulation clicked!")

        # Test SDK Snippet Execute
        exec_btn = page.locator("button:has-text('▶ Execute Snippet')")
        if exec_btn.count() > 0:
            exec_btn.click()
            print("Execute Snippet clicked!")
            time.sleep(1.0)

        browser.close()

    httpd.shutdown()
    print("\n--- AUDIT SUMMARY ---")
    print(f"Total Page Errors: {len(errors)}")
    for err in errors:
        print("ERROR:", err)
    print(f"Total Warnings: {len(warnings)}")
    for w in warnings:
        print("WARNING:", w)

if __name__ == '__main__':
    main()
