# RECON 2a — NAMES_LOCK Substring Matching
# Move A Pre-Build Gate

**Date:** 2026-05-02 evening
**Author:** Sonnet (sat1514session)
**Status:** COMPLETE — pending Scott + Opus review before code
**Spec parent:** 2026-05-02_MOVE_A_SPEC.md

---

## 1. What I looked at

- `io/analysis/halprin_mini/_stage3_1_out/rejections.jsonl` (12 drops, current run)
- `io/analysis/halprin_mini/_stage3_1_out/proposals.json` (all `after` values)
- `src/mrx_engine_v1/stage3/validate_ops.py` (check_word_budget implementation)
- `io/analysis/halprin_mini/_run_halprin_mini.py` (NAMES_LOCK set)

---

## 2. Current NAMES_LOCK (Halprin)

```
"Halprin", "Caughey", "Garner", "Muir", "Guastella", "Warren Seal",
"Lexitas", "Westlake", "Eagle", "Somerset", "Chevron", "W&T Offshore",
"Calcasieu", "Lemonwood Terrace"
```

---

## 3. How the current exemption works

In `check_word_budget` (validate_ops.py, V2.2):

```python
to_text = op.get("to", "").strip()
if to_text and to_text in names_lock:
    # exempt from word budget check
    return ValidationResult(True, ...)
```

This is a **set membership check** — exact match only. "W&T" is NOT a member of the set. "W&T Offshore" IS.

---

## 4. Failing proposals (word_budget_fail, W&T related)

All 5 come from the same batch of consecutive turns about W&T employment history.

| turn_idx | from (span text) | to | whole-turn ratio | MB FINAL form |
|---|---|---|---|---|
| 202 | "at with and T" | "W&T" | 78.6% (11/14) | "W&T" |
| 204 | "joined with and T" | "W&T" | 66.7% (6/9) | "W&T" |
| 206 | "with and T" | "W&T" | 66.7% (4/6) | "W&T" |
| 208 | "with with and T?" | "W&T" | 72.7% (8/11) | "W&T" |
| 210 | "at with and T?" | "at W&T" | 75.0% (6/8) | "W&T" |

All 5 propose the RIGHT form. All 5 fail because "W&T" and "at W&T" are not exact NAMES_LOCK members.

**Root cause in one line:** "W&T" is a word-boundary substring of NAMES_LOCK entry "W&T Offshore" but is not itself a NAMES_LOCK entry. The exemption only covers exact members.

---

## 5. Other word_budget_fail drops (NOT W&T, NOT affected by this fix)

| turn_idx | from | to | issue | notes |
|---|---|---|---|---|
| 159 | "MR. MADIGAN: Object to form." | "Objection to form." | house_style | Louisiana KB-001 rule. Separate issue. |
| 185 | "was crescent" | "Crescent" | case_dict | Span includes "was" — Writer overreaching span bounds. Separate issue. |
| 207 | "He in P" | "E&P" | case_dict | E&P not in NAMES_LOCK; 33.3% ratio. Separate issue — parked. |
| 219 | "He in P." | "E&P" | case_dict | Same E&P issue. |
| 261 | "there ENP?" | "their" | phonetic | Phonetic homophone; separate class. |

These 5 are NOT fixed by the substring exemption. They need separate rule work or are intentionally parked.

---

## 6. "Warren" partial-name scenario (spec example)

The spec asks about: raw token "Warren" alone → should propose "Warren Seal" (full NAMES_LOCK form).

**Halprin data says:** This scenario does NOT appear in the current 50-page run. Every Warren Seal reference in raw stage2 output uses the full two-word form "warren seal" (lowercase), never "warren" alone. The validate_ops exemption for Warren Seal already fires correctly (exact match after Writer proposes "Warren Seal").

**Verdict:** The "Warren" alone case is a valid theoretical edge case but has zero instances in Halprin mini. Implementing it would require new Reader-level detection (flag partial names for expansion). **Defer to Move B or later.** This recon confirms it is not blocking any current proposal.

---

## 7. "for W&T Offshore" edge case

Turn 110 produces `after: "for W&T Offshore"` — this contains "W&T Offshore" as a substring but is NOT itself in NAMES_LOCK. Yet it **passed** validate_ops.

**Why:** Turn 110 is long enough (16 words → 14 after replacement = 87.5%) that the word budget check passes without any exemption. The "for" prefix is inside the span, included in both `from` and `to`.

**Implication:** "for W&T Offshore" does not need the exemption. This edge case resolves itself at natural turn length.

---

## 8. Proposed fix (validate_ops.py only)

Replace the exact-match exemption check with a word-boundary substring check:

```python
def _names_lock_exempt(to_text: str, names_lock: Set[str]) -> bool:
    """Return True if to_text is an exact NAMES_LOCK member OR a
    word-boundary substring of one.

    Examples:
      "W&T Offshore" in {"W&T Offshore"} -> True (exact)
      "W&T" as substring of "W&T Offshore"  -> True (substring, word boundary)
      "at W&T" not substring of anything    -> False (prefix "at" not in NAMES_LOCK)
    """
    if to_text in names_lock:
        return True
    for name in names_lock:
        # Check if to_text matches a word-boundary segment of name
        # e.g., "W&T" is the first part of "W&T Offshore"
        parts = name.split()
        for i in range(len(parts)):
            for j in range(i + 1, len(parts)):
                segment = " ".join(parts[i:j])
                if segment == to_text:
                    return True
    return False
```

Then in `check_word_budget`:

```python
if names_lock:
    for op in ops:
        if op.get("op_type") != "REWORD":
            continue
        to_text = op.get("to", "").strip()
        if to_text and _names_lock_exempt(to_text, names_lock):
            warnings.append(...)
            return ValidationResult(True, warnings=warnings)
```

**This fixes:** turns 202, 204, 206, 208 (to="W&T" is a word-segment of "W&T Offshore").

**This does NOT fix:** turn 210 (to="at W&T") — "at W&T" contains "W&T" but is not a clean word-segment of any NAMES_LOCK entry. Fixing turn 210 requires either (a) stripping leading prepositions before the check, or (b) checking if any NAMES_LOCK segment appears WITHIN the `to` string.

---

## 9. Turn 210 edge case: "at W&T"

The `to` field is "at W&T" — the Writer included the preposition "at" in the span because it was inside the token_span. This is a Writer span-selection issue, not a validate_ops issue. Two possible fixes:

**Option A (validate_ops):** Check if any NAMES_LOCK entry appears as a suffix of `to_text` after stripping common prepositions (at, for, with, in, of, to). Simple, but fragile.

**Option B (Writer prompt):** Instruct Writer not to include leading prepositions in REWORD spans — span should start at the entity, not the preposition before it. Cleaner, but requires Writer prompt change.

**Recommendation:** Option B. Turn 210 is one miss. Writer prompt fix is the right long-term behavior. Don't patch validate_ops for leading-preposition edge case.

---

## 10. Summary table

| Issue | Turns affected | Fix location | Fix type |
|---|---|---|---|
| "W&T" not in NAMES_LOCK (exact) | 202, 204, 206, 208 | validate_ops | word-segment substring check |
| "at W&T" preposition-prefixed | 210 | Writer prompt | don't include leading prepositions in span |
| E&P not in NAMES_LOCK | 207, 219 | parked | out of A1 scope |
| Crescent span over-reach | 185 | parked | separate span issue |
| Louisiana objection form | 159 | parked | house_style separate |
| "Warren" alone (no instances) | 0 instances | defer | Move B |

---

## 11. Scope of change

- **Files touched by A1:** `src/mrx_engine_v1/stage3/validate_ops.py` only (plus new helper function in same file)
- **Tests to add:** 6+ cases in `tests/stage3/test_validate_ops_v2.py`
- **Writer prompt change needed:** Yes — strip leading prepositions from entity spans (turn 210)
- **NAMES_LOCK data change:** No change needed — fix is in the exemption logic

---

## 12. Gate question for Scott / Opus

1. Does the word-segment substring approach look right? Or prefer simpler: just add "W&T" to NAMES_LOCK directly?
2. Writer prompt fix for turn 210 preposition span — agree to fix in same move, or park?
3. No "Warren" alone instances found — agree to defer to Move B?

---

*End of recon 2a.*
