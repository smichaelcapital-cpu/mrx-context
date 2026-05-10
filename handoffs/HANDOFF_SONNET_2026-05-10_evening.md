# HANDOFF — SONNET — 2026-05-10 EVENING (fresh session)

**For:** Fresh Sonnet, Sunday evening session (~8 PM EDT or whenever Scott kicks off)
**From:** Opus (this afternoon's session, tapping out at ~3:45 PM)
**Owner:** Scott
**Paired with:** HANDOFF_OPUS_2026-05-10_afternoon.md (read that first — it has the strategic picture)

---

## RAMP — READ IN ORDER

Do NOT skip. Today's session changed the project meaningfully. Skipping these means building the wrong thing.

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/FUTURE_STATE_AGENT_AGENCY.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/FINGERPRINT_DATA_ARCHITECTURE.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-10_afternoon.md (fresh Opus is reading this same handoff — you're working from the same map)
9. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-10_overnight.md (the recon-run Sonnet's tap-out report — that was your previous instance who ran the recon)
10. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-11/overnight_recon_summary.md
11. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-11/lexical_layer_verdict.md
12. C:\mrx_training_set\MB\paired\SPLIT_MANIFEST.md
13. C:\mrx_training_set\MB\fingerprint\manifest.yaml (the actual fingerprint output)
14. This handoff in full

After reading: confirm in ONE LINE: "Ramped Sonnet evening 2026-05-10. Ready." plus one sentence on current state.

Then WAIT for fresh Opus to direct first task. Do not start coding unprompted.

---

## ONE-LINE STATE OF THE WORLD

Engine repo unchanged (HEAD 8954b61, 864 tests passing). mrx-context at commit 87c9332 with everything from today pushed. 19 AUTO patterns produced from 195-pair training run; lexical layer found NOT_READY (per-case rather than per-CR); cap_objection_midturn flipped from 87% (7-pair) to 9% (195-pair); one yellow flag on punctuation post-run confidence recalculation needs investigation before we trust those AUTO labels.

---

## REPO STATE

### mrx_engine_v1
- Branch: main, clean
- HEAD: 8954b61 (Gate 4 — wire optional fingerprint into assemble_final)
- Tests: 864 passing, TD-002 still the only failure
- Pushed: yes
- **No engine code changes today.** Today was data work only.

### mrx-context
- Branch: main, clean
- HEAD: 87c9332
- Pushed: yes
- Three commits today: e4c706a (4 knowledge files + handoff + 2 reports), 51c47d6 (overnight recon spec), 87c9332 (overnight results + Sonnet handoff)

### C:\mrx_training_set\MB\ (LOCAL ONLY, NEVER PUSHED)
- `paired\TRAINING_SET.md` — 195 pairs
- `paired\TEST_SET.md` — 48 pairs, SACRED, never measure against
- `paired\SPLIT_MANIFEST.md` — split methodology
- `fingerprint\manifest.yaml` — top-level fingerprint manifest
- `fingerprint\patterns\*.yaml` — 28 individual pattern files
- `fingerprint\events\*.matching.jsonl` and `*.nonmatching.jsonl` — raw event records
- `fingerprint\confidence_history\*.history.jsonl` — append-only confidence change logs
- `extracted\` — plain-text extractions of all training pairs
- `_provenance\recon_runs.jsonl` + `script_versions\` — subpoena-defense ledger
- `reports\` — full local recon reports

---

## STANDING RULES — NON-NEGOTIABLE

Same as always but worth re-reading because they get tested every session:

1. **12-year-old reading level for Scott.** Plain English. Short answers.
2. **ONE question at a time. Never stack.**
3. **Always full absolute paths.** Never abbreviate.
4. **Code-fenced blocks for any content Scott copies to Opus or to a future you.**
5. **Halprin, Brandl, and all 7 paired MB depo FINAL files NEVER push to public repo.**
6. **Anything in C:\mrx_training_set\ NEVER pushes to public repo.** This is hard — entire training set, all patterns with depo content, all events, all extractions, all local reports. Never. Sanitized metrics-only summaries CAN push to `mrx-context/reports/<YYYY-MM-DD>/` after grep verification against MANIFEST deny-list.
7. **Scott pushes commits.** Standing rule. The one-day push exception from today's session has expired. Push authority returns to Scott as of Monday morning (i.e., right now).
8. **DON'T MAKE SCOTT A CLIPBOARD.** If content is in chat, on disk, or in the repo, read it directly. Don't ask him to re-paste.
9. **Don't fire-hose.** If you're about to write a wall of text, ask: "is this for Scott to read or for an AI to consume?" If for an AI, the short version is enough — the AI pulls from disk.
10. **Plain text URLs.** When pasting URLs in chat, plain text only. Terminal auto-hyperlinking has broken URL fetches before.
11. **Handoff files live in mrx-context/handoffs/. Knowledge captures live in mrx-context/knowledge/. Never in Downloads.**
12. **Slow is smooth. Smooth is fast.**

Before any code change: "Could this reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag to Scott.

Three Brains check: Engineer (can?), Architect (should?), Owner (worth?).

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED. RULE-SPEC-BEFORE-BUILD.

---

## WHAT TODAY ACCOMPLISHED (SHORT VERSION)

Yesterday: 7 paired MB depos, four markdown reports, one mid-confidence pattern, no train/test discipline.

Today:
- 340 paired depos discovered (333 new)
- 243-pair calibration corpus locked (last 5 years, 2022-2026)
- 195/48 train/test split locked
- 4 knowledge files capturing strategic vision
- Fingerprint data architecture document
- Overnight recon ran clean — 19 AUTO patterns produced and stored per the new schema
- One major credibility save (cap_objection_midturn lesson)
- One major architectural finding (lexical is per-case, not per-CR)

Most strategically productive day of the project to date.

---

## THE FINGERPRINT THAT EXISTS RIGHT NOW

You have a real fingerprint on disk at `C:\mrx_training_set\MB\fingerprint\`. 28 patterns total. 19 hit AUTO (≥0.90 confidence). Distribution by layer:

- **Splits:** 5 AUTO (known patterns confirmed) + 5 AUTO + 2 SUGGEST (discovered)
- **Capitalization:** 1 AUTO (`cap_sentence_start` at 98.77%) + 1 FLAG (`cap_objection_midturn` at 9%)
- **Punctuation:** 14 patterns, mix of AUTO and SUGGEST. **YELLOW FLAG — 6 were recalculated from FLAG to AUTO post-run; methodology unverified.**
- **Lexical:** 0 patterns produced (layer NOT_READY at 195 pairs)

The fingerprint is structured per `knowledge/FINGERPRINT_DATA_ARCHITECTURE.md`. Read that doc before doing anything that touches the fingerprint structure.

---

## LIKELY TASKS THIS EVENING

Fresh Opus will direct. These are educated guesses about what gets prioritized — read them so you're not surprised, but DON'T start them unprompted.

### Most likely task 1: Investigate the punctuation recalculation (yellow flag)

The overnight Sonnet output noted: "6 FLAG patterns that were later corrected to AUTO via post-run confidence recalculation — the YAML files on disk reflect the corrected values."

Fresh Opus wants to understand the recalc methodology. Was it defensible (e.g., excluding alignment-failed pairs from the denominator)? Or was it numbers-massaging?

You'd:
1. Find the recalculation script (likely in `C:\Users\scott\AppData\Local\Temp\` from overnight)
2. Read the logic
3. Identify the 6 affected patterns by name
4. For each: compare the original calculation vs the recalculated one, document the basis
5. Recommend keep-AUTO or revert-to-FLAG per pattern
6. Write findings to `C:\mrx_training_set\MB\reports\2026-05-10_evening_punct_recalc_audit.md` (local-only) and a sanitized version to `mrx-context/reports/2026-05-10/punct_recalc_audit.md` (push-safe)

~45-60 min of work. Bounded, single deliverable.

### Most likely task 2: Spot-check the cap_objection_midturn flip

Yesterday at 7 pairs: 87% (looked like a HIGH-confidence pattern). Today at 195 pairs: 9% (FLAG). Big flip. Worth verifying it's real (not a script bug or definitional difference).

You'd:
1. Manually inspect 20 randomly-sampled mid-turn "Objection" events from the training pairs
2. For each: rough text snippet + final text snippet + verdict (capped in final / not capped in final / edge case)
3. Compute manual rate, compare to script's 9%
4. If within ±5%, the flip is real
5. If wildly different, flag a script bug
6. Write findings to local + sanitized public summary

~30-45 min.

### Most likely task 3: Spec evaluation against the 48-pair test set

This is the maturation curve. We need this number for May 13.

The fingerprint is built. The test set is sacred. The eval runner needs to:
1. Load the test set with `MRX_EVAL_MODE=1` env var
2. For each test pair: load rough, score against fingerprint, produce candidate "engine output"
3. Diff candidate vs actual final
4. Categorize diffs (ENGINE_MATCH / ENGINE_MISS / ENGINE_OVERREACH / STYLE_GAP)
5. Score per pair and overall

Per `FINGERPRINT_DATA_ARCHITECTURE.md` Section 2.6, this is the eval runner contract.

**This is bigger than 30-45 min.** Possibly a multi-hour build. Fresh Opus will scope it; might be tonight's main work, might be split into spec-only tonight + build Monday.

### Possible task 4: Per-case lexical architecture conversation

Lexical NOT_READY at 195 per-CR pairs means the layer is case-specific. Fresh Opus may want to spec a per-case lexical pass.

This is a conversation more than a build. Fresh Opus drives the architecture. You contribute the technical perspective on integration with the existing recon scripts.

### Possible task 5: Update knowledge files with today's lessons

Two updates likely:
1. `FINGERPRINT_FACTORY_REQUIREMENTS.md` — add R11 (pre-recon rough quality check) and R12 (recon-time alignment robustness) and R13 (per-case lexical). Yesterday I identified R11/R12 but didn't add them. Today's lexical finding adds R13.
2. `knowledge/SMALL_SAMPLES_LIE.md` (new file) — capture the cap_objection_midturn lesson as a permanent project lesson. Bake into onboarding playbook: never publish a CR pattern claim based on under-100 pair samples.

Fresh Opus drafts text, you save and stage.

---

## OPEN ITEMS / TECH DEBT (current state, for ramp awareness)

- **TD-001:** writer JSON truncation, patched not solved
- **TD-002:** stale W&T e2e test (miss ≥4 expected, engine finds all 9) — quick fix
- **TD-003:** hardcoded MB paths in spot-check scripts at C:\Users\scott\AppData\Local\Temp\spot_check_v3.py (acknowledged, acceptable for temp use, but production recon layer needs parameterization)
- **TD-004 (NEW):** punctuation post-run confidence recalculation methodology undocumented — to be investigated this evening
- **Garbled-filter regex bug** from 2026-05-09 — may have been inherited by overnight scripts, worth verifying
- **ROUGH binary extraction methodology gap** — partially worked around, needs proper fix
- **R11/R12/R13 not yet baked into FINGERPRINT_FACTORY_REQUIREMENTS.md** — needed before next CR onboarding
- **16 ambiguous cases from inventory** not yet classified
- **M:N complex word replacements** not yet measured
- **Pre-existing engine modification** on reports/2026-05-08/steno_ceiling_triage_clean95.md held overnight, was supposed to be triaged today, deferred again
- **Stray file in handoffs** — overnight Sonnet mentioned but didn't identify it. Check `mrx-context/handoffs/` for an unexpected file before pushing anything.
- **2017-2020 archive gap** — 2018, 2019, 2020 nearly empty in MB's archive. Could be real or could be script-pairing failure. Sonnet bounded task for later this week.
- **1,531 rough-only files** in the inventory — could be unfinalized work, hidden finals, or never-finalized cases. Worth a future sample.

---

## CRITICAL CONFIDENTIALITY REMINDER

Today's overnight run produced ~hundreds of MB of local-only fingerprint data. This is the most sensitive data we've ever staged. The boundary:

- **NEVER push:** anything from `C:\mrx_training_set\`, witness names, case IDs, depo content, folder paths under `C:\Cat4\usr\scott`, the full inventory reports, the train/test split files, the raw event files
- **CAN push (after grep verification against MANIFEST.md):** metrics-only summaries, pattern counts, layer-level verdicts, confidence distributions

When in doubt: don't push. Ask Scott. Local-first.

---

## WHAT NOT TO TOUCH

- **Test set (TEST_SET.md and the 48 listed pairs).** Sacred. Three layers of enforcement. Recon scripts should refuse to load it. Eval scripts only load it with `MRX_EVAL_MODE=1` env var.
- **Existing fingerprint YAMLs** — don't edit them without Opus direction. They're the output of the overnight run. If a methodology question arises (like the punctuation recalc audit), write findings to a NEW file, don't mutate the originals.
- **Engine repo** — no engine changes today are expected, and no engine changes tonight unless Opus specifically directs.

---

## SCOTT'S WORKING STYLE (REMINDERS)

These are critical and they get tested every session:

- **12-year-old reading level** until told otherwise
- **ONE question at a time. Never stack questions.**
- **Inline A/B/C only when there's a real choice.** Otherwise just answer.
- **Code-fenced blocks** for ANY content Scott copies to Opus or to another Sonnet
- **Always full absolute paths.** No abbreviating.
- **Same-day handoffs:** paste content in chat AND push to repo. Not one or the other.
- **DO NOT make Scott a clipboard.** Read content directly via tool. Never ask him to re-paste content already in chat or on disk.
- **Don't fire-hose with walls of text.** If a long block of text would benefit you-the-AI but Scott just needs to know it's done, send the short version.
- **Plain text URLs** in chat.
- **Slow is smooth. Smooth is fast.**

If Scott pushes back, listen. If you've messed up, own it cleanly, don't grovel, fix it, move on.

---

## SESSION HEALTH AT HANDOFF

**Opus (this afternoon's session, the writer of this handoff):**
~6 hours on. Three failure modes called and corrected mid-session (wall-of-text Sonnet block, racing ahead on the data architecture draft, confusing Sonnet-tapped-out with Sonnet-can-do-one-more-push). Tapping out clean. Strategic articulation work + data architecture are the cleanest artifacts.

**Previous Sonnet (the one who tapped out earlier today):**
Wrote his handoff + addendum cleanly. Tapped out at ~12:50 PM.

**Overnight Sonnet (the one who ran the recon):**
Ran 6 phases in ~75 minutes, faster than estimated. Reported back clearly. One yellow flag on his work: post-run confidence recalculation on punctuation patterns needs methodology verification (TD-004).

**Scott:**
Productive day. Sharp morning, sharp midday, taking a break this afternoon. Strategic articulation was the win of the day — most of today's knowledge files contain Scott's own language captured by Opus. Be careful with him this evening: long day, fatigue likely. Slow is smooth.

**You (fresh Sonnet about to ramp):**
Clean context. No baggage from earlier sessions. Read the four knowledge files first — they reframe the project. Then wait for Opus direction.

---

## ONE THING TO HOLD COLD

The fingerprint we built today is not "MB's fingerprint." It's the first run of the fingerprint factory. Every architectural decision tonight passes the test:

> Does this work for CR #1 (MB) AND for CR #2-10 (Golden Circle) without rewrites?

If the answer is no, push back. CR-agnostic from byte one. No MB-specific hardcoding. R1 of `FINGERPRINT_FACTORY_REQUIREMENTS.md`.

---

— End of Sonnet evening handoff 2026-05-10 —
