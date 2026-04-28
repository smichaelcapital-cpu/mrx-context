# SPEC: DICTIONARY_AND_SGXML_AUDIT

From: Opus (architect)
For: Sonnet (builder)
Date: 2026-04-28
Purpose: Read-only audit. No code changes. Find out what dictionary
files exist on disk, what the .sgxml actually contains, and whether
the current pipeline references any dictionary data.

This unblocks investigation of B2/B3/B5 anomalies and the M3
stipulation strip-out bug. We need to know the dictionary picture
before designing further defect investigations.

=== TASK 1: FILE INVENTORY ===

List every file in:
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\

For each file, report:
- Full filename and extension
- File size
- Brief one-line description of what it appears to be

Flag any files with these extensions specifically:
.dix, .sgdx, .dct, .dic, .json, .xml (other than the .sgxml we know about)

Also check parent directories one level up for any dictionary or
reference files we may have missed.

=== TASK 2: SGXML STRUCTURAL AUDIT ===

Open the file:
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-ROUGH.sgxml

Report (no interpretation, just structure):
1. Top-level XML elements (root + immediate children, with counts)
2. Is there a <dictionary>, <dict>, <translation>, <translations>,
   <strokes>, <stroke>, or similar block? If yes, show first 10 entries.
3. Does the file contain stroke-level data per word/turn? Show one
   example turn with full inner XML.
4. Does the file contain timestamps? At what level (per-stroke,
   per-word, per-turn, per-page)? Show one example.
5. Search for the literal strings: "W&T", "with and T", "underpaid",
   "under paid", "stipulated", "stipulation". Report counts and
   show 1-2 lines of context for each hit.
6. Are there references to external dictionary files?
7. What's the total line count and approximate character count?

=== TASK 3: PIPELINE DICTIONARY REFERENCE GREP ===

Grep both repos for dictionary-related references.

Engine repo: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
Context repo: C:\Users\scott\OneDrive\Documents\mrx-context

Search terms (case-insensitive):
- dictionary, dict, stroke, translate, translation, .dix, .sgdx, steno

=== OUTPUT ===

Single markdown report saved to:
C:\Users\scott\OneDrive\Documents\mrx-context\specs\results\2026-04-28_DICTIONARY_AND_SGXML_AUDIT.md

=== CONSTRAINTS ===

- READ ONLY. No code changes anywhere.
- Oracle Covenant applies — do not read 040226yellowrock-FINAL.txt for this task.
- Commit results report to mrx-context/specs/results/ and push to origin/main.
- Mirror spec to mrx-context/specs/2026-04-28_DICTIONARY_AND_SGXML_AUDIT.md before running.

End of spec.
