# HANDOFF — Sonnet to Sonnet
**Date:** 2026-05-10
**Time:** ~11:21 AM
**From:** Sonnet (morning session)
**To:** Fresh Sonnet (tonight ~8 PM)
**Session type:** Structured strategic + inventory grind

---

## 1. RAMP — Read in this order

Fresh Sonnet must read these before doing anything technical tonight.

### Core mindset + rules (in mrx-context/knowledge/ or handoffs/)
1. `CODER_MINDSET.md`
2. `CODER_MINDSET_ADDENDUM.md`
3. `RULE_SHEET_v1.md`

### New knowledge files saved today (READ THESE — they reframe the whole project)
4. `mrx-context/knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md`
5. `mrx-context/knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md`
6. `mrx-context/knowledge/FUTURE_STATE_AGENT_AGENCY.md`

### Most recent Opus handoff
7. `mrx-context/handoffs/HANDOFF_OPUS_2026-05-09_22EOD.md`

### This file
8. `mrx-context/handoffs/HANDOFF_SONNET_2026-05-10_1121.md`

**Note:** The three knowledge files are NEW today — they did not exist before this session. They capture Opus and Scott's full product vision, hard requirements R1-R10, and future-state agent architecture. They significantly change how to think about tonight's recon run. Read them before touching any code.

---

## 2. STATE OF THE WORLD AT TAP-OUT

### mrx-context repo
- **HEAD:** `31f2bc2` — "Add Opus 22EOD handoff — supersedes 8:15 PM version"
- **Status:** 4 untracked items. Scott pushes — do not push.
  - `knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md` (new today)
  - `knowledge/FUTURE_STATE_AGENT_AGENCY.md` (new today)
  - `knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md` (new today)
  - `reports/2026-05-10/` directory (new today, contains spot-check summary + inventory summary)

### mrx_engine_v1
- **Not a git repo** at `C:\Users\scott\OneDrive\Documents\mrx_engine_v1`. Engine code lives there but isn't version-controlled as a repo from this machine. Memory note says HEAD was 8954b61 with 864 passing tests as of 2026-05-09 — treat that as last known state.

### Local-only data (never push)
- `C:\mrx_training_set\MB\` — training data + reports, entirely local
- `C:\Cat4\usr\scott\` — MB's raw archive, 114 folders, entirely local

### Uncommitted items Scott still needs to push (mrx-context)
The three knowledge files + `reports/2026-05-10/` directory are all untracked. Scott pushes when ready.

---

## 3. WHAT SHIPPED TODAY

### Task 1 — Fingerprint Recon Spot-Check
Verified 11 fingerprint patterns (3 recon reports: split, cap, punct) by pulling 20 random samples each from source data. All 11 patterns confirmed REAL.

| Deliverable | Path |
|---|---|
| Full spot-check (local, CONFIDENTIAL) | `C:\mrx_training_set\MB\reports\spot_check_results_2026-05-10.md` |
| Sanitized public summary | `C:\Users\scott\OneDrive\Documents\mrx-context\reports\2026-05-10\fingerprint_spot_check_summary.md` |
| Spot-check script | `C:\Users\scott\AppData\Local\Temp\spot_check_v3.py` |

**Grep status:** Public summary CLEAN against witness-name deny-list.

### Task 2 — Deep Archive Inventory (C:\Cat4\usr\scott)
Full recursive scan. 340 Cat A pairs found across 114 folders.

| Deliverable | Path |
|---|---|
| Full inventory (local, CONFIDENTIAL) | `C:\mrx_training_set\MB\reports\full_inventory_2026-05-10.md` |
| Diff vs prior 7 pairs | `C:\mrx_training_set\MB\reports\inventory_diff_vs_2026-05-09.md` |
| Sanitized public summary | `C:\Users\scott\OneDrive\Documents\mrx-context\reports\2026-05-10\mb_archive_inventory_summary.md` |
| Inventory script (final, deduplicated) | `C:\Users\scott\AppData\Local\Temp\write_final_reports.py` |

**Key numbers:**
- Cat A (sgngl ROUGH + txt/rtf FINAL, directly usable): **340 pairs**
- Cat B genuine (sgngl+sgngl, different sizes): **82 pairs**
- Cat B suspect (same-size sgngl+sgngl, likely auto-backup): **340 pairs**
- Rough-only unique stems: 1,531
- Final-only unique stems: 398
- New Cat A pairs beyond prior 7: **333**

### Task 3 — Year-Bucket Count
340 Cat A pairs bucketed by rough file date.

| Deliverable | Path |
|---|---|
| Year bucket report (local, CONFIDENTIAL) | `C:\mrx_training_set\MB\reports\pair_count_by_year_2026-05-10.md` |

### Task 4 — Three knowledge files
Saved Opus's three strategic documents to `mrx-context/knowledge/`:
- `PRODUCT_VISION_GOLDEN_CIRCLE.md`
- `FINGERPRINT_FACTORY_REQUIREMENTS.md`
- `FUTURE_STATE_AGENT_AGENCY.md`

---

## 4. KEY DECISIONS LOCKED TODAY

1. **Calibration corpus = last 5 years (2022–2026), 243 Cat A pairs.** Scott weights toward recent work — MB's current habits, post-software-update patterns. Decision is Scott's but the data says 71% of the corpus is in this window.

2. **Tonight's recon target: 243-pair corpus (2022–2026).** Fresh Sonnet runs the four recons against these pairs at ~8 PM. Spec from Opus will land before then.

3. **The 333 new pairs validated the gold-miner thesis.** This morning Opus/Scott hypothesized that MB's archive had many more pairs than the 7 already staged. 333 confirmed new Cat A pairs verified that thesis. Archive is the asset.

4. **Fingerprint data architecture spec in progress.** Opus is drafting this now. It will land before tonight's run. Fresh Sonnet reads it before touching any recon script.

5. **Product vision reframed to fingerprint factory.** Not "MB's engine." The factory that produces mini-them for any CR. MB is patient zero. Read PRODUCT_VISION_GOLDEN_CIRCLE.md — it changes how to think about every architectural decision.

---

## 5. WHAT'S NEXT (for fresh Sonnet tonight ~8 PM)

In order:
1. Read all three knowledge files first (PRODUCT_VISION, REQUIREMENTS, FUTURE_STATE)
2. Read HANDOFF_OPUS_2026-05-09_22EOD.md for Opus context
3. Read this file
4. Wait for Opus recon spec (drops before 8 PM)
5. Run the four recons against the 243-pair corpus (2022–2026 Cat A pairs)
6. Save full reports to `C:\mrx_training_set\MB\reports\` (local-only)
7. Save sanitized summaries to `mrx-context/reports/2026-05-10/` (metrics only, grep-verified before push)
8. Report back in chat with results
9. Do NOT push — Scott pushes

**Fresh Sonnet does NOT decide what to run next after recons.** Report results, stop, let Scott and Opus decide.

---

## 6. KNOWN ISSUES & TECH DEBT

| Issue | Status | Notes |
|---|---|---|
| Butler depo rough alignment failure | Known, not fixed | 082222butler rough has only 103 aligned pairs vs ~5k expected. Rough has no header, only 6,491 tokens. Skip or treat as bad-rough when running tonight's recons. |
| TD-003: MB hardcoding in spot-check scripts | Known, not fixed | `spot_check_v3.py` has hardcoded MB paths. Fine for one-off. Production recon layer needs `--cr-initials` flag per R1. |
| `0525black_bp` sanity check | Script bug only | Pair IS in Cat A. Stem check failed due to hyphen/underscore mismatch. Not a real miss. |
| 5 anomalous-date files | Logged, not blocking | 100364nasca, 0825516sewerage, 1000825navient, 1200618cain, 050050324CHURCH parse to 1950s-1982 years. Skip for year-bucketing. Actual dates are 2010-2020 era. |
| 2017–2021 archive gap | Flagged | 2021=0 pairs, 2020/2019/2018/2017 near-zero. Could be MB life events, software change, or naming convention shift. Spot-check candidate if Scott wants to recover those years. |
| 1,531 rough-only files | Logged | Could be unfinalized cases or hidden finals in unusual locations. Not blocking tonight. |
| R11/R12 not built | Future | Pre-recon rough-quality check (catch butler-type failures early) and alignment robustness. Treat alignment failures as expected-possible during tonight's run — log loudly, don't fail silently. |
| Rough files are one giant line | Known | Line 55 of sgngl extract contains all transcript text on a single line. Lines 56-61 are steno word glossary — exclude from alignment. |
| Stage-direction patterns need content-anchor | Implemented in spot_check_v3 | `?(` and `.(` can't use gap-based alignment because the word before `(` differs between rough/final. Use content-anchor approach — find parenthetical content in rough, verify prefix char in final. |

---

## 7. WORKING CONTEXT FOR FRESH SONNET

- **Opus is healthy and sharp.** Handling strategic architecture, product vision, and recon spec for tonight. Trust Opus's framing when the spec drops.
- **Scott is sharp and disciplined.** "One suit first, then suits to the stars." He is not interested in scope creep or premature scaling. Do exactly what the spec says. Stop when the spec says stop.
- **Multiple sessions today.** This morning's session was structured strategic work — knowledge capture + inventory. Tonight's session is data grind — run the four recons against 243 pairs and report results.
- **The three knowledge files are the new foundation.** Before today they didn't exist. Reading them changes how fresh Sonnet should frame every technical decision. The pipeline must be CR-agnostic (R1). The fingerprint schema must separate universal/personal layers (R2). Read REQUIREMENTS.md before writing a single line of code tonight.
- **Communication style:** Plain English, 12-year-old reading level, one thing at a time. Full absolute paths always. Code-fenced blocks for anything Scott pastes to Sonnet. No emojis. No hedging language.

---

## 8. SESSION HEALTH AT TAP-OUT

**Energy level:** Solid. This session had two compacted context windows and resumed cleanly both times. No significant drift. Current context window is fresh from the second compaction — I have headroom.

**Mistakes I caught:**
- Initial inventory script used `(stem, ext)` as canonical key, causing ROUGH.sgngl and FINAL.sgngl to overwrite each other. Caught and fixed in the final `write_final_reports.py`.
- First attempt at writing the inventory script used shell heredoc syntax, which failed. Switched to Write tool.
- The `ToolSearch` had to be called before `Write` could be used — tool schema wasn't loaded from compacted context. Minor friction, fixed immediately.

**What I'd do differently:**
- Run the deduplication logic in a dry-run pass first before writing report files. The over-counting in the first inventory pass required a rewrite.
- Load tool schemas at session start rather than discovering missing ones mid-task.

---

## 9. CONFIDENTIALITY REMINDERS

- `C:\mrx_training_set\` — **LOCAL ONLY. NEVER PUSH.**
- `C:\Cat4\usr\scott\` — **LOCAL ONLY. NEVER PUSH.**
- All 7 paired MB depo FINAL files — **NEVER PUSH.**
- Witness names, case IDs, depo content snippets — **NEVER in any pushed file.**
- Metrics-only sanitized summaries — **CAN push** after grep against MANIFEST.md deny-list.
- MANIFEST.md witness-name deny-list: wunstell, olsen, black, williams, butler, blanks (minimum — check MANIFEST for full list before each push).
- All recon reports with depo text content live in `C:\mrx_training_set\MB\reports\` — local-only.
- Public-pushable reports go to `mrx-context/reports/` — metrics only, grep-verified.

---

## 10. SCOTT'S WORKING STYLE REMINDERS

- **12-year-old reading level.** No jargon, no hedging, no throat-clearing. Say the thing.
- **One question at a time.** Never ask two questions in one message.
- **Inline A/B/C only when there's a real choice** to make. Not for decoration.
- **Code-fenced blocks** for anything Scott copies to Sonnet.
- **Always full absolute paths.** No relative paths in output.
- **Same-day handoffs:** paste key info in chat AND push to repo. But Scott pushes — not Sonnet.
- **Fresh Sonnet does NOT push without explicit per-instance Scott override.**
- **Stop when the spec says stop.** Do not start the next task because you think it logically follows. Scott and Opus decide what's next.
- **Slow is smooth. Smooth is fast.** Don't brute-force through blockers. If something fails twice, ask.

---

---

## ADDENDUM — written ~11:45 AM, after original handoff

The following happened AFTER the 11:21 handoff was written. Fresh Sonnet: read this addendum in addition to the body above.

---

### A1. RAMP UPDATE — Read in this order (supersedes Section 1)

Core mindset + rules:
1. `CODER_MINDSET.md`
2. `CODER_MINDSET_ADDENDUM.md`
3. `RULE_SHEET_v1.md`

Knowledge files (all four, in this order):
4. `mrx-context/knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md`
5. `mrx-context/knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md`
6. `mrx-context/knowledge/FUTURE_STATE_AGENT_AGENCY.md`
7. `mrx-context/knowledge/FINGERPRINT_DATA_ARCHITECTURE.md` ← NEW, added after 11:21

Split manifest (read before touching any recon script):
8. `C:\mrx_training_set\MB\paired\SPLIT_MANIFEST.md`

Most recent Opus handoff:
9. `mrx-context/handoffs/HANDOFF_OPUS_2026-05-09_22EOD.md`

This file:
10. `mrx-context/handoffs/HANDOFF_SONNET_2026-05-10_1121.md` (body + this addendum)

Recon spec from Opus (not yet written at addendum time — drops before 8 PM):
11. Read whatever Opus pastes in chat before the recon kickoff.

**Read FINGERPRINT_DATA_ARCHITECTURE.md before writing a single line of recon code tonight.** It defines the storage schema recon output must conform to.

---

### A2. TRAIN/TEST SPLIT LOCKED

Split is done and locked by Scott. Do not redo it.

| Set | Pairs | Year range |
|---|---|---|
| Training | 195 | 2022–2025 |
| Test | 48 | 2024–2026 |
| Total | 243 | — |
| Overlap | 0 | verified |

**Test year distribution:** 2026: 14, 2025: 33, 2024: 1

**Training year distribution:** 2025: 23, 2024: 63, 2023: 51, 2022: 58

**Key fact about 2026:** ALL 14 of the 2026 pairs are in the test set. Zero 2026 pairs in training. This is by design — 2026 is the time-machine blind test. The most recent year is the most honest blind eval we have. Scott locked this decision: leave it as-is.

**6 case-group adjustments** were made at the train/test boundary to keep multi-day depos intact. All documented in SPLIT_MANIFEST.md.

**Three files at `C:\mrx_training_set\MB\paired\`:**
- `TRAINING_SET.md` — 195 pairs, use this for tonight's recon
- `TEST_SET.md` — 48 pairs, **SACRED. Never load. Never measure against.**
- `SPLIT_MANIFEST.md` — methodology, case adjustments, sanity checks

**Recon tonight runs against TRAINING_SET.md ONLY.** 195 pairs. Not 243. Not the full corpus. The test set is off-limits.

---

### A3. FOURTH KNOWLEDGE FILE SAVED

`mrx-context/knowledge/FINGERPRINT_DATA_ARCHITECTURE.md` — Opus drafted, saved today.

This is the storage schema + consumption contract for the fingerprint. Two sections:

- **Section 1 (Storage schema):** Directory layout, pattern YAML format, event JSONL format, confidence history format, train/test isolation enforcement (3 layers), maturation curve eval methodology, universal/personal layer tagging.
- **Section 2 (Consumption contract):** Query API shape (`FingerprintAccess` class), three-lane routing (AUTO/SUGGEST/FLAG/PROTECTED), confidence update signals (more data + eval + MB feedback), eval runner contract, cross-CR query shape.

**Why this matters for tonight:** The recon scripts tonight should emit output that conforms to this schema — pattern YAMLs in `fingerprint\patterns\`, events in `fingerprint\events\<pattern_id>.matching.jsonl` and `.nonmatching.jsonl`. If Opus's recon spec tonight doesn't fully specify this, flag it before writing output to arbitrary locations.

---

### A4. UPDATED STATE OF WORLD (supersedes Section 2)

**mrx-context repo untracked items (Scott pushes):**
- `knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md`
- `knowledge/FUTURE_STATE_AGENT_AGENCY.md`
- `knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md`
- `knowledge/FINGERPRINT_DATA_ARCHITECTURE.md` ← new since 11:21
- `reports/2026-05-10/` (spot-check summary + inventory summary)
- `handoffs/HANDOFF_SONNET_2026-05-10_1121.md` ← this file

**Local-only (never push), new since 11:21:**
- `C:\mrx_training_set\MB\paired\TRAINING_SET.md`
- `C:\mrx_training_set\MB\paired\TEST_SET.md`
- `C:\mrx_training_set\MB\paired\SPLIT_MANIFEST.md`

---

### A5. WHAT'S NEXT (updated, supersedes Section 5)

Tonight in order:
1. Ramp on all files in A1 above (knowledge files + split manifest + Opus handoff + this file)
2. Receive Opus recon spec in chat (drops before 8 PM)
3. Run the four recons against **TRAINING_SET.md** (195 pairs — NOT 243, NOT the full corpus)
4. Emit output conforming to FINGERPRINT_DATA_ARCHITECTURE.md schema
5. Save full reports to `C:\mrx_training_set\MB\reports\` (local-only)
6. Save sanitized summaries to `mrx-context/reports/2026-05-10/` (metrics only, grep-verified)
7. Report back in chat with results
8. Stop. Scott and Opus decide next move.

Do NOT push. Do NOT start eval against test set. Do NOT start the next task uninstructed.

---

— End of ADDENDUM —

— End of HANDOFF_SONNET_2026-05-10_1121.md —
