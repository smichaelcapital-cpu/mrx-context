# Verification Run — All 6 MB Depos

**Date:** 2026-05-16
**Builder:** Sonnet #1 (Lane B)
**Main commit verified:** `711eb26` (merge: B1.7.3 waive stipulation + B1.7.4 arbitration cover)
**Type:** Read-only. No code changes. No commits to engine repo.

---

## Results

| Depo | Exit | Pages | Back Matter | Notes |
|---|---|---|---|---|
| halprin | 0 | 16 | rendered | Clean. No regression. |
| 060122williams | 0 | 12 | rendered | Clean. No regression. |
| 082222butler | 0 | 4 | not applicable | Clean. B1.7.3 waive-mode unblocked. |
| 101322blanks | 0 | 4 | not applicable | Clean. B1.7.3 waive-mode unblocked. |
| 032025olsen | 0 | 5 | not applicable | Clean. B1.7.4 cover fix unblocked. |
| 0525black_bp | 0 | — | SKIPPED | WARN: `label_in_main=True, loc_len=4` — renderer not yet implemented. B1.7.5 tile. |

---

## Summary

- **5 of 6 depos render clean** (exit 0, pages produced).
- **halprin + williams:** zero regression vs pre-B1.7.3/B1.7.4 baseline.
- **butler + blanks:** newly unblocked by B1.7.3 (waive-mode stipulation). 4 pages each.
- **olsen:** newly unblocked by B1.7.4 (arbitration cover). 5 pages.
- **black_bp:** still blocked. Harness gracefully skips with WARN (exit 0). B1.7.5 covers this.

---

## Known Remaining Gaps (not regressions)

| Tile | Depo | Issue |
|---|---|---|
| B1.7.5 | 0525black_bp | Cover renderer: `label_in_main=True, loc_len=4` not yet implemented |
| B1.7.6 | 032025olsen | Appearances reporter anchor: renders at slot 18 sub vs oracle slot 18 main |
| B1.7.7 | 032025olsen | Appearances VIDEOGRAPHER: renders at slot 14 main vs oracle slot 15 sub |

---

## Phase Status After This Merge

All 5 rendered depos pass exit 0. B1.7.5 (black_bp cover) is the last cover-renderer gap before all 6 depos produce output.

— End of verification report —
