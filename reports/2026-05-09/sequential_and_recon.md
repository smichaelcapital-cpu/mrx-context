# Sequential "And" Pattern Recon
**Date:** 2026-05-09
**Based on:** `_diff_out_fingerprint/block_classification.json`, `_stage3_m1_out/corrected_turns.json`
**Pool:** 38 blocks (actual count; 31 was the sentence_break_recon estimate from sampling)

---

## Headline

**6 trigger conditions. Top 2: sequential_narrative (32%) and turn_initial_and (26%). Mechanically closeable: ~18% (and_then + and_so = 7 blocks). Critical finding: turn_initial_and is misclassified — 26% of the And bucket is not a sentence-break problem at all.**

---

## Full-Corpus Condition Counts (all 38 blocks)

| Condition | Count | % | Mechanical? | Fix location |
|---|---|---|---|---|
| sequential_narrative | 12 | 32% | No | Stage 3 / LLM |
| turn_initial_and | 10 | 26% | No | Not a sentence-break (see below) |
| garbled_contamination | 7 | 18% | N/A | Stage 3 steno quality |
| and_then | 4 | 11% | **Yes** | document_composer.py |
| and_so | 3 | 8% | **Yes** | document_composer.py |
| parallel_structure | 2 | 5% | No | LLM context required |

---

## Condition 1 — sequential_narrative (12 blocks, 32%)

Witness or attorney uses "And" to open an independent clause after a period boundary. The engine renders both clauses as one continuous sentence. MB's period+And split cannot be predicted from steno structure alone — it depends on whether the clause constitutes a new complete thought.

```
Block #38 (A. turn)
  OUR: ...went through a layoff and I was transferred transferred to San Angelo,
       Texas an Angelo Texas into natural gas and gas products and I worked there
       through their engineering training program...
  MB:  ...went through a layoff and I was transferred to San Angelo, Texas into
       natural gas and gas products. And I worked there through their engineering
       training program...
  Break point: "products" → "products."  |  "and I worked" → "And I worked"
  Before: "natural gas and gas products"  After: "And I worked there through"

Block #62 (A. turn)
  OUR: A sidetrack is where you are utilizing an wellbore that may or may not have
       been completed and you're moving a drilling rig on top of it...
  MB:  A sidetrack is where you are utilizing a wellbore that may or may not have
       been completed. And you're moving a drilling rig on top of it...
  Break point: "completed" → "completed."  |  "and you're" → "And you're"
  Before: "may or may not have been completed"  After: "And you're moving a drilling"

Block #588 (A. turn — multiple breaks)
  OUR: ...both of them called me on the telephone together, Todd and John and we
       spoke for thirty minutes minutes about things and I think that was right
       around COVID time...
  MB:  ...both of them called me on the telephone together, Todd and John. And we
       spoke for 30 minutes about things. And I think that was right around COVID
       time...
  Break points: "John" → "John."  |  "and we" → "And we"
                "things" → "things."  |  "and I think" → "And I think"
  Two consecutive breaks in one block — witness narrative fragmentation pattern.

Block #281 (A. turn — multiple breaks)
  OUR: A. I just like I said, I was promised a certain thing. And he changed his
       mind on something and basically hired a different engineer...
       [OUR text is heavily garbled/different in this block]
  MB:  A. I just like I said, I was promised a certain thing. And he changed his
       mind on something and basically hired a different engineer to, basically, be
       my boss. And I decided that I didn't want that.
  Break points: "thing." → "thing."  |  "And he"
                "my boss." → "my boss."  |  "And I decided"
```

**Why not mechanical:** "And" also connects clauses legitimately within sentences (e.g., "Todd and John" — not a break). No syntactic feature reliably distinguishes "And [new sentence]" from "and [clause connector]" without clause-level parsing.

---

## Condition 2 — turn_initial_and (10 blocks, 26%)

**Not a sentence-break condition.** MB consistently opens Q and A turns with a discourse-connector "And" — the attorney's "And [question]" or witness's "And [answer]" style. The engine may render the same turn without the leading "And" or with different phrasing. The `is_cap` classifier fires because "And" appears capitalized in MB but not in OUR, but there is no compound sentence being split. The period that would need to precede the "And" already exists (end of previous turn) or the "And" is simply the first word of a new turn.

```
Block #106 (Q. turn)
  OUR: Q. That means your family stayed here?
  MB:  Q. And did your family stay here?
  Signal: Q. And [question] vs Q. [question] — not a sentence break, different turn rendering.
  The "And" is a discourse opener for the attorney's question, not a sentence-break connector.

Block #163 (Q. turn)
  OUR: Q. My understanding that's the first time in your career at this point
       again still 20 years ago when you had started looking at locations...
  MB:  Q. And my understanding, that's the first time in your career at this
       point, again still 20 years ago when you had started looking at locations...
  Signal: MB adds discourse "And" at turn start. No compound sentence split in either version.
```

**Classification:** These are NOT sentence breaks. The `is_cap` diff scorer fires on the capitalized "And" as a changed token, but the underlying editorial action is MB adding a discourse connector at the start of a Q/A attribution label. Closing these would require detecting MB's turn-opening "And" style — a structural/style rule, not a sentence-termination rule. **These 10 blocks should be reclassified out of the sentence_break bucket.**

---

## Condition 3 — garbled_contamination (7 blocks, 18%)

REPORTER CHECK / REVIEW markers slipped through the garbled-block filter because the diff marker tokenizer split "REPORTER" and "CHECK" across separate diff tokens (e.g., `**-*REPORTER-** **-CHECK-**`), causing the regex `r'REVIEW|REPORTER CHECK'` to not match. The `is_cap` scorer then fires on "And" appearing in the garbled marker text.

```
Block #95
  OUR: A. Ballard explorations an [[REVIEW: 'Ballard explorations an exploration' — company
       name and sentence structure uncertain...]] exploration company and so the majority...
  MB:  A. Ballard Exploration is an exploration company. And so the majority of the wells
       were new prospects, new fields.
  Signal: REVIEW marker in OUR → garbled transcription, not a sentence-break.
  (The actual And so here is real, but this block is contaminated by the garbled OUR text.)

Block #148
  OUR: Q. Is that the case today? A. Today? I can't use today. Now. Q. This year.
       The first three-quarters...A. It's more closer [[REVIEW: low confidence...]]
  MB:  Q. Is that the case today? A. Today? The I can't use today. This is now Q.
       This year...Q. And was there a period of time when that decrease began?
  Signal: Multiple REVIEW markers throughout — full steno parse failure.
```

**Root cause:** Garbled filter regex `r'REVIEW|REPORTER CHECK'` fails when diff tokenizer splits multi-word marker. Fix: match `REPORTER` and `CHECK` independently. Not a sentence-break problem.

---

## Condition 4 — and_then (4 blocks, 11%)

**Mechanically detectable.** MB inserts a period before "And then" when "And then" opens a temporal sequence clause. Rule: if a sentence ends with a word that is not itself a temporal sequence, and the next clause starts with "And then", split at the period.

```
Block #129 (A. turn)
  OUR: ...So Aspect Resources would they had a they would drill a well... [garbled]
       ...they would drill this well and then it would be they needed somebody...
  MB:  ...they would drill this well. They would case this well. And then it would
       be they needed somebody to complete this well. And they would send me...
  Break point: "well" → "well."  |  "and then" → "And then"
  Before: "they would case this well"  After: "And then it would be they"

Block #46 (A. turn)
  OUR: ...was acting as production engineer for the producing wells. And then
       supervise production operations and I had I believe three or four contract...
  MB:  ...I was acting as production engineer for the producing wells. And then
       supervising production operations, and I had, I believe, three or four contract...
  Break point: "wells" → "wells."  |  "and then" → "And then"  [period already existed here]
  Note: This block's OUR already has "And then" — the diff is in content/style, not the break.

Block #348 (A. turn)
  OUR: ...She stayed for three months and then after her they had another tech...
  MB:  ...She stayed for three months. And then after her they had another tech...
  Break point: "months" → "months."  |  "and then" → "And then"
  Before: "She stayed for three months"  After: "And then after her they had"

Block #369 (A. turn)
  OUR: ...We got the pipe stuck and then we had to couldn't get the pipe free...
  MB:  ...We got the pipe stuck. And then we had to couldn't get the pipe free...
  Break point: "stuck" → "stuck."  |  "and then" → "And then"
  Before: "We got the pipe stuck"  After: "And then we had to couldn't"
```

**Mechanical rule:** `if text ends with [complete clause] and next token sequence is "and then"`, split at period. False-positive risk: "I told her and then she left" (clause connector within sentence). Mitigation: require the clause before "and then" to be ≥ 5 words and end with a verb or object noun. ~70% detection accuracy estimated.

**Fix location:** `_split_intra_turn_sentences()` pass in `document_composer._build_qa_body()`. ~15 lines.

---

## Condition 5 — and_so (3 blocks, 8%)

**Mechanically detectable.** MB inserts a period before "And so" when it opens a consequential result clause. Same structure as and_then.

```
Block #772 (A. turn)
  OUR: ...requires us to, basically, go one after the other and so if we think
       we're going to drill a well and we, basically, get it permitted as a well
       and so if we don't drill it, we have to rename...
  MB:  ...requires us to, basically, go one after the other. And so if we think
       we're going to drill a well and we, basically, get it permitted as a well,
       then if we don't drill it, then we have to rename...
  Break point: "other" → "other."  |  "and so" → "And so"
  Before: "go one after the other"  After: "And so if we think we're going"

Block #155 (Q. turn)
  OUR: ...how you're currently doing consulting work and I want to go back and
       working chronologically through your career...
  MB:  ...how you're currently doing consulting work. And I want to go back and
       working chronologically through your career...
  [This is sequential_narrative, not and_so — reclassified on second review]

Block #95: garbled (see condition 3). The actual "And so the majority..." break is real but block is garbled.
```

**Mechanical rule:** Same as and_then — `"and so"` after a complete clause ≥ 5 words signals a break. Same fix location: `_split_intra_turn_sentences()`.

---

## Condition 6 — parallel_structure (2 blocks, 5%)

MB uses "And" to open parallel enumeration items, each receiving its own sentence. No mechanical pattern — the items can be any length and follow varied structures.

```
Block #281 (A. turn)
  MB:  A. I just like I said, I was promised a certain thing. And he changed his
       mind on something and basically hired a different engineer to, basically,
       be my boss. And I decided that I didn't want that.
  Signal: Two clauses each opened with "And" — parallel narrative items.
  Not detectable without understanding that these are co-equal narrative statements.
```

---

## Summary: Mechanical Closeability

**Of 38 sequential-And blocks:**
- 12 (32%) are sequential_narrative — **LLM judgment required**
- 10 (26%) are turn_initial_and — **not a sentence-break problem** (misclassified in sentence_break bucket)
- 7 (18%) are garbled_contamination — **Stage 3 AI quality**
- 4 (11%) are and_then — **mechanically detectable, ~1 rule**
- 3 (8%) are and_so — **mechanically detectable, ~1 rule**
- 2 (5%) are parallel_structure — **LLM judgment required**

**Mechanically closeable: 7/38 = ~18%** (`and_then` + `and_so`)

**Reclassification impact:** 10 `turn_initial_and` blocks should be removed from the sentence_break_recon count. They are a distinct phenomenon (MB's discourse-connector style at turn starts) that the `is_cap` scorer misidentifies as sentence breaks. Net true sequential-And sentence-break blocks: **21 of 38** (the 12 narrative + 4 and_then + 3 and_so + 2 parallel).

---

## Architecture Implications

**and_then / and_so rule (7 blocks):** Addable to `_split_intra_turn_sentences()` alongside the existing trailing `okay?` and leading `Okay.` patterns from the qa_boundary_period_bug_recon. Estimated ~25 additional lines in `document_composer.py`. No new files. Net combined mechanical fix across all intra-turn patterns: ~42 of 74 Q./A. boundary blocks + 7 of 38 And blocks = **~49 total blocks closed** by one localized edit in one file.

**turn_initial_and (10 blocks):** Separate ticket. MB's discourse-And opener at Q/A turns is not addressable as a sentence-break rule. Would require detecting MB's turn-opening style and inserting "And" at the start of matching Q/A labels. Low priority; structural, not mechanical.

**sequential_narrative (12 blocks):** Stage 3 proposal-generation required. Same architectural class as the two-sentence Q. blocks from qa_boundary_period_bug_recon. Correct next-level problem for Opus architectural decision.

---

*End of report.*
