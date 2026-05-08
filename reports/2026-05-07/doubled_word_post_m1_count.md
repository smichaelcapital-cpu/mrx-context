# Doubled Word Bucket A — Post-M1 Count

**Date:** 2026-05-07
**Baseline:** pre-M1 diff (`_stage5_out`, 786 total blocks)
**M1 run:** post-M1 diff (`_stage5_m1_out`, 824 total blocks)
**Script:** `io/analysis/brandl_50pp/_run_brandl_diff_m1.py` → `_diff_out_m1/`

---

## 1. Total Count

| Run | Total diff blocks | Bucket A doubled_word |
|---|---|---|
| Pre-M1 (baseline) | 786 | **27** |
| Post-M1 | 824 | **27** |

**Bucket A doubled_word count is unchanged at 27.**

---

## 2. Status of Baseline #37 and #94

### Baseline #37 ("left left") → M1 #36: **STILL PRESENT**

In baseline: `Q. Okay. When you **-left-** left Conoco in 1994?`
In M1:       `Q. When you **-left-** left Conoco in 1994?`

The "Okay." prefix is gone (M1 promoted the preceding s2 Q. continuation to a standalone
paragraph). The "left left" artifact persists because it is a **Stage 5 line-wrap artifact**,
not a Stage 2 merge artifact. Stage 5 formats "When you left" on one layout line and
"left Conoco in 1994?" on the next; the paragraph normalizer joins them → "left left".
M1 changed the block boundary but did not fix the Stage 5 wrap.

The original `Q-DROP-primary` tag was partly wrong. The Q-DROP merge has been fixed by M1.
The remaining doubled word is a wrap-artifact. Re-tagged below.

### Baseline #94 ("those those") → M1 #90: **STILL PRESENT**

In baseline: `Q. Okay. And during that period, did you **----** were **-those-** those mostly vertical wells...`
In M1:       `Q. And during that period, did you **----** were **-those-** those mostly vertical wells...`

Same pattern: "Okay." prefix removed by M1 promotion; "those those" wrap-boundary artifact
persists. Re-tagged to `wrap-artifact`.

---

## 3. New Doubled-Word Blocks After M1

Two new blocks appeared that were not present in baseline.

### NEW: M1 #56 — tag: `across-punct`

| | Text |
|---|---|
| OUR | `A. After you drill the new well you run casing and you but not tubing. Tubing is` ... |
| MB | `A. After you drill the new well you run casing and you but not tubing, but` ... |

**Mechanism:** OUR has "not tubing. Tubing is" — the word "tubing" appears before a sentence-ending
period and then again sentence-initially. `low_tok` strips punctuation → "tubing tubing" → fires.
D-DOUBLED-WORD missed it at Stage 2 because the period between the tokens breaks adjacency.
Same `across-punct` failure mode as baseline blocks #83, #95, #102, etc.
This block is NEW because M1's paragraph promotion shifted the SequenceMatcher alignment,
surfacing a diff that previously was absorbed inside a larger replace block.

### NEW: M1 #66 — tag: `false-speaker-label`

| | Text |
|---|---|
| OUR | `A. A geologist would come up with a prospect to drill a well and I **-we-** would then...` |
| MB | `A. A **+geologist+** would come up with a prospect to drill a well and I we would then...` |

**Mechanism:** "A." speaker label + "A" (first word of content "A geologist…").
`low_tok` lowercases and strips punctuation → "a a" → fires.
Same `false-speaker-label` false-positive pattern as baseline #85 ("A. A back off") and
baseline #640 ("A. It looks like a **-a-** calculation").
This block is NEW because M1's paragraph promotion created a new paragraph boundary
here, exposing this block to the SequenceMatcher as a standalone diff unit.

---

## 4. Blocks That Dropped After M1

Two baseline blocks are no longer present in M1.

| Baseline block | Doubled token | Reason dropped |
|---|---|---|
| #69 | `a` (misclassification) | Multi-Q-DROP merge block. M1 promoted the s2 Q. continuations, breaking the merged paragraph into multiple standalone paragraphs. SequenceMatcher no longer aligns them as a single large replace block, so `is_doubled` does not fire. |
| #77 | `okay` (misclassification) | Same: the "Q. Okay. Q." Q-DROP merge pattern that produced "Okay. Okay." in baseline is broken by M1 paragraph promotion. "Okay. Okay." still exists in the MB oracle but is now correctly split across two diff blocks rather than a single merged block. |

Both were tagged `misclassification` in the baseline evidence — `is_doubled` fired on
"Okay. Okay." and "I I" patterns that existed in **both** OUR and MB (legitimate repetitions).
M1 incidentally eliminated these by changing paragraph boundaries.

---

## 5. Updated Tag Distribution Table

| Tag | Pre-M1 | Post-M1 | Delta | M1 block numbers |
|---|---:|---:|---:|---|
| `across-punct` | 7 | 8 | +1 | #56(NEW), #79, #91, #99, #311, #469, #723, #731 |
| `misclassification` | 6 | 4 | −2 | #276, #392, #506, #593 |
| `case-mismatch` | 5 | 5 | 0 | #68, #101, #285, #600, #790 |
| `wrap-artifact` | 0 | 2 | +2 | #36, #90 (re-tagged from Q-DROP-primary) |
| `Q-DROP-primary` | 2 | 0 | −2 | — (fixed by M1) |
| `stage3-introduced` | 2 | 2 | 0 | #87, #604 |
| `false-speaker-label` | 2 | 3 | +1 | #66(NEW), #81, #663 |
| `reporter-check` | 2 | 2 | 0 | #462, #512 |
| `multi-word-repeat` | 1 | 1 | 0 | #405 |
| **Total** | **27** | **27** | **0** | |

---

## Summary

- **M1 did not change the doubled_word count** (27 → 27).
- **Two Q-DROP-primary blocks are resolved at the tag level:** M1 promoted the s2 turns,
  so the merge-boundary artifact that caused baseline #37 and #94 to be labeled Q-DROP-primary
  is gone. However, both blocks still fire `is_doubled` due to Stage 5 line-wrap artifacts
  at the same turn boundaries. Root cause shifts from Q-DROP to Stage 5 wrap.
- **Two misclassification blocks were incidentally eliminated** (baseline #69, #77) —
  side effect of M1 paragraph promotion changing SequenceMatcher alignment.
- **Two new blocks appeared** (M1 #56 across-punct, M1 #66 false-speaker-label) —
  pre-existing content newly surfaced as standalone diff blocks after M1 paragraph promotion.
- **Net change in true actionable defects:** The 2 blocks that disappeared (#69, #77) were
  both false positives (misclassifications). The 2 new blocks are also false positives
  (#56 across-punct D-DOUBLED-WORD miss, #66 false-speaker-label classifier bug).
  No new true steno errors appeared.

---

*Oracle Covenant honored. No engine code changed. No FINAL RTF opened.*
*Source: `_diff_out_m1/block_classification.json` (824 blocks), `_diff_out/block_classification.json` (786 blocks).*
*Generated: 2026-05-07*
