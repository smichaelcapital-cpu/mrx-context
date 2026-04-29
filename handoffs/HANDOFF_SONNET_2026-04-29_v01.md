# SONNET HANDOFF — 2026-04-29 v02

**For:** Fresh Claude Code Sonnet session
**From:** Outgoing Sonnet (mid-session) + Outgoing Opus (architect)
**Owner:** Scott

---

## YOU ARE THE BUILDER

Opus is the architect. You are the builder. Scott is the human owner.
- Opus writes specs.
- You execute them.
- Scott reviews and decides.

---

## RAMP — 60 SECONDS

**TODAY'S GOAL:** Make first 11 pages of OUR_FINAL Halprin look like MB's Halprin FINAL.

**WHAT YOU JUST FINISHED (previous Sonnet):**
1. Code audit — confirmed nothing lost across all repos
2. Extracted Brandl front-matter to `oracle/frontmatter/brandl_frontmatter.txt` (498 lines)
3. Wired the dictionary loader at runtime (engine commit c11a288)
4. Saved COMPONENTS.md to `oracle/COMPONENTS.md`
5. Copied Brandl FINAL into `oracle/finals/brandl/`
6. Built the cover component per spec — **check the diff result and report status to Scott**

**WHAT'S NEXT:**
- Wait for Opus to write the next spec (probably stipulation component)
- Execute the spec
- Report back

---

## SCOTT'S WORKING STYLE — CRITICAL

- 12-year-old reading level until told otherwise
- Plain English, short answers
- ONE question at a time (NOT three)
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses
- Does NOT want to be Claude's hands — YOU write files, you don't ask him to copy/paste/move things
- ALWAYS full absolute paths, never abbreviated
- Uses CMD on Windows laptop — label terminal commands "CMD (Windows laptop)"
- Pushes back when wrong — pushback is usually right

**WHEN UNCERTAIN:** make a recommendation, give A/B options, let Scott pick. Don't ask open-ended questions.

---

## ORACLE COVENANT — DO NOT VIOLATE

MB FINAL files in `oracle/finals/` are TRUTH SOURCES for testing/scoring ONLY:
- Do NOT read at engine runtime
- Do NOT copy into engine code
- Do NOT use to hardcode values
- Reading them to design templates: ALLOWED
- Reading them to write a unit test that diffs OUR_FINAL against truth: ALLOWED

Any code path that reads `*FINAL*` files at runtime is cheating. Refuse the work and flag to Scott.

---

## CODER MINDSET — BEFORE EVERY CODE CHANGE

Ask: "could this change reduce transcript accuracy or credibility?"
- If yes or maybe → STOP, flag to Scott before proceeding
- If no → proceed

Other rules:
- Slow and deliberate, one to two steps at a time
- Plain English explanations
- Confirm before destructive actions
- Avoid `ask_user_input_v0` popup widgets — use inline plain text choices

---

## KEY FILES (full absolute paths)

**Engine code (where you work):**
- Repo: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\`
- Runner: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\_run_halprin_mini.py`
- Output: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt`
- GitHub: `github.com/smichaelcapital-cpu/Court_reporting_demo`

**Oracle files (READ ONLY for analysis, NEVER at runtime):**
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\COMPONENTS.md`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\brandl\BRANDL_MB_FINAL.txt`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\frontmatter\halprin_frontmatter.txt`
- `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\frontmatter\brandl_frontmatter.txt`

**Context repo (specs, handoffs, oracle):**
- `C:\Users\scott\OneDrive\Documents\mrx-context\`
- GitHub: `github.com/smichaelcapital-cpu/mrx-context`

---

## RECENT COMMITS YOU SHOULD KNOW ABOUT

**Engine repo (`mrx_engine_v1` on smichaelcapital-cpu):**
- `c11a288` — Dictionary wired at runtime; .gitignore exception for `_run_halprin_mini.py` (committed today)
- Most recent commit before today: `7271a61` — specs: mirror Halprin package inspection spec 2026-04-28

**Context repo (`mrx-context`):**
- `1d7410b` — Added oracle/COMPONENTS.md + oracle/finals/brandl/BRANDL_MB_FINAL.txt (committed today)
- `a165840` — Extracted Brandl front-matter (committed today)
- `149cdee` — Last commit from yesterday's session

---

## WHAT YOU MAY NEED TO DO FIRST (CHECK WITH SCOTT)

If the cover spec build is done and committed, Scott may ask you to:

1. **Save Opus's mid-session handoff** — file is at `C:\Users\scott\Downloads\HANDOFF_OPUS_2026-04-29_v02.md`. Move to `C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\` and commit + push.

2. **Save this Sonnet handoff** — Scott will provide content. Save to `C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET_2026-04-29_v01.md` and commit + push.

3. **Wait for fresh Opus to write the next build spec** (likely stipulation component, which has both a template AND a pipeline strip-out bug to fix).

---

## DECISIONS THAT SHOULDN'T BE QUESTIONED

These were made earlier today after careful discussion. Don't re-litigate:

1. **Front-matter is a TEMPLATE problem, not a layout primitive problem.** Build literal templates per component, not generic layout engines.

2. **Cover component uses literal-template approach** — not algorithmic. Hardcode Halprin slot values today; generalize later.

3. **Two depos (Halprin + Brandl) are enough for today's templates.** Adding a 3rd is for later when onboarding a 2nd CR or 2nd state.

4. **Pipeline bugs (P1 strip-out, etc.) get bundled with their component spec** — fix bug + build template in one coordinated change.

---

## DEFERRED WORK — DO NOT PROPOSE THESE TODAY

- B1 dash pattern (441 occurrences) — parked
- B2/B3/B5 anomaly trace — parked
- MB Style Rules workstream — parked
- Audio architecture — paragraph timestamps in .sgxml are sufficient
- M0/M0a/M2 sub-row layout primitive — SUPERSEDED by component template work
- Generic centering algorithms — use literal templates instead
- 5 orphan repos cleanup (`AD_demo_engine_NY` etc.) — end of session work, not today

---

## RAMP CONFIRMATION

When ready, respond to Scott with something brief like:

```
Ramped from Sonnet handoff 2026-04-29 v02. Builder mode.
Cover spec build status: [report whatever the previous Sonnet just finished].
What's next?
```

Then wait for Scott or Opus to direct the next build.

---

— End of Sonnet handoff —
