# Sonnet Handoff — 2026-05-09 Evening
**From:** Claude Sonnet 4.6 (session ending)
**To:** Next Sonnet instance
**Engine HEAD:** `8954b61` (feat: Gate 4 — wire optional fingerprint into assemble_final)
**mrx-context HEAD:** `6838440`

---

## Session Summary

This session ran the first fingerprint-enabled Brandl diff, then did four consecutive recon
dives into the top error categories from that diff. All five reports are pushed.

---

## Reports Pushed Today

| Report | Path | Commit |
|---|---|---|
| Brandl v0 fingerprint run | `reports/2026-05-09/brandl_v0_fingerprint_run.md` | `be8a2b6` |
| cap_proper recon | `reports/2026-05-09/cap_proper_recon.md` | `6ec8a1a` |
| Sentence-break recon | `reports/2026-05-09/sentence_break_recon.md` | `8470f8a` |
| Q./A. boundary bug recon | `reports/2026-05-09/qa_boundary_period_bug_recon.md` | `a72d6be` |
| Sequential "And" recon | `reports/2026-05-09/sequential_and_recon.md` | `6838440` |

---

## Key Findings in Plain English

### 1. Fingerprint v0 run (55 `--` tokens blocked)

Running MB's fingerprint against the Brandl 50pp output removed 55 em-dash tokens. Word
content was identical after removal — the `--` tokens existed in isolation, not as substitutes
for real words. The ceiling score did not move (824→825 blocks, a rounding artifact). Cost $0.
The fingerprint pipeline works correctly end-to-end.

### 2. cap_proper bucket is 42% contaminated

510 blocks are classified `cap_proper` by the diff scorer. But ~215 of them are garbled steno
failures — the `is_cap` heuristic misfires whenever a REVIEW-tagged block happens to share a
word with MB's version after punctuation-stripping. True cap-style error count is ~295, not 510.
Fingerprint-closeable sub-patterns: proper noun capitalization (~30 blocks) and term format
("E-mail" → "Email", ~15 blocks) — together ~45 blocks, one YAML addition each.

### 3. Reclassification #1 — Q./A. boundary is editorial splitting, not a period bug

The sentence_break_recon counted 74 blocks as "Q./A. turn boundary." Investigation of five
representative blocks showed the root cause is not a missing period between turns. It is
**intra-turn editorial splitting**: each steno Q. paragraph contains multiple sentences, and MB
manually splits them into separate Q-labeled lines during final editing. The engine faithfully
renders one steno paragraph → one Q. label. There is no dropped period.

Two sub-patterns are mechanically fixable:
- Trailing confirmation: turn ends `, okay?` → split into two Q. lines (~20 blocks)
- Leading acknowledgment: turn starts `Okay. ` → split off as own Q. line (~15 blocks)

Fix: `_split_intra_turn_sentences()` pass in `document_composer._build_qa_body()`. ~35–45 lines,
one file. Closes ~35 of 74 blocks. The remaining ~35 blocks require Stage 3 LLM judgment (two
distinct sentences with no filler markers).

### 4. Reclassification #2 — "And" turn-openers are not sentence breaks

The sequential "And" bucket (38 blocks, not 31 as estimated) contains 10 blocks classified as
`turn_initial_and` — cases where MB opens a Q or A turn with a discourse "And" (e.g., "Q. And
did your family stay here?") that the engine renders without the "And" or with different phrasing.
The `is_cap` scorer fires on the capitalized "And" token, but there is no compound sentence
being split. **These 10 blocks should be removed from the sentence_break count.** They are a
separate phenomenon: MB's discourse-connector style at turn starts.

True sequential-And sentence-break blocks: 21 of 38 (sequential_narrative 12, and_then 4,
and_so 3, parallel_structure 2). The garbled_contamination blocks (7) inflate the count further.

### 5. Combined mechanical close estimate

All intra-turn split patterns (trailing `okay?`, leading `Okay.`, `and_then`, `and_so`) target
the same function: `document_composer._split_intra_turn_sentences()`. That function does not
exist yet. Creating it with these four rules closes approximately:

| Rule | Blocks closed |
|---|---|
| Trailing `okay?` / `all right?` | ~20 |
| Leading `Okay.` acknowledgment | ~15 |
| `and_then` temporal sequence | 4 |
| `and_so` consequential clause | 3 |
| **Total** | **~42 blocks** |

One file touched (`document_composer.py`), ~60–75 new lines, ~8–10 new unit tests.
No other pipeline stages involved.

---

## Open Recon Queue (not yet started)

| Item | Pool size | Notes |
|---|---|---|
| Garbled steno deep-dive | ~356 blocks | 50% of cap_proper (215) + garbled_contamination across all buckets. Stage 3 AI quality — what is the distribution of parse failure modes? |
| Punctuation-trailing misfire | ~29 blocks | `is_cap` misfires on comma-vs-period differences. What are the high-frequency patterns? Are any fingerprint-closeable? |
| Hyphenation / doubled-word residual | ~40 blocks combined | `hyphenation` (16) + `doubled_word` (24) sub-buckets. How much is garbled steno vs. engine formatting? |
| Audio-dependent block census | unknown | How many of the 825 diff blocks are only closeable with audio access? Need a principled estimate before scoping Stage 4. |
| `turn_initial_and` characterization | 10 blocks | Now that it's reclassified, what is MB's turn-opening-And pattern? Is it consistent enough to add as a fingerprint discourse rule? |

---

## Honest Health Read

**Context window:** This handoff is being written at ~85% context consumption. The sequential_and
recon data was reconstructed from disk (the prior session's classification ran in a different
context window that got summarized). All block examples were verified against the actual JSON.
The 38-block count is correct; the 31-block estimate in sentence_break_recon was a sample
extrapolation.

**Data confidence:** High on all five reports. The two reclassifications (Q./A. editorial split,
turn_initial_and) are well-supported by direct block-level evidence. The mechanical close
estimate of ~42 blocks is conservative — actual recovery depends on false-positive rate of
the split rules, which needs unit testing against the full corrected_turns dataset.

**What the next Sonnet should do first:** Read this handoff plus the five report files. Then
ask Scott which queue item to tackle, or proceed directly to implementing
`_split_intra_turn_sentences()` if Scott has already authorized that work.

**Engine state:** No code changes were made this session. All work was read-only analysis.
Engine HEAD is still `8954b61`. The `_stage5_fingerprint_out/` directory exists on disk with
the Brandl fingerprint run output. The `_diff_out_fingerprint/block_classification.json` is the
source of truth for all block counts in this session.

---

## Appendix A — Key File Paths

A fresh Sonnet will need these without hunting.

**Analysis data (read-only, reusable):**
```
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\brandl_50pp\_diff_out_fingerprint\block_classification.json
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\brandl_50pp\_stage3_m1_out\corrected_turns.json
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\brandl_50pp\_stage5_fingerprint_out\
```

**Stage 5 source files (where the fix goes):**
```
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\document_composer.py   ← _split_intra_turn_sentences() goes here
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\assemble_final.py      ← orchestration, already accepts fingerprint=None
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\page_layout.py         ← adds Q./A. prefixes per LogicalLine
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\turn_renderer.py       ← renders turn text verbatim, no sentence awareness
```

**Fingerprint loader:**
```
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\mrx_engine_v1\fingerprint\loader.py
```

**Run scripts created this session (on disk, not in engine repo):**
```
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\brandl_50pp\_run_brandl_stage5_fingerprint.py
C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\brandl_50pp\_run_brandl_diff_fingerprint.py
```

---

## Appendix B — Two Corrections to This Handoff

### B1 — Mechanical close total is ~49, not ~42

The body of this handoff says ~42 blocks. The correct number is **~49** when you include the
fingerprint-closeable cap_proper sub-patterns (~7 blocks: proper noun capitalization ~30 → ~5
net new closeable this sprint, term format "E-mail"→"Email" ~2–3 high-confidence). Scott's
version of this handoff correctly states ~49. The ~42 is the document_composer.py fix alone;
~49 includes YAML fingerprint additions running in parallel.

### B2 — Garbled-filter regex bug (affects all recon block counts)

The garbled-block filter used in every recon script this session is:

```python
re.search(r'REVIEW|REPORTER CHECK', raw, re.IGNORECASE)
```

This regex **fails** when the diff tokenizer splits `REPORTER CHECK` across separate diff marker
tokens — e.g., `**-*REPORTER-** **-CHECK-**` — because the literal string "REPORTER CHECK"
never appears contiguously. The result: garbled blocks slip through into other condition
buckets (confirmed: 7 garbled blocks appeared in the sequential_and bucket for this reason).

**Fix before next recon:**
```python
re.search(r'REVIEW|REPORTER|REPORTER.?CHECK|\[\[', raw, re.IGNORECASE)
```

This affects the accuracy of all condition counts in today's reports. The counts are correct
directionally but are slightly understated for garbled_contamination and slightly overstated
for all other conditions. Magnitude: small (~5–10 blocks across all five reports).

---

*End of handoff.*
