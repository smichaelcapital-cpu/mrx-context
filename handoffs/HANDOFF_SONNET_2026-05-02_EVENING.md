# HANDOFF — SONNET — 2026-05-02 EVENING

**For:** Fresh Sonnet, evening session (or tomorrow morning)
**From:** Sonnet (afternoon — pinned post-restraint-watch ship)
**Owner:** Scott
**Architect:** Opus (this afternoon's session, also tapping out clean)

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_RUNNING_2026-05-02.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_VALIDATION_HARNESS_SPEC.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_EDITORIAL_RESTRAINT_WATCH_SPEC.md
6. This handoff

After reading: confirm in ONE LINE state-of-world table and "Ramped from Sonnet handoff 2026-05-02 evening. Ready."

DO NOT skip CODER_MINDSET. Last two sessions ago it was the failure mode.

---

## STATE OF THE WORLD

**Engine repo (mrx_engine_v1):**
- Branch: main, clean
- HEAD: 4f22ea8 (feat: MB calibration harness v1 — pattern engine, bucket classifier, restraint watch)
- Tests: 565 passing, 0 failures
- Pushed: yes

**Context repo (mrx-context):**
- Branch: main, clean
- HEAD: latest with afternoon handoffs + 2 specs
- Pushed: yes

**Harness state:**
- 5 INDUSTRIAL modules under harness/:
  - pattern_engine.py (PE1–PE19)
  - bucket_classifier.py (BC1–BC6)
  - report_writer.py
  - run_harness.py
  - restraint_watch.py (RW1–RW7)
- harness/patterns/MB_PROFILE.yaml — 12 patterns seeded
- harness/watch/EDITORIAL_RESTRAINT_LOG.md — append-only, 2 entries logged

**Halprin mini OUR_FINAL.txt:**
- 89,398 bytes, mtime 2026-05-02 14:12 EDT
- Engine commit: 83d5199
- Warren Seal corrected, FIX-tagged

**Most recent harness report:**
- io/analysis/halprin_mini/harness_report_20260502_v3.md
- Headline: 11/21 trackable (52.4%) — RED
- 2 over-reach patterns logged in restraint watch

---

## WHAT SHIPPED TODAY

Morning (Sonnet AM):
- validate_ops V2.2 fix bundle (engine 22f083b)
- Hotfix: drop overlap-resolved proposals (engine 83d5199)
- Fresh Stage 3.1 + Stage 5 rerun ($0.94)
- Warren Seal end-to-end fix verified

Afternoon (Sonnet PM — me, now pinned):
- harness/ module set built from scratch — 5 INDUSTRIAL files
- 38 new tests, 527 → 565 passing
- MB_PROFILE.yaml seeded with 12 patterns
- IGNORECASE flag support added to pattern engine
- Editorial Restraint Watch built — RW1–RW7 tests, persistent log
- 3 harness reports generated (v1, v2, v3)

---

## EVENING SESSION TASK (Scott's call)

**MOVE A: NAMES_LOCK substring + WT_OFFSHORE short-form**

Opus drafts spec. You build. Two-part fix:

1. **NAMES_LOCK substring matching** — current exact-match exemption misses Writer phrasing like "for W&T Offshore." Need word-boundary substring match. Recovers 6 W&T MISS turns.

2. **WT_OFFSHORE contextual short-form** — engine over-expands "W&T" to "W&T Offshore" in 2 places where MB used short form. Need rule for when to apply full vs short form.

Touches: Writer prompt, validate_ops, possibly suggester. **Multi-file = RULE-SPEC-BEFORE-BUILD applies. Wait for spec from Opus before writing any code.**

After code ships: re-run harness on Halprin mini. Goal: confidence number jumps from 52.4% toward 75–80%.

---

## RULES TO INVOKE THIS SESSION

- RULE-RECON-FIRST — multi-file change, recon before build
- RULE-CONTRADICTION-HUNT — Writer prompt edits, grep for contradictions
- RULE-SILENT-FAILURE-CHECK — substring matching might silently match wrong entities, prove it doesn't
- RULE-INPUT-IS-SACRED — don't normalize MB's short forms into full forms
- RULE-SPEC-BEFORE-BUILD — wait for Opus spec, do not freelance

---

## SCOTT'S WORKING STYLE (REMINDER)

- Plain English, 12-year-old level
- Short answers, ONE question at a time
- Full absolute paths always
- NEVER make Scott copy-paste — write to repo, push, reply with URL
- NEVER go silent — ping when waiting, ping when complete

---

## TODAY'S PROCESS LESSONS

- **Silent waits are leaks.** Always status when complete, when waiting, when stalling.
- **Don't shortcut to skip cheap re-runs.** Mid-day proposal-filter shortcut corrupted file, cost $0.95 anyway.
- **Spec precision matters at low energy.** Two spec misses today (NAMES_LOCK exact-match, manual filter option). Both caught, both small. Pit-stop earlier next time.
- **Reverse-engineer rules from MB FINALs before asking MB.**

---

## CODER MINDSET CORE

Before any code change: **"Could this change reduce transcript accuracy or credibility?"** If yes or maybe → STOP, flag to Scott.

Three Brains: Engineer (can?), Architect (should?), Owner (worth?).

Slow is smooth. Smooth is fast.

— End of Sonnet 2026-05-02 evening handoff —
