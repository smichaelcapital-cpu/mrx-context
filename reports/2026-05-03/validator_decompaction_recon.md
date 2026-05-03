# Validator Decompaction Recon — D-VALIDATOR-DECOMPACTION (Fix A candidate)
**Date:** 2026-05-03
**Session:** Sunday evening
**Analyst:** Sonnet
**Source:** `src/mrx_engine_v1/validate_ops/word_preservation.py`
**Rejections:** `io/analysis/halprin_full/_stage3_1_out/_word_preservation_rejections.jsonl`

---

## Upfront: Afternoon Recommendation Was Wrong

The hyphenation spot-check report recommended "Option A: validator decompaction extension" as the fix for these 6 blocks. **That recommendation is wrong.** This recon shows the validator is correct in every rejection, and the root cause is in the Writer's proposal spans. Recommendation flipped to **Option B: Writer-side fix**. Full reasoning below.

---

## Step 1 — Validator Code Walkthrough

### Key design: tokenizer strips hyphens

```python
_PUNC_STRIP = str.maketrans("", "", '.,!?";:-\'')
```

The hyphen (`-`) is included in the strip set. Code comment confirms intent:

> "Hyphen included so 'ten-minute' and 'tenminute' tokenize identically,
> satisfying edge-case 4 (hyphenated compounds)."

**This means the validator already handles compound recognition.** When a proposal is:
- `before`: "tenminute" → tokenized to `["tenminute"]`
- `after`:  "ten-minute" → tokenized to `["tenminute"]` (hyphen stripped)

Direct match succeeds. "tenminute" is accounted for. No decompaction extension is needed.

### The two gates that matter

**Rule 1 (line 161):** If `len(before_words) <= 1` → return None (skip, no rejection).
Single-word spans are pure substitutions. No drop is possible.

**Majority threshold (line 181):** `if accounted_count / len(before_words) < 0.5 → return None`.
Threshold is STRICT — 0.50 is NOT less than 0.50, so a 1/2 ratio does NOT skip. This is important (see below).

### The _consonant_skeleton helper

```python
def _consonant_skeleton(text):
    return "".join(c for c in text.lower() if c.isalpha() and c not in VOWELS)
```

Digits are NOT alpha — they produce empty skeletons. So `_consonant_skeleton("20172018") == ""`.
This means digit-only compounds like `20172018` cannot be matched via skeleton — only via direct match or number normalization.

---

## Step 2 — Rejection Records for All 6 Blocks

5 rejection records found. Blocks 191 and 389 have no rejection records (Writer never proposed a fix for those turns).

### Record 1 — Block 189 / turn 1034

```json
{
  "turn_idx": 1034, "proposal_id": "p_0020",
  "before": "that 20172018", "after": "2017-2018",
  "dropped_words": ["that"]
}
```

**Gate trace:**
- `before_words = ["that", "20172018"]`  len=2 → Rule 1 does not skip
- `after_words  = ["20172018"]`  (hyphen stripped: "2017-2018" → "20172018")
- `after_skel   = ""`  (digits have no consonant skeleton)
- `"that"`: direct=No, num=No, skel="tht"(len=3) but "tht" not in "" → NOT accounted
- `"20172018"`: direct=Yes → accounted
- `accounted=1/2=0.50` — NOT < 0.50 → majority threshold does not save it → **REJECT**

---

### Record 2 — Block 221 / turn 1161

```json
{
  "turn_idx": 1161, "proposal_id": "p_0032",
  "before": "the 20172018,", "after": "2017-2018",
  "dropped_words": ["the"]
}
```

**Gate trace:**
- `before_words = ["the", "20172018"]`  (comma stripped)
- `"the"`: skel="th"(len=2), "th" not in "" → NOT accounted
- `"20172018"`: direct match → accounted
- `accounted=1/2=0.50` → **REJECT**

---

### Record 3 — Block 191 or 389 / turn 1995

```json
{
  "turn_idx": 1995, "proposal_id": "p_0015",
  "before": "in 20172018,", "after": "2017-2018",
  "dropped_words": ["in"]
}
```

**Gate trace:**
- `before_words = ["in", "20172018"]`
- `"in"`: skel="n"(len=1) → below _SKEL_MIN_LEN=2 → skeleton check skipped → NOT accounted
- `"20172018"`: direct match → accounted
- `accounted=1/2=0.50` → **REJECT**

Mapping note: This rejection's "in 20172018," context does not match block 191's text ("other than 20172018?") or block 389's text ("MR. CAUGHEY: 20172018."). This may be a DIFFERENT turn with "20172018" that isn't represented as its own diff block (i.e., the proposal would have introduced a new error, but the turn's output matches OUR_FINAL for this block and isn't in the diff). This cannot be confirmed without full turn-level output access.

---

### Record 4 — Block 345 / turn 1798

```json
{
  "turn_idx": 1798, "proposal_id": "p_0004",
  "before": "in daytoday", "after": "day-to-day",
  "dropped_words": ["in"]
}
```

**Gate trace:**
- `before_words = ["in", "daytoday"]`
- `after_words  = ["daytoday"]`  (hyphen stripped: "day-to-day" → "daytoday")
- `after_skel   = "dytdy"`
- `"in"`: skel="n"(len=1) → skeleton check skipped → NOT accounted
- `"daytoday"`: direct match → accounted
- `accounted=1/2=0.50` → **REJECT**

Block 345 diff context:
- OUR: "Did he personally take **in** **daytoday** role..."
- MB:  "Did he personally take **on** **a** **day-to-day** role..."

Note: "in" → "on a" is a separate phonetic/word-substitution issue, independent of the compound fix.

---

### Record 5 — Block 728 / turn 3550

```json
{
  "turn_idx": 3550, "proposal_id": "p_0010",
  "before": "a tenminute", "after": "ten-minute",
  "dropped_words": ["a"]
}
```

**Gate trace:**
- `before_words = ["a", "tenminute"]`
- `after_words  = ["tenminute"]`  (hyphen stripped)
- `after_skel   = "tnmnt"`
- `"a"`: skel="" (pure vowel, len=0) → skeleton check skipped → NOT accounted
- `"tenminute"`: direct match → accounted
- `accounted=1/2=0.50` → **REJECT**

---

### Blocks 191 and 389 — No Rejection Records

Searched all 194 rejections. Only 3 records contain "20172018". Blocks 191 and 389 have no corresponding rejection:

- **Block 191**: "from sometime other than 20172018?" — contains TWO issues (sometime + 20172018?). Writer never proposed a fix for this turn at all.
- **Block 389**: "MR. CAUGHEY: 20172018." — standalone attorney utterance. Writer never proposed a fix for this turn.

These two blocks are NOT validator-blocked. They are REAL_ENGINE_BUG of the simpler kind: the Writer never tried to fix them.

---

## Step 3 — Per-Block Verdicts

### Verdict key (as defined in the probe)
- **PROPOSAL_GOOD** — proposal drops a word MB also drops; validator wrong to block
- **PROPOSAL_BAD** — proposal drops a word MB keeps; validator right to block
- **PROPOSAL_PARTIAL** — compound fix is right, span is too wide; Writer should narrow

---

| Block | Rejected turn | Dropped word | MB's output has that word? | Verdict |
|-------|--------------|-------------|---------------------------|---------|
| 189 | 1034 | "that" | Yes — "...in **that** 2017-2018 period..." | PROPOSAL_PARTIAL |
| 221 | 1161 | "the" | Yes — "...during **the** 2017-2018, 2021 period..." | PROPOSAL_PARTIAL |
| 191 or 389 | 1995 | "in" | Mapping unclear (see record 3 note) | PROPOSAL_PARTIAL |
| 345 | 1798 | "in" | No — MB has "on" not "in"; but "on a" still fills the slot | PROPOSAL_PARTIAL |
| 728 | 3550 | "a" | Yes — "...take about **a** ten-minute break..." | PROPOSAL_PARTIAL |
| 191 | (none) | n/a | Writer never proposed | REAL_ENGINE_BUG (no proposal) |
| 389 | (none) | n/a | Writer never proposed | REAL_ENGINE_BUG (no proposal) |

**All 5 rejections = PROPOSAL_PARTIAL.** Every case has the same structure:
1. The compound fix in the `after` is correct
2. The `before` span is exactly one word too wide — it grabbed the preceding article or preposition
3. That extra word IS preserved in MB's output (she kept "that", "the", "a")
4. The validator correctly flagged the extra word as dropped
5. The validator is doing its job

**Block 345 nuance:** "in" is dropped by the proposal AND "in" is wrong in our output (should be "on a"). However the proposal output would be just "day-to-day" with no article — also wrong (MB has "on a day-to-day"). The proposal conflated a phonetic word-sub fix with the hyphenation fix. It would have been wrong either way. PROPOSAL_PARTIAL still applies (the compound part was right, the span was too wide).

---

## Step 4 — Recommendation

### The verdict: Option B — Writer-side fix

**Option A (validator decompaction) is not the right fix.** Here is why:

1. **The validator already understands compounds.** The tokenizer strips hyphens, so "ten-minute" and "tenminute" tokenize identically. "20172018" matches "2017-2018" via direct match (after tokenization). There is no decompaction gap to close.

2. **The validator is correct in all 5 rejections.** The dropped words ("that", "the", "in", "a") are genuinely absent from the `after` and genuinely present in MB's output. If we added these to the EXPECTED_DROP allow-list or loosened the threshold, we would allow real word drops through on other proposals.

3. **The fix point is the Writer's span generation.** Every rejected proposal has the same structural bug: `before = [article] [compound]`, `after = [corrected-compound-only]`. The article falls out. If the Writer proposed `before = [compound]`, `after = [corrected-compound]` (single-word span), Rule 1 would immediately skip and the fix would pass.

4. **Narrow span = Rule 1 skip.** Confirmed by trace:
   - `before="20172018"` → `before_words=["20172018"]` len=1 → Rule 1 → SKIP → PASS
   - `before="tenminute"` → `before_words=["tenminute"]` len=1 → Rule 1 → SKIP → PASS
   - Same for "daytoday"

5. **Blocks 191 and 389 need the Writer to propose the fix at all.** These aren't blocked — they were never attempted. The Writer needs to detect the year-range pattern ("YYYYYYY" as concatenated digits) and generate a proposal.

### What the Writer prompt fix looks like (for Opus to spec)

The Writer prompt needs two additions for the hyphenation category:

**Addition 1 — Span discipline rule:**
When proposing a hyphenation fix (steno compound → hyphenated form), the `before` span must contain ONLY the compound word itself, not surrounding articles, prepositions, or context. Wrong: `"that 20172018"`. Right: `"20172018"`.

**Addition 2 — Year-range pattern detection:**
The Writer should recognize concatenated year ranges (four-digit string immediately followed by another four-digit string, e.g. `20172018`) as a steno artifact and propose the hyphenated form (`2017-2018`).

Block 345 (daytoday) is in the same Writer-fix bucket, but the "in"→"on a" word substitution is a SEPARATE defect and should NOT be addressed in the same proposal as the hyphenation fix.

### Is there anything that needs a validator change?

No. The validator behavior is correct and should not be changed for these cases.

There is one minor observation: the majority threshold `< 0.5` (strictly less than) means a 1/2 ratio (exactly one of two words accounted) still triggers rejection. This is intentional — the spec intended to catch the "one-position-too-wide" bug, which is precisely what's happening here. The threshold is calibrated correctly.

---

## Open Questions for Opus

1. **Block 191 compound issue**: "sometime" → "some time" is mixed in with the year-range fix. Should the Writer be prompted to handle "sometime" → "some time" splits in the same prompt rule as hyphenation, or is that a separate defect (word split, not hyphenation)?

2. **Block 345 isolation**: The "in"→"on a" phonetic error and the "daytoday"→"day-to-day" hyphenation are co-located in one diff block. The Writer fix (narrow span) would only fix the compound. The word-sub issue needs a separate proposal. Is that acceptable — partial fix via this spec, phonetic fix via a later spec?

3. **Year-range pattern scope**: The pattern is 8-digit string = concatenated YYYY+YYYY. How broadly should the Writer detect this? "20172018", "20172021", etc. — any adjacent 4+4 digit year pair? Or only specific known ranges?

4. **Proposal span discipline as a universal rule**: Should "narrow span for compounds" be a universal Writer prompt rule (prevents this class of error on all future hyphenation proposals), or targeted to the specific patterns (20172018, tenminute, daytoday)?

---

*Report generated: 2026-05-03 evening session*
