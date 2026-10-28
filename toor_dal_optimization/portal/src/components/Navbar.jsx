import React from 'react';
import { Activity, ShieldCheck, Terminal, Sun, Moon, Download, Layers } from 'lucide-react';

export default function Navbar({ theme, setTheme }) {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-[#1E2230] bg-[#090A0F]/90 backdrop-blur-md">
      <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        
        {/* Brand & Version Badge */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2">
            <span className="flex h-2 w-2 rounded-full bg-[#10B981] animate-pulse"></span>
            <span className="font-mono text-xs font-bold tracking-widest text-[#F3F4F6] uppercase">
              FINNOAQ<span className="text-[#F59E0B]">.OMEGA</span>
            </span>
          </div>
          <span className="hidden sm:inline-block font-mono text-[10px] tracking-wider text-[#64748B] border border-[#1E2230] px-2 py-0.5 rounded-sm bg-[#11131A]">
            v2.4 DETERMINISTIC ENGINE // SIL-3
          </span>
        </div>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center gap-6 font-mono text-xs text-[#94A3B8]">
          <a href="#architecture" className="hover:text-[#F3F4F6] transition-colors flex items-center gap-1.5">
            <Layers className="w-3.5 h-3.5 text-[#38BDF8]" />
            [01 // ARCHITECTURE]
          </a>
          <a href="#pipeline" className="hover:text-[#F3F4F6] transition-colors">
            [02 // PIPELINE]
          </a>
          <a href="#comparator" className="hover:text-[#F3F4F6] transition-colors">
            [03 // COMPARATOR]
          </a>
          <a href="#guarantees" className="hover:text-[#F3F4F6] transition-colors">
            [04 // BENTO]
          </a>
          <a href="#benchmarks" className="hover:text-[#F3F4F6] transition-colors">
            [05 // BENCHMARKS]
          </a>
          <a href="#playground" className="hover:text-[#F3F4F6] transition-colors flex items-center gap-1.5">
            <Terminal className="w-3.5 h-3.5 text-[#F59E0B]" />
            [06 // SDK]
          </a>
        </nav>

        {/* Actions & Telemetry */}
        <div className="flex items-center gap-3">
          <div className="hidden lg:flex items-center gap-2 font-mono text-[11px] text-[#10B981] bg-[#10B981]/10 border border-[#10B981]/30 px-2.5 py-1 rounded-sm">
            <Activity className="w-3 h-3" />
            <span className="tabular-nums">48.0°C // 25.0 kHz // 15.2N</span>
          </div>

          <a 
            href="#vault"
            className="flex items-center gap-1.5 bg-[#F3F4F6] hover:bg-white text-[#090A0F] font-mono text-xs font-semibold px-3 py-1.5 rounded-sm transition-all"
          >
            <Download className="w-3.5 h-3.5" />
            <span>Dossier PDF</span>
          </a>

          {/* Theme Toggle Button */}
          <button
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            className="flex h-8 w-8 items-center justify-center rounded-sm border border-[#1E2230] bg-[#11131A] text-[#94A3B8] hover:text-[#F3F4F6] transition-colors"
            aria-label="Toggle visual theme"
          >
            {theme === 'dark' ? <Sun className="w-4 h-4 text-[#F59E0B]" /> : <Moon className="w-4 h-4 text-[#38BDF8]" />}
          </button>
        </div>

      </div>
    </header>
  );
}
