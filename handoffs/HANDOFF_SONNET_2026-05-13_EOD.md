# HANDOFF — SONNET — 2026-05-13 EOD

**For:** Fresh Sonnet, 2026-05-14 session
**From:** Sonnet (current session, parked mid-spin on appearances fix)
**Owner:** Scott
**Architect:** Opus (handoff at `handoffs/HANDOFF_OPUS_2026-05-13_EOD.md`)

---

## STANDING RULES

1. 12-year-old reading level. Plain English. Short answers.
2. ONE question at a time.
3. Always full absolute paths.
4. SHAPE MATCH ONLY. Never byte-match a hand-typed fixture.
5. 5-line answers.
6. Before any code change ask: "Could this reduce transcript accuracy or credibility?" If yes/maybe, STOP and flag Scott.
7. Sonnet writes files and runs shell. Scott pushes commits when asked. Opus writes specs.
8. 30-minute wall on any build pass. If you hit it without a green test, STOP and regroup.

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-13_EOD.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-13_APPEARANCES_OVERFLOW_AND_BACK_MATTER_SPACING.md
6. This handoff in full

After ramp: confirm "Ramped Sonnet 2026-05-14. Ready." plus one sentence on state and one question for Scott.

---

## ONE-LINE STATE

Yesterday's Sonnet parked mid-spin on the appearances overflow fix (24+ minutes silent thinking with no checkpoint). Branch `fix/appearances-overflow-and-back-matter-spacing` exists with whatever state he left. Main is CLEAN and now has the recovered orchestrator + overflow-capable index.py from commit 1765b1c (merged via `a5e1628`).

---

## CRITICAL — WHAT HAPPENED YESTERDAY

The morning's branch cleanup deleted `front-matter/index` thinking it was merged. It wasn't fully merged — orchestrator.py and overflow-capable index.py were lost. Backup branch saved us. Recovered via sparse checkout from commit 1765b1c, merged to main.

**Main is now correct.** All 8 front matter modules present:
- cover.py, errata.py, index.py (overflow version), orchestrator.py, reporter_cert.py, stipulation.py, witness_cert.py, __init__.py

Recovery branch `recover/orchestrator-from-1765b1c` left intact on origin as safety net. Do not delete.

---

## YESTERDAY'S WIN

Recovery is byte-identical to yesterday's verified Halprin render (modulo CRLF and a manual debug label). 1,146 tests pass. 2 pre-existing failures unchanged (test_williams_byte_match, test_E2E3_wt_has_misses).

---

## TONIGHT'S UNFINISHED WORK

The appearances overflow fix is incomplete. Three issues from Scott's eyeball pass:

1. **KEEP-TOGETHER** — defendant blocks split mid-block across page break, orphaning addresses.
2. **Reported by: anchor** — needs to land at line 19 on final appearances page.
3. **ALSO PRESENT: position** — needs to land at line 13. May auto-resolve from Issue 1.

Spec is at `specs/2026-05-13_APPEARANCES_OVERFLOW_AND_BACK_MATTER_SPACING.md`. Scott signed off all 3 open questions yesterday.

Sonnet completed recon. Diagnosis was sound. Build went sideways.

**Lesson learned: 3 fixes in one pass was too much. Restart with tight scope.**

---

## TOMORROW'S FIRST MOVES (in order)

### Move 1 — Verify state
From C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\:

git branch -a
git status
git log main --oneline -10

Report all 3 outputs.

### Move 2 — Inspect what previous Sonnet left on the fix branch
git checkout fix/appearances-overflow-and-back-matter-spacing
git status
git diff main..fix/appearances-overflow-and-back-matter-spacing

If there's usable work — report what's there.
If the branch is clean or only has spin debris — delete the branch, start fresh.

### Move 3 — Recommendation to Opus
Based on Move 2, recommend either:
- A. Salvage what's on the branch and continue
- B. Delete branch, start fresh on a new branch off main

### Move 4 — Wait for Opus green light, then build ONE FIX AT A TIME

The spec covers 3 issues. **Do them one at a time. Branch per issue.**

- Pass 1: Issue 1 only (KEEP-TOGETHER). One test. Ship.
- Pass 2: Issue 2 (Reported by anchor). One test. Ship.
- Pass 3: Issue 3 (ALSO PRESENT) only if not auto-resolved.

30-minute wall on each pass. Hard stop if you hit it.

---

## KEY PATHS

- Engine root: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
- Front matter renderers: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\front_matter\
- Tests: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\stage5\
- Halprin JSON: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\profiles\mb\data\front_matter\halprin\
- Halprin FINAL (oracle): C:\Users\scott\OneDrive\Documents\mrx-context\io\halprin_FINAL_compare_2026-05-12.txt (20,834 bytes normalized)
- Yesterday's render: C:\Users\scott\OneDrive\Documents\mrx-context\io\halprin_full_render_2026-05-12.txt (21,705 raw / 20,834 normalized)
- Backup: C:\Users\scott\OneDrive\Documents\mrx-context\io\halprin_full_render_2026-05-12.BACKUP.txt
- Context repo: C:\Users\scott\OneDrive\Documents\mrx-context\
- Ledger: C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\ledger.md (18 rows)

---

## TOMORROW'S BIGGER PICTURE — AUDIO DESIGN

After appearances fix lands, Scott wants to design the audio component with fresh Opus. The 5-stage stack (A-E) is already locked from 5/3:
- Stage A: Aligner+Differ
- Stage B: Whisper integration
- Stage C: Comprehension Agent + Case Brief
- Stage D: Brief-aware defect-finder
- Stage E: Resident Oracle fallback

Scott wants Opus to walk him through the stack (it's a REVIEW, not a redesign), capture his questions, then split the work into TWO parallel Sonnet workstreams. Tomorrow will likely involve two-Sonnet parallel grinding — be ready for branch-per-task discipline.

---

## CODER MINDSET REMINDERS

- Recon before build (RULE-RECON-FIRST)
- 30-min wall (yesterday's silent thinking was the failure mode)
- Backup before any branch cleanup (today's near-miss proved its value)
- Three small ships beat one big spin

— End of Sonnet 2026-05-13 EOD handoff —
