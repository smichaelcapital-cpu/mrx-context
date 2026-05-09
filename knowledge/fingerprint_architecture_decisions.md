# Fingerprint Architecture — Locked Decisions
**Captured:** 2026-05-09
**Source:** Opus + Scott working session, morning of 2026-05-09
**Status:** Architecture locked, implementation pending

## North star
"My reporter, but multiplied." The product isn't an AI that fixes transcripts. It's an AI that fixes transcripts *like the specific court reporter would have*. The fingerprint is the technical artifact that makes this real.

## The four-layer model

When a new depo arrives, the engine composes a fingerprint stack from four layers:
[universal]    ← things every CR does (e.g., basic punctuation conventions)
+
[jurisdiction] ← state/court rules (e.g., Louisiana, Delaware, NY-WCB)
+
[case_type]    ← case category (e.g., civil engineering, workers comp, medical)
+
[reporter]     ← CR personal style overrides (e.g., MB.yaml)

The metadata in the depo (court, jurisdiction, case type, reporter) drives lookup. The composed fingerprint feeds the engine.

## Why this matters for the business
- **MB build = methodology build.** Every slot we add for MB teaches us how to fit a CR.
- **CR #2 onboards faster** because jurisdiction + case_type layers are reusable. New CR working in Louisiana inherits the LA jurisdiction profile automatically.
- **The ledger** (mrx-context/fingerprints/ledger.md) tracks which decisions are MB-specific vs. generalizable. It's the onboarding playbook for CR #2 onward.

## File layout (locked)
mrx-context/fingerprints/
├── _template.yaml                  ← shape of any fingerprint
├── ledger.md                       ← decisions and generalizations
├── jurisdictions/
│   ├── louisiana.yaml
│   ├── delaware.yaml
│   └── new_york_wcb.yaml
├── case_types/
│   ├── civil_engineering.yaml
│   ├── workers_comp.yaml
│   └── ...
└── reporters/
├── MB.yaml                     ← MB's PERSONAL overrides only
└── (future: AD.yaml, etc.)

## Six-layer trait structure (within any fingerprint file)
Per the ChatGPT/Copilot reviews from 2026-05-08:
1. Identity
2. Translation Artifacts
3. Structural Formatting
4. Lexical Preferences
5. Risk & Review
6. Drift

For v0: build layers 1, 2, and a partial 3 (negative fingerprint / protected zones). Defer 4-6.

## Critical caveat — AD data is jurisdiction-confounded
The cross-depo scan compared MB (Louisiana) to AD (likely NY-WCB). Patterns that are zero in AD columns may be:
- Personal: MB does X, AD does not
- Jurisdictional: Louisiana convention requires X, NY-WCB does not
- Both

Without LA state guidelines and NY guidelines parsed, we cannot fully isolate MB-the-person from LA-the-jurisdiction. The data is still useful — it tells us patterns are at minimum jurisdictional, possibly personal — but classification of each pattern (MB-specific vs. LA-jurisdictional) requires the state guideline files (currently missing or unintegrated).

## Hallucination finding (locked)
Across all six depos scanned (3 MB + 3 AD), zero `--` em-dashes appear in any raw transcript. Em-dashes that show up in OUR_FINAL output are Stage 3 LLM hallucinations. This is the second symptom of TD-001 (writer making decisions at write time).

The negative fingerprint must include: "MB never injects double-hyphen em-dashes in raw output."

## What this architecture replaces
- The original "ledger" concept (May 7 plan) is collapsed: ledger.md (decisions) + _template.yaml (shape) together replace what was originally one ledger artifact. They serve different purposes.
- The "just write more Stage 2 rules" approach is parked. The 49.5% ceiling on Brandl told us rules alone won't close the gap. Judgment, captured in fingerprint form, is the path.

## Realistic expectations for v0 ceiling lift
- Closes ~108 PER_CR_STYLE blocks
- Suppresses Stage 3 hallucinations (em-dash, possibly others)
- Estimated lift: 49.5% → 60-65% on Brandl
- Does NOT close 235 audio-required blocks (Stage 4 work)
- Does NOT close 116 LLM-judgment blocks (model work)

The fingerprint is the wedge that ALSO generalizes. That generalization is why we're doing it before audio integration.
