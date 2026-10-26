import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const PORT = 9222;
const TARGET_URL = 'http://127.0.0.1:5174/';
const OUTPUT_DIR = 'D:\\PROJECT\\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\\finnoaq\\toor_dal_optimization\\docs\\project-demo\\screenshots';

const VIEWPORTS = [
  { name: 'desktop_1440x900.png', width: 1440, height: 900, mobile: false },
  { name: 'desktop_1280x800.png', width: 1280, height: 800, mobile: false },
  { name: 'tablet_768x1024.png', width: 768, height: 1024, mobile: true },
  { name: 'mobile_390x844.png', width: 390, height: 844, mobile: true },
  { name: 'mobile_360x800.png', width: 360, height: 800, mobile: true },
];

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function main() {
  console.log('Spawning headless Chrome with remote debugging on port ' + PORT);
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--hide-scrollbars',
    '--disable-background-timer-throttling',
    '--disable-backgrounding-occluded-windows',
    '--disable-renderer-backgrounding',
    'about:blank'
  ]);

  chrome.stderr.on('data', (d) => {
    // console.log('[Chrome Stderr]', d.toString());
  });

  // Wait for debugger endpoint
  let pageTarget = null;
  for (let i = 0; i < 30; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/new?${encodeURIComponent(TARGET_URL)}`, { method: 'PUT' });
      pageTarget = await res.json();
      if (pageTarget && pageTarget.webSocketDebuggerUrl) {
        break;
      }
    } catch (e) {
      await sleep(300);
    }
  }

  if (!pageTarget || !pageTarget.webSocketDebuggerUrl) {
    console.error('Failed to connect to Chrome CDP endpoint');
    chrome.kill();
    process.exit(1);
  }

  console.log('Connected to target:', pageTarget.id);
  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);

  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });

  let messageId = 1;
  const pending = new Map();

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    }
  };

  function sendCommand(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = messageId++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await sendCommand('Page.enable');
  await sendCommand('DOM.enable');
  await sendCommand('CSS.enable');

  // Navigate to target and wait for load
  await sendCommand('Page.navigate', { url: TARGET_URL });
  await sleep(2000); // Allow Three.js and assets to load

  for (const vp of VIEWPORTS) {
    console.log(`Setting viewport: ${vp.width}x${vp.height} (mobile: ${vp.mobile}) -> ${vp.name}`);
    await sendCommand('Emulation.setDeviceMetricsOverride', {
      width: vp.width,
      height: vp.height,
      deviceScaleFactor: 1,
      mobile: vp.mobile
    });
    await sleep(600); // Allow CSS media queries and relayout

    const result = await sendCommand('Page.captureScreenshot', {
      format: 'png',
      captureBeyondViewport: false
    });

    const buffer = Buffer.from(result.data, 'base64');
    const outPath = path.join(OUTPUT_DIR, vp.name);
    fs.writeFileSync(outPath, buffer);
    console.log(`Saved screenshot: ${outPath} (${buffer.length} bytes)`);
  }

  // Also capture full-page desktop screenshot
  console.log('Capturing full-page desktop screenshot...');
  await sendCommand('Emulation.setDeviceMetricsOverride', {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await sleep(400);

  const fullResult = await sendCommand('Page.captureScreenshot', {
    format: 'png',
    captureBeyondViewport: true
  });
  const fullBuffer = Buffer.from(fullResult.data, 'base64');
  fs.writeFileSync(path.join(OUTPUT_DIR, 'desktop_1440_fullpage.png'), fullBuffer);
  console.log(`Saved full page desktop screenshot (${fullBuffer.length} bytes)`);

  ws.close();
  chrome.kill();
  console.log('Visual QA screenshot capture complete!');
}

main().catch((err) => {
  console.error('Error running QA screenshot capture:', err);
  process.exit(1);
});
