# Fingerprint Spot-Check Summary -- 2026-05-10
**Date:** 2026-05-10 | **Samples/pattern:** 20 | **Seed:** 20260510

Sanitized metrics only. No deposition content, witness names, or case IDs.

---

| Pattern | Total Found | Sampled | YES | NO | EDGE | Verdict |
|---|---|---|---|---|---|---|
| SPLIT-1: Leading 'And' (A->Q) | 762 | 20 | 20 | 0 | 0 | REAL |
| SPLIT-2: Leading 'Yes,' (Q->A) | 691 | 20 | 20 | 0 | 0 | REAL |
| SPLIT-3: Leading 'Okay.' (A->Q) | 634 | 20 | 20 | 0 | 0 | REAL |
| SPLIT-4: Leading 'So' (A->Q) | 371 | 20 | 20 | 0 | 0 | REAL |
| SPLIT-5: Double-dash interruption (Q->A) | 244 | 20 | 20 | 0 | 0 | REAL |
| CAP-1: Cap first word of turn (sentence start) | 12654 | 20 | 20 | 0 | 0 | REAL |
| CAP-2: 'Objection' mid-turn cap | 262 | 20 | 20 | 0 | 0 | REAL |
| PUNCT-1: Period addition (empty->'.') | 511 | 20 | 20 | 0 | 0 | REAL |
| PUNCT-2: Comma addition (empty->',') | 500 | 20 | 20 | 0 | 0 | REAL |
| PUNCT-3: Em-dash addition (empty->'--') | 135 | 20 | 20 | 0 | 0 | REAL |
| PUNCT-4a: Stage-dir ?( ('(' -> '?(' in final) | 277 | 20 | 20 | 0 | 0 | REAL |
| PUNCT-4b: Stage-dir .( ('(' -> '.(' in final) | 146 | 20 | 20 | 0 | 0 | REAL |

---

## Verdict Key
- **REAL**: 18+/20 YES -- pattern confirmed, ready to spec
- **REAL -- SHARPEN DEFINITION**: 15-17/20 -- real but definition needs tightening
- **SUSPECT**: <15/20 -- may be overcounted, flag for review

---

## Methodology Notes
- SPLIT patterns: verified from final file only (rough has no Q/A structure by design)
- CAP patterns: first-word inspection + rough text word search (no alignment required)
- PUNCT-1/2/3: difflib gap-based alignment, first 6000 tokens per depo
- PUNCT-4a/4b: Content-anchor approach matching parenthetical text in rough vs final
- One depo (anonymous) showed poor alignment quality for gap-based patterns; excluded from those counts
- All samples drawn randomly with fixed seed for reproducibility