# PROOF OF WORK — D-WRITER-FLAG-NOT-REWORD
**Date:** 2026-05-04 Monday morning
**Analyst:** Claude Sonnet (mrx-context session)
**Spec:** D-WRITER-FLAG-NOT-REWORD — Rule 8a: Proper-Noun Dictionary Guard
**Status: BLOCKED — live re-render verification failed. See §4.**

---

## 1. Prompt Edit — COMPLETE

**File:** `src/mrx_engine_v1/stage3/suggester.py`
**Change:** Inserted Rule 8a between lines 477 and 479 (after Rule 8, before Rule 9).
**Landed at:** Lines 479–489 post-edit.

Rule 8a as inserted (verbatim from spec):

```
8a. PROPER-NOUN DICTIONARY GUARD (FLAG instead of REWORD)
    If ALL of the following are true, emit FLAG instead of REWORD:
      (a) source is "case_dict" OR "phonetic_match"
      (b) reader_note explicitly identifies the proposed correction
          as a person name or company name
      (c) the proposed name is NOT present in NAMES_LOCK
          (case-insensitive, full-string match against any entry)
    This rule fires regardless of category or confidence.
    Reason: dictionary entries can be wrong. Phonetic guesses on proper
    nouns can sound right but be the wrong real person. When in doubt,
    hand it to MB.
```

Verified insertion with Read tool — rule present at correct location, surrounding
rules (8 and 9) unchanged.

---

## 2. Tests — 7/7 GREEN

**File:** `tests/stage3/test_writer_flag_not_reword.py` (new, 7 tests)

```
tests/stage3/test_writer_flag_not_reword.py::test_T17_rule8a_text_present_in_writer_prompt PASSED
tests/stage3/test_writer_flag_not_reword.py::test_T18_block537_analog_case_dict_person_not_in_names_lock_produces_flag PASSED
tests/stage3/test_writer_flag_not_reword.py::test_T19_block540_analog_case_dict_person_not_in_names_lock_produces_flag PASSED
tests/stage3/test_writer_flag_not_reword.py::test_T20_regression_case_dict_name_in_names_lock_allows_reword PASSED
tests/stage3/test_writer_flag_not_reword.py::test_T21_regression_case_dict_no_person_name_in_note_allows_reword PASSED
tests/stage3/test_writer_flag_not_reword.py::test_T22_phonetic_match_person_name_in_names_lock_allows_reword PASSED
tests/stage3/test_writer_flag_not_reword.py::test_T23_phonetic_match_company_name_not_in_names_lock_produces_flag PASSED

7 passed in 0.92s
```

**Note:** T17–T23 use mocked API responses. They verify:
- Prompt text contains Rule 8a key phrases (T17 — regression guard)
- Pipeline accepts FLAG ops for the 537/540 pattern (T18, T19, T23)
- Pipeline accepts REWORD ops when 8a should not fire (T20, T21, T22)

These tests do NOT verify that the live model follows Rule 8a. That is the function of
the targeted re-render in §4.

---

## 3. Regression Suite — 656 PASSING, 1 PRE-EXISTING FAILURE

```
656 passed, 1 failed — tests/test_e2e_halprin_mini.py::test_E2E3_wt_has_misses
```

**Pre-existing failure confirmed:** `test_E2E3_wt_has_misses` was failing before my
change (verified by stashing my edit and running the test — same failure). The test
expects `wt.miss >= 4` but the engine now achieves `miss=0` on W&T after Sunday's fixes.
This is a stale test expectation — the fix worked better than the test anticipated.
My change introduced zero new failures.

---

## 4. Targeted Re-render — VERIFICATION FAILED

**Scope:** Turns 2654–2662 (4-block window around turns 2657 and 2659).
**Cost:** $0.0545 (single live API call).
**NAMES_LOCK:** Same 15-entry set as the full halprin_full run.

### Anomalies detected by Reader

Reader correctly identified the "from an Schneider" artifact on both turns:

```
ANOMALY turn=2657 cat=steno_artifact
  note: 'named from an Schneider' — 'from an' is likely a steno artifact; ...

ANOMALY turn=2659 cat=steno_artifact
  note: 'named from an Schneider' — same pattern as turn 2657; 'from an' likely
        garbled rendering of 'Fran Schneider' (per dictionary)
```

Category is `steno_artifact` on both — same Reader miscategorization as the Sunday
recon. Reader Rule 8 violation persists (should be `name_uncertain`).

### Writer proposals produced

```
PROPOSAL turn=2657 op=REWORD src=case_dict
  before='named from an Schneider' after='named Fran Schneider'
  reason: "'from an Schneider' is a steno split of 'Fran Schneider';
           'Fran Schneider' appears in the case dictionary"

PROPOSAL turn=2659 op=REWORD src=case_dict
  before='named from an Schneider' after='named Fran Schneider'
  reason: "Same steno artifact pattern; 'from an Schneider' garbled
           rendering of 'Fran Schneider' per dictionary"
```

**Rule 8a did not fire.** Writer produced REWORD with source=case_dict on both turns,
despite all three Rule 8a conditions being met:
- (a) source=case_dict ✓
- (b) reader_note identifies "Fran Schneider" as the proposed correction ✓
- (c) "Fran Schneider" is NOT in NAMES_LOCK ✓

Expected outcome: FLAG. Actual outcome: REWORD.

Spec verification criterion — "Confirm FLAG marker {{MB_REVIEW-FLAG: ...}} appears
in output" — was NOT met.

---

## 5. Root Cause of Verification Failure

Rule 8a is a soft prompt instruction. When the model has high confidence in a correction
(source=case_dict, category=steno_artifact, confidence=high), it overrides soft
behavioral instructions in favor of the correction it "knows" is right.

This is not a prompt wording failure. The rule is clear:
- "If ALL of the following are true, emit FLAG instead of REWORD"
- "This rule fires regardless of category or confidence"

The model parsed these as advice and discounted them because the dictionary evidence
was strong. Prompt-only safety rules cannot reliably constrain confident model behavior
on cases where the model's training says "this is definitely correct."

### What the mocked tests verify vs. what the live model does

| What T18/T19 test | What the live model does |
|---|---|
| When Writer returns FLAG for this pattern, pipeline accepts it | Writer returns REWORD — FLAG is never produced |
| Rule 8a key phrases are in the prompt | Model reads the prompt and ignores Rule 8a |

The mocked tests are structurally correct — they verify the plumbing. They cannot
verify that the LLM follows the prompt rule consistently.

---

## 6. Options for Opus

The core question: how do we reliably enforce "case_dict + unverified proper noun →
FLAG"?

### Option 1 — Prompt strengthening only (INSUFFICIENT)

Add an explicit example to Rule 8a showing the exact "from an Schneider" → FLAG
pattern. The example would make the rule concrete and harder to override.

Estimated compliance improvement: partial. A confident high-confidence model may
still override it. Cannot guarantee compliance without code enforcement.

Risk: time spent, still probabilistic.

### Option 2 — validate_ops enforcement (RELIABLE but requires code change)

Add a new check or extend `check_names` in `validate_ops.py` to reject REWORD ops
where:
- source=case_dict OR source=phonetic_match, AND
- REWORD.to introduces a capitalized word sequence not in NAMES_LOCK, AND
- the capitalization is not sentence-initial (position check or reader_note signal)

If the REWORD is rejected by validate_ops, the proposal is dropped — and per Sunday's
recon (flag_op_downstream_recon.md §4), a dropped REWORD leaves the span verbatim with
NO review marker visible to MB. This is the same silent failure as before.

**Problem:** validate_ops rejection ≠ FLAG. Rejection silences the span. To get a FLAG,
the Writer must produce one. Validator can only reject.

**Partial fix:** validator rejection + a new "FLAG_ON_REJECT" recovery mechanism in
the pipeline. When validate_ops rejects a REWORD for the proper-noun reason, the
pipeline could auto-promote it to a FLAG op. This requires a code change but is
architecturally clean and fully reliable.

### Option 3 — Combined (RECOMMENDED)

(a) Add an explicit code-level recovery in the pipeline: when a REWORD with
    source=case_dict or phonetic_match is rejected by validate_ops for any reason
    (word_budget OR proper_noun), auto-generate a FLAG op for the same anomaly_id
    with reason="REWORD rejected — unverified correction held for human review."

(b) Keep Rule 8a in the prompt — the model may follow it on future runs and reduce
    validate_ops rejections. But the code-level recovery is the guaranteed path.

This requires:
- Change to pipeline.py: add auto-FLAG-on-reject logic for unverified-source REWORDs
- No changes to validate_ops.py or Stage 5 (FLAG plumbing is already complete)

### Option 4 — Reader fix only (INSUFFICIENT standalone)

Fix Reader to categorize proper-noun reconstructions as `name_uncertain` regardless
of steno mechanism. If Reader uses `name_uncertain`, Writer Rule 8 (not 8a) fires:
"When the Reader flags an anomaly on a name (category=name_uncertain ... and NOT in
NAMES_LOCK, you MUST produce a FLAG op)."

This fixes Layer 2 but not Layer 3. The live run today shows the Reader again used
`steno_artifact` — the Reader fix has not landed. Even if it landed, Rule 8's second
trigger "context indicates a proper noun" is still vague and may not fire.

Reader fix is defense in depth but not the primary fix.

---

## 7. Current State

| Step | Status |
|------|--------|
| Prompt edit (Rule 8a inserted) | COMPLETE |
| 7 new tests green | COMPLETE |
| Regression: 656 passing | COMPLETE |
| Pre-existing failure (E2E3_wt_has_misses) | PRE-EXISTING, not mine |
| Live re-render: FLAG marker in output | FAILED — REWORD produced |
| Spec verification criterion met | NO |

**Files modified:**
- `src/mrx_engine_v1/stage3/suggester.py` — Rule 8a inserted
- `tests/stage3/test_writer_flag_not_reword.py` — new file, 7 tests

**NOT committed. NOT pushed.** Awaiting Opus decision on path forward.

---

## 8. Recommendation to Opus

Rule 8a should stay in the prompt — it's correct and harmless, and establishes the
right intention. But a prompt-only fix cannot guarantee FLAG behavior on cases where
the model has high-confidence evidence from the dictionary.

The minimum code change needed for reliable enforcement: when the pipeline gets a
`validate_ops` rejection on a REWORD with `source in (case_dict, phonetic_match)`,
auto-generate a FLAG op for the same span/anomaly_id rather than silencing it.

This is a single change in `suggest_proposals()` or `_run_writer()` — about 10 lines.
It is architecturally consistent with Three Sealed Phases: the Composer never silently
drops uncertain corrections, it always hands them back to MB.

Should I spec that change, or does Opus want to redesign the approach?
