# Branch Drift Incident — 2026-05-15

**Date:** 2026-05-15 (evening session)
**Author:** Sonnet #1 (builder, Lane A) + Opus (architect) review
**Status:** Recovered cleanly. Captured for future guardrail design.

---

## What happened — plain

Sonnet #1 received the B1.7.1 v2 spec for the index renderer fix + index-only wire-in. The spec called for branch `feature/b1.7.1-index-fix` cut from main. Sonnet #1 did neither:

- Did not run `git fetch origin main` before cutting.
- Cut the branch from `feature/appearances-renderer-fix` (where he was standing from the morning A1.5.1 work) instead of from `origin/main`.
- Named the new branch `feature/front-matter-runner` — which is **Sonnet #2's branch name** for the parallel harness work.

Three commits landed on this misnamed, mis-parented branch:
- `2cf64df` (B1+B2+B3+B4+B5+NEW-7 fixes)
- `e5c98f4` (B6 fix)
- `41b1168` (wire-in)

Halprin verification passed (329/329 byte-identical). The code was correct. The branch was wrong.

Compounding the problem: Sonnet #2 then pushed his harness commit `0f8ef71` to `origin/feature/front-matter-runner` — landing on top of Sonnet #1's stale commits. Result: a 5-commit remote branch where 4 of the 5 commits did not belong there.

---

## Root cause

No explicit "fetch + cut from origin/main" step in the build assignment template. Builder defaulted to "branch from wherever I'm standing" — which was the previous session's working branch.

Secondary cause: no branch name verification step before the first commit. Builder did not run `git branch --show-current` to confirm the new branch name matched the spec.

Tertiary cause: when two builders work in parallel with similar-looking branch names, there's no cross-check that prevents accidental name collision.

---

## Recovery sequence

1. Sonnet #1's recon flagged the issue ("Branch feature/front-matter-runner is ready" in build report) when Opus expected `feature/b1.7.1-index-fix`.
2. Sonnet #1 stopped before any push.
3. Recovery plan: cherry-pick the 3 commits onto a freshly-cut `feature/b1.7.1-index-fix` from `origin/main`.
4. Cherry-picks landed clean: `55b44ab`, `2c3de9c`, `2d2e9d6`. Halprin verification re-passed.
5. Sonnet #1 pushed the correct branch to origin.
6. Sonnet #2 then ran a separate cleanup on his own branch: renamed the misparented branch to `backup/front-matter-runner-pre-cleanup`, cut a fresh `feature/front-matter-runner` from `origin/main`, cherry-picked only his harness commit `0f8ef71`, force-pushed.

Total recovery time: ~45 minutes. No code lost. No work redone — just commits moved.

---

## Cost

- 45 minutes of recovery work that wouldn't have been needed with clean branches.
- One force-push to remote (acceptable since Sonnet #2's branch had not been used by anyone else yet).
- One backup branch retained locally on Sonnet #2's clone (`backup/front-matter-runner-pre-cleanup`) until everything merges to main.

---

## Proposed guardrails for future review

(For Scott + Opus to evaluate after the depo demo lands. Not implementing tonight.)

### 1. RULE-FRESH-BRANCH-FROM-MAIN

Add to CODER_MINDSET_ADDENDUM. Every new build assignment that creates a branch must explicitly include:
git fetch origin main
git checkout -b <branch_name> origin/main

Builder confirms in recon: branch name, source branch (must be `origin/main`), HEAD commit on origin/main at time of cut.

### 2. Branch name read-back

Builder's recon report must include `git branch --show-current` output AND the branch name from the spec, side by side. If they don't match, recon fails. No commits until match is confirmed.

### 3. Pre-commit ancestry check

Before the first commit on any new branch, builder runs:
git log origin/main..HEAD --oneline

If output is non-empty (branch has commits not on origin/main), STOP. The branch was not cut clean. Report to Scott.

### 4. Cross-builder branch name visibility

When two Sonnets work in parallel, the assignment for each must explicitly list BOTH branch names — the builder's own AND the other builder's "do not touch" branch. Example:
YOUR BRANCH: feature/b1.7.1-index-fix
DO NOT TOUCH: feature/front-matter-runner (Sonnet #2's)

### 5. Optional automation (consider later)

A pre-commit hook in the repo that refuses to commit if `git log origin/main..HEAD --oneline` shows commits the builder didn't author this session. Heavyweight; defer until we see whether items 1-4 catch the problem.

---

## What worked

- Sonnet #1's recon gate caught the wrong branch name in the build report **before** any push. The existing RULE-RECON-FIRST + RULE-BRANCH-CHECK partially saved us.
- Cherry-pick recovery was clean because each fix was a logical separate commit (RULE-SPEC-BEFORE-BUILD habit of one-fix-per-commit paid off).
- Sonnet #2 was on a separate clone with separate working tree — no file-level collision.
- Halprin byte-identical verification gate caught nothing wrong with the code itself. The code was good; only the branch routing was bad.

---

## What to revisit later

Branch hygiene infrastructure tile — gates, automation, pre-commit hooks. Not tonight. After the multi-depo render demo lands. Filed under "infrastructure debt."

— End of capture —
