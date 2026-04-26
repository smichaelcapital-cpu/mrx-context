### Step 3: Draft ARCHITECTURE_DECISIONS.md (the big new doc).

Capture every architectural decision made on MyReporterX so far. Pull from Scott's user memories, the MASTER_COPIES docs, the inventory Sonnet pulled, and the seeds in the "ARCHITECTURE NOTES" section below. Sections:

- **Pipeline stages** (0.5 → 1 → 2 → 3.1 → 3.5 → 5) with status per stage
- **Whisper-first audio strategy** (and why — previous engine couldn't sync timestamps to raw)
- **Three-tag review system** (`Agent-Fix: confident` / `Agent-Fix: review` / `Agent-Flag: needs human`)
- **Audio as last gate before MB sees a tag** (scopist parallel)
- **Oracle Covenant** (humans read FINAL for design discovery, pipeline never touches it)
- **Read-Write Separation** (Writer never sees raw transcript)
- **Raw stays pristine, work from copies** (never modify MB's original data)
- **CAT scopist workflow as the model** (digital scopist hands back tagged work, MB's CAT does final assembly from her template)
- **Output format for validation** (plain .txt for now, not delivery format)
- **MB-first principle** (every decision passes the MB Test — single mom doing real CR work at 11 PM)
- **Three Brains check** (engineering / architecture / business on every decision)
- **Prime Directive** ("Could this change reduce transcript accuracy?" If yes or maybe → STOP)

Have Scott review. Correct what's wrong. Add what's missing. Commit + push.

### Step 4: Draft ONBOARDING_REQUIREMENTS.md.

What MyReporterX asks every new CR for. Tier 1 (per-depo bundle), Tier 2 (case-level), Tier 3 (CR-level), Tier 4 (per-depo style overrides). Full draft already exists in this session's chat — Opus can pull it from there or rebuild from scratch.

### Step 5: Then — and ONLY then — start the build.

Build target: **Stage 5 v0.1 — `assemble_final.py`**

Input:
- `corrected_turns.json` (552 turns post-Block H)
- `proposals.json` + `decisions.jsonl` (so we know what got changed and at what confidence)
- `case_info.json` (hand-built once for Halprin from what's already visible in stage1.txt + .sgxml metadata)

Output: `halprin_mini.OUR_FINAL.txt` — depo-formatted plain text:
- Cover page (from case_info)
- Appearances block (from case_info)
- Q/A body indented like a real depo, with synthesized page/line numbers
- Inline `{{MB_REVIEW-FIX: confident — reason}}` tags where high-confidence proposals were applied
- Inline `{{MB_REVIEW-VERIFY: reason}}` for medium-confidence applies
- Inline `{{MB_REVIEW-FLAG: reason}}` for anomalies detected but not auto-fixed
- Certification at end (boilerplate)

Goal: Scott opens MB's `040226yellowrock-FINAL.txt` in one window, our `halprin_mini.OUR_FINAL.txt` in another. He sees them side-by-side. He sees what's right and what's broken. He logs defects. **That's the test loop.**

---

## OPEN DECISIONS

- **Shared repo name:** `mrx-context` is a suggestion. Scott picks the actual name.
- **Where handoff files live going forward:** during transition, MASTER_COPIES is fine. Long-term, all handoffs commit to `mrx-context/handoffs/`. Migrate when ready.
- **case_info.json schema:** spec it as part of Stage 5 v0.1 design. Keep it minimal — just what's needed for cover, appearances, certification. Don't over-engineer.
- **Block H integration report:** still owed. We never sampled the 30 proposals or wrote a quality assessment. Not blocking — but on the list to revisit once Stage 5 produces a readable doc, because at that point we read the doc instead of the JSON.

---

## ARCHITECTURE NOTES MADE THIS SESSION

These need to land in `ARCHITECTURE_DECISIONS.md` next session:

1. **Whisper-first audio strategy.** Previous engine couldn't reliably sync per-word audio timestamps from raw RTF/.sgxml. .sgxml has only 88 session-level checkpoints across 300pp. New design: Whisper-transcribe the entire audio file upfront, get word-level timestamps from Whisper itself. Cost ~$1 per 3-hour depo via OpenAI Whisper API — negligible vs. revenue. This becomes Stage 0.5, runs before Stage 1.

2. **Stage 3.5 Audio Vote.** After Stage 3.1 produces text-only proposals, Stage 3.5 takes uncertain ones and does a three-way vote: steno raw / AI proposal / Whisper transcript. All three agree → upgrade to confident. Two agree → review. All differ or audio garbled → human flag. **This is the final gate before MB sees a tag, mirroring the scopist's "let me play the audio" instinct.**

3. **Stage 3.5 only runs on uncertain proposals, not all of them.** High-confidence text proposals (e.g., obvious doublets) skip audio. Saves cost, matches scopist behavior.

4. **Stage 5 plain text first, delivery format later.** Goal is validation (open side-by-side with MB's FINAL.txt), not production delivery. CAT round-trip is a separate problem we don't solve until quality is proven.

5. **No silent edits, ever.** Every Agent action gets a tag. Three buckets: confident-fix / review-needed / no-fix-flag-only. The tags are how MB audits in seconds vs. reading word-for-word.

6. **Stage 1 Q/A extraction is solved.** Reading RTF paragraph styles directly (s1/s2/s3/s5/s7) eliminates the previous engine's turn-boundary guessing problem. Don't rebuild this.

7. **The bundle from MB:** raw RTF + .sgxml metadata + .sgngl binary + audio + dictionaries. Stage 1 needs the RTF. .sgxml is useful for metadata. Audio feeds Stage 0.5. Dictionaries feed Stage 3.1's loader. .sgngl we don't currently need.

---

## PARKING LOT

Don't work these next session — they're for after Stage 5 v0.1 is done:

- **Block H integration report** (sample 10 proposals, assess quality) — replaced by reading the assembled .txt
- **Stage 0.5 Whisper pre-processor** — needed for Stage 3.5, but Stage 5 has to come first
- **Stage 3.5 Audio Vote** — depends on Stage 0.5
- **State module version mismatch** — runner loads older Brandl copy of LA Engineering module instead of newer mb_demo_engine_v4 copy. Confirm which is authoritative before next live run.
- **5 untracked docs in `docs/`** — commit-or-gitignore decision deferred
- **`test_dictionary_loader.py` drift** — pre-existing, not blocking
- **PROJECT_BOARD.md / CURRENT_SPRINT.md for mrx_engine_v1** — currently doesn't exist; v4 versions are stale by a month. Replace once `mrx-context` is set up.
- **CR onboarding UI** — depends on web app build, post-MVP
- **button_up.py automation** — replaced by HANDOFF convention; revisit if process matures
- **Code Cop / Story Teller / UI Agent** infrastructure brainstorms — post-MVP
- **CAT round-trip / .sgngl format reverse engineering** — only matters when we're ready to deliver to MB in production format

---

## SCOTT'S MOOD / SESSION ENERGY

Long session — 6+ hours by close. High frustration mid-session at the "every session starts from scratch" leak — Scott named it directly: *"this happens every session and it is expensive."* That frustration is real and is what drove the HANDOFF + `mrx-context` plan. He ended in good rhythm: code pushed, real understanding of the pipeline, clear next move. Respect the ground gained. Open next session calm and direct, do the repo setup first, then build. Don't reset to "let me ask 5 questions." He's earned the win and the plan is sound.

---

## FOR NEXT OPUS — EXPLICIT REMINDERS

- **Stop guessing about CAT, .sgxml, file formats, scopist workflow.** That research was done this session; it's all captured in ARCHITECTURE_DECISIONS.md (which you're about to write). Read it. Don't redo it.
- **Stop treating architecture decisions as news.** They're written down now. If Scott references something you don't know, fetch the relevant doc from `mrx-context` first.
- **Plain English, treat as 12-year-old until told otherwise.** Short answers. ONE question at a time. Inline A/B/C only when there's a real choice.
- **No popup widgets** (`ask_user_input_v0`) with Scott — offer choices inline.
- **Never read FINAL files at runtime.** Oracle Covenant. Humans only, design discovery only.
- **Full file paths whenever referencing files.** Scott asked for this explicitly today.

— End of handoff —
