# OPUS HANDOFF — Sunday 2026-05-03 evening

To: Fresh Opus, Sunday evening session
From: Opus, Sunday afternoon session
Owner: Scott

## Read in order — DO NOT SKIP

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-03_SUNDAY.md (this morning's morning ramp)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-03/halprin_full_scoreboard_v1.md ← MANDATORY, NEW SCOREBOARD
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-03/word_drop_rejection_classification.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-03_EVENING.md (the Sonnet evening ramp — read so you know what fresh Sonnet was told)
8. This handoff in full

After reading: confirm in ONE LINE: "Ramped Sunday evening. Ready."

## Walk in calm. Do not relitigate.

Scott is on a dinner break. He has been on this for 11+ hours today
across morning + afternoon sessions. Calm, sharp, productive.
Background in QA — values getting it right over getting it fast.
Trust the discipline that got us here. Don't reinvent.

## What shipped today (3 universal engine fixes)

1. D-COMPOSER-SILENT-TRUNCATE — engine commit 1c601fd (morning)
2. D-DOUBLED-WORD              — engine commit ff1fc17 (midday)
   • 35 real engine doubles fixed
3. D-WRITER-WORD-DROP validator — engine commits 2df5dce + db3dff8 (afternoon)
   • 194 silent word-drop proposals now blocked
   • 14 tests green, 582+ regression tests still passing

## The single most important thing you need to internalize

The diff-block count is NOT the scoreboard. The new scoreboard is at
link 5 above. Read it cold before doing anything.

  Total diff blocks: 740
  ├─ Engine bugs (Bucket A):       161 blocks (22%)  ← TODAY'S TARGETS
  ├─ MB editorial (Bucket B):      518 blocks (70%)  ← LEARNING LOOP, not bugs
  ├─ Validator-protected (C):       ~50 blocks (~7%) ← acceptable
  └─ Unknown (D):                    61 blocks (8%)  ← needs your review

True engine-bug surface is ~161 blocks. Bucket B will not drop until
Aligner+Differ ships (Day 2+). Stop treating the headline diff number
as the scoreboard.

## Today's discipline — locked, do not break

- Spot-check before every spec (validated 3x today)
- Rule sheet header on every spec (Universal? Code/Prompt? location? prefix?)
- Default to MB-specific when unsure (easier to promote than demote)
- Sonnet never commits or pushes independently
- Halprin OUR_FINAL files NEVER push to public repo (gitignore enforces)
- Push ONLY: engine code, tests, reports without raw transcript content
- Two distinct handoff files (Opus + Sonnet, never combined) — morning Opus
  broke this rule and got caught; afternoon Opus held the line
- Ping every 10 min or at logical break, never go silent
- Code-fenced blocks for ANY content Scott copies to Sonnet (visual
  differentiation — Scott asked for this explicitly today)

## Evening Bucket A target priorities (pick from these)

  1. hyphenation         41 blocks  (largest addressable)
  2. phonetic_error      28 blocks  (severe steno mis-reads)
  3. doubled_word        28 blocks  (residual after morning fix — investigate)
  4. word_drop           17 blocks  (residual after validator)
  5. acronym_mangle      17 blocks
  6. objection_style     12 blocks
  7. pronoun_swap        10 blocks
  8. number_style         8 blocks

Recommended evening grind: hyphenation (1 ship) → phonetic_error or
acronym_mangle (1 ship) → stretch for a 3rd if energy holds.

Pattern locked: spot-check (15 min) → spec (you write) → build (Sonnet)
→ verification (Sonnet, BEFORE push) → review (you) → push.

## Special note on hyphenation (the biggest evening target)

41 blocks. Likely Universal+Code. BUT — the word_preservation validator
already touches this space (some hyphenation diffs were tag-span bugs,
now blocked). Spot-check carefully to separate:
- Real hyphenation engine bugs (e.g. "daytoday" → "day-to-day")
- Tag-span artifacts already killed by validator (will disappear on re-render)
- MB editorial hyphen additions (Bucket B noise leaking in)

Do NOT spec hyphenation without a clean spot-check first.

## Open day-2+ backlog (do NOT spec these tonight)

1. D-WRITER-WORD-DROP Part C — Writer prompt hardening (belt-and-suspenders)
2. Phonetic-correction allow heuristic (16 SAFE candidates identified
   in word_drop_rejection_classification report)
3. Diff-tool noise fix (_generate_report_b.py)
4. MB tailoring catalog → Aligner+Differ v0 spec (THE big architectural play)
5. Aligner+Differ v0 BUILD (Saturday's call — extracts MB style from FINALs)
6. Bootstrap tooling (bootstrap.ps1, run_full_depo.ps1, RUNBOOK.md) —
   Saturday handoff item, never solved

## MB confirmation pending

Scott texted MB this afternoon to confirm the editorial-additions
hypothesis (does she add quotes / em-dashes / capitalization during
edit, or does steno have them). If MB has replied by evening, her
answer changes how we frame the entire Bucket B story. Check the chat
context for any MB update before locking the evening plan.

If MB has NOT replied: continue with the working hypothesis (steno
captures words, MB adds craft punctuation/casing).

## Scott's working style — non-negotiable

- 12-year-old reading level until told otherwise
- Plain English, ONE question at a time, never stack
- Inline A/B/C only when there's a real choice
- Code-fenced blocks for ANY content Scott copies to Sonnet
- Hates fire-hose responses, especially when tired
- Always full absolute paths
- NEVER go silent
- NEVER make Scott copy-paste content between AIs unnecessarily —
  Sonnet writes to repo, pushes, replies with raw URL
- Reverse-engineer rules from MB FINALs before asking MB
- Scott commits and pushes; Sonnet never commits or pushes independently
- If Scott says he's tired, frustrated, or fading — slow down and
  narrate, do not push harder

## Scott's mood at handoff

Calm, methodical, embracing the grind. He explicitly said: "I'm calm.
I'm collected. I'm embracing the grind. My background is QA, I want to
be right." He appreciated the slow-and-correct approach today and
shipped 3 universal fixes off the back of it.

He also said: "Bring a lunch, wear comfy shoes. We're getting through
this inventory." Evening session is a continuation of that mindset —
not a fresh start, a rested resumption. Walk in like you've been here
all day.

## Coder mindset for evening

Slow is smooth. Smooth is fast.
RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT.
RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Before any code change: "Could this change reduce transcript accuracy
or credibility?" If yes or maybe → STOP, flag.

— End of Opus evening ramp —
