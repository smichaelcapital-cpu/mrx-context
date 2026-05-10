# FINGERPRINT DATA ARCHITECTURE

**Status:** Load-bearing technical specification. The contract between recon output and engine consumption.
**Owner:** Scott
**Captured:** 2026-05-10 by Opus
**Pairs with:** PRODUCT_VISION_GOLDEN_CIRCLE.md, FINGERPRINT_FACTORY_REQUIREMENTS.md, FUTURE_STATE_AGENT_AGENCY.md
**Last review:** 2026-05-10

---

## Why this document exists

We are about to spend hours of compute and a calibrated subset of MB's archive (243 pairs in the 2022-2026 window) measuring her habits.

If we store the results badly, the work is hard to leverage. We get reports we can read but not query. We get patterns we can describe but not score against. We get a fingerprint that tells one CR's story but doesn't compose into a Golden Circle moat.

If we store it well, every measurement compounds. Every recon adds to a queryable corpus. Every CR onboarded sharpens the universal layer. Every accept/reject from MB tunes confidence numbers automatically. The fingerprint becomes a living asset, not a static document.

This file is the contract that makes the second outcome possible.

It has two sections:

- **Section 1 — Storage schema (the filing cabinet).** What does ONE measured pattern look like on disk? File format, fields, where the 20% misses live, train/test isolation, universal vs personal tagging.
- **Section 2 — Consumption contract (how the engine reads it).** How does the engine query the fingerprint to score a candidate output? How do agents (eventually) read their own slice? How do confidence numbers update over time?

---

## Foundational principles

Five rules every design decision in this document follows. If a future change violates one of these, push back.

**P1. Measurement is sacred. Storage is fungible.**
The recon process produces ground truth. The way we store it should never lose information. We can always re-derive denormalized views, summaries, or alternate indices from the source-of-truth records. We can never re-derive lost detail.
Implication: store raw events, not summaries. Compute summaries on demand.

**P2. Train and test never mix.**
Pairs designated as test (held-out, sacred) NEVER contribute to fingerprint measurements. Not even by accident. Not "just for this one experiment." The schema enforces the wall, the file structure enforces the wall, the recon scripts enforce the wall.
Implication: pair_id is namespaced by split designation. Recon scripts refuse to run against the test set. Audit trail logs every pair access.

**P3. The 20% is the gold. Preserve it always.**
For every measured pattern, the matching events (the 80% that follow the rule) AND the non-matching events (the 20% that don't) are stored with full context. Never throw away the long tail. The 20% is the conscious editorial choice the CR can articulate when she sees the data.
Implication: storage cost is real but acceptable. Long tail value is what makes mini-MB different from a generic engine.

**P4. CR-agnostic from byte one.**
No MB-specific paths, identifiers, or assumptions anywhere in the schema. Every storage path templates on `<INITIALS>`. Every recon script accepts a CR identifier as input. Migrating from MB-only to MB+CR2+CR3 should be a config change, not a refactor.
Implication: the schema must work for CR #1 and CR #11 without rewrites. Test by drafting how CR #2's data would land in the same structure.

**P5. Subpoena-defensible by construction.**
Every measurement traces back to its source pair, its source events, the script that produced it, and the version of the script. Every confidence number traces back to its evidence. Every accept/reject in the feedback loop carries a timestamp and a user. The provenance ledger is built into the schema, not bolted on.
Implication: append-only event logs for confidence updates. Hash the source pairs to detect drift. Version every recon script run.

---

## SECTION 1 — Storage schema (the filing cabinet)

### 1.1 What we are storing

Three categories of data:

**A. Source pairs** — the raw paired roughs and finals. The training corpus and the test corpus.

**B. Measurements** — the recon output. Pattern definitions, event counts, matching events, non-matching events (the 20%), confidence numbers.

**C. Decisions and feedback** — engine proposals, MB's accept/reject, confidence-update history. (Future state — but the schema must support it from day one.)

We design all three together because they reference each other.

### 1.2 Top-level directory layout

```
C:\mrx_training_set\<INITIALS>\
├── MANIFEST.md                          # CR identity, deny-list, metadata
├── paired\                              # Source pairs (cat A, training + test)
│   ├── SPLIT_MANIFEST.md                # Train/test split methodology + audit
│   ├── TRAINING_SET.md                  # List of training pair IDs + paths
│   ├── TEST_SET.md                      # List of test pair IDs + paths (SACRED)
│   ├── <case_id>\                       # One folder per case
│   │   ├── rough\                       # Rough source files
│   │   └── final\                       # Final source files
│   └── ...
├── extracted\                           # Plain-text extractions of all pairs
│   ├── <pair_id>.rough.txt              # One per pair
│   ├── <pair_id>.final.txt
│   └── _extraction_log.jsonl            # Append-only log of every extraction
├── fingerprint\                         # The fingerprint itself (Section 1.3+)
│   ├── manifest.yaml                    # Fingerprint version, recon run info
│   ├── patterns\                        # One file per pattern (Section 1.4)
│   │   ├── <pattern_id>.yaml
│   │   └── ...
│   ├── events\                          # Raw event store (Section 1.5)
│   │   ├── <pattern_id>.matching.jsonl
│   │   ├── <pattern_id>.nonmatching.jsonl
│   │   └── ...
│   └── confidence_history\              # Append-only confidence updates (Section 1.6)
│       └── <pattern_id>.history.jsonl
├── reports\                             # Recon and eval reports
│   ├── <YYYY-MM-DD>_<recon_name>.md     # Full local reports (may quote depo text)
│   └── eval\                            # Test-set evaluation results
│       └── <YYYY-MM-DD>_eval_run.md
└── _provenance\                         # Subpoena-defense ledger
    ├── recon_runs.jsonl                 # Every recon script execution
    ├── pair_access.jsonl                # Every read of every pair
    └── script_versions\                 # Hashed snapshots of every recon script
```

This structure is templated. CR #2 gets the same tree under `<INITIALS>` for her initials. Only the contents differ.

### 1.3 The fingerprint manifest

Every fingerprint version is anchored by a manifest file. This is the entry point for any consumer.

`fingerprint\manifest.yaml`:

```yaml
fingerprint_version: "2026-05-11.v1"
cr_initials: "MB"
created: "2026-05-11T08:00:00-04:00"
created_by_recon_run: "recon_run_20260511_0800"
training_pair_count: 195
training_pair_date_range: ["2022-01-15", "2026-04-30"]
test_pair_count: 48
test_pair_date_range: ["2025-09-01", "2026-04-30"]
patterns_total: 17
patterns_by_layer:
  splits: 5
  capitalization: 2
  punctuation: 14
  lexical: 0
patterns_by_confidence:
  AUTO: 8        # >= 0.90
  SUGGEST: 6     # 0.60 - 0.89
  FLAG: 3        # < 0.60
  PROTECTED: 0   # any confidence on protected class
schema_version: "1.0"
```

The manifest is human-readable and machine-readable. It tells us at a glance what fingerprint version we're looking at, what was used to build it, and what's in it.

Every recon run produces a NEW manifest with a new version. Old manifests are kept. The fingerprint is versioned, not overwritten.

### 1.4 Pattern record format

One YAML file per measured pattern. This is the heart of the fingerprint.

Example: `fingerprint\patterns\punct_stage_direction.yaml`

```yaml
# Pattern identity
pattern_id: "punct_stage_direction"
pattern_name: "End-of-sentence mark before parenthetical"
layer: "punctuation"        # splits | capitalization | punctuation | lexical
sublayer: "stage_direction" # optional finer grouping
universality_tag: "unknown" # universal | personal | unknown (until we have CR #2+)

# What the pattern detects
description: |
  When the rough contains an open-parenthesis introducing a stage direction
  (e.g., "(Witness peruses document.)" or "(Whereupon, Exhibit No. 1...)"),
  MB inserts an end-of-sentence punctuation mark immediately before the
  open-paren. The two specific forms observed: "?(" and ".(".
detection_method: "content_match"  # gap_alignment | content_match | regex
detection_method_notes: |
  Standard SequenceMatcher gap alignment fails for this pattern because
  the word before the paren often differs between rough and final.
  Use content_match: locate "?(" and ".(" in the final, identify the
  parenthetical content, find the matching parenthetical in the rough,
  compare punctuation immediately before the open-paren in both.

# Examples (for human review and engine reference)
example_canonical:
  rough_excerpt: "What about the form (Witness peruses document) ..."
  final_excerpt: "What about the form? (Witness peruses document.) ..."
  explanation: "MB added the question mark before the parenthetical."
example_non_matching:
  rough_excerpt: "..."
  final_excerpt: "..."
  explanation: "MB chose to leave the parenthetical without preceding end-mark in this context -- see events.nonmatching for full context."

# Measurement
measurement:
  recon_run_id: "recon_run_20260511_0800"
  matching_event_count: 203
  nonmatching_event_count: 0
  total_relevant_events: 203
  pairs_observed_in: 195       # how many training pairs had at least one event
  pairs_total_in_training: 195
  pairs_coverage_ratio: 1.0    # 195/195

# Confidence
confidence:
  current: 1.00
  current_lane: "AUTO"          # AUTO | SUGGEST | FLAG | PROTECTED
  current_lane_threshold_basis: "ratio"  # ratio | accept_reject | hybrid
  history_file: "confidence_history\\punct_stage_direction.history.jsonl"

# Routing
routing:
  protected_class: false        # if true, always routes through SUGGEST/FLAG regardless of confidence
  audio_evidence_required: false
  notes: ""

# Provenance
provenance:
  first_observed_recon: "recon_run_20260511_0800"
  last_updated_recon: "recon_run_20260511_0800"
  events_file_matching: "events\\punct_stage_direction.matching.jsonl"
  events_file_nonmatching: "events\\punct_stage_direction.nonmatching.jsonl"
  detector_script: "scripts/detectors/punct_stage_direction.py"
  detector_script_version_hash: "abc123def456..."
```

Notes:

- `universality_tag` starts at `unknown` and gets re-evaluated when CR #2 is measured. If CR #2 has the same pattern at similar ratio, both flip to `universal`. If only MB has it, MB flips to `personal`.
- `detection_method` matters because some patterns can't be measured by simple gap alignment (per the Butler / stage-direction lesson). Each pattern declares its method.
- `example_canonical` and `example_non_matching` live IN the YAML for quick human inspection. Full event lists live in the events files.
- `confidence.current_lane_threshold_basis` is a forward-looking field — early on, lane assignment is based purely on the matching/total ratio. Once we have engine deployment + MB feedback, lane assignment shifts to accept/reject ratios. The schema supports both.

### 1.5 Event records (the 80% and the 20%)

Each pattern has two append-only JSONL files:

- `events\<pattern_id>.matching.jsonl` — the events that follow the rule
- `events\<pattern_id>.nonmatching.jsonl` — the events that don't

Each line is one event:

```json
{
  "event_id": "evt_punct_stage_direction_000001",
  "pattern_id": "punct_stage_direction",
  "recon_run_id": "recon_run_20260511_0800",
  "pair_id": "training_032025olsen_001",
  "split_designation": "training",
  "rough_offset": 36931,
  "final_offset": 39112,
  "rough_excerpt": "you know what Bates numbers are (Whereupon, Exhibit",
  "final_excerpt": "you know what Bates numbers are? (Whereupon, Exhibit",
  "rough_context_before": "...500 chars before...",
  "rough_context_after": "...500 chars after...",
  "final_context_before": "...500 chars before...",
  "final_context_after": "...500 chars after...",
  "category": "matching",
  "subcategory": "question_mark_added",
  "captured_at": "2026-05-11T08:14:23-04:00"
}
```

Critical schema rules:

- `split_designation` is required. Recon runs assert that no event from a test pair ever appears here. (Test pairs only generate events in eval runs, stored under `reports\eval\`.)
- Context before/after is captured at recon time. Storage cost is real but small. This is what lets us inspect a pattern weeks later without re-reading the source pair.
- `subcategory` allows a pattern to split into sub-rules later without losing the original measurements. (E.g., "question_mark_added" vs "period_added" within stage_direction.)
- Append-only. Events are never deleted. If a pattern is deprecated, its events file is moved to `_archive\` with a tombstone.

### 1.6 Confidence history (the feedback loop)

For every pattern, an append-only history of confidence changes:

`confidence_history\<pattern_id>.history.jsonl`

```json
{"timestamp": "2026-05-11T08:00:00-04:00", "event_type": "initial_measurement", "recon_run_id": "recon_run_20260511_0800", "matching": 203, "nonmatching": 0, "ratio": 1.0, "lane": "AUTO", "trigger": "first_recon"}
{"timestamp": "2026-05-13T14:20:00-04:00", "event_type": "engine_proposal", "proposal_id": "prop_001", "pair_id": "test_<id>", "result": "auto_applied"}
{"timestamp": "2026-05-13T16:45:00-04:00", "event_type": "mb_review", "proposal_id": "prop_001", "decision": "accepted", "reviewer": "MB"}
```

This is the audit trail that makes the feedback loop subpoena-defensible. Every confidence number is justifiable from this log.

Future state: when MB accepts/rejects engine proposals, those events land here. A nightly process (or on-demand recompute) updates `pattern.yaml.confidence.current` based on the rolling history.

### 1.7 Train/test isolation enforcement

Three layers of enforcement:

**Layer 1 — File system separation.**
Training pair IDs are prefixed `training_*`. Test pair IDs are prefixed `test_*`. Recon scripts validate this prefix on every read.

**Layer 2 — Recon script assertion.**
Every recon script begins with:

```python
def load_pairs(corpus="training"):
    assert corpus in ("training", "test_eval_only"), \
        "Corpus must be explicitly declared. Test corpus only loadable in eval mode."
    if corpus == "test_eval_only":
        assert os.environ.get("MRX_EVAL_MODE") == "1", \
            "Test corpus access requires MRX_EVAL_MODE=1 env var. Recons cannot use test data."
```

**Layer 3 — Audit log.**
Every pair access is logged to `_provenance\pair_access.jsonl`:

```json
{"timestamp": "...", "pair_id": "training_032025olsen_001", "accessing_script": "recon_punctuation_v3.py", "purpose": "recon_measurement", "mode": "training"}
```

A weekly audit script reviews this log and alerts if any test pair was accessed by a non-eval script.

### 1.8 Test set scoring (the maturation curve)

Every time we want to know "how good is the fingerprint right now," we run an eval against the held-out test set. The eval produces a scoring report that lives at:

`reports\eval\<YYYY-MM-DD>_eval_run.md`

The eval scoring methodology (high-level):

1. For each test pair: load the rough, run the engine using the current fingerprint, produce a candidate final.
2. Diff the candidate against the actual final.
3. Categorize each diff: `ENGINE_MATCH` (engine produced what MB produced), `ENGINE_MISS` (MB did something engine didn't), `ENGINE_OVERREACH` (engine did something MB didn't), `STYLE_GAP` (engine and MB chose differently in a defensible way).
4. Score per pair: (matches) / (matches + misses + overreaches).
5. Score across the test set: average of per-pair scores, plus distribution.

Eval reports are versioned and never overwritten. This is the maturation curve. We watch it move week over week.

The test set itself is NEVER used to inform the fingerprint. Its only job is to measure the fingerprint.

### 1.9 Universal vs personal layer (forward-looking)

When CR #2's fingerprint is measured, the schema flips on a comparison process:

For each MB pattern:

- If CR #2 has a corresponding pattern AND ratios are within X% of each other AND both meet a universality bar (e.g., both >= 0.85) → both patterns flip `universality_tag` to `universal`.
- If CR #2 doesn't have the pattern OR ratios diverge significantly → MB's pattern flips to `personal`. CR #2's gets its own personal pattern.
- If CR #2 has the pattern at very different ratio → both flip to `personal_variable`. The pattern exists but per-CR calibration is required.

A separate ledger at `mrx-context/knowledge/REPORTER_PATTERN_HYPOTHESES.md` (per R10 of the requirements doc) tracks these comparisons. The hypotheses ledger is the cross-CR IP.

After CR #5, the universal layer should be largely stable. Onboarding CR #6+ becomes faster: pre-load universal patterns, only calibrate personal ones.

### 1.10 Confidentiality boundary in the schema

Per Rule 8 (anything in `C:\mrx_training_set\` never pushes) and per R8 of the requirements doc:

- Everything under `C:\mrx_training_set\<INITIALS>\` is local-only. None of it pushes.
- Sanitized summaries pushable to `mrx-context/reports/<YYYY-MM-DD>/` are derived FROM the local tree, with witness names and case content scrubbed.
- The sanitization process is automated (grep against MANIFEST.md deny-list). Human discipline is a backup, not a primary enforcement.

The schema makes this enforceable: MANIFEST.md is canonical, the sanitization script reads it, the public push is blocked if the script fails.

---

## SECTION 2 — Consumption contract (how the engine reads it)

### 2.1 Who consumes the fingerprint

Three consumers. Each has different needs.

**A. The current single-pass engine (immediate term).**
For each candidate change in a rough-to-final pass, the engine looks up the relevant pattern, reads the confidence number, decides the lane (AUTO / SUGGEST / FLAG / PROTECTED), and routes accordingly. The engine never modifies the fingerprint — it only reads.

**B. Future agent army (per FUTURE_STATE_AGENT_AGENCY.md).**
Each agent owns one or two patterns. Each agent reads its own slice of the fingerprint at startup. Each agent emits proposals with confidence + provenance. Same read pattern, narrower scope per agent.

**C. The eval runner (validation infrastructure).**
Reads the fingerprint AND the test set. Produces eval reports. Never modifies the fingerprint.

All three consumers use the same query interface. That's the consumption contract.

### 2.2 The query interface

A consumer doesn't read raw YAML/JSONL files directly. It uses a query API.

For the immediate term, this is a Python module (`fingerprint_query.py` or similar) that exposes:

```python
class FingerprintAccess:
    def __init__(self, cr_initials: str, fingerprint_version: str = "latest"):
        """Load the fingerprint manifest and patterns for the given CR."""
        ...

    def get_pattern(self, pattern_id: str) -> PatternRecord:
        """Return the full pattern record."""
        ...

    def list_patterns(self, layer: str = None, lane: str = None) -> List[PatternRecord]:
        """List patterns, optionally filtered."""
        ...

    def get_confidence(self, pattern_id: str) -> float:
        """Return the current confidence number for the pattern."""
        ...

    def get_lane(self, pattern_id: str) -> str:
        """Return the current routing lane (AUTO/SUGGEST/FLAG/PROTECTED)."""
        ...

    def get_examples(self, pattern_id: str, n: int = 5) -> dict:
        """Return canonical and non-matching examples for inspection."""
        ...

    def is_protected_class(self, pattern_id: str) -> bool:
        """Whether this pattern is in a protected class (always SUGGEST/FLAG regardless of confidence)."""
        ...
```

The API is read-only. Updates go through a separate `FingerprintWriter` that goes through the confidence history append + manifest re-issue path. Splitting reads and writes prevents accidental mutation.

### 2.3 Routing decision (the three-lane architecture)

When the engine has a candidate change:

1. Identify which pattern the change corresponds to (`pattern_id`).
2. Query `get_lane(pattern_id)`.
3. Route based on the lane.

```
AUTO       (confidence >= 0.90, no protected class)  -> apply, log to provenance
SUGGEST    (confidence 0.60-0.89, OR protected class with high confidence) -> propose to MB, await decision
FLAG       (confidence < 0.60)                       -> flag for MB review, no auto-action
PROTECTED  (any confidence on protected class with audio disagreement) -> always to MB
```

If a candidate change doesn't correspond to any pattern (unrecognized situation), it routes to FLAG by default.

**Critical rule:** AUTO does not mean "AI rewrites the final transcript." AUTO means "the engine applies the change in its candidate output, MB still reviews everything before final shipment." Per Three Sealed Phases (Scott, 2026-05-04), MB clears every transcript. AUTO is the engine's confidence in its own proposal, not authority to bypass review.

### 2.4 Confidence updates over time

Confidence numbers move based on three signals:

**Signal A — More data.**
Re-running recons against an expanded pair corpus updates matching and nonmatching counts. Confidence updates accordingly. This is recon-driven update.

**Signal B — Engine performance on test set.**
Eval runs measure how often the engine matches MB on the held-out 48 pairs. Patterns that systematically miss in eval get confidence pulled down even if their training-set ratio is high. This catches overfitting.

**Signal C — MB accept/reject in production.**
When MB reviews engine proposals and accepts or rejects, the result lands in `confidence_history\<pattern_id>.history.jsonl`. A rolling-window calculation updates the pattern's `confidence.current`.

Update rules (initial proposal — refine after deployment):

- Initial confidence: `matching / (matching + nonmatching)`.
- After 50+ engine proposals on a pattern: `0.7 * (training ratio) + 0.3 * (acceptance ratio)`.
- After 200+ engine proposals: acceptance ratio is primary.

Lane changes are handled by:

- Confidence crosses 0.90 -> promotes to AUTO (unless protected class).
- Confidence drops below 0.60 -> demotes to FLAG.
- A new accept/reject in the rolling window is evaluated against the lane thresholds.

All confidence changes log to history. Human intervention to manually pin a confidence is allowed but logged separately as `manual_override` events. (E.g., "MB explicitly told us never to auto-apply X, even though confidence is 0.97.")

### 2.5 Querying for a candidate change (the engine flow)

The engine's per-change flow:

1. **Detect candidate.** Reader emits a candidate change with associated `pattern_id`.
2. **Query fingerprint.** `lane = fingerprint.get_lane(pattern_id)`.
3. **Check protected class.** If `is_protected_class(pattern_id)` and audio disagrees with proposal, force PROTECTED.
4. **Route.** Based on lane:
   - `AUTO` -> apply to candidate output, log to provenance ledger
   - `SUGGEST` -> mark in candidate output, queue for MB review
   - `FLAG` -> mark in candidate output, escalate priority for MB review
   - `PROTECTED` -> always to MB
5. **Log proposal.** Every proposal (regardless of lane) gets logged to `confidence_history\<pattern_id>.history.jsonl` as an `engine_proposal` event.
6. **Await MB decision** (for non-AUTO lanes). When MB acts, log decision as `mb_review` event.

This flow is consistent across the current single-pass engine and the future agent army. The agent army's only difference is that each agent runs the same flow on a narrower scope, in parallel.

### 2.6 Eval runner contract

The eval runner is a separate process. It runs against the test set, NEVER training. Its contract:

1. Load test set. Set `MRX_EVAL_MODE=1` env var. Load `TEST_SET.md` pairs.
2. For each test pair: load the rough.
3. Run the engine in eval mode. Engine produces a candidate final using the current fingerprint. Eval mode means: AUTO/SUGGEST/FLAG decisions still get made, but no actual review happens — the candidate is treated as the eval output.
4. Diff candidate vs actual final. Categorize diffs (ENGINE_MATCH / ENGINE_MISS / ENGINE_OVERREACH / STYLE_GAP).
5. Score per pair, score overall. Write to eval report.
6. Update universality / drift signals. If a pattern systematically misses on test, that's signal — does it deserve a confidence pull-down?

The eval runner has its own provenance. Every eval run is timestamped, hashed, and archived. We track the maturation curve over weeks.

### 2.7 Cross-CR query (forward-looking)

When CR #2 is measured, queries can span both fingerprints:

```python
mb = FingerprintAccess(cr_initials="MB")
cr2 = FingerprintAccess(cr_initials="CR2")

# Compare a specific pattern across CRs
mb_objection = mb.get_pattern("cap_objection_midturn")
cr2_objection = cr2.get_pattern("cap_objection_midturn")

# Hypothesis test: is this pattern universal?
ratio_diff = abs(mb_objection.confidence.current - cr2_objection.confidence.current)
both_high = mb_objection.confidence.current >= 0.85 and cr2_objection.confidence.current >= 0.85
likely_universal = both_high and ratio_diff < 0.1
```

The cross-CR query is the foundation for the universal layer. After CR #5, this query informs which patterns ship as defaults in the onboarding playbook (R9) and which require fresh measurement.

### 2.8 The schema ages well

Three properties that keep this schema useful as the project scales:

**Append-only events.** New measurements never overwrite old ones. We can always look back. Storage cost grows, but linearly.

**Versioned patterns.** Pattern definitions can evolve (new sub-rules, refined detection methods) without invalidating prior measurements. Each pattern record carries `schema_version`. Migrations are explicit.

**CR-agnostic structure.** Every storage path templates on `<INITIALS>`. Adding CR #2 is a new directory tree, not a schema change. By CR #11, the schema hasn't been touched in months.

If any of these break in practice, the schema needs a v2. They are the load-bearing properties.

---

## What this enables for May 13

When the fingerprint is built per this architecture, here's what we can put in front of MB:

**1. A "we measured your work" report.** Not a marketing deck. A real document showing:
- 195 of her depos measured, 48 held out for blind testing
- Per-pattern measurements: count, ratio, examples
- The 20% — patterns where she breaks her own rule, and what the contexts are

**2. A maturation curve.** Day-1 score on the held-out 48 pairs. We can show MB: "this is how close the engine got on depos it has never seen." That number is honest. It's not 100%. It's whatever it is. Over time it climbs as the fingerprint tunes.

**3. The mini-MB pitch with evidence.** "We don't ask you to teach us your habits. We measured them. Here's what we found. Here's what we got right. Here's where we want your input on the 20% we couldn't decide alone."

That's the May 13 deliverable. It is built on this schema. Without this schema, it's a marketing deck. With it, it's evidence.

---

## What this enables for the Golden Circle

When MB introduces CR #2:

1. CR #2's archive lands at `C:\mrx_training_set\CR2\paired\`.
2. Inventory script runs on her root. New pairs found.
3. Train/test split runs. Sacred test set locked.
4. Recons run against her training set. Patterns measured. Per-pattern YAMLs generated.
5. Cross-CR comparison runs against MB's fingerprint. Patterns get tagged universal/personal.
6. Eval runner produces a maturation curve for CR #2 from day one.
7. Within hours, not weeks, CR #2 has a calibrated mini-her.

The schema makes this a templated process. The factory runs.

---

## Open questions / decisions deferred

These are real questions the schema design exposes but doesn't resolve. Worth tracking.

**Q1. How are pattern_ids assigned?**
Manual by humans (Opus + Scott naming new patterns) for now. As pattern count grows past ~50, we may need a registry. Defer.

**Q2. Storage size at scale.**
For MB at 195 training pairs and ~14 patterns measured tonight, storage is small (~hundreds of MB at most). At 10 CRs with 200+ pairs each and 30+ patterns, we're approaching tens of GB. Manageable on local disk. Cloud storage later.

**Q3. Pattern dependencies.**
Some patterns may depend on others. E.g., "Objection mid-turn cap" only fires after the split agent has identified mid-turn boundaries. The schema doesn't currently model dependencies. May need a `requires` field on patterns. Defer until we hit the dependency.

**Q4. Universal layer threshold.**
The "X% ratio similarity" threshold for tagging a pattern universal — is it 5%? 10%? 15%? Pick a number when CR #2 lands and we can calibrate empirically. Defer.

**Q5. Versioning the engine alongside the fingerprint.**
The eval scoring needs to record which engine version produced the candidate. The schema mentions this in passing but doesn't fully specify the engine-version coupling. Worth a follow-up. Defer to spec-build phase.

**Q6. Real-time confidence updates vs nightly batch.**
For MVP, nightly batch update of confidence numbers is fine. Real-time is a future optimization. Defer.

**Q7. Multi-detector patterns.**
Some patterns may need multiple detection methods voting (e.g., comma addition might use both gap alignment AND a regex-based check, with agreement scoring). Schema currently models one `detection_method` per pattern. Extend if needed. Defer.

These are not blockers for tonight's recon or tomorrow's analysis. They are watch items.

---

## What changes when this file changes

This file changes when:

- The schema's load-bearing properties change (P1-P5)
- A new consumer category emerges that the consumption contract doesn't cover
- A storage decision proves wrong in practice (e.g., file format changes from YAML/JSONL to something else)

This file does NOT change for:

- Adding new patterns (those land in `patterns\` per the existing schema)
- Adding new CRs (those land in new `<INITIALS>\` directories)
- Adding new recon scripts (those follow the existing event-emission contract)
- Confidence threshold tuning (those are config, not schema)

If the schema is churning, something is unstable upstream. Check whether the change is really structural or if it's just a tuning decision.

---

— End of FINGERPRINT_DATA_ARCHITECTURE.md —
