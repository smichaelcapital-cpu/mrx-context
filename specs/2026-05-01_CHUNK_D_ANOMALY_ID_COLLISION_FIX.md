# CHUNK D — Fix anomaly_id cross-batch collision in proposal_mapper

Date: 2026-05-01
Author: Opus (architect)
Builder: Sonnet
Gate: Hard (unlocks the "positional joins locked" design decision from 2026-04-27 EOD handoff)

## Background

Surfaced during Chunk B' Lemonwood fix. `anomaly_id` resets to `a_0001` in every Stage 3.1
batch. `proposal_mapper.py` builds `anomaly_by_id` as a plain dict keyed on `anomaly_id`
only. Result: the last `a_0001` (from the final batch) overwrites every earlier `a_0001`.
Every batch-first proposal gets wrong confidence lookups.

Concrete impact on Lemonwood: turn 96 anomaly is `a_0001` confidence=high. Final batch also
has `a_0001` confidence=medium (turn 634). Lemonwood's marker came out as MB_REVIEW-VERIFY
(medium) when it should be MB_REVIEW-FIX: confident (high).

Scope of impact: Every batch-first proposal across all 10 V2 batches has wrong confidence.
~10 of 126 proposals (~8%) silently miscalibrated.

The 2026-04-27 EOD handoff locked "positional joins for proposals/decisions/anomalies (i,
not ID)." That decision is now provably wrong for anomalies because the V2 contract has more
anomalies than proposals (147 vs 126). This spec asks Opus to re-architect the join under
guidance.

## Goal

Recon the actual failure surface and propose a fix architecture. Do NOT modify production
code in this chunk. Output is a written proposal that Opus reviews.

## Recon (REQUIRED, in order)

### 1. Document current state precisely

Read and report:
- The exact current join logic in `src/stage5/proposal_mapper.py` — paste the relevant function(s)
- The exact field set on a proposal record from `proposals.json` — confirm `batch_id` is
  present at proposal level (recon from 2026-04-26 said yes)
- The exact field set on an anomaly record from `anomalies.jsonl` — does `batch_id` exist there?
- The exact field set on a decision record from `decisions.jsonl` — same question
- Count: how many `a_0001` collisions exist in the Halprin V2 anomalies file? Paste the
  turn_idx + confidence for each
- Count: same for `p_0001`, `p_0002`, etc. across batches in `proposals.json`

### 2. Inventory the affected code paths

Find every place that joins/looks up by `anomaly_id` or `proposal_id`:
- `proposal_mapper.py`
- `apply.py`
- Anywhere in `src/stage5/` and `src/mrx_engine_v1/stage3/`
- Test files that exercise these paths

Report the file:line for each.

### 3. Inventory the affected tests

Which tests would need fixture or assertion updates if the join key changes? List them.
Don't fix yet — just list.

### 4. Propose three architecture options

Sonnet writes up three real options with trade-offs. At minimum:

- **Option 1:** Keep IDs as-is, change join key to `(batch_id, anomaly_id)` tuple —
  minimum code surface, requires `batch_id` present everywhere
- **Option 2:** Make IDs globally unique at generation time in suggester — clean key,
  but rewrites all existing artifacts and changes the suggester contract
- **Option 3:** Sonnet's choice — anything else recon surfaces (e.g., generate compound
  IDs at write time, or join on `(turn_idx, token_span)`, or something Opus hasn't thought of)

For each option, describe:
- Code changes required (files + rough scope)
- Test changes required
- Whether existing artifacts (`proposals.json`, `anomalies.jsonl`) need regeneration or
  are still valid
- Backward compat with V1 baseline (`baselines/halprin_mini.OUR_FINAL.V1.2026-04-30.txt`)
- Risk to the Prime Directive (could this change reduce transcript accuracy?)

### 5. Sonnet's recommendation

After inventorying options, Sonnet recommends one with reasoning. Opus reviews.

## Acceptance criteria for THIS chunk

- Recon report posted to chat for Opus review
- Three architecture options written up
- Sonnet's recommendation stated
- **No code changes**
- **No commits**

If Opus approves the recommendation, a follow-up build spec will be written. The build is
a separate chunk.

## Out of scope for this chunk

- Any production code change
- Bug 2 (apply.py multi-token skip) — separate chunk
- Diff methodology lockdown — separate chunk
- Re-running pipeline

## Report back

Post recon findings + 3 options + recommendation as a single message in chat. Opus will
review and write the build spec.

---
*End of spec*
