# Fingerprint Architecture — External Review (Microsoft Copilot)
**Date:** 2026-05-08
**Source:** Microsoft Copilot, prompted with MRX project context
**Purpose:** Outside-AI objective opinion on what belongs in a court reporter fingerprint file

---

You're thinking about this the right way.

The biggest insight in your entire writeup is this:

**Court reporters are not "users." They are deterministic linguistic systems with stable personal translation artifacts.**

That changes the architecture completely.

Most people would build:
- generic transcript cleanup
- then sprinkle AI on top

I would build:
- deterministic reporter-specific normalization first
- AI only where ambiguity remains
- continuous fingerprint learning after every finalized transcript

That ordering matters enormously.

## First hard truth: You are NOT building a proofreading engine

You are building a **personalized translation recovery system**.

The "rough" transcript is not English. It is:
- steno dictionary output
- translation artifacts
- software quirks
- personal editing doctrine
- jurisdiction formatting rules
- realtime cognitive shortcuts

That means:
- generic LLM cleanup will always plateau
- reporter-specific priors are the real moat

**The fingerprint becomes the product.**

## Second hard truth: Raw RTF alone is not enough long term

You can bootstrap fingerprints from roughs alone. But eventually your highest-quality system will require:
- rough transcript
- final transcript
- alignment diff between them

Why? Because many reporter preferences are invisible unless you compare RAW → FINAL.

Example:
- raw: twothirds
- final: two-thirds

Without finals: you can detect artifact frequency but not confidently infer intended normalization policy.

So architect for: rough corpus + aligned finals + correction history + override feedback. Even if you don't have all of it initially.

---

## What I would put in a reporter fingerprint

I would separate the fingerprint into SIX layers.

### 1. Reporter Identity Layer (Stable metadata)

Not just demographics. You want operational context.

```yaml
reporter:
  id: mb_louisiana_001
  jurisdiction: LA
  software: CaseCATalyst
  realtime: true
  years_experience: 18
  scopist_usage: false
  proofreader_usage: true
  preferred_style_guide:
    - NCRA
    - Louisiana custom
```

Why this matters:
- realtime writers leak different artifacts
- scopist workflows produce different rough characteristics
- jurisdictions change colloquy norms
- CAT software leaks are highly vendor-specific

### 2. Translation Artifact Layer

This is the MOST IMPORTANT section. These are deterministic machine defects.

```yaml
translation_artifacts:
  literal_leaks:
    - pattern: "943 point on"
      meaning: "decimal rendering failure"
      correction_strategy: decimal_recovery
      confidence: deterministic
  malformed_briefs:
    - raw: "twothirds"
      final: "two-thirds"
      confidence: 1.0
    - raw: "threeandahalf"
      final: "three-and-a-half"
  audio_placeholders:
    - token: "*REPORTER CHECK HERE*"
      meaning: audio_review_required
      severity: informational
      never_autocorrect: true
  colloquy_repairs:
    - raw: "Object"
      final: "Objection"
  filler_artifacts:
    - raw: "uhhuh"
      final: "uh-huh"
```

Key point: DO NOT treat these as regex rules. Treat them as **typed linguistic phenomena**. That distinction matters later.

### 3. Structural Formatting Layer

This is where most AI systems fail. You discovered:
- continuation paragraph behavior
- style code usage
- Q/A formatting habits

This matters because formatting contains meaning.

```yaml
formatting_behavior:
  qa_behavior:
    continuation_q_labels: frequent
    continuation_a_labels: rare
  paragraphing:
    average_turn_split_length: 142_words
  punctuation:
    em_dash_stutters_present: false
    ellipsis_frequency_per_1000: 0.8
  colloquy_style:
    objection_spelling: "Objection"
  capitalization:
    speaker_labels: uppercase
```

This layer should drive hallucination suppression and formatting confidence scoring.

Your em-dash insight is huge. You already found: **LLM prior > source truth**. That is a massive warning sign.

### 4. Lexical Preference Layer

These are stylistic preferences. Important: **DO NOT mix these with defects.**

Examples:
- two-thirds vs two thirds
- okay vs OK
- percent vs %

These are preferences, not corrections.

```yaml
lexical_preferences:
  hyphenation:
    compound_fractions: always_hyphenated
    age_modifiers: always_hyphenated
  numerics:
    percentages: word_form
    decades: apostrophe_style_b
  affirmatives:
    okay_variant: "okay"
  colloquial_forms:
    uh_huh_variant: "uh-huh"
```

This layer should have LOWER authority than deterministic defect rules.

### 5. Risk & Review Layer

This is where commercial value lives. You need reporter-specific risk modeling.

```yaml
review_policy:
  always_review:
    - low_confidence_audio
    - speaker_conflict
    - numeric_reconstruction
  never_flag:
    - uhhuh_normalization
    - object_to_objection
  escalate_if:
    decimal_recovery:
      confidence_below: 0.92
  hallucination_watch:
    forbidden_insertions:
      - em_dash_stutter
      - "[sic]"
```

This becomes time savings, trust preservation, malpractice prevention.

### 6. Drift / Evolution Layer

This is the truly advanced piece. Most systems freeze user preferences. Bad idea. You need temporal modeling.

```yaml
drift_tracking:
  tracked_metrics:
    - continuation_q_frequency
    - uhhuh_frequency
    - unresolved_tokens_per_1000
    - hyphenation_rate
  baseline_window:
    depositions: 20
  alert_thresholds:
    z_score: 2.5
  detected_changes:
    - metric: em_dash_usage
      changed_on: 2026-02-01
      previous_rate: 0.0
      current_rate: 14.2
```

This matters because reporters retrain dictionaries, change scopists, change CAT settings, adapt to firms, change realtime methods. Your system should evolve automatically.

---

## Biggest architecture recommendation: Separate FACTS from INFERENCES

This is critical.

Do NOT store:
```yaml
reporter_likes_hyphens: true
```

Store:
```yaml
observed:
  two-thirds:
    occurrences: 412
    correction_rate: 100%
```

Then derive:
```yaml
inference:
  compound_fraction_hyphenation: high_confidence
```

Why? Observations are durable. Inferences evolve. Models improve later. If you mix them, your fingerprint becomes brittle.

## Another major trap: Overfitting to tiny datasets

You analyzed 6 depos. That's enough to detect signals. Not enough to define doctrine.

You need: confidence per trait, sample size per trait, recency weighting.

```yaml
traits:
  em_dash_absence:
    confidence: 0.97
    sample_size: 6
    last_seen: 2026-05-01
```

Otherwise you'll encode noise as law.

## Another trap: Treating all corrections equally

They are NOT equal. You need correction classes:

| Class | Meaning | AI Needed? | Risk |
|-------|---------|------------|------|
| Mechanical | deterministic artifact | no | low |
| Stylistic | reporter preference | sometimes | low |
| Semantic | meaning reconstruction | yes | high |
| Evidentiary | affects testimony meaning | yes | critical |
| Audio-dependent | requires recording | impossible without audio | critical |

This classification becomes your routing engine.

## What you probably haven't thought about enough: Negative fingerprints

Not just: "What does this reporter do?"

But: "What does this reporter NEVER do?"

That's incredibly powerful.

Example:
- never uses em dashes
- never uses semicolons
- never drops continuation Q labels
- never writes "Object"

These become **hallucination suppressors**. This is probably more valuable than positive traits.

## I would NOT use Markdown

Use YAML for human editing OR JSON for machine-first systems.

My recommendation: **Hybrid architecture**
- Canonical storage: JSON
- Human-review/export layer: YAML

Reason: JSON validates better, schemas easier, APIs easier, embeddings cleaner, diffing cleaner. But YAML is fantastic for debugging, reporter review, ops tooling.

---

## Final architecture opinion

I would structure the engine like this:
INGEST RTF
↓
artifact detector
↓
reporter fingerprint matcher
↓
deterministic repair engine
↓
risk classifier
↓
LLM semantic cleanup
↓
hallucination suppression layer
↓
review queue generator
↓
final polish export
↓
learn from reporter edits
↓
update fingerprint

The hallucination suppression layer is essential. Most people won't build that. You should.

## One last hard truth: Your biggest business risk is not accuracy. It is trust volatility.

Court reporters will tolerate 2% residual cleanup.

They will NOT tolerate:
- one fabricated testimony fragment
- one hallucinated stutter
- one wrong decimal
- one fake speaker attribution

That means **precision matters more than recall**.

You are not building ChatGPT for transcripts. You are building **a conservative legal-language recovery system**.

That mindset should drive every architectural decision.
