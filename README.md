# mrx-context

Shared canonical docs and session handoffs for MyReporterX.

This repo is read by Claude Opus (Claude Chat) at session start via web_fetch.
It is read AND written by Claude Code (Sonnet) at session start and end.

## Files

- `ARCHITECTURE_DECISIONS.md` — every architectural decision made on the engine, with date and rationale
- `CODER_MINDSET.md` — base coder mindset (the "who you are this session")
- `CODER_MINDSET_ADDENDUM.md` — MyReporterX-specific rules (named, blood-written from real failures)
- `ONBOARDING_REQUIREMENTS.md` — what MyReporterX asks every new CR for at signup
- `ORACLE_COVENANT.md` — data integrity rule for FINAL files
- `CURRENT.md` — pointer to the latest Opus and Sonnet handoffs
- `handoffs/` — every session-end HANDOFF doc, never overwritten

## Naming convention

Handoffs follow: HANDOFF_<role>_<YYYY-MM-DD>_<HHMM>(am|pm).md

Sortable alphabetically = chronological. Multiple handoffs per day are fine.

## What is NOT in this repo

- Engine source code (lives in mrx_engine_v1)
- Customer data (Oracle Covenant — never leaves customer's local environment)
- Secrets, API keys, credentials
- Anything that should be private
