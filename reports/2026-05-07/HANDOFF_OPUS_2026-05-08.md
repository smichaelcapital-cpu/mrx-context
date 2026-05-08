# HANDOFF — Opus, end of 2026-05-07 session
For: Fresh Opus, next session (Friday 2026-05-08, daytime)
From: Opus 2026-05-07 evening session
Companion file: reports/2026-05-07/HANDOFF_SONNET_2026-05-07_eod.md (read both before starting)

## Read this first — the goal Scott set for Friday
Friday is a full daytime build day, not a phone-only review day. Scott will be available and ready to grind.
Scott's stated goal for Friday: "I want to be able to say what we can do from the steno systemically."
Translate that: Scott wants to know, by end of Friday, the upper bound of what the engine can extract from the steno alone — without audio, without MB's per-style codes, without any fixture cheating. What does pure structural + deterministic + Stage 3 LLM correction get us, ceiling-wise, working only from CaseCATalyst RTF + steno strokes?
That's the framing for tomorrow. Not "ship one more rule" — but "what does the steno-only ceiling look like, and how close are we to it?"

## What shipped tonight (locked, on main)
Q-DROP M1

- Commit 922aa0e on smichaelcapital-cpu/mrx_engine_v1 main
- Spec: in-session, not yet saved to specs/qdrop_m1.md on disk (gap — flag for Friday)
- Files: src/mrx_engine_v1/stage2/qdrop_m1.py, src/mrx_engine_v1/stage2/pipeline.py, tests/stage2/test_qdrop_m1.py
- Result: total diff blocks 76 → 65. A-side 27 → 16. Orphan warnings 287 → 0.
- Caveat: see "M1 unverified against MB's actual style" below.

## 3a (is_doubled classifier fix) — built but uncommitted

- Code complete on disk, 10/10 tests passing
- File path: src/mrx_engine_v1/classifier/is_doubled.py + tests at tests/classifier/test_is_doubled.py
- Result: doubled_word bucket 27 → 22 (5 false positives killed)
- Surprise: 3 blocks the 2026-05-06 evidence had tagged as false positives turned out to be real OUR defects (#66 well-well, #593 the-the, #663 a-a). This means the 2026-05-06 evidence file is partially mis-tagged.
- Decision pending: do we commit 3a tomorrow regardless of M1 question? (Probably yes — it's classifier-only, independent of any pipeline rule.)

## The M1 caveat — honest assessment
M1 was built tonight on solid evidence: a 339-turn position-check showing 100% structural promotion (after edge cases). 10 unit tests. Net diff dropped 11 blocks.
Then MB replied to Scott's email with a vague example showing a different format — Q. on one line with the next utterance indented underneath, no second Q. label. Scott emailed her back asking for a real Brandl example. She may not reply for days, or at all.
Scott's call (relayed at end of session): Do not block on MB. Make a decision and keep moving with the caveat that we may be wrong. Wrong is recoverable; stalled is not.
This is the right call. The session-end position is therefore:

- M1 stays shipped unless MB confirms otherwise.
- 3a is independent of M1 and can ship.
- 3b drafting was paused mid-flight (Opus reached cross-turn boundary section). Should resume Friday.
- If MB replies with a real example contradicting M1, we revert commit 922aa0e and redesign. Until then, we proceed.

Document this exactly in any new spec: "Built on the assumption M1 is correct. If M1 is reverted, this spec needs re-evaluation."

## Tonight's spec slate — status

| # | Spec | Status | Next move |
|---|---|---|---|
| 1 | Q-DROP M1 | ✅ Shipped, pushed | Save spec to disk at specs/qdrop_m1.md (gap) |
| 2 | Running Ledger structure | 🟡 Not started | Spec on Friday — captures MB-specific findings vs. CR onboarding questions |
| 3a | is_doubled classifier fix | 🟢 Built, uncommitted | Commit Friday (independent of M1) |
| 3b | D-DOUBLED-WORD engine fix (across-punct + case + cross-turn) | 🟡 ~40% drafted | Resume Friday after M1 question is decided |

## Friday's setup — recommended order of operations

### Block 1 (first hour, before any code work)

Re-read the M1 evidence files in this exact order:

1. reports/2026-05-07/qdrop_m1_position_check_339.md
2. reports/2026-05-07/qdrop_m1_no_entries_deepdive.md
3. reports/2026-05-07/qdrop_m1_new_qside_diffs.md

Read MB's reply email and any new reply if she sent one overnight. Decide one of three paths:

- **Path A** — MB confirmed M1 is correct: Commit 3a. Resume 3b drafting. Both fast wins.
- **Path B** — MB contradicted M1: Revert 922aa0e. Redesign Q-DROP rule from scratch. Stop everything else.
- **Path C** — MB silent: Treat M1 as provisionally correct. Commit 3a (independent anyway). Move to ceiling work below.

### Block 2 (the real Friday goal — the steno ceiling)
This is what Scott actually wants Friday to produce. Do not let Block 1 eat the whole day.

Question to answer by end of Friday: Without audio, without MB's per-style overrides, what is the maximum closeable diff-block percentage on brandl_50pp using only steno + Stage 1 + Stage 2 (deterministic) + Stage 3 (LLM)?

To answer that, we need a steno-ceiling triage of the current 65 diff blocks (or whatever the count is after 3a + any Friday work). Sort every remaining block into one of these categories:

1. Closeable by Stage 2 deterministic rule (more rules in M1's mold)
2. Closeable by Stage 3 LLM tightening (better prompts, better proof-of-work)
3. Requires audio (MB heard something the steno couldn't represent)
4. Requires per-CR style codes (MB-specific style choices, not steno-recoverable)
5. Pure reporter craft (em-dashes, paragraph breaks, quote nesting — likely audio + style)

The deliverable: reports/2026-05-08/steno_ceiling_triage.md. Numbers per category. Worked examples.
That gives Scott a concrete answer to "what can we do systemically from the steno." It also tells us where the 80/20 lives for the next two weeks of work.

### Block 3 (parking lot, only if Blocks 1-2 finish early)

- Resume 3b drafting (across-punct + case + cross-turn for D-DOUBLED-WORD)
- Spec the running ledger structure (#2)
- Spec button_up.py to handle the 5 untracked files automatically

## Untracked disk debt — handle it Friday
Per Sonnet's earlier flag, these files need disk decisions (commit / leave / delete):

- io/analysis/brandl_50pp/_run_brandl_stage3.py (gitignored, not in repo — pending move to scripts/run_brandl_stage3.py and commit)
- run_stage3.py
- run_full_depo.ps1
- depo_paths.psd1
- src/stage5/parse_rtf_frontmatter.py

Plus the new uncommitted 3a files (decision is straightforward — commit if MB doesn't contradict M1, or even unconditionally since 3a is classifier-only).
Best home for this: a button_up.py script that walks Scott through it once instead of asking 30 times. Spec it Friday if there's room.

## Lessons from tonight (for the running ledger when we build it)

### Column A — MB-specific findings earned tonight

- MB rewrites garbled rough s2 utterances at audio-review time. Position-check failures on s2 turns often indicate content rewrites, not structural rule violations.
- MB preserves legitimate witness stutters in finals ("had had", "I I", "until until", "Okay. Okay.").
- MB possibly does not promote s2 continuations to standalone Q. lines — instead keeps them under the same Q. label with indented continuation. Unverified. Pending real example.

### Column B — CR onboarding questions earned tonight

1. When the rough has steno-garbled or fragmented attorney utterances, do you rewrite from audio or preserve the rough? Show 2 examples.
2. When a witness's answer continues the prior topic, do you keep the next attorney utterance under the same Q. or start a new Q.? Show 3 examples from your finals — rough vs. final side by side.
3. Do you preserve witness stutters in your finals, or clean them up? Examples.
4. How do you format Q. continuations — standalone new Q. line, or indented under the previous Q. label?

## Process notes

- Position-check evidence files can be misleading if the rule under test is structural-only and MB's actual rule includes content rewrites. Tonight's 339-position check missed this — we need at least one real MB example to anchor any future structural rule.
- Evidence files from prior sessions can be partially wrong. The 2026-05-06 doubled_word evidence had 3 blocks mis-tagged. Re-verify evidence before building specs on it.
- Fire-hose protection: Scott called good time-outs tonight. Pencil discipline worked. Two stop-and-check moments (5 NO entries, +1 Q-side block) caught real issues.

## What Scott needs from Opus on Friday — communication rules

- Plain English, 12-year-old reading level
- One question at a time
- No A/B/C unless asked
- One code block per response when something goes to Sonnet
- Disk wins. Check disk before theorizing.
- Pencil. Slow is smooth.
- Halprin and Brandl FINALs NEVER push to public repo
- Scott pushes; Sonnet commits but does not push

## Quick state ledger

| Item | Value |
|---|---|
| Latest commit on mrx_engine_v1 main | 922aa0e (M1) |
| Push status | Pushed to origin/main |
| Doubled_word bucket count, post-M1 pre-3a | 27 |
| Doubled_word bucket count, post-M1 post-3a (uncommitted) | 22 |
| Total diff blocks, post-M1 | 65 |
| MB email | Sent, awaiting real Brandl example |
| Pending disk decisions | 5 untracked + 4 new 3a files |

---

End of handoff. Next Opus: read this top to bottom, then read the Sonnet handoff, then ask Scott his decision on Path A/B/C from Block 1 above.
