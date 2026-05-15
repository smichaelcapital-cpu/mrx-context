# Single-Clone Parallel Work Incident — 2026-05-16

**Date:** 2026-05-16 (evening session)
**Author:** Sonnet #1 (Lane B) + Opus (architect) review
**Status:** Recovered cleanly. Captured for future guardrail design.

---

## 1. What Happened — Plain

Two Sonnets were running on the same physical engine repo clone at:
`/c/Users/scott/OneDrive/Documents/mrx_engine_v1/mrx_engine_v1`

Sonnet #2 ran `git checkout -b feature/b1.7.3-waive-stipulation origin/main`. The command reported success. However, the active branch was still `feature/b1.7.4-arbitration-cover` — Sonnet #1's branch — because both sessions share the same working tree on disk.

Sonnet #2's B1.7.3 commit (`19c33e3`, waive-mode stipulation renderer) landed on Sonnet #1's branch instead of its own. Sonnet #1 then built B1.7.4 on top of it — commit `8319c22` (arbitration cover layout). Two fixes ended up intermixed on one branch: `feature/b1.7.4-arbitration-cover`.

Sonnet #1's test run during B1.7.4 build reported "B1.7.3 already locally present" — technically true, because B1.7.3's code was sitting on the same branch Sonnet #1 was operating on. This masked the routing error until post-build diagnosis.

`feature/b1.7.3-waive-stipulation` was never pushed to origin. It existed only as a local branch name with no commits.

---

## 2. Root Cause

- Two Claude Code sessions share one working tree on disk.
- Branch checkout in one session does not transfer to the other. `HEAD` is per-filesystem, not per-Claude-session.
- Branch creation (`git checkout -b`) appears to succeed in the calling session — the command output says "Switched to a new branch" — but the filesystem stays wherever the last actor left it.
- No automatic detection. Each session trusts the output of its own commands. Neither session has visibility into what the other session is doing to the shared working tree.

---

## 3. Recovery Sequence

1. Both Sonnets parked on Scott's request.
2. Diagnosis: ran `pwd` in both sessions to confirm both pointed to the same physical path.
3. State assessment: both commits intermixed on `feature/b1.7.4-arbitration-cover` on origin; `feature/b1.7.3-waive-stipulation` never pushed.
4. Decision: merge `feature/b1.7.4-arbitration-cover` to main directly with `--no-ff` and an explanatory merge message, rather than splitting commits onto separate branches (risky, time-consuming, no functional benefit).
5. Result: merge commit `711eb26` on main. Both fixes shipped together. History preserved. Verification run on all 6 depos confirmed clean post-merge state (5/6 exit 0; black_bp still pending B1.7.5).

---

## 4. Cost

- ~30 minutes of diagnosis and recovery.
- One non-standard merge commit on main (cosmetic, not functional — history is accurate).
- One never-pushed local branch name (`feature/b1.7.3-waive-stipulation`) discarded without ceremony.

---

## 5. What Worked

- `pwd` diagnostic caught the shared-path problem cleanly and immediately.
- Both Sonnets parked on request, no rogue commits during recovery window.
- Code itself was correct — only the branch routing was wrong. No rework needed.
- Verification run on main confirmed clean state post-merge.
- The `--no-ff` merge with an explanatory commit message preserves the full incident history in git log.

---

## 6. Proposed Guardrails for Future

**HARD RULE: Only one Sonnet operates on a given physical repo clone at a time.**

If parallel build work is needed, the second clone goes in a separate folder, e.g.:
- Lane A: `/c/Users/scott/OneDrive/Documents/mrx_engine_v1/mrx_engine_v1`
- Lane B: `/c/Users/scott/OneDrive/Documents/mrx_engine_v1_lane_b/mrx_engine_v1`

Additional pre-flight steps to add to every build assignment:

1. **Include `pwd` output in recon.** Every Sonnet recon must include `pwd` AND `git rev-parse --git-dir` so the working tree path is verifiable and logged.

2. **Confirm branch cut took effect.** Every branch-cut sequence must include `git rev-parse --abbrev-ref HEAD` AFTER the checkout — not just at session start. Confirms the cut actually landed on the filesystem.

3. **Explicit clone path in kickoff prompt.** When two Sonnets are assigned, each kickoff prompt must name a distinct, non-overlapping clone path. Ambiguity in path = ambiguity in ownership.

---

## 7. Relationship to 2026-05-15 Branch Drift Incident

Same family of root cause (branch hygiene). Different mechanism.

| | 2026-05-15 Branch Drift | 2026-05-16 Single-Clone Parallel |
|---|---|---|
| Sessions | Single Sonnet | Two Sonnets |
| Mechanism | Branched from wrong source (stood on prior session's branch instead of origin/main) | Branch checkout silently no-op'd due to shared filesystem |
| Detection | Recon gate caught wrong branch name in build report before push | Post-build: "B1.7.3 already locally present" flag triggered manual diagnosis |
| Recovery | Cherry-pick to correctly-parented branch | --no-ff merge to main with explanatory message |
| Recovery time | ~45 minutes | ~30 minutes |

Both incidents are fixable with explicit pre-flight branch state verification. Both argue for `git rev-parse --abbrev-ref HEAD` confirmation after every branch operation, not just at session start.

---

## 8. Open Items for Opus / Scott

**Q1 — Dual-clone pattern:** Should we adopt `lane_a` and `lane_b` folder structure as the standard for parallel Sonnet work? Cost: Scott must maintain two clones and keep both in sync with main before each session. Benefit: eliminates shared-filesystem ambiguity entirely.

**Q2 — Single-Sonnet-only default:** Should single-Sonnet-per-repo be the hard rule until dual-clone is set up? Simplest guardrail. Parallel lanes would require dual-clone as a prerequisite.

**Q3 — Pre-commit hook (deferred):** A hook that refuses commits when the working tree branch doesn't match the session's expected branch. Heavyweight to implement. Capture the idea; revisit after the A10 demo milestone.

— End of capture —
