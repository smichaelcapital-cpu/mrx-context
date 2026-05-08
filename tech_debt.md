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
