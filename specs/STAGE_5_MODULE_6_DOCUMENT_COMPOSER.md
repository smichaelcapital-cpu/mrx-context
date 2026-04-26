# STAGE 5 — MODULE 6: document_composer.py
Status: BUILT — commit TBD
Author: Opus, 2026-04-27 (§6.6 corrected after Sonnet recon 2026-04-27)
Build target: Sonnet
Repo: mrx_engine_v1
Spec path: docs/STAGE_5_MODULE_6_DOCUMENT_COMPOSER.md
Mirror to mrx-context: specs/STAGE_5_MODULE_6_DOCUMENT_COMPOSER.md

## 1. Purpose
Walk the full corrected_turns list, call Module 5's render_turn for every turn, and produce an ordered list of LogicalLine objects that represent the entire deposition document — cover page through errata sheet — pre-pagination.
This is Phase 3 of the parent spec (§5).

## 2. Non-Goals

- No wrapping at 61 chars (Module 7).
- No page numbers, line numbers, blank-line interleaving (Module 7).
- No index page (parent spec §10 — deferred to v0.2).
- No exhibit list.
- No widow/orphan handling.
- No modification to corrected_turns or proposals.
- No I/O — pure function.

## 3. Inputs
```python
def compose_document(
    corrected_turns: list[dict],
    application_map: dict[int, list[ApplicationEntry]],
    case_info: dict,
) -> ComposedDocument:
```

| Param | Source |
|---|---|
| corrected_turns | from corrected_turns.json (Stage 2 output) |
| application_map | from Module 3's proposal_mapper.build_application_map() |
| case_info | from Module 2's case_info_loader.load_case_info() |

## 4. Outputs

### 4.1 LogicalLine
```python
@dataclass(frozen=True)
class LogicalLine:
    text: str
    kind: LineKind
    indent: int = 0
    wrap_indent: int = 0
    turn_idx: Optional[int] = None
    review_entries: list = field(default_factory=list)
```

### 4.2 LineKind enum
```python
class LineKind(str, Enum):
    COVER = "cover"
    APPEARANCES = "appearances"
    STIPULATION_HEADER = "stipulation_header"
    BYLINE = "byline"
    QA_Q = "qa_q"
    QA_Q_CONTINUATION = "qa_q_continuation"   # NEW — was "QA_CONTINUATION" in draft
    QA_A = "qa_a"
    COLLOQUY = "colloquy"
    PARENTHETICAL = "parenthetical"            # reserved — not produced for Halprin
    CERT_REPORTER = "cert_reporter"
    CERT_WITNESS = "cert_witness"
    ERRATA = "errata"
    BLANK = "blank"
    CENTERED = "centered"
```

`QA_CONTINUATION` removed from spec. Reason: it conflated paragraph-level Q continuation
(s2 turns) with layout-level wrap behavior. Wrap is expressed via `wrap_indent` on each
`LogicalLine`; no LineKind needed for it.

### 4.3 ComposedDocument
```python
@dataclass(frozen=True)
class ComposedDocument:
    lines: list[LogicalLine]
    review_entries: list[ReviewQueueEntry]   # all entries flattened, in document order
    skipped_entries: list[SkippedEntry]      # bubbled from Module 5
    stats: ComposeStats
```

```python
@dataclass(frozen=True)
class ComposeStats:
    total_turns_rendered: int
    cover_lines: int
    appearances_lines: int
    body_lines: int
    cert_lines: int
    errata_lines: int
    bylines_emitted: int
```

## 5. Document Structure
In order:

| § | Section | Source |
|---|---|---|
| 5.1 | Cover page | synthesized from case_info |
| 5.2 | Appearances block | case_info.appearances[] |
| 5.3 | Stipulation header | synthetic centered line |
| 5.4 | Stipulation body | turns 77–89 |
| 5.5 | Body opening BYLINE | turn 90 |
| 5.6 | Q/A body + colloquy | turns 91–621 (BYLINEs at 503, 549) |
| 5.7 | Closing colloquy | turns 622–636 |
| 5.8 | Reporter's Certificate | synthesized from case_info.reporter |
| 5.9 | Witness's Certificate | synthesized from case_info.deposition.witness |
| 5.10 | Errata Sheet | synthetic boilerplate |

**Note on stipulation body:** Turn 76 text is "S T I P U L A T I O N" — it is the header
turn. The synthetic §5.3 header captures this, so §5.4 body renders turns 77–89 (not 76–89
as originally drafted). `# HARDCODE-HALPRIN-V01`

The turn ranges (77–89, 90, 91–621 with BYLINEs at 503/549, 622–636) are Halprin-specific.
v0.1 hard-codes them. v0.2 will derive these from paragraph_style markers.
All hard-coded values are annotated with `# HARDCODE-HALPRIN-V01` in code.

## 6. Section Builders

### 6.1 _build_cover(case_info) -> list[LogicalLine]
Synthetic, no turns consumed. Produces a COVER/CENTERED block matching MB's FINAL.txt
cover page layout. Pulls from case_info.case, case_info.deposition, case_info.reporter.
turn_idx=None, review_entries=[].

### 6.2 _build_appearances(case_info) -> list[LogicalLine]
Iterates case_info["appearances"]. For each party: role line, firm, address lines, phone,
emails, attorneys (with "(Via Zoom)" suffix where via is set).
indent=0, wrap_indent=0. kind=LineKind.APPEARANCES. turn_idx=None.

### 6.3 _build_stipulation_header() -> list[LogicalLine]
Single LineKind.STIPULATION_HEADER line: "S T I P U L A T I O N" centered.

### 6.4 _build_stipulation_body(turns, application_map) -> ...
Calls _render_turns_in_range(turns, 77, 89, kind=COLLOQUY, indent=17, wrap_indent=17).
Start=77 (not 76) because turn 76 = "S T I P U L A T I O N" is the synthetic header.

### 6.5 _build_body_opening_byline(turns, application_map) -> ...
Renders turn 90 as BYLINE, indent=3.

### 6.6 _build_qa_body(turns, byline_turn_idxs, application_map) -> ...
Walks turns 91–621. For each turn, decides kind by paragraph_style:

**Confirmed style → LineKind mapping (locked 2026-04-27 after Sonnet recon + Opus review):**

| paragraph_style | LineKind | indent | wrap_indent |
|---|---|---|---|
| `s1` | QA_Q | 8 | 3 |
| `s2` | QA_Q_CONTINUATION | 14 | 3 |
| `s3` | QA_A | 8 | 3 |
| `s5` | COLLOQUY | 17 | 17 |
| `s7` (or idx in {503,549}) | BYLINE | 3 | 0 |

PARENTHETICAL reserved in enum, not produced for Halprin.

If paragraph_style not in {s1, s2, s3, s5, s7} → raise ValueError with turn idx and value.

**s2 = QA_Q_CONTINUATION** (discovered during recon):
- 31/33 s2 turns preceded by s1; never follows an answer
- Renders at indent=14 (where Q. text starts) WITHOUT the "Q." prefix
- Module 7 may merge short s1+s2 pairs onto same physical line — that is Module 7's job

### 6.7 _build_closing_colloquy(turns, application_map) -> ...
_render_turns_in_range(turns, 622, 636, kind=COLLOQUY, indent=17, wrap_indent=17).

### 6.8 _build_reporters_cert(case_info) -> list[LogicalLine]
Synthetic template. Substitutes reporter.name_full, reporter.cert_text, deposition.witness.
kind=LineKind.CERT_REPORTER.

### 6.9 _build_witness_cert(case_info) -> list[LogicalLine]
Synthetic boilerplate, substitutes deposition.witness, deposition.date_taken.
kind=LineKind.CERT_WITNESS.

### 6.10 _build_errata(case_info) -> list[LogicalLine]
Synthetic boilerplate. kind=LineKind.ERRATA.

## 7. The _render_turns_in_range helper
```python
def _render_turns_in_range(
    turns: list[dict],
    start_idx: int,
    end_idx: int,
    application_map: dict[int, list[ApplicationEntry]],
    kind_resolver: Callable[[dict], LineKind],
    indent_resolver: Callable[[dict, LineKind], tuple[int, int]],
) -> tuple[list[LogicalLine], list[ReviewQueueEntry], list[SkippedEntry]]:
```
Iterates turns where start_idx <= turn["idx"] <= end_idx, calls render_turn, builds a
LogicalLine per turn, accumulates review and skipped entries.

## 8. Error Handling Contract

| Condition | Action |
|---|---|
| Missing turn idx in expected range | Log warning, insert BLANK placeholder, continue |
| paragraph_style not in mapping | Raise ValueError with turn idx and value |
| Empty corrected_turns | Returns cover + appearances + cert + errata only |
| application_map missing turn idx | Treated as no ops (application_map.get(idx, [])) |
| Module 5 returns SkippedEntry | Bubble up unchanged |

## 9. Revisit List (post-v0.1)
- [ ] Replace hardcoded turn ranges with derivation from paragraph_style markers
- [ ] Cert/errata templates may need per-state variants
- [ ] BYLINE detection from text content instead of hardcoded indices
- [ ] Module 7 s1+s2 same-line merge rule

## 10. Acceptance — COMPLETE ✅
- [x] schemas.py has LineKind, LogicalLine updated, ComposedDocument, ComposeStats
- [x] src/stage5/document_composer.py exists and matches §6 API
- [x] All 25 tests pass
- [x] paragraph_style values confirmed to map to known LineKinds
- [x] Integration smoke returns non-empty lines, zero ValueError on real Halprin data
- [x] Suite total ≥ 414 + new tests, all passing
- [x] Spec committed to docs/ and specs/
