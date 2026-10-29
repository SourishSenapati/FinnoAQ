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
    <header className={`sticky top-0 z-50 w-full transition-colors duration-200 ${
      scrolled 
        ? 'bg-[#0C0E12]/95 backdrop-blur-sm border-b border-[#1E232E] shadow-sm' 
        : 'bg-[#0C0E12] border-b border-[#1E232E]'
    }`}>
      <div className="max-w-[1440px] mx-auto px-4 sm:px-8 h-14 flex items-center justify-between">
        
        {/* Left: Engineering Brand Identifier */}
        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-2">
            <span className="w-2 h-2 rounded-full bg-[#10B981]"></span>
            <span className="font-sans font-semibold text-sm tracking-tight text-[#E6E8EC]">
              FINNOAQ <span className="text-[#D97706]">OMEGA</span>
            </span>
          </div>
          <div className="hidden sm:flex items-center space-x-2 pl-3 border-l border-[#1E232E]">
            <span className="px-2 py-0.5 bg-[#151821] text-[#8E95A2] border border-[#232836] font-mono text-[11px] rounded-xs tracking-wide">
              FNQ-PR-2026-COMM-001
            </span>
            <span className="font-mono text-[11px] text-[#5E6573]">
              15 TPD
            </span>
          </div>
        </div>

        {/* Center: Anchor Navigation */}
        <nav className="hidden lg:flex items-center space-x-5 font-mono text-xs text-[#8E95A2]">
          <button 
            onClick={() => scrollTo('hero')} 
            className="hover:text-[#E6E8EC] transition-colors cursor-pointer tracking-wide"
          >
            [00 // OVERVIEW]
          </button>
          <button 
            onClick={() => scrollTo('solidworks-cad')} 
            className="text-[#D97706] hover:text-[#B45309] font-medium transition-colors cursor-pointer tracking-wide"
          >
            [01 // 3D CAD STUDIO]
          </button>
          <button 
            onClick={() => scrollTo('arbitrage')} 
            className="hover:text-[#E6E8EC] transition-colors cursor-pointer tracking-wide"
          >
            [02 // ROI ARBITRAGE]
          </button>
          <button 
            onClick={() => scrollTo('biophysics')} 
            className="hover:text-[#E6E8EC] transition-colors cursor-pointer tracking-wide"
          >
            [03 // BIOPHYSICS]
          </button>
          <button 
            onClick={() => scrollTo('pfd-aspen')} 
            className="hover:text-[#E6E8EC] transition-colors cursor-pointer tracking-wide"
          >
            [04 // PFD & ASPEN]
          </button>
          <button 
            onClick={() => scrollTo('roadmap')} 
            className="hover:text-[#E6E8EC] transition-colors cursor-pointer tracking-wide"
          >
            [05 // ROADMAP]
          </button>
          <button 
            onClick={() => scrollTo('data-room')} 
            className="hover:text-[#E6E8EC] transition-colors cursor-pointer tracking-wide"
          >
            [06 // DATA ROOM]
          </button>
        </nav>

        {/* Right: Technical Deliverable Download & Trial Action */}
        <div className="flex items-center space-x-2.5">
          <a
            href="/finnoaq_commercial_investor_proposal.pdf"
            download="finnoaq_commercial_investor_proposal.pdf"
            className="hidden sm:inline-flex items-center px-2.5 py-1 font-mono text-[11px] text-[#8E95A2] hover:text-[#E6E8EC] border border-[#232836] hover:border-[#3D4559] rounded-xs transition-colors"
          >
            ↓ Proposal (PDF)
          </a>
          <button
            onClick={() => scrollTo('scoping')}
            className="px-3 py-1.5 bg-[#D97706] hover:bg-[#B45309] text-black font-semibold text-xs tracking-wider uppercase rounded-xs transition-colors cursor-pointer font-mono"
          >
            Request 48-Hr Trial →
          </button>
        </div>

      </div>
    </header>
  );
}
