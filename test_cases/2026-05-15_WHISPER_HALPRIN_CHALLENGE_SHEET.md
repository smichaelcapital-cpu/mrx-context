# WHISPER CHALLENGE SHEET — Halprin 040226 (v0)
**Date:** 2026-05-15
**Builder:** Sonnet #2 (Lane B, Tile B2.5)
**Status:** COMPLETE — ready for Opus review before Whisper runs
**DO NOT RUN WHISPER YET. This sheet is scored against Tile B3 output.**

---

## Section 1 — Purpose and Source Documents

**Purpose:** Give Whisper a known-answer test before we spend time or money running it. Instead of listening to the full 340-minute audio, we score Whisper against 25 defects we already know about from 5 weeks of Halprin work.

**Ground truth:** MB's FINAL transcript is the correct answer. Steno rough is the wrong version.

**Sources used:**

| Document | Path | What it contributed |
|---|---|---|
| Defect Inventory v1 | `reports/2026-05-04/defect_inventory_v1.md` | 738-block classified inventory, all sub-categories |
| Phonetic Error Spotcheck | `reports/2026-05-03/phonetic_error_spotcheck.md` | 28 phonetic blocks with turn_idx where available |
| Acronym Mangle Spotcheck | `reports/2026-05-04/acronym_mangle_spotcheck.md` | 17 acronym blocks with specific patterns |
| Pages 1-13 Diff | `audits/HALPRIN_PAGES_1_13_DIFF.md` | Exact page 13 defects with line numbers |
| Halprin FINAL compare | `io/halprin_FINAL_compare_2026-05-12.txt` | Full depo structure, page count confirmation |
| Audio file | `mrx_depo_library/MB/halprin_040226/input/040226yellowrock-ROUGH.opus` | 340 min, 76 MB |
| B1 Recon | `knowledge/2026-05-15_AUDIO_SYNC_RECON.md` | Audio duration confirmed 20,440 sec |

**Scott's approved caveats (2026-05-15):**

> **CAT-2 (ceremony language) — 0 rows.** Halprin's swearing-in was clean steno. This is not a gap in the sheet — it is a real signal. Clean ceremony language means audio will not help here because there is nothing to fix.

> **CAT-7 (em-dash) — 1 row.** Em-dash defects in Halprin are MB editorial additions, not audio events. MB adds em-dashes during proofread based on her judgment of hesitations and pauses. Whisper cannot produce em-dashes it was never trained to insert in this context. Low expectation of any CORRECT scores in this category. Not blocking the evaluation — informative for interpreting results.

**Timestamp estimation method (no per-stroke sync — B1 confirmed):**
- Total turns estimated: ~3,500 (evidence: block 690 at turn_idx 3381, ~50 pages remaining)
- Seconds per turn: 20,440 / 3,500 ≈ 5.8 sec/turn
- Formula: `turn_idx × 5.8 sec`
- For blocks without turn_idx: position estimated from block number ordering (block N ÷ 738 × 340 min)
- All position-based estimates marked `(pos-est)`. Turn-based estimates marked `(turn-est)`. Unknown = `UNKNOWN`.

---

## Section 2 — Eight Defect Categories

| # | Category Name | Plain Description | Spec Example |
|---|---|---|---|
| CAT-1 | HOMOPHONE_RESTATE | Wrong word that sounds like the right one. Witness restates or steno brief collision. | `permit address` → `permanent address` |
| CAT-2 | HOMOPHONE_CEREMONY | Homophone error in oath/ceremony language specifically. | `your sworn` → `you're sworn` |
| CAT-3 | ACRONYM_GARBLE | Steno brief for acronym or ampersand form translates to spelled-out words or wrong letters. | `with and T` → `W&T` |
| CAT-4 | PROPER_NOUN_SPLIT | Proper noun rendered as two separate words instead of one compound. | `lemon wood terrace` → `Lemonwood Terrace` |
| CAT-5 | PROPER_NOUN_CASE | Proper noun rendered lowercase or wrong capitalization. | `Warren seal` → `Warren Seal` |
| CAT-6 | COMPOUND_SPLIT | Compound word (with or without hyphen) rendered as two separate words. | `under paid` → `underpaid` |
| CAT-7 | EMDASH_MISSING | Self-correction or hesitation should have em-dash but steno omitted it. | `No no` → `No -- no` |
| CAT-8 | NUMBER_FORMAT | Number that should be spelled out is rendered as a digit, or wrong format. | `25 years ago` → `Twenty-five years ago` |

**Coverage note:** CAT-2 (ceremony language) has no confirmed instance in Halprin — the sworn-in section (page 13, lines 1-2) was clean in all diffs reviewed. CAT-2 row not included in v0. 7 of 8 categories covered.

---

## Section 3 — Challenge Rows (25 defects)

**Column definitions:**
- `defect_id`: unique row ID
- `category`: from the 8 families above
- `location`: page+line from MB FINAL or turn_idx if known; block # from defect inventory
- `steno_says`: wrong version verbatim from RAW (what audio model must improve on)
- `final_says`: correct version verbatim from MB FINAL (what we want Whisper to produce)
- `audio_ts_est`: estimated audio position in mm:ss
- `difficulty`: EASY / MEDIUM / HARD

| defect_id | category | location | steno_says | final_says | audio_ts_est | difficulty |
|---|---|---|---|---|---|---|
| HALPRIN_DEF_001 | CAT-4 | p.13 ln.14, block #6-region | `lemon wood terrace, Boynton Beach` | `Lemonwood Terrace, Boynton Beach` | ~00:30 (pos-est) | MEDIUM |
| HALPRIN_DEF_002 | CAT-1 | p.13 ln.16, block #6-region | `your permit address` | `your permanent address` | ~00:45 (pos-est) | MEDIUM |
| HALPRIN_DEF_003 | CAT-1 | p.13 ln.17, block #6-region | `my permission address` | `my permanent address` | ~00:50 (pos-est) | MEDIUM |
| HALPRIN_DEF_004 | CAT-8 | block #3, early testimony | `25 years ago` | `Twenty-five years ago` | ~01:24 (pos-est) | EASY |
| HALPRIN_DEF_005 | CAT-7 | block #8, early testimony | `Uhmm. I want to say I don't recall` | `Uhmm. I want to say -- I don't recall` | ~03:41 (pos-est) | HARD |
| HALPRIN_DEF_006 | CAT-3 | block #28, early testimony | `with and T` | `W&T` | ~12:54 (pos-est) | HARD |
| HALPRIN_DEF_007 | CAT-3 | block #34, early testimony | `He in P` | `E&P` | ~15:36 (pos-est) | HARD |
| HALPRIN_DEF_008 | CAT-3 | block #52, turn ~130 | `ENP` | `E&P` | ~23:56 (pos-est) | HARD |
| HALPRIN_DEF_009 | CAT-5 | block #47, turn 295 | `Marshall submit` | `Marshall Smith` | ~28:35 (turn-est) | HARD |
| HALPRIN_DEF_010 | CAT-6 | block #115, early-mid | `one field company` | `one-field company` | ~52:58 (pos-est) | EASY |
| HALPRIN_DEF_011 | CAT-4 | block #127, mid | `Storm Harbour Securities` | `StormHarbour Securities` | ~58:28 (pos-est) | MEDIUM |
| HALPRIN_DEF_012 | CAT-8 | block #165, mid | `Debt 6, 7 million` | `Debt six, 7 million` | ~01:15:57 (pos-est) | EASY |
| HALPRIN_DEF_013 | CAT-3 | block #178, mid | `good and good group` | `g&g group` | ~01:22:05 (pos-est) | HARD |
| HALPRIN_DEF_014 | CAT-5 | block #188, mid | `Come, credit on LE` | `Cole, C-o-l-e` | ~01:26:36 (pos-est) | HARD |
| HALPRIN_DEF_015 | CAT-1 | block #201, mid | `3000plus` | `3000+` | ~01:32:44 (pos-est) | MEDIUM |
| HALPRIN_DEF_016 | CAT-1 | block #207, mid | `seven ly didn't happen` | `certainly didn't happen` | ~01:35:24 (pos-est) | HARD |
| HALPRIN_DEF_017 | CAT-1 | block #250, mid | `Chris at perfect I man exploration` | `kris@perrymanexploration` | ~01:55:12 (pos-est) | HARD |
| HALPRIN_DEF_018 | CAT-6 | block #299, mid-late | `in person investor` | `in-person investor` | ~02:17:48 (pos-est) | EASY |
| HALPRIN_DEF_019 | CAT-8 | block #331, mid-late | `7, $8 million` | `seven, $8 million` | ~02:31:25 (pos-est) | EASY |
| HALPRIN_DEF_020 | CAT-5 | block #355, turn 1837 | `original Luminous loan` | `original Luminus loan` | ~02:58:23 (turn-est) | MEDIUM |
| HALPRIN_DEF_021 | CAT-1 | block #356, mid-late | `allegedly there was a 1031 drill` | `Eventually there was a 1031 well drilled` | ~02:44:00 (pos-est) | HARD |
| HALPRIN_DEF_022 | CAT-1 | block #457, late | `It ahold over from 2021` | `It's a holdover from 2021` | ~03:30:30 (pos-est) | HARD |
| HALPRIN_DEF_023 | CAT-1 | block #461, late | `I didn't know whose fault` | `I don't know whose fault` | ~03:32:24 (pos-est) | MEDIUM |
| HALPRIN_DEF_024 | CAT-5 | block #537, turn 2657 | `Fran Schneider` | `Fran Snyder` | ~04:17:51 (turn-est) | MEDIUM |
| HALPRIN_DEF_025 | CAT-1 | block #690, turn 3381 | `I'm hands go you what's been marked` | `I'm handing you what's been marked` | ~05:26:51 (turn-est) | HARD |

**Timestamp format note:** `mm:ss` for under 1 hour; `hh:mm:ss` for over 1 hour. All estimates are rough — Whisper returns its own timestamps on run, which will be authoritative. These estimates are only to help a human verify the right section.

---

## Section 4 — Difficulty Breakdown

| Difficulty | Count | Rows |
|---|---|---|
| EASY | 6 | DEF_004, DEF_010, DEF_012, DEF_018, DEF_019, DEF_023 |
| MEDIUM | 9 | DEF_001, DEF_002, DEF_003, DEF_008 (revised), DEF_011, DEF_015, DEF_020, DEF_024, — (see below) |
| HARD | 10 | DEF_005, DEF_006, DEF_007, DEF_009, DEF_013, DEF_014, DEF_016, DEF_017, DEF_021, DEF_022, DEF_025 |

**Corrected counts:**
- EASY: DEF_004, DEF_010, DEF_012, DEF_018, DEF_019 = **5 rows**
- MEDIUM: DEF_001, DEF_002, DEF_003, DEF_011, DEF_015, DEF_020, DEF_023, DEF_024 = **8 rows**
- HARD: DEF_005, DEF_006, DEF_007, DEF_008, DEF_009, DEF_013, DEF_014, DEF_016, DEF_017, DEF_021, DEF_022, DEF_025 = **12 rows**
- **Total: 25 rows**

**Category coverage:**

| Category | Row count | Notes |
|---|---|---|
| CAT-1 HOMOPHONE_RESTATE | 9 | DEF_002, 003, 015, 016, 017, 021, 022, 023, 025 |
| CAT-2 HOMOPHONE_CEREMONY | 0 | No confirmed instance in Halprin — ceremony pages were clean |
| CAT-3 ACRONYM_GARBLE | 4 | DEF_006, 007, 008, 013 |
| CAT-4 PROPER_NOUN_SPLIT | 2 | DEF_001, 011 |
| CAT-5 PROPER_NOUN_CASE | 4 | DEF_009, 014, 020, 024 |
| CAT-6 COMPOUND_SPLIT | 2 | DEF_010, 018 |
| CAT-7 EMDASH_MISSING | 1 | DEF_005 |
| CAT-8 NUMBER_FORMAT | 3 | DEF_004, 012, 019 |

**CAT-7 note:** Only 1 row because the ~30 doubled-token em-dash blocks in the inventory don't have individual block IDs in source docs. DEF_005 uses the one example cited directly. Recommend Scott or MB flag 2-3 more em-dash blocks by hand for v1 of this sheet.

---

## Section 5 — Scoring Method (Sonnet #2 Draft — Opus Reviews)

### How to Score After Whisper Runs (Tile B3)

For each of the 25 rows, find the Whisper transcript output at the estimated timestamp ± 30 seconds. Look for the target phrase.

**Per-row scoring:**

| Score code | Meaning |
|---|---|
| `CORRECT` | Whisper transcribed `final_says` (or close enough — within 1 word) |
| `STENO_MISS` | Whisper produced the same wrong phrase as `steno_says` — no improvement |
| `NEW_MISS` | Whisper produced something different from both steno and final — a new error |
| `PARTIAL` | Whisper got part of `final_says` right but not all |
| `SKIP` | Timestamp UNKNOWN, audio too unclear, or phrase not found in ± 30s window |

**Per-row data to record:**
1. Score code (above)
2. Whisper's actual transcript at that location (verbatim, ≤15 words)
3. Whisper confidence score (if the API returns word-level confidence)
4. Notes (background noise? multiple speakers? cut-off?)

### Roll-Up Metrics

After scoring all 25 rows:

```
% CORRECT        = CORRECT count / (25 - SKIP count) × 100
% STENO_MISS     = STENO_MISS count / (25 - SKIP count) × 100
% NEW_MISS       = NEW_MISS count / (25 - SKIP count) × 100
% PARTIAL        = PARTIAL count / (25 - SKIP count) × 100
```

Denominator excludes SKIP rows so the score reflects testable rows only.

**By-category breakdown:**
Compute CORRECT% for each of the 7 categories represented. This tells us which defect families Whisper helps (high CORRECT%) and which it doesn't (low CORRECT% or high STENO_MISS%).

**Interpretation guide for Opus:**

| Whisper score | Architecture signal |
|---|---|
| CORRECT ≥ 60% overall | Strong signal — Whisper meaningfully supplements steno |
| CORRECT ≥ 80% on CAT-3 (acronyms) | Whisper handles acronym context better than steno briefs |
| STENO_MISS ≥ 50% on CAT-1 (phonetics) | Whisper makes same phonetic errors as steno — limited uplift |
| NEW_MISS ≥ 25% overall | Whisper introduces new errors faster than it fixes known ones — caution |
| HARD rows CORRECT ≥ 40% | Whisper has meaningful reach into catastrophic garbles |
| HARD rows CORRECT < 20% | Whisper only helps easy cases — not the ones that matter most |

**What we're NOT measuring here:**
- Whisper's transcription of correct steno text (not the question — we assume it's fine)
- Whisper latency or cost (Tile B3 covers cost)
- Speaker diarization (separate evaluation)

---

*Generated by Sonnet #2, 2026-05-15. No engine commits. Test case data only.*
*Sources: defect_inventory_v1.md, phonetic_error_spotcheck.md, acronym_mangle_spotcheck.md, HALPRIN_PAGES_1_13_DIFF.md.*
*Scott reviews → Scott pushes to repo.*
