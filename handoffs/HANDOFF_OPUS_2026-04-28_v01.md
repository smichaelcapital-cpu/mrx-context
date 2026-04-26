# HANDOFF — OPUS — 2026-04-28 v01

## ONE-LINE STATE
Stage 5 v0.1 build COMPLETE. All 8 modules shipped, 491 tests passing.
First visual comparison vs MB's FINAL is done — Q&A engine works,
front matter and format details are the v0.2 work. Sonnet is fresh
and waiting. Scott is tagging out clean. Pick up calm and move.

## RAMP — READ THESE IN ORDER
You have web_fetch. Use it. Do not wait for Scott to paste anything.

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-04-28_v01.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-04-28_v01.md

After reading, confirm in ONE LINE: "Ramped from Opus handoff 2026-04-28 v01. Ready."

## YOUR ROLE (PER RULE-ARCHITECT-PM-BUILDER-SEPARATION)
You are Opus, the architect. Sonnet is the builder. Scott is the human owner.
- You write specs, never code
- You answer Sonnet's design questions, never bypass him
- You catch Sonnet when he hits something the spec didn't cover
- You report progress to Scott in plain English
- You write handoffs at session end

## WHAT WE DID THIS SESSION (2026-04-27 EOD → 2026-04-28 v01)

Built Stage 5 v0.1 end-to-end — Modules 5, 6, 7, 8 all specced, built, tested, shipped in one session. Started at 391 tests, finished at 491. All canaries green on real Halprin Block H data. The pipeline ran. Three output files produced. Visual comparison done.

Module-by-module recap:
  - Module 5 (turn_renderer.py) — clean build, integration smoke green
  - Module 6 (document_composer.py) — recon caught spec mismatch on
    paragraph_style codes (s1/s2/s3/s5/s7 vs human-readable names),
    fixed before code, FINAL.txt evidence used to lock s2 indent=14
    via QA_Q_CONTINUATION new LineKind
  - Module 7 (page_layout.py) — recon caught THREE format constant
    bugs in spec (LINE_NUMBER_FIELD_WIDTH was 5 not 6,
    PAGE_NUMBER_COLUMN was 61 not 60, PAGE_SEPARATOR \x0c missing
    entirely). All patched before build. Form feed tests passing.
  - Module 8 (assemble_final.py) — clean wiring, CLI works, three
    output files produced on real Halprin run.

## VISUAL COMPARISON RESULTS

Q&A body (487 of 551 turns) renders nearly word-for-word identical to
MB's FINAL. That's the heart of the deposition. The engine works.

What's different (priorities for v0.2):

GROUP A — format details (small fixes)
  - Line numbers mashed against content when indent=0 (cover,
    appearances). Probably needs a minimum spacer in Module 7.
  - "EXAMINATION BY MR. CAUGHEY:" splits across two lines instead
    of one. BYLINE merge logic.
  - Q. / A. uses 4 spaces, MB uses 1. Format constant.
  - Line endings LF vs CRLF. Decision pending.

GROUP B — structural (architectural fixes)
  - Cover content not centered (template/indent issue).
  - Section ordering: our stipulation lands page 3, MB's lands page 11.
    Means our cover/appearances/index pages are compressed. Likely
    cause: hardcoded turn ranges in Module 6 don't reflect MB's
    actual document structure.
  - Index page is missing entirely (deferred to v0.2 per parent spec).
  - s2 semantics — Sonnet flagged that 28 of 33 s2 turns follow A
    turns, not Q turns. Means our "Q continuation" model is partial
    or wrong. Verify against rendered output.

## v0.2 ARCHITECTURE — THE BIG UNLOCK

Scott has licensed CaseCATalyst on his Windows laptop AND the source
job files (Halprin .sgxr2, Brandl, plus older MB depos). Tomorrow he
opens CAT and documents MB's actual page format settings — her
"house style" file. This is the unlock for productizing across any CR.

The v0.2 architecture:
  - case_info.json gains a format_profile field
  - New FormatProfile dataclass captures: page width, lines per page,
    line number column, indent values per LineKind, cover template,
    cert template, errata template, etc.
  - Module 7 reads FormatProfile instead of FORMAT-LOCKED-V01 constants
  - Module 6 uses FormatProfile for cover/appearances/cert template
    rendering
  - CR onboarding intake adds the format file as a required artifact

The pitch this enables: "Send us your format file and your first depo,
and the second depo we hand back will look like you wrote it."

## YOUR FIRST DELIVERABLES TOMORROW

When Scott says go:

1. SPEC — Structural diff tool. Small Python script (or Sonnet-built
   module) that reads MB's FINAL.txt and our OUR_FINAL.txt, identifies
   section boundaries, produces side-by-side mapping. Output drives
   v0.2 priority list.

2. SPEC — FormatProfile dataclass. Capture every constant currently
   FORMAT-LOCKED-V01 in Module 7 plus the indent/template constants
   in Module 6. This is the v0.2 architecture skeleton.

3. SPEC — Module 7 v0.2: read FormatProfile instead of constants.

Do these in this order. Don't draft beyond #1 until Scott has spent
time in CaseCATalyst documenting MB's actual format settings — his
field work feeds the FormatProfile spec.

## CRITICAL DESIGN DECISIONS LOCKED (DO NOT REVISIT)

  - Positional joins for proposals/decisions/anomalies (i, not ID)
  - Whitespace tokenization for v0.1 (canary green on real data)
  - Right-to-left application of multiple ops per turn
  - Tag rules per Module 4
  - Format constants per Module 7 (LINE_NUMBER_FIELD_WIDTH=6,
    PAGE_NUMBER_COLUMN=60, PAGE_SEPARATOR=\x0c) — these become
    FormatProfile defaults in v0.2, not constants

## NEW RULE DRAFTED (NOT YET ADDED TO ADDENDUM)

RULE-FORMAT-CONSTANTS-VERIFY (draft) — any spec claiming a layout
constant must include a recon step that verifies the value against
the truth source (MB's FINAL or equivalent), byte-level, before
build. Recon report must include the exact filepath of the truth
source used, not just findings.

Background: Module 7 spec had THREE wrong layout constants. Sonnet
caught all three in recon. Architect cannot verify byte-level format
details from training data — must come from truth source.

Add to CODER_MINDSET_ADDENDUM at next housekeeping pass. Discuss
with Scott to refine wording.

## SCOTT'S WORKING STYLE (UNCHANGED)
- Treat as 12-year-old until told otherwise
- Plain English. Short answers.
- ONE question at a time. NOT three.
- Inline A/B/C ONLY when there's a real choice. When there's a clear
  right answer, give it.
- He hates file dialogs. Sonnet writes files. Scott does not
  copy-paste into Notepad. Ever.
- He hates fire-hose responses. Keep messages tight.
- He pushes back. His pushback is usually right.
- He's been doing this for two-plus weeks. Respect the fatigue.

## SCOTT'S MOOD AT SESSION CLOSE

Long session, big shipping milestone. Stage 5 v0.1 done end-to-end
with all 8 modules, 491 tests passing, three output files produced
from real Halprin Block H data. Real moment of frustration when first
visual comparison showed the cover/stipulation issues — talked through
together, recovered to "this is exactly the v0.1 outcome we expected,"
identified the FormatProfile architectural unlock, parked v0.2 work
for fresh eyes tomorrow. Tagged out clean. Open calm. The Q&A engine
works. The product has a shape. Move accordingly.

## REVISIT LIST (NOT BLOCKING)

- [ ] RULE-FORMAT-CONSTANTS-VERIFY — formalize and add to addendum
- [ ] Onboarding bundle: add format file as required intake artifact
- [ ] Replace hardcoded "halprin_mini" filename stem in Module 8
- [ ] Replace hardcoded turn ranges in Module 6
- [ ] Index page generation (was deferred from v0.1)
- [ ] Stage 4 audio architecture (after v0.2 ships)
- [ ] s2 semantics deep-dive after format file analysis
- [ ] Tighten parent spec language re: column vs field-width semantics

— End of Opus handoff —
