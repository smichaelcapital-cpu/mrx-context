# MyReporterX Handoff Log

Single rolling log of all Opus → Opus session handoffs.
Fresh Opus ramps by reading from the RAMP_START marker to end of file.

---

## 2026-04-29 v02

# MID-SESSION HANDOFF — OPUS → OPUS — 2026-04-29

**Session start:** Morning 2026-04-29
**Handoff written:** Mid-session, after cover spec sent to Sonnet
**Reason for handoff:** Outgoing Opus at ~70% context. Fresh Opus needed for stipulation spec and beyond.

---

## RAMP — 60-SECOND VERSION

Read this section only. Skip everything else unless needed.

**WHO:** Scott, founder of MyReporterX. Tired, just wants to see the depo look right today.

**TODAY'S GOAL:** Make first 11 pages of OUR_FINAL Halprin look like MB Halprin FINAL so Scott can read the whole depo side-by-side.

**WHERE WE ARE RIGHT NOW:**
- Halprin + Brandl front-matter extracted to `oracle/frontmatter/`
- COMPONENTS.md written and saved to `oracle/COMPONENTS.md` — analysis of 5 front-matter components with template + slot variables
- Brandl FINAL copied to `oracle/finals/brandl/`
- Dictionary loader WIRED at runtime (committed c11a288 in engine repo)
- Cover component build spec sent to Sonnet — Sonnet building NOW

**WHAT'S NEXT:**
- Wait for Sonnet to report back on cover component
- Diff against MB cover, iterate if needed
- Write stipulation spec (next biggest visual component, ALSO has pipeline strip-out bug to fix)
- Then appearances spec
- Then Tier 2: index, videographer opening, certificates

**SCOTT'S MOOD:** Burned out from yesterday. Patience thin. Earlier today there was friction — Opus over-narrated, asked too many questions, drifted off-task. Recovery happened. Now in flow. **Do not break the flow.**

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
- Will lose patience fast if you ask him to do file dialog work

**WHEN UNCERTAIN:** make a recommendation, give A/B options, let Scott pick. Don't ask open-ended questions.

---

## ACTIVE WORK QUEUE

**RIGHT NOW (Sonnet):**
- Building cover component per `SPEC_COVER_COMPONENT.md`
- Will run pipeline, run unit test, report diff results

**NEXT (Fresh Opus):**
- When Sonnet reports cover done → review diff
- If diff clean → write stipulation spec
- If diff has issues → write iteration spec for Sonnet

**THEN (Fresh Opus):**
- Stipulation spec (template + fix P1 strip-out bug)
- Appearances spec (most complex — biggest cascade impact)

**TIER 2 (later or tomorrow):**
- Index component
- Videographer opening
- Certificates (back-matter, separate work)

---

## KEY FILES (full absolute paths — Scott prefers no abbreviations)

**Truth source files:**
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\COMPONENTS.md` (today's analysis)
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt` (Halprin truth, READ ONLY)
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\brandl\BRANDL_MB_FINAL.txt` (Brandl truth, READ ONLY)
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\frontmatter\halprin_frontmatter.txt`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\frontmatter\brandl_frontmatter.txt`

**Engine code (where Sonnet works):**
- `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\`
- Runner: `_run_halprin_mini.py` (now committed — gitignore exception added today)
- Output: `_stage5_out\halprin_mini.OUR_FINAL.txt`

**Repos:**
- Engine: `github.com/smichaelcapital-cpu/Court_reporting_demo`
- Context: `github.com/smichaelcapital-cpu/mrx-context`

---

## ORACLE COVENANT — DO NOT VIOLATE

MB FINAL files in `oracle/finals/` are TRUTH SOURCES for testing/scoring ONLY:
- Do NOT read at engine runtime
- Do NOT copy into engine code
- Do NOT use to hardcode values
- Reading them to design templates: ALLOWED
- Reading them to write a unit test that diffs OUR_FINAL against truth: ALLOWED

---

## TODAY'S WINS (so far)

1. Code audit confirmed nothing lost. Two repos clean. 5 orphan repos exist (no remote) but unrelated to today's work. PARKED for end-of-session cleanup.
2. Brandl front-matter extracted (498 lines).
3. COMPONENTS.md written — 5 components mapped with templates + slots.
4. Brandl FINAL copied into oracle.
5. Dictionary loader WIRED at runtime — pipeline ran clean, 30/30 proposals applied, no errors. Cost $0.6751.
6. Cover component spec written — literal-template approach (not algorithmic), exact 55-line target output, byte-match success criteria.

---

## TODAY'S OPEN ISSUES

**REVISIT TOMORROW (logged in COMPONENTS.md):**
- Brandl source was text-only export (no line/page numbers). Need to extract `032626YELLOWROCK-FINAL.sgxr2` from `MASTER_COPIES\ORACLES\BRANDL_MB_DELIVERABLE_ORIGINAL.zip`, open in CaseCATalyst, export to formatted text. Then re-validate visual templates against true 2-example formatted comparison.

**PARKED for end-of-session:**
- 5 orphan repos with no remote: `AD_demo_engine_NY`, `AD_wade_0323`, `MD_demo_engine_LA_hammond`, `ad_foreman_0324`, `mb_Yellow_Brad_Brandl`. Files OneDrive-backed, git history at risk. Push to GitHub or archive.
- Easley FINAL flagged as possibly engine output, not MB original. Did not consolidate to oracle.

**DEFECTS DEFERRED (per Scott's priority decision):**
- B1 dash pattern (441 occurrences)
- B2/B3/B5 anomaly trace
- MB Style Rules workstream
- Audio architecture (paragraph timestamps in .sgxml are sufficient for nav)
- M0/M0a/M2 sub-row layout primitive (SUPERSEDED by component template work)

---

## CONTEXT-CRITICAL DECISIONS MADE THIS SESSION

1. **Front-matter is a TEMPLATE problem, not a layout primitive problem.** Scott's reframe from yesterday holds. When designing components, ask: "is this structure repeated across instances?" If yes → template, not primitive.

2. **Two depos is enough for today.** Halprin + Brandl proves the pattern. Generalization to 3+ depos can wait for onboarding a 2nd CR or 2nd state.

3. **Literal template approach for cover, not algorithmic.** The cover spec hardcodes the 55-line MB output as the target. Faster to ship, exact match guaranteed. Generalize later when we have more variation.

4. **Hardcode Halprin slot values for now.** Cover spec tells Sonnet to hardcode WITNESS_NAME, WITNESS_DATE, etc. for Halprin if .sgxml parsing is messy. TODO comments for Tier 2 generalization. Speed > perfection today.

5. **Pipeline bug (P1 stipulation strip-out) bundled with stipulation component spec.** Fixing the bug + building the template at the same time. One coordinated change, not two.

---

## KEY REFERENCE — COMPONENTS.md SUMMARY

5 front-matter components identified:
1. **Cover page** — defect 0428-1, 0428-2 (caption layout broken)
2. **Index** — Scott's "crime scene" zone
3. **Appearances** — defect 0428-3 (crime scene)
4. **Stipulation** — defect 0428-5 / P1 (pipeline STRIPS OUT, bug)
5. **Videographer opening** — cascade from 1+3

3 layers of constants:
- Per-CASE (YellowRock caption)
- Per-CR (MB signature/reporter line)
- Per-STATE (Louisiana stipulation language, R.S. 37:2554)

Build order:
- Tier 1: Cover → Stipulation → Appearances
- Tier 2: Index → Videographer → Certs

---

## RAMP CONFIRMATION FOR FRESH OPUS

When Scott opens, respond with something like:

```
Ramped from mid-session handoff 2026-04-29. Cover spec is with Sonnet.
What's the status?
```

Short. Direct. Wait for Scott's update before proposing next move.

DO NOT propose unprompted:
- New components beyond what's in queue
- Architectural rework
- Audio work
- Body defect work (B1/B2/B3/B5)

DO listen for:
- Sonnet's cover diff result (if Sonnet has reported)
- Any new pivots from Scott

---

— End of mid-session handoff —

---

## 2026-04-29 v03

MID-SESSION HANDOFF — OPUS → OPUS — 2026-04-29 (LATE NIGHT)
Session start: Evening 2026-04-29
Handoff written: End of session, ~midnight
Reason for handoff: Scott going to bed. Fresh Opus tomorrow.

RAMP — 60-SECOND VERSION
Read this section only. Skip everything else unless needed.
WHO: Scott, founder of MyReporterX. End of long day. Tonight he
got a real win — pages 1-13 of OUR_FINAL Halprin byte-match MB.
TONIGHT'S BIG WIN:
Pages 1-13 of OUR_FINAL Halprin are perfect against MB FINAL. Zero
diffs. Built four components in sequence: cover (yesterday),
stipulation, appearances+index, videographer opening.
WHAT TOMORROW'S OPUS DOES:

Read the audit files Scott reviewed overnight
Wait for Scott's reaction / priority call
Likely next: write spec for the two "quick fixes" Sonnet flagged
(EXAMINATION indent + double-space-after-period)
After that: certificates component (back matter, last Tier 2 piece)
After that: triage the ~15-20 root-cause body bugs from the audit

SCOTT'S MOOD: Exhausted but satisfied. Real progress shipped. Was
salty mid-session when Opus asked dumb clarifying questions ("first
45 vs last 5" was obvious from context). Don't repeat that.

SCOTT'S WORKING STYLE — CRITICAL

12-year-old reading level until told otherwise
Plain English, short answers
ONE question at a time (NOT three)
Inline A/B/C only when there's a real choice
Hates fire-hose responses
Does NOT want to be Claude's hands — Sonnet writes files
ALWAYS full absolute paths, never abbreviated
Pushes back when wrong — pushback is usually right
Will lose patience FAST if you ask him obvious clarifying questions

WHEN UNCERTAIN: make a recommendation, give A/B options, let Scott
pick. Don't ask open-ended questions.
SPECIFIC LESSON FROM TONIGHT: When Scott describes a setup ("50
pages, first 45 and last 5"), figure it out from context. Don't ask
"do you mean A or B?" when only A makes sense. He'll bite your head
off and he'll be right.

TIER 1 + TIER 2 STATUS
DONE:

✅ Cover component (yesterday, commit 245e2ef + earlier)
✅ Stipulation component (commit 6ef8dd4)
✅ Index/exhibits component (built into appearances literal template)
✅ Appearances component (commit 6b3437c)
✅ Videographer opening (commit 1a04545)
✅ Three-way diff audit shipped to mrx-context/audits/

REMAINING TIER 2:

Certificates component (back matter, pages 296 + 298 of full Halprin)

Reporter's Certificate (Louisiana R.S. 37:2554 territory)
Witness's Certificate
Both literal-template, same approach as cover/stipulation/etc.



TIER 3 (after Tier 2 closes):

Generalization of all hardcoded literals into slots

Per-CASE constants → case file (e.g., cases/yellowrock.json)
Per-CR constants → CR file (MB's reporter block)
Per-STATE constants → state module (Louisiana stip language)
Per-DEPO slots → .sgxml metadata + raw RTF parsing
This is what unblocks Brandl (and any future depo) to run through
the engine without breaking Halprin




AUDIT RESULTS — TONIGHT'S HEADLINE
Sonnet ran a three-way diff (RAW vs OURS vs MB) on pages 13-54 of the
Halprin mini and produced two files:

C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_PAGES_1_13_DIFF.md
C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_MINI_3WAY_DIFF.md

Headline numbers:

1,027 line mismatches total (pages 13-54)
BUT: ~875 of those are CASCADE from ~15-20 root causes
Real bug count: ~15-20 unique problems, not 1,000
Pages 1-12: perfect, zero diffs

Top 3 patterns:

Content/correction divergence — 875 lines (~15-20 root causes;
cascade auto-resolves when roots are fixed)
Back matter — 145 lines (synthetic certs/errata vs real — expected,
resolves when certificates component lands)
Double-space after period — 6 lines (CaseCATalyst convention; we
don't insert; trivial post-processing fix)

Two highest-value quick fixes Sonnet flagged:

EXAMINATION indent — 1-line code change
Double-space-after-period — post-processing pass

What needs judgment (not just code):

Steno artifact corrections ("with and T" → "W&T", address/name
errors, missing em-dashes)
Either improved Stage 3.1 prompts OR a manual review queue
This is a real product decision, not a code fix


DECISIONS THAT SHOULDN'T BE QUESTIONED
These were made tonight after careful discussion. Don't re-litigate:

Literal-template-first approach is correct. Cover, stipulation,
appearances, videographer opening all built as literal templates
with TODOs for Tier 3 generalization. This was the right call —
shipped real pages tonight.
Skip pages 1-13 from any future audit. Already proven byte-match.
Including them in diffs is noise.
Hardcoding for Halprin only is ACCEPTABLE for tonight's deliverable.
Tier 3 work generalizes everything. Brandl WILL break if run through
today — that's known and accepted.
Bundle pipeline bugs with their component spec. Stipulation +
P1 strip-out bug were fixed in one coordinated change. Pattern works.
Court reporter authority over format is absolute. If MB writes
"Darrein" instead of "Darren", or uses "(Zoom)" on one page and
"(Via Zoom)" elsewhere, ENGINE MATCHES MB. Do not normalize.


OPEN PIPELINE ISSUES (KNOWN, NOT URGENT)
Pre-existing architectural issue:

proposal_mapper.py has a positional-join length check that breaks
when proposals/anomalies counts don't match
Sonnet hit it tonight running the videographer pipeline; manual
workaround applied
Existing test suite already fails on this — it predates today
Logged for future cleanup, not blocking

Stage 1 strip-out:

Stipulation P1 bug fixed (turn_extractor.py — \s0 style was
IGNORE'd, dropping stipulation paragraphs)
Did NOT globally un-ignore \s0 (correct call — used for too much
other content)
Used literal template instead
Comment in code documents the constraint


WHAT TO LISTEN FOR FROM SCOTT TOMORROW
When he opens up tomorrow, he'll likely be reacting to the audit.
Possible directions:

"Let's fix the two quick wins" → write spec for EXAMINATION indent

double-space pass (small spec, both straightforward)


"Let's do certificates" → write certificates component spec (Tier 2
closer)
"Let's start generalization" → bigger conversation; help him think
through where to start (Tier 3 has multiple workstreams)
"Let's onboard MB or AD" → pivot to Golden Circle / business work
Pivot entirely → respect it, follow his lead

DO NOT propose unprompted:

Bigger architecture rework
Body defect deep dives (B1/B2/B3/B5 — parked)
Audio architecture (parked)
Anything from the 5 orphan repos cleanup list (parked)

DO listen for:

His read of the audit files
Any new pivots
Energy level — if tired, keep scope small


KEY FILES (full absolute paths — Scott prefers no abbreviations)
Truth source files:

C:\Users\scott\OneDrive\Documents\mrx-context\oracle\COMPONENTS.md
C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt
C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\brandl\BRANDL_MB_FINAL.txt

Audits (NEW from tonight):

C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_PAGES_1_13_DIFF.md
C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_MINI_3WAY_DIFF.md

Engine code (where Sonnet works):

C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\
Runner: _run_halprin_mini.py
Output: _stage5_out\halprin_mini.OUR_FINAL.txt

Repos:

Engine: github.com/smichaelcapital-cpu/Court_reporting_demo
Context: github.com/smichaelcapital-cpu/mrx-context


ORACLE COVENANT — DO NOT VIOLATE
MB FINAL files in oracle/finals/ are TRUTH SOURCES for testing/scoring ONLY:

Do NOT read at engine runtime
Do NOT copy into engine code
Do NOT use to hardcode values at runtime
Reading them to design templates: ALLOWED
Reading them to write a unit test that diffs OUR_FINAL against truth: ALLOWED

Hardcoding LITERAL TEMPLATE TEXT (Louisiana boilerplate, MB's reported-by
block) into engine code is acceptable for Tier 1/2 — that's not "reading
MB at runtime", that's encoding a template.

CODER MINDSET — BEFORE EVERY CODE CHANGE
Before any code change, ask: "could this change reduce transcript
accuracy or credibility?"

If yes or maybe → STOP, flag to Scott before proceeding
If no → proceed


RAMP CONFIRMATION FOR FRESH OPUS
When Scott opens, respond with something like:
Ramped from late-night handoff 2026-04-29.
Pages 1-13 byte-match MB. Audit shipped. What's the read?
Short. Direct. Wait for Scott's reaction before proposing anything.

— End of late-night handoff —

---

## 2026-04-30 v01 — V2 Reader prompt design

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

---

<!-- ===== RAMP_START ===== -->
<!-- Fresh Opus: begin reading here. Everything above is history.   -->
<!-- When you start a new session, move this marker down to above   -->
<!-- your new ## YYYY-MM-DD section header.                          -->

## 2026-04-30 v02 — V2 deployed, +20% improvement on Halprin mini

**Session:** ~5:00 PM to ~10:30 PM, 2026-04-30
**Outcome:** SHIPPED. V2 Reader prompt live. Halprin mini diff lines reduced from 1,040 to 827 (-20%). 4 of 10 tracked Cat 1 defects fixed; 3 more correctly flagged for human review.

### RAMP — 60-SECOND VERSION

V2 Reader prompt ("steno hunter") deployed and working. Tonight's run on Halprin mini fixed 4 defects V1 missed entirely (permit/permanent x2, underpaid, your→you're) and correctly flagged 3 more for review. 3 still missed. Reader found 147 anomalies vs V1's ~12. Zero regressions. Four infrastructure bugs surfaced and fixed along the way (Reader truncation, Writer truncation, cost ceiling, Stage 5 positional join).

**Tomorrow's open question:** Option A vs B vs C for next iteration. Scott has not decided. See "Open Items" below.

### What's live in code

Repo: `Court_reporting_demo` (main branch, Scott's local at `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\`)

- `src/mrx_engine_v1/stage3/suggester.py`:
  - READER_PROMPT_V1 string body now contains V2 ("steno hunter") prompt — variable name unchanged for compile compatibility
  - SuggesterConfig.reader_max_tokens: 1024 → 4096
  - SuggesterConfig.writer_max_tokens: 1024 → 4096
- `src/stage5/proposal_mapper.py`: positional zip replaced with anomaly_id keyed lookup + defensive ValueError if proposal references unknown anomaly_id
- `io/analysis/halprin_mini/_run_halprin_mini.py`: MAX_COST_USD: $1.00 → $5.00

### What's locked (do not re-litigate)

1. V2 Reader prompt is deployed. Source of truth: `mrx-context/stage3_1/READER_PROMPT_V2.md`
2. Em-dash for witness self-correction is a legitimate `steno_artifact` flag (explicit exception to the V1 "no punctuation flags" rule)
3. V1 OUR_FINAL baseline locked at: `mrx-context/baselines/halprin_mini.OUR_FINAL.V1.2026-04-30.txt`
4. V1 _stage5_out snapshot preserved at: `io/analysis/halprin_mini/_stage5_out_v1_baseline/`
5. Oracle Covenant intact — MB FINAL files only used by audit script, never at engine runtime, never in V2 example pairs
6. **MB outreach gate: do not show MB anything until Halprin OUR_FINAL is at ~90% match against her FINAL.** Until then, reverse-engineer answers from her FINAL. Use her sparingly and only on yes/no questions where reverse-engineering hits a wall (e.g., "is the em-dash convention X or Y").

### Tonight's wins (V2 vs V1 on Halprin mini)

| Defect | V1 | V2 |
|--------|----|----|
| permit address → permanent | missed | **fixed** |
| permission address → permanent | missed | **fixed** |
| under paid → underpaid | missed | **fixed** |
| your sworn → you're sworn | missed | **fixed** |
| lemon wood terrace | missed | flagged (names_lock blocked auto-fix) |
| flew into give → flew in to give | missed | flagged (medium confidence) |
| with and T (page 14, x3) | missed | partial (page 14 fixed, later pages still wrong) |
| No no → No -- no | missed | partial (em-dash applied, second "no" dropped) |
| 25 years ago → Twenty-five | missed | missed (Reader flagged, Writer didn't apply) |
| Warren seal → Warren Seal | missed | missed |

Score: V1 = 0/10. V2 = 4 fixed + 3 flagged/partial + 3 missed.

Full reports:
- `mrx-context/audits/HALPRIN_MINI_3WAY_DIFF_V2.md`
- `mrx-context/audits/V1_VS_V2_COMPARISON.md`

### Lessons learned (technical)

**Lesson 1 — Reader max_tokens too small for V2.**
V2 Reader prompt produces longer reader_notes and more anomalies per batch than V1 (~15-25 vs V1's ~2-5). Default `reader_max_tokens=1024` truncated mid-JSON on every batch. Parser silently returned empty list. Looked like prompt failure; was config failure. Fix: bumped to 4096.

**Lesson 2 — Writer max_tokens hit the same wall.**
Same root cause, downstream. V2 Reader's 17+ anomalies/batch required Writer to produce 17+ ops; 1024 truncated mid-JSON on every Writer call. Same silent zero. Fix: bumped to 4096. **Reader and Writer max_tokens should always be considered together when prompts get richer.**

**Lesson 3 — Silent zeroing on truncated JSON.**
The pipeline's failure mode for truncated JSON is silent — the except clause returns empty list with no warning. Future hardening: log WARN on `stop_reason=max_tokens` for any Reader or Writer call. Log WARN on suspiciously empty anomaly/op counts for non-empty primary turn batches.

**Lesson 4 — Cost ceiling lives in two places.**
`MAX_COST_USD` lives in `_run_halprin_mini.py`. SuggesterConfig also has `max_total_cost_usd`. Config is split. TODO: unify — runner should pass overrides into SuggesterConfig, not duplicate the parameter.

**Lesson 5 — Stage 5 positional join was a latent bug.**
`proposal_mapper.py` joined anomalies to proposals by positional index. Assumed 1:1 mapping. V1 honored it by accident (Reader was lazy); V2 broke it (anomaly count > proposal count is now normal because some anomalies become FLAG-only or get dropped by validate_ops). Fix: join by `anomaly_id`. **Lesson: any positional-zip pattern in this pipeline is suspect and should be audited.**

### TODOs surfaced (deferred to future sessions)

**Quick wins likely to flip remaining defects to fixed:**
- Add `W&T`, `Warren Seal`, `Lemonwood Terrace` to names_lock and case dictionary for Halprin
- Tune Writer prompt for number-format application (the `25 years ago` case)
- Tune Writer prompt for the `No no → No -- no` pattern (Writer's instinct was "remove duplicate" instead of "insert dash between them")

**Infrastructure hardening:**
- Audit Stage 3.1 → Stage 5 chain for other fragile assumptions (positional joins, length-equality assertions, implicit 1:1 mappings). V2 surfaced one. Likely more.
- Defensive logging: WARN on `stop_reason=max_tokens`, WARN on suspicious empty anomaly/op counts.
- Unify cost ceiling — should live in SuggesterConfig only, not also in the runner.

**Architecture (carry over from earlier):**
- Reader prompt should become ~90% static core + small dynamic slot for per-CR style/quirks.
- Revisit single-responsibility agent architecture (Read / Decide / Write split). Scott's mandate: no agent does more than one thing. Revisit before any Comprehension Agent build.
- Audio verification layer (Whisper/Deepgram + MFA) is the next architectural layer after the prompt-tuning loop saturates.

### Open items for tomorrow

**Decision needed: Option A vs B vs C for next iteration.**

- **Option A — Fix the cheap wins.** Update names_lock + dictionary entries for Halprin (W&T, Warren Seal, Lemonwood Terrace). Small Writer prompt tweaks for number format and em-dash patterns. Likely flips 3-5 of remaining defects to fixed. Low risk, high yield.
- **Option B — Iterate Reader prompt to V3.** Push for more aggressive lowercase proper noun detection. Probably modest gains since Reader already finds most of these.
- **Option C — Ship and move on.** 20% diff reduction is real progress. Move to next layer (audio verification or Comprehension Agent).

Opus's recommendation: Option A first. Updates to names_lock and case dictionary surfaced as the bottleneck for several remaining defects. Cheap, fast, low-risk, likely to produce another big jump.

Scott's preference: not yet stated. Ask before proceeding.

### Files of record (full absolute paths)

**Truth source:** `oracle/finals/halprin/040226yellowrock-FINAL.txt` (Oracle — never moves)
**V1 baseline (locked):** `mrx-context/baselines/halprin_mini.OUR_FINAL.V1.2026-04-30.txt`
**V2 output (current):** `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt`
**V1 _stage5_out snapshot:** `io/analysis/halprin_mini/_stage5_out_v1_baseline/`
**V2 prompt source:** `mrx-context/stage3_1/READER_PROMPT_V2.md`
**Tonight's audits:**
- `mrx-context/audits/HALPRIN_MINI_3WAY_DIFF_V2.md`
- `mrx-context/audits/V1_VS_V2_COMPARISON.md`

### Scott's working style (carry forward — re-read this every session)

- 12-year-old reading level until told otherwise
- Plain English, short answers
- ONE question at a time (NOT three)
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses
- Does NOT want to be Claude's hands — Sonnet writes files
- ALWAYS full absolute paths, never abbreviated
- Pushes back when wrong — pushback is usually right
- Will lose patience FAST on obvious clarifying questions
- Never make Scott the copy-paste mule. Long content goes to git, URL gets pasted.
- Before pushing files, prompt Scott with the proposed git path for approval

### Coder Mindset — Prime Directive

Before any code change, ask: "could this change reduce transcript accuracy or credibility?"
- If yes or maybe → STOP, flag to Scott before proceeding
- If no → proceed

### Oracle Covenant — DO NOT VIOLATE

MB FINAL files in `oracle/finals/` are TRUTH SOURCES for testing/scoring ONLY:
- Do NOT read at engine runtime
- Do NOT copy into engine code
- Do NOT use to hardcode values at runtime
- Do NOT use to construct example pairs in any prompt
- Reading them to design templates: ALLOWED
- Reading them to write a unit test that diffs OUR_FINAL against truth: ALLOWED


---

## DECISION LOG — Anomaly join key architecture (2026-05-01)

DECIDED: Option 3 — natural key (turn_idx, token_span)
WHY NOW: Smallest code surface, zero artifact cost, semantically correct,
         doesn't conflate with apply.py Bug 2.

ALSO CONSIDERED:
- Option 1 (compound key batch_id, anomaly_id) — requires schema change
  to anomalies.jsonl, $0.95 re-run, fix in two places
- Option 2 (globally unique IDs at suggester) — cleanest long-term, but
  invalidates all existing artifacts and changes suggester contract

REVISIT TRIGGER (when to reconsider):
- If onboarding a 2nd CR and we discover the natural-key assumption
  doesn't hold across CR styles (e.g., Reader prompts that flag
  overlapping spans)
- If we move to a production ID system where surrogate keys carry other
  metadata (audit trails, cross-system references)
- If the apply.py Bug 2 fix forces a schema change anyway — at that
  point Option 2 might be cheaper to do alongside it
- If anomaly volume scales 10x+ and the (turn_idx, token_span) tuple
  lookup becomes a perf concern (unlikely but worth flagging)

REVISIT CADENCE: Re-evaluate in ~3-4 weeks or when one of the triggers
above fires, whichever comes first.