# CHUNK B' — Lemonwood Terrace → NAMES_LOCK

Date: 2026-05-01
Author: Opus (architect)
Builder: Sonnet
Gate: Soft (single-name addition, no architecture change, no prompt change)

## Background

V2 Reader correctly flagged "lemon wood terrace" as a name uncertainty on Halprin mini,
but did NOT auto-correct it because "Lemonwood Terrace" is not in NAMES_LOCK. The result
was a FLAG instead of a REWORD.

Scott confirmed the canonical spelling from the source address:
"9757 Lemonwood Terrace, Boynton Beach" — capital L, capital T, one word "Lemonwood".

This is the same NAMES_LOCK list the runner uses to give Reader a list of locked spellings
(Halprin, Caughey, Garner, Muir, Guastella, Lexitas, Westlake, Eagle, Calcasieu, Somerset,
Chevron — 11 entries per the 2026-04-26 handoff).

## Goal

Add "Lemonwood Terrace" to NAMES_LOCK in `_run_halprin_mini.py`, re-run Halprin mini through
the pipeline, verify the existing "lemon wood terrace" defect now becomes a REWORD with high
confidence (not just a FLAG).

## Pre-build recon (REQUIRED)

1. Open `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_run_halprin_mini.py`
2. Locate the NAMES_LOCK list. Confirm current count is 11 entries and report the exact list.
3. Confirm "Lemonwood Terrace" is NOT already present.
4. Locate the V2 anomaly for "lemon wood terrace" in `_stage3_1_out/anomalies.jsonl` — report
   the turn_idx, token_span, confidence, and reader_note. Confirm it currently exists as a
   FLAG (not REWORD) in proposals.json.

After recon, report findings to Opus. Do not edit yet.

## Build (after Opus approves)

1. Add "Lemonwood Terrace" to NAMES_LOCK as the 12th entry. Match the existing
   format/quoting style of the list.
2. Re-run Halprin mini end-to-end:
   - Run Stage 1 + 2 if needed (or use existing `_pipeline_out/` if unchanged)
   - Run Block H (Stage 3.1) fresh — this is the test, since NAMES_LOCK is consumed by the Reader
   - Run Stage 5 to produce OUR_FINAL.txt
3. Note the run cost. Expected ~$0.95 like last V2 run. If significantly higher, flag.

## Acceptance criteria

- NAMES_LOCK now has 12 entries including "Lemonwood Terrace"
- New `proposals.json` contains a REWORD entry where `before = "lemon wood terrace"` (or
  similar tokenization) and `after = "Lemonwood Terrace"`
- New `OUR_FINAL.txt` shows "Lemonwood Terrace" at the relevant turn (no FLAG marker, or a
  `MB_REVIEW-FIX:` confident marker if the proposal got high confidence)
- `pytest tests/ -q` still shows 510 passing (no regression)
- Diff line count vs MB FINAL — report new total. Expected: ~826 (down from 827, since 1
  defect fixed). If much different, investigate before claiming success.
- Commit message: `feat(stage3): add Lemonwood Terrace to NAMES_LOCK (V2 miss fix #1)`

## Out of scope

- V2 prompt changes
- Other V2 misses (with and T, No no, Warren seal, 25 years ago) — those come later as
  separate chunks
- Any production code outside the runner's NAMES_LOCK list

## Report back

After build:
- Final pytest summary
- New diff line count vs MB FINAL
- The specific REWORD entry from new `proposals.json` (paste it)
- Run cost
- Commit hash

---
*End of spec*
