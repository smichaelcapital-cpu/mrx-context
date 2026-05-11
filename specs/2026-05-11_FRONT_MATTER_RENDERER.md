# SPEC — Front Matter Renderer (Consolidated)
Date: 2026-05-11
Author: Opus
Builder: Sonnet
Owner: Scott

---

## RULE SHEET HEADER

- **Universal?** YES — every CR has the same 5 front-matter blocks in the same order. MB-specific values (her boilerplate text, her cert language) live in profile data, not in renderer code.
- **Code or prompt?** CODE
- **File location:** `src/stage5/front_matter/` (new package) + `src/profiles/mb/data/front_matter/<depo_stem>/` (per-depo JSON)
- **Commit prefix:** `universal:`

---

## PRIME DIRECTIVE CHECK

Could this reduce transcript accuracy or credibility? Yes if done wrong — front matter is the first thing a judge or opposing counsel sees. Wrong witness name, wrong case caption, wrong cert date = transcript is unusable. Mitigation: every field that varies per case comes from JSON data, never hardcoded. Renderer is dumb — it lays out what the JSON says. JSON is reviewed by Scott (and eventually MB) before any depo ships.

---

## THE BIG IDEA — ONE SENTENCE

The renderer is universal. The data is per-CR per-depo. Adding a new CR means adding a profile folder, not changing code.

---

## THE 5 BLOCKS

| # | Block | Page count | Variability |
|---|---|---|---|
| 1 | Cover | 1 | Court, caption, witness, date/time/place, "Reported By" |
| 2 | Index | 1–3 | Exhibit count drives page count |
| 3 | Appearances | 1–6 | Already built — keep as-is |
| 4 | Stipulation | 1 | Reserve vs waive read/sign; who retains original |
| 5 | Reporter Cert | 2 | Witness name, page count, cert date |

Optional trailing blocks (not always present): Witness Cert, Errata Sheets. Spec'd here, generated only if present in JSON.

---

## DIRECTORY LAYOUT

```
src/stage5/front_matter/
    __init__.py
    cover.py
    index.py
    stipulation.py
    reporter_cert.py
    witness_cert.py            # optional block
    errata.py                  # optional block
    page_layout.py             # 25-line page assembler (already exists, may need extension)
    orchestrator.py            # composes all blocks in order, paginates

src/stage5/appearances_renderer.py     # ALREADY BUILT — leave it. Orchestrator calls it.

src/profiles/mb/data/front_matter/<depo_stem>/
    cover.json
    index.json
    stipulation.json
    reporter_cert.json
    witness_cert.json          # optional
    errata.json                # optional
    # appearances.json already lives at src/stage5/data/appearances/<depo_stem>.json — move it here in step 0
```

**Step 0 of the build:** move existing appearances JSONs from `src/stage5/data/appearances/` to `src/profiles/mb/data/front_matter/<depo_stem>/appearances.json`. Update one path in `document_composer.py`. This consolidates all MB data under one roof. Universal pattern from row 13 of the ledger.

---

## DATA MODEL — PER BLOCK

### cover.json

```json
{
  "court_header_lines": [
    "UNITED STATES DISTRICT COURT",
    "EASTERN DISTRICT OF LOUISIANA"
  ],
  "caption": {
    "left_block_lines": [
      "HERMAN WILLIAMS,",
      "     Plaintiff,",
      "  v.",
      "BP EXPLORATION &",
      "PRODUCTION",
      "INCORPORATED, BP",
      "AMERICA PRODUCTION",
      "COMPANY, BP P.L.C.",
      "     Defendants."
    ],
    "right_block_lines": [
      "CIVIL ACTION",
      "NO. 17-2675",
      "",
      "JUDGE AFRICK",
      "",
      "MAGISTRATE",
      "JUDGE NORTH"
    ],
    "trailing_lines": [
      "Related to: B3 PLEADING",
      "BUNDLE IN MDL NO. 2179"
    ]
  },
  "deposition_label": "VIDEOTAPED DEPOSITION",
  "witness_name": "CINDY WILLIAMS",
  "taken_on": "Wednesday, June 1, 2022",
  "commencing_at": "10:11 a.m.",
  "location_lines": [
    "at the",
    "offices of",
    "HERMAN, HERMAN & KATZ",
    "820 O'Keefe Avenue",
    "New Orleans, Louisiana"
  ],
  "reported_by": "MARYBETH E. MUIR, CCR, RPR"
}
```

**Field rules:**
- `court_header_lines` is a list. Olsen has 1 line (`"IN THE MATTER OF THE ARBITRATION BETWEEN:"`), USDC depos have 2. State depos have 3.
- `caption.left_block_lines` and `caption.right_block_lines` are verbatim. Renderer aligns them side-by-side. No parsing of party names.
- `caption.trailing_lines` is optional, for MDL/related-to text.
- `deposition_label` is `"VIDEOTAPED DEPOSITION"` or just `"DEPOSITION"` (Olsen).
- All other fields are simple strings — preserved verbatim.

---

### index.json

```json
{
  "navigational_entries": [
    {"label": "Caption", "page": 1},
    {"label": "Appearances", "page": 4},
    {"label": "Stipulation", "page": 6},
    {"label": "Examination", "page": null, "sub_entries": [
      {"label": "Mr. Leefe", "page": 8},
      {"label": "Mr. Gileson", "page": 198}
    ]},
    {"label": "Re Examination", "page": null, "sub_entries": [
      {"label": "Mr. Leefe", "page": 204}
    ]},
    {"label": "Reporter's Certificate", "page": 206},
    {"label": "Witness Certificate", "page": 208}
  ],
  "exhibits": [
    {"number": "1", "description_lines": ["U.S. Department of Treasury", "letter, 10/14/20"], "page": 51},
    {"number": "2", "description_lines": ["Internal Revenue Service", "letter, 5/9/14"], "page": 51}
  ]
}
```

**Field rules:**
- `navigational_entries` order is preserved verbatim. Sub-entries (examination by attorney) nest under parent.
- `exhibits[].description_lines` is a list — wraps long descriptions. Renderer prints each line, aligns page number right.
- `exhibits[].number` is a string (could be `"5A"` or `"11"` with `"NOT MARKED"` → handled in description).
- Exhibits paginate across pages with the header `E X H I B I T S` on continuation pages. First exhibit page uses the header pattern from the dump (Halprin page 2: `* * * * * * * *` divider, then `EXHIBITS`).

---

### stipulation.json

```json
{
  "witness_name_caps": "ROMOND MARCHE BLANKS",
  "witness_reserves_signature": false,
  "original_retained_by": "BRADY MCMILLIN, ESQ.",
  "filing_destination": "Clerk of Court",
  "proceeding_type": "Notice under the Louisiana Code of Federal Procedure"
}
```

**Field rules:**
- `witness_reserves_signature: true` → "reserves the right to read and sign". `false` → "waives the right to read and sign". Both observed.
- `proceeding_type`: usually the "Notice under the Louisiana Code..." line. Olsen uses "Notice under the arbitration rules applicable to this matter" — preserved verbatim.
- Rest of stipulation text is universal boilerplate — lives in renderer code, not JSON.

---

### reporter_cert.json

```json
{
  "witness_name_caps": "ROMOND MARCHE BLANKS",
  "page_count_of_testimony": 71,
  "cert_date_line": "This 14th day of October, 2022.",
  "reporter_signature_line": "MARYBETH E. MUIR, CCR, RPR"
}
```

**Field rules:**
- Cert boilerplate ("I, Marybeth E. Muir, Certified Court Reporter…") is universal — in renderer code with `{witness_name_caps}` and `{page_count_of_testimony}` as substitution points only.
- `reporter_signature_line` lives in MB profile defaults, can be overridden per-depo if needed.

---

### witness_cert.json (optional)

```json
{
  "witness_name_caps": "RICHARD HALPRIN",
  "errata_sheet_count": 4
}
```

Boilerplate lives in renderer. `errata_sheet_count` drives how many errata sheets follow (each is 1 page, ~8 numbered slots).

### errata.json (optional, derived from witness_cert)

No separate JSON. Renderer generates errata sheets from `witness_cert.errata_sheet_count` using a single boilerplate template.

---

## RENDERER CONTRACT

Each block module exports one function:

```python
def render(data: dict) -> list[LogicalLine]:
    ...
```

Where `LogicalLine` is the existing object from `page_layout.py` with `text: str` and `indent: int`.

The orchestrator at `src/stage5/front_matter/orchestrator.py` exports:

```python
def render_front_matter(profile: str, depo_stem: str) -> list[Page]:
    """
    Loads all JSON files for the given depo from src/profiles/<profile>/data/front_matter/<depo_stem>/,
    calls each block's render() in order, paginates into 25-line pages,
    returns list of Page objects.
    """
```

**Block order in orchestrator:**
1. cover
2. index
3. appearances (already-built renderer, called via existing module)
4. stipulation
5. reporter_cert (rendered at end, but stored separately — placed at back of book by document_composer)
6. witness_cert (optional, after reporter_cert)
7. errata (optional, after witness_cert)

---

## PAGINATION RULES (LOCKED)

- Every page is exactly 25 numbered content lines.
- Page numbers are right-justified in the page-number band above line 1 (existing page_layout behavior).
- **Atomic blocks:** cover (1 page), stipulation (1 page), reporter cert (2 pages) never split mid-block. If they don't fit, they push to the next page and the current page pads with blank lines.
- **Flowable blocks:** index, appearances, errata. These flow across pages with continuation headers (`E X H I B I T S`, `A P P E A R A N C E S:`).
- Last page of any block pads with blank lines to fill 25.

---

## ACCEPTANCE TESTS — SHAPE MATCH ONLY

For each of the 6 staged depos, write one test per block. The test asserts shape, not bytes:

1. Each block renders without error from its JSON.
2. Block produces the expected number of pages (within ±1 for flowable blocks).
3. Required content appears (witness name, case caption, date) — substring assertion, not byte equality.
4. Block boundaries align — no block bleeds into another's territory.
5. 25-line invariant holds on every page.

Test file: `tests/stage5/test_front_matter.py`.

**Explicit non-goal:** byte-matching any FINAL on disk. The FINALs are the shape reference, not the byte oracle.

---

## BUILD SEQUENCE — 6 STEPS

Each step ends with a test passing and a paste-to-Scott checkpoint. No step is bigger than 90 minutes.

**Step 0 — Move appearances data (10 min).** Move existing `src/stage5/data/appearances/halprin.json` and `williams.json` to the new profile path. Update one import in `document_composer.py`. Confirm existing stage5 tests still pass.

**Step 1 — Extract JSON for all 6 depos (60 min).** Read each FINAL in the dump file. Write the 5 (or 7) JSON files per depo into `src/profiles/mb/data/front_matter/<depo_stem>/`. No code yet. Just data.

**Step 2 — Cover renderer + tests (45 min).** Build `cover.py`. Test against all 6 `cover.json` files. Shape match.

**Step 3 — Stipulation renderer + tests (45 min).** Build `stipulation.py`. Test against all 6.

**Step 4 — Index renderer + tests (90 min).** Build `index.py`. Handle exhibit pagination. Test against all 6.

**Step 5 — Reporter cert + witness cert + errata renderers + tests (60 min).** Build all three. Test against the depos that have them.

**Step 6 — Orchestrator + integration test (45 min).** Build `orchestrator.py`. End-to-end test: render full front matter for all 6 depos, confirm shape, confirm 25-line invariant everywhere.

**Total Sonnet effort:** ~6 hours, broken into ~7 paste-and-wait checkpoints.

---

## SCOTT TOUCHPOINTS

1. Approve this spec (now)
2. Approve each step's output (paste from Sonnet, one-line yes/no)
3. Final eyeball of all 6 rendered front matters (~20 min, end of Step 6)

**Total Scott time:** ~30 min spread over the build.

---

## LEDGER ROWS TO ADD AFTER APPROVAL

- Row 16: Front-matter directory layout (`src/profiles/<reporter>/data/front_matter/<depo>/`)
- Row 17: Block atomicity rules (cover/stip/cert atomic; index/appearances/errata flowable)
- Row 18: Stipulation `proceeding_type` field (preserves arbitration vs deposition language verbatim)

---

## WHAT THIS SPEC DOES NOT COVER

- Auto-generation of JSON from raw RTF or `.sgxml`. Manual extraction for now. Auto-gen is a later tier.
- Per-case lexical fixes inside testimony. Front matter only.
- Second CR onboarding. Architecture supports it; actual second profile is its own spec.
- Halprin-specific byte quirks. Dead.

---

## SCOTT'S GATE

Approve this spec, then Sonnet runs Step 0.

— End spec —
