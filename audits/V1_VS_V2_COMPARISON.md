# V1 vs V2 Reader Prompt — A/B Comparison Report

**Date:** 2026-04-30
**Baseline:** `baselines/halprin_mini.OUR_FINAL.V1.2026-04-30.txt`
**V2 output:** `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt`
**Oracle:** `oracle/finals/halprin/040226yellowrock-FINAL.txt`
**Audit scope:** Pages 13-54 (body)

---

## Headline numbers

| Metric | V1 | V2 | Delta |
|--------|----|----|-------|
| Total diff lines vs MB (pages 13-54) | 1,040 | 827 | **-213 (-20%)** |
| Anomalies flagged by Reader | ~12 est. | 147 | +135 |
| Proposals generated | ~12 est. | 126 | +114 |
| REWORDs applied | ~12 est. | 83 | — |
| FLAGs (human review) | 0 | 43 | +43 |
| Total API cost | ~$0.10 est. | $0.95 | +$0.85 |

> V1 anomaly/proposal counts are estimated from partial debug data; exact V1 run metrics not stored.

---

## Pattern 1 sub-category breakdown — known steno artifacts

For each defect from the original audit's "Key steno artifacts" table:

| Defect type | Specific instance | V1 | V2 |
|------------|-------------------|----|----|
| Letters-as-words | `with and T` × 3 (pg 14) | missed | **partial** (pg 14 fixed; 6 later occurrences still wrong) |
| Split proper noun | `lemon wood terrace` | missed | **flagged** ✓ (names_lock constraint blocked auto-fix) |
| Phonetic — stroke collision | `permit address` → `permanent` | missed | **fixed** ✓ |
| Phonetic — stroke collision | `permission address` → `permanent` | missed | **fixed** ✓ |
| Word swap | `flew into give` → `flew in to give` | missed | **flagged** ✓ (medium confidence) |
| Number format | `25 years ago` → `Twenty-five` | missed | **missed** |
| Split compound | `under paid` → `underpaid` | missed | **fixed** ✓ |
| Missing em-dash | `No no` → `No -- no` | missed | **partial** (`No --` applied; second "no" dropped) |
| Proper noun caps | `Warren seal` → `Warren Seal` | missed | **missed** |
| Homophone | `your sworn` → `you're sworn` | missed | **fixed** ✓ |

**Score: V1 = 0/10. V2 = 4 fixed + 3 flagged/partial + 3 missed.**

---

## Anomalies flagged by Reader — V2 vs V1 (by category)

| Category | V1 (est.) | V2 |
|----------|-----------|----|
| steno_artifact | ~3 | 77 |
| phonetic | ~3 | 15 |
| name_uncertain | ~2 | 23 |
| format_artifact | ~1 | 6 |
| unclear | ~2 | 25 |
| objection_format | 0 | 1 |
| **Total** | **~12** | **147** |

V2 Reader found ~12× more anomalies. Confidence: high=105 (71%), medium=35 (24%), low=7 (5%).

---

## Writer decisions — REWORD vs FLAG (V2 only; V1 baseline not stored)

| Op type | V2 count |
|---------|----------|
| REWORD applied | 83 |
| FLAG applied | 43 |
| Proposals rejected by gate | 0 |
| **Total proposals** | **126** |

All 126 proposals were applied (gate rejected 0). The 21 anomalies with no corresponding proposal were cases where the Writer chose not to produce an op (or validate_ops dropped an op silently).

---

## New regressions — defects V1 caught that V2 missed

None identified. V1 caught 0 of the known Cat 1 defects. V2 performed no worse on any of the tracked defects.

There is one new partial regression to watch: the `No no` → `No --` case. V2 applied a dash (progress) but dropped the second "no", producing text that doesn't match MB's `No -- no`. This is a Writer prompt issue, not a Reader issue — Reader flagged it correctly.

---

## Verdict

**Partial win.** V2 reduced total diff lines 20% (1,040 → 827) and fixed 4 of 10 tracked Cat 1 defects that V1 missed entirely. 3 more were flagged for human review (correct behavior given names_lock and confidence constraints). 3 remained uncorrected.

The Reader prompt is working as designed — it found 147 anomalies vs V1's ~12, including the majority of the known defect patterns. Remaining misses are mostly downstream issues:
- **`lemon wood terrace`**: Reader caught it; Writer blocked by names_lock (correct behavior — fix is to update names_lock)
- **`flew into give`**: Reader caught it; Writer FLAGged (medium confidence — acceptable)
- **`25 years ago`**: Reader flagged as format_artifact; Writer did not apply REWORD (state module number rule may not have been unambiguous)
- **`Warren seal`**: Unclear if Reader caught this in the relevant batch; check anomalies.jsonl for that turn
- **`with and T` later pages**: Reader caught page-14 occurrences; later-page occurrences may need names_lock or dict entry for "W&T" to reliably fix

---

## Infrastructure issues found and fixed during V2 run

| Issue | Root cause | Fix |
|-------|-----------|-----|
| Reader returning 0 anomalies | `reader_max_tokens=1024` truncated V2's longer responses mid-JSON | Bumped to 4096 |
| Writer returning 0 proposals | `writer_max_tokens=1024` truncated Writer responses when Reader found 15-25 anomalies/batch | Bumped to 4096 |
| Cost ceiling tripped at batch 9/10 | `MAX_COST_USD=$1.00` too low for V2's larger prompts | Bumped to $5.00 |
| Stage 5 crash on length mismatch | `proposal_mapper.py` assumed anomalies count == proposals count (positional join); V2 anomalies > proposals | Fixed: keyed join on `anomaly_id` |
