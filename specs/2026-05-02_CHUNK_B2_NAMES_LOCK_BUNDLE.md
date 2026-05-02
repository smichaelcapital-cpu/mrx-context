# CHUNK B'' — Warren Seal + W&T Offshore NAMES_LOCK Bundle

**Date:** 2026-05-02 (overnight session, written by Opus 2026-05-01 EOD)
**Author:** Opus
**Builder:** Sonnet
**Owner:** Scott
**Type:** Single NAMES_LOCK edit + one Stage 3.1 re-run + Stage 5 re-render. ~$0.95.

---

## TRUTH SOURCES

Engine repo:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\

File to edit:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_run_halprin_mini.py
  (search for `NAMES_LOCK` constant)

Stage 3.1 output target (will be regenerated):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage3_1_out\

Stage 5 output target (will be regenerated):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt

Recon report this spec is built on:
  https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/results/2026-05-02_RECON_V2_MISSES_RESULTS.md

Reference pattern (Lemonwood, Chunk B'):
  Engine commit e7989e3 — `feat(stage3): add Lemonwood Terrace to NAMES_LOCK (V2 miss fix #1)`

---

## ONE-LINE GOAL

Add "Warren Seal" and "W&T Offshore" to NAMES_LOCK so Writer produces high-confidence REWORDs on the 1 Warren Seal occurrence (turn 124) and 9 `with and T` occurrences (turns 110-113 + 201-210) that Reader already flagged but Writer skipped or under-served.

---

## WHY (recon-grounded, in plain English)

Per recon report:

- **Warren Seal:** Reader flagged turn 124 with category `name_uncertain`, confidence `high`. Writer produced ZERO proposals. Writer is structurally cautious about proper-noun capitalization without a NAMES_LOCK anchor. Adding "Warren Seal" gives Writer the confidence anchor it needs.

- **W&T Offshore:** Reader flagged 9 turns (110, 111, 113, 201, 202, 204, 206, 208, 210) all at high confidence as `steno_artifact` ("with and T" → suspected company name). Writer proposed REWORDs only for batch 1 (turns 110-113). Batches 2+ Writer skipped despite identical Reader signal — likely because Writer treats "W&T" as ambiguous without a NAMES_LOCK entry. Adding "W&T Offshore" disambiguates.

Both fixes are the same architectural pattern as Lemonwood Terrace (Chunk B', commit e7989e3). Same risk profile. Same expected behavior.

---

## RECON CHECKPOINT (Sonnet does this BEFORE editing)

**STOP after recon. Post results in chat. Wait for Opus approval before building.**

### Recon Task 1: Locate NAMES_LOCK current state

Open `_run_halprin_mini.py`. Find the `NAMES_LOCK` constant. Quote it in full (all categories, all entries). Confirm the structure (is it categorized like `# People` / `# Companies` / `# Addresses / streets`?).

### Recon Task 2: Confirm category placement

Per recon report, "Warren Seal" is a person and "W&T Offshore" is a company.

- Confirm there is a `# People` category in NAMES_LOCK (Halprin, Caughey, Garner, Muir, Guastella should be there).
- Confirm there is a `# Companies` category (Westlake, Eagle, Calcasieu, Somerset, Chevron, Lexitas should be there).

If either category is missing or named differently, report exact names and stop for Opus to update spec.

### Recon Task 3: Confirm neither name is already present

Grep NAMES_LOCK for "Warren" and "W&T" (case-insensitive). Report any hits. If either is already present, STOP.

### Recon Task 4: Confirm test suite is currently green

Run `pytest tests/ -q`. Report passing/failing/skipped counts.

### Recon Task 5: Confirm engine + context repos clean

```cmd
cd C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
git status
git log --oneline -3

cd C:\Users\scott\OneDrive\Documents\mrx-context
git status
git log --oneline -3
```

Report. Both should be clean on main.

Post recon report in chat. Don't edit anything yet.

---

## BUILD STEPS (after Opus approves recon)

### Step 1: Edit NAMES_LOCK

Add `"Warren Seal"` to the People category. Add `"W&T Offshore"` to the Companies category. Match existing formatting style exactly (string quotes, comma placement, indentation).

If categories are alphabetized within themselves, insert in alphabetical order. If not, append to end of category. Match the existing convention.

### Step 2: Run Stage 3.1 + Stage 5 end-to-end

Use the same invocation pattern as the Lemonwood Chunk B' run. Watch for:

- Cost approximately $0.95 (acceptable range $0.85–$1.05; flag if outside)
- All batches complete (no cost-ceiling hits)
- No new error messages relative to last clean run

### Step 3: Verify the fixes

**Warren Seal (turn 124):**
1. Find turn 124 in OUR_FINAL.txt. Quote the marker.
2. Expected: `{{MB_REVIEW-FIX: confident — ...}}Warren Seal{{/}}`
3. Check proposals.json for the new proposal: should have `before: "warren seal"` (or similar), `after: "Warren Seal"`, `op_type: REWORD`, `source: "names_lock"`.

**W&T Offshore (turns 110-113 + 201-210):**
1. For each of the 9 flagged turns, report whether it now has `MB_REVIEW-FIX: confident` or still shows VERIFY/FLAG.
2. Report the count of new W&T-related REWORD proposals in proposals.json.

### Step 4: Acceptance — Three explicit checks

1. **No regression.** `pytest tests/ -q` still passes at baseline count.
2. **No silent normalization.** Spot-check 3 random non-target turns — confirm text unchanged.
3. **Lemonwood didn't regress.** Confirm turn 96 still shows `{{MB_REVIEW-FIX: confident — ...}}Lemonwood Terrace{{/}}`.

---

## END-OF-CHUNK LOG ENTRY (Sonnet appends to HANDOFF_LOG.md)

Append to current 2026-05-01 session block:

```
CHUNK B'' — Warren Seal + W&T Offshore NAMES_LOCK bundle (SHIPPED)
Status: Complete. Pushed by Scott. [N] tests passing.
What it did: Added "Warren Seal" (People) and "W&T Offshore"
(Companies) to NAMES_LOCK in _run_halprin_mini.py. Re-ran Stage 3.1
end-to-end + Stage 5 re-render.
Stage 3.1 cost: $[X.XX] (target ~$0.95)
V2 miss results post-Chunk B'':
  - Warren Seal turn 124: [marker quote]
  - W&T Offshore turns [list]: [N of M] now FIX confident, [P of M] still VERIFY/FLAG
  - Lemonwood turn 96: still FIX confident ✓ (no regression)
V2 miss scoreboard at session close:
  - Original 10 misses
  - 4 fixed in V2 (your, permission/permit, under paid, plus original Lemonwood flag)
  - Bug 1 fix added: No no (silent win, recon discovery)
  - Chunk B' fix: Lemonwood Terrace REWORD
  - Chunk B'' fix: Warren Seal + W&T Offshore (this chunk)
  - Remaining open: 25 years ago (deferred, format-rule decision), flew into give (audio-dependent)
Commits:
  [hash] feat(stage3): add Warren Seal + W&T Offshore to NAMES_LOCK
```

---

## EDGE CASES + WATCHOUTS

1. **Bundling violates Section 1 of decision tree** — Section 1 said "do not add Warren Seal AND with-and-T to NAMES_LOCK in the same commit." We're doing it anyway because Scott explicitly chose to maximize the $0.95 run. Attribution risk mitigation: each name is one line of code, easily diffable. If something goes weird, `git revert` the commit and re-add one at a time.

2. **W&T might not all auto-fix.** Recon shows Reader flagged 9 turns. Writer might still skip some after NAMES_LOCK addition. If only batch 1 fixes plus a few others, that's still a partial win. Report exact counts — don't paper over partial results.

3. **The "with and T" → "W&T Offshore" full string match** — Stage 2 text contains "with and T offshore" (lowercase, separated). Writer's job is to recognize this is steno fragmentation of "W&T Offshore". NAMES_LOCK provides the target string. Confidence will depend on Writer's pattern matching.

4. **Don't touch Reader or Writer prompt.** This chunk is data-only (NAMES_LOCK addition). If recon shows the prompt would need changes too, STOP — that's a separate spec.

5. **`*REPORTER CHECK HERE*` is in Stage 2 text.** Don't be confused by that marker during verification. It's MB's intentional flag from the rough RTF. Not an error.

---

## ROLLBACK PLAN

```cmd
cd C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
git revert [chunk-b''-commit-hash]
```

Then re-run Stage 3.1 (~$0.95 to recover).

---

## OPEN ITEMS DEFERRED OUT OF THIS CHUNK

- **25 years ago** — needs Writer-rule decision. Separate future spec.
- **flew into give** — audio-dependent. Parked per decision tree.
- **Bug 2 / Chunk E** — parked, hard-gate.
- **Diff methodology lockdown** — owed before any future "diff line count" acceptance criterion.

— End of Chunk B'' spec —
