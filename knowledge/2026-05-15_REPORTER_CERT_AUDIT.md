# B1.5 REPORTER CERTIFICATE AUDIT — Halprin
**Date:** 2026-05-15
**Builder:** Sonnet #2 (Lane B, Tile B1.5)
**Branch:** NONE — recon only, no code changes
**Status:** COMPLETE — ready for Opus review

---

## Section 1 — Files Found

### Renderer files

| File | Full Path | Size |
|---|---|---|
| reporter_cert.py | `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\front_matter\reporter_cert.py` | 7.2 KB |
| witness_cert.py | `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\front_matter\witness_cert.py` | 4.6 KB |
| orchestrator.py | `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\front_matter\orchestrator.py` | 5.0 KB |

### JSON data files (Halprin)

| File | Full Path | Size |
|---|---|---|
| reporter_cert.json | `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\profiles\mb\data\front_matter\halprin\reporter_cert.json` | 191 B |
| witness_cert.json | `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\profiles\mb\data\front_matter\halprin\witness_cert.json` | 136 B |

### JSON data files — other depos (confirms multi-depo pattern)

reporter_cert.json also exists for: `060122williams`, `101322blanks`, `082222butler`, `0525black_bp`, `032025olsen`
witness_cert.json also exists for: `060122williams`

### Where cert is called from `assemble_final.py`

**Nowhere.** `assemble_final.py` has zero imports of any cert renderer and zero calls to `build_back_matter`. Confirmed by grep: no hits for `cert`, `reporter_cert`, `witness_cert`, `build_back_matter`, or `orchestrator` in `assemble_final.py`.

`build_back_matter` and `build_front_matter` are defined only in `orchestrator.py` and called from **no other file in the engine**.

---

## Section 2 — Per-File Code Summary

### reporter_cert.py

Data-driven. Reads 4 fields from `reporter_cert.json`: `witness_name_caps`, `page_count_of_testimony`, `cert_date_line`, `reporter_signature_line`. All Louisiana-standard boilerplate is stored as Python constants in the file (`_PAGE1_MAIN`, `_PAGE2_MAIN`). Entry function: `build_reporter_cert_page(data: dict, page_num: int) -> str`. Returns two form-feed-terminated pages concatenated. The `{witness}` and `{pages}` placeholders in `_PAGE1_MAIN` are filled at render time. Raises `NotImplementedError` for page counts > 999.

**FLAG — MB name hardcoded in boilerplate:** Lines 7-8 of `_PAGE1_MAIN` read:
```
"          I, Marybeth E. Muir, Certified Court",
"  Reporter in and for the State of Louisiana, and",
```
This is inside the Louisiana-standard boilerplate text, not in the JSON data. When a second CR is onboarded, `reporter_name_prose` (or equivalent) must be parameterized. Not blocking for Halprin/MB.

### witness_cert.py

Data-driven. Reads 2 fields from `witness_cert.json`: `witness_name_caps`, `depo_date_prose`. Boilerplate is all Python constants. Entry function: `build_witness_cert_page(data: dict, page_num: int) -> str`. Returns one form-feed-terminated page. Year is extracted from the last word of `depo_date_prose` (e.g., `"April 2, 2026"` → `"2026"`). Raises `NotImplementedError` if required keys are missing — intentional fail-loud guard.

**FLAG — MB name hardcoded as module constant:**
```python
_REPORTER_LINE = "  Reported by:  Marybeth E. Muir, CCR, RPR"
```
Module docstring explicitly notes "Reporter name is fixed to Marybeth E. Muir, CCR, RPR (profile constant)." Not data-driven. Will require a change for CR #2.

### orchestrator.py

Provides two public functions:
- `build_front_matter(depo_stem: str) -> str` — assembles cover, index, appearances, stipulation
- `build_back_matter(depo_stem: str) -> str` — assembles reporter cert, and optionally witness cert + errata (if `stipulation.json` has `witness_reserves_signature: true`)

Both functions load JSON via `_load(depo_stem, filename)` from `profiles/mb/data/front_matter/{depo_stem}/`. Both are complete and appear correct. Neither is called from anywhere else in the engine. The orchestrator was built but never wired in.

---

## Section 3 — MB Cert Text Verbatim from Oracle

Oracle file: `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt`

**Page 296 — Reporter Certificate (page 1 of 2):**
```
                                                         296


     1                  C E R T I F I C A T E

     2

     3          Certification is valid only for a transcript

     4   accompanied by my original signature and

     5  Original required seal on this page.

     6

     7          I, Marybeth E. Muir, Certified Court

     8  Reporter in and for the State of Louisiana, and

     9  Registered Professional Reporter, as the officer

    10  before whom this testimony was taken, do hereby

    11  certify that RICHARD HALPRIN, after having been duly

    12  sworn by me upon authority of R.S. 37:2554, did

    13  testify as hereinbefore set forth in the foregoing

    14  295 pages; that this testimony was reported by me in

    15  the stenotype reporting method, was prepared and

    16  transcribed by me or under my personal direction and

    17  supervision, and is a true and correct transcript to

    18  the best of my ability and understanding; that the

    19  transcript has been prepared in compliance with

    20  transcript format guidelines required by statute or

    21  by rules of the board, and that I am informed about

    22  the complete arrangement, financial or otherwise,

    23  with the person or entity making arrangements for

    24  deposition services; that I have acted in compliance

    25  with the prohibition on contractual relationships,
```

**Page 297 — Reporter Certificate (page 2 of 2):**
```
                                                         297


     1  as defined by Louisiana Code of Civil Procedure

     2  Article 1434 and in rules and advisory opinions of

     3  the board; that I have no actual knowledge of any

     4  prohibited employment or contractual relationship,

     5  direct or indirect, between a court reporting firm

     6  and any party litigant in this matter nor is there

     7  any such relationship between myself and a party

     8  litigant in this matter.  I am not related to

     9  counsel or to the parties herein, nor am I otherwise

    10  interested in the outcome of this matter.

    11

    12          This 14th day of April, 2026.
    13-16      [blank]

    17                      _________________________
                            MARYBETH E. MUIR, CCR, RPR
    18-25      [blank]
```

**Page 298 — Witness Certificate:**
```
                                                         298


     1                  C E R T I F I C A T E

     2

     3      I, RICHARD HALPRIN, do hereby certify that I

     4  have read or have had read to me the foregoing

     5  transcript of my testimony given on April 2, 2026,

     6  and find same to be true and correct to the best of

     7  my ability and understanding with the exceptions

     8  noted on the amendment sheet;

     9

    10  CHECK ONE BOX BELOW:

    11  ( ) Without Correction.

    12  ( ) With corrections, deletions, and/or

    13      additions as reflected on the errata

    14      sheet attached hereto.

    15

    16                 Dated this ___ day of ___________,

    17              2026.

    18

    19     [sig underline]
    20          RICHARD HALPRIN

    21-24      [blank]

    25  Reported by:  Marybeth E. Muir, CCR, RPR
```

**Pages 299-300 — Errata sheets** (2 pages, standard form).

---

## Section 4 — Component Breakdown

### Reporter Certificate (pages 296-297)

| Text | Type | In JSON? |
|---|---|---|
| `RICHARD HALPRIN` (line 11) | Case-specific | YES — `witness_name_caps` |
| `295 pages` (line 14) | Case-specific | YES — `page_count_of_testimony` |
| `This 14th day of April, 2026.` (p.297 slot 12) | Case-specific | YES — `cert_date_line` |
| `MARYBETH E. MUIR, CCR, RPR` (p.297 slot 17 sub) | CR-specific | YES — `reporter_signature_line` |
| `I, Marybeth E. Muir, Certified Court` (line 7) | CR-specific | **NO — hardcoded in _PAGE1_MAIN** |
| `Reporter in and for the State of Louisiana` (line 8) | CR-specific | **NO — hardcoded in _PAGE1_MAIN** |
| All remaining boilerplate (lines 3-6, 9-13, 15-25, p.297 1-10) | Universal | N/A — Louisiana statute language |

### Witness Certificate (page 298)

| Text | Type | In JSON? |
|---|---|---|
| `RICHARD HALPRIN` (lines 3, 20) | Case-specific | YES — `witness_name_caps` |
| `April 2, 2026` (line 5) | Case-specific | YES — `depo_date_prose` |
| `2026` (line 17) | Case-specific | Derived from `depo_date_prose` |
| `Reported by: Marybeth E. Muir, CCR, RPR` (line 25) | CR-specific | **NO — hardcoded as `_REPORTER_LINE`** |
| All remaining boilerplate | Universal | N/A |

---

## Section 5 — Verdict

**VERDICT: C — modified.**

The cert renderer exists and is fully data-driven, but it is NOT wired into `assemble_final.py`. The cert pages (296-300) currently appear in the Halprin output because they flow through the body paginator — the steno source text includes the cert content, and `lay_out_pages()` renders it as part of the body starting at page 13.

This is exactly the same state appearances was in before A1.5: a complete, data-driven renderer sitting in `front_matter/` that `assemble_final.py` doesn't know about. The body passthrough currently produces correct-looking output for Halprin, but:
1. It will not produce correct output for a depo where the steno cert text differs from MB's cert format
2. It is not using the controlled renderer — the output depends on whatever comes through the steno body

The orchestrator's `build_back_matter(depo_stem)` is the right entry point. It is complete, tested against the Halprin data shape, and handles the read-and-sign conditional. It just needs to be called.

---

## Section 6 — Recommended Next Step

**Wire `build_back_matter()` into `assemble_final.py`.** Same pattern as A1.5 (appearances wire-in).

Scope of the wiring change:
1. Import `build_back_matter` from `front_matter.orchestrator` in `assemble_final.py`
2. After `body_paginated` is assembled, detect where the cert pages begin (likely via a `REPORTER_CERT` `LineKind` marker or a page count from `index.json`)
3. Strip cert/errata lines from `body_doc` before layout
4. Append `build_back_matter(depo_stem)` after the paginated body

**Two flags to resolve before or during the wire-in:**

| Flag | Location | Impact |
|---|---|---|
| MB's prose name hardcoded in `_PAGE1_MAIN` lines 7-8 | `reporter_cert.py` | Breaks for CR #2. Add `reporter_name_prose` field to JSON. |
| `_REPORTER_LINE` hardcoded in `witness_cert.py` | `witness_cert.py` | Breaks for CR #2. Move to JSON or profile constant. |

Both flags are non-blocking for Halprin/MB demo. Recommend flagging in a TODO comment now, fixing when CR #2 is onboarded.

**No new JSON data files needed.** `halprin/reporter_cert.json` and `halprin/witness_cert.json` both exist and match the oracle.

---

*Generated by Sonnet #2, 2026-05-15. No engine commits. Recon only.*
*Scott reviews → Scott pushes to repo.*
