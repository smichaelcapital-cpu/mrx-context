SONNET HANDOFF — 2026-04-29 v02 (LATE NIGHT)
For: Fresh Claude Code Sonnet session
From: Outgoing Sonnet (end of long evening) + Outgoing Opus (architect)
Owner: Scott

YOU ARE THE BUILDER
Opus is the architect. You are the builder. Scott is the human owner.

Opus writes specs.
You execute them.
Scott reviews and decides.


RAMP — 60 SECONDS
TONIGHT'S BIG WIN:
Pages 1-13 of OUR_FINAL Halprin byte-match MB FINAL. Zero diffs.
Built four components in sequence tonight: stipulation, appearances+index,
videographer opening. Cover was already done yesterday.
WHAT YOU JUST FINISHED (previous Sonnet):

Stipulation component — commit 6ef8dd4

Found Stage 1 strip-out bug (\s0 style was IGNORE'd)
Used literal template instead of globally un-ignoring \s0


Appearances + index component — commit 6b3437c

9 pages literal template (pages 2-10)
All byte-match MB


Videographer opening — commit 1a04545

Page 12 full literal + page 13 lines 1-2 injected as COLLOQUY
LogicalLines into body
Zero diffs vs oracle


Three-way diff audit — pushed to mrx-context/audits/
Saved Opus handoff v03 — commit 94c66d7

WHAT'S NEXT:

Wait for fresh Opus to read Scott's reaction to the audit
Wait for next spec from Opus
Likely candidates: EXAMINATION indent fix, double-space-after-period
pass, certificates component


SCOTT'S WORKING STYLE — CRITICAL

12-year-old reading level until told otherwise
Plain English, short answers
ONE question at a time (NOT three)
Inline A/B/C only when there's a real choice
Hates fire-hose responses
Does NOT want to be Claude's hands — YOU write files, you don't ask
him to copy/paste/move things
ALWAYS full absolute paths, never abbreviated
Uses CMD on Windows laptop — label terminal commands "CMD (Windows
laptop)"
Pushes back when wrong — pushback is usually right

WHEN UNCERTAIN: make a recommendation, give A/B options, let Scott
pick. Don't ask open-ended questions.
SPECIFIC LESSON FROM TONIGHT: Windows paths in Python heredocs
break (\U becomes a unicode escape error). When writing files, use
your file write tool directly with forward slashes, OR escape the
backslashes. Don't waste cycles on heredoc workarounds.

ORACLE COVENANT — DO NOT VIOLATE
MB FINAL files in oracle/finals/ are TRUTH SOURCES for testing/scoring ONLY:

Do NOT read at engine runtime
Do NOT copy into engine code as runtime input
Do NOT use to hardcode VALUES at runtime
Reading them to design templates: ALLOWED
Reading them to write a unit test that diffs OUR_FINAL against truth:
ALLOWED
Hardcoding LITERAL TEMPLATE TEXT (Louisiana boilerplate, MB's
reported-by block) as per-depo case constants in engine code:
ALLOWED for Tier 1/2 — that's encoding a template, not reading MB
at runtime

Any code path that reads *FINAL* files at runtime is cheating.
Refuse the work and flag to Scott.

CODER MINDSET — BEFORE EVERY CODE CHANGE
Ask: "could this change reduce transcript accuracy or credibility?"

If yes or maybe → STOP, flag to Scott before proceeding
If no → proceed

Other rules:

Slow and deliberate, one to two steps at a time
Plain English explanations
Confirm before destructive actions
Avoid ask_user_input_v0 popup widgets — use inline plain text choices


KEY FILES (full absolute paths)
Engine code (where you work):

Repo: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\
Runner: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\_run_halprin_mini.py
Output: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt
GitHub: github.com/smichaelcapital-cpu/Court_reporting_demo

Oracle files (READ ONLY for analysis, NEVER at runtime):

C:\Users\scott\OneDrive\Documents\mrx-context\oracle\COMPONENTS.md
C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt
C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\brandl\BRANDL_MB_FINAL.txt

Audits (NEW from tonight — Scott will read tomorrow):

C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_PAGES_1_13_DIFF.md
C:\Users\scott\OneDrive\Documents\mrx-context\audits\HALPRIN_MINI_3WAY_DIFF.md

Context repo (specs, handoffs, oracle, audits):

C:\Users\scott\OneDrive\Documents\mrx-context\
GitHub: github.com/smichaelcapital-cpu/mrx-context


RECENT COMMITS YOU SHOULD KNOW ABOUT
Engine repo (mrx_engine_v1 on smichaelcapital-cpu):

1a04545 — Videographer opening (today)
6b3437c — Appearances + index literal template (today)
6ef8dd4 — Stipulation component + P1 strip-out fix (today)
cdcac65 — Cover component (yesterday)

Context repo (mrx-context):

94c66d7 — Opus handoff v03 (today, late night)
(audit commits) — HALPRIN_PAGES_1_13_DIFF.md and HALPRIN_MINI_3WAY_DIFF.md
1d7410b — oracle/COMPONENTS.md + Brandl FINAL (yesterday)


AUDIT RESULTS — TONIGHT'S HEADLINE
Three-way diff (RAW vs OURS vs MB) on pages 13-54 of Halprin mini.
Headline numbers:

1,027 line mismatches total
BUT: ~875 are CASCADE from ~15-20 root causes
Real bug count: ~15-20 unique problems
Pages 1-12: perfect, zero diffs

Top 3 patterns:

Content/correction divergence — 875 lines (cascade from ~15-20 roots)
Back matter — 145 lines (synthetic certs/errata vs real — expected,
resolves when certificates component lands)
Double-space after period — 6 lines (CaseCATalyst convention)

Two highest-value quick fixes flagged:

EXAMINATION indent — 1-line code change
Double-space-after-period — post-processing pass


KNOWN OPEN ISSUES (NOT URGENT)
proposal_mapper.py architectural issue:

Positional-join length check breaks when proposals/anomalies counts
don't match
Hit during videographer pipeline run tonight; manual workaround used
(trim anomalies file to match proposals length, run, restore backup)
Pre-existing; existing test suite already fails on this
Flagged for future cleanup, not blocking

Stage 1 \s0 → IGNORE constraint:

Stipulation P1 fix: did NOT globally un-ignore \s0 (used for too
much other content)
Used literal template instead — correct call
Comment in turn_extractor.py documents the constraint


DECISIONS THAT SHOULDN'T BE QUESTIONED
These were made tonight after careful discussion. Don't re-litigate:

Literal-template approach is correct for Tier 1/2. Build literal
templates per component with TODOs for Tier 3 generalization.
Hardcoding for Halprin only is ACCEPTABLE for tonight's deliverable.
Tier 3 generalization will fix this. Brandl WILL break if run through
today — that's known and accepted.
Skip pages 1-13 in audits. Already proven byte-match. Including
them is noise.
Bundle pipeline bugs with their component spec. Stipulation +
P1 strip-out fixed in one coordinated change. Pattern works.
Court reporter authority over format is absolute. If MB writes
"Darrein" not "Darren", or "(Zoom)" on one page and "(Via Zoom)"
elsewhere, ENGINE MATCHES MB. Do not normalize.


DEFERRED WORK — DO NOT PROPOSE TODAY

B1 dash pattern (441 occurrences) — parked
B2/B3/B5 anomaly trace — parked
MB Style Rules workstream — parked
Audio architecture — parked
M0/M0a/M2 sub-row layout primitive — SUPERSEDED by component template work
Generic centering algorithms — use literal templates instead
5 orphan repos cleanup (AD_demo_engine_NY etc.) — end of session, not today
proposal_mapper.py architectural fix — flagged, not blocking


RAMP CONFIRMATION
When ready, respond to Scott with something brief like:
Ramped from Sonnet handoff 2026-04-29 v02 (late night). Builder mode.
Pages 1-13 byte-match MB. Audit shipped. Awaiting next spec from Opus.
Then wait for Scott or Opus to direct the next build.

— End of Sonnet handoff —
