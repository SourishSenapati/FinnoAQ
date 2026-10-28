import time
import os
import sys
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

URL = "https://portal-nine-self-55.vercel.app"

def main():
    os.makedirs("reports/portal_audit/live_refactored", exist_ok=True)

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
        page.screenshot(path="reports/portal_audit/live_refactored/live_01_full_page.png", full_page=True)
        print("Saved live full page screenshot: reports/portal_audit/live_refactored/live_01_full_page.png")

        # 2. Hero screenshot (Module 1)
        hero = page.locator("#hero")
        hero.screenshot(path="reports/portal_audit/live_refactored/live_02_hero_module.png")
        print("Saved live hero screenshot: reports/portal_audit/live_refactored/live_02_hero_module.png")

        # 3. Arbitrage Workstation (Module 2)
        arb = page.locator("#arbitrage")
        arb.screenshot(path="reports/portal_audit/live_refactored/live_03_arbitrage_workstation.png")
        print("Saved live arbitrage screenshot: reports/portal_audit/live_refactored/live_03_arbitrage_workstation.png")

        # Test Arbitrage sensitivity buttons
        btn_30tpd = page.locator("button:has-text('30 TPD')")
        if btn_30tpd.count() > 0:
            btn_30tpd.first.click()
            time.sleep(0.2)
            print("Live: Clicked 30 TPD button")

        # 4. Biophysics Workbench (Module 3)
        bio = page.locator("#biophysics")
        view_b_btn = page.locator("button:has-text('View B: Forensic')")
        if view_b_btn.count() > 0:
            view_b_btn.click()
            time.sleep(0.2)
            bio.screenshot(path="reports/portal_audit/live_refactored/live_04_biophysics_viewB.png")
            print("Live: Switched to View B")

        # 5. PFD & Aspen Inspector (Module 4)
        pfd = page.locator("#pfd-aspen")
        tk_btn = page.locator("button:has-text('TK-101A/B')")
        if tk_btn.count() > 0:
            tk_btn.first.click()
            time.sleep(0.2)
            print("Live: Clicked TK-101A/B PFD node")
        pfd.screenshot(path="reports/portal_audit/live_refactored/live_05_pfd_aspen.png")
        print("Saved live PFD & Aspen screenshot")

        # 6. Scaleup Roadmap (Module 5)
        roadmap = page.locator("#roadmap")
        phase1_btn = page.locator("button:has-text('Phase 1')")
        if phase1_btn.count() > 0:
            phase1_btn.click()
            time.sleep(0.2)
        roadmap.screenshot(path="reports/portal_audit/live_refactored/live_06_roadmap.png")
        print("Saved live roadmap screenshot")

        # 7. Miller Scoping (Module 6)
        scoping = page.locator("#scoping")
        scoping.screenshot(path="reports/portal_audit/live_refactored/live_07_miller_scoping.png")
        print("Saved live miller scoping screenshot")

        # 8. Data Room (Module 7)
        data_room = page.locator("#data-room")
        cad_tab = page.locator("button:has-text('TAB 2 // VERIFIED CAD')")
        if cad_tab.count() > 0:
            cad_tab.click()
            time.sleep(0.2)
        data_room.screenshot(path="reports/portal_audit/live_refactored/live_08_data_room.png")
        print("Saved live data room screenshot")

        browser.close()

    print("\n--- LIVE PRODUCTION AUDIT SUMMARY ---")
    print(f"Total Page Errors: {len(errors)}")
    for err in errors:
        print("ERROR:", err)
    print(f"Total Warnings: {len(warnings)}")
    for w in warnings:
        print("WARNING:", w)

if __name__ == '__main__':
    main()
