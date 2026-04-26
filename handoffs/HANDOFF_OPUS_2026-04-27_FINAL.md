# HANDOFF — OPUS — 2026-04-27 END OF SESSION

---

## ONE-LINE STATE

Stage 5 v0.1 build is 4 of 8 modules complete. 391 tests passing in engine repo. Module 5 (turn_renderer.py) spec is YOUR FIRST DELIVERABLE — it has not been written yet. Sonnet is fresh and waiting on you. Scott is exhausted and tagging out. Pick up clean and move.

---

## RAMP — READ THESE IN THIS ORDER BEFORE DOING ANYTHING

You have web_fetch. Use it. Do not wait for Scott to paste anything.

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_v01_BUILD_SPEC.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-04-27_FINAL.md (so you know what fresh Sonnet was told)
5. This handoff (you're reading it)

After reading, confirm in ONE LINE: "Ramped from Opus handoff 2026-04-27 EOD. Ready."

---

## YOUR ROLE (PER RULE-ARCHITECT-PM-BUILDER-SEPARATION)

You are Opus, the architect. Sonnet is the builder. Scott is the human owner.

- You write specs, never code
- You answer Sonnet's design questions, never bypass him
- You catch Sonnet when he hits something the spec didn't cover
- You report progress to Scott in plain English
- You write handoffs at session end

---

## WHERE THE BUILD STANDS

| Module | File | Status | Commit |
|---|---|---|---|
| 1 | src/stage5/schemas.py | DONE | 98607a2 |
| 2 | src/stage5/case_info_loader.py | DONE | 3cf2e62 |
| 3 | src/stage5/proposal_mapper.py | DONE | eb3cfc4 |
| 4 | src/stage5/review_tags.py | DONE | 0a05aad |
| 5 | src/stage5/turn_renderer.py | NEXT — your spec | — |
| 6 | src/stage5/document_composer.py | not started | — |
| 7 | src/stage5/page_layout.py | not started | — |
| 8 | src/stage5/assemble_final.py | not started | — |

391 tests passing in engine repo, all green. Two specs already exist for Modules 1-4 and the parent — same pattern Module 5 follows.

Existing module spec template you should copy:
- https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_5_MODULE_4_REVIEW_TAGS.md

---

## YOUR FIRST DELIVERABLE — STAGE 5 MODULE 5 SPEC

**Module 5 = turn_renderer.py** — the most complex module in the build.

### What it does
Takes a single turn (raw text + speaker + paragraph_style) plus its list of ApplicationEntries (REWORDs and FLAGs), produces the rendered turn text with inline `{{MB_REVIEW-*}}` markers and a list of ReviewQueueEntry records.

### Inputs
- One turn dict (from corrected_turns.json — fields: idx, speaker, text, paragraph_style, ...)
- list[ApplicationEntry] for that turn (from Module 3's application_map)

### Outputs
- Rendered text (string) with markers inline
- list[ReviewQueueEntry] for items to add to the side-channel queue

### Algorithm (per parent spec §5 Phase 2)
1. Tokenize text by whitespace: `tokens = text.split()` (v0.1 — must match Reader)
2. Verify each ApplicationEntry's token_span aligns: `tokens[start:end+1]` should equal entry.before. If mismatch, log warning, skip that entry.
3. Sort entries by `token_span[0]` DESCENDING (right-to-left application)
4. For each entry:
   - REWORD: replace tokens[start:end+1] with the rendered marker (`render_reword_marker` from Module 4) which contains the after text wrapped in `{{MB_REVIEW-*}}{{/}}`
   - FLAG: insert the marker (`render_flag_marker` from Module 4) immediately AFTER tokens[end]
5. Re-join with single spaces. Return rendered text + list of ReviewQueueEntry.

### Key risks (call these out in the spec)
- Tokenization mismatch with Reader → log warning, skip, do not crash
- Multiple ops on overlapping spans → reject the entry pair, log warning, skip both
- The tokens that come back from text.split() may have trailing punctuation attached. Spans from the Reader treat words as tokens. Verify behavior on real Block H data before locking the algorithm.

### Tests required
- Single REWORD high confidence
- Single REWORD medium confidence
- Single FLAG
- Multiple ops in one turn (right-to-left correctness)
- Tokenization mismatch (skip + warn)
- No ops (empty list returns text unchanged)
- Real Block H sample (integration check, can be skipped if files absent)

### Spec format
Match the format of `STAGE_5_MODULE_4_REVIEW_TAGS.md`. Save to:
`C:\Users\scott\OneDrive\Documents\mrx-context\specs\STAGE_5_MODULE_5_TURN_RENDERER.md`

Have Sonnet save it, push, recon, then await approval — same pattern as Modules 1-4.

---

## CRITICAL DESIGN DECISIONS LOCKED (DO NOT REVISIT)

### Positional joins (Modules 1-4 already use this)
proposals, decisions, anomalies join by index `i`, NOT by ID. Verified in Module 3. Do not propose dict-keyed joins.

### Tokenization for v0.1 = whitespace split
Must match Reader. Mismatch → log + skip, never crash.

### Multiple ops per turn = right-to-left
Sort by `token_span[0]` descending.

### Tag rules (already in Module 4)
- REWORD high → MB_REVIEW-FIX confident
- REWORD medium/low/unknown → MB_REVIEW-VERIFY
- FLAG always → MB_REVIEW-FLAG

### Output format = plain text first
v0.1 produces .txt. CAT round-trip / RTF / PDF deferred to v0.2.

---

## PIPELINE STAGES (FULL PICTURE)

| Stage | Status | Notes |
|---|---|---|
| 1 — RTF parse | DONE | 552 turns extracted, all acceptance criteria pass |
| 2 — Cleanup | DONE | 75 light transforms |
| 3.1 — Reader+Writer suggester | DONE | Block H ran 2026-04-26, 30 proposals, $0.63 |
| 3.5 — Audio Vote | NOT BUILT | Architecture B locked (Whisper + text-match), Brandl fixture ready |
| 4 — Audio Specialist | NOT BUILT | Becomes 7th specialist or separate stage — decision deferred |
| **5 — Assemble final document** | **IN PROGRESS — 4/8 modules done** | This build |

Stage 4 / 3.5 architecture context lives at:
https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/STAGE_4_OPUS_CONTEXT_2026-04-24.md

---

## WHAT FRESH OPUS DOES NEXT (AFTER RAMP)

1. Confirm "Ramped..." in one line
2. Wait for Scott to say "go"
3. Draft the Module 5 spec inline in chat
4. Hand it to Scott to paste to fresh Sonnet (same pattern as Modules 1-4)
5. Sonnet saves spec to mrx-context, pushes, recons
6. You approve build
7. Sonnet builds Module 5
8. Move to Module 6

---

## SCOTT'S WORKING STYLE (CRITICAL — DO NOT VIOLATE)

- Treat as 12-year-old until told otherwise
- Plain English. Short answers.
- ONE question at a time. NOT three.
- Inline A/B/C ONLY when there's a real choice. When there's a clear right answer, give it.
- He hates file dialogs. Sonnet writes files. Scott does not copy-paste into Notepad. Ever.
- He hates fire-hose responses. Keep messages tight.
- He pushes back. His pushback is usually right.
- He's been doing this for two weeks. He's tired. He's frustrated. Respect it.

---

## SCOTT'S MOOD AT SESSION CLOSE

Long session — many hours, multiple emotional peaks. Real frustration at file management overhead and the cross-session leak that drove this whole `mrx-context` system. **The leak is now closed.** This handoff is the proof. By the end he was clear-eyed and tagged us both out cleanly. Respect the ground gained. Open calm. Build Module 5. Get him a document tomorrow.

---

## REVISIT LIST (NOT BLOCKING — DO NOT WORK THESE)

- [ ] ARCHITECTURE_DECISIONS.md, ONBOARDING_REQUIREMENTS.md, ORACLE_COVENANT.md drafts (still placeholders in mrx-context — fill in after Stage 5 ships)
- [ ] State module version mismatch in Block H runner (older Brandl LA Engineering vs newer mb_demo)
- [ ] Block H integration report (replaced by reading the Stage 5 output)
- [ ] Index page generation (Stage 5 v0.2)
- [ ] Stage 4 audio architecture (after Stage 5 ships)
- [ ] Compound-key (batch_id, proposal_id) joins for proposals/decisions/anomalies (Module 3 Future Work)
- [ ] CR onboarding intake form (production version of case_info.json)
- [ ] File-management workflow improvement so Scott never touches files (deferred but acknowledged painful)

---

— End of Opus handoff —
