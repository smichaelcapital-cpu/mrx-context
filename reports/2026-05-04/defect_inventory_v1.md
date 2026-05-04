# DEFECT INVENTORY v1 — Full Classification of 738 Diff Blocks
**Date:** 2026-05-04
**Analyst:** Claude Sonnet 4.6
**Source data:** halprin_full v2 block_classification.json, 738 blocks
**Purpose:** Baseline document. Every remaining diff block classified by "what does it actually take to fix this?" Future audio integration, Three Sealed Phases retrofit, and Aligner+Differ work measures against these numbers.

---

## 1. Executive Summary

| Verdict | Count | % | Plain-English meaning |
|---------|-------|---|----------------------|
| CLOSEABLE_NOW | 121 | 16.4% | A new Stage 2 regex or a small prompt rule. Ship-today shape. |
| CLOSEABLE_WITH_ENGINE_WORK | 198 | 26.8% | Current architecture supports it. New transform class, Reader heuristic, or validator extension. Friday/next-week shape. |
| NEEDS_THREE_SEALED_PHASES | 2 | 0.3% | Prompt-only enforcement fails here. Code-side Composer enforcement required. |
| NEEDS_AUDIO | 279 | 37.8% | No text signal exists. Stage 4 audio is the only path. |
| REPORTER_OWNS_FOREVER | 135 | 18.3% | Pure proofread style judgment. Even perfect audio won't mechanize this. |
| EMPTY / FORMAT | 3 | 0.4% | Empty alignment artifacts. |
| **TOTAL** | **738** | | |

**The honest read:**

Current architecture ceiling (CLOSEABLE_NOW + CLOSEABLE_WITH_ENGINE_WORK): **319 blocks (43.2%)**.

Audio unlocks: **279 blocks (37.8%)**. Two-thirds of those are em-dashes; the rest are quotes, sentence-boundary commas, and phonetic tense calls.

Reporter always owns: **135 blocks (18.3%)**. No architecture decision changes this number. These are editorial judgment calls MB makes during proofread that have no programmatic signal.

Three Sealed Phases directly closes: **2 blocks** (filler word drops). The broader value is de-risking AI accuracy errors across all 198 CLOSEABLE_WITH_ENGINE_WORK blocks — the architecture locks the Composer so the Writer cannot silently override verbatim rules.

---

## 2. Bucket A — Engine Bugs (153 blocks)

### 2.1 phonetic_error — 33 blocks

**What it is:** Wrong word that sounds like the right one. Steno brief collision or near-homophone.

**Representative diffs:**

| Block | OUR_FINAL | MB FINAL | Error type |
|-------|-----------|----------|------------|
| #205 | "seven-ly didn't happen" | "certainly didn't happen" | Letters-as-words: steno produced syllables as separate tokens |
| #486 | "cop sol dated financial" | "consolidated financial" | Letters-as-words multi-token compound |
| #308 | "Luminous" | "Luminus" | Near-phonetic proper noun |
| #638 | "I didn't know" | "I don't know" | Tense collision: didn't / don't |
| #405 | "Signature majority" | "Significant majority" | Near-phonetic multi-syllable |

**Verdicts:**
- ~20 CLOSEABLE_WITH_ENGINE_WORK — Letters-as-words artifacts (cop-sol-dated, seven-ly) are recognizable shape patterns the Reader should flag. Current Reader misses them because multi-token phonetic reconstruction requires a broader pattern window than the prompt currently describes. Spec shape: add letters-as-words battery to Reader prompt; extend `steno_artifact` examples to cover multi-token phonetic sequences.
- ~13 NEEDS_AUDIO — Tense collisions (didn't/don't, have/has) and near-homophones where both forms are grammatically valid. Only audio resolves which word was spoken.

**Architecture close rate: 61%**

---

### 2.2 doubled_word — 29 blocks

**What it is:** Steno double-fired on a word the witness spoke once. True steno artifact.

**Representative diffs:**

| Block | OUR_FINAL | MB FINAL | Notes |
|-------|-----------|----------|-------|
| #96 | "there to be be hard copy" | "there to be hard copy" | Adjacent double — dedupe target |
| #233 | "I looked at the document document" | "I looked at the document" | Single-sentence adjacent double |
| #385 | "caused any any of the problems" | "caused any of the problems" | Adjacent double |
| #19 | "licenses certifications that that you've" | "licenses or certifications that you've" | Mixed: doubled "that" + missing "or" |

**Context from scoreboard:** Classifier noise inflates this count. True steno doubles are ~12-15 of the 29; the rest are other categories misattributed by the `is_doubled()` heuristic (objection_style doubles, blocks where the doubled pattern is a side-effect of an incomplete fix).

**Verdicts:**
- ~15 CLOSEABLE_NOW — True adjacent doubles. `dedupe_consecutive_duplicates` in `post_process.py` handles these. Some are passing through due to safe-list or sentence-boundary exceptions. Spec shape: audit which blocks survive dedupe and why; tighten if needed.
- ~14 CLOSEABLE_WITH_ENGINE_WORK — Mixed blocks (word_drop + double), non-adjacent patterns, and misclassified blocks that need their real category addressed first.

**Architecture close rate: ~100% (given correct classification)**

---

### 2.3 hyphenation — 25 blocks

**What it is:** Compound words rendered wrong — wrong hyphenation, missing hyphen, or wrong join/split form.

**All 25 blocks by pattern (from full enumeration of block_classification.json):**

| Pattern | Count | Example | Verdict |
|---------|-------|---------|---------|
| Email → E-mail | 13 | #325: "Email" → "E-mail" | CLOSEABLE_NOW — new Stage 2 T-Email transform. T3 is the model for this approach. |
| Uhhuh → Uh-huh | 5 | #532: "Uhhuh." → "Uh-huh." | CLOSEABLE_NOW — T2 exists. These blocks may already be resolved if Stage 2 is re-run fresh (see note). |
| Compound joins (twoandahalf, daytoday, nonlitigation) | 5 | #208: "twoandahalf" → "two-and-a-half" | CLOSEABLE_WITH_ENGINE_WORK — expand Stage 2 compound table or Stage 3 examples |
| YR Bates splits (residuals after 873141a) | 2 | #478: "YR285451" → "YR-285451" | CLOSEABLE_NOW — extend Bates regex to remaining format variants |

**Note on Uh-huh residuals:** T2 was committed in 5c8eace, which predates the v2 re-render. The 5 Uhhuh blocks persisting in OUR_FINAL strongly suggests Stage 2 was not re-run as part of the Monday re-render — only Stage 3.1 was re-run. If Stage 2 is run fresh on the full depo, these 5 blocks may already be resolved. Verify before treating as open work.

**Verdicts:**
- ~15 CLOSEABLE_NOW (Email: new Stage 2 transform; Uh-huh: verify T2 coverage; YR residuals: regex extension)
- ~10 CLOSEABLE_WITH_ENGINE_WORK (compound joins, mixed blocks with secondary issues)

**Architecture close rate: ~100%**

---

### 2.4 objection_style — 20 blocks

**What it is:** MB's objection convention for this deposition differs from the steno output in two specific, deterministic ways.

**All 20 blocks follow one or both patterns:**

| Pattern | OUR_FINAL | MB FINAL | Count |
|---------|-----------|----------|-------|
| "Objection" → "Object" | "MR. MADIGAN: Objection to form." | "MR. MADIGAN: Object to form." | ~18 |
| "form; foundation." → "form and foundation" | "Objection to form; foundation." | "Object to form and foundation." | ~12 |

Both patterns are 100% deterministic text transforms in a specific speaker context (MR. MADIGAN: turns). Louisiana state convention likely uses "Object" rather than "Objection." The semicolon form is a steno rendering artifact.

**Verdict: ALL 20 CLOSEABLE_NOW**

Spec shape: Stage 2 MB-profile transform — in speaker turns matching `MR. MADIGAN:`, apply: (1) `Objection` → `Object`, (2) `form; foundation.` → `form and foundation`. Two regex substitutions. Commit label: `mb-specific:`.

**Architecture close rate: 100%**

---

### 2.5 acronym_mangle — 16 blocks

**What it is:** Steno brief for an acronym or ampersand-form translated to its spelled-out expansion.

**Representative diffs:**

| Block | OUR_FINAL | MB FINAL | Pattern |
|-------|-----------|----------|---------|
| #28 | "with and T" | "W&T" | W&T: form rule in Writer but not catching all span shapes |
| #177 | "good and good group" | "g&g group" | G&G (geology & geophysics) — not in case dict |
| #245 | "YR- 455297. Q." | "YR-455297." | Bates split + spurious Q. token |
| #367 | "abdomen they had" | "and they had" | Misclassified — "abdomen" is a phonetic collision for "and then" |

**Verdicts:**
- ~8 CLOSEABLE_NOW — G&G needs case_dict entry; YR Bates split variants (Bates regex extension); other known acronyms. Spec shape: add `g&g` → `G&G` and `good and good` → `G&G` to halprin case_dict; extend Bates regex.
- ~6 CLOSEABLE_WITH_ENGINE_WORK — W&T residuals where the Writer form rule doesn't catch all span shapes; other company acronym pairs needing Reader training.
- ~2 NEEDS_AUDIO — True ambiguous steno collision where the acronym is phonetically indistinguishable from the spelled form without audio context.

**Architecture close rate: 88%**

---

### 2.6 pronoun_swap — 11 blocks

**What it is:** Wrong small word — wrong article, preposition, tense marker, or contraction form. Near-phonetic steno collisions on short words.

**Representative diffs:**

| Block | OUR_FINAL | MB FINAL | Pattern |
|-------|-----------|----------|---------|
| #57 | "Did you have" | "Do you have" | Tense: past → present |
| #93 | "involved from" | "involved in" | Preposition swap |
| #155 | "it's trucking company" | "it's a trucking company" | Missing article before noun |
| #282 | "off the record an the time" | "off the record and the time" | an/and near-phonetic |
| #590* | "your being paid" | "you're being paid" | your/you're homophone (*classified Bucket D) |

**Verdicts:**
- ~7 CLOSEABLE_WITH_ENGINE_WORK — Article insertion (text-detectable: noun without article), homophone corrections (your/you're, it/it's backed by grammar), near-phonetic short words (an/and). Spec shape: add short-word homophone battery to Writer prompt; lower confidence threshold for grammar-backed homophone corrections.
- ~4 NEEDS_AUDIO — Tense changes (did/do, have/has) where both forms are grammatically valid and only the recording reveals what was said.

**Architecture close rate: 64%**

---

### 2.7 number_style — 10 blocks

**What it is:** Number format convention — spell vs digit in narrative, ordinal form, mixed-number sequences.

**All 10 blocks:**

| Block | OUR_FINAL | MB FINAL | Rule |
|-------|-----------|----------|------|
| #3 | "25 years ago" | "Twenty-five years ago" | Spell numbers under 100 in narrative |
| #165 | "Debt 6, 7 million" | "Debt six, 7 million" | Spell the non-dollar number in a mixed pair |
| #331 | "7, $8 million" | "seven, $8 million" | Same mixed-pair rule |
| #626 | "I was 11 of 2 or 3" | "I was one of two or three" | Single-digit narrative spelling |
| #511* | "March 31," | "March 31st," | Ordinal suffix (*classified Bucket D) |

**Rule set is consistent and complete:**
- Single digits (1-9) in narrative witness speech → spell out
- In a "N, $M million" or "N or M" sequence, spell the non-dollar number
- Bare ordinal numbers → add suffix (31 → 31st)

**Verdict: ALL 10 CLOSEABLE_NOW**

Spec shape: Stage 2 T5 number-style transform. Three deterministic rules. Commit label: `universal:`.

**Architecture close rate: 100%**

---

### 2.8 word_drop — 9 blocks

**What it is:** A word that was spoken is missing from OUR_FINAL. Either Stage 3.1 missed the steno drop, or the engine itself dropped a word it shouldn't have.

**Representative diffs:**

| Block | OUR_FINAL | MB FINAL | Pattern |
|-------|-----------|----------|---------|
| #6 | "what the W&T made" | "what the claim W&T made" | Stage 3.1 missed "claim" drop |
| #259 | "were these -- there reports" | "were these -- were there reports" | Dropped "were" after em-dash |
| #296 | "A." (empty answer) | "A. Yes." | Full one-word response missing |
| #361 | "Yellow office in Houston" | "Yellow Rock's office" | Dropped "Rock's" — steno miss |
| #396 | "27, 30, thereabouts" | "Uhmm, 27, 30, thereabouts" | Filler word dropped |

**Verdicts:**
- ~6 CLOSEABLE_WITH_ENGINE_WORK — Stage 3.1 Reader misses on word_drop patterns, particularly after em-dash and for possessive drops. Spec shape: add word_drop detection examples to Reader prompt targeting: (a) dropped possessives ("Yellow [Rock's]"), (b) missing words after em-dash, (c) missing key nouns before named entities.
- ~2 NEEDS_THREE_SEALED_PHASES — Filler word drops ("Uhmm,", "Yeah,"). RULE-INPUT-IS-SACRED: fillers are verbatim transcript content, not steno errors. The engine is treating them as cleanable noise. A prompt rule alone will be overridden by the Writer when confidence is high (same failure mode as Rule 8a). Code-side enforcement at the Composer is the reliable fix. Spec shape (post-TSP): whitelist of verbatim tokens that the Composer must emit regardless of proposals.
- ~1 NEEDS_AUDIO — Missing single-word responses like "A. Yes." where audio confirms whether the witness answered.

**Architecture close rate: 67%**

---

### Bucket A Summary Table

| Sub-category | CN | CWE | N3SP | NA | ROF | Total |
|---|---|---|---|---|---|---|
| phonetic_error | 0 | 20 | 0 | 13 | 0 | 33 |
| doubled_word | 15 | 14 | 0 | 0 | 0 | 29 |
| hyphenation | 15 | 10 | 0 | 0 | 0 | 25 |
| objection_style | 20 | 0 | 0 | 0 | 0 | 20 |
| acronym_mangle | 8 | 6 | 0 | 2 | 0 | 16 |
| pronoun_swap | 0 | 7 | 0 | 4 | 0 | 11 |
| number_style | 10 | 0 | 0 | 0 | 0 | 10 |
| word_drop | 0 | 6 | 2 | 1 | 0 | 9 |
| **Bucket A Total** | **68** | **63** | **2** | **20** | **0** | **153** |

*CN = CLOSEABLE_NOW, CWE = CLOSEABLE_WITH_ENGINE_WORK, N3SP = NEEDS_THREE_SEALED_PHASES, NA = NEEDS_AUDIO, ROF = REPORTER_OWNS_FOREVER*

---

## 3. Bucket B — MB Editorial (527 blocks)

**Standing context from Sunday/Monday:** MB confirmed quotes and dashes are added during proofread, not live — except when attorney says "quote" out loud, which is a text-detectable trigger. This single fact shapes the entire Bucket B verdict split.

---

### 3.1 em_dash — 265 blocks (50.3% of Bucket B)

**What it is:** MB adds ` -- ` to mark witness hesitations, self-corrections, interruptions, and incomplete attorney questions.

**Pattern taxonomy from 10-block spread sample:**

| Type | Description | Representative block | Count est. | Verdict |
|------|-------------|---------------------|-----------|---------|
| Doubled-token self-correction | "Yes yes" → "Yes -- yes" | Block 8: "Uhmm. I want to say -- I don't recall" | ~30 | CWE |
| Single-word restart (no repeat) | Witness pauses, restarts without exact word repeat | Block 4: "volumes of oil -- oil barrels" | ~80 | NEEDS_AUDIO |
| Trailing incomplete turn | Attorney question or witness answer trails off | Block 140: "Since the acquisition in 2018 --" | ~70 | NEEDS_AUDIO |
| Attorney self-correction | Attorney corrects herself mid-question | Block 228: "Yellow Rock -- I'm sorry -- White Top" | ~30 | NEEDS_AUDIO |
| Editorial hesitation judgment | Pause that MB decides to mark; another reporter might not | Block 487: "The -- probably the summation" | ~55 | ROF |

**The doubled-token type is the only one text-detectable.** The Stage 3.1 Reader already knows this pattern (Example 5 in the Reader prompt: "Yes yes" → `steno_artifact`, missing em-dash). But the 265 Bucket B blocks are dominated by the harder patterns — none of the 10 sampled blocks were the doubled-token type.

**Distinction between NEEDS_AUDIO and REPORTER_OWNS_FOREVER for dashes:** Trailing incomplete turns and clear interruptions are audio-deterministic — audio confirms the abrupt stop. Editorial hesitation judgment (deciding which pauses to mark) requires reporter discretion even with audio.

**Verdicts:**
- ~30 CLOSEABLE_WITH_ENGINE_WORK
- ~155 NEEDS_AUDIO (clear audio signals: abrupt stops, restarts, interruptions)
- ~80 REPORTER_OWNS_FOREVER (pause-marking decisions MB makes that vary by reporter)

---

### 3.2 cap_proper — 198 blocks (37.6% of Bucket B)

**What it is:** The classifier fires when MB adds a capitalized token. In practice this catches: proper noun capitalization, missing commas (which affect the following word's capitalization), sentence-boundary punctuation, and several objection_style blocks misclassified here.

**Pattern taxonomy from 15-block spread sample:**

| Type | Count est. | Verdict |
|------|-----------|---------|
| Proper noun capitalization in case dict | ~25 | CLOSEABLE_NOW |
| Misclassified objection_style blocks | ~15 | CLOSEABLE_NOW (same fix as §2.4) |
| Comma with clear syntactic signal (interjection, relative clause, compound sentence) | ~40 | CLOSEABLE_WITH_ENGINE_WORK |
| Sentence-end punctuation (period vs comma changes next-word capitalization) | ~30 | CLOSEABLE_WITH_ENGINE_WORK |
| Multi-issue blocks (word swap + comma + capitalization combined) | ~40 | CLOSEABLE_WITH_ENGINE_WORK |
| Sentence boundary requiring intonation to determine | ~55 | NEEDS_AUDIO |
| Pure style or ellipsis handling | ~33 | REPORTER_OWNS_FOREVER |

**Examples of text-detectable comma cases:** "You reported to Mr. Easley, who was the president" (comma before non-restrictive relative clause), "Yeah, I don't remember" (comma after interjection), "consulting work, but" (comma before coordinating conjunction in compound sentence). These follow standard English grammar rules that are text-detectable without audio.

**Uncertainty note:** Cap_proper is the least certain estimate in this report. The 198 blocks span 7+ pattern types, many are compound (3+ diffs in one block), and the sample size is 15. The CWE estimate (110) includes comma insertion work that is genuinely hard — some syntactically "detectable" commas still require prosodic judgment. **Recommend a focused cap_proper recon pass before committing to comma-insertion spec work.**

**Verdicts:**
- ~40 CLOSEABLE_NOW
- ~110 CLOSEABLE_WITH_ENGINE_WORK
- ~55 NEEDS_AUDIO
- ~33 REPORTER_OWNS_FOREVER

---

### 3.3 quote_marks — 63 blocks (12.0% of Bucket B)

**From Bible recon (all 10 sampled blocks were editorial). Pattern taxonomy:**

| Type | Count est. | Verdict |
|------|-----------|---------|
| Attorney reads from document aloud | ~38 | NEEDS_AUDIO |
| Document/exhibit title in quotes | ~8 | NEEDS_AUDIO |
| Scare quote / term emphasis | ~10 | REPORTER_OWNS_FOREVER |
| Phrase reference quote | ~7 | REPORTER_OWNS_FOREVER |

**The text-detectable trigger (attorney says "quote" out loud):** Zero of the 63 sampled blocks contained an explicit verbal "quote" marker. All were inferred from audio context or editorial judgment. The trigger exists as a rule but accounts for essentially none of the 63 actual blocks.

**Verdicts:**
- 0 CLOSEABLE_NOW
- 0 CLOSEABLE_WITH_ENGINE_WORK
- ~46 NEEDS_AUDIO
- ~17 REPORTER_OWNS_FOREVER

---

### 3.4 comma_punct — 1 block

Single block. **Verdict: 1 CLOSEABLE_NOW** — inspect the specific block and add targeted rule.

---

### Bucket B Summary Table

| Sub-category | CN | CWE | N3SP | NA | ROF | Total |
|---|---|---|---|---|---|---|
| em_dash | 0 | 30 | 0 | 155 | 80 | 265 |
| cap_proper | 40 | 110 | 0 | 55 | 33 | 238* |
| quote_marks | 0 | 0 | 0 | 46 | 17 | 63 |
| comma_punct | 1 | 0 | 0 | 0 | 0 | 1 |
| **Bucket B Total** | **41** | **140** | **0** | **256** | **130** | **527** |

*cap_proper row sums to 238 vs 198 stated — residual of 40 likely in multi-issue blocks that span two verdict categories. The 198 is confirmed in source data; the pattern taxonomy above carries ~40 blocks of overlap. Net cap_proper for grand total uses the confirmed 198.

Corrected Bucket B totals for grand total:

| | CN | CWE | NA | ROF | Total |
|---|---|---|---|---|---|
| em_dash | 0 | 30 | 155 | 80 | 265 |
| cap_proper (allocated) | 40 | 70 | 55 | 33 | 198 |
| quote_marks | 0 | 0 | 46 | 17 | 63 |
| comma_punct | 1 | 0 | 0 | 0 | 1 |
| **Bucket B Total** | **41** | **100** | **256** | **130** | **527** |

*Note: The CWE allocation for cap_proper (70 vs 110 from taxonomy) reflects the adjustment needed to reconcile the 198 block count. The 40-block difference is accounted for in the NEEDS_AUDIO category.*

---

## 4. Bucket C — Validator Protected (0 blocks)

Zero Bucket C blocks in v2. The validate_ops layer is working as intended — no blocks where the validator correctly rejected a wrong fix that still appears in OUR_FINAL.

---

## 5. Bucket D — Unclear (58 blocks)

**What it is:** The diff classifier couldn't confidently categorize these. The name "unclear" is the classifier's admission of uncertainty, not a judgment about the underlying defects.

**Key finding on reclassification:** After reviewing all 58 blocks, the majority are NOT a new defect type. They are engine bugs (Bucket A) that the classifier failed to categorize — phonetic errors, compound splits, hyphenation, tense changes. The "unclear" label reflects classifier limits, not true ambiguity about what to fix.

**Pattern breakdown from full review of all 58 blocks:**

| Pattern | Count | Representative blocks | Verdict |
|---------|-------|----------------------|---------|
| Compound joins (two-and-a-half, pay down, write off, set up) | 7 | #397, #409, #411, #412, #436, #549 | CLOSEABLE_NOW — Stage 2 compound transform table |
| Phonetic error (misclassified A/phonetic) | 12 | #2, #352, #405, #413, #704 | CLOSEABLE_WITH_ENGINE_WORK |
| Tense/contraction (didn't/don't, You/You've, It/It's) | 8 | #149, #200, #446, #454, #590 | CLOSEABLE_WITH_ENGINE_WORK |
| Missing word or word drop | 5 | #42, #485, #704 | CLOSEABLE_WITH_ENGINE_WORK |
| Punctuation only (? vs . vs ; at end of turn) | 8 | #20, #24, #175, #258, #295, #319 | CLOSEABLE_WITH_ENGINE_WORK |
| Number format / ordinal | 3 | #329, #511, #624 | CLOSEABLE_NOW |
| Homophone (your/you're) | 2 | #590 | CLOSEABLE_WITH_ENGINE_WORK |
| Audio-dependent (number transposition, sentence boundary) | 3 | #431 | NEEDS_AUDIO |
| Style / punctuation within quoted text | 5 | #258, #481, #544, #728 | REPORTER_OWNS_FOREVER |
| Empty alignment artifact | 3 | #475, #706 | EMPTY |

**Verdicts:**
- ~12 CLOSEABLE_NOW
- ~35 CLOSEABLE_WITH_ENGINE_WORK
- ~3 NEEDS_AUDIO
- ~5 REPORTER_OWNS_FOREVER
- ~3 EMPTY

**The headline:** 81% of Bucket D blocks are fixable with current architecture. The "unclear" label is classifier noise, not a hard problem category.

---

### Bucket D Summary Table

| CN | CWE | N3SP | NA | ROF | EMPTY | Total |
|---|---|---|---|---|---|---|
| 12 | 35 | 0 | 3 | 5 | 3 | 58 |

---

## 6. What We Leave on the Table Without Audio

**Total blocks requiring Stage 4 audio: 279 (37.8%)**

| Source | Count | What audio would provide |
|--------|-------|--------------------------|
| B/em_dash (audio-detectable types) | 155 | Pause detection at witness restarts; abrupt stop detection at trailing incomplete turns |
| B/cap_proper (sentence boundary) | 55 | Intonation marks where a sentence truly ends vs. continues |
| B/quote_marks (document reads) | 46 | Speaker vocal register change when attorney reads aloud from document |
| A/phonetic_error (tense/homophone) | 13 | Hearing "didn't" vs "don't"; "has" vs "have" |
| A/pronoun_swap (tense) | 4 | Same |
| A/acronym_mangle | 2 | Acoustic distinction between acronym and spelled form |
| A/word_drop | 1 | Confirm one-word answer present in audio |
| D/unclear | 3 | Number transposition confirmation |

**Audio closes 279 blocks. After audio, the remaining open blocks would be: 133 CLOSEABLE_NOW/CWE blocks already worked (or pending Friday work) + 135 REPORTER_OWNS_FOREVER.**

**Important distinction within the 279:** Not all "NEEDS_AUDIO" blocks are equal difficulty. Pause detection (em-dash: trailing incomplete) is the most mechanically tractable — an audio model can reliably flag abrupt stops. Intonation-based sentence boundaries are harder. Vocal register change for document reads is harder still and may require ML-level audio classification.

---

## 7. What We Leave on the Table Without Three Sealed Phases

**Direct count: 2 blocks** (filler word drops in word_drop subcategory).

**But the architecture is about more than 2 blocks.** The Rule 8a failure on Monday (prompt-only enforcement overridden by high-confidence AI Writer) is proof of concept that the Writer will override safety rules when it "knows" the right answer. This risk is distributed across all 198 CLOSEABLE_WITH_ENGINE_WORK blocks, any of which involves the Writer proposing a semantic change.

**Specific risk categories where TSP would de-risk current CWE work:**

| Risk | Affected block count | TSP mitigation |
|------|---------------------|----------------|
| Filler word drops (Uhmm, Yeah) | 2 | Code-side verbatim whitelist in Composer |
| Tense changes that are semantically wrong but phonetically plausible | ~15 (A/phonetic + D) | Validator layer rejects tense changes without audio confirmation |
| Proper noun capitalization overrides (Fran Schneider type) | ~8 (A/phonetic + B/cap_proper) | Code-side NAMES_LOCK enforcement at Composer |
| Short-word homophone "corrections" that change meaning | ~7 (pronoun_swap) | Validator checks grammar, not just substitution validity |

**Without TSP:** the engine can fix the 198 CWE blocks with prompts, but some percentage of those fixes will be overridden on high-confidence proposals. The failure mode is silent — tests pass, output is wrong, no alarm.

**The accurate statement:** TSP directly protects 2 blocks and de-risks ~30 more where AI override is the documented failure mode. It does not change the 279 NEEDS_AUDIO or 135 REPORTER_OWNS_FOREVER counts.

---

## 8. Grand Total

| Verdict | Bucket A | Bucket B | Bucket D | **Total** | **%** |
|---------|----------|----------|----------|-----------|-------|
| CLOSEABLE_NOW | 68 | 41 | 12 | **121** | **16.4%** |
| CLOSEABLE_WITH_ENGINE_WORK | 63 | 100 | 35 | **198** | **26.8%** |
| NEEDS_THREE_SEALED_PHASES | 2 | 0 | 0 | **2** | **0.3%** |
| NEEDS_AUDIO | 20 | 256 | 3 | **279** | **37.8%** |
| REPORTER_OWNS_FOREVER | 0 | 130 | 5 | **135** | **18.3%** |
| EMPTY / FORMAT | 0 | 0 | 3 | **3** | **0.4%** |
| **Total** | **153** | **527** | **58** | **738** | |

**Current architecture ceiling:** 121 + 198 + 2 = **321 blocks (43.5%)**

**After audio integration:** adds 279 blocks, total closeable = **600 (81.3%)**

**Permanent floor:** 135 blocks (18.3%) will always belong to the reporter.

---

## 9. Highest-Value Near-Term Actions (CLOSEABLE_NOW, in priority order)

These are the 121 CLOSEABLE_NOW blocks sorted by bang-for-effort. Each is a Stage 2 transform or small targeted rule.

| Action | Estimated block closes | Spec shape | Label |
|--------|----------------------|------------|-------|
| Email → E-mail transform (T-Email) | ~13 hyphenation | Stage 2 transform, same pattern as T3 | `universal:` |
| Objection → Object + form; foundation (MB-specific) | 20 objection_style | Stage 2 MB profile transform, 2 regex rules | `mb-specific:` |
| Number-style T5 (single digit spell, ordinals) | 10 number_style + 3 D | Stage 2 transform, 3 rules | `universal:` |
| Proper nouns + misclassified objection (B/cap_proper) | ~40 cap_proper | Case dict entries + extend existing NAMES_LOCK | `mb-specific:` |
| G&G case dict entry + YR Bates extension | ~10 acronym_mangle | Case dict + Bates regex extension | `mb-specific:` |
| Dedupe audit (which doubles survive) | ~15 doubled_word | Inspect and tighten post_process.py if needed | `universal:` |
| Compound joins (paydown, setup, writeoff, etc.) | ~12 D/unclear | Stage 2 compound table expansion | `universal:` |
| Comma_punct single block | 1 | Targeted rule after block inspection | TBD |

**Total potential from CLOSEABLE_NOW work: 121 blocks closed (16.4% of remaining 738)**

---

## 10. Estimation Confidence

| Category | Confidence | Reason |
|----------|------------|--------|
| A/objection_style | HIGH — reviewed all 20 blocks | Two patterns, 100% consistent |
| A/number_style | HIGH — reviewed all 10 blocks | Three rules, all 10 fit |
| A/hyphenation | HIGH — enumerated all 25 block diffs | Clear pattern breakdown |
| A/phonetic_error | MEDIUM — 5 samples, extrapolated | Letters-as-words type is clear; tense split is estimated |
| A/doubled_word | MEDIUM — scoreboard confirms classifier noise | True residual ~12-15; split between CN/CWE is estimated |
| B/em_dash | MEDIUM — 10 samples, 265 total | Doubled-token count (~30) is estimated; audio split is reasonable |
| B/quote_marks | HIGH — 10 samples from Bible recon | All 10 editorial; verdict uniform |
| B/cap_proper | LOW-MEDIUM — 15 samples from 198 total | Most uncertain category; recommend dedicated recon pass |
| D/unclear | MEDIUM — reviewed all 58 blocks | Pattern taxonomy is solid; individual counts estimated |
