# MID-SESSION HANDOFF — OPUS → SONNET — 2026-04-30

**Time written:** Thursday 2026-04-30, 6:48 PM
**From:** Opus (mid-session, end of context)
**To:** Sonnet (next session)

---

## WHAT YOU NEED TO KNOW

Tonight Scott and Opus reviewed the audit (`HALPRIN_MINI_3WAY_DIFF.md`). Headline: 1,027 diff lines but only ~22 real defects across 4 categories. Cat 1 (steno artifacts not corrected by Stage 3.1) is the biggest and the focus of the next work session.

You already published the current Stage 3.1 state to git tonight at:
`mrx-context/stage3_1/STAGE3_1_CURRENT_STATE_2026-04-30.md`

That file documents the existing two-agent setup (Reader + Writer), both prompts verbatim, the output schema, and per-call input context. Opus has read it.

---

## WHAT'S COMING NEXT (TOMORROW MORNING)

Fresh Opus will:

1. Ramp from `mrx-context/handoffs/HANDOFF_OPUS_2026-04-30_v01.md`
2. Write a new Reader prompt (and minor Writer prompt updates if needed) targeting the defect categories from the audit
3. Send you a spec to: swap in the new prompt(s), make NO other code changes, re-run Halprin mini through the pipeline, run the same audit script that produced `HALPRIN_MINI_3WAY_DIFF.md`
4. Compare defect counts before vs after, by category

**The refactor target is the Reader prompt, not the Writer.** Reader is the one missing the defects. If Reader doesn't flag a homophone, Writer never gets a chance to fix it.

---

## CONSTRAINTS YOU MUST ENFORCE WHEN THE SPEC ARRIVES

1. **Few-shot examples in the new prompt MUST NOT use Halprin's actual defect words.** No W&T, no Lemonwood, no your/you're, no underpaid, no Warren Seal. Otherwise the Halprin re-run is a memorization test, not a real test. If Opus's spec slips and uses Halprin's words in examples, push back.

2. **Output schema CANNOT change.** Same JSON structure the existing pipeline expects. Opus has read your schema doc.

3. **Per-call input context CANNOT change.** Same sliding-window batches, same context turn structure.

4. **No other code changes during the test run.** Prompt swap only. Anything else and we won't know what moved the defect count.

5. **Oracle Covenant.** Do not read MB FINAL files at runtime, do not copy them into code, do not use them to construct prompt examples. Reading them to score the audit is the only allowed use.

---

## CURRENT REPO STATE

- `mrx-context` main branch — clean, all tonight's commits pushed
- `Court_reporting_demo` (engine) — pages 1-13 of OUR_FINAL Halprin byte-match MB; Cat 1 defects from audit are the focus

---

## SCOTT'S WORKING STYLE — REMINDERS

- 12-year-old reading level
- Plain English, short answers
- ALWAYS full absolute paths
- Will lose patience FAST on obvious questions
- **NEVER make Scott the copy-paste mule.** When responding to Opus or Scott with anything longer than a few lines, write to a file in `mrx-context`, push to git, reply with just the raw URL.

---

## CODER MINDSET

Before any code change: "could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag to Scott.

---

— End of handoff —
