# STAGE 5 — MODULE 4 BUILD SPEC: review_tags.py

**Parent spec:** https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_v01_BUILD_SPEC.md

## Goal
Pure functions that generate the inline `{{MB_REVIEW-*}}` tag strings and the corresponding `ReviewQueueEntry` records. No turn rendering, no document logic. Just tag generation.

## File to create

### `src/stage5/review_tags.py`

```python
from src.stage5.schemas import ApplicationEntry, ReviewQueueEntry

# Tag subtype constants
TAG_TYPE_FIX = "MB_REVIEW-FIX"
TAG_TYPE_VERIFY = "MB_REVIEW-VERIFY"
TAG_TYPE_FLAG = "MB_REVIEW-FLAG"

SUBTYPE_CONFIDENT = "confident"
SUBTYPE_VERIFY = "verify"
SUBTYPE_FLAG = "flag"

def make_reword_tag(entry: ApplicationEntry) -> tuple[str, str]:
    """
    For a REWORD application, return (tag_type, subtype).

    Rule (per parent spec §6):
    - confidence == "high"   → MB_REVIEW-FIX, confident
    - confidence in ("medium", "low", "unknown") → MB_REVIEW-VERIFY, verify

    Raises ValueError if entry.op_type != "REWORD".
    """
    pass

def make_flag_tag(entry: ApplicationEntry) -> tuple[str, str]:
    """
    For a FLAG application, return (tag_type, subtype).
    Always (MB_REVIEW-FLAG, flag) regardless of confidence.

    Raises ValueError if entry.op_type != "FLAG".
    """
    pass

def render_reword_marker(entry: ApplicationEntry, replacement_text: str) -> str:
    """
    Render the inline marker string for a REWORD substitution.

    For confident:  "{{MB_REVIEW-FIX: confident — <reason>}}<replacement_text>{{/}}"
    For verify:     "{{MB_REVIEW-VERIFY: <reason>}}<replacement_text>{{/}}"

    Where <reason> = entry.reason (truncated to 100 chars max with "..." if longer).
    """
    pass

def render_flag_marker(entry: ApplicationEntry) -> str:
    """
    Render the inline marker for a FLAG (no text replacement).

    Format: "{{MB_REVIEW-FLAG: <reason>}}"
    Where <reason> = entry.reason (truncated to 100 chars max with "..." if longer).
    """
    pass

def make_review_queue_entry(
    entry: ApplicationEntry,
    tag_id: str,
    page: int,
    line: int,
    turn_idx: int,
) -> ReviewQueueEntry:
    """
    Build a ReviewQueueEntry from an ApplicationEntry plus document position info.

    Auto-selects tag_type and subtype based on entry.op_type and entry.confidence
    using the same rules as make_reword_tag / make_flag_tag.

    For FLAG: after_text is empty string (no replacement happened).
    For REWORD: after_text = entry.after.
    """
    pass
```

## Reason truncation

Reasons can be long. To prevent unreadable inline tags, truncate at 100 chars:
- If `len(reason) <= 100`: use as-is
- Else: `reason[:97] + "..."`

This is a length-only truncation. No word-boundary smartness for v0.1.

## Tag examples (from parent spec §6)
{{MB_REVIEW-FIX: confident — phonetic match}}landmen{{/}}
{{MB_REVIEW-VERIFY: phonetic — verify}}accounts payable{{/}}
{{MB_REVIEW-FLAG: company name not in names_lock — confirm}}

## Tests

### `tests/stage5/test_review_tags.py`

At minimum:

1. `make_reword_tag` returns ("MB_REVIEW-FIX", "confident") for confidence="high"
2. `make_reword_tag` returns ("MB_REVIEW-VERIFY", "verify") for confidence="medium"
3. `make_reword_tag` returns ("MB_REVIEW-VERIFY", "verify") for confidence="low"
4. `make_reword_tag` returns ("MB_REVIEW-VERIFY", "verify") for confidence="unknown"
5. `make_reword_tag` raises ValueError if op_type is "FLAG"
6. `make_flag_tag` returns ("MB_REVIEW-FLAG", "flag") regardless of confidence
7. `make_flag_tag` raises ValueError if op_type is "REWORD"
8. `render_reword_marker` produces correct format for high confidence
9. `render_reword_marker` produces correct format for medium confidence
10. `render_flag_marker` produces correct format
11. `render_reword_marker` truncates long reasons at 100 chars with "..."
12. `render_flag_marker` truncates long reasons at 100 chars with "..."
13. `make_review_queue_entry` returns valid ReviewQueueEntry for REWORD high (subtype="confident")
14. `make_review_queue_entry` returns valid ReviewQueueEntry for REWORD low (subtype="verify")
15. `make_review_queue_entry` returns valid ReviewQueueEntry for FLAG (subtype="flag", after_text="")

Aim for 15 tests.

## Acceptance

- All 15 tests pass
- Existing 376 tests still pass (no regressions)
- Commit message: `feat(stage5): module 4 — review_tags.py + tests`

## What NOT to do

- No turn-text rendering (Module 5)
- No document composition (Module 6)
- No page layout (Module 7)
- No reading any input files
- Pure functions only — no I/O, no state
