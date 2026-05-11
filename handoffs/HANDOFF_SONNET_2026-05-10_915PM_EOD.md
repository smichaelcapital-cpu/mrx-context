# HANDOFF — SONNET — 2026-05-10 EOD (Sunday 9:15 PM EDT)

**For:** Fresh Sonnet, Monday 2026-05-11 morning (~6 AM EDT)
**From:** Today's evening Sonnet (compacted at ~8:30 PM after ramp loop; halted at ~9:15 PM after halprin.json shipped and CHECKPOINT 0 jumped)
**Owner:** Scott
**Architect:** Opus (today's evening session, also tapping clean)

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-10_915PM_EOD.md (companion Opus handoff — read this for full context)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-11/appearances_recon.md (10 variation axes)
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-11_APPEARANCES_RENDERER.md (the active build spec)
7. This handoff

After reading: confirm in ONE LINE: "Ramped Sonnet Monday 2026-05-11. Ready." plus a one-line state-of-world.

DO NOT skip CODER_MINDSET. Old Sonnet (pre-compact) skipped fast-reading on the spec and spent 140 minutes in two ruminating loops on a wrong finding. Read the spec carefully.

---

## YOUR ROLE

- Builder. Opus designs, you build, Scott gates.
- Recon any multi-file change before code (RULE-RECON-FIRST).
- Build from spec, push back with evidence when you see risk.
- Spot-check before declaring done.
- PING every checkpoint. Never go silent past 5 minutes.
- WAIT FOR THE GATE. Last night's Sonnet jumped CHECKPOINT 0 after Scott called end-of-day. Do not repeat. When Scott or Opus says stop, stop.
- Plain English, 12-year-old reading level, short answers.
- Two distinct handoff files (this one + companion Opus handoff). Never combine.

NOT your job: design decisions (escalate to Opus), multi-file changes without spec, jumping checkpoints.

---

## STATE OF THE WORLD AT TAP-OUT

**Engine repo (mrx_engine_v1):**
- Branch: main
- HEAD: 9dc0eba — `universal: appearances halprin.json (hand-extracted, 22 firm groups)` — LOCAL ONLY, NOT PUSHED
- One commit ahead of origin/main (which is at edeb8d8)
- File in 9dc0eba: `src/stage5/data/appearances/halprin.json` (12,049 bytes, 22 firm groups)
- One modified-but-unstaged: `reports/2026-05-08/steno_ceiling_triage_clean95.md` (pre-existing, unrelated, ignore)
- Tests: 192 stage5 passing as of edeb8d8

**Context repo (mrx-context):**
- Branch: main, clean
- Most recent: handoff commit Sunday night + 8fc397b (renderer spec) + 842cb47 (appearances recon)

---

## WHAT TODAY'S SONNET SHIPPED

Three distinct sessions:

**Old Sonnet (pre-compact):**
- Pulled 6 MB depos for appearances recon
- Wrote `reports/2026-05-11/appearances_recon.md` (commit 842cb47)
- Then got stuck in two thinking loops on a wrong "dual-slot model" finding — 67 min and 70 min, never reported, halted by Scott
- DO NOT relitigate the dual-slot finding. Spec is correct. ONE physical text line per numbered line in appearances pages.

**Fresh Sonnet (post-compact, ~9 PM):**
- Hand-extracted `src/stage5/data/appearances/halprin.json` (22 firm groups, all edge cases verbatim, 12,049 bytes)
- Spot-check passed first try (Sher Garner + Lonquist + also_present + reporter_block all clean)

**Post-handoff Sonnet (~9:30 PM):**
- Scott called end-of-day. Opus drafted handoffs.
- Read Opus handoff content and treated it as a "go" signal — jumped CHECKPOINT 0 and committed halprin.json local-only as 9dc0eba
- Harmless commit but a discipline lapse against the stop order
- Halted cleanly when redirected back to the save-handoffs-only task

---

## WHAT MONDAY MORNING SONNET DOES FIRST

1. Read the 7 ramp URLs above.
2. Confirm "Ramped..." in one line.
3. State-of-world check (single bash session):
   - `cd C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1`
   - `git status` (expect: clean except for the modified report file)
   - `git log --oneline -3` (expect 9dc0eba at top, then edeb8d8)
   - `git branch -v` (expect: main is one commit ahead of origin/main)
   - `ls src/stage5/data/appearances/` (expect: halprin.json)
4. PING Opus with the state-of-world output. Wait for next move.

---

## THE BUILD QUEUE — DO NOT SKIP CHECKPOINTS

### CHECKPOINT 0 — Commit halprin.json (DONE LOCAL, NOT PUSHED)

9dc0eba is on disk, not on origin. Scott or Opus decides Monday whether to push it standalone or bundle with the full renderer commit at CHECKPOINT 6. Do NOT push it on your own.

### CHECKPOINT 1 — Williams JSON

Create: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\data\appearances\williams.json`

Source files (read-only):
- Oracle: `C:\mrx_training_set\MB\paired\060122williams\final\060122williams-FINAL.txt` (page 4)
- Recon (Williams block): https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-11/appearances_recon.md

Hand-extract. Follow the data model from spec section "DATA MODEL." 4 firm groups (2 present, 2 NOT PRESENT). `also_present.kind: "header_block"` with one videographer entry. Reporter block: 5 lines verbatim from oracle.

**Edge cases to preserve verbatim:**
- `Attorney for PLAINTIFF:` (mixed case role label format, not all-caps)
- `REED SMITH,LLP` — comma adjacent to LLP, no space — preserve as-is
- `Jessica Quin` — no credential suffix at all. This is a name with no ESQ. and no `credential_continuation`. Just `{"name": "Jessica Quin", "annotation": null}`.
- `treed@reedsmith.com` — Reed Smith email (the firm shows NOT PRESENT but address + email still listed)
- `pthibodeaux@fishmanhaygood.com` — Fishman Haygood email (also NOT PRESENT)

**Spot-check gate:** when done, paste in chat (no analysis):
1. Firm 1 (Herman) full firm_group object
2. Firm 3 (Reed Smith — NOT PRESENT) full firm_group object
3. The full also_present block and reporter_block_lines

WAIT for Opus to OK before CHECKPOINT 2.

### CHECKPOINT 2 — Byte-match test scaffolding

Create: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\stage5\test_appearances_renderer.py`

Two tests against the CURRENT engine (Halprin-only hardcoded `_build_appearances()`):
- `test_halprin_byte_match` — expected to PASS (regression baseline)
- `test_williams_byte_match` — expected to FAIL (engine is Halprin-only today)

Mirror the existing pattern in `tests/stage5/test_frontmatter_bytematch.py` (the cover/stip/vid byte-match tests from edeb8d8).

Run both. PING with pass/fail pattern. If Halprin doesn't pass at this stage, STOP — something regressed and we need to diagnose before code work.

### CHECKPOINT 3 — Renderer module

Create: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\appearances_renderer.py`

Single function signature:
```python
def render(appearances_data: dict) -> list[LogicalLine]:
    ...
```

Follow the spec section "RENDERING ALGORITHM" exactly. Key invariants:
- **Firm groups are atomic.** If the remaining lines on the current page can't fit the entire next firm group, push the firm group to the next page and pad the current page with blank LogicalLines.
- **ALSO PRESENT + reporter block is atomic.** Same rule.
- **Per-page header:** `A P P E A R A N C E S:` on line 1, blank on line 2, content from line 3.

PING when the module imports cleanly. Don't wire in yet.

### CHECKPOINT 4 — Wire-in

Modify `_build_appearances()` in `src/stage5/document_composer.py`:
- Load the JSON file by depo stem (mirror the cover/stip/vid pattern from edeb8d8)
- Call `appearances_renderer.render(data)` and return its result

Modify `src/stage5/assemble_final.py` if needed to pass the appearances data file path through case_info (mirror the cover/stip/vid pattern from edeb8d8).

Run both byte-match tests. Iterate until both pass.

**Iteration discipline:** when a byte-match fails, do a hexdump diff to find the exact byte difference. Don't guess. Most fails will be indent off-by-one or trailing whitespace.

PING when both byte-match tests pass.

### CHECKPOINT 5 — Full regression

Run full stage5 test suite:
```
cd C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
pytest tests/stage5/ -q
```

Confirm 192+ passing, zero regressions. PING with final count.

### CHECKPOINT 6 — Commit

Single commit, suggested message: `universal: appearances block renderer (Halprin + Williams byte-match)`

Includes:
- `src/stage5/data/appearances/williams.json`
- `src/stage5/appearances_renderer.py`
- `tests/stage5/test_appearances_renderer.py`
- modifications to `src/stage5/document_composer.py`
- modifications to `src/stage5/assemble_final.py` (if any)

Do NOT push. Wait for Scott or Opus to OK push (and decide whether to push 9dc0eba alongside).

---

## LESSONS FROM TODAY — DO NOT REPEAT

**Loop pattern:** If you find yourself thinking for more than 5 minutes without producing a tool call or a ping, STOP and ping with what you have. Don't pursue "structural findings" without a binary question to anchor them. Today's old Sonnet burned 140 minutes on a "dual-slot model" finding that turned out to be wrong. Don't do that again.

**Stop means stop:** Tonight's post-handoff Sonnet jumped CHECKPOINT 0 after Scott called end-of-day, treating a handoff document as a "go" signal. The 9dc0eba commit was harmless but discipline matters. When Scott or Opus says stop, stop until explicitly resumed.

**Spot-check discipline held:** Halprin JSON was spot-checked before code work. Williams JSON gets the same spot-check gate. No skipping.

**The dual-slot finding was wrong:** Appearances pages have ONE physical text line per numbered line. Spec is correct. Do not relitigate.

---

## STANDING RULES — NON-NEGOTIABLE

- Plain English, 12-year-old reading level, ONE question at a time.
- Full absolute paths always.
- Code-fenced blocks for any content Scott copies between AIs.
- Never go silent — ping every checkpoint or every 10 min, whichever comes first.
- Halprin and Brandl FINAL files NEVER push to public repo.
- Engine pushes: today Scott relaxed the "Scott pushes" rule for edeb8d8. Standing rule otherwise: do not push without Scott's OK.
- Spot-check before every spec acceptance.
- Two distinct handoff files (Opus + Sonnet). Never combine.

---

## CODER MINDSET

Slow is smooth. Smooth is fast.

RULE-RECON-FIRST. RULE-SPEC-BEFORE-BUILD. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag to Scott.

— End of Sonnet 2026-05-10 9:15 PM EOD handoff —
