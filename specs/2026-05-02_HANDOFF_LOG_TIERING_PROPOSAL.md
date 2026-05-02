# HANDOFF_LOG.md Tiering Proposal — S3 Intelligent Tier Pattern

**Date:** 2026-05-02 (parked overnight, raised by Scott end of session)
**Author:** Opus (parked design)
**Owner:** Scott
**Status:** PARKED — design proposal, not yet specced for build
**Priority:** High — biggest single ramp risk identified to date

## The problem

HANDOFF_LOG.md is now ~4,000+ lines and growing. Three failures
in tonight's 2026-05-01 → 2026-05-02 session trace back to its
size:

1. web_fetch truncation hides the latest session entry — fresh
   Opus declares "ramped" without seeing current state
2. Internal contradictions (e.g., "BUILD QUEUED" vs "shipped at
   1519912") are harder to spot when scanning a sprawling file
3. File size makes cross-referencing slow, drives pattern-matching
   instead of careful reading

## The proposal — S3 Intelligent Tier pattern

Hot tier: handoffs/CURRENT.md
- Last 2-4 sessions only
- Strict size cap (~1500 lines, fits any web_fetch in one call)
- This is what fresh Opus reads on ramp
- Updated per existing end-of-chunk logging rule

Cold tier: handoffs/archive/HANDOFF_LOG_YYYY-MM.md
- Monthly archive files
- Read on demand only
- When CURRENT.md hits cap, oldest session rolls into current
  month's archive

Pinned content (stays in CURRENT.md regardless of age):
- Active "DECISIONS LOCKED" sections
- OPEN DECISIONS table
- Active PARKING LOT
- Anything tagged "do not archive"

## What this prevents

- Truncation failures on ramp
- Contradiction-spotting cost
- Standard ramp order enforced by structure, not memory

## When to build

Saturday or Monday morning, fresh session. Spec write +
Sonnet build = ~45 min total. Low risk. High infrastructure
value.

## Open design questions to answer in the build spec

1. Exact size cap for CURRENT.md (1500 lines is a guess —
   measure actual fetch limits)
2. Roll trigger — size-based or session-count-based?
3. How to surface "this content is in archive" cleanly when
   fresh Opus needs old context
4. Whether MANIFEST.md should reference both tiers or just
   CURRENT.md
5. Sonnet workflow for the roll — manual at end of session,
   or automated check at session start?

## Reference

Triggered by 2026-05-01 → 2026-05-02 session retrospective.
Three failures rooted in HANDOFF_LOG.md size. See last entry
of that session in the log for full root cause analysis.
