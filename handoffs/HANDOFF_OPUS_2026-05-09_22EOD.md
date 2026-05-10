HANDOFF — OPUS — 2026-05-09 22:00 EOD (TRUE END OF NIGHT)
For: Fresh Opus, next session (tomorrow morning)
From: Opus (this evening's session — 6:05 PM start, 10:00 PM wrap, ~4 hour session)
Owner: Scott
Builder: Sonnet (today's full marathon — multiple instances, final fresh instance ran the four overnight recons)

This SUPERSEDES the earlier HANDOFF_OPUS_2026-05-09_EOD.md saved at ~8:15 PM. Read this one. The earlier one is incomplete — written before the four overnight recons.

RAMP — READ IN ORDER

https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/HANDOFF_SYNC_GAP.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/COPY_TO_SONNET_RULE.md
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-09_22EOD.md (commit c298eba)
This handoff in full

After reading: confirm in ONE LINE: "Ramped Opus 22EOD 2026-05-09. Ready."

ONE-LINE STATE
Pivoted hard tonight from "build _split_intra_turn_sentences()" to "calibrate MB's fingerprint with real data" — discovered MB has 7 paired raw+final depos on disk, staged a confidential training set at C:\mrx_training_set\, ran four overnight recons (splits, word substitutions, capitalization, punctuation), surfaced 14+ HIGH-confidence rule candidates, and identified a new architectural design principle: fingerprint layers calibrate at different rates (structural fast, lexical slow). Both repos clean, all four recon reports on disk, both EOD handoffs (this one + Sonnet's) ready to push.

TONIGHT IN ONE PARAGRAPH
Picked up evening Opus handoff at 6:05 PM. Set chain-of-command tone with Sonnet (he had offered Scott a menu in his ramp; corrected). Confirmed engine path. Was about to spec _split_intra_turn_sentences() when Scott raised the credibility risk: splitting wrong puts words on wrong line. Pivoted to a three-lane confidence-banded design (AUTO ≥90%, SUGGEST 60-89%, FLAG <60%, PROTECTED). Realized we needed actual frequency numbers from MB's body of work to set the bands. Initially planned 2-depo recon on Halprin+Brandl. Scott pushed back: he has access to MB's CAT directory with many more depos. Sent Sonnet to inventory C:\Cat4\usr\scott — found 113 folders, 38 case groups, 7 confirmed PAIRED cases (020123wunstell, 032025olsen, 040825olsen, 0525black_bp, 060122williams, 082222butler, 101322blanks). Staged training set at C:\mrx_training_set\MB\paired\. Sonnet ran first frequency recon. Then ran three-hedge audio architecture consultation (ChatGPT + Copilot + Opus synthesis), all saved to C:\mrx_training_set\_design_consultations\2026-05-09_audio_architecture\. Scott pressure-tested the synthesis and surfaced four critical pieces from engine v1's old architecture: (1) Reader/Decider/Writer separation, (2) audio is evidence-only never writer (one exception: blank-fill, always to MB review), (3) provenance ledger required for every change, (4) Montreal Forced Alignment for phoneme-level disputes. Resurrected Comprehension Agent / Case Brief design from May 3 archive. First EOD handoffs written at ~8:15 PM. Then Scott decided to keep grinding — fresh Sonnet ran systematic split discovery sweep (12,786 transitions, 5 NEW HIGH-confidence patterns, biggest find: bare "And" as Q opener at 671 occurrences, 9× the volume of "and then" + "and so" combined that earlier recon was tracking). Then word substitution census (985 substitutions, ZERO HIGH-confidence — lexical layer is case-specific). Then capitalization scan (11,546 events, dominant rule = capitalize first word of every sentence, plus "Objection" mid-turn cap). Then punctuation transformation census (7,134 events, 14 HIGH-confidence patterns including the elegant stage-direction rule: end punct always precedes parentheticals like ?( and .(). Wrapped at ~10:00 PM after Scott declined a fifth recon, recognizing diminishing returns. Three of four layers are STRUCTURAL and ready to spec. The lexical layer needs more depos.

THE FOUR RECONS — KEY FINDINGS

1. **Split pattern discovery sweep** (12,786 Q/A transitions analyzed)
   - 5 NEW HIGH-confidence patterns surfaced (all 7 depos):
     - Bare "And" as Q opener: 671 (9× the previously-tracked sub-phrases combined)
     - "So" as Q opener: 373
     - Double-dash interruption: 244
     - Trailing "huh?" confirmation: 101 (6/7 depos)
     - "Now," as Q opener: 54 (6/7 depos)
   - Plus existing patterns confirmed at HIGH: leading "Yes," (1,382), leading "Okay." (620)
   - **Verdict: STRUCTURAL, ready to spec**
   - Report: C:\mrx_training_set\MB\reports\2026-05-09_split_pattern_discovery.md

2. **Word substitution census** (985 clean 1:1 substitutions)
   - ZERO HIGH-confidence pairs across 7 depos
   - Closest to a rule: there → their (9, 4/7), your → you're (6, 4/7)
   - Top categories noisy (synonym swap = 627 inflated by undetected steno artifacts)
   - M:N complex replacements explicitly excluded as separate larger signal
   - **Verdict: LEXICAL — case-specific, needs more depos to mature, NOT ready to ship**
   - Report: C:\mrx_training_set\MB\reports\2026-05-09_word_substitution_census.md

3. **Capitalization habit scan** (11,546 capitalization changes)
   - Dominant rule: capitalize first word of every sentence (turn-initial OR mid-turn) — fires ~11,000 times across all 7 depos
   - Second rule: "Objection" mid-turn cap (262, 5/7 depos)
   - Sonnet caught his own mis-classification on the "proper noun lift" bucket (actually mid-turn sentence starts) — discipline win
   - **Verdict: STRUCTURAL, ready to spec**
   - Report: C:\mrx_training_set\MB\reports\2026-05-09_capitalization_habit_scan.md

4. **Punctuation transformation census** (7,134 events, strongest result)
   - 94.8% additions, 4.7% substitutions, 0.5% removals
   - 14 HIGH-confidence patterns
   - Top 3: period addition (2,726), comma addition (2,561), em-dash addition (657) — all 7/7
   - Standout finding: stage-direction punctuation rule. End punct always precedes parentheticals. ?( = 125 (6/7), .( = 78 (7/7). Pure muscle memory.
   - **Verdict: STRUCTURAL, strongest fingerprint layer, ready to spec**
   - Report: C:\mrx_training_set\MB\reports\2026-05-09_punctuation_transformation_census.md

ARCHITECTURAL FINDING — NEW DESIGN PRINCIPLE
Layers of a court reporter's fingerprint calibrate at different rates:
- **Structural layers** (splits, capitalization, punctuation) — rules don't depend on case content, READY at 7 depos
- **Lexical layer** (word substitutions) — rules depend on this depo's vocabulary, NOT READY, needs 15-20+ depos OR per-depo handling

This is a real design constraint to bake into the fingerprint architecture going forward. The engine cannot expect all layers to mature at the same rate. Onboarding playbook for CR #2 must respect this — structural rules transfer fast, lexical rules need calibration.

WHAT SHIPPED TONIGHT

Engine repo (mrx_engine_v1):
- HEAD unchanged: 8954b61 (no engine code changes — research only)
- Tests: 864 passing, TD-002 still the only failure
- Pre-existing modification on reports/2026-05-08/steno_ceiling_triage_clean95.md held overnight, fresh Opus triages tomorrow

mrx-context repo:
- handoffs/HANDOFF_OPUS_2026-05-09_evening.md (afternoon session)
- handoffs/HANDOFF_OPUS_2026-05-09_EOD.md (8:15 PM, now superseded)
- handoffs/HANDOFF_SONNET_2026-05-09_evening.md
- handoffs/HANDOFF_SONNET_2026-05-09_EOD.md (8:15 PM, now superseded)
- handoffs/HANDOFF_SONNET_2026-05-09_22EOD.md (commit c298eba) <- active
- handoffs/HANDOFF_OPUS_2026-05-09_22EOD.md (this file) <- active, push when saved

Local-only training set (C:\mrx_training_set\, NEVER pushes):
- MB\paired\ (7 cases: roughs + finals)
- MB\extracted\ (14 plain text files)
- MB\reports\ (4 recon reports + directory inventory)
- MB\paired\MANIFEST.md
- _LEDGER\ (rules_of_engagement.md, onboarded_reporters.md)
- _design_consultations\2026-05-09_audio_architecture\ (chatgpt, copilot, opus_synthesis, INDEX)

KEY DECISIONS LOCKED THIS SESSION

1. Three-lane confidence-banded architecture: AUTO (≥90%, no protected tokens, multi-source agreement) / SUGGEST (60-89% or protected high-conf) / FLAG (<60%) / PROTECTED (any confidence on protected class with audio disagreement → always to MB).

2. The fingerprint earns its keep through measured frequency, not assumed rules. Confidence numbers rise with depo count. Patterns auto-promote and demote based on MB's accept/reject behavior.

3. Audio architecture (synthesized from three hedges):
   - ROUGH stays canonical. Audio is evidence, not authority.
   - Stage 4 enters between Stage 3 and Stage 5.
   - Two-tier sync: timestamps from CAT when available; semantic + token alignment when not.
   - Deepgram + Whisper consensus for low-confidence proposals.
   - Protected-span firewall on negations, numbers, names, yes/no, dates, exhibits, dosages, money, quoted testimony, objections.
   - Audio NEVER writes directly. Always evidence supporting/contradicting a proposal. Exception: literal blanks, audio can originate fill candidate but always routed to MB review.
   - Reporter UX is the actual moat.

4. Engine v1 architecture pieces to recover (from Scott's memory):
   - Reader/Decider/Writer separation
   - Provenance ledger — every change has backstory (rule, evidence, confidence, source)
   - Audio-as-evidence-only rule with blank-fill exception
   - Montreal Forced Alignment for phoneme-level disputes (bright vs brat case)

5. Comprehension Agent / Case Brief is Stage C of the architecture stack (per May 3 capture). Confirmed still right direction. Not a tonight build.

6. Calibration set structure is the template for future CRs. C:\mrx_training_set\<INITIALS>\paired\<case>\{rough,final}\ + manifest + extracted + recons. Repeatable for CR #2.

7. Confidentiality boundary: anything in C:\mrx_training_set\ is local-only. Anything containing MB's witness names, case content, or private folder structure NEVER pushes.

8. NEW: Fingerprint layers calibrate at different rates. Structural (splits, cap, punctuation) ready at 7 depos. Lexical (substitutions) needs 15-20+ OR per-depo. Bake into architecture.

WHAT'S NEXT — RECOMMENDATION

Priority order. Scott picks tomorrow.

1. **Spot-check the recon volumes.** Three of the four reports have HIGH-volume findings (11k cap events, 7k punctuation events, 12k transitions). Spot-check ~20 events per recon to verify counts are real, not artifacts. Quick task, ~30 min.

2. **Recovery search in mrx_engine_v1.** Sonnet greps for: provenance, audit_trail, decision_log, correction_source, rule_id, mfa, montreal, forced_alignment, phoneme. Tells us what survived from engine v1's old reader/decider/writer + provenance ledger. ~30 min.

3. **Solve ROUGH extraction.** Tonight's first frequency recon couldn't get reliable Q/A turn structure from .sgngl binaries. Route .sgngl files through existing Stage 1 turn extractor on the 7 paired roughs. Closes the methodology gap. ~1-2 hours.

4. **Spec the build for the four ready layers.** Splits (5 patterns), capitalization (1-2 rules), punctuation (14 patterns including stage-direction rule). The fingerprint v0 EXPANSION spec — extends the em-dash-only v0 to all the structural layers. ~2 hours.

5. **Build the reporter_pattern_hypotheses.md ledger.** Calibration accelerator for CR #2. Read all four recons, abstract MB's findings into general hypothesis list with evidence. From this point forward, every recon on every reporter updates this file. CR #5 probably needs only 3-4 paired depos. ~1 hour.

6. **Build the onboarding_playbook.md ledger.** Operational step-by-step for onboarding any new CR. Captures gotchas: ROUGH binary extraction, "FOR MB" folder pattern, frequency thresholds, lane structure, protected-class list, audio-as-evidence-only rule. ~30 min.

7. **Hunt for more paired depos.** Tonight's structural-vs-lexical finding tells us more pairs would specifically advance the lexical layer (closer to HIGH-confidence on substitutions). Worth Scott's time later this week to find more pairs. The 16 ambiguous cases from inventory may add some. Other CR contacts/sources may add more.

8. **M:N substitution recon.** Sonnet flagged this as separate larger signal excluded from tonight's lexical census. May surface multi-word substitution rules.

OPEN ITEMS / TECH DEBT

- TD-001: writer JSON truncation, patched not solved
- TD-002: stale W&T e2e test (miss ≥4 expected, engine finds all 9) — quick fix
- Garbled-filter regex bug — patched in tonight's recon scripts but should be locked into source
- ROUGH binary extraction methodology gap — partially worked around, needs proper fix via Stage 1
- 16 ambiguous cases from inventory not yet classified
- Cross-depo scan table at io/analysis/_cross_depo_scan/cross_depo_pattern_table.md still unintegrated
- M:N complex word replacements not yet measured
- Pre-existing engine modification on reports/2026-05-08/steno_ceiling_triage_clean95.md held overnight

SCOTT'S WORKING STYLE (REMINDERS)

- 12-year-old reading level until told otherwise
- Plain English, ONE question at a time, never stack
- Inline A/B/C only when there's a real choice; otherwise just answer
- Code-fenced blocks for ANY content Scott copies to Sonnet
- Always full absolute paths
- Same-day handoffs: paste content in chat AND push to repo
- Halprin and Brandl FINAL files NEVER push — extends to all 7 paired cases and anything in C:\mrx_training_set\
- Sonnet does not push without explicit per-instance Scott override
- Scott commits and pushes engine repo
- DO NOT make Scott a clipboard. If content is in chat or on disk, read directly.
- Slow is smooth. Smooth is fast.

SESSION HEALTH AT HANDOFF

Opus (this chat): healthy through the session, ~70% context used. Two failure modes called out and corrected mid-session: (1) dumped a 800+ line file save block when 4 lines would have done, (2) raced ahead of Scott on next moves multiple times. Reset, owned both. Slowed down second half. Final wrap is clean, not a crash.

Sonnet (today's marathon): cycled through multiple instances. Final fresh instance ran the four recons cleanly, caught his own mis-classification on capitalization, gracefully declined a fifth recon when Scott considered pushing further. Earned his rest.

Scott: 12-14 hour day. Two paste-twice mistakes tonight (Sonnet flagged both, Scott owned both). Pushed himself into a real research session that materially advanced the architecture. Wrapped at 10:00 PM. Calm, tired, satisfied.

THREE SESSION NOTES YOU SHOULD KNOW

One: The pivot tonight from "build" to "calibrate" was the most important architectural move of the week. Three of four fingerprint layers are now data-backed and ready to spec, instead of one mid-confidence pattern. The pattern discovery sweep specifically validated systematic recon over targeted matching — bare "And" as Q opener was 9× the volume of the sub-phrases earlier recons were tracking.

Two: The structural-vs-lexical layer-rate finding is a NEW architectural design principle. Tomorrow's spec work and the future onboarding_playbook should treat them as separate calibration tracks. Don't conflate them.

Three: All four recon reports were saved local-only at C:\mrx_training_set\MB\reports\. None pushed to public repo. Confidentiality boundary held tight throughout the night despite multiple data movements.

CODER MINDSET REMINDERS

Before any code change: "Could this change reduce transcript accuracy or credibility?" If yes or maybe → STOP, flag.

Three Brains: Engineer (can?), Architect (should?), Owner (worth?).

RULE-RECON-FIRST. RULE-CONTRADICTION-HUNT. RULE-SILENT-FAILURE-CHECK. RULE-INPUT-IS-SACRED. RULE-SPEC-BEFORE-BUILD.

Slow is smooth. Smooth is fast.

— End of Opus 2026-05-09 22:00 EOD handoff —
