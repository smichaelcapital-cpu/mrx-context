# B1.7 INDEX + EXHIBITS AUDIT
**Date:** 2026-05-15
**Builder:** Sonnet #2 (Lane B, Tile B1.7)
**Branch:** NONE — recon only, no code changes
**Status:** COMPLETE — ready for Opus review

---

## Section 1 — Files Used Per Depo

### Oracle files (ground truth)

| Depo | Oracle path | Status |
|---|---|---|
| halprin | `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt` | FOUND |
| 060122williams | `C:\mrx_training_set\MB\paired\060122williams\final\060122williams-FINAL.txt` | FOUND |
| 082222butler | `C:\mrx_training_set\MB\paired\082222butler\final\082222butler-FINAL.txt` | FOUND |
| 032025olsen | `C:\mrx_training_set\MB\paired\032025olsen\final\032025olsen-FINAL.txt` | FOUND |
| 0525black_bp | `C:\mrx_training_set\MB\paired\0525black_bp\final\0525black-bp-FINAL.txt` | FOUND |
| 101322blanks | `C:\mrx_training_set\MB\paired\101322blanks\final\101322blanks-FINAL.txt` | FOUND |

All 6 oracle files found. No missing sources.

### JSON data files (all at `src/profiles/mb/data/front_matter/<depo>/`)

| Depo | appearances.json | index.json | witness_cert.json | Notes |
|---|---|---|---|---|
| halprin | YES | YES | YES | read-and-sign |
| 060122williams | YES | YES | YES | read-and-sign |
| 082222butler | YES | YES | NO | no read-and-sign |
| 032025olsen | YES | YES | NO | no read-and-sign |
| 0525black_bp | YES | YES | NO | no read-and-sign |
| 101322blanks | YES | YES | NO | no read-and-sign |

All 6 depos have `index.json`. Exhibit data lives inside `index.json` (no separate `exhibits.json`). No new data files are needed for a renderer — the data is already extracted.

### Source code files examined

| File | Path | Role |
|---|---|---|
| appearances_page.py | `src/stage5/appearances_page.py` | ACTIVE path — contains hardcoded `_PAGE_2/_PAGE_3/_PAGE_4` |
| index.py | `src/stage5/front_matter/index.py` | Data-driven renderer — NOT called from assemble_final.py |
| orchestrator.py | `src/stage5/front_matter/orchestrator.py` | build_front_matter() calls build_index_pages() — NOT called from assemble_final.py |

---

## Section 2 — Per-Depo Table

| Depo | Index on p.2? | Exhibit pages | Total index/exhibit pages | Appearances start page | Witness cert in index? | Exhibit count |
|---|---|---|---|---|---|---|
| halprin | YES | p.2 (partial) + p.3 + p.4 (partial) | 3 | 5 | YES (p.298) | 23 (Nos. 236-258) |
| 060122williams | YES | p.2 (partial) + p.3 (partial) | 2 | 4 | YES (p.208) | 22 (Nos. 1-22) |
| 082222butler | YES | p.2 (partial, fits) | 1 | 3 | NO | 4 (Nos. 1-4) |
| 032025olsen | YES | p.2 (partial) + p.3 (partial) | 2 | 4 | NO | 22 (Nos. 1-22) |
| 0525black_bp | YES | p.2 (partial) + p.3 + p.4 (partial) | 3 | 5 | NO | 27 (Nos. 1-27) |
| 101322blanks | YES | p.2 (partial, fits) | 1 | 3 | NO | 2 (Nos. 1-2) |

**Pattern confirmed:** `appearances_start_page = 2 + number_of_index_exhibit_pages`. This matches `appearances.json["start_page"]` for all 6 depos.

### Page 2 structure (universal)

Page 2 is always identical in shape across all 6 depos:

```
[blank lines]
                    [60-col right-aligned page number: 2]
[blank lines]

 1                        I N D E X
                                                    Page
 2  Caption                                           1
 3  Appearances                                      [N]
 4  Stipulation                                      [N]
 5  Examination
        [Examiner name]                              [N]
 6      [Re Examination if present]
 7  Reporter's Certificate                           [N]
 8  [Witness's/Witness Certificate                   [N]]   ← read-and-sign only
 9  [blank or next slot]
        * * * * * * * *

[next available slot]  EXHIBITS

[exhibit entries...]
```

The nav entry count is **5 for non-read-and-sign** (Caption, Appearances, Stipulation, Examination, Reporter's Certificate) and **6 for read-and-sign** (adds Witness Certificate).

Slot layout on page 2: nav section uses approximately lines 1-9, separator on line 9-10, then exhibits start at line 11 and continue down as far as they fit. Overflow goes to pages 3+.

### Exhibit overflow page structure

Each overflow page (page 3, 4, ...) has:
```
 1  [blank]
                        E X H I B I T S
 2  [exhibit entries continuing...]
...
25  [last exhibit or blank]
```

Last partial page has blank rows from the last exhibit to line 25.

---

## Section 3 — Variation Summary

### What is universal (same across all 6 depos)

- Index/TOC is always page 2
- Page 2 always contains: `I N D E X` header, nav entries, `* * *` separator, exhibit list start
- Navigation entry labels are consistent: Caption, Appearances, Stipulation, Examination, Reporter's Certificate
- Exhibit entries always have: number, multi-line description, page number
- `appearances_start_page = 2 + number_of_index/exhibit_pages`
- All exhibit and page-number data is already captured in `index.json` for all 6 depos

### What varies (depo-specific)

| Field | Range observed | Driven by |
|---|---|---|
| Appearances start page | 3, 4, or 5 | Exhibit count → number of exhibit overflow pages |
| Number of index/exhibit pages | 1, 2, or 3 | Exhibit count |
| Exhibit count | 2 to 27 | Case-specific |
| Exhibit number range | Sequential from 1, or continuing (e.g., 236-258) | Case-specific |
| Witness Certificate in nav | Present or absent | `stipulation.json["witness_reserves_signature"]` |
| Examination sub-entries | 1 to 3 examiners | Case-specific |
| Re Examination entries | Present or absent | Case-specific |

### Hard-coded vs data-driven today

`appearances_page.py` lines 73/75/77 contain `_PAGE_2`, `_PAGE_3`, `_PAGE_4` as complete Halprin-specific string literals baked in. These are returned as the first three pages by `build_appearances_pages()`. If any non-Halprin depo is run through the current pipeline, these three pages will print Halprin's exhibit list over the wrong depo.

`index.json` for all 6 depos already contains the correct data. `index.py` renderer already produces the correct output. The data-driven path exists but is not connected to `assemble_final.py`.

---

## Section 4 — Recommended Data Model for Index/Exhibits Renderer

*Sonnet #2 sketches; Opus reviews.*

### Current `index.json` schema (already in use for all 6 depos)

```json
{
  "navigational_entries": [
    {"label": "Caption",       "page": 1},
    {"label": "Appearances",   "page": 5},
    {"label": "Stipulation",   "page": 11},
    {"label": "Examination",   "page": null, "sub_entries": [
      {"label": "Mr. Caughey", "page": 13}
    ]},
    {"label": "Reporter's Certificate",  "page": 296},
    {"label": "Witness's Certificate",   "page": 298}   // read-and-sign only
  ],
  "exhibits": [
    {"number": "236", "description_lines": ["E-mail, 5/25/17", "YR-325674-677"], "page": 60},
    ...
  ]
}
```

This schema already captures everything needed. No new fields required for the 6 MB depos observed.

### Renderer — `build_index_pages()` in `index.py`

Already implemented and handles multi-page overflow. **No renderer changes needed for the data model.**

### One blocker in the existing renderer

`index.py:build_index_pages()` line 193:
```python
if len(nav) < 6:
    raise NotImplementedError(
        f"Expected ≥6 navigational entries, got {len(nav)}. ..."
    )
```

And lines 209/217/220 hardcode:
```python
exam = nav[3]   # Examination
rpt  = nav[4]   # Reporter's Certificate
wit  = nav[5]   # Witness's Certificate  ← fails if not present
```

**This will raise `NotImplementedError` for butler, olsen, black_bp, blanks** — all 4 non-read-and-sign depos have only 5 nav entries. The renderer was built and tested against Halprin (6 entries) and has not been exercised against the other depos.

Fix required before any of these 4 depos can run: relax the `len(nav) < 6` guard to `len(nav) < 5` and make `wit = nav[5]` conditional (only render the witness cert nav slot if a 6th entry is present).

### Wire-in path recommendation

Two options:

**Option A (minimal, recommended):** Wire `build_index_pages(index_data, 2)` into `assemble_final.py` to replace `_PAGE_2/_PAGE_3/_PAGE_4`. This is the same pattern as B1.6 (cert wire-in) and A1.5 (appearances wire-in). The `index.json` data files already exist for all 6 depos.

**Option B (fuller scope):** Wire `build_front_matter(depo_stem)` from `orchestrator.py` into `assemble_final.py` to replace all front matter (cover through stipulation). This is a larger change but eliminates all hardcoded pages in one pass.

Option A is lower risk and keeps the same incremental tile pattern.

---

## Section 5 — Open Questions for Scott + Opus

1. **Renderer guard fix scope:** The `len(nav) < 6` guard in `index.py` must be relaxed before non-read-and-sign depos can run. Is this fix in scope for the same tile as the wire-in, or a separate tile?

2. **Exam sub-entries:** The nav slot for "Examination" has sub-entries (examiner names with page numbers). The current renderer handles them for halprin. Williams has 3 examination sub-entries (Mr. Leefe, Mr. Gisleson, Re Examination by Mr. Leefe). Does the renderer handle the Re Examination label? Not verified — worth testing before wiring in.

3. **Exhibit number format:** Halprin exhibits start at 236 (not 1). The renderer uses `number` verbatim from JSON, so this should work, but has not been verified for the non-starting-at-1 case.

4. **`appearances_page.py` status after A1.5:** After A1.5 wires in `appearances_renderer.py`, does `appearances_page.py` become dead code entirely, or does `assemble_final.py` still call it for pages 2-4? If pages 2-4 are still coming from `appearances_page.py`, this tile (index wire-in) should replace that call. If `appearances_page.py` is already fully deprecated by A1.5, confirm what is currently producing pages 2-4.

5. **No `witness_cert.json` for non-read-and-sign depos:** `build_back_matter()` in `orchestrator.py` calls `_load(depo_stem, "witness_cert.json")` unconditionally (before checking `read_and_sign`). This was flagged in the B1.6 prep read. Must be fixed before running any non-read-and-sign depo through `build_back_matter()`.

---

*Generated by Sonnet #2, 2026-05-15. No engine commits. Recon only.*
*Scott reviews → Scott pushes to repo.*
