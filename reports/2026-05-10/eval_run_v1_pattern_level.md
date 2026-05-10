# Eval A — Pattern-Level Evaluation Report

**Date:** 2026-05-10 (evening session)
**Author:** Sonnet (evening instance)
**Status:** COMPLETE — ready for Scott review, no commits made
**Report path:** C:\Users\scott\OneDrive\Documents\mrx-context\reports\2026-05-10\eval_run_v1_pattern_level.md

---

## 1. Headline

**13 of 15 AUTO patterns HOLD on the test set. 2 are SOFT. 0 WOBBLY. 0 FAILED.**

The core fingerprint is confirmed. The two SOFT patterns (`split_leading_well` and `split_leading_yeah`) were the weakest AUTO patterns in training (0.9086 and 0.9355) and dropped slightly into SUGGEST territory on the test set (0.8222 and 0.8667). Both are witness-dependent speech habits — they vary by who MB is transcribing, not just by MB's habits. The test set may have a different distribution of verbose vs. terse witnesses.

No pattern failed. No pattern is wobbly. The splits Q-opener patterns, leading Yes/No, cap_sentence_start, both stage-direction punctuation patterns, period addition, and double-period cleanup are all rock-solid.

---

## 2. Methodology

**Eval setup:**
- Test set: 45 of 48 pairs (3 quarantined: 031326yellowrock .rtf rough, 030526yellowrock .rtf final, 071125unitedhealth-guillotte .pdf rough)
- MRX_EVAL_MODE=1 enforced throughout
- Test pairs extracted in this same session using `eval_test_extraction.py` (extraction functions verbatim from phase0_preflight_v3.py)
- Training set: 186 clean pairs (195 total, 9 quarantined)
- 0 training/test stem overlap (checked by extraction script)

**Detection methodology:**
Identical regexes and turn-type filters as training recon scripts. Content_match throughout — no gap_alignment (same limitation as training recon). The comparison is therefore apples-to-apples: same detector applied to training finals vs test finals.

**Confidence metric used for comparison:**
- `pairs_coverage` patterns (12/15): test metric = pairs_with_≥1_match / total_test_pairs
- `ratio` patterns (3/15): test metric = matching_turns / total_target_turns

**Verdict thresholds:**
- **HOLDS**: delta ≥ −0.05 (within 5pp of training value)
- **SOFT**: −0.10 ≤ delta < −0.05
- **WOBBLY**: −0.20 ≤ delta < −0.10
- **FAILED**: delta < −0.20

**Script:** `C:\Users\scott\AppData\Local\Temp\eval_a_pattern_level.py`
**Results JSON:** `C:\mrx_training_set\MB\extracted\_eval_a_results.json`

---

## 3. Pattern-by-Pattern Table

| Pattern | Layer | Train | Test | Delta | Cover | Verdict |
|---|---|---|---|---|---|---|
| `split_bare_and_q_opener` | splits | 1.0000 | 1.0000 | +0.0000 | 45/45 | **HOLDS** |
| `split_so_q_opener` | splits | 1.0000 | 1.0000 | +0.0000 | 45/45 | **HOLDS** |
| `split_double_dash_interruption` | splits | 0.9624 | 0.9556 | −0.0068 | 43/45 | **HOLDS** |
| `split_leading_yes` | splits | 1.0000 | 1.0000 | +0.0000 | 45/45 | **HOLDS** |
| `split_leading_okay_a` | splits | 0.9731 | 0.9556 | −0.0175 | 43/45 | **HOLDS** |
| `split_leading_uhmm` | splits | 0.9516 | 0.9556 | +0.0040 | 43/45 | **HOLDS** |
| `split_leading_yeah` | splits | 0.9355 | 0.8667 | **−0.0688** | 39/45 | **SOFT** |
| `split_leading_well` | splits | 0.9086 | 0.8222 | **−0.0864** | 37/45 | **SOFT** |
| `split_leading_no` | splits | 1.0000 | 1.0000 | +0.0000 | 45/45 | **HOLDS** |
| `split_okay_q_opener` | splits | 0.9946 | 1.0000 | +0.0054 | 45/45 | **HOLDS** |
| `cap_sentence_start` | cap | 0.9877 | 0.9874 | −0.0003 | 45/45 | **HOLDS** |
| `punct_stage_direction_question` | punct | 0.9355 | 1.0000 | +0.0645 | 45/45 | **HOLDS** |
| `punct_stage_direction_period` | punct | 0.9946 | 0.9778 | −0.0168 | 44/45 | **HOLDS** |
| `punct_period_addition` | punct | 0.9302 | 0.9446 | +0.0144 | 45/45 | **HOLDS** |
| `punct_double_period_cleanup` | punct | 0.9961 | 0.9968 | +0.0007 | 45/45 | **HOLDS** |

*Train/Test columns: pairs_coverage for pairs_coverage-basis patterns; ratio for ratio-basis patterns.*
*Cover = test pairs with ≥1 matching event / total test pairs evaluated.*

---

## 4. Spot-Check — Most-Changed Pattern: `split_leading_well`

Training value: 0.9086 (169/186 pairs). Test value: 0.8222 (37/45 pairs). Delta: −0.0864.

8 test pairs had zero "Well," or "Well." A-turn openers. That accounts for the full drop.

**Three test pairs examined:**

**[010626everett]** — 1 match / 81 A turns (0.0123)
- e.g.: `Well, workers' comp, right, yeah.`
- This witness gives very short answers. Only 1 "Well" opener in the whole deposition. Not absent — just a low-frequency witness.

**[011824smith]** — 7 matches / 406 A turns (0.0172)
- e.g.: `Well, this is -- we call it Jefferson Neurobehavioral Group, but there's also a second name on the d...`
- e.g.: `Well, there was no Jefferson Neurobehavioral at that time.`
- e.g.: `Well, but you can't go to that low -- you have to look at the validity scales first.`
- A medical expert witness. Uses "Well," but rarely (1.7%). Confirmed real pattern, low frequency.

**[012026spasevski]** — 0 matches / 610 A turns (0.0000)
- Zero "Well," openers in 610 A turns. This witness does not use "Well" as a hedge. The attorney's style may also direct terse answers.

**Conclusion:** The pattern drop is witness-dependent, not an extraction error. When MB transcribes witnesses who don't say "Well,", the pattern doesn't appear — because it's a preserved speech habit, not an insertion. In 8/45 test depositions, witnesses used no "Well," openers. The habit is real in MB's work but is gated on witness speech patterns. This is expected behavior for a preserved-speech pattern.

**Recommendation for `split_leading_well`:** Drop to SUGGEST (0.82 is SUGGEST-lane territory). The pattern is real and consistent when it occurs — but it doesn't occur universally. SUGGEST is honest.

**Same recommendation for `split_leading_yeah`:** test_pc = 0.8667 (39/45). Same root cause: 6 test pairs had no "Yeah" openers. Drop to SUGGEST.

---

## 5. Notable Results

**`punct_stage_direction_question` improved:** train=0.9355, test=1.0000. All 45 test pairs had at least one `?(` event. This is a stronger signal than training (174/186). The test set (newer depos, 2024–2026) may have more exhibit marking activity.

**`split_okay_q_opener` improved:** train=0.9946, test=1.0000. The one training pair that lacked "Okay" Q openers didn't appear in test. 45/45 test pairs have it.

**`cap_sentence_start` is essentially identical:** train=0.9877, test=0.9874. Three-decimal precision match. This is the most robust pattern in the fingerprint.

**`punct_period_addition` improved slightly:** train=0.9302, test=0.9446. Test finals may have cleaner steno-to-final conversion, or the specific attorneys in the test set elicit more complete answer turns.

**`split_double_dash_interruption`:** 43/45. Two test pairs had no interruptions. That's expected variance — some depositions run without cutoffs.

---

## 6. Provenance

- Extraction script: `C:\Users\scott\AppData\Local\Temp\eval_test_extraction.py`
- Eval script: `C:\Users\scott\AppData\Local\Temp\eval_a_pattern_level.py`
- All 45 test pair accesses logged to `C:\mrx_training_set\MB\_provenance\pair_access.jsonl` with `purpose: eval_a_measurement, mode: eval_read`
- Results JSON: `C:\mrx_training_set\MB\extracted\_eval_a_results.json`
- No YAML files modified. No training data modified. Read-only eval.
- MRX_EVAL_MODE=1 enforced by script assertion.

---

## 7. Rollup

**Overall assessment: The fingerprint is real and holds at test-set scale.**

| Verdict | Count | Patterns |
|---|---|---|
| HOLDS | 13 | All Q-openers, leading Yes/No, double-dash, Okay-A, Uhmm, cap, all 4 punct |
| SOFT | 2 | split_leading_well (−0.086), split_leading_yeah (−0.069) |
| WOBBLY | 0 | — |
| FAILED | 0 | — |

The two SOFTs were the two weakest AUTO patterns at training time (0.9086 and 0.9355). They are now correctly landing in SUGGEST territory on an independent test set. This is the system working as designed — patterns that were barely AUTO at 186 training pairs are SUGGEST at the test population.

---

## 8. Recommendations

**Action on SOFT patterns:**

| Pattern | Current lane | Recommended | Reason |
|---|---|---|---|
| `split_leading_well` | AUTO (0.9086 train) | **SUGGEST** (0.8222 test) | Witness-dependent; 8/45 test pairs had none. Honest SUGGEST. |
| `split_leading_yeah` | AUTO (0.9355 train) | **SUGGEST** (0.8667 test) | Same root cause; 6/45 test pairs had none. |

**Do NOT execute these demotions.** Scott decides.

**If Scott agrees:** Net result = 13 AUTO patterns (down from 15). SUGGEST count increases by 2.

**Action on 13 HOLDS patterns:** No action needed. These are confirmed. Engine can consume all 13 at AUTO confidence.

---

## 9. May 13 Story

**The fingerprint survives its first independent test.**

Trained on 186 deposition pairs, measured against 45 held-out pairs it has never seen: 13 of 15 AUTO patterns hold within a 5-percentage-point tolerance. Zero patterns failed. The two that softened were the two that were closest to the AUTO/SUGGEST boundary at training time — which means the measurement system is calibrated correctly, not lenient.

For MB's May 13 review: the patterns that always appear (Yes, No, And, Okay, So as Q opener, sentence capitalization, stage directions, period endings) are confirmed universal habits. The patterns that softened (Well, Yeah as A openers) are preserved speech habits — MB keeps them when witnesses say them, but they don't appear universally because witnesses vary. That distinction is itself a finding: MB's fingerprint includes both universal habits and witness-dependent preservation patterns.

---

— End of Eval A —
