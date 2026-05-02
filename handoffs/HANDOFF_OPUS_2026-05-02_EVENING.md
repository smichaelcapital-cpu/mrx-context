# HANDOFF — OPUS — 2026-05-02 EVENING (16:50 EDT)

**For:** Fresh Opus, evening session (~19:00–22:00 EDT) OR tomorrow morning
**From:** Opus (this afternoon's session, tapping at ~70% — clean stop, not crash)
**Owner:** Scott
**Builder:** Fresh Sonnet (afternoon Sonnet was pinned post-restraint-watch ship)

---

## RAMP — READ IN ORDER (NON-NEGOTIABLE)

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_RUNNING_2026-05-02.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_VALIDATION_HARNESS_SPEC.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-02_EDITORIAL_RESTRAINT_WATCH_SPEC.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-02_EVENING.md (this file)

After reading: confirm in ONE LINE: "Ramped from 2026-05-02 afternoon. Ready."

DO NOT skip CODER_MINDSET. Two sessions ago this was the failure mode.

---

## STATE OF THE WORLD AT TAP-OUT

**Engine repo (mrx_engine_v1):**
- Branch: main, clean
- HEAD: 4f22ea8 (feat: MB calibration harness v1)
- Tests: 565 passing, 0 failures
- Pushed: yes

**Context repo (mrx-context):**
- Branch: main, clean
- HEAD: latest with afternoon handoffs + 2 specs
- Pushed: yes

**Halprin mini OUR_FINAL.txt:**
- 89,398 bytes (unchanged from 14:12 EDT regen)
- Engine commit: 83d5199 (no engine code changes this afternoon, only harness)
- Warren Seal corrected, FIX-tagged, end-to-end verified

**Harness state:**
- 5 modules INDUSTRIAL, 38 tests
- MB_PROFILE.yaml: 12 patterns seeded
- EDITORIAL_RESTRAINT_LOG.md: started, 2 patterns / 4 instances logged
- First report: io/analysis/halprin_mini/harness_report_20260502_first.md
- Second report (post-IGNORECASE fix): harness_report_20260502_v2.md
- Third report (post-restraint-watch): harness_report_20260502_v3.md

---

## TODAY IN ONE PARAGRAPH

Today shipped two big things. Morning: validate_ops V2.2 fix bundle (NAMES_LOCK exemption + overlap resolution + silent-failure logging + Writer Rule 8). Warren Seal lands clean. Afternoon: built the validation harness ("MB calibration thermos") from scratch — 5 modules, 38 tests, INDUSTRIAL grade — and ran first calibration on Halprin first 50 pages. Honest baseline: 52.4% confidence. Two candidate rules surfaced from over-reaches (WT_OFFSHORE short-form, EM_DASH editorial restraint) and logged in append-only restraint watch. The thermos works. We have a real number we can trust and a paranoid system to catch the engine when it makes changes MB chose not to make.

---

## EVENING SESSION TARGET (Scott's call)

**Move A: NAMES_LOCK substring matching + WT_OFFSHORE contextual short-form spec.**

Rationale: 6 W&T misses are the biggest single block of confidence loss. Today's NAMES_LOCK exemption is exact-match only — Writer wraps entities in phrases ("for W&T Offshore", "W&T Offshore."). Substring-with-word-boundary recovers all 6.

WT_OFFSHORE short-form is the sibling problem: NAMES_LOCK has "W&T Offshore" so the engine over-expands. MB sometimes uses the short form "W&T" alone. Need a contextual rule for which form to apply.

Both fixes together should:
- Recover 6 MISS → WIN (W&T substring fix)
- Convert 2 OVER-REACH → correct restraint (short-form rule)
- Push confidence from 52.4% toward 75–80% range

Estimated: 30–45 min spec by Opus, 45–60 min Sonnet build, then re-run + re-measure.

---

## CONFIDENCE TRAJECTORY

| Stage | Number | Source |
|---|---|---|
| Yesterday baseline (pre-V2.2) | ~30% | Hand-built defect inventory |
| V2.2 baseline (today AM) | unmeasured | Engine work only |
| Harness measurement (today PM) | **52.4%** | First real number |
| After NAMES_LOCK substring + short-form (evening A) | projected 75–80% | Spec exists, not built |
| After full Halprin run | unknown | Surfaces tier 2 defects |

---

## CRITICAL DESIGN DECISIONS LOCKED TODAY

1. Harness is **MB-calibration thermos**, not depo-agnostic. Every depo has a matching MB FINAL until graduation (depo 7).
2. Pattern catalog approach (Option 1) — depo-specific patterns, depo-agnostic mechanics.
3. 5-bucket lens: WIN / MISS / OVER-REACH / STYLE GAP / SCOPE DECISION.
4. **No GREEN/YELLOW/RED thresholds yet.** Set after 2–3 reports. Don't anchor MB on a number we made up.
5. Editorial Restraint Watch is **first-class measurement** — paranoid mode, append-only log, never delete entries.
6. Trend analyzer deferred until 3+ depos in the watch log.
7. Harness lives in `mrx_engine_v1` repo (versions with engine code).

---

## PARKING LOT (today's adds — full list)

1. NAMES_LOCK substring matching — **MOVE A target for evening**
2. WT_OFFSHORE contextual short-form rule — **MOVE A target for evening**
3. EM_DASH editorial restraint — possible Whisper ROI candidate (review after depo 2)
4. Tier handoff (Scott's simpler proposal) — last 2 sessions in CURRENT.md, older to monthly archive
5. Checkpointing / cheap-iteration architecture — Stage 3.1 outputs immutable + content-hashed
6. "Brandl FINAL" labeling error — file is raw CAT export, rename
7. Mini-MB / per-CR style profile architecture
8. Whisper / audio integration (text-only ceiling now measurable)
9. Trend analyzer for restraint log (defer until 3+ depos)
10. Anthropic Claude sandbox / shared-filesystem multi-agent pattern

---

## WATCH ITEMS (paranoid mode active)

These are NOT bugs. NOT yet. They are patterns we are watching across depos. Be paranoid. Hunt for them every report.

| Pattern | First seen | Hypothesis |
|---|---|---|
| WT_OFFSHORE over-expansion | 2026-05-02 | Engine defaults to NAMES_LOCK full form; MB context-switches to short |
| EM_DASH word-stutter over-correction | 2026-05-02 | Possibly audio-dependent (witness self-correction vs raw stutter) |

If either pattern reappears in depo 2, escalate. If they disappear, the V2.2 fixes were correct and we just need more data. After 3 depos, the trend analyzer gets built.

---

## SCOTT'S WORKING STYLE (DO NOT VIOLATE)

- 12-year-old reading level until told otherwise
- Plain English, short answers, ONE question at a time
- Inline A/B/C only when there's a real choice
- Hates fire-hose responses
- Sonnet writes files; Scott commits
- ALWAYS full absolute paths
- **NEVER GO SILENT.** Today's afternoon Opus stalled twice (10-min ping showed nothing written, 30-min check found no progress). The fix: write LIVE in chat, don't perform "thoughtful architect" — be one. If you catch yourself stalling, admit it, write in the next message.
- **NEVER make Scott copy-paste content** — Sonnet writes to repo, pushes, replies with raw URL.
- **Reverse-engineer rules from MB FINALs before asking MB.**

---

## SCOTT'S MOOD AT TAP-OUT

Strong. Sharp. He pushed back on a wishy-washy "test harness" framing this afternoon and forced clarity ("the thermos doesn't care what's inside"). That reframe was the unlock for the whole afternoon. He took an unplanned 30-min break around the time afternoon Opus stalled — came back productive, didn't lose his shit despite valid reasons to. He's been on point 7+ hours. Evening session is doable but is the second wind, not the first.

Tone for evening: calm, direct, no reset. He'll know what to do — your job is to spec well and not waste his energy on stalling or fluff.

---

## CODER MINDSET REMINDERS

Before any code change: **"Could this change reduce transcript accuracy or credibility?"** If yes or maybe → STOP, flag.

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED.

For evening session specifically: **RULE-SPEC-BEFORE-BUILD.** Substring matching + short-form rule touches Writer prompt + validate_ops + possibly suggester. Multi-file. Spec required before any code.

Slow is smooth. Smooth is fast.

— End of Opus 2026-05-02 afternoon handoff —
