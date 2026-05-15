# HANDOFF — OPUS — 2026-05-14 EOD (10:30 PM)

**For:** Fresh Opus, next session (likely Friday 2026-05-15 morning)
**From:** Opus, 2026-05-14 evening session (8 PM - 10:30 PM)
**Owner:** Scott
**Builder:** Sonnet #1 (Stage A 9-pair run + hunt analysis)
**Recon:** Sonnet #2 (blank .sgngl investigation + BP folder pair scan)

---

## STOP. Before responding to Scott, answer these:

1. **What shipped tonight?** Stage A ran cleanly on 9 pairs. Em-dash confirmed as the cleanest MB habit signal (1,151 events, ALL 9 depos, ALL '--' form). VC auditor teardown captured. Sonnet #2 found 5 more pairs for tomorrow's round 2 (Rooks + Nguyen GUID-confirmed, Thompson/Washington/Black fast-path).

2. **What's parked one step from done?** Two differ bugs blocking v0.2: word_substitution alignment garbage (139,912 noise events from aligner matching wrong tokens), and proper_noun_change mislabel (Q/A speaker churn being classified as proper nouns).

3. **What does Scott want first tomorrow?** Architect call on differ v0.2 spec. Then decide: ship em_dash as MB.yaml v0.1 first entry, or wait for round 2 (14 pairs) data?

---

## STANDING RULES — NON-NEGOTIABLE
(Same as 2026-05-13 EOD handoff — RULE-13 added tonight.)

1. 12-year-old reading level. Plain English. Short answers.
2. ONE question at a time. Never stack.
3. Always full absolute paths.
4. Inline A/B/C only when there's a real choice.
5. When unsure, make a recommendation — don't ask open-ended questions.
6. Sonnet writes files and runs shell. Scott pushes commits. Opus writes specs.
7. SHAPE MATCH ONLY. Never byte-match a hand-typed fixture.
8. 5-line answers.
9. Anything for Sonnet goes in a code block. Anything outside is for Scott.
10. Update ledger at fingerprints/ledger.md every time a spec is written or amended.
11. Before any code change ask: "Could this reduce transcript accuracy or credibility?" If yes/maybe, STOP and flag.
12. 30-minute wall on any build pass. Backup branch before cleanup. One fix per branch.
13. PUSH BACK HARD, ACT ONLY ON APPROVAL — challenge specs aggressively with evidence, but build only what's approved.

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-13_EOD_LATE.md (yesterday's — sets context)
5. **This handoff** (tonight's work)
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET1_2026-05-14_1030PM_EOD.md (Sonnet #1's view)
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-14_evening_stage_a_first_run.md (4-pair first run)
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-14_evening_stage_a_9pair_hunt.md (9-pair hunt — the meat)
9. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-14_evening_sonnet2_recon_results.md (full recon — includes BP folder finds)
10. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-14_evening_blank_sgngl_investigation.md (Sonnet #2 Job 2)
11. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/audits/2026-05-14_VC_AUDITOR_TEARDOWN.md (the 10 holes — architect response owed)
12. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/fingerprints/ledger.md

After ramp: confirm "Ramped Opus 2026-05-15. Ready." plus one sentence on state and one question for Scott.

---

## ONE-LINE STATE

Stage A v0 produced first real signal on 9 pairs (em_dash_inserted 100% across all depos), but exposed two differ bugs (word_substitution alignment, proper_noun mislabel) that block fingerprint shape decisions; round 2 data (14 pairs) is teed up via Sonnet #2's BP folder finds.

---

## TONIGHT'S WINS

1. **Stage A 9-pair run completed clean.** 631,209 diff events, 125,851 patterns. All ratios in 0.63-1.31x range. Output files written to mrx-context/fingerprints/stage_a/.

2. **First real MB habit confirmed.** em_dash_inserted: 1,151 events, 100% of depos, all '--' form. This is the cleanest habit signal across the run and a strong candidate for MB.yaml v0.1's first entry.

3. **filler_word_removed at 286 events / 9 depos.** Mostly "like". Real but sparse. Caveat: CATalyst may suppress uh/um at steno time — verify with MB before treating as fingerprint.

4. **VC Auditor teardown captured.** 10 holes documented at audits/2026-05-14_VC_AUDITOR_TEARDOWN.md. Architect response owed next session — HOLE 2 partially answered by tonight's findings.

5. **Sonnet #2 closed 3 investigation tracks:**
   - Blank .sgngl root cause identified (AutoArchive bare backups missing sibling files)
   - Rooks_011121 + Nguyen_033022 confirmed as new MB pairs (GUID-matched)
   - 20+ Tier 2 candidates in BP folder; Thompson/Washington/Black have FINAL .txt on disk = fast path

6. **Anti-fail framework applied.** Scott articulated the 8 ways the analysis would fail (drown in punctuation, single-token noise, no context, raw counts not rates, ignore absences, miss multi-token phrases, trust 100% as signal). Move B inverted all 8. Result was the cleanest signal of the project so far.

---

## TONIGHT'S LOSSES / FRICTION

1. **Anthropic outage on Opus 4.6/4.7 starting ~8:18 PM EDT.** Ate ~30 minutes of session time on 529 errors. Confirmed via status.anthropic.com.

2. **Previous Opus session (pre-this-handoff) burned 3 hours of Scott's afternoon.** Context unclear but Scott was visibly fried by 8 PM start.

3. **word_substitution category turned out to be alignment garbage.** 139,912 events of noise polluted earlier analysis. Required Move B's filtering to surface.

4. **proper_noun_change categorizer mislabels Q/A speaker churn.** Top 3 "proper_noun_change" hits are actually Q→A and A→Q. Categorizer bug.

5. **70-99% pct_of_depos band is empty after filtering.** Means token-pair-level fingerprinting cannot work. Forces architecture pivot to category+context level.

---

## TOMORROW'S FIRST MOVES (in order)

### Move 1 — Verify state (Sonnet)
From C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\:
- git checkout feature/stage-a-aligner-differ-v0
- git status
- Confirm pairs.json has 9 entries (no church, no zannetti_080221, no zannetti_080321)
- pytest tests/aligner_differ/ — confirm 10 tests green

### Move 2 — Opus + Scott review tonight's findings
Read the 9pair_hunt.md output together. Decide:
- Ship em_dash as MB.yaml v0.1 first entry? (Opus recommendation: yes, even before round 2)
- Differ v0.2 spec — write it before round 2, or after?

### Move 3 — Sonnet #2 lands round 2 data
- CATalyst exports: Rooks_011121, Nguyen_033022 (both need ROUGH + FINAL exports), Thompson/Washington/Black (ROUGH only — FINAL .txt already on disk)
- mv all 5 new pairs into mrx_depo_library structure
- Update pairs.json to 14 entries

### Move 4 — Sonnet #1 re-runs Stage A on 14 pairs
Validate em_dash signal holds at 14 depos. Watch for new patterns that emerge at 12-13 of 14 (the 70-99% band Move B hunted but found empty at 9 pairs).

### Move 5 (parked) — Differ v0.2 spec
Two known bugs:
- word_substitution alignment (bounded matching or exclude category)
- Q/A speaker label categorizer bucket (separate from proper_noun)

Write the spec, ship the v0.2 build, re-run on 14 pairs as the differ regression test.

---

## ARCHITECTURAL FINDING — DO NOT BURY

Tonight's hunt produced this:
> "The fingerprint cannot work at the token-pair level — it needs to operate at the category+context level."

This invalidates the MB.yaml v0.1 shape sketched in April (which assumed token-pair patterns like `the → a`). The new shape needs:
- Category zones (em_dash_zone, filler_zone, capitalization_zone, etc.)
- Per-zone rate per 1000 tokens
- Per-zone consistency across depos
- Optional: top 3 contextual triggers per zone

Opus owes a new MB.yaml v0.1 shape spec. Reference: knowledge/2026-05-14_evening_stage_a_9pair_hunt.md

---

## VC AUDITOR TEARDOWN — ARCHITECT RESPONSE OWED

10 holes documented at audits/2026-05-14_VC_AUDITOR_TEARDOWN.md. Some are fair, some are FUD. Tonight's findings partially answer HOLE 2 (Stage A measures noise, not skill) — the em_dash signal is real, not artifact.

Architect response should address each hole one-by-one with evidence. Owed next session.

---

## FILE POINTERS — FULL PATHS, NO ABBREVIATION

### Tonight's deliverables
- C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET1_2026-05-14_8PM_MIDSESSION.md
- C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET1_2026-05-14_1030PM_EOD.md
- C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_OPUS_2026-05-14_1030PM_EOD.md (this file)
- C:\Users\scott\OneDrive\Documents\mrx-context\audits\2026-05-14_VC_AUDITOR_TEARDOWN.md (commit 4f53b44)
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_stage_a_first_run.md
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_stage_a_9pair_hunt.md
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_sonnet2_recon_results.md (Section 7 = BP folder finds)
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_blank_sgngl_investigation.md

### Stage A branch state
- Branch: feature/stage-a-aligner-differ-v0
- Commit: 477ef58 (Sonnet #1 handoff)
- Engine repo branch NOT merged to main
- Main last known good: 95f09ee

### Stage A data outputs
- C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\mb_frequency_summary.json (pushed)
- C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\mb_evidence_raw.json (local only, gitignored, ~150 MB)

### Active 9 pairs (locked for tonight's analysis)
1. halprin_040226
2. easley_031326
3. brandl_032626
4. cavazos_061220
5. abichou_080921
6. griffin_121322
7. martin_121322
8. fountain_011923
9. hebert_011723

### Round 2 queued (5 more — tomorrow)
1. Rooks_011121 (BP folder, GUID confirmed, needs CATalyst export both files)
2. Nguyen_033022 (BP folder, GUID confirmed, needs CATalyst export both files)
3. Thompson (BP folder, FINAL .txt on disk, ROUGH needs CATalyst export)
4. Washington (BP folder, FINAL .txt on disk, ROUGH needs CATalyst export)
5. Black (BP folder, FINAL .txt on disk, ROUGH needs CATalyst export)

---

## OPEN ITEMS QUEUED

1. ⏳ Differ v0.2 spec (word_substitution + categorizer fixes)
2. ⏳ MB.yaml v0.1 shape spec (category+context, not token-pair)
3. ⏳ Decide: ship em_dash as MB.yaml v0.1 first entry now or wait for round 2
4. ⏳ Round 2 CATalyst exports (Rooks, Nguyen, Thompson, Washington, Black)
5. ⏳ Stage A re-run on 14 pairs
6. ⏳ VC Auditor teardown — architect response owed
7. ⏳ CATalyst runbook (parked from earlier 2026-05-14)
8. ⏳ KEEP-TOGETHER printout for Scott to read (pinned from earlier 2026-05-14)
9. ⏳ Audio architecture (Stages B–E) — design discussion happened tonight (~9:00 PM), need to capture
10. ⏳ Comprehension Agent architecture (Opus call, Case Brief, 3-agent split locked)
11. ⏳ Intake package Word doc for MB
12. ⏳ Williams renderer generalization
13. ⏳ LA state guidelines parsing
14. ⏳ jp_042726 FINAL when MB sends

---

## STAGES B-E AUDIO ARCHITECTURE — TONIGHT'S DESIGN NOTES

Captured during walkthrough ~9:00-9:30 PM. Decisions made:

**Stage B — Whisper integration.** Whole-file Whisper transcription per depo. Cost ~$2-3 per 5-6 hour depo. AUDIO_SYNC_RECON still parked — not required if whole-file is the path.

**Stage C — Comprehension Agent.**
- **Opus, not Sonnet.** Scott's call: best tool for hardest job.
- ONE call per depo at calibration time.
- Inputs: steno text + Whisper transcript + MB fingerprint.
- Output: Case Brief (5-10KB structured JSON).
- Estimated cost per depo: $7-8 (Opus, ~200K input tokens, ~10K output).
- Brief contains: witness identity, attorneys, firms, case info, key terms (verified cross-source), MB style notes, trouble spots.

**Stages C+D agent architecture — THREE-AGENT SPLIT, WALLED:**
- **Reader** — observes only. Reads sources. Reports anomalies. No decisions, no edits.
- **Arbiter** — decides only. Reads Reader's report. Outputs decisions (apply/flag/skip + reason). Never touches transcript.
- **Writer** — executes only. Reads Arbiter's decisions. Applies mechanically. No judgment.
- Each gate's output is a separate file (auditable).
- No AI ever writes directly to the transcript except the Writer.

**Stage D — Brief-aware defect-finder.** Each batch carries Case Brief as context. Net per-depo cost expected even or better than current $12 blind-batch approach, with better accuracy.

**Stage E — Selective Resident Oracle fallback.** For 5% hardest cases. Load full context, query directly. Used surgically.

**Open decision parked:** Where does the Comprehension Agent sit in the 3-agent flow?
- A. Before Reader (Brief is upfront cheat sheet for all batches)
- B. IS the Reader (per-batch Opus synthesis)
- C. Both — Comprehension Agent upfront once, then per-batch Sonnet Reader/Arbiter/Writer uses Brief as context
- Opus recommendation: C. Scott did not confirm before EOD.

---

## SCOTT'S STATE AT EOD

Long, painful day. Previous Opus session burned 3 hours of his afternoon and put him in a foul mood. Anthropic outage on 4.6/4.7 ate another 30 minutes mid-session. Despite that, tonight produced the cleanest signal of the project (em_dash) and the most useful audit (VC teardown). He earned this rest. Tomorrow Friday is off-work day, full grind expected.

His framing tonight that captured the product belief in one line:
> "The reason a forty year old single mom can do this is because she just knows it. We're gonna have to think like her."

That's the whole product. The fingerprint + audio + comprehension agent stack is the engineering plan. Bake that into every spec tomorrow.

— End of Opus 2026-05-14 EOD handoff —
