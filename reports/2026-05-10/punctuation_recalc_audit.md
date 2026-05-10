# Punctuation Post-Run Confidence Recalculation Audit (TD-004)

**Date:** 2026-05-10 (audited evening session)
**Auditor:** Sonnet (evening instance)
**Status:** COMPLETE — ready for Scott review, no commits made
**Report path:** C:\Users\scott\OneDrive\Documents\mrx-context\reports\2026-05-10\punctuation_recalc_audit.md

---

## 1. Headline

**2 of the 6 recalculated patterns are clean. 3 need Scott's judgment. 1 should revert to FLAG.**

The two stage-direction patterns (`?(` and `.(`) used pairs_coverage for the right reason — those patterns are presence-per-depo habits, not per-turn habits, and the metric fits. They are GREEN.

The comma, em-dash, and quote patterns used pairs_coverage for a weaker reason — "does this depo have any commas/dashes/quotes?" which is almost always true and doesn't prove MB added them. They are YELLOW. The underlying habit is real (7-pair evidence exists), but the current measurement doesn't prove it at 186-pair scale.

The hyphen pattern is RED. The events contain steno phonetic name spellings ("H-o-r-e-c-k-y", "D-o-u-r-e-s-s-e-a-u-x") that match the regex but are not MB's hyphenation habit. pairs_coverage = 1.0 here is trivially true and noise-contaminated. It should revert to FLAG.

**Recommendation:** Keep 2 AUTO (stage-direction). Flag 3 for Scott (comma, emdash, quote). Revert 1 to FLAG (hyphen). Net result if Scott agrees with all: 18 AUTO patterns (down from 19).

---

## 2. The Recalculation Methodology — Plain English

Here is what happened, step by step.

**Step 1 — Phase 3 ran and wrote all 9 patterns using ratio as confidence.**

Ratio = (turns matching the pattern) ÷ (all turns measured). The script wrote this as `conf = ratio` for every punctuation pattern without exception.

**Step 2 — Four minutes later, a batch correction updated 6 of the 9 patterns.**

The confidence history files show a `confidence_correction` event at 13:59:06, exactly 4 minutes after the initial `initial_measurement` at 13:55:17. All 6 corrections share the same timestamp, meaning they were done as a single batch operation.

**Step 3 — The correction changed the metric from ratio to pairs_coverage.**

pairs_coverage = (number of training pairs that had at least one matching event) ÷ (total training pairs). For example: if 174 of 186 depos had at least one `?(` event, pairs_coverage = 0.9355.

**Step 4 — Phase 5 (manifest) did not do the recalculation.**

Phase 5 reads the YAML files as-is. It has no recalculation logic. The correction happened between phase 3 and phase 5 via direct YAML edits by the overnight Sonnet.

**Why the overnight Sonnet made this change:**

The rationale logged in the YAML files reads: "Pattern fires rarely per turn but appears in nearly all pairs. Confidence = pairs_observed / pairs_total."

That rationale is correct for the stage-direction patterns. It is partially correct for the others. The issue (detailed per-pattern below) is that "appears in nearly all pairs" and "MB has a habit of adding this" are two different claims, and the measurement can only confirm the first one.

**What the spec said about confidence metrics:**

The overnight recon spec did NOT specify which confidence metric to use for different pattern types. The spec called out that stage-direction patterns require content_match detection (not gap_alignment), but was silent on confidence calculation. The metric switch was a judgment call made during the run, not a pre-authorized decision.

---

## 3. Pattern-by-Pattern Table

| Pattern | Initial ratio | Initial lane | pairs_coverage | Recalc lane | Verdict |
|---|---|---|---|---|---|
| `punct_stage_direction_question` | 0.0112 (1.1%) | FLAG | 0.9355 (174/186) | AUTO | GREEN |
| `punct_stage_direction_period` | 0.0115 (1.2%) | FLAG | 0.9946 (185/186) | AUTO | GREEN |
| `punct_comma_addition` | 0.3314 (33.1%) | FLAG | 1.0000 (186/186) | AUTO | YELLOW |
| `punct_emdash_addition` | 0.1166 (11.7%) | FLAG | 1.0000 (186/186) | AUTO | YELLOW |
| `punct_quote_addition` | 0.0194 (1.9%) | FLAG | 0.9892 (184/186) | AUTO | YELLOW |
| `punct_hyphen_addition` | 0.0550 (5.5%) | FLAG | 1.0000 (186/186) | AUTO | RED |

**Verdicts explained in plain English:**

- **GREEN** = The recalculation was legitimate. Keep AUTO.
- **YELLOW** = The recalculation is defensible but not airtight. Real habit, unproven measurement. Scott decides.
- **RED** = The measurement is counting the wrong things. Revert to FLAG. Do not present to MB as AUTO.

---

## 4. Spot-Check Evidence

### Spot-check A: `punct_stage_direction_question` — 10 matching events verified

Opened `events\punct_stage_direction_question.matching.jsonl`. First 10 events, all from `training_092625williams`:

Every event is a real `? (` pattern where MB placed a question mark at the end of a Q turn immediately before a parenthetical stage direction:

- "...prepare for your deposition? **(Whereupon, Exhibit No. 1**, was marked for Identification.)"
- "...Are you able to see that? **(Witness peruses document.)**"
- "...Have you ever read the lawsuit that was filed on your behalf? **(Whereupon, Exhibit No. 2**, was marked for Identification.) (Witness peruses document.)"
- "...Do you see that? **(Witness peruses document.)**"
- "...Who is Irene Smith? **(Whereupon, Exhibit No. 5**, was marked for Identification.)"

**Conclusion:** 10/10 events are genuine. pairs_coverage = 93.5% is a real measurement of a real habit. GREEN confirmed.

### Spot-check B: `punct_hyphen_addition` — 20 matching events examined

Opened `events\punct_hyphen_addition.matching.jsonl`. First 20 events from `training_092625williams` fall into four categories:

**Category 1 — Phonetic name spellings (NOT MB's addition habit):**
- `"A. 244 south Horecky Street. Horecky is H-o-r-e-c-k-y..."` — the regex matches `H-o` inside the spelled-out name
- `"A. Douresseaux, D-o-u-r-e-s-s-e-a-u-x."` — the regex matches `D-o` inside the phonetic spelling
- `"A. Bonjour. B-o-n-j-o-u-r."` — same issue
- `"Q. Do you remember a Dr. Darren Strother, S-t-r-o-t-h-e-r?"` — same issue

These are court reporter phonetic spellings of proper nouns. The hyphens are steno convention, not MB's compound-word addition habit. They would appear in any court reporter's work. The regex `\b\w+-\w+\b` matches them because it finds the first `single_char-single_char` sequence inside the spelled name.

**Category 2 — Proper nouns (likely already in rough):**
- `"Penn-American Insurance Company"` — company name, would be in rough as-is
- `"Piggly-Wiggly"` — store name, same

**Category 3 — Compound words/adjectives (could be MB additions):**
- `"ex-husband"`, `"part-time"`, `"on-the-job"`, `"work-related"`, `"right-hand"`, `"five-minute"`, `"computer-generated"`, `"set-aside"`, `"flip-flops"`, `"Uh-huh"`

Of 20 events examined: ~6 are phonetic name spellings (clearly not MB habit), ~2 are proper nouns (unknown), ~12 are compound words that might be additions.

**This means roughly 30% of matched events in this depo are noise.** The measurement cannot be cleaned up without rough→final alignment to confirm which hyphens MB actually added.

**Conclusion:** pairs_coverage = 1.0 here is meaningless as a measure of MB's hyphenation habit. Any deposition transcript in English will have hyphenated words. The regex also captures phonetic name spellings. RED confirmed.

---

## 5. Cross-Check Against the Overnight Recon Spec

The overnight recon spec (`2026-05-10_OVERNIGHT_RECON_SPEC.md`) specified:

> **Phase 3 — Punctuation**: Confirms punctuation transformations (period, comma, em-dash additions) and stage-direction parenthetical patterns using content-matching rather than gap-alignment methods where word differences prevent sequence comparison.

**What the spec specified:**
- Stage-direction patterns: use content_match (not gap_alignment). ✓ Done correctly.
- Period, comma, em-dash: measured as occurrence proxies in final, direct alignment deferred. ✓ Done correctly.
- Confidence metric: **not specified**. The spec was silent on ratio vs pairs_coverage.

**Where the recalculation diverged from the spec:**

The spec did not authorize or specify the post-run confidence correction. The correction was a judgment call made during the run. It is documented in the confidence history files but was not pre-authorized.

**The manifest notes undersell what actually happened:**

The manifest notes read: "Punctuation stage-direction patterns: confidence corrected to pairs_coverage (initial run used occurrence ratio; corrected post-run)."

That note only mentions stage-direction patterns. In reality, 4 additional patterns (comma, emdash, quote, hyphen) were also corrected to pairs_coverage. The manifest does not reflect this. This is an inconsistency between the note and the actual YAML files.

---

## 6. Rollup — Final AUTO Count After This Audit

**Current state:** 19 AUTO patterns total (10 splits + 1 cap_sentence_start + 8 punct AUTO)

**Punctuation AUTO breakdown:**
- 3 never recalculated (stayed ratio-based): period_addition (0.93), double_period_cleanup (0.996), question_mark_addition is SUGGEST at 0.78
- 6 recalculated: 2 GREEN, 3 YELLOW, 1 RED

**If RED revert is applied (hyphen → FLAG):**
Punctuation AUTO drops from 8 to 7. Total AUTO: **18**.

**If Scott also pulls the 3 YELLOWs back to SUGGEST pending proper gap-alignment measurement:**
Punctuation AUTO drops from 8 to 4. Total AUTO: **15**.

The 10 splits patterns and cap_sentence_start are not affected by this audit.

---

## 7. Recommendations

**GREEN — No action needed:**

| Pattern | Keep as | Reason |
|---|---|---|
| `punct_stage_direction_question` | AUTO (0.9355) | pairs_coverage is correct metric; 10/10 events verified real |
| `punct_stage_direction_period` | AUTO (0.9946) | Same. 185/186 pairs = nearly universal |

**YELLOW — Scott's call. Options: keep AUTO, drop to SUGGEST, or defer to next recon:**

| Pattern | Current | Underlying habit strength | Issue |
|---|---|---|---|
| `punct_comma_addition` | AUTO (1.0) | Real (7-pair: 2,515 additions) | pairs_coverage=1.0 is trivially true for any English doc |
| `punct_emdash_addition` | AUTO (1.0) | Real (7-pair: 651 additions) | pairs_coverage=1.0 doesn't prove addition vs presence |
| `punct_quote_addition` | AUTO (0.99) | Real (7-pair: 148 additions) | pairs_coverage doesn't prove addition |

Suggested path for YELLOW patterns: label as SUGGEST (not FLAG, not AUTO) until Phase 3 v3 runs gap-alignment after TD-001 steno filtering is fixed. The habit is real; the measurement is just a proxy.

**RED — Recommend revert to FLAG. Do NOT present to MB as AUTO:**

| Pattern | Current | Should be | Reason |
|---|---|---|---|
| `punct_hyphen_addition` | AUTO (1.0) | FLAG | Matching events contain phonetic name spellings (not MB habit). pairs_coverage=1.0 trivially true. Only 50 events in 7-pair baseline. |

To revert `punct_hyphen_addition`:
- File: `C:\mrx_training_set\MB\fingerprint\patterns\punct_hyphen_addition.yaml`
- Change `confidence.current` from `1.0` to `0.055`
- Change `confidence.current_lane` from `AUTO` to `FLAG`
- Change `confidence.current_lane_threshold_basis` from `pairs_coverage` to `ratio`
- Remove the `note` field added by the recalculation
- Append a `confidence_correction` entry to `confidence_history\punct_hyphen_addition.history.jsonl`

**Do NOT execute this revert.** Scott decides.

---

## Notes on What Was NOT Changed

This audit is read-only. No YAML files were edited. No scripts were run. No commits were made. The confidence history files were read but not modified.

The three non-recalculated patterns (`punct_period_addition`, `punct_question_mark_addition`, `punct_double_period_cleanup`) were reviewed and are not part of this audit. Their ratio-based confidence values are correct — they are per-turn habits where ratio is the right metric.

---

— End of TD-004 Punctuation Recalc Audit —
