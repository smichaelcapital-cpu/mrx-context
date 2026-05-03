# Three Sealed Phases — Architectural North Star
**Locked:** 2026-05-03 evening session
**Owner:** Scott
**Status:** Future architecture, not tonight's work

## The principle
AI must NEVER touch the final transcript at write time. The system must
have three sealed phases with a hard boundary between them.

| Phase | Role | AI? |
|-------|------|-----|
| 1. Reader | Proposes what the right text is, given steno + audio + context | YES |
| 2. Validator | Confirms via independent agent + audio cross-check | YES |
| 3. Composer | Writes the locked decisions to the page, mechanically | NO |

## Why
Legal defensibility. Under subpoena, Scott needs an auditable trail:
"this word is on the page because Reader proposed X, Validator confirmed
X with audio match Y, Composer mechanically wrote X." Three checkpoints,
zero AI freedom at the moment of writing. A wrong word reaching paper
is a defensible failure (two agents agreed) — not a magical hallucination.

## Current state vs. future state
Today, Stage 3 contains an AI agent currently called "Writer" that
generates REWORD proposals. This is misnamed — it's a Proposer, not a
Writer. The deterministic apply layer rubber-stamps the AI's text choices.

In the target architecture: rename "Writer" to "Proposer" or "Reader";
add explicit Validator with audio cross-check; the Composer becomes a
dumb deterministic emitter that only knows how to write decisions to
the page, no model, no prompt.

## Priority
Top-tier retrofit alongside Aligner+Differ. Do not lose sight. Harder
to retrofit the further the system grows.

## Do not
- Redesign tonight
- Rename code tonight
- Block any current shipping on this

## Do
- Reference this when naming new components
- Flag any new feature that adds AI to the write phase
- Surface this in MyReporterX customer messaging when ready
  ("AI never writes your transcript — three sealed phases")
