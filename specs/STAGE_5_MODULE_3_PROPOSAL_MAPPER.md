# STAGE 5 — MODULE 3 BUILD SPEC: proposal_mapper.py

**Parent spec:** https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_v01_BUILD_SPEC.md

## Goal
Read Block H output (proposals.json + decisions.jsonl + anomalies.jsonl), join all three positionally (all[i] → same proposal), return a clean per-turn application map plus a list of warnings.

This is the data-prep layer. Modules 4-7 consume what this produces.

> **Join design note (Option A — fully positional):** All three Block H output files use per-batch IDs (p_0001…p_000N and a_0001…a_000N reset per batch), not globally unique. All three files are written in lockstep by Block H, so a positional join across all three is correct and safe. `proposal["anomaly_id"]` is stored on `ApplicationEntry` for traceability only — it is NOT used as a join key. See Future Work section for Option B (compound-key join).

## File to create

### `src/stage5/proposal_mapper.py`

Function signatures:

```python
from pathlib import Path
from src.stage5.schemas import ApplicationEntry

def load_proposals(path: Path) -> list[dict]:
    """Read proposals.json. Returns flat list of all proposal records from batch.proposals."""
    pass

def load_decisions(path: Path) -> list[dict]:
    """Read decisions.jsonl. Returns ordered list of decision records (positional — decisions[i] → proposals[i])."""
    pass

def load_anomalies(path: Path) -> list[dict]:
    """Read anomalies.jsonl. Returns ordered list of anomaly records (positional — anomalies[i] → proposals[i])."""
    pass

def build_application_map(
    proposals: list[dict],
    decisions: list[dict],
    anomalies: list[dict],
) -> tuple[dict[int, list[ApplicationEntry]], list[str]]:
    """
    Join proposals + decisions + anomalies all positionally (all[i] → same proposal).
    Filter to only outcome=='apply'.
    Returns:
        - dict keyed by turn_idx → list of ApplicationEntry (ordered by token_span[0] ascending)
        - list of warning strings
    """
    pass
```

## Logic per parent spec §5 Phase 1

### load_proposals
Open the JSON file. Navigate to `data["batch"]["proposals"]`. Return as a flat list. If structure is malformed, raise ValueError with clear message.

### load_decisions
Open the JSONL file. Parse each line as JSON. Return as an ordered list. Do NOT key by proposal_id — proposal_ids are per-batch and not globally unique.

### load_anomalies
Open the JSONL file. Parse each line as JSON. Return as an ordered list. Do NOT key by anomaly_id — anomaly_ids are per-batch and not globally unique.

### build_application_map
Single invariant check at entry: raise ValueError if `len(proposals) != len(decisions) or len(proposals) != len(anomalies)`.

For each index `i`, using `(proposal, decision, anomaly) = (proposals[i], decisions[i], anomalies[i])`:
1. If decision["outcome"] != "apply" → skip (rejected/review proposals don't generate ApplicationEntry).
2. Use `anomaly["confidence"]` for the ApplicationEntry's confidence field. (anomaly is always present via positional join — no missing-anomaly warning needed.)
3. Build an ApplicationEntry from the proposal + anomaly data.
4. Append to `application_map[proposal["turn_idx"]]`.

After all proposals processed, sort each turn's list by `token_span[0]` ascending. (Modules 4-5 will reverse for application — sort here makes inspection easier.)

## ApplicationEntry mapping

| ApplicationEntry field | Source |
|---|---|
| proposal_id | proposal["proposal_id"] |
| op_type | proposal["op_type"] |
| token_span | tuple(proposal["token_span"]) |
| before | proposal["before"] |
| after | proposal["after"] |
| reason | proposal["reason"] |
| confidence | anomaly["confidence"] (positional — anomalies[i]) |
| specialist_hint | proposal["specialist_hint"] |
| source | proposal["source"] |
| anomaly_id | proposal["anomaly_id"] (stored for traceability, not used as join key) |

## Tests

### `tests/stage5/fixtures/`
Three small fixture files for testing (4 records each, positionally aligned):
- `proposals_mini.json` — same structure as Block H proposals.json with metadata + batch
- `decisions_mini.jsonl` — JSONL, 4 lines, positionally aligned with proposals
- `anomalies_mini.jsonl` — JSONL, 4 lines, positionally aligned with proposals

Cover at least: 1 REWORD high-confidence apply, 1 REWORD low-confidence apply, 1 FLAG apply, 1 non-apply decision (to test skip behavior).

### `tests/stage5/test_proposal_mapper.py`

At minimum:
1. load_proposals returns flat list of correct length
2. load_proposals raises ValueError on malformed structure
3. load_decisions returns ordered list of correct length
4. load_anomalies returns ordered list of correct length
5. build_application_map raises ValueError if lengths mismatch (proposals vs decisions vs anomalies)
6. build_application_map produces correct turn_idx → entries mapping
7. build_application_map skips proposals where decision.outcome != "apply"
8. build_application_map preserves all proposal fields correctly in ApplicationEntry
9. build_application_map uses anomaly confidence from positional anomalies[i]
10. build_application_map sorts entries within a turn by token_span[0] ascending
11. build_application_map stores anomaly_id from proposal on ApplicationEntry (traceability)

Aim for 11-13 tests.

### Integration check (smoke test, not full pipeline)
One additional test that loads the REAL Block H output files and confirms:
- Total ApplicationEntry count matches expected (12 REWORD + 18 FLAG = 30 entries)
- No exceptions

Path the test reads from:
- `io/analysis/halprin_mini/_stage3_1_out/proposals.json`
- `io/analysis/halprin_mini/_stage3_1_out/decisions.jsonl`
- `io/analysis/halprin_mini/_stage3_1_out/anomalies.jsonl`

If those files don't exist (e.g., CI), skip the test with `pytest.skip("Block H artifacts not present")`.

## Acceptance

- All new tests pass
- Existing 362 tests still pass (no regressions)
- Commit message: `feat(stage5): module 3 — proposal_mapper.py + tests`

## What NOT to do

- No tag generation (that's Module 4)
- No turn rendering (that's Module 5)
- No JSON schema validation beyond what's needed to parse — assume Block H output is well-formed (we generated it)
- No mutation of the input JSON — read-only parsing

---

## Future Work — Option B (deferred)

Current join is fully positional: all three files (proposals, decisions, anomalies) are joined by index i. This works because Block H writes all three files in lockstep, one record per proposal per batch.

A more robust future design would use compound-key joins across all three files:
- proposals.json already has `batch_id` per proposal
- decisions.jsonl would gain a `batch_id` field → compound key (batch_id, proposal_id) globally unique
- anomalies.jsonl would gain a `batch_id` field → compound key (batch_id, anomaly_id) globally unique
- All joins become hash-based, order-independent
- Resilient to future Block H changes (parallel batch writes, partial reruns, merged outputs from multiple runs, etc.)

Cost to implement: edit Stage 3.1 to emit batch_id in decisions.jsonl and anomalies.jsonl, re-run Block H once.

Trigger to do this work: any time Block H output ordering becomes non-deterministic, OR Stage 5 needs to merge decisions/anomalies from multiple Block H runs.
