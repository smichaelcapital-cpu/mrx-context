# STAGE 5 — MODULE 2 BUILD SPEC: case_info_loader.py

**Parent spec:** https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_v01_BUILD_SPEC.md

## Goal
Load and validate case_info.json. Hard-fail with a clear error if any required field is missing. No defaulting — if it's missing, we abort.

## File to create

### `src/stage5/case_info_loader.py`

Function signatures:

```python
from pathlib import Path
from typing import Any

class CaseInfoValidationError(Exception):
    """Raised when case_info.json is missing required fields or has bad structure."""
    pass

def load_case_info(path: Path) -> dict[str, Any]:
    """Load and validate case_info.json. Returns the dict if valid, raises CaseInfoValidationError if not."""
    pass
```

## Required structure (per parent spec §2.2)

The loaded dict MUST have these top-level keys:
- `schema_version` (string, must equal "1.0")
- `case` (dict)
- `deposition` (dict)
- `reporter` (dict)
- `appearances` (list, length >= 1)
- `examiner_primary` (string, non-empty)

Within `case`:
- `caption` (string, non-empty)
- `docket_number` (string, non-empty)
- `division` (string)
- `court` (string, non-empty)
- `jurisdiction` (dict with keys `state` and `parish`, both non-empty strings)

Within `deposition`:
- `type` (string, non-empty)
- `witness` (string, non-empty)
- `date_taken` (string, non-empty)
- `time_started` (string, non-empty)
- `time_ended` (string, non-empty)
- `location` (dict with keys `firm`, `address_line_1`, `city_state`, all non-empty strings)

Within `reporter`:
- `name_full` (string, non-empty)
- `credentials` (string)
- `name_line` (string, non-empty)
- `cert_text` (string, non-empty)

Within each entry of `appearances`:
- `role` (string, non-empty)
- `firm` (string, non-empty)
- `address_lines` (list of strings, length >= 1)
- `phone` (string)
- `emails` (list of strings, may be empty)
- `attorneys` (list of dicts, length >= 1)

Within each `attorneys` entry:
- `name` (string, non-empty)
- (optional) `title` (string)
- (optional) `via` (string or null)

## Error handling

- File doesn't exist → CaseInfoValidationError("case_info.json not found at <path>")
- Invalid JSON → CaseInfoValidationError("case_info.json is not valid JSON: <error>")
- Missing required key → CaseInfoValidationError("Missing required field: <field path>")
- Empty required string → CaseInfoValidationError("Required field <field path> cannot be empty")
- Empty required list → CaseInfoValidationError("Required field <field path> cannot be empty list")
- schema_version mismatch → CaseInfoValidationError("Unsupported schema_version: <value> (expected '1.0')")

## Tests

### `tests/stage5/test_case_info_loader.py`

At minimum:
1. Loads valid Halprin case_info.json fixture (create as `tests/stage5/fixtures/case_info_halprin_valid.json` using parent spec §2.2 example data)
2. Raises CaseInfoValidationError if file doesn't exist
3. Raises CaseInfoValidationError if JSON is malformed
4. Raises CaseInfoValidationError if `case` key is missing
5. Raises CaseInfoValidationError if `appearances` is empty list
6. Raises CaseInfoValidationError if `case.caption` is empty string
7. Raises CaseInfoValidationError if `schema_version` is "0.9" instead of "1.0"
8. Raises CaseInfoValidationError if an attorney is missing the `name` field

Aim for 8-10 tests covering happy path + each major error type.

## Acceptance

- All new tests pass
- Existing 352 tests still pass (no regressions)
- Commit message: `feat(stage5): module 2 — case_info_loader.py + tests`

## What NOT to do

- No reading of any other Stage 5 inputs (corrected_turns, proposals, etc.)
- No tag generation
- No turn rendering
- No defaulting of missing values — hard fail per RULE-INPUT-IS-SACRED
