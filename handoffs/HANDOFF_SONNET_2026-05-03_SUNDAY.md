# SONNET HANDOFF — Sunday 2026-05-03 morning

## Last night's wrap

Move A shipped end of Saturday. Two commits on engine main:
- be5ecad — validate_ops _names_lock_exempt() (3-tier: exact → strip function words → word-segment substring) + "W&T" in NAMES_LOCK + 14 new tests
- 8b1ca21 — Writer prompt W&T form rule (offshore in raw → full form, else short form)

Tests: 579 passing, zero failures.

Halprin first 50 pages confidence: 52.4% → 71.4% (15/21). Acceptance band: YELLOW. Shipped per spec.

## Last night's full-depo run

Saturday evening Scott ran the FULL Halprin (305 pages, 3,547 turns, 60 batches) tip-to-tail through Stages 1, 2, 3.1, 5 in his Windows PowerShell. This was the wallpaper-only baseline run — same NAMES_LOCK + MB_PROFILE as the 50-page run, applied to the full depo.

Run output lives in: io/analysis/halprin_full/

If the run completed before Scott logged off:
- Confidence number captured in RUN_SUMMARY_2026-05-02_evening.md
- All artifacts in io/analysis/halprin_full/_stage1_out, _stage2_out, _stage3_1_out, _stage5_out
- Pushed to mrx-context

If the run failed midstream: error captured in RUN_SUMMARY. Don't re-run automatically. Wait for Opus.

## Today's first task — DO NOT START CODING

Read in this order before doing anything:
1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. The new Opus-to-Opus handoff (URL forthcoming once committed)
4. The full Halprin RUN_SUMMARY

After reading, post ONE LINE: "Ramped Sunday morning. Ready."

Then wait for Opus to assign the first task. The first task will NOT be a Halprin analysis. It will be the Aligner+Differ design — the architectural pivot Scott crystallized last night.

## Standing context

- CODER_MINDSET active. Slow is smooth.
- Plain English, 12-year-old reading level, short answers, ONE question at a time
- Inline A/B/C only when there's a real choice
- Always full absolute paths
- Sonnet never commits or pushes — Scott does
- Oracle Covenant — FINALs are training-time only, never runtime

## Major architectural pivot logged last night

NAMES_LOCK as currently used is wallpaper. Real engine performance without per-depo wallpaper is ~19% (Bucket 3 only). The 71.4% number is wallpaper-inflated.

Scott's design (now locked as the path forward): build a Raw↔FINAL aligner+differ. Read MB FINAL line-by-line against MB RAW. Every diff is a labeled training example. Patterns that show up in multiple FINALs are habitual MB style. Patterns in only one FINAL are case-specific. Habitual goes in MB_PROFILE; case-specific gets calibrated per depo.

This replaces hand-coded NAMES_LOCK with learned NAMES_LOCK. End of wallpaper.

Spec drafting starts when Scott is back online.
