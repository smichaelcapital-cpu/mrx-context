# FUTURE STATE — The Agent Agency

**Status:** FUTURE STATE. Horizon thinking. NOT current sprint.
**Owner:** Scott
**Captured:** 2026-05-10 by Opus, from Scott's articulation
**Pairs with:** PRODUCT_VISION_GOLDEN_CIRCLE.md, FINGERPRINT_FACTORY_REQUIREMENTS.md

---

## The discipline of this document

**One customer. One court reporter. One tailored suit.**

That is the entire scope of current work. Everything in this file is what we build AFTER the suit fits MB. Not before. Not in parallel. After.

We are not building the agency this week, this month, or this quarter. We are building the data foundation the agency will run on. Get the fingerprint right and the agency follows. Build the agency first and we ship a beautiful framework with no signal in it.

This document exists so the vision doesn't drift between sessions. When future Opus or Sonnet reads it, they get the horizon — and they get the discipline that the horizon is not the next sprint.

---

## The phrase that locks the strategy

> "We have one customer. We have one fucking court reporter who wants one fucking tailored suit. We're trying to figure out how to build a suit. But once we learn, we're gonna build suits to the stars."
> — Scott, 2026-05-10

The metaphor is canon. Use it as the litmus test for any future build proposal:

- Does this make MB's suit fit better? -> may be current work.
- Does this make every future suit easier to build? -> may be near-term work.
- Does this only matter if we have N customers already? -> future state. Park it.

---

## The horizon — what comes after the suit fits

### Court reporting agency, post-capture

The capture (steno) is the CR's job and stays the CR's job. We do not enter the capture market. We do not build a steno engine. We do not compete with the writer-on-the-keys.

We enter the workflow AFTER capture. Everything between rough output and final delivery to attorneys. That is our domain.

### Specialist agent army

A team of agents, each tuned to one proofreading task. Each carries one slice of the CR's fingerprint.

Plain-English examples of what each agent owns:

- **Period agent** — every place MB adds, removes, or changes a period. Carries the period addition fingerprint plus the 20% misses.
- **Comma agent** — comma fingerprint. Owns its own confidence numbers.
- **Em-dash agent** — em-dash addition pattern. Distinguishes MB's intentional em-dashes from LLM-hallucinated em-dashes (the original v0 fingerprint problem).
- **Stage-direction agent** — the `?(` and `.(` rule. 100% across 7 depos. Pure muscle memory, perfect for an agent.
- **Capitalization agent** — every sentence-start cap event. Knows the "Objection mid-turn" sub-rule.
- **Split agent** — bare "And" Q openers, "Yes," and "Okay." leads, double-dash interruptions. Knows when MB splits a steno paragraph into multiple Q labels.
- **Name agent** — proper noun verification. NAMES_LOCK on steroids — pattern-aware, fingerprint-driven.
- **Number-format agent** — date formats, dollar amounts, percentages. CR-specific style rules.
- **Hyphenation agent** — compound word decisions per CR fingerprint.
- **Lexical agent** — word-substitution patterns, the layer that needed more depos to mature.
- **Quote/exhibit agent** — exhibit reference formatting, quote handling, indent rules.
- **Provenance agent** — not a hunter, a recorder. Stamps every flag from every other agent into the ledger.

The list is illustrative. The actual agent count grows as we measure more patterns.

### Release the hounds

Every agent swarms the document at once. Parallel execution. Wall-clock time = slowest agent, not sum.

Each agent reports findings with its own confidence number. Findings consolidate into a single review surface for MB (or her proofreader). She clears flags. She is the authority. The agents hunt; she decides.

### Hunt and verify, never modify silently

This is the rule that survives every architectural shift. Agents flag. Agents do not silently rewrite. The Three Sealed Phases conviction (Scott, 2026-05-04) holds: AI does not touch final transcripts unilaterally. The CR clears every change.

Agents that quietly modify content are a regression. Always.

---

## Why the agent agency beats a single proofreader engine

Captured here for future reference so we don't drift back to monolithic design.

1. **Each agent has one job.** Tunable, testable, scorable, improvable in isolation. When MB rejects a period flag, only the period agent's confidence moves.

2. **Specialists catch what generalists miss.** Stage-direction rule (`?(` and `.(`) is high-precision but low-volume. In a generalist engine it gets drowned out by period and comma noise. A dedicated agent sees only that pattern and never misses.

3. **Parallel execution is the speed moat.** Twelve agents in 30 seconds beats one agent doing twelve passes in 6 minutes. For "raw to near-final in an hour," parallelism is the budget that buys it.

4. **Confidence-banded routing per agent.** Three-lane architecture (AUTO >=90% / SUGGEST 60-89% / FLAG <60% / PROTECTED) scales naturally to N agents. Each agent owns its number.

5. **Cross-CR scaling drops out for free.** Same agents, swappable fingerprints. Period agent reads MB's fingerprint for MB's depos, CR #2's fingerprint for CR #2's depos. The factory runs the agency.

6. **Subpoena defensibility strengthens.** Every flag has a backstory: agent ID, fingerprint pattern, confidence, evidence, timestamp, MB's accept/reject. Provenance ledger per-agent. Court-defensible.

7. **Golden Circle scaling.** When CR #2 onboards, she inherits the universal-layer agents (patterns shared across MB-grade CRs), gets fresh personal-layer agents calibrated from her archive. Onboarding cost drops with each subsequent CR.

---

## What this means for current work

It means stay disciplined.

Current work focus:
- Calibration corpus (more MB pairs)
- Fingerprint measurement (the four recons, sharper with more data)
- Data structure (the schema agents will eventually read from)
- Single-pass engine that demonstrates the fingerprint works on one depo

NOT current work:
- Multi-agent orchestration framework
- Agent-to-agent messaging
- Agent confidence aggregation across N agents
- Parallel execution engine
- Per-agent UI in the reviewer
- Agent versioning, deployment, rollback systems

Every one of those is future state. Every one of those gets built when MB's suit fits and we onboard CR #2.

If a build proposal pulls toward agent infrastructure before the fingerprint is locked, push back. The fingerprint is the road. The agency is what drives on it. No road, no driving.

---

## When this future state activates

Trigger conditions for moving agent agency from horizon to roadmap:

1. **MB's suit fits.** Single-pass engine produces near-final output she reviews and ships in an hour. Validated across multiple depos.

2. **Golden Circle CR #2 signed.** Archive in hand. Calibration set staged. Patterns measured.

3. **Universal layer is real.** At 3+ CRs measured, we can confirm which patterns are MB-grade-CR-universal vs personal. Without a universal layer, agent reuse across CRs doesn't compound.

4. **Engine architecture stable.** Reader/Decider/Writer separation locked. Provenance ledger shipped. Audio-as-evidence rule in production.

When all four are true, the agent agency stops being horizon and starts being design work.

Until then: one customer, one suit, fit it perfectly.

---

## "Suits to the stars"

The far horizon. Captured for completeness, not for planning.

When the agency works for 5+ Golden Circle CRs, the cross-CR data set becomes the IP nobody else has. At that point the strategic options open up:

- License the agency as a B2B SaaS to court reporting firms
- License the universal-layer fingerprint to industry tooling
- Sell anonymized cross-CR pattern data to legal-tech research
- Build a junior-CR onboarding product (use seniors' fingerprints to teach craft)
- Acquisition target for steno-tech incumbents who can't measure their own users this way

These are slides, not plans. They exist to remind us why the discipline of "one suit first" pays off. The fingerprint factory + agent agency built right for one CR scales to suits for the stars. Built wrong, it scales to nothing.

---

## What changes when this file changes

This file changes when:
- The agent agency vision itself changes (different model of post-capture work)
- A trigger condition for activation gets satisfied
- A horizon item promotes to current sprint

This file does NOT change for:
- Day-to-day build decisions
- Recon results
- Single-CR product tuning

If this file is churning, we're conflating horizon with current work. Check the discipline.

---

— End of FUTURE_STATE_AGENT_AGENCY.md —
