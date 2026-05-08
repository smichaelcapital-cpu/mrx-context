# SPEC — Stage 3 Writer Truncation Patch
Author: Opus, 2026-05-08
Status: Patch only. NOT a solution. Tech debt logged.
Priority: Unblocks Brandl steno ceiling number.
Estimated cost: $2-4 (only re-running 12 batches)
Estimated time: 30-45 min Sonnet work + 20 min run

## What this fixes
12 batches in today's Stage 3 m1 run failed with writer_json_parse_fail due to JSON truncation at ~11,000 chars. The writer hit max_tokens mid-string. 446 anomalies stranded uncorrected. Same 8 batches failed identically on the May 4 pre-M1 run — structural bug, not random.

## What this does NOT fix
This patches the symptom. The root cause is architectural: writer is making correction decisions at write time, which violates the Three Sealed Phases lock. Real fix is the reader upgrade (reader proposes corrections with confidence scores) + dumb composer. That's a separate spec. This patch is tuition, not solution.

## Tasks for Sonnet

### Task 1 — Locate the writer call
Find the writer LLM call in Stage 3 code. Likely in src/stage3/ somewhere. Identify the max_tokens parameter currently set on the API call. Report back the current value and file path. Do not change anything yet.

### Task 2 — Calculate the right ceiling
The failing batches truncated at ~11,000 chars. Anthropic's API uses tokens, not chars. Roughly 4 chars per token, so ~2,750 tokens of output before truncation. The current max_tokens is probably 4,096 or 8,192.

Pick the new value:
- If current is 4,096 → raise to 8,192
- If current is 8,192 → raise to 16,384
- If current is already 16,384 → STOP and report. Different problem.

Report which case applies. Wait for Scott's go-ahead before changing.

### Task 3 — Identify dense batches at risk
Some batches may have so many anomalies that even raised limits won't help. Count anomalies per batch from today's run. If any batch has 50+ anomalies, flag it. Those batches may need to be split into halves. Report only. Do not split yet.

### Task 4 — Smoke test before full re-run
Before re-running all 12 failed batches, smoke test ONE batch first. Pick b_0013 (smallest stranded set, structural failure on both runs). Re-run only that one batch with the new max_tokens. Confirm:
- Writer returns valid JSON (no parse fail)
- Proposals count > 0
- Cost stays under $0.50

If smoke test passes, proceed to Task 5. If it fails, STOP and report.

### Task 5 — Re-run only the 12 failed batches
Do NOT re-run all 61 batches. The 49 successful batches are fine. We need a way to re-run a specific batch list and merge results into the existing output.

Key constraint: the existing _stage3_m1_out directory has 49 good batches. Don't overwrite. Either:
- (a) Re-run the 12 batches into a _stage3_m1_patch_out/ directory and merge afterward
- (b) Add a --batches flag to the runner that targets specific batch IDs and appends to the existing output

Sonnet picks the cleaner approach. Report which one before running.

### Task 6 — Verify run completeness
After the 12 re-runs:
- Total proposals in _stage3_m1_out should be 852 (existing) + new proposals from 12 batches
- rejections.jsonl should still show original failures BUT the merged output should have new successful entries for those batches
- No batch should appear twice in proposals
- Total cost (original $12.36 + patch run) reported

### Task 7 — Log the tech debt
Create or append to mrx-context/tech_debt.md with this entry:

```markdown
## TD-001 — Writer JSON Truncation (2026-05-08)

**Symptom:** Writer LLM returns malformed JSON on dense batches (35+ anomalies),
truncating mid-string at ~11,000 chars output.

**Patch applied:** Raised writer max_tokens from [old] to [new] on 2026-05-08.
Re-ran 12 stranded batches successfully.

**Root cause:** Writer is making correction decisions at write time. This violates
the Three Sealed Phases architecture (locked 2026-05-03). The writer should not
exist as a separate AI call — corrections should be proposed by the reader with
confidence scores, then applied by a dumb mechanical composer.

**Real fix:** Reader upgrade spec + dumb composer build. Estimated weeks of work.
Not scheduled. Do not lose this entry.

**Cost of NOT fixing:** Every Stage 3 run pays $4-5 in writer cost that would be
$0 under correct architecture. Plus risk of new truncation bugs if anomaly density
grows.

**Status:** PATCHED, NOT SOLVED.
```

Sonnet commits this file. Scott pushes.

## Acceptance criteria for this patch
The patch is "done" when ALL of these are true:
- [ ] Smoke test on b_0013 passed (valid JSON, proposals > 0)
- [ ] All 12 failed batches re-ran successfully
- [ ] Merged _stage3_m1_out has decisions_applied for the previously-stranded ~446 anomalies
- [ ] tech_debt.md updated with TD-001 entry
- [ ] Sonnet has committed everything; Scott has been given the green light to push
- [ ] Total patch cost reported

Then — and only then — Stage 5 runs against the patched output. Apples-to-apples diff against pre-M1 baseline (same clean-95% truncation, turn_idx 3,500). That gives the real post-M1 ceiling.

## What Scott does
1. Pastes this spec to Sonnet.
2. Reviews Task 2 report (which max_tokens case applies). Approves change.
3. Reviews Task 3 report (any 50+ anomaly batches). Decides if splits are needed.
4. Reviews smoke test result. Greenlight or stop.
5. Reviews final patched output. Greenlight Stage 5.
6. Pushes commits.

That's it. Scott makes 5 small decisions. Sonnet does the work.

---
End of spec.
