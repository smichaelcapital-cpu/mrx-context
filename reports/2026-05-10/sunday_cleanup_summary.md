# Sunday Evening Cleanup Summary

**Date:** 2026-05-10 (evening)
**Author:** Sonnet (evening instance, directed by Scott via Opus)
**Status:** COMPLETE — local fingerprint updated, manifest bumped, history logged

---

Six patterns were demoted or reverted Sunday evening based on two audits run earlier the same day. No measurements were changed — only lane assignments. Confidence numeric values are frozen. All changes are logged in the local confidence_history files with `manual_override` events.

---

## Pattern Lane Changes

| pattern_id | Previous lane | New lane | Source |
|---|---|---|---|
| `punct_hyphen_addition` | AUTO | FLAG | Recalc audit (TD-004) — RED |
| `punct_comma_addition` | AUTO | SUGGEST | Recalc audit (TD-004) — YELLOW |
| `punct_emdash_addition` | AUTO | SUGGEST | Recalc audit (TD-004) — YELLOW |
| `punct_quote_addition` | AUTO | SUGGEST | Recalc audit (TD-004) — YELLOW |
| `split_leading_yeah` | AUTO | SUGGEST | Eval A — SOFT (test PC 0.8667 vs training 0.9355) |
| `split_leading_well` | AUTO | SUGGEST | Eval A — SOFT (test PC 0.8222 vs training 0.9086) |

---

## Final Pattern Counts (fingerprint v2026-05-10.v2_cleanup)

| Lane | Count |
|---|---|
| AUTO | 13 |
| SUGGEST | 8 |
| FLAG | 7 |
| PROTECTED | 0 |
| **Total** | **28** |

---

## Source Reports

- Punctuation recalc audit (TD-004): `reports/2026-05-10/punctuation_recalc_audit.md`
- Eval A pattern-level results: `reports/2026-05-10/eval_run_v1_pattern_level.md`

Full audit trail (confidence history JSONL files with `manual_override` events) lives in the local fingerprint directory and is not pushed to this repo.

---

## What Did Not Change

Confidence numeric values are frozen. Only `current_lane` was reassigned. The measurements that produced those numbers are unmodified.

The 13 remaining AUTO patterns were confirmed on 45 held-out test pairs in Eval A (same session). See eval A report for full table.
