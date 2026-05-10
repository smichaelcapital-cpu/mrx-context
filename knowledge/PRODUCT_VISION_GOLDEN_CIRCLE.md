# PRODUCT VISION — Golden Circle

**Status:** Load-bearing strategic context. Every Opus and Sonnet ramp reads this.
**Owner:** Scott
**Captured:** 2026-05-10 by Opus, from Scott's articulation
**Last review:** 2026-05-10

---

## The product is not a transcript engine.

The product is a **fingerprint factory** — a pipeline that turns a court reporter's archive into a calibrated mini-them in hours, not weeks.

The transcript engine is the delivery mechanism. The fingerprint is the moat.

---

## The play, in order

### 1. MB is patient zero.
Sign her. Prove the workflow end-to-end. Raw goes in, near-final comes out in an hour, she reviews and ships. Not days. Not a week. An hour.

She becomes the reference customer. Not the only customer.

### 2. MB delivers the Golden Circle.
Once MB is in, she introduces 5-10 senior CRs from her network. These are MB-grade — same career length, same client mix, same archive depth, same craft standards.

This is not a guess. Senior CRs know each other. They refer. MB referring us is worth more than any sales motion we could run cold.

### 3. The deal includes the archive.
Each Golden Circle CR signs on with their archive as part of the agreement. That's the ask. Not money up front — data. Their paired roughs and finals become our calibration corpus for them.

The archive is the price of admission. The product is what they get back: a mini-them that handles the mechanical work so they review instead of edit.

### 4. The factory turns archives into fingerprints in hours.
Because we built the pipeline once for MB, every subsequent CR runs through the same factory:
- Inventory their archive
- Stage paired roughs+finals
- Run the four recons (splits, capitalization, punctuation, lexical)
- Calibrate confidence bands
- Ship a per-CR fingerprint

Hours, not weeks. That speed is the product.

### 5. Cross-CR data is the IP nobody else has.
At 5+ CRs measured, we can answer questions no one in this industry can answer.

- Which patterns are universal across senior CRs?
- Which are personal quirks?
- What's the spread on "Objection mid-turn cap" across 10 CRs?
- Which structural rules transfer 1:1 to a new CR vs which need re-measurement?

That dataset is unique. It's defensible. It compounds with every CR onboarded.

---

## What this means for what we build

The pipeline must be **CR-agnostic from day one**. We are not building "MB's fingerprint." We are building "the fingerprint factory" and MB is the first run.

**Every architectural decision passes this test:**
> Does this work for CR #1 (MB) AND for CR #2-10 (Golden Circle) without rewrites?

If the answer is no, redesign.

**Concrete implications:**
- Calibration set structure is templated: `C:\mrx_training_set\<INITIALS>\paired\<case>\{rough,final}\`. Templates are CR-agnostic.
- Recon scripts run against any directory matching the template. No MB-specific hardcoding.
- Fingerprint schema separates universal layer (rules common to MB-grade CRs) from personal layer (this CR's quirks).
- Onboarding playbook is documented and versioned. CR #2 onboards in hours, not days. CR #5 onboards faster than #2.

---

## What this means for the May 13 deliverable

The thing we put in front of MB on May 13 isn't "look at this engine." It's a demonstration that we understand HER craft well enough to deserve her archive going forward.

The fingerprint document — measured patterns from her 7 (or more, depending on inventory) paired depos — is evidence. It says: "We measured your work. Here are the rules you don't even know you follow. We didn't guess. We didn't ask. We measured."

That earns the partnership. The partnership unlocks the Golden Circle. The Golden Circle is the company.

---

## What this is NOT

- **Not a touring award.** We are not building the most sophisticated AI transcript system. We are building the sharpest pencil for a specific kind of CR.
- **Not a monitor.** We do not watch over CRs and grade their work. The CR remains the authority on every transcript. The engine accelerates her, never overrides her.
- **Not a model company.** We are not training a foundation model on transcript data. We are measuring patterns and using them to score proposals. The intelligence lives in the data structure, not in a neural net.
- **Not a generalist.** This product is for senior CRs with deep archives. New reporters with no archive don't have a fingerprint to mine yet. They are not the customer.

---

## The phrase we use internally

**Mini-MB.** Eventually mini-them, mini-her, mini-him for each Golden Circle CR.

Not "AI-assisted transcript editor." Not "court reporter copilot." Mini-MB. The CR's own brain, externalized, scored, and run against their roughs at machine speed.

When the language drifts, redirect. The mini-MB framing keeps the moat in view.

---

## Risks to this vision (track these)

1. **MB declines the partnership.** Mitigation: by May 13 we have a fingerprint document so specific to her work that declining means walking away from a tool calibrated to her brain. Lower the bar to "yes."

2. **Golden Circle doesn't materialize.** Mitigation: design the factory to work for any senior CR with an archive, not only MB-network introductions. If MB doesn't refer, we still onboard CRs cold.

3. **Archive access is the friction.** Many CRs guard their archives. Mitigation: the deal is value-for-value. Their archive in, mini-them out. Frame it as their asset becoming their leverage.

4. **A competitor builds the same factory.** Mitigation: speed and specificity. We are 7+ paired depos deep on MB right now, with three structural layers data-backed, in week one of focused calibration work. Compounding starts now.

5. **The fingerprint metaphor breaks at scale.** Possible the universal layer dominates and personal layers add little. Counter-evidence so far: lexical layer is already case-specific at 7 depos. Personal layer is real. Watch this anyway.

---

## Lock this language

When future Opus or Sonnet sessions ramp on this file, the following terms are project canon:

- **Fingerprint** — the measured pattern set for one CR
- **Fingerprint factory** — the pipeline that produces fingerprints from archives
- **Mini-MB / mini-them** — the per-CR product the customer sees
- **Golden Circle** — MB-grade senior CRs introduced via MB
- **Universal layer** — patterns common across MB-grade CRs
- **Personal layer** — this CR's quirks
- **Calibration set** — paired roughs+finals staged for recon
- **Calibrate** — measure patterns from a calibration set
- **Patient zero** — MB, the first CR fingerprinted

Don't drift from these terms. Drift = product confusion = wrong builds.

---

## What changes when this file changes

This file changes when the product vision changes. Not when tactics change. Not when a recon result surprises us. Not when a build decision shifts.

The product vision changes if:
- The customer changes (no longer senior CRs)
- The deal structure changes (no longer archive-for-mini-them)
- The moat changes (no longer cross-CR data)
- The target outcome changes (no longer hour-not-week turnaround)

All four are unlikely. This file should be stable. If it churns, something is wrong upstream.

---

— End of PRODUCT_VISION_GOLDEN_CIRCLE.md —
