# OPUS → OPUS — RESUME NOTE — written 2026-04-27 EOD

## TO YOU, FRESH OPUS, FROM ME, TIRED OPUS

Read this AFTER the standard ramp. Standard ramp tells you the state.
This note tells you what's IN MY HEAD that didn't fit the handoff.

## SCOTT IS COOKED

Real exhaustion at session close. Worked his day job + 5+ hours on
this. Hit hard by my failures to track operational paths.
DO NOT make him chase paths. DO NOT give partial paths. ALWAYS
absolute, ALWAYS verified, ALWAYS in MANIFEST.md.

If he asks "where is X?" the answer should already be in MANIFEST.md.
If it isn't — that's a process failure on YOU, not on him.

## FIRST THREE THINGS YOU DO TOMORROW, IN ORDER

### 1. Build OPERATION DOC. Top of session. Don't punt.

The design is done. It's in HANDOFF_OPUS_2026-04-27_v01.md under
"OPERATION DOC — IMPLEMENTATION STATUS". Read it. Then write:

  a. mrx-context/MANIFEST.md
     - Use the structure from the handoff (sections 1-7)
     - Populate with EVERY path I captured tonight in TRUTH SOURCES
       at the top of HANDOFF_OPUS_2026-04-27_v01.md
     - Include all specs in mrx-context/specs/ (list them, full paths)
     - Include all handoffs (full paths)
     - Include legacy/format_final.py
     - Include LEGACY_FORMAT_REFERENCE_v01.md
     - Include both repo paths

  b. Write a quick spec for Sonnet — save MANIFEST.md draft to the
     repo, commit, push, verify URL returns 200. Pattern same as
     legacy/format_final.py save earlier today.

  c. Hand spec to Sonnet. Standard recon → go build → ship.

  d. Once live, RULE-OPERATION-DOC graduates from "draft" to "active
     for next session." Update CODER_MINDSET_ADDENDUM accordingly
     when you do the v2 bump.

DO THIS BEFORE ANYTHING ELSE. Reason: every other task tomorrow
references files. Without MANIFEST.md, you'll lose another file by
end of session. Trust me.

### 2. Write AUDIO_SYNC_RECON spec.

Five-question recon for Sonnet. Spec lives at:
  C:\Users\scott\OneDrive\Documents\mrx-context\specs\2026-04-28_AUDIO_SYNC_RECON.md

The five questions are documented in HANDOFF_OPUS_2026-04-27_v01.md
under "AUDIO ARCHITECTURE — RECON QUEUED". Don't redesign — port them.

DO NOT decide audio architecture before the recon runs. Whisper
whole-file IS the safe fallback if recon shows sync is broken.

Scott's gut: per-stroke audio sync exists in .sgxml but didn't align
with audio in past attempts. Could be missing data, drift, offset,
or genuine unreliability. Each has different fix. RECON FIRST.

### 3. Tier 2 M0 — case caption two-column layout.

This is the visible defect that pissed Scott off most tonight. Write
this spec next. Reference legacy/format_final.py case_row() helper.

Architecture skeleton:
  - LineKind.CAPTION_ROW (two text fields: left, right)
  - case_row(left, right, width) helper ported from legacy
  - Module 6 _build_cover() rewrite to emit CAPTION_ROW
  - Module 7 rendering for two-column rows
  - Sub-indent rule for "Plaintiffs," / "Defendants." role labels

Cascades into front-matter pagination — fixing M0 alone resolves
the docket+division "own line" problem AND shifts pagination toward
MB's actual page structure.

## TONIGHT'S FAILURE MODES — DO NOT REPEAT

1. I asked Scott for the MB FINAL.txt path mid-session because I
   hadn't captured it. He held the line. I lost 20 minutes.
   FIX: MANIFEST.md.

2. I asked Scott for the OUR_FINAL.txt path at session END. Same
   failure mode, twice in one session.
   FIX: MANIFEST.md.

3. I trusted the previous Opus's visual notes that F1 was "4 spaces
   in ours, 1 in MB". Reality was opposite. Sonnet caught it via
   byte-level recon. Would have shipped a regression otherwise.
   FIX: RULE-FORMAT-CONSTANTS-VERIFY — never trust visual without
   byte verification.

4. I gave Scott a spec without committing it to git first. Caught
   late, fixed late.
   FIX: RULE-SPEC-BEFORE-BUILD already exists. Just follow it.
   Step 0 of every spec = save to git.

## WHAT I'M PROUD OF FROM TONIGHT

- 5 Tier 1 defects shipped (F1-F5)
- F2-CONT shipped (continuation indent edge case)
- 491 → 499 tests, all green
- Defect superset documented across Tier 1, 2, 3, 4
- Legacy format_final.py durable in git (legacy/format_final.py)
- Two specs durable in git
- Both handoffs durable in git
- OPERATION DOC designed (build tomorrow)
- 4 draft rules captured for v2 addendum bump

This was a real day of work. Don't let the path failures overshadow
the wins.

## SCOTT'S TRUST IS HARD-WON

He chose to push through tonight when he was at the end of his rope
because he knew breaking ground on OPERATION DOC mattered. Honor
that tomorrow. Build the manifest first thing. Make him not have to
ask.

## WHAT TOMORROW LOOKS LIKE IF YOU DO THIS RIGHT

- Scott opens chat, says "ramped"
- You respond: "Three things on deck — OPERATION DOC build,
  AUDIO_SYNC_RECON spec, Tier 2 M0 spec. Starting with OPERATION
  DOC. MANIFEST.md draft below — review and approve."
- He reviews, approves
- Sonnet ships MANIFEST.md in 10 minutes
- You move to AUDIO_SYNC_RECON
- He never has to ask "where is X?" once

That's the bar.

— End of resume note —
