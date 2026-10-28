import time
import os
import sys
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

URL = "https://portal-nine-self-55.vercel.app"

def main():
    os.makedirs("reports/portal_audit/live", exist_ok=True)

    errors = []
    warnings = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 900})
        
        page.on('console', lambda msg: 
                errors.append(f"[{msg.type}] {msg.text}") if msg.type == 'error' 
                else (warnings.append(f"[{msg.type}] {msg.text}") if msg.type == 'warning' else None))
        page.on('pageerror', lambda err: errors.append(f"[PAGE ERROR] {err}"))

        print(f"Navigating to live production site: {URL} ...")
        page.goto(URL, wait_until='networkidle')
        time.sleep(1.5)

        print("Page Title:", page.title())
        headline = page.locator("h1").text_content()
        print("Hero Headline:", headline.strip().replace("\n", " "))

        # 1. Full page screenshot
        page.screenshot(path="reports/portal_audit/live/live_01_full_page.png", full_page=True)
        print("Saved live full page screenshot: reports/portal_audit/live/live_01_full_page.png")

        # 2. Hero screenshot
        hero = page.locator("#architecture")
        hero.screenshot(path="reports/portal_audit/live/live_02_hero_command.png")
        print("Saved live hero screenshot: reports/portal_audit/live/live_02_hero_command.png")

        # 3. Pipeline screenshot
        pipe = page.locator("#pipeline")
        pipe.screenshot(path="reports/portal_audit/live/live_03_execution_pipeline.png")
        print("Saved live pipeline screenshot: reports/portal_audit/live/live_03_execution_pipeline.png")

        # 4. Comparator screenshot
        comp = page.locator("#comparator")
        comp.screenshot(path="reports/portal_audit/live/live_04_before_after_comparator.png")
        print("Saved live comparator screenshot: reports/portal_audit/live/live_04_before_after_comparator.png")

        # 5. Bento Guarantees screenshot
        bento = page.locator("#guarantees")
        bento.screenshot(path="reports/portal_audit/live/live_05_bento_guarantees.png")
        print("Saved live bento screenshot: reports/portal_audit/live/live_05_bento_guarantees.png")

        # 6. Benchmark Matrix screenshot
        bench = page.locator("#benchmarks")
        bench.screenshot(path="reports/portal_audit/live/live_06_benchmark_matrix.png")
        print("Saved live benchmark screenshot: reports/portal_audit/live/live_06_benchmark_matrix.png")

        # 7. SDK Playground screenshot
        sdk = page.locator("#playground")
        sdk.screenshot(path="reports/portal_audit/live/live_07_sdk_playground.png")
        print("Saved live playground screenshot: reports/portal_audit/live/live_07_sdk_playground.png")

        # Test interactive buttons
        # Test Fault Injection Toggle
        fault_btn = page.locator("button:has-text('Inject Simulated Fault')")
        if fault_btn.count() > 0:
            fault_btn.click()
            time.sleep(0.3)
            print("Fault button clicked! New text:", page.locator("#guarantees button").first.text_content())
            bento.screenshot(path="reports/portal_audit/live/live_05b_fault_interlock.png")

        # Test Comparator Run Simulation
        sim_btn = page.locator("button:has-text('▶ Run Simulation')")
        if sim_btn.count() > 0:
            sim_btn.click()
            print("Run Simulation clicked!")
            time.sleep(1.0)
            comp.screenshot(path="reports/portal_audit/live/live_04b_sim_running.png")

        # Test SDK Snippet Execute
        exec_btn = page.locator("button:has-text('▶ Execute Snippet')")
        if exec_btn.count() > 0:
            exec_btn.click()
            print("Execute Snippet clicked!")
            time.sleep(1.2)
            sdk.screenshot(path="reports/portal_audit/live/live_07b_snippet_executed.png")

        browser.close()

    print("\n--- LIVE AUDIT SUMMARY ---")
    print(f"Total Page Errors: {len(errors)}")
    for err in errors:
        print("ERROR:", err)
    print(f"Total Warnings: {len(warnings)}")
    for w in warnings:
        print("WARNING:", w)

if __name__ == '__main__':
    main()
