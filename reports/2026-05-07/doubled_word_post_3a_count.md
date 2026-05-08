# Doubled Word Bucket A — Post-Spec-3a Count

**Date:** 2026-05-07
**Spec:** SPEC 3a — is_doubled classifier fix
**Classifier:** `src/mrx_engine_v1/classifier/is_doubled.py`
**Tests:** `tests/classifier/test_is_doubled.py` — 10/10 pass
**Baseline:** post-M1 count = 27 (see `doubled_word_post_m1_count.md`)

---

## 1. Total Count

| Run | Bucket A doubled_word |
|---|---|
| Pre-M1 | 27 |
| Post-M1 | 27 |
| Post-spec-3a | **22** |

Net reduction from spec 3a: **5 blocks suppressed.**
Spec target was ≤ 20. Achieved 22. See Section 4 for STOP-AND-REPORT.

---

## 2. Blocks Suppressed by Spec 3a (5)

| M1 block # | Doubled token | Mechanism |
|---|---|---|
| #56 | `tubing` | Both OUR and MB have "not tubing. Tubing is…" — after `low_tok` strips the period, "tubing tubing" is adjacent in BOTH sides → `mb_doubled` includes "tubing" → suppressed. *(Bonus suppression not in spec's 7 targets.)* |
| #81 | `a` | Both OUR and MB have "A. A backoff" → both produce "a a" in `low_tok` → suppressed. Spec target ✓ |
| #276 | `i` | "I I" in both OUR and MB (witness stutter preserved) → suppressed. Spec target ✓ |
| #392 | `okay` | "Okay. Okay." in both → suppressed. Spec target ✓ |
| #506 | `had` | "had had" in both (legitimate past-perfect construction) → suppressed. Spec target ✓ |

---

## 3. Spec Targets That Still Fire (3) — STOP-AND-REPORT

Three of the spec's 7 intended targets still fire because they contain **genuine OUR
defects** not present in MB. The original tagging of these blocks as false-positives
was incorrect.

### Block #66 — fires on `well well` (tagged `false-speaker-label` — INCORRECT)

**Claimed trigger (spec analysis):** "A. A geologist" → `is_doubled` fires on "a a"
from speaker label + article.

**Actual trigger after 3a fix:** "A. A geologist" is suppressed (MB also has "A. A
geologist" → mb_doubled includes "a"). BUT: OUR also has "for the **-well-** well" →
`low_tok` → "well well" → MB has only "for the well" → NOT suppressed → block fires.

**Root cause:** OUR renders "well" twice at a sentence boundary; MB has it once.
This is a real Stage 5 wrap/merge artifact — OUR has an extra "well". The
`false-speaker-label` tag was wrong.

---

### Block #593 — fires on `the the` (tagged `misclassification` — INCORRECT)

**Claimed trigger (spec analysis):** "until until" in both → suppressed.

**Actual trigger after 3a fix:** "until until" IS suppressed (MB also has it). BUT:
OUR also has "**-the-** the geologists" → "the the" after `low_tok` → MB has only
"the geologists" → NOT suppressed → block fires.

**Root cause:** OUR has an extra "the" (diff marker shows it is OUR-only). This is a
real doubled word in OUR. The `misclassification` tag was partially wrong — there IS
a real defect in this block beyond the legitimate "until until".

---

### Block #663 — fires on `a a` (tagged `false-speaker-label` — INCORRECT)

**Claimed trigger (spec analysis):** "A." speaker label + "a" first content word.

**Actual trigger:** The "a a" comes from "like a **-a-** calculation" — OUR has two
"a"s (the article + an OUR-specific extra "a"), MB has only one. The "A." speaker
label → "a" appears earlier in the token stream at a non-adjacent position. This is
NOT a speaker-label false positive; it is a real doubled-word defect in OUR.

---

## 4. STOP-AND-REPORT to Opus

Per spec protocol: "If any of those 7 still fire as doubled_word after the patch, STOP
and report numbers to Opus."

**Result: 22 (not ≤ 20). 3 of 7 targets still fire.**

Three blocks from the spec's target list remain in the `doubled_word` bucket:
- **#66** fires on `well well` (genuine Stage 5 wrap/merge artifact — real defect)
- **#593** fires on `the the` (genuine OUR-extra "the" — real defect)
- **#663** fires on `a a` (genuine OUR-extra "a" — real defect)

All three were incorrectly tagged as false-positives in the analysis that fed the spec.
They are not suppressible by MB-doubled comparison because MB genuinely differs from
OUR on these tokens.

**Recommendation for Opus:** Update the tag analysis for blocks #66, #593, #663.
These are real defects that belong in different categories (Stage 5 wrap artifact,
Stage 3 correction artifact, etc.) and should be tracked in spec 3b or later.
The 3a fix as implemented is correct — suppressing them would hide real OUR defects.

---

## 5. Updated Tag Distribution Table (post-3a, 22 blocks)

| Tag | Post-M1 | Post-3a | Delta | Notes |
|---|---:|---:|---:|---|
| `across-punct` | 8 | 7 | −1 | #56 (tubing) suppressed — both sides have "tubing. Tubing" |
| `misclassification` | 4 | 3 | −1 | #276 (#I I), #392 (Okay. Okay.), #506 (had had) suppressed; #593 remains (see §3) |
| `case-mismatch` | 5 | 5 | 0 | unchanged |
| `wrap-artifact` | 2 | 2 | 0 | unchanged |
| `stage3-introduced` | 2 | 2 | 0 | unchanged |
| `false-speaker-label` | 3 | 2 | −1 | #81 suppressed; #66 and #663 remain (see §3) |
| `reporter-check` | 2 | 2 | 0 | unchanged (marker fragmented in diff line; literal check doesn't fire) |
| `multi-word-repeat` | 1 | 1 | 0 | unchanged |
| **Total** | **27** | **22** | **−5** | |

---

## 6. Call Site Log

Updated call sites per spec:

| File | Old call | New call |
|---|---|---|
| `io/analysis/brandl_50pp/_run_brandl_diff_m1.py` | `is_doubled(mb_line, our_line)` inline | `from mrx_engine_v1.classifier.is_doubled import is_doubled` + `is_doubled(our_line, mb_line)` |
| `io/analysis/brandl_50pp/_run_brandl_diff.py` | `is_doubled(mb_line, our_line)` inline | Not updated — baseline script; MB-doubled suppression would retroactively change archived baseline numbers |

`_run_brandl_diff.py` call site **not updated** to preserve the archived
`_diff_out/block_classification.json` (786 blocks, 27 doubled_word). The baseline
numbers are the reference point for all post-M1 comparisons.

---

*Oracle Covenant honored. No engine code changed. No FINAL RTF opened.*
*Generated: 2026-05-07*
*Awaiting Opus revised analysis on blocks #66, #593, #663.*
