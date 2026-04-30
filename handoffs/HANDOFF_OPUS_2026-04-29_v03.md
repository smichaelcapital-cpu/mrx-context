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