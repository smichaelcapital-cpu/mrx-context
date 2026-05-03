# Phonetic Error Spot-Check — Halprin Full Depo
**Date:** 2026-05-03 evening session
**Analyst:** Claude Sonnet (mrx-context session)
**Scope:** All 28 Bucket A blocks classified `sub == "phonetic_error"`
**Method:** Manual classification against MB reference + word_preservation rejection cross-reference

---

## Summary Counts

| Bucket | Count |
|--------|-------|
| READER_MISSED_IT | 15 |
| VALIDATOR_BLOCKED | 5 |
| READER_FLAGGED_WRITER_WRONG | 2 |
| UNCLEAR | 5 |
| MB_EDITORIAL | 1 |
| **Total** | **28** |

---

## Severity Distribution

| Bucket | HIGH | MEDIUM | LOW |
|--------|------|--------|-----|
| READER_MISSED_IT | 7 | 2 | 6 |
| VALIDATOR_BLOCKED | 5 | 0 | 0 |
| READER_FLAGGED_WRITER_WRONG | 2 | 0 | 0 |
| UNCLEAR | 0 | 1 | 4 |
| MB_EDITORIAL | 0 | 0 | 1 |

**9 HIGH severity blocks are engine bugs with no fix landing.**

---

## All 28 Blocks

### Block 6 — VALIDATOR_BLOCKED / HIGH
```
MB:  "being underpaid"
OUR: "being under paid"
```
Reader identified `under paid` → `underpaid` but set span to `"being under paid"`.
Validator rejected: dropped word `being`.
Root cause: span too wide (same class as D-READER-COMPOUND-SPAN).
Rejection record: turn=114 p_0010.

---

### Block 19 — READER_MISSED_IT / HIGH
```
MB:  "any other degrees,"
OUR: "any degree"
```
Steno compressed "other degrees" to "degree" (dropped "other", changed number).
Reader produced no proposal. Complete miss.

---

### Block 47 — VALIDATOR_BLOCKED / HIGH
```
MB:  "Marshall Smith."
OUR: "Marshall submit."
```
`submit` is a phonetic garble of `Smith` (steno artifact). Reader correctly flagged
`Marshall submit.` → `Marshall Smith` but span included `Marshall`.
Validator rejected: dropped word `submit` (cannot find it in `Smith`).
Rejection record: turn=295 p_0006.
Note: the fix was semantically correct — blocked by span width, not logic.

---

### Block 72 — READER_MISSED_IT / MEDIUM
```
MB:  "All right." ... "Love's"
OUR: "Okay."   ... "loves"
```
Two differences: "Okay" → "All right" (MB_EDITORIAL); "loves" → "Love's" (Reader
missed proper-noun possessive — `Love's` is the witness surname with possessive).

---

### Block 91 — READER_MISSED_IT / HIGH
```
MB:  "why don't you explain"
OUR: "judge don't you explain"
```
`judge` is a phonetic garble of `why` — completely different word, high WER.
Secondary difference: `field based` → `field-based` (hyphenation, LOW severity).
Reader produced no proposal for `judge`.

---

### Block 115 — READER_MISSED_IT / LOW
```
MB:  "one-field company"
OUR: "one field company"
```
Missing hyphen in compound modifier. Reader missed it.

---

### Block 127 — READER_MISSED_IT / MEDIUM
```
MB:  "\"StormHarbour Securities"
OUR: "\"Storm Harbour Securities"
```
`StormHarbour` is a proper noun (company name) that should be one word.
Steno wrote it as two. Reader did not flag.

---

### Block 201 — READER_MISSED_IT / HIGH
```
MB:  "3000+"  ... "(Court Reporter clarification.)"
OUR: "3000plus"
```
`3000plus` should be `3000+` (phonetic "plus" not expanded to symbol).
MB also includes a court reporter clarification parenthetical entirely absent from our output.
Reader missed both.

---

### Block 207 — READER_MISSED_IT / HIGH
```
MB:  "certainly didn't happen"
OUR: "seven ly didn't happen"
```
`seven ly` is a catastrophic phonetic garble of `certainly`. Completely different words.
Reader produced no proposal. This is one of the highest-severity misses in the dataset.

---

### Block 250 — READER_MISSED_IT / HIGH
```
MB:  "kris@perrymanexploration,"
OUR: "Chris at perfect I man exploration,"
```
Email address `kris@perrymanexploration` was phonetically transcribed as spoken words.
Reader did not recognize this as an email address or flag the garble.

---

### Block 255 — UNCLEAR / LOW
```
MB:  "signature."  (Witness peruses document.)
OUR: "signature?"
```
`signature?` → `signature.` is punctuation (? vs .). Missing parenthetical stage direction.
Neither difference is clearly a Reader failure vs. a missing input source.

---

### Block 256 — VALIDATOR_BLOCKED / HIGH
```
MB:  "communication is all about"
OUR: "communications all"
```
`communications` is a phonetic merge of `communication is`. Reader correctly proposed fix
but span included `this` before the token. Validator rejected: dropped `this`.
Rejection record: turn=1351 p_0002.

---

### Block 299 — READER_MISSED_IT / LOW
```
MB:  "in-person investor"
OUR: "in person investor"
```
Missing hyphen in compound modifier. Reader missed it.

---

### Block 355 — VALIDATOR_BLOCKED / HIGH
```
MB:  "original Luminus loan"
OUR: "original Luminous loan"
```
`Luminous` → `Luminus` (correct company name). Reader included `original` in span.
Validator rejected: dropped `original`. Rejection record: turn=1837 p_0004.
Secondary differences in same block: `becoming` → `coming`, `itself` → `its` — also missed.

---

### Block 356 — READER_MISSED_IT / HIGH
```
MB:  "this.  Eventually there was a 1031 well drilled?"
OUR: "allegedly there was a 1031 drill?"
```
`allegedly` is a garble of `Eventually` (and context is wrong — "this. Eventually").
Missing word `well`. Spurious `Q.` inserted in our output.
Reader produced no proposals for these errors.

---

### Block 457 — READER_MISSED_IT / HIGH
```
MB:  "It's a holdover from 2021"
OUR: "It ahold over from 2021"
```
`It ahold over` is a phonetic decompaction failure for `It's a holdover`.
Reader did not flag.

---

### Block 461 — READER_MISSED_IT / LOW
```
MB:  "I don't know whose fault"
OUR: "I didn't know whose fault"
```
`didn't` vs `don't` — subtle tense difference. Steno may have phonetically written
the wrong contraction. Reader missed it.

---

### Block 499 — READER_MISSED_IT / LOW
```
MB:  "include"  "upside.\""
OUR: "includes" "upsides.\" \""
```
Subject-verb agreement (`include` vs `includes`) and singular/plural (`upside` vs `upsides`).
Also misplaced closing quote mark. Reader missed grammar inconsistencies.

---

### Block 507 — UNCLEAR / MEDIUM
```
MB:  "the lower-right-hand coroner"
OUR: "lower right-hand corner"
```
MB has `coroner` where our has `corner`. Our output is semantically correct (`corner`).
MB may have a typo or the witness actually said "coroner" (unlikely in context).
Our engine is also missing `the` article. Cannot classify without audio verification.

---

### Block 537 — READER_FLAGGED_WRITER_WRONG / HIGH
```
MB:  "Fran Snyder"
OUR: "from an Schneider"
```
Reader correctly flagged `from an Schneider` (phonetic garble of `Fran Snyder`).
Writer proposed `Fran Schneider` — got first name right but wrong surname.
Validator rejected anyway: dropped `from`, `an`. Rejection record: turn=2657 p_0012.
Secondary: `email` → `E-mail` (MB_EDITORIAL).

---

### Block 540 — READER_FLAGGED_WRITER_WRONG / HIGH
```
MB:  "Fran Snyder?" / "Fran Snyder."
OUR: "Fran Schneider?" / "Fran Schneider."
```
Same Snyder/Schneider confusion as Block 537 — Writer consistently writes `Schneider`
when the correct name (per MB) is `Snyder`. Two occurrences.
Rejection record: turn=2659 p_0015.

---

### Block 639 — READER_MISSED_IT / LOW
```
MB:  "I don't know if I personally"
OUR: "I didn't know if I personally"
```
Same pattern as Block 461 — `didn't` → `don't`. Reader missed.

---

### Block 642 — UNCLEAR / LOW
```
MB:  "August 2023 Fund Raise?"
OUR: "August 2023 fundraise?"
```
Our engine correctly compounded to `fundraise`. MB splits and capitalizes: `Fund Raise`.
This may be MB house style for the fundraising round as a proper-noun-like event name.
Our output is arguably more correct standard English.

---

### Block 645 — UNCLEAR / LOW
```
MB:  "August 2023 Fund Raise,"
OUR: "August 2023 fundraise,"
```
Same pattern as Block 642.

---

### Block 663 — READER_MISSED_IT / LOW
```
MB:  "direction."  (Witness peruses document.)
OUR: "directions."
```
`directions` → `direction` (number). Reader missed.
Missing parenthetical stage direction (separate issue).

---

### Block 674 — UNCLEAR / LOW
```
MB:  "all of the interest parties"
OUR: "all of the interested parties"
```
Our output (`interested parties`) is the correct legal phrasing.
MB has `interest parties` — may be a MB transcription error.
Also: `them..."` vs `them."` (ellipsis vs period, MB editorial).

---

### Block 690 — VALIDATOR_BLOCKED / HIGH
```
MB:  "I'm handing you what's been marked"
OUR: "I'm hands go you what's been marked"
```
`hands go` is a catastrophic phonetic garble of `handing`.
Reader correctly proposed fix but span was `I'm hands go you what's`.
Validator rejected: dropped `hands`, `go`. Rejection record: turn=3381 p_0017.

---

### Block 710 — MB_EDITORIAL / LOW
```
MB:  "stuck...probably"  "side tracking"
OUR: "stuck."  "Probably"  "sidetracking"
```
Our engine correctly capitalizes new sentence and compounds `sidetracking`.
MB uses ellipsis continuation and splits the compound. Editorial preference.

---

## Top 3 Sub-Patterns

### 1. VALIDATOR_BLOCKED — Wide Span on Phonetic Fix (5 blocks)
Blocks: 6, 47, 256, 355, 690.
Reader correctly identifies the phonetic error and proposes the right fix, but sets
the token_span too wide — including surrounding context words (articles, pronouns,
prior name tokens). The validator then rejects the fix for dropping those context words.
**Root cause is identical to D-READER-COMPOUND-SPAN.**
The D-READER-COMPOUND-SPAN span-discipline fix already landed addresses this class —
phonetic word fixes need the same span tightening rule the compound-span fix provides.

### 2. Total Phonetic Garbles Missed by Reader (4 blocks, all HIGH)
Blocks: 207 ("seven ly"→"certainly"), 250 (email address), 356 ("allegedly"→"eventually"),
457 ("It ahold over"→"It's a holdover").
These are steno artifacts where phonetic transcription produced wrong words with zero
resemblance to the correct words in context. Reader's sensitivity to these patterns
is low — possibly because the garbled text is superficially grammatical/plausible.
Audio cross-check (future Validator phase) is the right fix; prompt-only improvement
will have limited reach here.

### 3. Proper Noun / Named Entity Errors (3 blocks)
Blocks 47 (Smith/submit), 127 (StormHarbour), 537/540 (Snyder/Schneider).
Reader catches proper-noun phonetic garbles (good) but either gets the wrong target name
(537/540) or has span issues that block the fix (47). The name `Schneider` vs `Snyder`
is a Writer hallucination — Reader flagged it correctly but Writer substituted a
phonetically similar but wrong surname.

---

## Recommendation: Where Would Fixes Go

| Bucket | Count | Fix Location |
|--------|-------|-------------|
| VALIDATOR_BLOCKED | 5 | READER_PROMPT_V1 — same span discipline already added by D-READER-COMPOUND-SPAN. These phonetic-fix spans need the same tight-span rule. Verify that span discipline section covers multi-word phonetic tokens, not just compound hyphenation tokens. |
| READER_MISSED_IT (HIGH) | 7 | Requires audio cross-check (Phase 2 Validator) for catastrophic garbles. Prompt improvement alone insufficient for "seven ly" → "certainly" class. |
| READER_FLAGGED_WRITER_WRONG | 2 | WRITER_PROMPT_V1 — Writer needs a rule: when the Reader flags a phonetic proper noun, do not hallucinate a "similar sounding" name. Propose FLAG op instead of REWORD when uncertain of the correct proper noun. |
| READER_MISSED_IT (LOW) | 6 | Low priority; mostly hyphenation/grammar. Stage 2 deterministic transforms could absorb the hyphenation cases (in-person, one-field). |
| UNCLEAR | 5 | Require audio/context review before any fix. |
| MB_EDITORIAL | 1 | No fix needed. |

**Single highest-ROI action:** Verify that the D-READER-COMPOUND-SPAN span discipline
rule already landed is broad enough to cover phonetic-fix spans (not just compound-word
spans). If it only mentions "concatenated or mis-hyphenated compound token", add
"phonetic substitution" to the examples so the Reader tightens spans on word-level
phonetic fixes too.

---

## Open Questions for Opus

1. **Block 207 proposal trace:** Is "seven ly" present in any Reader anomaly record for turn ~2291 area? The rejection at turn=2291 shows "Email certainly" → "email" which hints Reader may have flagged `certainly` as extra context but the turn does not match Block 207's location. Need turn index for Block 207 to confirm READER_MISSED_IT vs. something else.

2. **Block 507 audio check:** Did the witness actually say "coroner" or "corner"? Our engine output "corner" (semantically correct). If the witness said "coroner" by mistake, MB is correct and our engine missed the verbatim. Requires audio.

3. **D-READER-COMPOUND-SPAN scope:** The span discipline rule added tonight mentions "concatenated or mis-hyphenated compound token" specifically. Should it be broadened to "compound token or phonetic word substitution" to also cover blocks 6, 47, 256, 355, 690 (phonetic fixes with wide spans)?

4. **Blocks 642/645 — "Fund Raise" house style:** Is MB's capitalized two-word form the intended style for the fundraising round (treating it as a proper event)? If so, this is an intentional editorial choice that the engine should not try to match. Confirm with Scott.

5. **Snyder vs. Schneider (blocks 537/540):** The Writer hallucinated "Schneider" for "Snyder". Is this a one-time error or a systematic bias toward "Schneider"? Check if "Schneider" appears anywhere else in the depo text as a named entity that might have primed the Writer.
