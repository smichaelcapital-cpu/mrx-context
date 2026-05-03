# HANDOFF — OPUS — Sunday 2026-05-03 afternoon

For: Fresh Opus, Sunday afternoon
From: Opus, Sunday morning (~10:20 AM → ~3:00 PM EDT)
Owner: Scott

## Read in order

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md (mandatory — locked this morning)
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-03_SUNDAY.md (this morning's morning handoff)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-03/halprin_full.frequency_report.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-03_DOUBLED_WORD_FIX.md

After reading: confirm in ONE LINE: "Ramped Sunday afternoon. Ready."

## What shipped this morning

1. Composer range fix (D-COMPOSER-SILENT-TRUNCATE) — engine commit 1c601fd. halprin_full.OUR_FINAL.txt now exists, 510 KB, 333 pages.
2. Diff Report B (Honest Diff) — 742 discrepancy blocks identified.
3. Frequency Report — top 6 categories = 82% of diff. Key numbers: em_dash_drop 206 (28%), doubled_word 101 (14%), unclassified 90 (12%), quote_marks_stripped 73 (10%), hyphenation 73 (10%), cap_proper_noun 68 (9%).
4. RULE_SHEET_v1 — every spec must include header (Universal? Y/N, Code/Prompt, file location, commit prefix). Mandatory.
5. doubled_word fix — built and ran. **Did NOT meet acceptance criteria.** See below.

## State at handoff — IMPORTANT

doubled_word fix: Sonnet built it correctly per spec. apply_ops dedupe ran on all 3,547 turns and fixed 35 real within-turn engine doubles. Those are good fixes. BUT: total diff dropped 742 → 743 (basically zero), doubled_word category went 101 → 104 (UP).

Root cause: morning Opus's spec was wrong. The 101 "doubled_word" blocks in the diff were a mix of:
- ~35 real within-turn engine doubles (which Sonnet correctly fixed)
- ~66 paragraph-join artifacts in the DIFF MEASUREMENT TOOL itself (when turn N ends with "foundation." and turn N+1 starts with "foundation.", they join into "foundation. foundation." in the words-only diff)

So the fix was real but invisible at the headline level because most of what the classifier called "doubled_word" was measurement noise, not engine output.

## Open decision waiting for you

Sonnet was told to spot-check 5 random remaining doubled_word blocks BEFORE pushing anything. Do NOT push corrected_turns.json or OUR_FINAL.v2.txt until that spot-check returns and you decide:

- Option 1: Accept the 35 real within-turn fixes, push them, document the measurement caveat in the frequency report
- Option 2: Revert (corrected_turns.pre_dedup.json exists)
- Option 3: (Recommended) Wait for spot-check, then probably go Option 1

## The bigger concern — must address before next fix

**The frequency classifier may have similar measurement artifacts in OTHER categories.** If "doubled_word" was 65% measurement noise, em_dash_drop and hyphenation might also be partially inflated. Before spec'ing the next fix, validate the classifier by spot-checking 5 random blocks in the next-priority category (likely quote_marks_stripped — Universal + Code, cleanest target).

## Architectural framing (locked, do not relitigate)

Scott's tailor analogy: ONE engine, two parts inside.
- Universal core (the brain) — same for every CR
- CR-specific tailoring (settings file) — MB's house style, MB's case dictionary, loaded per-reporter

Brain NEVER gets MB's preferences glued in. Refer to RULE_SHEET_v1 for routing every fix.

## Afternoon goal (recommended order, not locked — confirm with Scott)

1. Resolve doubled_word push/revert decision based on Sonnet spot-check
2. Validate frequency classifier is clean for quote_marks_stripped (5-block spot-check)
3. If clean: spec quote_marks_stripped (Universal + Code, ~73 blocks) — same shape as doubled_word but accurate this time
4. If energy holds: tackle em_dash_drop carefully (206 blocks, MB-specific + Prompt, needs 20+ block read first to understand sub-types)

Expected end-of-afternoon: diff blocks 742 → ~620-650, two clean wins shipped, no architectural drift.

## Process discipline — locked this morning

- Every spec MUST include rule-sheet header. No exceptions.
- Every commit prefixed `universal:` or `mb-specific:`. No exceptions.
- Sonnet caught his own classifier bug this morning. Encourage that. Spot-checks before trusting numbers. Always.
- Default to MB-specific when unsure. Easier to promote later than demote.

## Scott's working style — non-negotiable

- 12-year-old reading level until told otherwise
- Plain English, ONE question at a time, never stack
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses, especially when tired
- ALWAYS full absolute paths
- NEVER go silent
- NEVER make Scott copy-paste content between AIs — Sonnet writes to repo, pushes, replies with raw URL
- Reverse-engineer rules from MB FINALs before asking MB
- Scott commits and pushes; Sonnet never commits or pushes independently
- **CRITICAL: Always separate Opus handoff from Sonnet handoff. Never combine. Two distinct files.**
- If Scott says he's tired, frustrated, or fading — that's the signal to slow down and narrate, not push harder

## Scott's mood at handoff

8 hours in. Calm but worn. Has been the hammer multiple times today catching morning Opus's drift (over-engineering specs, racing ahead, combining handoffs, fire-hosing). The morning Opus failures were real. Walk in calm. Show numbers. Pick the next fight from a validated frequency table. Do NOT relitigate the architecture — refer to RULE_SHEET.

## Coder mindset

Slow is smooth. Smooth is fast.
RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-SPEC-BEFORE-BUILD. RULE-INPUT-IS-SACRED.

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag.

— End of Opus afternoon handoff —
