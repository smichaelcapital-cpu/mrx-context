# MID-SESSION SONNET HANDOFF — Monday 2026-05-04 ~12:00pm

To:    Fresh Sonnet, Monday afternoon session
From:  Sonnet, Monday morning session
Owner: Scott
Status: Mid-session handoff. Today is a Monday build day. Work
        continues until energy fades.

## Read in order — DO NOT SKIP

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/backlog/THREE_SEALED_PHASES.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-04/halprin_full_scoreboard_v2.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-04/defect_inventory_v1.md <- READ THIS
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/MIDSESSION_OPUS_2026-05-04_1200.md (Opus side)
8. This handoff in full

After reading: confirm in ONE LINE: "Mid-session ramped. Ready."
Then wait for Opus to assign the first task.

## State at handoff

Latest commit on main: 6ee8750
Test count: 681 passing + 1 pre-existing failure
Working tree: 2 modified files predating today's work
(harness/watch/EDITORIAL_RESTRAINT_LOG.md and
tests/stage3/test_dictionary_loader.py) — leave them alone.

halprin_full Stage 3.1 + Stage 5 output is ON DISK from this
morning's re-render. DO NOT re-run Stage 3.1 unless Opus
explicitly says so ($6.43 API spend; reuse Monday's output).

## Critical context to hold cold

### Defect inventory is the strategic anchor
Today's defect_inventory_v1.md classifies all 738 diff blocks by
"what does it actually take to fix this?" — current architecture
ceiling is 321 blocks (CLOSEABLE_NOW + CLOSEABLE_WITH_ENGINE_WORK).
Audio unlocks another 279. Three Sealed Phases only unlocks 2
diff-blocks (still right for legal defensibility, but not for
volume).

### Rule 8a is in the prompt but didn't fire on the live run
Documented in writer_flag_not_reword_pow.md. Prompt-only safety
rules are unreliable on high-confidence proposals. Don't propose
more prompt-side safety patches without explicit code-side backup.

### proposal_mapper now tolerates orphan-anomaly span collisions
Stage 5 hard-rejected on duplicate (turn_idx, token_span) keys
before today. Now warn-and-continues when the loser has no
proposals. Strict path preserved when both colliders have proposals.

### Bible vs Bucket B answered
Punctuation Bible doesn't exist in code. Bucket B quotes/dashes
are MB's proofread additions, not steno errors. Audio is the
unlock for those, not a Bible.

### MB's stated rules (relevant for any Bucket B work)
- Quotes/dashes added during proofread by default
- Exception: if attorney says "quote" out loud, goes in live
  (text-detectable trigger — implementable as Stage 2 transform)

## Likely tasks this afternoon (Opus drives, you build)

**TASK 1: cap_proper deep recon (~1.5 hr, no API)**
- Sample 50+ of the 198 cap_proper blocks
- Classify into CLOSEABLE_NOW / CLOSEABLE_WITH_ENGINE_WORK /
  misclassified
- Output: reports/2026-05-04/cap_proper_deep_recon.md
- Why: original sample of 15 was thin. Biggest single category in
  inventory needs solid baseline before spec work.

**TASK 2: deep recon on highest-volume CLOSEABLE_NOW pattern**
- Top candidates: phonetic_error (33), doubled_word residual (29),
  hyphenation residual (25)
- Output: reports/2026-05-04/<pattern>_deep_recon.md

**TASK 3 (if energy holds): stale test cleanup**
- test_E2E3_wt_has_misses — pre-existing failure, ~5 min
- Update expected output to current correct output

## Standing rules — non-negotiable

- Never commit or push independently. Scott pushes everything.
- Halprin OUR_FINAL files NEVER push to public repo.
- Spot-check before every spec. Opus leads, you build.
- Rule sheet header on every spec (Universal/MB? Code/Prompt?
  File path? Commit prefix?).
- Full absolute paths always.
- Code-fenced blocks for any content Scott copies between AIs.
- Never go silent — ping every 10 min or at logical break.
- Plain English, 12-year-old reading level, ONE question at a
  time, short answers.
- Two distinct handoff files (Opus + Sonnet, never combined).
- Plain text URLs only.

## Coder mindset

Slow is smooth. Smooth is fast.
RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT.
RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Before any code change: "Could this change reduce transcript
accuracy or credibility?" If yes or maybe -> STOP, flag.

— End of mid-session Sonnet handoff —
