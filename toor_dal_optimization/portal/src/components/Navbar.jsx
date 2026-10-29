import React, { useState, useEffect } from 'react';

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className={`sticky top-0 z-50 w-full transition-all duration-300 ${
      scrolled 
        ? 'bg-[#090A0E]/95 backdrop-blur-md border-b border-white/[0.08] shadow-2xl' 
        : 'bg-[#090A0E] border-b border-[#1E2330]'
    }`}>
      <div className="max-w-[1440px] mx-auto px-4 sm:px-8 h-16 flex items-center justify-between">
        
        {/* Left: Prestige Institutional Brand Identifier */}
        <div className="flex items-center space-x-3.5">
          <div className="flex items-center space-x-2">
            <span className="w-2.5 h-2.5 rounded-full bg-[#F59E0B] shadow-[0_0_10px_#F59E0B] animate-pulse"></span>
            <span className="font-sans font-bold text-base tracking-tight text-white">
              FINNOAQ <span className="text-[#F59E0B]">OMEGA</span>
            </span>
          </div>
          <div className="hidden sm:flex items-center space-x-2 pl-3 border-l border-[#222630]">
            <span className="px-2 py-0.5 bg-[#141720] text-[#94A3B8] border border-[#262C3D] font-mono text-[11px] rounded tracking-wide">
              FNQ-PR-2026-COMM-001
            </span>
            <span className="font-mono text-[11px] text-[#64748B]">
              15 TPD TURNKEY
            </span>
          </div>
        </div>

        {/* Center: Luxury Monospace Anchor Navigation */}
        <nav className="hidden lg:flex items-center space-x-6 font-mono text-xs text-[#94A3B8]">
          <button 
            onClick={() => scrollTo('hero')} 
            className="hover:text-white transition-colors cursor-pointer tracking-wider"
          >
            [00 // OVERVIEW]
          </button>
          <button 
            onClick={() => scrollTo('solidworks-cad')} 
            className="text-[#F59E0B] hover:text-[#FBBF24] font-semibold transition-colors cursor-pointer tracking-wider flex items-center space-x-1"
          >
            <span>[01 // 3D CAD STUDIO]</span>
          </button>
          <button 
            onClick={() => scrollTo('arbitrage')} 
            className="hover:text-white transition-colors cursor-pointer tracking-wider"
          >
            [02 // ROI ARBITRAGE]
          </button>
          <button 
            onClick={() => scrollTo('biophysics')} 
            className="hover:text-white transition-colors cursor-pointer tracking-wider"
          >
            [03 // BIOPHYSICS]
          </button>
          <button 
            onClick={() => scrollTo('pfd-aspen')} 
            className="hover:text-white transition-colors cursor-pointer tracking-wider"
          >
            [04 // PFD & ASPEN]
          </button>
          <button 
            onClick={() => scrollTo('roadmap')} 
            className="hover:text-white transition-colors cursor-pointer tracking-wider"
          >
            [05 // ROADMAP]
          </button>
          <button 
            onClick={() => scrollTo('data-room')} 
            className="hover:text-white transition-colors cursor-pointer tracking-wider"
          >
            [06 // DATA ROOM]
          </button>
        </nav>

        {/* Right: High-Conversion VIP Call To Action */}
        <div className="flex items-center space-x-3">
          <a
            href="/finnoaq_commercial_investor_proposal.pdf"
            download="finnoaq_commercial_investor_proposal.pdf"
            className="hidden sm:inline-flex items-center px-3 py-1.5 font-mono text-xs text-[#94A3B8] hover:text-white border border-[#262C3D] hover:border-white/30 rounded transition-colors"
          >
            ↓ Proposal (PDF)
          </a>
          <button
            onClick={() => scrollTo('scoping')}
            className="px-4 py-2 bg-gradient-to-r from-[#F59E0B] to-[#D97706] hover:from-[#FBBF24] hover:to-[#F59E0B] text-black font-semibold text-xs tracking-wide uppercase rounded shadow-[0_0_15px_rgba(245,158,11,0.35)] hover:shadow-[0_0_25px_rgba(245,158,11,0.55)] transition-all transform hover:-translate-y-0.5 cursor-pointer font-mono"
          >
            Request 48-Hr Trial →
          </button>
        </div>

      </div>
    </header>
  );
}
