# HANDOFF — OPUS — 2026-05-16 MID-SESSION (~11:15 AM swap)

You are fresh Opus replacing the morning's Opus. This handoff is written candidly because the prior Opus session ended poorly. Read it carefully.

## WHAT WENT RIGHT TODAY

Real wins. Don't lose sight of these:

- B1.7.5 black_bp cover merged (f876fcd) — 6 of 6 MB depos now render end-to-end
- B1.7.6 Olsen reporter anchor merged (842e406)
- B1.8.1/2/3 — built and merged a working side-by-side review harness
- RULE-19 (dual-lane Sonnet operation) live and working
- Defect ledger committed (6dc0067) — 5 defects identified, 1 closed, 4 open

That's a real morning of shipping.

## WHAT WENT WRONG TODAY

Late morning, after the harness was working, Scott did a personal read-through of Olsen + Halprin and surfaced 5 defects. Opus spec'd B1.9.1 (D-2 firm-group separator fix). Sonnet #2 took the recon, tried to build, hit oracle inconsistency — different depos demand different separator behavior. Sonnet's two fix attempts each broke a different depo. He stopped, correctly, and flagged to Opus.

**The deeper failure was Opus's, not Sonnet's.** Scott had explicitly told prior Opus this morning: "don't byte-chase a single oracle — derive MB's style from her body of work using the fingerprint files." That note is in Scott's project memory. There is a `fingerprints/` directory in the repo for exactly this purpose. Prior Opus ignored both and spec'd the fix off single-oracle observations.

Scott called this out, hard. Fair callout. He has spent the past four sessions watching this same pattern repeat.

## WHAT YOU MUST INTERNALIZE BEFORE TOUCHING ANY CODE

1. **MB's oracle files are NOT internally consistent.** Different depos use different separator behavior, indentation, encoding. You cannot fix the renderer to byte-match all 6 simultaneously. It's mathematically impossible.

2. **The 80% rule.** Pull frequency distribution from fingerprint files. Build the renderer to match the DOMINANT pattern. Edge cases get a TODO and move on.

3. **The harness is great for SEEING drift. It is NOT a fix-everything target.** Diff lines come from at least three sources: encoding (non-breaking spaces), indentation off-by-one, and genuinely inconsistent oracle separator behavior. Don't conflate them.

4. **Fingerprint files exist for a reason.** Use them. The prior Opus did not.

5. **Scott has limited patience for spinning.** "Slow is smooth" does not mean "exhaustively explore every edge case." It means deliberate, not slow.

## STATE AT SWAP

- **Main:** all today's merges through B1.8.3 are live. Defect ledger committed.
- **B1.9.1 (D-2 firm-group separator):** STOPPED, not merged, branch laneB/B1.9.1-firm-group-separator may still exist with reverted source. The spec is invalid as written. Close the branch on next session.
- **Sonnet #1 (laneA):** was doing D-5 cross-check recon when session ended. May have output landing. Read his report when it arrives.
- **Sonnet #2 (laneB):** parked clean after stopping B1.9.1.
- **Fingerprint task:** drafted but NOT sent. Should be the FIRST task of next session.

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_FRONT_MATTER_DEFECT_LEDGER.md
3. This handoff
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/tech_debt.md
5. Sonnet #2's B1.9.1 stop report (in his chat, search for "Three distinct oracle behaviors observed")
6. The fingerprint files (paths TBD — find them yourself, do not ask Scott)

## CRITICAL — DO NOT REPEAT

- Do not spec ANY renderer fix without first pulling frequency data from the fingerprint files.
- Do not write a fix that "looks at one or two oracle pages and proposes a rule." That has failed every time.
- Do not stack questions to Scott. One question, one answer.
- Do not propose A/B/C choices when there's an obvious right answer.
- If a fix needs more than 2 oracle data points to validate, you're in a swamp. Pull back.

## OPEN DEFECTS — PRIORITY ORDER (DO NOT START FIX WORK UNTIL FINGERPRINT DATA IS IN HAND)

1. D-2 firm-group separator — RE-SCOPE based on fingerprint frequency
2. D-1 Page header on INDEX — universal cosmetic, may be the quick win to ship something
3. D-4 Olsen Reporter cert slot — Olsen-specific
4. D-5 Olsen exhibits packing — depends on Sonnet #1's recon report
5. B1.7.7 Olsen VIDEOGRAPHER — backlog

## OPEN STRATEGIC QUESTION

Scott raised this morning and again at session end: when a 7th depo arrives with no MB final, how do we validate? Today's harness is Layer 1 (byte-match against existing finals). Layer 2 (style profile derived from frequency across all known depos) is the bet. **Layer 2 starts with the fingerprint files.** Do not put off Layer 2 thinking — it should inform every renderer decision going forward.

## YOUR FIRST TASK NEXT SESSION

1. Read all 6 ramp files
2. Pull the fingerprint file data — find it, read it, know what it tells you about MB's frequency distribution on firm-separator behavior, INDENT_FIRM spacing, Unicode space handling
3. Confirm in ONE LINE to Scott: "Ramped Opus 2026-05-16 [datetime] post-stop. Ready." plus one sentence on what the fingerprint data shows and one recommendation for D-2 re-scope
4. Wait for Scott

## DO NOT

- Apologize to Scott on his behalf or yours. He doesn't want it.
- Recap what went wrong. He lived it.
- Send the fingerprint task to Sonnet as YOUR first move — read the fingerprint files yourself first, understand them, THEN task Sonnet.

## REMEMBER

The 40-year-old single mom does this in 40 minutes. We are eight days in. Scott's patience is gone. Every minute spent on something that doesn't ship costs trust. The next session's job is to ship one real fix using the data Scott already gave us months ago via the fingerprint files.
