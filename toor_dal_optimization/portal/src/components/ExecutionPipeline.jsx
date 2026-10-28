import React, { useState } from 'react';
import { Eye, ShieldAlert, Cpu, Gauge, CheckCircle2, ChevronRight, Binary, ArrowRight } from 'lucide-react';

export default function ExecutionPipeline() {
  const [activeStage, setActiveStage] = useState(0);

  const stages = [
    {
      id: "01",
      title: "NIR & Acoustic Sensor Ingestion",
      tag: "REAL-TIME DIAGNOSTIC TELEMETRY",
      latency: "3.2ms",
      desc: "Continuous dual-beam NIR spectroscopy continuously interrogates incoming Tanzanian and Mozambique cotyledons at 1,450 nm and 1,940 nm, measuring native moisture (11.5% wb ± 0.4%) and cotyledon surface hardness before steeping.",
      equation: "\\text{Moisture (wb)} = a_0 + a_1 \\cdot \\log\\left(\\frac{R_{1450}}{R_{1300}}\\right) + a_2 \\cdot \\log\\left(\\frac{R_{1940}}{R_{1300}}\\right)",
      codeSnippet: `// NIR Ingestion Loop (Rate: 100 Hz)
const rawSample = nirSpectrometer.readWavelength([1450, 1940]);
const batchHardness = texturePress.sampleLot(rawSample);
if (batchHardness > 40.0) {
  telemetry.triggerAdaptiveProtocol("HTC_SEVERE_CHELATION");
}`,
      schematic: {
        unit: "D-101 // NIR SENSOR ARRAY",
        signal: "Reflectance Index R = 0.842",
        status: "SAMPLING CONTINUOUS (100 Hz)",
        activeNode: "Ingestion Array"
      }
    },
    {
      id: "02",
      title: "Transient Reaction-Diffusion Mechanistic Solver",
      tag: "FICKIAN CONTINUUM DISCRETIZATION",
      latency: "14.8ms",
      desc: "Solves coupled second-order reaction-diffusion PDEs over an axisymmetric cotyledon mesh (12x12 & 24x24 verified). Unzips middle lamella calcium pectate egg-box complexes via multi-salt tripotassium citrate chelation.",
      equation: "\\frac{\\partial [\\text{Ca}^{2+}]}{\\partial t} = D_{\\text{eff}} \\left( \\frac{\\partial^2 [\\text{Ca}^{2+}]}{\\partial r^2} + \\frac{1}{r} \\frac{\\partial [\\text{Ca}^{2+}]}{\\partial r} \\right) - k_{\\text{chel}} [\\text{Cit}^{3-}] [\\text{Ca}^{2+}]",
      codeSnippet: `// 2D Finite Difference Spatial Operator
const d2Ca_dr2 = (Ca[r+1] - 2*Ca[r] + Ca[r-1]) / (dr * dr);
const dCa_dr   = (Ca[r+1] - Ca[r-1]) / (2 * dr);
const R_chel   = k_chel * Math.max(0, Citrate[r]) * Ca[r];
dCa_dt[r]      = D_eff * (d2Ca_dr2 + (1/r) * dCa_dr) - R_chel;`,
      schematic: {
        unit: "TK-101A/B // ULTRASONIC CHELATION",
        signal: "k_chel = 4.82e-3 s⁻¹ // Deff = 1.45e-10 m²/s",
        status: "PDE CONVERGED (L2 Norm < 1e-6)",
        activeNode: "Diffusion Solver"
      }
    },
    {
      id: "03",
      title: "Deterministic Safety & pH Drift Interlock",
      tag: "SIL-3 HARDWARE INTERLOCK",
      latency: "2.4ms",
      desc: "Monitors steep liquor pH at 5.20 ± 0.05. If lipoxygenase (LOX) inhibition drops or ultrasonic horn impedance excursions exceed ±8%, automated pneumatic dump valves actuate in <5ms, diverting off-spec liquor to the bleed buffer.",
      equation: "\\Delta \\text{pH} = |\\text{pH}_{\\text{measured}} - 5.20| > 0.15 \\implies \\text{TRIP}_{\\text{SCRAM}} < 5.0\\text{ ms}",
      codeSnippet: `// SIL-3 Hardware Interlock
if (Math.abs(liquor_pH - 5.20) > 0.15 || horn_impedance > 1.25 * Z_nom) {
  pneumaticValve.actuateSafetyBypass(); // Latency < 4.2ms
  interlockLog.recordFault("pH_DRIFT_INTERLOCK_ACTUATED");
  systemState.setMode("FAIL_SAFE_RECIRCULATION");
}`,
      schematic: {
        unit: "ESD-101 // PNEUMATIC SCRAM VALVE",
        signal: "pH = 5.20 ± 0.02 // LOX Inhibition = 86.4%",
        status: "INTERLOCK ARMED // TRIP < 5ms",
        activeNode: "Safety Trip"
      }
    },
    {
      id: "04",
      title: "12s Deluge Wash & Tempered Fluid-Bed Actuation",
      tag: "ZERO LIQUID DISCHARGE ACTUATION",
      latency: "18.2ms",
      desc: "Hydrated cotyledons receive a 12-second counter-current deluge rinse with ZLD MVR evaporator condensate, stripping surface citrate to 48.2 mg/kg. An adiabatic 20-min tempering deck bounds cotyledon hoop stress below 0.40 MPa.",
      equation: "\\sigma_{\\theta\\theta} = \\frac{E}{1 - \\nu} \\left( \\frac{1}{R^3} \\int_0^R M(r) r^2 dr - M(r) \\right) \\le 0.40\\text{ MPa}",
      codeSnippet: `// Two-Stage Tempered Drying Controller
deck1.setAirTemperature(65.0); // Rapid surface moisture removal
temperingDeck.holdAdiabatic(20.0); // Gradients equilibrate
deck2.setAirTemperature(55.0); // Final conditioning to 10.5% wb
stressMonitor.verifyHoopStressMax(0.38); // Broken fines < 0.35%`,
      schematic: {
        unit: "DR-101A/B & SC-101 // TEMPERED DRYER",
        signal: "M_out = 10.5% wb // Fines Breakage < 0.35%",
        status: "ACTUATION ACTIVE (97.37% Dry Yield)",
        activeNode: "Drying Actuation"
      }
    }
  ];

  const current = stages[activeStage];

  return (
    <section id="pipeline" className="border-b border-[#1E2230] bg-[#090A0F] py-14">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading */}
        <div className="flex flex-col gap-2 mb-10 border-b border-[#1E2230] pb-6">
          <div className="flex items-center gap-2">
            <span className="font-mono text-xs font-bold text-[#38BDF8] tracking-widest uppercase">[01 // EXECUTION PIPELINE]</span>
            <span className="h-1 w-1 rounded-full bg-[#38BDF8]"></span>
            <span className="font-mono text-xs text-[#64748B]">SCROLLYTELLING MULTIPHYSICS ARCHITECTURE</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-[#F3F4F6] tracking-tight">
            Deterministic Closed-Loop Pulse Engineering Pipeline
          </h2>
          <p className="text-sm text-[#94A3B8] max-w-3xl">
            From raw Tanzanian intake to tenderized finished split toor dal: 4 deterministic pipeline stages executing under 20ms real-time supervisory control.
          </p>
        </div>

        {/* Split-Layout: Left 4 Stage Selectors, Right Sticky Morphing Schematic */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Left Column (5 Cols): Interactive Stepper */}
          <div className="lg:col-span-5 flex flex-col gap-3">
            {stages.map((st, idx) => (
              <div
                key={st.id}
                onClick={() => setActiveStage(idx)}
                className={`border p-4 rounded-sm cursor-pointer transition-all ${
                  activeStage === idx
                    ? 'border-[#38BDF8] bg-[#11131A] shadow-lg'
                    : 'border-[#1E2230] bg-[#090A0F] hover:bg-[#11131A]/50 opacity-75'
                }`}
              >
                <div className="flex items-center justify-between font-mono text-[11px] mb-1.5">
                  <span className={activeStage === idx ? 'text-[#38BDF8] font-bold' : 'text-[#64748B]'}>
                    STAGE {st.id} // {st.tag}
                  </span>
                  <span className="text-[#10B981] tabular-nums font-bold">
                    {st.latency}
                  </span>
                </div>
                <h3 className={`text-base font-bold transition-colors ${activeStage === idx ? 'text-[#F3F4F6]' : 'text-[#94A3B8]'}`}>
                  {st.title}
                </h3>
                <p className="text-xs text-[#64748B] mt-2 line-clamp-2 leading-relaxed">
                  {st.desc}
                </p>
              </div>
            ))}
          </div>

          {/* Right Column (7 Cols): Sticky Dynamic Morphing Schematic & Math Box */}
          <div className="lg:col-span-7 sticky top-20 border border-[#1E2230] bg-[#11131A] rounded-sm p-6 flex flex-col gap-5 shadow-2xl">
            
            {/* Header Telemetry Bar */}
            <div className="flex items-center justify-between border-b border-[#1E2230] pb-3 font-mono text-xs">
              <div className="flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-[#10B981] animate-ping"></span>
                <span className="font-bold text-[#F3F4F6]">{current.schematic.unit}</span>
              </div>
              <span className="text-[#38BDF8] border border-[#1E2230] px-2 py-0.5 rounded-sm bg-[#090A0F]">
                {current.schematic.status}
              </span>
            </div>

            {/* Morphing Visual Schematic Box */}
            <div className="border border-[#1E2230] bg-[#090A0F] p-4 rounded-sm">
              <div className="flex items-center justify-between text-[11px] font-mono text-[#64748B] mb-3">
                <span>ACTIVE SUBSYSTEM SCHEMATIC: <strong>{current.schematic.activeNode}</strong></span>
                <span className="text-[#F59E0B] font-bold tabular-nums">LATENCY: {current.latency}</span>
              </div>

              {/* Dynamic Subsystem Flow Diagram */}
              <div className="relative h-28 border border-[#1E2230] bg-[#0D111A] rounded-sm p-3 flex items-center justify-between font-mono text-xs overflow-hidden">
                <div className="border border-[#1E2230] bg-[#151C2A] p-2 rounded-sm text-center w-28">
                  <span className="text-[9px] text-[#64748B]">INLET</span>
                  <div className="font-bold text-[#F3F4F6]">Stream In</div>
                </div>

                {/* Animated Flow Arrow */}
                <div className="flex-1 px-4 flex flex-col items-center">
                  <div className="w-full h-0.5 bg-[#1E2230] relative overflow-hidden">
                    <div className="absolute inset-y-0 w-1/3 bg-[#38BDF8] animate-pulse"></div>
                  </div>
                  <span className="text-[10px] text-[#38BDF8] mt-1 tabular-nums">
                    {current.schematic.signal}
                  </span>
                </div>

                <div className="border border-[#10B981] bg-[#10B981]/10 p-2 rounded-sm text-center w-36">
                  <span className="text-[9px] text-[#10B981]">OPERATIONAL NODE</span>
                  <div className="font-bold text-[#F3F4F6] text-[11px]">{current.schematic.activeNode}</div>
                </div>
              </div>
            </div>

            {/* Governing Mathematical Equation Card */}
            <div className="border border-[#1E2230] bg-[#090A0F] p-4 rounded-sm flex flex-col gap-2">
              <span className="font-mono text-[10px] text-[#64748B] uppercase tracking-wider">
                GOVERNING CONTINUUM PHYSICS & PDE EQUATION
              </span>
              <div className="font-mono text-xs sm:text-sm text-[#38BDF8] bg-[#11131A] p-3 rounded-sm border border-[#1E2230] overflow-x-auto tabular-nums">
                {current.equation}
              </div>
            </div>

            {/* State Transition Code Window */}
            <div className="border border-[#1E2230] bg-[#090A0F] p-4 rounded-sm flex flex-col gap-2">
              <div className="flex justify-between font-mono text-[10px] text-[#64748B]">
                <span>STATE TRANSITION CODE SNIPPET</span>
                <span className="text-[#10B981]">DETERMINISTIC JIT COMPILED</span>
              </div>
              <pre className="font-mono text-[11px] text-[#94A3B8] bg-[#050811] p-3 rounded-sm border border-[#1E2230] overflow-x-auto leading-relaxed">
                {current.codeSnippet}
              </pre>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}
