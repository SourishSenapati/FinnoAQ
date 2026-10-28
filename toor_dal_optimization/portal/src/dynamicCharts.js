// FinnoaQ Dynamic Vector Graphics & Interactive Financial Simulator
// Standard: Institutional Deep-Tech Editorial Aesthetic (Anthropic / Google Research style)
// Zero external charting dependencies — Pure, responsive, retina-sharp SVG

export function initDynamicVisualizations() {
  renderInteractiveArbitrageWaterfall('chart-arbitrage-waterfall');
  renderBiophysicsKineticsChart('chart-biophysics-kinetics');
  renderFiveYearFinancialChart('chart-five-year-financials');
  renderInteractiveMillSimulator('interactive-mill-calculator');
  renderInteractiveProcessArchitecture('process-architecture-diagram');
}

// ============================================================================
// 1. DYNAMIC MANDI ARBITRAGE WATERFALL CHART
// ============================================================================
export function renderInteractiveArbitrageWaterfall(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const data = [
    { label: "African HTC Infeed", val: 85.00, type: "base", color: "#64748B", desc: "Mandi port wholesale landing price" },
    { label: "S1-09 Reagents", val: 2.22, type: "step", color: "#F59E0B", desc: "Citrate, citric acid, SHMP (85% recycle)" },
    { label: "Biomass Steam", val: 2.12, type: "step", color: "#F59E0B", desc: "250 kg/h boiler @ ₹3.50/kg briquettes" },
    { label: "Electric Power", val: 0.72, type: "step", color: "#F59E0B", desc: "54.2 kW connected load @ ₹8.50/kWh" },
    { label: "Labor & O&M", val: 1.28, type: "step", color: "#F59E0B", desc: "Technicians, ZLD water, maintenance" },
    { label: "FinnoaQ Margin", val: 5.66, type: "step", color: "#38BDF8", desc: "Technology & operations gross profit" },
    { label: "Partner Net Lift", val: 8.00, type: "step", color: "#10B981", desc: "Pure profit captured by dal miller" },
    { label: "Finished Dal Parity", val: 105.00, type: "total", color: "#FBBF24", desc: "Domestic Indian Latur Desi wholesale" }
  ];

  const width = 840;
  const height = 340;
  const margin = { top: 30, right: 30, bottom: 65, left: 55 };
  const chartW = width - margin.left - margin.right;
  const chartH = height - margin.top - margin.bottom;

  const minY = 75;
  const maxY = 115;
  const scaleY = (v) => chartH - ((v - minY) / (maxY - minY)) * chartH;
  const barW = Math.floor(chartW / data.length) - 14;

  let currentY = 85.00;
  const bars = data.map((d, i) => {
    const x = margin.left + i * (barW + 14);
    let yTop, yHeight, prevY = currentY;

    if (d.type === "base") {
      yTop = scaleY(d.val);
      yHeight = chartH - yTop;
      currentY = d.val;
    } else if (d.type === "step") {
      const nextY = currentY + d.val;
      yTop = scaleY(nextY);
      yHeight = Math.abs(scaleY(nextY) - scaleY(currentY));
      currentY = nextY;
    } else { // total
      yTop = scaleY(d.val);
      yHeight = chartH - yTop;
    }

    return {
      ...d,
      x,
      y: yTop,
      h: Math.max(yHeight, 3),
      prevY,
      nextY: currentY
    };
  });

  const gridLines = [80, 90, 100, 110].map(val => `
    <line x1="${margin.left}" y1="${margin.top + scaleY(val)}" x2="${margin.left + chartW}" y2="${margin.top + scaleY(val)}" stroke="#1E293B" stroke-dasharray="3,3" />
    <text x="${margin.left - 10}" y="${margin.top + scaleY(val) + 4}" fill="#64748B" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="end">₹${val}</text>
  `).join('');

  const svgBars = bars.map((b, i) => {
    const connectLine = (i > 0 && i < bars.length - 1) ? `
      <line x1="${b.x - 14}" y1="${margin.top + b.y + b.h}" x2="${b.x}" y2="${margin.top + b.y + b.h}" stroke="#475569" stroke-dasharray="2,2" />
    ` : '';

    return `
      <g class="wf-bar-group" data-label="${b.label}" data-val="₹${b.val.toFixed(2)}" data-desc="${b.desc}">
        ${connectLine}
        <rect x="${b.x}" y="${margin.top + b.y}" width="${barW}" height="${b.h}" fill="${b.color}" rx="3" style="cursor:pointer; transition:opacity 0.2s;" />
        <text x="${b.x + barW / 2}" y="${margin.top + b.y - 8}" fill="#F8FAFC" font-size="11" font-weight="600" font-family="'JetBrains Mono', monospace" text-anchor="middle">
          ${b.type === 'step' ? '+' : ''}₹${b.val.toFixed(2)}
        </text>
        <text x="${b.x + barW / 2}" y="${margin.top + chartH + 18}" fill="#94A3B8" font-size="10.5" font-weight="500" text-anchor="middle" transform="rotate(0, ${b.x + barW / 2}, ${margin.top + chartH + 18})">
          ${b.label}
        </text>
      </g>
    `;
  }).join('');

  container.innerHTML = `
    <div class="dynamic-chart-card">
      <div class="chart-header">
        <div>
          <span class="chart-badge">DYNAMIC VALUE DECOMPOSITION</span>
          <h4 class="chart-title">Mandi Arbitrage Unit Economics Waterfall (₹/kg)</h4>
        </div>
        <div class="chart-legend">
          <span class="legend-pill" style="--c:#64748B">Base Intake</span>
          <span class="legend-pill" style="--c:#F59E0B">Direct OpEx (₹6.34)</span>
          <span class="legend-pill" style="--c:#38BDF8">Tolling Margin (₹5.66)</span>
          <span class="legend-pill" style="--c:#10B981">Miller Lift (+₹8.00)</span>
        </div>
      </div>
      <div class="chart-svg-wrap">
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg" preserveAspectRatio="xMidYMid meet">
          ${gridLines}
          ${svgBars}
        </svg>
        <div class="chart-tooltip is-hidden" id="wf-tooltip"></div>
      </div>
      <div class="chart-caption-bar">
        <span><strong>Key Takeaway:</strong> African imported dal bought at ₹85.00/kg processed at ₹6.34 direct OpEx unlocks ₹8.00/kg (₹3.60 Cr/yr) in net miller value lift.</span>
      </div>
    </div>
  `;

  // Attach hover tooltip
  const tooltip = container.querySelector('#wf-tooltip');
  container.querySelectorAll('.wf-bar-group').forEach(grp => {
    grp.addEventListener('mouseenter', (e) => {
      const label = grp.dataset.label;
      const val = grp.dataset.val;
      const desc = grp.dataset.desc;
      tooltip.innerHTML = `<strong>${label}: ${val}</strong><br><span style="color:#94A3B8; font-size:0.8rem;">${desc}</span>`;
      tooltip.classList.remove('is-hidden');
    });
    grp.addEventListener('mousemove', (e) => {
      const rect = container.getBoundingClientRect();
      tooltip.style.left = `${e.clientX - rect.left + 15}px`;
      tooltip.style.top = `${e.clientY - rect.top - 35}px`;
    });
    grp.addEventListener('mouseleave', () => {
      tooltip.classList.add('is-hidden');
    });
  });
}

// ============================================================================
// 2. DYNAMIC BIOPHYSICS KINETICS CHART (CALCIUM CHELATION & CORE HARDNESS)
// ============================================================================
export function renderBiophysicsKineticsChart(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const width = 840;
  const height = 340;
  const margin = { top: 30, right: 60, bottom: 50, left: 60 };
  const chartW = width - margin.left - margin.right;
  const chartH = height - margin.top - margin.bottom;

  // Kinetic time series (t: min, ca: % extracted, force: N)
  const timePoints = [
    { t: 0, ca: 0.0, force: 48.5 },
    { t: 4, ca: 14.2, force: 39.4 },
    { t: 8, ca: 24.8, force: 31.0 },
    { t: 12, ca: 31.6, force: 24.8 },
    { t: 16, ca: 36.2, force: 20.4 },
    { t: 20, ca: 39.5, force: 17.35 }, // Stage 1 nominal
    { t: 24, ca: 41.8, force: 15.2 },  // Stage 3 robust optimum
    { t: 28, ca: 42.9, force: 14.8 },
    { t: 30, ca: 43.4, force: 14.5 }
  ];

  const scaleX = (t) => margin.left + (t / 30) * chartW;
  const scaleCa = (ca) => margin.top + chartH - (ca / 50) * chartH;
  const scaleForce = (f) => margin.top + chartH - ((f - 10) / (50 - 10)) * chartH;

  const caPath = "M " + timePoints.map(p => `${scaleX(p.t)},${scaleCa(p.ca)}`).join(' L ');
  const forcePath = "M " + timePoints.map(p => `${scaleX(p.t)},${scaleForce(p.force)}`).join(' L ');

  // Target threshold line (18.0 N)
  const y18N = scaleForce(18.0);
  const targetLine = `
    <line x1="${margin.left}" y1="${y18N}" x2="${margin.left + chartW}" y2="${y18N}" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="4,4" />
    <text x="${margin.left + chartW - 5}" y="${y18N - 6}" fill="#EF4444" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="end">2-Whistle Cookability Threshold (≤ 18.0 N)</text>
  `;

  // Gridlines
  const gridX = [0, 5, 10, 15, 20, 24, 30].map(t => `
    <line x1="${scaleX(t)}" y1="${margin.top}" x2="${scaleX(t)}" y2="${margin.top + chartH}" stroke="#1E293B" stroke-dasharray="2,2" />
    <text x="${scaleX(t)}" y="${margin.top + chartH + 18}" fill="#64748B" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="middle">${t}m</text>
  `).join('');

  const gridYLeft = [0, 10, 20, 30, 40, 50].map(ca => `
    <text x="${margin.left - 10}" y="${scaleCa(ca) + 4}" fill="#38BDF8" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="end">${ca}%</text>
  `).join('');

  const gridYRight = [15, 20, 30, 40, 50].map(f => `
    <text x="${margin.left + chartW + 10}" y="${scaleForce(f) + 4}" fill="#F59E0B" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="start">${f}N</text>
  `).join('');

  // 24 min optimum callout
  const p24 = timePoints.find(p => p.t === 24);
  const marker24 = `
    <circle cx="${scaleX(24)}" cy="${scaleCa(p24.ca)}" r="5" fill="#38BDF8" stroke="#0F172A" stroke-width="2" />
    <circle cx="${scaleX(24)}" cy="${scaleForce(p24.force)}" r="5" fill="#10B981" stroke="#0F172A" stroke-width="2" />
    <line x1="${scaleX(24)}" y1="${margin.top}" x2="${scaleX(24)}" y2="${margin.top + chartH}" stroke="#10B981" stroke-width="1.5" stroke-dasharray="3,3" />
    <rect x="${scaleX(24) - 55}" y="${margin.top + 8}" width="110" height="24" rx="4" fill="#064E3B" stroke="#10B981" />
    <text x="${scaleX(24)}" y="${margin.top + 24}" fill="#6EE7B7" font-size="10.5" font-weight="600" font-family="'JetBrains Mono', monospace" text-anchor="middle">24 min OPTIMUM</text>
  `;

  container.innerHTML = `
    <div class="dynamic-chart-card">
      <div class="chart-header">
        <div>
          <span class="chart-badge">TRANSIENT MULTIPHYSICS DYNAMICS</span>
          <h4 class="chart-title">Calcium Extraction vs Cotyledon Firmness (24-Min Chelation Curve)</h4>
        </div>
        <div class="chart-legend">
          <span class="legend-pill" style="--c:#38BDF8">Bound Ca²+ Extracted (%)</span>
          <span class="legend-pill" style="--c:#F59E0B">Core Shear Force (N)</span>
          <span class="legend-pill" style="--c:#EF4444">18N Limit Threshold</span>
        </div>
      </div>
      <div class="chart-svg-wrap">
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg" preserveAspectRatio="xMidYMid meet">
          ${gridX}
          ${gridYLeft}
          ${gridYRight}
          ${targetLine}
          <path d="${caPath}" fill="none" stroke="#38BDF8" stroke-width="2.5" stroke-linecap="round" />
          <path d="${forcePath}" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-linecap="round" />
          ${marker24}
        </svg>
      </div>
      <div class="chart-caption-bar">
        <span><strong>Physics Grounding:</strong> Ultrasound (25 kHz, 1.8 W/cm²) thins acoustic boundary layer by 73%, driving 41.8% calcium extraction and reducing core hardness to 15.2 N (passing 2-whistle criterion).</span>
      </div>
    </div>
  `;
}

// ============================================================================
// 3. DYNAMIC 5-YEAR FINANCIAL CASH FLOW & EBITDA CHART
// ============================================================================
export function renderFiveYearFinancialChart(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const data = [
    { year: "Year 1 (33%)", rev: 180.0, opex: 95.1, ebitda: 84.9 },
    { year: "Year 2 (60%)", rev: 324.0, opex: 171.2, ebitda: 152.8 },
    { year: "Year 3 (90%)", rev: 486.0, opex: 256.8, ebitda: 229.2 },
    { year: "Year 4 (90%)", rev: 510.3, opex: 269.6, ebitda: 240.7 },
    { year: "Year 5 (90%)", rev: 535.8, opex: 283.1, ebitda: 252.7 }
  ];

  const width = 840;
  const height = 320;
  const margin = { top: 30, right: 30, bottom: 50, left: 55 };
  const chartW = width - margin.left - margin.right;
  const chartH = height - margin.top - margin.bottom;

  const maxVal = 600;
  const scaleY = (v) => chartH - (v / maxVal) * chartH;
  const groupW = chartW / data.length;
  const subBarW = (groupW - 30) / 3;

  const gridY = [0, 150, 300, 450, 600].map(v => `
    <line x1="${margin.left}" y1="${margin.top + scaleY(v)}" x2="${margin.left + chartW}" y2="${margin.top + scaleY(v)}" stroke="#1E293B" stroke-dasharray="2,2" />
    <text x="${margin.left - 10}" y="${margin.top + scaleY(v) + 4}" fill="#64748B" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="end">₹${v}L</text>
  `).join('');

  const groups = data.map((d, i) => {
    const gx = margin.left + i * groupW + 15;
    return `
      <g class="fin-group">
        <!-- Revenue Bar -->
        <rect x="${gx}" y="${margin.top + scaleY(d.rev)}" width="${subBarW}" height="${chartH - scaleY(d.rev)}" fill="#38BDF8" rx="2" />
        <text x="${gx + subBarW / 2}" y="${margin.top + scaleY(d.rev) - 6}" fill="#94A3B8" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">₹${d.rev.toFixed(0)}</text>
        
        <!-- OpEx Bar -->
        <rect x="${gx + subBarW + 2}" y="${margin.top + scaleY(d.opex)}" width="${subBarW}" height="${chartH - scaleY(d.opex)}" fill="#64748B" rx="2" />
        
        <!-- EBITDA Bar -->
        <rect x="${gx + (subBarW + 2) * 2}" y="${margin.top + scaleY(d.ebitda)}" width="${subBarW}" height="${chartH - scaleY(d.ebitda)}" fill="#10B981" rx="2" />
        <text x="${gx + (subBarW + 2) * 2 + subBarW / 2}" y="${margin.top + scaleY(d.ebitda) - 6}" fill="#34D399" font-size="10.5" font-weight="600" font-family="'JetBrains Mono', monospace" text-anchor="middle">₹${d.ebitda.toFixed(0)}</text>

        <!-- X Label -->
        <text x="${gx + (groupW - 30) / 2}" y="${margin.top + chartH + 20}" fill="#94A3B8" font-size="11" font-weight="500" text-anchor="middle">${d.year}</text>
      </g>
    `;
  }).join('');

  container.innerHTML = `
    <div class="dynamic-chart-card">
      <div class="chart-header">
        <div>
          <span class="chart-badge">5-YEAR DISCOUNTED PROJECTIONS</span>
          <h4 class="chart-title">Revenue, Operating Costs & EBITDA Growth (₹ Lakhs)</h4>
        </div>
        <div class="chart-legend">
          <span class="legend-pill" style="--c:#38BDF8">Tolling Revenue</span>
          <span class="legend-pill" style="--c:#64748B">Operating Costs</span>
          <span class="legend-pill" style="--c:#10B981">EBITDA (47.2% Margin)</span>
        </div>
      </div>
      <div class="chart-svg-wrap">
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg" preserveAspectRatio="xMidYMid meet">
          ${gridY}
          ${groups}
        </svg>
      </div>
      <div class="chart-caption-bar">
        <span><strong>Return Metrics:</strong> 78.4% 5-Year IRR &bull; 1.12-Year Capital Payback &bull; ₹135.0 Lakhs Turnkey Line CapEx &bull; 18.7% Breakeven Operating Capacity.</span>
      </div>
    </div>
  `;
}

// ============================================================================
// 4. INTERACTIVE LIVE MILL UNIT ECONOMICS & CAPACITY SIMULATOR
// ============================================================================
export function renderInteractiveMillSimulator(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = `
    <div class="simulator-card">
      <div class="sim-header">
        <span class="section-eyebrow" style="color:var(--accent-gold);">DYNAMIC SENSITIVITY ENGINE</span>
        <h3 class="sim-title">Live Commercial Mill ROI & Tolling Profit Simulator</h3>
        <p class="sim-desc">Adjust the daily plant capacity, wholesale mandi spread, and tolling split to model custom cash flow yields for partner mills.</p>
      </div>

      <div class="sim-controls-grid">
        <div class="sim-slider-box">
          <div class="slider-label-row">
            <span>Plant Daily Capacity</span>
            <strong id="val-capacity" class="slider-value">15 TPD</strong>
          </div>
          <input type="range" min="5" max="30" step="1" value="15" id="slider-capacity" class="fin-slider" />
          <div class="slider-bounds"><span>5 TPD (Pilot)</span><span>15 TPD (Reference)</span><span>30 TPD (Commercial)</span></div>
        </div>

        <div class="sim-slider-box">
          <div class="slider-label-row">
            <span>Mandi Wholesale Price Spread</span>
            <strong id="val-spread" class="slider-value">₹20.00 / kg</strong>
          </div>
          <input type="range" min="14" max="28" step="1" value="20" id="slider-spread" class="fin-slider" />
          <div class="slider-bounds"><span>₹14/kg (Conservative)</span><span>₹20/kg (Audited)</span><span>₹28/kg (Peak Gap)</span></div>
        </div>

        <div class="sim-slider-box">
          <div class="slider-label-row">
            <span>Annual Operating Days</span>
            <strong id="val-days" class="slider-value">300 Days</strong>
          </div>
          <input type="range" min="200" max="330" step="10" value="300" id="slider-days" class="fin-slider" />
          <div class="slider-bounds"><span>200 Days</span><span>300 Days</span><span>330 Days (Continuous)</span></div>
        </div>
      </div>

      <div class="sim-results-grid">
        <div class="sim-metric-card highlight-gold">
          <span class="sm-label">TOTAL VALUE ARBITRAGE POOL</span>
          <span class="sm-val" id="metric-total-pool">₹9.00 Cr / yr</span>
          <span class="sm-sub" id="metric-total-daily">₹3,00,000 / operating day</span>
        </div>

        <div class="sim-metric-card highlight-green">
          <span class="sm-label">PARTNER MILLER NET PROFIT LIFT</span>
          <span class="sm-val" id="metric-miller-profit">₹3.60 Cr / yr</span>
          <span class="sm-sub" id="metric-miller-unit">+₹8.00/kg clean arbitrage margin</span>
        </div>

        <div class="sim-metric-card highlight-blue">
          <span class="sm-label">FINNOAQ TOLLING REVENUE</span>
          <span class="sm-val" id="metric-finnoaq-rev">₹5.40 Cr / yr</span>
          <span class="sm-sub" id="metric-finnoaq-ebitda">₹2.55 Cr / yr Net EBITDA (47.2%)</span>
        </div>

        <div class="sim-metric-card">
          <span class="sm-label">CAPEX PAYBACK PERIOD</span>
          <span class="sm-val" id="metric-payback">1.12 Years</span>
          <span class="sm-sub">On ₹135.0 Lakhs Turnkey Skid</span>
        </div>
      </div>
    </div>
  `;

  const sCap = container.querySelector('#slider-capacity');
  const sSpread = container.querySelector('#slider-spread');
  const sDays = container.querySelector('#slider-days');

  const lCap = container.querySelector('#val-capacity');
  const lSpread = container.querySelector('#val-spread');
  const lDays = container.querySelector('#val-days');

  const mTotalPool = container.querySelector('#metric-total-pool');
  const mTotalDaily = container.querySelector('#metric-total-daily');
  const mMillerProfit = container.querySelector('#metric-miller-profit');
  const mMillerUnit = container.querySelector('#metric-miller-unit');
  const mFinnoaqRev = container.querySelector('#metric-finnoaq-rev');
  const mFinnoaqEbitda = container.querySelector('#metric-finnoaq-ebitda');
  const mPayback = container.querySelector('#metric-payback');

  function update() {
    const capTPD = parseFloat(sCap.value);
    const spread = parseFloat(sSpread.value);
    const days = parseFloat(sDays.value);

    lCap.textContent = `${capTPD} TPD`;
    lSpread.textContent = `₹${spread.toFixed(2)} / kg`;
    lDays.textContent = `${days} Days`;

    const totalKgDay = capTPD * 1000;
    const totalDailyVal = totalKgDay * spread;
    const totalAnnualCr = (totalDailyVal * days) / 10000000;

    // Fixed OpEx per kg: ₹6.34
    // FinnoaQ Tolling Fee: 60% of spread = spread * 0.60
    // Miller Net Lift: 40% of spread = spread * 0.40
    const tollingFee = spread * 0.60;
    const millerLift = spread * 0.40;
    const opexPerKg = 6.34;
    const finnoaqEbitdaMarginPerKg = Math.max(tollingFee - opexPerKg, 0);

    const millerAnnualCr = (totalKgDay * millerLift * days) / 10000000;
    const finnoaqAnnualRevCr = (totalKgDay * tollingFee * days) / 10000000;
    const finnoaqAnnualEbitdaCr = (totalKgDay * finnoaqEbitdaMarginPerKg * days) / 10000000;

    // CapEx = ₹135L (scales slightly with capacity: 135 * (cap/15)^0.65)
    const capexLakhs = 135 * Math.pow(capTPD / 15, 0.65);
    const ebitdaLakhs = finnoaqAnnualEbitdaCr * 100;
    const paybackYears = ebitdaLakhs > 0 ? (capexLakhs / ebitdaLakhs).toFixed(2) : "--";

    mTotalPool.textContent = `₹${totalAnnualCr.toFixed(2)} Cr / yr`;
    mTotalDaily.textContent = `₹${(totalDailyVal / 100000).toFixed(2)} Lakhs / day`;
    mMillerProfit.textContent = `₹${millerAnnualCr.toFixed(2)} Cr / yr`;
    mMillerUnit.textContent = `+₹${millerLift.toFixed(2)}/kg clean net margin lift`;
    mFinnoaqRev.textContent = `₹${finnoaqAnnualRevCr.toFixed(2)} Cr / yr`;
    mFinnoaqEbitda.textContent = `₹${finnoaqAnnualEbitdaCr.toFixed(2)} Cr / yr EBITDA`;
    mPayback.textContent = `${paybackYears} Years`;
  }

  sCap.addEventListener('input', update);
  sSpread.addEventListener('input', update);
  sDays.addEventListener('input', update);
}

// ============================================================================
// 5. INTERACTIVE 15 TPD MODULAR PROCESS ARCHITECTURE DIAGRAM
// ============================================================================
export function renderInteractiveProcessArchitecture(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const steps = [
    { tag: "D-101", title: "Air Destoning & Sizing", duty: "De-dusts and air-classifies raw Tanzanian HTC split pigeon pea cotyledons.", specs: "625 kg/h intake, 2.2 kW aspirator blower, vibro-screen grading" },
    { tag: "TK-101", title: "Ultrasonic Chelation Battery", duty: "Twin 2,500L SS316L steeping tanks with 40 kHz ultrasound horns at 48°C.", specs: "24-min residence, pH 5.20 S1-09 buffer, 41.8% calcium extraction" },
    { tag: "SC-101", title: "Vibrating Dewatering & Rinse", duty: "Separates steeped dal from liquor down to 28.0% wb with 12s deluge wash.", specs: "1,200 kg/h wet capacity, 3.0 kW pump, residual citrate 48.2 mg/kg" },
    { tag: "DR-101", title: "Two-Stage Tempered Fluid Bed", duty: "65°C zone 1 drying, 20-min adiabatic tempering, 55°C zone 2 drying.", specs: "850 kg/h dry discharge, 10.5% wb final moisture, breakage <0.35%" },
    { tag: "EV-101", title: "Zero Liquid Discharge (ZLD) MVR", duty: "Falling-film mechanical vapor recompression evaporator recovering 98.2% water.", specs: "250 kg/h evaporative rate, 11 kW turbo fan, 45% solids feed byproduct" },
    { tag: "B-101", title: "Optical Sorting & Packaging", duty: "High-speed trichromatic color sorting and 25 kg / 50 kg automated bagging.", specs: "97.37% finished dry solids yield, 2-whistle Hawkins cookability" }
  ];

  const stepsHtml = steps.map((s, i) => `
    <div class="proc-step-node ${i === 1 ? 'active' : ''}" data-index="${i}">
      <span class="psn-tag">${s.tag}</span>
      <h5 class="psn-title">${s.title}</h5>
      <p class="psn-desc">${s.duty}</p>
    </div>
  `).join('');

  container.innerHTML = `
    <div class="dynamic-chart-card">
      <div class="chart-header">
        <div>
          <span class="chart-badge">CONTINUOUS MODULAR INTEGRATION</span>
          <h4 class="chart-title">15 MT/day Continuous Plant Architecture (ASME / Aspen Converged)</h4>
        </div>
        <div style="font-size:0.8rem; color:#94A3B8;">Click any unit operation below to inspect engineering parameters</div>
      </div>

      <div class="process-flow-track">
        ${stepsHtml}
      </div>

      <div class="process-inspector-pane" id="proc-inspector">
        <div class="pip-header">
          <span class="status-tag tag-verified" id="pip-tag">${steps[1].tag}</span>
          <h4 id="pip-title">${steps[1].title}</h4>
        </div>
        <p id="pip-duty" style="color:#CBD5E1; margin:8px 0;">${steps[1].duty}</p>
        <div class="pip-specs" id="pip-specs"><strong>Design Specifications:</strong> ${steps[1].specs}</div>
      </div>
    </div>
  `;

  const inspector = container.querySelector('#proc-inspector');
  const pTag = container.querySelector('#pip-tag');
  const pTitle = container.querySelector('#pip-title');
  const pDuty = container.querySelector('#pip-duty');
  const pSpecs = container.querySelector('#pip-specs');

  container.querySelectorAll('.proc-step-node').forEach(node => {
    node.addEventListener('click', () => {
      container.querySelectorAll('.proc-step-node').forEach(n => n.classList.remove('active'));
      node.classList.add('active');
      const idx = parseInt(node.dataset.index, 10);
      const sel = steps[idx];
      pTag.textContent = sel.tag;
      pTitle.textContent = sel.title;
      pDuty.textContent = sel.duty;
      pSpecs.innerHTML = `<strong>Design Specifications:</strong> ${sel.specs}`;
    });
  });
}
