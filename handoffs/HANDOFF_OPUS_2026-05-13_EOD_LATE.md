# HANDOFF — OPUS — 2026-05-13 EOD (LATE NIGHT)

**For:** Fresh Opus, 2026-05-14 session
**From:** Opus (2026-05-13 evening session, Scott calling it ~10:30 PM EDT)
**Owner:** Scott
**Builder:** Sonnet #1 (Stage A build), Sonnet #2 (recon — done for the cycle)
**Sonnet #1 EOD:** C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET_2026-05-13_EOD_v2.md

---

## STOP. Before responding to Scott, answer these:

1. **What shipped today?** Front page appearances fix — Pass 1 (KEEP-TOGETHER) and Pass 2 (Reported by anchor to line 19). Both merged to main. 473 tests green. Halprin renders end-to-end with no orphans.
2. **What's parked one step from done?** Stage A (Aligner+Differ) — 6 modules built, 7 unit tests green, integration test proved the pipeline works on Halprin (47,089 diff events) but full-doc diff-match-patch took 13 min. Two small fixes queued for tomorrow.
3. **What does Scott want first tomorrow?** Finish Stage A. Two fixes. Run on 4 pairs. Get the first frequency table. Then look at the data together and decide what counts as habitual MB.

If you can't answer all three from this doc, RE-READ.

---

## STANDING RULES — NON-NEGOTIABLE

1. 12-year-old reading level. Plain English. Short answers.
2. ONE question at a time. Never stack.
3. Always full absolute paths.
4. Inline A/B/C only when there's a real choice.
5. When unsure, make a recommendation — don't ask open-ended questions.
6. Sonnet writes files and runs shell. Scott pushes commits. Opus writes specs.
7. SHAPE MATCH ONLY. Never byte-match a hand-typed fixture.
8. 5-line answers.
9. Anything for Sonnet goes in a code block. Anything outside is for Scott.
10. Update the ledger at fingerprints/ledger.md every time a spec is written or amended.
11. Before any code change ask: "Could this reduce transcript accuracy or credibility?" If yes/maybe, STOP and flag.
12. 30-minute wall on any build pass. Backup branch before any cleanup. One fix per branch.

---

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-13_EOD.md (yesterday's handoff — sets the context)
5. **This handoff** (everything from today)
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-13_STAGE_A_ALIGNER_DIFFER.md — THE STAGE A SPEC
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-13_EOD_v2.md — Sonnet's view
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-13_evening_depo_library_recon.md — the depo inventory
9. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-13_evening_catalyst_inventory_and_staging.md — full Cat4 inventory + staging
10. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/fingerprints/ledger.md

After ramp: confirm "Ramped Opus 2026-05-14. Ready." plus one sentence on state and one question for Scott.

---

## ONE-LINE STATE

Front page appearances 100% shipped (main is clean at 95f09ee, 473 tests green). Stage A code 95% built but uncommitted on feature branch — two tiny fixes (500-token chunking + U+2011 detection) and a full pipeline run on 4 pairs will produce the first MB frequency table tomorrow morning.

---

## TODAY'S WINS

1. **Front page fix SHIPPED.** Both passes merged to main. Issue 1 (KEEP-TOGETHER) and Issue 2 (Reported by line 19). Issue 3 (ALSO PRESENT line 13) auto-resolved by Pass 1, exactly as the spec predicted.
2. **Stage A philosophy locked with Scott.** Deterministic frequency-counting tool. NO AI in the diff loop. "If MB does it 97 out of 100 times, on depo #101 the engine should do it for her." Three tiers: 100% auto-apply / 90–99% auto-apply + log / 70–89% suggest / <70% don't act.
3. **Stage A spec written and on disk.** All 7 questions Scott had during walkthrough answered (line vs word, output format, batch size approach, deterministic vs AI, etc.).
4. **Stage A code 95% built.** 6 modules, 7 unit tests green. Pipeline proven to produce 47,089 diff events on Halprin (slow run, but the math works).
5. **Depo inventory CLARIFIED.** The "198" Scott remembered = ~136 .sgxml files in C:\Cat4\usr\scott\. From 2020-forward with confirmed FINAL match: ~18 pairs. Plus the 4 already-exported pairs = ~22 potentially accessible after CATalyst export work.
6. **Staging folder set up.** 20 .sgxml files copied to C:\Users\scott\OneDrive\Documents\mrx_depo_library\_staging_for_export_2026-05-13\ ready for Scott to manually export from Case CATalyst when he's ready.

---

## TODAY'S NEAR-MISSES (LESSONS BAKED IN)

1. **First KEEP-TOGETHER attempt was overly aggressive.** Counted full 2-row blank after every block; should be 0 when last content row leaves sub-row empty. Caught by failing tests. Rolled back. Re-shipped clean on second pass.
2. **Sonnet #1 silent-thought past 10-min ceiling on diff-match-patch run.** Standing rule held — Opus issued hard stop. Sonnet stopped on the third try (after some additional bash runs). Branch intact, no damage. **Rule worked.** First real test of the 30-min wall under pressure.
3. **Sonnet #2's first recon used over-strict matcher.** Missed obvious pairs (Aggrenox ROUGH + TSFINAL same folder). Scott caught it by eyeballing the CATalyst manager. Amendment 01 with revised rules ran clean — 23 → 136 RAWs, ~18 confirmed 2020+ pairs.

---

## TOMORROW'S FIRST MOVES (in order)

### Move 1 — Verify state (Sonnet)

From C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\:
- git checkout main
- git pull origin main (confirm at 95f09ee)
- pytest tests/stage5/ (confirm 473 pass, 1 pre-existing fail)
- git checkout feature/stage-a-aligner-differ-v0
- git status (should show 8 untracked files — the Stage A modules + tests)
- pytest tests/aligner_differ/ (confirm 7 unit tests green)

Report state.

### Move 2 — Fix #1 — 500-token chunking in align.py

The current align.py runs diff-match-patch on full normalized documents. On Halprin (~100k tokens RAW, ~133k FINAL) this takes 13 minutes — unacceptable.

Fix: chunk both token streams into 500-token windows BEFORE calling diff_main. Run diff_main on each pair of windows independently. Concatenate the per-chunk op streams back into one flat stream.

Tradeoff Scott accepted: ~1% of edits that span chunk boundaries will be missed or mis-attributed. For a frequency fingerprint, statistically irrelevant. Document the limitation.

One test: test_align_chunked_halprin — runs align on Halprin in under 60 seconds and produces >40,000 diff events (we know from yesterday's slow run it should be ~47,000).

### Move 3 — Fix #2 — U+2011 detection in categorize.py

RAW uses U+2011 (non-breaking hyphen pairs) where FINAL uses ASCII `--` or U+2014. The current em_dash_inserted / em_dash_removed detection misses these.

Fix: add U+2011 and U+2011+U+2011 to the em-dash token set. Two lines of code.

One test: test_categorize_em_dash_u2011 — insert of "\u2011\u2011" lands in em_dash_inserted bucket.

### Move 4 — Full pipeline run on 4 pairs

After both fixes green:
1. Run run_stage_a.py on all 4 pairs (Halprin, Easley, Brandl, Church).
2. Confirm two JSON files written to C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\
3. Report top 20 patterns + total diff event count.
4. NO COMMITS. Scott eyeballs first.

### Move 5 — Scott + Opus review

Look at the frequency table together. Identify:
- 100% patterns → candidates for MB.yaml
- 75% patterns (3 of 4 depos) → "tendency, needs more data"
- Surprises → flag for human review

Decide: commit Stage A v0? Promote any patterns into MB.yaml? Or run more depos through (via CATalyst export work) before declaring v0 done?

---

## FILE POINTERS — FULL PATHS, NO ABBREVIATION

### Today's deliverables
- C:\Users\scott\OneDrive\Documents\mrx-context\specs\2026-05-13_STAGE_A_ALIGNER_DIFFER.md — Stage A v0 spec (with Amendment 01 path corrections inline)
- C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET_2026-05-13_EOD_v2.md — Sonnet handoff
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-13_evening_depo_library_recon.md — first recon report
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-13_evening_catalyst_inventory_and_staging.md — amended recon + staging report
- C:\Users\scott\OneDrive\Documents\mrx_depo_library\_staging_for_export_2026-05-13\ — 20 .sgxml folders staged for manual CATalyst export

### Stage A branch (uncommitted)
Branch: feature/stage-a-aligner-differ-v0
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\__init__.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\normalize.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\tokenize.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\align.py (needs chunking fix)
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\diff.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\categorize.py (needs U+2011 fix)
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\frequency.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\run_stage_a.py
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\aligner_differ\test_aligner_differ.py

### Stage A inputs (the 4 pairs)
| # | Depo | RAW | FINAL |
|---|---|---|---|
| 1 | halprin_040226 | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\input\040226yellowrock-ROUGH_Tsmd.rtf | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\oracle\040226yellowrock-FINAL.txt |
| 2 | easley_031326 | C:\Cat4\usr\scott\031326yellowrock-ROUGH_T.rtf | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\easley_031326\oracle\Easley_YellowRock_FINAL_TRANSCRIPT.txt |
| 3 | brandl_032626 | C:\Users\scott\Downloads\depofiles\032626YELLOWROCK TO SCOTT\032626YELLOWROCK_smd_T.rtf | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\brandl_032626\oracle\BRANDL_MB_FINAL.txt |
| 4 | church_073124 | C:\Cat4\usr\scott\073124CHURCH-ROUGH.txt | C:\Cat4\usr\scott\073124church3-FINAL.txt |

### Engine state
- Main: 95f09ee (Pass 2 merge: Reported by anchor)
- All 8 front matter renderers present and tested
- 473 tests pass on main; 1 pre-existing fail (test_williams_byte_match — unchanged for weeks)

### Backup branches on origin (DO NOT DELETE)
- backup/pre-appearances-issue1-2026-05-13
- backup/pre-appearances-issue2-2026-05-13
- backup/pre-stage-a-2026-05-13 (if it was created — verify)

---

## DATA INVENTORY (updated tonight)

### Already-exported MB pairs (4)
| Depo | RAW format | FINAL format | Audio |
|---|---|---|---|
| Halprin (040226) | .rtf | .txt | .opus 79MB |
| Easley (031326) | .rtf | .txt | no |
| Brandl (032626) | .rtf | .txt | .opus 99MB |
| Church (073124) | .txt | .txt | no |

### CATalyst-native pairs awaiting export (from amended recon)
- ~18 confirmed pairs from 2020-forward in C:\Cat4\usr\scott\
- ~37 confirmed pairs all years (includes 2017–2019 like Aggrenox, Hornbeck, Taxotere)
- 20 already staged in C:\Users\scott\OneDrive\Documents\mrx_depo_library\_staging_for_export_2026-05-13\

### The 198 question — RESOLVED
The 198 number Scott remembered = approximately the total .sgxml count across all Cat4 subfolders. Today's inventory found 136 unique .sgxml files. Difference likely = year filter (Scott was thinking lifetime, today scanned 2020+ initially) and same-job-multiple-files (CATalyst stores .sgxml + .sgngl + .sgdct + .sgglb per job).

**Realistic pair ceiling: ~37 pairs all years, ~18 from 2020-forward — far from 198, but enough to make Stage A meaningful.**

---

## OPEN ITEMS QUEUED

1. ⏳ Stage A two fixes (chunking + U+2011) — fresh Sonnet morning
2. ⏳ Stage A full pipeline run on 4 pairs
3. ⏳ Frequency table review with Scott
4. ⏳ Decide: promote any patterns into MB.yaml v0.1? Or wait for more pairs?
5. ⏳ Manual CATalyst export of staged 20 .sgxml files (Scott's task, when ready — Garcia is the recommended first)
6. ⏳ Audio architecture (Stages B–E) walkthrough still owed to Scott — pushed from yesterday because front page work + Stage A took priority
7. ⏳ Intake package Word doc deliverable for MB (still owed from earlier this week)
8. ⏳ Williams renderer generalization
9. ⏳ LA state guidelines parsing (unlocks 6 ambiguous MB.yaml classifications)
10. ⏳ jp_042726 FINAL when MB sends it

---

## TWO-SONNET PARALLEL — LESSONS FROM TONIGHT

Tonight ran Sonnet #1 (build) and Sonnet #2 (recon) in parallel for several hours. Worked because:
- Lanes were CLEAN. Sonnet #1 stayed in mrx_engine_v1 codebase. Sonnet #2 stayed in mrx-context inventory + file system recon.
- No file collision risk — different repos, different concerns.
- Scott managed both, asking each one separately when context demanded.

What broke:
- Sonnet #1 hit the silent-thinking failure mode twice (SequenceMatcher choke, diff-match-patch choke). The 30-min wall held — required Opus to issue hard-stop both times.
- Context compaction on Sonnet #1's session lost the original Stage A spec text. Required re-paste.

Going forward: when a Sonnet session approaches compaction (~6-8 hours of activity), force a clean handoff and start fresh, even if mid-task.

---

## LEDGER PROPOSED ADDITIONS

(Did NOT add to ledger yet — fresh Opus should add tomorrow after Stage A v0 ships.)

| 16 | Appearances pagination block-cost math | Per-MB measured row costs from her FINAL output (6 pages, 22 firm blocks, KEEP-TOGETHER honored with sub-row separator rule) | Universal: paginator accepts per-CR block-cost table derived from that CR's FINAL output. Code reads the table, applies KEEP-TOGETHER, breaks pages accordingly. No CR-specific math in code. | MB.yaml gets a measured appearances.block_costs section once we generalize. CR #2 gets their own table after Aligner+Differ runs on their data. | 2026-05-13 | appearances overflow fix |

| 17 | Stage A frequency table (MB v0) | MB-specific: 4-depo frequency table at fingerprints/stage_a/mb_frequency_summary.json | Universal: tool runs on any CR's RAW+FINAL pairs and emits per-CR frequency table | Tool is universal-ready; output is per-CR. Confirm row when Stage A v0 first run completes. | 2026-05-13 | Stage A v0 spec |

| 18 | RAW transcript U+2011 vs ASCII em-dash | MB's CATalyst uses U+2011 non-breaking hyphen pairs in RAW; FINAL converts to either ASCII -- or U+2014 | Universal: aligner-differ categorize step must handle U+2011, U+2014, and ASCII -- as the em-dash family | Discovered during Stage A integration test 2026-05-13 evening | 2026-05-13 | Stage A integration test |

---

## SCOTT'S STATE AT EOD

Pushed hard tonight. Stayed disciplined when Sonnet drifted. Made the right call to stop instead of forcing tired fixes. Called it ~10:30 PM EDT. Wants tomorrow morning's first move to be finishing Stage A and getting the first frequency table.

His framing during tonight's design conversation captured the product belief in one sentence:
> "If MB does it 97 out of 100 times, on depo #101 the engine should do it for her."

That's the whole product. The fingerprint is a trend file. The engine is a trend matcher. Bake that into every Stage A decision tomorrow.

— End of Opus 2026-05-13 EOD (late night) handoff —
