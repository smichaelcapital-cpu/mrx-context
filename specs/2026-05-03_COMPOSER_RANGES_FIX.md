# SPEC: Composer Range Fix for Full Depo (D-COMPOSER-SILENT-TRUNCATE)

Date: 2026-05-03
Author: Opus (architect)
Builder: Sonnet
Status: APPROVED for build

## Problem
document_composer.py has 4 hardcoded turn-range constants tied to halprin_mini.
Plus _DEPOSITION_STEM = "halprin_mini" in assemble_final.py.
Running the full Halprin corrected_turns (3,547 turns, idx max 3635) silently
truncated 2,900+ turns. Stage 5 reported "completed." RULE-SILENT-FAILURE-CHECK
violation.

## Goal (today)
Render halprin_full.OUR_FINAL.txt — ~293 body pages, ~3,500 turns, ending
in errata + RICHARD HALPRIN signature. This is the input to today's
Aligner+Differ design.

NON-goal: v0.2 derivation from paragraph_style markers (parking lot, belongs
with Aligner+Differ generalization).

## Approach: Parameterize via case_info JSON
Move the 4 range constants + stem out of composer.py / assemble_final.py
into case_info JSON. Composer reads at runtime.

Why over hardcode-swap:
- Preserves mini regression path
- Half-step toward v0.2 (data-driven, not hardcoded)
- ~30 min extra vs pure swap, acceptable

## Files touched

1. case_info_halprin_full.json — NEW
   - deposition_name: "halprin_full"
   - qa_start: 91
   - qa_end: 3620
   - close_start: 3621
   - close_end: 3635
   - byline_open_idx: 90
   - byline_idxs: [503, 549, 737, 845, 860, 917, 976, 1018, 1022, 1235,
     1306, 1432, 1461, 1478, 1483, 1486, 1493, 1502, 1649, 1899, 2016,
     2107, 2229, 2246, 2264, 2333, 2344, 2441, 2507, 2656, 2704, 2943,
     2950, 2983, 3038, 3068, 3294, 3391, 3556, 3563]

2. case_info_halprin_valid.json (mini) — UPDATE
   - Add same 6 new fields with mini values:
     qa_start: 91, qa_end: 621, close_start: 622, close_end: 636
     byline_open_idx: 90, byline_idxs: [503, 549]
   - Preserves mini behavior, no regression.

3. document_composer.py — UPDATE
   - Remove module-level _QA_START, _QA_END, _CLOSE_START, _CLOSE_END,
     _BYLINE_IDXS, _BYLINE_OPEN_IDX
   - Read from case_info parameter
   - Missing fields → raise ConfigError with explicit list
   - NEW SILENT-TRUNCATE GUARD: after loading turns, count turns with
     idx > close_end. If > 0, raise RangeError with count + close_end value.
     Kills D-COMPOSER-SILENT-TRUNCATE permanently.

4. assemble_final.py — UPDATE
   - Remove _DEPOSITION_STEM
   - Read deposition_name from case_info

5. _run_halprin_full_stage5.py — UPDATE or CREATE
   - case_info: case_info_halprin_full.json
   - input: _stage3_1_out/corrected_turns.json (full, 3.5 MB)
   - output: derives from deposition_name → halprin_full.OUR_FINAL.txt

6. Tests
   - Update existing mini composer tests to pass case_info
   - NEW test_composer_silent_truncate_guard.py: feeds composer turns
     beyond close_end, asserts RangeError
   - All tests pass before commit

## Prime Directive
"Could this reduce transcript accuracy or credibility?"
NO. Actively reduces risk via the silent-truncate guard.

## Acceptance criteria
- [ ] All existing tests pass
- [ ] New silent-truncate guard test passes
- [ ] halprin_full.OUR_FINAL.txt exists, 450-550 KB
- [ ] ~293 body pages rendered
- [ ] ~3,500 turns rendered (close to 3,547 total)
- [ ] Last 5 lines: errata block + RICHARD HALPRIN signature
- [ ] halprin_mini.OUR_FINAL.txt (89,916 bytes) preserved as bug evidence,
      NOT overwritten
- [ ] Re-run mini Stage 5 produces byte-identical output to existing
      mini file (regression check)

## Rollback
git revert. proposals.json and corrected_turns.json untouched.

## Estimate
45-60 min build.
After building, report back with:

New spec URL
Mini regression check result (byte-identical y/n)
New file size, page count, turn count rendered
Last 5 lines of halprin_full.OUR_FINAL.txt

Do NOT commit until all tests pass. Do NOT push without explicit Scott approval.
