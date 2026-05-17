# Front Matter Defect Ledger — 2026-05-16

**Source:** Scott's read-through of fm_review.py side-by-side files for Olsen + Halprin, performed 2026-05-16 morning after B1.8.1 + B1.8.2 + B1.8.3 shipped.

**Method:** Visual comparison of `review/<stem>_front_sxs.txt` files against MB's FINAL.txt slices, page by page.

**Depos read:** 032025olsen (5 front matter pages), halprin (11 front matter pages). Other 4 depos not yet read.

## Known defects

### D-1 — Missing "Page" column header on INDEX page (RESOLVED: phantom defect — see Closed section)

### D-2 — Firm-group blank separator missing on APPEARANCES pages (UNIVERSAL)
- **Observed:** Olsen page 4, Halprin pages 6, 7, 8 — every appearances page checked
- **Oracle:** Inserts one blank slot between consecutive firm groups
- **Ours:** Packs firm groups tighter, no blank between
- **Effect:** 1-slot drift that compounds down the page; later firm groups end up 1+ slots ahead of oracle
- **Severity:** Functional drift, not cosmetic — every multi-firm appearances page is wrong
- **Context:** Scott's project memory previously flagged this issue. The fix was attempted and rolled back. Cross-depo audit at the time confirmed MB's standard is HALF blank between firm groups.
- **Likely module:** appearances_renderer.py — pagination or firm-group concatenation logic

### D-3 — Exhibits page-number column (RESOLVED: display truncation only)
- **Observed:** Halprin page 3 exhibits index — page numbers (215, 222, 245, etc.) appeared missing in the side-by-side view
- **Diagnosis (Sonnet, 2026-05-16):** Read the raw rendered files directly.
  - Halprin verbatim: `     3                  YR-288754-288810             215` (56 chars) — 215 IS present
  - Halprin verbatim: `                        YR-289548-289550             222` (56 chars) — 222 IS present
  - Olsen verbatim: `                        000131.00005                104` (59 chars) — 104 IS present
- **Root cause:** Exhibit description lines with Bates numbers land page numbers at column ~54–59. The 55-char SXS column truncates 1–4 chars at the right edge, hiding the page number in the `_sxs.txt` view. The full content is in the `_diff.txt` files.
- **Resolution:** No code defect. Display-only limitation of the 55-char sxs format.

### D-4 — INDEX page Reporter's Certificate slot position (DEFERRED — B1.9.4 Phase 3)
- **Observed:** Olsen page 2 — cert at slot 7 MAIN (rendered) vs slot 6 SUB (oracle). 1-slot
  drift cascades through sep, EXHIBITS, and all exhibits. black_bp has same pattern (slot 9
  MAIN rendered vs slot 8 SUB oracle). Butler and blanks are correct at slot 7 MAIN.
- **Root cause (recon 2026-05-17):** `build_index_pages()` no-witness path hardcodes cert to
  MAIN position with a blank slot inserted before it. This matches butler/blanks but is wrong
  for olsen and black_bp, where oracle places cert in SUB with no preceding blank. The
  renderer does not track MAIN/SUB parity state through the nav/exam section — cert placement
  is hardcoded, not parity-derived. Code comment at line 344 acknowledges this:
  "Generalised parity derivation is Phase 2 work."
- **Fingerprint data (13-depo Query B):** 76% MAIN / 23% SUB across all depos. Within the
  no-witness group (butler, blanks, olsen, black_bp): 2/4 MAIN, 2/4 SUB — no dominant
  pattern. 76% all-depos is below the 80% ship-confidence threshold.
- **Fix paths considered:**
  - Option A — Phase 3 parity threading: extend micro 1B parity tracker through
    cert/sep/EXHIBITS block; let cert fall wherever the MAIN/SUB cycle lands naturally.
    Correct fix; same architectural pattern as Phase 2B exhibit parity threading.
  - Option B — hardcoded olsen/black_bp override: second no-witness sub-path. Fragile;
    fails on new CRs; creates a new class of hardcoded exception.
- **Decision: Option A. Defer as B1.9.4 Phase 3 — cert parity threading.**
- **Rationale:** Extends micro 1B parity tracker (already wired in B1.9.3); avoids
  hardcoded exceptions; architecturally consistent with Phase 2B stash. Butler and blanks
  must be verified unchanged after any parity fix.
- **Severity:** Cosmetic on olsen/black_bp; affects slot alignment but not content.
- **Module:** `src/stage5/front_matter/index.py` — `build_index_pages()`, no-witness branch.

### D-5 — Olsen exhibits index packing tighter than oracle (possibly Olsen-specific)
- **Observed:** Olsen page 3 — exhibits drift increases down the page; by bottom of page our list is 3-4 exhibits ahead of oracle
- **Halprin:** Did not check Halprin exhibits page comparable drift — needs follow-up
- **Severity:** Functional — affects exhibits index page count and where things sit
- **Likely module:** index renderer

## Not-yet-checked

- Williams (7 front matter pages) — not read
- Butler (4 front matter pages) — not read
- Blanks (4 front matter pages) — not read
- black_bp (6 front matter pages) — not read
- Back matter on Halprin and Williams (5 pages each) — not read

## Read-through left for future sessions

- Cross-check D-2 firm-group separator on Williams and Butler appearances
- Confirm D-5 exhibits packing on a depo other than Olsen
- Read back matter pages on Halprin and Williams
- Skim the 3 untested depos for new defect patterns

## Recommended fix priority for next session

1. **D-2 (firm-group separator)** — universal, functional, compounds drift. Highest blast radius.
2. **D-5 (Olsen exhibits packing)** — may be universal but only seen on one depo; needs cross-check first.
3. ~~D-4~~ — deferred as B1.9.4 Phase 3 (cert parity threading); see revisit list.
4. ~~D-1~~ — closed, phantom defect.
5. ~~D-3~~ — closed, no work needed.

## Standing revisit list

- B1.9.3 Phase 2B — exhibit parity threading (stashed on laneB/B1.9.3-cycle-continuity; ~15 lines)
- B1.9.4 Phase 3 — cert parity threading (D-4 fix path)
- D-5 cross-check — confirm exhibits packing drift on depo other than Olsen before fixing
- B1.7.7 — Olsen videographer cosmetic
- Unread front matter pages: williams, butler, blanks, black_bp
- Unread back matter pages: halprin, williams
- TD-003 — fm_review.py harness display width (55-char column too narrow)
- Church depo ingest failure (12x raw/final ratio anomaly)

---

## Closed

### D-1 — Page column header (CLOSED — PHANTOM, display truncation only)
- Verified 2026-05-16. Code emits "Page" correctly in slot 1 SUB.
- The fm_review.py 55-char SxS column truncates _HEADING_SUB at
  position 53-56, hiding "Page" in the side-by-side view.
- Same root cause as D-3.
- No code defect.
- **Recon confirmed 2026-05-17:** `_HEADING_SUB` (56 chars, 52 spaces + "Page")
  byte-matches oracle on 4/4 depos (halprin, olsen, williams, butler).
  Slot 1 SUB is correct and complete. Root cause is TD-003 (fm_review.py
  55-char column width). No code fix needed.

## Notes

- The harness (B1.8.1-3) made all of this visible. None of these defects would have been caught by the "exit 0 across 6 depos" verification Scott was running this morning before the harness existed.
- D-2 confirms the strategic pivot in Scott's project memory: don't byte-chase a single oracle. We need MB's style derived from her body of work, because the fix that was rolled back was rolled back due to inconsistencies in one source file. Now we have side-by-side across multiple depos to actually triangulate.
