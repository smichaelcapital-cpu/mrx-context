# SPEC: Frequency Distribution of All 742 Diff Blocks

Date: 2026-05-03
Author: Opus
Builder: Sonnet
Status: APPROVED for build

## Goal
Read every one of the 742 diff blocks in halprin_full.diff_report.md.
Bucket each block into a category. Produce a real frequency table.
No sampling, no estimates. Count everything.

## Input
Raw URL of the existing diff report (already pushed):
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-03/halprin_full.diff_report.md
Or local: io/analysis/halprin_full/_diff_out/halprin_full.diff_report.md

## Method
For each block (delimited by `### Block N`), inspect the **replace** section.
Look at what's in `**+...+**` (MB has, OURS missing) and `**-...-**` (OURS has, MB missing).
Classify into ONE bucket using the catalog below. If a block contains multiple
patterns, classify by the DOMINANT one. If unclear, use `unclassified`.

## Starter category catalog (15 buckets — extend if needed)

1. comma_drop                — MB has comma, OURS missing
2. em_dash_drop               — MB has ` -- `, OURS missing
3. cap_proper_noun            — capitalization differs on names/titles/companies
4. quote_marks_stripped       — MB has `"word"`, OURS has `word`
5. hyphenation                — MB hyphenates compound, OURS doesn't (or reverse)
6. word_drop                  — OURS missing a word MB has (flew, joined, claim, etc.)
7. number_style               — MB writes "Twenty-five" / OURS "25" or similar
8. acronym_mangle             — E&P / W&T / M&M corruption (any direction)
9. terminator_punctuation     — period/question/exclamation differs at sentence end
10. speaker_attribution_punct — "Mr. X, who" vs "Mr. X. Who"
11. phonetic_disaster         — wrong word entirely (cyst/analysis, geneos/gone, judge/why)
12. doubled_word              — same word repeated
13. pronoun_preposition_swap  — their/there, did/do, in/at, but/you-don't
14. style_object_objection    — "Object to form" vs "Objection to form"
15. unclassified              — doesn't cleanly fit anything above

If you find a 16th category that has 5+ instances, add it and report.

## Output
Markdown report at:
- io/analysis/halprin_full/_diff_out/halprin_full.frequency_report.md
- Mirror to mrx-context/reports/2026-05-03/halprin_full.frequency_report.md

Format:

### Header
- Total blocks counted
- Date / engine commit
- Note: "Each block classified by dominant pattern; some blocks contain multiple"

### Frequency table
| Rank | Category | Count | % of 742 | Example block # |
|---|---|---|---|---|
(sorted descending by count)

### Per-category sample
For each category, list the 3 lowest-numbered block IDs that fall in it,
so Scott can spot-check classifications.

### Anything notable
- New category added (if any), why
- High `unclassified` count? Note the most common shape inside it.

## Acceptance criteria
- [ ] Total counts sum to 742 (no block double-counted, none missed)
- [ ] Frequency table sorted descending
- [ ] At least 3 sample block IDs per category
- [ ] Pushed to both repos, raw URL returned

## Estimate
30-45 minutes. Pencil job. Don't overbuild.

## Prime Directive
Read-only analysis. No engine changes. No risk.
