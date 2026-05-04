# SONNET HANDOFF — Monday 2026-05-04 morning

To:    Fresh Sonnet, Monday morning session
From:  Sonnet, Sunday evening session
Owner: Scott

## Read in order — DO NOT SKIP

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/backlog/THREE_SEALED_PHASES.md  <- READ THIS, NEW NORTH STAR
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-04_MONDAY.md  (Opus side — read so you know what fresh Opus was told)
6. This handoff in full

After reading: confirm in ONE LINE: "Ramped Monday morning. Ready."
Then wait for Opus to assign the first task. Do NOT start coding unprompted.

## What shipped Sunday — 6 universal fixes (best day on the project)

| # | Defect | Repo | Commit |
|---|--------|------|--------|
| 1 | D-COMPOSER-SILENT-TRUNCATE | mrx_engine_v1 | morning |
| 2 | D-DOUBLED-WORD | mrx_engine_v1 | midday |
| 3 | D-WRITER-WORD-DROP validator | mrx_engine_v1 | afternoon |
| 4 | D-UHHUH-HYPHENATION | mrx_engine_v1 | 5c8eace |
| 5 | D-READER-COMPOUND-SPAN | mrx_engine_v1 | 1713fe9 |
| 6 | D-READER-SPAN-DISCIPLINE-V2 | mrx_engine_v1 | e79bc11 |

Plus in mrx-context:
- THREE_SEALED_PHASES.md backlog (commit 19f5ae8)
- 5 recon/spot-check reports in reports/2026-05-03/

Tests: 645 passing in mrx_engine_v1.

## Critical technical context — hold this cold

### Read-Write Separation (architectural)
- READER reads raw text -> produces anomaly_id + token_span + category
- WRITER receives only the anomaly list and span metadata. Writer NEVER sees raw text.
- This means: span-width fixes belong in the Reader prompt, not Writer.

### Active prompt locations
- `src/mrx_engine_v1/stage3/suggester.py` -- both prompts live here as inline strings
  - READER_PROMPT_V1: lines 75-376
  - WRITER_PROMPT_V1: lines 383-478
- `src/mrx_engine_v1/stage3/prompts.py` -- LEGACY (PDF pipeline only). IGNORE.

### Span discipline rules (shipped Sunday)
READER_PROMPT_V1 now contains:
1. Compound-token narrow-span rule (commit 1713fe9)
2. Year-range concatenation rule with explicit carve-out from "digits stay" (1713fe9)
3. Broadened scope to all word-level fixes -- phonetic mis-reads and stroke collisions (e79bc11)

The original commit fixed 6 hyphenation blocks. The v2 broadening covered an additional 5 phonetic_error blocks for free.

### Stage 2 deterministic transforms
- T2 (uh-huh decompaction) added in commit 5c8eace
- Lives in `src/mrx_engine_v1/stage2/transforms.py`, registered in pipeline.py
- Pattern: regex-based, word-boundary anchored, case-preserving
- Tests in `tests/stage2/test_transforms.py`

### Validator (don't touch)
- `src/mrx_engine_v1/validate_ops/word_preservation.py`
- Confirmed correct on Sunday -- Sonnet evening recon (validator_decompaction_recon.md)
- Rule 1 single-word skip + 50% majority threshold are working as intended
- Do NOT propose changes to the validator without recon evidence it's wrong

### FLAG op infrastructure (confirmed Sunday)
- FLAG bypasses word_preservation architecturally (apply.py L136 exits for non-REWORD)
- Renders inline as `{{MB_REVIEW-FLAG: reason}}` and writes to `review_queue.json`
- 762 items confirmed live in halprin_full output -- plumbing is working
- This means: a Writer rule emitting FLAG on uncertain proper nouns will surface to MB without new infrastructure

### THREE_SEALED_PHASES -- architectural North Star
Read backlog/THREE_SEALED_PHASES.md in full. Key points:
- Future architecture: Reader (AI proposes) -> Validator (AI + audio confirms) -> Composer (DUMB mechanical, NO AI at write time)
- Current Stage 3 "Writer" is misnamed -- it's a Proposer
- The FLAG/review_queue plumbing (above) is essentially proto-Composer behavior -- already exists, just under-used
- Concrete evidence this matters: Sunday found Writer outputting "Fran Schneider" for actual person "Fran Snyder" (blocks 537/540, halprin_full)
- Top-tier retrofit alongside Aligner+Differ
- Do NOT redesign in the current session. Reference only when naming new things.

## Sunday recon reports (read if working in these areas)

- `reports/2026-05-03/halprin_full_scoreboard_v1.md` -- the 740-block diff bucketed (A=161 engine, B=518 editorial, C=~50 validator-protected, D=61 unknown). True engine-bug surface is ~22%, not the raw 740.
- `reports/2026-05-03/hyphenation_spotcheck.md` -- 41 blocks -> 21 real bugs / 20 MB editorial. 13 closed Sunday, 8 remain (fractions, non-X, yearend, writeoff).
- `reports/2026-05-03/validator_decompaction_recon.md` -- flipped recommendation to "fix Reader, not validator." Validator is correct.
- `reports/2026-05-03/phonetic_error_spotcheck.md` -- 28 blocks classified. Top finding closed by D-READER-SPAN-DISCIPLINE-V2.
- `reports/2026-05-03/writer_flag_not_reword_recon.md` -- discovered the 3-layer failure chain (dictionary data + Reader categorization + Writer trigger gap). Recommends Option D Writer-side safety net.
- `reports/2026-05-03/flag_op_downstream_recon.md` -- Q1 verdict: YES_ROBUST. FLAG ops surface to MB via inline marker + review_queue.json. Finding 2 spec is unblocked.

## Likely Monday tasks (Opus drives, you build)

### Primary: D-WRITER-FLAG-NOT-REWORD spec + build

The proper-noun fabrication safety net. Q1 verdict (YES_ROBUST) confirmed FLAG ops reach MB cleanly -- spec is unblocked.

Expected fix shape (Option D from writer_flag_not_reword_recon.md):
> "If source=case_dict (or phonetic_match) AND proposed `to` introduces a proper noun (person/company name identified in reader_note) AND that name is not in NAMES_LOCK -> FLAG."

This is RESTRICTIVE (do less, FLAG instead of REWORD). Cannot introduce wrong names -- only prevents commits to uncertain ones. Lives in WRITER_PROMPT_V1.

Pattern: Opus writes spec -> recon (you) -> build (you) -> verify against blocks 537/540 -> push.

### Secondary: end-to-end re-render of halprin_full

Validate the cumulative effect of Sunday's 6 fixes on the actual 305-page transcript. API spend, single overnight run. Compare new diff bucket counts vs Sunday's scoreboard (Bucket A target: <=100, was 161).

### Queue (if energy allows after primary + secondary)

- acronym_mangle spot-check (17 blocks) -- drafted Sunday, in Opus's back pocket
- doubled_word residual investigation (28 blocks remain after morning fix -- why?)
- word_drop residual (17 blocks remain after validator)
- Remaining hyphenation patterns (8 blocks: fractions, non-X, yearend, writeoff)

## Standing rules -- non-negotiable

- Never commit or push independently. Scott does all commits and pushes.
- Halprin OUR_FINAL files NEVER push to public repo. Gitignore enforces -- verify before any push.
- Spot-check before every spec. Opus leads, you build.
- Rule sheet header on every spec (Universal/MB? Code/Prompt? File path? Commit prefix?).
- Full absolute paths always.
- Code-fenced blocks for any content Scott copies between AIs.
- Never go silent -- ping every 10 min or at logical break.
- Plain English, 12-year-old reading level, ONE question at a time, short answers.
- Two distinct handoff files (Opus + Sonnet, never combined).
- When pasting URLs in chat, plain text only -- terminal auto-hyperlinking has broken URL fetches twice in this project.

## Lessons from Sunday -- internalize

1. Read-Write Separation is real. When a fix looks like a "Writer" fix, check whether the bug is upstream in Reader's anomaly categorization first.
2. Dictionary data quality is a failure mode separate from prompt logic. Fran Schneider/Snyder was a dictionary error, not an engine bug.
3. The validator is mature and usually right. Test the assumption that the validator is wrong before patching it.
4. Span discipline applies to ALL word-level corrections, not just compound tokens.
5. FLAG infrastructure already exists and works. Use it as the safety hatch for uncertain corrections rather than letting Writer guess.
6. Auto-compact during Claude Code work survives if context is well-summarized. Sunday afternoon and evening compacts both held.

## Scott's state at handoff

Sunday was an 11+ hour day (morning + afternoon + evening sessions). Calm, methodical, embraced the grind. Shipped his best single-day output. Locked the THREE_SEALED_PHASES architectural North Star. Surfaced concrete evidence (the Fran Schneider bug) that proves the current architecture is leaking AI judgment into the write phase, AND confirmed (via Q1) that the existing FLAG/review_queue system is the natural foundation for Three Sealed Phases.

Walk into Monday calm. Treat it as continuation, not a fresh start.

## Coder mindset for Monday

Slow is smooth. Smooth is fast.
RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT.
RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe -> STOP, flag.

-- End of Sonnet Monday ramp --
