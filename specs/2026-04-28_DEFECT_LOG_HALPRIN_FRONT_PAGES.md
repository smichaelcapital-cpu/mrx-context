# Defect Log — Halprin Front Pages — 2026-04-28

*Placeholder header — Opus to populate defect entries.*

---

## Dictionary Thread — Package Inspection Findings (2026-04-28)

- **Dictionary files in package:**
  - `040226yellowrock-ROUGH.rtf` (5,289 bytes) — CRE/RTF, readable NOW
  - `040226yellowrock-ROUGH.sgdct` (6,660 bytes) — SGCAT32 binary, not readable
  - `040226yellowrock-ROUGH.sgdcx` (7,344 bytes) — SGCAT32 binary, not readable
  - `040226yellowrock-ROUGH.sgdcg` (0 bytes) — empty
  - `040226yellowrock-ROUGH.sgglb` (28,450 bytes) — SGCAT32 binary conflict table, not readable
  - `040226yellowrock-ROUGH.tlx` (232 bytes) — plain text word list, 22 proper nouns, readable
  - `040226yellowrock-ROUGH.sgstn` (417,144 bytes) — SGCAT32 steno data, fully binary, unreadable

- **Readable directly by dictionary_loader.py:** `040226yellowrock-ROUGH.rtf` only — YES, immediately.

- **Conversion needed:** NO — .rtf is byte-for-byte identical to `tests/fixtures/halprin_mini/dictionary.rtf`. The fixture we already have IS the package dictionary.

- **Existing dictionary_loader.py compatibility:** FULLY COMPATIBLE. Already tested against this exact file. 116 unique translations, 3 speaker labels. No work needed.

- **Files copied to engine working folder:**
  `io/analysis/halprin_mini/package/` — 10 files copied (all non-.opus, non-.sgxr2, non-FINAL files). FINAL files not touched per Oracle Covenant.

- **W&T / underpaid / stipulated in any package file:** NONE. These are not in the job-specific dictionary. Likely in MB's system dictionaries (not available to us).

- **Recommended next step:** Verify that `_run_halprin_mini.py` passes the dictionary to Stage 3 at runtime (quick read, one task). Then investigate B2 (under paid introduced by pipeline) and 0428-5 (stipulation block dropped by Stage 1) as the two highest-priority pipeline bugs. B5 (W&T) and B1 (dashes) require either system dictionary access or post-processing rules and should be deprioritized.
