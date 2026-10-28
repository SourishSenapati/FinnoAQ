import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const CAD_MODELS = [
  {
    id: 'assembly',
    name: 'PLANT-15T General Arrangement',
    file: '/models/plant_15t_assembly.glb',
    tag: 'PLANT-15T',
    scale: '1:1 Parametric Master',
    dimensions: '10.7m L x 7.5m W x 5.8m H',
    standard: 'ASME Sec VIII / NFPA 68',
    description: 'Complete 15,000 kg/day turnkey processing facility including mezzanine steel deck, twin steep tanks, transfer chutes, dewatering screen, fluid bed dryer, and ZLD evaporator.'
  },
  {
    id: 'tk101',
    name: 'TK-101A/B Ultrasonic Steeping Battery',
    file: '/models/TK-101_Soak_Tank.glb',
    tag: 'TK-101A/B',
    scale: 'Twin 2,500L',
    dimensions: '1.85m Dia x 3.2m H',
    standard: 'ASME Sec VIII Div 1',
    description: 'Vertical cylindrical bio-chelation vessel with conical bottom, dimple jacket, geared hydrofoil agitator, and 17 W/L ultrasonic transducer array.'
  },
  {
    id: 'dr101',
    name: 'DR-101A/B Two-Stage Fluid Bed Dryer',
    file: '/models/DR-101_Fluid_Bed_Dryer.glb',
    tag: 'DR-101A/B',
    scale: '850 kg/h Duty',
    dimensions: '4.8m L x 1.4m W x 2.2m H',
    standard: 'NFPA 68 Dust Compliant',
    description: 'Continuous vibrating fluid bed dryer with perforated distributor deck, 195 kWth air heater, and 20-min adiabatic moisture tempering zone.'
  },
  {
    id: 'ev101',
    name: 'EV-101 MVR Falling Film ZLD Evaporator',
    file: '/models/EV-101_ZLD_Evaporator.glb',
    tag: 'EV-101',
    scale: '250 kg/h Vapor',
    dimensions: '1.2m Dia x 4.5m H',
    standard: 'ISA-5.1 Instrumented',
    description: 'Zero liquid discharge falling film tubular concentrator with MVR vapor turbo-fan and 85% closed-loop condensate recovery.'
  },
  {
    id: 'sc101',
    name: 'SC-101 High-Frequency Dewatering Screen',
    file: '/models/SC-101_Dewatering_Screen.glb',
    tag: 'SC-101',
    scale: '1,500 kg/h Slurry',
    dimensions: '2.4m L x 0.9m W x 1.1m H',
    standard: 'SS304 Sanitary Deck',
    description: 'Linear motion vibrating dewatering screen equipped with 12s high-pressure counter-current deluge rinse spray manifold.'
  },
  {
    id: 'str100',
    name: 'STR-100 Structural Steel Mezzanine Platform',
    file: '/models/STR-100_Mezzanine_Platform.glb',
    tag: 'STR-100',
    scale: '+4.2m TOC Elevation',
    dimensions: '10.7m L x 7.5m W x 4.2m H',
    standard: 'IS 800 Structural Steel',
    description: 'Heavy structural ISMB 300 perimeter framework with dual circular tank penetrations, access stairways, and OSHA-compliant safety railings.'
  }
];

export default function SolidWorksViewer() {
  const mountRef = useRef(null);
  const [selectedModelIdx, setSelectedModelIdx] = useState(0);
  const [loading, setLoading] = useState(true);
  const [loadProgress, setLoadProgress] = useState(0);
  const [autoRotate, setAutoRotate] = useState(false);
  const [wireframe, setWireframe] = useState(false);
  const [showGrid, setShowGrid] = useState(true);

  // Three.js instance references
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const rendererRef = useRef(null);
  const controlsRef = useRef(null);
  const modelGroupRef = useRef(null);
  const gridHelperRef = useRef(null);
  const animFrameIdRef = useRef(null);

  const currentModel = CAD_MODELS[selectedModelIdx];

  // Initialize Three.js scene once
  useEffect(() => {
    const container = mountRef.current;
    if (!container) return;

    const width = container.clientWidth;
    const height = container.clientHeight || 480;

    // 1. Scene
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0b0d);
    sceneRef.current = scene;

    // 2. Camera
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(12, 10, 16);
    cameraRef.current = camera;

    // 3. Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFShadowMap;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.2;
    rendererRef.current = renderer;

    // Clear previous children and attach canvas
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // 4. OrbitControls
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxDistance = 50;
    controls.minDistance = 2;
    controls.maxPolarAngle = Math.PI / 2 + 0.1; // Allow slightly below horizon
    controlsRef.current = controls;

    // 5. Lighting Setup (Photorealistic Engineering Studio Lighting)
    const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
    scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0xfff5e6, 2.5); // Key light (warm industrial amber)
    dirLight1.position.set(15, 25, 20);
    dirLight1.castShadow = true;
    dirLight1.shadow.mapSize.width = 1024;
    dirLight1.shadow.mapSize.height = 1024;
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0xb0c4de, 1.5); // Fill light (cool metallic blue)
    dirLight2.position.set(-15, 15, -15);
    scene.add(dirLight2);

    const rimLight = new THREE.DirectionalLight(0xf59e0b, 1.0); // Rim light for SS316L edges
    rimLight.position.set(0, -10, 15);
    scene.add(rimLight);

    // 6. ASME Datum Grid
    const gridHelper = new THREE.GridHelper(30, 30, 0xf59e0b, 0x222630);
    gridHelper.position.y = -0.01;
    scene.add(gridHelper);
    gridHelperRef.current = gridHelper;

    // 7. Group for Model
    const modelGroup = new THREE.Group();
    scene.add(modelGroup);
    modelGroupRef.current = modelGroup;

    // 8. Animation Loop
    const animate = () => {
      animFrameIdRef.current = requestAnimationFrame(animate);
      if (controlsRef.current) controlsRef.current.update();
      if (rendererRef.current && sceneRef.current && cameraRef.current) {
        rendererRef.current.render(sceneRef.current, cameraRef.current);
      }
    };
    animate();

    // 9. Resize Listener
    const handleResize = () => {
      if (!container || !rendererRef.current || !cameraRef.current) return;
      const newWidth = container.clientWidth;
      const newHeight = container.clientHeight;
      cameraRef.current.aspect = newWidth / newHeight;
      cameraRef.current.updateProjectionMatrix();
      rendererRef.current.setSize(newWidth, newHeight);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      if (animFrameIdRef.current) cancelAnimationFrame(animFrameIdRef.current);
      if (rendererRef.current && rendererRef.current.domElement) {
        rendererRef.current.dispose();
      }
    };
  }, []);

  // Load Model whenever selectedModelIdx changes
  useEffect(() => {
    if (!modelGroupRef.current || !sceneRef.current) return;

    setLoading(true);
    setLoadProgress(0);

    // Clear existing model children
    while (modelGroupRef.current.children.length > 0) {
      const obj = modelGroupRef.current.children[0];
      modelGroupRef.current.remove(obj);
    }

    const loader = new GLTFLoader();
    loader.load(
      currentModel.file,
      (gltf) => {
        const model = gltf.scene;
        
        // Compute bounding box and center model
        const box = new THREE.Box3().setFromObject(model);
        const size = box.getSize(new THREE.Vector3());
        const center = box.getCenter(new THREE.Vector3());

        // Center on X and Z, place base on ground (Y = 0)
        model.position.x = -center.x;
        model.position.y = -box.min.y;
        model.position.z = -center.z;

        // Apply authentic SS316L / SS304 PBR metallic materials if textures are plain
        model.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
            if (child.material) {
              child.material.wireframe = wireframe;
              child.material.metalness = Math.max(child.material.metalness || 0.85, 0.8);
              child.material.roughness = Math.min(child.material.roughness || 0.25, 0.35);
              child.material.needsUpdate = true;
            }
          }
        });

        modelGroupRef.current.add(model);

        // Adjust camera distance based on bounding box radius
        const maxDim = Math.max(size.x, size.y, size.z);
        const fov = cameraRef.current.fov * (Math.PI / 180);
        let cameraDist = maxDim / (2 * Math.tan(fov / 2));
        cameraDist *= 1.5; // Padding

        cameraRef.current.position.set(cameraDist * 0.8, cameraDist * 0.6, cameraDist);
        controlsRef.current.target.set(0, size.y * 0.4, 0);
        controlsRef.current.update();

        setLoading(false);
      },
      (xhr) => {
        if (xhr.total > 0) {
          const pct = Math.round((xhr.loaded / xhr.total) * 100);
          setLoadProgress(pct);
        }
      },
      (error) => {
        console.warn('Failed to load GLB model, generating procedural geometry:', error);
        createProceduralCadFallback();
        setLoading(false);
      }
    );
  }, [selectedModelIdx, currentModel.file]);

  // Handle Wireframe Toggle
  useEffect(() => {
    if (!modelGroupRef.current) return;
    modelGroupRef.current.traverse((child) => {
      if (child.isMesh && child.material) {
        child.material.wireframe = wireframe;
        child.material.needsUpdate = true;
      }
    });
  }, [wireframe]);

  // Handle Auto-Rotate Toggle
  useEffect(() => {
    if (controlsRef.current) {
      controlsRef.current.autoRotate = autoRotate;
      controlsRef.current.autoRotateSpeed = 2.0;
    }
  }, [autoRotate]);

  // Handle Grid Toggle
  useEffect(() => {
    if (gridHelperRef.current) {
      gridHelperRef.current.visible = showGrid;
    }
  }, [showGrid]);

  // Camera Presets
  const setCameraPreset = (preset) => {
    if (!cameraRef.current || !controlsRef.current || !modelGroupRef.current) return;
    const box = new THREE.Box3().setFromObject(modelGroupRef.current);
    const size = box.getSize(new THREE.Vector3());
    const maxDim = Math.max(size.x, size.y, size.z) || 10;
    const targetY = size.y * 0.4 || 2;

    controlsRef.current.target.set(0, targetY, 0);

    if (preset === 'iso') {
      cameraRef.current.position.set(maxDim * 1.2, maxDim * 0.9, maxDim * 1.2);
    } else if (preset === 'front') {
      cameraRef.current.position.set(0, targetY, maxDim * 1.8);
    } else if (preset === 'side') {
      cameraRef.current.position.set(maxDim * 1.8, targetY, 0);
    } else if (preset === 'top') {
      cameraRef.current.position.set(0, maxDim * 2.2, 0.01);
    } else if (preset === 'reset') {
      cameraRef.current.position.set(maxDim * 1.1, maxDim * 0.8, maxDim * 1.3);
    }
    controlsRef.current.update();
  };

  // Fallback Procedural CAD geometry if GLB fails
  const createProceduralCadFallback = () => {
    if (!modelGroupRef.current) return;
    const group = new THREE.Group();
    const mat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.85, roughness: 0.25 });
    
    // Cylindrical Soak Tank
    const cyl = new THREE.Mesh(new THREE.CylinderGeometry(1.5, 1.5, 4.0, 32), mat);
    cyl.position.y = 2.0;
    group.add(cyl);

    // Mezzanine Deck
    const deck = new THREE.Mesh(new THREE.BoxGeometry(6.0, 0.2, 4.0), mat);
    deck.position.y = 0.1;
    group.add(deck);

    modelGroupRef.current.add(group);
  };

  return (
    <section id="solidworks-cad" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Workstation Header */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [INTERACTIVE SOLIDWORKS 3D CAD ENGINE]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Parametric 3D Solid Model & Assembly Workstation
            </h2>
          </div>
          <div className="flex items-center space-x-2 font-mono text-xs">
            <span className="px-2 py-0.5 bg-[#1E222A] text-[#F59E0B] border border-[#2E3440] rounded-sm font-semibold">
              SOLIDWORKS 2025 SP01.2
            </span>
            <span className="px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm font-semibold">
              ASME SEC VIII DIV 1
            </span>
          </div>
        </div>

        {/* CAD Model Selector Bar */}
        <div className="p-4 bg-[#0A0B0D] border-b border-[#222630] overflow-x-auto">
          <div className="flex items-center space-x-2 min-w-max">
            <span className="font-mono text-xs text-[#64748B] uppercase mr-2">
              ACTIVE CAD MODEL:
            </span>
            {CAD_MODELS.map((m, idx) => (
              <button
                key={m.id}
                onClick={() => setSelectedModelIdx(idx)}
                className={`px-3 py-1.5 font-mono text-xs rounded-sm border transition-colors cursor-pointer ${
                  selectedModelIdx === idx
                    ? 'bg-[#171A21] border-[#F59E0B] text-[#F59E0B] font-semibold shadow-sm'
                    : 'bg-[#111317] border-[#222630] text-[#9CA3AF] hover:text-[#F3F4F6]'
                }`}
              >
                {m.tag} ({m.name.split(' ')[0]})
              </button>
            ))}
          </div>
        </div>

        {/* 3D Viewport + CAD Tool Controls Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12">
          
          {/* Main 3D Canvas (8 Cols) */}
          <div className="lg:col-span-8 relative bg-[#0A0B0D] border-b lg:border-b-0 lg:border-r border-[#222630] min-h-[480px] lg:min-h-[580px] flex flex-col justify-between">
            
            {/* Canvas Mount Container */}
            <div ref={mountRef} className="w-full h-full min-h-[480px] lg:min-h-[580px] cursor-grab active:cursor-grabbing relative" />

            {/* Loading Overlay */}
            {loading && (
              <div className="absolute inset-0 bg-[#0A0B0D]/85 backdrop-blur-xs flex flex-col items-center justify-center font-mono text-xs text-[#F3F4F6] z-20">
                <div className="w-48 h-1.5 bg-[#1E222A] border border-[#2E3440] rounded-xs overflow-hidden mb-3">
                  <div 
                    className="h-full bg-[#F59E0B] transition-all duration-200" 
                    style={{ width: `${loadProgress}%` }}
                  />
                </div>
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-[#F59E0B] animate-ping"></span>
                  <span>Tesselating Parametric Solid ({loadProgress > 0 ? `${loadProgress}%` : 'Loading...'})</span>
                </div>
                <span className="text-[10px] text-[#64748B] mt-1">{currentModel.file}</span>
              </div>
            )}

            {/* Floating Camera & Shading Toolbar (Top Left) */}
            <div className="absolute top-4 left-4 z-10 flex flex-wrap gap-1 font-mono text-[11px] bg-[#111317]/90 p-1.5 border border-[#222630] rounded-sm backdrop-blur-xs shadow-lg">
              <span className="text-[#64748B] px-1 py-0.5 text-[10px] uppercase font-semibold">VIEW:</span>
              <button 
                onClick={() => setCameraPreset('iso')}
                className="px-2 py-0.5 bg-[#1E222A] hover:bg-[#2E3440] text-[#F3F4F6] rounded-xs cursor-pointer border border-[#2E3440]"
                title="Isometric Projection"
              >
                [ISO]
              </button>
              <button 
                onClick={() => setCameraPreset('front')}
                className="px-2 py-0.5 bg-[#1E222A] hover:bg-[#2E3440] text-[#F3F4F6] rounded-xs cursor-pointer border border-[#2E3440]"
                title="Front Elevation"
              >
                [FRONT]
              </button>
              <button 
                onClick={() => setCameraPreset('side')}
                className="px-2 py-0.5 bg-[#1E222A] hover:bg-[#2E3440] text-[#F3F4F6] rounded-xs cursor-pointer border border-[#2E3440]"
                title="Right Side Elevation"
              >
                [SIDE]
              </button>
              <button 
                onClick={() => setCameraPreset('top')}
                className="px-2 py-0.5 bg-[#1E222A] hover:bg-[#2E3440] text-[#F3F4F6] rounded-xs cursor-pointer border border-[#2E3440]"
                title="Top Plan View"
              >
                [TOP]
              </button>
              <button 
                onClick={() => setCameraPreset('reset')}
                className="px-2 py-0.5 bg-[#171A21] hover:bg-[#222630] text-[#F59E0B] rounded-xs cursor-pointer border border-[#F59E0B]/40 font-semibold"
                title="Reset Camera Target"
              >
                [RESET]
              </button>
            </div>

            {/* Floating Display Mode Toggles (Top Right) */}
            <div className="absolute top-4 right-4 z-10 flex items-center space-x-1 font-mono text-[11px] bg-[#111317]/90 p-1.5 border border-[#222630] rounded-sm backdrop-blur-xs shadow-lg">
              <button
                onClick={() => setAutoRotate(!autoRotate)}
                className={`px-2 py-0.5 rounded-xs border cursor-pointer transition-colors ${
                  autoRotate 
                    ? 'bg-[#F59E0B]/20 text-[#F59E0B] border-[#F59E0B]' 
                    : 'bg-[#1E222A] text-[#9CA3AF] border-[#2E3440] hover:text-[#F3F4F6]'
                }`}
                title="Auto-Turntable Rotation"
              >
                ↻ Turntable
              </button>
              <button
                onClick={() => setWireframe(!wireframe)}
                className={`px-2 py-0.5 rounded-xs border cursor-pointer transition-colors ${
                  wireframe 
                    ? 'bg-[#10B981]/20 text-[#10B981] border-[#10B981]' 
                    : 'bg-[#1E222A] text-[#9CA3AF] border-[#2E3440] hover:text-[#F3F4F6]'
                }`}
                title="Wireframe Mesh Tessellation Mode"
              >
                🕸 Wireframe
              </button>
              <button
                onClick={() => setShowGrid(!showGrid)}
                className={`px-2 py-0.5 rounded-xs border cursor-pointer transition-colors ${
                  showGrid 
                    ? 'bg-[#171A21] text-[#F3F4F6] border-[#222630]' 
                    : 'bg-[#1E222A] text-[#64748B] border-[#2E3440]'
                }`}
                title="Toggle ASME Coordinate Grid"
              >
                # Datum Grid
              </button>
            </div>

            {/* Bottom HUD: Live Interaction Hints */}
            <div className="p-3 bg-[#111317]/90 border-t border-[#222630] flex flex-wrap justify-between items-center font-mono text-[11px] text-[#64748B]">
              <div className="flex items-center space-x-3">
                <span className="text-[#F59E0B] font-semibold">● ORBIT CONTROLS ACTIVE</span>
                <span>Left Click: 360° Rotate</span>
                <span>Right Click: Pan</span>
                <span>Scroll: Zoom</span>
              </div>
              <span className="text-[#10B981]">WebGL 2.0 PBR Shader Active</span>
            </div>

          </div>

          {/* Right Inspection & Telemetry Panel (4 Cols) */}
          <div className="lg:col-span-4 p-6 sm:p-8 bg-[#111317] flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-center mb-4 pb-2 border-b border-[#222630]">
                <div>
                  <span className="font-mono text-base font-bold text-[#F59E0B] mr-2">
                    {currentModel.tag}
                  </span>
                  <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-xs font-semibold">
                    SOLID BODY
                  </span>
                </div>
                <span className="font-mono text-[11px] text-[#64748B]">
                  {currentModel.standard}
                </span>
              </div>

              <h3 className="text-base font-semibold text-[#F3F4F6] mb-2">
                {currentModel.name}
              </h3>

              <p className="text-xs text-[#9CA3AF] leading-relaxed mb-6 font-normal">
                {currentModel.description}
              </p>

              {/* Dimensional & Physical HUD Box */}
              <div className="space-y-2 font-mono text-xs mb-6">
                <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm flex justify-between items-center">
                  <span className="text-[#64748B]">BOUNDING ENVELOPE:</span>
                  <span className="text-[#F3F4F6] font-semibold">{currentModel.dimensions}</span>
                </div>
                <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm flex justify-between items-center">
                  <span className="text-[#64748B]">DESIGN CAPACITY:</span>
                  <span className="text-[#F59E0B] font-semibold">{currentModel.scale}</span>
                </div>
                <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm flex justify-between items-center">
                  <span className="text-[#64748B]">WETTED METALLURGY:</span>
                  <span className="text-[#10B981] font-semibold">SS316L / SS304 Tri-Clamp</span>
                </div>
                <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm flex justify-between items-center">
                  <span className="text-[#64748B]">NATIVE CAD ARTIFACT:</span>
                  <span className="text-[#F3F4F6] text-[11px]">{currentModel.file.split('/').pop()}</span>
                </div>
              </div>
            </div>

            {/* Engineering Attributions */}
            <div className="pt-4 border-t border-[#222630] font-mono text-[11px] text-[#64748B] space-y-1">
              <div>SolidWorks Model Derived from STEP AP214</div>
              <div>Lead Engineer: <span className="text-[#F3F4F6]">Sourish Senapati</span></div>
              <div className="text-[#10B981]">FinnoaQ Agro-Industrial Technologies Ltd.</div>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}
