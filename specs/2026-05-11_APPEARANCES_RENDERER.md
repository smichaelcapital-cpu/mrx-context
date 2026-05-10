# SPEC — Appearances Block Renderer

**Date:** 2026-05-11
**Author:** Opus (architect)
**Builder:** Sonnet
**Owner:** Scott

---

## RULE SHEET HEADER

- **Universal? YES** — every CR's appearances block has the same shape (firm groups + ALSO PRESENT + reporter). MB-specific values (her reporter block text) live in CR house-style data, not in this renderer.
- **Code or prompt? CODE**
- **File location:** `src/stage5/document_composer.py` (replace `_build_appearances()`) + `src/stage5/data/appearances/halprin.json` + `src/stage5/data/appearances/williams.json` + new `src/stage5/appearances_renderer.py`
- **Commit prefix:** `universal:`

---

## PRIME DIRECTIVE CHECK

**Could this change reduce transcript accuracy or credibility?**

Yes — if the renderer drops or reorders attorneys, misattributes firms, or corrupts contact info, MB's appearances page is wrong and the depo is unusable. **Mitigation:** byte-match acceptance test against two oracle finals (Halprin + Williams). Renderer ships only if both byte-match.

---

## GOAL

Replace the Halprin-only hardcoded `_build_appearances()` with a data-driven block renderer that handles the variation observed across 6 MB depos in the 2026-05-11 recon.

Acceptance: Halprin OUR_FINAL still byte-matches its oracle, AND Williams OUR_FINAL byte-matches its oracle.

---

## DATA MODEL

Each depo's appearances data lives in one JSON file at `src/stage5/data/appearances/<depo_stem>.json`.

```json
{
  "start_page": 5,
  "firm_groups": [
    {
      "role_label": "ATTORNEY FOR PLAINTIFF:",
      "party_name_continuation": null,
      "firm_name_lines": ["SHER GARNER CAHILL RICHTER KLEIN &", "HILBERT, L.L.C."],
      "address_lines": ["909 Poydras Street", "Suite 2800", "New Orleans, Louisiana 70112"],
      "phone": "504.299.2100",
      "emails": ["tmadigan@shergarner.com", "jgarner@shergarner.com"],
      "appearance": {
        "kind": "present",
        "attorneys": [
          {"name": "THOMAS J. MADIGAN, ESQ.", "annotation": null},
          {"name": "MELISSA ROME HARRIS, ESQ.", "annotation": "(Zoom)", "annotation_on_new_line": true},
          {"name": "LESLIE PARTIDA DEPAZ,", "annotation": null, "credential_continuation": "Paralegal"}
        ]
      }
    },
    {
      "role_label": "FOR THE DEFENDANTS, WESTLAKE US 2 LLC, WESTLAKE",
      "party_name_continuation": ["CORPORATION AND WESTLAKE CHLOR-VINYLS CORPORATION:"],
      "firm_name_lines": ["SUSMAN GODFREY LLP"],
      "address_lines": ["1000 Louisiana Street", "Suite 5100", "Houston, Texas 77002-5096"],
      "phone": "713.651.9366",
      "emails": ["rcaughey@susmangodfrey.com"],
      "appearance": {
        "kind": "present",
        "attorneys": [{"name": "RYAN CAUGHEY, ESQ.", "annotation": null}]
      }
    },
    {
      "role_label": "FOR THE DEFENDANT, NATIONAL CASUALTY COMPANY:",
      "firm_name_lines": ["PHELPS DUNBAR"],
      "address_lines": ["365 Canal Street", "Suite 2000", "New Orleans, Louisiana 70130-6534"],
      "phone": "504.679.5686",
      "emails": [],
      "appearance": {"kind": "not_present"}
    }
  ],
  "also_present": {
    "kind": "header_block",
    "entries": [
      {"name": "Darren Guastella", "role": "Videographer"}
    ]
  },
  "reporter_block_lines": [
    "Reported by:  Marybeth E. Muir,",
    "              Certified Court Reporter",
    "              In and for the State of",
    "              Louisiana and Registered",
    "              Professional Reporter"
  ]
}
```

### Field rules

- **`role_label`** is an opaque string. Renderer never parses it.
- **`party_name_continuation`** is an optional list of strings for cases where the role label wraps (Halprin Lonquist case).
- **`firm_name_lines`** is always a list (handles multi-line firm names like Sher Garner).
- **`emails`** is always a list. May be empty.
- **`appearance.kind`** is one of: `"present"`, `"not_present"`.
- **`appearance.attorneys[].annotation`** holds the Zoom marker verbatim. Renderer prints it as-is.
- **`appearance.attorneys[].annotation_on_new_line`** optional bool. If true, annotation prints on its own line at indent 32 (Halprin page 5 line 9 pattern).
- **`appearance.attorneys[].credential_continuation`** optional string. If present, prints on next line at indent 32.
- **`also_present.kind`** is one of:
  - `"header_block"` — emit `ALSO PRESENT:` header, then entries indented.
  - `"inline_label"` — emit `VIDEOGRAPHER: <name>` as a single labeled line, no header.
  - `"none"` — no also-present block.
- **`also_present.entries[]`** for `header_block` mode: list of `{name, role}` where role may be a string or `null`.
- **`reporter_block_lines`** is a verbatim list of strings. Indent 0, emit as-is.

---

## RENDERING ALGORITHM

### Page structure

Each appearances page has 25 numbered content lines (1–25). This renderer produces a stream of `LogicalLine` objects with line content + indent. The existing `page_layout` module assembles them into pages.

### Pagination rule (LOCKED)

**Firm groups are atomic.** A firm group renders as a single contiguous block. If the remaining lines on the current page cannot fit the entire next firm group, push the firm group to the next page and pad the current page with blank lines through line 25.

**ALSO PRESENT + reporter block is also atomic.** Renders as a single trailing unit. If it doesn't fit on the last firm-group page, push to an overflow page.

### Per-page header

Every appearances page emits `A P P E A R A N C E S:` at line 1, blank at line 2, content beginning line 3.

### Firm group rendering

For each firm group, emit in this order:

1. **Role label line(s):** `role_label` + any `party_name_continuation` strings. Indent: 0.
2. **Firm name lines:** indent 4. One LogicalLine per entry in `firm_name_lines`.
3. **Address lines:** indent 4. One per entry.
4. **Phone line:** indent 4. Skip if null/empty.
5. **Email lines:** indent 4. One per entry. Skip if list empty.
6. **Appearance line(s):**
   - If `not_present`: emit `NOT PRESENT` at indent 4.
   - If `present`:
     - First attorney: `BY: <name>` at indent 4. Annotation, if present and `annotation_on_new_line` is not true, follows the name with a single space.
     - Subsequent attorneys: indent 8, name only (no BY:).
     - If attorney has `credential_continuation`: emit on new line at indent 32.
     - If attorney has `annotation_on_new_line: true`: emit annotation on new line at indent 32.
7. **Blank line** after the firm group.

### ALSO PRESENT rendering

- **`header_block` mode:**
  - `ALSO PRESENT:` at indent 0.
  - For each entry: `<NAME>, <role>` at indent 4 if role non-null; `<name>` at indent 4 if role null.
- **`inline_label` mode:** `VIDEOGRAPHER: <name>` at indent 0.
- **`none` mode:** emit nothing.

### Reporter block rendering

- Blank line, then emit each `reporter_block_lines` string at indent 0. Strings come pre-aligned — emit verbatim.

### Last-page padding

After the final content line, emit blank line numbers until line 25.

---

## TWO DATA FILES TO CREATE

### 1. `src/stage5/data/appearances/halprin.json`

Extract from `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt` pages 5–10. Use the recon at `C:\Users\scott\OneDrive\Documents\mrx-context\reports\2026-05-11\appearances_recon.md` as the verbatim source.

Halprin structural cases:
- Multi-line firm name (Sher Garner)
- Multi-line role label / verbose party name (Westlake)
- Role label that wraps mid-party-name (Lonquist page 6 lines 2–3)
- `(Zoom)` as hanging annotation on its own line (page 5 line 9)
- `Paralegal` as credential_continuation (page 5 line 10)
- Same firm appearing twice for different defendants (Phelps Dunbar, Lugenbuhl)
- 6 NOT PRESENT entries
- Double `@@` in email (page 6 line 11) — preserve verbatim

### 2. `src/stage5/data/appearances/williams.json`

Extract from `C:\mrx_training_set\MB\paired\060122williams\final\060122williams-FINAL.txt` page 4.

Williams structural cases:
- 4 firm groups (2 present, 2 NOT PRESENT)
- `Attorney for PLAINTIFF:` role label format (mixed case)
- Attorney without ESQ. credential ("Jessica Quin")
- `REED SMITH,LLP` — preserve verbatim
- Overflow page 5 with `ALSO PRESENT:` header + reporter block + 19 blank lines

---

## EDGE CASES — EXPLICIT BEHAVIOR

| Edge case | Behavior |
|---|---|
| Empty `emails` list | Skip email lines entirely |
| `phone` is null | Skip phone line |
| `attorney.name` ends with comma | Preserve verbatim |
| Annotation case variations `(Via Zoom)` / `(via Zoom)` / `(Zoom)` | Preserve verbatim |
| Multi-email firm (Halprin Sher Garner has 4) | Emit all, one per line |
| Non-attorney in ALSO PRESENT (Wunstell pattern) | Emit at indent 4, name only, no role |
| Page-2 sparse layout (BP MDL pattern) | Emit ALSO PRESENT + reporter + pad to line 25 |
| Firm group won't fit on current page | Force push to next page. Never split. |

---

## ACCEPTANCE CRITERIA

1. **Byte-match Halprin oracle** at `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt` for pages 5–10. Test: `tests/stage5/test_appearances_renderer.py::test_halprin_byte_match`.

2. **Byte-match Williams oracle** at `C:\mrx_training_set\MB\paired\060122williams\final\060122williams-FINAL.txt` for pages 4–5. Test: `tests/stage5/test_appearances_renderer.py::test_williams_byte_match`.

3. **All existing stage5 tests still pass** (192 tests as of edeb8d8). No regressions.

4. **JSON schema validation:** create `tests/stage5/test_appearances_data.py::test_schema` that validates both JSON files against the data model.

5. **Pagination invariant test:** synthetic 12-firm appearance, assert no firm group split across page boundary.

---

## FILES CHANGED

**New:**
- `src/stage5/data/appearances/halprin.json`
- `src/stage5/data/appearances/williams.json`
- `src/stage5/appearances_renderer.py`
- `tests/stage5/test_appearances_renderer.py`
- `tests/stage5/test_appearances_data.py`

**Modified:**
- `src/stage5/document_composer.py` — `_build_appearances()` now loads JSON and delegates to `appearances_renderer.render()`. Old hardcoded Halprin literal goes away.
- `src/stage5/assemble_final.py` — pass appearances data file path through case_info (mirror the cover/stipulation pattern from edeb8d8).

---

## WHAT THIS SPEC DOES NOT COVER

- Auto-generation of the JSON files from raw RTF or `.sgxml`. JSON is hand-extracted from the oracle for this build. Auto-gen is Tier 3.
- Per-case lexical layer.
- Generalization to a third or fourth depo (Olsen inline VIDEOGRAPHER, Wunstell non-attorney in ALSO PRESENT) — Tier 3 follow-up after this ships.

---

## BUILD SEQUENCE (FOR SONNET)

1. Create both JSON data files first. Manual extraction. No code yet.
2. Write `test_halprin_byte_match` and `test_williams_byte_match` AGAINST THE EXISTING ENGINE first — confirm they fail with current `_build_appearances()` on Williams (expected) and pass on Halprin (regression baseline).
3. Build `appearances_renderer.py` module. Single function: `render(appearances_data: dict) -> list[LogicalLine]`.
4. Wire it into `_build_appearances()` — load JSON by depo stem, call renderer.
5. Iterate against byte-match tests until both pass.
6. Run full stage5 test suite. Confirm 192+ passing.

---

## ESTIMATED EFFORT

- JSON extraction: ~45 min
- Renderer module: ~90 min
- Tests: ~60 min
- Byte-match iteration: ~30–60 min

**Total:** ~4 hours Sonnet.

---

## SCOTT'S GATE

This is a HARD GATE. Spec must be approved before Sonnet starts.

— End spec —
