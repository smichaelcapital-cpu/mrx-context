STAGE 5 v0.1 — BUILD SPEC: assemble_final.py
Status: DRAFT for Scott review
Author: Opus, 2026-04-27
Build target: Sonnet
Repo: mrx_engine_v1
Spec path (when committed): docs/STAGE_5_v01_BUILD_SPEC.md

1. Goal & Non-Goals
Goal
Produce a human-readable plain-text deposition document from Block H output that Scott can open side-by-side with MB's 040226yellowrock-FINAL.txt and visually compare. The document carries inline {{MB_REVIEW-*}} review tags wherever the Agent took action.
Success criterion: Scott opens both files in Notepad. Body content, Q/A formatting, page width, line numbers, and indentation visually match. Review tags are visible and meaningful.
Non-goals (deferred to v0.2 or later)

Index page generation (page references, exhibit list)
Exhibit numbering and tracking
CAT round-trip / .sgxml output
Audio verification (Stage 4)
Multi-depo batch processing
UI / web app integration
PDF or RTF output formats
Real-time / streaming output

What "v0.1" means
Single deposition. Single run. Plain text. Deterministic. No API calls. Zero AI in this stage.

2. Inputs
All paths assume root = C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\
2.1 Block H pipeline outputs (existing — DO NOT modify)
FilePathCorrected turnsio/analysis/halprin_mini/_stage3_1_out/corrected_turns.jsonProposalsio/analysis/halprin_mini/_stage3_1_out/proposals.jsonDecisionsio/analysis/halprin_mini/_stage3_1_out/decisions.jsonlAnomaliesio/analysis/halprin_mini/_stage3_1_out/anomalies.jsonl
Critical reminders from recon:

corrected_turns.json.text is Stage 2 output, NOT yet corrected. REWORD ops must be applied at render time.
decisions.jsonl does NOT carry confidence. Confidence (string: low/medium/high) lives in anomalies.jsonl. Stage 5 must join via anomaly_id.
proposals.json is a JSON object with metadata + batch, not a flat array.

2.2 case_info.json (NEW — hand-built once for Halprin v0.1)
Path: io/analysis/halprin_mini/case_info.json
Schema:
json{
  "schema_version": "1.0",
  "case": {
    "caption": "YELLOW ROCK, LLC, et al, Plaintiffs, v. WESTLAKE US 2 LLC f/k/a EAGLE US 2 LLC et al., Defendants.",
    "docket_number": "202-001594",
    "division": "H",
    "court": "14TH JUDICIAL DISTRICT",
    "jurisdiction": {
      "state": "LOUISIANA",
      "parish": "CALCASIEU"
    }
  },
  "deposition": {
    "type": "VIDEOTAPED DEPOSITION",
    "witness": "RICHARD HALPRIN",
    "date_taken": "Thursday, April 2, 2026",
    "time_started": "9:04 a.m.",
    "time_ended": "4:20 p.m.",
    "location": {
      "firm": "SHER GARNER",
      "address_line_1": "909 Poydras Street",
      "city_state": "New Orleans, Louisiana"
    }
  },
  "reporter": {
    "name_full": "MARYBETH E. MUIR",
    "credentials": "CCR, RPR",
    "name_line": "MARYBETH E. MUIR, CCR, RPR",
    "cert_text": "Certified Court Reporter in and for the State of Louisiana, and Registered Professional Reporter"
  },
  "appearances": [
    {
      "role": "ATTORNEY FOR PLAINTIFF",
      "firm": "SHER GARNER CAHILL RICHTER KLEIN & HILBERT, L.L.C.",
      "address_lines": ["909 Poydras Street", "Suite 2800", "New Orleans, Louisiana 70112"],
      "phone": "504.299.2100",
      "emails": ["tmadigan@shergarner.com", "jgarner@shergarner.com", "khandy@shergarner.com", "mharris@shergarner.com"],
      "attorneys": [
        {"name": "THOMAS J. MADIGAN, ESQ.", "via": null},
        {"name": "JAMES GARNER, ESQ.", "via": null},
        {"name": "KAYLYN HANDY, ESQ.", "via": null},
        {"name": "MELISSA ROME HARRIS, ESQ.", "via": "Zoom"},
        {"name": "LESLIE PARTIDA DEPAZ", "title": "Paralegal", "via": null}
      ]
    },
    {
      "role": "FOR THE DEFENDANTS, WESTLAKE US 2 LLC, WESTLAKE CORPORATION AND WESTLAKE CHLOR-VINYLS CORPORATION",
      "firm": "SUSMAN GODFREY LLP",
      "address_lines": ["1000 Louisiana Street", "Suite 5100", "Houston, Texas 77002-5096"],
      "phone": "713.651.9366",
      "emails": ["rcaughey@susmangodfrey.com"],
      "attorneys": [{"name": "RYAN CAUGHEY, ESQ.", "via": null}]
    },
    {
      "role": "FOR THE DEFENDANTS, PPG",
      "firm": "JONES WALKER",
      "address_lines": ["445 North Boulevard", "Suite 800", "Baton Rouge, Louisiana 70802"],
      "phone": "225.248.2056",
      "emails": [],
      "attorneys": [{"name": "[FILL IN FROM FINAL]", "via": null}]
    }
  ],
  "examiner_primary": "MR. CAUGHEY"
}
Note: During v0.1 this file is hand-built once from MB's FINAL by Scott. In production, this becomes the CR onboarding intake form.

3. Outputs
3.1 Primary output
Path: io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt
Format guarantees:

UTF-8 encoded, LF line endings
61 characters maximum width per line
25 numbered lines per page
Right-justified line numbers in 5-character field
Right-justified page numbers at column 61
Blank line between every text line (matches MB's format)

3.2 Side-channel review queue
Path: io/analysis/halprin_mini/_stage5_out/halprin_mini.review_queue.json
Schema:
json{
  "schema_version": "1.0",
  "deposition_name": "halprin_mini",
  "generated_at": "2026-04-27T...",
  "source_run": {
    "stage3_1_run_at": "2026-04-26T14:48:49Z",
    "total_proposals": 30,
    "applied": 30,
    "rejected": 0
  },
  "review_items": [
    {
      "tag_id": "r_0001",
      "tag_type": "MB_REVIEW-FIX",
      "subtype": "confident|verify|flag",
      "page": 17,
      "line": 12,
      "turn_idx": 267,
      "before_text": "trek",
      "after_text": "",
      "reason": "Company name 'trek' not in names_lock; cannot confirm spelling or capitalization",
      "confidence": "medium",
      "specialist_hint": "consistency",
      "source": "raw_steno",
      "anomaly_id": "a_0001",
      "proposal_id": "p_0001"
    }
  ]
}
3.3 Run summary
Path: io/analysis/halprin_mini/_stage5_out/stage5.summary.json
json{
  "schema_version": "1.0",
  "input_paths": {},
  "output_paths": {},
  "case_info_path": "",
  "duration_sec": 0.0,
  "totals": {
    "turns_rendered": 552,
    "proposals_applied_REWORD": 12,
    "proposals_applied_FLAG": 18,
    "proposals_rejected": 0,
    "review_tags_emitted": {
      "MB_REVIEW-FIX_confident": 0,
      "MB_REVIEW-VERIFY": 0,
      "MB_REVIEW-FLAG": 0
    },
    "pages_rendered": 0,
    "lines_rendered": 0
  },
  "warnings": []
}

4. case_info.json Schema (Authoritative)
See §2.2 above. Six top-level sections: case, deposition, reporter, appearances, examiner_primary. v0.1 contract: all required fields must be present. Missing required field = hard error, abort run.

5. Logic — Four Phases
Phase 1 — Build the Proposal Application Map
Goal: Single in-memory data structure keyed by turn_idx, listing every applied REWORD and applied FLAG joined with anomaly confidence.
Steps:

Load proposals.json → flatten batch.proposals into list of 30 records
Load decisions.jsonl → dict keyed by proposal_id, value is outcome
Load anomalies.jsonl → dict keyed by anomaly_id, value is full record
For each proposal: keep only outcome="apply"; look up anomaly via anomaly_id
Build application_map: dict[turn_idx, list[ApplicationEntry]]

ApplicationEntry fields:

proposal_id, op_type (REWORD or FLAG), token_span [start, end], before, after, reason, confidence (low/medium/high), specialist_hint, source, anomaly_id

Validation: Every applied proposal must have a matching anomaly. Missing anomaly = warning logged, proposal still applied with confidence="unknown".
Phase 2 — Emit Text Per Turn
Goal: Walk corrected_turns.json in order. For each turn, produce rendered text with REWORDs applied and FLAG markers inserted, plus review_queue entries.
Per turn:

Get turn's text and application_map[turn_idx]
Tokenize by whitespace, preserving original indices
Sort applications by token_span.start descending (substitutions don't shift downstream indices)
For each REWORD: replace tokens at span with after text, wrap in {{MB_REVIEW-FIX: confident — reason}} or {{MB_REVIEW-VERIFY: reason}} based on confidence (rule §6), generate review_queue entry
For each FLAG: insert {{MB_REVIEW-FLAG: reason}} marker after flagged token, generate review_queue entry
Re-join tokens with single spaces

Phase 3 — Compose the Document
Goal: Linear list of LogicalLine objects (pre-pagination).
Document structure for v0.1:

Cover page block
Skip index page (v0.2)
Appearances block (one per party in case_info.appearances)
Stipulation header (synthetic: "S T I P U L A T I O N" centered)
Stipulation body (turns 76–89, COLLOQUY)
Body opening BYLINE (turn 90: "EXAMINATION BY MR. CAUGHEY:")
Q/A body + colloquy (turns 91–621, plus BYLINE at 503 and 549)
Closing colloquy (turns 622–636)
Reporter's Certificate (synthetic boilerplate from case_info.reporter)
Witness's Certificate (synthetic boilerplate from case_info.deposition.witness)
Errata Sheet (synthetic boilerplate)

LogicalLine attributes: text, kind (cover/appearances/stipulation_header/colloquy/byline/qa_q/qa_a/qa_continuation/parenthetical/cert_reporter/cert_witness/errata/blank/centered), indent, wrap_indent
Indentation rules (from FINAL.txt recon):
kindFirst-line indentContinuation indentqa_q / qa_a8 spaces, then Q. or A., then 4 spaces3 spaces from leftqa_continuation3 spaces3 spacescolloquy (named)17 spaces17 spacesparenthetical11 spaces11 spacesbyline3 spacesn/astipulation_headercentered to col 61n/acert_* / errataper templateper template
Phase 4 — Lay Out Pages
Steps:

Wrap each logical line: if len(text) + indent <= 61, single line. Else soft-wrap on whitespace at width 61 - indent. First line uses indent, subsequent lines use wrap_indent.
Insert blank line between every content line (matches MB's format).
Group into 25-content-line pages with page header: 2 blanks, page number right-justified to col 61, 2 blanks, then 25 numbered lines (line numbers 1–25, right-justified 5-char field), each numbered line followed by one blank line.
Output to halprin_mini.OUR_FINAL.txt.

Pagination is mechanical and deterministic. No widow/orphan handling in v0.1.
5.5 Tokenization rules
Critical — must match Reader's tokenization so token_span indices align.
For v0.1: assume whitespace tokenization (text.split()). Verify against Reader's actual tokenization in code review. If Reader uses a different tokenizer, Stage 5 must use the same one.
Test: For each REWORD, confirm text_tokens[token_span[0]:token_span[1]+1] equals before. If mismatch detected, log warning, skip proposal, continue. Do not crash.

6. Review Tag Rules
{{MB_REVIEW-FIX: confident — <reason>}}<text>{{/}}

Trigger: REWORD applied, anomaly.confidence = high
Behavior: Substitute text. Wrap. MB approves on read.
Example: Standard {{MB_REVIEW-FIX: confident — phonetic match}}landmen{{/}} are common.

{{MB_REVIEW-VERIFY: <reason>}}<text>{{/}}

Trigger: REWORD applied, anomaly.confidence = medium, low, or unknown
Behavior: Substitute text. Wrap with cautious tag. MB checks against notes/audio.
Example: couple {{MB_REVIEW-VERIFY: phonetic — verify}}accounts payable{{/}}

{{MB_REVIEW-FLAG: <reason>}}

Trigger: FLAG op_type, decision.outcome = apply
Behavior: Insert marker after flagged token. NO text change.
Example: worked at trek{{MB_REVIEW-FLAG: company name not in names_lock — confirm}} from 2010.

Stripping
v0.1 does NOT include strip-tags mode. Future work: --clean flag for tag-free output. Tags exist for review only. Add to revisit list.

7. Module Structure
New module: src/stage5/
src/stage5/
├── __init__.py
├── assemble_final.py       — main entry point + CLI
├── case_info_loader.py     — load + validate case_info.json
├── proposal_mapper.py      — Phase 1: build application_map
├── turn_renderer.py        — Phase 2: render single turn with reviews
├── document_composer.py    — Phase 3: build LogicalLine list
├── page_layout.py          — Phase 4: wrap, paginate, format
├── review_tags.py          — tag generation rules
└── schemas.py              — dataclasses
Entry point:
pythondef assemble_final(
    corrected_turns_path: Path,
    proposals_path: Path,
    decisions_path: Path,
    anomalies_path: Path,
    case_info_path: Path,
    output_dir: Path,
) -> Stage5Summary:
    """Stage 5 v0.1 — assemble human-readable depo from Block H output."""
CLI:
bashpython -m src.stage5.assemble_final \
    --corrected-turns io/analysis/halprin_mini/_stage3_1_out/corrected_turns.json \
    --proposals       io/analysis/halprin_mini/_stage3_1_out/proposals.json \
    --decisions       io/analysis/halprin_mini/_stage3_1_out/decisions.jsonl \
    --anomalies       io/analysis/halprin_mini/_stage3_1_out/anomalies.jsonl \
    --case-info       io/analysis/halprin_mini/case_info.json \
    --output-dir      io/analysis/halprin_mini/_stage5_out

8. Test Plan
8.1 Unit tests per module

case_info_loader: valid loads; missing fields raise; schema version check
proposal_mapper: join logic; missing anomaly → warning; rejected proposals excluded
turn_renderer: REWORD substitution; FLAG insertion; multiple ops per turn (right-to-left); tokenization mismatch logs warning
document_composer: section ordering; cover/appearances generated; turns 76–636 rendered; BYLINE handling
page_layout: wrap at 61 chars; line numbering 1–25; page numbering; blank-line interleaving
review_tags: tag selection by confidence; FLAG tag format

8.2 Integration test
tests/stage5/test_integration_halprin_mini.py:

Run end-to-end on Block H artifacts + test case_info.json fixture
Assert: output file exists, max line width <= 61
Assert: review_queue.json record count = 30
Assert: tag counts: 12 REWORDs split FIX_confident + VERIFY by confidence; 18 FLAGs
Assert: no exceptions, no unexpected stderr

8.3 Manual acceptance test (Scott)

Run on real Block H output
Open halprin_mini.OUR_FINAL.txt and 040226yellowrock-FINAL.txt in Notepad side-by-side
Compare: cover, appearances, Q/A page, page width, line count, tag visibility
Acceptance: readable end-to-end, Q/A formatting visually similar, tags clear, cover/appearances/cert render without manual intervention


9. Rollback & Risk
Rollback: Stage 5 is purely additive. New module under src/stage5/. New output dir _stage5_out/. Reads existing pipeline outputs without modifying them. Rollback = rm -rf src/stage5/ tests/stage5/. Zero impact on Stages 1, 2, 3.1.
Prime Directive check: "Could what I am about to code reduce accuracy or credibility?" No. Stage 5 reads existing pipeline output and renders for human review. Does not modify transcript data. Every visible change corresponds to an existing applied proposal — making the pipeline MORE auditable.
Risks:

Tokenization mismatch between Stage 5 and Reader → wrong text positions. Mitigation: verify in code review, log warnings, skip mismatched.
Pagination breaks Q/A pairs across pages → readability hurt. v0.1 accepts; v0.2 adds widow/orphan handling.
case_info.json incomplete for non-Halprin depos → hard fail. v0.1 accepts.


10. Open Items / Revisit List
Add to v0.2 or later — explicitly NOT in v0.1:

 Index page with examination page refs and exhibit list
 Exhibit numbering and tracking
 Widow/orphan control for Q/A pairs at page boundaries
 Tokenization unification with Reader
 --clean mode for tag-free output
 Multi-witness depos
 Multi-day / multi-volume depos
 Realtime markers (*REPORTER CHECK HERE*) as structured review items
 Ambiguous BYLINEs (e.g., EXAMINATIONBY MR. CAUGHEY: missing space)
 Index of corrections summary at end of document
 Pretty-printer for review_queue.json
 CAT round-trip output (RTF or .sgngl) for actual delivery
 case_info.json auto-extraction from raw RTF (Stage 0 work)
 Stage 4 Audio Specialist integration — when Stage 4 v1 ships (Architecture B: Whisper + text-match, Brandl fixture ready per mrx-context/specs/STAGE_4_OPUS_CONTEXT_2026-04-24.md), Stage 5 will consume audio votes that may upgrade Reader/Writer confidence. Tag selection logic in §6 unchanged — better input only.


11. Build Sequence (for Sonnet)

Spec PR — commit this doc to docs/STAGE_5_v01_BUILD_SPEC.md
Schemas + dataclasses — src/stage5/schemas.py
case_info_loader.py + tests
Hand-build Halprin case_info.json fixture
proposal_mapper.py + tests
review_tags.py + tests
turn_renderer.py + tests
document_composer.py + tests
page_layout.py + tests
assemble_final.py — wires it together
Integration test
Run on real Halprin Block H output
Manual acceptance review with Scott

Each step: recon → spec section → code → test → commit. No multi-file commits without spec coverage.

12. Acceptance Sign-off
Spec ready for build when:

 Scott approved approach
 case_info.json schema reviewed
 Tokenization approach agreed (whitespace v0.1)
 Output path approved (_stage5_out/)
 Spec committed to docs/STAGE_5_v01_BUILD_SPEC.md
 Sonnet handoff written

— End of spec —
