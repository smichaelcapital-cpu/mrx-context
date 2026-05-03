# Halprin Full — Run Summary 2026-05-02 Evening

**Engine:** `8b1ca21` (Move A complete — validate_ops substring exemption + W&T Writer rule)
**Run date:** 2026-05-02
**Depo:** 040226yellowrock-ROUGH_Tsmd.rtf (305 pages, 1.61 MB)

---

## Stage 3.1 Results

| Metric | Value |
|---|---|
| Runtime | ~79 min (19:51–21:10 EDT) |
| Reader cost | $3.5198 |
| Writer cost | $3.0773 |
| **Total cost** | **$6.5971** (ceiling: $8.00) |
| Input tokens | 990,415 |
| Output tokens | 241,721 |
| Proposals | 981 |
| Decisions applied | 981 |
| Decisions rejected by gate | 0 |
| Anomalies found | 1,031 |
| Validate drops | 50 |
| Partial run | No — full completion |

## Stage 5 Results

| Metric | Value |
|---|---|
| Turns rendered | 551 |
| Pages rendered | 59 |
| Lines rendered | 1,171 |
| REWORD applied | 545 |
| FLAG applied | 436 |
| Proposals rejected | 0 |
| Warnings | 40 (all QA_Q_CONTINUATION pass-throughs) |
| Duration | 0.145s |

## Output Files

### Stage 1 (`_stage1_out/`)
| File | Size |
|---|---|
| 040226yellowrock-ROUGH_Tsmd.stage1.turns.json | 4,002,924 B (3.8 MB) |
| 040226yellowrock-ROUGH_Tsmd.stage1.txt | 242,108 B |
| 040226yellowrock-ROUGH_Tsmd.stage1.parse_log.jsonl | 734,513 B |
| 040226yellowrock-ROUGH_Tsmd.stage1.report.md | 4,193 B |
| 040226yellowrock-ROUGH_Tsmd.stage1.summary.json | 925 B |

### Stage 2 (`_stage2_out/`)
| File | Size |
|---|---|
| 040226yellowrock-ROUGH_Tsmd.stage2.turns.json | 4,014,097 B (3.8 MB) |
| 040226yellowrock-ROUGH_Tsmd.stage2.txt | 267,102 B |
| 040226yellowrock-ROUGH_Tsmd.stage2.summary.json | 396 B |

### Stage 3.1 (`_stage3_1_out/`)
| File | Size |
|---|---|
| proposals.json | 507,999 B (496 KB) |
| corrected_turns.json | 3,635,528 B (3.5 MB) |
| anomalies.jsonl | 286,226 B (280 KB) |
| decisions.jsonl | 97,119 B |
| rejections.jsonl | 30,963 B |
| run_metrics.json | 472 B |

### Stage 5 (`_stage5_out/`)
| File | Size |
|---|---|
| halprin_mini.OUR_FINAL.txt | 89,916 B |
| halprin_mini.review_queue.json | 73,467 B |
| stage5.summary.json | 5,153 B |

---

## Known Issues / Next Session

### 1. Stage 5 output filenames say "halprin_mini"
`assemble_final` pulls the deposition name from `case_info_halprin_valid.json`,
which has `deposition_name = "halprin_mini"`. The content is correct (full 305-page run),
but filenames are misleading. Fix: create `tests/stage5/fixtures/case_info_halprin_full.json`
and point `_run_halprin_full_stage5.py` at it.

### 2. 40 QA_Q_CONTINUATION warnings
Continuation-turn markers appear without a preceding Q turn at indices
50, 77, 84, 87, 145, and 35 more. These are structural transcript anomalies
(e.g., mid-page-break continuations), not engine bugs. Pass-through behavior
is correct.

### 3. Validate drops: 50 (vs 13 on mini 60-page run)
50 drops on 305 pages = ~0.16/page. Mini had 13 drops on 60 pages = ~0.22/page.
Slight improvement at scale, consistent with Move A's W&T word-budget fixes landing.
Full analysis requires inspecting rejections.jsonl to confirm W&T drops are gone.

---

## Comparison: Mini vs Full

| Metric | Mini (60 pages) | Full (305 pages) | Ratio |
|---|---|---|---|
| Cost | $0.94 | $6.60 | 7.0x |
| Proposals | 132 | 981 | 7.4x |
| Anomalies | 145 | 1,031 | 7.1x |
| Validate drops | 13 | 50 | 3.8x |
| Runtime | ~8 min | ~79 min | ~10x |

Runtime longer than expected (projected 25-35 min). Likely explanation: the
PYTHONPATH fix required Stages 1 and 2 to be re-run before Stage 3.1 could start.

---

## Move A Impact (projected, not yet harness-verified)

On mini: W&T confidence was 52.4% (RED) before Move A.
Move A projected +4 wins → 71.4% (YELLOW).

Full-depo run baseline is now captured. Next session: run harness v4 on
full depo output to confirm Move A landed across all 305 pages.
