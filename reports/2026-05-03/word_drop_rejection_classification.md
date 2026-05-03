# Word-Drop Rejection Classification Report
**Date:** 2026-05-03
**Rule:** D-WRITER-WORD-DROP
**Source:** `_word_preservation_rejections.jsonl` — halprin_full Stage 3.1 run
**Purpose:** Knowledge accrual for Day-2 allow-heuristic design. No code changes.

---

## Summary

| Bucket | Name | Count | % |
|--------|------|-------|---|
| 1 | Category A — context-word leak | 160 | 82.5% |
| 2 | Phonetic correction | 19 | 9.8% |
| 3 | Steno fragment | 0 | 0.0% |
| 4 | Other / unclear | 15 | 7.7% |
| **Total** | | **194** | **100%** |

**Key finding:** 82.5% of rejections are confirmed Category A context-word leaks (the D-WRITER-WORD-DROP bug we hunted). The 19 phonetic corrections are the primary Day-2 candidate for an allow-heuristic. The 15 "other/unclear" items are listed in full at the bottom for Opus review.

---

## Classification Methodology

**Bucket 1 (context-word leak):** The non-dropped before-words have a consonant-skeleton that matches as a substring of the after-skeleton — confirming a steno compound was present in the span and the dropped word was a real-word context leak (one-position-too-wide bug).

**Bucket 2 (phonetic correction):** The dropped word has a skeleton-prefix match OR is in a hand-validated phonetic-pairs list against at least one after-word. These are mis-transcriptions the Writer was correctly fixing, not context leaks.

**Bucket 3 (steno fragment):** The dropped "word" is 1–2 non-English characters or an all-consonant token with ≤3 chars. Count: 0 — the 50% majority threshold already filtered most fragments (they produce 0% match ratios, falling below the threshold).

**Bucket 4 (other/unclear):** Catch-all. Full list below.

---

## Bucket 2 — Phonetic Corrections (all 19, with SAFE/RISKY assessment)

For Day-2 design: could an allow-heuristic safely pass these through?

| Turn | before | after | dropped | Assessment |
|------|--------|-------|---------|------------|
| 124 | `"I no one of them was Warren seal."` | `"I know one of them was Warren Seal"` | `['no']` | **SAFE** — "no"→"know", same phoneme, obvious correction |
| 295 | `"Marshall submit."` | `"Marshall Smith"` | `['submit']` | **SAFE** — "submit" is steno for proper name "Smith" |
| 343 | `"oil and gassy"` | `"oil and gas"` | `['gassy']` | **SAFE** — "gassy" is steno artifact for "gas", oil/gas context unambiguous |
| 360 | `"your personally"` | `"you personally"` | `['your']` | **SAFE** — possessive→pronoun form correction, meaning preserved |
| 584 | `"Least operating"` | `"Lease operating statements"` | `['least']` | **SAFE** — "Least"→"Lease", well-known term, context confirms |
| 681 | `"seized doing"` | `"ceased doing"` | `['seized']` | **SAFE** — "seized"→"ceased", context "North Summit ceased doing business" confirms |
| 699 | `"Revenant Signal"` | `"Revenant Group"` | `['signal']` | **RISKY** — "Signal"→"Group" is a name/entity correction; "Revenant Signal" vs "Revenant Group" could be different entities; requires MB confirmation |
| 1278 | `"Face two"` | `"Phase two"` | `['face']` | **SAFE** — "Face"→"Phase", legal/procedural context, "Phase Two" standard terminology |
| 1463 | `"bring hip"` | `"bring him back"` | `['hip']` | **SAFE** — "hip"→"him", pronoun steno collision |
| 1584 | `"get become to"` | `"get back to"` | `['become']` | **SAFE** — "become"→"back", fixed phrase "get back to", no ambiguity |
| 2068 | `"Signature majority."` | `"Significant majority"` | `['signature']` | **SAFE** — "Signature"→"Significant", fixed phrase "significant majority" |
| 2070 | `"Signature majority"` | `"significant majority"` | `['signature']` | **SAFE** — duplicate of above |
| 2174 | `"water singing into"` | `"water seeping into"` | `['singing']` | **SAFE** — "singing"→"seeping", geological context confirms water seeping |
| 2330 | `"a reasons"` | `"a reason"` | `['reasons']` | **SAFE** — plural→singular normalization, meaning unchanged |
| 2770 | `"big different"` | `"a big difference between"` | `['different']` | **SAFE** — "different"→"difference", adjective→noun correction |
| 3381 | `"I'm hands go you what's"` | `"I'm handing you what's been marked"` | `['hands', 'go']` | **SAFE** — "hands go"→"handing", steno run-together corrected |
| 3392 | `"through keep"` | `"to keep"` | `['through']` | **SAFE** — "through"→"to", preposition steno collision, fixed phrase |
| 3517 | `"opposite and geo category."` | `"operations and geo"` | `['opposite', 'category']` | **RISKY** — "opposite"→"operations" is a significant semantic change; if wrong, meaning inverted; requires MB confirmation |
| 3525 | `"terminology opposite and geo"` | `"operations and geo category"` | `['terminology', 'opposite']` | **RISKY** — same as t3517; "opposite"→"operations" and "terminology" dropped |

**B2 summary: 16 SAFE, 3 RISKY**
The 3 RISKY cases (t699, t3517, t3525) involve entity-name substitutions or semantic inversions where an incorrect phonetic correction would change meaning. These should remain in the reject list even after a Day-2 heuristic is implemented.

**Day-2 signal:** A conservative phonetic-correction heuristic covering the 16 SAFE cases would reduce the reject count from 194 → ~178 (−16 rejections, ~8% reduction). This is modest — the remaining 160 B1 context-word leaks need a separate strategy.

---

## Bucket 1 — Context-Word Leaks (first 20 of 160)

These are the D-WRITER-WORD-DROP bug in its canonical form. The Writer's token span is one position too wide; the steno compound at the right end of the span decompacts cleanly, but the context word at the left end is lost.

| Turn | before | after | dropped |
|------|--------|-------|---------|
| 99 | `"flew into give"` | `"in to give"` | `['flew']` |
| 108 | `"of oil oil"` | `"oil -- oil barrels"` | `['of']` |
| 114 | `"being under paid"` | `"underpaid"` | `['being']` |
| 131 | `"that your"` | `"you're"` | `['that']` |
| 152 | `"professional certification"` | `"certifications"` | `['professional']` |
| 156 | `"You don't you have"` | `"But you have"` | `['dont']` |
| 167 | `"certification is"` | `"certifications"` | `['is']` |
| 181 | `"in mid1980's."` | `"mid-1980s"` | `['in']` |
| 214 | `"joined Somerset production company,"` | `"Somerset Production Company"` | `['joined']` |
| 232 | `"I we"` | `"I --"` | `['we']` |
| 240 | `"a mat er of"` | `"a matter of"` | `['er']` |
| 247 | `"called trek oil and"` | `"Trek Oil and Gas"` | `['called']` |
| 258 | `"also there CFO."` | `"their CFO"` | `['also']` |
| 343 | `"paying Bill's"` | `"bills"` | `['paying']` |
| 350 | `"want too fast forward"` | `"to fast-forward"` | `['want', 'too']` |
| 382 | `"are you can paid"` | `"are you paid"` | `['can']` |
| 390 | `"What so"` | `"What \ufffd"` | `['so']` |
| 399 | `"the a lot"` | `"handle a lot"` | `['the']` |
| 435 | `"are he they"` | `"are they"` | `['he']` |
| 439 | `"Love an the"` | `"Mr. Love and the field guys"` | `['an']` |

*(140 more B1 entries omitted — full list in `_word_preservation_rejections.jsonl`)*

---

## Bucket 4 — Other / Unclear (all 15, verbatim)

Listed verbatim for Opus review. These do not fit cleanly into any of the three spec buckets.

| Turn | before | after | dropped | Notes |
|------|--------|-------|---------|-------|
| 108 | `"of oil oil"` | `"oil -- oil barrels"` | `['of']` | Inserted content (barrels) not present in before; structural rewrite |
| 232 | `"I we"` | `"I --"` | `['we']` | "we" dropped, dash inserted; steno hesitation mark? |
| 823 | `"5 or"` | `"five"` | `['or']` | Number + conjunction → just number; "or" is context |
| 823 | `"6 investors."` | `"six"` | `['investors']` | Number + noun → just number; "investors" semantically present but dropped |
| 1034 | `"that 20172018"` | `"2017-2018"` | `['that']` | Year-range compound: context word "that" leaked |
| 1156 | `"than 70"` | `"seventy wells"` | `['than']` | Number context: "than" is a comparison word, dropped during number normalization |
| 1161 | `"the 20172018,"` | `"2017-2018"` | `['the']` | Year-range compound: context word "the" leaked (same pattern as t1034) |
| 1367 | `"first 3 or 4 wells,"` | `"three or four"` | `['first', 'wells']` | Number normalization dropped "first" and "wells" — content words |
| 1407 | `"an we"` | `"and we"` | `['an']` | "an"→"and" correction; "an" is a steno artifact for "and" |
| 1825 | `"an a"` | `"a"` | `['an']` | Duplicate article: "an a" → "a"; redundant article dropped |
| 1965 | `"than 2"` | `"two"` | `['than']` | Same as t1156: comparison word dropped during number normalization |
| 1995 | `"in 20172018,"` | `"2017-2018"` | `['in']` | Year-range compound: context word "in" leaked (same pattern as t1034, t1161) |
| 2606 | `"70 percent"` | `"seventy"` | `['percent']` | "percent" dropped when normalizing "70"→"seventy"; unit word lost |
| 3095 | `"say 30."` | `"thirty"` | `['say']` | Verbal filler "say" (as in "say, thirty") dropped; may be intentional |
| 3095 | `"be 30"` | `"thirty"` | `['be']` | Similar; "be" as in "could be 30" context word |

**Patterns visible in B4:**
- **Year-range compounds** (t1034, t1161, t1995): 3 cases of "X 20172018" → "2017-2018". The year range is treated as a steno compound; the preposition/determiner before it is a context leak. These are arguably B1 (context-word leak) but the classifier couldn't detect the year-compound.
- **Number normalization with unit** (t1156, t1367, t1965, t2606, t3095): number context words ("than", "percent", "first", "say", "be") dropped during digit→word conversion. Judgment call: "percent" and "wells" dropping is a semantic concern; "than/say/be" dropping is less critical.
- **Article/conjunction steno artifacts** (t1407, t1825): "an"→"and" correction and duplicate-article cleanup. Arguably B2 (phonetic: "an"≈"and") or B3 (steno fragment).

---

## Day-2 Design Notes

**Highest-leverage target:** The 160 B1 context-word leaks. These require a fix to the token-span selection in the Writer prompt (or a post-hoc heuristic that detects the `[context_word] [steno_compound]` pattern and allows the drop). The pattern is: one real word before a steno compound, and the real word has no skeleton match in the after text.

**Low-risk quick win:** The 16 SAFE B2 phonetic corrections could be added to `EXPECTED_DROP` (or a phonetic-allow heuristic) with minimal risk. Each has an unambiguous steno-word → correct-word mapping.

**Do not allow:** t699 (Revenant Signal→Group), t3517, t3525 (opposite→operations) without MB explicit confirmation. Meaning-changing substitutions are not safe to allow automatically.

**B4 year-range cases:** The three "X 20172018" → "2017-2018" cases with context word leaks (t1034, t1161, t1995) should probably be reclassified as B1 and treated identically to the steno-compound context leaks. Low priority.

---

*Classification algorithm: Python heuristic using consonant-skeleton decompaction (T9 pattern) + phonetic-pairs hand-list. Source: `_word_preservation_rejections.jsonl`, 194 records. Run: 2026-05-03.*
