# MB Archive Inventory Summary -- 2026-05-10
**Date:** 2026-05-10

Sanitized metrics only. No witness names, case IDs, folder paths, or filenames.

---

## Pair Counts (Deduplicated)
| Classification | Count |
|---|---|
| Cat A: sgngl ROUGH + txt/rtf FINAL (directly usable) | 340 |
| Cat B genuine: sgngl ROUGH + sgngl FINAL, different sizes | 82 |
| Cat B suspect: sgngl+sgngl, same size (likely backup copies) | 340 |
| Rough-only (no paired final found) | 1531 |
| Final-only (no paired rough found) | 398 |
| Total unique transcript files (deduplicated) | 4206 |
| Total folders scanned | 114 |

**Prior inventory (2026-05-09):** 7 confirmed pairs
**New pairs found today (Cat A):** 334

---

## Date Range (Cat A pairs)
- Earliest year: 2013
- Latest year: 2026
- Span: 14 years

## Cat A Pairs by Year
| Year | Pairs |
|---|---|
| 2013 | 1 |
| 2014 | 2 |
| 2015 | 35 |
| 2016 | 43 |
| 2017 | 6 |
| 2018 | 2 |
| 2019 | 1 |
| 2020 | 1 |
| 2022 | 58 |
| 2023 | 51 |
| 2024 | 64 |
| 2025 | 56 |
| 2026 | 14 |

---

## Structural Findings
- Archive spans approximately 14 years of work
- Two final transcript formats: plain text (.txt, modern era) and RTF (.rtf, pre-2019 era)
- AutoArchive folder contains rough-only auto-saves; not counted as additional pairs
- Duplicates exist across subfolders (same file in root + subfolder); deduplicated by filename
- 340 same-size sgngl+sgngl pairs likely represent auto-backup file pairs, not genuine edits
- Filename date convention varies by era: 6-digit (MMDDYY) standard for most; 7-8 digit anomalies in older folders

## Recommendation for Calibration Set
- Cat A pairs (340 total) are ready for recon pipeline with no additional extraction steps
- Cat B genuine pairs (82) require sgngl extraction of the FINAL file before use
- Priority: stage highest-quality Cat A pairs by year coverage for lexical layer maturation