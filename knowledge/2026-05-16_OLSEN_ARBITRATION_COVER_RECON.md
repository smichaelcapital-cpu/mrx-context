# B1.7.4 Recon Capture — Olsen Arbitration Cover Layout

**Date:** 2026-05-16
**Author:** Sonnet #1 (Lane B)
**Spec:** `specs/2026-05-16_B1.7.4_RECON_ARBITRATION_COVER.md`
**Status:** READ-ONLY. No engine code changed.

---

## Section 1 — Branch Verification

**mrx-context:**
```
git branch --show-current → feature/b1.7.4-recon
git log origin/main..HEAD --oneline → (empty)
```
Branch cut from origin/main after `git fetch`. Clean.

**mrx_engine_v1:**
```
git branch --show-current → feature/b1.7.4-recon
git log origin/main..HEAD --oneline → (empty)
```
Branch cut from origin/main after `git fetch`. Clean.

---

## Section 2 — Olsen Oracle Pages 1 and 4 (Cover + Appearances)

**NOTE:** Spec assumed pages 1-2 = cover + appearances. In Olsen's oracle, page 2 is the INDEX (continues to page 3). Appearances is on **page 4**. Capturing page 1 (cover) + page 4 (appearances) per the intent of the spec. PII redacted per Rule 16 guidance — names replaced with role placeholders. Structure preserved verbatim.

### Page 1 — Cover (redacted)

```
                                                           1


     1  IN THE MATTER OF THE ARBITRATION BETWEEN:

     2   * * * * * * * * * * * * * * * * * * * * * * * *
         [CLAIMANT_ENTITY_1],              JAMS REF NO.
     3   [CLAIMANT_ENTITY_2]              [JAMS_REF_NUM]
         [CLAIMANT_ENTITY_3]
     4   [CLAIMANT_ENTITY_3_CONT],
         [CLAIMANT_ENTITY_4]
     5   [CLAIMANT_ENTITY_4_CONT],
         [CLAIMANT_ENTITY_4_CONT2],
     6          Claimants,
         v.
     7   [RESPONDENT_LIST — approximately 7 left-block lines,
         spread over slots 7-11, following same caption_main/sub
     8   pair pattern as claimants above]
     9   ...
    10   ...
    11   [last respondent line],
                   Respondents.
    12

    13

    14
           * * * * * * * * * * * * * * * * * * * * * * * *
    15

    16                       DEPOSITION
                                 OF
    17                     [WITNESS]

    18                [Day], [Month DD], [YYYY]
                       commencing at [H:MM a.m.]
    19                           at
                            the offices
    20                           of
              [LAW_FIRM_LOCATION]
    21              [STREET_ADDRESS]
                    [CITY_STATE_ZIP]
    22
              Reported By:  [REPORTER]
    23
           * * * * * * * * * * * * * * * * * * * * * * * *
    24

    25
```

**Oracle artifact noted:** The raw file has a backtick character before "IN" on line 1 of the oracle: `` `IN THE MATTER OF THE ARBITRATION BETWEEN:``. Possible file-format artifact. Open question — see Section 10.

### Page 4 — Appearances (redacted)

```
                                                           4


     1  A P P E A R A N C E S:

     2  Attorney for [ROLE_A]:
           [FIRM_A]
     3     [FIRM_A_STREET]
           [FIRM_A_CITY_STATE_ZIP]
     4     [FIRM_A_PHONE]
           [FIRM_A_EMAIL_1]
     5     [FIRM_A_EMAIL_2]
            BY: [ATTY_A1], ESQ.
     6          [ATTY_A2], ESQ. (Via Zoom)

     7
        Attorney for [ROLE_B]:
     8     [FIRM_B]
           [FIRM_B_CONT]
     9     [FIRM_B_ADDR_1]
           [FIRM_B_ADDR_2]
    10     [FIRM_B_ADDR_3]
           [FIRM_B_CITY_STATE_ZIP]
    11     [FIRM_B_PHONE]
           [FIRM_B_EMAIL_1]
    12     [FIRM_B_EMAIL_2]
            BY:  [ATTY_B1], ESQ.
    13           [ATTY_B2], ESQ.

    14

    15
        VIDEOGRAPHER: [VIDEOGRAPHER_NAME]
    16

    17

    18  Reported by:  [REPORTER_FIRST_LAST],
                      Certified Court Reporter
    19              In and for the State of
                      [STATE] and Registered
    20              Professional Reporter

    21

    22

    23

    24

    25
```

**Appearances structure summary:**
- 2 firm groups (Claimants counsel + Respondents counsel)
- 1 ALSO PRESENT entry, `kind=inline_label` (VIDEOGRAPHER: [name])
- Reporter block at line 18 (main), continues through lines 19-20 (sub rows)
- Page has substantial blank space slots 21-25

---

## Section 3 — Current Cover Renderer Code

**File:** `src/stage5/front_matter/cover.py`

### `_DEPO_START_IDX` lookup table (line 31):
```python
_DEPO_START_IDX = {2: 12, 3: 10}
```
- Key: number of `court_header_lines`
- Value: 0-based slot index where the deposition block begins
- Count=1 is NOT in this dict → crash point (below)

### Where count=1 raises NotImplementedError (lines 133-135):
```python
depo_start_idx = _DEPO_START_IDX.get(num_headers)
if depo_start_idx is None:
    raise NotImplementedError(f"Unsupported court_header_lines count: {num_headers}")
```
Olsen has `num_headers=1` → `_DEPO_START_IDX.get(1) = None` → crash here before any layout work begins.

### 3-header code path (state court — Halprin-style, lines 202-213):
```python
if not label_in_main and loc_len == 4:
    # depo_start_idx=10, label_in_main=False, 4-item location
    slots.append(("", _c(depo_label, 67)))
    slots.append((_c("OF", 57), _c(witness, 67)))
    slots.append(("", " " * 30 + "taken on"))
    slots.append((_c(taken_on, 57), ""))
    slots.append((_c(commencing_str, 55), ""))
    slots.append((_c(location_lines[0], 55), _c(location_lines[1], 69)))
    slots.append((_c(location_lines[2], 57), _c(location_lines[3], 69)))
    slots.append(("", _c(reporter_str, 69)))
    slots.append(("", _STAR_SUB))
    # 9 depo slots: 0-indexed 10-18 → 1-indexed slots 11-19
```

### 2-header code paths (federal — Williams/Blanks-style, lines 215-239):
```python
elif label_in_main and loc_len == 5:
    # depo_start_idx=12, Williams-style, 5-loc
    slots.append((_c(depo_label, 55), _c("OF", 69)))
    slots.append((_c(witness, 57), ""))
    slots.append((_c("taken on", 57), _c(taken_on, 69)))
    slots.append(("", _c(commencing_str, 69)))
    slots.append(("", _c(location_lines[0], 69)))
    slots.append((_c(location_lines[1], 57), _c(location_lines[2], 69)))
    slots.append((_c(location_lines[3], 57), _c(location_lines[4], 69)))
    slots.append(("", _c(reporter_str, 69)))
    slots.append(("", _STAR_SUB))
    # 9 depo slots: 0-indexed 12-20

elif label_in_main and loc_len == 3:
    # depo_start_idx=12, Blanks-style, 3-loc, reporter/STAR in main
    slots.append((_c(depo_label, 55), _c("OF", 69)))
    slots.append((_c(witness, 57), ""))
    slots.append((_c("taken on", 57), _c(taken_on, 69)))
    slots.append(("", _c(commencing_str, 69)))
    slots.append(("", _c(location_lines[0], 69)))
    slots.append(("", _c(location_lines[1], 69)))
    slots.append((_c(location_lines[2], 57), ""))
    slots.append((_c(reporter_str, 57), ""))
    slots.append((_STAR_MAIN, ""))
    # 9 depo slots: 0-indexed 12-20
```

### Helper function signatures (all short, full bodies in file):
- `_leading(text: str) -> int` — count leading spaces
- `_caption_sub(left: str, right: str = "") -> str` — render sub-row caption line
- `_caption_main(left: str, right: str = "") -> str` — render main-row caption line
- `_c(text: str, width: int) -> str` — center-pad text to width
- `_format_page(page_num: int, slots: list[tuple[str, str]]) -> str` — render 25-slot page

---

## Section 4 — Olsen cover.json (full)

```json
{
  "court_header_lines": [
    "IN THE MATTER OF THE ARBITRATION BETWEEN:"
  ],
  "caption": {
    "left_block_lines": [
      "[CLAIMANT_ENTITY_1],",
      "[CLAIMANT_ENTITY_2]",
      "[CLAIMANT_ENTITY_3]",
      "[CLAIMANT_ENTITY_3_CONT],",
      "[CLAIMANT_ENTITY_4]",
      "[CLAIMANT_ENTITY_4_CONT],",
      "[CLAIMANT_ENTITY_4_CONT2],",
      "     Claimants,",
      "v.",
      "[RESPONDENT_LINE_1]",
      "[RESPONDENT_LINE_2]",
      "[RESPONDENT_LINE_3]",
      "[RESPONDENT_LINE_4]",
      "[RESPONDENT_LINE_5]",
      "[RESPONDENT_LINE_6]",
      "[RESPONDENT_LINE_7]",
      "[RESPONDENT_LINE_8]",
      "[RESPONDENT_LINE_9]",
      "     Respondents."
    ],
    "right_block_lines": [
      "JAMS REF NO.",
      "[JAMS_REF_NUM]"
    ],
    "trailing_lines": null
  },
  "deposition_label": "DEPOSITION",
  "witness_name": "[WITNESS]",
  "_note_witness_name": "TODO: cover vs cert name variance is intentional (MB's habit). Do not normalize.",
  "taken_on": "[Day], [Month DD], [YYYY]",
  "commencing_at": "[H:MM a.m.]",
  "location_lines": [
    "at",
    "the offices",
    "of",
    "[LAW_FIRM_LOCATION]",
    "[STREET_ADDRESS]",
    "[CITY_STATE_ZIP]"
  ],
  "reported_by": "[REPORTER]"
}
```

**Key structural facts (unredacted):**
- `court_header_lines`: **1 item** (the crash trigger)
- `caption.left_block_lines`: **19 items** (vs Halprin's 7)
- `caption.right_block_lines`: **2 items** (vs Halprin's 3)
- `caption.trailing_lines`: null (same as Halprin)
- `deposition_label`: "DEPOSITION" (vs Halprin's "VIDEOTAPED DEPOSITION")
- `location_lines`: **6 items** (vs Halprin's 4) — no existing code path handles loc_len=6
- `_note_witness_name` field present (Olsen-specific note, absent from Halprin)

---

## Section 5 — Halprin vs Olsen cover.json Field-by-Field Diff

| Field | Halprin | Olsen | Difference |
|---|---|---|---|
| `court_header_lines` count | 3 | 1 | **Critical** — drives depo_start_idx and label_in_main |
| `caption.left_block_lines` count | 7 | 19 | Olsen caption is 2.7x longer |
| `caption.right_block_lines` count | 3 (docket no., number, division) | 2 (JAMS REF NO., number) | No division line in arbitration |
| `caption.trailing_lines` | null | null | Same |
| `deposition_label` | "VIDEOTAPED DEPOSITION" | "DEPOSITION" | Shorter label |
| `witness_name` | present | present | Different content (not structural) |
| `_note_witness_name` | absent | present | Olsen has cover/cert name note |
| `taken_on` | date string | date string | Different content |
| `commencing_at` | time string | time string | Different content |
| `location_lines` count | 4 | 6 | **Critical** — no loc_len=6 code branch exists |
| `reported_by` | present | present | Same reporter |

**Two structural blockers identified:**
1. `court_header_lines` count=1 → crashes at `_DEPO_START_IDX.get(1)` returns None
2. `location_lines` count=6 → no `elif label_in_main and loc_len == 6` branch exists (falls to `raise NotImplementedError`)

---

## Section 6 — Appearances Page Anchoring Check

**File:** `src/stage5/appearances_renderer.py`
(Note: actual path is `src/stage5/appearances_renderer.py`, NOT `src/stage5/front_matter/appearances_renderer.py` as spec assumed.)

### Cover-dependent code in appearances_renderer.py:

The appearances renderer does NOT depend on cover layout at all. The `start_page` parameter is passed in by the orchestrator:

```python
def build_appearances_pages_v2(appearances_data: dict, start_page: int) -> str:
    ...
```

The renderer does not know or care what the cover looked like. So B1.7.4 does not directly affect the appearances renderer code.

### MB-specific bottom-anchor (line 362):
```python
reporter_anchor_line=19 if reporter_rows else None,
```
Hardcoded at line 19. MB-specific — flagged in module header comment.

### Olsen appearances structure vs Halprin:

| Element | Halprin | Olsen | Notes |
|---|---|---|---|
| `firm_groups` count | unknown (full depo) | 2 | Claimants + Respondents counsel |
| `also_present.kind` | unknown | `inline_label` | Videographer only; not `header_block` |
| `reporter_block_lines` | present | present | Both have reporter block |
| reporter line in oracle | line 19 | line 18 | **1-slot discrepancy vs anchor=19** |

**Appearances anchoring finding:** Olsen oracle shows "Reported by:" starting at line 18 of page 4, but `reporter_anchor_line=19`. This means the renderer will pad one extra blank slot and push reporter to line 19, not line 18. This will NOT match the oracle.

**However:** This is an MB-specific setting labeled as such. Whether Olsen's appearances truly anchors at 18 vs 19 needs confirmation. It's possible the oracle has fewer items than expected and the anchor=19 setting over-padded. Flagging as open question for Opus — this may be a separate tile or a parameter to tune per-depo.

**Page numbering impact:** The appearances `start_page` is assigned by the orchestrator based on how many index pages the index renderer emits. Cover=1, then however many index pages, then appearances. If the index renderer (B1.7.1) correctly counts Olsen's index pages, appearances page numbering will be correct. No cover-layout dependency there.

---

## Section 7 — Proposed Slot Layout for Arbitration Cover

### Slot-by-slot analysis from oracle (1-indexed, matching oracle display):

| Oracle slot | Content | Renderer source |
|---|---|---|
| 1 | Court header (centered) | `court_headers[0]` |
| 2 | STAR_MAIN + caption_sub(rows[0]) | Opening STAR + first caption pair |
| 3–11 | Caption main/sub pairs (9 pairs, 10 total rows → 9 slots after slot 2) | rows[1]–rows[18], paired |
| 12–13 | Blank | Gap |
| 14 | Blank main + STAR_SUB | Gap star (gap_size=4, star_offset=2, star_in_main=False) |
| 15 | Blank | Gap |
| 16 | depo_label (centered 55) + "OF" (centered 69) | Depo block slot 1 |
| 17 | witness (centered 57) + blank | Depo block slot 2 |
| 18 | taken_on (centered 57) + commencing (centered 69) | Depo block slot 3 |
| 19 | loc[0] (centered 57) + loc[1] (centered 69) | Depo block slot 4 |
| 20 | loc[2] (centered 57) + loc[3] (centered 69) | Depo block slot 5 |
| 21 | loc[4] (centered 57) + loc[5] (centered 69) | Depo block slot 6 |
| 22 | blank + reporter (centered 69) | Depo block slot 7 |
| 23 | blank + STAR_SUB | Depo block slot 8 |
| 24–25 | Blank | Trailing fill-to-25 |

**Total: 25 slots ✓**

### Slot math:
- Caption slots: 1 header + 1 star+first-pair + 9 caption pairs = **11 slots** (indices 0–10)
- Gap: depo_start_idx=15 (0-based) → gap_size = 15 - 11 = **4 slots**
- Star lands at gap[2] (star_offset=2, star_in_main=False) → index 13 = oracle slot 14 ✓
- Depo block: **8 slots** (indices 15–22) — note: one fewer than existing 9-slot patterns
- Trailing blanks: **2 slots** (indices 23–24) to fill to 25 ✓

### What changes in code:

**Change 1: Add to `_DEPO_START_IDX`**
```python
_DEPO_START_IDX = {1: 15, 2: 12, 3: 10}
```

**Change 2: Add new depo block branch (loc_len=6)**
```python
elif label_in_main and loc_len == 6:
    # 1-header arbitration case, 6-item location (Olsen-style)
    # 6-item loc pairs into 3 main/sub slots → ends in sub → reporter/STAR in sub
    slots.append((_c(depo_label, 55), _c("OF", 69)))
    slots.append((_c(witness, 57), ""))
    slots.append((_c(taken_on, 57), _c(commencing_str, 69)))
    slots.append((_c(location_lines[0], 57), _c(location_lines[1], 69)))
    slots.append((_c(location_lines[2], 57), _c(location_lines[3], 69)))
    slots.append((_c(location_lines[4], 57), _c(location_lines[5], 69)))
    slots.append(("", _c(reporter_str, 69)))
    slots.append(("", _STAR_SUB))
    # 8 slots: indices 15-22
```

**Note on `label_in_main` flag:** The existing flag `label_in_main = num_headers < 3` evaluates to True for count=1. This is structurally correct for Olsen (depo label lands in main row of first depo slot, same as federal cases). The flag doesn't need changing — the `loc_len=6` condition distinguishes Olsen from existing federal patterns.

### Tradeoffs / alternatives:

**Option A (recommended):** Add `1: 15` to `_DEPO_START_IDX` + add `loc_len==6` branch as above. Minimal, targeted, fits the existing pattern.

**Option B:** Add a `case_type` field to cover.json and route by `case_type=="arbitration"`. More explicit but introduces a new data field and changes all cover JSONs. Overkill for now — only one arbitration depo in play.

**Recommendation: Option A.** Two-line dict change + one new elif block. Matches existing code style exactly.

---

## Section 8 — Files B1.7.4 Build Will Touch

| File | Change | Why |
|---|---|---|
| `src/stage5/front_matter/cover.py` | `_DEPO_START_IDX` dict + new `elif` branch | Core fix for count=1 + loc_len=6 |
| `io/analysis/032025olsen/_front_matter_out/032025olsen.front_matter.txt` | New output file | Harness render output (auto-generated, not hand-edited) |

**No other files expected to change.** The appearances_renderer.py, orchestrator, and harness runner do not need modification for the cover fix.

**Possible out-of-scope finding:** The appearances reporter anchor (anchor=19 vs oracle line 18) may need a separate fix. If yes, that would touch `appearances_renderer.py`. Not including it in B1.7.4 scope without Opus call.

---

## Section 9 — Collision Check with B1.7.3

| Question | Answer |
|---|---|
| Does B1.7.4 touch `src/stage5/front_matter/stipulation.py`? | **No** |
| Does B1.7.4 touch any file B1.7.3 touches? | **No** — B1.7.3 owns `stipulation.py`; B1.7.4 owns `cover.py`. Zero overlap. |

No flag needed. Clean separation.

---

## Section 10 — Open Questions for Opus

**Q1 — Oracle backtick artifact:** The raw oracle file has a leading backtick on line 1: `` `IN THE MATTER OF THE ARBITRATION BETWEEN:``. Is this a file-format artifact (not part of the rendered text), or does it represent a real character in the FINAL? If it's an artifact, no action needed. If real, the cover renderer may need to strip it or the cover.json field may already handle it (the JSON does not have a backtick).

**Q2 — Appearances reporter anchor line:** Olsen oracle page 4 shows "Reported by:" at line 18. The `reporter_anchor_line` is hardcoded at 19. Rendering Olsen with the current code would push reporter to line 19, adding one extra blank slot — not matching oracle. Options: (a) leave it (acceptable delta), (b) make anchor a per-depo data field, (c) fix to 18 for Olsen as a separate small tile. Opus to decide scope.

**Q3 — Arbitration `label_in_main` semantics:** For count=1, `label_in_main = num_headers < 3 = True`. This happens to produce the correct layout for Olsen. But is this the right long-term design, or should arbitration get its own flag (e.g., `case_type`) to avoid ambiguity? Fine for now with Option A, but worth noting for CR #2 generalization.

**Q4 — loc_len=6 universality:** Is 6-item location specific to this arbitration, or could other arbitration depos have 4 or 5 location lines? If other loc_len values are possible for count=1 headers, the build spec should address them or at least guard against them.

**Q5 — Olsen appearances page number:** The harness will render Olsen front matter. The appearances `start_page` depends on how many index pages the index renderer emits for Olsen. Olsen oracle has index on pages 2-3 (2 index pages). Does the index renderer currently produce 2 pages for Olsen? If not, appearances will land on the wrong page number.

---

## Summary for Opus

Two code changes needed in `cover.py` to unblock Olsen:

1. `_DEPO_START_IDX = {1: 15, 2: 12, 3: 10}` (add `1: 15`)
2. New `elif label_in_main and loc_len == 6:` branch with 8 depo slots

Both changes are small, contained in one file, and follow existing code patterns exactly. No other engine files need to change for the cover fix.

Five open questions above for Opus before build spec is written, particularly Q2 (appearances anchor) and Q5 (Olsen index page count) which could affect whether Olsen renders correctly after the cover fix alone.

— End of recon —
