# AUDIT DIRECTIVE: MANDATORY FORENSIC CHALLENGE & VERIFICATION

**Document ID:** FIN-AUD-DIR-2026-001  
**Status:** ACTIVE / MANDATORY ENFORCEMENT  
**Controlling Authority:** Project Engineering Red-Team & Forensic Audit  
**Date:** 2026-10-14  

---

## What Needs to Be Challenged First

### 1. The 8192 × 8192 Benchmark Needs Verification
The report claims 67,108,864 grid nodes, a runtime of 0.0051 seconds and just 64.06 MB of peak VRAM.

A single full-grid float32 field alone requires 256 MiB, before any additional physical variables. The claimed runtime equates to roughly 13.2 billion grid nodes per second. That is a major red flag for a coupled multiphysics solver on a laptop GPU. It may be measuring only a small chunk, an analytical shortcut, or something other than a complete grid solve. The source code and profiler evidence must establish which.

### 2. The Material-Recovery Results Contradict One Another
The candidate-ranking table reports 96.8% recovery, while the executive summary and final recommendation claim 98.54% for the winning candidate. The reported retained-sodium figures also differ between the table and recommendation, without a clearly reconciled measurement basis.

These values must be recalculated from the actual equations, parameter configuration and mass balances—not adjusted to make the candidate appear successful.

### 3. The Molecular Mechanism Has Not Been Demonstrated
The report proposes that pectin methylesterase, phytase, calcium pectate formation and sodium bicarbonate explain the treatment response. It then uses a mathematical expression to predict a 7.73-fold increase in softening rate.

These are hypotheses until the relevant source evidence, parameter provenance and experiments establish the links. An equation that produces a plausible prediction does not establish that the mechanism occurs in the target dal.

### 4. The Treatment Winner Is Still Computationally Proposed
Candidate CAND-004 predicts 13.8 minutes, but the untreated baseline in the ranking is 58 minutes and 16.9 whistles. That is not the same as an experimentally standardized comparison against your original approximately six-whistle observation.

The predicted time reduction is worth investigating; it is not yet an observed result.

### 5. Four Control and Four Treatment Batches Cannot Automatically Establish Five Sigma
The report claims that entering four control and four candidate timestamps will immediately establish five-sigma significance and unlock industrial scale-up.

That conclusion is invalid. Statistical significance depends on the actual effect size, variability, experimental design and prespecified analysis. The experiment must not be guaranteed to pass before its observations exist. Nor should it unlock Stage 2 automatically without satisfying all acceptance criteria.

---

## Operating Instruction
Do not ask it to add more molecular dynamics, larger meshes or more AI models yet. First establish whether the current components compute what their reports claim they compute. Paste this audit directive into the existing workspace.
