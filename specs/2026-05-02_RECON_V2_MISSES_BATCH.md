# RECON — V2 Misses Batch

**Date:** 2026-05-02 (overnight session, written by Opus 2026-05-01 EOD)
**Author:** Opus
**Builder:** Sonnet
**Owner:** Scott
**Type:** Recon only. No code. No $. Output is a markdown report Opus reads to design the bundle fix spec.

---

## TRUTH SOURCES

V2 Stage 3.1 artifacts (read-only for this recon):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage3_1_out\anomalies.jsonl
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage3_1_out\proposals.json
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage3_1_out\decisions.jsonl

V2 final output (for cross-reference):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt

Stage 2 input (for cross-reference of Reader input):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage2_out\halprin_mini.stage2.txt

V2 Reader prompt (for understanding what Reader was told to look for):
  https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/stage3_1/READER_PROMPT_V2.md

NAMES_LOCK current state:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_run_halprin_mini.py
  (search for `NAMES_LOCK` constant)

---

## ONE-LINE GOAL

For each of three V2 misses (`with and T`, `Warren seal`, `25 years ago`), determine: did Reader flag it? If yes, what did Reader say + what did Writer do? If no, why not? Output drives the next spec's fix design (NAMES_LOCK add vs prompt patch vs state module).

---

## RECON TASKS

### Task 1 — `with and T` (6+ later occurrences)

V2 partial-fix: Reader caught batch 1 (page 14, ~3 occurrences) and Writer rewrote to "W&T". V2 missed 6 later occurrences in attorney Q section (per HANDOFF_LOG 2026-04-30 v02 entry).

For Sonnet:
1. Grep `_stage2_out/halprin_mini.stage2.txt` for "with and T" — list every turn_idx that contains it. Quote a 1-sentence snippet for context.
2. For each turn_idx in that list, look up anomalies.jsonl and report:
   - Did Reader flag it (yes / no)?
   - If yes: anomaly_id, category, confidence, reader_note (full text)
   - If no: turn_idx and "no anomaly recorded"
3. For every "yes" above, look up proposals.json and report:
   - proposal_id, op_type, before, after, reason, source

Output format: a table.

### Task 2 — `Warren seal`

V2 missed entirely (per V1_VS_V2_COMPARISON.md scorecard).

For Sonnet:
1. Grep `_stage2_out/halprin_mini.stage2.txt` for "Warren seal" (case-insensitive). List turn_idx(s).
2. For each turn_idx, check anomalies.jsonl: did Reader flag anything on that turn? Quote any anomaly records that touch that turn (any token_span on that turn_idx, not just spans that overlap "Warren seal").
3. Check NAMES_LOCK in `_run_halprin_mini.py` — is "Warren Seal" present? Quote the People category.

Output: short paragraph + the NAMES_LOCK quote.

### Task 3 — `25 years ago`

V2 missed (per scorecard) but a related "format_artifact" category exists in V2 (6 records per HANDOFF_LOG 2026-04-30 v02 open items).

For Sonnet:
1. Grep `_stage2_out/halprin_mini.stage2.txt` for "25 years ago". List turn_idx.
2. Check anomalies.jsonl on that turn_idx — was anything flagged? If yes, quote the full record.
3. Independently: grep anomalies.jsonl for `category: format_artifact` — list ALL 6 records (anomaly_id, turn_idx, token_span, reader_note, confidence).  We want to see what Reader's number-format pattern looks like in practice.
4. Quote the section of READER_PROMPT_V2.md that addresses number formatting (search for "number", "spell", "twenty-five", or "format_artifact"). If no such section exists, say so explicitly.

Output: table for items 1-3, prompt quote for item 4.

### Task 4 — Sanity check on `No no`

V2 produced "No --" instead of "No -- no" (Writer truncation, per scorecard). Quick recon to confirm before we patch the Writer.

For Sonnet:
1. Grep `_stage2_out/halprin_mini.stage2.txt` for "No no" — list turn_idx.
2. Look up anomalies.jsonl on that turn — what did Reader say?
3. Look up proposals.json — what did Writer propose? Quote the full proposal record (we need to see if Writer's `after` field already contains the truncation, or if truncation happens later).

Output: table.

### Task 5 — Cross-cutting: confirm Bug 1 fix didn't change the anomaly data

Bug 1 (Chunk D, commit 1519912) was a read-side fix only — it changed how proposal_mapper.py joins anomalies to proposals. It did NOT modify anomalies.jsonl or proposals.json on disk.

For Sonnet:
1. Confirm the anomalies.jsonl and proposals.json files we're reading in this recon are the same V2 artifacts that produced the V2 audit (no re-run happened between then and now).
2. Quick way: check file modification timestamps. If they match the 2026-04-30 V2 deployment timestamps from HANDOFF_LOG.md, we're good.

Output: 1-sentence confirmation + timestamps.

---

## ACCEPTANCE CRITERIA

1. One markdown report posted by Sonnet, structured by Task 1 → Task 5 above.
2. Tables filled in with actual data (not placeholders).
3. Direct quotes where requested (Reader notes, NAMES_LOCK contents, prompt sections).
4. No code changes. No $. No git operations beyond the spec save + push.

---

## END-OF-CHUNK LOG ENTRY (Sonnet appends to HANDOFF_LOG.md after recon ships)

Append to current 2026-05-01 session block:

```
RECON — V2 misses batch (DONE)
Status: Recon complete. Report at [link to wherever Sonnet posts it].
Findings summary (one line each):
  - with and T (6 later): [Reader flagged? / Reader silent? + brief]
  - Warren seal: [Reader flagged? + NAMES_LOCK status]
  - 25 years ago: [Reader flagged? + format_artifact count]
  - No no: [Writer proposal after value]
Bug 1 fix did/did not change anomaly data on disk: [confirmed].
Drives next spec: [bundle fix design — Opus picks fix type per item].
```

---

## WHERE TO POST THE REPORT

Save the recon report as a new file:
  C:\Users\scott\OneDrive\Documents\mrx-context\specs\results\2026-05-02_RECON_V2_MISSES_RESULTS.md

Commit, push, reply with raw URL. Opus reads it directly.

— End of Recon spec —
