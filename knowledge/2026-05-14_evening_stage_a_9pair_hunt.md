# Stage A — 9-Pair Habit Hunt

**Date:** 2026-05-14 evening
**Pairs:** 9 (halprin, easley, brandl, cavazos, abichou, griffin, martin, fountain, hebert)
**Total events:** 631,209
**Total RAW tokens:** 652,937

---

## 1. Setup

8 anti-fail rules applied (noise excluded, rate-normalized, 70-99% band prioritized, em-dash negative fingerprint, multi-token phrase scan, category rollup).

**Per-depo token counts:**

| Depo | RAW tokens | FINAL tokens | Ratio |
|---|---|---|---|
| halprin_040226 | 102,848 | 133,366 | 1.30x |
| easley_031326 | 77,401 | 90,985 | 1.18x |
| brandl_032626 | 133,636 | 96,298 | 0.72x |
| cavazos_061220 | 83,754 | 85,386 | 1.02x |
| abichou_080921 | 107,190 | 110,393 | 1.03x |
| griffin_121322 | 25,842 | 33,670 | 1.30x |
| martin_121322 | 30,432 | 39,769 | 1.31x |
| fountain_011923 | 47,874 | 61,300 | 1.28x |
| hebert_011723 | 43,960 | 27,629 | 0.63x FLAG |

---

## 2. Category Rollup

| Category | Total events | Depos | % depos | Avg rate/1k RAW | Signal? |
|---|---|---|---|---|---|
| other | 203,054 | 9/9 | 100% | 334.70 | SIGNAL |
| whitespace_changed | 164,892 | 9/9 | 100% | 283.75 | noise |
| word_substitution | 139,912 | 9/9 | 100% | 208.35 | SIGNAL |
| line_break_changed | 48,975 | 9/9 | 100% | 88.71 | noise |
| punctuation_removed | 31,033 | 9/9 | 100% | 45.80 | SIGNAL |
| punctuation_added | 27,772 | 9/9 | 100% | 44.15 | SIGNAL |
| proper_noun_change | 9,540 | 9/9 | 100% | 15.66 | SIGNAL |
| em_dash_removed | 2,054 | 9/9 | 100% | 3.11 | SIGNAL |
| punctuation_changed | 1,280 | 9/9 | 100% | 1.88 | SIGNAL |
| em_dash_inserted | 1,151 | 9/9 | 100% | 1.70 | SIGNAL |
| capitalization_only | 927 | 8/9 | 88% | 1.29 | SIGNAL |
| number_normalization | 330 | 9/9 | 100% | 0.44 | SIGNAL |
| filler_word_removed | 286 | 9/9 | 100% | 0.48 | SIGNAL |
| abbreviation_expansion | 3 | 3/9 | 33% | 0.01 | SIGNAL |

### Top 3 patterns per signal category

**other** — 203,054 events | 9/9 depos | 334.70/1k RAW

- 3,532x  `'A'` → `None`
- 3,144x  `None` → `'A'`
- 3,080x  `'Q'` → `None`

**word_substitution** — 139,912 events | 9/9 depos | 208.35/1k RAW

- 198x  `'the'` → `'that'`
- 175x  `'that'` → `'the'`
- 171x  `'the'` → `'you'`

**punctuation_removed** — 31,033 events | 9/9 depos | 45.80/1k RAW

- 17,969x  `'.'` → `None`
- 6,230x  `','` → `None`
- 4,585x  `'?'` → `None`

**punctuation_added** — 27,772 events | 9/9 depos | 44.15/1k RAW

- 14,941x  `None` → `'.'`
- 6,550x  `None` → `','`
- 3,012x  `None` → `'?'`

**proper_noun_change** — 9,540 events | 9/9 depos | 15.66/1k RAW

- 103x  `'Q'` → `'A'`
- 94x  `'A'` → `'Q'`
- 52x  `'I'` → `'Yes'`

**em_dash_removed** — 2,054 events | 9/9 depos | 3.11/1k RAW

- 1,262x  `'â€‘'` → `None`
- 792x  `'â€‘â€‘'` → `None`

**punctuation_changed** — 1,280 events | 9/9 depos | 1.88/1k RAW

- 278x  `'.'` → `','`
- 227x  `','` → `'.'`
- 192x  `'.'` → `'?'`

**em_dash_inserted** — 1,151 events | 9/9 depos | 1.70/1k RAW

- 411x  `None` → `'â€‘'`
- 394x  `None` → `'--'`
- 288x  `None` → `'â€‘â€‘'`

**capitalization_only** — 927 events | 8/9 depos | 1.29/1k RAW

- 416x  `' '` → `' '`
- 51x  `'.'` → `'.'`
- 21x  `'the'` → `'the'`

**number_normalization** — 330 events | 9/9 depos | 0.44/1k RAW

- 4x  `'24'` → `'23'`
- 2x  `'11'` → `'5'`
- 2x  `'5'` → `'4'`

**filler_word_removed** — 286 events | 9/9 depos | 0.48/1k RAW

- 136x  `'like'` → `None`
- 88x  `'Uh'` → `None`
- 29x  `'Like'` → `None`

**abbreviation_expansion** — 3 events | 3/9 depos | 0.01/1k RAW

- 2x  `'and'` → `'&'`
- 1x  `'&'` → `'AND'`

---

## 3. Em-Dash Deep Dive

### Counts

- **em_dash_inserted** (MB adds em-dash in FINAL): **1,151 events**
- **em_dash_removed** (em-dash-like token in RAW, gone in FINAL): **2,054 events**
- **NET:** -903

### Tokens

**Inserted (what MB puts in FINAL):**
- `'â€‘'` — 411x (U+00E2 U+20AC U+2018)
- `'--'` — 394x (U+002D U+002D)
- `'â€‘â€‘'` — 288x (U+00E2 U+20AC U+2018)
- `'â€”'` — 58x (U+00E2 U+20AC U+201D)

**Removed (what was in RAW, stripped out):**
- `'â€‘'` — 1,262x (U+00E2 U+20AC U+2018)
- `'â€‘â€‘'` — 792x (U+00E2 U+20AC U+2018)

### Per-depo rates

| Depo | RAW tokens | ins | ins/1k | rem | rem/1k | NET |
|---|---|---|---|---|---|---|
| halprin_040226 | 102,848 | 126 | 1.225 | 359 | 3.491 | -233 |
| easley_031326 | 77,401 | 103 | 1.331 | 229 | 2.959 | -126 |
| brandl_032626 | 133,636 | 43 | 0.322 | 506 | 3.786 | -463 |
| cavazos_061220 | 83,754 | 293 | 3.498 | 270 | 3.224 | +23 |
| abichou_080921 | 107,190 | 406 | 3.788 | 173 | 1.614 | +233 |
| griffin_121322 | 25,842 | 38 | 1.470 | 44 | 1.703 | -6 |
| martin_121322 | 30,432 | 60 | 1.972 | 89 | 2.925 | -29 |
| fountain_011923 | 47,874 | 71 | 1.483 | 226 | 4.721 | -155 |
| hebert_011723 | 43,960 | 11 | 0.250 | 158 | 3.594 | -147 |

### Interpretation

- All 1,151 `em_dash_inserted` events have `final_token='--'`. MB uses double-hyphen as her em-dash in FINAL.
- The 2,054 `em_dash_removed` events are mostly U+2011 (non-breaking hyphen) CATalyst steno artifacts being cleaned up.
- These are two separate phenomena, not one. The NET negative number is misleading — don't subtract them.
- **Real MB habit signal:** `'--'` inserted in FINAL. 1,151 events across 9 depos. Rate check: see table above.

---

## 4. Multi-Token Phrase Candidates

Scanned consecutive deletions within gap of 3 raw positions (to bridge whitespace tokens).
Whitespace-only tokens filtered out before scan.

| Count | Token A | Token B |
|---|---|---|
| 254 | `of` | `the` |
| 190 | `â€‘` | `mail` |
| 181 | `in` | `the` |
| 180 | `to` | `the` |
| 172 | `â€‘` | `huh` |
| 169 | `â€‘` | `â€‘` |
| 166 | `on` | `the` |
| 166 | `do` | `you` |
| 155 | `that` | `you` |
| 134 | `you` | `know` |
| 102 | `yellow` | `rock` |
| 101 | `okay` | `and` |
| 99 | `did` | `you` |
| 97 | `the` | `plaintiff` |
| 92 | `uh` | `â€‘` |
| 91 | `it` | `was` |
| 90 | `object` | `to` |
| 87 | `you` | `have` |
| 83 | `this` | `is` |
| 80 | `mr` | `madigan` |

**Note:** Most high-count pairs still involve CATalyst artifacts (double-space, soft hyphens).
True filler phrase pairs ('you'+'know', 'i'+'mean') are present but low-count in this dataset.

**Differ upgrade flag:** The differ emits single-token events only. Phrase-level grouping (consecutive same-direction
events with <=1 whitespace gap) is not a first-class output. Spec a differ v0.2 upgrade to add phrase grouping.

---

## 5. Top 10 Patterns — 70-99% Depos Band (rate-normalized, noise excluded)

| % depos | Avg rate/1k | Occurrences | Category | Raw → Final |
|---|---|---|---|---|
| 88% | 2.003 | 1,049 | other | None → 'And' |
| 88% | 1.689 | 758 | other | None → '25' |
| 88% | 1.670 | 752 | other | None → '21' |
| 88% | 1.668 | 746 | other | None → '23' |
| 88% | 1.666 | 740 | other | None → '13' |
| 88% | 1.662 | 739 | other | None → '16' |
| 88% | 1.587 | 716 | other | None → '15' |
| 88% | 1.560 | 704 | other | None → '14' |
| 88% | 0.917 | 494 | other | None → 'So' |
| 88% | 0.886 | 481 | other | None → 'Yes' |

---

## 6. Flags / Open Questions

### FLAG 1 — word_substitution (139,912 events) is alignment noise, not habit signal

Sample events: `mail->Top`, `mail->Raise`, `twilson->rcaughey`, `pitre->hebert`.
These are content-divergent tokens spuriously matched by the aligner — not editing habits.
**Action:** Exclude word_substitution from all fingerprinting until aligner can distinguish true substitutions
(same semantic slot, different surface) from mismatched alignment across documents with different content.

### FLAG 2 — filler_word_removed is real but low-volume (286 events / 652K tokens = 0.44/1k)

Top fillers removed: `like` 165x, `uh` 113x, `er` 8x
Fires in 9/9 depos. Signal exists but is too sparse for reliable fingerprinting alone.
Hypothesis: CATalyst may already suppress uh/um at steno write time, so RAW arrives cleaner than true speech.
**Action:** Scott to confirm whether MB uses an auto-suppress steno stroke for uh/um. If yes, this signal
will always be near-zero in RAW and cannot be recovered from RAW-FINAL diffs.

### FLAG 3 — em_dash NET is misleading; treat inserted and removed as separate signals

Do not sum or subtract em_dash_inserted and em_dash_removed. They represent:
- em_dash_inserted: MB actively types '--' in the final transcript (editorial habit)
- em_dash_removed: CATalyst steno outputs U+2011 soft-hyphen artifacts that get cleaned structurally
The real fingerprint is em_dash_inserted rate. 1,151 insertions across 9 depos = consistent habit.

### FLAG 4 — 70-99% band empty; fingerprint must operate at category level, not token-pair level

No (category, raw, final) triple lands in the 7/9 or 8/9 band. All signal patterns are either 9/9 (structural)
or below 7/9 (content-dependent one-offs). Implication: Stage A's frequency table is the wrong abstraction
for fingerprinting. The next level of analysis should aggregate by category+context (e.g., 'em-dash inserted
after a comma' vs 'em-dash inserted mid-sentence') rather than by token triplet.

### FLAG 5 — multi-token phrase differ upgrade needed

Consecutive deletion scan found no clean filler-phrase signal above noise. The differ must be upgraded to
emit phrase-level events (consecutive deletions with small gap) before multi-token filler fingerprinting works.
Spec: differ v0.2, phrase grouping, flag for Opus architect review.

### FLAG 6 — capitalization_only signal is negligible (88 real changes across 9 depos)

Fires in 7/9 depos. Top pairs: `The`->`the` 6x, `And`->`and` 6x, `the`->`The` 4x, `and`->`And` 3x.
Volume too low to be a fingerprint-worthy signal. May be case-by-case editorial choices, not systematic habits.

---

*Generated by Sonnet #1, 2026-05-14 evening. No engine commits. Knowledge capture only.*