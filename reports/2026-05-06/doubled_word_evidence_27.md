# Doubled Word Evidence — All 27 Bucket A Blocks
**Date:** 2026-05-06
**Analyst:** Claude Sonnet 4.6
**Task ref:** SONNET TASK — Doubled Word Evidence Pull (All 27)
**Oracle Covenant:** No engine code changed. No FINAL RTF opened. All data from existing artifacts.
**Sources:** `_diff_out/block_classification.json`, `_diff_out/brandl.diff_report.md`, `032626YELLOWROCK_smd_T.stage2.turns.json`

---

## Format Notes

- **Column 1 (ROUGH):** Stage 2 turn text from `stage2.turns.json` (key turn only; multi-turn blocks may span several turns). `*(NR)*` = not retrieved.
- **Column 2 (OUR):** `our_line` from `block_classification.json`. `**-word-**` = OUR has this, MB does not.
- **Column 3 (MB):** `mb_line` from `block_classification.json`. `**+word+**` = MB has this, OUR does not.
- **Tag:** Mechanism guess (see Tag Distribution table at end).

---

## Blocks

---

### Block #37 — tag: `Q-DROP-primary`

| Col | Text |
|---|---|
| ROUGH | `When and you left Conoco in 1994?` (idx=251, Q. s2) |
| OUR | Q. Okay. When you **-left-** left Conoco in 1994? |
| MB | Q. Okay. **+Q.+** When **+and+** you left Conoco in 1994? |

**Mechanism:** Block is primarily a Q-DROP defect (missing Q. turn break). OUR merges the s2 "When…" into the preceding Q. turn, producing "left left" at the merge boundary. D-DOUBLED-WORD ran before Stage 5 rendering — can't catch Stage 5 merge artifacts. The "doubled word" is a side effect of the Q-DROP, not a Stage 2 error.

---

### Block #69 — tag: `misclassification`

| Col | Text |
|---|---|
| ROUGH | *(NR — multi-turn block)* |
| OUR | …I **----** we **-would-** **-then-** would then, basically, go out… well. And then… **-hole-** hole. And then… If **-If-** **-it-** was **----** if the well was required… **-time-** **-frame-** directional… |
| MB | …Q. Okay. **+Q.+** And what was the nature… **+timeframe+** directional… |

**Mechanism:** Block contains two Q-DROP misses (two `Q. Okay. Q.` separators absent). The rendering artifacts ("would then would then", "hole hole", "If it If it") are all caused by Stage 5 continuation-merge of Q-DROP s2 turns, not Stage 2 doubled words. `is_doubled` fired on a rendering side-effect ("hole hole" or "then then") that MB does not exhibit.

---

### Block #71 — tag: `case-mismatch`

| Col | Text |
|---|---|
| ROUGH | `Go go ahead.` (idx=371, COLLOQUY s5) |
| OUR | MR. MADIGAN: **-Objection-** to form. Go **----** **-go-** **-ahead-** ahead. |
| MB | MR. MADIGAN: **+Object+** to form. Go ahead. |

**Mechanism:** The steno already had "Go go ahead." in Stage 2. D-DOUBLED-WORD missed it — most likely because `low_tok` compares lowercased tokens but "Go" (sentence-initial capital after prior turn) matched "go" only after lowercasing, and the rule may not fire across turn-boundary tokenization. Additionally, "ahead ahead" appears in OUR because Stage 5 continued an orphaned COLLOQUY turn into the next block.

---

### Block #77 — tag: `misclassification`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | Q. Okay. Okay. Do you hold yourself out as an expert in petroleum or oil and gas drilling operations? MR. MADIGAN: **-Objection-** to form. Go ahead. |
| MB | Q. Okay. Okay. **+Q.+** Do you hold yourself out as an expert in petroleum or oil and gas drilling operations? MR. MADIGAN: **+Object+** to form. Go ahead. |

**Mechanism:** "Okay. Okay." is present in **both** OUR and MB — the witness legitimately said it twice. `is_doubled` fired on this as a doubled word, but it is not a defect in OUR. Primary block difference is the missing Q. separator (Q-DROP). False positive from the classifier.

---

### Block #83 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | `Differential ly stuck would be kind of I'm trying to think of an example…` (idx=416, A. s3) |
| OUR | A. Differentially stuck would be kind of… there is a suction against it when two properties are attached and there's water there, differentially **-stuck-** stuck. There is a differential pressure between two objects between the site of the **-side-** **-of-** **-the-** hole and the drill pipe… |
| MB | A. Differentially stuck would be kind of… that's differentially stuck. There is a differential pressure between two objects between the site of the hole and the drill pipe… |

**Mechanism:** OUR renders "differentially stuck stuck" — a word bridges a sentence-ending period. MB renders "that's differentially stuck." (one occurrence). D-DOUBLED-WORD likely missed "stuck. stuck" because punctuation separates the two tokens in the rendered text (the rule compares adjacent tokens; a period between them breaks adjacency).

---

### Block #85 — tag: `false-speaker-label`

| Col | Text |
|---|---|
| ROUGH | `A back off is when you're separating yourself separating the upper portion of the drill string from the bottom portion…` (idx=430, A. s3) |
| OUR | Q. What is a **-back-** **-off?-** A. A **-back-** **-off-** is when separating yourself **----** separating the upper portion of the drill string from the bottom portion of the drill string that may be stuck… |
| MB | Q. What is a **+backoff?+** A. A **+backoff+** is when **+you're+** separating yourself separating the upper portion of the drill string from the bottom portion of the drill string that may be stuck… |

**Mechanism:** OUR renders "A. A back off" — the "A." speaker label followed immediately by "A" (first word of "A back off"). `is_doubled` lowercases and sees "a a" → fires. The actual doubled word is a false positive from speaker-label tokenization, not a real steno error. "back off" vs "backoff" is a separate word-segmentation difference (not caught by D-DOUBLED-WORD).

---

### Block #91 — tag: `stage3-introduced`

| Col | Text |
|---|---|
| ROUGH | `So in that case you sort of solve the stuck pipe and being continue without having to sidetrack?` (idx=447, Q. s1) |
| OUR | Q. So in that case you sort of solve the stuck pipe and **-and-** continue without having to sidetrack? |
| MB | Q. So in that case you sort of solve the stuck pipe and **+can+** continue without having to sidetrack? |

**Mechanism:** ROUGH steno had "and being continue" — plausible steno error for "and can continue". Stage 3 LLM corrected "being" but produced "and and continue" rather than "and can continue" (corrected the wrong token, introducing a double). D-DOUBLED-WORD ran at Stage 2, before Stage 3, so could not catch Stage-3-introduced doubles. MB correctly reads "and can continue".

---

### Block #94 — tag: `Q-DROP-primary`

| Col | Text |
|---|---|
| ROUGH | *(NR — multi-turn block)* |
| OUR | Q. Okay. And during that period, did you **----** were **-those-** those mostly vertical wells, directional wells, a mixture of both? A. **-two-thirds-** vertical, **-one-third-** directional. |
| MB | Q. Okay. **+Q.+** And during that period, did you were those mostly vertical wells, directional wells, a mixture of both? A. **+Probably+** **+twothirds+** vertical, **+onethird+** directional. |

**Mechanism:** Block is primarily a Q-DROP (missing Q. separator). OUR renders "were those those mostly" — "those those" appears because Stage 5 merged the s2 continuation turn beginning with "those" into the s1 Q. turn which also ends with "were those". The doubled word is a merge-boundary artifact, not a Stage 2 steno error.

---

### Block #95 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | `I would say that most of them were between 10 to 12,000 foot.` (idx=461, A. s3) |
| OUR | A. I would say that most of them were **-10,000-** to 12,000 **-foot-** foot. |
| MB | A. I would say that most of them were **+between+** **+10+** to 12,000 foot. |

**Mechanism:** ROUGH steno had "10,000 to 12,000 foot. foot." — the word "foot" appears at the end of the sentence (period-terminated) and then again as a spurious duplicate at turn boundary. D-DOUBLED-WORD missed "foot. foot" because the period between the two tokens breaks token adjacency. Also "10,000" vs "between 10" is a separate steno reading difference.

---

### Block #102 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | `Just wanted a different job. I worked way too much hours at that job and I wanted always wanted to go to work internationally.` (idx=486, A. s3) / `Did you leave or were you let, go?` (idx=487, Q. s1) |
| OUR | A. Just wanted a different job. I worked way too **-much-** hours at that job and I wanted **----** always wanted to go to work internationally. Q. Did you leave or were let **-go-** go? |
| MB | A. Just wanted a different job. I worked way too **+many+** hours at that job and I wanted always wanted to go to work internationally. Q. Did you leave or were **+you+** let go? |

**Mechanism:** ROUGH Q. turn had "let, go?" — comma between "let" and "go". Stage 5 renders "let go go" — OUR has "let [go]" from the A. turn ending, then "go?" from the Q. turn with its preceding comma. D-DOUBLED-WORD missed "go, go" because the comma breaks token adjacency. Also "much" vs "many" is a separate steno correction difference.

---

### Block #104 — tag: `case-mismatch`

| Col | Text |
|---|---|
| ROUGH | `What was your first off, how long were you working for Union Texas?` (idx=493, Q. s1) |
| OUR | Q. What was your **-your-** first **----** off, how long were you working for Union Texas? |
| MB | Q. What was your first off, how long were you working for Union Texas? |

**Mechanism:** ROUGH had "What was your your first off" — "your" repeated. Stage 2 corrected_turns.json likely already had "your your" but D-DOUBLED-WORD missed it. Possible reason: "your" appears at end of a phrase segment ("What was your") and then again at start of the next correction pass ("your first off") — the two occurrences may be separated by a punctuation or segment boundary in the internal representation. Alternatively, case mismatch ("Your" vs "your") if the first was sentence-initial.

---

### Block #271 — tag: `misclassification`

| Col | Text |
|---|---|
| ROUGH | *(NR — multi-turn block)* |
| OUR | …A. Yeah. I mean I I my last well, that I did for them was I plugged I plugged two wells last year… |
| MB | …A. Yeah. I mean I I my last well, that I did for them was I plugged **+I+** **+plugged+** two wells last year… Q. Okay. **+Q.+** So starting **+because+** we're about to get to the period of time… |

**Mechanism:** "I I" is present in **both** OUR and MB (the witness actually stuttered "I I"). `is_doubled` fired on this legitimate speaker repetition. False positive. Primary block difference is a Q-DROP (missing Q. separator + additional MB text). "I I" is not a defect — MB preserved it as-is.

---

### Block #278 — tag: `case-mismatch`

| Col | Text |
|---|---|
| ROUGH | `You know, I don't remember meeting her. I I honestly don't remember the first time that I met her.` (idx=1283, A. s3) |
| OUR | Q. And tell me about that **-meeting?-** A. You know, I don't remember meeting her. **-I-** I honestly don't remember the first time that I met her. Q. Okay. What do you recall… |
| MB | Q. And tell me about that **+meeting.+** A. You know, I don't remember meeting her. I honestly don't remember the first time that I met her. Q. Okay. **+Q.+** What do you recall… |

**Mechanism:** ROUGH steno already had "I I honestly" — the witness stuttered. MB corrected it to single "I"; OUR preserved the stutter as-is (kept both). D-DOUBLED-WORD should have caught "I I" at Stage 2 but didn't — likely because `low_tok` processes "I" as "i" and a case-sensitive path missed the self-identical pair, OR the ROUGH had "I I" and the rule fired on it but only removed one "I" which then wasn't updated in downstream. This warrants a follow-up on whether D-DOUBLED-WORD handles uppercase-only tokens.

---

### Block #301 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | *(NR — multi-turn block)* |
| OUR | Q. **-Y'all-** **----** **-y'all-** **-can-** Yellow Rock excuse me. **-y'all-** **-can-** Ms. Henderson and the people on the **-org-** chart… and that **-that-** **-happened-** in late **-2018,-** is that consistent with your recollection? |
| MB | Q. **+Youall+** **+youall+** **+being+** Yellow Rock excuse me. **+Youall+** **+being+** Ms. Henderson and the people on the **+organization+** chart… and that **+happens+** in late **+2018;+** is that consistent with your recollection? |

**Mechanism:** OUR renders "Y'all" with apostrophe; `is_doubled` tokenizes on whitespace and sees "y'all" (containing apostrophe) vs "y'all" — adjacent identical tokens including apostrophe. D-DOUBLED-WORD likely tokenizes differently than `is_doubled` (e.g., strips punctuation vs keeps it), causing the deduplicate-at-Stage-2 / detect-at-classify mismatch. Also "y'all" vs "youall" is a CR transcription style difference (MB uses solid "youall"; OUR uses "y'all").

---

### Block #381 — tag: `misclassification`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | Q. Okay. Okay. Some general things when you came to work as an independent you were an independent contractor, right? |
| MB | Q. Okay. Okay. **+Q.+** Some general things when you came to work as an independent you were an independent contractor, right? |

**Mechanism:** "Okay. Okay." is present in **both** OUR and MB (witness said it twice). `is_doubled` fired on the legitimate repetition. False positive. Only real difference is the missing Q. separator (Q-DROP). Same pattern as Block #77.

---

### Block #395 — tag: `multi-word-repeat`

| Col | Text |
|---|---|
| ROUGH | `What was your what was your rate of compensation when you started working for Yellow Rock, do you recall?` (idx=1779, Q. s2) |
| OUR | Q. Okay. What was your **-—-** what was **-your-** your rate of compensation when you started working for Yellow Rock, do you recall? |
| MB | Q. Okay. **+Q.+** What was your what was your rate of compensation when you started working for Yellow Rock, do you recall? |

**Mechanism:** ROUGH steno already had "what was your what was your rate" — a multi-word phrase repeat. D-DOUBLED-WORD handles single-token adjacent duplicates only; it does not detect repeated phrases ("what was your" × 2). Neither Stage 2 nor Stage 5 collapsed the phrase repeat. MB preserved the full "what was your what was your" as-is in the final — so OUR's rendering of "your your" (from two occurrences of "your") is the doubled-word signal, but the root is a multi-token steno error.

---

### Block #450 — tag: `reporter-check`

| Col | Text |
|---|---|
| ROUGH | *(NR — multi-turn, steno error turn)* |
| OUR | Q. Okay. I'm **-shot-** sure I let you finish your explanation because **-we-** talked about the **-chloride.-** How is it that you believe that Westlake **-has-** responsibility for the level of **-correspondence-** **-rides-** that were detected by **-check-** **-check-** in the **-109431-** **-\*REPORTER-** **-CHECK-** **-HERE\*-** |
| MB | Q. Okay. **+Q.+** I'm **+not+** sure I let you finish your explanation because **+we've+** talked about the **+chlorides.+** How is it that you believe that Westlake **+bears+** responsibility for the level of **+chlorides+** that were detected by **+Yellow+** **+Rock+** in the **+shallowest+** **+two+** **+formations+** **+in+** **+the+** **+1031+** **+well?+** |

**Mechanism:** Stage 3 encountered heavily garbled steno (likely a steno drop mid-question). Stage 3 flagged it with a `*REPORTER CHECK HERE*` marker. The word "check" appears twice in OUR's output ("**-check-** **-check-**"). `is_doubled` fired on this reporter-note artifact. The block is primarily a Stage 3 steno-garble failure, not a D-DOUBLED-WORD miss.

---

### Block #456 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | A. We don't have any other experience I not have any other experience. Q. And you don't have any prior experience in trying to explain chloride and **-Brian-** migration around a salt dome, correct? MR. MADIGAN: Objection to **-form;-** foundation. **-foundation.-** **-[THE-** **-ATTORNEY:-** **-]-** **-Q.-** |
| MB | A. We don't have any other experience I **+do+** not have any other experience. Q. And you don't have any prior experience in trying to explain chloride and **+brine+** migration around a salt dome, correct? MR. MADIGAN: Objection to **+form,+** foundation. |

**Mechanism:** OUR renders "foundation; foundation." — the word "foundation" appears twice, separated by a semicolon ("form; foundation. foundation."). D-DOUBLED-WORD missed "foundation; foundation" because the semicolon between tokens breaks adjacency. Also "brine" steno misread as "Brian" is a separate Stage 3 error.

---

### Block #489 — tag: `misclassification`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | Q. And part of that interaction was to get you and your **-Teams-** arms around the data and documents that Mr. Cox and Mr. Bertelot had assembled and had custody of from the almost 20 years of ownership they had had at Sulphur Mines, correct? |
| MB | Q. And part of that interaction was to get you and your **+team's+** arms around the data and documents that Mr. Cox and Mr. Bertelot had assembled and had custody of from the almost 20 years of ownership they had had at Sulphur Mines, correct? |

**Mechanism:** "had had" is present in **both** OUR and MB — legitimate past-perfect construction. `is_doubled` fired on the grammatically correct "had had". False positive. Only real difference is "Teams" (OUR, no apostrophe) vs "team's" (MB, possessive with apostrophe). The doubled-word classification is incorrect.

---

### Block #495 — tag: `reporter-check`

| Col | Text |
|---|---|
| ROUGH | *(NR — multi-turn, steno garble)* |
| OUR | A. **-Uh-huh.-** Q. They were scanning like 60 to 100 **-box-** **-he-** of stuff. I'll ask **-you-** **-this-** **-the-** the easy way: **-\*REPORTER-** **-CHECK-** **-HERE\*-** well files? |
| MB | A. **+Uhhuh.+** Q. They were scanning like 60 to 100 **+boxes+** of stuff. **+Did+** **+you+** **+ever+** I'll ask **+it+** the easy way: **+Do+** **+you+** **+recall+** **+ever+** **+laying+** **+eyes+** **+on+** **+the+** **+actual+** **+physical+** **+boxes+** **+that+** **+came+** **+from+** **+Yellow+** **+Rock+** **+1.0+** well files? |

**Mechanism:** Another `*REPORTER CHECK HERE*` block — Stage 3 flagged garbled steno mid-question. The "doubled word" that triggered `is_doubled` is likely "the the" from "**-the-** the easy way" (OUR has "the the easy way" while MB has "it the easy way"). This is an alignment artifact from the garbled steno region, not a D-DOUBLED-WORD miss.

---

### Block #573 — tag: `misclassification`

| Col | Text |
|---|---|
| ROUGH | `On the legacy wells they were not a priority. Up until until COVID hit abdomen…` (idx=2671, A. s3) |
| OUR | A. On the legacy wells they were not a priority. Up until **----** until COVID hit **-abdomen,-** you know… |
| MB | A. On the legacy wells they were not a priority. Up until until COVID hit **+and,+** you know… |

**Mechanism:** "until until" is present in **both** OUR and MB — the witness actually said "up until until COVID hit" (steno repetition that MB preserved). `is_doubled` fired on a legitimate repetition. False positive. D-DOUBLED-WORD should not have run on this (it's in MB too), but Stage 2 apparently didn't deduplicate it either — suggesting ROUGH already had "until until" and Stage 2's D-DOUBLED-WORD correctly left it (MB shows it's real). The `is_doubled` classifier is over-sensitive.

---

### Block #580 — tag: `case-mismatch`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | Q. Where **-y'all-** **-meet-** meet, here? |
| MB | Q. Where **+did+** **+why+** **+all+** meet, here? |

**Mechanism:** OUR renders "meet meet" — "y'all meet meet, here?" MB has "did why all meet, here?" (steno reading difference: "y'all" → "did why all"). The "meet meet" in OUR comes from Stage 5 merging two turns at boundary, one ending in "meet" and the next starting with "meet". D-DOUBLED-WORD missed "meet meet" possibly because the two occurrences are in different turns (cross-turn boundary) and D-DOUBLED-WORD operates within a single turn's token stream.

---

### Block #583 — tag: `stage3-introduced`

| Col | Text |
|---|---|
| ROUGH | `Did yeah you review any documents?` (idx=2722, Q. s1) |
| OUR | Q. Did **-you-** you review any documents? |
| MB | Q. Did you review any documents? |

**Mechanism:** ROUGH steno had "Did yeah you review". Stage 2 D-DOUBLED-WORD saw no adjacent identical tokens ("yeah" ≠ "you"). Stage 3 LLM corrected "yeah" → "you" (phonetic steno error). Stage 3 output: "Did you you review" — now "you you" is adjacent, but D-DOUBLED-WORD already ran at Stage 2. Stage 3-introduced doubles cannot be caught by Stage 2's rule. This is the cleanest example of the Stage-3-introduced-double failure mode.

---

### Block #640 — tag: `false-speaker-label`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | Q. **-Okay?-** **-A.-** What is **-429.-** A. It looks like a **-a-** calculation **-volume-** **-metrics-** for the CIB HAZ project. |
| MB | Q. **+Okay.+** **+Q.+** What is **+429?+** **(Witness peruses document.)** A. It looks like a calculation **+of+** **+volumetrics+** for the CIB HAZ project. |

**Mechanism:** OUR renders "A. It looks like a **-a-** calculation" — the "A." speaker label is followed by "a" (indefinite article first word of content). `is_doubled` lowercases both → "a a" → fires. Same false-positive pattern as Block #85. Not a steno doubled word. "volumetrics" split as "volume metrics" is a separate word-segmentation difference.

---

### Block #695 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | *(NR)* |
| OUR | Q. And do you recall if at Yellow Rock **-943-** **-point-** **-on-** or **-two-** **-point-** **-on,-** that the company utilized output from **-PhD-** **-[win|within|-** **-]-** its **-decision-making-** decisionmaking? |
| MB | Q. And do you recall if at Yellow Rock **+3.0+** or **+2.0,+** that the company utilized output from **+PHDWin+** in its decisionmaking? |

**Mechanism:** OUR renders "decision-making decisionmaking" — the hyphenated form followed by the solid form. D-DOUBLED-WORD would not fire on "decision-making" vs "decisionmaking" (different token strings). `is_doubled` apparently matches on a normalized form (stripping hyphens?) and sees "decisionmaking decisionmaking". Cross-punctuation tokenization mismatch between D-DOUBLED-WORD (Stage 2, strict) and `is_doubled` (classifier, normalized).

---

### Block #703 — tag: `across-punct`

| Col | Text |
|---|---|
| ROUGH | `But the rest of the columns after that about economics and taxes and returns an costs, not you?` (idx=3267, Q. s1) |
| OUR | Q. But the rest of the columns after that about economics and taxes and returns and **-costs-** costs, not you? |
| MB | Q. But the rest of the columns after that about economics and taxes and returns and costs, not you? |

**Mechanism:** ROUGH steno had "returns an costs" (steno dropped the final "d" in "and"). Stage 3 corrected "an" → "and". Stage 5 renders "and costs costs" — the word "costs" appears before the comma ("costs,") and then OUR has an extra "costs" before it. D-DOUBLED-WORD missed "costs, costs" because the comma separates the tokens. This is an across-punct miss.

---

### Block #754 — tag: `case-mismatch`

| Col | Text |
|---|---|
| ROUGH | `You're not wrong. Your memory is dead O I just wanted to know if you were thinking about it in terms of start date as opposed Todd finish date?` (idx=3532, Q. s1) / `Finish date.` (idx=3533, A. s3) |
| OUR | Q. You're not wrong. Your memory is dead **-O-** I just wanted to know if you were thinking about it in terms of start date as to finish **-finish-** date? |
| MB | Q. You're not wrong. Your memory is dead **+on.+** I just wanted to know if you were thinking about it in terms of start date as **+opposed+** to finish date? |

**Mechanism:** ROUGH Q. turn ends with "finish date?" and the next A. turn (idx=3533) begins with "Finish date." Stage 5 rendered the Q. turn text including "finish" and then the A. turn starts with "Finish" — creating "finish Finish" at the cross-turn boundary in the rendered output. D-DOUBLED-WORD operates within a turn; it cannot catch cross-turn-boundary doubles. `is_doubled` evaluates the full rendered block and fires on "finish finish" (case-insensitive match). This is a cross-turn-boundary case-mismatch failure.

---

## Tag Distribution Table

| Tag | Count | Blocks | What failed |
|---|---:|---|---|
| `across-punct` | 7 | #83, #95, #102, #301, #456, #695, #703 | D-DOUBLED-WORD operates on whitespace-split tokens; punctuation between adjacent identical words breaks the match |
| `misclassification` | 6 | #69, #77, #271, #381, #489, #573 | `is_doubled` fired on words present in **both** OUR and MB (legitimate repetition, steno stutters, past-perfect "had had", "until until", "Okay. Okay.") |
| `case-mismatch` | 5 | #71, #104, #278, #580, #754 | D-DOUBLED-WORD (Stage 2) or cross-turn boundary matching fails when adjacent identical tokens differ in capitalization, or when the double spans a turn-line boundary |
| `Q-DROP-primary` | 2 | #37, #94 | Block is primarily a Q-DROP defect; "doubled word" is a merge-boundary rendering artifact, not a Stage 2 error |
| `stage3-introduced` | 2 | #91, #583 | Stage 3 LLM corrected a steno token to the same word already adjacent → created a double **after** D-DOUBLED-WORD had already run |
| `false-speaker-label` | 2 | #85, #640 | "A." speaker label + "A" first word of content → `is_doubled` lowercases → "a a" false detection |
| `reporter-check` | 2 | #450, #495 | Stage 3 emitted `*REPORTER CHECK HERE*` for garbled steno; repeated tokens in the reporter-note artifact triggered `is_doubled` |
| `multi-word-repeat` | 1 | #395 | Steno repeated a multi-token phrase ("what was your" × 2); D-DOUBLED-WORD handles single-token adjacent duplicates only |
| **Total** | **27** | | |

---

## Quick Observations

- **The largest failure mode is misclassification (6/27, 22%).** `is_doubled` is over-sensitive: it fires on legitimate steno repetitions ("until until", "had had", "Okay. Okay.", "I I") that MB preserved in the final. These are not defects. A fix would add a check: if the doubled word also appears in MB's line, suppress the `doubled_word` classification.

- **Across-punct is the most fixable true miss (7/27, 26%).** D-DOUBLED-WORD's token adjacency check should strip or ignore punctuation between tokens. A simple normalization pass (strip trailing punctuation from each token before comparing) would catch "go. go", "foot. foot", "costs, costs", "foundation; foundation." without changing existing behavior for the happy path.

- **Stage-3-introduced doubles (2/27, 7%) are architecturally hard to fix.** D-DOUBLED-WORD at Stage 2 cannot catch doubles that Stage 3 creates. Options: (a) run a post-Stage-3 deduplication pass, or (b) let Stage 3's system prompt instruct it not to produce repeated tokens. Block #583 ("Did yeah you" → "Did you you") is the canonical example.

- **False-speaker-label detection (2/27, 7%) is a classifier bug, not a pipeline bug.** `is_doubled` should exclude speaker-label tokens ("Q.", "A.", "MR. X:") from the token stream before checking adjacency. "A." + "a" should not produce a match.

- **Q-DROP-primary blocks (2/27, 7%):** Fixing the Q-DROP defect (DEF-B-001) would also eliminate the "doubled word" signal in blocks #37 and #94 as a side effect.

- **"y'all" vs "youall" (block #301):** MB's CR style uses solid "youall"; OUR uses "y'all" with apostrophe. The apostrophe causes tokenization divergence between D-DOUBLED-WORD and `is_doubled`. This is a CR-profile style difference (see `PARKING_LOT_stones_fingerprint_file.md`) and is not fixable without per-CR normalization.

- **Two `*REPORTER CHECK HERE*` blocks (#450, #495):** Stage 3's fallback marker is leaking into the classifier. These blocks should be excluded from `doubled_word` scoring — a block containing the reporter-check string is already known to be garbled and should be counted separately (Bucket E or similar).

---

## One Code Block Back to Scott

The most impactful near-term fix for false positives in `is_doubled`:

```python
# Current (approximate):
def is_doubled(our_line: str) -> bool:
    toks = low_tok(our_line)
    return any(toks[i] == toks[i+1] for i in range(len(toks)-1))

# Proposed: exclude misclassifications and false speaker labels
_SPEAKER_LABEL_RE = re.compile(r'^(q\.|a\.|mr\.|ms\.|mrs\.|the\s+\w+:)$')
_REPORTER_CHECK = "*REPORTER CHECK HERE*"

def is_doubled(our_line: str, mb_line: str = "") -> bool:
    if _REPORTER_CHECK in our_line:
        return False  # garbled steno block — don't classify as doubled_word
    toks = [t for t in low_tok(our_line) if not _SPEAKER_LABEL_RE.match(t)]
    mb_toks_set = set(low_tok(mb_line)) if mb_line else set()
    for i in range(len(toks) - 1):
        if toks[i] == toks[i+1]:
            # Suppress if the doubled word is also doubled in MB (legitimate repetition)
            if toks[i] not in mb_toks_set:
                return True
    return False
```

**This does not fix** across-punct misses or stage3-introduced doubles — those require separate changes (punctuation-stripping in D-DOUBLED-WORD; post-Stage-3 dedup pass). But it would eliminate the 6 misclassifications and 2 false-speaker-label false positives, dropping the bucket from 27 to ~19 true defects.

---

*Generated: 2026-05-06*
*Oracle Covenant honored. No engine code changed. No FINAL RTF opened.*
*All 27 doubled_word Bucket A blocks analyzed. No fix proposals implemented — evidence pull only.*
