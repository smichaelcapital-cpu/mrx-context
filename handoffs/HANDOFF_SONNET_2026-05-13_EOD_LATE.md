# Sonnet EOD Handoff — 2026-05-13 (v2)

## Stage A v0 Build Status

**6 modules built** (all untracked, not yet committed):
- `src/aligner_differ/__init__.py`
- `src/aligner_differ/normalize.py`
- `src/aligner_differ/tokenize.py`
- `src/aligner_differ/align.py` — currently uses diff-match-patch
- `src/aligner_differ/diff.py`
- `src/aligner_differ/categorize.py`
- `src/aligner_differ/frequency.py`
- `src/aligner_differ/run_stage_a.py`
- `src/aligner_differ/pairs.json`

**7 unit tests green** (`tests/aligner_differ/test_aligner_differ.py`, tests 1–6 + em-dash variant):
- normalize_strips_rtf, tokenize_words, align_simple, categorize_em_dash_insert (x2), categorize_capitalization, frequency_rollup

**Integration test (test 7 — Halprin full pipeline):**
- Ran once to completion: 778s (13 min) total
- normalize: 0.4s, tokenize: 0.1s
- align (diff-match-patch, 103k raw / 133k final tokens): ~777s — too slow
- diff + categorize + rollup: <1s
- Result: 47,089 diff events, FAILED on em_dash assertion (see below)
- No output files written (test used pytest tmp_path, not the permanent output dir)

---

## Tomorrow's Two Fixes

### Fix 1 — 500-Token Chunking (align.py)

Problem: diff-match-patch diff_main on 103k/133k tokens takes ~13 minutes.

Solution (Option A from recon): Before calling dmp, split both token lists into fixed-size chunks of ~500 tokens. Run dmp independently on each chunk. Concatenate results. Cross-boundary edit loss is statistically negligible for frequency analysis.

Implementation: In `align.py`, replace the single `dmp.diff_main(raw_enc, fin_enc)` call with a loop that chunks `raw_enc` and `fin_enc` into 500-char segments (since each token = 1 char in the encoded string), runs diff_main on each pair, and concatenates the op lists.

Expected result: ~200 chunks × <1ms each = <1s total alignment.

### Fix 2 — Em-Dash Categorization (categorize.py)

Problem: RAW file uses U+2011 (non-breaking hyphen) pairs `‑‑` instead of ASCII `--` or U+2014. The categorizer's `_EM_DASH_FORMS` set only contains `{"--", "\u2014"}` so U+2011 pairs fall to `other`.

Solution: Add `"\u2011\u2011"` (double non-breaking hyphen) and `"\u2011"` (single) to `_EM_DASH_FORMS`. Also check whether tokenizer splits `‑‑` as two separate PUNCTUATION tokens or one token — if two, the categorizer sees each `‑` individually (not in the set either). May need to handle in a post-tokenization step or extend the token regex.

---

## Branch State

- Branch: `feature/stage-a-aligner-differ-v0`
- Base: `main` at `95f09ee` (Merge: appearances Reported by anchor Pass 2)
- All files untracked. Nothing committed. Nothing pushed.
- Backup branch: `backup/pre-stage-a-2026-05-13` at same base commit.

---

## Halprin Baseline (sanity check from slow run)

- RAW tokens: 103,206
- FINAL tokens: 133,807
- Diff events: **47,089**
- Categories found: abbreviation_expansion, capitalization_only, filler_word_removed, line_break_changed, number_normalization, other, proper_noun_change, punctuation_added, punctuation_changed, punctuation_removed, whitespace_changed, word_substitution
- Missing (expected but absent): em_dash_inserted — due to U+2011 issue above

---

## Output Files

Neither `mb_evidence_raw.json` nor `mb_frequency_summary.json` exists on disk yet.
The slow run only exercised the integration test (which uses tmp_path, cleaned up by pytest).
Both files will be produced once Fix 1 (chunking) is in place and `run_stage_a.py` is executed directly.

---

## Tomorrow's Start Sequence

1. Open branch `feature/stage-a-aligner-differ-v0`
2. Fix 1: chunk align.py (500-token chunks, ~10 lines of code)
3. Fix 2: extend em-dash detection in categorize.py (check U+2011 tokenization first)
4. Re-run 7 unit tests — must stay green
5. Re-run integration test (Halprin only) — expect <30s total
6. Run full 4-pair pipeline via `run_stage_a.py`
7. Report top 20 patterns to Scott
8. Scott eyeballs, then commit

— End of handoff —
