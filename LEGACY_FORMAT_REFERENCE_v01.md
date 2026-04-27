# LEGACY FORMAT REFERENCE — format_final.py
**Surfaced:** 2026-04-28 v01
**Status:** PRIMARY REFERENCE for House of Style v0.2 work.
**Origin:** Pre-Stage-5-architecture renderer. Production-tested
against MB's real output across multiple depos (Easley, Brandl,
Halprin, Cox).

## Why This File Matters

The Stage 5 v0.1 build we just shipped has clean modular architecture
(8 modules, 491 tests) but minimal real-world format knowledge —
constants and templates were recon'd from MB's FINAL.txt one byte at
a time during this session.

`format_final.py` is the inverse: a monolithic renderer with deep,
production-tested format knowledge. Every constant in it has been
measured directly from MB's PDFs. Every house-style rule was added
because something was wrong without it. Every bug fix carries
institutional memory in its comments (DEF-004, DEF-009, DEF-011,
DEF-012, DEF-012a, DEF-013).

This is more valuable than opening CaseCATalyst because it represents
the RESOLVED output — what MB's CAT settings + her stylistic choices
+ LA legal requirements actually produce. CAT shows the source; this
shows the answer.

## What's In It

### Measured-from-PDF constants
- LINE_WIDTH = 64 chars (7.59" - 1.129" / 0.1" per char)
- QA_LINE_WIDTH = 52
- Q/A wrap: first_width=42, cont_width=45 (calibrated 52→211pp,
  47→218pp, 44→target ~223pp where MB=223)
- Colloquy indent = 14 chars (measured x0=2.499")
- Witness signature indent = 18 chars (measured x0=210.9)
- Body indent at x0=81.3 → 0 chars

### MB house-style rules
- "(Zoom)" → "(Via Zoom)" normalization
- Midpoint dot between state and zip ("Louisiana· 70130")
- Two-row appearances format with sub-rows (50-string flat list,
  pairs as main/sub)
- Single EXAMINATION header per witness (subsequent BY MR. X:
  lines bare)
- Whereupon parentheticals indented 14 chars, no Q/A label
- Witness info block at 8-char indent
- Consecutive same-type Q/A blocks merge ("All right." then "Are
  you ready?" = one Q)
- Witness info reordering: VIDEOGRAPHER first, then witness name/
  oath (steno order is opposite)

### Louisiana legal layer
- "No blank numbered lines on body pages" rule with documented
  exceptions (final page, title page, contents, appearances,
  stipulations, certificates)
- Article 1434 certificate language verbatim
- R.S. 37:2554 oath authority

### Section templates
- build_caption — 25-line page with reporter credit, with the
  line-count constraint solved and documented in docstring
- build_reporter_cert — 2-page LA cert, full legal language
- build_witness_cert — exhibit index + signature block
- build_errata — 3 lines per entry, 7 per page, 2 pages
- build_index — TOC + exhibit list with multi-page overflow
- format_appearances — config-first / steno-fallback path
- format_stipulation — paragraph wrapping
- format_testimony — Q/A labeling + colloquy + whereupon dispatch

### Configuration architecture (already a House of Style precursor)
- CASE_CAPTION.json — human-verified, authoritative
- depo_config.json — AI-extracted fallback
- boilerplate_blocks.json — pre-populated structural sections
- correction_log.json — drives review-anchor system

### Bug-history comments to PRESERVE during port
- DEF-004 steno bracket artifact family
- DEF-009 Q./A. with whitespace OR end-of-block
- DEF-011 *REPORTER CHECK HERE* with line wrap
- DEF-012/012a [[REVIEW:]] double-bracket forms
- DEF-013 ~~REVIEW:...~~ multiline system error tags
- Caption 25-line constraint (silent-drop bug from blank insertion)
- Anchor injection guard against [[REVIEW:]] outer-bracket form

## How v0.2 Should Use It

1. MINE every measured constant for FormatProfile (MB's house style
   layer) and StateProfile (LA Freelance/Deposition layer).
2. PORT every house-style rule into the appropriate Module 6 builder
   or Module 7 layout pass — preserving the comment that explains
   why each rule exists.
3. EXTRACT each section template (caption, cert, errata, index) into
   a Template class that takes case_info + format_profile and emits
   LogicalLines.
4. KEEP the bug-history comments alive in the ported code — that
   institutional memory is more valuable than the lines of code
   themselves.
5. TREAT format_final.py as the gold standard for House of Style
   v0.2 acceptance: the new pipeline must produce output equivalent
   to (or better than) what this renderer produced.

## File Location

The full source is at `legacy/format_final.py` in this repo.
Fetch URL:
  https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/legacy/format_final.py

Originally sourced from:
  C:\Users\scott\OneDrive\Documents\MASTER_COPIES\mb_demo_engine_v4\format_final.py
Saved into context repo: 2026-04-27.

## Architectural Note

This file SUPERSEDES the pure-recon approach to v0.2 specs. Where the
Stage 5 v0.1 specs (Modules 6 and 7) said "Sonnet greps for distinct
paragraph_style values" or "Sonnet visually verifies indent against
FINAL.txt" — for v0.2, the answer is "consult format_final.py for the
production-tested value, then verify it still matches MB's current
output." The mining-then-verify pattern is faster and more accurate
than recon-from-zero.

— End Legacy Format Reference —
