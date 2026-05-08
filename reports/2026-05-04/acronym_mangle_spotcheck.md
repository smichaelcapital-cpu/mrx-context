# SPOT-CHECK — acronym_mangle (17 blocks)
**Date:** 2026-05-04
**Analyst:** Claude Sonnet
**Source:** `io/analysis/halprin_full/_diff_out/block_classification.json`
**DO NOT SPEC. DO NOT CODE. Recon findings only.**

---

## Classification of 17 Blocks

### Category 1 — REPORTER_PLACEHOLDER (7 blocks)

OUR output contains `*REPORTER CHECK HERE*` or `CHECK` — the original steno had an
inaudible or garbled segment the stenographer flagged for later resolution. MB resolved
it from audio; OUR correctly preserved the placeholder. These are **not engine bugs.**
The engine cannot fix these without the audio.

| Block | OUR placeholder | MB resolved to |
|-------|----------------|----------------|
| #290 | `*REPORTER CHECK HERE*` | Full sentence (8 words) |
| #305 | `*REPORTER CHECK HERE*?` | Full sentence (8 words) |
| #311 | `CHECK` | Full sentence (6 words) |
| #340 | `*REPORTER CHECK HERE*?` | Full sentence (4 words) |
| #367 | `*REPORTER CHECK HERE*?` + `*REPORTER CHECK HERE*` | Long multi-part question |
| #594 | `CHECK` | `I don't know.` |
| #689 | `*REPORTER CHECK HERE*?` | Full sentence (7 words) |

**Verdict:** Not fixable by engine. The steno had inaudible audio at these points.
MB fixed them manually from the recording. These are correctly in the scoreboard as
the engine's known limitation — they cannot be eliminated without audio processing.

---

### Category 2 — REAL_ENGINE_BUG (10 blocks)

#### Pattern A — Ampersand in acronym rendered as steno words (3 blocks)

The steno "&" stroke translated to English words ("and", "in", "N") instead of "&".

| Block | MB | OUR | Pattern |
|-------|-----|-----|---------|
| #34 | `E&P.` | `He in P.` | "E" → "He", "&" → "in", "P" → "P" |
| #52 | `E&P.` | `ENP.` | "&P" → "NP" (single-stroke collapse) |
| #178 | `g&g` | `good and good` | "g" → "good", "&" → "and", "g" → "good" |

**Root cause:** The steno brief for "&" in an acronym context translates to an English
connective. The engine has no rule to recognize "X & Y" acronym shapes and preserve them.

**Fix options:**
- Dictionary: add "E&P" and "G&G" to the case dictionary as known terms → Writer would
  recognize and fix. Works for known acronyms only. MB-specific for E&P/G&G specifically.
- Stage 2 transform: detect "letter(s) + and/in/of + letter(s)" where all are single chars
  or short abbreviations → rejoin with "&". Universal but narrow regex.
- Reader + Writer: Reader flags "He in P" as steno_artifact (letters-as-words pattern);
  Writer uses dictionary to propose "E&P". This already exists in Reader's PASS 2 rules
  (letters-as-words heuristic) — why didn't it fire?

**Recommendation:** Dictionary entry approach for E&P. The Reader's letters-as-words
detection should have flagged "He in P" — this is worth investigating why it didn't.
If Reader is not firing on this pattern, a READER_PROMPT fix may close all three blocks.

#### Pattern B — Date range slash vs. hyphen (2 blocks)

| Block | MB | OUR | Pattern |
|-------|-----|-----|---------|
| #104 | `2017-2018`, `2017-2018,` | `2017/2018`, `2017/2018` | Slash → hyphen in year range |
| #150 | `2017-2018` (in context) | `2017/2018` (in context) | Same |

**Root cause:** The steno produced "/" for the range separator; MB convention is "-".
This is a deterministic Stage 2 transform.

**Fix:** `\b(\d{4})/(\d{4})\b` → `$1-$2`
**Scope:** Universal (year ranges in deposition context always use hyphen, not slash).
**Risk:** Very low. The pattern `YYYY/YYYY` is unambiguous in deposition context.
**Verdict: CHEAP FIX. 1 regex transform. Universal.**

#### Pattern C — Bates label split and digit errors (3 blocks)

| Block | MB | OUR | Pattern |
|-------|-----|-----|---------|
| #247 | `YR-455297.` | `YR 455297.` | Hyphen dropped — "YR-[digits]" → "YR [digits]" |
| #669 | `YR-249174.` | `YR 249174.` | Same split pattern |
| #700 | `YR-239492` | `YR 329492` | Split + digit transposition ("239" → "329") |

**Root cause for #247/#669:** The Bates label hyphen was not captured by steno — the
prefix "YR" and digits ran as two tokens. Pattern is consistent: "YR [5-6 digits]" should
be "YR-[5-6 digits]".

**Root cause for #700:** Same split plus a digit transposition in the number itself
("239492" → "329492"). The digit error is uncorrectable by the engine (no way to know
the correct Bates number without the exhibit list).

**Fix for #247/#669:** Stage 2 transform or Writer → recognize "YR [\d]{5,6}" and rejoin.
**Scope:** MB-specific (YR prefix is this case's Bates format).
**Risk:** Low. The pattern "YR" + 5-6 digits is unambiguous.
**Verdict: MB-SPECIFIC cheap fix for #247 and #669. #700 not fixable (digit error).**

#### Pattern D — Miscellaneous steno artifacts (2 blocks)

| Block | MB | OUR | Pattern |
|-------|-----|-----|---------|
| #188 | `Cole, C-o-l-e.` | `Come, credit on LE.` | "Cole" → "Come" (phonetic) + "C-o-l-e" → "credit on LE" (steno garble of spelled name) |
| #651 | `I. And he` | `I&E` | Sentence-end "I." + "And" → steno single stroke "I&E" |

**#188:** The name "Cole" is not in NAMES_LOCK. "Come" for "Cole" is a phonetic near-miss
(one consonant off). "C-o-l-e" (spelled-out name) was garbled by steno into "credit on LE" —
steno strokes for C, o, l, e were each read as words. Cannot fix without "Cole" in NAMES_LOCK
and the Reader recognizing the spelled-out pattern.

**#651:** The steno produced a single stroke "I&E" for what was actually "I. And he" (sentence
break + new clause). This is a steno brief collision — the stroke for "I&E" also exists as the
end-of-sentence "I." + "And". Not fixable without knowing this steno brief.

**Verdict: Both #188 and #651 are BACKLOG — require case-specific knowledge or steno brief lookup.**

---

## Summary Table: All 17 Blocks

| # | Block | Category | Pattern | Fixable? |
|---|-------|----------|---------|----------|
| 1 | #34 | REAL_ENGINE_BUG | E&P ampersand → "He in P" | Dictionary/Reader fix |
| 2 | #52 | REAL_ENGINE_BUG | E&P ampersand → "ENP" | Dictionary/Reader fix |
| 3 | #104 | REAL_ENGINE_BUG | 2017/2018 → 2017-2018 | YES — cheap transform |
| 4 | #150 | REAL_ENGINE_BUG | 2017/2018 → 2017-2018 | YES — cheap transform |
| 5 | #178 | REAL_ENGINE_BUG | g&g → "good and good" | Dictionary/Reader fix |
| 6 | #188 | REAL_ENGINE_BUG | Cole → Come + garbled spelled name | Backlog (name missing) |
| 7 | #247 | REAL_ENGINE_BUG | YR-455297 split | YES — MB-specific transform |
| 8 | #290 | REPORTER_PLACEHOLDER | *REPORTER CHECK HERE* | Not fixable |
| 9 | #305 | REPORTER_PLACEHOLDER | *REPORTER CHECK HERE* | Not fixable |
| 10 | #311 | REPORTER_PLACEHOLDER | CHECK | Not fixable |
| 11 | #340 | REPORTER_PLACEHOLDER | *REPORTER CHECK HERE* | Not fixable |
| 12 | #367 | REPORTER_PLACEHOLDER | Multiple CHECKs | Not fixable |
| 13 | #594 | REPORTER_PLACEHOLDER | CHECK | Not fixable |
| 14 | #651 | REAL_ENGINE_BUG | I&E steno collision | Backlog (steno brief) |
| 15 | #669 | REAL_ENGINE_BUG | YR-249174 split | YES — MB-specific transform |
| 16 | #689 | REPORTER_PLACEHOLDER | *REPORTER CHECK HERE* | Not fixable |
| 17 | #700 | REAL_ENGINE_BUG | YR-329492 digit error | No (wrong digit) |

**Totals: 7 REPORTER_PLACEHOLDER · 10 REAL_ENGINE_BUG**
**Of 10 bugs: 4 cheap-fixable, 6 backlog/not-fixable**

---

## Pattern Recommendations

### Fix A — Year-range slash → hyphen (UNIVERSAL, HIGH CONFIDENCE)

```
Stage 2 transform: \b(\d{4})/(\d{4})\b → $1-$2
```
Fixes: #104, #150
Commit prefix: `universal:`
Risk: Very low. `YYYY/YYYY` in deposition text is always a date range.
Verdict: **CHEAP FIX. Pile on before re-render. 1 regex.**

### Fix B — Bates label rejoin (MB-SPECIFIC)

```
Stage 2 transform (MB): YR\s+(\d{5,6})\b → YR-$1
```
Fixes: #247, #669 (not #700 — digit error unfixable)
Commit prefix: `mb-specific:`
Risk: Low. "YR" prefix is case-specific; would need to be in MB profile.
Verdict: **Worth adding as MB-specific transform. 1 regex.**

### Fix C — Ampersand acronym detection (READER PROMPT, MEDIUM RISK)

Reader's PASS 2 already has a "letters-as-words" heuristic that should catch "He in P"
as a steno artifact. Needs investigation: why didn't it fire on #34, #52, #178?
Possible causes: (a) Reader requires a capital adjacent to trigger letters-as-words; "he"
is lowercase so it was read as a word. (b) "in" doesn't trigger the pattern.
If Reader fires correctly, Writer can use the dictionary to propose "E&P".
Verdict: **Needs Reader prompt investigation. Not before re-render (too broad to spec today).**

### Fix D — Add domain terms to dictionary (DATA FIX)

Add "E&P" and "G&G" (geoscience & geophysics) to the case dictionary. Would let Reader
and Writer recognize these as known terms.
Verdict: **Scott's call — data fix, not code. Trivial if terms are case-appropriate.**

---

## Verdict: Pile on before re-render?

**YES on Fix A (date range):** Universal, 1 regex, zero risk. Closes 2 Bucket A blocks
and any future `YYYY/YYYY` patterns across all depositions.

**YES on Fix B (Bates rejoin):** MB-specific, 1 regex, low risk. Closes 2 more blocks
(#247, #669) from the Bates label split pattern that appears consistently throughout
halprin_full.

**NO on everything else before re-render.** Ampersand acronym requires Reader investigation
(not a quick fix). Reporter placeholders are not engine problems. The remaining bugs
require case knowledge or steno brief lookup.

**Net impact of pile-on (Fix A + Fix B):** 4 fewer Bucket A blocks on re-render.
Combined with doubled_word Fix 1 (remove "the" from safelist), that's potentially
5 additional blocks closed before the re-render at essentially zero risk.

**Recommendation to Scott:** Fix A (date range) is a universal commit worth adding now.
Fix B (Bates) is MB-specific — Scott decides if it's worth the commit given it's
case-specific infrastructure. Both are 1-regex transforms.
