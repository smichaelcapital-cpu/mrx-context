# SPEC — Appearances Overflow + Back Matter Spacing Fix
Date: 2026-05-13
Architect: Opus
Builder: Sonnet
Owner: Scott

## Universal? NO — MB-specific (Halprin scope today)
## Code or prompt? CODE
## File location:
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\front_matter\appearances.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\front_matter\orchestrator.py
- Tests: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\stage5\test_front_matter.py

## Commit prefix: mb-specific:

---

## CONTEXT

Halprin front matter renders end-to-end (21,705 bytes vs 21,782 oracle, 77-byte delta, all tests green). Scott eyeballed the output 2026-05-13 morning. Three shape issues surfaced. None reduce content accuracy. All reduce visual credibility on the page.

## PRIME DIRECTIVE CHECK

Could this reduce transcript accuracy or credibility?
- Accuracy: NO — no content added, removed, or changed. Layout only.
- Credibility: YES — current output looks broken (orphaned firm name on a page with no header above it). Fix INCREASES credibility.

Safe to proceed.

---

## ISSUE 1 — Appearances Overflow Splits Defendant Block Mid-Block

### Observed (rendered output)
On the appearances overflow page, the renderer page-breaks inside a defendant block. Result: page 1 ends with "FOR THE DEFENDANT, ZURICH..." header + caption. Page 2 starts with "A P P E A R A N C E S:" header, then jumps straight into "Suite 3600 / Chicago, Illinois" — an orphaned address with no firm name visible above it on that page.

### Expected (MB FINAL)
Each FOR THE DEFENDANT... block stays together. If a defendant block won't fit in the remaining lines on the current page, the WHOLE block moves to the next page. Page 1 ends with the LAST defendant block that fit completely. Page 2 starts with A P P E A R A N C E S: header, then the next defendant block beginning with its FOR THE DEFENDANT... line.

### Rule
KEEP-TOGETHER for defendant blocks. A defendant block is the unit from FOR THE DEFENDANT... (or FOR THE PLAINTIFF..., etc.) through the last line of that party's appearance (typically BY: ... or NOT PRESENT or the last email line).

Before emitting a defendant block, compute the line cost of the block (count of content lines + intra-block spacing). If current_line + block_line_cost > 25, page-break BEFORE the block, emit A P P E A R A N C E S: header on the new page, then emit the block.

### Test
Render Halprin appearances. Diff against C:\Users\scott\OneDrive\Documents\mrx-context\io\halprin_FINAL_compare_2026-05-12.txt. The "Suite 3600" orphan must be gone. The Zurich block must start with FOR THE DEFENDANT, ZURICH... at the top of its page (after the A P P E A R A N C E S: header).

---

## ISSUE 2 — Missing Padding Above Reported by:

### Observed (rendered output)
After the last FOR THE DEFENDANT... block on the final appearances page, ALSO PRESENT: follows immediately with normal spacing. Then Reported by: follows immediately after Darren Guastella, Videographer. Result: Reported by: lands too high on the page (line 13). Bottom of page is mostly empty (lines 16-23 are blank line numbers only).

### Expected (MB FINAL)
ALSO PRESENT: and Reported by: blocks are bottom-anchored on the final appearances page. The empty space sits ABOVE these blocks, not below them. In Halprin FINAL:
- ALSO PRESENT: lands at line 13
- Videographer name at line 14
- 4 blank lines (15-18)
- Reported by: block starts at line 19
- Reported by: block fills lines 19-21
- Page ends at line 25 (lines 22-25 blank)

### Rule
On the final appearances page, after the last defendant block, the renderer pads with blank lines so that the Reported by: block ends at line 25 - REPORTER_BLOCK_BOTTOM_MARGIN.

For Halprin: Reported by: block spans lines 19-21 in FINAL.

Recommended approach (simple, MB-specific for now):
1. Compute current line position after emitting ALSO PRESENT: + videographer.
2. Compute lines required for Reported by: block (count from JSON).
3. Target final line = 21 (where Reported by: block ends in Halprin FINAL).
4. Pad with blank lines between videographer and Reported by: so the block lands at the target.

This is Halprin-shaped today. Generalize later when Williams or Olsen reveals their shape.

### Test
Diff against FINAL. Reported by: Marybeth E. Muir, line must land on line 19 of the final appearances page (matching FINAL). Lines 22-25 must be blank line-number-only.

---

## ISSUE 3 — ALSO PRESENT: Vertical Position

### Observed
ALSO PRESENT: currently lands at line 11 (Halprin render). In FINAL it lands at line 13.

### Expected
ALSO PRESENT: lands at line 13 on the final appearances page (after the last FOR THE DEFENDANT... block).

### Rule
Same anchor concept as Issue 2. The 2-line gap between the last FOR THE DEFENDANT... block (which ends at line 11 with NOT PRESENT) and ALSO PRESENT: (line 13) means 1 blank line between them, then ALSO PRESENT: on line 13.

Already shape-matches for the gap between blocks. The line-11-vs-13 difference is a downstream effect of Issue 1 (when defendant blocks page-break correctly, the last block ends at a different line, and ALSO PRESENT: falls into place).

Recommendation: Fix Issue 1 first. Re-render. If ALSO PRESENT: is still off, treat as a separate spacing tweak.

---

## RECON GATE (RULE-RECON-FIRST)

Before any code change, Sonnet must:

1. git checkout -b fix/appearances-overflow-and-back-matter-spacing off main
2. Read current src\stage5\front_matter\appearances.py end-to-end
3. Read current src\stage5\front_matter\orchestrator.py end-to-end
4. Read the Halprin appearances JSON at src\profiles\mb\data\front_matter\halprin\appearances.json
5. Report:
   - How does the current code decide where to page-break?
   - Is there a KEEP_TOGETHER concept already in the code?
   - Where does ALSO PRESENT: get emitted (appearances.py or orchestrator.py)?
   - Where does Reported by: get emitted?
6. Wait for explicit "go build" from Opus before writing any code.

## CONTRADICTION HUNT (RULE-CONTRADICTION-HUNT)

Grep across appearances.py and orchestrator.py for: page_break, line_count, 25, also_present, reported_by, bottom, anchor, pad. Report all hits in context. Identify any logic that might fight a KEEP_TOGETHER rule.

## SILENT FAILURE CHECK (RULE-SILENT-FAILURE-CHECK)

After the fix, re-run ALL existing tests in tests/stage5/test_front_matter.py to confirm nothing else broke. Specifically:
- All 137 cover tests
- All Halprin index tests
- All Halprin appearances tests (existing)
- All stipulation/cert/witness/errata/orchestrator tests

If any pre-existing test fails, STOP and report. Do not "fix" the existing test to pass.

## TEST PLAN

1. Update or add tests in tests/stage5/test_front_matter.py:
   - test_appearances_defendant_block_keep_together — assert no orphaned address blocks at top of overflow pages.
   - test_appearances_overflow_header_repeats — assert A P P E A R A N C E S: appears at line 1 of every overflow page.
   - test_appearances_final_page_reported_by_anchor — assert Reported by: block starts at line 19 on Halprin's final appearances page.
   - test_appearances_final_page_also_present_line — assert ALSO PRESENT: lands at line 13.
2. Re-run full orchestrator render against Halprin.
3. Diff rendered output against halprin_FINAL_compare_2026-05-12.txt. Target: zero new diffs, byte delta improves from 77 toward 0.
4. Eyeball-check pages 9, 10, 11 of rendered output (where the overflow + back matter spacing live).

## ROLLOUT SEQUENCE

1. Branch off main (RECON gate)
2. Recon report → Opus reviews → green light
3. Code changes on branch
4. Tests green
5. Re-render Halprin
6. Diff vs FINAL
7. Scott eyeballs
8. Merge to main, push origin
9. Delete branch (keep backup branch from earlier today)

## ROLLBACK PLAN

If the fix breaks anything:
1. Revert the merge commit on main
2. Backup branch backup/pre-appearances-overflow-2026-05-13 is the safety snapshot
3. Backup file at C:\Users\scott\OneDrive\Documents\mrx-context\io\halprin_full_render_2026-05-12.BACKUP.txt is the byte-level safety net

## OPEN ITEMS REQUIRING SCOTT SIGN-OFF

1. Confirm KEEP-TOGETHER unit is the full FOR THE DEFENDANT... block (start of FOR THE... line through end of that party's last line). Yes / No.
2. Confirm Reported by: target line = 19 on the final appearances page (matching FINAL). Yes / No.
3. Confirm ALSO PRESENT: target line = 13 on the final appearances page (matching FINAL). Yes / No.

— End of spec —
