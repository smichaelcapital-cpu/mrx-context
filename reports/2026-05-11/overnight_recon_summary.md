# MB Fingerprint Recon — Overnight Run 2026-05-10

**Date:** 2026-05-10 (overnight)
**Run type:** Full fingerprint recon — all four layers
**Status:** COMPLETE (Phase 0–6)

---

## Pre-flight

| Metric | Value |
|---|---|
| Training pairs loaded | 195 |
| Pairs extracted (both rough + final ok) | 195 |
| Pairs quarantined (quality issues) | 9 |
| Pairs used for full recon | 186 |
| Test pairs (sacred, never touched) | 48 |

Quarantine reasons: 3 short-rough (non-testimony transcripts), 4 ratio out of range (steno anomalies), 2 zero-turn finals (no Q./A. content).

Pre-flight: **CLEAN**. All integrity checks passed.

---

## Patterns Produced

| Layer | Patterns | AUTO | SUGGEST | FLAG |
|---|---|---|---|---|
| Splits | 14 | 10 | 2 | 2 |
| Capitalization | 2 | 1 | 0 | 1 |
| Punctuation | 9 | 8 | 1 | 0 |
| Lexical | 3 | 0 | 0 | 3 |
| **TOTAL** | **28** | **19** | **3** | **6** |

Fingerprint version: `2026-05-11.v1`

---

## Layer Verdicts

### Splits — READY

14 patterns measured. 10 AUTO. 5 previously-known patterns confirmed, 7 new patterns discovered in the sweep.

Key findings:
- Top Q openers: "Okay" (18.5% of Q turns), "And" (12.1%), "So" (5.5%), "But" (0.97%)
- Top A starters: "Yes" (15.2%), "No" (12.0%), "Uhmm" (5.0%), "Yeah" (3.1%)
- Double-dash interruption: present in 96.2% of pairs
- `trailing_huh` and `now_q_opener` demoted from HIGH to FLAG: were overrepresented in the original 7-pair sample

### Capitalization — PARTIAL

2 patterns measured.
- `cap_sentence_start`: AUTO (98.77% ratio) — near-universal
- `cap_objection_midturn`: FLAG (17/186 pairs = 9.1%) — rare at 186-pair scale vs 5/7 pairs at 7-pair scale. Original sample was biased toward litigation depositions with active objection practice.

### Punctuation — READY

9 patterns measured. 8 AUTO (after confidence correction to pairs_coverage for occurrence-based patterns).

Key findings:
- Turn-end period: 93% of A turns end with period → AUTO
- Stage-direction `?(` pattern: 93.5% pairs coverage → AUTO (corr.)
- Stage-direction `.(` pattern: 99.5% pairs coverage → AUTO (corr.)
- Em-dash in turns: 100% pairs coverage → AUTO (corr.)
- Comma usage: 100% pairs coverage → AUTO (corr.)
- Question mark at Q-turn end: 77.9% → SUGGEST

Note: addition patterns (period, comma, em-dash) measured as occurrence proxies (content_match on final), not rough→final deltas. Gap alignment deferred — rough extraction v2 includes steno dictionary entries requiring filtering before alignment is reliable. Accuracy of these measurements is directionally valid but not additive-delta precise.

### Lexical — NOT READY

0 AUTO, 0 SUGGEST patterns. Verdict: **NOT_READY**.

Root cause: v2 rough extraction concatenates all text-bearing lines from the sgngl binary, including steno dictionary entries. The entries appear as doubled-word artifacts ("pastorpastor", "panepain") that dominate the SequenceMatcher substitution output. Real lexical substitutions (there→their, your→you're) are present but buried in noise (3-4 events per pair vs ~25 total artifacts per pair).

What would change the verdict:
1. Implement steno-code-filtered rough extraction: strip lines that are steno dictionary entries (recognizable by the doubled-word pattern or by matching steno code format) before alignment
2. Alternatively: use only the Q./A. portion of the rough (requires parsing the sgngl differently to isolate transcript lines)
3. Target coverage: if there→their or your→you're patterns appear in 60%+ of pairs at sufficient event count, that alone would cross SUGGEST

This is the top action item for the next recon run.

---

## Anomalies and Deviations

1. **trailing_huh and now_q_opener**: Both demoted from HIGH (6/7 at 7-pair scale) to FLAG (29.6% and 49.5% at 186 pairs). The original 7 pairs likely included attorney-specific depositions where these patterns were common. At 186-pair scale across many attorneys, they're minority patterns.

2. **Punctuation confidence correction**: Initial Phase 3 run used occurrence ratio as confidence for all punct patterns (e.g., stage-direction patterns got ratio=1.1% → FLAG even though they fire in 93%+ of pairs). Corrected post-run to pairs_coverage for patterns where the appropriate denominator is "pairs where the context appears," not "all turns."

3. **cap_objection_midturn low coverage**: 56 events in 17/186 pairs. Original 7 pairs were litigation-heavy (more objections). At 186-pair scale with mixed case types, mid-turn objections are rare.

4. **Lexical NOT_READY**: Expected to cross HIGH at 195 pairs. Blocked by v2 rough extraction quality. Architectural fix required (steno code stripping), not more data.

---

## Next Actions

1. **Immediate (next recon run)**: Implement steno-code-filtered rough extraction. Test on 5 pairs. If there→their crosses 30%+ pairs coverage, lexical is unblocked.
2. **Manifest v1 ready**: 19 AUTO patterns are engine-consumable. Splits and punctuation layers are ready for May 13 MB review.
3. **Test set**: 48 pairs untouched. Reserve for eval run when engine is ready.
4. **Alignment pipeline**: rough→final gap alignment needed for precise addition measurements (Period, comma, em-dash). Lexical alignment is the blocker for Phase 4 v3.

---

*Generated by overnight recon run. Sanitized for public repo — no witness names, case IDs, or local paths.*
