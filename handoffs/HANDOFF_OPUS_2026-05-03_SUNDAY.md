# OPUS HANDOFF — Sunday 2026-05-03 morning

To: Fresh Opus, Sunday morning session
From: Opus, Saturday night session (sat1514session)
Scott's status at handoff: 12+ hours on, exhausted, frustrated by tooling, sharp on architecture

## Read these in order

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. The previous Opus handoff: HANDOFF_OPUS_2026-05-02_EVENING.md
4. This handoff in full
5. The full Halprin RUN_SUMMARY (Sonnet writes this Saturday night)

DO NOT skip CODER_MINDSET. Saturday afternoon Opus skipped it and stalled twice. Saturday evening Opus (me) read it and it shaped every call. Read it.

After reading, confirm in ONE LINE: "Ramped Sunday morning. Ready."

## What shipped Saturday

Move A:
- be5ecad — validate_ops _names_lock_exempt() + "W&T" in NAMES_LOCK + 14 tests
- 8b1ca21 — Writer prompt W&T form rule

Tests: 579 passing.
Halprin first 50 pages: 52.4% → 71.4%. YELLOW band. Shipped.

Full Halprin (305 pages) wallpaper-only baseline run: completed Saturday night, ~$4.75. Number captured in RUN_SUMMARY.

## The architectural pivot — most important thing in this handoff

Saturday evening, while debugging tonight's run, Scott surfaced the architectural call this whole project has needed:

**NAMES_LOCK is wallpaper. Stop hand-coding it. Extract it from MB FINALs.**

Honest accounting of Halprin first 50 pages 71.4% confidence:
- ~4 wins are real engine (phonetic match, em-dash detection) — Bucket 3, transferable
- ~9 wins are wallpaper (W&T strings, Warren Seal, MB_PROFILE entries) — Bucket 2, Halprin-only
- Move A's architectural improvements (validate_ops + Writer prompt) are real and transfer — they are why the wallpaper *delivers wins*

If the engine ran on Brandl right now with current NAMES_LOCK, ~9 wins evaporate. Real "pure engine on a new depo" is ~19%.

Scott's solution, designed by him in plain English (named tonight as "the learning loop"):

> Build a Raw↔FINAL aligner+differ. Diff at the turn level. Every change MB made is a labeled training example. Across multiple MB FINALs, intersection = habitual MB (goes in MB_PROFILE). Set difference = case-specific (gets calibrated per depo from raw). Engine stops guessing MB's style. Engine *queries* it from data.

This is not calibration. This is a learning loop. The thermos analogy he used: "thermos doesn't care what's hot or cold inside — it preserves what it's given. Engine should be the same. We give it MB's style as data, not as guesses."

## First task Sunday morning — Aligner+Differ v0 spec

Don't write code Sunday. Write the spec.

Spec must answer:
1. What's the input? (Raw RTF turns + FINAL RTF turns, both already parsed by Stage 1)
2. What's the alignment unit? (Turn-level? Sentence-level? Word-level? Likely all three, in nested layers.)
3. What's the diff representation? (Structured: position, raw_token, final_token, change_type)
4. What change types do we track? (capitalization, spelling, abbreviation, punctuation, deletion, insertion, reordering, formatting)
5. What's the output artifact? (A diff dataset per depo, queryable, joinable across depos)
6. How does intersection across multiple depos produce MB_PROFILE? (Pattern frequency thresholds, not hand-curated rules)
7. How does the per-depo set difference seed NAMES_LOCK automatically?
8. How does the Oracle Covenant hold? (FINALs read at training time only. The artifact is the diff dataset and learned profile. Engine runtime never sees a FINAL.)

Only when spec is locked, Sonnet builds v0.

## Materials available

Halprin RAW + FINAL: both on Scott's laptop, both parseable by Stage 1.
Brandl RAW + FINAL: also on Scott's laptop. The second depo. Critical for intersection — without two depos there's no habitual-vs-case-specific distinction.
Easley: queued, not yet processed.

Two depos is the minimum viable starting point for the learning loop. Scott has both.

## Scott's working style — non-negotiable

- Plain English, 12-year-old reading level until told otherwise
- ONE question at a time, never stack
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses, especially when tired
- Always full absolute paths
- NEVER go silent — write live in chat, don't disappear into "thinking"
- NEVER make Scott copy-paste content between AIs — Sonnet writes to repo, pushes, replies with raw URL
- Reverse-engineer rules from MB FINALs before asking MB
- Scott commits and pushes; Sonnet never commits or pushes
- If Scott says he's tired, frustrated, or fading — that is the signal to slow down and narrate everything, not to push harder

## Tonight's tooling lesson — to be solved Sunday

PowerShell environment was not documented for human-driven runs. PYTHONPATH wasn't set; package lives in src\; multi-line paste with backticks hung the prompt. Scott went in circles for 20+ min.

Three artifacts to spec and ship Sunday alongside the aligner+differ work (whichever Sonnet has bandwidth for after the spec is locked):
1. `scripts\bootstrap.ps1` — one command, sets env, verifies imports, prints READY or MISSING
2. `scripts\run_full_depo.ps1` — parameterized script, no paste fragility
3. `RUNBOOK.md` — plain-English cold-start manual

Goal: Scott opens PowerShell, runs bootstrap, runs the script, walks away. No 20-minute environment fights ever again.

## Watch items

- EM_DASH word-stutter over-correction (1 instance Halprin first 50, on editorial restraint watch)
- WT_OFFSHORE over-expansion — fixed by Move A but stays on watch list until 3 depos confirm
- Comprehension agent stays parked. Pattern engine has more headroom via the learning loop than via comprehension.

## Mood at handoff

Saturday night Scott pushed through a 12+ hour day. Shipped Move A. Caught the wallpaper trap. Designed the learning loop himself. Survived a brutal tooling fight on the full-depo run. Ended frustrated but intact, and the architecture call he made is the most important one in the project so far. Sunday morning Opus — open with calm, narrate progress, lead with the Aligner+Differ spec. Treat the Halprin number as a footnote, not the headline.

## Coder mindset for Sunday

Slow is smooth. Smooth is fast. RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT. RULE-NUMBERS-OR-IT-DIDNT-HAPPEN. Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe — STOP, flag.
