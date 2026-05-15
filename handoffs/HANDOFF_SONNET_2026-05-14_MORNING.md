# HANDOFF — SONNET — 2026-05-13 EOD (LATE NIGHT)

**For:** Fresh Sonnet, 2026-05-14 morning session
**From:** Sonnet #1 (current session, signed off ~10:30 PM EDT after long build day)
**Owner:** Scott
**Architect:** Opus (handoff at handoffs/HANDOFF_OPUS_2026-05-13_EOD_LATE.md)

---

## STANDING RULES

1. 12-year-old reading level. Plain English. Short answers.
2. ONE question at a time.
3. Always full absolute paths.
4. SHAPE MATCH ONLY. Never byte-match a hand-typed fixture.
5. 5-line answers.
6. Before any code change ask: "Could this reduce transcript accuracy or credibility?" If yes/maybe, STOP and flag Scott.
7. Sonnet writes files and runs shell. Scott pushes commits when asked. Opus writes specs.
8. 30-minute wall on any build pass. Backup branch before any cleanup. One fix per branch.
9. Silent thinking past the wall is the failure mode. If you cannot show progress every 5-10 min, STOP and report.

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-13_EOD_LATE.md (or _v2 if that path was used)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-13_STAGE_A_ALIGNER_DIFFER.md
6. This handoff in full

After ramp: confirm "Ramped Sonnet 2026-05-14. Ready." plus one sentence on state and one question for Scott.

---

## ONE-LINE STATE

Stage A v0 code is 95% built on branch feature/stage-a-aligner-differ-v0 (8 untracked files). 6 modules complete, 7 unit tests green. Two small fixes queued for tomorrow morning before the first real frequency table can be generated.

---

## WHAT SHIPPED YESTERDAY (2026-05-13)

Front page appearances fix landed on main in two passes:
- Pass 1 (KEEP-TOGETHER) — commit 5280ef9, merged at f0c2de2
- Pass 2 (Reported by anchor line 19) — merged at 95f09ee
- Issue 3 (ALSO PRESENT line 13) auto-resolved by Pass 1, as spec predicted
- 473 tests green, 1 pre-existing fail (test_williams_byte_match — unchanged)

Main is now at 95f09ee. Halprin renders end-to-end with no orphaned address blocks.

---

## WHAT'S PARKED ON THE STAGE A BRANCH

Branch: feature/stage-a-aligner-differ-v0 (8 untracked files, no commits yet)
Backup branch: backup/pre-stage-a-2026-05-13 (off main at 95f09ee — DO NOT DELETE)

Files built (all uncommitted, all unit-tested):
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\__init__.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\normalize.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\tokenize.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\align.py <- NEEDS CHUNKING FIX
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\diff.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\categorize.py <- NEEDS U+2011 FIX
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\frequency.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\run_stage_a.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\aligner_differ\test_aligner_differ.py

Unit test results (7/7 passing in 0.08s):
- test_normalize_strips_rtf — PASS
- test_tokenize_words — PASS
- test_align_simple — PASS
- test_categorize_em_dash_insert — PASS
- test_categorize_capitalization — PASS
- test_frequency_rollup — PASS
- test_full_pipeline_halprin_only — passed structurally but ran SLOW (13 min align on full Halprin)

---

## YESTERDAY'S NEAR-MISSES

1. **First KEEP-TOGETHER attempt overshot** — counted full 2-row blank after every firm block. Should be 0 rows when the last content row leaves its sub-row empty. Caught by failing tests. Rolled back. Re-shipped clean.
2. **diff-match-patch choked on full Halprin** — 100k+ tokens RAW vs 133k FINAL. Took 13 min. Will not scale to 4 pairs let alone 20.
3. **Silent-thought past 10-min ceiling twice tonight.** Opus issued hard-stops both times. The 30-min wall held. Branch intact.

---

## TOMORROW'S FIRST MOVES (in order)

### Move 1 — Verify state

From C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\:
- git checkout main
- git pull origin main -> should be at 95f09ee
- pytest tests/stage5/ -> confirm 473 pass, 1 pre-existing fail
- git checkout feature/stage-a-aligner-differ-v0
- git status -> should show 8 untracked files
- pytest tests/aligner_differ/ -> confirm 7 unit tests green

Report state. Wait for Opus go-build.

### Move 2 — Fix #1 — 500-token chunking in align.py

Problem: align.py runs diff-match-patch on full normalized documents. Halprin (100k/133k tokens) took 13 min. Won't scale.

Fix: chunk both RAW and FINAL token streams into 500-token windows BEFORE calling diff_main. Pair windows by index (RAW chunk 0 vs FINAL chunk 0, RAW chunk 1 vs FINAL chunk 1, etc.). Run diff_main on each pair independently. Concatenate the per-chunk op streams back into one flat stream that diff.py and categorize.py can consume unchanged.

Tradeoff Scott accepted last night: ~1% of edits that span chunk boundaries will be missed or mis-attributed. For a statistical fingerprint, irrelevant. Document the limitation in a comment at the top of align.py.

One new test: test_align_chunked_halprin
- Runs align on Halprin in under 60 seconds
- Produces > 40,000 diff events (the slow run produced 47,089 — sanity check baseline)

### Move 3 — Fix #2 — U+2011 detection in categorize.py

Problem: RAW uses U+2011 (non-breaking hyphen) PAIRS where FINAL converts to either ASCII "--" or U+2014. The current em_dash_inserted / em_dash_removed detection only looks at "--" and U+2014, so every U+2011 em-dash edit lands in `other` instead of `em_dash_*`.

Fix: add U+2011 single and U+2011+U+2011 pair to the em-dash token set in categorize.py. Two lines of code.

One new test: test_categorize_em_dash_u2011
- Insert of "\u2011\u2011" lands in em_dash_inserted bucket

### Move 4 — Full pipeline run

After both fixes green:
1. Run run_stage_a.py on all 4 pairs (Halprin, Easley, Brandl, Church — see Stage A spec for exact paths)
2. Confirm two JSON files written to C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\
   - mb_frequency_summary.json (top patterns sorted by pct_of_depos)
   - mb_evidence_raw.json (every diff event for audit)
3. Report: total diff event count, top 20 patterns
4. **DO NOT COMMIT.** Scott eyeballs first.

30-min wall on each move. Report progress at every checkpoint.

---

## KEY DATA POINTS FROM YESTERDAY

- Halprin RAW: 1.7 MB .rtf, 4,030 lines, 243k chars after RTF strip, ~100k tokens after tokenization
- Halprin FINAL: 397 KB .txt, 25-line numbered pages with form feeds, ~133k tokens
- RAW and FINAL share NO coordinate system (RAW has no line numbers, no page breaks)
- Slow run produced 47,089 diff events on Halprin alone (sanity baseline)
- RAW em-dashes are U+2011, NOT ASCII -- or U+2014 (mystery solved during recon)

---

## KEY PATHS

- Engine root: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
- Stage A code: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\
- Stage A tests: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\aligner_differ\
- Stage A output: C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\
- Stage A spec: C:\Users\scott\OneDrive\Documents\mrx-context\specs\2026-05-13_STAGE_A_ALIGNER_DIFFER.md
- Context repo: C:\Users\scott\OneDrive\Documents\mrx-context\
- Depo library: C:\Users\scott\OneDrive\Documents\mrx_depo_library\
- Staging folder: C:\Users\scott\OneDrive\Documents\mrx_depo_library\_staging_for_export_2026-05-13\ (20 .sgxml ready for manual CATalyst export when Scott chooses)

---

## CODER MINDSET REMINDERS

- Recon before build (RULE-RECON-FIRST)
- 30-min wall is HARD. Silent thinking is the failure mode.
- Backup before any cleanup
- Three small ships beat one big spin
- Print statements at every pipeline stage so progress is visible

---

## THE NORTH STAR

Stage A's whole job is to produce frequency counts of MB's habits. Deterministic. No AI in the diff loop. The product belief Scott locked yesterday:

> "If MB does it 97 out of 100 times, on depo #101 the engine should do it for her."

Stage A is the data factory. The fingerprint is the brain. Don't overthink it.

— End of Sonnet 2026-05-13 EOD late night handoff —
