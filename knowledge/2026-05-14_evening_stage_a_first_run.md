# Stage A v0 — First Full Pipeline Run

**Date:** 2026-05-14 evening
**Branch:** feature/stage-a-aligner-differ-v0 (commit 6d330aa, wip — not yet merged)
**Raw evidence file (local only, 136 MB, gitignored):** C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\mb_evidence_raw.json

---

## Run Summary

| Field | Value |
|---|---|
| Depos analyzed | 4 |
| Total diff events | 451,335 |
| Total patterns | 75,430 |
| Output: mb_evidence_raw.json | 150 MB |
| Output: mb_frequency_summary.json | 22 MB |

---

## Depos Analyzed

| # | Depo ID | RAW tokens | FINAL tokens | Ratio | Diff events |
|---|---|---|---|---|---|
| 1 | halprin_040226 | 102,848 | 133,366 | 1.30x | 129,180 |
| 2 | easley_031326 | 77,401 | 90,985 | 1.18x | 80,979 |
| 3 | brandl_032626 | 133,636 | 96,298 | 0.72x | 110,181 |
| 4 | church_073124 | 11,212 | 133,172 | 11.87x | 130,995 |

---

## Top 20 Patterns (sorted by pct_of_depos, then total_occurrences)

| % depos | occurrences | category | raw_token | final_token |
|---|---|---|---|---|
| 100% | 55,487 | whitespace_changed | None | `' '` |
| 100% | 32,736 | whitespace_changed | `' '` | None |
| 100% | 29,213 | line_break_changed | None | `'\n'` |
| 100% | 11,224 | punctuation_added | None | `'.'` |
| 100% | 9,863 | punctuation_removed | `'.'` | None |
| 100% | 4,200 | punctuation_added | None | `','` |
| 100% | 4,092 | whitespace_changed | `'  '` | None |
| 100% | 3,191 | punctuation_removed | `','` | None |
| 100% | 2,974 | other | None | `'the'` |
| 100% | 2,625 | line_break_changed | `'\n'` | None |
| 100% | 2,494 | punctuation_removed | `'?'` | None |
| 100% | 2,098 | other | None | `'to'` |
| 100% | 2,075 | other | None | `'A'` |
| 100% | 2,057 | other | None | `'that'` |
| 100% | 1,979 | other | None | `'I'` |
| 100% | 1,957 | punctuation_added | None | `'?'` |
| 100% | 1,902 | other | `'A'` | None |
| 100% | 1,663 | other | `'Q'` | None |
| 100% | 1,592 | line_break_changed | `' '` | `'\n'` |
| 100% | 1,507 | other | None | `'you'` |

---

## Anomaly Flags

### Church 073124 — 12x RAW/FINAL token ratio
- RAW: 11,212 tokens. FINAL: 133,172 tokens.
- All other pairs are in the 0.72–1.30x range.
- Most likely cause: wrong RAW file paired with the FINAL, or the RAW is an extremely terse rough draft.
- **Church data should NOT be trusted for fingerprinting until this is investigated.**
- Action needed: Scott to verify the Church RAW file at `C:\Cat4\usr\scott\073124CHURCH-ROUGH.txt` is the correct pair for `073124church3-FINAL.txt`.

### em_dash_inserted not in top 20
- The pattern exists in the data but ranks below position 20.
- Expected: it should be a significant MB habit.
- Explanation: top 20 is dominated by high-volume whitespace and formatting noise from the RAW→FINAL structural transformation (page numbers, line breaks, spacing normalization).
- Action: filter out whitespace_changed and line_break_changed to see the habit patterns more clearly.

### Top 20 dominated by whitespace/formatting noise
- whitespace_changed and line_break_changed together account for the top 3 patterns and several others.
- This is expected: RAW has no page structure, FINAL has numbered pages with form feeds and consistent spacing.
- For MB habit fingerprinting, these categories should be suppressed or filtered in the frequency view.
- The signal (em_dash, capitalization, filler word removal, punctuation habits) is present in the data — just ranked below the noise.

---

## Notes

- Runtime: under 2 minutes for all 4 pairs (chunked alignment working as designed)
- Pipeline printed live progress at every stage — no silent thinking
- Both output files written successfully to `fingerprints/stage_a/`
- Stage A code branch NOT yet merged to main — pending Scott + Opus review of this data
