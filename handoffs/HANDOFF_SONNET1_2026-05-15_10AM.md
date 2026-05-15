# HANDOFF — Sonnet #1 — 2026-05-15 ~10AM

## Session summary
Friday morning grind. Lane A. Two tiles completed, one in recon.

---

## COMPLETED THIS SESSION

### Tile A1 — Differ v0.2 (DONE, pushed)
**Branch:** `feature/differ-v0.2` — pushed to origin, NOT merged to main yet.
**Commit:** `0f6352f` — `universal: differ v0.2 — drop word_substitution noise, add q_a_speaker_change category`
**Files changed:**
- `src/aligner_differ/categorize.py` — two changes:
  1. Added `_DROP` sentinel + detection logic for would-be word_substitution events (both alpha tokens, replace op, no earlier rule matched)
  2. Added `q_a_speaker_change` check BEFORE `proper_noun_change` — triggers on Q↔A replace ops
  3. `categorize_events()` now filters out `_DROP` events entirely (mutates list in-place)
- `tests/aligner_differ/test_aligner_differ.py` — two new tests added (tests 7 and 8, old 7/8 renumbered to 9/10)
**Test result:** 12/12 green
**Stage A re-run results (9 pairs):**
- Total events: 631,209 → 491,297 (−139,912 word_substitution dropped ✓)
- word_substitution: absent ✓
- q_a_speaker_change: 197 events (Q→A 103x, A→Q 94x) ✓
- em_dash_inserted: 1,151 — untouched ✓
- proper_noun_change: 9,343 (top patterns now real names, no Q/A) ✓
**v0.2 outputs at:** `mrx-context/fingerprints/stage_a/v0.2/`
**Scott action needed:** Review branch, merge to main when satisfied.

---

### Tile: Missing knowledge files (DONE, pushed to mrx-context main)
**Commit:** `ca73206`
- `knowledge/2026-05-14_evening_stage_a_9pair_hunt.md` — was untracked, never pushed
- `knowledge/2026-05-14_evening_blank_sgngl_investigation.md` — same

---

### Tile: Halprin front matter re-render (DONE, no push)
- Pre-fix baseline saved: `io/analysis/halprin_full/_stage5_out/halprin_full.OUR_FINAL.pre-fix.txt`
- Post-fix render: `io/analysis/halprin_full/_stage5_out/halprin_full.OUR_FINAL.txt`
- Copy at: `mrx-context/renders/2026-05-15_halprin_front_matter_verify.txt`
- **Finding:** Files are byte-for-byte identical. Root cause: Thursday's fixes landed in `appearances_renderer.py` but the live pipeline calls `appearances_page.py` (hardcoded literal template). The renderer is correct but not wired in. This is why A1.5 exists.
- Halprin appearances visual check: "Reported by:" IS at line 19, pages 5-10 render correctly (because the hardcoded template already had the right layout from oracle extraction).

---

### Tile: Ledger + spec saves (DONE)
- `mrx-context/specs/2026-05-15_A1.5_APPEARANCES_WIRE_IN.md` — saved
- `mrx-context/specs/2026-05-15_A1_DIFFER_v0.2.md` — saved
- `mrx-context/fingerprints/ledger.md` — row 19 added (Appearances renderer wiring debt), item 5 added to generalization questions
- **NOT pushed yet** — Scott batching with other pending pushes.

---

## IN PROGRESS — HAND OFF TO NEXT SONNET

### Tile A1.5 — Wire in appearances_renderer.py (RECON DONE, build not started)
**Branch:** `feature/appearances-wire-in` — created locally, clean, no commits yet.
**Spec:** `mrx-context/specs/2026-05-15_A1.5_APPEARANCES_WIRE_IN.md`

**Recon findings (Step 1 complete):**

Call site in assemble_final.py:
```
line 25:  from .appearances_page import APPEARANCES_PAGE_COUNT, build_appearances_pages
line 245: _appearances_text = build_appearances_pages(case_info)
line 246: _appearances_pages = APPEARANCES_PAGE_COUNT  # = 9
```

Renderer entry function:
```python
build_appearances_pages_v2(appearances_data: dict, start_page: int) -> str
```

**GAP 1 — Spec has wrong data path.**
Spec says: `src/stage5/data/appearances/halprin.json` — does NOT exist.
Real path: `src/profiles/mb/data/front_matter/halprin/appearances.json`
JSON has `"start_page": 5` field built in.

**GAP 2 — Renderer only covers pages 5-10 (appearances), not 2-4 (index/exhibits).**
`build_appearances_pages(case_info)` returns pages 2-10 (9 pages).
`build_appearances_pages_v2(...)` returns pages 5-10 only (6 pages).
Wire-in must:
1. Keep pages 2-4 from `appearances_page.py` (import `_PAGE_2`, `_PAGE_3`, `_PAGE_4` directly)
2. Call `build_appearances_pages_v2(appearances_data, start_page=5)` for pages 5-10
3. Concatenate: `_PAGE_2 + _PAGE_3 + _PAGE_4 + renderer_output`
4. `_appearances_pages` stays 9 (3 + 6)

**Second depo JSONs available (5 others):**
```
src/profiles/mb/data/front_matter/032025olsen/appearances.json
src/profiles/mb/data/front_matter/0525black_bp/appearances.json
src/profiles/mb/data/front_matter/060122williams/appearances.json
src/profiles/mb/data/front_matter/082222butler/appearances.json
src/profiles/mb/data/front_matter/101322blanks/appearances.json
```

**Scott + Opus approval received for recon.** Awaiting go-build for Step 2.

**Step 2 build plan (for next Sonnet):**
1. In `assemble_final.py`:
   - Add import: `from .appearances_page import _PAGE_2, _PAGE_3, _PAGE_4`
   - Add import: `from .appearances_renderer import build_appearances_pages_v2`
   - Load appearances JSON: `src/profiles/mb/data/front_matter/{depo_name}/appearances.json`
   - Replace line 245-246 with the stitched call
2. Run pytest tests/stage5/ — all green
3. Run `_run_halprin_full_stage5.py`
4. Diff output against `halprin_full.OUR_FINAL.pre-fix.txt` (must match byte-for-byte)
5. Diff against oracle FINAL (path in spec)
6. If green: report, do NOT push — Scott reviews

---

## REPO STATE SUMMARY

| Repo | Branch | Status |
|---|---|---|
| mrx_engine_v1 | `feature/differ-v0.2` | pushed, awaiting Scott merge to main |
| mrx_engine_v1 | `feature/appearances-wire-in` | local only, clean, no commits |
| mrx-context | `main` | ledger + specs + renders uncommitted locally |

---

## STANDING REMINDERS FOR NEXT SONNET
- RULE-SPEC-SAVED-FIRST: spec already saved, skip that step
- PRINT BEFORE COMMIT: `cat assemble_final.py` + `cat appearances_renderer.py`
- DO NOT PUSH feature/appearances-wire-in — Scott reviews first
- DO NOT modify appearances_renderer.py internals — only assemble_final.py
- appearances_page.py stays on disk (rollback fallback)
- Opus owns ledger update after wire-in confirms (row 19 DEBT → RESOLVED)

---

*Sonnet #1 tapping out. Context full. Good session.*
