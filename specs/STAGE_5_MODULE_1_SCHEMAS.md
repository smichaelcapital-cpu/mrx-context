# STAGE 5 — MODULE 1 BUILD SPEC: schemas.py

**Parent spec:** https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_v01_BUILD_SPEC.md

## Goal
Pure dataclass definitions for Stage 5. No business logic. Just type structure that the rest of the modules will consume.

## Files to create

### `src/stage5/__init__.py`
Empty file.

### `src/stage5/schemas.py`

Use Python `@dataclass` decorators with full type hints. Use `from dataclasses import dataclass, field` and `from typing import Optional`.

Required dataclasses (per parent spec §5 and §3):

**ApplicationEntry** — represents a single applied proposal joined with its anomaly:
- `proposal_id: str`
- `op_type: str`  (REWORD or FLAG)
- `token_span: tuple[int, int]`  (start, end)
- `before: str`
- `after: str`  (empty for FLAG)
- `reason: str`
- `confidence: str`  (high / medium / low / unknown)
- `specialist_hint: str`
- `source: str`
- `anomaly_id: str`

**LogicalLine** — a pre-pagination line of document content:
- `text: str`
- `kind: str`  (cover / appearances / stipulation_header / colloquy / byline / qa_q / qa_a / qa_continuation / parenthetical / cert_reporter / cert_witness / errata / blank / centered)
- `indent: int` (default 0)
- `wrap_indent: int` (default 0)

**ReviewQueueEntry** — one entry in the side-channel review queue:
- `tag_id: str`
- `tag_type: str`  (MB_REVIEW-FIX / MB_REVIEW-VERIFY / MB_REVIEW-FLAG)
- `subtype: str`  (confident / verify / flag)
- `page: int`
- `line: int`
- `turn_idx: int`
- `before_text: str`
- `after_text: str`
- `reason: str`
- `confidence: str`
- `specialist_hint: str`
- `source: str`
- `anomaly_id: str`
- `proposal_id: str`

**TagCounts** — review tag tallies for the run summary:
- `MB_REVIEW_FIX_confident: int` (default 0)
- `MB_REVIEW_VERIFY: int` (default 0)
- `MB_REVIEW_FLAG: int` (default 0)

**Stage5Totals** — totals block for run summary:
- `turns_rendered: int` (default 0)
- `proposals_applied_REWORD: int` (default 0)
- `proposals_applied_FLAG: int` (default 0)
- `proposals_rejected: int` (default 0)
- `review_tags_emitted: TagCounts`  (use field(default_factory=TagCounts))
- `pages_rendered: int` (default 0)
- `lines_rendered: int` (default 0)

**Stage5Summary** — the run summary written to disk:
- `schema_version: str` (default "1.0")
- `input_paths: dict[str, str]`  (default_factory=dict)
- `output_paths: dict[str, str]`  (default_factory=dict)
- `case_info_path: str` (default "")
- `duration_sec: float` (default 0.0)
- `totals: Stage5Totals`  (default_factory=Stage5Totals)
- `warnings: list[str]`  (default_factory=list)

## Tests to create

### `tests/stage5/__init__.py`
Empty file.

### `tests/stage5/test_schemas.py`

For each dataclass, write a test that:
1. Instantiates with valid sample values
2. Confirms field types and defaults work
3. Confirms required fields raise TypeError if missing

Example test pattern:
```python
def test_application_entry_instantiates():
    e = ApplicationEntry(
        proposal_id="p_0001",
        op_type="REWORD",
        token_span=(3, 4),
        before="land men",
        after="landmen",
        reason="compound word",
        confidence="medium",
        specialist_hint="grammar",
        source="kb",
        anomaly_id="a_0001",
    )
    assert e.proposal_id == "p_0001"
    assert e.token_span == (3, 4)
```

At minimum 7 tests — one instantiation test per dataclass.

## Acceptance

- All 7+ tests pass under `pytest tests/stage5/ -v`
- Existing 337 tests still pass (no regressions): `pytest tests/ -q`
- Files committed to engine repo with message: `feat(stage5): module 1 — schemas.py + tests`
- Pushed to origin/main

## What NOT to do

- No business logic in schemas.py
- No imports of other Stage 5 modules
- No JSON loading/saving (that's Module 2)
- No tag generation (that's Module 4)
