import React, { useState } from 'react';
import { CUSTOMER_DISCOVERY } from '../data/micrositeData.js';

export default function Module6MillerScoping() {
  const [formData, setFormData] = useState({
    millName: '',
    contactPerson: '',
    phoneEmail: '',
    dailyCapacityTpd: '100 TPD',
    origin: 'Tanzania (Shinyanga / Dar)',
    whistleCount: '8+ Whistles (60–70 min)',
    sampleReady: true
  });

  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <section id="scoping" className="w-full bg-[#0A0B0D] border-b border-[#222630] scroll-mt-20">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [05 // MILLER DISCOVERY & 48-HR DIAGNOSTIC WORKFLOW]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Miller Discovery, 48-Hour Diagnostic Trial & Scoping Portal
            </h2>
          </div>
          <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm">
            15/15 MILLS CONFIRMED HTC PAIN // 86.7% WTP
          </span>
        </div>

        {/* 2-Column Swiss Grid Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-12">
          
          {/* Left Column: 4 Metrics, 2 Editorial Blockquotes & 5-Step Timeline (6 Cols) */}
          <div className="lg:col-span-6 p-6 sm:p-8 bg-[#0A0B0D] border-b lg:border-b-0 lg:border-r border-[#222630] flex flex-col justify-between">
            <div>
              <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider mb-4">
                COMMERCIAL MILLER VALIDATION & PAIN-POINT AUDIT
              </div>

              {/* 4 Validation Metrics */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-6">
                <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm text-center">
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#F3F4F6] tabular-nums">
                    {CUSTOMER_DISCOVERY.totalMillersInterviewed}
                  </div>
                  <div className="font-mono text-[10px] text-[#64748B]">Millers Audited</div>
                  <div className="font-mono text-[9px] text-[#9CA3AF]">Latur, Akola, Indore</div>
                </div>

                <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm text-center">
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#EF4444] tabular-nums">
                    100%
                  </div>
                  <div className="font-mono text-[10px] text-[#64748B]">Confirmed HTC</div>
                  <div className="font-mono text-[9px] text-[#EF4444]">8+ Whistles Rejection</div>
                </div>

                <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm text-center">
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#F59E0B] tabular-nums">
                    86.7%
                  </div>
                  <div className="font-mono text-[10px] text-[#64748B]">WTP Tolling</div>
                  <div className="font-mono text-[9px] text-[#F59E0B]">₹10–₹12/kg Fee</div>
                </div>

                <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm text-center">
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#10B981] tabular-nums">
                    6
                  </div>
                  <div className="font-mono text-[10px] text-[#64748B]">Host Mills</div>
                  <div className="font-mono text-[9px] text-[#10B981]">Signed EOIs for Demo</div>
                </div>
              </div>

              {/* 2 Understated Editorial Blockquotes */}
              <div className="space-y-3 mb-6">
                {CUSTOMER_DISCOVERY.keyMillerQuotes.map((q, idx) => (
                  <blockquote 
                    key={idx}
                    className="p-3.5 bg-[#111317] border-l-2 border-[#F59E0B] border-y border-r border-[#222630] rounded-sm"
                  >
                    <p className="text-xs sm:text-sm text-[#F3F4F6] italic leading-relaxed mb-2 font-serif">
                      "{q.quote}"
                    </p>
                    <footer className="font-mono text-[11px] text-[#64748B] flex items-center space-x-2">
                      <span className="text-[#F59E0B]">—</span>
                      <span>{q.miller}</span>
                    </footer>
                  </blockquote>
                ))}
              </div>

              {/* 5-Step Vertical 48-Hour Diagnostic Timeline */}
              <div className="mt-6 pt-4 border-t border-[#222630]">
                <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider mb-3">
                  48-HOUR 5-KG DIAGNOSTIC TRIAL PROTOCOL
                </div>
                <div className="space-y-2">
                  {CUSTOMER_DISCOVERY.diagnosticWorkflow.map((step, idx) => (
                    <div 
                      key={idx}
                      className="p-3 bg-[#111317] border border-[#222630] rounded-sm flex items-start space-x-3 font-mono text-xs"
                    >
                      <div className="px-2 py-0.5 bg-[#0A0B0D] text-[#F59E0B] border border-[#222630] rounded-xs font-semibold shrink-0">
                        {step.time}
                      </div>
                      <div className="flex-1">
                        <div className="text-[#F3F4F6] font-medium mb-0.5">{step.step}</div>
                        <div className="text-[#9CA3AF] text-[11px] font-sans">{step.desc}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

            </div>

            <div className="font-mono text-[11px] text-[#64748B] pt-4 mt-6 border-t border-[#222630]">
              Empirical Customer Discovery Interviews Audited under FNQ-PR-2026-COMM-001
            </div>
          </div>

          {/* Right Column: Industrial Laboratory Intake Manifest Form (6 Cols) */}
          <div className="lg:col-span-6 p-6 sm:p-8 bg-[#111317] flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-center mb-4">
                <span className="font-mono text-xs text-[#64748B] uppercase tracking-wider">
                  LABORATORY INTAKE MANIFEST // 48-HR DIAGNOSTIC
                </span>
                <span className="font-mono text-xs text-[#F59E0B]">
                  SECURE MILL INTAKE
                </span>
              </div>

              {submitted ? (
                <div className="p-6 bg-[#0A0B0D] border border-[#10B981] rounded-sm text-left">
                  <div className="flex items-center space-x-2 text-[#10B981] font-mono text-sm font-semibold mb-2">
                    <span>✓</span>
                    <span>INTAKE MANIFEST REGISTERED // TICKET #FNQ-DT-2026-088</span>
                  </div>
                  <p className="text-xs text-[#9CA3AF] leading-relaxed mb-4 font-mono">
                    Diagnostic trial protocol dispatched for <strong className="text-[#F3F4F6]">{formData.millName || 'Your Pulse Mill'}</strong>. 
                    Our laboratory coordination desk will transmit courier sample packaging guidelines 
                    for your 5.0 kg unconditioned consignment.
                  </p>
                  <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm font-mono text-xs space-y-1 text-[#64748B]">
                    <div>Facility: <span className="text-[#F3F4F6]">{formData.millName}</span></div>
                    <div>Contact: <span className="text-[#F3F4F6]">{formData.contactPerson} ({formData.phoneEmail})</span></div>
                    <div>Consignment: <span className="text-[#F59E0B]">{formData.origin} // {formData.whistleCount}</span></div>
                    <div>Assay: Hawkins 3L Venting + FWB Shear Force + ISO 4120 Sensory</div>
                  </div>
                  <button
                    onClick={() => setSubmitted(false)}
                    className="mt-4 px-4 py-1.5 bg-[#171A21] hover:bg-[#222630] text-[#9CA3AF] hover:text-[#F3F4F6] border border-[#222630] rounded-sm font-mono text-xs cursor-pointer transition-colors"
                  >
                    ← Submit Another Manifest
                  </button>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-4 font-mono text-xs">
                  
                  {/* Field 1: Mill Name */}
                  <div>
                    <label className="block text-[#9CA3AF] mb-1.5 uppercase tracking-wide">
                      01 // Mill / Processing Facility Name *
                    </label>
                    <input
                      type="text"
                      required
                      placeholder="e.g. Sri Balaji Dal Mill / Latur Agro"
                      value={formData.millName}
                      onChange={(e) => setFormData({ ...formData, millName: e.target.value })}
                      className="w-full px-3 py-2 bg-[#0A0B0D] border border-[#222630] focus:border-[#F59E0B] text-[#F3F4F6] rounded-sm outline-none transition-colors"
                    />
                  </div>

                  {/* Field 2 & 3: Contact Person & Phone/Email */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                      <label className="block text-[#9CA3AF] mb-1.5 uppercase tracking-wide">
                        02 // Representative Name & Role *
                      </label>
                      <input
                        type="text"
                        required
                        placeholder="e.g. Rajesh Patil (Managing Partner)"
                        value={formData.contactPerson}
                        onChange={(e) => setFormData({ ...formData, contactPerson: e.target.value })}
                        className="w-full px-3 py-2 bg-[#0A0B0D] border border-[#222630] focus:border-[#F59E0B] text-[#F3F4F6] rounded-sm outline-none transition-colors"
                      />
                    </div>
                    <div>
                      <label className="block text-[#9CA3AF] mb-1.5 uppercase tracking-wide">
                        03 // Mobile / Business Email *
                      </label>
                      <input
                        type="text"
                        required
                        placeholder="e.g. +91 98230 XXXXX / info@dalmill.in"
                        value={formData.phoneEmail}
                        onChange={(e) => setFormData({ ...formData, phoneEmail: e.target.value })}
                        className="w-full px-3 py-2 bg-[#0A0B0D] border border-[#222630] focus:border-[#F59E0B] text-[#F3F4F6] rounded-sm outline-none transition-colors"
                      />
                    </div>
                  </div>

                  {/* Field 4 & 5: Daily Capacity & Consignment Origin */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                      <label className="block text-[#9CA3AF] mb-1.5 uppercase tracking-wide">
                        04 // Daily Milling Capacity
                      </label>
                      <select
                        value={formData.dailyCapacityTpd}
                        onChange={(e) => setFormData({ ...formData, dailyCapacityTpd: e.target.value })}
                        className="w-full px-3 py-2 bg-[#0A0B0D] border border-[#222630] focus:border-[#F59E0B] text-[#F3F4F6] rounded-sm outline-none transition-colors cursor-pointer"
                      >
                        <option value="50 TPD">50 TPD (Medium Mill)</option>
                        <option value="100 TPD">100 TPD (Standard Commercial)</option>
                        <option value="150 TPD">150 TPD (Large Commercial)</option>
                        <option value="200+ TPD">200+ TPD (Industrial Group)</option>
                      </select>
                    </div>

                    <div>
                      <label className="block text-[#9CA3AF] mb-1.5 uppercase tracking-wide">
                        05 // Consignment Origin
                      </label>
                      <select
                        value={formData.origin}
                        onChange={(e) => setFormData({ ...formData, origin: e.target.value })}
                        className="w-full px-3 py-2 bg-[#0A0B0D] border border-[#222630] focus:border-[#F59E0B] text-[#F3F4F6] rounded-sm outline-none transition-colors cursor-pointer"
                      >
                        <option value="Tanzania (Shinyanga / Dar)">Tanzania (Shinyanga / Dar)</option>
                        <option value="Mozambique (Nampula / Nacala)">Mozambique (Nampula / Nacala)</option>
                        <option value="Malawi / East Africa Bold">Malawi / East Africa Bold</option>
                        <option value="Myanmar (Lemon / White)">Myanmar (Lemon / White)</option>
                      </select>
                    </div>
                  </div>

                  {/* Field 6: Observed Whistle Count */}
                  <div>
                    <label className="block text-[#9CA3AF] mb-1.5 uppercase tracking-wide">
                      06 // Observed Pressure Cooker Whistle Count
                    </label>
                    <select
                      value={formData.whistleCount}
                      onChange={(e) => setFormData({ ...formData, whistleCount: e.target.value })}
                      className="w-full px-3 py-2 bg-[#0A0B0D] border border-[#222630] focus:border-[#F59E0B] text-[#F3F4F6] rounded-sm outline-none transition-colors cursor-pointer"
                    >
                      <option value="8+ Whistles (60–70 min)">8+ Whistles (Severe HTC Defect)</option>
                      <option value="6 to 8 Whistles (45–60 min)">6 to 8 Whistles (Moderate Hardening)</option>
                      <option value="4 to 6 Whistles (30–45 min)">4 to 6 Whistles (Intermediate)</option>
                    </select>
                  </div>

                  {/* Sample Ready Checkbox */}
                  <div className="pt-2">
                    <label className="flex items-center space-x-2 text-[#9CA3AF] cursor-pointer">
                      <input
                        type="checkbox"
                        checked={formData.sampleReady}
                        onChange={(e) => setFormData({ ...formData, sampleReady: e.target.checked })}
                        className="accent-[#F59E0B] rounded-xs cursor-pointer"
                      />
                      <span className="text-[11px]">
                        5.0 kg representative split dal lot ready for courier dispatch to FinnoaQ bench
                      </span>
                    </label>
                  </div>

                  {/* Submit Button */}
                  <div className="pt-2">
                    <button
                      type="submit"
                      className="w-full py-2.5 bg-[#F59E0B] hover:bg-[#D97706] text-black font-semibold rounded-sm transition-colors cursor-pointer font-mono text-xs uppercase tracking-tight"
                    >
                      Transmit Diagnostic Trial Request (48-Hr Protocol)
                    </button>
                  </div>

                </form>
              )}
            </div>

            <div className="font-mono text-[11px] text-[#64748B] pt-4 mt-6 border-t border-[#222630]">
              Confidentiality Notice: Consignment assays protected under mutual FinnoaQ Industrial NDA
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}

