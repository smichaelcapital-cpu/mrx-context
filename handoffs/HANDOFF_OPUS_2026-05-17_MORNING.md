# HANDOFF — OPUS — 2026-05-17 MORNING

You are fresh Opus on 2026-05-17 morning. Scott is founder and PM. Sonnet #1 and Sonnet #2 are builder agents in separate chats with terminal access to mrx-context and mrx_engine_v1 repos.

## STANDING RULES — non-negotiable

Same 18 rules from 2026-05-16. No changes. Particular emphasis tomorrow on Rule 18 (branch hygiene) given last night's incident.

NEW provisional rule pending Scott confirmation:
**RULE-SINGLE-SONNET-PER-CLONE** — Only one Sonnet operates on a given physical engine repo clone at a time. Parallel lanes require separate clone folders. See 2026-05-16 single-clone parallel work incident capture.

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-17_MORNING.md (this file)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_SINGLE_CLONE_PARALLEL_INCIDENT.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-15_BRANCH_DRIFT_INCIDENT.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_OLSEN_ARBITRATION_COVER_RECON.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/build-reports/2026-05-16_VERIFICATION_ALL_6.md
9. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/build-reports/2026-05-16_B1.7.4_SONNET1.md
10. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/fingerprints/ledger.md

## ORACLE FILE LOCATION — CAPTURED FOR FUTURE SESSIONS

`C:/Users/scott/OneDrive/Documents/mrx-context/oracle/finals/`

Contains FINAL oracle .txt files for all 6 MB depos. Use this path before hunting elsewhere.

## ONE-LINE STATE

5 of 6 MB depos render end-to-end on main commit 711eb26 (Halprin, Williams, Butler, Blanks, Olsen). black_bp is the last cover-renderer gap. Two separate Olsen appearances tiles deferred (B1.7.6 reporter anchor, B1.7.7 videographer slot).

## LAST NIGHT'S SHIPS

1. B1.7.3 — waive-mode stipulation renderer. Commit 19c33e3. Unblocks Butler, Blanks.
2. B1.7.4 — arbitration cover layout (count=1, loc_len=6). Commit 8319c22. Unblocks Olsen.
3. Merge to main: 711eb26 (--no-ff, both fixes shipped together after branch drift recovery).
4. Verification run on all 6 depos: 5 pass exit 0, 1 graceful skip (black_bp).
5. Knowledge captures: single-clone parallel work incident.

## SINGLE-CLONE INCIDENT — TLDR

Two Sonnets on one filesystem. Sonnet #2's B1.7.3 commit landed on Sonnet #1's branch. Sonnet #1 built B1.7.4 on top. Both fixes intermixed on one branch. Recovery: --no-ff merge to main with explanatory message. Cost: ~30 min. No code rework needed. Lesson: one Sonnet per clone until separate clones are set up.

## 3 DEFERRED TILES — PRIORITY ORDER

**B1.7.5 — black_bp cover loc_len=4 (TOP PRIORITY)**
- Blocks: black_bp (1 of 6 depos)
- Same family as B1.7.4 — add new `elif label_in_main and loc_len == 4:` branch to cover.py
- Recon needed: read black_bp oracle page 1 from /c/Users/scott/OneDrive/Documents/mrx-context/oracle/finals/0525black_bp/, design slot layout, implement, verify
- Estimated 30-45 min build after spec
- Recommended builder: single Sonnet, the only Sonnet awake

**B1.7.6 — Olsen appearances reporter anchor**
- Blocks: nothing critical; cosmetic 1-line drift
- Scope: appearances_renderer.py hardcodes reporter_anchor_line=19; Olsen oracle shows line 18
- Options: (a) accept delta, (b) make per-depo data field, (c) per-depo override
- Recommendation: (b) — generalize as per-depo field

**B1.7.7 — Olsen appearances VIDEOGRAPHER slot**
- Blocks: nothing critical; pre-existing 1-slot drift
- Scope: VIDEOGRAPHER renders at slot 14 main, oracle shows slot 15 sub
- Likely a position calculation in also_present handling for inline_label kind

## OPEN QUESTIONS FROM INCIDENT CAPTURE

Q1 — Dual-clone pattern (lane_a / lane_b folders)? Recommended: yes, eventually.
Q2 — Single-Sonnet-only default until dual-clone setup? Recommended: yes, immediately. Make this the rule for next session.
Q3 — Pre-commit hook for branch verification? Defer per capture.

## AGENT STATES AT SWAP

- Sonnet #1: fresh-ramp tomorrow. Carried last night's recovery and verification.
- Sonnet #2: hard-parked end of last session after incident. Fresh-ramp tomorrow.

## ONE-CUSTOMER FRAME

MB is the customer. 5 of 6 depos rendering on main is the demo-ready story tonight. B1.7.5 unblocks the 6th. After B1.7.5, MB sees her full body of work rendered through the universal pipeline.

## WHAT YOU DO FIRST

1. Read the 10 files above in order.
2. Confirm in ONE LINE: "Ramped Opus 2026-05-17 [datetime]. Ready." plus one sentence on state + one question for Scott.
3. Do not start work until Scott responds.

## LIKELY FIRST QUESTION FOR SCOTT

"Ready to spec B1.7.5 (black_bp cover loc_len=4), with single-Sonnet-per-clone rule in effect?"

## REMEMBER

- Slow is smooth, smooth is fast.
- One Sonnet per clone. Last night proved why.
- Spec saved BEFORE builder work starts.
- Ask before writing any spec.
- Oracle path: /c/Users/scott/OneDrive/Documents/mrx-context/oracle/finals/
