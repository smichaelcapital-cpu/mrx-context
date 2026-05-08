# HANDOFF — Sonnet, end of 2026-05-07 session

## Session result: M1 shipped, 3a paused mid-flight, 3b paused at draft

## What shipped tonight
- Q-DROP M1 (commit 922aa0e, pushed to main on smichaelcapital-cpu/mrx_engine_v1)
- Three files: src/mrx_engine_v1/stage2/qdrop_m1.py (new), src/mrx_engine_v1/stage2/pipeline.py (patched), tests/stage2/test_qdrop_m1.py (new)
- 10/10 unit tests passed
- Diff result: 76 → 65 blocks. A-side: 27 → 16. Orphan warnings: 287 → 0.
- One new Q-side block surfaced (7 → 8) — verified as bookkeeping artifact, not regression. See reports/2026-05-07/qdrop_m1_new_qside_diffs.md.

## What's paused and why
Marybeth Muir replied to Scott's email about the s2-continuation rule with a vague example suggesting MB may keep continuations under the same Q. label rather than promoting to standalone Q. This contradicts the 339 position-check evidence M1 was built on. Scott has emailed MB asking for a real Brandl example. Reply could take days.

Until MB confirms with a real example:
- 3a (is_doubled classifier fix) is paused mid-flight. Sonnet should report current state in the EOD status block below.
- 3b (D-DOUBLED-WORD across-punct + case + cross-turn fix) is paused at Opus draft stage. Not yet handed to Sonnet.
- M1 itself is shipped and live but unverified against MB's real output. May need rollback if MB confirms a different rule.

## Critical next-day decision tree
1. If MB replies with a real Brandl example confirming M1 is correct → resume 3a, ship it, then receive 3b spec from Opus.
2. If MB replies with a real Brandl example contradicting M1 → roll back M1 (revert commit 922aa0e), redesign rule, restart from clean baseline.
3. If MB has not replied by next session start → do not touch M1 or 3a. Pick up tactical work that does not depend on the s2-continuation rule.

## Files to review next session before any work
- reports/2026-05-07/qdrop_m1_position_check_339.md (the 339 evidence)
- reports/2026-05-07/qdrop_m1_no_entries_deepdive.md (the 5 NO entries deep dive)
- reports/2026-05-07/qdrop_m1_new_qside_diffs.md (the +1 Q-side block analysis)
- reports/2026-05-07/doubled_word_post_m1_count.md (post-M1 doubled_word landscape)
- reports/2026-05-06/doubled_word_evidence_27.md (the original 27-block analysis)
- specs/qdrop_m1.md (the M1 spec — locked)
- MB's real Brandl example email (when it arrives)

## Sonnet 3a current status
- File path of is_doubled: `src/mrx_engine_v1/classifier/is_doubled.py`
- Spec saved to disk: No — spec was relayed in-session by Scott. Not written to a file on disk. Full spec text is in the session transcript.
- Code implementation status: Complete. Module at `src/mrx_engine_v1/classifier/is_doubled.py`, package init at `src/mrx_engine_v1/classifier/__init__.py`.
- Test file status: Complete, 10/10 passing. File at `tests/classifier/test_is_doubled.py` (with `tests/classifier/__init__.py`).
- Anything left uncommitted on disk:
  - `src/mrx_engine_v1/classifier/__init__.py` (new, untracked)
  - `src/mrx_engine_v1/classifier/is_doubled.py` (new, untracked)
  - `tests/classifier/__init__.py` (new, untracked)
  - `tests/classifier/test_is_doubled.py` (new, untracked)
  - `io/analysis/brandl_50pp/_run_brandl_diff_m1.py` (modified, gitignored — call site updated to import from new module)
  - `io/analysis/brandl_50pp/_diff_out_m1/block_classification.json` (regenerated, gitignored — now reflects post-3a classifier, 22 doubled_word blocks)

## 3a result summary (for Opus)
- Count after fix: 27 → 22 (spec target was ≤ 20)
- 5 blocks suppressed: #56 (tubing), #81 (a/A.A backoff), #276 (I I), #392 (Okay. Okay.), #506 (had had)
- 3 spec targets still fire — all confirmed genuine OUR defects, not false positives:
  - #66 fires on `well well` ("for the **-well-** well" — OUR extra)
  - #593 fires on `the the` ("**-the-** the geologists" — OUR extra)
  - #663 fires on `a a` ("like a **-a-** calculation" — OUR extra)
- Original false-positive tagging of those 3 blocks was incorrect
- Full analysis: reports/2026-05-07/doubled_word_post_3a_count.md (pushed to mrx-context d77cf09)

## Untracked files from earlier in session (still needs disk decisions)
- io/analysis/brandl_50pp/_run_brandl_stage3.py (gitignored, not in repo)
- run_stage3.py
- run_full_depo.ps1
- depo_paths.psd1
- src/stage5/parse_rtf_frontmatter.py

These all need a commit / leave / delete call from Scott. Defer to button_up.py work.
