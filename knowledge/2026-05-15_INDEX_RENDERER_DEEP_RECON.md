# INDEX RENDERER DEEP RECON
**Date:** 2026-05-15
**Branch:** main (mrx-context)
**Scope:** Recon only — zero code changes. Read actual files, no assumptions.
**Author:** Sonnet #2 (Lane B)

---

## Purpose

Pre-build recon for B1.7.1 (index wire-in + guard fix). Extends the 2026-05-15 B1.7 audit.
Expands the known 2-bug list to 6 bugs and identifies a critical false-pass risk.

Files examined:
- `src/stage5/front_matter/index.py`
- `src/stage5/front_matter/orchestrator.py`
- `src/stage5/assemble_final.py`
- `src/profiles/mb/data/front_matter/{depo}/index.json` (all 6 depos)

---

## Bug Table (B1–B6)

| # | File | Line | Issue | Status in prior audit |
|---|---|---|---|---|
| B1 | `src/stage5/front_matter/index.py` | 193 | `if len(nav) < 6: raise NotImplementedError` — hard stop; blocks butler, olsen, blanks (5-entry nav) | Known |
| B2 | `src/stage5/front_matter/index.py` | 221 | `wit = nav[5]` unconditional — crashes for any depo with fewer than 6 nav entries | Known |
| B3 | `src/stage5/front_matter/index.py` | 204–221 | Renderer uses **hardcoded nav indices**: nav[3]=Exam, nav[4]=Rpt Cert, nav[5]=Wit Cert. Fails silently for depos with a "Re Examination" entry (black_bp, Williams) — Re Examination occupies nav[4], pushing certs to wrong slots. Depos pass the `< 6` guard but render incorrect labels. | **NEW — not in prior audit** |
| B4 | `src/stage5/front_matter/index.py` | 210 | `exam["sub_entries"][0]` hardcoded — only first sub_entry rendered. Williams (Mr. Leefe, Mr. Gileson) and black_bp (Mr. McNeal, Mr. Falcon) each have 2 Examination sub_entries; second examiner silently dropped from index. | **NEW — not in prior audit** |
| B5 | `src/stage5/front_matter/index.py` | 83, 86, 92, 95 | `str(page)` called unconditionally when `is_last=True`. black_bp exhibit 11 (`"NOT MARKED"`) has `page: null` → renders as string `"None"` in output. | **NEW — not in prior audit** |
| B6 | `src/stage5/front_matter/orchestrator.py` | 122 | `wc_data = _load(depo_stem, "witness_cert.json")` loaded **before** the `read_and_sign` guard at line 127. Crashes immediately for butler, olsen, black_bp, blanks — none have witness_cert.json. | **NEW — not in prior audit** |

---

## Wire-In Status

`build_index_pages()` is called from `orchestrator.py` line 91 inside `build_front_matter()`.
`build_front_matter()` and `build_back_matter()` are **not imported or called** from `assemble_final.py`.
Only reference in assemble_final is a path string at line 250 — not a function call.
The entire front_matter orchestrator is unwired from the assembly pipeline.

---

## Per-Depo Nav Structure

| Depo | Nav entry count | Examination sub_entries | Has Re Examination | Has Witness Cert in nav | Exhibit count | Shape oddities |
|---|---|---|---|---|---|---|
| halprin | 6 | 1 (Mr. Caughey) | No | Yes ("Witness's Certificate") | 23 (starting #236) | None |
| 060122williams | 7 | 2 (Mr. Leefe, Mr. Gileson) | Yes (1 sub_entry: Mr. Leefe) | Yes ("Witness Certificate" — label differs from Halprin) | 22 | Label variant; Re Examination present; 2 Exam sub_entries |
| 082222butler | 5 | 1 (Mr. Bullock) | No | No | 4 | None |
| 032025olsen | 5 | 1 (Mr. Knight) | No | No | 22 | None |
| 0525black_bp | 6 | 2 (Mr. McNeal, Mr. Falcon) | Yes (1 sub_entry: Mr. McNeal, page 198) | No | 27 | Exhibit 11: `"NOT MARKED"`, page null (B5 trigger); Exhibit 5A: non-sequential number (string label, likely fine); 2 Exam sub_entries |
| 101322blanks | 5 | 1 (Mr. McMillin) | No | No | 2 | None |

---

## Flags for Opus / Scott

### FLAG 1 — B3+B4 false-pass risk (HIGH)
black_bp has 6 nav entries and passes the `< 6` guard. The prior audit implied fixing the guard
to `< 5` would unblock butler/olsen/blanks and that black_bp was fine. It is not fine.
black_bp's Re Examination entry sits at nav[4], so the renderer assigns it the "Reporter's Certificate"
slot and assigns nav[5] ("Reporter's Certificate") the "Witness's Certificate" slot.
The index page would render with incorrect section labels and no Re Examination entry.
Williams (7 entries) has the same structural problem plus an entire nav entry (Witness Certificate)
that is never reached by the renderer.
**Fixing only the guard produces incorrect output for 2 of 6 depos with no error raised.**

### FLAG 2 — "Witness Certificate" vs "Witness's Certificate" label variant
Halprin index.json uses `"Witness's Certificate"`. Williams uses `"Witness Certificate"` (no possessive).
Before any label-based nav lookup is implemented, Opus must confirm:
(a) which spelling each depo's oracle FINAL uses, and
(b) whether the lookup should match by substring (e.g., `"witness"`) or require exact label.

### FLAG 3 — "NOT MARKED" exhibit with page: null (display decision needed)
black_bp exhibit 11 has `"description_lines": ["NOT MARKED"], "page": null`.
The renderer has no null-page handling. Opus/Scott must decide before build:
- Option A: Render page field as blank (empty string)
- Option B: Render literal text "NOT MARKED" where the page number would appear
- Option C: Skip the exhibit entirely from the index
This is a credibility question — a court reporter's index must match the actual transcript.

---

## Recommended B1.7.1 v2 Scope

The prior spec described 2 fixes. The correct scope is 6:

1. **Replace hardcoded nav index access with label-based lookup** — handles 5, 6, and 7 entry nav lists correctly. Use a pattern like `_nav_page()` already in orchestrator.py. Resolves B1, B2, B3.
2. **Loop over all sub_entries for Examination (and Re Examination)** — not just `[0]`. Resolves B4.
3. **Guard `page` before `str(page)` in exhibit renderer** — handle null page per FLAG 3 decision. Resolves B5.
4. **Move `witness_cert.json` load inside `if read_and_sign:` block** in orchestrator.py. Resolves B6.
5. **Wire `build_front_matter()` + `build_back_matter()` into `assemble_final.py`** — the orchestrator exists and is correct in structure but is never called.
6. **Confirm "Witness Certificate" label variant** before implementing label-based lookup (FLAG 2).

Items 1–4 are code fixes. Item 5 is the wire-in. Item 6 is a data/spec clarification that must be resolved by Opus before build starts.

---

## Closing

Original B1.7 audit verdict was incomplete. B1.7.1 spec must be rewritten before any build work.
