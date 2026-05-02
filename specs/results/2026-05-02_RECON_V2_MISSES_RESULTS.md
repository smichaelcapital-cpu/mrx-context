# RECON RESULTS — V2 Misses Batch

**Date:** 2026-05-02
**Builder:** Sonnet
**Spec:** specs/2026-05-02_RECON_V2_MISSES_BATCH.md
**Status:** Complete. No code changes. No $.

---

## TASK 1 — `with and T`

### Stage 2 occurrences

| turn_idx | snippet |
|----------|---------|
| 110 | "I was at Somerset and it went back to do a deposition for with and T offshore." |
| 111 | "And do you know whether with and T was the plaintiff or the defendant in that case?" |
| 113 | "And could you describe to the best of your recollection what the claim with and T made..." |
| 201 | "With and T offshore." |
| 202 | "And you were at with and T all the way through about 1998, right?" |
| 204 | "And you joined with and T in about 1990?" |
| 206 | "What was with and T business?" |
| 208 | "And were you still in New Orleans with with and T?" |
| 210 | "What was your position at with and T?" |

### Reader anomaly status

| turn_idx | Flagged? | anomaly_id | category | confidence | reader_note (excerpt) |
|----------|----------|------------|----------|------------|----------------------|
| 110 | YES | a_0007 | steno_artifact | high | "'with and T' appears to be letters-as-words steno artifact; likely a company acronym (e.g., 'W&T Offshore')" |
| 111 | YES | a_0008 | steno_artifact | high | "'with and T' — same letters-as-words artifact as turn 110; likely 'W&T' (company acronym)" |
| 113 | YES | a_0009 | steno_artifact | high | "'with and T' — same letters-as-words artifact; likely 'W&T'" |
| 201 | YES | a_0015 | steno_artifact | high | "'With and T offshore' — letters-as-words pattern; 'With and T' likely an acronym or company name (e.g., 'W&T Offshore')" |
| 202 | YES | a_0016 | steno_artifact | high | "'with and T' — same letters-as-words artifact as turn 201; likely 'W&T' (company acronym)" |
| 204 | YES | a_0017 | steno_artifact | high | "'joined with and T' — same letters-as-words artifact; likely 'joined W&T'" |
| 206 | YES | a_0002 | steno_artifact | high | "letters-as-words: 'with and T' — same company name artifact as context turn 204; likely 'W&T'" |
| 208 | YES | a_0004 | steno_artifact | high | "'with with and T' — doubled 'with' plus letters-as-words artifact; likely 'W&T' company name with steno doubling" |
| 210 | YES | a_0005 | steno_artifact | high | "'at with and T' — letters-as-words: 'with and T' likely 'W&T' company name" |

**Reader flagged all 9 turns.** No Reader miss here.

### Writer proposals

| turn_idx | Proposal exists? | op_type | before | after |
|----------|-----------------|---------|--------|-------|
| 110 | YES | REWORD | 'to do a deposition for with and T' | 'a deposition for W&T Offshore' |
| 111 | YES | REWORD | 'whether with and T' | 'W&T' |
| 113 | YES | REWORD | 'claim with and T' | 'W&T' |
| 201 | **NO** | — | — | — |
| 202 | **NO** | — | — | — |
| 204 | **NO** | — | — | — |
| 206 | **NO** | — | — | — |
| 208 | **NO** | — | — | — |
| 210 | **NO** | — | — | — |

### Root cause

**Writer miss in batches 2+.** Reader flagged all 9 turns at high confidence. Writer produced REWORD proposals for turns 110, 111, 113 (first batch, ~turns 76-150) but produced **zero** proposals for the 6 later occurrences (turns 201-210, second+ batches).

Note: the anomaly_ids for batch 2 turns (a_0002, a_0004, a_0005, a_0015–a_0017) collide with anomaly_ids from other batches — but that cross-batch collision is irrelevant here. The issue is simpler: Writer was given the anomalies for turns 201-210 and produced no "with and T" → "W&T" proposals at all.

**Fix options:**
- Add "W&T Offshore" to NAMES_LOCK → Reader gets locked spelling → should drive high-confidence REWORD in all batches
- OR: patch Writer prompt to explicitly handle letters-as-words pattern when Reader's reader_note contains "W&T"
- NAMES_LOCK is cheaper and lower-risk. The Reader already says "likely 'W&T Offshore'" — NAMES_LOCK confirms it.

---

## TASK 2 — `Warren seal`

### Stage 2 occurrence

**turn_idx 124:** "Uhmm, I want to say I don't recall. I no one of them was Warren seal. And I don't know if he was the defendant or the plaintiff. It's been a while."

### Reader anomaly status

Two anomalies flagged on turn 124:

**Anomaly 1:**
- anomaly_id: a_0013
- category: name_uncertain
- confidence: **high**
- reader_note: "'Warren seal' — lowercase 'seal' in a personal name slot; likely a proper name 'Warren Seal' (person's surname); should be capitalized"

**Anomaly 2 (same turn):**
- anomaly_id: a_0014
- category: steno_artifact
- confidence: **high**
- reader_note: "'I no one of them' — 'no' likely 'know'; phonetic/steno collision: 'I know one of them was Warren Seal'"

Reader flagged it correctly. Name_uncertain + high confidence.

### Writer proposals

**NO proposals for turn 124.** Writer produced nothing for either anomaly on this turn.

### NAMES_LOCK — People category (current state)

```python
NAMES_LOCK = {
    # People
    "Halprin", "Caughey", "Garner", "Muir", "Guastella",
    ...
}
```

"Warren Seal" is **NOT** present.

### Root cause

Reader flagged it (name_uncertain, high confidence). Writer produced no proposal. Without "Warren Seal" in NAMES_LOCK, Reader categorizes as `name_uncertain` rather than a confirmed names_lock hit — which leaves Writer without a strong enough signal to REWORD.

**Fix path:** Add "Warren Seal" to NAMES_LOCK under People. Re-run Stage 3.1 (~$0.95). Expect Reader to produce `source=names_lock`, Writer to produce REWORD `before='Warren seal'` → `after='Warren Seal'`.

Also likely: the "I no one" → "I know" anomaly may now produce a REWORD proposal too (Reader already has the right read).

---

## TASK 3 — `25 years ago`

### Stage 2 occurrence

**turn_idx 104:** "25 years ago potentially. It was probably in the early 2000's."

### Reader anomaly on turn 104

```
anomaly_id: a_0005
category: format_artifact
confidence: medium
token_span: [0, 1]
reader_note: "narrative number '25' — state convention spells out numbers under 100 in
             narrative speech; likely 'Twenty-five'"
```

Reader flagged it. Medium confidence.

### Writer proposal for turn 104

```
proposal_id: p_0005
op_type: FLAG
before: '25 years'
after: ''
outcome: apply
```

Writer produced a **FLAG**, not a REWORD. Medium confidence → FLAG by design.
OUR_FINAL.txt at turn 104: `MB_REVIEW-FLAG` (not FIX). Text is unchanged; reviewer is prompted to check.

### All format_artifact anomalies (full list)

Only **3** format_artifact records exist in current V2 artifacts (not 6 as stated in HANDOFF_LOG 2026-04-30 v02 — that count may have referred to a different run or was an estimate):

| turn_idx | anomaly_id | token_span | confidence | reader_note (excerpt) |
|----------|------------|------------|------------|----------------------|
| 104 | a_0005 | [0, 1] | medium | "narrative number '25' — state convention spells out numbers under 100; likely 'Twenty-five'" |
| 320 | a_0009 | [18, 19] | medium | "narrative number '20 miles' — state convention spells out numbers under 100 in narrative speech ('twenty miles')" |
| 618 | a_0013 | [12, 13] | low | "'23 barrels per day' — number in narrative speech; state convention spells out numbers under 100 ('twenty-three barrels per day'); however this is a technical/operational figure which may warrant digits" |

### Reader prompt — number formatting section

From READER_PROMPT_V2.md, PASS 3 — DOES THE FORMAT MATCH CONVENTION?:

> "Numbers under 100 in narrative speech: usually spelled out. ('25 years ago' → suspect; spelled-out form is convention.)"
> "Compound numbers, ages, durations in narrative: spelled. Dates, dollar amounts, exhibit numbers: digits stay."

Category definition from HARD RULES:
> "format_artifact (number, date, or unit format)"

Example in prompt uses "30 minutes" → format_artifact, medium confidence.

### Root cause

Reader is working correctly. It flags narrative numbers as format_artifact at medium confidence. Writer correctly converts medium-confidence format_artifact → FLAG (not REWORD). The "miss" is that the fix requires human judgment (is this narrative or technical?). For "25 years ago" it's clearly narrative, but the pipeline correctly defers to the reviewer.

**Fix path options:**
- Raise Reader confidence for canonical narrative-number patterns ("N years ago") to high → Writer would REWORD
- Add explicit Writer rule: "format_artifact + narrative context (years, months, decades) → REWORD with spelled-out form"
- Accept current behavior: FLAG is correct, human reviewer should apply. Only "fix" if Scott wants auto-apply.

This is a judgment call for Opus, not a clear bug.

---

## TASK 4 — `No no`

### Stage 2 occurrence

**turn_idx 118:** "No no, yes, I have one time."

### Reader anomaly

```
anomaly_id: a_0011
category: steno_artifact
confidence: high
reader_note: "doubled 'No no' followed by self-correction 'yes' — witness self-correction
             missing em-dash; likely 'No -- no, yes'"
```

### Writer proposal

```
proposal_id: p_0011
op_type: REWORD
before: 'No no,'
after: 'No -- no,'
outcome: apply
reason: "high-confidence witness self-correction; em-dash needed between doubled 'No no' per house style"
```

Writer produced the **correct** fix. Outcome=apply.

### OUR_FINAL.txt

Turn 118 review queue: `tag=MB_REVIEW-FIX:confident`, `before='No no,'`, `after='No -- no,'`

**"No no" is already fixed in current V2 output.** The prior session's V2 miss assessment (listed as "Writer truncation producing 'No --'") was likely measured against the old anomaly_id collision state. With Bug 1 fixed (natural-key join, commit 1519912), the correct proposal is now joined to the correct anomaly and applies at full confidence.

**No fix needed.**

---

## TASK 5 — Artifact timestamps (Bug 1 data integrity check)

```
anomalies.jsonl:  2026-05-01T13:53:26.974036
proposals.json:   2026-05-01T13:53:26.970681
```

These timestamps correspond to the Chunk B' Lemonwood re-run (2026-05-01, ~$0.93 spend). Bug 1 fix (commit 1519912) was read-side only — proposal_mapper.py code change, no data files touched. **Confirmed: anomalies.jsonl and proposals.json are unchanged from the V2 run that produced the V2 audit.**

---

## SUMMARY FOR OPUS

| Miss | Reader status | Writer status | Current OUR_FINAL | Fix path |
|------|--------------|---------------|-------------------|----------|
| `with and T` (all 9 turns) | Flagged all 9, high conf | REWORD for turns 110-113 only; **no proposal for turns 201-210** | Turns 201-210 uncorrected | Add "W&T Offshore" to NAMES_LOCK → forces high-conf REWORD in all batches |
| `Warren seal` | Flagged (name_uncertain, high) | **No proposal** | Unflagged | Add "Warren Seal" to NAMES_LOCK → expect REWORD |
| `25 years ago` | Flagged (format_artifact, medium) | FLAG produced, applied | MB_REVIEW-FLAG (deferred to human) | Judgment call: accept FLAG, or raise confidence / add Writer rule |
| `No no` | Flagged (high) | REWORD produced, applied | **MB_REVIEW-FIX:confident — already correct** | None needed post-Bug 1 fix |

**Recommended next moves (Sonnet's read, for Opus to confirm):**

1. **Warren Seal + W&T Offshore → NAMES_LOCK** — both are pure NAMES_LOCK additions. Could be one chunk (two names, one re-run) or two separate chunks. Low risk, no prompt changes.
2. **25 years ago** — defer to Opus decision. The pipeline behavior is defensible (FLAG = correct for medium confidence). Only change if Scott wants auto-apply.
3. **No no** — no action needed. Already fixed.

---

*End of recon report*
