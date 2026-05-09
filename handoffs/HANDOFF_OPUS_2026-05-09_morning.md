# HANDOFF — Opus, morning of 2026-05-09
**For:** Fresh Opus
**From:** Opus 2026-05-08 evening (context running thin, clean wrap)

---

## STOP. Before responding to Scott, answer these in your head:

1. What deposition was the focus yesterday? **(Brandl 50pp, post-M1 ceiling work)**
2. What's the new strategic direction? **(fingerprint architecture — locked tonight after two outside reviews)**
3. What's the next concrete deliverable? **(v0 fingerprint YAML for MB, drafted with fresh heads)**

If you can't answer all three from this doc, RE-READ. Do not guess.

---

## What landed yesterday (the wins)

### 1. Stage 3 m1 patch — DONE and PUSHED
- Writer max_tokens 4096 → 8192. Commit d2ebe1e (mrx_engine_v1, pushed).
- 1,196 proposals total, $14.92 cost, is_partial:false.
- TD-001 logged in mrx-context/tech_debt.md (commit 8182ff4, pushed).
- Patch is tuition, not solution. Three Sealed Phases retrofit still owed.

### 2. Post-M1 Brandl ceiling: 49.5%
- Predicted 75-85%, came in at 49.5%. Honest miss.
- Why: Q-labels WERE the ceiling. Removing them exposed the harder residual.
- Triage of remaining 679 blocks:
  - 235 AUDIO_REQUIRED (34.6%) — Stage 4 needed
  - 220 STAGE_2_RULE (32.4%) — incremental
  - 116 STAGE_3_LLM (17.1%) — model work
  - 108 PER_CR_STYLE (15.9%) — fingerprint territory

### 3. Cross-depo pattern scan — completed across 6 raws
- MB depos: Brandl, Halprin, Easley
- AD depos: Wade, Fourman, Leon
- New MB depo received (042726/jp): RTF missing, has audio + steno package, filed but blocked. Scott has Cat4 — can export RTF himself when he's not exhausted.
- Confirmed MB-specific patterns: q_label_s2, objection_style, uhhuh, hyphenation, compound_solid, number_style_raw
- Confirmed universal: doubled_pure, speaker_in_body
- CRITICAL FINDING: zero `--` em-dashes in any raw. The em-dashes are Stage 3 LLM hallucinations. TD-001 second symptom.

### 4. Compound dict additions — pending implementation
- 2 confirmed missing: twothirds, threequarters
- 4 safe-by-analogy: onehalf, onethird, onequarter, oneandahalf
- Decision: add all 6 with prefix `universal:` not `mb-specific:`
- Sonnet had paused before implementing — verify status with him before resuming.

---

## The big strategic shift (locked yesterday evening)

Scott's instinct: "we're hitting a wall on the engine — let's pivot to understanding MB's mindset deeply before building more rules."

This produced the fingerprint architecture decision.

**Two outside reviews obtained:**
1. ChatGPT — saved as design/fingerprint_architecture_chatgpt_2026-05-08.md (renamed from copilot_)
2. Copilot — to be obtained (Scott reversed labels mid-session, only one outside opinion was actually captured)

**Architecture locked (consensus across reviews):**
- Six-layer fingerprint: Identity / Translation Artifacts / Structural Formatting / Lexical Preferences / Risk & Review / Drift
- Facts vs. Inferences separated structurally (observations.json + inferences.yaml)
- Negative fingerprints — what reporter NEVER does — as hallucination suppressors
- Protected zones (names, dates, exhibit refs, sworn figures) as untouchable
- JSON canonical, YAML for humans, Markdown for review only
- Profiles within reporter: Reporter → Jurisdiction → Profile → Context rules
- Confidence per trait, sample size per trait, last_seen date

**Compound dict question:** Option A locked — fingerprint is source of truth, Stage 2 reads from fingerprint at runtime. Migration is later work.

**Scott has LA state and NY-WCB jurisdiction files already on disk somewhere — not yet integrated into the architecture.** Worth a Sonnet hunt.

---

## What's queued for today

### Step 1 — v0 fingerprint YAML for MB (Opus drafts)
Three layers only:
1. Identity
2. Translation Artifacts (observations from yesterday's scan)
3. Negative fingerprint / Protected zones

Defer layers 4-6 until more data justifies them.

Build the slots, leave them empty, fill as evidence accumulates.

### Step 2 — Compound dict implementation (if not done yesterday)
Confirm with Sonnet whether the 6 additions were committed before he wrote the handoff. If not, finish that first as the simple closeout.

### Step 3 — Locate jurisdiction files
Scott has Louisiana state + NY style files somewhere. Sonnet hunt mission.

### Step 4 — Stage 5 verification
Yesterday's Stage 5 run had 778 proposals "skipped during rendering" (tokenization_mismatch / span conflict). Doesn't affect the ceiling number but is debt. Investigate when ceiling work is parked.

---

## Hard rules (DO NOT VIOLATE)

- Plain English, 12-year-old reading level
- One question at a time
- All Sonnet-bound instructions go in code blocks (the copy-button window) — Scott's locked formatting standard from yesterday
- No fire hose. High level first. Detail on request.
- Sonnet runs shell. Scott runs decisions. Opus writes specs.
- Scott pushes commits. Sonnet commits but does not push.
- Halprin/Brandl FINAL files NEVER push to public repo.
- No tees, no extra logging. If you find yourself adding "just to be safe" steps, STOP.

---

## Open uncertainties

1. **Em-dash hallucination at Stage 3** is now a confirmed second symptom of TD-001. The doubled_word em-dash Stage 2 rule was killed because Stage 2 never sees `--`. Real fix: constrain writer to not inject `--`, or post-process to strip them. Not yet specced.

2. **042726 depo (jp witness, MB)** is filed but blocked on RTF export. Scott has Cat4 and can do this himself; he indicated Cat files are "traumatic" when tired. Don't push until he raises it fresh.

3. **MB still offline until 2026-05-13.** M1 unverified against a real Brandl example from her. Risk accepted by Scott.

4. **The 042726 sgxml shows it's a "Draft Printed / In Progress" status.** MB was still editing when she sent it. The RTF, when exported, may not be a true "rough" — could already have some edits applied. Worth flagging when we run pattern scan on it.

---

## Scott's state at end of yesterday

- Tired but smiling.
- "Slow is smooth, smooth is fast."
- Quoted Alan Turing breaking Enigma — daily key changes, 28 months. Our raw doesn't change, MB's final doesn't change. Finite problem.
- "In for a dime, in for a dollar" — diamond-for-a-dollar mentality on data quality.
- Rejected the "just keep building rules" approach. Wants understanding before building.
- Approved Option A on compound dict (fingerprint is source of truth).
- Three of his four Stage 2 cheap targets got cut by diagnostic data — only hyphenation+objection_style+compound_dict remain, and only compound_dict is implementation-ready.

---

## First thing fresh Opus should do

1. Read this doc top to bottom.
2. Read HANDOFF_SONNET_2026-05-09_morning.md.
3. Read mrx-context/design/fingerprint_architecture_chatgpt_2026-05-08.md (the saved external review).
4. Confirm to Scott: "Opus ramped. Ready." + one sentence on current state + one question.
5. Most important question: **"Compound dict additions first, or jump straight to v0 fingerprint draft?"**

Do not start work until Scott answers.

---

End of Opus handoff.
