# NEXT MOVES — Decision tree for post-Chunk D work

**Date:** Friday 2026-05-01, late evening
**Author:** Opus (this session)
**Audience:** Fresh Opus, tomorrow morning + future architects
**Purpose:** Remove "Scott has to remember this" decisions from his head and put them on paper

---

## Read this doc when

- You're a fresh Opus ramping for the next session
- You've already read HANDOFF_LOG.md's 2026-05-01 entry
- You know Chunk D shipped (commit 1519912) and Bug 1 is fixed
- You're trying to decide what to ship next without re-deriving priorities from cold

If any of those aren't true, go read HANDOFF_LOG.md first. This doc assumes that context.

---

## SECTION 1 — V2 MISS CLEANUP PRIORITY ORDER

After Chunk B' (Lemonwood) and Chunk D (Bug 1 confidence fix), 5 V2 misses remain from the original 10-item scoring:

| # | Miss | Type | Estimated effort | Risk | Visible win |
|---|---|---|---|---|---|
| 1 | `with and T` (W&T Offshore) — 6 occurrences | Reader inconsistency | Medium | Medium | High |
| 2 | `Warren seal` → `Warren Seal` | Reader miss | Low | Low | Low |
| 3 | `25 years ago` → `Twenty-five years ago` | Reader/Writer judgment | Medium | Low | Medium |
| 4 | `No no` → `No -- no` | Writer truncation | Low | Low | Low |
| 5 | `flew into give` → audio-dependent | Reader flag, no fix | High (needs audio) | High | Unknown |

### Recommended ship order

**Ship #2 (Warren Seal) FIRST.** Reasoning:
- It's the cheapest, most mechanical fix in the pile — likely a NAMES_LOCK addition under "People" category
- Same proven pattern as Lemonwood (Chunk B'). One name added, one re-run, one verification
- Low risk, low effort, immediate measurable win
- Builds confidence in the chunked workflow before we touch prompts
- **Action:** Add `"Warren Seal"` to NAMES_LOCK in `_run_halprin_mini.py`. Re-run Stage 3.1 (~$0.95). Verify FLAG → REWORD with FIX confident marker.

**Ship #4 (No no) SECOND.** Reasoning:
- Writer prompt clarification only — no NAMES_LOCK touch
- Low risk: the rule "self-correction `[word] -- [word]` keeps both words" is unambiguous
- Cheap test loop: re-run only the relevant batch, not the full pipeline
- Touches the V2 Writer prompt — first prompt patch since V2 deployed, useful canary for the prompt-edit workflow
- **Action:** Patch Writer prompt em-dash insertion rule. Add a few-shot example using a different word pair (NOT "no no" — see Chunk B' lesson on memorization tests). Re-run, verify "No -- no" appears in OUR_FINAL.txt at the relevant turn.

**Ship #1 (with and T) THIRD.** Reasoning:
- Highest-visibility miss (6 occurrences in attorney section), but more complex than the first two
- Reader catches batch 1 occurrence, misses 6 later — either prompt context decays in later batches, or the later batches don't have enough surrounding context for "W&T Offshore" to register as a company name
- Needs anomaly inspection FIRST: fetch all 7 turns where "with and T" appears, check what the Reader said about each in `anomalies.jsonl`. If Reader didn't flag at all in batches 2-10, it's a prompt issue. If Reader flagged but Writer FLAG'd instead of REWORD'd, it's a Writer/lock issue.
- **Action:** Recon first — Sonnet posts a table of all 7 "with and T" occurrences with Reader's anomaly note (or "no anomaly recorded") for each. Opus then specs the right fix based on the pattern.

**Ship #3 (25 years ago) FOURTH.** Reasoning:
- Tests the state module's number-spelling rule for Louisiana Engineering depos
- Higher complexity: requires checking whether the rule is in the Reader prompt OR the state module that gets injected at runtime, AND whether Writer would auto-spell or just FLAG
- May surface a state-module-vs-prompt architecture question that's worth its own discussion
- **Action:** Recon — read the LA Engineering state module and the V2 Reader prompt, find where number-spelling is (or isn't) defined. Then spec.

**SHIP #5 (flew into give) LAST OR DEFER.** Reasoning:
- Audio-dependent. The Reader correctly flagged it as uncertain ("flew into give" doesn't parse semantically); the question is what it should be ("threw into give"? "flew into Geebee"? something else entirely).
- **No text-only fix can solve this.** This is the canonical case for the Comprehension Agent / audio verification work (see Section 4).
- **Recommendation:** Skip this one until Comprehension Agent / Whisper integration ships. Park it as the test case that proves the audio layer works.

### What NOT to do

- **Do not bundle multiple V2 misses into one Sonnet chunk.** Each fix is small enough that the spec → recon → build → verify loop is cheap, and bundling makes failure attribution hard. One miss per chunk.
- **Do not add Warren Seal AND `with and T` to NAMES_LOCK in the same commit.** Even though both are NAMES_LOCK additions, keep them separate so we can attribute any test failures cleanly.
- **Do not patch the Writer prompt without re-reading the current Writer prompt first.** The 2026-04-30 V2 deployment may have changed pieces of it Sonnet's recon doesn't know about.

---

## SECTION 2 — apply.py BUG 2 SCOPING (Chunk E)

Bug 2 from this session: `apply.py` has a 1-for-1 multi-token substitution constraint that silently skips proposals where `before` and `after` token counts differ. AND the runner's `proposals_map` has the same `proposal_id` cross-batch collision Bug 1 had.

**Net effect today:** `corrected_turns.json` is essentially a no-op for any multi-batch run. Stage 5's `render_turn` re-applies all proposals from scratch on the original Stage 2 text, so OUR_FINAL.txt is correct. Only the intermediate artifact is wrong.

**As of Chunk D:** The silent failure is now visible — `logger.warning` fires when `ApplyHardBlock` is caught. Any future pipeline run will surface this in logs.

### When to fix Bug 2

**NOT YET. Park until one of these triggers fires:**

1. **A new pipeline component starts reading `corrected_turns.json` directly.** Today, only Stage 5 reads it, and Stage 5 doesn't trust it (re-applies everything). If anything else starts reading it as truth, Bug 2 becomes user-facing.
2. **Stage 5 architecture changes such that re-applying from scratch becomes expensive or wrong.** E.g., if Stage 5 starts streaming, or if proposals start having side effects beyond text substitution.
3. **Onboarding a 2nd CR or 2nd state module.** New CR/state combinations may produce more multi-token proposals (compound words, name expansions) and the silent skip rate could grow. At that point, the warning frequency in logs becomes the trigger.
4. **Production deployment.** Before MyReporterX serves a real customer depo, `corrected_turns.json` needs to be the ground truth artifact. Bug 2 must be fixed before that ship.

### Estimated scope when we do fix it

Two pieces:
- **Multi-token apply** — generalize apply.py to accept any `(before_token_count, after_token_count)` ratio. Probably ~30 lines, one file.
- **proposal_id collision** — same Option 3 natural-key pattern from Chunk D. ~10 lines, one file.

Probably one chunk. Maybe two if the test surface is bigger than expected. **Hard gate from Scott** because it touches Stage 3 core.

### Reference

- Bug surfaced: HANDOFF_LOG.md 2026-05-01 entry, "BUGS SURFACED THIS SESSION" section
- Visibility added: Chunk D commit 1519912 (apply.py warning logger)
- Prior decision context: HANDOFF_LOG.md 2026-04-26 EOD handoff "CRITICAL DESIGN DECISIONS LOCKED" — the locked "positional joins" decision that Chunk D unlocked. Chunk E will continue that unlock for proposal_id specifically.

---

## SECTION 3 — DIFF METHODOLOGY LOCKDOWN

The 827 baseline diff count from `audits/HALPRIN_MINI_3WAY_DIFF_V2.md` is currently **unreliable as an acceptance criterion** because Sonnet could not reproduce it. Sonnet's recon got 4,486 changed lines on V2 and 4,252 on V1 using `unified_diff` with markers stripped on pages 13-54.

The original audit was likely produced by a section-aware script (treating cover/index/appearances/Q&A/cert/errata as separate diffs) that wasn't documented at write time.

### Why this matters

Going forward, every V2 miss cleanup chunk wants a "diff line count went down" success metric. Without methodology lockdown, that metric is unfalsifiable — different scripts produce different numbers and we can't tell whether a fix actually reduced the diff or whether the methodology shifted.

### Recommendation

**Park as Chunk F (low priority, ~30 min work, do during a low-energy session).**

Spec for Chunk F:
1. Inventory: find all diff scripts in the repos. Likely candidates in `audits/`, `_run_halprin_mini.py`, `tests/`. Confirm whether the original 827 script still exists.
2. Decide: section-aware diff vs unified_diff with markers stripped. Section-aware is closer to how MB would read the doc; unified is closer to how Sonnet would test programmatically.
3. Pick one. Document the choice in `audits/DIFF_METHODOLOGY_v01.md`. Update HANDOFF_LOG.md with the decision.
4. Re-baseline V1 and V2 with the chosen method. Update audit files with new numbers.

### Until Chunk F ships

**Acceptance criteria for V2 miss chunks should NOT include diff line counts.** Use these instead:
- Specific REWORD entry inspection in `proposals.json` (the `before` → `after` content matches expected)
- Visual spot-check of the relevant turn in OUR_FINAL.txt (correct marker, correct text)
- pytest still passing (no regression)
- Cost is within expected range

These are what Chunks B' and D actually used and what worked.

---

## SECTION 4 — COMPREHENSION AGENT DECISION FRAMING

Last night's Opus 4.7 note laid out 5 architectural options for the comprehension layer. The shortlist:
- **Option 3** — Comprehension reads Whisper transcript first, advises Reader at uncertainty points (Scott's original instinct, refined)
- **Option 5** — One Comprehension Agent reads BOTH Whisper and steno transcripts together, treats discrepancies as information rather than errors

The 4.7 note's recommendation: Option 5 long-term, Option 3 as the right first build.

The decision was deferred until V3 prompt + names_lock work surfaces what's left. We're now partway through that work.

### What tonight's work tells us

**Tonight's Halprin V2 results, post-Chunk D:**
- 4 of original 10 misses fixed by V2 prompt alone (your, permission, permit, under paid)
- 1 of 10 fixed by Lemonwood NAMES_LOCK addition (now FIX confident after Bug 1 fix)
- 5 misses still open: Warren Seal, with and T, 25 years ago, No no, flew into give
- Of those 5: 4 are text-fixable (NAMES_LOCK or prompt patches), 1 is audio-dependent (flew into give)

**The signal:** The remaining defect distribution is roughly 80% text-fixable, 20% audio-dependent. That ratio matters for the architecture decision.

### What we still don't know

- Does the 80/20 ratio hold across other depos (Brandl, Easley) or is it Halprin-specific?
- Of the audio-dependent cases, how many resolve with whole-file Whisper alone (Option 3) vs requiring side-by-side reconciliation (Option 5)?
- What's the actual cost difference between Option 3 and Option 5 on a 300-page depo? (Estimated $1 vs $1.50-2 — within noise, probably doesn't drive the decision)

### Recommendation

**Stay parked until at least one more depo ships through the V2 pipeline.**

Rationale:
- Halprin alone doesn't tell us whether the 80/20 ratio is real or a Halprin artifact
- A second depo (Brandl is closest to ready) ratifies or breaks the ratio cheaply
- Brandl is also blocked on Tier 3 generalization (Section 5) — tackling that work also surfaces audio-dependence data

**The trigger to revisit: after Brandl runs through the pipeline cleanly.** At that point we have two-depo data and can pick Option 3 vs 5 with evidence.

### If forced to pick now

Option 3 first, plan to graduate to Option 5 if data shows audio-dependent misses cluster around words where steno and Whisper disagree productively. Aligns with 4.7's read.

But we don't have to pick now. Don't.

---

## SECTION 5 — TIER 3 GENERALIZATION GATE

Halprin's first 13 pages byte-match MB FINAL because they're hardcoded literal templates in `document_composer.py`. Brandl will break if run through the engine today.

Tier 3 generalization = lifting those literal templates into structured templates with three layers of constants:
- **Per-CASE** (YellowRock caption — case name, docket, division, parties)
- **Per-CR** (MB's reporter block — name, credentials, signature)
- **Per-STATE** (Louisiana Article 1434 stipulation, R.S. 37:2554 certificate)

### When to ship Tier 3

**Trigger conditions (any one fires the work):**

1. **Onboarding a 2nd CR.** New CR has different reporter block, different style preferences, possibly different state. Forces all three layers into the open.
2. **Halprin pipeline ships to MB for review.** Once MB starts reading Halprin output, she'll request format adjustments. Each request is easier if the templates are already structured.
3. **Brandl needs to run through the pipeline.** Brandl is in Louisiana too, so per-STATE is reusable, but per-CASE and per-CR (same MB) need slot extraction. Brandl is the cheapest second-depo signal source.
4. **Comprehension Agent decision (Section 4) needs Brandl data.** This circles back — Tier 3 work unblocks Brandl, Brandl unblocks Comprehension Agent decision.

### Recommended trigger

**#3 (Brandl through pipeline) is the right first trigger.** Reasoning:
- Cheapest data signal (no new CR onboarding overhead, no waiting for MB review cycle)
- Per-STATE layer gets exercised first (Louisiana shared between Halprin and Brandl)
- Per-CR is trivially the same (both are MB)
- Per-CASE is the actual generalization work

### Estimated scope

Big. Multiple chunks:
- **Chunk G** — Define `case_info.json` schema with full per-CASE / per-CR / per-STATE structure
- **Chunk H** — Refactor `document_composer.py` cover, stipulation, appearances, videographer to consume the schema
- **Chunk I** — Build `cases/halprin_yellowrock.json` and `cases/brandl_yellowrock.json` from existing data
- **Chunk J** — Run Brandl through pipeline, fix what breaks
- **Chunk K** — Add reporter/witness/errata templates (currently boilerplate, need slot-driven)

This is a real architecture project. Probably 1-2 weeks of focused work. **Hard gate from Scott** before starting.

### Until Tier 3 ships

Halprin work continues against the literal templates. New V2 misses, NAMES_LOCK additions, prompt patches — all safe. Just don't try to run Brandl through the engine without expecting failure.

---

## SECTION 6 — RECOMMENDED MORNING SEQUENCE FOR FRESH OPUS

When Scott opens tomorrow with "ramped":

**Recommended response:**

> Ramped from 2026-05-01 EOD. Four chunks shipped Friday — A (fixtures), C (push), B' (Lemonwood), D (Bug 1 fix). 510 tests passing. Lemonwood and 4 other batch-first proposals now produce FIX confident markers.
>
> Next per the decision tree: Warren Seal → NAMES_LOCK (Chunk B'' — same pattern as Lemonwood). 10-min Sonnet build, ~$0.95 re-run.
>
> Want me to write the Warren Seal spec, or different priority?

That's the opening.

**If Scott says "go on Warren Seal":** Write a spec that mirrors the Chunk B' Lemonwood spec almost exactly. Add `"Warren Seal"` to NAMES_LOCK under People category. Recon + build + verify + ship.

**If Scott pivots to something else:** Read whatever section of this doc is relevant to his pivot. Don't re-derive.

### What fresh-Opus must NOT do tomorrow

- Don't re-litigate the Option 3 join key decision (it's logged with revisit triggers — none have fired)
- Don't propose a Comprehension Agent build (parked until Brandl data)
- Don't propose Tier 3 generalization (parked until Brandl trigger)
- Don't propose Bug 2 fix (parked, has explicit trigger conditions)
- Don't propose diff methodology lockdown unless Scott asks (low priority)
- Don't ask Scott "where is X?" — read MANIFEST.md and HANDOFF_LOG.md first

### What fresh-Opus SHOULD do tomorrow

- Honor the chunked workflow (designed Friday — see HANDOFF_LOG.md "NEW WORKFLOW" subsection)
- Honor the end-of-chunk logging rule (every chunk gets a paragraph appended to HANDOFF_LOG.md the moment it ships)
- Use definitive recommendations, not A/B/C menus, when the right call is clear
- Push back on Scott when his pushback feels right and his pushback feels wrong — both happen, and his pushback is usually right

---

## CROSS-REFERENCES

- HANDOFF_LOG.md → 2026-05-01 entry (today's full session log)
- HANDOFF_LOG.md → 2026-04-30 v02 (V2 deployment + 10-item miss inventory)
- audits/HALPRIN_MINI_3WAY_DIFF_V2.md (the unreliable 827 number — see Section 3)
- audits/V1_VS_V2_COMPARISON.md (the 10-item scorecard)
- specs/2026-05-01_CHUNK_D_ANOMALY_ID_COLLISION_FIX.md (recon-only spec from this session — superseded by SPEC 2 build)

— End of decision tree —
