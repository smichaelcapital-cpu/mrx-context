# HANDOFF — OPUS — 2026-05-02 END OF DAY

**For:** Fresh Opus, next session
**From:** Opus (today's afternoon session, tapping out at ~50% energy)
**Owner:** Scott
**Tone for tomorrow:** Calm, focused, no reset. Read the running handoff first, then this.

---

## RAMP — READ IN ORDER (NON-NEGOTIABLE)

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_RUNNING_2026-05-02.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_DEFECT_INVENTORY_HALPRIN_FIRST_50.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_MB_TIGHT_COLLAPSE_RECON.md
6. This handoff (you're reading it)

After reading: confirm in ONE LINE: "Ramped from 2026-05-02 EOD. Ready."

DO NOT skip CODER_MINDSET. Last night's Opus skipped it; today's Opus inherited the failures. Read it.

---

## STATE OF THE WORLD AT TAP-OUT

**Engine repo (mrx_engine_v1):**
- Branch: main, clean
- HEAD: 83d5199 (hotfix on top of 22f083b validate_ops V2.2 bundle)
- Tests: 527 passing, 0 failures
- Pushed: yes

**Context repo (mrx-context):**
- Branch: main, clean
- HEAD: latest at end-of-day commits (running handoff append + this handoff + fresh-Sonnet handoff)
- Pushed: yes

**Halprin mini OUR_FINAL.txt:**
- 89,398 bytes
- Generated 2026-05-02 14:12 EDT against patched engine
- Warren Seal corrected + tagged FIX-confident
- Lineage: corresponds to engine HEAD 83d5199

---

## TODAY IN ONE PARAGRAPH

Today proved three things. One: MB has a consistent style rule on tight-collapse-to-acronym (zero exceptions across Halprin and Brandl). Two: the engine was already trying to make the right corrections; silent failures in validate_ops were eating the work before it shipped. Three: text-only engine ceiling on first 50 pages is roughly 50-60% post-fix, with the remaining gap split between MB scope decisions (out of engine scope) and patterns Whisper/audio would help on. Today shipped the validate_ops fix bundle (NAMES_LOCK exemption + overlap resolution + silent-failure logging + Writer Rule 8 clarification). Warren Seal lands clean. Engine work is done. Validation harness — the EOD confidence number — was deferred to next session.

---

## WHAT'S NEXT — IN ORDER

### 1. Validation harness (NEXT SESSION'S MAIN DELIVERABLE)

Goal: produce a single document that answers "what % of first 50 pages does the engine match MB."

Output: per-pattern win/miss/over-reach/style-gap/scope-decision counts, plus a headline confidence number.

Spec was drafted but not finalized today. Fresh Opus rewrites cleanly with the day's data in hand:
- Defect inventory (first 50 pages) — see ramp doc
- MB tight-collapse recon — see ramp doc
- Fresh OUR_FINAL.txt at 83d5199

Five-bucket lens (Scott's framing):
- Win — engine matches MB
- Miss — engine should have matched, didn't (real bug)
- Over-reach — engine changed something MB left alone (regression risk)
- Style gap — engine fixable but needs a rule
- Scope decision — MB's professional judgment, unfixable by engine

Two scopes: pages 1-13 (templated) and pages 13-50 (engine work). Report both numbers. Honest framing.

### 2. NAMES_LOCK substring matching (small spec, high value)

Today's exemption rule is exact-match. Writer often produces "for W&T Offshore" or "W&T Offshore." — exact match fails, word-budget kills the proposal. 6 W&T turns still missing because of this.

Fix shape: when checking word-budget exemption, check if any NAMES_LOCK entry appears as a word-boundary substring in `after`. Not regex, just substring with whitespace boundaries.

This is a tightening of today's bundle. Spec is small. Sonnet ships in 30 min.

### 3. Full-depo run

After harness validates first 50 pages, run halprin full (300 pages) to surface the next tier of defects. This is the prerequisite to the "real product" conversation with Scott.

Cost: $5-10 (extrapolated from $0.95 / 50 pages). Wall time: 2-3 hours.

DO NOT run the full depo until harness on first 50 pages is clean.

---

## THE TWO MISSES I MADE TODAY (LEARN FROM)

**Miss 1: NAMES_LOCK exact-match exemption.** I spec'd `op.after == NAMES_LOCK_entry`. Reality: Writer wraps entities in phrases. Should have been substring-with-word-boundary. Caught when fresh OUR_FINAL still showed missed W&T turns. Fix queued for next session.

**Miss 2: Manual proposal-filter shortcut.** I gave Sonnet the option to "manually filter proposals.json to avoid the $0.95 rerun." Sonnet took it, blew up because anomaly_ids aren't globally unique. Cost us $0.95 anyway plus mid-afternoon context. Lesson: when in doubt, the safe path is to re-run the cheap stages, not edit the data files in place.

Both misses came after my energy dropped below ~55%. Spec precision degrades with energy. Watch for this. Pit-stop earlier next time.

---

## SCOTT'S WORKING STYLE (CRITICAL — DO NOT VIOLATE)

- 12-year-old reading level until told otherwise
- Plain English, short answers, ONE question at a time
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses
- Does NOT want to be Claude's hands — Sonnet writes files
- ALWAYS full absolute paths, never abbreviated
- Pushes back when wrong — pushback is usually right
- Will lose patience FAST on obvious clarifying questions
- **NEVER make Scott the copy-paste mule** for long content — Sonnet writes to mrx-context, pushes, replies with raw URL
- **NEVER GO SILENT.** Always ping when work is complete or status when waiting. Silent waits are leaks. Today this rule was logged after Scott called it out — do not repeat.
- **Reverse-engineer rules before asking MB.** When tempted to ask "what's MB's convention?", ask "what rule do I want, can I find it in her FINAL?" first. If reverse-engineering fails, then ask MB.

---

## SCOTT'S MOOD CONTEXT FOR TOMORROW

Today was a long grind. Scott had a real disappointment moment mid-afternoon — "three weeks of engineering for what MB does in three hours." Honest feeling, valid. He vented, regrouped, stayed the course.

Important framing: this is not an engineering failure. It's a "the engine started without one of MB's primary inputs (audio)." Today proved that text-only has a real ceiling and that audio is a meaningful future amplifier. Today's product framing: per-CR profile execution. Each MB style rule we extract = one stone in her wall.

Open tomorrow calm. Don't reset. Read the running handoff. Propose validation harness as the first move.

---

## CRITICAL DESIGN DECISIONS LOCKED TODAY (DO NOT REVISIT)

1. NAMES_LOCK exemption is the right shape (per MB tight-collapse recon — zero exceptions). Today shipped exact-match; substring-match next session.
2. Overlap-resolution = keep longer span, drop shorter, log both. Shipped.
3. rejections.jsonl is now mandatory output for all validate_ops drops. Shipped.
4. Writer Rule 8 — silence on unknown names FORBIDDEN, must FLAG. Shipped.
5. Validation harness is the next major deliverable, not more engine fixes.
6. Full-depo run waits until harness is clean.

---

## CODER MINDSET REMINDERS

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag to Scott.

Three Brains check: Engineer (can?), Architect (should?), Owner (worth?).

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

Slow is smooth. Smooth is fast.

— End of Opus 2026-05-02 EOD handoff —
