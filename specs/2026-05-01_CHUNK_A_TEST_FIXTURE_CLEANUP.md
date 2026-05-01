# CHUNK A — Test fixture cleanup for V2 schema

Date: 2026-05-01
Author: Opus (architect)
Builder: Sonnet
Gate: Soft (no architecture change, no runtime behavior change)

## Background

V2 Reader prompt deployment (commits 22a24d7, 502061e, 657649a, 7d5bb93) changed two contracts that the test suite was not updated for:

1. `proposal_mapper.py` now joins proposals/decisions/anomalies on `anomaly_id`, not by positional index. The old positional length-equality guard was removed.
2. V2 Reader produces ~147 anomalies + 126 proposals on Halprin mini, vs ~30 in V1. Tests with hardcoded counts of 30 are stale.

10 tests fail. All 10 are fixture/expectation drift, not real regressions.

## Goal

Update test fixtures and assertions so the suite passes against the V2 contract. No production code changes. No runtime behavior change.

## Pre-build recon (REQUIRED before any code change)

Per RULE-RECON-FIRST, run these and paste output to chat before editing:

1. `git status` and `git log --oneline -5` on engine repo
2. `pytest tests/stage5/test_proposal_mapper.py -v 2>&1 | head -80` — capture exact failure messages
3. `pytest tests/stage5/test_document_composer.py -v 2>&1 | head -80`
4. `pytest tests/stage5/test_assemble_final.py -v 2>&1 | head -40`
5. Read current `src/stage5/proposal_mapper.py` — confirm the join is on `anomaly_id` and report the actual error message it raises when an anomaly_id is missing
6. Read `tests/stage5/test_proposal_mapper.py` — locate the test that expects `"length mismatch"` regex and report the exact assertion

After recon, STOP and report findings to Opus before editing. This is a hard checkpoint. If recon surfaces anything that looks like a real regression (not fixture drift), flag it.

## Build (after Opus approves recon)

### Fix 1 — proposal_mapper test fixture

The test that asserts `"length mismatch"` is now wrong because the V2 contract doesn't use length equality. Two acceptable fixes (Sonnet picks based on recon, asks Opus if unsure):

- **Option 1:** Update the assertion to match the new error message (e.g. `"unknown anomaly_id"`).
- **Option 2:** Update the fixture so it actually triggers a different specific error path the test was originally meant to catch.

Whichever you pick, document the choice in the test docstring.

### Fix 2 — document_composer + assemble_final hardcoded counts

Find every hardcoded `30` (or `len(...)==30`, `assert ... == 30` etc.) tied to review queue size. Replace with count-from-fixture:

1. Read the fixture's anomalies/proposals at test setup
2. Compute expected count from fixture data
3. Assert against computed value

This makes tests resilient to future Reader prompt changes that move the count.

### Fix 3 — cover section "0 lines" failures

- If recon shows the cover section failures are purely from hardcoded count assertions, they fall under Fix 2 above.
- If recon shows actual cover output is empty (Module 6 regression), **STOP**. That is Chunk B (hard gate), not Chunk A. Report and wait.

## Acceptance criteria

- `pytest tests/ -q` shows 510 passing, 0 failing
- No changes to any file under `src/`
- No changes to V2 Reader prompt, `suggester.py`, or runner config
- Commit message: `test(stage5): align fixtures with V2 anomaly_id-keyed join + dynamic counts`

## Out of scope (do NOT touch)

- Production code (`src/`)
- V2 prompt
- Runner config
- Cover regression IF it turns out to be real (that's Chunk B)
- The 5 untracked docs in repo
- The pre-existing `test_dictionary_loader.py` drift

## Report back

After build, paste:
- Final pytest summary line
- Diff stat (`git diff --stat`)
- Commit hash
- Any judgment calls made during the build

---
*End of spec*
