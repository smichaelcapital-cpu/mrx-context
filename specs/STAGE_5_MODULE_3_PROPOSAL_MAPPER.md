# STAGE 5 — MODULE 3 BUILD SPEC: proposal_mapper.py

**Parent spec:** https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_v01_BUILD_SPEC.md

## Goal
Read Block H output (proposals.json + decisions.jsonl + anomalies.jsonl), join them positionally (decisions[i] → proposals[i]), return a clean per-turn application map plus a list of warnings.

This is the data-prep layer. Modules 4-7 consume what this produces.

> **Join design note (Option A — positional):** proposal_ids in Block H output are per-batch IDs (p_0001…p_000N reset per batch), not globally unique. The decisions file is written in lockstep with proposals, so a positional join is correct and safe. See Future Work section for Option B (compound-key join).

## File to create

### `src/stage5/proposal_mapper.py`

Function signatures:

```python
from pathlib import Path
from src.stage5.schemas import ApplicationEntry

def load_proposals(path: Path) -> list[dict]:
    """Read proposals.json. Returns flat list of all 30 proposal records from batch.proposals."""
    pass

def load_decisions(path: Path) -> list[dict]:
    """Read decisions.jsonl. Returns ordered list of decision records (positional — matches proposals order)."""
    pass

def load_anomalies(path: Path) -> dict[str, dict]:
    """Read anomalies.jsonl. Returns dict keyed by anomaly_id → full anomaly record."""
    pass

def build_application_map(
    proposals: list[dict],
    decisions: list[dict],
    anomalies: dict[str, dict],
) -> tuple[dict[int, list[ApplicationEntry]], list[str]]:
    """
    Join proposals + decisions positionally (decisions[i] → proposals[i]) + anomalies by anomaly_id.
    Filter to only outcome=='apply'.
    Returns:
        - dict keyed by turn_idx → list of ApplicationEntry (ordered by token_span.start)
        - list of warning strings (e.g., missing anomaly, etc.)
    """
    pass
```

## Logic per parent spec §5 Phase 1

### load_proposals
Open the JSON file. Navigate to `data["batch"]["proposals"]`. Return as a flat list. If structure is malformed, raise ValueError with clear message.

### load_decisions
Open the JSONL file. Parse each line as JSON. Return as an ordered list. Do NOT deduplicate or key by proposal_id — proposal_ids are per-batch and not globally unique. If `len(decisions) != len(proposals)` the caller (`build_application_map`) will detect the mismatch via positional indexing.

### load_anomalies
Open the JSONL file. Parse each line as JSON. Build dict keyed by `record["anomaly_id"]`. anomaly_ids ARE globally unique. If duplicate anomaly_id is found, raise ValueError.

### build_application_map
Raises ValueError if `len(proposals) != len(decisions)` (positional join requires 1:1 correspondence).

For each `(proposal, decision)` pair at index `i`:
1. decision = decisions[i] (positional join — not keyed by proposal_id).
2. If decision["outcome"] != "apply" → skip (rejected/review proposals don't generate ApplicationEntry).
3. Look up the anomaly via `anomaly_id`.
   - If anomaly found → use `anomaly["confidence"]` for the ApplicationEntry's confidence field.
   - If anomaly missing → warning: "Proposal <id> references missing anomaly <id> — using confidence='unknown'". Use confidence="unknown" but still create the entry.
4. Build an ApplicationEntry from the proposal + anomaly data.
5. Append to `application_map[proposal["turn_idx"]]`.

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
| confidence | anomaly["confidence"] OR "unknown" |
| specialist_hint | proposal["specialist_hint"] |
| source | proposal["source"] |
| anomaly_id | proposal["anomaly_id"] |

## Tests

### `tests/stage5/fixtures/`
Create three small fixture files for testing (3-5 records each, not the full 30):
- `proposals_mini.json` — same structure as Block H proposals.json with metadata + batch
- `decisions_mini.jsonl` — JSONL with matching proposal_ids
- `anomalies_mini.jsonl` — JSONL with matching anomaly_ids

Cover at least: 1 REWORD high-confidence apply, 1 REWORD low-confidence apply, 1 FLAG apply, 1 with missing anomaly (intentional, to test warning).

### `tests/stage5/test_proposal_mapper.py`

At minimum:
1. load_proposals returns flat list of correct length
2. load_proposals raises ValueError on malformed structure
3. load_decisions returns ordered list of correct length
4. build_application_map raises ValueError if proposals/decisions length mismatch
5. load_anomalies returns dict keyed by anomaly_id
6. build_application_map produces correct turn_idx → entries mapping
7. build_application_map skips proposals with no decision (warning logged)
8. build_application_map skips proposals where decision.outcome != "apply"
9. build_application_map handles missing anomaly with confidence="unknown" (warning logged)
10. build_application_map preserves proposal fields correctly in ApplicationEntry
11. build_application_map sorts entries within a turn by token_span[0] ascending

Aim for 11-13 tests.

### Integration check (smoke test, not full pipeline)
One additional test that loads the REAL Block H output files and confirms:
- Total ApplicationEntry count matches expected (12 REWORD + 18 FLAG = 30 entries)
- All 30 entries have outcome=apply (since rejections.jsonl is empty)
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

Current join is positional (decisions[i] joins to proposals[i] by file order). This works because Block H writes both files in lockstep.

A more robust future design would use compound-key joins:
- decisions.jsonl line schema would gain a `batch_id` field
- Compound key: (batch_id, proposal_id) — globally unique
- Join becomes hash-based, order-independent
- Resilient to future Block H changes (parallel batch writes, partial reruns, etc.)

Cost to implement: edit Stage 3.1 to emit batch_id in decisions.jsonl, re-run Block H once.

Trigger to do this work: any time Block H output ordering becomes non-deterministic, OR Stage 5 needs to merge decisions from multiple Block H runs.
