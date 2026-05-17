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

### D-4 — Olsen INDEX page Reporter's Certificate slot position (OLSEN-SPECIFIC, possibly)
- **Observed:** Olsen page 2 — Reporter's Certificate sits 1 slot lower than oracle
- **Halprin:** Reporter's Certificate sits at correct slot
- **Severity:** Cosmetic; tied to whether Olsen has different index spacing rules
- **Likely module:** index renderer

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
2. **D-4 (Olsen reporter slot)** — single-depo, cosmetic.
3. **D-5 (Olsen exhibits packing)** — may be universal but only seen on one depo; needs cross-check first.
4. ~~D-1~~ — closed, phantom defect.
5. ~~D-3~~ — closed, no work needed.

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
