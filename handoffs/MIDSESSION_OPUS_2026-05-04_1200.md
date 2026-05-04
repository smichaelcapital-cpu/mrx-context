# MID-SESSION OPUS HANDOFF — Monday 2026-05-04 ~12:00pm

To:    Fresh Opus, Monday afternoon session
From:  Opus, Monday morning session
Owner: Scott
Status: Mid-session handoff. Today is a Monday build day. Scott is
        working his day job in parallel and may or may not be
        available — work continues regardless until energy fades.

## Read in order — DO NOT SKIP

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/backlog/THREE_SEALED_PHASES.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-04/halprin_full_scoreboard_v2.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-04/defect_inventory_v1.md  <- READ THIS, TODAY'S STRATEGIC ANCHOR
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-04/bible_vs_bucket_b_recon.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-04_MONDAY.md (the morning ramp — for context on what landed)
9. This handoff in full

After reading: confirm in ONE LINE: "Mid-session ramped. Ready to drive."

## What's already shipped today (Monday morning session)

6 commits pushed to main:
- c17c1c7 universal: Rule 8a (Writer prompt proper-noun guard)
- ac9a234 universal: D-DOUBLED-WORD-THE (SAFE_LIST tightening)
- 6bc2129 universal: T3 year-range slash -> hyphen
- 873141a mb-specific: Bates rejoin
- e1f86d0 universal: proposal_mapper collision tolerance
- 6ee8750 report: v2 scoreboard

Plus halprin_full re-render: $6.43 API spend. 959 proposals applied,
983 anomalies, 24 validate drops. Output on disk at
io\analysis\halprin_full\_stage5_out\halprin_full.OUR_FINAL.txt.

Test count: 681 passing + 1 pre-existing failure
(test_E2E3_wt_has_misses, backlog cleanup item).

## The defect inventory just changed the strategic picture

Read defect_inventory_v1.md cold before doing anything else. The
headline numbers from the 738-block analysis:

| Verdict | Count | % |
|---|---|---|
| CLOSEABLE_NOW | 121 | 16.4% |
| CLOSEABLE_WITH_ENGINE_WORK | 198 | 26.8% |
| NEEDS_THREE_SEALED_PHASES | 2 | 0.3% |
| NEEDS_AUDIO | 279 | 37.8% |
| REPORTER_OWNS_FOREVER | 135 | 18.3% |

Three reads:
1. Current architecture ceiling: 321 blocks (43.5%) closeable
   without new tools. That's the runway.
2. Audio unlocks 279 blocks (37.8%) — Stage 4 is the biggest
   single lever, NOT Three Sealed Phases.
3. Three Sealed Phases urgency dropped — only 2 blocks need it for
   diff-closure. Still right for legal defensibility, but not for
   volume.

Sonnet flagged ONE estimate as shaky: cap_proper (198 Bucket B
blocks, comma insertion family). Sample was only 15 of 198. Needs
dedicated recon before any spec.

## What's in flight when you take over

Scott approved the next two-task arc just before this handoff:

**TASK 1 (Sonnet, ~1.5 hr): cap_proper deep recon**
- Sample 50+ of the 198 cap_proper blocks (vs original 15)
- Output: which sub-patterns are CLOSEABLE_NOW vs CLOSEABLE_WITH_
  ENGINE_WORK vs misclassified
- Target: reports/2026-05-04/cap_proper_deep_recon.md
- This unblocks the biggest single category in the inventory.

**TASK 2 (Sonnet, ~1 hr after Task 1): pick highest-volume
CLOSEABLE_NOW pattern from inventory, deep recon it**
- Top candidates: phonetic_error (33), doubled_word residual (29),
  hyphenation residual (25)
- Sets up the next spec build

If Sonnet hasn't started yet when you arrive: the Task 1 recon
prompt is in the morning Opus chat history. Re-issue it cleanly.

## Items in the queue (do NOT spec without Scott's call)

- Three Sealed Phases Exhibit A doc — was on Opus's plate at handoff,
  ~30 min. Locks today's Rule 8a failure as evidence. Skim
  reports/2026-05-04/writer_flag_not_reword_pow.md if writing this.
- Stale test cleanup: test_E2E3_wt_has_misses (~5 min Sonnet)
- Audio integration scoping (when fresh enough to think about it)
- Aligner+Differ v0 scoping (now lower priority given inventory —
  audio is the bigger lever)

## Standing rules — non-negotiable

- 12-year-old reading level until told otherwise
- Plain English, ONE question at a time, never stack
- Code-fenced blocks for ANY content Scott copies to Sonnet
- Plain text URLs only when Scott pastes to Sonnet
- Halprin OUR_FINAL files NEVER push to public repo
- Sonnet never commits or pushes independently; Scott pushes
- Two distinct handoff files (Opus + Sonnet, never combined)
- Slow is smooth. Smooth is fast.
- Scott may be working day job in parallel — work continues without
  him, ping when something needs his eyes

## Coder mindset

RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT.
RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Before any code change: "Could this reduce transcript accuracy or
credibility?" If yes or maybe -> STOP, flag.

— End of mid-session Opus handoff —
