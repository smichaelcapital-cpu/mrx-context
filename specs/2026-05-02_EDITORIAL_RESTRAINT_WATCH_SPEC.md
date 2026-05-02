# EDITORIAL RESTRAINT WATCH — Harness Spec Addendum
**Date:** 2026-05-02
**Author:** Opus
**Builder:** Sonnet (next)
**Status:** SHIPPED — built same session
**Parent spec:** 2026-05-02_VALIDATION_HARNESS_SPEC.md

---

## 1. PURPOSE

Today's harness run surfaced two patterns where the engine made corrections MB chose NOT to make:
- WT_OFFSHORE: engine expanded short form to full form 2 extra times
- EM_DASH_REPEAT_WORD: engine added em-dashes for "I -- I", "whether -- whether", "to -- to" — MB left them alone

These are NOT necessarily bugs. MB exercises **editorial restraint** — she knows the rule but chooses when to apply it. The engine doesn't yet know when to hold back.

This addendum makes restraint a **first-class measurement** in every harness report. Be paranoid. Track every instance across every depo. Let the data tell us:
- **Consistent context** → new rule to learn (when to NOT apply)
- **Random pattern** → engine over-correcting, regression risk
- **Audio-correlated** → Whisper integration ROI

---

## 2. DEFINITION

For any pattern with `bucket_hint: trackable`, an OVER-REACH instance is a candidate **Restraint Event**:

> An OVER-REACH where the engine applied a correction the rule supports, but MB chose not to apply it in that specific instance.

Every OVER-REACH gets logged with full context for human review. None are auto-classified as bugs. None are auto-classified as missing rules. We collect data; humans interpret.

---

## 3. NEW HARNESS OUTPUT SECTION

Every harness report from this date forward includes:

```
EDITORIAL RESTRAINT WATCH (paranoid)
Patterns where engine acted but MB chose NOT to in this depo's scope.

Pattern ID          | Engine acted | MB acted | Restraint count | First observed
WT_OFFSHORE         | 4            | 2        | 2               | 2026-05-02 halprin_mini
EM_DASH_REPEAT_WORD | 3            | 1        | 2               | 2026-05-02 halprin_mini

Per-instance evidence
[For each restraint event: surrounding context (3 lines before/after),
engine's correction, MB's actual text]
```

Section appears in every report even when empty (signals the check ran).

---

## 4. PERSISTENT WATCH FILE

In addition to per-report logging, maintain a cumulative file:

`harness/watch/EDITORIAL_RESTRAINT_LOG.md`

Append-only across all harness runs. Format:

```markdown
# Editorial Restraint Log
# Append-only — never delete entries — only mark resolved with reason

## 2026-05-02 — halprin_mini, pages 13-50, engine 83d5199

### WT_OFFSHORE
- Restraint count: 2
- Pattern: engine expanded "W&T" to "W&T Offshore" where MB used short form
- Status: OPEN — needs >=3 depos data before classifying
- Next review: after depo #2 harness run

### EM_DASH_REPEAT_WORD
- Restraint count: 2
- Pattern: engine added em-dashes for word-level stutters where MB left raw
- Status: OPEN — possible audio-dependent (witness self-correction vs raw stutter)
- Next review: after depo #2 harness run

---
```

Rule: **Never delete entries.** Resolution = mark `Status: RESOLVED — <reason>`. History preserved.

---

## 5. CROSS-DEPO TRENDING (after 3+ depos)

Once 3 depos in the watch log:

`harness/run_trend_analyzer.py` (separate script, build later) reads the watch log and produces:

| Pattern | Depo 1 | Depo 2 | Depo 3 | Trend |
|---|---|---|---|---|
| WT_OFFSHORE | 2 | 1 | 0 | Decreasing — context likely learnable |
| EM_DASH_REPEAT_WORD | 2 | 4 | 3 | Stable — random, regression risk |

**Trend interpretation:**
- **Decreasing:** engine is finding the right context, no fix needed
- **Stable & consistent context:** new rule needed (when NOT to apply)
- **Stable & random context:** engine is over-correcting — fix it
- **Audio-correlated:** Whisper ROI confirmed

DEFER the trend analyzer until we have >=3 depos. Today is depo 1.

---

## 6. DECISION TREE FOR EVERY RESTRAINT EVENT

When humans review the watch log:

```
For each restraint event:

Is this a regression? (engine should never have made this change)
→ YES: file as defect, fix engine
→ NO: continue
Is the context predictable from text alone?
→ YES: candidate new rule, add to MB profile
→ NO: continue
Is the context predictable WITH audio?
→ YES: log as Whisper ROI candidate
→ NO: continue
Is this pure MB editorial judgment?
→ YES: mark SCOPE_DECISION, exclude from confidence number, accept FLAG-only
→ NO: escalate to Scott
```

---

## 7. IMPLEMENTATION SCOPE

**Sonnet builds today:**

1. `harness/restraint_watch.py` — INDUSTRIAL
   - Reads OVER-REACH counts from bucket classifier
   - For each OVER-REACH instance, captures: surrounding context (3 lines), engine correction, mb_form vs engine action
   - Writes per-report section
   - Appends to cumulative `harness/watch/EDITORIAL_RESTRAINT_LOG.md`

2. Update `report_writer.py` — INDUSTRIAL
   - New section "EDITORIAL RESTRAINT WATCH (paranoid)" between "DEFECTS BY PATTERN" and "CANDIDATE NEW MB RULES"
   - Always renders, even if empty

3. Update `harness/patterns/MB_PROFILE.yaml` — DATA
   - No changes to existing patterns
   - Confirm `bucket_hint: trackable` is the trigger

4. Tests — `test_restraint_watch.py` — 7 tests (RW1–RW7):
   - RW1: No event when engine_correct <= mb_count
   - RW2: Event captured when engine_correct > mb_count
   - RW3: Restraint count = engine_correct - mb_count
   - RW4: Per-instance evidence captured correctly
   - RW5: Persistent log appends, never overwrites
   - RW6: Empty section still renders
   - RW7: Non-trackable patterns skipped

**Sonnet does NOT build today:**
- Trend analyzer (deferred until 3+ depos)
- Auto-classification of restraint events
- Any decision logic — humans interpret, code logs

---

## 8. PRIME DIRECTIVE CHECK

> "Could this change reduce transcript accuracy or credibility?"

**No.** Read-only addition. Logs measurements. Modifies nothing in engine pipeline. Worst case: noisy log → Scott reviews → ignores entries.

**Could this MISS a real regression?** Only if engine over-applies AND MB also over-applies in the same pattern. The harness can't catch it then. Acceptable tradeoff — our oracle is MB.

---

## 9. FIRST RUN OUTPUT (actual, post-ship)

```
EDITORIAL RESTRAINT WATCH (paranoid)
Pattern             | Engine acted | MB acted | Restraint count | First observed
WT_OFFSHORE         | 4            | 2        | 2               | 2026-05-02
EM_DASH_REPEAT_WORD | 3            | 1        | 2               | 2026-05-02

Total restraint events: 4
```

`harness/watch/EDITORIAL_RESTRAINT_LOG.md` created with 2 entries.

---

## 10. ACCEPTANCE CRITERIA (all met)

- [x] All existing harness tests still green (558 → 565)
- [x] 7 new tests for restraint watch — green (RW1–RW7)
- [x] Re-run on halprin_mini produces report with new section
- [x] `EDITORIAL_RESTRAINT_LOG.md` created with 2 entries (WT_OFFSHORE, EM_DASH_REPEAT_WORD)
- [x] Per-instance evidence captured (surrounding context, 3 lines)
- [x] Headline confidence number unchanged (52.4%) — restraint is separate measurement

---

## 11. OPEN ITEMS (resolved)

1. Watch file location: `harness/watch/EDITORIAL_RESTRAINT_LOG.md` — confirmed in engine repo
2. 3 depos minimum before classifying any restraint event — confirmed
3. Empty section renders (signals check ran) — confirmed, always renders

---

*End of spec.*
