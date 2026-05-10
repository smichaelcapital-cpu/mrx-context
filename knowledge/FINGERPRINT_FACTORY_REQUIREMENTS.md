# FINGERPRINT FACTORY REQUIREMENTS

**Status:** Load-bearing technical context. Pairs with PRODUCT_VISION_GOLDEN_CIRCLE.md.
**Owner:** Scott
**Captured:** 2026-05-10 by Opus
**Last review:** 2026-05-10

---

## The frame

Read PRODUCT_VISION_GOLDEN_CIRCLE.md first. This file is the technical implication of that vision.

**Short version:** the pipeline must turn a court reporter's archive into a calibrated mini-them in hours. Not weeks. Not "MB's fingerprint" — the factory that runs on any CR's archive and outputs a calibrated mini-them.

Every architectural decision must pass this test:

> Does this work for CR #1 (MB) AND for CR #2-10 (Golden Circle) without rewrites?

If the answer is no, redesign.

---

## Hard requirements

### R1. CR-agnostic from day one
No MB-specific hardcoding anywhere in the pipeline.

- Calibration set path template: `C:\mrx_training_set\<INITIALS>\paired\<case>\{rough,final}\`
- Recon scripts accept `<INITIALS>` as a parameter
- Fingerprint output filenames use `<INITIALS>` as a prefix
- Deny-lists for confidentiality grep are per-CR, loaded from each CR's MANIFEST.md

If any module references "MB", "halprin", "brandl", or any MB-specific identifier, that's a bug in the factory. Move it to a config file scoped to CR initials.

### R2. Universal vs personal layer separation
The fingerprint schema must distinguish two layers from the first byte:

- **Universal layer** — patterns common across MB-grade CRs (discovered at scale once we have 3+ CRs)
- **Personal layer** — this CR's quirks (calibrated from this CR's archive)

Each pattern in the schema carries a `layer: universal | personal | unknown` tag. Until we have CR #2, every pattern is `unknown`. After CR #2, patterns that match across both get auto-tagged `universal`. After CR #5, the universal layer should be largely stable.

When CR #11 onboards, the universal layer is shipped pre-loaded. Only the personal layer needs calibration. That's how onboarding cost drops.

### R3. Archive inventory is templated and re-runnable
Inventory is a script, not a manual process. It scans a CR root directory and outputs:

- Total folders found
- Folders matching paired-case heuristics (rough+final filename patterns)
- Folders matching system or non-case patterns (skip list)
- Confidence score per candidate pair

The inventory script ran manually for MB. Going forward it must be re-runnable on any path with one flag.

### R4. Recon scripts re-run cleanly on any calibration set
The four recons (splits, capitalization, punctuation, lexical) accept a calibration set path and produce reports.

No hardcoded depo case IDs. No hardcoded path components. Path-in, report-out.

Reports are versioned by CR and by date. `C:\mrx_training_set\<INITIALS>\reports\<YYYY-MM-DD>_<recon_name>.md`.

### R5. Confidence bands are per-CR, calibrated from data
The three-lane architecture (AUTO >=90% / SUGGEST 60-89% / FLAG <60% / PROTECTED) is universal. The thresholds are universal.

But the per-pattern confidence numbers are calibrated from each CR's archive. MB's "Objection mid-turn cap" might fire 87% of the time. CR #2's might fire 64%. Same architecture, different number, different lane.

The fingerprint storage format must allow per-pattern, per-CR confidence values that update as more pairs are added.

### R6. Pattern auto-promotion and demotion
As MB (or any CR) accepts and rejects engine proposals, confidence numbers move.

- Rule fires correctly -> confidence creeps up
- Rule fires and gets rejected -> confidence drops
- Confidence crosses >=90% threshold -> promotes from SUGGEST to AUTO
- Confidence drops below 60% -> demotes to FLAG

This is Stage 6 territory (post-ship feedback loop). Schema must support it from day one even if we don't build the loop until later.

### R7. The 20% is preserved, never summarized away
For every measured pattern, the schema stores:

- The pattern definition
- The matching events (the 80% that follow the rule)
- **The non-matching events (the 20% that don't)** — full context, full snippet
- Per-event metadata: case ID, line number, context

The 20% is the gold. It's the conscious editorial choice the CR can articulate when she sees the data. We never throw it away.

Storage cost is low. Long tail value is high. Keep it.

### R8. Confidentiality boundary is built into the pipeline
- Anything in `C:\mrx_training_set\` is local-only. Hard rule.
- Recon reports come in two flavors: full (local-only, may quote depo text) and sanitized (metrics only, public-pushable).
- Sanitization is automated: grep for witness names from MANIFEST.md before any public push.
- If grep finds a name, the public push is blocked and flagged to Scott.

The boundary is enforced by the pipeline, not by human discipline alone. Human discipline fails at scale.

### R9. Onboarding playbook is documented and versioned
Step-by-step procedure for onboarding a new CR. Captures:

- How to inventory their archive
- How to identify paired roughs+finals
- How to handle filename conventions that differ from MB's
- How to extract from .sgngl binaries (and ASCII alternatives if .sgngl extraction fails)
- How to handle missing pairs (rough without final, final without rough)
- How to set initial confidence thresholds before the first 7 pairs
- Gotchas from MB onboarding

The first pass of this playbook is written FROM MB's onboarding. Every subsequent CR onboarding adds to it. By CR #5, the playbook is mature.

### R10. Reporter pattern hypotheses ledger
A separate ledger tracks abstract hypotheses across all measured CRs.

Example: "Senior CRs cap 'Objection' mid-turn." Hypothesis. Evidence: MB does it 87% of the time. CR #2 does it 64%. CR #3 doesn't do it at all.

After 5 CRs, hypotheses earn a verdict: confirmed universal / personal-variable / disconfirmed.

This ledger is the cross-CR IP. It's the answer to "what do we know about senior CRs that nobody else knows?"

---

## Architectural separations to preserve

These come from engine v1's old architecture (per Scott's recall, validated 2026-05-09). They survived for a reason. Keep them.

### Reader / Decider / Writer separation
- **Reader** — surface anomalies and candidate corrections from the rough
- **Decider** — score against the fingerprint, apply confidence bands, route to AUTO / SUGGEST / FLAG / PROTECTED
- **Writer** — render the final output with the approved changes

Three modules. Clear contracts between them. Mixing responsibilities is how silent failures creep in.

### Audio is evidence-only, never writer
Audio (Stage 4) supports or contradicts proposals. It does not originate proposals. The one exception: literal blanks in the rough where the engine cannot infer the word — audio can originate a candidate, but always routes to MB review.

This rule survives any architectural shift. If a future design lets audio write directly, that's a regression.

### Provenance ledger
Every change in the final output carries a backstory:

- Rule that fired
- Evidence that supported the change
- Confidence number at time of change
- Source data reference
- Whether MB later accepted, edited, or rejected the change

Subpoena-defensible. MB can answer "why does this transcript say X" with the ledger. The ledger is the credibility moat under the product moat.

---

## What's NOT in scope yet

These are real concerns but later concerns. Don't conflate them with current work.

- **Real-time transcript generation** — the product is post-rough acceleration, not live capture
- **Speaker diarization beyond CAT's existing labeling** — MB's CAT export is the input; the engine does not add speaker IDs
- **Multi-CR collaboration on a single depo** — one CR per transcript
- **Mobile UX** — desktop reviewer interface only
- **Spanish or non-English transcripts** — English depositions only
- **Anything beyond legal depositions** — courtroom, hearing, conference transcripts are out of scope

When scope creep pressure shows up, this list is the bounce-back.

---

## What this means for today's decisions

When we spec the build for the three structural layers (splits, capitalization, punctuation), every spec passes the **R1 test:** does this work for CR #1 AND CR #2-10 without rewrites?

When we design the fingerprint data architecture, every schema decision passes **R2, R5, R6, R7:** universal/personal separation, per-CR confidence, auto-promotion, 20% preserved.

When we draft the onboarding playbook, **R9 and R10** are the deliverables.

This file is the contract. If a build proposal violates a requirement here, push back before it ships.

---

— End of FINGERPRINT_FACTORY_REQUIREMENTS.md —
