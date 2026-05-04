# RECON: Punctuation Bible vs. Bucket B Reality Check
**Date:** 2026-05-04
**Analyst:** Claude Sonnet 4.6
**Requested by:** Opus Tuesday ramp (Priority 3)
**Status:** Recon only — no code changes, no spec

---

## 1. Bible Location and What It Is

**Short answer: the Punctuation Bible does not exist as a file, a prompt, or a rule set in this repo.**

It is referenced as "Layer 5" in two spec/architecture docs:

- docs/STAGE_3_1_SUGGESTER_SPEC.md (lines 466 and 744)
- docs/STAGE_3_ARCHITECTURE_v2.md (line 165)

Both references describe it as a *future* component of the Writer agent's system prompt — the layer the Writer is supposed to consult for normalization choices. It has not been written. There is no Layer 5 prompt. There is no Bible file anywhere in the repo.

**What the current engine actually does for quotes and dashes:**

Stage 2 transforms (stage2/transforms.py): T1 double-space after sentence punctuation, T2 uh-huh hyphenation, T3 year-range slash-to-hyphen, T-WS variants for whitespace. Zero quote or em-dash rules.

Stage 3.1 Reader (suggester.py line 228): Explicitly told "You must NOT flag missing Q/A labels, missing punctuation, or capitalization issues." One exception carved out: if a witness doubles a word ("Yes yes") the Reader flags it as steno_artifact so the Writer can insert the em-dash. That is the only punctuation-adjacent rule in the entire engine.

Stage 3.1 Writer (suggester.py, prompts.py): "Do not fix punctuation unless it's clearly wrong. Stage 2 handles most punctuation." No quote rules. No em-dash rules beyond the doubled-word exception.

**One-paragraph summary of what a Bible would cover (per spec):**
The spec envisions the Punctuation Bible as a Layer 5 reference given to the Writer agent covering commas, periods, quotes, and semicolons per court-reporter convention. The Reviewer specialist table also references it for a "Punctuation" specialist checking quotes and semicolons. It would define MB's normalization choices so the Writer knows what form is correct when proposing a REWORD. It has not been written and no rules from it have been implemented.

---

## 2. The 20 Sample Blocks

### Em-Dash Samples (10 of 265 Bucket B blocks)

| Block | What MB did | Bible rule covers this? | If yes — which stage? | Gap if NO/PARTIAL |
|-------|-------------|------------------------|----------------------|-------------------|
| 4 | Em-dash for single-word mid-thought restart: "volumes of oil -- oil barrels" (witness paused, no exact word repeat) | NO | — | Single-restart without repeated token. Reader only flags doubled tokens. |
| 75 | Em-dash for hesitation/false-start mid-sentence: "about -- not as much lately" | NO | — | Hesitation restart. Audio-dependent; no text signal. |
| 140 | Trailing em-dash on incomplete question: "Since the acquisition in 2018 --" | NO | — | Attorney turn cut off or left incomplete. No rule for trailing dash on a truncated turn. |
| 228 | Two em-dashes for attorney self-correction: "Yellow Rock -- I'm sorry -- for White Top" | NO | — | Attorney (not witness) mid-sentence correction. Reader exception is witness-only doubled-token. |
| 292 | Trailing em-dash on incomplete question: "communications still being made --" | NO | — | Same pattern as Block 140. Trailing truncation. |
| 342 | Trailing em-dash on incomplete question: "when Mr. Barrett and Luminus --" | NO | — | Same. |
| 418 | Multiple em-dashes for compound mid-stream hesitations across one long turn | NO | — | Complex hesitation pattern; multiple restarts. Audio-dependent. |
| 487 | Leading false-start dash: "The -- probably the summation" | NO | — | False-start at beginning of witness answer. No rule. |
| 558 | Trailing em-dash on incomplete question: "Not really, were you --" | NO | — | Same pattern as Blocks 140/292/342. |
| 601 | Multiple em-dashes throughout long witness answer with restarts, hedges, corrections | NO | — | Complex multi-point hesitation. Audio-dependent throughout. |

### Quote-Mark Samples (10 of 63 Bucket B blocks)

| Block | What MB did | Bible rule covers this? | If yes — which stage? | Gap if NO/PARTIAL |
|-------|-------------|------------------------|----------------------|-------------------|
| 12 | Scare-quoted a single word: Q. What do you mean "unlicensed"? | NO | — | Editorial judgment. Attorney highlighting a term used by the witness. |
| 192 | Quotes around attorney reading document aloud: "We acquired the rights to take over operations from current operator (Mom & Pop outfit)" | NO | — | Audio-dependent. MB recognizes attorney is reading. Steno captures it as plain text. |
| 207 | Attorney reads from document; MB added opening quote mark to match closing that was already present | NO | — | Partial-quote correction. Editorial. |
| 255 | Quotes around a document title: "Signal JV Checklist" | NO | — | Named document/exhibit. Editorial convention. |
| 316 | Scare-quoted a single word in witness testimony: "drive" | NO | — | Editorial judgment. Witness distancing from their own word choice. |
| 468 | Quotes around a phrase being referenced: "at this point in time" | NO | — | Attorney referencing prior testimony phrasing. Editorial. |
| 512 | Quotes extended around an accounting term: "less accumulated DD&A" (existing close-quote was already there; MB added the open-quote) | NO | — | Partial quote completion. Editorial. |
| 550 | Attorney reads multi-sentence document excerpt; MB added opening quote and closing quote | NO | — | Audio-dependent document read. Steno produces it as plain text. |
| 629 | Attorney reads document subject line: "Updated Financial Statements reclassifying the investment in Yellow Rock." | NO | — | Audio-dependent. |
| 676 | Quotes around document subject: "White Top Seismic Cost" | NO | — | Document subject/title. Editorial. |

---

## 3. Verdict

**Verdict B — The Bible doesn't cover MB's actual habits.**

More precisely: the Bible does not exist yet. But even if it were written today, it would not close the gap — because the gap is not a missing rule, it is a missing capability.

**Why dashes are not catchable by a Bible rule:**

10 of 10 em-dash samples fall into patterns that require audio or inference the engine cannot make:
- Trailing truncation (Blocks 140, 292, 342, 558): there is no text-level signal that a question was left incomplete. The steno just ends. MB hears the recording and adds the dash.
- Single-restart without repeated word (Blocks 4, 75, 487): the witness said something, paused, restarted. The steno captured the restart. Without the pause, there is no text signal.
- Multiple hesitations and complex restarts (Blocks 418, 601): audio-dependent throughout.
- Attorney self-correction (Block 228): the word "I'm sorry" is present but reliably connecting that to a preceding dash requires discourse parsing the engine does not do.

The one em-dash pattern the engine DOES partially handle (doubled-token self-correction, e.g. "Yes yes") does not appear in any of the 10 sampled blocks. The 265 Bucket B em-dash blocks are dominated by the harder patterns.

**Why quotes are not catchable by a Bible rule:**

10 of 10 quote samples are proofread editorial additions, exactly as MB confirmed to Scott on Sunday/Monday:

- Attorney reading from a document (Blocks 192, 207, 550, 629): MB adds quotes because she hears the attorney switch to reading aloud. No text signal. The steno renders the read content as plain testimony.
- Document/exhibit titles (Blocks 255, 676): editorial convention for naming exhibits. The engine would need to know these are titles, which requires case-level context not present in the steno.
- Scare quotes / term highlighting (Blocks 12, 316, 468): pure editorial judgment. MB decides a word is being used with irony, emphasis, or distance. No rule produces this.
- Partial quote completion (Blocks 207, 512): the closing quote was already present from a prior sentence; MB added the opening quote she missed the first time. This is a proofread correction, not a rule-based pattern.

**MB's question answered directly:**

MB asked: "If quotes and dashes are general punctuation rules, why doesn't the Bible catch them?"

The answer is: they are not steno errors. They are proofread additions. A Bible codifies what the correct form is when a steno error is detected. But you cannot detect the absence of a quote or dash from a steno output that never contained one. The engine would need to know that the attorney is reading a document aloud (audio), or that the witness paused and restarted (audio), or that a word is being used with editorial distance (human judgment). None of those signals are in the steno text.

---

## 4. Stage 2 Candidates (Verdict A or MIXED only)

Not applicable — Verdict is B. No Bible rules exist, and even if they did, none of the 20 sampled patterns could be moved to Stage 2 as deterministic transforms. Stage 2 requires text-level certainty with no judgment. All 20 samples require either audio context or editorial judgment.

**One narrow note for future reference:** the doubled-token em-dash case ("Yes yes" → "Yes -- yes") is the only em-dash type that is text-detectable. It is partially handled in the Stage 3.1 Reader as a steno_artifact exception. It does not appear in the sampled Bucket B blocks, suggesting most of the 265 em-dash misses are the harder non-detectable types. A deeper count of how many of the 265 are doubled-token vs. the other types would sharpen the picture — but that is a separate analysis.

---

## Appendix: Key Facts for the Strategy Conversation

- Bucket B total: 527 blocks
- em_dash: 265 blocks (50.3% of Bucket B)
- quote_marks: 63 blocks (12.0% of Bucket B)
- cap_proper: 198 blocks (37.6% of Bucket B)
- comma_punct: 1 block

Quotes + dashes alone = 328 of 527 Bucket B blocks (62.2%). These are not engine bugs. They are proofread editorial steps that require capabilities the current architecture explicitly defers to audio (Stage 4) or human review. They will not move until either Stage 4 audio ships or the product decides to leave them to the reporter.

The 198 cap_proper blocks are a different category — those may have a mix of text-detectable (proper-noun capitalization) and editorial cases. That is outside the scope of this recon.
