import React, { useState } from 'react';
import { Terminal, Copy, Check, Play, CornerDownRight, Code2 } from 'lucide-react';

export default function SdkPlayground() {
  const [activeLang, setActiveLang] = useState('python');
  const [copied, setCopied] = useState(false);
  const [isExecuting, setIsExecuting] = useState(false);
  const [terminalOutput, setTerminalOutput] = useState([
    "FinnoaQ OMEGA Deterministic Multiphysics Engine [v2.4.0-release]",
    "Type or select an SDK runtime above, then click '▶ Execute Snippet' to simulate execution."
  ]);

  const snippets = {
    python: `# Python SDK: finnoaq-omega v2.4.0
import numpy as np
from finnoaq import MultiphysicsEngine, BatchProfile

# Initialize HTC pulse profile for Tanzanian nominal lot
lot = BatchProfile.from_lot_id("TZA-2026-B01", bound_ca=12.4, moisture=0.115)

# Configure S1-09 bio-chelation buffer constraints
engine = MultiphysicsEngine(
    chelation_buffer="S1-09",
    ph_target=5.20,
    ultrasound_khz=25.0,
    intensity_w_cm2=1.80
)

# Run transient 2D reaction-diffusion solver
result = engine.solve_tenderization_trajectory(lot, duration_min=24.0)

print(f"Convergence Status : {result.status}")
print(f"Core Hardness Fwb  : {result.fwb_core:.2f} N (Target <= 18.0 N)")
print(f"2-Whistle Passing  : {result.passes_two_whistles}")`,

    rust: `// Rust Core: finnoaq_core::engine
use finnoaq_core::{BioprocessEngine, PulseBatch, BufferConfig};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let batch = PulseBatch::load_tanzanian_htc("TZA-2026-B01")?;
    let config = BufferConfig::builder()
        .ph(5.20)
        .ultrasonic_intensity(1.80)
        .steep_duration_secs(1440)
        .build()?;

    let outcome = BioprocessEngine::solve_continuum(&batch, &config)?;
    assert!(outcome.core_firmness_n <= 18.0, "Two-whistle criterion failed!");
    
    println!("Processed 15 TPD lot with zero aftertaste: {:.2} N", outcome.core_firmness_n);
    Ok(())
}`,

    cli: `# FinnoaQ Unified Engineering CLI
$ finnoaq solve-trajectory \\
    --lot-id "TZA-2026-B01" \\
    --infeed-tpd 15.0 \\
    --steep-temp 48.0 \\
    --ultrasound-intensity 1.8 \\
    --duration-min 24.0 \\
    --enforce-sil3-interlock

$ finnoaq audit-economics \\
    --daily-capacity 15.0 \\
    --mandi-spread 20.0 \\
    --report-format json`,

    aspen: `* Aspen Plus V14 ELECNRTL Property Method
BLOCK EXTRACTOR D-101
  PARAM TEMP=48.0 PRES=1.01325
  MOISTURE-IN=0.115 MOISTURE-OUT=0.280
  RECYCLE-RATIO STREAM-8=0.850

BLOCK DRYER DR-101
  PARAM STAGE-1-TEMP=65.0 TEMPERING-MIN=20.0 STAGE-2-TEMP=55.0
  SPEC HOOP-STRESS-MAX=0.40 FINES-MAX=0.0035

* Stream Conservation: 0.000000% Enthalpy & Mass Balance Closure`
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(snippets[activeLang]);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleExecute = () => {
    setIsExecuting(true);
    setTerminalOutput([
      `[${new Date().toLocaleTimeString()}] Executing ${activeLang.toUpperCase()} runtime payload...`,
      "Loading finite difference mesh [540,000 spatial cells]...",
      "Coupled Fickian reaction-diffusion PDE initialized (k_chel = 4.82e-3 s⁻¹)..."
    ]);

    setTimeout(() => {
      setTerminalOutput(prev => [
        ...prev,
        "Acoustic cavitation streaming applied (BL compressed: 52 µm -> 14 µm)...",
        "Bound calcium extraction converged at t = 24.0 min: 41.8% removed.",
        "Hawkins 3L cooker acoustics: Core shear force = 15.2 N (PASSED <= 18.0 N)",
        "Zero off-flavor interlock verified: Hexanal = 0.025 ppm (OAV = 0.84 < 1.0)",
        "Status: CONVERGED // Two-Whistle Tenderization Certified (97.37% Dry Yield)."
      ]);
      setIsExecuting(false);
    }, 900);
  };

  return (
    <section id="playground" className="border-b border-[#1E2230] bg-[#090A0F] py-14">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col gap-2 mb-8 border-b border-[#1E2230] pb-6">
          <div className="flex items-center gap-2">
            <span className="font-mono text-xs font-bold text-[#F59E0B] tracking-widest uppercase">[05 // DEVELOPER PLAYGROUND]</span>
            <span className="h-1 w-1 rounded-full bg-[#F59E0B]"></span>
            <span className="font-mono text-xs text-[#64748B]">MULTI-LANGUAGE SDK & DETERMINISTIC CLI</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-[#F3F4F6] tracking-tight">
            Developer Quickstart & Interactive SDK Playground
          </h2>
          <p className="text-sm text-[#94A3B8] max-w-3xl">
            Integrate the FinnoaQ deterministic multiphysics solver into your industrial automation pipeline. Execute code snippets live below.
          </p>
        </div>

        {/* Code Editor Window */}
        <div className="border border-[#1E2230] bg-[#11131A] rounded-sm shadow-2xl overflow-hidden">
          
          {/* Top Window Bar */}
          <div className="flex flex-wrap items-center justify-between border-b border-[#1E2230] bg-[#0D111A] px-4 py-2.5">
            
            {/* Language Tabs */}
            <div className="flex items-center gap-1.5">
              {[
                { id: 'python', label: 'Python (SDK)' },
                { id: 'rust', label: 'Rust (Core)' },
                { id: 'cli', label: 'CLI (omega)' },
                { id: 'aspen', label: 'Aspen ELECNRTL' }
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveLang(tab.id)}
                  className={`font-mono text-xs px-3 py-1.5 rounded-xs transition-all ${
                    activeLang === tab.id
                      ? 'bg-[#1E2230] text-[#38BDF8] font-bold border-b-2 border-b-[#38BDF8]'
                      : 'text-[#94A3B8] hover:text-[#F3F4F6]'
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>

            {/* Actions: Copy & Execute Snippet */}
            <div className="flex items-center gap-2 mt-2 sm:mt-0">
              <button
                onClick={handleCopy}
                className="flex items-center gap-1.5 border border-[#1E2230] bg-[#090A0F] text-[#94A3B8] hover:text-[#F3F4F6] font-mono text-xs px-2.5 py-1.5 rounded-xs transition-colors"
              >
                {copied ? <Check className="w-3.5 h-3.5 text-[#10B981]" /> : <Copy className="w-3.5 h-3.5" />}
                <span>{copied ? 'Copied!' : 'Copy Code'}</span>
              </button>

              <button
                onClick={handleExecute}
                disabled={isExecuting}
                className="flex items-center gap-1.5 bg-[#10B981] hover:bg-[#059669] text-[#090A0F] font-mono text-xs font-bold px-3 py-1.5 rounded-xs transition-all disabled:opacity-50"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>{isExecuting ? 'Executing...' : '▶ Execute Snippet'}</span>
              </button>
            </div>

          </div>

          {/* Code Body */}
          <div className="p-4 bg-[#050811] overflow-x-auto">
            <pre className="font-mono text-xs sm:text-sm text-[#F3F4F6] leading-relaxed">
              <code>{snippets[activeLang]}</code>
            </pre>
          </div>

          {/* Simulated Terminal Output Pane */}
          <div className="border-t border-[#1E2230] bg-[#090A0F] p-4">
            <div className="flex items-center justify-between text-xs font-mono text-[#64748B] mb-2 pb-1 border-b border-[#1E2230]">
              <div className="flex items-center gap-2">
                <Terminal className="w-3.5 h-3.5 text-[#F59E0B]" />
                <span className="font-bold text-[#94A3B8]">SIMULATED TERMINAL STDOUT</span>
              </div>
              <span className="text-[#10B981] tabular-nums">RATE: 100 Hz // EXIT CODE 0</span>
            </div>

            <div className="font-mono text-xs text-[#CBD5E1] flex flex-col gap-1 min-h-[90px]">
              {terminalOutput.map((line, idx) => (
                <div key={idx} className="flex items-start gap-2">
                  <span className="text-[#64748B] select-none">&gt;</span>
                  <span className={line.includes("Status: CONVERGED") ? "text-[#10B981] font-bold" : line.includes("Convergence Status") ? "text-[#38BDF8]" : ""}>
                    {line}
                  </span>
                </div>
              ))}
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
