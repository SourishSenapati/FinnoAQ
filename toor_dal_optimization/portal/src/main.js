// FinnoaQ 15 TPD Digital Twin & Engineering Command Application
// Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati | Academic Guidance: Dr. Archisman Ray (IIT KGP)

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

import {
  PROJECT_METADATA,
  EQUIPMENT_SPECS,
  STREAMS_DATA,
  MOTOR_LOAD_LIST,
  SCADA_TAGS,
  HAZOP_DATA,
  EQUIPMENT_SIZING_TABLE,
  DOSSIER_PAGES
} from './data/plantData.js';

// ============================================================================
// STATE STORE
// ============================================================================
const state = {
  currentTab: 'twin',
  cameraView: 'iso',
  renderMode: 'pbr',
  activeSubsystem: 'ALL',
  explodePercent: 0,
  autoRotate: false,
  selectedMesh: null,
  selectedEquipmentTag: null,
  activeDataSubtab: 'sizing',
  dataSearchQuery: '',
  dossierCurrentPage: 1,
  dossierDualMode: false,
  dossierZoom: 1.0,
  streamPhaseFilter: 'ALL'
};

// ============================================================================
// 1. THREE.JS 3D DIGITAL TWIN INITIALIZATION
// ============================================================================
let scene, camera, renderer, controls;
let modelRoot = null;
const meshRegistry = new Map(); // name -> { mesh, origMaterial, origPosition, origParent, specKey }
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
let hoveredMesh = null;

// Camera preset viewpoints [eyeX, eyeY, eyeZ, targetX, targetY, targetZ]
const CAMERA_PRESETS = {
  iso: [-13.5, 9.5, 13.5, 0.0, 2.6, -3.0],
  reverse: [13.5, 9.0, -13.5, 0.0, 2.6, -3.0],
  front: [0.0, 5.0, 18.0, 0.0, 3.0, -3.0],
  side: [18.0, 5.5, -3.0, 0.0, 3.0, -3.0],
  top: [0.0, 24.0, -3.0, 0.0, 0.0, -3.0],
  platform: [-3.8, 5.8, 3.2, -1.0, 4.2, 0.0]
};

// Subsystem grouping mapping
const SUBSYSTEM_MAPPING = {
  SOAKING: ['TK-101_Soak_Tank', 'TK-101_Soak_Tank_1', 'AG-101_Agitator', 'AG-101_Agitator_1'],
  DEWATERING: ['SC-101_Dewatering_Screen', 'CHU-100_Transfer_Chutes'],
  DRYING: ['DR-101_Fluid_Bed_Dryer', 'CY-101_Cyclone_Separator'],
  EVAPORATOR: ['EV-101_ZLD_Evaporator'],
  DOSING: ['SK-100_Dosing_Skid'],
  STRUCTURE: ['STR-100_Mezzanine_Platform'],
  PIPING: ['PIP-100_Interconnecting_Piping']
};

// Explode displacement vectors (meters at 100%)
const EXPLODE_VECTORS = {
  'TK-101_Soak_Tank': new THREE.Vector3(-2.5, 0.5, 2.0),
  'TK-101_Soak_Tank_1': new THREE.Vector3(2.5, 0.5, 2.0),
  'AG-101_Agitator': new THREE.Vector3(-2.5, 3.5, 2.0),
  'AG-101_Agitator_1': new THREE.Vector3(2.5, 3.5, 2.0),
  'CHU-100_Transfer_Chutes': new THREE.Vector3(0.0, -1.0, 3.0),
  'SC-101_Dewatering_Screen': new THREE.Vector3(0.0, -1.5, 5.0),
  'DR-101_Fluid_Bed_Dryer': new THREE.Vector3(0.0, 0.0, -4.5),
  'CY-101_Cyclone_Separator': new THREE.Vector3(4.0, 2.5, -4.5),
  'SK-100_Dosing_Skid': new THREE.Vector3(-5.0, 0.0, 0.0),
  'EV-101_ZLD_Evaporator': new THREE.Vector3(0.0, 0.0, -8.0),
  'STR-100_Mezzanine_Platform': new THREE.Vector3(0.0, -3.0, 0.0),
  'PIP-100_Interconnecting_Piping': new THREE.Vector3(0.0, 3.0, 0.0)
};

function initThree() {
  const container = document.getElementById('canvas-container');
  if (!container) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x070A11);
  scene.fog = new THREE.FogExp2(0x070A11, 0.015);

  // Camera
  camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 1000);
  setCameraPreset('iso', false);

  // Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'high-performance' });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.2;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  container.appendChild(renderer.domElement);

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.screenSpacePanning = true;
  controls.maxPolarAngle = Math.PI / 2 + 0.05; // don't go below floor
  controls.minDistance = 3.0;
  controls.maxDistance = 50.0;

  // Environment Lighting
  setupLighting();

  // Floor Grid
  setupGround();

  // Load GLB Model
  loadMasterAssembly();

  // Event Listeners
  window.addEventListener('resize', onWindowResize);
  renderer.domElement.addEventListener('mousemove', onMouseMove);
  renderer.domElement.addEventListener('click', onCanvasClick);

  // Animation Loop
  animate();
}

function setupLighting() {
  // Ambient fill
  const ambient = new THREE.AmbientLight(0x1E293B, 1.4);
  scene.add(ambient);

  // Hemisphere
  const hemi = new THREE.HemisphereLight(0x38BDF8, 0x0F172A, 1.0);
  scene.add(hemi);

  // Key Directional Sun
  const keyLight = new THREE.DirectionalLight(0xFFFFFF, 2.6);
  keyLight.position.set(-15, 25, 20);
  keyLight.castShadow = true;
  keyLight.shadow.mapSize.width = 2048;
  keyLight.shadow.mapSize.height = 2048;
  keyLight.shadow.camera.near = 0.5;
  keyLight.shadow.camera.far = 80;
  keyLight.shadow.camera.left = -16;
  keyLight.shadow.camera.right = 16;
  keyLight.shadow.camera.top = 16;
  keyLight.shadow.camera.bottom = -16;
  keyLight.shadow.bias = -0.0005;
  scene.add(keyLight);

  // Rim / Fill Light
  const fillLight = new THREE.DirectionalLight(0x00F0FF, 1.2);
  fillLight.position.set(18, 15, -18);
  scene.add(fillLight);

  // Under-skid Accent Light
  const floorGlow = new THREE.PointLight(0x0284C7, 2.0, 18);
  floorGlow.position.set(0, 0.5, -2);
  scene.add(floorGlow);
}

function setupGround() {
  // Circular ground grid
  const gridHelper = new THREE.GridHelper(40, 40, 0x00F0FF, 0x1E293B);
  gridHelper.position.y = -0.01;
  gridHelper.material.opacity = 0.25;
  gridHelper.material.transparent = true;
  scene.add(gridHelper);

  // Shadow receiver ground disk
  const groundGeo = new THREE.CircleGeometry(25, 64);
  const groundMat = new THREE.MeshStandardMaterial({
    color: 0x070A11,
    roughness: 0.9,
    metalness: 0.1
  });
  const ground = new THREE.Mesh(groundGeo, groundMat);
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);
}

function loadMasterAssembly() {
  const loader = new GLTFLoader();
  const loadingOverlay = document.getElementById('three-loading-overlay');

  loader.load(
    '/models/plant_15t_assembly.glb',
    (gltf) => {
      modelRoot = gltf.scene;
      scene.add(modelRoot);

      // Register and enhance materials
      modelRoot.traverse((child) => {
        if (child.isMesh) {
          child.castShadow = true;
          child.receiveShadow = true;

          // Find equipment spec key matching mesh name
          let matchedKey = null;
          for (const key of Object.keys(EQUIPMENT_SPECS)) {
            if (child.name.includes(key) || key.includes(child.name)) {
              matchedKey = key;
              break;
            }
          }
          if (!matchedKey && child.name.includes('TK-101_Soak_Tank')) matchedKey = 'TK-101_Soak_Tank';
          if (!matchedKey && child.name.includes('AG-101_Agitator')) matchedKey = 'AG-101_Agitator';

          // Assign realistic stainless steel PBR material if default is generic
          enhanceMeshMaterial(child);

          meshRegistry.set(child.name, {
            mesh: child,
            origMaterial: child.material,
            origPosition: child.position.clone(),
            specKey: matchedKey
          });
        }
      });

      // Hide loading overlay
      if (loadingOverlay) {
        loadingOverlay.classList.add('fade-out');
        setTimeout(() => loadingOverlay.style.display = 'none', 500);
      }

      console.log(`[FinnoaQ 3D Twin] Master Assembly loaded successfully. Registered ${meshRegistry.size} meshes.`);
    },
    (xhr) => {
      if (xhr.lengthComputable) {
        const percent = Math.round((xhr.loaded / xhr.total) * 100);
        const subText = document.querySelector('.loading-sub');
        if (subText) subText.textContent = `Streaming SolidWorks 2025 SP01.2 Geometry: ${percent}%`;
      }
    },
    (err) => {
      console.error('[FinnoaQ 3D Twin] Error loading master assembly GLB:', err);
      const loadingOverlay = document.getElementById('three-loading-overlay');
      if (loadingOverlay) {
        loadingOverlay.innerHTML = `<div style="color: #EF4444; font-weight: 700;">Error Loading 3D Model: ${err.message}</div>`;
      }
    }
  );
}

function enhanceMeshMaterial(mesh) {
  // Differentiate visual materials based on equipment type
  const name = mesh.name;
  let color = 0xD4D4D8; // default SS304 bright satin
  let metalness = 0.85;
  let roughness = 0.28;

  if (name.includes('STR-100')) {
    // Structural steel mezzanine: Industrial safety blue / epoxy grey
    color = 0x2A374A;
    metalness = 0.4;
    roughness = 0.55;
  } else if (name.includes('TK-101')) {
    // Cylindrical soak tanks: mirror/satin stainless steel
    color = 0xE2E8F0;
    metalness = 0.9;
    roughness = 0.2;
  } else if (name.includes('AG-101')) {
    // Agitator & shaft: SS316L high polished
    color = 0xF1F5F9;
    metalness = 0.95;
    roughness = 0.15;
  } else if (name.includes('DR-101')) {
    // Fluid Bed Dryer: Insulated casing with stainless plenum
    color = 0xCBD5E1;
    metalness = 0.75;
    roughness = 0.35;
  } else if (name.includes('CY-101')) {
    // Sanitary Cyclone: Smooth polished stainless steel
    color = 0xE2E8F0;
    metalness = 0.9;
    roughness = 0.25;
  } else if (name.includes('EV-101')) {
    // ZLD Evaporator Calandrias: SS316L polished tubes and shell
    color = 0x93C5FD;
    metalness = 0.8;
    roughness = 0.25;
  } else if (name.includes('SK-100')) {
    // Chemical skid: Compact dosing package
    color = 0x38BDF8;
    metalness = 0.6;
    roughness = 0.4;
  } else if (name.includes('PIP-100')) {
    // Interconnecting process piping: Bright stainless tube
    color = 0x38BDF8;
    metalness = 0.9;
    roughness = 0.2;
  }

  mesh.material = new THREE.MeshStandardMaterial({
    color: color,
    metalness: metalness,
    roughness: roughness,
    envMapIntensity: 1.2
  });
}

function setCameraPreset(presetKey, animateTransition = true) {
  const p = CAMERA_PRESETS[presetKey];
  if (!p || !camera || !controls) return;

  state.cameraView = presetKey;
  updateCameraHUDButtons();

  if (!animateTransition) {
    camera.position.set(p[0], p[1], p[2]);
    controls.target.set(p[3], p[4], p[5]);
    controls.update();
  } else {
    smoothMoveCamera(
      new THREE.Vector3(p[0], p[1], p[2]),
      new THREE.Vector3(p[3], p[4], p[5]),
      800
    );
  }
}

function smoothMoveCamera(targetPos, targetLookAt, duration = 600) {
  const startPos = camera.position.clone();
  const startTarget = controls.target.clone();
  const startTime = performance.now();

  function step(now) {
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1.0);
    // Smooth easeInOutQuad
    const t = progress < 0.5 ? 2 * progress * progress : -1 + (4 - 2 * progress) * progress;

    camera.position.lerpVectors(startPos, targetPos, t);
    controls.target.lerpVectors(startTarget, targetLookAt, t);
    controls.update();

    if (progress < 1.0) {
      requestAnimationFrame(step);
    }
  }
  requestAnimationFrame(step);
}

function setRenderMode(mode) {
  state.renderMode = mode;
  updateRenderModeButtons();

  meshRegistry.forEach(({ mesh, origMaterial }) => {
    if (mode === 'pbr') {
      mesh.material = origMaterial;
      mesh.material.wireframe = false;
    } else if (mode === 'clay') {
      mesh.material = new THREE.MeshStandardMaterial({
        color: 0xE2E8F0,
        roughness: 0.85,
        metalness: 0.05
      });
    } else if (mode === 'wireframe') {
      mesh.material = new THREE.MeshBasicMaterial({
        color: 0x00F0FF,
        wireframe: true
      });
    } else if (mode === 'xray') {
      mesh.material = new THREE.MeshStandardMaterial({
        color: 0x38BDF8,
        transparent: true,
        opacity: 0.3,
        roughness: 0.2,
        metalness: 0.9,
        depthWrite: false
      });
    }
  });
}

function setExplodeView(percent) {
  state.explodePercent = percent;
  const factor = percent / 100;

  meshRegistry.forEach(({ mesh, origPosition }) => {
    let displaceVec = null;
    for (const [key, vec] of Object.entries(EXPLODE_VECTORS)) {
      if (mesh.name.includes(key)) {
        displaceVec = vec;
        break;
      }
    }

    if (displaceVec) {
      mesh.position.copy(origPosition).addScaledVector(displaceVec, factor);
    }
  });

  const explodeValEl = document.getElementById('explode-val');
  if (explodeValEl) explodeValEl.textContent = `${percent}%`;
}

function filterSubsystem(subsystemKey) {
  state.activeSubsystem = subsystemKey;
  updateSubsystemFilterPills();

  if (subsystemKey === 'ALL') {
    meshRegistry.forEach(({ mesh }) => {
      mesh.visible = true;
      if (mesh.material && mesh.material.opacity !== undefined) {
        mesh.material.opacity = 1.0;
        mesh.material.transparent = false;
      }
    });
    return;
  }

  const allowedPrefixes = SUBSYSTEM_MAPPING[subsystemKey] || [];
  meshRegistry.forEach(({ mesh }) => {
    const isMember = allowedPrefixes.some(prefix => mesh.name.includes(prefix));
    if (isMember) {
      mesh.visible = true;
      if (mesh.material) {
        mesh.material.opacity = 1.0;
        mesh.material.transparent = false;
      }
    } else {
      // Semi-transparent ghosting rather than complete hiding for context
      mesh.visible = true;
      if (mesh.material) {
        mesh.material.transparent = true;
        mesh.material.opacity = 0.08;
      }
    }
  });
}

function onMouseMove(event) {
  const rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children, true);

  // Filter out ground disk & grid
  const validIntersects = intersects.filter(i => i.object.isMesh && i.object.name && !i.object.name.includes('Circle'));

  if (validIntersects.length > 0) {
    const hit = validIntersects[0].object;
    if (hoveredMesh !== hit) {
      if (hoveredMesh && hoveredMesh !== state.selectedMesh && hoveredMesh.material.emissive) {
        hoveredMesh.material.emissive.setHex(0x000000);
      }
      hoveredMesh = hit;
      if (hoveredMesh.material && hoveredMesh.material.emissive) {
        hoveredMesh.material.emissive.setHex(0x002B47);
      }
      renderer.domElement.style.cursor = 'pointer';
    }
  } else {
    if (hoveredMesh && hoveredMesh !== state.selectedMesh && hoveredMesh.material.emissive) {
      hoveredMesh.material.emissive.setHex(0x000000);
    }
    hoveredMesh = null;
    renderer.domElement.style.cursor = 'default';
  }
}

function onCanvasClick(event) {
  const rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children, true);
  const validIntersects = intersects.filter(i => i.object.isMesh && i.object.name && !i.object.name.includes('Circle'));

  if (validIntersects.length > 0) {
    const hit = validIntersects[0].object;
    selectEquipment(hit);
  }
}

function selectEquipment(mesh) {
  // Clear previous selection highlight
  if (state.selectedMesh && state.selectedMesh.material && state.selectedMesh.material.emissive) {
    state.selectedMesh.material.emissive.setHex(0x000000);
  }

  state.selectedMesh = mesh;
  if (mesh.material && mesh.material.emissive) {
    mesh.material.emissive.setHex(0x004B7A);
  }

  // Find spec
  const regEntry = meshRegistry.get(mesh.name);
  let specKey = regEntry ? regEntry.specKey : null;
  if (!specKey) {
    for (const key of Object.keys(EQUIPMENT_SPECS)) {
      if (mesh.name.includes(key)) {
        specKey = key;
        break;
      }
    }
  }

  if (specKey && EQUIPMENT_SPECS[specKey]) {
    state.selectedEquipmentTag = specKey;
    displayEquipmentInInspector(EQUIPMENT_SPECS[specKey]);
  }
}

function displayEquipmentInInspector(spec) {
  const drawer = document.getElementById('equipment-inspector');
  if (!drawer) return;

  document.getElementById('insp-tag').textContent = spec.tag;
  document.getElementById('insp-name').textContent = spec.name;
  document.getElementById('insp-category').textContent = spec.category;
  document.getElementById('insp-code').textContent = spec.designCode;
  document.getElementById('insp-dim').textContent = spec.dimensions;
  document.getElementById('insp-vol').textContent = spec.volume;
  document.getElementById('insp-moc').textContent = spec.moc;
  document.getElementById('insp-wt').textContent = `${spec.emptyWeight} / ${spec.fullWeight}`;
  document.getElementById('insp-op').textContent = `${spec.operatingTemp} / ${spec.operatingPress}`;
  document.getElementById('insp-motor').textContent = spec.motorKw;
  document.getElementById('insp-scada').textContent = spec.scadaTag;
  document.getElementById('insp-desc').textContent = spec.description;

  // Nozzles Table
  const tbody = document.getElementById('insp-nozzles-tbody');
  tbody.innerHTML = '';
  if (spec.nozzles && spec.nozzles.length > 0) {
    spec.nozzles.forEach(n => {
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${n.tag}</td><td>${n.size}</td><td>${n.desc}</td>`;
      tbody.appendChild(tr);
    });
    document.getElementById('insp-nozzle-section').style.display = 'block';
  } else {
    document.getElementById('insp-nozzle-section').style.display = 'none';
  }

  drawer.classList.add('open');
}

function closeInspector() {
  const drawer = document.getElementById('equipment-inspector');
  if (drawer) drawer.classList.remove('open');
  if (state.selectedMesh && state.selectedMesh.material && state.selectedMesh.material.emissive) {
    state.selectedMesh.material.emissive.setHex(0x000000);
  }
  state.selectedMesh = null;
  state.selectedEquipmentTag = null;
}

function onWindowResize() {
  const container = document.getElementById('canvas-container');
  if (!container || !renderer || !camera) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

function animate() {
  requestAnimationFrame(animate);

  if (controls) {
    controls.autoRotate = state.autoRotate;
    controls.autoRotateSpeed = 1.0;
    controls.update();
  }

  // Telemetry Position Output
  const camPosEl = document.getElementById('cam-pos-display');
  if (camPosEl && camera) {
    camPosEl.textContent = `X: ${camera.position.x.toFixed(1)} Y: ${camera.position.y.toFixed(1)} Z: ${camera.position.z.toFixed(1)}`;
  }

  if (renderer && scene && camera) {
    renderer.render(scene, camera);
  }
}

// UI Helpers for 3D HUD
function updateCameraHUDButtons() {
  document.querySelectorAll('#camera-presets-group .hud-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.view === state.cameraView);
  });
}

function updateRenderModeButtons() {
  document.querySelectorAll('#render-modes-group .hud-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.mode === state.renderMode);
  });
}

function updateSubsystemFilterPills() {
  document.querySelectorAll('#subsystem-filters .filter-pill').forEach(pill => {
    pill.classList.toggle('active', pill.dataset.subsystem === state.activeSubsystem);
  });
}

// ============================================================================
// 2. TAB SWITCHING SYSTEM
// ============================================================================
function setupTabs() {
  const tabButtons = document.querySelectorAll('.nav-tab');
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.dataset.tab;
      switchTab(targetTab);
    });
  });
}

function switchTab(tabId) {
  state.currentTab = tabId;

  // Update nav buttons
  document.querySelectorAll('.nav-tab').forEach(b => {
    const isActive = b.dataset.tab === tabId;
    b.classList.toggle('active', isActive);
    b.setAttribute('aria-selected', isActive ? 'true' : 'false');
  });

  // Update panels
  document.querySelectorAll('.tab-panel').forEach(p => {
    p.classList.toggle('active', p.id === `tab-panel-${tabId}`);
  });

  // If 3D tab activated, resize renderer
  if (tabId === 'twin') {
    setTimeout(onWindowResize, 50);
  }
}

// ============================================================================
// 3. TAB 2: PROCESS FLOW & ASPEN V14 STREAMS
// ============================================================================
function setupStreamsView() {
  renderStreamCards(STREAMS_DATA);

  // Phase Filter Buttons
  document.querySelectorAll('.stream-filter-btns .filter-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.stream-filter-btns .filter-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const phase = btn.dataset.phaseFilter;
      state.streamPhaseFilter = phase;

      if (phase === 'ALL') {
        renderStreamCards(STREAMS_DATA);
      } else {
        const filtered = STREAMS_DATA.filter(s => s.phase.toLowerCase().includes(phase.toLowerCase()));
        renderStreamCards(filtered);
      }
    });
  });

  // Stage block anchor pills
  document.querySelectorAll('.stream-badge-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      const streamId = pill.dataset.stream;
      highlightStreamCard(streamId);
    });
  });
}

function renderStreamCards(streams) {
  const container = document.getElementById('stream-cards-container');
  if (!container) return;

  container.innerHTML = '';
  streams.forEach(s => {
    const card = document.createElement('div');
    card.className = 'stream-card';
    card.id = `stream-card-${s.id}`;
    card.innerHTML = `
      <div class="stream-card-header">
        <span class="stream-id-badge">${s.id}</span>
        <span class="stream-phase-badge">${s.phase}</span>
      </div>
      <div class="stream-name">${s.name}</div>
      <div class="stream-route">
        <span>${s.source}</span>
        <span class="arrow">&rarr;</span>
        <span>${s.dest}</span>
      </div>
      <div class="stream-metrics-grid">
        <div class="sm-item"><span class="sm-k">Mass Flow:</span><span class="sm-v highlight">${s.massFlow.toLocaleString('en-US', { minimumFractionDigits: 1 })} kg/h</span></div>
        <div class="sm-item"><span class="sm-k">Temperature:</span><span class="sm-v">${s.temp.toFixed(1)} °C</span></div>
        <div class="sm-item"><span class="sm-k">Pressure:</span><span class="sm-v">${s.press.toFixed(3)} bar</span></div>
        <div class="sm-item"><span class="sm-k">Dry Solids:</span><span class="sm-v">${s.solidsPct.toFixed(1)}% w/w</span></div>
      </div>
      <div class="stream-desc">${s.desc}</div>
    `;

    card.addEventListener('click', () => {
      document.querySelectorAll('.stream-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
    });

    container.appendChild(card);
  });
}

function highlightStreamCard(streamId) {
  const card = document.getElementById(`stream-card-${streamId}`);
  if (card) {
    document.querySelectorAll('.stream-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

// ============================================================================
// 4. TAB 3: ENGINEERING DATA HUB
// ============================================================================
function setupDataHub() {
  const subtabs = document.querySelectorAll('#data-subtabs-nav .subtab-btn');
  subtabs.forEach(btn => {
    btn.addEventListener('click', () => {
      subtabs.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      state.activeDataSubtab = btn.dataset.subtab;
      renderActiveDataTable();
    });
  });

  const searchInput = document.getElementById('hub-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.dataSearchQuery = e.target.value.toLowerCase().trim();
      renderActiveDataTable();
    });
  }

  const exportBtn = document.getElementById('btn-export-csv');
  if (exportBtn) {
    exportBtn.addEventListener('click', exportActiveTableToCSV);
  }

  // Initial render
  renderActiveDataTable();
}

function renderActiveDataTable() {
  const wrapper = document.getElementById('hub-table-wrapper');
  if (!wrapper) return;

  const subtab = state.activeDataSubtab;
  const q = state.dataSearchQuery;

  if (subtab === 'sizing') {
    const data = EQUIPMENT_SIZING_TABLE.filter(r =>
      !q || r.tag.toLowerCase().includes(q) || r.name.toLowerCase().includes(q) || r.code.toLowerCase().includes(q) || r.moc.toLowerCase().includes(q)
    );
    wrapper.innerHTML = `
      <table class="engineering-table" id="active-eng-table">
        <thead>
          <tr>
            <th>Tag</th><th>Equipment Name</th><th>ASME / Design Code</th><th>Dimensions</th><th>Length / Height</th>
            <th>Gross Vol</th><th>Operating Param</th><th>MOC</th><th>Power (kW)</th><th>Op Temp</th><th>Op Press</th>
          </tr>
        </thead>
        <tbody>
          ${data.map(r => `
            <tr>
              <td class="tag-cell">${r.tag}</td>
              <td><strong>${r.name}</strong></td>
              <td>${r.code}</td>
              <td>${r.shellId}</td>
              <td>${r.tanLength}</td>
              <td>${r.grossVol}</td>
              <td>${r.workVol}</td>
              <td>${r.moc}</td>
              <td class="kw-cell">${r.motorKw > 0 ? r.motorKw.toFixed(2) + ' kW' : 'Static'}</td>
              <td>${r.opTemp}</td>
              <td>${r.opPress}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  } else if (subtab === 'electrical') {
    const data = MOTOR_LOAD_LIST.filter(r =>
      !q || r.tag.toLowerCase().includes(q) || r.equip.toLowerCase().includes(q) || r.mcc.toLowerCase().includes(q)
    );
    wrapper.innerHTML = `
      <table class="engineering-table" id="active-eng-table">
        <thead>
          <tr><th>Motor Tag</th><th>Equipment Service Description</th><th>Rating (kW)</th><th>Voltage (V)</th><th>FLA (A)</th><th>MCC Bus</th><th>VFD Duty</th></tr>
        </thead>
        <tbody>
          ${data.map(r => `
            <tr style="${r.tag === 'TOTAL' ? 'font-weight: 800; background: rgba(0, 240, 255, 0.1);' : ''}">
              <td class="tag-cell">${r.tag}</td>
              <td>${r.equip}</td>
              <td class="kw-cell">${r.kw.toFixed(2)} kW</td>
              <td>${r.v} V</td>
              <td>${r.fla.toFixed(1)} A</td>
              <td>${r.mcc}</td>
              <td>${r.vfd ? '<span style="color: #00F0FF; font-weight: 700;">YES (Inverter Duty)</span>' : 'DOL / Soft Starter'}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  } else if (subtab === 'scada') {
    const data = SCADA_TAGS.filter(r =>
      !q || r.tag.toLowerCase().includes(q) || r.desc.toLowerCase().includes(q) || r.type.toLowerCase().includes(q)
    );
    wrapper.innerHTML = `
      <table class="engineering-table" id="active-eng-table">
        <thead>
          <tr><th>ISA-5.1 Tag</th><th>Loop Description</th><th>Signal Type</th><th>Calibrated Range</th><th>Normal Setpoint</th><th>Trip / Alarm Limits</th></tr>
        </thead>
        <tbody>
          ${data.map(r => `
            <tr>
              <td class="tag-cell">${r.tag}</td>
              <td>${r.desc}</td>
              <td>${r.type}</td>
              <td>${r.range}</td>
              <td><strong style="color: #10B981;">${r.sp}</strong></td>
              <td><span style="color: #F59E0B;">${r.alarm}</span></td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  } else if (subtab === 'hazop') {
    const data = HAZOP_DATA.filter(r =>
      !q || r.node.toLowerCase().includes(q) || r.param.toLowerCase().includes(q) || r.deviation.toLowerCase().includes(q) || r.cause.toLowerCase().includes(q)
    );
    wrapper.innerHTML = `
      <table class="engineering-table" id="active-eng-table">
        <thead>
          <tr><th>Process Node</th><th>Parameter</th><th>Deviation</th><th>Root Cause</th><th>Consequence</th><th>Existing Safeguards</th><th>Action Item</th></tr>
        </thead>
        <tbody>
          ${data.map(r => `
            <tr>
              <td class="tag-cell">${r.node}</td>
              <td><strong>${r.param}</strong></td>
              <td><span style="color: #EF4444; font-weight: 700;">${r.deviation}</span></td>
              <td>${r.cause}</td>
              <td>${r.consequence}</td>
              <td>${r.safeguards}</td>
              <td><em style="color: #38BDF8;">${r.action}</em></td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  } else if (subtab === 'streams-table') {
    const data = STREAMS_DATA.filter(r =>
      !q || r.id.toLowerCase().includes(q) || r.name.toLowerCase().includes(q) || r.phase.toLowerCase().includes(q)
    );
    wrapper.innerHTML = `
      <table class="engineering-table" id="active-eng-table">
        <thead>
          <tr><th>Stream ID</th><th>Stream Name</th><th>Source</th><th>Destination</th><th>Mass Flow (kg/h)</th><th>Temp (°C)</th><th>Press (bar)</th><th>Phase</th><th>Dry Solids %</th><th>Process Function</th></tr>
        </thead>
        <tbody>
          ${data.map(r => `
            <tr>
              <td class="tag-cell">${r.id}</td>
              <td><strong>${r.name}</strong></td>
              <td>${r.source}</td>
              <td>${r.dest}</td>
              <td class="kw-cell">${r.massFlow.toFixed(1)}</td>
              <td>${r.temp.toFixed(1)}</td>
              <td>${r.press.toFixed(3)}</td>
              <td>${r.phase}</td>
              <td>${r.solidsPct.toFixed(1)}%</td>
              <td>${r.desc}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  }
}

function exportActiveTableToCSV() {
  const table = document.getElementById('active-eng-table');
  if (!table) return;

  const rows = Array.from(table.querySelectorAll('tr'));
  const csvContent = rows.map(r => {
    const cells = Array.from(r.querySelectorAll('th, td'));
    return cells.map(c => `"${c.textContent.replace(/"/g, '""')}"`).join(',');
  }).join('\n');

  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.setAttribute('href', url);
  link.setAttribute('download', `FinnoaQ_15TPD_${state.activeDataSubtab.toUpperCase()}_SCHEDULE.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// ============================================================================
// 5. TAB 4: 50-PAGE MASTER DOSSIER READER
// ============================================================================
function setupDossierReader() {
  renderDossierThumbnails(DOSSIER_PAGES);

  // Prev / Next controls
  const prevBtn = document.getElementById('btn-doc-prev');
  const nextBtn = document.getElementById('btn-doc-next');
  const pageInput = document.getElementById('doc-page-input');

  if (prevBtn) prevBtn.addEventListener('click', () => changeDossierPage(state.dossierCurrentPage - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => changeDossierPage(state.dossierCurrentPage + 1));
  if (pageInput) {
    pageInput.addEventListener('change', (e) => {
      const p = parseInt(e.target.value, 10);
      if (!isNaN(p)) changeDossierPage(p);
    });
  }

  // Dual Page Mode Toggle
  const dualBtn = document.getElementById('btn-dual-mode');
  if (dualBtn) {
    dualBtn.addEventListener('click', () => {
      state.dossierDualMode = !state.dossierDualMode;
      dualBtn.classList.toggle('highlight', state.dossierDualMode);
      dualBtn.textContent = state.dossierDualMode ? 'Dual-Page Mode [Active]' : 'Dual-Page View';
      updateDossierDisplay();
    });
  }

  // Zoom buttons
  const zoomIn = document.getElementById('btn-zoom-in');
  const zoomOut = document.getElementById('btn-zoom-out');
  const zoomReset = document.getElementById('btn-zoom-reset');

  if (zoomIn) zoomIn.addEventListener('click', () => setDossierZoom(state.dossierZoom + 0.2));
  if (zoomOut) zoomOut.addEventListener('click', () => setDossierZoom(state.dossierZoom - 0.2));
  if (zoomReset) zoomReset.addEventListener('click', () => setDossierZoom(1.0));

  // Chapter filter pills
  document.querySelectorAll('.chapter-quick-nav .chapter-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.chapter-quick-nav .chapter-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const sec = btn.dataset.secFilter;

      if (sec === 'ALL') {
        renderDossierThumbnails(DOSSIER_PAGES);
      } else {
        const filtered = DOSSIER_PAGES.filter(p => p.section.includes(sec));
        renderDossierThumbnails(filtered);
      }
    });
  });

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (state.currentTab !== 'dossier') return;
    if (e.key === 'ArrowLeft') changeDossierPage(state.dossierCurrentPage - 1);
    if (e.key === 'ArrowRight') changeDossierPage(state.dossierCurrentPage + 1);
  });
}

function renderDossierThumbnails(pages) {
  const container = document.getElementById('dossier-thumbnail-container');
  if (!container) return;

  container.innerHTML = '';
  pages.forEach(p => {
    const item = document.createElement('div');
    item.className = `thumb-item ${p.pageNumber === state.dossierCurrentPage ? 'active' : ''}`;
    item.id = `thumb-item-${p.pageNumber}`;
    item.innerHTML = `
      <img src="${p.image}" class="thumb-img" alt="Page ${p.pad}" loading="lazy" />
      <div class="thumb-meta">
        <span class="thumb-pnum">PAGE ${p.pad}</span>
        <span class="thumb-title" title="${p.title}">${p.title}</span>
      </div>
    `;

    item.addEventListener('click', () => {
      changeDossierPage(p.pageNumber);
    });

    container.appendChild(item);
  });
}

function changeDossierPage(pageNum) {
  if (pageNum < 1) pageNum = 1;
  if (pageNum > 50) pageNum = 50;
  state.dossierCurrentPage = pageNum;

  // Update Page Input
  const pageInput = document.getElementById('doc-page-input');
  if (pageInput) pageInput.value = pageNum;

  // Update Active Title
  const activePageData = DOSSIER_PAGES[pageNum - 1];
  const titleBanner = document.getElementById('doc-active-title');
  if (titleBanner && activePageData) {
    titleBanner.textContent = `Page ${activePageData.pad}: ${activePageData.title}`;
  }

  // Update Thumbnail Active State
  document.querySelectorAll('.thumb-item').forEach(t => t.classList.remove('active'));
  const activeThumb = document.getElementById(`thumb-item-${pageNum}`);
  if (activeThumb) {
    activeThumb.classList.add('active');
    activeThumb.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  updateDossierDisplay();
}

function updateDossierDisplay() {
  const primaryImg = document.getElementById('dossier-primary-page');
  const secondaryImg = document.getElementById('dossier-secondary-page');
  if (!primaryImg || !secondaryImg) return;

  const pageNum = state.dossierCurrentPage;
  const pad = String(pageNum).padStart(2, '0');
  primaryImg.src = `/dossier_pages/page_${pad}.png`;

  if (state.dossierDualMode && pageNum < 50) {
    const nextPad = String(pageNum + 1).padStart(2, '0');
    secondaryImg.src = `/dossier_pages/page_${nextPad}.png`;
    secondaryImg.style.display = 'block';
  } else {
    secondaryImg.style.display = 'none';
  }
}

function setDossierZoom(zoom) {
  zoom = Math.max(0.6, Math.min(2.5, zoom));
  state.dossierZoom = zoom;

  const wrapper = document.getElementById('page-display-wrapper');
  if (wrapper) {
    wrapper.style.transform = `scale(${zoom})`;
    wrapper.style.transformOrigin = 'center center';
  }

  const zoomReset = document.getElementById('btn-zoom-reset');
  if (zoomReset) zoomReset.textContent = `${Math.round(zoom * 100)}%`;
}

// ============================================================================
// 6. TAB 5: HANDOVER VAULT & MISC ACTIONS
// ============================================================================
function setupVault() {
  const exportJsonBtn = document.getElementById('btn-export-aspen-json');
  if (exportJsonBtn) {
    exportJsonBtn.addEventListener('click', () => {
      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify({
        project: PROJECT_METADATA,
        streams: STREAMS_DATA,
        equipment: EQUIPMENT_SPECS,
        sizing: EQUIPMENT_SIZING_TABLE,
        motors: MOTOR_LOAD_LIST,
        scada: SCADA_TAGS,
        hazop: HAZOP_DATA
      }, null, 2));

      const dlAnchor = document.createElement('a');
      dlAnchor.setAttribute('href', dataStr);
      dlAnchor.setAttribute('download', 'FINNOAQ_15TPD_ASPEN_V14_CONVERGED_EXPORT.json');
      document.body.appendChild(dlAnchor);
      dlAnchor.click();
      document.body.removeChild(dlAnchor);
    });
  }
}

// Jump from 3D Inspector to 2D AutoCAD Sheet in Dossier Reader
function setupInspectorActions() {
  const closeBtn = document.getElementById('btn-close-inspector');
  if (closeBtn) closeBtn.addEventListener('click', closeInspector);

  const jumpBtn = document.getElementById('btn-jump-dossier-page');
  if (jumpBtn) {
    jumpBtn.addEventListener('click', () => {
      const tag = state.selectedEquipmentTag;
      // Target pages in dossier
      let targetPage = 2; // default PFD
      if (tag.includes('TK-101')) targetPage = 14;
      else if (tag.includes('AG-101')) targetPage = 16;
      else if (tag.includes('CHU-100')) targetPage = 17;
      else if (tag.includes('SC-101')) targetPage = 18;
      else if (tag.includes('DR-101')) targetPage = 20;
      else if (tag.includes('CY-101')) targetPage = 22;
      else if (tag.includes('SK-100')) targetPage = 24;
      else if (tag.includes('EV-101')) targetPage = 26;
      else if (tag.includes('STR-100')) targetPage = 33;
      else if (tag.includes('PIP-100')) targetPage = 35;

      switchTab('dossier');
      changeDossierPage(targetPage);
    });
  }

  const isolateBtn = document.getElementById('btn-isolate-equipment');
  if (isolateBtn) {
    isolateBtn.addEventListener('click', () => {
      const tag = state.selectedEquipmentTag;
      if (!tag) return;

      // Find subsystem for this equipment
      for (const [subKey, members] of Object.entries(SUBSYSTEM_MAPPING)) {
        if (members.includes(tag)) {
          filterSubsystem(subKey);
          break;
        }
      }
    });
  }
}

// 3D HUD Event Handlers
function setupHUDControls() {
  // Camera Presets
  document.querySelectorAll('#camera-presets-group .hud-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      setCameraPreset(btn.dataset.view, true);
    });
  });

  // Render Modes
  document.querySelectorAll('#render-modes-group .hud-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      setRenderMode(btn.dataset.mode);
    });
  });

  // Explode slider
  const slider = document.getElementById('explode-slider');
  if (slider) {
    slider.addEventListener('input', (e) => {
      setExplodeView(parseInt(e.target.value, 10));
    });
  }

  // Turntable button
  const turntableBtn = document.getElementById('btn-turntable');
  if (turntableBtn) {
    turntableBtn.addEventListener('click', () => {
      state.autoRotate = !state.autoRotate;
      turntableBtn.classList.toggle('active', state.autoRotate);
    });
  }

  // Reset View
  const resetBtn = document.getElementById('btn-reset-view');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      setCameraPreset('iso', true);
      setExplodeView(0);
      if (slider) slider.value = 0;
      filterSubsystem('ALL');
      closeInspector();
    });
  }

  // Subsystem Filter Pills
  document.querySelectorAll('#subsystem-filters .filter-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      filterSubsystem(pill.dataset.subsystem);
    });
  });
}

// ============================================================================
// MAIN DOM INITIALIZATION
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
  console.log('[FinnoaQ Portal] Initializing Executive Command System...');

  setupTabs();
  initThree();
  setupHUDControls();
  setupInspectorActions();
  setupStreamsView();
  setupDataHub();
  setupDossierReader();
  setupVault();

  console.log('[FinnoaQ Portal] Ready. Project Ref: FNQ-PR-2026-001 | Lead: Sourish Senapati');
});
