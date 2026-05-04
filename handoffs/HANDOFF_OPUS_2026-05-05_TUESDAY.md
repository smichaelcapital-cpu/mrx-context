# OPUS HANDOFF — Tuesday 2026-05-05 morning

To:    Fresh Opus, Tuesday morning session
From:  Opus, Monday session
Owner: Scott

## Read in order — DO NOT SKIP

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/backlog/THREE_SEALED_PHASES.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-04/halprin_full_scoreboard_v2.md  <- READ THIS, FRESH SCOREBOARD
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-04_MONDAY.md (Monday's ramp — for context on what landed)
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-05_TUESDAY.md (Sonnet's Tuesday ramp — read so you know what fresh Sonnet was told)
8. This handoff in full

After reading: confirm in ONE LINE: "Ramped Tuesday morning. Ready."

## Walk in calm. Tuesday is a phone-only review day.

Per Scott's weekly rhythm: Mon/Fri are full build days. Tue–Thu are
phone-only review days — decisions, spec approvals, planning only.
NO heavy build work today. Treat Tuesday as analysis and direction-
setting before Friday's next build push.

## What shipped Monday — 6 commits

| # | Commit | What | Type |
|---|--------|------|------|
| 1 | c17c1c7 | Rule 8a (Writer prompt proper-noun guard) | universal |
| 2 | ac9a234 | "the the" fix (SAFE_LIST tightening) | universal |
| 3 | 6bc2129 | Year-range slash → hyphen (T3) | universal |
| 4 | 873141a | Bates rejoin (YR-XXXXXX) | mb-specific |
| 5 | e1f86d0 | proposal_mapper collision tolerance | universal |
| 6 | 6ee8750 | v2 scoreboard report | report |

Plus halprin_full re-render: $6.43 API spend, 959 proposals applied,
983 anomalies found, full OUR_FINAL.txt rendered.

Test count at end of day: 681 passing + 1 pre-existing failure
(test_E2E3_wt_has_misses — stale expectation from Sunday's W&T fix,
backlog cleanup item).

## Monday's two big lessons — internalize

### Lesson 1: Prompt-only enforcement does not work for safety rules

D-WRITER-FLAG-NOT-REWORD shipped as Rule 8a. Tests passed. Live
re-render: model overrode the rule on high-confidence case_dict
proposals. Twice. Same Fran Schneider failure as before.

The v2 scoreboard confirms it: Rule 8a had **zero measurable
bucket impact** on the 305-page render.

This is hard evidence — not theory — that the Three Sealed Phases
architecture is necessary. AI in the write phase will override
instructions when confidence is high. Code-level enforcement is
the only reliable path.

For Tuesday: do NOT propose more prompt-side safety patches. Any
new safety work goes code-side or waits for the architecture.

### Lesson 2: The diff bucket scoreboard moved less than hoped

V1 scoreboard (Sunday): Bucket A = 161 engine bugs.
V2 scoreboard (Monday): Bucket A = 153 engine bugs (-8).

Across 10 fixes shipped Sun+Mon, only 8 real diff blocks closed.

The +5 phonetic and +8 objection_style numbers are reclassification
artifacts from SequenceMatcher realignment after fixes shifted
positions, NOT regressions. Still — net real progress is small.

What this means: marginal returns on incremental engine patches.
The 518-block Bucket B (MB editorial) is the real volume, and
Bucket B doesn't move until Aligner+Differ ships. Tuesday's
strategic conversation should weigh: more Stage 2 transforms vs.
starting Aligner+Differ vs. starting Three Sealed Phases retrofit.

## Tuesday's plan — REVIEW DAY, no heavy build

### Priority 1: Scott reads v2 scoreboard with fresh eyes

Before any conversation with Opus: Scott reads
reports/2026-05-04/halprin_full_scoreboard_v2.md cold. Forms his
own read on what closed and what didn't. THEN brings questions to
this session.

### Priority 2: Three-way strategic conversation

The big call coming this week: where does engineering effort go
next?

Option A: More cheap Stage 2 transforms (close ~5-10 more Bucket A
blocks per fix, but marginal returns visible).

Option B: Start Aligner+Differ v0 spec (THE big architectural play,
attacks the 518 Bucket B blocks, hardest design problem on the
project).

Option C: Start Three Sealed Phases retrofit spec (most consequential
long-term, addresses the Rule 8a failure mode permanently, but huge
scope).

Don't force a decision Tuesday. Lay out tradeoffs cleanly. Scott
decides.

### Priority 3: Bible vs Bucket B recon (queued from Monday)

If energy allows after the strategic conversation, paste the Bible
vs Bucket B recon prompt to Sonnet. This was queued Monday but
held when Scott pivoted to the re-render. Answers MB's question:
"if quotes/dashes are general punctuation rules, why doesn't the
Bible catch them?" Pure recon, no API spend, ~1 hour Sonnet work.

### Queue (do NOT spec Tuesday)

- doubled_word residual T-WS5 (7 real bugs identified Monday)
- acronym_mangle deeper fixes (10 real bugs, 4 already done as
  date-range + Bates)
- Stale test cleanup: test_E2E3_wt_has_misses (5-min job)
- Aligner+Differ v0 spec proper
- Three Sealed Phases retrofit scoping
- Phonetic-correction allow heuristic (16 SAFE candidates from
  Sunday's word_drop_rejection_classification.md)

## MB context Scott needs to remember

Sunday/Monday MB confirmed: quotes/dashes are added during
proofread, not live. Exception: if attorney says "quote" out loud,
quotes go in live. This confirms Bucket B is genuinely editorial,
not engine.

MB also pushed back: "if those are general punctuation rules,
why aren't we catching them in the Punctuation Bible?" — that's
the recon question for Sonnet (Priority 3 above).

## Scott's state at Monday handoff

End of a long day. 6 commits shipped. Was working in parallel
during most of the session — mentally split between this and his
day job. Asked good architectural questions ("expose all the dirty
laundry"), made the right call to run the re-render. Embraced the
Sunday lesson: slow is smooth.

He explicitly noted he was confused mid-day during the re-render
kick — that's a flag that Tuesday should NOT stack decisions or
fire-hose. ONE question at a time. Phone-only review day means
short, simple, decision-focused exchanges.

## Standing rules — non-negotiable

- 12-year-old reading level until told otherwise
- Plain English, ONE question at a time, never stack
- Code-fenced blocks for ANY content Scott copies to Sonnet
- Plain text URLs only when Scott pastes to Sonnet
- Halprin OUR_FINAL files NEVER push to public repo
- Sonnet never commits or pushes independently; Scott pushes
- Two distinct handoff files (Opus + Sonnet, never combined)
- Slow is smooth. Smooth is fast.
- Before any code change: "Could this reduce transcript accuracy
  or credibility?" If yes or maybe → STOP, flag.

## Coder mindset for Tuesday

RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT.
RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Tuesday is review/strategy, not build. Honor the day's purpose.

— End of Opus Tuesday ramp —
