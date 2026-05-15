# HANDOFF — OPUS — 2026-05-15 ~11AM (line change)

**For:** Fresh Opus, next session same day
**From:** Opus, 2026-05-15 7AM-11AM session
**Owner:** Scott
**Builders:** Sonnet #1 (Lane A — pipeline), Sonnet #2 (Lane B — data + validation)

---

## STANDING RULES — non-negotiable

1. 12-year-old reading level. Plain English. Short answers.
2. ONE question at a time. Never stack.
3. Always full absolute paths.
4. Inline A/B/C only when there's a real choice.
5. When unsure, make a recommendation — don't ask open-ended.
6. Sonnet writes files and runs shell. Scott pushes commits when asked. Opus writes specs.
7. SHAPE MATCH ONLY. Never byte-match a hand-typed fixture.
8. 5-line answers.
9. Anything for Sonnet goes in a code block. Anything outside is for Scott.
10. Print every file Sonnet writes to terminal (type <path>) for visibility.
11. RULE-SPEC-SAVED-FIRST — spec saved to repo BEFORE builder work starts.
12. RULE-TEST-CASE-FIRST — design test cases BEFORE running any model.
13. Before any code change: "Could this reduce transcript accuracy or credibility?" If yes/maybe, STOP.
14. 30-min wall per build pass. Backup branch before cleanup. One fix per branch.
15. PUSH BACK HARD, ACT ONLY ON APPROVAL.
16. Halprin and Brandl FINAL files NEVER push to public repo.
17. NEW today — ASK SCOTT "ready for the spec?" BEFORE writing any spec.

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md (includes RULE-SPEC-SAVED-FIRST + RULE-TEST-CASE-FIRST added today)
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-15_11AM.md (this file)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET1_2026-05-15_10AM.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-15_A1.5_APPEARANCES_WIRE_IN_v2.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-15_A1.5.1_APPEARANCES_RENDERER_BUG_FIX.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-15_B1.6_CERT_WIRE_IN.md
9. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-15_B1.7_INDEX_EXHIBITS_AUDIT.md
10. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-15_AUDIO_SYNC_RECON.md
11. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-15_REPORTER_CERT_AUDIT.md
12. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-15_INDEX_EXHIBITS_AUDIT.md
13. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/test_cases/2026-05-15_WHISPER_HALPRIN_CHALLENGE_SHEET.md
14. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/fingerprints/ledger.md

After ramp: confirm "Ramped Opus 2026-05-15 11AM. Ready." plus one sentence on state + one question for Scott.

## ONE-LINE STATE

Front matter generalization in flight — A1.5 wire-in works mechanically but surfaced 2 pre-existing renderer bugs blocking Halprin byte-match; Sonnet #1 reconning A1.5.1 fix; Sonnet #2 idle, ready for B1.6 (cert wire-in) once A1.5 lands; B1.7.1 (index wire-in + guard fix) queued with prep complete.

## WHAT SHIPPED THIS SESSION (7AM-11AM)

1. **A1 differ v0.2** — pushed to `feature/differ-v0.2` (commit 0f6352f). word_substitution dropped (139,912 noise events gone), q_a_speaker_change added (197 events). Halprin re-run clean. NOT merged to main pending 14-pair validation.

2. **B1 audio sync recon** — verdict WHOLE-FILE WHISPER. .sgxml has only 88 playback bookmarks covering 13% of depo. Whisper cost ~$1-2/depo. Knowledge file at knowledge/2026-05-15_AUDIO_SYNC_RECON.md.

3. **B1.5 reporter cert audit** — verdict C (modified). Renderer built and data-driven but build_back_matter() called from nowhere. Same pre-A1.5 state. Two latent MB-name hardcodes flagged.

4. **B1.7 index + exhibits audit** — all 6 depos have hand-extracted index.json. Renderer (index.py) exists with 2 guard issues for 5-entry nav depos (butler, olsen, black_bp, blanks).

5. **B2.5 Whisper challenge sheet** — 25 rows across 7 of 8 defect categories. Ready to score Whisper when B3 runs.

6. **RULE-SPEC-SAVED-FIRST + RULE-TEST-CASE-FIRST** — added to addendum. Scott to push when convenient.

7. **Halprin front matter verify** — Sonnet #1 ran re-render, files identical because Thursday's fixes live in appearances_renderer.py but pipeline still calls appearances_page.py. This is what triggered A1.5.

## OPEN WORK

### Sonnet #1 — in progress
- Working A1.5.1 (renderer bug fix) on `feature/appearances-renderer-fix`
- Bug A: middle dot (U+00B7) replaced with two spaces on Halprin page 5 line 32
- Bug B: 1-space indent shift on pages 6-10
- Status: in recon phase as of 11AM
- Branch cut from `feature/appearances-wire-in` (preserves wire-in)

### Sonnet #2 — idle, holding
- B1.6 (cert wire-in) on `feature/cert-wire-in` — recon done, awaiting A1.5 in main
- B1.7.1 (index wire-in + guard fix) prep complete — exact line numbers ready
- Compacted once this session, plenty of runway

### Queued tiles
- **A3** — 14-pair Stage A re-run on differ v0.2 (blocked on Round 2 CATalyst exports)
- **B2** — Round 2 CATalyst exports (Rooks, Nguyen, Thompson, Washington, Black) — Scott on CATalyst
- **B1.7.1** — index wire-in + index.py guard fix (Sonnet #2's next when A1.5 lands)
- **B3** — Whisper run against challenge sheet (blocked on OpenAI API key — Scott to fix)
- **A2** — MB.yaml v0.1 shape spec (after differ v0.2 validates on 14 pairs)
- **A6+** — Stage C Comprehension Agent (post-fingerprint, weeks out)

## MERGE PLAN (when ready)

Sequence:
1. A1.5.1 lands → byte-match Halprin oracle clean
2. Merge `feature/appearances-renderer-fix` INTO `feature/appearances-wire-in`
3. Merge `feature/appearances-wire-in` INTO main (one commit, clean story)
4. Sonnet #2 pulls main, rebases `feature/cert-wire-in`
5. B1.6 builds → byte-match Halprin oracle clean
6. Merge `feature/cert-wire-in` INTO main
7. Sonnet #2 starts B1.7.1 → wire in index renderer + guard fix
8. Merge → main now renders any of 6 MB depos with correct front matter

## KNOWN DEBT (capture for ledger when wire-ins land)

1. Premature witness_cert.json load in build_back_matter() (B1.5 audit finding)
2. MB name hardcoded in reporter_cert.py line 7-8 and witness_cert.py _REPORTER_LINE
3. cert_year extraction breaks if date doesn't end in 4-digit year (witness_cert.py)
4. word_substitution category formally excluded from differ — revisit if true substitutions ever needed

## KEY FILE POINTERS

### Engine repo
- Branch: feature/appearances-wire-in (Sonnet #1's wire-in, no commits)
- Sub-branch: feature/appearances-renderer-fix (Sonnet #1's active work)
- Branch: feature/cert-wire-in (Sonnet #2 holding)
- Branch: feature/differ-v0.2 (pushed, awaiting 14-pair validation)
- Main: 95f09ee — appearances code in main but not wired in

### Halprin baselines
- Oracle: C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt
- Pre-fix snapshot: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_full\_stage5_out\halprin_full.OUR_FINAL.pre-fix.txt

### 6 MB depos with front matter JSONs
- halprin, 060122williams, 082222butler, 032025olsen, 0525black_bp, 101322blanks

## SCOTT'S STATE AT 11AM

Sharp morning. Caught architect mid-mistake twice (A1.5 spec gaps surfaced by Sonnet #1 recon, hardcoded front matter framing that previous Opus had wrong). Set new rule today: ASK before writing specs. Energy: focused, deliberate, slow-is-smooth mode. Goal still MB demo on a non-Halprin depo. Critical path: complete front matter generalization today, Round 2 data + 14-pair re-run next.

## ONE-CUSTOMER FRAME (do not lose)

MB is the customer. The bar for v0 is MB's bar. Today's work makes the engine able to render any of 6 MB depos with correct front matter (cover, index, exhibits, appearances, stipulation, videographer, cert). That's the precondition for the A10 demo.

— End of Opus 2026-05-15 11AM handoff —
