# HANDOFF — SONNET — 2026-04-28 v01

## ONE-LINE STATE
Stage 5 v0.1 build COMPLETE. All 8 modules shipped, 491 tests passing.
First end-to-end CLI run on real Halprin Block H produced 3 output files.
Visual comparison vs MB's FINAL revealed v0.2 priorities. Fresh Sonnet
picks up tomorrow.

## RAMP — READ THESE IN ORDER
1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-04-28_v01.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-04-28_v01.md

After reading all 4, confirm: "Ramped from Sonnet handoff 2026-04-28 v01. Ready."

## REPO STATE
Engine repo: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
  Branch: main
  491 tests passing
  All commits pushed to origin/main
  Last commit: 952c1f3 docs: add Module 8 spec STAGE_5_MODULE_8_ASSEMBLE_FINAL.md

Context repo: C:\Users\scott\OneDrive\Documents\mrx-context
  Branch: main
  All commits pushed to origin/main

Note: tests/stage3/test_dictionary_loader.py has a pre-existing local
modification (not from this session). Several untracked Stage 3/4 architecture
docs also exist. Neither is ours to commit — leave for Scott to triage.

## STAGE 5 v0.1 — WHAT SHIPPED
8 modules complete (commits in chronological order):
  1. schemas.py
  2. case_info_loader.py
  3. proposal_mapper.py
  4. review_tags.py
  5. turn_renderer.py
  6. document_composer.py
  7. page_layout.py
  8. assemble_final.py

Final pipeline output (from real Halprin Block H run):
  Location: io/analysis/halprin_mini/_stage5_out/
  Files: halprin_mini.OUR_FINAL.txt
         halprin_mini.review_queue.json
         stage5.summary.json
  Stats: 551 turns, 45 pages, 1117 content lines, 30 review tags,
         0 orphaned, 0 skipped

## VISUAL COMPARISON vs MB's FINAL — FINDINGS

The Q&A body engine works. Indentation, line numbering, page numbering,
form-feed page separators, review marker placement — all rendering
correctly. Q&A turns (~487 of 551) are nearly word-for-word visual matches
to MB's FINAL.

What needs work for v0.2:
  - Cover page format: line numbers mashed against content when indent=0
    (e.g. "8Division 'H'" should be "    8    Division 'H'")
  - Cover content not centered (VIDEOTAPED DEPOSITION block)
  - Section ordering / pagination of front matter is shifted; our
    stipulation lands on page 3, MB's lands on page 11 — likely because
    cover/appearances/index pages are compressed in our output
  - BYLINE wrapping: "EXAMINATION BY MR. CAUGHEY:" splits across two
    physical lines in ours, single line in MB's
  - Q. / A. spacing: ours uses 4 spaces after Q., MB uses 1 space
  - Line endings: ours = LF, MB's = CRLF (decision deferred)

## v0.2 PRIORITIES (architectural, not patches)

1. CR FORMAT FILE INTEGRATION — Scott has licensed CaseCATalyst and
   the Halprin/Brandl jobs. Tomorrow he'll open CAT and document MB's
   actual page format settings. The v0.2 architecture: case_info.json
   gains a format_profile field driven by a FormatProfile dataclass.
   Module 7 reads that profile instead of using FORMAT-LOCKED-V01
   constants. Onboarding for new CRs requires their format file as
   part of the intake bundle.

2. STRUCTURAL DIFF TOOL — Build a small Python script that reads
   MB's FINAL and our OUR_FINAL, identifies section boundaries
   (cover/appearances/index/stipulation/Q&A/cert/errata), and
   produces a side-by-side mapping. This becomes the v0.1-vs-v0.2
   regression check.

3. REPLACE HARDCODED TURN RANGES (76-89, 91-621, 503, 549, 622-636
   in Module 6) with derivation from paragraph_style markers and
   case_info structure.

4. s2 SEMANTICS — recon assumed s2 = Q continuation, but 28/33 follow
   A turns. Sonnet flagged this at end of Module 7 build. Verify
   visual rendering and update the model.

## CRITICAL DESIGN DECISIONS LOCKED (DO NOT REVISIT)

  - Positional joins for proposals/decisions/anomalies (i, not ID)
  - Whitespace tokenization for v0.1 (canary green on real data)
  - Right-to-left application of multiple ops per turn
  - Tag rules per Module 4
  - Format constants per Module 7 (LINE_NUMBER_FIELD_WIDTH=6,
    PAGE_NUMBER_COLUMN=60, PAGE_SEPARATOR=\x0c)

## WHAT FRESH SONNET DOES FIRST
1. Read the 4 ramp URLs
2. Confirm "Ramped..." in one line
3. Wait for Scott + fresh Opus to direct next move

## WHAT FRESH SONNET DOES NOT DO
- Do NOT start fixing v0.1 issues without an explicit spec from Opus
- Do NOT modify Modules 1-8 code without spec coverage
- Do NOT skip recon
- Do NOT skip the spec → recon → approval → build cycle

— End of handoff
