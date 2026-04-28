# SPEC — F2-CONT — Wrapped Continuation Lines Lose Indent
**Date:** 2026-04-27
**Architect:** Opus
**Builder:** Sonnet
**Repo:** mrx_engine_v1
**Branch:** main
**Tier:** 1 follow-up (incomplete fix from earlier today)

## Why

Tier 1 F2 fix added explicit indent values to LogicalLines emitted by
`_build_cover()` and `_build_appearances()`. Worked for parent lines. But
when a LogicalLine wraps to multiple physical lines, the wrapped
continuations are landing with indent=0 instead of inheriting the parent's
indent. Visible symptom on page 2 of OUR_FINAL.txt:

```
10CORPORATION AND WESTLAKE CHLOR-VINYLS CORPORATION
```

Should be:

```
    10        CORPORATION AND WESTLAKE CHLOR-VINYLS CORPORATION
```

Same root cause F2 was supposed to address. Same family. Just on wrap
continuations instead of parent lines.

## Step 0 — Save spec to git first

Before any code:
- `mrx_engine_v1/docs/specs/2026-04-27_F2_CONT_WRAP_INDENT.md`
- `mrx-context/specs/2026-04-27_F2_CONT_WRAP_INDENT.md`

Save full spec to both. Commit messages:
- mrx_engine_v1: `docs(specs): add F2-CONT wrap continuation indent spec`
- mrx-context: `specs: add F2-CONT wrap continuation indent spec (mirror)`

Push both. Verify context repo URL returns 200. Report commits.

## Recon

Per RULE-RECON-FIRST and RULE-CONTRADICTION-HUNT:

1. `git branch --show-current` — confirm main
2. Open `src/stage5/page_layout.py`, find `_wrap_line()`. Read the wrap-and-emit logic end to end.
3. Identify exactly where wrapped continuation lines are produced and what indent value they carry. Quote the code.
4. Confirm hypothesis: when a LogicalLine has `indent=4` and wraps to a second physical line, the second line is emitted with `indent=0` (or some default that's not 4).
5. Refute hypothesis if wrong — report what's actually happening instead.
6. Grep entire codebase for `wrap_indent`, `subsequent_indent`, `cont_indent`, `continuation`, anything that suggests an existing concept of wrap-line indent. Report findings.

Report all 6 to Scott. Wait for "go build."

## Build

After "go build":

- Make wrapped continuation lines inherit the parent LogicalLine's indent.
- Edge case: if the parent LogicalLine has both `indent` and an explicit
  `wrap_indent` (hanging indent style), use `wrap_indent` for continuations.
  If only `indent` is set, use `indent` for continuations. Default behavior
  preserves existing tests.
- Add at least one test that proves: a LogicalLine with `indent=4` and text
  long enough to wrap produces continuation physical lines that ALSO carry
  the `indent=4` spacer before the line number.

## Verify

- Full test suite green (≥ 498 + new test)
- Run real Halprin pipeline. Open OUR_FINAL.txt page 2.
- Confirm line 10 (or wherever the WESTLAKE continuation lands now) renders
  with proper indent — no more `10CORPORATION` mash.
- Spot check 2–3 other wrap continuations across front matter for the same fix.
- Report bytes-changed count vs prior OUR_FINAL.txt.

## ALSO — capture the truth source path

While you're in this session, in your final report give Scott the exact full
absolute path to MB Halprin's FINAL.txt — the file you used for byte-level
verification today. Just the path. One line. Scott needs it for handoff
documentation.

## Acceptance

- [ ] Spec saved to both repos, both commits + 200 reported
- [ ] Recon complete, hypothesis confirmed/refuted, contradiction hunt done
- [ ] Code change in `_wrap_line()` (or wherever continuation indent is decided)
- [ ] New test proving wrap continuation inherits indent
- [ ] Full suite green
- [ ] Visual confirmation in OUR_FINAL.txt — no more mashed continuation lines on front matter
- [ ] MB FINAL.txt path reported to Scott

## Out of scope

- Tier 2 cover work (two-column case caption, sub-row packing, missing index page)
- Anything beyond fixing wrap continuation indent

## Rollback

`git revert <commit>` if anything goes sideways.

— End of spec —
