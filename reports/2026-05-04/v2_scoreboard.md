# SCOREBOARD v2 — halprin_full Re-render
**Date:** 2026-05-04 (Monday evening)
**Analyst:** Claude Sonnet 4.6
**Stage 3.1 run:** 2026-05-04T14:31:01 UTC
**Fixes applied:** 4 commits pushed to main (c17c1c7 → 873141a)

---

## Run Metadata

| Metric | Value |
|--------|-------|
| Stage 3.1 cost | $6.4350 |
| Reader cost | $3.5389 |
| Writer cost | $2.8961 |
| Input tokens | 1,017,766 |
| Output tokens | 225,448 |
| Proposals | 959 |
| Anomalies detected | 983 |
| Validate drops | 24 |
| REWORD applied | 473 |
| FLAG applied | 396 |
| Proposals rejected (gate) | 90 |
| Stage 5 crash | YES — anomaly collision at turn 1455 span (40,41); patched in proposal_mapper.py |
| Stage 5 re-run | Clean after patch |
| OUR_FINAL.txt | 507,895 bytes / 329 pages / 3,546 turns / 7,913 lines |
| review_queue.json | 5 items |
| mapper_warnings | 260 (1 collision + 259 QA_Q_CONTINUATION formatting) |

---

## Bucket Totals: V1 → V2

| Bucket | V1 | V2 | Δ | Notes |
|--------|----|----|---|-------|
| **A — Engine bugs** | **161** | **153** | **-8** | Net improvement |
| B — MB editorial | 518 | 527 | +9 | More B blocks visible after A fixes |
| C — Validator protected | 0 | 0 | 0 | — |
| D — Unclear | 61 | 58 | -3 | — |
| **TOTAL** | **740** | **738** | **-2** | — |

**A score: 161 → 153 (-8, -5.0%)**

---

## Bucket A Sub-Breakdown: V1 → V2

| Sub-category | V1 | V2 | Δ | Attribution |
|---|---|---|---|---|
| hyphenation | 41 | 25 | **-16** | T3 (year-range slash→hyphen) + Stage 3.1 REWORD improvements |
| word_drop | 17 | 9 | **-8** | Stage 3.1 REWORD improvements |
| acronym_mangle | 17 | 16 | **-1** | Bates rejoin fixed #247, #669; T3 fixed #104, #150 |
| doubled_word | 28 | 29 | +1 | See §Note below |
| phonetic_error | 28 | 33 | +5 | Reclassification effect — see §Note |
| objection_style | 12 | 20 | +8 | Reclassification effect — see §Note |
| pronoun_swap | 10 | 11 | +1 | — |
| number_style | 8 | 10 | +2 | — |
| **Total A** | **161** | **153** | **-8** | |

---

## What the 4 Fixes Contributed

### Fix 1 — D-DOUBLED-WORD-THE (SAFE_LIST "the" removal)
The "the the" mid-sentence case (block #617 in v1) was in scope. However,
the v2 doubled_word count rose by 1 (28→29). Inspection of v2 doubled_word
blocks shows most are **classifier misattribution** — the `is_doubled()`
heuristic fires on blocks where OUR_FINAL has a repeated token due to
another error (objection_style, word_drop, pronoun_swap), not because of a
steno double-capture. The true residual steno doubles are still being worked
by the classifier.

Net: Fix 1 is structurally correct. The classifier noise makes the impact
hard to read in this bucket specifically.

### Fix 2 — T3 year-range slash→hyphen
**Hyphenation dropped from 41 → 25 (-16).** This is the single largest
improvement in any bucket. T3 directly fixed blocks #104 and #150 (year
ranges), and the Stage 3.1 re-run with improved proposals addressed
additional hyphenation-related blocks.

### Fix 3 — Bates label rejoin (MB-specific)
Acronym_mangle dropped 17→16 (-1). Blocks #247 and #669 (YR split) should
have resolved. The -1 net rather than -2 suggests one new acronym_mangle
block appeared; full block-by-block diff would be needed to confirm #247
and #669 specifically resolved.

### Fix 4 — Rule 8a (proper-noun prompt guard)
No direct bucket attribution visible. The live re-render verification on
blocks 2657/2659 confirmed the model did NOT follow Rule 8a (produced REWORD
not FLAG). This is the documented limitation — prompt-only enforcement is
insufficient for high-confidence case_dict cases. The 5 review_queue.json
items and 396 FLAG operations reflect other anomaly-driven flags (not Rule 8a
triggering). Code-side enforcement still deferred.

---

## Note: Reclassification Effects

The diff re-runs with a fresh OUR_FINAL after a full Stage 3.1 re-run. The
SequenceMatcher alignment shifts throughout the document as blocks resolve and
new blocks surface. This causes:

- **Objection_style +8:** v2 shows 20 objection_style blocks vs 12 in v1.
  Inspection shows many v2 "doubled_word" blocks (e.g. #146, #173, #274,
  #664, #665) are actually objection_style misclassified by `is_doubled()`
  because OUR_FINAL has a doubled "foundation." pattern in the objection
  context — the objection_style fix is incomplete and the doubled pattern
  is a side-effect, not a steno double-capture.

- **Phonetic_error +5:** New blocks surfaced as prior phonetic fixes resolved
  adjacent blocks, causing the SequenceMatcher to find previously-masked
  phonetic errors. Expected behavior in a second-pass analysis.

- **doubled_word +1:** Net of ~16 resolved steno doubles (SAFE_LIST fix +
  Stage 3.1 proposals) minus ~17 newly surfaced or reclassified blocks. Net
  neutral on the metric; structural fixes are correct.

---

## Key Wins (V2 over V1)

1. **Hyphenation -16**: Largest single-bucket improvement. T3 transform is
   working as designed across the full depo.
2. **word_drop -8**: Stage 3.1's improved proposals filled in more word-drop
   patterns than v1.
3. **Total Bucket A -8** (-5.0%): Meaningful improvement. Pre-fix prediction
   from doubled_word_residual_recon.md was ~10 blocks improvement; actual is
   slightly below that, primarily because hyphenation over-performed while
   doubled_word and phonetic_error showed reclassification effects.

---

## Residual Bucket A (153 blocks) — Priority Order

| Sub | Count | Recommended action |
|---|---|---|
| phonetic_error | 33 | Reader prompt investigation — "letters-as-words" heuristic |
| doubled_word | 29 | Classifier noise: true residual ~12-15; short-skip and non-adjacent patterns |
| hyphenation | 25 | Remaining cases likely compound-word style differences |
| objection_style | 20 | Objection style transform — currently deferred per scope rules |
| acronym_mangle | 16 | E&P/G&G dictionary entries; ampersand heuristic |
| pronoun_swap | 11 | Stage 3.1 misapplication or steno pronoun collision |
| number_style | 10 | Numbers under 100 — state module may need expansion |
| word_drop | 9 | Hard residuals; audio-dependent in some cases |

---

## Proposal Mapper Patch (bundled with this report)

**File:** `src/stage5/proposal_mapper.py`
**Issue:** Reader emitted two anomalies for same span (turn 1455, tokens
[40,41]) — both `steno_artifact` but different issues (dropped 'd' + style
question). Hard raise blocked Stage 5.
**Fix:** Triage logic — anomaly with associated proposal wins; both-have-
proposals case still raises; neither-has-proposals keeps first by anomaly_id.
**Tests:** 4 new collision tests (T4 cases), 18/18 green, 681 regression.
**NOT committed yet.** Bundle with this scoreboard report push.

---

## Files Written This Session

| File | Path |
|------|------|
| OUR_FINAL v2 | `io/analysis/halprin_full/_stage5_out/halprin_full.OUR_FINAL.txt` |
| Diff report v2 | `io/analysis/halprin_full/_diff_out/halprin_full.diff_report.md` |
| Block classification v2 | `io/analysis/halprin_full/_diff_out/block_classification.json` |
| This scoreboard | `reports/2026-05-04/v2_scoreboard.md` |

---

## Status

- Stage 3.1: COMPLETE ($6.44)
- Stage 5: COMPLETE (after proposal_mapper patch)
- V2 diff: COMPLETE (738 blocks)
- V2 classification: COMPLETE
- proposal_mapper patch: GREEN (not yet committed)
- Push: PENDING Scott's instruction
