# HANDOFF — OPUS — 2026-05-09 MIDDAY 3:30
For: Fresh Opus, next session
From: Opus (today's midday session — clean stop after Gate 4 v0 ship)
Owner: Scott
Builder: Sonnet (today's session, also handing off after Gate 4)

## RAMP — READ IN ORDER

https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/fingerprint_architecture_decisions.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/design/fingerprint_architecture_copilot_2026-05-08.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-09_FINGERPRINT_V0_SPEC.md
This handoff in full

After reading: confirm in ONE LINE: "Ramped from Opus handoff 2026-05-09 midday 3:30. Ready."
DO NOT skip CODER_MINDSET. Multiple sessions ago this was the failure mode.

---

## ONE-LINE STATE

Fingerprint v0 shipped end-to-end. Four gates, four commits, 14 hallucinated em-dashes blocked from Halprin mini OUR_FINAL.txt. Architecture is live. Brandl ceiling untouched. Next move is yours to set.

---

## TODAY IN ONE PARAGRAPH

Ramped at 1:30 PM. Cleaned up handoff drift (May 9 files were in repo root, moved to handoffs/). Renamed the Copilot review file to match its content header. Read the architecture decisions and the Copilot review verbatim. Drafted the v0 spec with Scott using a tollgate frame (each module = checkpoint with input contract / output contract / acceptance criteria / failure modes). Spec saved as specs/2026-05-09_FINGERPRINT_V0_SPEC.md. Built v0 gate-by-gate with Sonnet — Gate 1 (YAML files), Gate 2 (loader module + 6 tests), Gate 3 (is_forbidden_token + 3 v1+ stubs + 7 tests), Gate 4 (assemble_final.py wired + 4 tests + e2e proof). All four gates green. 864 tests passing, no regressions. v0 enforces one rule: MB never types `--`. End-to-end proof: 14 LLM-hallucinated em-dashes dropped, all logged.

---

## WHAT SHIPPED TODAY

**4 fingerprint gate commits (engine repo):**

- `60b7681` — Gate 1 (mrx-context: YAML files + validator)
- `abe2908` — Gate 2 (loader module + 6 tests)
- `ab5c1d7` — Gate 3 (is_forbidden_token + 3 stubs + 7 tests)
- `8954b61` — Gate 4 (assemble_final.py wired + 4 tests + e2e)

**2 admin commits (mrx-context repo):**

- `8b01493` — handoff drift fix (move May 9 files to handoffs/)
- `5ad9352` — Copilot review file rename

**Spec saved:**

- `specs/2026-05-09_FINGERPRINT_V0_SPEC.md` (358 lines, locked)

---

## ARCHITECTURAL DECISIONS LOCKED THIS SESSION (DO NOT RE-LITIGATE)

1. **Tollgate frame for the fingerprint subsystem.** Four gates, each with a contract: required input, expected output, acceptance criteria, failure modes. Future fingerprint work extends this frame.

2. **Facts-and-inferences split inside every fingerprint file.** Each layer has `observed:` (durable raw data) and `inferred:` (rules derived from data). Inferences can be regenerated as our reasoning improves; observations don't change. Copilot's recommendation, adopted in full.

3. **List merge = replace, not append.** Reporter layer's `forbidden_tokens` list replaces universal's wholesale. If we ever need additive, that's a v1+ design conversation. Don't change this lightly — it touches every CR onboarding behavior.

4. **Hook point = post-compose, pre-paginate.** Filter runs on LogicalLine objects while turn_idx is still attached. After `lay_out_pages()` text becomes a flat string and turn_idx is gone — too late.

5. **Whitespace handling on token removal:** surrounded → collapse, wedged → insert space, leading/trailing → no insert. JSONL log captures `whitespace_inserted` flag.

6. **Duck-typed fingerprint param in stage5.** No import of the Fingerprint class into stage5. Deliberate decoupling. The engine consumer doesn't need to know the loader's type.

7. **Default-allow, not default-deny.** Scott raised AWS least-privilege framing. Decided: default-allow for token-level. Default-deny only makes sense for narrow scopes (e.g., punctuation), candidate for v1+.

8. **v0 enforces ONE rule (em-dash forbidden) to prove the loop.** Everything else (full Identity, Translation Artifacts, Lexical Preferences, Risk & Review, Drift) is defined in YAML but not enforced. Belt-and-suspenders against premature complexity.

---

## SCOPE-DECISION NOTES

- **Old MB.yaml pattern data** (Q-label freq, doubled tokens, uh-huh frequency, etc.) was wiped when Gate 1 overwrote MB.yaml. Data is not lost — it's in git history and in `io/analysis/_cross_depo_scan/cross_depo_pattern_table.md`. We deferred migrating it into the v0 structure because:
  - Each pattern needs to be classified observed-vs-inferred before it lands
  - v0's job was to prove the wiring, not to be data-complete
  - Migration is a clean separable task for next session

- **Literal templates** (cover, appearances, stipulation, videographer opening) are NOT filtered by the fingerprint. They bypass compose_document(). Acceptable for v0 because they're static. If we ever generate them dynamically, extend the filter.

- **Brandl ceiling untouched.** v0 was a Halprin mini proof, not a Brandl run. We have not measured impact on the 49.5% Brandl ceiling. That's a future session task.

---

## WHAT'S NEXT — RECOMMENDATION

In priority order. Scott will pick.

**1. Migrate old MB.yaml data into v0 observed/inferred structure** (highest leverage, builds on what we have)

- Read `io/analysis/_cross_depo_scan/cross_depo_pattern_table.md`
- Classify each pattern: observed fact vs inferred rule
- Add to `fingerprints/reporters/MB.yaml` under the right layer
- Some patterns will become new `forbidden_tokens` entries (free expansion of v0 enforcement)
- Others go in `lexical_preferences`, `risk_and_review` for future enforcement

**2. Build Aligner+Differ v0** (the bigger play, designed May 3)

- Tool that diffs Raw RTF against MB FINAL at turn level
- Every diff is a labeled training example
- Across multiple MB depos: intersection = habitual MB style → fingerprint
- This is the engine that generates fingerprint rules from data
- Far more work than #1 but the strategic move

**3. Run Brandl with v0 fingerprint enabled** (measure real impact)

- Quick scoreboard run
- Tells us whether v0's one rule moves the 49.5% ceiling at all
- Sets baseline for future fingerprint expansions

**4. Add jurisdiction layer (louisiana.yaml)** (proves layer-merge in production)

- Currently only the reporter layer is populated
- Adding a jurisdiction layer with one or two real LA-specific rules tests the merge in real conditions

**My pick: #1 then #3.** Migrate the data we have, run Brandl to measure, then decide between Aligner+Differ and jurisdiction layer based on what Brandl tells us.

---

## OPEN ITEMS / TECH DEBT

- **TD-001** (writer JSON truncation, patched not solved) — still real, weeks of work, parked
- **TD-002** (stale W&T e2e test, miss ≥4 expected, engine finds all 9) — quick fix, low effort, surface to Scott if you have 10 minutes
- The cross-depo scan table (`io/analysis/_cross_depo_scan/cross_depo_pattern_table.md`) is unintegrated rich data. Useful for #1 above.
- Brandl baseline scoreboard doesn't exist yet at v0 fingerprint level. If Scott wants to track ceiling lift over time, we need a baseline run.

---

## SCOTT'S WORKING STYLE (REMINDERS)

- 12-year-old reading level until told otherwise
- Plain English, ONE question at a time, never stack
- Inline A/B/C only when there's a real choice
- Code-fenced blocks for ANY content Scott copies to Sonnet
- Always full absolute paths
- Hates fire-hose responses
- NEVER make Scott copy-paste content between AIs unnecessarily — Sonnet writes to repo, pushes, replies confirm. Then both Opus and Sonnet read from repo. The repo IS the bridge.
- Reverse-engineer rules from MB FINALs before asking MB
- Default rule: Scott commits and pushes engine repo. Sonnet may push mrx-context repo. (Today's session Scott granted Sonnet temporary engine push authority — that authority is REVOKED at session end. Restore default.)
- If Scott says he's tired, frustrated, or fading — slow down, narrate, do not push harder
- Slow is smooth. Smooth is fast. He cited Alan Turing and Enigma today: "We have a depo of 300 pages. It doesn't change. We're in a finite world. We're gonna figure this out."

---

## TWO SESSION NOTES YOU SHOULD KNOW

**One:** Outgoing Opus burned a real chunk of context early-session by asking Scott to copy-paste a long Copilot file from Sonnet's terminal into chat. Scott correctly called this out as wasteful — the file was already in the repo, Opus could have just searched it via project knowledge. Lesson: when something might already be in the repo, search first. Don't make Scott a clipboard.

**Two:** Outgoing Opus also wrote the v0 spec inline in chat first (long), got Scott's approval, then tried to forward it to Sonnet via paste. That's two pastes when one would do. The right move is: write the spec as a single instruction addressed to Sonnet with the file content in a code block. Scott pastes once. Sonnet saves. Done. Lesson: if it's going in the repo, write it for Sonnet directly. Show Scott if he wants to see it before paste, but don't draft it twice.

---

## CODER MINDSET REMINDERS

- Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag.
- Three Brains: Engineer (can?), Architect (should?), Owner (worth?).
- RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED. RULE-SPEC-BEFORE-BUILD.
- Slow is smooth. Smooth is fast.

---

*End of Opus midday 3:30 handoff.*
