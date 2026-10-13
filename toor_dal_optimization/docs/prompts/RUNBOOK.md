# Harakutir Prompt Pack — Runbook

## Files
- `HARAKUTIR_MASTER_PROMPT.txt`: the one-shot master prompt to paste into Antigravity.
- `PROMPT_RESUME.txt`: use after an IDE restart, terminal interruption or a long-run continuation.
- `PROMPT_INGEST_NEW_LAB_DATA.txt`: use when actual laboratory data arrive.
- `PROMPT_DREAM_RSI_CYCLE.txt`: use to run one bounded adaptive exploration/replay cycle.
- `PROMPT_RED_TEAM_AUDIT.txt`: independent scientific/software audit.
- `PROMPT_PHASE2_OED.txt`: preliminary Phase 2 experiment design only; not authorization to perform physical tests.
- `PROMPT_REPORT_RELEASE.txt`: compile and validate an evidence-backed report.
- `AGENTS.md`: persistent workspace rules.
- `.agents/workflows/*.md`: short repeatable workflows, when supported by the installed Antigravity version.

## First run
1. Extract the pack into the intended project workspace (or copy `AGENTS.md` and workflow files into the existing repository). Preserve existing files and inspect diffs before accepting changes.
2. Put `Phase1_Scope_of_Work_Toor_Dal.docx` in the project workspace if the agent must read it locally. Put actual lab measurements in a clearly named input folder; do not mix mock/test files with actual data.
3. Open the project root in Antigravity and paste the complete contents of `HARAKUTIR_MASTER_PROMPT.txt` into the agent chat. Allow the agent to inspect, implement and test the system within the existing tool permission configuration.
4. The agent should create a local supervisor (`run.ps1`/Python entrypoint) so computation is not tied to the lifetime of the chat context. Inspect its budget/config before starting a multi-day run.
5. To continue later, start the supervisor with its documented `--resume`/PowerShell option and use `PROMPT_RESUME.txt` in the IDE if code-level orchestration help is needed.

## Important limits
- Graceful Ctrl+C can trigger a save, but no application can execute a shutdown save after sudden power loss. Frequent atomic checkpoints limit lost work.
- Dream-RSI replay can evaluate alternative policies over recorded histories; it cannot invent the outcomes of unperformed food-science experiments. Verify the official code release before calling any local integration official Dream-RSI.
- No real analytical dataset was included with the scope document alone. Unless additional measurement files are supplied, the correct result is a data-readiness/protocol system, not a scientific root-cause conclusion.
- A 72-hour budget is a ceiling for useful work, not a requirement to consume all time or GPU capacity.
