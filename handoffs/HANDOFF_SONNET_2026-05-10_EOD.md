# Handoff — End of Day 2026-05-10

**From:** Sonnet (evening instance)
**To:** Fresh Sonnet, Monday morning
**Owner:** Scott
**Date:** 2026-05-10 (evening)
**Status:** Clean tap-out. No partial work. No uncommitted local state except the fingerprint (which is local-only by design).

---

## Ramp — Read in This Order

1. `knowledge/CODER_MINDSET.md`
2. `knowledge/ADDENDUM_TO_CODER_MINDSET.md`
3. `knowledge/RULE_SHEET.md`
4. The four 2026-05-10 knowledge files (check `knowledge/` for anything dated 2026-05-10)
5. `handoffs/HANDOFF_OPUS_2026-05-10_afternoon.md` — the afternoon Opus session that set the agenda for this evening
6. Today's reports in order:
   - `reports/2026-05-10/punctuation_recalc_audit.md` (TD-004)
   - `reports/2026-05-10/eval_run_v1_pattern_level.md` (Eval A)
   - `reports/2026-05-10/sunday_cleanup_summary.md` (this evening's lane changes)
7. This handoff

When you're ramped: confirm in one line, then wait for Scott or Opus.

---

## State at Tap-Out

- **Engine repo:** unchanged from this morning. No engine code touched today.
- **mrx-context HEAD:** see commit after Step 7 push (sunday cleanup summary + this handoff)
- **Local fingerprint:** `C:\mrx_training_set\MB\fingerprint\manifest.yaml` at version `2026-05-10.v2_cleanup`
  - 13 AUTO patterns confirmed against test set
  - 6 patterns demoted/reverted with full audit trail in `confidence_history\`
  - Manifest counts: AUTO=13, SUGGEST=8, FLAG=7, PROTECTED=0, total=28
- **Test set:** 45 of 48 pairs extracted to `C:\mrx_training_set\MB\extracted\test_<stem>\`
  - 3 quarantined (see below)
  - All 45 logged in `_provenance\pair_access.jsonl` with `mode: eval_read`

---

## Today's Three Wins

**Win 1: Recalc audit (TD-004) retired 4 fake AUTO patterns before MB saw them.**

The overnight Sonnet ran a batch confidence correction 4 minutes after phase3. Six patterns got switched from ratio to pairs_coverage. The audit found that 4 of those 6 were wrong: hyphen_addition matched phonetic name spellings (not MB's habit), and comma/emdash/quote used pairs_coverage=1.0 which is trivially true for any English document. Two stage-direction patterns (`?(` and `.(`) were legitimate — those stay AUTO. Net: 4 patterns pulled from AUTO before any of this reached MB.

**Win 2: Eval A confirmed 13 patterns hold on 45 held-out test pairs.**

First independent test of the fingerprint. 45 test pairs, never seen in training. 13 of 15 surviving AUTO patterns held within a 5pp tolerance (HOLDS). Two softened: `split_leading_well` (−0.086) and `split_leading_yeah` (−0.069), both witness-dependent preserved-speech habits. Zero WOBBLY, zero FAILED. The core fingerprint is real.

**Win 3: Test set extraction methodology established with quarantine discipline.**

The test set had never been extracted. Three pairs had unusual formats (.rtf rough, .rtf final, .pdf rough) that don't match the training extraction methodology. Rather than one-off them under time pressure, they were quarantined explicitly with documented reasons. 45 clean pairs extracted using verbatim functions from the training pipeline. MRX_EVAL_MODE=1 enforced throughout. Provenance logged.

---

## 3 Quarantined Test Pairs

| stem | Format issue | Status |
|---|---|---|
| `031326yellowrock` | Rough is `.rtf` — no .rtf rough handler in training methodology | Quarantined per Scott's explicit instruction |
| `030526yellowrock` | Final is `.rtf` — .rtf finals not present in training set | Quarantined |
| `071125unitedhealth-guillotte` | Rough is `.pdf` — training roughs were all .sgngl; different extraction path | Quarantined |

These are excluded from Eval A by design, not by accident. Documented in `C:\mrx_training_set\MB\extracted\_test_quarantine.md`.

---

## Open Items / What's Next

No recommendations — just the queue, in rough priority order:

1. **May 13 deliverable draft** — "we measured your work" report for MB. Foundation is `overnight_recon_summary.md`. Needs the Eval A story added now that it's confirmed.
2. **Engine fingerprint integration** — 13 AUTO patterns are ready to consume. Splits and punct layers are the story.
3. **Per-case lexical (Q1 from afternoon Opus handoff)** — the "per-case fingerprint" question Opus flagged. Not yet spec'd.
4. **TD-001: Steno-code-filtered rough extraction** — prerequisite for lexical layer v3 and punct gap-alignment. Two approaches documented in overnight handoff (line-level filter vs token-level filter).
5. **TD-002: Punct addition gap alignment** — blocked on TD-001. The SequenceMatcher methodology from the 7-pair run is proven; needs clean rough input.
6. **TD-003: Date parsing anomaly** — manifest upper bound shows "2466-09-19" (cosmetic, stem with case# in date position). Fix: limit date parsing to 6 digits only.
7. **TD-004 pending decisions** — hyphen_addition reverted (done). The 3 YELLOW patterns (comma, emdash, quote) are now SUGGEST; they stay there until TD-002 gap alignment gives a real measurement.
8. **Extraction for 3 quarantined test pairs** — bounded tasks, each needs its own extraction approach. Do as separate specs; don't one-off under time pressure.

---

## Scott's Working Style Reminders

- One question at a time. Never stack questions.
- Full absolute paths in all file references.
- No public push of anything from `C:\mrx_training_set\` or `C:\Cat4\`. Only sanitized summaries go public.
- No commits without Scott review.
- Fingerprint state is sacred: wrong AUTO labels hurt MB's trust. Slow is smooth.
- If stuck or unclear: stop and ping. Don't improvise on fingerprint state.
- MRX_EVAL_MODE=1 required any time test set files are accessed.
- Plain English. No flowery language.

---

## Session Health at Tap-Out

Clean, not a crash. All three tasks fully completed: audit, eval, cleanup. No partial files. No open scripts. The fingerprint is in a better state than it was this morning — tighter, more honest, tested against data it hadn't seen.

The work today was mostly about credibility: making sure what's labeled AUTO is actually AUTO before MB sees it. That job is done. The 13 patterns that remain AUTO survived an independent test.

Good luck Monday.

— Sonnet, evening 2026-05-10
