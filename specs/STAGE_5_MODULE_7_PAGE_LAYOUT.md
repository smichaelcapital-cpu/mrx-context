# STAGE 5 — MODULE 7: page_layout.py
Status: BUILT — commit TBD
Author: Opus, 2026-04-27 (§5 corrected after Sonnet recon 2026-04-27)
Build target: Sonnet
Repo: mrx_engine_v1
Spec path: docs/STAGE_5_MODULE_7_PAGE_LAYOUT.md
Mirror to mrx-context: specs/STAGE_5_MODULE_7_PAGE_LAYOUT.md

## 1. Purpose
Take Module 6's ComposedDocument and produce the final paginated, line-numbered,
page-numbered plain-text output matching MB's FINAL.txt visual format. Fill in the
page and line fields on every ReviewQueueEntry based on where each review marker
landed on the page.

## 2. Non-Goals
- No modification of rendered_text content (markers stay intact).
- No widow/orphan handling (v0.2).
- No index page generation (v0.2).
- No RTF / PDF output formats.
- No strip-tags mode (v0.2).
- No I/O — pure function.

## 3. Inputs
```python
def lay_out_pages(document: ComposedDocument) -> PaginatedDocument:
```

## 4. Outputs

### 4.1 PaginatedDocument
```python
@dataclass(frozen=True)
class PaginatedDocument:
    text: str
    review_entries: list[ReviewQueueEntry]
    stats: LayoutStats
```

### 4.2 LayoutStats
```python
@dataclass(frozen=True)
class LayoutStats:
    total_pages: int
    total_content_lines: int
    total_physical_lines: int
    s1_s2_merges_performed: int
    wraps_performed: int
    review_entries_located: int
    review_entries_orphaned: int
    page_separators_emitted: int   # should equal total_pages - 1
```

## 5. Format Constants (Authoritative) — corrected from draft per recon 2026-04-27

| Constant | Value | Note |
|---|---|---|
| PAGE_WIDTH | 61 | max chars per content line (incl. line num field) |
| LINES_PER_PAGE | 25 | — |
| LINE_NUMBER_FIELD_WIDTH | **6** | was 5, corrected per recon — `f"{line:>6}"` |
| PAGE_NUMBER_COLUMN | **60** | was 61, corrected — `f"{page:>60}"`, digit lands at col 60 |
| BLANKS_BEFORE_PAGE_NUMBER | 2 | — |
| BLANKS_AFTER_PAGE_NUMBER | 2 | — |
| BLANK_LINE_BETWEEN_CONTENT | True | blank after every numbered line incl. line 25 |
| PAGE_SEPARATOR | `"\x0c"` | **NEW** — form feed between pages (CAT-software standard) |

All constants annotated `# FORMAT-LOCKED-V01` in code.

Format strings (corrected):
- Numbered content line: `f"{line_num:>6}{' ' * indent}{text}"`
- Page number line: `f"{page_num:>60}"`
- Page separator: `"\x0c"` inserted between page texts (N pages → N-1 form feeds)

## 6. Algorithm — Five Steps

### 6.1 Step 1: s1+s2 merge pass
Walk lines left-to-right. When QA_Q is followed by QA_Q_CONTINUATION, merge if:
```
len(s1.text) + 2 + len(s2.text) + s1.indent <= PAGE_WIDTH
```
The +2 is the two spaces between sentences. Chained s2s: greedily merge while each next
s2 fits. Merged line: kind=QA_Q, text=s1+"  "+s2, review_entries combined.
If QA_Q_CONTINUATION has no preceding QA_Q: warn, pass through.

### 6.2 Step 2: Soft-wrap pass
Speaker prefixes added here (not in Module 6):
- QA_Q first line: "Q.    " prepended to text (indent=8, so full prefix at 8 spaces)
- QA_A first line: "A.    " prepended to text (indent=8)
- All other kinds: text as-is

Available width:
- First line: `PAGE_WIDTH - LINE_NUMBER_FIELD_WIDTH - indent`
- Continuation: `PAGE_WIDTH - LINE_NUMBER_FIELD_WIDTH - wrap_indent`

Markers (`{{MB_REVIEW-*}}...{{/}}` or `{{MB_REVIEW-FLAG:...}}`) are single non-breakable
units. Overflow allowed for markers that exceed line width (log warning, preserve marker).

CENTERED lines: center text within content area width (55 chars).

### 6.3 Step 3: Pagination pass
Group physical lines into pages of LINES_PER_PAGE. No widow/orphan handling in v0.1.

### 6.4 Step 4: Format pass
Per page:
```
"" + "\n" + "" + "\n" + f"{page_num:>60}" + "\n" + "" + "\n" + "" + "\n" +
f"{1:>6}{indent}{l1}" + "\n" + "" + "\n" +
f"{2:>6}{indent}{l2}" + "\n" + "" + "\n" + ...
f"{N:>6}{indent}{lN}" + "\n" + ""
```
Pages joined with PAGE_SEPARATOR (`"\x0c"`). LF only (`\n`).

### 6.5 Step 5: Backfill review entries
Map turn_idx → (page, line) of first physical line of that turn.
Create updated ReviewQueueEntry with page+line filled.
Orphaned (turn_idx not found): warn, leave page=None, line=None.

## 7. Public API
```python
def lay_out_pages(document: ComposedDocument) -> PaginatedDocument:
```
Internal helpers: `_merge_s1_s2`, `_wrap_logical_lines`, `_paginate`,
`_format_pages`, `_backfill_review_entries`. `_PhysicalLine` and `_Page` are
private dataclasses internal to the module.

## 8. Error Handling
| Condition | Action |
|---|---|
| Empty ComposedDocument.lines | Return empty PaginatedDocument |
| Single marker longer than line width | Warn, allow overflow |
| Review entry turn_idx not found | Warn, orphaned count++, page=None |
| No whitespace in line to wrap | Warn, emit as-is, allow overflow |
| Indent > PAGE_WIDTH | Raise ValueError (Module 6 bug) |

## 9. Test Plan (31 tests)

### 9.1 s1+s2 merge (8): tests 1–8
### 9.2 Wrap (6): tests 9–14
### 9.3 Pagination (5): tests 15–19
### 9.4 Format (5): tests 20–24
### 9.5 Review entry backfill (4): tests 25–28
### 9.6 Stats (1): test 29
### 9.7 Integration smoke (1): test 30
### 9.8 Form feed (1): test 31 (added per Opus 2026-04-27)
- Form feed present between every consecutive page, absent before page 1 and after last.
- Count of `\x0c` in output == total_pages - 1.

## 10. Revisit List (post-v0.1)
- Widow/orphan handling
- Marker overflow (currently allow; v0.2 wrap inside)
- Strip-tags mode
- Single-token wrap (currently emit as-is)
- Per-state formatting variants
- Merged s2 turn_idx tracking for review entry backfill

## 11. Acceptance — COMPLETE ✅
- [x] schemas.py has PaginatedDocument, LayoutStats (with page_separators_emitted)
- [x] src/stage5/page_layout.py exists and matches §7 API
- [x] All 31 tests pass
- [x] Recon §5 constants confirmed and corrected
- [x] Integration smoke: non-empty string, 30 review entries located, 0 orphaned
- [x] Suite total ≥ 439 + new tests, all passing
- [x] Spec committed to docs/ and specs/
