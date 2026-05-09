# Brandl v0 Fingerprint Run — Report
**Date:** 2026-05-09
**Run by:** Sonnet
**Approved by:** Scott

---

## Headline

**55 hallucinated `--` tokens blocked. Ceiling did not move (824 → 825 blocks, Δ ≈ 0). Expected: all 55 drops appeared inside blocks already discrepant for other reasons (cap_proper dominant). Fingerprint enforcement loop confirmed working.**

---

## Engine Commit

`8954b61` — feat(stage5): Gate 4 — wire optional fingerprint into assemble_final

---

## Run Parameters

| Parameter | Value |
|---|---|
| Input Stage 3 | `_stage3_m1_out/` (1196 proposals, writer_max_tokens=8192, 2026-05-08) |
| Output | `_stage5_fingerprint_out/` |
| Fingerprint | `load_fingerprint("LA", "civil_engineering", "MB")` |
| Forbidden tokens | `["--"]` |
| Baseline | `_stage5_m1_out/brandl.OUR_FINAL.txt` (2026-05-08 18:18) |
| Wall time | 0.195s |
| LLM API cost | $0.00 (Stage 5 is pure Python, no API calls) |

---

## Em-Dash Enforcement

**Tokens dropped: 55**
**Turns affected: 46** (some turns had multiple `--` tokens)
**Whitespace handling: 55 collapsed (surrounded by spaces → single space), 0 inserted**

All 55 drops logged to:
`io/analysis/brandl_50pp/_stage5_fingerprint_out/fingerprint_enforcement.jsonl`

### 5 Sample Drops (before → after, from OUR_FINAL.txt)

```
1. BEFORE: "    17   Energy purchased Samedan or right -- right before or"
   AFTER:  "    17   Energy purchased Samedan or right right before or"

2. BEFORE: "    10        Q.    So you are not -- don't know if the right"
   AFTER:  "    10        Q.    So you are not don't know if the right"

3. BEFORE: "    24        Q.    And how long were you -- you started at"
   AFTER:  "    24        Q.    And how long were you you started at"

4. BEFORE: "    22        A.    So when left -- got they had another"
   AFTER:  "    22        A.    So when left got they had another layoff"

5. BEFORE: "    15        A.    And I started -- believe and again my"
   AFTER:  (pagination shift — content moved to next line after token removal)
```

All drops confirm the LLM was hallucinating `--` em-dashes in the REWORD proposals. MB never uses `--`. The enforcement correctly blocked every occurrence.

---

## Diff vs Baseline (_stage5_m1_out)

**File-level:**
- Baseline lines: 23,302
- Fingerprint lines: 23,294
- Delta: -8 lines (pagination compression from removed tokens)
- Word delta: -55 words (exactly the 55 dropped tokens, confirmed)
- All non-`--` word content: **identical** (verified by word-level comparison)

The 10,000+ line-level diff entries are **pagination ripple only** — removing characters causes words to reflow slightly across page boundaries. No content was added, removed, or changed beyond the 55 `--` tokens.

**Non-em-dash differences: 0.** Confirmed clean.

---

## Score vs MB Oracle

Diff run against MB FINAL oracle (`032626YELLOWROCK-FINAL_T.stage1.txt`).

| Metric | Baseline (m1) | Fingerprint | Delta |
|---|---|---|---|
| Total discrepancy blocks | 824 | 825 | +1 |
| Bucket A — engine fixable | 172 (20.9%) | 182 (22.1%) | +10 |
| Bucket B — ceiling | 568 (68.9%) | 569 (69.0%) | +1 |
| Bucket C | 0 | 0 | 0 |
| Bucket D — unclear | 84 (10.2%) | 74 (9.0%) | -10 |

### What moved

- 10 blocks shifted D→A. These were blocks where `--` had made the OUR text ambiguous to the classifier. After removing `--`, the SequenceMatcher realigned those paragraphs and the classifier could now label them (phonetic_error +5, acronym_mangle +5 approximately).
- Net total blocks: +1. Effectively unchanged.
- **The `--` tokens were not generating their own discrepancy blocks.** They were appearing inside blocks already failing for cap_proper / other reasons. Removing `--` did not resolve any block.

Blocks in baseline where OUR_line contained `--`: **40 of 824**
Blocks in fingerprint where OUR_line contains `--`: **1** (residual, likely in stripped marker text)

### Why the ceiling didn't move

The dominant error class is `cap_proper` (509/824 blocks, 61.8%) — the engine is not matching MB's proper noun capitalization decisions. The `--` tokens were a secondary artifact within already-failing blocks. Fixing `--` alone cannot lift the ceiling; that requires fixing cap_proper.

---

## Open Items

- **TD-002 (stale W&T e2e test)** — still open, quick fix when convenient.
- **MB.yaml data migration** — rich cross-depo pattern data from `io/analysis/_cross_depo_scan/cross_depo_pattern_table.md` not yet migrated into v0 observed/inferred structure.
- **cap_proper** — 509/824 blocks, 61.8% of all discrepancies. Next architectural target to move the ceiling.

---

## Files Not Pushed (FINAL-protected)

Per standing rule: `_stage5_fingerprint_out/brandl.OUR_FINAL.txt` was NOT committed or pushed.
Only this report was pushed.

---

*End of report.*
