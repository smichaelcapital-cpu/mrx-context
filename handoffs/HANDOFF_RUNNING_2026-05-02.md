# RUNNING HANDOFF — 2026-05-02 (Saturday)

**Status:** LIVE — updated periodically through the day
**Owner:** Scott
**Architect:** Opus (this session)
**Builder:** Sonnet (this session)

**Purpose:** Capture everything from today's session as it happens, so
nothing depends on Opus's working memory. At end of day this becomes
the basis for the true HANDOFF_LOG.md entry.

---

## SESSION GOAL

By EOD: Halprin mini OUR_FINAL is MB-readable. Scott has clear
confidence numbers — what % of the first 50 pages the engine handles,
what % is MB judgment we'll never auto-fix. Zero embarrassment risk.

---

## CHRONOLOGY

### ~09:00 — Session start
- Scott fresh. Last night's handoff was missing — this morning had
  ramp-recovery overhead (Opus had to be hand-fed the May-01 EOD
  section because HANDOFF_LOG.md truncates on web_fetch).
- This is the exact failure the parked tiering proposal addresses.

### ~09:30 — Ramp clean
- CODER_MINDSET + ADDENDUM read.
- Engine repo at ce3870d, mrx-context at 65c12e8, 510 tests passing.
- State of world: clean.

### ~09:45 — Sonnet state-of-world recon
- Confirmed repos clean, all key artifacts present.
- Surfaced 3 issues:
  1. OUR_FINAL.txt is stale by ~2 min vs ce3870d (predates last
     night's Warren Seal + W&T NAMES_LOCK additions)
  2. No reusable audit script exists — V2 3-way diff was hand-built
  3. No full-depo runner — only halprin_mini fixture is wired

### ~10:00 — Defect inventory clarified with Scott
Five known defects in first 45 pages:
1. `with and T` → `W&T` — 6 turns remaining
2. `Warren seal` → `Warren Seal` — turn 124
3. `25 years ago` → number-format rule undecided
4. `flew into give` — audio-dependent
5. `No no` → `No -- no` — partial fix only

Scott's framing: don't keep paying for re-runs to find bugs. Run
once, examine all outputs, build a harness that classifies what
the agent can/can't do. Five-bucket verdict lens (win / miss /
over-reach / style gap / scope decision).

### ~10:30 — Writer batch-decay diagnosis (Sonnet recon)
- "Batch-decay" was a mislabel. The real cause is two silent failures
  in validate_ops:
  - check_word_budget — 80% rule blocks legitimate steno-acronym
    compressions on short turns
  - check_coverage — overlapping Reader spans drop entire turn
    silently (Warren Seal turn 124 has two overlapping anomalies)
- Plus a Writer prompt issue (Rule 8 mis-read as "don't touch"
  instead of "produce FLAG op") — accounts for "Crescent" misses.
- All three failures are SILENT. No log, no rejections.jsonl entry.
  Pipeline reports "0 rejections" while quietly killing valid ops.
- Recon report: in HANDOFF_LOG.md context, no separate file.

### ~10:50 — MB tight-collapse recon (Sonnet)
- Saved to:
  https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_MB_TIGHT_COLLAPSE_RECON.md
- HEADLINE: MB's tight-collapse-to-acronym is a CONSISTENT RULE,
  not a judgment call.
  - 11 W&T events in Halprin → all collapsed, zero exceptions
  - 45 Samedan events in Brandl → all collapsed, zero exceptions
  - All ratios 0.33–0.67, all below current 80% word-budget threshold
- Implication: the word-budget check is correctly calibrated for
  random corrections, miscalibrated specifically for this entire
  class of legitimate MB style.
- Surprising find: "Brandl FINAL" in oracle/finals/brandl/ is
  actually MB's raw CAT export, not a formatted final. The data
  is still valid for steno→correction patterns but cannot be used
  to evaluate MB's formatted output style.

### ~11:15 — Mini-MB / per-CR profile concept captured (parking lot)

---

## DECISIONS LOCKED TODAY

1. New rule of thumb: when tempted to ask "what is MB's convention?",
   first ask "what rule do I want, and can I reverse-engineer it from
   her FINAL?" If reverse-engineering fails, then ask MB.
2. Tight-collapse rule shape (data confirmed): exempt validate_ops
   word-budget when REWORD targets a NAMES_LOCK entity. Other
   corrections still subject to the 80% rule.
3. Silent failures in validate_ops are themselves a Prime Directive
   issue — every drop must be logged. Fix bundles with the rule fix.

---

## PARKING LOT (added today)

1. **Anthropic Claude sandbox / shared-filesystem multi-agent pattern**
   — Investigate post-V3, post-tiering. Today's git-as-shared-fs works.
   Bottleneck is handoff fidelity, not file sharing.

2. **Mini-MB / per-CR style profile architecture (NEW)**
   - Today proves MB has a consistent reflex (tight-collapse, zero
     exceptions, ratio 0.33–0.67). We're encoding it via NAMES_LOCK
     exemption. That works only when entities are pre-loaded.
   - Open question: how does engine recognize the reflex on NEW depo
     with NEW entities not in NAMES_LOCK?
   - Two paths: (a) per-case intake — MB hands over case entity list
     at onboarding, engine populates per-case NAMES_LOCK; (b)
     Comprehension Agent (already parked) — AI reads whole depo,
     builds entity registry from context.
   - Bigger frame: each rule we extract = one stone in MB's profile
     wall. AD gets her own profile. Profile becomes the product.
   - Revisit after V3 prompt + tight-collapse fix ship.

3. **HANDOFF_LOG tiering — Scott's simpler proposal (NEW)**
   - Last 2 sessions live in CURRENT.md (small enough for one fetch).
   - Everything older rolls to monthly archive file.
   - Manual moves at end of session, no auto-roll, no edge cases.
   - Simpler than parked tiering proposal; ship Scott's version.
   - When to build: end of today, or tomorrow morning.

4. **"Brandl FINAL" labeling error in oracle**
   - oracle/finals/brandl/BRANDL_MB_FINAL.txt is actually MB's raw
     CAT export, not a formatted final. File is useful for steno→
     correction patterns but NOT for evaluating MB's formatted style.
   - File contains MB's local Cat path on last line — confirms it's
     a rough export.
   - Action: rename or relabel post-today. Don't draw inferences
     about MB's pagination/formatting from this file.

5. **No reusable audit script exists**
   - V2 3-way diff was hand-built. If we're going to validate runs
     repeatedly, we need a scripted audit harness. Build candidate
     for after today's spec ships.

6. **No full-depo runner**
   - Only halprin_mini is wired. Full Halprin RTF lives in
     mrx-context but no engine runner points at it. Build candidate
     for after first-50-pages confidence is locked.

---

## NEXT MOVE QUEUE

(In order, as of last update)

1. Spec the validate_ops fix bundle:
   - Word-budget exemption for NAMES_LOCK targets
   - Overlapping-spans handling (pick longer / drop shorter, log)
   - Silent-failure logging — every drop writes to rejections.jsonl
   - Writer prompt Rule 8 clarification (Crescent → FLAG)

2. Sonnet builds the spec, commits.

3. Re-run halprin_mini ($0.95).

4. Build minimal validation harness — answers "what % of first 50
   pages does engine match MB."

5. Read harness output. Decide ship/no-ship for MB demo.

---

## OPEN QUESTIONS (for Scott)

1. Energy / pacing — sharp enough to argue rule shape during spec
   write, or want Opus to draft solo and review?
2. Number-format rule (`25 years ago`) — fold into validate_ops
   spec, or separate Writer-rule conversation?

---

### ~13:00 — Defect inventory complete (Sonnet)

Spec saved: `specs/2026-05-02_DEFECT_INVENTORY_HALPRIN_FIRST_50.md`

**Method:** Targeted pattern search (difflib alignment unreliable — corrections
shift line wrapping, making line-by-line comparison misleading).

**Engine activity:** 114 annotation touches — 63 FIX, 10 VERIFY, 41 FLAG.

**Key findings by defect category:**

| Category | MB | Engine | Coverage |
|---|---|---|---|
| W&T acronym | 9 | 3 correct | 33% (6 missed by word-budget) |
| Em-dash | 49 | 10 correct | 20% (39 missed, mix of fixable + MB judgment) |
| Warren Seal cap | 1 | 0 | 0% (overlapping spans blocked) |
| Crescent case | 4 | 2 correct | 50% (2 wrong case, Rule 8 issue) |
| SVP title case | 3 | 0 | 0% (scope decision — no rule yet) |
| Sentence spacing | 158 | 0 | OUT OF SCOPE (style gap, formatting pass) |
| flew in to give | 1 | 1 | 100% WIN |
| No -- no | 1 | 1 | 100% WIN |
| underpaid | 1 | 1 | 100% WIN |
| 25-years FLAG | 1 | 1 (FLAG) | 100% correct behavior |

**Overall: ~30% gross coverage pre-fix. Projected ~50–60% after validate_ops
fix bundle (word-budget + check_coverage + Writer Rule 8 prompt clarification).**

**Zero-embarrassment verdict:** Safe to demo with framing — engine catches
high-confidence phonetic/steno errors in batch 1. Diagnosis of batch 2+ miss
is complete and fix is queued. Don't claim a % without noting validate_ops
silent-failure distorts the number.

---

*This file is updated periodically through the day. Sonnet appends
new entries at Opus's direction. Last-updated timestamp goes at the
top of each new section.*
