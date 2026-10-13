# Harakutir R&D Workspace Rules

## Scientific integrity
- Never invent, randomize, impute or hard-code laboratory measurements as observed results.
- Synthetic records belong only in `data/synthetic/` with an unmistakable `synthetic_test_only` marker; tests must prove they cannot enter a real report.
- Every empirical claim must link to data provenance. Preserve missingness and source units; log conversions and exclusions.
- Distinguish measured difference, association, potential mechanism, and Phase 2 validation. Correlation and p-values do not establish causality.
- Phase 1 is diagnostic. Do not silently add commercial process optimization, pilot production, shelf-life or regulatory validation.

## Execution and recovery
- Inspect existing files before modifying them; never overwrite source files or clear state on startup.
- Checkpoint task-level progress atomically, periodically and before/after phase transitions. Save on graceful interrupt and recover after process failure from the last verified checkpoint.
- Make tasks idempotent; keep an append-only event log; preserve the previous known-good checkpoint.
- Use one supervisor/run lock and at most one GPU-consuming worker unless benchmarked evidence supports another configuration.
- Run deterministic tests before promoting any output or candidate policy. Do not claim completion when a critical gate fails.

## Privacy and operations
- Keep project/sample/client data local unless transfer is explicitly approved. Do not put secrets or unnecessary personal/contact details in logs.
- No paid services, purchases, external lab outreach, physical treatments, destructive commands or large model downloads without appropriate approval.
- Follow Antigravity's actual permission model. Do not attempt to bypass approval prompts or security controls.

## Reporting
- State whether the output is empirical analysis, partial analysis, data-readiness only or blocked.
- Cite source rows/records, method and version for reported measurements. Label literature values, assumptions, hypotheses and simulated results distinctly.
- Include uncertainty, sample size, statistical assumptions, deviations, limitations, output hashes, and exact resume instructions.
