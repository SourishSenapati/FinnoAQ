import React, { useState } from 'react';
import { ShieldCheck, AlertTriangle, Zap, Server, Activity, Droplets, CheckCircle, Flame } from 'lucide-react';

export default function BentoGuarantees() {
  // Card 1: Fault-Tolerance Interlock State
  const [faultInjected, setFaultInjected] = useState(false);
  const [faultTimestamp, setFaultTimestamp] = useState(null);

  const toggleFault = () => {
    if (!faultInjected) {
      setFaultInjected(true);
      setFaultTimestamp(new Date().toISOString().substring(11, 23));
    } else {
      setFaultInjected(false);
      setFaultTimestamp(null);
    }
  };

  // Card 2: Interactive Throughput benchmark hover
  const [hoveredBaseline, setHoveredBaseline] = useState(null);
  const baselines = [
    { name: "Traditional Atmospheric Steep", rate: 120, unit: "kg/h", color: "#64748B", time: "60-70 min" },
    { name: "Industrial Pressure Autoclave", rate: 350, unit: "kg/h", color: "#F59E0B", time: "35 min" },
    { name: "Microwave Thermal Cavitation", rate: 420, unit: "kg/h", color: "#38BDF8", time: "25 min" },
    { name: "FinnoaQ OMEGA Continuous Skid", rate: 625, unit: "kg/h", color: "#10B981", time: "14.8 min (2 Whistles)" }
  ];

  return (
    <section id="guarantees" className="border-b border-[#1E2230] bg-[#090A0F] py-14">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col gap-2 mb-10 border-b border-[#1E2230] pb-6">
          <div className="flex items-center gap-2">
            <span className="font-mono text-xs font-bold text-[#10B981] tracking-widest uppercase">[03 // SYSTEM GUARANTEES]</span>
            <span className="h-1 w-1 rounded-full bg-[#10B981]"></span>
            <span className="font-mono text-xs text-[#64748B]">BENTO GRID MULTI-MODAL PROOF</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-[#F3F4F6] tracking-tight">
            Deterministic System Guarantees & Hardware Telemetry
          </h2>
          <p className="text-sm text-[#94A3B8] max-w-3xl">
            Asymmetric 3x2 Swiss-grid architecture pairing live hardware fault-injection with verified biophysical bounds.
          </p>
        </div>

        {/* 3x2 Asymmetric Bento Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          {/* Card 1: Interactive Fault Tolerance & Interlock (Spans 1 Col) */}
          <div className="border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col justify-between shadow-md">
            <div>
              <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2">
                <span>[CARD 01 // INTERLOCK]</span>
                <span className={`px-2 py-0.5 rounded-sm font-bold ${faultInjected ? 'bg-[#EF4444]/10 text-[#EF4444] border border-[#EF4444]/30' : 'bg-[#10B981]/10 text-[#10B981] border border-[#10B981]/30'}`}>
                  {faultInjected ? 'TRIP ACTUATED (3.8ms)' : 'NOMINAL (SIL-3)'}
                </span>
              </div>
              <h3 className="text-base font-bold text-[#F3F4F6]">SIL-3 Fault-Tolerance & Scram Interlock</h3>
              <p className="text-xs text-[#94A3B8] mt-1 leading-relaxed">
                Test the deterministic safety loop by injecting a simulated ultrasonic transducer impedance spike or pH excursion.
              </p>
            </div>

            {/* Interactive Micro-Demo */}
            <div className="my-4 p-3 bg-[#090A0F] border border-[#1E2230] rounded-sm font-mono text-xs flex flex-col gap-2">
              <div className="flex justify-between items-center text-[11px]">
                <span className="text-[#64748B]">STATUS:</span>
                <span className={faultInjected ? "text-[#EF4444] font-bold" : "text-[#10B981]"}>
                  {faultInjected ? "FLOW DIVERTED TO ZLD TANK" : "CONTINUOUS FORWARD FLOW"}
                </span>
              </div>
              <div className="flex justify-between items-center text-[11px]">
                <span className="text-[#64748B]">TRIP LATENCY:</span>
                <span className="text-[#38BDF8] font-bold tabular-nums">3.8 ms (&lt;5ms threshold)</span>
              </div>
              {faultTimestamp && (
                <div className="text-[10px] text-[#EF4444] border-t border-[#1E2230] pt-1">
                  EVENT: pH_DRIFT_FAULT @ {faultTimestamp}
                </div>
              )}
            </div>

            <button
              onClick={toggleFault}
              className={`w-full py-2 font-mono text-xs font-bold rounded-sm border transition-all ${
                faultInjected
                  ? 'border-[#10B981] bg-[#10B981]/10 text-[#10B981] hover:bg-[#10B981]/20'
                  : 'border-[#EF4444] bg-[#EF4444]/10 text-[#EF4444] hover:bg-[#EF4444]/20'
              }`}
            >
              {faultInjected ? "Reset Safety System" : "⚠️ Inject Simulated Fault"}
            </button>
          </div>

          {/* Card 2: Throughput Benchmark Chart (Spans 1 Col) */}
          <div className="border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col justify-between shadow-md">
            <div>
              <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2">
                <span>[CARD 02 // BENCHMARK]</span>
                <span className="text-[#38BDF8] font-mono text-[10px]">625 kg/h (15 TPD)</span>
              </div>
              <h3 className="text-base font-bold text-[#F3F4F6]">Continuous Throughput vs Baselines</h3>
              <p className="text-xs text-[#94A3B8] mt-1 leading-relaxed">
                Comparison of finished split toor dal continuous rate under verified ASME steady-state conditions.
              </p>
            </div>

            {/* Interactive Bar Chart */}
            <div className="my-4 flex flex-col gap-2.5">
              {baselines.map((b, i) => (
                <div
                  key={i}
                  onMouseEnter={() => setHoveredBaseline(b)}
                  onMouseLeave={() => setHoveredBaseline(null)}
                  className="cursor-pointer"
                >
                  <div className="flex justify-between text-[11px] font-mono mb-1">
                    <span className="text-[#94A3B8] truncate max-w-[190px]">{b.name}</span>
                    <span className="font-bold tabular-nums" style={{ color: b.color }}>{b.rate} {b.unit}</span>
                  </div>
                  <div className="w-full h-2 bg-[#090A0F] rounded-xs border border-[#1E2230] overflow-hidden">
                    <div
                      className="h-full transition-all duration-500 rounded-xs"
                      style={{
                        width: `${(b.rate / 625) * 100}%`,
                        backgroundColor: b.color
                      }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>

            <div className="text-[10px] font-mono text-[#64748B] border-t border-[#1E2230] pt-2">
              {hoveredBaseline ? (
                <span className="text-[#38BDF8]">Selected: {hoveredBaseline.name} (Cook Time: {hoveredBaseline.time})</span>
              ) : (
                <span>Hover over bars for cooking duration and yield profile.</span>
              )}
            </div>
          </div>

          {/* Card 3: Live Compute & Memory Footprint Gauge (Spans 1 Col) */}
          <div className="border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col justify-between shadow-md">
            <div>
              <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2">
                <span>[CARD 03 // COMPUTE]</span>
                <span className="text-[#10B981] font-mono text-[10px] font-bold">RTX 4050 GPU READY</span>
              </div>
              <h3 className="text-base font-bold text-[#F3F4F6]">GPU Memory & Multiphysics Telemetry</h3>
              <p className="text-xs text-[#94A3B8] mt-1 leading-relaxed">
                Deterministic 2D-PDE finite difference grid study (540,000 spatial cells converged under 18.2ms).
              </p>
            </div>

            {/* Gauge Readout Box */}
            <div className="my-4 p-3 bg-[#090A0F] border border-[#1E2230] rounded-sm font-mono flex flex-col gap-2">
              <div className="flex justify-between items-center text-xs">
                <span className="text-[#64748B]">VRAM USAGE:</span>
                <span className="text-[#F59E0B] font-bold tabular-nums">1.42 GB / 6.00 GB (23.6%)</span>
              </div>
              <div className="w-full h-2 bg-[#11131A] rounded-xs border border-[#1E2230] overflow-hidden">
                <div className="w-[23.6%] h-full bg-[#F59E0B]"></div>
              </div>

              <div className="grid grid-cols-2 gap-2 pt-2 border-t border-[#1E2230] text-[10.5px]">
                <div>
                  <span className="text-[#64748B] block text-[9px]">SOLVER LATENCY</span>
                  <span className="text-[#10B981] font-bold tabular-nums">18.2 ms</span>
                </div>
                <div>
                  <span className="text-[#64748B] block text-[9px]">GRID CELLS</span>
                  <span className="text-[#38BDF8] font-bold tabular-nums">540,000 Nodes</span>
                </div>
              </div>
            </div>

            <div className="text-[10px] font-mono text-[#10B981] flex items-center gap-1.5 border-t border-[#1E2230] pt-2">
              <CheckCircle className="w-3 h-3 text-[#10B981]" />
              <span>Zero GPU memory leakage over 10,000 consecutive runs.</span>
            </div>
          </div>

          {/* Card 4: Acoustic Micro-Jet Shear Velocity */}
          <div className="border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col justify-between shadow-md">
            <div>
              <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2">
                <span>[CARD 04 // ACOUSTICS]</span>
                <span className="text-[#38BDF8] font-mono text-[10px] font-bold">25 kHz TRANSDUCER</span>
              </div>
              <h3 className="text-base font-bold text-[#F3F4F6]">Acoustic Micro-Jet Cavitation</h3>
              <p className="text-xs text-[#94A3B8] mt-1 leading-relaxed">
                High-intensity ultrasound streaming compresses laminar boundary layer from 52 µm to 14 µm.
              </p>
            </div>

            <div className="my-4 p-3 bg-[#090A0F] border border-[#1E2230] rounded-sm font-mono text-xs flex flex-col gap-2">
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">ACOUSTIC INTENSITY:</span>
                <span className="text-[#38BDF8] font-bold tabular-nums">1.8 W/cm² (17 W/L)</span>
              </div>
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">MASS TRANSFER LIFT:</span>
                <span className="text-[#10B981] font-bold tabular-nums">+73.0% Acceleration</span>
              </div>
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">STEADY-STATE TEMP:</span>
                <span className="text-[#F59E0B] font-bold tabular-nums">48.0°C ± 0.5°C</span>
              </div>
            </div>

            <span className="text-[10px] font-mono text-[#64748B] border-t border-[#1E2230] pt-2">
              ASME Sec VIII Div 1 certified dimple jacket steeping battery.
            </span>
          </div>

          {/* Card 5: Closed-Loop Bleed-and-Feed ZLD */}
          <div className="border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col justify-between shadow-md">
            <div>
              <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2">
                <span>[CARD 05 // ZLD SKID]</span>
                <span className="text-[#10B981] font-mono text-[10px] font-bold">85% RECYCLE LOOP</span>
              </div>
              <h3 className="text-base font-bold text-[#F3F4F6]">Zero Liquid Discharge (ZLD) MVR</h3>
              <p className="text-xs text-[#94A3B8] mt-1 leading-relaxed">
                Falling-film mechanical vapor recompression concentrator recycles 98.2% water back to wash battery.
              </p>
            </div>

            <div className="my-4 p-3 bg-[#090A0F] border border-[#1E2230] rounded-sm font-mono text-xs flex flex-col gap-2">
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">DIRECT OPEX:</span>
                <span className="text-[#10B981] font-bold tabular-nums">₹6.34 / kg Finished Dal</span>
              </div>
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">REAGENT SAVINGS:</span>
                <span className="text-[#38BDF8] font-bold tabular-nums">371.3 kg/d makeup (vs 880.9kg)</span>
              </div>
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">BYPRODUCT SYRUP:</span>
                <span className="text-[#F59E0B] font-bold tabular-nums">45% Dry Solids Cattle Feed</span>
              </div>
            </div>

            <span className="text-[10px] font-mono text-[#64748B] border-t border-[#1E2230] pt-2">
              Zero regulatory effluent discharge liability for partner mills.
            </span>
          </div>

          {/* Card 6: FSSAI / Codex Safety & Food Certification */}
          <div className="border border-[#1E2230] bg-[#11131A] rounded-sm p-5 flex flex-col justify-between shadow-md">
            <div>
              <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2">
                <span>[CARD 06 // REGULATORY]</span>
                <span className="text-[#10B981] font-mono text-[10px] font-bold">FSSAI SEC 22 COMPLIANT</span>
              </div>
              <h3 className="text-base font-bold text-[#F3F4F6]">Food Safety & Sensory Parity</h3>
              <p className="text-xs text-[#94A3B8] mt-1 leading-relaxed">
                Certified compliant with Codex Alimentarius Stan 171-1989 and ISO 11136:2014 consumer sensory protocols.
              </p>
            </div>

            <div className="my-4 p-3 bg-[#090A0F] border border-[#1E2230] rounded-sm font-mono text-xs flex flex-col gap-2">
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">RESIDUAL CITRATE:</span>
                <span className="text-[#10B981] font-bold tabular-nums">48.2 mg/kg (&lt;120 mg/kg MRL)</span>
              </div>
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">RETAINED PHOSPHATE:</span>
                <span className="text-[#10B981] font-bold tabular-nums">142 mg/kg (35x below 5,000 MRL)</span>
              </div>
              <div className="flex justify-between text-[11px]">
                <span className="text-[#64748B]">SENSORY PANEL (ISO 4120):</span>
                <span className="text-[#38BDF8] font-bold tabular-nums">p = 0.420 (Zero Parity Delta)</span>
              </div>
            </div>

            <span className="text-[10px] font-mono text-[#10B981] flex items-center gap-1 border-t border-[#1E2230] pt-2">
              <ShieldCheck className="w-3 h-3 text-[#10B981]" />
              <span>Full compliance with FSSAI Category 06.0 whole/split pulses.</span>
            </span>
          </div>

        </div>

      </div>
    </section>
  );
}
