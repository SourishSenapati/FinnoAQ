// FinnoaQ Single-Project Engineering Demonstration Microsite Application
// Project Ref: FNQ-PR-2026-001 | SOW Rev V10 (Evidence-Gated Baseline)
// Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)
// Technical Oversight: Technical Advisory Panel & FinnoaQ Process Engineering Board

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

import {
  PROJECT_INFO,
  CORE_QUESTIONS,
  PROCESS_STAGES,
  TREATMENT_CONDITIONS,
  TEN_HYPOTHESES,
  DIGITAL_TWIN_SIMULATION,
  DREAM_RSI_CANDIDATES,
  BATCH_VARIABILITY_DATA,
  FLAVOR_REMEDIATION_DATA,
  RAPID_PRETREATMENT_DATA,
  RICHARDSON_CONVERGENCE_DATA,
  PLANT_EQUIPMENT,
  MASS_BALANCE_RECONCILIATION,
  SCHEDULE_SCENARIOS,
  PHASE_1_MILESTONES,
  CAD_DRAWING_SHEETS
} from './data/micrositeData.js';

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
  renderProcessPipeline();
  renderTenHypotheses();
  renderDigitalTwinSimulation();
  renderDreamRsiCandidates();
  renderBatchVariability();
  renderFlavorRemediation();
  renderRapidPretreatment();
  renderRichardsonConvergence();
  renderTreatmentMatrix();
  renderPlantEquipment();
  renderScheduleScenarios();
  renderMassBalance();
  renderMilestones();
  renderCadDrawingViewer();

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
        <span class="status-tag ${q.status.includes('VERIFIED') ? 'tag-verified' : q.status.includes('PENDING') ? 'tag-pending' : 'tag-calculated'}">${q.status}</span>
      </div>
      <h3 class="qc-question">${q.title}</h3>
      <p class="qc-answer">${q.summary}</p>
      <div class="qc-footer">
        <span class="qc-basis">Basis: ${q.basis}</span>
      </div>
    </article>
  `).join('');
}

function renderProcessPipeline() {
  const container = document.getElementById('process-pipeline-container');
  if (!container) return;

  container.innerHTML = PROCESS_STAGES.map(s => `
    <div class="pipeline-step-card">
      <div class="step-top">
        <span class="step-num">STEP ${s.step}</span>
        <span class="status-tag ${s.status === 'VERIFIED' ? 'tag-verified' : s.status === 'CALCULATED' ? 'tag-calculated' : 'tag-neutral'}">${s.status}</span>
      </div>
      <h4 class="step-name">${s.name}</h4>
      <div class="step-unit">${s.unit}</div>
      <p class="step-desc">${s.desc}</p>
    </div>
  `).join('');
}

function renderTenHypotheses() {
  const tbody = document.getElementById('hypotheses-matrix-tbody');
  if (!tbody) return;

  tbody.innerHTML = TEN_HYPOTHESES.map(h => `
    <tr>
      <td><strong><code>${h.id}</code></strong></td>
      <td><strong>${h.name}</strong></td>
      <td>${h.mechanism}</td>
      <td>${h.test}</td>
      <td><span class="status-tag ${h.id === 'H3' ? 'tag-calculated' : 'tag-neutral'}">${h.status}</span></td>
    </tr>
  `).join('');
}

function renderDigitalTwinSimulation() {
  const container = document.getElementById('simulation-features-container');
  if (!container) return;

  container.innerHTML = DIGITAL_TWIN_SIMULATION.components.map(c => `
    <div class="protocol-card">
      <div class="protocol-header">
        <span class="protocol-tag">IN SILICO METHODOLOGY</span>
        <h4>${c.name}</h4>
      </div>
      <p class="protocol-desc">${c.desc}</p>
      <div class="protocol-criteria">
        <span class="crit-label">ACCELERATION:</span>
        <span class="crit-val">NVIDIA RTX 4050 GPU (PyTorch CUDA)</span>
      </div>
    </div>
  `).join('');
}

function renderDreamRsiCandidates() {
  const tbody = document.getElementById('dream-rsi-candidates-tbody');
  if (!tbody) return;

  tbody.innerHTML = DREAM_RSI_CANDIDATES.map(c => `
    <tr>
      <td><strong>${c.rank}</strong></td>
      <td><strong><code>${c.id}</code></strong></td>
      <td><strong>${c.name}</strong><br><small style="color: var(--text-muted);">${c.reagent}</small></td>
      <td><code>${c.time}</code></td>
      <td>${c.disp}</td>
      <td>${c.rec}</td>
      <td>${c.na}</td>
      <td><strong>${c.sens} / 9</strong></td>
      <td><code>${c.opex}</code></td>
      <td><strong><code>${c.util}</code></strong></td>
      <td><span class="status-tag ${c.status.includes('ADVANCED') ? 'tag-verified' : c.status.includes('BASELINE') ? 'tag-neutral' : 'tag-pending'}">${c.status.replace(/_/g, ' ')}</span></td>
    </tr>
  `).join('');
}

function renderBatchVariability() {
  const tbody = document.getElementById('batch-variability-tbody');
  if (!tbody) return;

  tbody.innerHTML = BATCH_VARIABILITY_DATA.map(b => `
    <tr>
      <td><strong>${b.feedstock}</strong></td>
      <td><code>${b.caContent}</code></td>
      <td><code>${b.thickness}</code></td>
      <td><span class="status-tag tag-pending">${b.staticPass}</span></td>
      <td><strong>${b.adaptiveRegime}</strong></td>
      <td><span class="status-tag tag-verified">${b.adaptivePass}</span></td>
      <td><code>${b.retainedNa}</code></td>
      <td><span class="status-tag ${b.status.includes('100%') ? 'tag-verified' : 'tag-calculated'}">${b.status}</span></td>
    </tr>
  `).join('');
}

function renderFlavorRemediation() {
  const tbody = document.getElementById('flavor-remediation-tbody');
  if (!tbody) return;

  tbody.innerHTML = FLAVOR_REMEDIATION_DATA.map(f => `
    <tr>
      <td><strong>${f.parameter}</strong></td>
      <td><code>${f.rawUntreated}</code></td>
      <td><strong style="color: var(--accent);">${f.thermalTreated}</strong></td>
      <td><code>${f.indianDesiBenchmark}</code></td>
      <td>${f.organolepticImpact}</td>
    </tr>
  `).join('');
}

function renderRapidPretreatment() {
  const tbody = document.getElementById('rapid-pretreatment-tbody');
  if (!tbody) return;

  tbody.innerHTML = RAPID_PRETREATMENT_DATA.map(r => `
    <tr>
      <td><strong>${r.technology}</strong></td>
      <td><code>${r.pulsePressure}</code></td>
      <td><strong><code>${r.coreTime}</code></strong></td>
      <td><code>${r.delugeWashTime}</code></td>
      <td>${r.moisturePickup}</td>
      <td><code>${r.capexCost}</code></td>
      <td><span class="status-tag ${r.status.includes('RECOMMENDED') ? 'tag-verified' : 'tag-neutral'}">${r.status.replace(/_/g, ' ')}</span></td>
    </tr>
  `).join('');
}

function renderRichardsonConvergence() {
  const tbody = document.getElementById('richardson-convergence-tbody');
  if (!tbody) return;

  tbody.innerHTML = RICHARDSON_CONVERGENCE_DATA.grids.map(g => `
    <tr>
      <td><strong>${g.grid}</strong></td>
      <td><code>${g.nodes}</code></td>
      <td><strong><code>${g.cookTime}</code></strong></td>
      <td>${g.whistles}</td>
      <td>${g.coreForce}</td>
      <td><code>${g.solveTime}</code></td>
      <td><span class="status-tag tag-verified">CONVERGED</span></td>
    </tr>
  `).join('');
}

function renderTreatmentMatrix() {
  const tbody = document.getElementById('treatment-matrix-tbody');
  if (!tbody) return;

  tbody.innerHTML = TREATMENT_CONDITIONS.map(t => `
    <tr>
      <td><strong><code>${t.code}</code></strong></td>
      <td><strong>${t.name}</strong><br><small style="color: var(--text-muted);">${t.notes}</small></td>
      <td>${t.reagent}</td>
      <td><code>${t.ratio}</code></td>
      <td>${t.mechanism}</td>
      <td><span class="status-tag ${t.status.includes('BASELINE') ? 'tag-verified' : t.status.includes('CONTROL') ? 'tag-calculated' : 'tag-pending'}">${t.status}</span></td>
    </tr>
  `).join('');
}

function renderPlantEquipment() {
  const container = document.getElementById('equipment-grid-container');
  if (!container) return;

  container.innerHTML = PLANT_EQUIPMENT.map(e => `
    <div class="equipment-unit-card">
      <div class="euc-media">
        <img src="${e.image}" alt="${e.name}" class="euc-img" loading="lazy" />
        <span class="euc-badge-tag">${e.tag}</span>
      </div>
      <div class="euc-content">
        <h4 class="euc-title">${e.name}</h4>
        <div class="euc-type">${e.type} &bull; ${e.code}</div>
        <table class="euc-specs-table">
          <tr><td class="k">Working Capacity:</td><td class="v">${e.capacity}</td></tr>
          <tr><td class="k">Dimensions:</td><td class="v">${e.dimensions}</td></tr>
          <tr><td class="k">Materials:</td><td class="v">${e.moc}</td></tr>
          <tr><td class="k">Motor Drive:</td><td class="v">${e.motor}</td></tr>
          <tr><td class="k">Ref Drawing:</td><td class="v">${e.dwg}</td></tr>
        </table>
        <p class="euc-desc">${e.desc}</p>
      </div>
    </div>
  `).join('');
}

function renderScheduleScenarios() {
  const tbody = document.getElementById('schedule-scenarios-tbody');
  if (!tbody) return;

  tbody.innerHTML = SCHEDULE_SCENARIOS.map(s => `
    <tr>
      <td><strong>${s.scenario}</strong></td>
      <td>${s.hours}</td>
      <td><code>${s.nominalRate}</code></td>
      <td>${s.oee}</td>
      <td><strong><code>${s.effectiveRate}</code></strong></td>
      <td><span class="status-tag tag-calculated">${s.surge}</span></td>
    </tr>
  `).join('');
}

function renderMassBalance() {
  const tbody = document.getElementById('mass-balance-tbody');
  if (!tbody) return;

  tbody.innerHTML = MASS_BALANCE_RECONCILIATION.map(m => `
    <tr>
      <td><strong>${m.item}</strong></td>
      <td><strong><code>${m.val}</code></strong></td>
      <td>${m.basis}</td>
      <td><span class="status-tag ${m.status === 'LOCKED' ? 'tag-verified' : m.status === 'RECONCILED' ? 'tag-calculated' : 'tag-pending'}">${m.status}</span></td>
    </tr>
  `).join('');
}

function renderMilestones() {
  const tbody = document.getElementById('milestones-tbody');
  if (!tbody) return;

  tbody.innerHTML = PHASE_1_MILESTONES.map(m => `
    <tr>
      <td><strong><code>${m.milestone}</code></strong></td>
      <td><strong>${m.phase}</strong></td>
      <td><code>${m.share}</code></td>
      <td>${m.deliverables}</td>
      <td><span class="status-tag tag-neutral">${m.turnaround}</span></td>
    </tr>
  `).join('');
}

// ============================================================================
// 3. INTERACTIVE CAD DRAWING SHEET VIEWER
// ============================================================================
function renderCadDrawingViewer() {
  const sidebar = document.getElementById('cad-sheet-list-container');
  if (!sidebar) return;

  sidebar.innerHTML = CAD_DRAWING_SHEETS.map((s, idx) => `
    <div class="sheet-item ${idx === state.activeCadIndex ? 'active' : ''}" data-index="${idx}">
      <div class="sheet-item-header">
        <span class="sheet-tag">${s.tag}</span>
        <span class="sheet-cat">${s.category}</span>
      </div>
      <div class="sheet-title">${s.title}</div>
    </div>
  `).join('');

  // Wire sheet clicks
  document.querySelectorAll('#cad-sheet-list-container .sheet-item').forEach(item => {
    item.addEventListener('click', () => {
      const idx = parseInt(item.dataset.index, 10);
      setActiveCadSheet(idx);
    });
  });

  setActiveCadSheet(0);
}

function setActiveCadSheet(idx) {
  state.activeCadIndex = idx;
  const sheet = CAD_DRAWING_SHEETS[idx];
  if (!sheet) return;

  // Update active state in sidebar
  document.querySelectorAll('#cad-sheet-list-container .sheet-item').forEach((el, i) => {
    el.classList.toggle('active', i === idx);
  });

  // Update Main Stage Elements
  const tagEl = document.getElementById('active-cad-tag');
  const titleEl = document.getElementById('active-cad-title');
  const statusEl = document.getElementById('active-cad-status');
  const imgEl = document.getElementById('active-cad-display');
  const descEl = document.getElementById('active-cad-desc');
  const linkEl = document.getElementById('btn-cad-open-full');

  if (tagEl) tagEl.textContent = sheet.tag;
  if (titleEl) titleEl.textContent = sheet.title;
  if (statusEl) statusEl.textContent = sheet.status;
  if (imgEl) {
    imgEl.src = sheet.image;
    imgEl.alt = `${sheet.tag}: ${sheet.title}`;
  }
  if (descEl) descEl.textContent = sheet.desc;
  if (linkEl) linkEl.href = sheet.image;
}

// ============================================================================
// 4. NAVIGATION & MOBILE MENU
// ============================================================================
function setupNavigationScrollspy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.header-nav .nav-link');

  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.scrollY + 100;

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        currentId = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
    });
  }, { passive: true });
}

function setupMobileNav() {
  const btn = document.getElementById('mobile-menu-btn');
  const drawer = document.getElementById('mobile-nav-drawer');
  if (!btn || !drawer) return;

  btn.addEventListener('click', () => {
    state.mobileNavOpen = !state.mobileNavOpen;
    btn.setAttribute('aria-expanded', state.mobileNavOpen ? 'true' : 'false');
    drawer.setAttribute('aria-hidden', state.mobileNavOpen ? 'false' : 'true');
    drawer.style.display = state.mobileNavOpen ? 'block' : 'none';
  });

  // Close drawer on clicking links
  drawer.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', () => {
      state.mobileNavOpen = false;
      btn.setAttribute('aria-expanded', 'false');
      drawer.setAttribute('aria-hidden', 'true');
      drawer.style.display = 'none';
    });
  });
}

// ============================================================================
// 5. ONBOARDING & SCOPING DEMONSTRATION FORM
// ============================================================================
function setupOnboardingForm() {
  const form = document.getElementById('project-scoping-form');
  const confBox = document.getElementById('form-confirmation');
  const detailsEl = document.getElementById('conf-details');
  const resetBtn = document.getElementById('btn-reset-form');

  if (!form || !confBox) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const org = document.getElementById('input-org').value.trim();
    const contact = document.getElementById('input-contact').value.trim();
    const email = document.getElementById('input-email').value.trim();
    const origin = document.getElementById('input-origin').value;
    const vol = document.getElementById('input-capacity').value;
    const curCook = document.getElementById('input-cur-cook').value || 'Unspecified';
    const tgtCook = document.getElementById('input-tgt-cook').value || '15';

    if (!org || !contact || !email || !origin || !vol) {
      alert('Please fill in all required fields marked with an asterisk (*).');
      return;
    }

    // Show demonstration confirmation
    if (detailsEl) {
      detailsEl.innerHTML = `
        <strong>Organization:</strong> ${org}<br>
        <strong>Technical Contact:</strong> ${contact} (${email})<br>
        <strong>Consignment:</strong> ${origin} &bull; <strong>Target Capacity:</strong> ${vol}<br>
        <strong>Cooking Time Reduction:</strong> From ${curCook} min &rarr; Target ${tgtCook} min.<br><br>
        <em>Parameters logged in local demo environment. No external network request was emitted.</em>
      `;
    }

    form.classList.add('is-hidden');
    confBox.classList.remove('is-hidden');
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      form.reset();
      confBox.classList.add('is-hidden');
      form.classList.remove('is-hidden');
    });
  }
}

// ============================================================================
// 6. ON-DEMAND THREE.JS 3D MASTER ASSEMBLY VIEWER (MODAL)
// ============================================================================
function setup3DModal() {
  const openBtn = document.getElementById('btn-view-3d-modal');
  const closeBtn = document.getElementById('btn-close-3d-modal');
  const modal = document.getElementById('modal-3d');

  if (!openBtn || !closeBtn || !modal) return;

  openBtn.addEventListener('click', () => {
    modal.classList.remove('is-hidden');
    modal.setAttribute('aria-hidden', 'false');

    if (!state.threeInitialized) {
      initThreeModal();
      state.threeInitialized = true;
    } else {
      onModalResize();
    }
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.add('is-hidden');
    modal.setAttribute('aria-hidden', 'true');
  });

  // Close on outside backdrop click
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.add('is-hidden');
      modal.setAttribute('aria-hidden', 'true');
    }
  });

  // Modal Camera Preset Controls
  const camPresets = {
    iso: [-13.5, 9.5, 13.5, 0.0, 2.6, -3.0],
    front: [0.0, 5.0, 18.0, 0.0, 3.0, -3.0],
    side: [18.0, 5.5, -3.0, 0.0, 3.0, -3.0],
    top: [0.0, 24.0, -3.0, 0.0, 0.0, -3.0]
  };

  document.querySelectorAll('.modal-hud-controls button[data-view]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.modal-hud-controls button[data-view]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const preset = camPresets[btn.dataset.view];
      if (preset && camera && controls) {
        camera.position.set(preset[0], preset[1], preset[2]);
        controls.target.set(preset[3], preset[4], preset[5]);
        controls.update();
      }
    });
  });

  const turntableBtn = document.getElementById('btn-modal-turntable');
  if (turntableBtn) {
    turntableBtn.addEventListener('click', () => {
      state.autoRotate = !state.autoRotate;
      turntableBtn.classList.toggle('active', state.autoRotate);
    });
  }
}

function initThreeModal() {
  const container = document.getElementById('canvas-container');
  if (!container) return;

  const width = container.clientWidth || 800;
  const height = container.clientHeight || 500;

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x070B14);

  // Camera
  camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 1000);
  camera.position.set(-13.5, 9.5, 13.5);

  // Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;
  container.appendChild(renderer.domElement);

  // OrbitControls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.target.set(0.0, 2.6, -3.0);
  controls.update();

  // Lighting
  const hemiLight = new THREE.HemisphereLight(0xFFFFFF, 0x1E293B, 1.2);
  hemiLight.position.set(0, 50, 0);
  scene.add(hemiLight);

  const keyLight = new THREE.DirectionalLight(0xFFFFFF, 2.0);
  keyLight.position.set(15, 25, 20);
  scene.add(keyLight);

  const fillLight = new THREE.DirectionalLight(0x38BDF8, 0.8);
  fillLight.position.set(-20, 10, -15);
  scene.add(fillLight);

  // Grid floor
  const gridHelper = new THREE.GridHelper(30, 30, 0x334155, 0x1E293B);
  gridHelper.position.y = -0.05;
  scene.add(gridHelper);

  // Load Model
  const loader = new GLTFLoader();
  const loadingIndicator = document.getElementById('canvas-loading');

  loader.load('/models/plant_15t_assembly.glb', (gltf) => {
    const model = gltf.scene;
    scene.add(model);
    modelLoaded = true;

    if (loadingIndicator) {
      loadingIndicator.style.display = 'none';
    }
  }, undefined, (err) => {
    console.warn('GLB load notice:', err);
    if (loadingIndicator) {
      loadingIndicator.textContent = '3D Model Viewport (Static preview active)';
    }
  });

  window.addEventListener('resize', onModalResize);
  animateModal();
}

function onModalResize() {
  const container = document.getElementById('canvas-container');
  if (!container || !renderer || !camera) return;

  const width = container.clientWidth;
  const height = container.clientHeight;
  if (width === 0 || height === 0) return;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

function animateModal() {
  requestAnimationFrame(animateModal);

  if (controls) {
    controls.autoRotate = state.autoRotate;
    controls.autoRotateSpeed = 1.0;
    controls.update();
  }

  if (renderer && scene && camera) {
    renderer.render(scene, camera);
  }
}
