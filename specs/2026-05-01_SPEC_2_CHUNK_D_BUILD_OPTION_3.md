# SPEC 2 — Chunk D build: Implement Option 3 anomaly join (natural key)

Date: Friday 2026-05-01
Author: Opus (architect)
Builder: Sonnet
Gate: Hard (architectural — unlocks "positional joins locked" decision per HANDOFF_LOG.md decision log) — Scott has already approved Option 3 in chat. Build authorized.

## Background

Bug 1 from this session's recon: proposal_mapper.py joins on anomaly_id alone. Anomaly IDs reset to a_0001 per Stage 3.1 batch — multi-batch runs collide and the last batch silently overwrites all earlier ones. ~10 of 126 V2 proposals get wrong confidence (FIX confident → VERIFY).

Decision logged in HANDOFF_LOG.md: Option 3 — change the join key from anomaly_id to natural key (turn_idx, token_span). Zero artifact cost, smallest code surface, semantically correct.

## Goal

Fix Bug 1 by switching proposal_mapper.py to natural-key join. Add a guard against the documented edge case. Add visibility logging for Bug 2 (apply.py silent fallback) without fixing Bug 2 itself. Update the one affected test. Verify Halprin V2 Lemonwood now produces FIX confident marker.

## Files in scope

- `src/stage5/proposal_mapper.py` (the actual fix)
- `src/mrx_engine_v1/stage3/pipeline.py` OR `_run_halprin_mini.py` (Bug 2 visibility — see Build step 3 for which one)
- `tests/stage5/test_proposal_mapper.py` (update one assertion to match new error message)

## Files explicitly NOT in scope

- `src/mrx_engine_v1/stage3/apply.py` — Bug 2 actual fix is Chunk E, future
- `src/stage5/schemas.py` — no field changes
- Any other Stage 3 or Stage 5 module
- Any audit script
- The runner's NAMES_LOCK or any prompt

## Pre-build recon (REQUIRED)

1. git status and git log --oneline -5 on engine repo. Confirm clean working tree, last commit e7989e3 (Lemonwood).
2. Re-read src/stage5/proposal_mapper.py — confirm the join site and lookup line numbers.
3. Locate the test that currently expects match="unknown anomaly_id" — confirm file:line.
4. Identify where the ApplyHardBlock exception is caught and corrected_turns = list(turns) fallback happens.

After recon, report findings briefly (4-6 lines) and proceed to build. No second checkpoint needed — Scott has authorized the build.

## Build

### Step 1 — proposal_mapper.py natural-key join

Replace:
```python
anomaly_by_id = {a["anomaly_id"]: a for a in anomalies}
```

With:
```python
# Join on natural key (turn_idx, token_span) instead of anomaly_id.
# Rationale: anomaly_id resets per-Stage-3.1-batch; multi-batch runs
# collide on dict keys and the last batch silently overwrites earlier
# ones. The natural key is unique because Writer is structurally
# constrained to cite Reader's exact (turn_idx, token_span).
# Decision logged 2026-05-01 in mrx-context/handoffs/HANDOFF_LOG.md
# under "DECISION LOG — Anomaly join key architecture (2026-05-01)".
# Two alternatives considered (compound key, globally-unique IDs) —
# see log for revisit triggers. Do not change without reading the log
# entry first.
anomaly_by_natural_key = {
    (a["turn_idx"], tuple(a["token_span"])): a for a in anomalies
}

# Edge case guard: if two anomalies ever share (turn_idx, token_span),
# the dict comprehension would silently drop one. Reader currently does
# not produce this, but the assumption is untested across CR styles.
# Fail loud rather than corrupt confidence silently.
if len(anomaly_by_natural_key) != len(anomalies):
    raise ValueError(
        f"Anomaly natural-key collision: {len(anomalies)} anomalies "
        f"but only {len(anomaly_by_natural_key)} unique "
        f"(turn_idx, token_span) keys. Two or more anomalies share "
        f"the same span on the same turn — Writer's structural "
        f"assumption is violated. Inspect anomalies.jsonl."
    )
```

Replace the lookup:
```python
anomaly = anomaly_by_id[proposal["anomaly_id"]]
```

With:
```python
natural_key = (proposal["turn_idx"], tuple(proposal["token_span"]))
try:
    anomaly = anomaly_by_natural_key[natural_key]
except KeyError:
    raise ValueError(
        f"Proposal {proposal.get('proposal_id', '?')} references "
        f"natural key {natural_key} but no matching anomaly found. "
        f"Reader/Writer span mismatch."
    ) from None
```

### Step 2 — Update test_proposal_mapper.py

Update the assertion that expects `match="unknown anomaly_id"` to match the new error message. Sonnet's judgment call on which error path to exercise and test naming.

### Step 3 — Bug 2 visibility log

Add logger.warning before the `corrected_turns = list(turns)` fallback in the ApplyHardBlock catch block:

```python
except ApplyHardBlock as e:
    logger.warning(
        f"apply.py raised ApplyHardBlock — Stage 3 corrections silently "
        f"skipped, corrected_turns falls back to unmodified Stage 2 text. "
        f"This is Bug 2 (proposal_id cross-batch collision in apply.py). "
        f"Stage 5 render_turn will re-apply proposals from scratch and "
        f"OUR_FINAL.txt will be correct, but corrected_turns.json is "
        f"a no-op for this run. See HANDOFF_LOG.md 2026-05-01 entry, "
        f"Chunk E queued. Original error: {e}"
    )
    corrected_turns = list(turns)
```

### Step 4 — Verify the fix on real data

1. Run `pytest tests/ -q` — expect 510 passing.
2. Re-run Stage 5 only against existing Halprin V2 artifacts.
3. grep for "Lemonwood" in new OUR_FINAL.txt — must be MB_REVIEW-FIX: confident.
4. Spot-check turns 152, 267, 327, 575.

## Acceptance criteria

- pytest tests/ -q shows 510 passing, 0 failing
- Lemonwood at turn 96 in OUR_FINAL.txt now renders with MB_REVIEW-FIX: confident marker (not VERIFY)
- At least 2 of the 4 spot-checked turns (152, 267, 327, 575) also show FIX confident if their anomalies were originally high-confidence
- corrected_turns.json artifact is unchanged (Stage 3 not re-run)
- Inline code comment at the join site is present and references HANDOFF_LOG.md by name
- apply.py silent-fallback warning log is present
- Commit message: `fix(stage5): switch proposal_mapper to natural-key join (Bug 1) + apply.py warning (Bug 2 visibility)`

## Out of scope

- Bug 2 actual fix (apply.py multi-token + I-5 crash)
- Stage 3.1 re-run
- Diff methodology lockdown
- V2 prompt changes
- NAMES_LOCK additions
- Cleanup of duplicate Option 3 decision blocks in HANDOFF_LOG.md

## Report back

- Recon findings (4-6 lines)
- Final pytest summary line
- Lemonwood marker line from new OUR_FINAL.txt
- Confidence markers on 4 spot-checked turns
- git diff --stat
- Commit hash
- Any judgment calls

Then stop — Scott pushes the engine commit.

---
*End of spec*
