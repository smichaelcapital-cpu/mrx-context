# SPEC: Doubled-Word Deduplication (D-DOUBLED-WORD)

Date: 2026-05-03
Author: Opus
Builder: Sonnet
Status: APPROVED for build

## Rule sheet header
- Universal? YES — applies to every court reporter forever
- Code or prompt? CODE — deterministic, no judgment needed
- File location: src/transforms/ (universal core)
- Commit prefix: universal:

## Problem
Frequency report (2026-05-03) shows 101 of 742 diff blocks have OUR_FINAL emitting
the same word twice consecutively where MB has it once. Examples:
  Block #4:  "oil -- oil barrels barrels"  (MB: "oil -- oil barrels")
  Block #75: "pretty pretty good"            (MB: "pretty good")
  Block #68: "Mr. Mr. Love"                  (MB: "Mr. Love")

These are pure engine bugs. No reporter wants doubled words.

## Goal
Add a deterministic post-processing step that detects and removes consecutive
duplicate words. Drop the doubled_word count from 101 → near 0.

## Approach: dedupe_consecutive_duplicates() — new function

Add to: src/transforms/post_process.py (NEW file if it doesn't exist,
otherwise add to existing post-processor).

Called from: apply_ops.py, AFTER all proposals are applied, BEFORE Stage 5
formatting receives the corrected_turns.

## Algorithm

For each turn's text:
1. Tokenize into words (preserve punctuation as part of adjacent word)
2. Walk token list with two-pointer comparison
3. If tokens[i].lower().strip(punctuation) == tokens[i+1].lower().strip(punctuation):
   - SAFE-LIST CHECK: skip dedup if the doubled word is in {"had", "that", "is", "the"}
     AND surrounding context suggests legitimate grammar
     (e.g., "I think that that is..." — legitimate; "Mr. Mr. Love" — not)
   - For v1: only auto-dedupe if word length >= 3 AND word is NOT in safe-list
   - Safe-list cases get FLAGGED (logged to rejections.jsonl with reason
     "doubled_word_safelist_skip"), not auto-deduped
4. When deduping: keep the first occurrence, drop the second, log the change
   to a new file: io/analysis/<depo>/_post_process_log.jsonl

## What gets logged

Every dedupe writes:
{
  "turn_idx": 124,
  "rule": "dedupe_consecutive_duplicates",
  "before": "Mr. Mr. Love",
  "after": "Mr. Love",
  "position": 0,
  "confidence": "high"
}

This satisfies RULE-PROOF-OF-WORK — no silent changes.

## Edge cases (specified)

1. Punctuation between: "X. X" → still doubled (period is just sentence boundary)
2. Different case: "The the" → still doubled (case-insensitive compare)
3. Possessives: "John's John's" → doubled (compare lemma after stripping 's)
4. Hyphenated: "back-and-back-and-forth" → not in scope (not consecutive tokens)
5. Three+ in a row: "very very very" → dedupe to "very" (one pass removes all)
6. Across sentence boundaries: "...end. End of..." → DO NOT dedupe (sentence end is significant)

## Tests required

File: tests/transforms/test_dedupe_consecutive_duplicates.py

Required test cases:
- T1: Simple double ("expenditures expenditures" → "expenditures")
- T2: Title double ("Mr. Mr. Love" → "Mr. Love")
- T3: Three in a row ("very very very good" → "very good")
- T4: Case insensitive ("The the table" → "The table")
- T5: Safe-list skip ("I think that that is" → unchanged, FLAGGED to log)
- T6: Sentence boundary ("end. End of" → unchanged)
- T7: Short word skip ("I I went" → unchanged, length < 3)
- T8: Possessive ("John's John's" → "John's")
- T9: Empty string → no error
- T10: Single word → no error
- T11: Verify post_process_log.jsonl gets written for every dedupe
- T12: Regression: run on 5 known doubled_word blocks from frequency report,
       confirm all 5 are correctly deduped

## Acceptance criteria

- [ ] All 12 tests pass
- [ ] Existing 582 engine tests still pass (regression)
- [ ] Run on halprin_full corrected_turns.json → re-render Stage 5 →
      diff again → doubled_word count drops from 101 to <= 5
- [ ] post_process_log.jsonl exists with N entries (N ≈ 96+)
- [ ] Total diff block count drops by ~95+ (from 742 toward ~647)
- [ ] No regression in OTHER categories (em_dash, quotes, etc. counts unchanged ±5)

## Prime Directive check

"Could this reduce transcript accuracy or credibility?"
Edge case worry: legitimate "had had" or "that that" gets incorrectly deduped.
Mitigation: safe-list skip + FLAG instead of auto-dedupe for ambiguous cases.
Worst case: a real "had had" gets flagged to log, MB sees it on review.
Net: REDUCES accuracy risk by removing engine-introduced doubles.

## Rollout

1. Sonnet builds the function + tests, all green
2. Sonnet runs apply_ops on existing halprin_full corrected_turns.json
3. Sonnet re-renders Stage 5 (free — no LLM cost)
4. Sonnet re-runs frequency report on new OUR_FINAL.v2.txt
5. Three-way verification:
   - Doubled_word count: 101 → <= 5 (the safe-list flagged ones)
   - Other category counts: unchanged ±5
   - Total diff blocks: 742 → ~647
6. Push everything to mrx_engine_v1 + mrx-context, send Scott raw URLs

## Files touched

- src/transforms/post_process.py (NEW or extend)
- src/apply_ops.py (call hook)
- tests/transforms/test_dedupe_consecutive_duplicates.py (NEW)
- (nothing else)

## Rollback

git revert. apply_ops just doesn't call the new function.

## Save and build instructions

1. Save this spec as specs/2026-05-03_DOUBLED_WORD_FIX.md in mrx-context.
   Commit, push, send raw URL.
2. Build per the spec — all 12 tests green before any commit.
3. Commit + push to mrx_engine_v1 with message:
   universal: dedupe consecutive duplicates (D-DOUBLED-WORD)
4. Run apply_ops on existing halprin_full corrected_turns.json.
5. Re-render Stage 5 (no LLM cost).
6. Re-run the frequency report on new OUR_FINAL.v2.txt.
7. Report verification numbers BEFORE pushing OUR_FINAL.v2 — Scott approves first.

Estimate: ~105 minutes.

Ping at: spec push, tests green, verification numbers. Don't go silent.
