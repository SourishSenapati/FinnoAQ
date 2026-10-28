import React, { useState, useEffect } from 'react';
import { Play, FileText, CheckCircle2, AlertTriangle, Cpu, Gauge, Zap, ArrowRight, ShieldCheck } from 'lucide-react';

export default function HeroCommandView() {
  // Workload preset state
  const [activeWorkload, setActiveWorkload] = useState('constrained'); // 'baseline', 'constrained', 'adversarial'
  
  // 3 Interactive parameter sliders
  const [loadTPD, setLoadTPD] = useState(15);
  const [tempSetpoint, setTempSetpoint] = useState(48);
  const [acousticGain, setAcousticGain] = useState(1.8);

  // Dynamic simulation telemetry
  const [waveOffset, setWaveOffset] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setWaveOffset(prev => (prev + 0.15) % (Math.PI * 2));
    }, 50);
    return () => clearInterval(interval);
  }, []);

  // Calculated physical parameters
  const caExtractionPct = Math.min(46.0, 28.0 + (tempSetpoint - 40) * 0.45 + (acousticGain - 0.5) * 5.2).toFixed(1);
  const coreFirmnessN = Math.max(13.5, 48.5 - (caExtractionPct * 0.79)).toFixed(2);
  const systemEfficiencyPct = (97.37 - (loadTPD > 20 ? (loadTPD - 20) * 0.15 : 0)).toFixed(2);
  const solverLatencyMs = (11.4 + (loadTPD / 15) * 2.1).toFixed(1);
  const isPassing = parseFloat(coreFirmnessN) <= 18.0;

  // Workload payloads
  const workloads = {
    baseline: {
      name: "Tanzanian HTC Baseline",
      spec: "Aged 18mo Bold Lot // Untreated",
      inputMoisture: "11.5% wb",
      chelationAgent: "None (Raw Water)",
      targetFwb: "48.5 N (8 Whistles // FAIL)",
      jsonDiff: {
        batch_id: "TZA-2026-B01",
        middle_lamella_ca: "12.4 mol/m³",
        chelation_kinetics: "k_chel = 0.0 s⁻¹",
        cavitation_streaming: "OFF",
        two_whistle_status: "REJECTED (P99 = 48.5N)"
      }
    },
    constrained: {
      name: "Constrained S1-09 Chelation",
      spec: "Multi-Salt Bio-Buffer // pH 5.20",
      inputMoisture: "28.0% wb post-steep",
      chelationAgent: "0.085M K3Cit + 0.035M SHMP",
      targetFwb: "15.2 N (2 Whistles // PASS)",
      jsonDiff: {
        batch_id: "FNQ-S109-OPT",
        middle_lamella_ca: "7.2 mol/m³ (-41.8%)",
        chelation_kinetics: "k_chel = 4.82e-3 s⁻¹",
        cavitation_streaming: "ACTIVE (25 kHz, 1.8 W/cm²)",
        two_whistle_status: "CONVERGED (P95 ≤ 18.0N)"
      }
    },
    adversarial: {
      name: "Adversarial LOX Interlock",
      spec: "Lipoxygenase Acid Inactivation",
      inputMoisture: "Surface Salt <48.2 mg/kg",
      chelationAgent: "Buffer pH Locked at 5.20 ± 0.05",
      targetFwb: "Hexanal 0.025 ppm (OAV = 0.84)",
      jsonDiff: {
        batch_id: "LOX-ADV-PASS",
        enzyme_denaturation: "86.4% inactive",
        off_flavor_beany: "0.025 ppm (<0.03 ppm thr)",
        deluge_wash_cycle: "12s counter-current",
        two_whistle_status: "FSSAI & SENSORY PASSED"
      }
    }
  };

  const currentWl = workloads[activeWorkload];

  return (
    <section id="architecture" className="relative border-b border-[#1E2230] bg-[#090A0F] pt-8 pb-14">
      {/* Structural Crosshair Markers */}
      <div className="absolute top-0 left-0 w-3 h-3 text-[#38BDF8] font-mono text-xs leading-none select-none">+</div>
      <div className="absolute top-0 right-0 w-3 h-3 text-[#38BDF8] font-mono text-xs leading-none select-none text-right">+</div>

      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Split-Screen 12-Column Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Left 5 Columns: Executive Technical Pitch */}
          <div className="lg:col-span-5 flex flex-col gap-5 pt-2">
            
            {/* Status Strip */}
            <div className="inline-flex items-center gap-2 border border-[#1E2230] bg-[#11131A] px-3 py-1 rounded-sm w-fit">
              <span className="h-1.5 w-1.5 rounded-full bg-[#10B981]"></span>
              <span className="font-mono text-[10px] tracking-widest text-[#94A3B8] uppercase">
                v2.4 DETERMINISTIC ENGINE // SIL-3 COMPLIANT
              </span>
            </div>

            {/* Main Headline */}
            <h1 className="text-3xl sm:text-4xl lg:text-[42px] font-bold text-[#F3F4F6] tracking-tight leading-[1.12]">
              Autonomous Pulse Tenderization & <span className="text-[#F59E0B]">₹20.00 / kg Mandi Arbitrage</span> Digital Twin
            </h1>

            {/* Concise Engineering Sub-Copy */}
            <p className="text-sm text-[#94A3B8] leading-relaxed">
              A first-principles industrial bioprocess platform eliminating the Hard-to-Cook (HTC) cellular defect in imported African split pigeon peas (<em>Cajanus cajan</em>). Enforces transient Fickian reaction-diffusion PDE constraints to extract 41.8% of core calcium in 24 min at 48°C, guaranteeing 2-whistle Hawkins pressure cooker tenderization (<span className="font-mono text-[#F3F4F6] tabular-nums">Fwb ≤ 18.0 N</span>) with zero aftertaste and audited 15 TPD turnkey skid economics.
            </p>

            {/* Primary Action Buttons */}
            <div className="flex flex-wrap items-center gap-3 pt-2">
              <a
                href="#playground"
                className="inline-flex items-center gap-2 bg-[#F3F4F6] hover:bg-white text-[#090A0F] font-mono text-xs font-bold px-5 py-2.5 rounded-sm transition-all shadow-sm"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                Launch Live Sandbox
              </a>

              <a
                href="/pdf/finnoaq_dalopt_q1_master_treatise.pdf"
                download="finnoaq_dalopt_q1_master_treatise.pdf"
                className="inline-flex items-center gap-2 border border-[#1E2230] hover:border-[#38BDF8] bg-[#11131A] text-[#F3F4F6] font-mono text-xs font-semibold px-4 py-2.5 rounded-sm transition-all"
              >
                <FileText className="w-3.5 h-3.5 text-[#38BDF8]" />
                Architecture Monograph [27p]
              </a>
            </div>

            {/* Live Telemetry KPI Matrix */}
            <div className="grid grid-cols-3 gap-2 pt-4 border-t border-[#1E2230]">
              <div className="bg-[#11131A] border border-[#1E2230] p-2.5 rounded-sm">
                <span className="block font-mono text-[9px] text-[#64748B] uppercase tracking-wider">MANDI ARBITRAGE</span>
                <span className="font-mono text-base font-bold text-[#F59E0B] tabular-nums">₹20.00 / kg</span>
                <span className="block text-[10px] text-[#64748B]">Port Wholesale Spread</span>
              </div>
              <div className="bg-[#11131A] border border-[#1E2230] p-2.5 rounded-sm">
                <span className="block font-mono text-[9px] text-[#64748B] uppercase tracking-wider">COOKING FIRMNESS</span>
                <span className={`font-mono text-base font-bold tabular-nums ${isPassing ? 'text-[#10B981]' : 'text-[#EF4444]'}`}>
                  {coreFirmnessN} N
                </span>
                <span className="block text-[10px] text-[#64748B]">≤18.0N (2 Whistles)</span>
              </div>
              <div className="bg-[#11131A] border border-[#1E2230] p-2.5 rounded-sm">
                <span className="block font-mono text-[9px] text-[#64748B] uppercase tracking-wider">SOLIDS YIELD</span>
                <span className="font-mono text-base font-bold text-[#38BDF8] tabular-nums">{systemEfficiencyPct}%</span>
                <span className="block text-[10px] text-[#64748B]">Aspen Converged</span>
              </div>
            </div>

          </div>

          {/* Right 7 Columns: Live Process Node Canvas & Interactive DAG */}
          <div className="lg:col-span-7 border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col gap-4 shadow-xl">
            
            {/* Header Toolbar: Preset Workload Tabs */}
            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[#1E2230] pb-3">
              <div className="flex items-center gap-2">
                <Cpu className="w-4 h-4 text-[#38BDF8]" />
                <span className="font-mono text-xs font-bold text-[#F3F4F6] tracking-wider uppercase">
                  [00 // ARCHITECTURE DAG ENGINE]
                </span>
              </div>
              <div className="flex items-center gap-1.5">
                {Object.keys(workloads).map(key => (
                  <button
                    key={key}
                    onClick={() => setActiveWorkload(key)}
                    className={`font-mono text-[11px] px-2.5 py-1 rounded-sm border transition-all ${
                      activeWorkload === key
                        ? 'border-[#38BDF8] bg-[#38BDF8]/10 text-[#38BDF8] font-bold'
                        : 'border-[#1E2230] bg-[#090A0F] text-[#94A3B8] hover:text-[#F3F4F6]'
                    }`}
                  >
                    {key === 'baseline' ? 'Raw Lot' : key === 'constrained' ? 'S1-09 Chelation' : 'LOX Interlock'}
                  </button>
                ))}
              </div>
            </div>

            {/* Interactive Animated SVG DAG Canvas */}
            <div className="relative bg-[#090A0F] border border-[#1E2230] rounded-sm p-4 overflow-hidden">
              <div className="flex items-center justify-between text-[11px] font-mono text-[#64748B] mb-2">
                <span>ACTIVE PIPELINE WORKLOAD: <strong className="text-[#F3F4F6]">{currentWl.name}</strong></span>
                <span className="text-[#10B981] flex items-center gap-1">
                  <span className="h-1.5 w-1.5 rounded-full bg-[#10B981] animate-ping"></span>
                  LATENCY: {solverLatencyMs}ms
                </span>
              </div>

              {/* 5-Node Directed Acyclic Graph */}
              <div className="grid grid-cols-5 gap-2 my-3 text-center font-mono">
                
                {/* Node 1 */}
                <div className="border border-[#1E2230] bg-[#11131A] p-2 rounded-sm flex flex-col items-center">
                  <span className="text-[9px] text-[#64748B]">NODE 01</span>
                  <span className="text-xs font-bold text-[#F3F4F6]">NIR Ingestion</span>
                  <span className="text-[10px] text-[#38BDF8] mt-1 tabular-nums">{loadTPD} TPD</span>
                </div>

                {/* Node 2 */}
                <div className={`border p-2 rounded-sm flex flex-col items-center ${activeWorkload !== 'baseline' ? 'border-[#38BDF8] bg-[#38BDF8]/5' : 'border-[#1E2230] bg-[#11131A]'}`}>
                  <span className="text-[9px] text-[#64748B]">NODE 02</span>
                  <span className="text-xs font-bold text-[#F3F4F6]">PDE Solver</span>
                  <span className="text-[10px] text-[#F59E0B] mt-1 tabular-nums">{tempSetpoint}°C</span>
                </div>

                {/* Node 3 */}
                <div className={`border p-2 rounded-sm flex flex-col items-center ${activeWorkload !== 'baseline' ? 'border-[#10B981] bg-[#10B981]/5' : 'border-[#1E2230] bg-[#11131A]'}`}>
                  <span className="text-[9px] text-[#64748B]">NODE 03</span>
                  <span className="text-xs font-bold text-[#F3F4F6]">Ultrasound</span>
                  <span className="text-[10px] text-[#10B981] mt-1 tabular-nums">{acousticGain} W/cm²</span>
                </div>

                {/* Node 4 */}
                <div className="border border-[#1E2230] bg-[#11131A] p-2 rounded-sm flex flex-col items-center">
                  <span className="text-[9px] text-[#64748B]">NODE 04</span>
                  <span className="text-xs font-bold text-[#F3F4F6]">Tempering</span>
                  <span className="text-[10px] text-[#94A3B8] mt-1">20m Deck</span>
                </div>

                {/* Node 5 */}
                <div className="border border-[#1E2230] bg-[#11131A] p-2 rounded-sm flex flex-col items-center">
                  <span className="text-[9px] text-[#64748B]">NODE 05</span>
                  <span className="text-xs font-bold text-[#F3F4F6]">Actuation</span>
                  <span className={`text-[10px] font-bold mt-1 ${isPassing ? 'text-[#10B981]' : 'text-[#EF4444]'}`}>
                    {isPassing ? '2-WHISTLE' : '8-WHISTLE'}
                  </span>
                </div>

              </div>

              {/* Dynamic Waveform & Payload Inspector */}
              <div className="grid grid-cols-1 md:grid-cols-12 gap-3 pt-2">
                
                {/* Live Real-Time Sine Waveform (Canvas simulation) */}
                <div className="md:col-span-6 bg-[#11131A] border border-[#1E2230] p-2.5 rounded-sm">
                  <div className="flex justify-between text-[10px] font-mono text-[#64748B] mb-1">
                    <span>ACOUSTIC CAVITATION PRESSURE WAVE</span>
                    <span className="text-[#38BDF8] tabular-nums">25.0 kHz</span>
                  </div>
                  <svg viewBox="0 0 240 60" className="w-full h-14 overflow-visible">
                    <line x1="0" y1="30" x2="240" y2="30" stroke="#1E2230" strokeDasharray="2,2" />
                    <path
                      d={`M ${Array.from({ length: 48 }, (_, i) => {
                        const x = i * 5;
                        const y = 30 + Math.sin(x * 0.08 + waveOffset) * (acousticGain * 8) * (activeWorkload === 'baseline' ? 0.1 : 1.0);
                        return `${x},${y}`;
                      }).join(' L ')}`}
                      fill="none"
                      stroke={activeWorkload === 'baseline' ? '#64748B' : '#38BDF8'}
                      strokeWidth="2"
                    />
                  </svg>
                  <div className="flex justify-between text-[9px] font-mono text-[#64748B] mt-1">
                    <span>P_ac: ±1.8 MPa</span>
                    <span className="text-[#10B981] tabular-nums">BL Thickness: 14 µm</span>
                  </div>
                </div>

                {/* Side Inspector: Live JSON Payload Diff */}
                <div className="md:col-span-6 bg-[#090A0F] border border-[#1E2230] p-2 rounded-sm font-mono text-[10.5px]">
                  <div className="text-[9px] text-[#64748B] pb-1 border-b border-[#1E2230] flex justify-between">
                    <span>PAYLOAD TELEMETRY DIFF</span>
                    <span className="text-[#10B981]">PROVENANCE VERIFIED</span>
                  </div>
                  <pre className="text-[#94A3B8] leading-tight pt-1 overflow-x-auto">
                    {JSON.stringify(currentWl.jsonDiff, null, 2)}
                  </pre>
                </div>

              </div>
            </div>

            {/* 3 Interactive Parameter Sliders */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
              
              {/* Slider 1: Flow / Load */}
              <div className="bg-[#090A0F] border border-[#1E2230] p-2.5 rounded-sm">
                <div className="flex justify-between items-center text-xs font-mono mb-1">
                  <span className="text-[#94A3B8]">Infeed Load</span>
                  <span className="text-[#F59E0B] font-bold tabular-nums">{loadTPD} TPD</span>
                </div>
                <input
                  type="range"
                  min="5"
                  max="30"
                  step="1"
                  value={loadTPD}
                  onChange={e => setLoadTPD(parseFloat(e.target.value))}
                  className="w-full accent-[#F59E0B] cursor-pointer h-1.5 bg-[#1E2230] rounded-sm"
                />
                <div className="flex justify-between text-[9px] font-mono text-[#64748B] mt-1">
                  <span>5 TPD</span>
                  <span>15 TPD Ref</span>
                  <span>30 TPD</span>
                </div>
              </div>

              {/* Slider 2: Thermal Setpoint */}
              <div className="bg-[#090A0F] border border-[#1E2230] p-2.5 rounded-sm">
                <div className="flex justify-between items-center text-xs font-mono mb-1">
                  <span className="text-[#94A3B8]">Thermal Steep</span>
                  <span className="text-[#38BDF8] font-bold tabular-nums">{tempSetpoint}°C</span>
                </div>
                <input
                  type="range"
                  min="40"
                  max="65"
                  step="1"
                  value={tempSetpoint}
                  onChange={e => setTempSetpoint(parseFloat(e.target.value))}
                  className="w-full accent-[#38BDF8] cursor-pointer h-1.5 bg-[#1E2230] rounded-sm"
                />
                <div className="flex justify-between text-[9px] font-mono text-[#64748B] mt-1">
                  <span>40°C</span>
                  <span>48°C Ref</span>
                  <span>65°C</span>
                </div>
              </div>

              {/* Slider 3: Acoustic Gain */}
              <div className="bg-[#090A0F] border border-[#1E2230] p-2.5 rounded-sm">
                <div className="flex justify-between items-center text-xs font-mono mb-1">
                  <span className="text-[#94A3B8]">Ultrasound Intensity</span>
                  <span className="text-[#10B981] font-bold tabular-nums">{acousticGain} W/cm²</span>
                </div>
                <input
                  type="range"
                  min="0.5"
                  max="2.5"
                  step="0.1"
                  value={acousticGain}
                  onChange={e => setAcousticGain(parseFloat(e.target.value))}
                  className="w-full accent-[#10B981] cursor-pointer h-1.5 bg-[#1E2230] rounded-sm"
                />
                <div className="flex justify-between text-[9px] font-mono text-[#64748B] mt-1">
                  <span>0.5 W</span>
                  <span>1.8 W Ref</span>
                  <span>2.5 W</span>
                </div>
              </div>

            </div>

          </div>

        </div>

      </div>
    </section>
  );
}
