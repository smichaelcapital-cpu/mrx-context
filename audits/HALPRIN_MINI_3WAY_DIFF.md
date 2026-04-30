# Halprin Mini — Three-Way Diff (RAW vs OURS vs MB)

**Date:** 2026-04-29
**Scope:** Pages 13-54 of OURS vs same range of MB
**RAW source:** `io/analysis/halprin_mini/_pipeline_out/halprin_mini.stage1.turns.json`
**OURS source:** `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt`
**MB source:** `oracle/finals/halprin/040226yellowrock-FINAL.txt`, pages 13-49 (body) + pages 296-300 (back matter)

> **RAW note:** Stage 1 turns are not line-aligned to OURS pages. RAW column shows the relevant stage1 turn text where identifiable; shows `(cascade)` for lines that differ only due to upstream wrapping effects.

**Headline numbers:**
- Total diff lines (pages 13-54): **1,027**
- Pages 1-12: **0 diffs** (all literal template — proven clean)
- Pages with zero diffs (13-54): **none** (all body pages have at least one diff)
- Most common pattern: **content/correction divergence** (875 lines)

---

## PATTERN SUMMARY

| Pattern | Count | Recommendation |
|---------|-------|---------------|
| Content / correction divergence | 875 | ASK SCOTT |
| Back matter (synthetic vs real) | 145 | TIER 2 LATER |
| Double-space after period | 6 | FIX |
| EXAMINATION indentation | 1 | FIX |
| **Total** | **1,027** | |

---

## PATTERN 1: Content / Correction Divergence (875 lines)

**Root cause:** Two sub-issues tightly intertwined:

**1a. Uncorrected steno artifacts** — Stage 3.1 LLM did not catch these errors. MB's manual corrections differ from ours (or we made no correction at all).

**1b. Wrapping cascade** — Once a line has different content (longer or shorter than MB's), all subsequent lines on that page wrap at different word boundaries. This makes downstream lines look like diffs even when the underlying words are the same. A single uncorrected steno artifact can cause 10-20 downstream diff lines per page.

### Key steno artifacts identified (RAW → OURS → MB):

| Page | Line | RAW (stage1) | OURS | MB | Notes |
|------|------|-------------|------|-----|-------|
| 14 | 11 | `with and T offshore` | `with and T offshore.` | `W&T Offshore.` | Company name garbled |
| 14 | 12 | `with and T` | `with and T` | `W&T` | Same artifact, 2nd occurrence |
| 14 | 16 | `with and T` | `with and T` | `W&T` | Same artifact, 3rd occurrence |
| 13 | 14 | `lemon wood terrace` | `lemon wood terrace` | `Lemonwood Terrace` | Proper noun, split |
| 13 | 16 | `permit address` | `permit address` | `permanent address` | Word corruption |
| 13 | 17 | `permission address` | `permission address` | `permanent address` | Same turn, restated |
| 13 | 18 | `flew into give testimony` | `flew into give testimony` | `flew in to give testimony` | Word swap |
| 13 | 23 | `25 years ago` | `25 years ago` | `Twenty-five years ago` | Number format |
| 14 | 18 | `under paid` | `under paid` | `underpaid` | Compound word |
| 14 | 24 | `No no` | `No no` | `No -- no` | Missing em-dash |
| 15 | 8 | `Warren seal` | `Warren seal` | `Warren Seal` | Proper noun capitalization |
| 15 | 7 | `Uhmm, I want to say` | `Uhmm, I want to say` | `Uhmm.  I want to say --` | Missing period + em-dash |
| 15 | 15 | `should have come out versus` | `should have come out versus` | `should have come out -- should...` | Missing em-dash |
| 15 | 22 | `your sworn un-` | `your sworn under oath` | `you're sworn` | `your` vs `you're` |

### Sample diffs (pages 13-16, first body pages):

| Page | Line | OURS | MB |
|------|------|------|-----|
| 13 | 4 | `                      EXAMINATION` | `   EXAMINATION` |
| 13 | 6 | `...Good morning, sir. My name is...` | `...Good morning, sir.  My name is...` |
| 13 | 9 | `...Houston. It's good to meet you.` | `...Houston.  It's good to meet you.` |
| 13 | 14 | `...9757 lemon wood terrace, Boynton...` | `...9757 Lemonwood Terrace, Boynton...` |
| 13 | 16 | `...your permit address?` | `...your permanent address?` |
| 13 | 17 | `...That is my permission address.` | `...That is my permanent address.` |
| 13 | 23 | `...25 years ago potentially. It was...` | `...Twenty-five years ago potentially....` |
| 14 | 5 | `   oil barrels being paid to one of...` | `   -- oil barrels being paid to one...` |
| 14 | 10 | `...Somerset and it went back to do...` | `...Somerset and I went back to do...` |
| 14 | 11 | `...a deposition for with and T offshore.` | `...a deposition for W&T Offshore.` |
| 14 | 18 | `...being under paid for the volume...` | `...being underpaid for the volume...` |
| 14 | 24 | `...No no, yes, I have one time.` | `...No -- no, yes, I have one time.` |
| 15 | 1 | `...1980's being late 80's potentially.` | `...1980's, late 80's potentially.` |
| 15 | 7 | `...Uhmm, I want to say I don't recall.` | `...Uhmm.  I want to say -- I don't recall.` |
| 15 | 8 | `...one of them was Warren seal. And...` | `...I know one of them was Warren Seal.  And...` |
| 15 | 15 | `...should have come out versus what...` | `...should have come out -- should have come...` |
| 15 | 22 | `...your sworn under oath...` | `...you're sworn under oath...` |
| 16 | 1 | `...I don't you've done this before so not...` | `...I don't -- you've done this before,...` |
| 16 | 7 | `        A.    Yes, sir.` | `              Does that work?` |

> **Note:** By page 16 line 7, OURS and MB are no longer on the same Q&A (complete page drift). The content at the same page/line is a completely different speaker turn.

---

## PATTERN 2: Back Matter — Synthetic vs Real (145 lines)

OURS pages 50-54 contain synthetic content (built from `case_info.json`). MB's pages 296-300 contain the actual signed certificates.

**Sub-patterns:**
- Reporter's Certificate: boilerplate text matches in structure but exact wording differs
- Witness's Certificate: blank checkboxes vs MB's filled form
- Errata Sheet: generic template vs actual errata entries (if any)
- Signature lines: underscores vs actual signatures/dates

**Recommendation:** TIER 2 LATER — synthetic back matter is expected at this stage; real back matter requires post-deposition data not available at render time.

---

## PATTERN 3: Double-Space After Period (6 lines)

CaseCATalyst auto-inserts two spaces after sentence-ending periods. Our pipeline doesn't.

**Count:** 6 occurrences (likely more are hidden inside the content/cascade diffs)

**Examples:**

| Page | Line | OURS | MB |
|------|------|------|-----|
| 13 | 6 | `...sir. My name is Ryan...` | `...sir.  My name is Ryan...` |
| 13 | 7 | `...minutes ago. I represent...` | `...minutes ago.  I represent...` |
| 13 | 8 | `...this case. I'm in from...` | `...this case.  I'm in from...` |
| 13 | 9 | `...meet you.` | `...meet you.` |

**Recommendation:** FIX — apply double-space-after-period post-processing pass to all Q/A/COLLOQUY lines in Stage 5. This is a systemic issue affecting all body content.

---

## PATTERN 4: EXAMINATION Indentation (1 line)

OURS centers `EXAMINATION` in the 55-char content area (using `LineKind.CENTERED`). MB uses 3-space left-indent (same as `BYLINE`).

| Page | Line | OURS | MB |
|------|------|------|-----|
| 13 | 4 | `                      EXAMINATION                      ` | `   EXAMINATION` |

**Recommendation:** FIX — emit `EXAMINATION` as `LineKind.BYLINE` with indent=3, not `LineKind.CENTERED`. Change in `document_composer.py` section 5.5.

---

## PAGE DRIFT ANALYSIS

OURS and MB diverge at **page 13, line 6** (first Q&A line). The divergence is caused by:

1. **Immediate causes** (pages 13-15): Uncorrected steno artifacts that produce different word counts per line
2. **Cascade effect** (pages 15+): Wrapping differences from upstream errors cause all downstream lines on each page to be at different word positions
3. **Complete drift** (page 16+): OURS and MB are on different Q&A turns at the same page/line

The 875 "content" diffs are NOT 875 independent corrections needed. The actual root corrections needed are approximately **15-20 distinct steno artifacts** (listed in Pattern 1 above). Fixing those would collapse the cascade and dramatically reduce the diff count.

**Key uncorrected steno artifacts to fix:**
1. `"with and T"` → `"W&T"` (company name — highest priority, appears 3+ times)
2. `"lemon wood terrace"` → `"Lemonwood Terrace"` (address)
3. `"permit address"` / `"permission address"` → `"permanent address"` (x2)
4. `"flew into give testimony"` → `"flew in to give testimony"`
5. `"25 years ago"` → `"Twenty-five years ago"` (number format)
6. `"Warren seal"` → `"Warren Seal"` (proper noun)
7. `"under paid"` → `"underpaid"`
8. Missing em-dashes (`--`) — MB uses `--` where OURS has none (5-10 occurrences)
9. `"your"` → `"you're"` (one occurrence visible in first 15 pages)

---

## RECOMMENDATION SUMMARY

| Pattern | Count | Action |
|---------|-------|--------|
| EXAMINATION indent | 1 | **FIX** — change LineKind.CENTERED → BYLINE(indent=3) in document_composer.py |
| Double-space after period | ~30+ | **FIX** — add post-processing pass in Stage 5 layout |
| Uncorrected steno artifacts | ~15-20 root | **ASK SCOTT** — manual review queue? Or retrain Stage 3.1 with better prompts? |
| Wrapping cascade | ~850 | **AUTO-RESOLVES** once steno artifacts are fixed |
| Back matter | 145 | **TIER 2 LATER** — needs post-deposition data |

---

*Generated 2026-04-29 by audit script. Pages 1-12 excluded (proven clean). Pages 13-54 compared against MB oracle pages 13-49 + 296-300.*
