# OPUS HANDOFF — Monday 2026-05-04 morning

To:    Fresh Opus, Monday morning session
From:  Opus, Sunday evening session
Owner: Scott

## Read in order — DO NOT SKIP

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/backlog/THREE_SEALED_PHASES.md  <- READ THIS, NEW NORTH STAR
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-03_EVENING.md (Sunday evening ramp -- for context on what landed)
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-04_MONDAY.md (Sonnet's Monday ramp -- read so you know what fresh Sonnet was told)
7. This handoff in full

After reading: confirm in ONE LINE: "Ramped Monday morning. Ready."

## Walk in calm. Sunday was the best day on the project.

Scott shipped 6 universal fixes Sunday across morning, afternoon, and evening sessions. That's a personal best on this project. Walk into Monday like a continuation, not a fresh start. The discipline that produced 6 fixes in a day is the same discipline that should produce Monday's work.

## What shipped Sunday -- 6 universal fixes

| # | Defect | Repo | Commit |
|---|--------|------|--------|
| 1 | D-COMPOSER-SILENT-TRUNCATE | mrx_engine_v1 | morning |
| 2 | D-DOUBLED-WORD | mrx_engine_v1 | midday |
| 3 | D-WRITER-WORD-DROP validator | mrx_engine_v1 | afternoon |
| 4 | D-UHHUH-HYPHENATION (Stage 2 transform T2) | mrx_engine_v1 | 5c8eace |
| 5 | D-READER-COMPOUND-SPAN (Reader prompt) | mrx_engine_v1 | 1713fe9 |
| 6 | D-READER-SPAN-DISCIPLINE-V2 (Reader prompt broaden) | mrx_engine_v1 | e79bc11 |

Plus in mrx-context:
- THREE_SEALED_PHASES.md backlog (commit 19f5ae8) -- architectural North Star
- 5 recon/spot-check reports under reports/2026-05-03/

Tests: 645 passing in mrx_engine_v1.

## The single most important architectural moment from Sunday evening

Scott locked the Three Sealed Phases principle in writing:

> AI must NEVER touch the final transcript at write time. Three sealed phases:
> 1. **Reader** (AI proposes)
> 2. **Validator** (AI + audio cross-check confirms)
> 3. **Composer** (DUMB mechanical writer, NO AI)

Reason: legal defensibility. Under subpoena, Scott needs an auditable trail. A wrong word reaching paper must be a defensible failure (two agents agreed) -- not a magical hallucination.

Key implication for naming: current Stage 3 "Writer" is misnamed -- it's a Proposer. Don't rename in code yet, but reference this when naming new components.

Concrete evidence the principle is needed: blocks 537/540 of halprin_full. Reader correctly identified "an Schneider" as a steno garble of a proper name. Writer fabricated "Fran Schneider" -- but the actual person is "Fran Snyder." A wrong real-sounding name reached paper. That's the failure mode Three Sealed Phases prevents.

Good news from Q1 recon (Sunday night): the FLAG/review_queue infrastructure already exists and works. 762 FLAG items confirmed in halprin_full output today. FLAGs render as `{{MB_REVIEW-FLAG: reason}}` inline AND in review_queue.json. This is essentially proto-Composer behavior already in production.

DO NOT redesign the architecture in the Monday session. The North Star is logged. Reference it; don't rebuild around it.

## Monday's plan -- locked priorities

### Priority 1: D-WRITER-FLAG-NOT-REWORD (the proper-noun safety net)

Sunday's recon (writer_flag_not_reword_recon.md) found a 3-layer failure:
1. dictionary.rtf has bad data ("Fran Schneider" instead of "Fran Snyder")
2. Reader miscategorized as `steno_artifact` instead of `name_uncertain` (Rule 8 violation)
3. Writer Rule 8 already exists for this case but its trigger conditions didn't match because Reader miscategorized

Recommended fix (Option D from the recon): a Writer-side mechanical safety net that doesn't depend on Reader categorizing correctly:

> "If source=case_dict (or phonetic_match) AND proposed `to` introduces a proper noun (person/company name identified in reader_note) AND that name is not in NAMES_LOCK -> FLAG."

Q1 recon confirmed FLAG infrastructure works downstream. Spec is unblocked.

This rule is RESTRICTIVE (do less, hand back to MB instead of guessing). Failure mode is "MB sees more flagged proposals" -- which is correct behavior. Cannot introduce wrong names; can only prevent commits to uncertain ones.

Spec pattern Sunday established: spot-check -> spec -> recon (Sonnet) -> build (Sonnet) -> verify (Sonnet, against blocks 537/540) -> review (you) -> Scott pushes.

Edit target is WRITER_PROMPT_V1 in `src/mrx_engine_v1/stage3/suggester.py` (lines 383-478). Sonnet's writer-prompt recon already mapped the territory.

### Priority 2: halprin_full re-render

Validate the cumulative effect of Sunday's 6 fixes against the full 305-page transcript. Single API spend overnight. Compare new diff bucket counts vs Sunday's scoreboard:

- Sunday baseline: Bucket A = 161 engine bugs, Bucket B = 518 editorial, Bucket C ~= 50 validator-protected, Bucket D = 61 unknown, total 740
- Target after Sunday's fixes: Bucket A <= 145 (closing 13 hyphenation + ~5 phonetic from span discipline broaden = ~18 closures expected)

Don't decide to spend the API casually. Confirm with Scott first.

### Queue (if energy holds)

- acronym_mangle spot-check (17 blocks) -- probe drafted Sunday, in your back pocket; ask Scott to paste it
- doubled_word residual investigation (28 blocks remain after morning fix -- why?)
- word_drop residual (17 blocks remain after validator)
- Remaining hyphenation patterns (8 blocks: fractions, non-X, yearend, writeoff)

DO NOT spec these tonight. Day-2+ backlog also includes:

- Aligner+Differ v0 spec -- THE big architectural play, addresses the 518 Bucket B editorial diffs that no engine fix can close
- Bootstrap tooling (bootstrap.ps1, run_full_depo.ps1, RUNBOOK.md) -- Saturday's leftover
- D-WRITER-WORD-DROP Part C -- Writer prompt hardening (belt-and-suspenders)
- Phonetic-correction allow heuristic (16 SAFE candidates from Sunday's analysis)

## Sunday's discipline -- locked, do not break

- Spot-check before every spec (validated 5+ times Sunday, every time the recon caught something)
- Rule sheet header on every spec (Universal? Code/Prompt? File path? Commit prefix?)
- Default to MB-specific when unsure -- easier to promote than demote
- Sonnet never commits or pushes independently; Scott pushes
- Halprin OUR_FINAL files NEVER push to public repo (gitignore enforces)
- Push ONLY: engine code, tests, reports without raw transcript content
- Two distinct handoff files (Opus + Sonnet, never combined)
- Ping every 10 min or at logical break
- Code-fenced blocks for ANY content Scott copies to Sonnet
- When asking Sonnet to paste a URL, specify "PLAIN TEXT, no markdown link, no auto-hyperlink" -- terminal auto-linking broke URL fetches twice Sunday

## Lessons from Sunday -- keep front of mind

1. **Read-Write Separation is real.** When a fix looks like a "Writer" fix, check whether the bug is upstream in Reader's anomaly categorization first. The D-WRITER-COMPOUND-SPAN spec became D-READER-COMPOUND-SPAN after recon flipped the target.

2. **The validator is mature and usually right.** Test the assumption that the validator is wrong before patching it. Sunday's afternoon recommendation was Option A (fix validator); Sonnet's evening recon flipped to Option B (fix Reader span generation). Always test the validator-is-wrong hypothesis before acting on it.

3. **Dictionary data quality is its own failure mode.** The "Fran Schneider" bug originated in dictionary.rtf, not in any engine logic. Future architectural work should think about dictionary integrity guardrails as a separate concern from prompt rules.

4. **Restrictive rules are safer than permissive ones.** Every Sunday fix that landed cleanly was restrictive: validator blocking word drops, Reader narrowing spans, Writer FLAG-instead-of-REWORD. Rules that say "do less" can't introduce new bugs.

5. **Auto-compact during Sonnet's work survives if context is well-summarized.** Both Sunday compacts (afternoon + evening) held cleanly. Scott now sends a focused resume note rather than a full re-ramp when compact happens mid-task.

## Scott's state at handoff

Sunday night, end of an 11+ hour day. Calm, sharp, embraced the grind. Shipped his best day on the project. The architectural call he made on Three Sealed Phases is the most consequential moment in the project history alongside the Aligner+Differ design from Saturday night. He's not in a rush -- Monday is a continuation, not a sprint.

He explicitly told Sunday evening Opus: "I'm calm. I'm collected. I'm embracing the grind. My background is QA. I want to be right." Honor that mindset. Slow is smooth. Smooth is fast.

He also surfaced a hard architectural conviction Sunday evening: he does NOT want the obligation of AI touching final transcripts. Under subpoena, he wants the logic to hold up -- auditable, even if imperfect. That's the Three Sealed Phases driver, and it's a permanent design constraint going forward.

## Coder mindset for Monday

Slow is smooth. Smooth is fast.
RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT.
RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe -> STOP, flag.

-- End of Opus Monday ramp --
