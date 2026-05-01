# Halprin Mini — Three-Way Diff V2 (RAW vs OURS-V2 vs MB)

**Date:** 2026-04-30
**Scope:** Pages 13-54 of OURS-V2 vs same range of MB
**RAW source:** `io/analysis/halprin_mini/_pipeline_out/halprin_mini.stage1.turns.json`
**OURS-V2 source:** `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt` (post V2 run)
**MB source:** `oracle/finals/halprin/040226yellowrock-FINAL.txt`, pages 13-49 (body) + pages 296-300 (back matter)
**V1 baseline:** `baselines/halprin_mini.OUR_FINAL.V1.2026-04-30.txt`

> **Comparison note:** Diff counts use clean V2 output ({{MB_REVIEW}} tags stripped). V2 applies 83 REWORDs and 43 FLAGs; FLAGs leave text verbatim and append a review marker.

**Headline numbers:**
- Total diff lines V1 vs MB (pages 13-54): **1,040**
- Total diff lines V2 vs MB (pages 13-54): **827**
- Delta: **-213 lines (-20%)**
- Pages 1-12: **0 diffs** (template — unchanged)

---

## Stage 3.1 run stats (V2)

| Metric | V1 | V2 |
|--------|----|----|
| Anomalies found | ~10-15 est. | **147** |
| Proposals generated | ~10-15 est. | **126** |
| REWORDs applied | unknown | **83** |
| FLAGs applied | unknown | **43** |
| Reader cost | ~$0.05 est. | $0.52 |
| Writer cost | ~$0.05 est. | $0.43 |
| Total cost | ~$0.10 est. | $0.95 |

V2 anomaly breakdown by category:

| Category | Count |
|----------|-------|
| steno_artifact | 77 |
| unclear | 25 |
| name_uncertain | 23 |
| phonetic | 15 |
| format_artifact | 6 |
| objection_format | 1 |
| **Total** | **147** |

Confidence breakdown: high=105, medium=35, low=7.

---

## PATTERN 1: Key steno artifacts — V1 vs V2 status

These are the 10 defects identified in the original V1 audit (HALPRIN_MINI_3WAY_DIFF.md).

| Page | Defect (RAW) | MB target | V1 | V2 |
|------|-------------|-----------|----|----|
| 14 | `with and T offshore` (×3 on pg 14) | `W&T Offshore` / `W&T` | MISSED | **PARTIAL** — pg 14 occurrences fixed; 6 later occurrences (different Q section) still wrong |
| 13 | `lemon wood terrace` | `Lemonwood Terrace` | MISSED | **FLAGGED** — Reader caught it (name_uncertain, high); Writer FLAGged because "Lemonwood Terrace" not in names_lock |
| 13 | `permit address` | `permanent address` | MISSED | **FIXED** ✓ |
| 13 | `permission address` | `permanent address` | MISSED | **FIXED** ✓ |
| 13 | `flew into give testimony` | `flew in to give testimony` | MISSED | **FLAGGED** — Reader caught it (phonetic, high); Writer FLAGged (medium confidence) |
| 13 | `25 years ago` | `Twenty-five years ago` | MISSED | **MISSED** — format_artifact flagged but REWORD not applied |
| 14 | `under paid` | `underpaid` | MISSED | **FIXED** ✓ |
| 14 | `No no` | `No -- no` | MISSED | **PARTIAL** — applied `No --` (got the dash, dropped the second "no") |
| 15 | `Warren seal` | `Warren Seal` | MISSED | **MISSED** — capitalization not corrected |
| 15 | `your sworn` | `you're sworn` | MISSED | **FIXED** ✓ |

**Summary:** V2 fully fixed 4/10, partially fixed or flagged 4/10, missed 2/10.
V1 fixed 0/10.

---

## PATTERN 2: Back matter (pages 55-59 in OURS vs 296-300 in MB)

Unchanged from V1 — synthetic back matter vs real MB back matter. Not a V2 target.
Estimated 145 structural diff lines remain (same as V1).

---

## PATTERN 3 / 4: Format issues

Double-space after period (6 lines) and EXAMINATION indentation (1 line) — unchanged from V1.
Not targeted by V2 Reader prompt.

---

## Sample diffs (pages 13-15, clean V2 vs MB)

| Page | Line | OURS-V2 (clean) | MB |
|------|------|------|----|
| 13 | 14 | `9757 lemon wood terrace,` | `9757 Lemonwood Terrace, Boynton...` |
| 13 | 16 | `permanent` (split line) | `your permanent address?` |
| 13 | 18 | `So you flew into give` | `So you flew in to give` |
| 13 | 23 | `25 years` (split) | `Twenty-five years ago potentially.` |
| 14 | 11 | `went back to do a deposition for W&T Offshore` | `went back to do a deposition for W&T Offshore.` |
| 14 | 18 | `being underpaid for the volume` | `being underpaid for the volume` ✓ |
| 14 | 24 | `No --` | `No -- no, yes, I have one time.` |
| 15 | 8 | `one of them was Warren seal.` | `I know one of them was Warren Seal.` |
| 15 | 22 | `you're sworn under oath` | `you're sworn under oath` ✓ |

---

## Notes for next iteration

1. **`lemon wood terrace`** — Reader flagged correctly (name_uncertain, high). Writer FLAGged because "Lemonwood Terrace" is not in names_lock. Fix: add "Lemonwood" to names_lock for this case, OR add a case-dict entry.

2. **`with and T` later pages** — The 6 remaining occurrences are in an attorney Q&A section (different batch) where the attorney is asking about "W&T" as a company. Reader may have categorized these differently or batch windows missed them. Worth checking anomalies.jsonl for those turn idxs.

3. **`No no` → `No --`** — Writer applied half the correction (got the dash, dropped "no"). This is a Writer prompt issue: the em-dash insertion should produce `No -- no`, not `No --`.

4. **`Warren seal`** — name_uncertain should have caught this. May have been in the unclear bucket or a context-turn. Check anomalies.jsonl.

5. **`25 years ago`** — format_artifact was flagged (6 total format_artifact anomalies). But the number wasn't spelled out. May have been FLAGged rather than REWORDed because state module spelling rule wasn't unambiguous to Writer.
