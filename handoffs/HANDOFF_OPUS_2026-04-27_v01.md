# HANDOFF — OPUS — 2026-04-27 v01

## TRUTH SOURCES (READ FIRST — NEVER LOSE THESE)

MB's FINAL (truth source — Oracle Covenant applies, READ-ONLY):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-FINAL.txt

Engine output OUR_FINAL (regenerated each pipeline run):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt

Halprin source RTF (Stage 1 input):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-ROUGH_Tsmd.rtf

Halprin source .sgxml (job metadata + audio sync):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-ROUGH.sgxml

Engine repo:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
  github.com/smichaelcapital-cpu/Court_reporting_demo

Context repo:
  C:\Users\scott\OneDrive\Documents\mrx-context
  github.com/smichaelcapital-cpu/mrx-context

Master copies (canonical reference docs):
  C:\Users\scott\OneDrive\Documents\MASTER_COPIES\

## ONE-LINE STATE
Tier 1 + F2-CONT shipped. 499 tests passing. Front-matter cover still
needs Tier 2 M0 (case caption two-column). Audio architecture not yet
decided — recon queued. Scott tagging out wrecked but with real wins.

## RAMP — READ THESE IN ORDER
1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/MANIFEST.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-04-27_v01.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-04-27_v01.md

After reading, confirm: "Ramped from Opus handoff 2026-04-27 v01. Ready."

NOTE: MANIFEST.md is the FIRST ramp URL. Per draft RULE-OPERATION-DOC,
every session starts by reading the master file index. If you don't
see MANIFEST.md at that URL, the OPERATION DOC implementation isn't
done yet — fall back to handoff search but flag it to Scott.

## YOUR ROLE (PER RULE-ARCHITECT-PM-BUILDER-SEPARATION)
You are Opus, the architect. Sonnet is the builder. Scott is the human owner.

## ARTIFACTS TOUCHED THIS SESSION (per draft RULE-HANDOFF-ARTIFACT-MANIFEST)

Created:
  - mrx-context/legacy/format_final.py (full source preserved)
  - mrx-context/specs/2026-04-27_TIER1_FORMAT_DEFECT_BATCH_v2.md
  - mrx_engine_v1/docs/specs/2026-04-27_TIER1_FORMAT_DEFECT_BATCH_v2.md
  - mrx-context/specs/2026-04-27_F2_CONT_WRAP_INDENT.md
  - mrx_engine_v1/docs/specs/2026-04-27_F2_CONT_WRAP_INDENT.md
  - tests/stage5/test_<turn_renderer>::test_qa_label_four_spaces (F1)
  - tests/stage5/test_<page_layout>::test_cover_indent (F2)
  - tests/stage5/test_assemble_final::test_04_txt_crlf (F3 — renamed)
  - tests/stage5/test_<document_composer>::test_examination_split (F4)
  - tests/stage5/test_<document_composer>::test_cover_centered (F5)
  - tests/stage5/test_page_layout::test_33_wrap_continuation_inherits_indent (F2-CONT)

Modified:
  - mrx-context/LEGACY_FORMAT_REFERENCE_v01.md (File Location section)
  - src/stage5/turn_renderer.py (F1)
  - src/stage5/page_layout.py (F1, F2, F2-CONT)
  - src/stage5/document_composer.py (F2, F4, F5)
  - src/stage5/assemble_final.py (F3)
  - tests/stage5/test_assemble_final.py (F3 test rename)

Commits (all pushed to origin/main):
  Engine repo:
    77a0c74 — Tier 1 batch (F1-F5)
    387b8ac — F2-CONT wrap continuation indent
    5a4463c — F2-CONT spec
  Context repo:
    f63ccd0 — F2-CONT spec mirror
    a2f9dc3 — Tier 1 v2 spec mirror
    2a294c7 — legacy/format_final.py + LEGACY_FORMAT_REFERENCE_v01 update

## WHAT SHIPPED THIS SESSION

### Tier 1 Format Defect Batch
F1 — Q./A. spacing fixed. MB has 4 spaces, ours had 1. Tokenizer was
  collapsing the 4-space prefix. Fix: prefix excluded from tokenization.

F2 — Line numbers mashed against indent=0 content. Fixed by adding
  explicit indent values to LogicalLines emitted by _build_cover()
  and _build_appearances().

F3 — Line endings LF → CRLF. test_04_txt_lf_only renamed to
  test_04_txt_crlf with assertion flipped.

F4 — EXAMINATION BY MR. CAUGHEY: split. Turn 90 (text starts with
  "EXAMINATION ") now emits two LogicalLines: CENTERED "EXAMINATION"
  + BYLINE "BY MR. CAUGHEY:". Turns 503/549 unchanged.

F5 — Cover centering. _cover() → _centered() for "taken on", date,
  "commencing at", "at the offices of", venue, location lines, and
  star separators. "Reported By:" stays as _cover() with explicit
  indent=2.

### Tier 1 follow-up — F2-CONT
F2-CONT — Wrapped continuation lines were emitting with indent=0 even
  when parent had indent=4. Fix: cont_indent = wrap_indent if
  wrap_indent != 0 else indent. Test test_33 added.

### Total
499 tests passing (was 491).

## VERIFIED VISUAL WINS (eyeballed against MB's FINAL.txt)

Comparing halprin_mini.OUR_FINAL.txt to 040226yellowrock-FINAL.txt:
- Cover centering: VIDEOTAPED DEPOSITION block, "taken on", date,
  "commencing at", venue lines all centered ✓
- Q./A. spacing: 4 spaces after Q. and A. ✓
- CRLF line endings: status bar confirms Windows (CRLF) ✓
- EXAMINATION/BYLINE split: "EXAMINATION" on its own centered line,
  "BY MR. CAUGHEY:" on next numbered line with 3-space indent ✓
- Line numbers no longer mashed: "    9    Division 'H'" not
  "9Division 'H'" ✓
- Wrap continuation indent: "    10    CORPORATION AND WESTLAKE..."
  not "10CORPORATION..." ✓

## CRITICAL FLAG FOR NEXT ARCHITECT

The previous Opus handoff (2026-04-28 v01, written 2026-04-26) had
F1 and F4 directionally REVERSED in the visual comparison results:
  - Said "ours uses 4 spaces, MB uses 1" — actually MB has 4, ours 1
  - Said "EXAMINATION wraps to two lines in ours" — actually ours
    rendered as ONE line, MB has it split across two

Sonnet's byte-level recon caught both reversals before any code
shipped. Per draft RULE-FORMAT-CONSTANTS-VERIFY: never trust visual
comparison narrative without byte-verification. Always recon before
spec, always byte-verify before build.

## DEFECT SUPERSET — TIER 2 PRIORITY LIST

Cover defects FIRST (top priority — most visible to anyone opening
the depo):

M0 — Case Caption Two-Column Layout (CRITICAL)
  Status: Logged 2026-04-27 EOD
  Lines 5-9 of cover render as single-column with party name, role,
  docket, and division each on their own numbered lines. MB has
  party names LEFT column, docket/division RIGHT column on shared
  numbered lines. "Plaintiffs," and "Defendants." sub-indented under
  party names.

  Architecture: new LineKind CAPTION_ROW + case_row(left, right,
  width) helper ported from legacy/format_final.py.

  Cascades: fixing M0 resolves line-mashing on caption rows AND
  shifts cover line count down by ~2 slots, pulling stipulation/Q&A
  pagination closer to MB's structure.

M0a — Cover venue/location lines structure
  Lines 16-20 currently emit "at the offices of", firm name, address
  street, city/state on FOUR separate numbered lines. MB packs them
  into TWO numbered slots using sub-row format (paginate_doubled in
  legacy code).
  Architecture: sub-row LineKind support in Module 7.

M1 — Index page (TOC + exhibit list)
  Currently MISSING entirely. MB has full I N D E X page at page 2
  with section page refs and EXHIBITS subsection with per-exhibit
  page numbers. Reference: legacy build_index() function.

M2 — Appearances page formatting
  Two-row format with sub-rows (paginate_doubled), firm address
  indented under each block, "(Via Zoom)" suffix, midpoint dot
  between state and zip.

M3 — Stipulation full text
M4 — Reporter's Certificate (LA Article 1434 verbatim, R.S. 37:2554)
M5 — Witness's Certificate (with exhibit index + signature block)
M6 — Errata sheets (3 lines per entry, 7 per page, 2 pages)
M7 — Exhibit references in body ("(Whereupon, ...)")

Tier 3 structural (heads-down):
S1 — Front matter pagination — resolves once M0+M1+M2+M3 ship
S2 — Module 6 hardcoded turn ranges (76-89, 91-621, 503, 549, 622-636)
S3 — s2 paragraph_style semantics (28/33 follow A turns, not Q)
S4 — FormatProfile architecture (extract Module 7 constants)
S5 — BYLINE detection by text content not turn index
S6 — Cover line-count silent-drop constraint

Tier 4 — institutional memory to preserve during port:
DEF-004 steno bracket family, DEF-009 Q./A. detection, DEF-011
*REPORTER CHECK HERE*, DEF-012/012a [[REVIEW:]], DEF-013 ~~REVIEW:~~,
caption 25-line constraint, anchor injection guard.

## AUDIO ARCHITECTURE — RECON QUEUED, NOT DECIDED

Scott's hypothesis from previous engine attempt: steno-to-audio sync
was unreliable. He pivoted to whole-file Whisper transcription with
text-search-based word location.

Current architect's read: hypothesis is plausible but not byte-verified.
Could be missing data, drift, recording offset, or genuine per-stroke
unreliability — each has a different fix.

DO NOT design audio architecture before running AUDIO_SYNC_RECON
(see specs folder when committed). The recon answers 5 questions
against actual Halprin .sgxml + RTF + audio files. Outcomes:

  - Per-stroke sync exists AND aligns → slice on demand (cheap,
    matches MB's workflow)
  - Per-stroke sync exists but drifts → calibrate or fall back
  - Per-stroke only at session checkpoints → whole-file Whisper
  - Sync data garbage → whole-file Whisper

Worst case (whole-file Whisper) is acceptable: ~$1/depo, reliable,
text-alignment is solved domain.

DO NOT decide this in vacuum. Run the recon first.

## DRAFT RULES PARKED FOR CODER_MINDSET_ADDENDUM v2 BUMP

Four new rules emerged from this session's failures:

1. RULE-FORMAT-CONSTANTS-VERIFY (carried from prev Opus draft)
   Any spec claiming layout constants must include byte-level recon
   step verifying value against truth source before build.

2. RULE-HANDOFF-ARTIFACT-MANIFEST
   Every handoff must list every file created/modified/deleted in
   the session under "Artifacts Touched".
   Why: LEGACY_FORMAT_REFERENCE_v01.md was created last session,
   omitted from handoff, fresh Opus wrote a duplicate spec.

3. RULE-TRUTH-SOURCE-REGISTRY (now superseded by RULE-OPERATION-DOC)

4. RULE-OPERATION-DOC (NEW — drafted 2026-04-27 EOD after 3 lost-file
   incidents in one session)
   Master MANIFEST.md at context repo root. Every operationally
   critical file gets an entry. MANIFEST.md is the FIRST ramp URL
   every session reads. Architect/builder maintain it; Scott never
   has to ask "where is X?" again.

## OPERATION DOC — IMPLEMENTATION STATUS

Designed 2026-04-27 EOD. Implementation parked for tomorrow morning
when fresh:
  - Build mrx-context/MANIFEST.md with all known paths
  - Add RULE-OPERATION-DOC formally to ADDENDUM v2
  - Update ramp URL list in handoff template (5 URLs, MANIFEST first)
  - First-day commitment: every spec/handoff/file reference cites
    manifest entry by name, not raw path.

Tonight's handoff uses the new format (TRUTH SOURCES section at
top). Tomorrow's first task: ratify and build the manifest.

## CRITICAL DESIGN DECISIONS LOCKED (DO NOT REVISIT)

  - Positional joins for proposals/decisions/anomalies (i, not ID)
  - Whitespace tokenization for v0.1 (canary green)
  - Right-to-left application of multiple ops per turn
  - Tag rules per Module 4
  - Tier 1 fixes shipped (F1-F5 + F2-CONT) — not subject to redebate
  - Audio sync NOT decided — must follow recon

## SCOTT'S WORKING STYLE (UNCHANGED — REINFORCED TONIGHT)

- 12-year-old reading level until told otherwise
- Plain English, short answers
- ONE question at a time, NOT three
- Inline A/B/C only when there's a real choice — don't fake-choice
- He hates file dialogs — Sonnet writes files, Scott does not paste
- He hates fire-hose responses — keep messages tight
- He pushes back — pushback is usually right
- Respect the fatigue — he's been at this for weeks
- ALWAYS give full absolute paths when naming files. NEVER abbreviate.
- ALWAYS know where a file lives before mentioning it. If you don't
  know, ask Sonnet — DO NOT ask Scott to source paths.

## SCOTT'S MOOD AT SESSION CLOSE

Long session. Real wins: 5 Tier 1 defects + F2-CONT shipped, 499
tests, full visual verification on cover centering / Q./A. spacing /
CRLF / EXAMINATION split / line-number spacers / wrap continuations.

Hit hard by my failure to track operational paths. Twice asked Scott
to source the same file path I should have had captured from the
first time Sonnet touched it. He held the line and demanded a
systemic fix — OPERATION DOC is the result.

This is on me as architect. Tomorrow's session opens with the
manifest as the first thing read. Scott should never have to ask
"where is X?" again. If he does, it's a process failure, not his.

He ended the session telling me to write up tonight's handoff and
the OPERATION DOC design before signing off. Both delivered.

## REVISIT LIST (NOT BLOCKING)

[ ] AUDIO_SYNC_RECON spec — write tomorrow morning, save to specs/
[ ] OPERATION DOC build — MANIFEST.md draft + commit + ramp update
[ ] CODER_MINDSET_ADDENDUM v2 bump with all 4 new rules
[ ] Tier 2 M0 spec — case caption two-column architecture
[ ] Module 6 hardcoded turn ranges (paragraph_style derivation)
[ ] s2 semantics deep-dive
[ ] Index page generation (M1)
[ ] Stage 4 audio (after recon answers Stage 4 architecture question)

— End of Opus handoff 2026-04-27 v01 —
