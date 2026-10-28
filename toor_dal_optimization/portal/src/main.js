// FinnoaQ Commercial Investor & Q1 Scientific Master Demonstration Microsite Application
// Project Ref: FNQ-PR-2026-001 | Revision: V11 Baseline
// Lead Chemical & Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
// Technical Oversight: FinnoaQ Process Engineering Board & Industrial Advisory Panel

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

import {
  PROJECT_INFO,
  CORE_QUESTIONS,
  COMMERCIAL_UNIT_ECONOMICS,
  OPEX_BREAKDOWN,
  CAPEX_SCHEDULE,
  FIVE_YEAR_CASH_FLOW,
  BIOPHYSICAL_SOLUTION,
  FORENSIC_FAILURE_ANALYSIS,
  SCALEUP_PHASES,
  CUSTOMER_DISCOVERY,
  REGULATORY_STANDARDS,
  MASS_BALANCE_RECONCILIATION,
  PLANT_EQUIPMENT,
  CAD_DRAWING_SHEETS
} from './data/micrositeData.js';

import { initDynamicVisualizations } from './dynamicCharts.js';

// Application State
const state = {
  activeCadIndex: 0,
  mobileNavOpen: false,
  threeInitialized: false,
  autoRotate: false
};

// 3D Viewport Instances
let scene, camera, renderer, controls;
let modelLoaded = false;

// ============================================================================
// 1. DOM INITIALIZATION & DATA RENDERING
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
  renderCoreQuestions();
  renderUnitEconomics();
  renderOpexBreakdown();
  renderCapexSchedule();
  renderFiveYearCashFlow();
  renderBiophysicalSolution();
  renderForensicFailureAnalysis();
  renderPlantEquipment();
  renderMassBalance();
  renderScaleUpRoadmap();
  renderCustomerDiscovery();
  renderRegulatoryStandards();
  renderCadDrawingViewer();

  // Initialize Dynamic Vector Visualizations & Mill Simulator
  initDynamicVisualizations();

  setupNavigationScrollspy();
  setupMobileNav();
  setupOnboardingForm();
  setup3DModal();
});

// ============================================================================
// 2. DATA SECTION RENDERERS
// ============================================================================

function renderCoreQuestions() {
  const container = document.getElementById('core-questions-container');
  if (!container) return;

  container.innerHTML = CORE_QUESTIONS.map(q => `
    <article class="question-card">
      <div class="qc-header">
        <span class="qc-num">QUESTION ${q.num}</span>
        <span class="status-tag tag-verified">${q.status}</span>
      </div>
      <h3 class="qc-question">${q.title}</h3>
      <p class="qc-answer">${q.summary}</p>
      <div class="qc-footer">
        <span class="qc-basis"><strong>Audited Evidence:</strong> ${q.basis}</span>
      </div>
    </article>
  `).join('');
}

function renderUnitEconomics() {
  const waterfallContainer = document.getElementById('arbitrage-waterfall-container');
  if (waterfallContainer) {
    waterfallContainer.innerHTML = `
      <div class="arbitrage-waterfall-card">
        <div class="waterfall-header">
          <span class="section-eyebrow" style="color:#60A5FA;">MANDI ARBITRAGE WATERFALL</span>
          <h3>₹20.00 / kg Gross Mandi Spread Decomposition</h3>
          <p>How FinnoaQ turns severely discounted imported African toor dal into shared industrial profit parity with domestic Indian Desi dal.</p>
        </div>
        <div class="waterfall-steps-grid">
          <div class="waterfall-step">
            <span class="step-label">1. RAW AFRICAN DAL</span>
            <span class="step-val">₹85.00</span>
            <p class="step-desc">Mandi port intake price (Tanzania / Mozambique bold lot).</p>
          </div>
          <div class="waterfall-step">
            <span class="step-label">2. FINNOAQ OPEX</span>
            <span class="step-val">₹6.34</span>
            <p class="step-desc">Direct processing cost with 85% closed-loop liquor recycling.</p>
          </div>
          <div class="waterfall-step highlight-tolling">
            <span class="step-label">3. TOLLING CHARGE</span>
            <span class="step-val">₹12.00</span>
            <p class="step-desc">FinnoaQ fee (yielding ₹5.66/kg net operating margin).</p>
          </div>
          <div class="waterfall-step highlight-lift">
            <span class="step-label">4. MILLER PROFIT LIFT</span>
            <span class="step-val">₹8.00 / kg</span>
            <p class="step-desc"><strong>₹8,000 / MT</strong> pure net profit captured by partner pulse mill!</p>
          </div>
          <div class="waterfall-step">
            <span class="step-label">5. WHOLESALE PARITY</span>
            <span class="step-val">₹105.00</span>
            <p class="step-desc">Realized wholesale selling price (matching Indian Latur Desi dal).</p>
          </div>
        </div>
      </div>
    `;
  }

  const kpiContainer = document.getElementById('kpi-summary-badges-container');
  if (kpiContainer) {
    kpiContainer.innerHTML = `
      <div class="kpi-badge-grid">
        <div class="kpi-badge-card cobalt">
          <span class="kpi-badge-label">MANDI SPREAD CAPTURE</span>
          <span class="kpi-badge-val">₹20.00 / kg</span>
          <span class="kpi-badge-sub">₹3,00,000 / day total arbitrage pool at 15 TPD</span>
        </div>
        <div class="kpi-badge-card emerald">
          <span class="kpi-badge-label">5-YEAR PROJECT IRR</span>
          <span class="kpi-badge-val">78.4%</span>
          <span class="kpi-badge-sub">Audited discounted cash flow return on equity</span>
        </div>
        <div class="kpi-badge-card amber">
          <span class="kpi-badge-label">SIMPLE CAPITAL PAYBACK</span>
          <span class="kpi-badge-val">1.12 Years</span>
          <span class="kpi-badge-sub">13.4 months from commercial commissioning</span>
        </div>
        <div class="kpi-badge-card emerald">
          <span class="kpi-badge-label">BREAKEVEN UTILIZATION</span>
          <span class="kpi-badge-val">18.7%</span>
          <span class="kpi-badge-sub">Covers total OpEx + CapEx service at just 2.81 TPD</span>
        </div>
      </div>
    `;
  }
}

function renderOpexBreakdown() {
  const tbody = document.getElementById('opex-breakdown-tbody');
  if (!tbody) return;

  tbody.innerHTML = OPEX_BREAKDOWN.map(item => `
    <tr>
      <td><strong>${item.category}</strong></td>
      <td><strong>₹${item.costPerKg.toFixed(2)} / kg</strong></td>
      <td><code>${item.percentage.toFixed(1)}%</code></td>
      <td>${item.details}</td>
    </tr>
  `).join('') + `
    <tr style="background: #F8FAFC; font-weight: 800; border-top: 2px solid #CBD5E1;">
      <td>TOTAL DIRECT PROCESSING OPEX (85% RECYCLE)</td>
      <td style="color: #059669; font-size: 15px;">₹6.34 / kg</td>
      <td>100.0%</td>
      <td><strong>Saves ₹5.31 / kg (-45.6%)</strong> vs once-through dumping (₹11.65/kg)!</td>
    </tr>
  `;
}

function renderCapexSchedule() {
  const tbody = document.getElementById('capex-schedule-tbody');
  if (!tbody) return;

  tbody.innerHTML = CAPEX_SCHEDULE.map(item => `
    <tr>
      <td><strong><code>${item.area}</code></strong></td>
      <td><strong>${item.name}</strong></td>
      <td><strong>₹${item.costLakhs.toFixed(2)} L</strong></td>
      <td>${item.specs}</td>
    </tr>
  `).join('') + `
    <tr style="background: #F8FAFC; font-weight: 800; border-top: 2px solid #CBD5E1;">
      <td colspan="2">TOTAL TURNKEY 15 TPD CAPITAL EXPENDITURE</td>
      <td style="color: #2563EB; font-size: 15px;">₹135.00 Lakhs</td>
      <td><strong>~$160,000 USD</strong> complete food-grade turnkey engineering package</td>
    </tr>
  `;
}

function renderFiveYearCashFlow() {
  const tbody = document.getElementById('five-year-cashflow-tbody');
  if (!tbody) return;

  tbody.innerHTML = FIVE_YEAR_CASH_FLOW.map(row => `
    <tr>
      <td><strong>${row.year}</strong></td>
      <td><code>${row.utilization}</code></td>
      <td>${row.volumeMT}</td>
      <td><strong>${row.revenue}</strong></td>
      <td>${row.opex}</td>
      <td><strong style="color: #059669;">${row.ebitda}</strong></td>
      <td><code>${row.ebitdaMargin}</code></td>
      <td>${row.depreciation}</td>
      <td><strong>${row.pat}</strong></td>
      <td><strong style="color: #2563EB;">${row.cumFcf}</strong></td>
    </tr>
  `).join('');
}

function renderBiophysicalSolution() {
  const container = document.getElementById('biophysics-showcase-container');
  if (!container) return;

  const b = BIOPHYSICAL_SOLUTION;
  container.innerHTML = `
    <div class="biophysics-grid">
      <div class="biophysics-card">
        <div class="biophysics-card-header">
          <span class="biophysics-card-tag">BIOPHYSICAL PATHOLOGY</span>
          <h4 class="biophysics-card-title">${b.pathology.title}</h4>
        </div>
        <div class="biophysics-card-body">
          <p>${b.pathology.description}</p>
          <div class="biophysics-formula-box">
            Reaction: Homogalacturonan-COO⁻ + Ca²⁺ + ⁻OOC-Homogalacturonan ⇄ [Ca(HG)₂] (insoluble egg-box)
          </div>
        </div>
      </div>

      <div class="biophysics-card">
        <div class="biophysics-card-header">
          <span class="biophysics-card-tag">S1-09 BUFFER FORMULATION</span>
          <h4 class="biophysics-card-title">Stoichiometric Bio-Chelation Buffer (pH 5.20 ± 0.05)</h4>
        </div>
        <div class="biophysics-card-body">
          <p>Tri-salt buffer balancing chelation affinity, multi-protic equilibrium, and ionic tonicity:</p>
          <ul style="padding-left: 18px; margin: 8px 0; font-size: 12.5px;">
            ${b.formulation.components.map(c => `<li><strong>${c.name}:</strong> ${c.molarity} (${c.concentration}) &bull; ${c.function}</li>`).join('')}
          </ul>
          <div class="biophysics-formula-box">
            Buffering: pH locked at 5.20 ± 0.05 | Van Slyke β = 0.042 mol/(L·pH) | 41.8% core Ca²⁺ removed
          </div>
        </div>
      </div>

      <div class="biophysics-card">
        <div class="biophysics-card-header">
          <span class="biophysics-card-tag">PRESSURE COOKER THERMODYNAMICS</span>
          <h4 class="biophysics-card-title">Hawkins 3L Acoustic Venting Dynamics</h4>
        </div>
        <div class="biophysics-card-body">
          <p>${b.cookerThermodynamics.whistleDynamics}</p>
          <div class="biophysics-formula-box">
            Saturated Steam: 15 psi (103.4 kPa gauge, 121.1°C) | F_WB,core ≤ 18.0 N in exactly 2 whistles!
          </div>
          <p style="font-size: 12px; color: var(--text-muted);">${b.cookerThermodynamics.cookingTimeReduction}</p>
        </div>
      </div>

      <div class="biophysics-card">
        <div class="biophysics-card-header">
          <span class="biophysics-card-tag">VISCOELASTIC DRYING MECHANICS</span>
          <h4 class="biophysics-card-title">Two-Stage Tempered Fluid Bed Drying</h4>
        </div>
        <div class="biophysics-card-body">
          <p>${b.dryingMechanics.checkingPhenomenon}</p>
          <div class="biophysics-formula-box">
            FinnoaQ Schedule: 65°C (45m) → 55°C Tempering (20m) → 55°C (40m) | σ_θθ ≤ 0.40 MPa | Fines <0.35%
          </div>
          <p style="font-size: 12px; color: var(--text-muted);">${b.dryingMechanics.stressSuppression}</p>
        </div>
      </div>

      <div class="biophysics-card">
        <div class="biophysics-card-header">
          <span class="biophysics-card-tag">FLAVOR & DELUGE RINSE KINETICS</span>
          <h4 class="biophysics-card-title">LOX Inactivation & Parity with Indian Desi Dal</h4>
        </div>
        <div class="biophysics-card-body">
          <p>${b.flavorAndPurity.lipoxygenaseInactivation} Hexanal suppressed to 0.025 ppm (OAV = 0.84 < 1.0).</p>
          <div class="biophysics-formula-box">
            12s Counter-Current Wash: <27.6 ppm surface salts | 142 mg/kg phosphate (35x below FSSAI MRL)
          </div>
          <p style="font-size: 12px; color: #059669; font-weight: 700;">${b.flavorAndPurity.sensoryValidation}</p>
        </div>
      </div>
    </div>
  `;
}

function renderForensicFailureAnalysis() {
  const tbody = document.getElementById('failure-forensics-tbody');
  if (!tbody) return;

  tbody.innerHTML = FORENSIC_FAILURE_ANALYSIS.map(f => `
    <tr>
      <td><strong>${f.failureMode}</strong></td>
      <td>${f.chemicalMechanism}</td>
      <td style="color: #DC2626; font-size: 12.5px;"><strong>${f.observedDefect}</strong></td>
      <td style="color: #059669; font-size: 12.5px;"><strong>${f.finnoaqSolution}</strong></td>
      <td><span class="status-tag tag-verified">${f.status}</span></td>
    </tr>
  `).join('');
}

function renderPlantEquipment() {
  const container = document.getElementById('equipment-grid-container');
  if (!container) return;

  container.innerHTML = PLANT_EQUIPMENT.map(e => `
    <div class="equipment-unit-card">
      <div class="euc-media">
        <img src="${e.render}" alt="${e.name}" class="euc-img" loading="lazy" />
        <span class="euc-badge-tag">${e.tag}</span>
      </div>
      <div class="euc-content">
        <h4 class="euc-title">${e.name}</h4>
        <div class="euc-type">${e.type}</div>
        <table class="euc-specs-table">
          <tr><td class="k">Capacity:</td><td class="v">${e.capacity}</td></tr>
          <tr><td class="k">Drive Power:</td><td class="v">${e.power}</td></tr>
        </table>
        <p class="euc-desc">${e.duty}</p>
      </div>
    </div>
  `).join('');
}

function renderMassBalance() {
  const tbody = document.getElementById('mass-balance-tbody');
  if (!tbody) return;

  tbody.innerHTML = MASS_BALANCE_RECONCILIATION.map(m => `
    <tr>
      <td><strong>${m.component}</strong></td>
      <td><strong><code>${m.value}</code></strong></td>
      <td>${m.basis}</td>
      <td><span class="status-tag ${m.tier.includes('CONVERGED') || m.tier.includes('MEASURED') ? 'tag-verified' : 'tag-calculated'}">${m.tier}</span></td>
    </tr>
  `).join('');
}

function renderScaleUpRoadmap() {
  const flowContainer = document.getElementById('roadmap-flow-container');
  if (flowContainer) {
    flowContainer.innerHTML = SCALEUP_PHASES.map(p => `
      <div class="roadmap-card ${p.phase === 'Phase 1' ? 'active-target' : p.phase === 'Phase 0' ? 'completed' : ''}">
        <span class="roadmap-phase-tag">${p.phase} &bull; ${p.timeline}</span>
        <h4 class="roadmap-card-title">${p.name}</h4>
        <div class="roadmap-meta">Budget: <strong>₹${p.budgetLakhs.toFixed(1)} Lakhs</strong></div>
        <p class="roadmap-desc">${p.objectives}</p>
        <div class="roadmap-gate">${p.gateDecision}</div>
      </div>
    `).join('');
  }

  const tbody = document.getElementById('roadmap-table-tbody');
  if (tbody) {
    tbody.innerHTML = SCALEUP_PHASES.map(p => `
      <tr>
        <td><strong><code>${p.phase}</code></strong></td>
        <td><strong>${p.name}</strong></td>
        <td><code>${p.timeline}</code></td>
        <td><strong>₹${p.budgetLakhs.toFixed(1)} L</strong></td>
        <td>${p.batches}</td>
        <td>${p.objectives}</td>
        <td><span class="status-tag ${p.phase === 'Phase 0' ? 'tag-verified' : p.phase === 'Phase 1' ? 'tag-pending' : 'tag-neutral'}">${p.gateDecision.split(':')[0]}</span></td>
      </tr>
    `).join('');
  }
}

function renderCustomerDiscovery() {
  const quotesContainer = document.getElementById('miller-quotes-container');
  if (quotesContainer) {
    quotesContainer.innerHTML = CUSTOMER_DISCOVERY.keyMillerQuotes.map(q => `
      <div class="miller-quote-card">
        <p class="miller-quote-text">"${q.quote}"</p>
        <span class="miller-quote-author">&mdash; ${q.miller}</span>
      </div>
    `).join('');
  }

  const workflowContainer = document.getElementById('diagnostic-workflow-container');
  if (workflowContainer) {
    workflowContainer.innerHTML = CUSTOMER_DISCOVERY.diagnosticWorkflow.map(s => `
      <div class="workflow-step-card">
        <span class="ws-time">${s.time}</span>
        <h5 class="ws-title">${s.step}</h5>
        <p class="ws-desc">${s.desc}</p>
      </div>
    `).join('');
  }
}

function renderRegulatoryStandards() {
  const tbody = document.getElementById('regulatory-standards-tbody');
  if (!tbody) return;

  tbody.innerHTML = REGULATORY_STANDARDS.map(r => `
    <tr>
      <td><strong>${r.standard}</strong></td>
      <td>${r.scope}</td>
      <td><span class="status-tag tag-verified">${r.complianceStatus}</span></td>
      <td>${r.details}</td>
    </tr>
  `).join('');
}

function renderCadDrawingViewer() {
  const listContainer = document.getElementById('cad-sheet-list-container');
  if (!listContainer) return;

  listContainer.innerHTML = CAD_DRAWING_SHEETS.map((s, idx) => `
    <button class="cad-sheet-btn ${idx === state.activeCadIndex ? 'active' : ''}" data-index="${idx}">
      <span class="csb-tag">${s.tag}</span>
      <span class="csb-title">${s.title}</span>
    </button>
  `).join('');

  listContainer.querySelectorAll('.cad-sheet-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const idx = parseInt(btn.dataset.index, 10);
      switchCadSheet(idx);
    });
  });

  updateCadDisplay();
}

function switchCadSheet(idx) {
  state.activeCadIndex = idx;
  const listContainer = document.getElementById('cad-sheet-list-container');
  if (listContainer) {
    listContainer.querySelectorAll('.cad-sheet-btn').forEach((b, i) => {
      b.classList.toggle('active', i === idx);
    });
  }
  updateCadDisplay();
}

function updateCadDisplay() {
  const sheet = CAD_DRAWING_SHEETS[state.activeCadIndex];
  if (!sheet) return;

  const tagEl = document.getElementById('active-cad-tag');
  const titleEl = document.getElementById('active-cad-title');
  const statusEl = document.getElementById('active-cad-status');
  const descEl = document.getElementById('active-cad-desc');
  const imgEl = document.getElementById('active-cad-display');
  const openBtn = document.getElementById('btn-cad-open-full');

  if (tagEl) tagEl.textContent = sheet.tag;
  if (titleEl) titleEl.textContent = sheet.title;
  if (statusEl) statusEl.textContent = sheet.status;
  if (descEl) descEl.textContent = sheet.desc;
  if (imgEl) {
    imgEl.src = sheet.file;
    imgEl.alt = `${sheet.tag}: ${sheet.title}`;
  }
  if (openBtn) {
    openBtn.href = sheet.file;
  }
}

// ============================================================================
// 3. NAVIGATION & UI CONTROLS
// ============================================================================

function setupNavigationScrollspy() {
  const navLinks = document.querySelectorAll('.header-nav .nav-link, .mobile-nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 120;

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        current = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      const href = link.getAttribute('href')?.replace('#', '');
      link.classList.toggle('active', href === current);
    });
  }, { passive: true });
}

function setupMobileNav() {
  const btn = document.getElementById('mobile-menu-btn');
  const drawer = document.getElementById('mobile-nav-drawer');
  if (!btn || !drawer) return;

  btn.addEventListener('click', () => {
    state.mobileNavOpen = !state.mobileNavOpen;
    btn.setAttribute('aria-expanded', state.mobileNavOpen);
    drawer.style.display = state.mobileNavOpen ? 'block' : 'none';
  });

  drawer.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', () => {
      state.mobileNavOpen = false;
      btn.setAttribute('aria-expanded', 'false');
      drawer.style.display = 'none';
    });
  });
}

function setupOnboardingForm() {
  const form = document.getElementById('project-scoping-form');
  const confBox = document.getElementById('form-confirmation');
  const confDetails = document.getElementById('conf-details');
  const resetBtn = document.getElementById('btn-reset-form');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const org = data.get('organization') || 'Partner Organization';
    const origin = data.get('grainOrigin') || 'Imported Pulse Lot';
    const volume = data.get('targetVolume') || '15 TPD';

    if (confDetails) {
      confDetails.innerHTML = `
        Thank you, <strong>${org}</strong>. Your project scoping request for <strong>${origin}</strong> (${volume}) has been recorded.
        Our process engineering team will review your milling parameters and contact you to schedule a 48-Hour 5-kg diagnostic trial.
      `;
    }

    form.classList.add('is-hidden');
    if (confBox) confBox.classList.remove('is-hidden');
  });

  if (resetBtn && confBox) {
    resetBtn.addEventListener('click', () => {
      form.reset();
      form.classList.remove('is-hidden');
      confBox.classList.add('is-hidden');
    });
  }
}

// ============================================================================
// 4. THREE.JS 3D MODEL VIEWER
// ============================================================================

function setup3DModal() {
  const openBtn = document.getElementById('btn-view-3d-modal');
  const modal = document.getElementById('modal-3d');
  const closeBtn = document.getElementById('btn-close-3d-modal');

  if (!openBtn || !modal) return;

  openBtn.addEventListener('click', () => {
    modal.classList.remove('is-hidden');
    modal.setAttribute('aria-hidden', 'false');
    if (!state.threeInitialized) {
      initThreeViewport();
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      modal.classList.add('is-hidden');
      modal.setAttribute('aria-hidden', 'true');
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.add('is-hidden');
      modal.setAttribute('aria-hidden', 'true');
    }
  });
}

function initThreeViewport() {
  const container = document.getElementById('canvas-container');
  const loadingIndicator = document.getElementById('canvas-loading');
  if (!container) return;

  state.threeInitialized = true;

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0f1d);

  camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
  camera.position.set(12, 10, 16);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.2;
  container.appendChild(renderer.domElement);

  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.maxDistance = 50;
  controls.minDistance = 2;

  // Studio Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
  scene.add(ambientLight);

  const mainLight = new THREE.DirectionalLight(0xffffff, 1.8);
  mainLight.position.set(15, 25, 20);
  scene.add(mainLight);

  const fillLight = new THREE.DirectionalLight(0x60a5fa, 0.8);
  fillLight.position.set(-15, 10, -10);
  scene.add(fillLight);

  const gridHelper = new THREE.GridHelper(30, 30, 0x1e3a8a, 0x1e293b);
  gridHelper.position.y = -0.01;
  scene.add(gridHelper);

  // Load GLB
  const loader = new GLTFLoader();
  loader.load('/models/plant_15t_assembly.glb', (gltf) => {
    const model = gltf.scene;
    scene.add(model);
    modelLoaded = true;
    if (loadingIndicator) loadingIndicator.style.display = 'none';

    // Center model
    const box = new THREE.Box3().setFromObject(model);
    const center = box.getCenter(new THREE.Vector3());
    model.position.sub(center);
    controls.target.set(0, 0, 0);
  }, undefined, (err) => {
    console.warn('GLB load error, using fallback geometry:', err);
    createFallbackGeometry();
    if (loadingIndicator) loadingIndicator.style.display = 'none';
  });

  // Presets
  const btnIso = document.getElementById('btn-modal-cam-iso');
  const btnFront = document.getElementById('btn-modal-cam-front');
  const btnSide = document.getElementById('btn-modal-cam-side');
  const btnTop = document.getElementById('btn-modal-cam-top');
  const btnTurntable = document.getElementById('btn-modal-turntable');

  if (btnIso) btnIso.addEventListener('click', () => setCamPosition(12, 10, 16));
  if (btnFront) btnFront.addEventListener('click', () => setCamPosition(0, 5, 22));
  if (btnSide) btnSide.addEventListener('click', () => setCamPosition(22, 5, 0));
  if (btnTop) btnTop.addEventListener('click', () => setCamPosition(0, 24, 0));
  if (btnTurntable) {
    btnTurntable.addEventListener('click', () => {
      state.autoRotate = !state.autoRotate;
      controls.autoRotate = state.autoRotate;
      btnTurntable.classList.toggle('active', state.autoRotate);
    });
  }

  window.addEventListener('resize', () => {
    if (!container || !renderer || !camera) return;
    camera.aspect = container.clientWidth / container.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
  });

  animate();
}

function setCamPosition(x, y, z) {
  if (!camera || !controls) return;
  camera.position.set(x, y, z);
  controls.target.set(0, 0, 0);
  controls.update();
}

function createFallbackGeometry() {
  const group = new THREE.Group();
  const mat = new THREE.MeshStandardMaterial({ color: 0x2563eb, metalness: 0.8, roughness: 0.2 });
  const cylGeo = new THREE.CylinderGeometry(1.5, 1.5, 4, 32);
  const tank = new THREE.Mesh(cylGeo, mat);
  tank.position.y = 2;
  group.add(tank);
  scene.add(group);
}

function animate() {
  requestAnimationFrame(animate);
  if (controls) controls.update();
  if (renderer && scene && camera) {
    renderer.render(scene, camera);
  }
}
