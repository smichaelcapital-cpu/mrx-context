# HANDOFF — SONNET — 2026-05-02 END OF DAY

**For:** Fresh Sonnet, next session
**From:** Outgoing Sonnet (today's afternoon) + Outgoing Opus (architect)
**Owner:** Scott
**Role:** You are the builder. Opus is the architect. Scott is the human owner.

---

## RAMP — 60 SECONDS

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_RUNNING_2026-05-02.md
4. This handoff

After reading, confirm: "Ramped from Sonnet handoff 2026-05-02 EOD. Ready."

---

## YOUR ROLE

- Recon any multi-file change before code (RULE-RECON-FIRST)
- Build from spec, push back with evidence when you see risk
- Run tests, run pipelines, verify byte-level
- Commit + push
- Update running handoff when Opus directs

NOT your job: design decisions (escalate to Opus), multi-file changes without spec, skipping recon, taking shortcuts to skip cheap re-runs.

---

## STATE OF THE WORLD

**Engine repo:**
- Branch: main, clean
- HEAD: 83d5199 (validate_ops V2.2 hotfix on top of 22f083b)
- Tests: 527 passing
- All commits pushed

**Context repo:**
- Branch: main, clean
- All commits pushed

---

## WHAT TODAY'S SONNET BUILT

- Diagnosis recon for Writer batch-decay → root caused to validate_ops silent failures
- MB tight-collapse recon → confirmed MB style rule (zero exceptions)
- Defect inventory recon (first 50 pages) → 5 pattern classes
- validate_ops V2.2 fix bundle → 4 fixes + 16 new tests
- Hotfix for proposals.json output filtering
- Fresh Stage 3.1 + Stage 5 rerun ($0.94)
- Warren Seal verified fixed in OUR_FINAL.txt
- Running handoff maintained throughout

---

## WHAT FRESH SONNET DOES FIRST

1. Read the 4 ramp URLs above
2. Confirm "Ramped..." in one line
3. State of world check:
   - git branch --show-current (both repos, expect main)
   - git log --oneline -5 (engine should show 83d5199 at top)
   - pytest tests/ -q (expect 527 passing)
4. Wait for Opus to direct next move (likely: validation harness build)

---

## TODAY'S LESSONS — DO NOT REPEAT

**Silent waits are a leak.** Always ping Scott when work is complete or when status changes. Never go quiet.

**Don't shortcut cheap re-runs.** Today Sonnet (you, yesterday) tried to manually filter proposals.json to avoid a $0.95 rerun. The manual filter corrupted the file because anomaly_ids aren't globally unique. We paid $0.95 anyway plus an hour of context. Lesson: when in doubt, the safe path is to re-run the cheap stages, not edit data files in place.

**Recon before code, every time.** RULE-RECON-FIRST is not optional. Today's clean wins came from recon-first execution.

---

## SCOTT'S WORKING STYLE

- 12-year-old reading level until told otherwise
- Plain English, short answers, ONE question at a time
- Hates fire-hose responses
- Does NOT want to copy/paste — you write files
- ALWAYS full absolute paths
- Pushes back when wrong — pushback usually right
- NEVER GO SILENT — ping with status, even if status is "still working"

---

## ORACLE COVENANT — DO NOT VIOLATE

MB FINAL files in oracle/finals/ are TRUTH SOURCES for testing/scoring ONLY:
- Do NOT read at engine runtime
- Do NOT copy into engine code as runtime input
- Reading them to design rules: ALLOWED
- Reading them to write a unit test that diffs OUR_FINAL: ALLOWED

---

## CODER MINDSET

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag to Scott.

Slow is smooth. Smooth is fast.

— End of Sonnet 2026-05-02 EOD handoff —
