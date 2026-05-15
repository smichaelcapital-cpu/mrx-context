# Renderer + Data Gaps Surfaced in Phase 2 — 2026-05-15

**Date:** 2026-05-15 (evening session)
**Author:** Sonnet #1 (knowledge), Sonnet #2 (Phase 2 runner), Opus (architect)
**Status:** All gaps deferred to next session. Phase 2 shipped with 2 fully rendered depos (Halprin + Williams).

---

## Context

Phase 2 of the front matter harness ran the orchestrator against all 6 MB depos. Halprin (the reference depo) and Williams rendered fully. The other 4 surfaced renderer and data gaps that were not known before this run. This is exactly the kind of signal the pivot was supposed to produce — cross-depo render exposed real renderer coverage gaps that single-depo Halprin polish never would have.

All four gaps are documented below as separate tiles for next session.

---

## B1.7.2 — Williams witness_cert + Olsen stipulation data fixes (LANDED TONIGHT)

**Status:** Resolved tonight. Listed here for completeness.

### Williams gap
- File: `src/profiles/mb/data/front_matter/060122williams/witness_cert.json`
- Original content was incomplete — missing `depo_date_prose` and `errata_page_count`
- Halprin's schema (working reference): `witness_name_caps`, `depo_date_prose`, `errata_sheet_count`, `errata_page_count`
- Sonnet #1 read Williams' oracle FINAL and extracted: `depo_date_prose: "June 1, 2022"`, `errata_page_count: 2`
- JSON updated. Williams re-rendered: 7 pages → 12 pages with full back matter
- Commit: 1ed648c (data fix) + a1cbece (refresh render)

### Olsen gap
- File: `src/profiles/mb/data/front_matter/032025olsen/stipulation.json`
- Original said `witness_reserves_signature: true`, but Olsen's oracle FINAL has no witness certificate / read-and-sign section anywhere in the document
- Stipulation value was wrong. Corrected to `false`
- Olsen still can't render — blocked downstream by B1.7.4 (arbitration cover layout)
- Commit: 1ed648c

---

## B1.7.3 — Stipulation waive-mode renderer NOT IMPLEMENTED (NEW TILE)

**Status:** Deferred. Blocks Butler, black_bp, Blanks.

### What we found
The stipulation renderer in `src/stage5/front_matter/stipulation.py` (or wherever it lives — confirm in recon) raises `NotImplementedError` when `witness_reserves_signature: false`. The "waive" variant — the witness waives signature instead of reserving it — has no renderer code path.

### Which depos this blocks
- 082222butler — waive mode
- 0525black_bp — waive mode
- 101322blanks — waive mode
- 032025olsen — waive mode (after B1.7.2 fix)

That's 4 of 6 MB depos. Waive mode is the common case, not the edge case. The renderer was only built for the read-and-sign variant Halprin uses.

### What it needs
A new stipulation page variant. Read what waive-mode stipulation language looks like in any of the 4 oracle FINAL files (recommend Butler — smallest). Build the renderer to produce that variant when `witness_reserves_signature: false`.

### Estimated scope
Medium. Stipulation page is short (typically 1 page). New renderer function or branch inside existing function. Verify against Butler oracle first, then re-render the other 3 depos.

### Discovery
Sonnet #2's Phase 2 run on Butler crashed with `NotImplementedError` from the stipulation renderer. Confirmed pattern across black_bp, Blanks too.

### Spec path when written
`specs/2026-05-1X_B1.7.3_WAIVE_MODE_STIPULATION.md`

---

## B1.7.4 — Arbitration cover layout NOT IMPLEMENTED (NEW TILE)

**Status:** Deferred. Blocks Olsen specifically.

### What we found
The cover renderer in `src/stage5/front_matter/cover.py` (or wherever — confirm in recon) supports `court_header_lines` count of 2 or 3 only. Olsen has a `court_header_lines` count of 1 — a single "IN THE MATTER OF..." header for an arbitration proceeding.

The internal `_DEPO_START_IDX` lookup has no entry for `count=1`, so `depo_start_idx` resolves to None and the renderer raises `NotImplementedError`.

### Which depos this blocks
- 032025olsen — arbitration with single-header cover

That's 1 of 6 MB depos. May appear in other arbitration matters MB handles. Single-instance for this depo set.

### What it needs
Arbitration cover layout variant. Slot counts and depo block placement structurally differ from court case covers — this is not just a count extension, it's a different layout. Recommend reading Olsen oracle pages 1-2 to see the exact format MB uses for arbitration cover, then designing the renderer slot structure.

### Estimated scope
Medium-to-larger. Cover layout has many positional rules (witness block, date block, attorney appearances anchor). Arbitration matter format will likely also affect appearances page anchoring. Recon-first mandatory.

### Discovery
Sonnet #2's Phase 2 run on Olsen crashed with `NotImplementedError` from the cover renderer (after waive-mode skip — cover failed earlier in the pipeline than stipulation).

### Spec path when written
`specs/2026-05-1X_B1.7.4_ARBITRATION_COVER_LAYOUT.md`

---

## Cross-cutting observation — "the pivot worked"

The whole point of the multi-depo pivot was that Halprin byte-chasing was teaching us about one depo's quirks, not MB's actual style. Phase 2 produced exactly the signal the pivot promised:

- 2 of 6 depos render fully (Halprin + Williams)
- 3 of 6 depos block on **renderer features that don't exist** (B1.7.3 + B1.7.4 — waive mode + arbitration cover)
- 1 of 6 depos blocked on a data correctness issue surfaced by attempting the render (Olsen's stipulation was wrong; only by trying to render her did we discover the discrepancy with her oracle)

None of these gaps would have been found by continuing to polish Halprin. All were found in a single Phase 2 run by running the existing universal renderer against new data.

This pattern — "render to discover gaps" — is now the proven workflow. Future MB depos onboard by: extract front matter JSONs, render, fix gaps surfaced.

---

## Next-session priority (Opus call, not committed)

If the goal is rendering more MB depos by end of next session, the highest-leverage tile is **B1.7.3 (waive-mode stipulation)** because it unblocks 3 depos in one fix. B1.7.4 (arbitration cover) unblocks 1 depo and is structurally larger.

Recommendation: B1.7.3 first, B1.7.4 second.

— End of capture —
