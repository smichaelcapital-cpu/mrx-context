Save to:
C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET_2026-04-27_v01.md

Commit message: handoffs: add Sonnet handoff 2026-04-27 v01

Then push to origin/main and verify:
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-04-27_v01.md

Returns 200 = done. Report commit hash + 200.

CONTENTS BELOW THIS LINE
========================

# HANDOFF — SONNET — 2026-04-27 v01

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
  Branch: main
  github.com/smichaelcapital-cpu/Court_reporting_demo

Context repo:
  C:\Users\scott\OneDrive\Documents\mrx-context
  Branch: main
  github.com/smichaelcapital-cpu/mrx-context

Master copies (canonical reference docs — read-only):
  C:\Users\scott\OneDrive\Documents\MASTER_COPIES\

## ONE-LINE STATE
Tier 1 + F2-CONT shipped today, 499 tests passing on main, both 
commits pushed. Tier 2 M0 (case caption two-column) is next 
priority — spec coming from Opus tomorrow.

## RAMP — READ THESE IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/MANIFEST.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-04-27_v01.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-04-27_v01.md

After reading, confirm: "Ramped from Sonnet handoff 2026-04-27 v01. Ready."

NOTE: MANIFEST.md is the FIRST ramp URL. If it doesn't exist yet, 
fall back to handoff search but flag it to Scott — Operation Doc 
implementation is in progress.

## YOUR ROLE (PER RULE-ARCHITECT-PM-BUILDER-SEPARATION)
You are Sonnet, the builder. Opus is the architect. Scott is the 
human owner.

Your job:
- Recon any multi-file change before code (RULE-RECON-FIRST)
- Build from spec, push back with evidence when you see risk
- Run tests, run pipelines, verify byte-level
- Commit + push
- Update MANIFEST.md when you create/move/modify any operationally 
  critical file (RULE-OPERATION-DOC, draft)

Your job is NOT:
- Design decisions — escalate to Opus
- Multi-file changes without a written spec — RULE-SPEC-BEFORE-BUILD
- Skipping recon — RULE-RECON-FIRST
- Trusting visual notes from Opus without byte-verification — 
  RULE-FORMAT-CONSTANTS-VERIFY (you've already been burned twice 
  today by reversed visual claims; trust your byte-level recon)

## REPO STATE AT SESSION CLOSE

Engine repo C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1:
  Branch: main, clean working tree
  Last commits (chronological):
    77a0c74 — Tier 1 batch (F1-F5)
    387b8ac — F2-CONT wrap continuation indent
    5a4463c — F2-CONT spec
  All pushed to origin/main
  Tests: 499 passing
  Pre-existing local modification on tests/stage3/test_dictionary_loader.py 
  (not from this session — leave for Scott to triage)

Context repo C:\Users\scott\OneDrive\Documents\mrx-context:
  Branch: main, clean working tree
  Last commits (chronological):
    2a294c7 — legacy/format_final.py + reference doc updated
    a2f9dc3 — Tier 1 v2 spec mirror
    f63ccd0 — F2-CONT spec mirror
    8b3c8f1 — Opus handoff 2026-04-27 v01
  All pushed to origin/main

## WHAT SHIPPED THIS SESSION

Tier 1 Format Defect Batch (commit 77a0c74):
  F1 — Q./A. spacing fix in src/stage5/page_layout.py:171-228
  F2 — Indent fix in src/stage5/document_composer.py (cover + appearances)
  F3 — CRLF in src/stage5/assemble_final.py:119 + test rename
  F4 — EXAMINATION split in src/stage5/document_composer.py:109-126
  F5 — Cover centering in src/stage5/document_composer.py
  Tests: +5 (491 → 496)

F2-CONT (commit 387b8ac):
  src/stage5/page_layout.py — _wrap_line() continuation indent fallback
  cont_indent = wrap_indent if wrap_indent != 0 else indent
  Test: tests/stage5/test_page_layout::test_33_wrap_continuation_inherits_indent
  Tests: +1 (498 → 499)

OUR_FINAL.txt size after F2-CONT: 57,747 bytes

## WHAT FRESH SONNET DOES FIRST TOMORROW

1. Read all 5 ramp URLs in order
2. Confirm "Ramped from Sonnet handoff 2026-04-27 v01. Ready."
3. Run RULE-BRANCH-CHECK: git branch --show-current on both repos. 
   Both should be main, clean.
4. Run pytest tests/ -q on engine repo. Should report 499 passing.
5. Wait for Opus to direct next move.

## WHAT FRESH SONNET DOES NOT DO

- Do NOT start fixing Tier 2 defects without explicit spec from Opus
- Do NOT modify v0.1 modules (5/6/7/8) without a written spec
- Do NOT skip recon
- Do NOT skip the spec → recon → approval → build cycle
- Do NOT trust Opus's visual claims without byte-level recon. Today 
  Opus had F1 and F4 directionally REVERSED in the original spec. 
  Your byte-level recon caught both. Keep doing that.
- Do NOT design audio architecture before AUDIO_SYNC_RECON runs
- Do NOT delete or rename anything in MASTER_COPIES

## TIER 2 M0 — NEXT BUILD (when spec arrives)

The defect: cover page case caption renders as single-column. MB has 
two-column layout — party names left, docket/division right, with 
sub-indented role labels.

When Opus writes the spec, it will likely require:
- New LineKind.CAPTION_ROW in src/stage5/schemas.py
- Port case_row(left, right, width) from 
  C:\Users\scott\OneDrive\Documents\mrx-context\legacy\format_final.py 
  (read-only reference, do not import)
- Module 6 _build_cover() rewrite
- Module 7 rendering for two-column rows

Wait for the spec. Don't pre-build.

## PROCESS FAILURES THIS SESSION (LEARN FROM)

Three lost-file incidents in one session:

1. LEGACY_FORMAT_REFERENCE_v01.md existed but Opus didn't know it 
   existed (created in prior session, omitted from prior handoff). 
   Your recon caught it before duplicate work shipped.
2. MB FINAL.txt path lost mid-session — Opus had to ask Scott. You 
   knew the path; the architect did not.
3. OUR_FINAL.txt path lost at end of session — same failure mode.

The structural fix is OPERATION DOC: a master MANIFEST.md at the 
context repo root that lists every operationally critical file with 
its full absolute path. Every session reads MANIFEST.md FIRST. 
Every session that creates or modifies a critical file updates 
MANIFEST.md before closing.

Tomorrow's first build is likely creating MANIFEST.md and adding 
RULE-OPERATION-DOC to the addendum.

## DRAFT RULES PARKED FOR ADDENDUM v2 BUMP

1. RULE-FORMAT-CONSTANTS-VERIFY — byte-verify layout constants 
   before code
2. RULE-HANDOFF-ARTIFACT-MANIFEST — every handoff lists every 
   artifact touched
3. RULE-OPERATION-DOC — master MANIFEST.md, first ramp URL, 
   universal file index

## AUDIO ARCHITECTURE — RECON QUEUED

DO NOT design audio architecture. AUDIO_SYNC_RECON spec coming 
tomorrow. The recon answers 5 questions against Halprin .sgxml + 
RTF + audio. Outcomes determine whether to build slice-on-demand 
audio verification or whole-file Whisper transcription.

## SCOTT'S WORKING STYLE (UNCHANGED)

- 12-year-old reading level until told otherwise
- Plain English, short answers
- ONE question at a time
- Hates file dialogs — you write files, he doesn't paste into Notepad
- Hates fire-hose responses
- Pushes back — usually right
- ALWAYS give full absolute paths when naming files
- ALWAYS update MANIFEST.md when you create/move/modify a critical file

## CRITICAL DESIGN DECISIONS LOCKED (DO NOT REVISIT)

  - Positional joins for proposals/decisions/anomalies (i, not ID)
  - Whitespace tokenization for v0.1 (canary green on real data)
  - Right-to-left application of multiple ops per turn
  - Tag rules per Module 4
  - Tier 1 fixes shipped (F1-F5 + F2-CONT) — not subject to redebate
  - Audio sync NOT decided — must follow AUDIO_SYNC_RECON

— End of Sonnet handoff 2026-04-27 v01 —-