# SPEC: HALPRIN_RECON_FULL
Save to: mrx-context/specs/2026-04-28_HALPRIN_RECON_FULL.md + mirror to mrx_engine_v1/docs/specs/
For: Sonnet (builder)
From: Opus (architect)
Date: 2026-04-28

## Purpose
Before we spec architectural fixes for the front-page defects (M0/M0a/M2/M3) and body-text issues (Bucket 2), we need to know per defect: is the gap in the source RTF, in the pipeline, or in MB's hand-polish?
Every architectural decision downstream depends on this answer. Don't build before knowing.

## Inputs
Three files (full absolute paths):

- Source RTF (Stage 1 input):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-ROUGH_Tsmd.rtf
- MB's FINAL (truth source — READ ONLY, Oracle Covenant):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-FINAL.txt
- Our OUR_FINAL (current pipeline output):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt

## Output
ONE markdown report with a verdict table. Save to:
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_recon_2026-04-28.md
Plus print summary to terminal.

## What to check (per defect)
For EACH defect below, count occurrences in all three files, then assign verdict.

### Verdict codes:
- A = Source RTF lacks it, MB inserts during polish → expected, not a bug
- B = Source RTF has it, pipeline strips it → real bug
- C = Source RTF has it, pipeline preserves it → no defect, visual review error
- D = Source RTF has it in different form (e.g. RTF control word), pipeline doesn't translate → narrow translation bug

### Defect 0428-5 (Stipulation content)
- Search source RTF for: "It is stipulated", "stipulated and agreed", "pursuant to Notice", "Louisiana Code of Civil Procedure"
- Search MB FINAL for same phrases
- Search OUR_FINAL for same phrases
- Verdict: A or B?

### Defect B1 (Interrupting dashes --)
- Search source RTF for: --, — (em dash U+2014), – (en dash U+2013), \emdash, \endash, INTERRUPT
- Search MB FINAL for: -- (with surrounding spaces)
- Search OUR_FINAL for: --
- Report counts for each pattern in each file
- Verdict per pattern: A, B, C, or D?

### Defect B2 (Compound words split)
- Specific phrase: under paid vs underpaid
- Search all three files
- Verdict: A or B?

### Defect B3 (Sentence breaks merged)
- Specific phrase: launch in. Does (MB) vs launch in, does (ours)
- Search all three files
- Verdict: A or B?

### Defect B4 (Word-level errors)
- Specific phrases: I no one vs I know one; Warren seal vs Warren Seal
- Search all three files
- Verdict: A or B?

### Defect B5 (Brand casing)
- Specific phrases: with and T offshore, W&T Offshore, W and T Offshore, WT Offshore
- Search all three files
- Verdict: A, B, or D?

### Defect 0428-1, 0428-2, 0428-3 (formatting/layout)
- These are layout, not content. Recon NOT needed at text level.
- Instead: count line-numbered slots used by each file for cover (lines 1-25), VIDEOTAPED block (where it lives), and APPEARANCES section.
- Report deltas in slot counts. Confirms "ours uses more slots than MB" hypothesis quantitatively.

## Output report format
```markdown
# HALPRIN RECON — 2026-04-28

## Defect 0428-5 (Stipulation)
- Source RTF "stipulated and agreed": [count]
- MB FINAL "stipulated and agreed": [count]
- OUR_FINAL "stipulated and agreed": [count]
- VERDICT: [A/B] — [one-line reasoning]

## Defect B1 (dashes)
[same structure]

[... etc for B2-B5, 0428-1, 0428-2, 0428-3 ...]

## Summary
- Pipeline bugs (B/D verdicts): [list]
- Polish work (A verdicts): [list]
- Visual review errors (C verdicts): [list]
- Recommended next step: [one paragraph]
```

## Constraints
- Oracle Covenant: MB FINAL is READ-ONLY. No copying values into code. No hardcoding from it.
- No code changes in this task. Recon only.
- Use rg (ripgrep) or grep — your choice. Python script if cleaner.
- Save report to git: mrx-context/specs/results/2026-04-28_HALPRIN_RECON_RESULTS.md after recon completes.
