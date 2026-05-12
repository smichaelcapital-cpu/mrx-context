# HANDOFF — OPUS — 2026-05-13 EOD

**For:** Fresh Opus, 2026-05-14 morning session
**From:** Opus (2026-05-13 session, tired Scott tapping out ~8 PM EDT)
**Owner:** Scott
**Builder:** Sonnet (separate chat, handoff at `handoffs/HANDOFF_SONNET_2026-05-13_EOD.md`)

---

## STOP. Before responding to Scott, answer these:

1. **What is the product?** "My reporter, but multiplied." MRX fixes transcripts like the specific court reporter would have, not like a generic editor.
2. **What's live today?** Fingerprint v0 (em-dash rule enforcing on Halprin), Halprin front matter end-to-end (11 pages), recovered orchestrator on main.
3. **What does Scott want tomorrow morning?** A REVIEW of the locked 5-stage audio design (Stages A–E), capturing his questions, then a build-ready design refinement, then a plan to split into two parallel Sonnet workstreams.

If you can't answer all three from this doc, RE-READ.

---

## STANDING RULES — NON-NEGOTIABLE

1. 12-year-old reading level. Plain English. Short answers.
2. ONE question at a time. Never stack.
3. Always full absolute paths.
4. Inline A/B/C only when there's a real choice.
5. When unsure, make a recommendation — don't ask open-ended questions.
6. Sonnet writes files and runs shell. Scott pushes commits. Opus writes specs.
7. SHAPE MATCH ONLY. Never byte-match a hand-typed fixture.
8. 5-line answers.
9. Anything for Sonnet goes in a code block. Anything outside is for Scott.
10. Before any code change ask: "Could this reduce transcript accuracy or credibility?" If yes/maybe, STOP and flag.

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-03_SUNDAY_ADDENDUM_ARCHITECTURE.md — THIS IS THE AUDIO DESIGN. Read it carefully.
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/fingerprint_architecture_decisions.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-13_repo_inventory_audio_fingerprint_discovery.md — full asset inventory
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/fingerprints/ledger.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-13_EOD.md
9. This handoff

After ramp: confirm "Ramped Opus 2026-05-14 fresh. Ready." plus one sentence on state.

---

## ONE-LINE STATE

Front page appearances fix is unfinished and parked (Sonnet spun on 3-in-one-pass). Main is clean with all 8 front matter renderers restored. Scott wants tomorrow to be 50% appearances cleanup + 50% audio architecture review with potential two-Sonnet parallel build kicked off.

---

## YESTERDAY'S WINS

1. Recovered orchestrator + overflow-capable index.py to main (commit a5e1628). Lost code was never actually lost — backup branch saved us.
2. Discovered and documented the silent merge gap (front-matter/index branch merge to main dropped 2 files).
3. Created `STATE_OF_MRX.md` discipline (single source of truth pointer — see file pointers section below).
4. 3 shape defects identified by Scott eyeball on Halprin render. Proves eyeball-gate works.

---

## YESTERDAY'S NEAR-MISSES (LESSONS BAKED IN)

1. **Branch cleanup before verifying merge** — deleted front-matter/index thinking it was fully merged. Saved by the backup branch we created that morning. **Rule baked in:** backup branch before any cleanup. Always.
2. **Silent thinking past 24 minutes** — Sonnet went heads-down on the appearances fix and never came up for air. **Rule baked in:** 30-minute wall on every build pass. Hard stop.
3. **3 fixes in one pass** — KEEP-TOGETHER + Reported by anchor + ALSO PRESENT was too much. **Rule baked in:** one fix per branch. Three small ships beat one big spin.

---

## TODAY'S FIRST MOVE — TWO PARTS

### Part 1 — Help Scott close the appearances fix (probably 1-2 hours)
Sonnet has a stale fix branch. Inspect it. Either salvage or restart with TIGHT scope:
- Pass 1: Issue 1 (KEEP-TOGETHER) only. One test. Ship.
- Pass 2: Issue 2 (Reported by anchor). One test. Ship.
- Pass 3: Issue 3 (ALSO PRESENT) only if not auto-resolved.

Spec is at `specs/2026-05-13_APPEARANCES_OVERFLOW_AND_BACK_MATTER_SPACING.md`. Scott already signed off all 3 open questions.

When all 3 pass, Scott eyeballs the new render side-by-side with `io/halprin_FINAL_compare_2026-05-12.txt`. Locks the front page win.

### Part 2 — THE BIG ONE: Audio architecture review with Scott

**Scott's exact ask:** "I prefer to start from scratch. You laid out the steps, like, five or six chunks, and I had questions about them... it'll be easier with the new Opus if you can have them bring me up to that point."

**What this means:** Walk Scott through the 5-stage audio stack from the 5/3 addendum. He has questions. Capture them. This is a REVIEW conversation, not a redesign — the architecture is locked. The conversation will refine details and surface gaps.

**The 5 stages (from `handoffs/HANDOFF_OPUS_2026-05-03_SUNDAY_ADDENDUM_ARCHITECTURE.md`):**
- **Stage A — Aligner+Differ.** Reads MB FINAL against MB raw line-by-line. Every diff = labeled training example. Habitual → fingerprint. Case-specific → per-depo. Stage A produces the data foundation everything else stands on.
- **Stage B — Whisper integration.** Whisper transcribes audio. Output aligned to turns. Second source for triangulation. Halprin audio is on disk (79MB .opus). Brandl Whisper output already exists.
- **Stage C — Comprehension Agent + Case Brief.** One expensive call (~$3-5) reads Whisper + steno + fingerprint. Outputs 5-10KB JSON Case Brief (witness identity, employer history, key people, addresses, terminology, names, facts).
- **Stage D — Brief-aware defect-finder.** Replaces 60-batch cold finder. Each batch carries Case Brief + candidate. Smarter, possibly cheaper.
- **Stage E — Resident Oracle fallback.** For hard cases. Load full context, query directly. Surgical use only.

**Triangulation principle:** Steno says X, Whisper says Y, Case Brief says Z. Three independent signals = high-confidence fix.

---

## SCOTT'S QUESTIONS — ANTICIPATED FROM YESTERDAY'S CONVERSATION

1. **On Stage A:** "We have 198 depos — how do we leverage them?" — Inventory shows we have 4 MB depos with usable data (Halprin full triple, Brandl FINAL+audio, Easley pair, jp_042726 raw+audio missing FINAL) + 5 AD raws + 7 FINAL-only oracles. **The 198 number is not yet verified** — Scott may have a larger library elsewhere we haven't inventoried. Confirm with Scott.
2. **On time-slicing:** Scott mentioned "Whisper with specific time slices, the way a real steno or scopist would do it and match up the steno with the time slice." That's a Stage B implementation detail. Worth a focused discussion.
3. **On 198 leverage:** If 198 exists, Aligner+Differ at scale produces the MB fingerprint from data not hand-coded rules. That's the big leverage.

---

## TWO-SONNET PARALLEL — SCOTT'S TOMORROW PLAN

Scott wants two Sonnets grinding tomorrow on independent chunks. Audio splits naturally:
- **Sonnet A**: Stage A (Aligner+Differ)
- **Sonnet B**: Stage B (Whisper integration)

They're independent enough that they don't step on each other. Meeting point is when output feeds Stage C.

**Caution baked in:** Today's near-misses happened with ONE Sonnet. Two Sonnets = double the change-management discipline. Branch-per-task is the rule. Backup before cleanup. Recon gate every time. Yesterday's broken merge would have been twice as bad with two Sonnets pushing.

Scott named it: this is a use case to harden change management. Better to find cracks tomorrow than later under pressure.

---

## FILE POINTERS — FULL PATHS, NO ABBREVIATION

### Repos
- Engine: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\
- Context: C:\Users\scott\OneDrive\Documents\mrx-context\
- Depo library: C:\Users\scott\OneDrive\Documents\mrx_depo_library\

### Architecture & design docs (read these to understand the WHY)
- mrx-context\knowledge\PRODUCT_VISION_GOLDEN_CIRCLE.md — North star
- mrx-context\knowledge\fingerprint_architecture_decisions.md — 4-layer model, locked
- mrx-context\knowledge\FINGERPRINT_DATA_ARCHITECTURE.md — Full data schema
- mrx-context\knowledge\FINGERPRINT_FACTORY_REQUIREMENTS.md — Factory requirements
- mrx-context\knowledge\FUTURE_STATE_AGENT_AGENCY.md — Agent autonomy design
- mrx-context\design\fingerprint_architecture_copilot_2026-05-08.md — Outside review
- mrx-context\handoffs\HANDOFF_OPUS_2026-05-03_SUNDAY_ADDENDUM_ARCHITECTURE.md — THE AUDIO DESIGN
- mrx-context\handoffs\HANDOFF_OPUS_2026-04-26_1210pm.md — Stage 0.5 Whisper, Stage 3.5 audio vote

### Specs
- mrx-context\specs\2026-05-09_FINGERPRINT_V0_SPEC.md — v0 build (shipped)
- mrx-context\specs\2026-05-10_OVERNIGHT_RECON_SPEC.md
- mrx-context\specs\2026-05-13_APPEARANCES_OVERFLOW_AND_BACK_MATTER_SPACING.md — TOMORROW'S FIRST FIX

### Fingerprint files (the live data)
- mrx-context\fingerprints\_template.yaml
- mrx-context\fingerprints\reporters\MB.yaml — v0, em-dash forbidden
- mrx-context\fingerprints\ledger.md — 18 rows of MB-vs-universal decisions

### Engine — fingerprint subsystem (in production)
- mrx_engine_v1\src\mrx_engine_v1\fingerprint\loader.py
- mrx_engine_v1\tests\fingerprint\test_loader.py — 13 tests

### Engine — front matter renderers (all 8 on main as of a5e1628)
- mrx_engine_v1\src\stage5\front_matter\cover.py
- mrx_engine_v1\src\stage5\front_matter\index.py (overflow version, recovered)
- mrx_engine_v1\src\stage5\front_matter\orchestrator.py (recovered)
- mrx_engine_v1\src\stage5\front_matter\appearances.py (the one to fix tomorrow)
- + stipulation, reporter_cert, witness_cert, errata

### Knowledge captures (read for context)
- mrx-context\knowledge\2026-05-12_intake_package_todo.md
- mrx-context\knowledge\2026-05-12_MB_front_matter_workflow.md — MB does all 5 pages
- mrx-context\knowledge\2026-05-12_NY_workers_comp_pipeline.md
- mrx-context\knowledge\2026-05-13_repo_inventory_audio_fingerprint_discovery.md — Full asset inventory

### Render outputs
- mrx-context\io\halprin_full_render_2026-05-12.txt (21,705 raw / 20,834 normalized)
- mrx-context\io\halprin_FINAL_compare_2026-05-12.txt (20,834 — MB FINAL extract for shape comparison)
- mrx-context\io\halprin_full_render_2026-05-12.BACKUP.txt

---

## DATA INVENTORY (5/13 ACCURATE)

| Asset | Count | Status |
|---|---|---|
| MB raw+FINAL+audio triple | 1 (Halprin) | gold standard |
| MB FINAL+audio (no raw) | 1 (Brandl) | usable |
| MB raw+FINAL pair (no audio) | 1 (Easley) | usable |
| MB raw+audio (no FINAL) | 1 (jp_042726) | blocked until MB sends FINAL |
| AD/other raws | 5 | cross-depo scan only, no FINALs |
| FINAL-only oracles | 7 | shape testing only |
| Whisper outputs already run | 1 (Brandl 0-40min) | already on disk |

**Open question for Scott:** Are there more depos somewhere we haven't inventoried? He mentioned 198. Inventory shows 16.

---

## OPEN ITEMS QUEUED

1. ⏳ Appearances overflow fix — restart tomorrow with tight scope
2. ⏳ Audio architecture design review with Scott
3. Intake package spec deliverable — 6-week ask, still owed to MB
4. Williams renderer generalization — second depo for fingerprint validation
5. LA state guidelines parsing — unlocks 6 ambiguous MB.yaml classifications
6. jp_042726 FINAL when MB sends it
7. NY workers' comp files when received

---

## SCOTT'S STATE AT EOD

Tired but clear. Ran a long session. Maintained discipline through 3 near-misses (deleted branch saved by backup, missing orchestrator caught by recon, byte delta caught by diagnostic). Wants tomorrow to start clean with audio design review and aimed at two-Sonnet parallel. Recognizes change management has to be airtight before more parallel work.

Closing quote: "Good plumbing right there." The plumbing held.

— End of Opus 2026-05-13 EOD handoff —
