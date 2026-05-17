HANDOFF — OPUS — 2026-05-16 EOD

You are fresh Opus arriving for the next MRX session. Scott just
finished a 6-hour session that shipped B1.9.3 (cycle continuity
fix). This handoff is candid because the session was a real win
and you should know exactly what landed.

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_GET_IT_WORKING_FIRST.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_FRONT_MATTER_DEFECT_LEDGER.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_FINGERPRINT_13_DEPO_FREQ.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_MB_QUESTION_D5_EXHIBITS_START.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-16_MIDSESSION.md
9. This handoff in full

Confirm in ONE LINE: "Ramped Opus 2026-05-16 EOD handoff. Ready."
Plus one sentence on session priorities. Plus one recommended
first action.

DO NOT skip the ramp files. Today's Opus initially tried to skip
them and got called out by Scott. Read everything.

## ONE-LINE STATE

B1.9.3 cycle continuity fix shipped to main — every depo improved
or held, halprin clean at 25/25. Phase 2B stashed on laneB for
pickup. D-5 awaits MB ping. Two new infrastructure conversations
queued.

## WHAT SHIPPED THIS SESSION

### Code (engine repo, laneB merged to main)
- 1A/1B/1C/2A — B1.9.3 cycle continuity fix
- Defects D-2 and D-4 closed via dominant-pattern rules
- Defects D-1 and D-3 closed as phantoms

### Knowledge (mrx-context, all pushed)
- 2026-05-16_FRONT_MATTER_DEFECT_LEDGER.md — updated with closures
- 2026-05-16_FINGERPRINT_13_DEPO_FREQ.md — 13-depo frequency data
- 2026-05-16_MB_QUESTION_D5_EXHIBITS_START.md — MB ping draft
- 2026-05-16_GET_IT_WORKING_FIRST.md — locked principle + revisit list
- tech_debt.md — TD-003 added (harness display width)

### Specs
- 2026-05-16_B1.9.3_MAIN_SUB_CYCLE_CONTINUITY.md — shipped
- 2026-05-16_B1.9.4_PAGE_HEADER.md — closed (phantom)

## NEW DISCIPLINES LOCKED THIS SESSION

1. **Peer review before merge.** Opposite-lane Sonnet reviews
   every multi-file change before merge to main. Builder does not
   merge their own work. This caught real things on B1.9.3 —
   wrong commit count in the brief, pre-existing test failures,
   improved scores beyond what builder reported.

2. **Data before decision.** Pull more oracle data before fixing
   a defect off a small sample. 6 depos couldn't settle D-2/D-4/D-5.
   13 depos could. The 80% rule decides: >=80% -> ship; 60-79% ->
   ship with low confidence flag; <60% -> MB decides.

3. **Working first, perfect later.** Ship what works. Stash what's
   partial. Add it to the revisit list. Move on. We stopped Phase
   2B at "15 lines from done" because the session was long and
   Sonnet was post-compact — bird in hand beat hand in bush.

4. **The Stanley thermos principle.** Take complex things, make
   them simple. The thermos works every time. No app, no settings,
   no firmware update. That's the standard for everything we build.

## TWO INFRASTRUCTURE CONVERSATIONS QUEUED FOR NEXT SESSION

### A. Handoff process redesign
Current handoffs/ directory has 30+ files mixing fresh and stale.
Scott wants:
- Top-level master README
- `current/` tier (last 48 hours)
- `archive/YYYY-MM/` per project
- Per-project subdirectories: myreporterx, future addons, future website

Open question: when does current -> archive happen? (auto, manual at
EOD, or on next-session start)

### B. Rule sheet additions
Today's three new disciplines need to be formalized as RULE-21, 22,
23 in RULE_SHEET_v1.md (or promote to v2). The Stanley thermos
principle belongs in CODER_MINDSET.md, not the addendum — it's
philosophy, not a rule.

## REVISIT LIST (carries forward)

- B1.9.3 Phase 2B — stashed on laneB/B1.9.3-cycle-continuity
- D-5 MB decision pending — MAIN-first default holds
- B1.7.7 Olsen videographer cosmetic
- Unread front matter pages: williams, butler, blanks, black_bp
- Unread back matter pages: halprin, williams
- TD-003 harness display width
- Church depo ingest failure (12x raw/final ratio anomaly)
- Infrastructure book of work — needs structured kickoff

## SCOTT'S WORKING STYLE — DO NOT VIOLATE

- 12-year-old reading level
- ONE question at a time, never stacked
- Short answers, no firehose
- Inline A/B/C only when there's a real choice
- Lead with recommendations, don't ask open-ended
- Full absolute paths always
- Sonnet writes files, Scott pushes commits
- Halprin and Brandl FINALs NEVER push to public repo

If you firehose Scott or skip the ramp files, he will call it out.
He's right when he does. Listen.

## SCOTT'S MOOD AT SIGN-OFF

Strong. The session shipped real code and surfaced a new discipline
(peer review before merge) that he called the best engineering move
of the project. He's tired but satisfied. Walk into next session
like a continuation, not a fresh start.

## CODER MINDSET REMINDERS

Before any code change: "Could this change reduce transcript
accuracy or credibility?" If yes or maybe -> STOP, flag to Scott.

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK.
RULE-INPUT-IS-SACRED. RULE-PEER-REVIEW-BEFORE-MERGE (new today).

Slow is smooth. Smooth is fast.
