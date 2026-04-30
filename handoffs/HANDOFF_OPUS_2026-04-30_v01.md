# MID-SESSION HANDOFF — OPUS → OPUS — 2026-04-30

**Session start:** Evening 2026-04-30, ~5:00 PM
**Handoff written:** Thursday 2026-04-30, 6:48 PM
**Reason for handoff:** Outgoing Opus end of context window. Fresh Opus tomorrow writes the new Stage 3.1 Reader prompt.

---

## RAMP — 60-SECOND VERSION

Read this section only. Skip everything else unless needed.

**WHO:** Scott, founder of MyReporterX. End of long Thursday. Tired but locked in on next move.

**TONIGHT'S WORK (already done):**
- Reviewed `HALPRIN_MINI_3WAY_DIFF.md` audit
- Categorized 1,027 diff lines into 4 patterns, ~22 real defects
- Agreed Cat 1 (steno artifact correction by Stage 3.1) is the hardest and highest value
- Long design discussion on two-agent architecture (Comprehension Agent + Correction Agent)
- Agreed: tonight, do NOT build the Comprehension Agent yet
- Agreed: tonight's first move is to refactor the existing Stage 3.1 prompt(s), re-run Halprin mini, see if defect count moves
- Sonnet published current Stage 3.1 state to git: `mrx-context/stage3_1/STAGE3_1_CURRENT_STATE_2026-04-30.md`
- Discovered Stage 3.1 is already two agents (Reader finds anomalies, Writer proposes fixes). The refactor target is the **Reader prompt** because Reader is the one missing defects — if Reader doesn't flag a homophone, Writer never gets a chance to fix it.
- Outgoing Opus called context window concerns, recommended fresh Opus write the new prompt tomorrow

**WHAT FRESH OPUS DOES (tomorrow morning):**
1. Read `mrx-context/stage3_1/STAGE3_1_CURRENT_STATE_2026-04-30.md` — the current Reader and Writer prompts, output schema, per-call input context
2. Read `mrx-context/audits/HALPRIN_MINI_3WAY_DIFF.md` — the defect categories
3. Rewrite the Stage 3.1 Reader prompt (and minor Writer prompt updates if needed) targeting the defect categories from the audit
4. Send Sonnet a spec to: swap in new prompt(s), no other code changes, re-run Halprin mini, run the same audit script
5. Compare defect count before vs after, by category
6. Report results to Scott

**SCOTT'S MOOD:** Tired but engaged. Pushed back hard tonight when outgoing Opus ramped on the wrong (older) handoff and started re-litigating settled work. Recovery happened. Stay sharp tomorrow.

---

## SCOTT'S WORKING STYLE — CRITICAL

- 12-year-old reading level until told otherwise
- Plain English, short answers
- ONE question at a time (NOT three)
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses
- Does NOT want to be Claude's hands — Sonnet writes files
- ALWAYS full absolute paths, never abbreviated
- Pushes back when wrong — pushback is usually right
- Will lose patience FAST on obvious clarifying questions
- **NEVER make Scott the copy-paste mule.** When Opus needs information from Sonnet that's longer than a few lines, Opus tells Sonnet to write it to a file in `mrx-context`, push to git, and reply with just the raw URL. Opus fetches directly. Same rule in reverse — when Opus has long output (handoffs, specs, audits) for Sonnet to act on, Opus tells Sonnet to write it directly, never dumps long markdown into chat for Scott to manually paste. Before pushing, Opus prompts Scott with the proposed git path ("Going to have Sonnet write to `mrx-context/[folder]/[filename].md` — okay?") for approval.

**LESSON FROM TONIGHT:** Outgoing Opus ramped on `HANDOFF_OPUS_2026-04-29_v02.md` (mid-day) instead of `HANDOFF_OPUS_2026-04-29_v03.md` (late night). Result: 45+ minutes wasted treating yesterday's defects as fresh discovery. Scott had to manually paste v03. **Always check for the latest handoff before assuming you're caught up.** If a handoff feels stale, ask.

---

## TIER 1 + TIER 2 STATUS (unchanged from v03)

**DONE:**
- ✅ Cover, stipulation, appearances+index, videographer opening (all literal templates)
- ✅ Pages 1-13 of OUR_FINAL Halprin byte-match MB
- ✅ Three-way diff audit shipped to `mrx-context/audits/`

**REMAINING TIER 2:**
- Certificates component (back matter)

**TIER 3 (later):**
- Generalize hardcoded literals into slots (per-CASE, per-CR, per-STATE)

---

## THE STAGE 3.1 REFACTOR — DETAILED PLAN

**Goal:** Rewrite the Stage 3.1 Reader prompt (and minor Writer updates if needed) to catch the defect categories Halprin mini exposed, without changing pipeline architecture or building new agents.

**Defect categories the new prompt must address (from `HALPRIN_MINI_3WAY_DIFF.md`):**

1. Homophones the witness restates ("permit address" / "permission address" → "permanent address")
2. Homophones in standard ceremony language ("your sworn under oath" → "you're sworn under oath")
3. Garbled company names that should be acronyms ("with and T" → "W&T")
4. Proper nouns split into common words ("lemon wood terrace" → "Lemonwood Terrace")
5. Proper nouns lowercase that should be capitalized ("Warren seal" → "Warren Seal")
6. Compound words split ("under paid" → "underpaid")
7. Self-corrections missing em-dashes ("No no" → "No -- no")
8. Number format per CR convention ("25 years ago" → "Twenty-five years ago")

**Constraints on the new prompt:**

- Few-shot examples MUST use different words than Halprin's actual defects (no W&T, no Lemonwood, no your/you're, no underpaid, no Warren Seal). Use similar patterns with different words. Otherwise Halprin re-run is a memorization test, not a real test.
  - Suggested example pairs:
    - Homophone: their/there or to/too
    - Garbled acronym: invent one (e.g., "be PE" → "BP")
    - Proper noun split: "Greenfield Avenue" not "Lemonwood Terrace"
    - Compound: "workout" not "underpaid"
    - Self-correction em-dash: use a different short word
- Output schema cannot change — same JSON structure existing pipeline expects
- Per-call input context cannot change — same sliding-window batches (~6,000 tokens, 60 turn cap, 1 turn context overlap)
- Reader/Writer firewall stays — Writer still does not see raw text

**Success metric for the test run:**

Lower defect count in Cat 1 (steno artifacts) on Halprin mini, broken out by sub-category (homophones, proper nouns, etc.). Don't need to hit zero. Need to see the prompt move the needle.

**Test loop:**

1. Sonnet swaps in new prompt(s), no other code changes
2. Sonnet re-runs Halprin mini through pipeline
3. Sonnet runs the same audit script that produced `HALPRIN_MINI_3WAY_DIFF.md`
4. Compare defect counts (old vs new) by category
5. Report to Scott

---

## TODO — DEFERRED TO NEXT PHASE (DO NOT LOSE)

After the prompt-only refactor proves out (or doesn't), the next phase is:

**Add audio verification to Stage 3.1 correction loop.**
- Layer Whisper / Deepgram for word-level timestamps
- Layer MFA (Montreal Forced Aligner) for phoneme verification
- Reference: existing five-layer audio architecture
- Tonight's prompt refactor is steno-only. Audio is the next layer.

**And after that, the bigger architectural move:**

**Build the two-agent Comprehension architecture discussed tonight:**
- Comprehension Agent (Scopist Agent): reads whole depo once for understanding, builds entity registry + glossary + speaker patterns + proactive flag list. Acts as advisor, not authority.
- Correction Agent (current Reader+Writer, upgraded): walks turn by turn, consults Comprehension Agent on uncertain items, outputs structured corrections with confidence + rationale + provenance.
- Confidence < 80% → human review queue
- Architecture inspired by: Scott's design + objective input from another AI tool, merged tonight

This is bigger than the prompt refactor. Don't do it until prompt refactor results are in.

---

## DECISIONS LOCKED TONIGHT (DO NOT RE-LITIGATE)

1. **Tonight is prompt-only, not architecture.** No new agents built tonight. No pipeline changes tonight.
2. **Examples in the prompt must NOT use Halprin's actual defect words.** Otherwise the test is fake.
3. **Refactor target is the Reader prompt.** Writer is downstream — fixing Writer alone can't help if Reader doesn't flag.
4. **Test = same audit script that produced tonight's diff.** Apples-to-apples comparison.
5. **Two-agent Comprehension architecture is the right long-term direction** but only after prompt refactor data is in.
6. **Audio is the next layer after that** but explicitly out of scope tonight and tomorrow morning.

---

## OPEN — WAITING ON FRESH OPUS

Stage 3.1 current state already published at:
`mrx-context/stage3_1/STAGE3_1_CURRENT_STATE_2026-04-30.md`

Fresh Opus reads that file + the audit, then writes the new Reader prompt.

---

## KEY FILES (full absolute paths)

**Truth source files:**
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\COMPONENTS.md`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\brandl\BRANDL_MB_FINAL.txt`

**Audits:**
- `C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_PAGES_1_13_DIFF.md`
- `C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_MINI_3WAY_DIFF.md`

**Stage 3.1 current state:**
- `C:\Users\scott\OneDrive\Documents\mrx-context\stage3_1\STAGE3_1_CURRENT_STATE_2026-04-30.md`

**Engine code:**
- `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\`
- Reader/Writer prompts: `src/mrx_engine_v1/stage3/suggester.py`
- Runner: `_run_halprin_mini.py`
- Output: `_stage5_out\halprin_mini.OUR_FINAL.txt`

**Repos:**
- Engine: `github.com/smichaelcapital-cpu/Court_reporting_demo`
- Context: `github.com/smichaelcapital-cpu/mrx-context`

---

## ORACLE COVENANT — DO NOT VIOLATE

MB FINAL files in `oracle/finals/` are TRUTH SOURCES for testing/scoring ONLY:
- Do NOT read at engine runtime
- Do NOT copy into engine code
- Do NOT use to hardcode values at runtime
- Do NOT use to construct example pairs in the new Stage 3.1 prompt
- Reading them to design templates: ALLOWED
- Reading them to write a unit test that diffs OUR_FINAL against truth: ALLOWED

---

## CODER MINDSET — BEFORE EVERY CODE CHANGE

Before any code change, ask: "could this change reduce transcript accuracy or credibility?"
- If yes or maybe → STOP, flag to Scott before proceeding
- If no → proceed

---

## RAMP CONFIRMATION FOR FRESH OPUS

When Scott opens, respond with something like:

> Ramped from mid-session handoff 2026-04-30 v01.
> Tonight's plan: refactor Stage 3.1 Reader prompt, re-run Halprin mini, compare defects.
> Stage 3.1 current state and audit both in mrx-context. Ready when you are.

Short. Direct. Wait for Scott's update before proposing anything.

---

— End of mid-session handoff —Opus 4.7
