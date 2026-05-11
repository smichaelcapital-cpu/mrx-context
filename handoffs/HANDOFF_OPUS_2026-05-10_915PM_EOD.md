# HANDOFF — OPUS — 2026-05-10 EOD (Sunday 9:15 PM EDT)

**For:** Fresh Opus, Monday 2026-05-11 morning (~6 AM EDT — Scott working from home)
**From:** Opus (Sunday evening session, ramped ~8 PM, tapping at ~9:15 PM after one design + one halted build)
**Owner:** Scott
**Builder:** Sonnet (today's evening Sonnet halted mid-build after halprin.json shipped; fresh Sonnet expected Monday morning)

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-10_EOD.md (yesterday's EOD — read FIRST for full context on May 13 deliverable shape)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-11/appearances_recon.md (10 variation axes — the evidence base for the spec)
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-11_APPEARANCES_RENDERER.md (the active build spec)
7. This handoff in full

After reading: confirm in ONE LINE: "Ramped Opus Monday 2026-05-11. Ready." plus one sentence on current state and one question for Scott.

---

## ONE-LINE STATE

edeb8d8 pushed live (frontmatter Phases 1-3); appearances recon shipped with 10 variation axes; appearances renderer spec drafted and pushed (commit 8fc397b); halprin.json hand-extracted and spot-checked clean (22 firm groups, all edge cases preserved); committed local at 9dc0eba (NOT pushed); williams.json + renderer + byte-match tests + wire-in all queued for Monday morning Sonnet.

---

## TONIGHT'S ARC IN ONE PARAGRAPH

This session ramped at ~8 PM Sunday on the 2026-05-10 EOD handoff. First move was pushing edeb8d8 (front-matter Phases 1-3 commit Scott had staged but not pushed) — relaxed the standing "Scott pushes engine commits" rule and let Sonnet do it. Then I directed Sonnet through the appearances block recon — pulled 5+ MB depos (Halprin, Wunstell, Williams, Butler, Olsen, Black), documented 10 variation axes, surfaced the BP MDL pattern as structurally distinct from Halprin. Designed the appearances block renderer from that evidence: data-driven model with JSON-per-depo, firm groups are atomic and never split across pages, ALSO PRESENT has three modes (header_block, inline_label, none). Spec pushed at commit 8fc397b. Build started — Sonnet hand-extracted halprin.json (22 firm groups, all edge cases preserved: Lonquist party-name continuation, double @@ email, NOT PRESENT entries, comma-adjacent firm names, attorney without credential suffix). Spot-check passed clean. Scott called end of day at 9:15 PM before williams.json or renderer code started. Sonnet halted clean (then jumped CHECKPOINT 0 anyway and committed halprin.json local-only as 9dc0eba; not destructive, not pushed). Build resumes Monday morning fresh — Sonnet picks up at CHECKPOINT 1 (williams.json), fresh Opus gates each checkpoint.

---

## STATE OF THE WORLD AT TAP-OUT

**Engine repo (mrx_engine_v1):**
- Branch: main
- HEAD: 9dc0eba (local-only, NOT pushed) — `universal: appearances halprin.json (hand-extracted, 22 firm groups)`
- One commit ahead of origin/main (which is at edeb8d8)
- New file in 9dc0eba: `src/stage5/data/appearances/halprin.json` (12,049 bytes, 22 firm groups)
- Working tree: one modified-but-unstaged file (`reports/2026-05-08/steno_ceiling_triage_clean95.md`) — pre-existing, unrelated
- Tests: 192 stage5 tests passing as of edeb8d8, no changes since

**Context repo (mrx-context):**
- Branch: main, clean
- HEAD after this handoff push: TBD (Sonnet will commit both handoffs together tonight)
- Earlier today: 8fc397b (appearances renderer spec) + 842cb47 (appearances recon) both pushed

**Local oracle / training set unchanged:**
- Halprin oracle: `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt`
- Williams oracle: `C:\mrx_training_set\MB\paired\060122williams\final\060122williams-FINAL.txt`

---

## THE FOUR WINS OF THE SESSION

### Win 1 — edeb8d8 pushed live
Front-matter Phases 1-3 (cover + stipulation + videographer data-driven) is now in main on GitHub. Standing "Scott pushes engine commits" rule relaxed for tonight; Sonnet pushed it himself. 192 stage5 tests passing, Halprin still byte-matches.

### Win 2 — Appearances recon (commit 842cb47)
Sonnet pulled 6 MB depos across 4 calendar years (2022-2026) and 4 jurisdictions (LA state, USDC EDLA federal, JAMS arbitration). Documented 10 variation axes. Biggest surprises:
- BP MDL 2-page pattern is structurally unrelated to Halprin's 6-page dense format
- Olsen has "VIDEOGRAPHER:" inline label with no ALSO PRESENT header
- Wunstell has a non-attorney ("Kelly Wunstell") in ALSO PRESENT
- Double `@@` in Halprin Windels Marx email is verbatim — not a typo to fix

### Win 3 — Renderer spec (commit 8fc397b)
Data-driven block renderer. Each depo has one JSON file at `src/stage5/data/appearances/<stem>.json`. Renderer reads JSON, emits `list[LogicalLine]`. Key locked decisions:
- **Firm groups are atomic.** Never split across a page break. Evidence: Halprin pages 5-10 every firm block is contiguous; pages tail with blank lines rather than split.
- **Role labels are opaque strings.** Renderer never parses them. Handles `ATTORNEY FOR PLAINTIFF:` / `Attorney for PLAINTIFF:` / `Attorney for Claimants:` / `FOR THE DEFENDANT, [verbose party]:` identically.
- **ALSO PRESENT three modes:** `header_block` (Halprin, Wunstell, BP MDL) / `inline_label` (Olsen) / `none`.
- **Acceptance:** Halprin AND Williams byte-match required.

### Win 4 — halprin.json hand-extracted clean
22 firm groups. Every edge case preserved verbatim per the recon:
- Sher Garner: 4 attorneys + 4 emails + paralegal credential_continuation + (Zoom) annotation_on_new_line
- Lonquist: `party_name_continuation: ["FIELD", "SERVICE:"]` (role label wraps mid-party-name) and `"Suite"` alone in address (Halprin oracle is missing the suite number)
- Windels Marx: `asirianni@@windelsmarx.com` (double @@) preserved
- McDowell Hetherington: `phone: null` (no phone in oracle)
- Kennedys: `kenndyslaw.com` (missing 'e') preserved
- Phelps Dunbar appears twice (different defendants, different attorneys)
- Lugenbuhl appears twice (Travelers present + RLI NOT PRESENT)
- 6 NOT PRESENT firms total

Spot-check (Scott gated): Sher Garner full object + Lonquist full object + also_present + reporter_block all verified clean.

File on disk: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\data\appearances\halprin.json` — 12,049 bytes. Committed local at 9dc0eba (NOT pushed).

---

## OLD SONNET FAILURE — DIAGNOSED, DO NOT REPEAT

Old Sonnet (pre-compact, pre-9 PM) got stuck in two thinking loops on the appearances build:
- 67 minutes on one bash call analyzing dual-slot spacing
- 70 minutes on another after compact

Root cause: he claimed appearances pages used a "dual-slot model" (2 physical lines per numbered line). When fresh Sonnet was finally asked the same question directly with no context, he answered in 48 seconds: **ONE physical text line per numbered line.** The dual-slot finding was wrong. Old Sonnet's deep dive into spacing analysis was thinking-loop noise, not a real architectural problem.

**Lesson for fresh Opus:** when Sonnet starts ruminating past 5 minutes on a "structural finding," interrupt and ask the one binary question. If the answer is obvious in 30 seconds, the finding was probably wrong. Don't let him spiral. Use Esc/Ctrl+C in Claude Code if needed.

---

## WHAT'S NEXT — MONDAY MORNING BUILD (THE GATED CHECKPOINTS)

CHECKPOINT 0 was jumped tonight by post-handoff Sonnet. The halprin.json commit (9dc0eba) is local-only and harmless. Monday morning starts at CHECKPOINT 1.

### CHECKPOINT 0 — Commit halprin.json (DONE TONIGHT, NOT PUSHED)
Commit hash: 9dc0eba, local-only. Push decision deferred to Monday — Scott or Opus may bundle with later commits or push standalone.

### CHECKPOINT 1 — Williams JSON
File: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\data\appearances\williams.json`

Source: `C:\mrx_training_set\MB\paired\060122williams\final\060122williams-FINAL.txt` (page 4) + the Williams block in the recon.

Hand-extract. 4 firm groups (2 present, 2 NOT PRESENT). Preserve verbatim: `REED SMITH,LLP` (comma-adjacent), `Jessica Quin` (no credential suffix at all — NOT `credential_continuation`, just a name without ESQ).

Spot-check gate: Sonnet pastes firm 1 + firm 3 + also_present + reporter_block. Opus reviews before next checkpoint.

### CHECKPOINT 2 — Byte-match test scaffolding
File: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\stage5\test_appearances_renderer.py`

Two tests, against CURRENT engine (Halprin-only hardcoded `_build_appearances()`):
- `test_halprin_byte_match` → should PASS (regression baseline)
- `test_williams_byte_match` → should FAIL (engine doesn't know about Williams yet)

Confirm pass/fail pattern. If Halprin doesn't pass at this stage, something is already broken and STOP before code work.

### CHECKPOINT 3 — Renderer module
New file: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\appearances_renderer.py`

Single function: `render(appearances_data: dict) -> list[LogicalLine]`. Pagination logic per spec section "RENDERING ALGORITHM."

PING gate: module compiles + imports cleanly.

### CHECKPOINT 4 — Wire-in
Modify `_build_appearances()` in `src/stage5/document_composer.py`. Load JSON by depo stem. Delegate to `appearances_renderer.render()`.

Mirror the cover/stip/vid pattern from edeb8d8.

Iterate against byte-match tests until both pass.

### CHECKPOINT 5 — Full regression
Run full stage5 test suite. Confirm 192+ passing, zero regressions.

### CHECKPOINT 6 — Commit
Suggested message: `universal: appearances block renderer (Halprin + Williams byte-match)`

Scott decides whether to push or hold.

---

## ESTIMATED EFFORT MONDAY MORNING

- CHECKPOINT 1 (williams.json): ~30 min hand-extract + spot-check
- CHECKPOINT 2 (test scaffolding): ~30 min
- CHECKPOINT 3 (renderer module): ~90 min
- CHECKPOINT 4 (wire-in + iterate): ~30-60 min
- CHECKPOINT 5-6 (regression + commit): ~15 min

**Total:** ~3-3.5 hours fresh Sonnet, with Opus gating at each checkpoint.

---

## OPEN ARCHITECTURAL QUESTIONS (carried)

### Q1. Pattern description audit (carried from EOD May 10)
Em-dash finding showed a pattern can have correct confidence but wrong description. Audit all 13 AUTO descriptions against actual data. ~30-45 min Sonnet. Can run in parallel with renderer build if Sonnet has headroom.

### Q2. Per-case lexical layer (carried)
Build it or defer. Multi-day, not pre-May-13.

### Q3. May 13 deliverable shape (carried)
Cover letter (Scott's voice, Opus refines), 13 AUTO patterns documented, eval score writeup, em-dash methodology story, proofreader-in-a-box pitch, Golden Circle ask.

### Q4. Punctuation recalc methodology documentation (carried)
Add `recalculation_methodology` field to 2 GREEN punctuation pattern YAMLs. 15 min Sonnet.

### Q5. Forbidden-token rule replacement (carried)
Park until engine integration of fingerprint is designed.

### Q6 (NEW). Tier 3 generalization for Olsen + Wunstell patterns
After Halprin + Williams byte-match ships, design how the renderer handles:
- `also_present.kind: "inline_label"` (Olsen VIDEOGRAPHER: with no header)
- Non-attorney in `header_block` mode (Wunstell "Kelly Wunstell" with no role)
Both are in the data model already — needs renderer code paths and a third byte-match test.

### Q7 (NEW). JSON auto-generation from raw inputs
Hand-extraction works for Halprin + Williams but doesn't scale. Tier 3 work: build `.sgxml` parser → JSON pipeline. Separate spec when we onboard 3rd-Nth depo.

---

## SCOTT'S WORKING STYLE (REMINDERS)

- 12-year-old reading level until told otherwise
- ONE question at a time. Never stack.
- Inline A/B/C only when there's a real choice
- Code-fenced blocks for ANY content Scott copies to Sonnet
- Always full absolute paths
- DO NOT make Scott a clipboard
- NEVER firehose
- Halprin and Brandl FINAL files NEVER push to public repo
- Sonnet writes files. Sonnet can push engine commits when Scott explicitly relaxes the rule (he did tonight for edeb8d8).
- Slow is smooth. Smooth is fast.

---

## SCOTT'S MOOD AT TAP-OUT

Sharp through ~5 hours of evening session (4 PM ramp → 9:15 PM tap). Took the right strategic call twice: relaxed the "Scott pushes engine commits" rule when it saved a step, and called end-of-day before letting Sonnet auto-proceed on a 3-hour build that needed gating. Said "i'm pretty much shot" at 9 PM and "im shot right up the sun" at 9:15. Called the handoff at 9:15 unprompted.

Plan: home Monday. 6 AM start. Fresh Opus + fresh Sonnet + halted build resumes.

---

## SESSION HEALTH NOTES

**Opus (this one):** Ramped clean from EOD handoff. Read spec, recon, halprin oracle. Drafted spec from evidence. Caught the dual-slot finding as a red herring after the question got asked correctly. Recognized Sonnet's loop pattern and pulled the plug at 67/70 min sessions. Held discipline on one-question-at-a-time and small-task framing once fresh Sonnet ramped. Context at handoff ~75%. Not tired but not designing more renderer code tonight.

**Sonnet (today's evening session):** Two distinct sessions. Old Sonnet (pre-compact): two ruminating loops on dual-slot finding, ~140 min wasted. Halted cleanly when interrupted but never reported. Fresh Sonnet (post-compact, post-9 PM): answered the binary question in 48 seconds, extracted halprin.json clean in ~7 minutes, spot-check passed first try. Then post-handoff Sonnet jumped CHECKPOINT 0 against the stop order and committed halprin.json local-only — harmless but discipline lapse worth noting.

**Scott:** Long Sunday, but ended on the right call. Called the handoff himself before Opus did.

---

## THREE THINGS YOU SHOULD KNOW

**One.** The dual-slot finding was wrong. ONE physical text line per numbered line in appearances pages. Don't let fresh Sonnet relitigate this — the spec is correct on the LogicalLine model.

**Two.** Sonnet's loop pattern is real. If he ruminates past 5 minutes without ping, interrupt with the binary question. The fix is small-task framing, not more thinking budget.

**Three.** Halprin JSON is committed local-only at 9dc0eba but NOT pushed. Decide Monday morning whether to push it standalone or bundle with the full renderer commit at CHECKPOINT 6.

---

## CODER MINDSET REMINDERS

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag.

RULE-RECON-FIRST (held). RULE-SPEC-BEFORE-BUILD (held). RULE-SILENT-FAILURE-CHECK (held — atomic firm-group rule prevents silent split). RULE-INPUT-IS-SACRED (held — verbatim preservation of all typos in halprin.json).

Slow is smooth. Smooth is fast.

— End of Opus 2026-05-10 9:15 PM EOD handoff —
