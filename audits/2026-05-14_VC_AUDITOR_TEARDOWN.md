# VC Auditor Teardown — 2026-05-14

**Frame:** Opus playing a code auditor sent by a VC firm looking to talk their partners OUT of buying MRX. Looking for holes and logical gaps. Captured verbatim because the criticism is sharper than the architect's own self-review.

---

## HOLE 1 — You don't actually have an engine. You have a pile of fixes.

5+ weeks on Halprin. Text-only ceiling is 71% on that single depo, achieved with hand-tuned "wallpaper" that explicitly does not transfer to the next depo. 11 pairs of training data. Eleven. To detect MB's habits. To then generalize to other reporters. The honest number for "data foundation everything else stands on" is statistically a coin flip.

## HOLE 2 — Stage A measures noise, not skill.

First frequency table is dominated by whitespace and line-breaks. Actual habit signals (em-dash, capitalization, filler removal) rank below position 20. Calling this a fingerprint reads like a token-stream artifact of the RAW→FINAL structural transform. No out-of-sample test.

## HOLE 3 — The Comprehension Agent is one expensive call away from being a hallucination machine.

About to pay Opus ~$8 to read 200K tokens of steno + Whisper + fingerprint and write a 10KB Case Brief. That Brief becomes the source of truth for 60 downstream batches. If the Brief is wrong on a witness name, firm name, or key term — every downstream batch silently propagates the error. No verification step on the Brief. No QA layer. MB is the customer, not the auditor.

## HOLE 4 — Three-agent separation is a slogan, not an architecture.

Reader / Arbiter / Writer sounds clean. But:
- The Arbiter is a single point of failure. One bad decision rule poisons the whole transcript.
- "Three agents that don't talk" still share one prompt designer. If the spec is wrong, all three are wrong consistently.
- No test harness that proves the wall holds under adversarial inputs.

## HOLE 5 — You can't ship without MB, and MB is one person.

Entire validation strategy depends on a single court reporter. She gets sick, retires, changes her mind about em-dashes — fingerprint is stale. CR #2 onboarding has been queued since April and hasn't started. Building a product for a market of one.

## HOLE 6 — Whisper is not the safety net you think it is.

Whisper hallucinates on cross-talk, mumbling, accents, and legal jargon. Depositions have all four. Using Whisper as the second source to triangulate steno errors. What happens when Whisper IS the error? No third source. "Triangulation" reduces to "two-out-of-two, hope they're both right."

## HOLE 7 — The audio sync recon has been parked for three weeks.

Designing Stage B-E assuming Whisper whole-file works. Fine. But AUDIO_SYNC_RECON never ran. Don't know if .sgxml has usable per-stroke timestamps. If it does, architecture is wrong (slice on demand). If it doesn't, committed to ~$2-3 per depo forever. Either way, committed before measuring.

## HOLE 8 — There is no business model in this conversation.

11 handoff files. Engineering decisions, frequency tables, Opus mood. NOT visible: target ACV, CAC, churn assumption, pricing tier, court reporter market sizing, or a single signed pilot. 5+ weeks deep on a v0 engine. Where is the LOI from a court reporting agency?

## HOLE 9 — Founder is the bottleneck.

Scott reviews every spec, eyeballs every frequency table, decides every architectural call. System assumes Scott is available. He's working a day job. He's exhausted. He's frustrated. If he gets hit by a bus or loses interest in month 4, this codebase is unmaintainable by anyone else because institutional knowledge lives in his head and in 200 handoff files.

## HOLE 10 — Your moat is a frequency table.

Once shipped and proven, what stops a well-funded competitor (or Veritext, or a Big Law transcription vendor) from running the same Aligner+Differ on 1,000 court reporters in 90 days? Moat is the data, but data isn't yours — it's MB's, and the next CR's. Thin layer of orchestration on top of Whisper, Opus, and Sonnet. All three are commodity APIs.

---

## Auditor's recommendation to VC partners

Pass at this round. Revisit if Scott can show:
(a) generalized fingerprint working across 3 distinct court reporters end-to-end
(b) 90%+ accuracy on an out-of-sample depo neither he nor MB has seen
(c) one paying pilot customer
(d) a co-founder who can keep the lights on if Scott is unavailable

---

*Captured 2026-05-14 evening. Architect response to each hole tracked separately.*
