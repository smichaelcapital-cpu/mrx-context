# Oracle — Truth Source Files

These files are MB Muir's polished deposition deliverables. They serve as truth
source for testing and comparison ONLY.

## Oracle Covenant

- READ ONLY at all times
- NEVER read by pipeline code at runtime
- NEVER copied into code as hardcoded values
- NEVER modified
- Used only by tests and comparison/recon scripts

## Structure

- `finals/{depo_name}/` — original FINAL files (one folder per depo)
- `frontmatter/{depo_name}_frontmatter.txt` — extracted front-matter only
  (lines 1 through line before first occurrence of "EXAMINATION" / "BY MR." /
  first "Q." — whichever comes first)

## Current contents

| Depo | Date | Folder | Status |
|------|------|--------|--------|
| Halprin (Yellow Rock) | 2026-04-02 | finals/halprin/ | Consolidated 2026-04-28 |

## Maintenance

Add new MB FINALs by creating `finals/{depo_name}/` subfolder and copying the
FINAL .txt and .sgxml files in. Re-run the front-matter extraction to populate
`frontmatter/`. Large binary files (.sgngl, .rtf, .opus) should NOT be
committed to git — copy locally but add to .gitignore.

## Note on MASTER_COPIES/ORACLES

A prior oracle structure exists at:
`C:\Users\scott\OneDrive\Documents\MASTER_COPIES\ORACLES\`

That folder contains the Brandl (032626) oracle (BRANDL_MB_FINAL.txt + full
deliverable package). It has its own README (ORACLES_README.md). Once Scott
approves, the Brandl oracle should be cross-referenced or migrated here.
