# Front Matter Render Harness

**Date:** 2026-05-15
**Author:** Opus (architect)
**Builder:** Sonnet #2 (Lane B)
**Branch:** feature/front-matter-runner (cut from main)

---

## Header (per RULE_SHEET_v1)

- Universal? YES (harness is reporter-agnostic; takes depo name as arg)
- Code or prompt? CODE
- File location: io/analysis/run_front_matter.py
- Commit prefix: universal:

---

## Purpose

Build a generic front-matter-only runner that takes a depo name as input, loads that depo's JSON data, calls the front matter orchestrator, and writes output to a per-depo folder. This runs in parallel with Sonnet #1's B1.7.1 v2 work. The harness is independent of B1.7.1 — it can be built and tested on Halprin BEFORE B1.7.1 lands, then run against all 6 MB depos AFTER B1.7.1 lands.

This is the deliverable that produces visible artifacts: 6 rendered front matter files Scott can open and read.

---

## Files Touched

| File | Why |
|---|---|
| io/analysis/run_front_matter.py | New file — the harness |
| io/analysis/<depo>/_front_matter_out/<depo>.front_matter.txt | New output dir + file per depo (6 total) |

No edits to renderer code, orchestrator, or assemble_final. This harness is read-only against the existing renderer.

---

## Canonical Depo Stem

The harness uses the **front_matter folder name** as the canonical depo identifier passed via `--depo`:

| Depo | Stem (`--depo` value) |
|---|---|
| Halprin | `halprin` |
| Williams | `060122williams` |
| Butler | `082222butler` |
| Olsen | `032025olsen` |
| Black BP | `0525black_bp` |
| Blanks | `101322blanks` |

Rationale: it's the only identifier consistent across all 6 depos. `cover.json` has no `depo_stem` field. Only Halprin has a case_info fixture, and that fixture uses `halprin_full` (legacy naming to distinguish from the test-environment `halprin_mini` slice). The harness does not use case_info fixture naming.

---

## Harness Behavior

**Call signature:**
python io/analysis/run_front_matter.py --depo <stem>

**Steps the harness executes:**

1. Validate `--depo` arg. Reject if folder `src/profiles/mb/data/front_matter/<stem>/` does not exist.

2. Locate the depo's front matter data folder: `src/profiles/mb/data/front_matter/<stem>/`. Confirm it contains at minimum: `cover.json`, `index.json`, `appearances.json`, `stipulation.json`. Reporter cert and witness cert are optional (per known data variance).

3. Construct or load `case_info`:
   - If `tests/stage5/fixtures/case_info_<stem>.json` exists, load it.
   - Else, generate a minimal in-memory `case_info` dict using only the fields `build_front_matter()` actually requires (see Recon Requirement below for which fields these are).
   - Use `cover.json` content as the primary source for generated fields.

4. Call `build_front_matter(case_info, stem)` from `src/stage5/front_matter/orchestrator.py`.

5. Conditionally call `build_back_matter(case_info, stem)`:
   - Read `stipulation.json` for the depo.
   - If `witness_reserves_signature` is `true`:
     - Check if `src/profiles/mb/data/front_matter/<stem>/witness_cert.json` exists.
     - If yes: call `build_back_matter()`.
     - If no: emit warning to stderr ("WARN: <stem> claims read_and_sign but has no witness_cert.json — skipping back matter"), do NOT call `build_back_matter()`, continue.
   - If `witness_reserves_signature` is `false`: do not call `build_back_matter()`.

6. Concatenate front matter and back matter (if produced). Use `\x0c` (form feed) as page separator — match Halprin's existing output convention.

7. Create output dir if missing: `io/analysis/<stem>/_front_matter_out/`. Write output to: `io/analysis/<stem>/_front_matter_out/<stem>.front_matter.txt`.

8. Print to stdout: input stem, output path, page count (count of `\x0c` plus 1), whether back matter was rendered, warnings if any. One block, clean format.

9. Exit code 0 on success, non-zero on validation failure or render exception.

---

## Olsen Data Gap — Handling

Per Sonnet #2's recon: `032025olsen/stipulation.json` has `witness_reserves_signature: true` but the folder has no `witness_cert.json`. The harness skip-with-warning behavior in step 5 handles this without blocking. Olsen front matter renders. Olsen back matter is skipped with a warning.

The data gap itself (decide whether Olsen's stipulation value is wrong or whether her witness_cert.json was never extracted) is filed as a separate tile: **B1.7.2** — queued for tomorrow. Out of scope for this harness.

---

## Recon Requirement (RULE-RECON-FIRST)

Before writing the harness, Sonnet #2 must report:

1. `git branch --show-current`
2. The exact signature of `build_front_matter()` and `build_back_matter()` in `src/stage5/front_matter/orchestrator.py` — argument names, types, return values.
3. Every field in `case_info` that those functions actually read (grep the orchestrator + the renderers it calls). One list per function.
4. Which of those required fields are present in each depo's `cover.json` (one table, 6 rows).
5. For fields NOT in `cover.json`, the proposed source: hardcoded default, derived from `--depo` arg, derived from another JSON file in the depo folder, or flagged as a blocker.
6. Confirm the form-feed convention used by `build_front_matter()` and `build_back_matter()` — does each page already end in `\x0c`, or does the harness need to insert separators?

WAIT for Scott approval on the case_info generation plan before building.

---

## Verification Sequence

### Phase 1 — BEFORE Sonnet #1's B1.7.1 lands (works on main as-is)

1. Build the harness on `feature/front-matter-runner` branch cut from current main.
2. Run only against Halprin: `python io/analysis/run_front_matter.py --depo halprin`
3. Compare the harness output against the front matter section of the existing Halprin render at:
   `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_full\_stage5_out\halprin_full.OUR_FINAL.txt`
4. Specifically: harness output must match the byte content of pages 1 through (end of front matter, before paginated body) of that file.

   Note: the existing Halprin render produces front matter by a mix of cover_page.py + appearances_page.py + stipulation_page.py + build_index_pages(). The orchestrator-based path may produce subtly different output (whitespace, newline counts) for cover and stipulation since those use front_matter/ renderers that have not been proven byte-identical to the stage5/ renderers.

   **If byte-identity fails on Halprin, the cause is likely the cover or stipulation renderer divergence — NOT the harness itself.** In that case, report the diff to Scott. We may accept the new orchestrator-path output as the new baseline for the harness, with the understanding that the full orchestrator wire-in (A12 / B1.8) will need to resolve this for production use. The harness's goal is multi-depo render visibility, not byte-replacement of the existing stage5 pipeline.

5. DO NOT run against the other 5 depos in Phase 1 — they'll crash on B1.7.1 bugs Sonnet #1 hasn't fixed yet.

6. Commit the harness file once Phase 1 passes (or once Scott accepts the divergence). Push branch. Scott pushes commits.

### Phase 2 — AFTER B1.7.1 v2 lands on main

1. Rebase `feature/front-matter-runner` on updated main.
2. Re-run against Halprin. Output must match Phase 1's accepted Halprin output (no regression from rebase).
3. Run against the other 5 depos in this exact order:
   1. `--depo 060122williams`
   2. `--depo 082222butler`
   3. `--depo 032025olsen`
   4. `--depo 0525black_bp`
   5. `--depo 101322blanks`
4. For each depo, confirm:
   - Harness exits 0.
   - Output file exists at expected path.
   - Output file is not empty.
   - Output visually looks like front matter (cover + index + appearances + stipulation + cert), not garbage.
   - Olsen produces the documented warning about back matter skip.
5. Commit all 6 output files in a single commit: `render: front matter for 6 MB depos via harness`. Push branch.

---

## Coordination With Sonnet #1

- DO NOT touch any of: `src/stage5/front_matter/index.py`, `src/stage5/front_matter/orchestrator.py`, `src/stage5/assemble_final.py`, `src/stage5/front_matter/appearances_renderer.py`.
- Sonnet #1 owns those files for this session via B1.7.1 v2.
- After Sonnet #1's branch merges to main, rebase before Phase 2.
- If Phase 1 surfaces a renderer bug that's NOT in Sonnet #1's 7-bug list, flag to Scott. Do not patch it yourself.

---

## Rollout Sequence

1. Sonnet #2 cuts `feature/front-matter-runner` from main.
2. Sonnet #2 builds `io/analysis/run_front_matter.py`.
3. Sonnet #2 runs Phase 1 on Halprin. Reports diff.
4. Scott reviews — accepts Halprin baseline (either byte-identical to old or new accepted baseline).
5. Sonnet #2 commits the harness. Pushes branch. Scott pushes commit.
6. Sonnet #2 holds until Sonnet #1's B1.7.1 lands on main.
7. Sonnet #2 rebases. Phase 2.
8. Sonnet #2 commits 6 outputs. Pushes. Scott pushes.
9. Both branches merge to main.

---

## Rollback Plan

- Harness is one file. If it produces bad output, delete the file. No engine code is touched.
- Output files are in `io/analysis/<depo>/_front_matter_out/` — independent of any existing pipeline output. Safe to delete and regenerate.
- Branch isolation: feature/front-matter-runner is independent of main and of feature/b1.7.1-index-fix. Abandoning is cheap.

---

## Open Items Requiring Scott Sign-Off

- None at spec time. case_info generation plan needs Scott approval after recon, before build (per Recon Requirement step).

---

## Prime Directive Check

Could this reduce transcript accuracy or credibility?
- Risk 1: Harness generates a bad case_info for non-Halprin depos, producing wrong cover or header data. MITIGATION: Recon Requirement forces explicit field-by-field plan reviewed by Scott BEFORE build. Verification gate against Halprin in Phase 1 catches harness-level errors.
- Risk 2: Olsen back matter silently dropped without warning. MITIGATION: Explicit stderr warning required in step 5. Output stdout block also reports "back matter rendered: yes/no/skipped".
- Risk 3: Harness output bytes diverge from existing Halprin pipeline output due to cover/stipulation renderer differences. MITIGATION: Phase 1 captures the diff explicitly. Scott decides whether to accept new baseline or hold until full orchestrator wire-in (A12 / B1.8) resolves the divergence. Either way the harness is not silently shipping a divergent render.

All risks have explicit mitigations. Recon Requirement is the primary safety gate.

— End of spec —
