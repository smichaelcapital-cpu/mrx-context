# RECON — D-WRITER-FLAG-NOT-REWORD Pre-Spec
**Date:** 2026-05-04 Monday morning
**Analyst:** Claude Sonnet (mrx-context session)
**Scope:** Pre-spec recon of WRITER_PROMPT_V1 and validate_ops before speccing Option D.
**Files read:**
- `src/mrx_engine_v1/stage3/suggester.py` (full file; WRITER_PROMPT_V1 at lines 420–515)
- `src/mrx_engine_v1/stage3/validate_ops.py` (check_names at lines 248–323; main entry at 563–626)
**Sunday recon carried forward:**
- `reports/2026-05-03/writer_flag_not_reword_recon.md`
- `reports/2026-05-03/flag_op_downstream_recon.md`
**DO NOT SPEC. DO NOT CODE. Recon findings only.**

---

## 1. Where NAMES_LOCK Is Defined and How Writer Reads It

**Python side:**
`names_lock` is a `set` passed into `suggest_proposals()` at the top-level entry point
(`suggester.py:1014`). It flows into `_run_writer()` (`suggester.py:883`).

**Injection into Writer prompt** (`suggester.py:907–923`):
```python
if names_lock:
    names_lock_section = "# NAMES LOCK\n\n" + json.dumps(sorted(names_lock))
    # W&T form rule injected here when both "W&T" and "W&T Offshore" present
    parts.append(names_lock_section)
```
The Writer sees NAMES_LOCK as a sorted JSON array appended to its system prompt under
the header `# NAMES LOCK`. It is injected only when `names_lock` is a non-empty set.
If `names_lock` is empty or None, no NAMES_LOCK section appears — and `check_names`
in validate_ops will hard-reject any REWORD that runs (see §4 below).

**validate_ops side:**
`names_lock` is passed directly as a Python `Set[str]` to `validate_ops()` (`suggester.py:1075`)
and used in `check_names()` and `check_word_budget()`.

**Key fact:** The Writer's view of NAMES_LOCK (a JSON array in its system prompt) and
the validator's view (a Python set) are two separate copies derived from the same source
object. They should always be consistent.

---

## 2. Exact Wording of Rule 8 Today

From `WRITER_PROMPT_V1` (`suggester.py:468–477`):

```
8. Unknown names MUST produce a FLAG op:
   When the Reader flags an anomaly on a name (category=name_uncertain or
   context indicates a proper noun), and that name is NOT in NAMES_LOCK,
   you MUST produce a FLAG op for that anomaly_id. Going silent is FORBIDDEN.
   The FLAG op has after="" and reason="unknown name not in NAMES_LOCK —
   human review required."

   Critical: producing no op for a Reader anomaly is reserved ONLY for cases
   where the anomaly is a genuine Reader false positive (e.g., text is already
   correct). Even then, produce op_type="REJECT" with a reason. Silence is never the answer.
```

Rule 8's two trigger conditions, verbatim:
1. `category=name_uncertain` — explicit category match
2. `context indicates a proper noun` — vague; relies on Writer's judgment

---

## 3. Why Rule 8 Didn't Fire on Blocks 537/540

### Block 537 anomaly (from anomalies.jsonl):
```json
{
  "anomaly_id": "a_0012",
  "turn_idx": 2657,
  "token_span": [13, 16],
  "category": "steno_artifact",
  "reader_note": "'named from an Schneider' — 'from an' is likely a steno artifact; probable reading is 'named Fran Schneider' (Fran Schneider appears in dictionary). 'from an' makes no grammatical sense in this slot.",
  "confidence": "high"
}
```

### Writer proposal produced:
```json
{
  "op_type": "REWORD",
  "to": "named Fran Schneider",
  "source": "case_dict"
}
```

### Failure trace — three layers:

**Layer 1 (Data):** `dictionary.rtf` contains "Fran Schneider". Correct name is "Fran Snyder".
This seeded the Reader's note with the wrong name.

**Layer 2 (Reader):** Reader categorized the anomaly as `steno_artifact` instead of
`name_uncertain`. This bypassed Rule 8's first trigger. Reader's own Rule 8 (READER_PROMPT_V1,
line ~249) says: "if a token resembles a name in the dictionary or appears to be a proper
noun missing capitalization, flag name_uncertain." Reader violated its own rule by treating
the correction mechanism (steno split) as the controlling factor for category, rather than
the correction target (a proper noun).

**Layer 3 (Writer):** Rule 8's second trigger, "context indicates a proper noun," did not
fire despite the reader_note explicitly naming a person ("probable reading is 'named Fran
Schneider'"). The Writer treated this as a steno decompaction case (source=case_dict, high
confidence) and emitted REWORD.

**Layer 4 (validate_ops — new finding):** `check_names` in `validate_ops.py` also did not
catch this. See §4 for the detailed reason. The word_budget check DID reject the proposal
(3 output words vs. 4 input words = 75% < 80% WORD_BUDGET_HARD), but this rejection was
silent — MB received the uncorrected steno with zero review signal.

### Net result:
- REWORD was rejected by word_budget (not check_names)
- Rejection produced `outcome="word_preservation_rejected"` in the application map
- MB saw: `"...someone named from an Schneider in December of 2022, right?"` — raw steno, no FLAG marker

---

## 4. Contradiction Hunt Results (RULE-CONTRADICTION-HUNT)

Patterns searched across full `suggester.py`: `proper.?noun`, `name`, `NAMES_LOCK`, `dict`,
`case_dict`, `phonetic_match`. All hits read in context.

### Finding A — Rule 8 trigger gap (gap, not contradiction)

Rule 8 requires either `category=name_uncertain` OR `context indicates a proper noun`.
The second condition is underspecified. "Context indicates a proper noun" is not defined
in terms of concrete, checkable signals. The Writer has these signals available:
- `category` field
- `confidence` field
- `reader_note` free text
- Its own proposed `to` text
- NAMES_LOCK (system prompt)
- Case dictionary (system prompt)

None of these are named in Rule 8 as the evidence to check. The Writer resolved the
ambiguity in the wrong direction — it treated high confidence + steno category as
sufficient to override the proper-noun check.

**Verdict:** Gap in Rule 8's second trigger. No direct contradiction with other rules.

### Finding B — REJECT op type is a ghost (inconsistency)

Rule 8's note (`suggester.py:477`) says: "Even then, produce op_type='REJECT' with a
reason." But:
- `REJECT` does not appear in the schema example (`suggester.py:485–508`) — only REWORD
  and FLAG are shown
- `check_coverage` (`validate_ops.py:126`) only processes ops with
  `op_type in ("REWORD", "FLAG")` — REJECT ops are treated as `non_active`
- No downstream code in apply.py, Stage 5, or validate_ops handles REJECT explicitly
- A REJECT op passes all validation silently and then does nothing

**Verdict:** REJECT is an undocumented dead branch. If the Writer emits it, the span is
left verbatim with no review marker — same outcome as silence. This is the opposite of
what the prompt intends. Needs to be removed from Rule 8's text or formally defined.
(Recommend: remove the REJECT mention; replace with "FLAG with reason='Reader false
positive — text is already correct'")

### Finding C — check_names in validate_ops is narrower than the prompt implies (new finding)

`validate_ops.check_names` (`validate_ops.py:248–323`) is the code-level safety net for
proper nouns. Its trigger condition:

```python
TITLE_WORDS = re.compile(r'^(Mr|Mrs|Ms|Dr|Prof|Hon|Esq)\.?$', re.IGNORECASE)
# ... builds title_preceded set ...
if i not in title_preceded:
    continue  # SKIP — not after a title word
```

`check_names` only rejects a capitalized word in REWORD.to if it IMMEDIATELY FOLLOWS a
formal title word (Mr., Mrs., Ms., Dr., Prof., Hon., Esq.). It does NOT fire on names
introduced by non-title words like "named", "by", "called", "known as", "of", etc.

**Applied to blocks 537/540:**
- `to` = "named Fran Schneider"
- "named" → NOT a TITLE_WORD → prev_was_title = False
- "Fran" → NOT title_preceded → SKIP (line 311)
- "Schneider" → already capitalized in from_text ("named from an Schneider") →
  in from_caps → SKIP (line 309)
- Result: `check_names` returns `ValidationResult(True)` — PASSES

The code-level name guard is weaker than both the prompt and Rule 8 imply. It would
catch "Mr. Fran Schneider" but not "named Fran Schneider."

**Verdict:** Inconsistency between the scope of Rule 8 ("any proper noun not in
NAMES_LOCK") and the scope of check_names ("only names following formal title words").
This is not causing active bugs today beyond the known Fran Schneider case, but it means
the validator cannot be relied upon as a complete safety net for the new rule.

### Finding D — source=case_dict permits REWORD of proper nouns (gap)

Rule 3 (`suggester.py:444–451`) defines the closed source list:
```
raw_steno / case_dict / kb / names_lock / phonetic_match / house_style
```
No rule says: "if source=case_dict and proposed `to` introduces a proper noun not in
NAMES_LOCK, FLAG instead of REWORD." This is the missing guard that Option D would add.

The source list was designed for classification, not for triggering safety behavior.
`case_dict` and `phonetic_match` are qualitatively different from `names_lock` — they
are unverified sources — but the prompt treats all six identically in terms of
permissible ops.

**Verdict:** Gap. Option D closes this by adding source-conditional behavior to Rule 8.

### No outright contradictions found.

The existing rules are internally consistent. The problem is accumulated gaps:
- Rule 8 exists but its trigger is underspecified
- The validator's `check_names` covers less than Rule 8 implies
- REJECT is mentioned but inert
- No source-conditional rule distinguishes verified (names_lock) from unverified (case_dict) sources for proper nouns

---

## 5. Recommended Trigger Logic for Option D

### What the Writer has available to evaluate

At the moment of producing an op, the Writer knows:
1. `anomaly_id`, `category`, `confidence`, `reader_note` — from the AnomalyList
2. Its own proposed `to` text and `source` — self-generated
3. NAMES_LOCK — in its system prompt as a JSON array
4. The case dictionary — in its system prompt

It does NOT know: raw token text, exact capitalization of original tokens, phonetic distance.

### Reliable signal combination for Option D

The trigger should be mechanical — no judgment required. The most reliable combination:

> **Source signal:** `source` is `case_dict` OR `phonetic_match`
> (These are unverified sources. `names_lock` source already implies the name was verified.)
>
> **Proper noun signal:** The `reader_note` explicitly names a person or company as
> the proposed correction — i.e., the note contains a Title Case multi-word phrase
> introduced by language like "probable reading is", "likely", "per dictionary",
> "should be", etc. This is the clearest signal that the Writer is about to commit
> a specific named entity, not a generic decompaction.
>
> **NAMES_LOCK check:** The named person or company, or any component word of it
> that is capitalized (other than "the", "of", "and", etc.), is NOT in NAMES_LOCK.

When all three conditions are met: emit FLAG instead of REWORD.

### Draft Rule 8a wording (for spec to refine):

```
8a. Unverified-source proper-noun safety net:
    If you are about to emit a REWORD with source=case_dict OR
    source=phonetic_match, AND the reader_note names a specific person
    or company as the proposed correction (e.g., "probable reading is
    'Fran Schneider'", "likely 'W&T Offshore' per dictionary"), AND
    that name or any non-function component word of it is NOT in
    NAMES_LOCK — emit FLAG instead of REWORD.

    Reason field: "uncertain proper noun: candidate '[name]' not in
    NAMES_LOCK — verify spelling and add to NAMES_LOCK if correct."

    Rationale: case_dict and phonetic_match are unverified sources.
    Only NAMES_LOCK entries have been attorney-verified. When these
    sources propose a person or company name, you cannot confirm the
    spelling — FLAG and let MB confirm.

    This rule fires regardless of Reader category. Even if category
    is steno_artifact and confidence is high, a proper noun introduced
    via an unverified source must be held for human review.
```

### Why "reader_note names a person/company" is the right proper-noun signal

The Writer's `to` field is self-generated. Checking it for "new capitalized words not
in NAMES_LOCK" risks false positives on sentence-initial capitalization (the first word
of a proposed correction is always capitalized). Using the reader_note instead is more
reliable: when the Reader explicitly names a correction target ("probable reading is
'Fran Schneider'"), that is unambiguously a proper noun assertion — not sentence-initial
capitalization.

This also handles the steno_artifact bypass: in blocks 537/540, the reader_note said
"probable reading is 'named Fran Schneider'" — a clear proper noun nomination. Rule 8a
would have fired on that text regardless of category.

### False-FLAG rate assessment

From Sunday's recon (writer_flag_not_reword_recon.md §Q4): the case dictionary has
~116 entries including proper nouns like "Marshall Smith", "Jonathan Barrett",
"Harman Singh", "Rahul Bhasin", "Tim Morton", "Tom Easley" — none in NAMES_LOCK.

Any future REWORD sourced from case_dict where the reader_note names these people
would FLAG under Rule 8a. **This is correct behavior.** None of those names have been
attorney-verified. MB should confirm any name the engine introduces from an unverified
source.

Expected false-FLAG rate on a well-curated NAMES_LOCK: near-zero, because common names
should be in NAMES_LOCK. Expected false-FLAG rate on a sparse NAMES_LOCK (like the
current halprin_full 15-entry list): moderate — but each FLAG is a legitimate deferral,
not a false positive. The fix for high FLAG rates is populating NAMES_LOCK, not loosening
the rule.

---

## 6. Complementary Fixes (Out of Scope for This Spec)

These are NOT part of Option D. Logged here for Opus's queue.

### 6a. Reader-side fix (defense in depth)
READER_PROMPT_V1, Rule 8 (~line 258): "if a token resembles a name in the dictionary
or appears to be a proper noun missing capitalization, flag name_uncertain."

Add explicit carve-out: "When the steno mechanism is a split or decompaction BUT the
correction produces a personal name or company name, use category=`name_uncertain`,
NOT `steno_artifact`. The steno mechanism explains how the error occurred; the category
must reflect that the correction is a proper noun."

This fixes Layer 2 independently of the Writer fix. Defense in depth — both can coexist.

### 6b. validate_ops check_names expansion
Expand `TITLE_WORDS` pattern to include non-formal person-name introducers: "named",
"called", "by", "for", "of", "known" (as title-word-equivalents for the check_names
heuristic). This would make the validator catch more proper-noun REWORDs not after
formal titles. Lower priority than the Writer prompt fix because: (1) prompt fix prevents
the REWORD from being emitted in the first place, (2) this requires code changes with
potential false-positive risk.

### 6c. REJECT op cleanup
Remove `op_type="REJECT"` from Rule 8's note or define it formally. Current state:
mentioned in the prompt, silently inert in the validator, not in the schema example.
If Writer emits REJECT, the span is left verbatim with no review marker — same as
silence, which Rule 8 explicitly forbids. Either: (a) define REJECT as equivalent to
FLAG with reason="Reader false positive" and add it to the schema, or (b) remove the
mention and say "FLAG with reason='Reader false positive — text is already correct'".

---

## 7. Summary for Spec

| Item | Finding | Action for spec |
|------|---------|----------------|
| NAMES_LOCK location | Sorted JSON array in Writer system prompt; Python set in validator; both from same source | No change needed |
| Rule 8 wording | Exists at lines 468–477; two triggers: category=name_uncertain OR "context indicates proper noun" | Tighten with Rule 8a |
| Why Rule 8 didn't fire | category=steno_artifact bypassed trigger 1; "context indicates proper noun" too vague for trigger 2 | Rule 8a fixes both by adding source-conditional trigger independent of category |
| check_names gap | Only catches names after formal title words (Mr./Dr.); misses "named X", "by X", etc. | Option D in prompt prevents the REWORD from being emitted; validator gap is secondary |
| REJECT dead branch | Mentioned in Rule 8, inert in code, absent from schema | Out of scope for this spec; note for cleanup |
| Option D trigger | source=(case_dict OR phonetic_match) AND reader_note names a person/company AND name not in NAMES_LOCK | Ready to spec |
| FLAG downstream | Confirmed live (762 items in halprin_full); bypasses word_preservation; reaches MB in OUR_FINAL.txt and review_queue.json | No downstream changes needed |

**Edit target for spec:** `WRITER_PROMPT_V1` in
`src/mrx_engine_v1/stage3/suggester.py`, insert Rule 8a between Rule 8 (line 477)
and Rule 9 (line 479). No changes to Python code, validate_ops, apply.py, or Stage 5.

**Spec is unblocked.** Ready for Opus to design and Sonnet to build.
