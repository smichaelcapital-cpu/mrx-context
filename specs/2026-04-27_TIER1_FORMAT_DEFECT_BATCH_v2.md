# SPEC v2 — Tier 1 Format Defect Batch (F1–F5) — REVISED
**Date:** 2026-04-27
**Architect:** Opus
**Builder:** Sonnet
**Repo:** mrx_engine_v1
**Branch:** main (or working branch — confirm via RULE-BRANCH-CHECK)
**Supersedes:** Tier 1 Format Defect Batch v1

## Why v2

Sonnet's recon caught two reversed assumptions in v1 of this spec:

- **F1** was directionally wrong: MB has 4 spaces after Q./A., we have 1. Fix is to PRESERVE the 4-space prefix, not remove it.
- **F4** was structurally wrong: the issue isn't wrap width. MB splits EXAMINATION BY MR. X: into two physical lines (header + byline). Ours emits it as one line. Fix is a structural split, not a wrap tweak.

Plus a test conflict on F3 (test_04_txt_lf_only) needs to be handled in the same PR.

Per RULE-FORMAT-CONSTANTS-VERIFY: every byte-level claim in this spec is sourced from Sonnet's 2026-04-27 recon report against `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt` and MB's FINAL.txt.

## Rules invoked

- RULE-BRANCH-CHECK
- RULE-RECON-FIRST (already complete; skip to build with Scott's go)
- RULE-CONTRADICTION-HUNT
- RULE-SILENT-FAILURE-CHECK
- RULE-DEPO-PRIME-DIRECTIVE
- RULE-INPUT-IS-SACRED
- RULE-FORMAT-CONSTANTS-VERIFY (draft)

## Truth sources (read-only; do NOT copy into engine code)

- MB's FINAL.txt — for byte-level verification
- halprin_mini.OUR_FINAL.txt — current v0.1 output
- corrected_turns.json — for turn data verification (turn 90 confirmed: paragraph_style='s7', text 'EXAMINATION BY MR. CAUGHEY:')
- Legacy reference: https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/legacy/format_final.py

---

## Defect specifications

### F1 — Q./A. spacing (REVISED)

**Reality:** MB has 4 spaces after Q. and A.. Our output has 1 space. The code defines `_QA_Q_PREFIX = "Q.    "` (4 spaces) but `_wrap_line()` tokenizes the prefix and `" ".join(tokens)` collapses the multi-space gap to single space.

**Files:** `src/stage5/page_layout.py`

**Fix:** Refactor `_wrap_line()` so the prefix is NOT tokenized. Prepend the prefix to the first physical line AFTER wrapping the body text. Compute `first_avail = content_width - indent - len(prefix)` so wrapped content fits correctly after the prefix.

**Test to add:** assert that the literal byte sequence `b"Q.    "` (Q dot four-spaces) appears at the expected column in the output for any QA_Q line. Same for A..

**Prime Directive check:** spacing change, no content change. ✓

---

### F2 — Line numbers mashed against indent=0 content (REVISED)

**Reality:** Cover lines and appearances lines both render with implicit `indent=0` because `_build_cover()` and `_build_appearances()` create `LogicalLine` objects without explicit indent values, and `LineKind.COVER` / `LineKind.APPEARANCES` aren't in `_KIND_TO_INDENT`. The format string `f"{line_num:>6}{pl.text}"` then produces `     8Division "H"` with no spacer.

**Files:** `src/stage5/document_composer.py`

**Fix:** In `_build_cover()` and `_build_appearances()`, set explicit indent values on every `LogicalLine` emitted. Reference values from legacy `build_caption()` and `format_appearances()`:

- Cover non-centered content (caption lines, Division "H" lines): `indent=8`
- Appearances body lines: `indent=4` (per legacy `wrap_line(f"    {line}", ...)`)
- Cover star separators (`* * *`): keep `CENTERED` kind handling
- `"Reported By:"` line on cover: `indent=2` per legacy

**Note:** Sonnet's recon flagged that this is a shared root cause with F5 — fix together in one pass.

**Test to add:** assert that for every `LineKind.COVER` and `LineKind.APPEARANCES` `LogicalLine` emitted by `_build_cover()` and `_build_appearances()`, the `indent` field is greater than 0.

**Prime Directive check:** indent change, no content change. ✓

---

### F3 — Line endings LF → CRLF (REVISED with test rename)

**Reality:** MB's FINAL is pure CRLF (16,200 CRLF, zero LF-only). Ours is pure LF (zero CRLF, 2,414 LF). Code at `src/stage5/assemble_final.py:119` explicitly sets `newline="\n"`.

**Files:**
- `src/stage5/assemble_final.py`
- `tests/stage5/test_assemble_final.py`

**Fix:**
1. Change `newline="\n"` to `newline="\r\n"` in `assemble_final.py:119`.
2. Rename test method `test_04_txt_lf_only` → `test_04_txt_crlf` and flip the assertion: instead of `assert b"\r\n" not in raw`, assert `b"\r\n" in raw` AND `\n` count equals `\r\n` count (no orphan LFs).
3. Leave `review_queue.json` and `stage5.summary.json` writes alone (JSON, no CRLF requirement).

**Note:** Per RULE-SILENT-FAILURE-CHECK, the existing test would have made this fix appear to "succeed" (code change merges) while a downstream assertion immediately reverts the assumption. The test rename is part of the same fix, not a separate task.

**Prime Directive check:** byte-level encoding, no content change. ✓

---

### F4 — BYLINE structural split (REVISED — opposite direction from v1)

**Reality:** Turn 90 (paragraph_style='s7', text `'EXAMINATION BY MR. CAUGHEY:'`) renders today as ONE physical line in our output. MB renders it as TWO physical lines:

```
EXAMINATION                       (centered, own line)

     5   BY MR. CAUGHEY:          (3-space indent, own line)
```

Turns 503 and 549 (also paragraph_style='s7') carry text `'BY MR. CAUGHEY:'` only — no EXAMINATION prefix. They're mid-deposition byline restarts after objections/breaks. They render fine today and need no change.

**Files:** `src/stage5/document_composer.py`

**Fix:** In the opening-byline emission path (`_BYLINE_OPEN_IDX` handling for turn 90), check if the turn's text starts with `"EXAMINATION "` (case-sensitive, including trailing space). If yes, emit TWO `LogicalLine`s:

1. `LogicalLine(text="EXAMINATION", kind=LineKind.CENTERED)`
2. `LogicalLine(text="BY MR. <NAME>:", kind=LineKind.BYLINE, indent=3)`

If the text does NOT start with `"EXAMINATION "`, emit a single BYLINE line as today (defensive — handles edge cases).

Apply this split logic ONLY to the opening byline path. Do NOT apply to the `byline_turn_idxs` set ({503, 549}); those turns must continue to emit single BYLINE lines.

**Verification data** (from Sonnet recon):

| idx | paragraph_style | text | Action |
|-----|-----------------|------|--------|
| 90  | s7 | `EXAMINATION BY MR. CAUGHEY:` | SPLIT into 2 lines |
| 503 | s7 | `BY MR. CAUGHEY:` | leave as-is |
| 549 | s7 | `BY MR. CAUGHEY:` | leave as-is |

**Tests to add:**
- Assert that for opening-byline turn (turn 90 in Halprin), the path emits exactly 2 `LogicalLine`s: the first with `kind=LineKind.CENTERED` and `text="EXAMINATION"`, the second with `kind=LineKind.BYLINE` and text starting with `"BY "`.
- Assert that for turns in `byline_turn_idxs` (503, 549), exactly 1 `LogicalLine` with `kind=LineKind.BYLINE` is emitted.

**Contradiction hunt (RULE-CONTRADICTION-HUNT):** grep entire codebase for `EXAMINATION` (case sensitive) and confirm no other path is asserting EXAMINATION should remain inline with BY MR. X:.

**Prime Directive check:** structural split is format-only, no content change. ✓ Most architecturally invasive of the 5 — build last per build order.

---

### F5 — Cover content not centered (REVISED — bundled with F2)

**Reality:** `_build_cover()` uses `_centered()` for some lines (STATE OF, PARISH OF, court, VIDEOTAPED DEPOSITION, OF, witness) but uses `_cover()` for others that should be centered per MB's format and per legacy `build_caption()`.

**Lines that currently use `_cover()` but should use `_centered()`:**
- `document_composer.py:202` — `"taken on"`
- `document_composer.py:203` — `dep["date_taken"]`
- `document_composer.py:204` — `f"commencing at {dep['time_started']}"`
- `document_composer.py:205` — `"at the offices of"`
- `document_composer.py:206` — `dep["location"]["firm"]`
- `document_composer.py:207` — `dep["location"]["address_line_1"]`
- `document_composer.py:208` — `dep["location"]["city_state"]`
- `document_composer.py:190, 197, 210` — `_STAR_SEP` lines

**Files:** `src/stage5/document_composer.py`

**Fix:** Change `_cover()` to `_centered()` for the lines listed above. Keep `Reported By:` as `_cover()` with explicit `indent=2` (per legacy — "Reported By:" is left-aligned with 2-space indent in MB's format, NOT centered).

**Note:** F2 + F5 share the same function (`_build_cover()`). Fix in one pass, one commit.

**Test to add:** assert that `_build_cover()` emits `CENTERED` `LineKind` for the location/date/venue lines and for star separators.

**Contradiction hunt:** grep `_cover(` and `_centered(` across `document_composer.py`. Confirm every cover line that should be centered uses `_centered()`.

**Prime Directive check:** centering only. Content unchanged. ✓

---

## Build sequence (after Scott says "go build")

One branch, one PR. Build in this order:

1. **F3** — line endings + test rename. Smallest blast radius. Get a green pipeline before touching anything else.
2. **F1** — Q./A. spacing tokenizer fix. Refactor `_wrap_line()` prefix handling.
3. **F2 + F5 together** — single pass through `_build_cover()` and `_build_appearances()`. Add explicit indents AND change `_cover()` to `_centered()` where needed.
4. **F4 last** — most architecturally invasive. Add the EXAMINATION-prefix split.

After EACH defect:
- Run full test suite. Baseline 491 → expected ≥ 491 + new tests for that defect, all green.
- Run real Halprin pipeline. Diff OUR_FINAL.txt against MB's FINAL on the specific area you fixed. Report bytes-changed count.

If any prior test breaks, STOP and report. Do not proceed to the next defect.

## Acceptance

Tier 1 v2 batch is done when:

- [ ] All 5 defects fixed per the revised specifications above
- [ ] `test_04_txt_lf_only` renamed and flipped to `test_04_txt_crlf`
- [ ] Full test suite green (≥ 491 + new tests, count reported)
- [ ] Real Halprin run produces OUR_FINAL.txt with all 5 visible improvements
- [ ] Byte-level diff against MB's FINAL on each of the 5 areas: each one matches MB byte-for-byte (excepting still-broken sections out of scope for this batch)
- [ ] One commit (or one PR) on main (or working branch — confirm before push)
- [ ] Brief PR/commit description listing each defect and the file/line changed

## Out of scope

- Tier 2 missing sections (index page, full appearances format, stipulation, certs, errata)
- Tier 3 structural work (FormatProfile, hardcoded turn ranges, s2 semantics)
- Module 6 hardcoded turn-range refactor
- Anything in `legacy/format_final.py` — reference only

## Rollback

`git revert <commit>` if anything goes sideways. No schema changes, no data migration.

## Note for tonight's handoff

The original handoff's "Visual Comparison Results" section had F1 and F4 directionally reversed. Calling this out in tonight's Opus handoff so the next architect knows to byte-verify before trusting visual notes. Per draft RULE-FORMAT-CONSTANTS-VERIFY.

— End of revised spec —
