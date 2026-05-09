# FINGERPRINT v0 — SPEC

**Date:** 2026-05-09
**Author:** Opus
**For:** Sonnet to build, Scott to approve
**Status:** DRAFT — awaiting Scott's review

---

## NORTH STAR

Build the first real fingerprint enforcement loop. One rule. End-to-end. Prove the wiring works. Then expand.

The one rule for v0: **MB never injects double-hyphen em-dashes.** If the engine is about to write `--` to OUR_FINAL.txt for an MB depo, it must not.

Everything else (Identity, full Translation Artifacts, Lexical Preferences, etc.) gets *defined* in the YAML but is not yet *enforced*. v0 proves the loop. v1+ adds more rules.

---

## THE FOUR TOLLGATES

The fingerprint subsystem is four checkpoints. Each has a contract.

### Gate 1 — Fingerprint Files (YAMLs on disk)

**Required input:** Human edits (Scott + Opus). One YAML per layer.

**Expected output:** Well-formed YAML files at:
- `mrx-context/fingerprints/_template.yaml` (the universal shape)
- `mrx-context/fingerprints/reporters/MB.yaml` (MB's overrides)
- (jurisdictions/ and case_types/ remain empty for v0)

**Acceptance criteria:**
- Files parse as valid YAML (no syntax errors)
- MB.yaml conforms to the shape declared in `_template.yaml`
- Every section is split into `observed:` (facts) and `inferred:` (rules)
- A schema validator (Sonnet writes a small Python script) confirms structure

**Failure modes:**
- Malformed YAML → loader refuses to start, raises clear error
- Missing required field → loader refuses, names the missing field
- `inferred` rule with no `observed` evidence → loader logs a warning but proceeds

---

### Gate 2 — Fingerprint Loader (Python module)

**Required input:** A depo's metadata: `{jurisdiction, case_type, reporter}`. For Halprin: `{jurisdiction: "LA", case_type: "civil_engineering", reporter: "MB"}`.

**Expected output:** A composed fingerprint object — a Python dict (or dataclass) holding the merged rules from all four layers. For v0, only the `reporter` layer is populated; the others are empty stubs.

**Acceptance criteria:**
- Loader is a standalone module: `src/mrx_engine_v1/fingerprint/loader.py`
- Function signature: `load_fingerprint(jurisdiction, case_type, reporter) -> Fingerprint`
- Reads YAMLs from a configurable path (defaults to `mrx-context/fingerprints/`)
- Tested: 100% line coverage on the loader module, no exceptions
- Tests cover: happy path, missing reporter file, malformed YAML, empty layers

**Failure modes:**
- Reporter file missing → raise `FingerprintNotFoundError` with the path it tried
- YAML malformed → raise `FingerprintParseError` with the line number
- Required field missing → raise `FingerprintSchemaError` with the field name

**No silent failures.** Ever.

---

### Gate 3 — Composed Fingerprint (in-memory object)

**Required input:** Output of Gate 2.

**Expected output:** An immutable object that the engine queries. v0 supports one query:
```
fingerprint.is_forbidden_token(token: str) -> bool
```
For MB v0, `fingerprint.is_forbidden_token("--")` returns `True`. Everything else returns `False`.

**Acceptance criteria:**
- The object is read-only after construction (no mutation)
- `is_forbidden_token()` is the only enforcement method in v0
- Tested: returns `True` for `--`, `False` for normal tokens

**Failure modes:**
- Caller mutates the object → raises (immutable by design)
- Caller queries an unsupported method → raises `NotImplementedError` with what's planned

---

### Gate 4 — Engine Consumer (assemble_final.py)

**Required input:** Composed fingerprint object + existing pipeline JSONs.

**Expected output:** OUR_FINAL.txt with no `--` tokens (for MB depos).

**Acceptance criteria:**
- `assemble_final.py` accepts a `fingerprint` parameter
- If `fingerprint=None`, behavior is unchanged (backward compatible)
- If `fingerprint` is provided, every token about to be written is checked against `fingerprint.is_forbidden_token()`
- If forbidden: token is dropped, the drop is logged to a new file `fingerprint_enforcement.jsonl`
- Every drop logs: turn_idx, token, reason, source_proposal_id (if applicable)
- Tested: an integration test that feeds a fake proposal containing `--` and proves the output doesn't have it

**Failure modes:**
- `fingerprint_enforcement.jsonl` is mandatory output. If we can't write to it, fail loudly. No silent enforcement.
- If a forbidden token is dropped but its removal would corrupt the turn (e.g., leave dangling whitespace), log the drop but also log a `requires_review` flag for MB.

---

## THE FILE SHAPES

### `_template.yaml` (universal shape)

This file documents the structure every fingerprint must follow. It's a self-documenting reference. All six layers appear, with comments. Layers 4-6 are stubbed for v0.

```yaml
# CR-agnostic fingerprint template.
# Defines all fields any CR fingerprint must populate.
# Each section has TWO subsections: observed (facts) and inferred (rules).

# -----------------------------------------------------------------------
# LAYER 1 — IDENTITY
# Operational metadata about the reporter. Not just demographics —
# context that affects how their rough transcripts behave.
# -----------------------------------------------------------------------
identity:
  observed:
    reporter_id:           # e.g., "mb_louisiana_001"
    jurisdiction:          # e.g., "LA"
    cat_software:          # e.g., "CaseCATalyst"
    realtime_writer:       # bool
    years_experience:      # int
    uses_scopist:          # bool
    uses_proofreader:      # bool
  inferred:
    style_guides:          # list, e.g., ["NCRA", "Louisiana custom"]

# -----------------------------------------------------------------------
# LAYER 2 — TRANSLATION ARTIFACTS
# Deterministic machine defects. Steno output, software quirks.
# These are facts — corrections that are mechanically right.
# -----------------------------------------------------------------------
translation_artifacts:
  observed:
    literal_leaks: []      # list of {pattern, raw_count, final_form}
    malformed_briefs: []   # list of {raw, final, occurrences}
    audio_placeholders: [] # list of {token, meaning, never_autocorrect}
    colloquy_repairs: []   # list of {raw, final}
    filler_artifacts: []   # list of {raw, final}
  inferred:
    correction_strategies: []  # list of typed strategies

# -----------------------------------------------------------------------
# LAYER 3 — STRUCTURAL FORMATTING
# Q/A behavior, paragraphing, punctuation, capitalization habits.
# -----------------------------------------------------------------------
structural_formatting:
  observed:
    em_dash_count_in_raw:   # int. For MB this is 0.
    em_dash_count_in_final: # int. For MB this is 0.
    qa_continuation_q_freq: # float
    qa_continuation_a_freq: # float
  inferred:
    forbidden_tokens: []   # list. For MB v0: ["--"]
    # ^^^ THIS IS THE ONLY v0 ENFORCED FIELD ^^^

# -----------------------------------------------------------------------
# LAYER 4 — LEXICAL PREFERENCES (DEFINED, NOT ENFORCED IN v0)
# -----------------------------------------------------------------------
lexical_preferences:
  observed: {}
  inferred: {}

# -----------------------------------------------------------------------
# LAYER 5 — RISK & REVIEW (DEFINED, NOT ENFORCED IN v0)
# -----------------------------------------------------------------------
risk_and_review:
  observed: {}
  inferred: {}

# -----------------------------------------------------------------------
# LAYER 6 — DRIFT (DEFINED, NOT ENFORCED IN v0)
# -----------------------------------------------------------------------
drift:
  observed: {}
  inferred: {}
```

### `MB.yaml` (v0 — only what we know)

Only fields where we have observed evidence. No speculation.

```yaml
identity:
  observed:
    reporter_id: mb_louisiana_001
    jurisdiction: LA
    cat_software: CaseCATalyst
    realtime_writer: true   # tentative — confirm with Scott
    years_experience: null  # unknown
    uses_scopist: false     # tentative
    uses_proofreader: true  # tentative
  inferred:
    style_guides:
      - NCRA
      - Louisiana custom

translation_artifacts:
  observed:
    literal_leaks: []
    malformed_briefs: []
    audio_placeholders: []
    colloquy_repairs: []
    filler_artifacts: []
  inferred:
    correction_strategies: []

structural_formatting:
  observed:
    em_dash_count_in_raw: 0
    em_dash_count_in_final: 0
    sample_size_depos: 6
    confidence: 0.97
  inferred:
    forbidden_tokens:
      - "--"

lexical_preferences:
  observed: {}
  inferred: {}

risk_and_review:
  observed: {}
  inferred: {}

drift:
  observed: {}
  inferred: {}
```

---

## THE LOADER MODULE — DETAILED

**Location:** `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\mrx_engine_v1\fingerprint\loader.py`

**Public API:**
```python
def load_fingerprint(
    jurisdiction: str,
    case_type: str,
    reporter: str,
    fingerprint_root: Path = DEFAULT_ROOT,
) -> Fingerprint:
    """Load and compose the four-layer fingerprint stack."""
```

**Behavior:**
1. Load `reporters/{reporter}.yaml` — required, raise if missing
2. Load `jurisdictions/{jurisdiction}.yaml` — optional, empty if missing
3. Load `case_types/{case_type}.yaml` — optional, empty if missing
4. Load `_universal.yaml` — optional, empty if missing
5. Merge in stack order: universal → jurisdiction → case_type → reporter (later layers override earlier)
6. Validate the merged result against the schema
7. Return immutable `Fingerprint` object

**Tests required (minimum 6):**
1. Happy path — MB.yaml loads correctly
2. Missing reporter file — raises `FingerprintNotFoundError`
3. Malformed YAML — raises `FingerprintParseError`
4. Empty jurisdictions/case_types files — loads fine, missing layers default to empty
5. `is_forbidden_token("--")` returns `True` for MB
6. `is_forbidden_token("hello")` returns `False` for MB

---

## ENGINE WIRING — DETAILED

**File touched:** `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\assemble_final.py`

**Change scope:** Minimal. Add an optional `fingerprint` parameter to `assemble_final()`. If provided, before writing each token to OUR_FINAL.txt, check `fingerprint.is_forbidden_token(token)`. If True, drop the token and log to `fingerprint_enforcement.jsonl`.

**Backward compatibility:** If `fingerprint=None`, behavior is identical to today. No existing tests break.

**New output file:** `io/analysis/halprin_mini/_stage5_out/fingerprint_enforcement.jsonl`. One JSON line per drop:
```json
{"turn_idx": 124, "token": "--", "reason": "forbidden_token", "rule_source": "MB.structural_formatting.inferred.forbidden_tokens"}
```

---

## ACCEPTANCE TEST — END-TO-END

**The proof v0 works:**

1. Sonnet writes MB.yaml with `forbidden_tokens: ["--"]`
2. Sonnet writes the loader, all 6 unit tests pass
3. Sonnet wires `assemble_final.py` with the optional fingerprint parameter
4. Sonnet writes an integration test that:
   - Constructs a fake proposal that would inject `--` into a turn
   - Runs `assemble_final` with the MB fingerprint
   - Asserts the OUR_FINAL.txt output contains zero `--` tokens
   - Asserts `fingerprint_enforcement.jsonl` has one entry for the dropped token
5. Sonnet runs the full halprin_mini pipeline end-to-end with the fingerprint enabled
6. Diff the new OUR_FINAL.txt against the previous one. Every diff should be a removed `--`. Nothing else.

**If step 6 produces unexpected diffs, v0 fails. Stop. Investigate.**

---

## OUT OF SCOPE FOR v0

- Layers 4, 5, 6 (defined as empty stubs only)
- Jurisdiction and case_type layer files (the merger handles their absence)
- Drift detection
- Multiple enforcement rules (one rule, period)
- Any fingerprint editing UI
- Auto-learning from FINAL files
- Removing existing Reader/Writer prompt rules about em-dashes (those stay; this is belt-and-suspenders for v0)

---

## RISKS

1. **The forbidden token check might break legitimate `--` use cases.** v0 only runs on MB depos and MB never uses `--`. But: confirm with Scott before shipping that no other reporter-agnostic use of `--` exists in the pipeline output.

2. **Backward compatibility.** Existing tests must still pass with `fingerprint=None`. Sonnet must run the full test suite before declaring done.

3. **Double-enforcement.** If the Reader/Writer prompts also remove `--`, the fingerprint enforcement might never fire on real data. That's fine — the integration test injects a synthetic `--` to prove the wiring works, separate from the production loop.

---

## COMMIT PREFIXES (per RULE_SHEET_v1)

- `universal: feat(fingerprint): add four-layer loader module`
- `mb-specific: feat(fingerprint): add MB.yaml v0 with em-dash forbidden token rule`
- `universal: feat(stage5): wire optional fingerprint parameter into assemble_final`

---

## THREE BRAINS CHECK

- 🔧 **Engineer:** Can we build it? Yes. Standard YAML loader + dict merge + token filter. ~200 lines of code, ~150 lines of tests.
- 🏗️ **Architect:** Should we build it? Yes. This is the wedge. Every CR after MB onboards faster.
- 💰 **Owner:** Worth it? Yes. v0 ships in one Sonnet session. Proves the architecture. Kills one known hallucination class for MB. Lays groundwork for the 49.5% → 60-65% Brandl ceiling lift.

---

## ACCURACY CHECK (Prime Directive)

*"Could this reduce transcript accuracy or credibility?"*

**Answer: No.** The only behavior change is removing `--` tokens for MB. MB never uses `--`. Therefore removing `--` for MB cannot reduce her transcript's fidelity to her style. The change *increases* fidelity.

**Edge case:** If MB ever did use `--` (which we have not observed), the fingerprint would silently strip it. Mitigation: every drop is logged to `fingerprint_enforcement.jsonl`. MB can review.

---

*End of spec.*
