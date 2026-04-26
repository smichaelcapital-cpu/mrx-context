# HANDOFF — SONNET — 2026-04-26 1200pm

---

## ONE-LINE STATE

9 local commits pushed to origin/main (ecd7a55). 337 tests passing. Block H runner reviewed and NAMES_LOCK corrected to 11 entries. .sgxml schema inspected (human-authorized, one-time). halprin_mini directory fully inventoried. No code changes to committed source. Ready for Opus architecture review.

---

## WHAT GOT DONE THIS SESSION

1. **Ramped up cleanly** — all 3 required files present (CODER_MINDSET_v1.md, CLAUDE_STARTUP.md, SONNET_BUTTONUP_block_G_pickup.md). Git state confirmed: 9 ahead of origin, 337 passing.

2. **Runner script reviewed** (`_run_halprin_mini.py`, 344 lines):
   - API key: env first, falls back to mb_demo_engine_v4/.env. Confirmed correct.
   - State module: loads from mb_Yellow_Brad_Brandl\STATE_MODULE_louisiana_engineering.md (older copy — 2026-03-25). mb_demo_engine_v4 copy is newer (2026-04-16). FLAG: two copies may have diverged. Opus to decide which is authoritative.
   - Cost ceiling: $1.00. Confirmed.
   - Per-batch flush=True: confirmed.
   - Ctrl+C writes partial: confirmed (on interrupt and cost ceiling hit, not after each batch).
   - Stage 2 input path: confirmed correct.
   - All 6 output files: confirmed.
   - Model: claude-sonnet-4-6. Confirmed.
   - `suggest_proposals` 3rd arg `{}`: confirmed maps to `dictionary: Any`. Empty dict is falsy — DICTIONARY block skipped. Correct.

3. **NAMES_LOCK fix** — removed "Exhibit", "Videographer", "Reporter" (were added by prior Sonnet without spec authorization). Now 11 entries per spec: Halprin, Caughey, Garner, Muir, Guastella, Lexitas, Westlake, Eagle, Calcasieu, Somerset, Chevron. Not committed (runner is gitignored).

4. **Full project inventory** — all key docs catalogued with paths, last-modified dates, canonical/superseded status. CURRENT_SPRINT.md and PROJECT_BOARD.md confirmed as mb_demo_engine_v4 v4 engine docs only (last updated 2026-03-30) — not applicable to mrx_engine_v1 work.

5. **Pre-push checklist** — all checks passed:
   - git status: only pre-existing test_dictionary_loader.py drift + 5 untracked docs
   - git log: exactly 9 commits ahead of origin
   - pytest: 337 passed, 0 failed
   - gitignore: Oracle files, _stage3_1_out/, runner all confirmed ignored via io/analysis/** rule

6. **Pushed 9 commits to origin/main** — Scott + Opus approved. Pushed successfully. origin/main now at ecd7a55.
   ```
   ecd7a55 test(stage3): firewall negative tests
   32fca7a docs(stage3): add STAGE_3_1_SUGGESTER_SPEC.md
   14e93be feat(stage3): add pipeline.py with cost ceiling and anomalies.jsonl
   106316d feat(stage3): wire Reader -> Writer -> validate -> Proposal
   bbf3b58 feat(stage3): add Writer agent + Read-Write Separation enforcement
   335a271 feat(stage3): add Reader agent in suggester
   94bef40 feat(stage3): extend apply for multi-token spans + invariant 8
   3adba26 feat(stage3): port validate_ops with new check_anomaly_link
   7bd189d feat(stage3): extend Proposal schema to v2.0 with op_type, span, source, anomaly_id
   ```

7. **Oracle .sgxml schema inspection** — human-authorized one-time read of 040226yellowrock-FINAL.sgxml. Key findings:
   - File is CaseCATalyst job PREFERENCES only — no transcript content, no Q/A turns.
   - Root: `<SGXML_Preferences CompactMode="1">` — 2 lines total, entire doc is one-line compact XML blob.
   - Contains: speaker role definitions (6 roles, numeric IDs 300-305), audio sync timestamps (88 pairs, milliseconds), job history, CVN live attendee list, translation settings, 38-dictionary stack.
   - NO hotspots, NO oops, NO annotation elements. "flag" hits are all sgpref-flags XML attribute names.
   - Key signal: 253 untranslates, 195 steno conflicts — expected anomaly volume for Stage 3.1.
   - CVN attendees (Caughey, Garner/Sher Garner, Lexitas) match NAMES_LOCK — confirmed real live viewers.
   - Transcript content lives in: .sgngl (binary), .txt (plain text export), _T.rtf (RTF, Stage 1 input).
   - Oracle Covenant maintained: read-only, no code path, no copy.

8. **halprin_mini directory inventory** — full file listing with sizes and first-50-line samples for all Stage 1 (_pipeline_out/) and Stage 2 (_stage2_out/) files. Key numbers:
   - Stage 1: 552 turns (244 Q, 243 A, 29 colloquy, 3 byline, 33 Q-continuation), 503 with strokes, 81 with deletions, all 7 acceptance criteria PASS.
   - Stage 2: 75 turns transformed (74 x T1 whitespace normalization, 1 x T-WS3), 0.015 sec.
   - _stage3_1_out/ files exist with 2026-04-26 10:48 timestamps — Block H ran this morning before this session.

9. **HANDOFF naming convention** — Scott established new rule: session-end docs are now called HANDOFFs (not button-ups), same name in both directions (Opus and Sonnet both use HANDOFF_*).

---

## WHAT FRESH SONNET DOES FIRST NEXT SESSION

1. **Check for mrx-context GitHub repo** — Scott + Opus plan to create a new public GitHub repo called `mrx-context` to hold architecture docs and handoff files so Opus can read them via web_fetch. If the repo exists, confirm its URL and read the latest handoff doc in it before doing anything else. If it doesn't exist yet, ask Scott.

2. **Read the latest HANDOFF from Opus** (will be at a path Opus specifies, or in mrx-context repo).

3. **Run standard entry checks:**
   - git log --oneline -10
   - git status
   - pytest tests/ -q
   - Report state to Scott before touching anything.

4. **Confirm Block H output is valid** — _stage3_1_out/ files exist from a run at 10:48 this morning. Fresh Sonnet should read run_metrics.json and report: was it a full or partial run, what was the cost, how many proposals, any anomalies. Do NOT re-run Block H without explicit Scott + Opus approval.

---

## OPEN DECISIONS

| # | Decision Needed | Owner |
|---|---|---|
| OD-1 | Which STATE_MODULE_louisiana_engineering.md is authoritative? mb_demo_engine_v4 copy (2026-04-16, newer) or mb_Yellow_Brad_Brandl copy (2026-03-25, older, what the runner currently loads)? | Opus + Scott |
| OD-2 | Block H ran this morning (10:48am) before this session. Was this intentional? Are the _stage3_1_out/ files the "real" Block H result, or a test run that should be discarded and re-run? | Scott |
| OD-3 | mrx-context repo — create it? Public or private? What goes in it first? | Scott + Opus |
| OD-4 | 5 untracked docs in docs/ — should any of them be committed? (STAGE_3_1_BUILD_SPEC.md, STAGE_3_ARCHITECTURE_v2.md, STAGE_4_ARCHITECTURE.md, etc.) | Opus |
| OD-5 | Partial save timing — runner only checkpoints on Ctrl+C or cost ceiling, not after each completed batch. For production runs, should per-batch checkpoint be added? | Opus |

---

## ARCHITECTURE NOTES MADE THIS SESSION

- **sgxml is preferences, not transcript.** Do not attempt to parse .sgxml for turn content. The turn data lives in .sgngl (binary) or the RTF/TXT exports. If future work needs audio sync data, it lives in sgxml Read-Audio-Timestamp/ElapsedTime arrays.

- **Stage 1 → Stage 2 delta is small.** 552 turns in, 552 turns out, 75 changed. T1 (whitespace normalization) is the dominant transform (74 turns). One T-WS3 applied. This is the expected behavior — Stage 2 is cleanup, not reconstruction.

- **253 steno untranslates in the depo.** This is the raw count of words CaseCATalyst could not resolve from its stroke dictionary during live realtime. These are the highest-probability anomaly candidates for Stage 3.1. Our Reader should find a meaningful subset of these.

- **BYLINE "EXAMINATIONBY MR. CAUGHEY"** — note the missing space in Stage 1 .txt. Stage 2 .txt shows "EXAMINATION BY MR. CAUGHEY" (space added). T-WS3 likely responsible. This is the kind of artifact the pipeline is correctly handling.

---

## PARKING LOT

- `test_dictionary_loader.py` pre-existing drift — leave alone, not from this session.
- 5 untracked docs in docs/ — not committed, not causing any issues. Opus to decide if they get committed.
- `*REPORTER CHECK HERE*` marker visible in Stage 1/Stage 2 .txt files (Videographer's opening statement). This is MB's realtime flag for herself — not an error, not something to correct.
- `"lemon wood terrace"` — appears as two words in A. turn idx 96. Correct is "Lemonwood Terrace." Candidate steno artifact for Stage 3.1 to catch.
- `"permit address"` / `"permission address"` — Q. idx 97 / A. idx 98. These look like steno phonetic errors for "permanent address." Strong Stage 3.1 anomaly candidate.
- `"with and T offshore"` — A. idx 110. Likely "Whitney" or "Whiting" — steno untranslate. Strong Stage 3.1 anomaly candidate.
- `"Warren seal"` — A. idx 124. Likely a proper name steno untranslate.

---

## SCOTT'S MOOD / SESSION ENERGY

Methodical and thorough. Scott ran a careful pre-push checklist, authorized the Oracle .sgxml read with explicit covenant language, and requested the full directory inventory before any next steps. No rushing. Establishing solid ground truth before moving forward. Good energy — deliberate, building confidence in the system before running live API calls.
