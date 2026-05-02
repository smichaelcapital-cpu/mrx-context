# RECON 2b — WT_OFFSHORE Contextual Short-Form Rule
# Move A Pre-Build Gate

**Date:** 2026-05-02 evening
**Author:** Sonnet (sat1514session)
**Status:** COMPLETE — pending Scott + Opus review before code
**Spec parent:** 2026-05-02_MOVE_A_SPEC.md

---

## 1. What I looked at

- `io/analysis/halprin_mini/_stage2_out/halprin_mini.stage2.turns.json` — raw steno turns
- `io/analysis/halprin_mini/040226yellowrock-FINAL.txt` — MB FINAL ground truth
- `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt` — engine output
- `io/analysis/halprin_mini/_stage3_1_out/proposals.json` + `rejections.jsonl`

---

## 2. All W&T mentions — raw vs MB FINAL vs OUR_FINAL (pages 13-50)

### Section 1 — turns 110-113 (MB FINAL lines 728-738, ~page 14)

Context: witness mentions a prior deposition he gave for W&T.

| turn_idx | speaker | raw steno text | MB FINAL | OUR_FINAL | engine bucket |
|---|---|---|---|---|---|
| 110 | A | "...for **with and T offshore**." | "for **W&T Offshore**." | "for **W&T Offshore**" (FIX) | WIN |
| 111 | Q | "...whether **with and T** was the plaintiff..." | "...whether **W&T** was the..." | "**W&T Offshore**" | OVER-REACH |
| 113 | Q | "...what the claim **with and T** made..." | "...what the claim **W&T** made..." | "**W&T Offshore**" | OVER-REACH |

### Section 2 — turns 201-210 (MB FINAL lines 1032-1058, ~page 27-28)

Context: Q&A about witness's employment history at W&T.

| turn_idx | speaker | raw steno text | MB FINAL | OUR_FINAL | engine bucket |
|---|---|---|---|---|---|
| 201 | A | "**With and T offshore**." | "**W&T Offshore**." | "**W&T Offshore**" (FIX) | WIN |
| 202 | Q | "...at **with and T** all the way..." | "...at **W&T** all the way..." | "with and T" (raw, dropped) | MISS |
| 204 | Q | "...joined **with and T** in about 1990?" | "...joined **W&T** in about 1990?" | "with and T" (raw, dropped) | MISS |
| 206 | Q | "What was **with and T** business?" | "What was **W&T's** business?" | "with and T" (raw, dropped) | MISS |
| 208 | Q | "...with **with with and T**?" | "...with **W&T**?" | "with and T" (raw, dropped) | MISS |
| 210 | Q | "...at **with and T**?" | "...at **W&T**?" | "with and T" (raw, dropped) | MISS |

**Total W&T instances in MB FINAL pages 13-50:** 9
- "W&T Offshore" (full form): 2 instances (turns 110, 201)
- "W&T" (short form): 7 instances (turns 111, 113, 202, 204, 206, 208, 210)
- "W&T's" (possessive short form): 1 (turn 206 — counts as short form)

---

## 3. The rule — what the data says

The pattern is **fully deterministic**. No ambiguity.

| Signal in raw steno | MB form to use |
|---|---|
| "with and T offshore" (contains "offshore") | W&T Offshore |
| "with and T" alone (no "offshore") | W&T |

That's it. MB is not doing document-position tracking ("first mention = full, rest = short"). She is not doing speaker-role tracking ("Q = short, A = full"). She is reading what was actually said and restoring it faithfully:

- When speaker said "W&T Offshore" → steno wrote "with and T offshore" → MB writes "W&T Offshore"
- When speaker said "W&T" → steno wrote "with and T" → MB writes "W&T"

**The rule is a raw-text signal, not a semantic/positional one.**

Evidence: Turn 110 is an A-line → "W&T Offshore" (full). Turn 201 is also an A-line → "W&T Offshore" (full). Both contain "offshore" in raw. All other turns (both Q and A) lack "offshore" → "W&T" (short).

---

## 4. What the engine is currently doing wrong

**Over-reach (2 instances — turns 111, 113):**

Engine sees "with and T" → looks up NAMES_LOCK → finds "W&T Offshore" (only entry) → proposes "W&T Offshore" → proposal passes word budget (turns are long enough) → OUR_FINAL shows "W&T Offshore" where MB used "W&T".

Root cause: NAMES_LOCK has only one W&T entry ("W&T Offshore"). Writer uses it for ALL "with and T" occurrences regardless of whether raw contains "offshore".

**Miss (5 instances — turns 202, 204, 206, 208, 210):**

Engine correctly proposes "W&T" (not "W&T Offshore") for these turns. But validate_ops drops all 5 because "W&T" is not in NAMES_LOCK. Fix covered by Recon 2a.

**Note:** The Writer IS getting the form right for the 5 dropped proposals — it proposes "W&T" not "W&T Offshore". The over-reach is the separate problem where proposals pass but are wrong.

---

## 5. Proposed fix

Two-part fix, both in the Writer prompt (suggester.py NAMES_LOCK section):

### Part A — Writer prompt rule for W&T

Add to the Writer prompt's NAMES_LOCK instruction section:

> **W&T Offshore form rule:** "W&T Offshore" and "W&T" are both valid forms of the same entity. Use the form that matches what the speaker said:
> - If the raw span contains "offshore" (e.g., "with and T offshore") → use "W&T Offshore"
> - If the raw span does NOT contain "offshore" (e.g., "with and T" alone) → use "W&T"
> Never substitute "W&T Offshore" for a span that did not contain "offshore" in the steno.

### Part B — NAMES_LOCK set addition

Add "W&T" to NAMES_LOCK in `_run_halprin_mini.py`:

```python
NAMES_LOCK = {
    ...
    "W&T Offshore",
    "W&T",         # short form — see W&T form rule in Writer prompt
    ...
}
```

This also fixes validate_ops for the 5 dropped proposals (alternative to the word-segment substring approach from Recon 2a for the W&T-specific case).

---

## 6. Which fix approach for validate_ops?

Recon 2a proposes a general word-segment substring fix to validate_ops. Recon 2b surfaces a simpler alternative for the W&T case: just add "W&T" to NAMES_LOCK.

**Tradeoff:**

| Approach | Scope | Risk | Benefit |
|---|---|---|---|
| Add "W&T" to NAMES_LOCK | W&T only | Near-zero | Fixes 5 drops, zero code change in validate_ops |
| Word-segment substring in validate_ops | General | Low but needs tests | Handles future partial-name exemptions without NAMES_LOCK additions |

**Recommendation:** Do BOTH. Add "W&T" to NAMES_LOCK as the immediate fix, AND ship the general substring exemption in validate_ops as the architectural upgrade. Belt and suspenders.

---

## 7. Writer prompt contradiction hunt (RULE-CONTRADICTION-HUNT)

Current Writer prompt NAMES_LOCK section (from suggester.py) says:

> "NAMES_LOCK (visible to the Writer) is the set of locked proper nouns for this case. When the Writer proposes a REWORD that results in a NAMES_LOCK entry, the word budget is exempt."

This does NOT currently distinguish W&T from W&T Offshore. Adding the form rule above does not contradict anything — it adds specificity.

**No contradictions found.**

---

## 8. Silent failure check (RULE-SILENT-FAILURE-CHECK)

Risk: Engine proposes "W&T" for a span containing "with and T" when context is actually about a different company, not W&T Offshore.

**Halprin data:** No such false-positive risk found. Every "with and T" in this depo refers to W&T Offshore. The witness worked there; the context is unambiguous.

**General risk for other depos:** If "with and T" appears in a depo where W&T Offshore is not a party, the Writer could incorrectly propose W&T. Mitigation: NAMES_LOCK is case-specific. If "W&T" and "W&T Offshore" are not in NAMES_LOCK, the Writer has no basis to propose them. The rule only fires when NAMES_LOCK is loaded. Zero risk for depos where W&T is not a named entity.

---

## 9. Harness impact

After fix ships:
- WT_OFFSHORE OVER-REACH: 2 → 0 (turns 111, 113 fixed)
- WT_ACRONYM WIN: 4 → 9 (turns 202, 204, 206, 208, 210 recovered after validate_ops fix)
- WT_OFFSHORE WIN: 2 → 2 (unchanged — turns 110, 201 already correct)

Projected confidence number: 11/21 (52.4%) → 15/21 (71.4%) from W&T alone.

Note: WT_ACRONYM and WT_OFFSHORE patterns in MB_PROFILE.yaml will need updating after fix:
- WT_ACRONYM: add "W&T" as a separate mb_form tracking entry or split pattern
- WT_OFFSHORE: reclassify so it only tracks the 2 genuine full-form instances

---

## 10. Summary — is the rule deterministic?

**YES.** The rule has zero exceptions across 9 instances in this depo. Rule shape:

> `"offshore"` present in raw span → full form "W&T Offshore"
> `"offshore"` absent from raw span → short form "W&T"

This is a raw-text rule, not a contextual/positional one. It is implementable with a simple string check, no LLM inference required.

Move A can ship WT_OFFSHORE contextual short-form as planned.

---

*End of recon 2b.*
