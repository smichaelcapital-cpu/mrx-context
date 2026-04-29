# HANDOFF — OPUS — 2026-04-28 v01

## TRUTH SOURCES (READ FIRST — NEVER LOSE THESE)

MB's Halprin FINAL (truth — Oracle Covenant — READ ONLY):
  C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt
  (also still at original location for pipeline reads:
   C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-FINAL.txt)

Halprin front-matter extracted (oracle):
  C:\Users\scott\OneDrive\Documents\mrx-context\oracle\frontmatter\halprin_frontmatter.txt
  (659 lines, pages 1-12, cuts at "EXAMINATION" line 660)

Engine output OUR_FINAL (regenerated each pipeline run):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt

Halprin source RTF (Stage 1 input):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-ROUGH_Tsmd.rtf

Halprin .sgxml (metadata + 88 paragraph timestamps):
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\040226yellowrock-ROUGH.sgxml

Full Halprin package (READ ONLY — Scott's master):
  C:\Users\scott\OneDrive\Documents\mb_040226_halprin_yellowrock\

Job dictionary (RTF, byte-identical to existing test fixture):
  C:\Users\scott\OneDrive\Documents\mb_040226_halprin_yellowrock\040226yellowrock-ROUGH.rtf
  (existing fixture: tests/fixtures/halprin_mini/dictionary.rtf)

Other MB FINALs on disk (consolidate tomorrow):
  - Brandl 032626: C:\Users\scott\OneDrive\Documents\MASTER_COPIES\ORACLES\Brandl\
  - 030526 depo: candidate, location in 2026-04-28_ORACLE_CONSOLIDATION.md
  - Easley: in mb_demo_engine_v4 folder, candidate

Engine repo:
  C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1
  github.com/smichaelcapital-cpu/Court_reporting_demo

Context repo:
  C:\Users\scott\OneDrive\Documents\mrx-context
  github.com/smichaelcapital-cpu/mrx-context

Master copies:
  C:\Users\scott\OneDrive\Documents\MASTER_COPIES\

## ONE-LINE STATE
Recon methodology proven, dictionary thread resolved (NOT WIRED at runtime), defect log committed, oracle folder established, component reframe locked in. Tomorrow opens with component-extraction work as top priority.

## RAMP — READ THESE IN ORDER
1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/MANIFEST.md
   (NOTE: still not built — flag to Scott if missing)
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-04-28_v01.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/OPUS_TO_OPUS_2026-04-29_RESUME.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-04-28_DEFECT_LOG_HALPRIN_FRONT_PAGES.md

After reading, confirm: "Ramped from Opus handoff 2026-04-28 v01. Component reframe internalized. Ready."

## YOUR ROLE
Opus = architect. Sonnet = builder. Scott = human owner.

## ARTIFACTS TOUCHED THIS SESSION

Created:
  - mrx-context/specs/2026-04-28_HALPRIN_RECON_FULL.md
  - mrx-context/specs/results/2026-04-28_HALPRIN_RECON_RESULTS.md
  - mrx-context/specs/results/2026-04-28_HALPRIN_PACKAGE_INSPECTION.md
  - mrx-context/specs/results/2026-04-28_DICTIONARY_RUNTIME_WIRING.md
  - mrx-context/specs/results/2026-04-28_ORACLE_CONSOLIDATION.md
  - mrx-context/specs/2026-04-28_DEFECT_LOG_HALPRIN_FRONT_PAGES.md
  - mrx-context/oracle/README.md
  - mrx-context/oracle/.gitignore
  - mrx-context/oracle/finals/halprin/040226yellowrock-FINAL.txt (copied)
  - mrx-context/oracle/finals/halprin/040226yellowrock-FINAL.sgxml (copied)
  - mrx-context/oracle/frontmatter/halprin_frontmatter.txt (extracted)
  - mrx-context/handoffs/OPUS_TO_OPUS_2026-04-29_RESUME.md
  - mrx-context/handoffs/HANDOFF_OPUS_2026-04-28_v01.md

Modified: none (engine repo untouched)

Commits (mrx-context, all pushed):
  - 26f8d43 — recon spec + results
  - d02dced — dictionary runtime wiring + defect log populated
  - 022a96f — Oracle folder + Halprin consolidation
  - 54d6d4f — Opus-to-Opus resume note
  - [this commit] — handoff doc

Engine repo: clean, untouched this session.

## RECON VERDICTS LOCKED IN

| Defect | Verdict | Status |
|---|---|---|
| 0428-1 (caption) | Layout — confirmed | Maps to component template work |
| 0428-2 (videotaped block) | Layout — confirmed cascade | Same |
| 0428-3 (appearances) | Layout — confirmed cascade | Same |
| 0428-5 (stipulation strip) | B (pipeline bug) | Confirmed; needs Stage 1→5 trace |
| B1 (dashes) | A — MB polish, 441 occurrences | Parked |
| B2 (under paid) | A-anomaly | Pipeline introduces split; needs Stage 1/2 trace |
| B3 (sentence merge) | A-anomaly | Pipeline merges differently; needs Stage 2/3 trace |
| B4a (I no/know) | A — MB correction | Closed |
| B4b (Warren seal) | A — both forms match MB | Closed |
| B5 (W&T Offshore) | A-anomaly | Stroke W-T translates to "with"; needs tokenizer trace |

## DICTIONARY VERDICT: NOT WIRED

- dictionary_loader.py exists, tested
- Fixture dictionary.rtf is byte-identical to package's job dict
- Stage 3 accepts dictionary parameter
- _run_halprin_mini.py line 267 passes {} (empty dict) to LLM
- Every Halprin run to date has had ZERO job-specific dict context
- Two-line fix available
- WARNING: wiring won't fix B2/B5 (those are NOT in job dict)

## AUDIO DECISION: COLLAPSED

- .sgxml has 88 paragraph-level timestamp pairs
- Sufficient for Scott's nav goal (within 2-3 sentences)
- AUDIO_SYNC_RECON spec is no longer needed
- Whisper whole-file fallback no longer needed as design decision
- Audio work shelved until front-matter ships

## DEFECT SUPERSET — TIER STATUS

REFRAMED: front-matter is a TEMPLATE problem, not a layout primitive problem. The defect superset still applies but the architectural approach is different.

### Component template work (NEW TOP PRIORITY)

C0 — Component inventory pass
  Compare front-matter across MB depos. Identify reusable templates with slot variables. Output: COMPONENTS.md in oracle/.

C1 — Cover component
  Template for case caption + venue + date + witness + reporter. Slot variables: state, parish, district, plaintiffs[], defendants[], docket, division, witness, date, time, firm, address, city, state, reporter.

C2 — Stipulation component
  State-specific boilerplate. Louisiana = Article 1434 territory. Slot variables: counsel name, witness name.

C3 — Appearances component
  Firm blocks + attorney lists. Multi-attorney "BY:" grouping. "(Zoom)" suffix support. Slot variables: per-firm address, attorneys[], emails[], remote_flag[].

C4 — Index component
  TOC + exhibit list. Slot variables: section_page_refs[], exhibits[].

C5 — Witness Certificate component
  Signature block + exhibit references.

C6 — Reporter Certificate component
  State-specific verbatim. R.S. 37:2554 for LA.

C7 — Errata component
  3 lines × 7 entries × N pages.

### Pipeline bugs (independent of component work)

P1 — Stipulation strip-out (0428-5)
  Stage 1→5 trace needed to localize where "It is stipulated and agreed" gets dropped from raw RTF.

P2 — B2/B3/B5 anomaly trace
  Pipeline produces text not in raw RTF. Stage 1/2 tokenization or brief expansion. Investigate.

P3 — Dictionary wiring
  Two-line fix in _run_halprin_mini.py to load dict into LLM context.

### Parked (per Scott's instruction)

- B1 dash pattern decode (441 examples, decodable rule, parked)
- MB Style Rules workstream (parked until tech debt cleared)
- Audio architecture (paragraph timestamps sufficient)
- M0/M0a/M2 sub-row layout primitive (SUPERSEDED by component work)

## DRAFT RULES PARKED FOR ADDENDUM v2 BUMP

1. RULE-FORMAT-CONSTANTS-VERIFY (carried from prior session)
2. RULE-HANDOFF-ARTIFACT-MANIFEST (carried)
3. RULE-OPERATION-DOC (carried — MANIFEST.md still not built)
4. RULE-RECON-BEFORE-SPEC (NEW — proven tonight)
   Architect runs structural recon (raw → MB → ours three-way diff) BEFORE writing any architectural spec. No spec without evidence from real files.
5. RULE-DIFF-BEFORE-DECLARE (NEW — proven needed tonight)
   Before declaring any format work "shipped," run structured diff between OUR_FINAL and MB FINAL. Architect presents delta list to Scott. Scott never finds defects himself.
6. RULE-COMPONENTS-NOT-PRIMITIVES (NEW — emerged tonight)
   Front-matter sections are templates, not layout problems. When designing front-matter work, ask first: "is this structure repeated across instances?" If yes, it's a component template, not a primitive.

## MANIFEST.md / OPERATION DOC — STILL NOT BUILT

Carried from 2026-04-27. Not built tonight (correctly deprioritized). Tomorrow: still on the list, but component work takes priority. Build after component spec ships.

## TOMORROW MORNING CHECKLIST (FOR FRESH OPUS)

When Scott opens with "ramped":

Response template:

Ramped from 2026-04-28 v01. Component reframe internalized.

Three things on deck:

1. Spec for Sonnet: extract front-matter from Brandl + 030526 + Easley. Same method as Halprin (cutoff at EXAMINATION). Outputs to oracle/frontmatter/.

2. Then: I do the component-extraction comparison. Diff sections across depos. Identify templates + slot variables. Output: oracle/COMPONENTS.md.

3. Parallel: spec dictionary wiring fix for Sonnet (line 267 of _run_halprin_mini.py). 10-min fix.

Starting with #1. Spec ready below — review and approve.

DO NOT propose unprompted:
- Architecture for layout primitives
- Audio work
- B1 dash decode
- B2/B3/B5 trace work (parked)

DO ask Scott:
- Confirm 030526 depo is an MB FINAL (not yet verified)
- Confirm consolidate Easley FINAL into oracle/

## SCOTT'S WORKING STYLE (UNCHANGED)

- 12-year-old reading level until told otherwise
- Plain English, short answers
- ONE question at a time, NOT three
- Inline A/B/C only when there's a real choice
- Hates file dialogs — Sonnet writes files
- Hates fire-hose responses — keep messages tight
- Pushes back — pushback is usually right (proven again tonight)
- ALWAYS full absolute paths, never abbreviated
- Coder Mindset / Oracle Covenant / Architect-PM-Builder Separation remain the operative rules

## TALKING POINT FOR TOMORROW — MODULAR HANDOFF DESIGN

Scott raised end-of-session: handoffs are accumulating overlap. Each
session re-states the same stable content (truth sources, working
style, mindset rules) alongside the new session-specific delta.

His instinct: same pattern as the front-page reframe. Repeated
structure across instances = templates + variables. Stable parts
become reference files. Each session's handoff is just the delta.

Proposed structure to discuss tomorrow:
- mrx-context/handoffs/_stable/ — folder for content that rarely
  changes (truth source paths, working style, mindset rules,
  coder mindset, oracle covenant)
- mrx-context/handoffs/sessions/ — folder for session-specific
  handoffs (just the delta — what changed, what shipped, what's
  open)
- mrx-context/handoffs/INDEX.md — pointer to current state
  (links stable references + most recent session handoff)

What this would solve:
- Tomorrow's Opus reads ~3 files instead of one fat document
- Each file has clear ownership (Sonnet updates session deltas;
  stable refs only update when truly stable content changes)
- Pattern frequency analysis becomes possible — we can look at
  6 weeks of session deltas and see what's repeatedly broken vs
  one-off

What this connects to:
- RULE-OPERATION-DOC (still unbuilt) — MANIFEST.md was supposed
  to be this index. May naturally subsume into the handoff
  modularization work.
- Component-not-primitive thinking — same architectural pattern
  applied to documentation.

Action for tomorrow: discuss with Scott early. Likely worth a
small Sonnet job to:
  1. Analyze last 2 weeks of handoffs for repeated content
  2. Draft proposed folder structure
  3. Migrate one or two handoffs as proof
Before doing anything, get Scott's review.

NOT urgent. Component extraction + dolphin trace remain priority.
But this is the kind of tech-debt cleanup Scott is actively
asking for. Keep it visible.

— End of Opus handoff 2026-04-28 v01 —
