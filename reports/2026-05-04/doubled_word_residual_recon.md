# RECON — doubled_word Residuals (28 blocks)
**Date:** 2026-05-04
**Analyst:** Claude Sonnet
**Source:** `io/analysis/halprin_full/_diff_out/block_classification.json`
**Morning fix:** D-DOUBLED-WORD — `dedupe_consecutive_duplicates` in `transforms/post_process.py`
**DO NOT SPEC. DO NOT CODE. Recon findings only.**

---

## Morning Fix Behavior (constraints)

`dedupe_consecutive_duplicates` removes consecutive identical tokens under these rules:
- **Adjacent only**: tokens must be directly next to each other (no gap words between)
- **Short-skip**: tokens < 3 chars are skipped ("be", "to", "on", "in", "I", "of")
- **Safelist**: "the", "that", "is", "had" are never deduped
- **Sentence boundary**: `word. CapitalWord` is NOT deduped (period + capital = new sentence)
- **Case-insensitive**: "Mark" + "mark" → deduped
- **Possessives**: `'s` stripped before comparison

---

## Classification of 28 Blocks

### Category 1 — WILL_RESOLVE (re-render picks these up, 14 blocks)

These contain adjacent identical tokens ≥ 3 chars, not in safelist, not sentence-boundary.
The morning fix will eliminate them when halprin_full re-renders. Not true residuals.

| Block | Duplicate | Notes |
|-------|-----------|-------|
| #28 | "They They were" | Adjacent 4-char, not safelist |
| #186 | "Mark Mark" | Adjacent 4-char, not safelist |
| #190 | "Mark mark" | Case-insensitive match |
| #239 | "two two" | Adjacent 3-char, not safelist |
| #240 | "guess guess" | T12 regression — confirmed |
| #331 | "was was" | Adjacent 3-char, not safelist |
| #349 | "you you" | Adjacent 3-char, not safelist |
| #386 | "any any" | Adjacent 3-char, not safelist |
| #396 | "they they" | Adjacent 4-char, not safelist |
| #416 | "foundation. foundation." | T12 regression pattern; also has pronoun_swap component |
| #488 | "role role" | Adjacent 4-char, not safelist |
| #635 | "foundation. foundation." | T12 regression pattern |
| #664 | "foundation. foundation." | T12 regression pattern |
| #665 | "foundation. foundation." | T12 regression pattern |
| #705 | "foundation. foundation." | T12 regression pattern |

**Net: 15 blocks resolve on re-render.** After re-render, the Bucket A doubled_word count should drop from 28 to ~13.

---

### Category 2 — REAL_ENGINE_BUG (fix genuinely misses, 8 blocks)

These are real steno duplicates the morning fix cannot catch due to design constraints.

| Block | MB | OUR (our_added) | Gap pattern | Why fix misses |
|-------|-----|-----------------|-------------|----------------|
| #24 | `mid-1980's.` | `mid1980's.`, `next?` | "next" repeated at sentence end after garble | Non-adjacent (buried in full sentence) |
| #81 | (none) | `--`, `to` | "to -- to do" | `--` between the two "to" — not adjacent |
| #100 | (none) | `be` | "to be be hard copy" | "be" = 2 chars → short-skip rule |
| #185 | (none) | `YR`, `46`, `on`, `on`, `28.` | "on on" inside Bates garble | "on" = 2 chars → short-skip rule |
| #339 | `option`, `into` | `opportunity`, `from`, `to`, `equity` | "equity equity" at tail of garbled sentence | Mixed phonetic errors make adjacency unclear; also has non-"equity" tokens between |
| #388 | `Westlake` | `any` | "caused any any of" | "any" = 3 chars — wait, should catch. Let me re-check: "any" is in the fix scope. Actually this may RESOLVE on re-render too. |
| #617 | (none) | `the` | "the the letter" | "the" IS in the safelist → never deduped |
| #715 | `an` | `inperson` | "in-person inperson meeting" | Variant forms (hyphenated vs joined) — not identical tokens |

**Correction on #388:** "any" is 3 chars and NOT in the safelist. The morning fix WOULD catch "any any". Moving #388 to WILL_RESOLVE. Updated net: **7 REAL_ENGINE_BUG.**

**Revised WILL_RESOLVE count: 16 blocks. REAL_ENGINE_BUG: 7 blocks.**

Confirmed REAL_ENGINE_BUG blocks: **#24, #81, #100, #185, #339, #617, #715**

#### Gap pattern breakdown:

**Gap 1 — Short word (2 chars): #100, #185**
- "be be", "on on" — both 2-char words blocked by short-skip
- The short-skip rule prevents false positives on "to be", "be prepared", etc.
- But "be be" and "on on" in steno output are always errors

**Gap 2 — Safelist word: #617**
- "the the letter" — "the" is in SAFE_LIST, never deduped
- Safe-list was added to prevent false positives on "the the way" type phrases
- But "the the" in steno output is always an error (witnesses don't say "the the")

**Gap 3 — Non-adjacent duplicate: #81, #24**
- "to -- to do" and "next... next?" — punctuation or other tokens between duplicates
- Current fix is single-pass adjacent-only; cannot catch with gap words between

**Gap 4 — Variant-form duplicate: #715**
- "in-person inperson" — hyphenated vs joined form of same compound
- Requires normalization before comparison

---

### Category 3 — EDITORIAL (misclassified by doubled_word heuristic, 5 blocks)

Not real doubled-word bugs. The classifier fired on surface patterns that look like doubles
but are editorial or style differences.

| Block | MB | OUR | Why misclassified |
|-------|-----|-----|-------------------|
| #23 | `O-d-e-c-o.` | `Odeco.` | MB spelled name letter-by-letter on first reference (editorial). Both versions have "Odeco" in full line; classifier saw two "Odeco" tokens |
| #169 | `Object form and` | `Objection form; foundation.` | "foundation." doubled in OUR is objection_style artifact, not steno double |
| #462 | `form.` | `form; argumentative.` | "Argumentative. Argumentative." — sentence boundary (capital after period), not caught by fix anyway |
| #615 | `Object form and` | `of Objection form;` | Objection_style artifact |
| #717 | `E-mail` | `Email` | Hyphenation style (E-mail vs Email) — single-word diff, not a doubled word at all |

---

## Summary Table: All 28 Blocks

| # | Block | Category | Gap / Reason |
|---|-------|----------|--------------|
| 1 | #23 | EDITORIAL | MB spelled-out form (first reference style) |
| 2 | #24 | REAL_ENGINE_BUG | Non-adjacent — "next?" buried at sentence end |
| 3 | #28 | WILL_RESOLVE | "They They" — caught by morning fix |
| 4 | #81 | REAL_ENGINE_BUG | Non-adjacent — "to -- to" with em-dash between |
| 5 | #100 | REAL_ENGINE_BUG | Short-skip — "be" (2 chars) |
| 6 | #169 | EDITORIAL | Objection_style artifact misclassified |
| 7 | #185 | REAL_ENGINE_BUG | Short-skip — "on" (2 chars) in Bates garble |
| 8 | #186 | WILL_RESOLVE | "Mark Mark" — caught by morning fix |
| 9 | #190 | WILL_RESOLVE | "Mark mark" case-insensitive — caught |
| 10 | #239 | WILL_RESOLVE | "two two" — caught by morning fix |
| 11 | #240 | WILL_RESOLVE | "guess guess" — T12 regression, confirmed |
| 12 | #331 | WILL_RESOLVE | "was was" — caught by morning fix |
| 13 | #339 | REAL_ENGINE_BUG | Mixed phonetic + "equity equity" non-adjacent |
| 14 | #349 | WILL_RESOLVE | "you you" — caught by morning fix |
| 15 | #386 | WILL_RESOLVE | "any any" — caught by morning fix |
| 16 | #388 | WILL_RESOLVE | "any any" — 3 chars, not safelist, caught |
| 17 | #396 | WILL_RESOLVE | "they they" — caught by morning fix |
| 18 | #416 | WILL_RESOLVE | "foundation. foundation." component caught; pronoun_swap is separate |
| 19 | #462 | EDITORIAL | "Argumentative. Argumentative." — sentence boundary |
| 20 | #488 | WILL_RESOLVE | "role role" — caught by morning fix |
| 21 | #615 | EDITORIAL | Objection_style artifact |
| 22 | #617 | REAL_ENGINE_BUG | Safelist — "the" is in SAFE_LIST |
| 23 | #635 | WILL_RESOLVE | "foundation. foundation." — caught |
| 24 | #664 | WILL_RESOLVE | "foundation. foundation." — caught |
| 25 | #665 | WILL_RESOLVE | "foundation. foundation." — caught |
| 26 | #705 | WILL_RESOLVE | "foundation. foundation." — caught |
| 27 | #715 | REAL_ENGINE_BUG | Variant-form — "in-person" ≠ "inperson" |
| 28 | #717 | EDITORIAL | Hyphenation style (E-mail vs Email), not a double |

**Totals: 16 WILL_RESOLVE · 7 REAL_ENGINE_BUG · 5 EDITORIAL**

Expected Bucket A doubled_word count after re-render: **28 − 16 = 12** (minus ~2 EDITORIAL
that may re-classify, net ~10–12 true residuals).

---

## Pattern Recommendations for Follow-on Fix

### Fix 1 — Remove "the" from SAFE_LIST (LOW RISK, HIGH CONFIDENCE)

**Blocks fixed:** #617 (and any future "the the" steno doubles).
**Code location:** `src/mrx_engine_v1/transforms/post_process.py` — `SAFE_LIST` constant.
**Change:** Remove "the" from SAFE_LIST.
**Rationale:** Witnesses never intentionally say "the the." The safe-list was conservative.
The test T5 tests "that that" (stays in safelist); "the" can be removed independently.
"the the" in steno output is always a duplicate capture.
**Risk:** Very low. Only fires on adjacent "the the" — no legitimate testimony case.
**Verdict: CHEAP FIX. Worth adding before re-render. ~2 lines of code.**

### Fix 2 — Add "be" and "on" as short-word exceptions (MODERATE RISK)

**Blocks fixed:** #100 ("be be"), #185 ("on on").
**Change:** Add "be" and "on" to a 2-char dedup exception list (distinct from SAFE_LIST).
**Rationale:** Neither "be be" nor "on on" appears in legitimate testimony.
**Risk:** "be" could appear in "to be or not to be" style adjacent phrases (unlikely in
deposition). "on on" is harder to imagine in context. Risk is low but not zero.
**Verdict: WORTH CONSIDERING but not a slam dunk. Total: 2 blocks. Assess with Scott.**

### Fix 3 — Non-adjacent near-duplicates (HIGH COMPLEXITY, DON'T DO NOW)

**Blocks fixed:** #81, #24 (2 blocks).
**Pattern:** word + `--` + same word → dedupe.
**Risk:** Witnesses DO intentionally repeat after a pause ("I was -- I was there"). This is
the VERBATIM rule — steno captures both halves. Cannot safely auto-dedup without knowing
if the steno was capturing two distinct utterances.
**Verdict: BACKLOG. Not before re-render.**

### Fix 4 — Variant-form normalization (LOW YIELD)

**Blocks fixed:** #715 (1 block).
**Pattern:** Normalize hyphenated form before comparison.
**Verdict: BACKLOG. 1 block doesn't justify complexity before re-render.**

---

## Verdict

**Is there a cheap follow-on fix worth piling on before the re-render?**

**YES — Fix 1 only:** Remove "the" from SAFE_LIST. 1–2 lines, zero risk, fixes a real class
of steno double that the safelist was too cautious to handle.

**NO on everything else** — the remaining REAL_ENGINE_BUG residuals (7 blocks → ~4 after
accounting for #339 being mixed and #388 resolving) are either complex to fix (non-adjacent),
risky to touch (short-word exceptions), or too narrow (variant-form).

After re-render with the morning fix + Fix 1 (if Scott approves), expected doubled_word
Bucket A residuals: **~10 blocks**, down from 28. That's a significant improvement.
The remaining ~10 are the hard cases that require more targeted work or represent true
steno ambiguity (witness self-corrections the VERBATIM rule should protect).
