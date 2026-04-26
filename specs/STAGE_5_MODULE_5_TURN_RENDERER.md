# STAGE 5 — MODULE 5: turn_renderer.py
Status: BUILT — commit 87112b5
Author: Opus, 2026-04-27
Build target: Sonnet
Repo: mrx_engine_v1
Spec path: docs/STAGE_5_MODULE_5_TURN_RENDERER.md
Mirror to mrx-context: specs/STAGE_5_MODULE_5_TURN_RENDERER.md

## 1. Purpose
Render a single turn's text with inline {{MB_REVIEW-*}} markers applied for every REWORD and FLAG operation that targets that turn. Emit one ReviewQueueEntry per applied entry for the side-channel review queue.
This is Phase 2 of the parent spec (§5).

## 2. Non-Goals

- No document-level composition (Module 6).
- No pagination / wrapping (Module 7).
- No mutation of inputs.
- No tag-stripping mode.
- No page/line numbers in ReviewQueueEntry — those are filled in by Module 7 after layout.

## 3. Inputs

### 3.1 Turn record
Single dict from corrected_turns.json. Required fields used by this module:

| Field | Type | Purpose |
|---|---|---|
| idx | int | Turn index — used as turn_idx in queue entries |
| text | str | Stage 2 corrected text (REWORDs not yet applied) |
| speaker | str \| null | Pass-through; not used in render |
| paragraph_style | str | Pass-through; not used in render |

Other fields are ignored by this module.

### 3.2 Application entries
list[ApplicationEntry] for that turn (from Module 3's application_map[turn_idx]).

Required fields per entry (already defined in schemas.py):
proposal_id, op_type ("REWORD" | "FLAG"), token_span ([start, end], inclusive), before (str), after (str), reason (str), confidence ("high" | "medium" | "low" | "unknown"), specialist_hint (str), source (str), anomaly_id (str).

## 4. Outputs

### 4.1 Function return
A RenderedTurn dataclass (added to schemas.py):
```python
@dataclass(frozen=True)
class RenderedTurn:
    turn_idx: int
    rendered_text: str
    review_entries: list[ReviewQueueEntry]
    skipped_entries: list[SkippedEntry]   # for Stage 5 summary diagnostics
```

### 4.2 ReviewQueueEntry
Already defined in Module 4 / schemas. Module 5 fills these fields:

| Field | Source |
|---|---|
| tag_id | sequential per-turn placeholder ("r_pending") — Module 8 assigns final IDs |
| tag_type | "MB_REVIEW-FIX" \| "MB_REVIEW-VERIFY" \| "MB_REVIEW-FLAG" |
| subtype | "confident" \| "verify" \| "flag" |
| page | None (Module 7 fills) |
| line | None (Module 7 fills) |
| turn_idx | from input turn |
| before_text | entry.before |
| after_text | entry.after ("" for FLAG) |
| reason | entry.reason (truncated per Module 4 rules) |
| confidence | entry.confidence |
| specialist_hint | entry.specialist_hint |
| source | entry.source |
| anomaly_id | entry.anomaly_id |
| proposal_id | entry.proposal_id |

### 4.3 SkippedEntry (new)
```python
@dataclass(frozen=True)
class SkippedEntry:
    proposal_id: str
    turn_idx: int
    reason: str   # "tokenization_mismatch" | "overlapping_span" | "out_of_range"
    detail: str
```
Returned but not raised. Stage 5 summary aggregates these into warnings[].

## 5. Algorithm

### 5.1 Tokenize
```python
tokens = turn["text"].split()
```
v0.1 contract: whitespace tokenization. Must match Reader. If Reader changes, Module 5 changes with it.

### 5.2 Validate every entry's span (before any mutation)
For each entry in input order:

1. **Bounds check.** If start < 0 or end >= len(tokens) or start > end → record SkippedEntry(reason="out_of_range"), drop entry.
2. **Before-text match.** Compute actual = " ".join(tokens[start:end+1]). If actual != entry.before → record SkippedEntry(reason="tokenization_mismatch", detail=f"expected {entry.before!r}, got {actual!r}"), drop entry.

### 5.3 Detect overlapping spans
After validation, check pairwise: if any two surviving entries have spans that intersect (touching at a boundary is NOT overlap; [2,3] and [4,5] are fine; [2,4] and [3,5] overlap), reject both entries in the overlap pair, log SkippedEntry(reason="overlapping_span") for each. Continue with remaining entries.

**Rationale:** Right-to-left application is only safe for non-overlapping spans. Two ops on the same word would silently corrupt each other. Per RULE-SILENT-FAILURE-CHECK, we surface and skip rather than guess.

### 5.4 Sort surviving entries
By token_span[0] descending. Ties broken by token_span[1] descending, then proposal_id ascending (deterministic).

### 5.5 Apply right-to-left
For each entry in sorted order:

**REWORD:**
```python
  marker = render_reword_marker(entry, entry.after)   # Module 4
  tokens[start:end+1] = [marker]
```
Single token replaces the span. The marker string already contains the after-text wrapped in {{MB_REVIEW-FIX|VERIFY: ...}}{{/}}.

**FLAG:**
```python
  marker = render_flag_marker(entry)     # Module 4
  tokens.insert(end + 1, marker)
```
No replacement. Marker inserted after the flagged token. entry.after must be ""; if not, treat as data error → SkippedEntry(reason="flag_with_after") and drop.

### 5.6 Re-join
```python
rendered_text = " ".join(tokens)
```

### 5.7 Build review entries
One ReviewQueueEntry per successfully applied entry (not skipped). Order: original input order (NOT sorted order), so the queue reads top-to-bottom.

### 5.8 No-ops
Empty entry list → return RenderedTurn(idx, turn["text"], [], []) unchanged. Whitespace must round-trip exactly when there are zero ops, so use turn["text"] directly rather than " ".join(turn["text"].split()).

## 6. Public API
```python
def render_turn(
    turn: dict,
    entries: list[ApplicationEntry],
) -> RenderedTurn:
    """Render one turn with review markers applied. Pure function."""
```
No I/O. No logging side effects (caller logs from skipped_entries). Deterministic for fixed inputs.

## 7. Error Handling Contract

| Condition | Action |
|---|---|
| Out-of-range span | Skip, append SkippedEntry, continue |
| Tokenization mismatch | Skip, append SkippedEntry, continue |
| Overlapping spans | Skip BOTH entries, append SkippedEntry for each, continue |
| FLAG with non-empty after | Skip, append SkippedEntry, continue |
| Empty entries list | Return text unchanged, empty lists |
| Empty turn["text"] with non-empty entries | Every entry fails out-of-range, return "" + skipped list |
| Missing idx or text key | Raise KeyError (caller bug) |

Crashes are forbidden for any data-shape problem in entries. Bugs in inputs surface as SkippedEntry; Module 8 escalates if skip rate is high.

## 8. Test Plan
File: tests/stage5/test_turn_renderer.py

### 8.1 Happy path
- Single REWORD high confidence — verify marker contains MB_REVIEW-FIX, confident, after-text; surrounding tokens preserved.
- Single REWORD medium confidence — marker contains MB_REVIEW-VERIFY.
- Single REWORD low confidence — marker contains MB_REVIEW-VERIFY.
- Single REWORD unknown confidence — marker contains MB_REVIEW-VERIFY.
- Single FLAG — marker inserted after flagged token, no text replacement.

### 8.2 Multi-op
- Two REWORDs same turn, non-overlapping — both applied, right-to-left order means later (higher-index) span unchanged by earlier substitution.
- REWORD + FLAG same turn — both render; FLAG marker present; REWORD substituted.
- Three ops same turn — all render correctly; ordering deterministic.

### 8.3 Failure modes (must not crash)
- Tokenization mismatch — entry's before doesn't equal " ".join(tokens[start:end+1]) → SkippedEntry, original tokens untouched at that span.
- Out-of-range span — end >= len(tokens) → SkippedEntry, no exception.
- Negative start — SkippedEntry.
- start > end — SkippedEntry.
- Overlapping spans — both entries skipped, both in skipped_entries, original text returned (since no other ops).
- FLAG with non-empty after — SkippedEntry, original tokens unchanged.

### 8.4 Edge cases
- No ops — rendered_text == turn["text"] byte-for-byte.
- Empty text + no ops — returns "".
- Empty text + one op — out-of-range skip.
- Single-token turn, single REWORD covering it — full replacement.
- First-token REWORD — start=0, end=0, marker at position 0.
- Last-token FLAG — marker appended at end.
- review_entries order matches input order (not sort order) — important for downstream determinism.

### 8.5 Integration smoke (skippable if files absent)
Real Block H sample — load 5 actual turns from io/analysis/halprin_mini/_stage3_1_out/corrected_turns.json plus their application_map entries. Render each. Assert: zero exceptions, zero SkippedEntry for tokenization_mismatch (this test is the canary for the v0.1 tokenization assumption — if it fails, escalate to Opus before continuing the build).

Mark with @pytest.mark.skipif(not files_exist, reason=...).

**Result (2026-04-27):** Zero tokenization mismatches on real Halprin Block H data. Whitespace-split assumption holds. ✅

## 9. Prime Directive Check

"Could what I am about to code reduce accuracy or credibility of the transcript?"

Answer: No, with one watchpoint.

- No silent normalization. Every change traces to a logged proposal. ✓ (RULE-INPUT-IS-SACRED)
- Every applied entry produces a ReviewQueueEntry. ✓ (RULE-PROOF-OF-WORK)
- Validation failures skip rather than corrupt. ✓ (RULE-SILENT-FAILURE-CHECK)

**Watchpoint:** if the Reader's tokenization differs from text.split(), every REWORD will silently skip on real data. Test 8.5 is the canary. Verified clean on Halprin data 2026-04-27.

## 10. Rollout
Pure additive module. No changes to Modules 1–4. New file src/stage5/turn_renderer.py, new test file, new dataclasses (RenderedTurn, SkippedEntry) in schemas.py.
Rollback: git revert 87112b5. No schema migrations, no pipeline impact.

## 11. Acceptance — COMPLETE ✅

- [x] schemas.py has RenderedTurn and SkippedEntry
- [x] src/stage5/turn_renderer.py exists and matches §6 API
- [x] All 23 tests pass (22 spec cases + 1 integration smoke)
- [x] Integration smoke (8.5) reports zero tokenization mismatches on real Halprin Block H data
- [x] Suite total 414 (was 391 + 23 new), all passing
- [x] Spec committed to docs/ in engine repo and specs/ in mrx-context
