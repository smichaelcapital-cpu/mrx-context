# SPEC — Overnight Fingerprint Recon Run

**Date:** 2026-05-10
**Owner:** Scott
**Architect:** Opus
**Builder:** Fresh Sonnet (overnight, ~8 PM kickoff)
**Target:** mrx-context/specs/2026-05-10_OVERNIGHT_RECON_SPEC.md

---

## RAMP — READ IN ORDER BEFORE TOUCHING ANY DATA

This is non-negotiable. The four knowledge files reframe the project. Skipping them means building the wrong thing.

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/FUTURE_STATE_AGENT_AGENCY.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/FINGERPRINT_DATA_ARCHITECTURE.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-10_1121.md (with addendum at the bottom)
9. `C:\mrx_training_set\MB\paired\SPLIT_MANIFEST.md`
10. This spec in full

After reading: confirm in ONE LINE: "Ramped fresh Sonnet 2026-05-10 overnight. Ready."

---

## ONE-LINE PURPOSE

Re-run all four fingerprint recons (splits, capitalization, punctuation, lexical) against the 195-pair training set, producing structured output per FINGERPRINT_DATA_ARCHITECTURE.md so the engine can consume the fingerprint directly.

---

## WHY THIS RUN MATTERS

Yesterday's recons were against 7 pairs. Three layers crossed HIGH-confidence (structural). One did not (lexical). Today we have 195 training pairs. The lexical layer should cross HIGH. The structural three should tighten dramatically.

This is the run that produces the fingerprint we put in front of MB on May 13.

---

## CRITICAL RULES (READ TWICE)

### RULE 1 — Test set is sacred

The 48 test pairs at `C:\mrx_training_set\MB\paired\TEST_SET.md` are NEVER touched by this run. Not loaded. Not measured. Not referenced.

Every recon script MUST begin with this assertion:

```python
TEST_SET_PATH = r"C:\mrx_training_set\MB\paired\TEST_SET.md"
TRAINING_SET_PATH = r"C:\mrx_training_set\MB\paired\TRAINING_SET.md"

def load_pairs(corpus="training"):
    assert corpus == "training", \
        f"Recon scripts cannot load test corpus. Got: {corpus}"
    # Load training pairs only
    ...
```

If you find yourself writing code that reads TEST_SET.md or any pair listed in it, STOP. That's a bug.

### RULE 2 — Confidentiality boundary

Everything in `C:\mrx_training_set\MB\` is local-only. Includes:

- Source pairs (rough + final)
- Extracted text
- Pattern measurements
- Event records (matching AND non-matching)
- Reports with depo content

NEVER push to public repo:

- Witness names
- Case IDs
- Folder paths under `C:\Cat4\usr\scott`
- Depo text in any form

CAN push to public repo (sanitized):

- Pattern counts (e.g., "punctuation patterns: 14 HIGH-confidence")
- Layer-level summaries
- Layer verdicts

Sanitization runs grep against `C:\mrx_training_set\MB\paired\MANIFEST.md` before any public push. If grep returns ANY witness name or case ID, BLOCK the push and flag to Scott.

### RULE 3 — Output structure follows the data architecture

This run produces FINGERPRINT_DATA_ARCHITECTURE-compliant output. Not just markdown reports. The actual filing cabinet.

Output goes to: `C:\mrx_training_set\MB\fingerprint\`

Structure:

```
C:\mrx_training_set\MB\fingerprint\manifest.yaml
C:\mrx_training_set\MB\fingerprint\patterns\<pattern_id>.yaml  (one per pattern)
C:\mrx_training_set\MB\fingerprint\events\<pattern_id>.matching.jsonl
C:\mrx_training_set\MB\fingerprint\events\<pattern_id>.nonmatching.jsonl
C:\mrx_training_set\MB\fingerprint\confidence_history\<pattern_id>.history.jsonl
```

Markdown reports for human reading also produced (see Section "Deliverables" below), but the YAML/JSONL filing cabinet is the authoritative output. Engine consumers read the cabinet, not the reports.

### RULE 4 — Push authority

Push authority IS granted to fresh Sonnet for tonight's run, since Scott may be asleep when the run completes. This is a one-night exception. Standing rule (Scott-only push) restores Monday morning.

Push:

- Public summaries to `mrx-context/reports/2026-05-11/` (after grep verification)
- Updated handoff to `mrx-context/handoffs/HANDOFF_SONNET_2026-05-10_overnight.md`

DO NOT push:

- Anything from `C:\mrx_training_set\`
- Engine repo changes (no engine code changes expected this run anyway)

### RULE 5 — Coder mindset

Before any change to scripts or output: "Could this reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag to Scott in chat (he'll see it Monday morning), proceed with the safer path.

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Slow is smooth. Smooth is fast.

---

## INPUT CORPUS

Training set: 195 pairs.
Source list: `C:\mrx_training_set\MB\paired\TRAINING_SET.md`

Year distribution:

- 2025: 23 pairs
- 2024: 63 pairs
- 2023: 51 pairs
- 2022: 58 pairs
- Total: 195

Each pair has:

- Rough file (typically .sgngl)
- Final file (typically .txt or .rtf)

Extracted plain-text versions are at `C:\mrx_training_set\MB\extracted\` for the original 7 pairs. The other 188 pairs need extraction as a Phase 0 step.

---

## PHASE 0 — Pre-flight checks (must complete before any recon runs)

### 0.1 — Verify input integrity

Load TRAINING_SET.md and assert:

- Exactly 195 entries
- Every entry has both rough and final file paths
- Every file path exists and is >5KB
- Zero overlap with TEST_SET.md (cross-reference)

If ANY check fails: STOP, write findings to `C:\mrx_training_set\MB\reports\2026-05-10_overnight_preflight_FAILED.md`, do not proceed.

### 0.2 — Extract plain text for all 195 pairs

For each pair without an existing extraction:

- Extract rough .sgngl to plain text -> `C:\mrx_training_set\MB\extracted\<pair_id>.rough.txt`
- Extract final .txt/.rtf to plain text -> `C:\mrx_training_set\MB\extracted\<pair_id>.final.txt`

Use the extraction methodology from yesterday's run. If a pair fails extraction, log it to `C:\mrx_training_set\MB\extracted\_extraction_log.jsonl` with:

```json
{"timestamp": "...", "pair_id": "...", "status": "failed", "reason": "..."}
```

Don't block the run on extraction failures. Excluded pairs are reported in the manifest.

### 0.3 — Rough quality check (per R11)

For each successfully-extracted pair, compute:

- Rough token count
- Final token count
- Ratio rough/final

Flag pairs as QUARANTINED if:

- Rough token count < 1,000 (suspiciously short)
- Rough/final ratio outside 0.3 - 1.5 (alignment likely to fail)
- Either file fails to extract

Quarantined pairs are excluded from gap-based recons (lexical, gap-based punctuation) but MAY contribute to content-match recons (stage-direction, etc.) where alignment isn't required.

Write quarantine list to: `C:\mrx_training_set\MB\fingerprint_preflight\quarantined_pairs.jsonl`

Yesterday's Butler depo (082222butler) is the prototype for this issue. Expect similar cases at 195 pairs scale. Catch them up front, don't let them silently corrupt counts.

### 0.4 — Confirm pre-flight clean

Write summary to `C:\mrx_training_set\MB\reports\2026-05-10_overnight_preflight.md`:

- Pairs loaded: N
- Pairs extracted: M
- Pairs quarantined: K
- Pairs available for full recons: N - K
- Pairs available for content-match recons: M (includes quarantined for some patterns)

If the available-for-full-recon count drops below 150, STOP and flag Scott. That's a signal something went wrong upstream.

---

## PHASE 1 — Splits recon

### Pattern targets (from yesterday's 7-pair run)

Confirmed HIGH-confidence patterns (re-measure at 195):

- `split_bare_and_q_opener` — bare "And" as Q opener (was 671 events at 7 pairs)
- `split_so_q_opener` — "So" as Q opener (373 events)
- `split_double_dash_interruption` — double-dash interruption (244 events)
- `split_trailing_huh` — trailing "huh?" confirmation (101 events, 6/7 depos)
- `split_now_q_opener` — "Now," as Q opener (54 events, 6/7 depos)
- `split_leading_yes` — leading "Yes," (1,382 events)
- `split_leading_okay` — leading "Okay." (620 events)

### Discovery sweep

After re-measuring known patterns, run the systematic Q/A transition discovery sweep again. At 195 pairs we expect:

- Confirmation of all 7 known patterns at HIGH-confidence
- Possible new patterns that were below noise floor at 7 pairs
- Sub-pattern discovery within existing patterns (e.g., "And" might split into "And" + "And then" + "And so" with different ratios)

### Per RULE 3, output goes to FINGERPRINT_DATA_ARCHITECTURE format:

- `patterns\split_<pattern_id>.yaml`
- `events\split_<pattern_id>.matching.jsonl`
- `events\split_<pattern_id>.nonmatching.jsonl`
- `confidence_history\split_<pattern_id>.history.jsonl` (with initial_measurement event)

### Detection method per pattern

Most splits use `gap_alignment` detection. Document any pattern that requires `content_match` or `regex` in the pattern YAML.

### Markdown report

Also produce: `C:\mrx_training_set\MB\reports\2026-05-11_splits_recon_v2.md`

- Top-line: total events, patterns confirmed/discovered, confidence summary
- Per-pattern breakdown with HIGH/MEDIUM/LOW verdict
- Coverage: pairs observed in / pairs total
- Comparison vs yesterday's 7-pair numbers (where applicable)

---

## PHASE 2 — Capitalization recon

### Pattern targets

Confirmed HIGH-confidence patterns (re-measure at 195):

- `cap_sentence_start` — capitalize first word of every sentence (was ~11,000 events at 7 pairs)
- `cap_objection_midturn` — "Objection" mid-turn cap (262 events, 5/7 depos)

### Discovery sweep

Re-run the capitalization habit scan against 195 pairs. Look for:

- Sub-patterns within cap_sentence_start (e.g., post-colon, post-em-dash, post-question-mark)
- New cap patterns below 7-pair noise floor
- Patterns that fire reliably in some contexts but not others (becomes the 20%)

### Mis-classification check

Yesterday's recon initially misclassified some cap_sentence_start events as "proper noun lift." Sonnet caught it and fixed. At 195 pairs, this kind of error compounds. Build the mis-classification check INTO the script — flag any pattern where >5% of events have alternate plausible explanations, surface for review.

### Output per data architecture

- `patterns\cap_<pattern_id>.yaml`
- `events\cap_<pattern_id>.matching.jsonl`
- `events\cap_<pattern_id>.nonmatching.jsonl`
- Markdown report: `C:\mrx_training_set\MB\reports\2026-05-11_capitalization_recon_v2.md`

---

## PHASE 3 — Punctuation recon

### Pattern targets

Confirmed HIGH-confidence patterns (re-measure at 195):

Top three (all 7/7 depos at 7-pair scale):

- `punct_period_addition` — period addition (was 2,726 events)
- `punct_comma_addition` — comma addition (2,561 events)
- `punct_emdash_addition` — em-dash addition (657 events)

Stage-direction patterns (use content_match, NOT gap_alignment):

- `punct_stage_direction_question` — ?( pattern (125 events at 7 pairs, 6/7 depos)
- `punct_stage_direction_period` — .( pattern (78 events at 7 pairs, 7/7 depos)

Plus 9 other HIGH-confidence patterns from yesterday's report (full list in `C:\mrx_training_set\MB\reports\2026-05-09_punctuation_transformation_census.md`).

### Critical: detection method per pattern

The stage-direction patterns CANNOT use `gap_alignment`. The word before `(` differs between rough and final, so SequenceMatcher equal-pair approach returns zero. Use content-match: locate the parenthetical content, find it in both rough and final, compare punctuation immediately before the open-paren.

Document this in the pattern YAML's `detection_method_notes` field.

### Discovery sweep

Punctuation was the strongest layer at 7 pairs (14 HIGH-confidence patterns). At 195 pairs expect:

- All 14 confirmed
- Possibly 5-10 new patterns surfaced
- Sub-pattern discovery (e.g., comma addition might split by context: "before but", "before so", "in lists", etc.)

### Output per data architecture

- `patterns\punct_<pattern_id>.yaml` for each pattern
- `events\punct_<pattern_id>.matching.jsonl`
- `events\punct_<pattern_id>.nonmatching.jsonl`
- Markdown report: `C:\mrx_training_set\MB\reports\2026-05-11_punctuation_recon_v2.md`

---

## PHASE 4 — Lexical recon (THE BIG ONE)

### Why this is the headline phase

At 7 pairs, lexical was NOT READY — zero HIGH-confidence patterns. At 195 pairs, the lexical layer SHOULD cross HIGH-confidence. This is the run that produces it.

If the lexical layer doesn't cross HIGH at 195 pairs, that's a major finding — it means lexical patterns may be irreducibly case-specific, and the architecture needs to handle per-case calibration. Either way, we learn something definitive.

### Detection methodology

Lexical recon measures word-substitution patterns: places where the rough has word X and the final has word Y, with X != Y.

For each clean 1:1 substitution event, capture:

- Rough word(s)
- Final word(s)
- Surrounding context (500 chars before and after)
- Pair ID

Then bucket and count:

- By substitution type (your/you're, there/their, sound-alike, synonym, format change, etc.)
- By context (turn-internal, turn-opening, etc.)
- By frequency across pairs

### Excluded from this phase

- M:N substitutions (multi-word replacements). Yesterday's recon noted these as a separate larger signal. Continue to exclude. Note exclusions in the recon report — this is a backlog item, not a current measurement.
- Substitutions where the rough word is recognizably garbled steno (e.g., random letter sequences). Use the same garbled-filter logic from yesterday, but verify the regex bug Sonnet flagged is fixed before running.

### Pattern hypotheses to specifically test

From yesterday's near-misses:

- `lex_there_their` — there -> their (was 9 events at 4/7 depos)
- `lex_your_youre` — your -> you're (6 events at 4/7 depos)

Plus: bucket all sound-alike substitutions (homophones) and format-change substitutions (hyphenation, capitalization without case-change being the signal). At 195 pairs, sound-alike patterns may emerge as HIGH-confidence even if individual word pairs don't.

### Confidence threshold for "HIGH" at lexical scale

Lexical patterns are individually rarer than structural patterns. A "HIGH-confidence" lexical pattern might fire only 50-100 times across 195 pairs, whereas a HIGH-confidence punctuation pattern fires thousands of times.

Threshold proposal:

- HIGH: pattern fires in 80%+ of pairs where the trigger context appears
- MEDIUM: pattern fires in 60-80% of trigger contexts
- LOW: under 60%

This is different from the structural threshold. Document the difference in the pattern YAML's `confidence.current_lane_threshold_basis` field.

### Output per data architecture

- `patterns\lex_<pattern_id>.yaml` for each pattern that crosses MEDIUM or higher
- `events\lex_<pattern_id>.matching.jsonl`
- `events\lex_<pattern_id>.nonmatching.jsonl`
- Markdown report: `C:\mrx_training_set\MB\reports\2026-05-11_lexical_recon_v2.md`

The markdown report should clearly state:

- How many patterns crossed HIGH
- How many crossed MEDIUM
- The verdict for the layer overall: READY / MARGINAL / NOT READY at 195 pairs
- If NOT READY: what would change the verdict (more pairs? different methodology? per-case fingerprinting?)

---

## PHASE 5 — Manifest assembly

After all four phases complete, write the fingerprint manifest:

`C:\mrx_training_set\MB\fingerprint\manifest.yaml`

Per the schema in FINGERPRINT_DATA_ARCHITECTURE.md Section 1.3:

```yaml
fingerprint_version: "2026-05-11.v1"
cr_initials: "MB"
created: "<ISO timestamp at completion>"
created_by_recon_run: "recon_run_<timestamp>"
training_pair_count: <actual count after quarantine>
training_pair_date_range: ["<earliest>", "<latest>"]
test_pair_count: 48
test_pair_date_range: ["<earliest>", "<latest>"]
patterns_total: <count>
patterns_by_layer:
  splits: <count>
  capitalization: <count>
  punctuation: <count>
  lexical: <count>
patterns_by_confidence:
  AUTO: <count>     # >= 0.90
  SUGGEST: <count>  # 0.60 - 0.89
  FLAG: <count>     # < 0.60
  PROTECTED: 0      # not yet assigned this run
schema_version: "1.0"
```

---

## PHASE 6 — Provenance ledger

Per RULE-INPUT-IS-SACRED and the schema's P5:

Write to: `C:\mrx_training_set\MB\_provenance\recon_runs.jsonl`

```json
{"run_id": "recon_run_<timestamp>", "started_at": "<ISO>", "completed_at": "<ISO>", "training_pair_count": N, "patterns_produced": M, "scripts_run": [...], "script_hashes": {...}}
```

Snapshot every recon script used to: `C:\mrx_training_set\MB\_provenance\script_versions\<run_id>\`

This is the subpoena-defense ledger. Don't skip it.

---

## DELIVERABLES SUMMARY

### Local-only (NEVER push)

- `C:\mrx_training_set\MB\fingerprint\` — full filing cabinet (manifest, patterns, events, confidence history)
- `C:\mrx_training_set\MB\extracted\` — plain-text extractions
- `C:\mrx_training_set\MB\reports\2026-05-11_*` — full local reports per phase
- `C:\mrx_training_set\MB\_provenance\` — recon run log + script snapshots

### Public-pushable (after grep verification)

**mrx-context/reports/2026-05-11/overnight_recon_summary.md** — top-line summary

- Pair counts (training only, never test)
- Patterns per layer (count only, no witness names or case IDs)
- Verdict per layer (READY / MARGINAL / NOT READY)
- Layer-level confidence distribution
- Anomalies and quarantine count

**mrx-context/reports/2026-05-11/lexical_layer_verdict.md** — focused on the headline finding

- Did lexical cross HIGH at 195 pairs? Yes / No / Marginal
- If yes: how many patterns, brief categorization (no specific word pairs)
- If no: what would change the verdict

**mrx-context/handoffs/HANDOFF_SONNET_2026-05-10_overnight.md** — handoff for whoever picks up next

- State of the world at recon completion
- What was learned
- Open issues
- Next moves recommendation

### Sanitization checklist (before any push)

For each public file:

- Grep against `C:\mrx_training_set\MB\paired\MANIFEST.md` witness names
- Grep against any case ID format (date-prefixed strings like 032025olsen)
- Grep for absolute paths under `C:\Cat4\usr\scott`
- Grep for absolute paths under `C:\mrx_training_set\`

If grep finds anything: BLOCK push, log to chat, fix the file, re-grep, then push.

---

## WHAT TO REPORT IN CHAT WHEN DONE

Single message in chat with:

- Run completion status: SUCCESS / PARTIAL / FAILED
- Total wall-clock runtime
- Pre-flight: pairs loaded / extracted / quarantined
- Phase-by-phase: patterns produced + verdict per layer
- Headline: did lexical cross HIGH-confidence?
- Pushed files (with commit hashes)
- Anything weird worth flagging
- Energy level for handoff (clean tap-out vs degraded)

---

## RUNTIME EXPECTATIONS

Based on yesterday's 7-pair runtimes scaled to 195:

- Phase 0 (pre-flight + extraction): 30-60 minutes
- Phase 1 (splits): 60-90 minutes
- Phase 2 (capitalization): 60-90 minutes
- Phase 3 (punctuation): 90-120 minutes
- Phase 4 (lexical): 120-180 minutes (slowest layer, likely the bottleneck)
- Phase 5+6 (manifest + provenance): 15 minutes

Total: 6-9 hours wall-clock.

If any phase takes >2x estimate, pause and write status to a CHECKPOINT.md file. Don't burn through the night on a runaway script.

---

## WHAT TO DO IF SOMETHING'S WEIRD

- **Script crashes:** log to checkpoint file, attempt restart with same parameters, then move to next phase
- **Disk space issues:** stop, log, alert in chat
- **Cannot extract a pair:** log to extraction_log.jsonl, skip, continue
- **Pattern produces wildly different result vs 7-pair baseline (>50% deviation):** flag in markdown report, do not change confidence calculation methodology
- **Suspect data corruption:** STOP, do not push anything, write findings, leave for human review

---

## PRE-FLIGHT BUG CHECKS

Before kicking off, verify:

1. The garbled-filter regex bug Sonnet flagged in yesterday's recon (Appendix B2 of HANDOFF_SONNET_2026-05-09_evening.md) — has it been fixed in the active scripts? If not, fix it before running. If unsure, run a 5-pair test of just the lexical recon and verify counts are sane before scaling to 195.

2. The hardcoded MB paths in spot_check_v3.py (TD-003) — these are temp scripts and acceptable to use as-is for tonight, but production recons going forward need parameterization. Note in the handoff if you replicate the hardcoded pattern.

3. The 0525black_bp filename mismatch (hyphen vs underscore) flagged in inventory — verify the active recon scripts handle filename variation correctly.

---

## CODER MINDSET REMINDERS

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe -> STOP, flag, document, choose the safer path.

Three Brains check: Engineer (can?), Architect (should?), Owner (worth?).

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED. RULE-SPEC-BEFORE-BUILD.

You're alone overnight. No safety net of human review until morning. That means more conservative, not less. When in doubt, write a CHECKPOINT.md and stop. Better to have partial output Monday morning than full output that's wrong.

Slow is smooth. Smooth is fast.

---

— End of overnight recon spec —
