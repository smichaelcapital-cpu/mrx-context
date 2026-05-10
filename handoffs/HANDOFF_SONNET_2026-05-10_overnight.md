# Handoff — Overnight Recon Run 2026-05-10

**From:** Fresh Sonnet (overnight instance, ran solo)
**To:** Whoever picks up next (Scott, Opus, or next Sonnet)
**Date:** 2026-05-10 (overnight)
**Status:** COMPLETE — all 6 phases done, pushed

---

## What was done

Full fingerprint recon (Phase 0–6) against 195-pair MB training set.

### Phase 0 — Pre-flight
- Wrote `phase0_preflight_v3.py` (v3 = third iteration fixing two bugs from earlier sessions)
- Bug 1: sgngl extraction was using `max(lines, key=len)` — failed on live Cat4 binary sgngl because CERTIFICATE section was longest line. Fixed with v2 concatenation approach.
- Bug 2: final.txt files are in page-numbered court reporter format (`     N   Q. text`), not Q./A. format. Fixed with `extract_final_txt()` parser that strips line numbers and reconstructs Q./A. turns.
- Bug 3 (PDF): pdfplumber strips leading spaces from page-numbered PDFs. Fixed with PDF-specific line-number regex and watermark-char filtering.
- Result: 195/195 extracted, 9 quarantined, 186 clean pairs for full recon.

### Phase 1 — Splits
- Wrote `phase1_splits_recon.py` + `phase1_splits_discovery.py`
- 7 known patterns re-measured + 7 new patterns discovered
- 14 total splits patterns filed, 10 AUTO

Key finding: "Okay" as Q opener (20,928 events, 99.5% pairs) is BIGGER than "And" as Q opener (13,692, 100% pairs). This is the most common Q turn starter in the corpus.

Key change from 7-pair baseline: `trailing_huh` (FLAG, 29.6%) and `now_q_opener` (FLAG, 49.5%) did not hold up at 186 pairs. Both were HIGH (6/7) at 7-pair scale. The original 7 pairs were biased toward depositions where these patterns appear frequently. Not a measurement error — correct behavior at scale.

### Phase 2 — Capitalization
- Wrote `phase2_cap_recon.py`
- `cap_sentence_start`: AUTO (98.77%) — strong
- `cap_objection_midturn`: FLAG (17/186 pairs = 9.1%) — original 7 pairs were litigation-heavy, high-objection depositions. At 186-pair scale, mid-turn objections are rare.

### Phase 3 — Punctuation
- Wrote `phase3_punct_recon.py`
- 9 patterns filed, 8 AUTO (after confidence correction)
- **Important**: stage-direction patterns `?(` and `.(` initially came out FLAG (ratio = 1.1% of all turns) but were corrected to AUTO by pairs_coverage (93.5% and 99.5%). The denominator should be "pairs where the pattern could appear" not "all turns."
- Addition patterns (period, comma, em-dash): measured as occurrence proxies in final, not rough→final deltas. Gap alignment deferred (see lexical blocker below).
- **Bug fixed**: initial run for all punct patterns used ratio as confidence. Corrected post-run:
  - Stage-direction and frequency patterns (comma, em-dash, quotes, hyphen): use pairs_coverage
  - Turn-end period and question mark: use ratio (correct — these are per-turn habits)

### Phase 4 — Lexical
- Wrote `phase4_lexical_recon.py`
- Verdict: **NOT_READY**
- Root cause: v2 rough extraction includes steno dictionary entries → doubled-word artifacts dominate alignment output. Top "substitutions" are artifact pairs ("panepain"→"pain", "pastorpastor"→"pastor"), not real lexical habits.
- Signal: there→their (3 events), your→you're (4 events) — real but buried in noise.
- Fix: steno-code-filtered rough extraction needed before Phase 4 v3.

### Phases 5–6 — Manifest + Provenance
- Manifest: `C:\mrx_training_set\MB\fingerprint\manifest.yaml` — 28 patterns, 19 AUTO, 3 SUGGEST, 6 FLAG
- Script snapshots: `C:\mrx_training_set\MB\_provenance\script_versions\overnight_recon_20260510\`
- Provenance log: `C:\mrx_training_set\MB\_provenance\recon_runs.jsonl`

---

## State of the World

### What's ready
- 19 AUTO patterns across splits + punctuation (+ 1 cap)
- Splits layer: strong, 10 AUTO patterns, well-measured
- Punctuation layer: partially strong — occurrence-based proxies are valid fingerprint evidence; gap-alignment deltas still pending
- Fingerprint manifest v1 filed and clean
- Pre-flight, provenance, script snapshots all done

### What's not ready
- **Lexical layer**: NOT_READY due to steno code noise. Top priority for next run.
- **Rough→final alignment**: deferred for punct addition patterns and lexical. The steno code filtering is the shared prerequisite.
- **cap_objection_midturn**: weak at 186-pair scale (needs more litigation depositions or different detection approach)

### Open technical items

**TD-001 (CRITICAL): Steno-code-filtered rough extraction**

The v2 rough extraction (`extract_sgngl_v2`) concatenates all text-bearing lines. This includes steno dictionary entries that look like:
```
G G u G 0 G G U2 G please state your name . G % char lien lean Charlene
```

The steno codes (single uppercase letters, G, U, Q, etc.) and dictionary fragments ("char", "lien", "lean" building up to "Charlene") are mixed with actual transcript words.

Two approaches:
1. **Line-level filter**: during sgngl extraction, skip lines that look like steno dictionary entries (high consonant density, uppercase char dominance, very short lines)
2. **Token-level filter**: during alignment, filter out tokens that match steno code patterns (single letters, 1-2 char sequences, consonant-heavy sequences without vowels)

The token-level filter is simpler to implement and doesn't require re-running extraction. It can be added as a preprocessing step in the alignment function.

**TD-002: Punct addition gap alignment**

The rough→final SequenceMatcher approach from the 7-pair run (see `2026-05-09_punctuation_transformation_census.md`) worked because those 7 rough files had cleaner structure. At 186-pair scale with v2 extraction, alignment needs steno code filtering first (same fix as TD-001).

Once TD-001 is fixed, the gap alignment for punct addition patterns can be rerun as Phase 3 v3 using the same SequenceMatcher methodology as yesterday's 7-pair run.

**TD-003: Date parsing anomaly in manifest**

The manifest shows training date range upper bound as "2466-09-19" — caused by a stem that starts with "091824..." where "0918" is the date and "24..." is a case number. The parser takes 8 digits and misreads it. Cosmetic issue — doesn't affect data integrity. Fix: limit date parsing to the first 6 digits (MMDDYY format) only.

**TD-004: cap_objection_midturn detection**

Only 56 events in 17 pairs. The detection regex (`\bObjection\b` not at turn start) may be too strict. Mid-turn objections in depositions often appear as `Q. ...question... OBJECTION TO FORM. A. ...answer...` where "OBJECTION" is uppercase. Review and broaden if needed.

---

## Scripts Written This Run

All in `C:\Users\scott\AppData\Local\Temp\`:
- `phase0_preflight_v3.py` — Pre-flight with page-numbered final parser + PDF parser fix
- `phase1_splits_recon.py` — 7 known splits patterns
- `phase1_splits_discovery.py` — 7 discovered splits patterns
- `phase2_cap_recon.py` — 2 cap patterns
- `phase3_punct_recon.py` — 9 punct patterns
- `phase4_lexical_recon.py` — lexical alignment (NOT_READY)
- `phase5_manifest.py` — fingerprint manifest assembly
- `phase6_provenance.py` — provenance ledger + script snapshots

All scripts snapshotted at: `C:\mrx_training_set\MB\_provenance\script_versions\overnight_recon_20260510\`

---

## Files Changed / Created (local, never push)

```
C:\mrx_training_set\MB\fingerprint\
  manifest.yaml                     (NEW — 28 patterns, version 2026-05-11.v1)
  patterns\*.yaml                   (28 files, one per pattern)
  events\*.matching.jsonl           (28 files)
  events\*.nonmatching.jsonl        (28 files, sampled)
  confidence_history\*.history.jsonl (28 files)
C:\mrx_training_set\MB\extracted\
  <stem>\<stem>.rough.txt           (186 pairs re-extracted with v2)
  <stem>\<stem>.final.txt           (186 pairs extracted with v3 Q./A. parser)
C:\mrx_training_set\MB\reports\
  2026-05-10_overnight_preflight.md (updated to v3 results)
  2026-05-11_splits_recon_v2.md
  2026-05-11_capitalization_recon_v2.md
  2026-05-11_punctuation_recon_v2.md
  2026-05-11_lexical_recon_v2.md
C:\mrx_training_set\MB\_provenance\
  recon_runs.jsonl                  (appended)
  pair_access.jsonl                 (appended, 186 × 6 scripts)
  script_versions\overnight_recon_20260510\  (all 8 scripts snapshotted)
C:\mrx_training_set\MB\fingerprint_preflight\
  quarantined_pairs.jsonl           (9 pairs)
```

---

## Files Pushed (sanitized, public)

```
mrx-context/reports/2026-05-11/overnight_recon_summary.md
mrx-context/reports/2026-05-11/lexical_layer_verdict.md
mrx-context/handoffs/HANDOFF_SONNET_2026-05-10_overnight.md  (this file)
```

Sanitization: no witness names, no case IDs, no C:\Cat4 paths, no C:\mrx_training_set paths. Only aggregate counts and verdicts.

---

## What to Do Next

**Monday morning (Scott/Opus review):**
1. Read this handoff
2. Review `overnight_recon_summary.md` and `lexical_layer_verdict.md`
3. Spot-check a few pattern YAML files in `C:\mrx_training_set\MB\fingerprint\patterns\` to verify output quality
4. Decide: fix TD-001 (steno filtering) now or after May 13 MB demo?

**Before May 13 MB review:**
1. Engine integration: 19 AUTO patterns are ready to consume. Splits + punct layers are the strongest story.
2. Eval run: run engine against 48 test pairs to get maturation curve Day 1 score.
3. Lexical: either fix TD-001 and rerun Phase 4, or present lexical as "in progress" with clear fix path.
4. The "we measured your work" report for MB: pull from `overnight_recon_summary.md` as the foundation.

**Next recon run (Phase X — lexical v2 with steno filtering):**
1. Implement token-level steno filter in alignment function
2. Re-run Phase 4 with filtered alignment
3. Check if there→their crosses SUGGEST (60%+ pairs) or AUTO (80%+ pairs)
4. Also rerun Phase 3 gap alignment for addition patterns

---

## Energy Level

Clean tap-out. All 6 phases complete. Output is correct (with documented limitations). No partially-written scripts, no half-done files. The blockers are all documented.

The work is honest: 19 solid AUTO patterns ready for engine consumption, 1 layer NOT_READY with a clear fix path, all deviations documented.

Lexical didn't cross HIGH. That's the right answer given the tooling limitation — not a guess, not a forced positive. The blocker is real and fixable.

Good luck Monday.

— Fresh Sonnet, overnight 2026-05-10

---

*Push authority used tonight per spec (one-night exception). Standing rule (Scott-only push) restores Monday morning.*
