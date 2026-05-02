# CHUNK D — Bug 1 Natural-Key Join Fix

**Date:** 2026-05-02 (overnight session, written by Opus 2026-05-01 EOD)
**Author:** Opus
**Builder:** Sonnet
**Owner:** Scott
**Type:** Code-only fix. No $ run required. No prompt changes.

---

## TRUTH SOURCES

Engine repo:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\

File to fix:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\proposal_mapper.py

Tests to update:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\stage5\test_proposal_mapper.py

Related file (logger.warning add):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage3\apply.py

Decision log reference (read before building):
  https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_LOG.md
  Section: "DECISION LOG — Anomaly join key architecture (2026-05-01)"

---

## ONE-LINE GOAL

Replace `anomaly_by_id = {a.anomaly_id: a for a in anomalies}` with a natural-key dict keyed on `(turn_idx, token_span)` so cross-batch `anomaly_id` collisions stop overwriting earlier anomalies.

---

## WHY (the bug, in plain English)

`anomaly_id` resets to `a_0001` at the start of every Stage 3.1 batch. V2's 10 batches produce 10 different `a_0001` records (one per batch, all different turns). The current code builds a plain dict keyed on `anomaly_id`, so the LAST `a_0001` written wins. Earlier `a_0001`s — including the Lemonwood Terrace anomaly at turn 96 with confidence=high — get overwritten by later batches' `a_0001` (turn 634, confidence=medium).

Result: ~10 of 126 proposals get wrong confidence. Lemonwood rendered as `MB_REVIEW-VERIFY` instead of `MB_REVIEW-FIX: confident`.

The natural join key is `(turn_idx, token_span)` because Writer is structurally constrained to cite Reader's exact span. `anomaly_id` was always a surrogate for that relationship.

Full reasoning + alternatives considered + revisit triggers: see decision log link above.

---

## RECON CHECKPOINT (Sonnet does this BEFORE writing any code)

**STOP after recon. Post results in chat. Wait for Opus approval before building.**

Recon tasks:

1. **Confirm bug presence in current repo state.** Open `src/stage5/proposal_mapper.py`. Find the `build_application_map()` function. Locate the line that builds the anomaly lookup dict (currently keyed on `anomaly_id`). Quote the line + surrounding 5 lines.

2. **Count the collisions in current Halprin V2 artifacts.** Read `io/analysis/halprin_mini/_stage3_1_out/anomalies.jsonl`. Count how many distinct `anomaly_id` values appear, and how many records share each ID. Report:
   - Total anomaly records
   - Distinct `anomaly_id` values
   - Number of `anomaly_id` values that appear more than once
   - Sample collision: e.g., "a_0001 appears in 10 records on turns [96, 267, 380, ...] with confidences [high, medium, medium, ...]"

3. **Confirm `(turn_idx, token_span)` is unique across all anomalies in current data.** Same anomalies.jsonl. Build the natural key for every record. Report:
   - Total records: N
   - Distinct natural keys: M
   - If N != M, list every duplicate natural key with the anomaly_ids and turn_idxs involved

   **If N != M, STOP and flag to Opus before continuing.** That means the natural-key assumption doesn't hold and Option 3 needs revisit.

4. **Inventory existing tests that touch `anomaly_by_id` or join-by-anomaly-id.** Grep `tests/stage5/` for `anomaly_id` and report which tests reference the join-key behavior. We need to know which tests will need updating.

5. **Inspect `src/stage3/apply.py` ApplyHardBlock catch block in the runner.** The runner catches `ApplyHardBlock` exceptions and silently sets `corrected_turns = list(turns)`. Find that catch block. Quote it + surrounding 5 lines. We're adding a `logger.warning` here.

Post the recon report in chat. Don't write any code yet.

---

## BUILD STEPS (after Opus approves recon)

### Step 1: Update `src/stage5/proposal_mapper.py`

Find the existing line:

```python
anomaly_by_id = {a.anomaly_id: a for a in anomalies}
```

Replace with:

```python
# NATURAL-KEY JOIN (2026-05-02, Chunk D — Bug 1 fix)
# anomaly_id resets to a_0001 each Stage 3.1 batch, so cross-batch
# collisions overwrite earlier anomalies in a plain {anomaly_id: anomaly}
# dict. The natural join key is (turn_idx, token_span) because Writer
# is structurally constrained to cite Reader's exact span.
# See: mrx-context HANDOFF_LOG.md "DECISION LOG — Anomaly join key
# architecture (2026-05-01)" for full reasoning + revisit triggers.
anomaly_by_natural_key = {
    (a.turn_idx, tuple(a.token_span)): a for a in anomalies
}

# Edge case guard: if two anomalies share (turn_idx, token_span) on
# the same turn, the dict comp silently drops one. The natural-key
# assumption depends on Reader producing distinct spans per turn.
# If this fires, Option 3 needs revisit (see decision log).
if len(anomaly_by_natural_key) != len(anomalies):
    raise ValueError(
        f"Natural-key collision: {len(anomalies)} anomalies "
        f"reduced to {len(anomaly_by_natural_key)} unique "
        f"(turn_idx, token_span) pairs. Two anomalies share the "
        f"same span on the same turn — this violates the natural-key "
        f"assumption from 2026-05-01 decision log."
    )
```

Find every reference to `anomaly_by_id` downstream in the same function. Replace each with a lookup against `anomaly_by_natural_key` using `(proposal.turn_idx, tuple(proposal.token_span))` as the key.

The error message when a proposal can't find its matching anomaly should change from `"unknown anomaly_id"` to `"unknown natural key (turn_idx, token_span)"`. Include the actual key value in the error string for debugging.

### Step 2: Update `src/stage3/apply.py` (Bug 2 visibility)

In the runner's catch block for `ApplyHardBlock`, add a `logger.warning` BEFORE the silent fallback:

```python
except ApplyHardBlock as e:
    logger.warning(
        "ApplyHardBlock caught — corrected_turns.json will be a "
        "no-op (Stage 2 text passed through unchanged). This is "
        "Bug 2 from 2026-05-01 (multi-token apply constraint + "
        "proposal_id collision). Stage 5 re-applies proposals from "
        "scratch so OUR_FINAL.txt is still correct, but the "
        "intermediate artifact is stale. Error: %s",
        e
    )
    corrected_turns = list(turns)
```

Match the existing logger import style in apply.py. If apply.py doesn't have a logger imported, add `import logging; logger = logging.getLogger(__name__)` at module top.

### Step 3: Update `tests/stage5/test_proposal_mapper.py`

Find the test currently expecting `match="unknown anomaly_id"`. Update the assertion to `match="unknown natural key"` (or whatever exact string the new error message uses — keep the assertion regex generous enough to survive minor wording changes).

If recon turned up additional tests that reference `anomaly_id`-based join behavior, update them per Sonnet's judgment. Each update should preserve the test's intent (i.e., the test still tests what it was testing, just against the new join key).

If a test fundamentally tests the old behavior in a way that doesn't translate, mark it `@pytest.mark.skip(reason="Superseded by natural-key join — see Chunk D 2026-05-02")` and flag in the build report. Do not delete tests.

### Step 4: Add a new test for the edge-case guard

In `tests/stage5/test_proposal_mapper.py`, add a test that constructs two anomalies sharing the same `(turn_idx, token_span)` and asserts that `build_application_map()` raises `ValueError` matching `"Natural-key collision"`.

Use minimal fixtures — two anomaly objects, no proposals needed, just the dict-build path.

---

## ACCEPTANCE CRITERIA

1. `pytest tests/ -q` reports all tests passing (target: >= 510 minus any tests that became `@pytest.mark.skip`, plus 1 new collision-guard test).
2. The new test for the natural-key collision guard passes.
3. Stage 5 OUR_FINAL.txt re-render (no $ run, just Stage 5 against existing _stage3_1_out/) shows Lemonwood Terrace turn 96 marker as `{{MB_REVIEW-FIX: confident — ...}}` instead of `{{MB_REVIEW-VERIFY: ...}}`. This is the Bug 1 visible win.
4. `git status` shows only the three files listed in Build Steps modified (proposal_mapper.py, apply.py, test_proposal_mapper.py), plus any tests Sonnet had to update per recon findings.
5. No re-run of Stage 3.1 required. No Anthropic API calls. $0.

---

## VERIFICATION STEPS (Sonnet runs these and reports)

1. `pytest tests/ -q` — count passed/failed/skipped, report.
2. Run Stage 5 in isolation against existing `_stage3_1_out/` directory:
```cmd
   cd C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
   python -m src.stage5.assemble_final --input io/analysis/halprin_mini --output io/analysis/halprin_mini/_stage5_out
```
   (Use whatever the canonical Stage 5 invocation is — check the runner script if unsure.)
3. Open `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt`. Find turn 96 (search for "Lemonwood Terrace" or the line containing it). Quote the marker. Report whether it's `MB_REVIEW-FIX: confident` (success) or `MB_REVIEW-VERIFY` (failure — flag to Opus).
4. Spot-check 3-5 other previously-applied proposals to confirm their markers haven't regressed. Pick any 3 from earlier batches. Report turn_idx + marker type.

---

## END-OF-CHUNK LOG ENTRY (Sonnet appends to HANDOFF_LOG.md after ship)

Append to current 2026-05-01 session block — do NOT create a new dated entry:

```
CHUNK D — Bug 1 natural-key join fix (SHIPPED)
Status: Complete. Pushed by Scott. [N] tests passing.
What it did: Replaced {anomaly_id: anomaly} dict in proposal_mapper.py
with {(turn_idx, token_span): anomaly}. Adds collision guard that
raises if two anomalies ever share the same span on the same turn.
Adds logger.warning in apply.py's ApplyHardBlock catch block for
Bug 2 visibility.
Verification:
  - pytest: [N] passing, [M] skipped (skips: [list], reason: superseded by natural-key path)
  - Stage 5 re-render against existing _stage3_1_out/: Lemonwood turn 96
    marker now {{MB_REVIEW-FIX: confident — ...}} ✓
  - Spot-checked 3 other proposals (turns [X, Y, Z]): markers correct ✓
Cost: $0. No Stage 3.1 re-run.
Commits:
  [hash] fix(stage5): natural-key anomaly join (Bug 1)
  [hash] feat(stage3): logger.warning in ApplyHardBlock catch (Bug 2 visibility)
  [hash] test(stage5): natural-key collision guard
```

---

## EDGE CASES + WATCHOUTS

1. **`token_span` is a list in JSON, must be tuple for dict key.** Sonnet's already used to this — `tuple(a.token_span)` everywhere it's used as a key.

2. **The collision guard could fire on real data if Reader ever produces overlapping spans on the same turn.** If it fires during the Stage 5 re-render, STOP and flag to Opus before proceeding. The guard is doing its job — telling us the natural-key assumption broke.

3. **There may be other places in the codebase that join on `anomaly_id`.** Recon item 4 above is meant to catch them. If Sonnet finds joins outside `proposal_mapper.py`, flag in the recon report — don't fix them in this chunk without Opus approval.

4. **Don't change the anomalies.jsonl schema.** This fix is read-side only. The on-disk format stays exactly as it is. No re-run needed precisely because the data is unchanged.

5. **If pytest reveals tests that fail for reasons unrelated to the join key change** (e.g., flaky tests, environment issues), flag in the build report. Don't try to fix them in this chunk.

---

## ROLLBACK PLAN

If anything goes sideways:

```cmd
cd C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
git revert [chunk-d-commit-hashes]
```

Each step is its own commit so partial revert is possible. The fix is read-side only — no data corruption risk, no re-run cost to recover.

— End of Chunk D spec —
