# Tech Debt Log — mrx_engine_v1

## TD-001 — Writer JSON Truncation (2026-05-08)

**Symptom:** Writer LLM returns malformed JSON on dense batches (35+ anomalies),
truncating mid-string at ~11,000 chars output.

**Patch applied:** Raised writer max_tokens from 4096 to 8192 on 2026-05-08.
Re-ran 11 stranded batches successfully. Total patch cost: $14.92 (baseline $12.36 + ~$2.56 patch).

**Root cause:** Writer is making correction decisions at write time. This violates
the Three Sealed Phases architecture (locked 2026-05-03). The writer should not
exist as a separate AI call — corrections should be proposed by the reader with
confidence scores, then applied by a dumb mechanical composer.

**Real fix:** Reader upgrade spec + dumb composer build. Estimated weeks of work.
Not scheduled. Do not lose this entry.

**Cost of NOT fixing:** Every Stage 3 run pays $4-5 in writer cost that would be
$0 under correct architecture. Plus risk of new truncation bugs if anomaly density
grows.

**Status:** PATCHED, NOT SOLVED.

---

## TD-002 — Stale E2E Test Expectation: test_E2E3_wt_has_misses (2026-05-09)

**Symptom:** `tests/test_e2e_halprin_mini.py::test_E2E3_wt_has_misses` fails with:
`AssertionError: Expected W&T miss >= 4, got miss=0`

**What happened:** Test was written when the engine was missing ≥4 W&T hits.
Engine has since improved — now correctly finds all 9 W&T hits (0 misses).
Test expectation was never updated to match.

**Real fix:** Update the assertion to reflect current engine behavior (miss == 0,
win == 9). Quick fix — low effort. Verify no other e2e assertions depend on
the miss count before editing.

**Status:** LOGGED, NOT FIXED.

---
## 2026-05-16 — appearances reporter anchor: pending-row coupling is a structural gap

**Status:** Surgical fix landing in B1.7.6. Real design fix deferred.
**Severity:** Medium — affects any depo with an inline_label also_present (single-item tail) before the reporter block.

**Context:**
B1.7.6 needed two changes to land Olsen's reporter at oracle line 18:
1. Make `reporter_anchor_line` a per-depo field (the original spec)
2. Clear `pending=True` before the anchor padding loop in `_paginate_blocks` so the reporter starts a fresh main row instead of filling an open sub-row

The 2nd fix surfaced because Olsen's `also_present.kind = "inline_label"` emits a single item, leaving `pending=True`. Halprin's `also_present.kind = "header_block"` emits two items, leaving `pending=False` — which is why anchor=19 always worked for Halprin and the bug stayed hidden.

**The real problem:**
The anchor target is computed in slot space (`(anchor-1)*2`), but the renderer's pending-row state can offset where `emit_item` actually lands by one half-slot. The fix in B1.7.6 force-closes pending before anchoring. This works for now, but the underlying design conflates two things:
- Where the reporter block *should* anchor (a layout intent)
- Where the renderer's current row state *happens to be* when anchoring (a render-loop side effect)

**Future risk — without final files to byte-match:**
When we onboard depos for which we don't have an MB-authored FINAL, we won't have ground truth to detect anchor-off-by-one issues. The current design needs the operator to spot the drift. That's fragile.

**Better long-term design (candidates):**
- (a) Make `reporter_anchor_line` semantic: "start reporter on line N main, regardless of current pending state." Implementation handles padding + row-state both.
- (b) Replace anchor-by-line with anchor-by-event: "reporter follows N empty slots after the last also_present row." Decouples from absolute line numbers.
- (c) Capture the also_present.kind → pending behavior as a typed contract; reporter anchoring knows the contract instead of hand-clearing pending.

**Trigger to revisit:**
- Any new depo where also_present is a different kind we haven't seen
- Any new customer with different appearances tail patterns
- Or when we onboard our first depo without an MB FINAL — we'll need anchor logic robust enough to trust without ground-truth comparison
- Or when we have demo headroom and want to clean before scaling

**Connection to fish-or-cut-bait question:**
Scott raised this directly — when no final exists, how do we know we got it right? This ticket is exactly that scenario in miniature. The current answer is "operator-spotted diff against oracle." That doesn't scale.
