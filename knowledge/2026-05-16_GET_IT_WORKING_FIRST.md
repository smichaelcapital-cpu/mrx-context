# Get It Working First

## The Principle
The goal right now is to get the engine working end-to-end. Not
perfect. Working.

Once it works, we go back piece by piece and make each piece
better. We do not optimize a piece that does not yet work in the
larger context. We do not chase the last 5% on one component
while the next component is still broken.

## What This Means In Practice
- Ship what works. Bank wins.
- Partial work that does not break anything goes on the revisit
  list, not the trash.
- Decisions waiting on MB stay waiting. The default holds.
- Phantom defects get closed, not chased.
- "Slow is smooth" means deliberate, not exhaustive.

## What This Replaces
The pattern of grinding one defect until it byte-matches a single
oracle. The pattern of "one more recon" before stopping. The
pattern of perfect being the enemy of shipped.

## When We Revisit
After the engine works end-to-end across all 6 (and eventually
12-13) depos, we walk back through the revisit list piece by
piece. Each revisit is a new session with a clean scope.

## Standing Revisit List (as of 2026-05-16 EOD)
- B1.9.3 Phase 2B (exhibit parity threading) — stashed on
  laneB/B1.9.3-cycle-continuity; root cause identified, ~15 lines
- D-5 MB decision (exhibits start position default) — MAIN-first
  default holds until MB responds
- B1.7.7 Olsen videographer cosmetic
- Unread front matter pages: williams, butler, blanks, black_bp
- Unread back matter pages: halprin, williams
- TD-003 harness display width (55-char column too narrow)
- Church depo ingest failure (12x raw/final ratio anomaly)
