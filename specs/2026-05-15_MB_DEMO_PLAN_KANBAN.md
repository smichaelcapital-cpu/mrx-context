# MB Demo Plan — Kanban Board v1
**Date:** 2026-05-14 EOD (for Friday 2026-05-15 morning grind)
**Frame:** One customer. MB. When she says "holy shit, I'd use this," we win — she drops dime on 10 peers and we're set.

---

## North Star

**The demo moment:** One full deposition MB did not touch. Cleaned by MRX. Delivered to her 24 hours after she submits the RAW. She opens it. Less than 1 hour of cleanup needed. Looks like her style. Sounds like her voice.

That's the win condition. Everything below serves that.

---

## Operating Principle

**We are not building for the market. We are building for MB.**

- Stage A does not need to work on 14 reporters. It needs to work on MB.
- The Comprehension Agent does not need to be perfect on every case. It needs to be perfect on MB's cases.
- The architecture stays universal-ready (code stays generic, data stays per-CR) so CR #2 onboards fast WHEN MB makes the call.
- The bar for v0 ship is MB's bar, not the auditor's bar.

---

## Lane Structure — Two Parallel Tracks

We have two builders (Sonnet #1, Sonnet #2). Two lanes maximizes throughput without collision.

**Lane A — Pipeline (Sonnet #1):** code changes to the engine. Differ, fingerprint shape, MB.yaml, Comprehension Agent, 3-agent flow.

**Lane B — Data + Validation (Sonnet #2):** CATalyst exports, pair expansion, audio recon, Whisper measurement, validation runs.

Lanes do not touch the same files. No collision risk.

---

## Kanban Tiles

### COLUMN 1 — READY (Friday morning, both lanes can pick up)

**Tile A1 — Differ v0.2 spec**
- Lane: A (Sonnet #1)
- Owner spec: Opus
- Owner build: Sonnet #1
- Fix word_substitution alignment garbage (139,912 noise events on 9-pair run)
- Fix proper_noun_change categorizer (Q/A mislabeled as proper noun)
- Bounded matching OR exclusion of word_substitution category
- Q/A speaker label bucket BEFORE proper_noun classification
- Acceptance: 9-pair rerun shows <5% noise in category breakdown
- Estimated: half-day

**Tile A2 — MB.yaml v0.1 shape spec**
- Lane: A (Sonnet #1)
- Owner spec: Opus
- Owner build: Sonnet #1
- New shape: category+context, NOT token-pair (per tonight's architectural finding)
- Sections: category zones, per-zone rate per 1000 tokens, per-zone consistency across depos, top 3 contextual triggers per zone
- First entry: em_dash_inserted (1,151 events, 100% across 9 depos, all '--' form)
- Acceptance: MB.yaml v0.1 file lives at reporters/MB.yaml with em_dash entry validated
- Estimated: half-day

**Tile B1 — AUDIO_SYNC_RECON run**
- Lane: B (Sonnet #2)
- Owner spec: Opus (port from existing recon design)
- Owner run: Sonnet #2
- 5-question recon against Halprin .sgxml + RTF + audio
- Goal: decide whether per-stroke audio sync is usable OR commit to whole-file Whisper
- Parked 3 weeks. No more excuses.
- Estimated: half-day

**Tile B2 — Round 2 CATalyst exports (5 new pairs)**
- Lane: B (Sonnet #2)
- Owner: Scott (CATalyst manual) + Sonnet #2 (file moves)
- Rooks_011121 (ROUGH + FINAL exports)
- Nguyen_033022 (ROUGH + FINAL exports)
- Thompson, Washington, Black (ROUGH exports — FINAL .txt already on disk)
- mv into mrx_depo_library structure
- Update pairs.json to 14 entries
- Acceptance: pairs.json has 14 entries, all in mrx_depo_library
- Estimated: full day (CATalyst friction)

---

### COLUMN 2 — QUEUED (after Friday)

**Tile A3 — Stage A 14-pair rerun**
- Depends on: A1 (differ v0.2) + B2 (round 2 exports)
- Lane: A (Sonnet #1)
- Validate em_dash signal holds at 14 pairs
- Hunt for patterns in 70-99% pct_of_depos band (was empty at 9, may emerge at 14)
- Acceptance: knowledge capture written, signal report delivered
- Estimated: half-day

**Tile B3 — Whisper run on Halprin audio**
- Depends on: B1 (AUDIO_SYNC_RECON decision)
- Lane: B (Sonnet #2)
- Whole-file Whisper transcription of Halprin .opus audio
- Measure disagreement rate vs steno transcript
- Cost target: ~$2-3
- Acceptance: Whisper transcript + word timestamps + disagreement report
- Estimated: half-day

**Tile A4 — Brief validator design**
- Lane: A (Opus spec)
- VC Auditor HOLE 3 fix
- Second cheaper call validates Brief claims against source documents before lock
- OR human-in-the-loop checkpoint (Scott eyeballs Brief before downstream consumes)
- Acceptance: spec written, validator architecture locked
- Estimated: half-day spec, build later
- Blocking: Stage C build cannot start without this

**Tile A5 — Adversarial test harness for 3-agent wall**
- Lane: A (Opus spec)
- VC Auditor HOLE 4 fix
- Test cases: bad input to Reader, prove Arbiter doesn't propagate, prove Writer can't reinterpret
- Acceptance: test suite scaffolded, first 5 adversarial cases pass
- Estimated: half-day spec, half-day build
- Blocking: Stage C v0.2 cannot ship without this

---

### COLUMN 3 — STAGE C BUILD (week 2)

**Tile A6 — Stage C: Comprehension Agent**
- Depends on: A1, A2, A3, A4, B1, B3
- Lane: A (Sonnet #1 build, Opus spec)
- ONE Opus call per depo. Inputs: steno + Whisper + MB fingerprint. Output: Case Brief JSON (5-10KB)
- Brief validator runs immediately after (per A4)
- Acceptance: Case Brief written for Halprin, validator approves, manual review confirms claims correct
- Estimated: 2 days spec + build + test

**Tile A7 — Stage D: Brief-aware defect-finder**
- Depends on: A6 (Brief exists)
- Lane: A (Sonnet #1)
- Replaces current 60-batch blind defect-finder
- Each batch carries Case Brief as context
- Reader/Arbiter/Writer 3-agent split (walled per A5 harness)
- Acceptance: Halprin defect-finder run with Brief, output measured against MB FINAL
- Estimated: 3 days spec + build + test

**Tile A8 — End-to-end Halprin clean run**
- Depends on: A7
- Lane: A (Sonnet #1 + Scott review)
- Full pipeline: RAW → Stage A fingerprint → Whisper → Brief → Stage D defect-finder → Writer → FINAL
- Measure new ceiling vs old 71%
- Acceptance: measured accuracy number, list of remaining defects categorized
- Estimated: 1 day run + analysis

---

### COLUMN 4 — DEMO PREP (week 3)

**Tile A9 — Cleanup pass on Halprin output**
- Depends on: A8 (we have a number)
- Lane: A (Opus spec, Sonnet #1 build)
- Fix the top 5 categories of remaining defects
- Re-run, re-measure
- Acceptance: cleanup time on the output is <1 hour for Scott (proxy for MB)
- Estimated: 2-3 days

**Tile A10 — MB demo package**
- Depends on: A9 (output is demo-able)
- Lane: A (Opus + Scott)
- One depo MB has not seen (NOT Halprin — she's seen Halprin)
- Run full pipeline
- Side-by-side: MB's RAW → MRX OUTPUT
- Cover letter: "Here is one of your depos. Cleaned by MRX. Tell me what you think."
- Acceptance: package ready to send
- Estimated: half-day

**Tile A11 — Send to MB**
- Depends on: A10
- Owner: Scott
- Timing: Scott's call (when she's back from grandmother time)
- Acceptance: MB has the package
- This is the demo moment

---

### COLUMN 5 — POST-MB (months 2-3, only if MB says yes)

**Tile A12 — CR #2 onboarding playbook**
- VC Auditor HOLE 9 fix
- Step-by-step how to onboard another reporter without Scott in the loop
- Decision criteria documentation (when does judgment kick in, when does auto-apply)
- Estimated: 1 week

**Tile A13 — Stage A run on AD data**
- VC Auditor HOLE 5 fix
- Already have AD data
- Prove fingerprint transfers OR learn what's wrong
- Estimated: 2-3 days

**Tile A14 — Whisper disagreement rate measurement**
- VC Auditor HOLE 6 fix
- Beyond Halprin — measure across all 14 pairs
- Estimated: 2 days

---

## Critical Path

A1 → A2 → A3 → A6 → A7 → A8 → A9 → A10 → A11

That's the chain. Everything else is parallel support.

**Estimated critical path:** 10-14 days of focused work to A11 (MB demo sent).

---

## Friday 2026-05-15 Targets

**Lane A — Sonnet #1:**
- Read this plan
- Read tonight's handoffs
- Wait for Opus spec on A1 (differ v0.2)
- Build A1
- Stretch: start A2 (MB.yaml v0.1 shape)

**Lane B — Sonnet #2:**
- B1 (AUDIO_SYNC_RECON) in the morning
- B2 (Round 2 exports) Scott + Sonnet #2 in the afternoon

**Scott:**
- Up at 7 AM
- Fresh Opus ramps on this plan
- Opus writes A1 + A2 specs by 9 AM
- Hands to Sonnets, sits and watches
- CATalyst export work alongside

---

## What This Plan Does NOT Cover

- Business case / pricing / VC pitch (parked)
- Front-end UI / customer-facing tools (parked until MB says yes)
- CR #3+ onboarding (parked until CR #2 works)
- Audit Holes 8 + 10 (business-side, parked)

---

## Operating Principle Reminder

> "I don't want to hear good news until it's good news. Until then we grind, we disrupt, we stay paranoid. We assume we suck until we don't."

Iron trap stays shut until A8 produces a real number. Until then, no celebrations, no premature ship-its, no telling MB anything.

— End of MB Demo Plan v1 —
