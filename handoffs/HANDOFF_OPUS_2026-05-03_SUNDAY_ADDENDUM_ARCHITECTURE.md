# ARCHITECTURE INSIGHT — Saturday 2026-05-02 ~21:30 EDT
Captured for Sunday morning Opus
This conversation, late Saturday night, surfaced the next two architectural layers beyond Move A and aligner+differ. Capture is verbatim-faithful to the reasoning, not just the conclusions.

## 1. What $6.60 actually bought tonight (mechanics review)
60 API batches, ~60 turns each, structured prompt with NAMES_LOCK + rules + Stage 2 cleaned text. Each batch returned JSON proposals. ~$0.10/batch. Already batched at the sweet spot — bigger context drifts attention.
Cost shape is one-tenth of one cent per turn analyzed. Not a batching problem. That's just the cost of asking a serious model to carefully analyze 305 pages of testimony.

## 2. The Oracle question — Scott's first move
Proposal: Load whole depo (Stage 2 + Whisper + maybe prior FINALs) into model context. Treat as Oracle. Ask targeted questions: "Did witness work at W&T or W&T Offshore?" "What's the address?" "Who is Warren Seal?"
Three concrete advantages over current architecture:

- Cross-turn comprehension (no tunnel vision across 60-turn batches)
- Triangulation across sources (steno + Whisper compared in-context)
- Self-built NAMES_LOCK ("list every proper noun" replaces wallpaper)

Three concrete costs/risks:

- Full-context calls cost $1-3 each vs $0.10 — 10-20× more expensive per query
- Oracle returns prose, loses structured JSON discipline (proposals need turn IDs, locations, structured tags)
- Verification is harder — Oracle answers can't be checked the way structured fixes can

Verdict logged Saturday night: Oracle-first today, before aligner+differ exists, would mean asking the Oracle to invent rules instead of learn them. LLMs invent confidently. Prime Directive fabrication risk. Sequencing matters: aligner+differ provides the constraint data that lets the Oracle reason from measured truth.

## 3. The comprehension agent design — Scott's second move
The architectural pattern Scott described in his own words:

"We have an agent that transcribes Whisper. Then we have a comprehension agent. That is fed to a specific AI prompt that says, 'read this document like a scopist.' And after we go through all the chunks, instead of going to the AI with 60 chunks, we formulate a question to the AI that says — and summarizes what we found. I got a list of defects, and I knew the case."

That last sentence is the whole architecture: A scopist doesn't read each turn cold. A scopist knows the case. That knowledge is what enables 200 micro-decisions per page.
This is the standard production AI pattern: build understanding once, query it many times. Retrieval-Augmented Generation with a memory-resident comprehension layer. Scott arrived at it from first principles.

Two implementation paths:

**Way 1 — Case Brief (recommended):**

- Comprehension agent reads Whisper + steno + raw RTF once, expensively (~$3-5)
- Outputs a structured Case Brief (5-10KB JSON):
  - witness identity
  - employer history with dates
  - key people and roles
  - addresses
  - case-specific terminology
  - names and their valid forms (the auto-built NAMES_LOCK)
  - facts witness stated
- Every subsequent defect-finding call carries: brief + candidate (both small, ~$0.02-0.04/call)
- Total cost: comparable to today, possibly cheaper, much more accurate per call

**Way 2 — Resident Oracle:**

- Comprehension agent stays loaded with full depo in context
- Every defect candidate is a direct query
- More expensive per call, maximally informed
- Use as fallback for cases Way 1 can't resolve

Right answer: Way 1 default + selective Way 2 escalation for hard cases.

## 4. The Whisper unlock — the decision point
Scott's decision Saturday night:

"We're going to have to use some form of the audio. The previous engine gave me false hope and made it appear that we were closer than we were."

This is a strategic pivot. No more text-only ceiling games. No more pretending steno alone can hit 90%. Whisper is in scope, not parked.

Why this changes everything:
A comprehension agent reading only raw steno inherits steno errors and propagates them confidently. It might tell us the witness worked at "W and T offshore" — because that's what raw says. Garbage in, garbage out.
Whisper is the second source that lets the comprehension agent triangulate. Steno says X, Whisper says Y, both refer to the same entity, canonical form is Z. That triangulation is the moment the engine becomes what Scott has been describing.

Critical asset Scott flagged tonight: Halprin audio came in the package with the RTF/sgxml. It exists. We have it. It is not a future request. It is sitting on Scott's machine.

## 5. Updated sequencing — locked
The roadmap viewed clearly, in order:

**Stage A (next 1-2 weeks): Aligner+Differ**

- Read MB FINAL line-by-line against MB RAW
- Every diff is a labeled training example
- Habitual = MB style → MB_PROFILE
- Case-specific → per-depo calibration
- Replaces hand-coded NAMES_LOCK with learned NAMES_LOCK
- Two-depo minimum (Halprin + Brandl) for intersection
- This is the data foundation everything else stands on

**Stage B: Whisper integration**

- Wire Whisper for Halprin (audio in hand)
- Output: Whisper transcript aligned to turns
- Establishes second source for triangulation

**Stage C: Comprehension agent + Case Brief**

- Reads Whisper + steno + extracted MB style
- Produces Case Brief (structured JSON, ~5-10KB)
- One expensive call per depo at calibration time

**Stage D: Brief-aware defect-finder**

- Replaces current 60-batch cold defect-finder
- Each batch carries Case Brief + candidate turns
- Smarter, possibly cheaper, dramatically more accurate

**Stage E (downstream): Selective Resident Oracle fallback**

- For hard cases that the Brief-aware finder can't resolve
- Load full context, query directly
- Used surgically, not as default

## 6. Honest reframe — what tonight actually changed
The roadmap before tonight: steno engine first, audio maybe later.
The roadmap after tonight: audio is required. Steno alone cannot reach 90%.

This is not a setback. It is finally seeing the problem clearly. The previous engine's false hope was at 70.8% on Brandl with text-only — it implied steno alone could go further with effort. Five weeks of Move A-style work has revealed the real ceiling: pure steno engine without per-depo wallpaper is ~19%, and the hand-tuned wallpaper that gets it to 71.4% does not transfer to the next depo.

The aligner+differ + Whisper + comprehension agent stack is the architecture. Everything else is preamble.

## 7. What Sonnet should do with this Sunday morning
This file goes into mrx-context as handoffs/HANDOFF_OPUS_2026-05-03_SUNDAY_ADDENDUM_ARCHITECTURE.md. Sunday Opus reads it after the main handoff. The Aligner+Differ spec drafted Sunday morning should be written knowing it is Stage A of this stack — not a one-off tool. The output of the differ has to be a structure the Comprehension Agent can consume cleanly downstream. Design with that in mind.

Whisper integration moves from "parked Stage 4 future work" to "Stage B, scheduled, audio in hand." That changes Sunday's planning conversation.

## 8. Scott's mood at capture
Tired. Clear-eyed. Made the strategic call to commit to audio. Arrived at the comprehension agent architecture from first principles and verbalized it clean at midnight after 13 hours. Going to bed.

---

END CAPTURE
