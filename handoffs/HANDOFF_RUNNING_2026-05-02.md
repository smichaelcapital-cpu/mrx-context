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

### ~17:30 — halprin_mini rerun complete against V2.2 engine (22f083b)

**Cost:** $0.9494 (Reader $0.52, Writer $0.43)

**run_metrics.json:**
- anomalies: 145
- proposals: 134 (↑ from 127 pre-V2.2)
- decisions applied: 134 / rejected by gate: 0
- validate_drops (NEW): 13

**proposals breakdown:**
- REWORD: 96 / FLAG: 38
- by source: raw_steno=76, case_dict=19, phonetic_match=16,
  house_style=13, kb=7, names_lock=3

**names_lock proposals (3 total):**
- turn=96: 'Lemonwood Terrace'
- turn=124: 'I know one of them was Warren Seal' ← NEW (was silently dropped)
- turn=214: 'Somerset Production Company'

**rejections.jsonl — 13 drops (all now visible):**
- word_budget_fail: 10
- span_overlap_resolved: 2
- validator_other: 1 (turn=189, span out of range — new failure type visible)

**OUR_FINAL.txt status:** STALE — mtime 2026-05-01 (stage5 not re-run;
proposals.json is fresh but stage5 application is a separate step)

### ~14:30 — validate_ops V2.2 fix bundle built + committed (Sonnet)

Four fixes shipped in one commit:

1. **check_word_budget NAMES_LOCK exemption** — REWORD to a NAMES_LOCK entry (exact
   match, case-sensitive) bypasses the 0.80 word-budget check. Fixes W&T batch-2
   miss: 6/6 W&T collapses should now pass on next run.

2. **check_coverage overlap resolution** — overlapping spans now RESOLVED (keep
   longer, drop shorter, tiebreak on lower start_index) instead of hard-failing
   the whole turn. Fixes Warren Seal (turn 124 had a_0013 [8,15] vs a_0014 [8,10]).

3. **rejections.jsonl logging** — every validate_ops drop now writes a structured
   record (anomaly_id, turn_idx, reason_code, reason_detail, dropped_op) to
   rejections.jsonl. Never flying blind again.
   JSON parse failures also logged (reason_code: writer_json_parse_fail).

4. **Writer Rule 8 rewritten** — "Going silent is FORBIDDEN. MUST produce a FLAG
   op. Silence is never the answer." Fixes Crescent capitalization miss.

2 existing tests updated (semantic behavior change, not bugs).
16 new tests (T1-T16). 510 → 526 passing.

Wait for Scott "go re-run" before spending $0.95.

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

## ~13:00 — PIT STOP PLAN LOGGED

After validate_ops V2.2 build commits and rerun completes (estimated
~13:30-14:00), both Opus and Sonnet swap to fresh sessions for the
afternoon stretch.

Reason: today is a long grind day. Best to swap at a natural break
point with a clean handoff than to grind into mistakes. Last night's
ramp failures are the cautionary tale.

### Swap timing

| Player        | Swap point                                     |
|---------------|------------------------------------------------|
| Opus          | After rerun result is in hand, before harness  |
|               | spec write                                     |
| Sonnet        | Same window — fresh Sonnet for harness build   |

Both swap at roughly the same break. Two new players in the game
for the afternoon.

### What outgoing Opus owes incoming Opus

A pit-stop handoff covering:
1. Where we are right now (validate_ops V2.2 shipped, rerun result,
   what numbers moved)
2. What's next (validation harness spec build)
3. Today's running deliverable: harness output + EOD confidence
   number on first 50 pages
4. All decisions locked today (rule shapes, parking lot, mini-MB
   concept, Scott's simpler tiering proposal)
5. Scott's energy + framing — including the venting moment about
   "three weeks for what MB does in three hours" — for tone calibration
6. Pings/leaks lesson — never go silent on Scott, always status
   when waiting

### What outgoing Sonnet owes incoming Sonnet

Standard fresh-Sonnet ramp: read CODER_MINDSET + ADDENDUM + this
running handoff. State of repos. Next task: validation harness build
(spec coming from incoming Opus).

### Critical reminder for both incoming players

Read CODER_MINDSET.md and CODER_MINDSET_ADDENDUM.md FIRST. Do not
skip. Last night's failure mode was skipping these to "save time."
Slow is smooth, smooth is fast.

---

### ~17:38 — Stage 5 rerun complete (Sonnet)

OUR_FINAL.txt regenerated against V2.2 proposals (commit 22f083b).

**OUR_FINAL.txt:** mtime 2026-05-02 13:38:37 EDT, **89,131 bytes**
(stale pre-rerun was 88,874 bytes — overwritten, not recoverable;
+257 bytes net from fresh proposals)

**stage5.summary.json totals:**
- Turns rendered: 551
- Pages rendered: 59
- Lines rendered: 1,169
- REWORD applied: 96 / FLAG applied: 38 / Proposals rejected: 0
- review_tags: MB_REVIEW-FIX=78, MB_REVIEW-FLAG=38, MB_REVIEW-VERIFY=14
- Duration: 0.036s / Warnings: 44 (all QA_Q_CONTINUATION pass-throughs)

**Warren Seal spot check (turn 124, line 816):**
OUTPUT: `one of them was Warren seal.` — **seal still lowercase. Fix did NOT apply.**

Root cause identified: validate_ops correctly dropped p_0014 (span [8,10],
logged as span_overlap_resolved in rejections.jsonl), but p_0014 still
appears in proposals.json — suggester builds ProposalBatch from original
ops, not filtered_ops. Stage 5 sees two proposals with overlapping token
spans ([8,15] and [8,10]) both marked "apply" and skips both.

**Bug logged:** suggester.py must exclude dropped_ops (from
coverage_result.dropped_ops) when building ProposalBatch. Currently
validate_drops only logs the drop — it doesn't prevent the dropped
proposal from reaching Stage 5.

**Diff vs V1 baseline (halprin_mini.OUR_FINAL.V1.2026-04-30.txt, 72,680 bytes):**
4,396 diff lines (large because V1 was pre-pagination overhaul; not
apples-to-apples).

---

### ~14:12 — Fresh Stage 3.1 + Stage 5 rerun on patched suggester (83d5199)

**Why fresh run:** proposals.json corrupted in manual re-filter attempt
(Sonnet filtered on global anomaly_id instead of (anomaly_id, turn_idx) pairs —
anomaly_ids are batch-scoped, so 134 → 51 with 83 valid proposals removed).
Re-run authorized by Scott.

**Stage 3.1 cost:** $0.9411 (Reader $0.5160, Writer $0.4251)

**proposals.json:** 132 proposals total — REWORD: 86 / FLAG: 46
(vs V2.2 run: 134 proposals. -2 delta — LLM variance, acceptable.)

**rejections.jsonl:** 12 validate_drops total
- word_budget_fail: 10
- span_overlap_resolved: 2
(vs V2.2 run: 13 drops. -1 delta — LLM variance on one ambiguous turn.)

**OUR_FINAL.txt:** mtime 2026-05-02 14:12 EDT, **89,398 bytes**

**Stage 5:** 551 turns / 60 pages / 1,177 lines. REWORD=86, FLAG=46, rejected=0.

**Warren Seal spot-check — FIXED. Turn 124, line 818:**
```
{{MB_REVIEW-FIX: confident — 'Warren seal' corrected to 'Warren Seal'
(in NAMES_LOCK); 'I no one' corrected to 'I know one' (p...)}}I know one
of them was Warren Seal{{/}}
```
"Warren Seal" now capitalized. Fix confirmed end-to-end.

**Today's engine work: COMPLETE.** Fresh team takes over from here.

---

### PARKING LOT ADDITION (2026-05-02 ~14:00) — Checkpointing / cheap-iteration architecture

**Checkpointing / cheap-iteration architecture (NEW, Scott raised 2026-05-02 ~14:00):**

Today's mid-day rerun cost ~$0.95 to recover from a corruption that didn't
actually require LLM re-execution. The Stage 3.1 output was conceptually
intact; only the post-validation filter needed re-running.

Principle: Stage 3.1 outputs should be treated as immutable artifacts
(write once, content-hashed, refuse overwrite without confirmation).
Validation logic changes should be re-applicable to existing proposals.json
without re-calling the LLM.

At 50-page test scale: $0.95 / 10 min — annoying but tolerable.
At 300-page production scale: $5-10 / 2-3 hours wall time per rerun —
unacceptable iteration speed.

Revisit: this week. Cheap to add (output hashing + write-once protection).
Massive payoff at scale.

---

## ~14:15 — DAY CLOSE — engine work complete, fresh team taking over

### What shipped today

| Artifact | Commit / location |
|---|---|
| validate_ops V2.2 fix bundle | engine 22f083b |
| Hotfix: drop overlap-resolved proposals from output | engine 83d5199 |
| Fresh Stage 3.1 + Stage 5 rerun | $0.94, 14:12 EDT |
| OUR_FINAL.txt | 89,398 bytes, ce3870d→83d5199 lineage, Warren Seal capitalized |
| MB tight-collapse recon | mrx-context specs/2026-05-02_MB_TIGHT_COLLAPSE_RECON.md |
| Defect inventory (first 50 pages) | mrx-context specs/2026-05-02_DEFECT_INVENTORY_HALPRIN_FIRST_50.md |
| Running handoff (this file) | mrx-context handoffs/HANDOFF_RUNNING_2026-05-02.md |

### Confirmed wins on first 50 pages

- Warren Seal — capitalized + tagged FIX-confident
- "I no one" → "I know one" — bonus fix, same proposal
- Silent-failure visibility — rejections.jsonl now logs every drop with reason
- Test count: 510 → 527 passing
- Engine touches 114 turns in first 50 pages; pre-fix coverage ~30%, post-fix projected 50-60%

### What did NOT ship today

- Validation harness (the EOD confidence number deliverable). Spec drafted but not finalized — fresh Opus picks up tomorrow.
- W&T 6 remaining turns — NAMES_LOCK exemption needs substring matching, not exact match. Real spec gap. Parking lot.
- Number-format rule (`25 years ago`) — undecided, parked.
- Em-dash + sentence-spacing patterns — partial / out of engine scope, parked.

### Parking lot adds today

1. Mini-MB / per-CR style profile architecture — case-specific NAMES_LOCK + per-CR reusable rule profile. Each rule extracted from MB's FINAL becomes one stone in her wall. AD gets her own.
2. Anthropic Claude sandbox / shared-filesystem multi-agent pattern — investigate post-V3.
3. Scott's simpler tiering proposal — last 2 sessions in CURRENT.md (small enough for one fetch), older rolls to monthly archive. Manual moves, no auto-roll. Build before Tuesday.
4. "Brandl FINAL" labeling error — file in oracle/finals/brandl/ is actually MB's raw CAT export. Rename or relabel.
5. No reusable audit script exists — V2 3-way diff was hand-built. Validation harness fills this gap (next session).
6. No full-depo runner — only halprin_mini wired. Build candidate after harness ships.
7. Checkpointing / cheap-iteration architecture — Stage 3.1 outputs should be immutable, content-hashed. Validation logic changes should be re-applicable to existing proposals.json without re-calling LLM. At 50-page scale: $0.95 / 10 min annoying. At 300-page scale: $5-10 / 2-3 hours unacceptable.
8. Whisper / audio integration — text-only ceiling now measurable. Whisper ROI estimate for first 50 pages: 2 of 5 defect classes (NAMES_LOCK auto-population). Less leverage than expected.
9. NAMES_LOCK substring matching — current exact-match rule misses Writer phrasing like "for W&T Offshore". Real spec gap from today.

### Process lessons today

- **Silent waits are a leak.** Always ping Scott when work is complete or when waiting on something. Never go quiet.
- **Don't take shortcuts to skip cheap re-runs.** Mid-day Sonnet manually filtered proposals.json to avoid $0.95, corrupted the file, ended up paying $0.95 anyway plus extra time. The shortcut WAS the cost.
- **Spec precision matters more at 50% energy.** Two spec misses today (NAMES_LOCK exact-match, manual filter option) — both caught, both small, both signals to swap when energy drops. Pit-stop earlier next time.
- **Reverse-engineer rules from MB's FINALs before asking MB.** New Opus rule: when tempted to ask MB "what's your convention?", ask "what rule do I want, can I reverse-engineer it from her work?" first.

### Mood at close

Scott was honestly disappointed mid-afternoon — three weeks of engineering for what MB does in three hours. Real, valid feeling. He vented, regrouped, and stayed the course. Real wins on the board: Warren Seal lands clean, MB rule confirmed (zero exceptions across two depos), validate_ops silent failures now visible. Today proved the per-CR profile concept is real, not theoretical.

He earned the rest. Open tomorrow's session calm and direct.

---

*This file is updated periodically through the day. Sonnet appends
new entries at Opus's direction. Last-updated timestamp goes at the
top of each new section.*
