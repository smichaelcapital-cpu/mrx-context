SPEC: validate_ops — REWORD word-preservation guard (D-WRITER-WORD-DROP)

Date: 2026-05-03
Author: Opus
Builder: Sonnet
Status: APPROVED for build

## Rule sheet header
- Universal? YES — applies to every court reporter forever
- Code or prompt? CODE — deterministic, no judgment
- File location: src/mrx_engine_v1/validate_ops/ (universal core)
- Commit prefix: universal:

## Problem
Recon (2026-05-03) confirmed the AI Writer systematically anchors REWORD
token spans one position too wide, pulling in a valid context word, then
emits an `after` text that drops that word.

Confirmed examples:
- before="a tenminute"        after="ten-minute"     → drops "a"
- before="invested twoandahalf" after="two and a half" → drops "invested"
- before="that your"          after="you're"         → drops "that"

Affected: ~105-120 of 545 REWORD proposals on halprin_full (~20%).
Cross-category contamination confirmed: at least hyphenation, possibly
others. Every affected proposal silently drops a real word from the
transcript. RULE-INPUT-IS-SACRED violation.

## Goal
Add a deterministic validator that REJECTS any REWORD proposal where a
word in `before` silently disappears from `after`. Log every rejection
to rejections.jsonl with full context for review.

This is a guard, not a corrector. Bad proposals get blocked, not patched.
The Writer can re-propose. Worst case: a flagged anomaly reaches MB
without an auto-fix — which is the safe failure mode.

## Algorithm

For each REWORD proposal:

1. Tokenize `before` into words (case-insensitive, strip punctuation)
2. Tokenize `after` into words (case-insensitive, strip punctuation)
3. For each word in `before`:
   - If word appears in `after` → OK
   - If word is on the EXPECTED_DROP allow-list → OK (see below)
   - If word is a known steno artifact being corrected → OK (see below)
   - Otherwise → REJECT proposal, log to rejections.jsonl

EXPECTED_DROP allow-list (initial, conservative):
- Empty list at v1. Every drop must be explicitly justified later.

STENO_ARTIFACT detection (the legitimate-correction case):
A word in `before` may legitimately not appear in `after` if:
- The word in `before` is a single token that contains 3+ concatenated
  words (e.g. "twoandahalf", "tenminute", "writeoff", "daytoday")
  AND the `after` text contains those component words split apart
- This is the "decompaction" case and is legitimate

Decompaction detection (deterministic, no AI):
- For each word in `before` not in `after`:
  - Strip vowels, check if remaining consonants appear as substring
    sequence in `after` (loose match)
  - If yes → likely decompaction, allow
  - If no → REJECT

## What gets logged on rejection

{
  "turn_idx": 3550,
  "proposal_id": "p_0007",
  "rule": "validate_ops.word_preservation",
  "before": "a tenminute",
  "after": "ten-minute",
  "dropped_words": ["a"],
  "verdict": "rejected",
  "reason": "word 'a' in before not present in after, no decompaction match"
}

Rejected proposals do NOT get applied. The turn passes through with no
correction. The original (uncorrected) text remains. RULE-PROOF-OF-WORK
satisfied — every block is logged.

## Edge cases (specified)

1. Punctuation differences ("Yes," → "Yes.") — not a word drop, OK
2. Capitalization differences ("That" → "that") — not a word drop, OK
3. Possessives ("John's" → "Johns") — strip apostrophes before compare
4. Hyphenated compounds ("part-time") — count as single token in both
5. Quotation marks added/removed — not a word drop, OK
6. Empty `after` — REJECT (entire turn dropped is never legitimate)
7. Numbers as digits vs words ("10" vs "ten") — special handler:
   build a small bidirectional map for 0-99, treat as equivalent

## Tests required

File: tests/validate_ops/test_word_preservation.py

Required test cases:
- T1: Simple drop ("a tenminute" → "ten-minute") → REJECTED
- T2: Decompaction ("twoandahalf" → "two and a half") → ACCEPTED
- T3: Mixed ("invested twoandahalf" → "two and a half") → REJECTED ("invested" lost)
- T4: Capitalization-only change ("Yes" → "yes") → ACCEPTED
- T5: Punctuation-only change ("Yes," → "Yes.") → ACCEPTED
- T6: Number style ("10" → "ten") → ACCEPTED via number map
- T7: Possessive ("John's" → "Johns") → ACCEPTED
- T8: Empty after → REJECTED
- T9: All 5 confirmed bug cases from recon (turns 131, 1011, 1798, 2649, 3550) → REJECTED
- T10: Verify rejections.jsonl gets written for every REJECT
- T11: Hyphenated compound ("part-time" → "parttime") both directions → ACCEPTED
- T12: Quote add ("only" → '"only"') → ACCEPTED
- T13: Multi-word drop ("Email certainly" → "email") → REJECTED
- T14: Regression: existing 582 engine tests still pass

## Acceptance criteria

- [ ] All 14 tests pass
- [ ] Existing 582 engine tests still pass (regression)
- [ ] Run apply_ops on existing halprin_full proposals → measure rejected count
- [ ] Rejected count: 100-130 (matches recon estimate of 105-120)
- [ ] rejections.jsonl exists with N entries (N = rejected count)
- [ ] Re-render Stage 5, re-run frequency report → word_drop count drops
- [ ] No regression in OTHER categories (counts unchanged ±5)

## Prime Directive check

"Could this reduce transcript accuracy or credibility?"

Direct effect: REJECTED proposals leave the original (uncorrected) text
in place. The original came from the steno rough. Steno rough is the
ground truth input. Leaving it unmodified is the safe default.

Indirect effect: a legitimate correction might be rejected if our
decompaction detector misses it. Mitigation: log every rejection with
full context, MB sees flagged anomalies on review, decompaction logic
can be tightened over time based on real misses.

Net: STRONGLY INCREASES accuracy. Stops ~110 silent word drops per depo.
Worst case: a few correctable anomalies stay flagged-not-fixed instead
of corrected, which is the safe failure mode.

## Rollout

1. Sonnet builds the validator + tests, all green
2. Sonnet runs apply_ops on existing halprin_full proposals
3. Sonnet reports: rejected count, sample of 10 rejections (mix of
   confirmed-bug + any surprise rejections)
4. Opus reviews surprise rejections to confirm they are real bugs
   (not legitimate corrections being wrongly blocked)
5. If clean → re-render Stage 5, re-run frequency report
6. Three-way verification:
   - Rejected count: 100-130
   - word_drop category: drops by ~50-80 blocks
   - Other categories: unchanged ±5
   - Total diff blocks: 743 → ~660-690
7. Push commit. Halprin output stays local (Oracle Covenant + repo-public rule).

## Files touched

- src/mrx_engine_v1/validate_ops/word_preservation.py (NEW)
- src/mrx_engine_v1/validate_ops/__init__.py (register new validator)
- src/mrx_engine_v1/apply_ops.py (call hook before applying REWORD)
- tests/validate_ops/test_word_preservation.py (NEW)

## Rollback

git revert. apply_ops stops calling the new validator. Behavior reverts
to current (silent drops continue).

## Save and build instructions

1. Save this spec as specs/2026-05-03_VALIDATE_WORD_PRESERVATION.md
   in mrx-context. Commit, push, reply with raw URL.
2. Build per the spec — all 14 tests green before any commit.
3. Commit + push to mrx_engine_v1 with message:
   universal: validate_ops word preservation guard (D-WRITER-WORD-DROP)
4. Run apply_ops on existing halprin_full proposals.
5. Report rejected count + 10-sample BEFORE re-rendering Stage 5.
   Wait for Opus review of the sample.
6. After Opus approval: re-render Stage 5, re-run frequency report,
   report verification numbers.
7. Halprin OUR_FINAL.v3.txt and corrected_turns stay LOCAL. Do not push.

Estimate: ~75 minutes.

Ping at: spec push, tests green, rejected count + sample, verification numbers.
Don't go silent.
