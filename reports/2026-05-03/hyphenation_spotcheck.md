# Hyphenation Spot-Check Report
**Date:** 2026-05-03
**Session:** Sunday evening
**Analyst:** Sonnet
**Source:** `io/analysis/halprin_full/_diff_out/block_classification.json`
**Cross-ref:** `io/analysis/halprin_full/_stage3_1_out/_word_preservation_rejections.jsonl`

---

## Summary

| Bucket | Count | % | Notes |
|--------|-------|---|-------|
| REAL_ENGINE_BUG | 21 | 51% | Steno compounds not hyphenated; 6 are validator-blocked |
| MB_EDITORIAL | 20 | 49% | "Email" style preference (18) + Bates label style (2) |
| VALIDATOR_ARTIFACT | 0 | 0% | None confirmed self-resolving |
| UNCLEAR | 0 | 0% | |
| **Total** | **41** | | |

---

## Critical Finding: Validator Is Blocking Valid Fixes

6 of the 21 REAL_ENGINE_BUG blocks have a confirmed complication: the word_preservation validator **already tried to fix the pattern but was blocked**. These are not self-resolving like classic validator artifacts — they are persistent bugs with a different root cause.

| Pattern | Blocks | Rejected proposal example | Why rejected |
|---------|--------|--------------------------|--------------|
| `20172018` -> `2017-2018` | 189, 191, 221, 389 | `that 20172018 -> 2017-2018` | "that" dropped from span |
| `daytoday` -> `day-to-day` | 345 | `in daytoday -> day-to-day` | "in" dropped from span |
| `tenminute` -> `ten-minute` | 728 | `a tenminute -> ten-minute` | "a" dropped from span |

**Pattern:** In all 6 cases, the proposal span was wider than needed — it included the preceding article ("that", "the", "in", "a") in the `before`, but the `after` only contained the corrected compound. The validator saw the article as a dropped word and rejected the otherwise-correct fix.

**Fix implication:** Two options:
- A) Add decompaction rules to `word_preservation.py` for these numeric and compound patterns (so `20172018` is recognized as equivalent to `2017-2018`)
- B) Fix proposal generation to use narrower spans (just the compound word, not surrounding context)

These 6 blocks will **not** disappear on re-render without a code change.

---

## Bucket: REAL_ENGINE_BUG — 21 blocks

### Sub-pattern breakdown

| Sub-pattern | Blocks | Count | Validator-blocked? |
|------------|--------|-------|-------------------|
| `uhhuh` -> `uh-huh` | 155, 234, 325, 335, 535, 554, 687 | 7 | No |
| `20172018` -> `2017-2018` (year ranges) | 189, 191, 221, 389 | 4 | Yes |
| `Xandahalf` -> `X-and-a-half` (fractions) | 210, 411, 412, 481 | 4 | No |
| `nonX` -> `non-X` | 287, 288 | 2 | No |
| `daytoday` -> `day-to-day` | 345 | 1 | Yes |
| `yearend` -> `year-end` | 520 | 1 | No |
| `writeoff` -> `write-off` | 528 | 1 | No |
| `tenminute` -> `ten-minute` | 728 | 1 | Yes |

### All 21 REAL_ENGINE_BUG blocks

| Block | our_output | mb_output | Notes |
|-------|-----------|-----------|-------|
| 155 | Uhhuh. | Uh-huh. | |
| 189 | 20172018 | 2017-2018 | validator-blocked |
| 191 | sometime / 20172018? | some time / 2017-2018? | validator-blocked; "sometime"->"some time" is secondary |
| 210 | twoandahalf | two-and-a-half | |
| 221 | 20172018, | 2017-2018, | validator-blocked |
| 234 | Uhhuh. | Uh-huh. | |
| 287 | nonlitigation / question. | non-litigation / question? | also punctuation diff (separate defect) |
| 288 | nonlitigation (x2) | non-litigation (x2) | |
| 325 | Uhhuh. | Uh-huh. | |
| 335 | Uhhuh. / Yes. | Uh-huh. / Yes? | also punctuation diff (separate defect) |
| 345 | in / daytoday | on / a / day-to-day | validator-blocked; "in"->"on a" is separate word sub defect |
| 389 | 20172018. | 2017-2018. | validator-blocked |
| 411 | twoandahalf | two-and-a-half | |
| 412 | fiveandahalf | five-and-a-half | |
| 481 | seven and a half (split words) | Seven-and-a-half | engine split but didn't hyphenate; block also has YR Bates + Email |
| 520 | yearend / Yearend | year-end / Year-end | |
| 528 | writeoff (x2) | write-off (x2) | |
| 535 | Uhhuh. | Uh-huh. | |
| 554 | Uhhuh. | Uh-huh. + stage marker | also missing "(Witness peruses document.)" (separate defect) |
| 687 | Uhhuh. / 28th, | Uh-huh. / 28, | also ordinal style diff (separate defect) |
| 728 | tenminute | ten-minute | validator-blocked |

### Example blocks (verbatim)

**Example 1 — Uh-huh (Block 155)**
```
MB:  A. **+Uh-huh.+**
OUR: A. **-Uhhuh.-**
```

**Example 2 — Year range (Block 189)**
```
MB:  Q. And this was from back in that **+2017-2018+** period of initial investment...
OUR: Q. And this was from back in that **-20172018-** period of initial investment...
```

**Example 3 — Fractional compound (Block 210)**
```
MB:  Q. And that Black Box had invested **+two-and-a-half+** million in the field, right?
OUR: Q. And that Black Box had invested **-twoandahalf-** million in the field, right?
```

**Example 4 — non-litigation (Block 288)**
```
MB:  Q. ...investments are used only for **+non-litigation+** purposes? A. Only for **+non-litigation+** purposes?
OUR: Q. ...investments are used only for **-nonlitigation-** purposes? A. Only for **-nonlitigation-** purposes?
```

**Example 5 — write-off (Block 528)**
```
MB:  Q. And how is that 70 percent **+write-off+** documented? A. ...recorded in the books as a **+write-off.+**
OUR: Q. And how is that 70 percent **-writeoff-** documented? A. ...recorded in the books as a **-writeoff.-**
```

---

## Bucket: MB_EDITORIAL — 20 blocks

### Sub-pattern breakdown

| Sub-pattern | Blocks | Count |
|------------|--------|-------|
| `Email` -> `E-mail` (style preference) | 133, 328, 329, 330, 454, 604, 625, 627, 628, 670, 671, 681, 686, 699, 713, 716, 718, 719 | 18 |
| `YRnnnnnn` -> `YR-nnnnnn` (Bates label style) | 480, 685 | 2 |

**Key call on Email:** "Email" is a valid modern spelling (AP style, Merriam-Webster). "E-mail" is MB's consistent court-reporter style preference. Not objectively wrong. The engine should NOT fix this universally — it is MB-specific tailoring (Aligner+Differ territory). 18 blocks / 44% of all hyphenation diffs live here.

**Key call on Bates labels:** Bates label hyphenation (YR-285451 vs YR285451) varies by case setup. MB adds the hyphen as her style convention for this depo. Engine cannot know this rule universally.

### All 20 MB_EDITORIAL blocks

| Block | our_output | mb_output | Sub-pattern |
|-------|-----------|-----------|-------------|
| 133 | Email | E-mail | Email (block also has other diffs) |
| 328 | Email | E-mail | Email |
| 329 | Email | E-mail | Email |
| 330 | Email | E-mail | Email (block also missing "is") |
| 454 | Email | E-mail | Email (block also has phonetic diff "rose I"->"rosy") |
| 480 | YR285451. | YR-285451. | Bates label |
| 604 | Email | E-mail | Email (block also missing "and") |
| 625 | Email | E-mail | Email |
| 627 | Email / productions | E-mail / production is | Email (block also has word diff) |
| 628 | Email | E-mail | Email |
| 670 | Email | E-mail | Email |
| 671 | Email | E-mail | Email (block also missing stage marker) |
| 681 | Email | E-mail | Email (block also missing "with") |
| 685 | YR201481 | YR-201481 | Bates label |
| 686 | Email | E-mail | Email |
| 699 | Email / other | E-mail / others | Email (block also "other"->"others") |
| 713 | Email (x2) | E-mail (x2) | Email |
| 716 | Email (x2) | E-mail (x2) | Email |
| 718 | Email | E-mail | Email |
| 719 | Email | E-mail | Email |

### Example blocks (verbatim)

**Example 1 — Email style (Block 713)**
```
MB:  Q. Sir, Exhibit 257 is an **+E-mail+** exchange or **+E-mail+** that you received from Jonathan Love...
OUR: Q. Sir, Exhibit 257 is an **-Email-** exchange or **-Email-** that you received from Jonathan Love...
```

**Example 2 — Bates label (Block 480)**
```
MB:  Q. ...which bears the Bates label **+YR-285451.+**
OUR: Q. ...which bears the Bates label **-YR285451.-**
```

---

## VALIDATOR_ARTIFACT

**Count: 0 confirmed self-resolving**

Six blocks have validator-related complications (documented above under Critical Finding), but these will NOT disappear on re-render. They require active code changes and are classified REAL_ENGINE_BUG with validator-blocked flags.

---

## Recommendation

### Is this worth speccing? Yes — with a narrowed scope.

True fix surface: **21 REAL_ENGINE_BUG blocks** representing **6-7 distinct steno compound patterns**. All are objectively wrong with clear universal fixes.

Do NOT spec: The 20 MB_EDITORIAL blocks (Email + Bates). Those are MB tailoring, not engine bugs. They will be addressed by Aligner+Differ.

### Recommended approach: Two distinct fixes

**Fix A — Validator decompaction extension (highest ROI, do first)**

Patch `word_preservation.py` to recognize numeric year-range and compound patterns as valid decompactions. This unblocks the 6 validator-blocked blocks without any new prompt logic.

Candidates to add:
- `20172018` -> `2017` + `-` + `2018` (numeric year range pattern)
- `daytoday` -> `day` + `to` + `day`
- `tenminute` -> `ten` + `minute`

This is a targeted code change with immediate payoff on 6 blocks and also prevents future false-positive validator rejections on similar patterns.

**Fix B — Engine prompt rule for steno compound concatenation (remaining 15 blocks)**

Universal rule covering what the validator never attempted:
- `uhhuh` -> `uh-huh` (7 blocks — highest count, cleanest pattern, best quick win)
- `twoandahalf` / `fiveandahalf` -> `two-and-a-half` / `five-and-a-half` (4 blocks)
- `nonlitigation` -> `non-litigation` (2 blocks)
- `yearend` -> `year-end`, `writeoff` -> `write-off` (2 blocks)

**Uh-huh is the fastest win:** 7 blocks, universal, unambiguous, no validator complications, no co-occurring issues. If only one sub-pattern gets specced tonight, this is it.

### Secondary notes

1. Several REAL_ENGINE_BUG blocks have **co-occurring issues** beyond hyphenation (punctuation: 287, 335; word subs: 345; ordinal: 687; missing stage markers: 554, 671). The spec should address only the hyphenation component — co-occurring issues belong in separate defects.

2. **Block 481** is complex: our engine split `sevenandahalf` into "seven and a half" (4 separate words) via a stage-3 proposal but didn't hyphenate. MB wants "Seven-and-a-half" with capitalization. The hyphenation part is covered by Fix B; capitalization is a separate concern.

3. **Email (18 blocks) is 44% of this diff set but 0% of the fix surface.** If Opus or Scott want to revisit this later as MB tailoring, the pattern is unambiguous — MB always prefers "E-mail", engine always outputs "Email".

---

*Report generated: 2026-05-03 evening session*
