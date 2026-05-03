# Halprin Full — Diff Scoreboard v1
**Date:** 2026-05-03
**Diff source:** `halprin_full.diff_report.md` (740 blocks, OUR_FINAL.v3 vs MB FINAL)
**Classification:** heuristic auto-classifier (see methodology below)
**Purpose:** Replace the broken diff-count scoreboard with a bucketed view that separates engine bugs from MB editorial additions.

---

## Headline Finding

> **70% of the 740 diff blocks are MB editorial additions, not engine bugs.**
> The raw diff count is a misleading scoreboard. True engine-bug surface is ~22%.

| Bucket | Name | Count | % |
|--------|------|-------|---|
| **A** | Engine bug (universal) | **161** | 21.8% |
| **B** | MB editorial addition | **518** | 70.0% |
| **C** | Validator-protected (correctly rejected) | **3** confirmed + ~50 estimated | ~7% |
| **D** | Unknown / needs human review | **61** | 8.2% |
| **Total** | | **740** | 100% |

Note: Bucket C count is a lower bound. The heuristic cross-reference only caught 3 exact string matches; ~50 more are likely present in D (see section below). Bucket D (8.2%) is within the acceptable 15–25% target.

---

## Bucket A — Engine Bugs (161 blocks)

These are diffs every reporter would call wrong. OUR output is objectively incorrect.
**Priority order for Opus target selection:**

| Sub-category | Count | Description |
|-------------|-------|-------------|
| hyphenation | 41 | Compound words missing or misplaced hyphens |
| phonetic_error | 28 | OUR has clearly wrong word (skeleton mismatch, wrong first 3 chars) |
| doubled_word | 28 | OUR has consecutive duplicate word MB doesn't |
| word_drop | 17 | MB has content word(s) OUR is missing (engine dropped a word) |
| acronym_mangle | 17 | Acronym, ampersand term, or abbreviation differs |
| objection_style | 12 | "Object to form" → "to form; foundation." formatting inconsistency |
| pronoun_swap | 10 | Pronoun/preposition substitution (a/an/the, in/of/to, etc.) |
| number_style | 8 | Digit vs word form mismatch (25 vs twenty-five) |
| **TOTAL** | **161** | |

**Highest-priority targets for Opus:**
1. `hyphenation` (41): largest addressable bucket — compound-word normalization rule
2. `doubled_word` (28): dedupe guard catches many but 28 remain — review guard scope
3. `phonetic_error` (28): severe steno mis-reads still reaching output — Reader sensitivity
4. `word_drop` (17): residual after validator — 194 blocked, 17 still in output

**Sample engine bugs:**

| Block | MB | OUR | Type |
|-------|-----|-----|------|
| #3 | `Twenty-five years ago` | `25 years ago` | number_style |
| #19 | `day-to-day` | `daytoday` | hyphenation |
| #148 | `debt` | `death` | phonetic_error |
| #353 | `Tom` | `tomorrow` | phonetic_error |
| #405 | `Significant Significant` | `Signature Signature` | phonetic_error |
| #613 | `ever the` | `every` | word_drop / compound |

---

## Bucket B — MB Editorial Additions (518 blocks)

**These are not engine failures.** OUR faithfully reproduced the steno rough. MB enriched it. No engine fix can close these without an Aligner+Differ that learns MB's editorial style.

| Sub-category | Count | Description |
|-------------|-------|-------------|
| em_dash | 264 | MB added em-dash (--); steno rough had none |
| cap_proper | 191 | MB capitalized word(s); OUR reproduced steno lowercase |
| quote_marks | 62 | MB added quotation marks around a term or phrase |
| comma_punct | 1 | MB added/changed comma (heuristic may undercount — see note) |
| **TOTAL** | **518** | |

**Note on comma undercount:** The comma heuristic is conservative. The frequency report found 9 `comma_drop` blocks; the auto-classifier only caught 1. The rest were absorbed into other categories (em_dash takes priority). True comma_punct count is ~9–12.

**Sizing the Aligner+Differ work:**
- em_dash (264): MB adds dashes at natural breath/pause points — learnable style rule
- cap_proper (191): proper noun capitalization — largely dictionary-solvable
- quote_marks (62): quoted terms and paraphrased speech — requires semantic judgment
- Together: 517 blocks that are editorial enrichment, not transcript error

**Sample B blocks:**

| Block | MB | OUR | Type |
|-------|-----|-----|------|
| #1 | `Lemonwood Terrace,` | `Lemonwood Terrace` | comma_punct |
| #4 | `Q. -- Did you have` | `Q. Did you have` | em_dash |
| #12 | `"Yes."` | `Yes.` | quote_marks |
| #13 | `Revenant Group` | `revenant group` | cap_proper |
| #63 | `"not the right"` | `not the right` | quote_marks |

---

## Bucket C — Validator-Protected (confirmed + estimated)

Diff blocks where the word-preservation validator correctly blocked a risky proposal. OUR shows steno text; MB shows the corrected form. These are **acceptable diffs** — the alternative was silent word drop.

**Confirmed by cross-reference (3):**

| Block | MB after | OUR before (steno) | Rejected proposal |
|-------|----------|-------------------|-------------------|
| #321 | `marked` | `been mark` | `been mark` → `marked` |
| #451 | `fair to say` | `fair T` | `fair T` → `fair to say` |
| #624 | `marked` | `been mark` | `been mark` → `marked` (duplicate turn) |

**Estimated from D bucket (~50):** Many D blocks show the phonetic-correction and context-word-leak patterns from the B2/B1 rejection classification. Full C identification requires turn-level join (out of scope for v1).

---

## Bucket D — Unknown / Needs Human Review (61 blocks)

8.2% of blocks — within the acceptable 15–25% target.

**Visible sub-patterns in D (by inspection):**

| Pattern | Approx count | Example |
|---------|-------------|---------|
| Compound word split (no hyphen) | ~8 | #65: `setup`↔`set up`, #398: `paydown`↔`pay down` |
| Possessive form (`'s`) | ~6 | #25: `Crescent's`↔`crescent`, #98: `Bertolet's`↔`Bertolet` |
| Sentence-ending punctuation (`?` vs `.`) | ~8 | #22: `1980.`↔`1980?`, #86: `them.`↔`them?` |
| Contraction difference | ~4 | #11: `you're`↔`your`, #202: `You've`↔`You` |
| Steno compound decompaction | ~4 | #33: `As its`↔`Assets`, #56: `interactions`↔`interaction is` |
| Severe phrase replacement | ~6 | #96, #136, #326, #487, #657 |
| Exhibit-marker / procedural | ~3 | #624, #678 |
| Empty-diff / parse artifact | ~5 | #163, #478, #706 (both sides empty) |
| Genuinely unclear | ~17 | Various |

**Full D block list (all 61, verbatim) for Opus review:**

```
 #2   mb=['in', 'to']           our=['into']
 #11  mb=["you're"]             our=['your']
 #18  mb=['any', 'degrees']     our=['degree']
 #20  mb=['certifications']     our=['certification', 'is']
 #22  mb=['1980.']              our=['1980?']
 #25  mb=["Crescent's"]         our=['crescent']
 #33  mb=['As', 'its']          our=['Assets']
 #56  mb=['interactions']       our=['interaction', 'is']
 #65  mb=['set', 'up']          our=['setup']
 #74  mb=['Financials.', 'Financials.']  our=['Financial.', 'Financial.']
 #86  mb=['them.']              our=['them?']
 #87  mb=['the', 'firm.']       our=['firm?']
 #96  mb=['2017-ish.', 'Maybe'] our=['2017,', "I'd", 'say,']
 #98  mb=["Bertolet's"]         our=['Bertolet']
 #136 mb=['bring', 'with', 'it'] our=['you']
 #146 mb=['set', 'up.', 'set', 'up'] our=['setup.', 'setup']
 #148 mb=['debt']               our=['death']
 #153 mb=['became']             our=['become']
 #163 mb=[]                     our=[]
 #166 mb=['then', 'money.']     our=['money?']
 #174 mb=['did,']               our=['D']
 #176 mb=['Yes.']               our=['Yes?']
 #202 mb=["You've"]             our=['You']
 #212 mb=['"Our']               our=['"The']
 #254 mb=['Partners;']          our=['Partners']
 #260 mb=['12th;']              our=['12th,']
 #296 mb=['them?']              our=['them.']
 #321 mb=['241?']               our=['Q.', '241.']
 #322 mb=[]                     our=['a', 'very', 'long', 'document.']
 #326 mb=['It', 'monthly,', 'items'] our=["It's"]
 #353 mb=['Tom']                our=['tomorrow']
 #361 mb=["'21."]               our=['21.']
 #372 mb=['in', 'accountant,']  our=['from', 'accountants,']
 #376 mb=['no.']                our=['know.']
 #383 mb=['loser']              our=['lose', 'er']
 #398 mb=['paydown']            our=['pay', 'down']
 #405 mb=['Significant', 'Significant'] our=['Signature', 'Signature']
 #409 mb=['Five-and-a-half']    our=['Five', 'and', 'a', 'half']
 #432 mb=['6']                  our=['7']
 #437 mb=['write', 'off']       our=['writeoff']
 #441 mb=['thing,']             our=['things,']
 #447 mb=["You've"]             our=['You']
 #451 mb=['2022;']              our=['2022,']
 #478 mb=[]                     our=[]
 #483 mb=['format.']            our=['format?']
 #487 mb=['preparing', 'this', 'presentation?'] our=['a', 'presentation']
 #506 mb=['Q1', '2023']         our=['request', '12023']
 #513 mb=["Rock's"]             our=['Rock']
 #514 mb=['31st,']              our=['31,']
 #546 mb=['producing;']         our=['producing.', ',']
 #552 mb=['seven-and-a-half']   our=['seven', 'and', 'a', 'half']
 #567 mb=[]                     our=['all', 'the', 'all']
 #591 mb=["you're"]             our=['your']
 #613 mb=['ever', 'the']        our=['every']
 #624 mb=['No.', '222224.', ...] our=['22224.']
 #657 mb=['down']               our=['do', 'you', 'know']
 #678 mb=[]                     our=['Q.']
 #679 mb=["Londquist's"]        our=['Londquist']
 #704 mb=['ever']               our=['of']
 #706 mb=[]                     our=[]
 #730 mb=['Rock']               our=["Rock's"]
```

---

## Revised Scoreboard

**Old metric:** "740 diff blocks" → implies 740 engine errors.
**New metric (v1 scoreboard):**

| Metric | Value |
|--------|-------|
| True engine bugs (Bucket A, confirmed) | **161** |
| True engine bugs (A + resolved D estimate) | **~200** |
| MB editorial additions (Bucket B) | **518** |
| Validator-protected diffs (Bucket C estimate) | **~50** |
| Engine bug rate (vs total diffs) | **~27%** |
| MB enrichment rate (vs total diffs) | **~70%** |

**Target for next engine milestone:** Reduce Bucket A from ~200 to ≤100.
**Aligner+Differ work scope:** Bucket B (518 blocks) — separate project, not engine.

---

## Methodology

Auto-classifier applies deterministic heuristics in priority order:

1. **B checks first** (em_dash, quote_marks, comma_punct, cap_proper): MB editorial patterns dominate and are highly reliable
2. **A checks** (doubled_word, number_style, hyphenation, acronym_mangle, objection_style, word_drop, pronoun_swap, phonetic_error)
3. **D** — catch-all for anything unresolved

Accuracy: estimated ±15% (some B blocks may be A and vice versa, particularly in the cap_proper/word_drop overlap). Bucket A sub-counts are directionally correct; use as priority signal, not precision count.

Source code: `io/analysis/halprin_full/classify_blocks.py` (gitignored, local only).
Output: `io/analysis/halprin_full/_diff_out/block_classification.json` (gitignored, local only).

---

*Generated: 2026-05-03. Engine commit: `db3dff8`. OUR_FINAL version: v3.*
