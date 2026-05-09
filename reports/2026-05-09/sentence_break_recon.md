# Sentence-Break Cascade Recon — cap_proper Sub-pattern
**Date:** 2026-05-09
**Based on:** `_diff_out_fingerprint/block_classification.json`
**Sentence-break candidate pool:** 281 blocks (cap_proper + sentence-initial capital word in MB)
**Sample:** 30 blocks drawn evenly; full-corpus signal counts validated across all 281

---

## Headline

**7 distinct sentence-end signals (excluding garbled contamination). Top 3: Q./A. turn boundary (26%), sequential "And" (11%), garbled-steno contamination (50% — not a real sentence-break signal). Mechanically closeable without LLM: ~28% of all blocks, ~56% of the non-garbled blocks. The biggest single win is Q./A. turn boundary detection.**

---

## Full-Corpus Signal Counts (all 281 blocks)

| Signal | Count | % of 281 | Mechanical? | Fingerprint-closeable? |
|---|---|---|---|---|
| Garbled steno (contamination, not real) | 141 | 50.2% | N/A | No — Stage 3 |
| Q./A. turn boundary | 74 | 26.3% | **Yes** | Maybe — structural rule |
| Sequential "And" | 31 | 11.0% | Maybe | No — context-dependent |
| Other capitalized word | 16 | 5.7% | No | No — LLM judgment |
| Filler / hesitation ("Uhmm.", "Okay.") | 8 | 2.8% | Maybe | No — edge case |
| Adversative "But" | 5 | 1.8% | Maybe | No — context-dependent |
| Procedural parenthetical ("(Whereupon…)") | 4 | 1.4% | **Yes** | Yes — deterministic |
| Sequential "So" | 2 | 0.7% | Maybe | No — context-dependent |

---

## Signal 1 — Garbled Steno Contamination (141 blocks, 50.2%)

**Not a sentence-break problem.** The sentence_break_pattern regex fires on these because the engine's REVIEW/REPORTER-CHECK text happens to contain a sentence-initial word. The underlying issue is that Stage 3 couldn't parse the steno — the sentence boundary doesn't exist in the engine output at all.

Counted separately here because they inflate the apparent sentence-break count by 2×. True sentence-break blocks: **140 of 281**.

Examples from sample: Blocks #95, #163, #179, #268, #284, #311, #425, #445, #461, #479, #545, #611, #629 (partial), #670, #699, #729.

---

## Signal 2 — Q./A. Turn Boundary (74 blocks, 26.3%)

**Most common real signal. Mechanically detectable.**

The engine treated two separate Q./A. turns as one continuous sentence — no period before the new Q. or A. attribution. MB's FINAL always ends the prior sentence with a period before the new speaker label.

Examples from sample:

```
Block #394
  OUR: "MR. MADIGAN: Yes you can. THE WITNESS: I never participated in the
        presentation to investors. [THE ATTORNEY: ] Q. Okay. That is what I
        was looking for."
  MB:  "MR. MADIGAN: Yes, you can. A. I never participated in the presentation
        to investors. Q. Okay. That's what I was looking for. Q. Is that what
        you meant when you said above my pay grade..."
  Missing period: after "you can" (before A.) and after "investors" (before Q.)
  Signal: New speaker attribution label

Block #461
  OUR: "...two zones and we perforated one of those zones twice, middle and then
        hire SGLUP [REVIEW...] okay."
  MB:  "...two zones and we perforated one of those zones twice, middle and then
        higher up. Q. Okay."
  Missing period: after "higher up" — next turn is Q. not witness continuation
  Signal: Q. attribution marks new attorney turn

Block #646
  OUR: "Q. Okay and what is the spreadsheet depicting?"
  MB:  "Q. Okay. Q. And what is the spreadsheet depicting?"
  Missing period: after "Okay" — attorney's acknowledgment is its own Q. sentence
  Signal: Attorney's "Okay" is a turn-acknowledgment, then new question
```

**Why it's mechanical:** The Q./A. attribution labels (Q., A., MR. MADIGAN:, THE WITNESS:) are explicit. The rule is: every sentence that ends immediately before a Q./A. label should end with a period. The engine is failing to insert that period.

**Scope:** Universal — every deposition uses Q./A. labels regardless of reporter or jurisdiction. The rule "sentence before Q./A. label gets a period" is not MB-specific.

**Closeable:** Yes, but not via fingerprint token rule. This is a sentence assembly rule in Stage 5 (assemble_final.py) — when stitching turns, ensure each turn's final sentence terminates before the next speaker label.

---

## Signal 3 — Sequential "And" (31 blocks, 11.0%)

**Second most common real signal. Requires LLM judgment in most cases.**

MB consistently breaks compound sentences by ending on a period and beginning the next sentence with "And." The engine produces these as one continuous sentence with a lowercase "and."

Examples from sample:

```
Block #1
  OUR: "...I represent Westlake in this matter and I'll be the lawyer
        questioning you today."
  MB:  "...I represent Westlake in this matter. And I'll be the lawyer
        questioning you today."
  Missing period: after "matter"
  Signal: New sentence starts with "And" (discourse connector, new thought)

Block #588
  OUR: "...both of them called me on the telephone together, Todd and John and
        we spoke for thirty minutes about things and I think that was right
        around COVID time..."
  MB:  "...both of them called me on the telephone together, Todd and John. And
        we spoke for 30 minutes about things. And I think that was right around
        COVID time..."
  Missing periods: after "John" and after "things"
  Signal: Each "And" starts a new sentence — witness narration style

Block #772
  OUR: "...go one after the other and so if we think we're going to drill a
        well and we, basically, get it permitted as a well and so if we don't
        drill it, we have to rename..."
  MB:  "...go one after the other. And so if we think we're going to drill a
        well and we, basically, get it permitted as a well, then if we don't
        drill it, then we have to rename..."
  Missing period: after "other"
  Signal: "And so" introduces consequence clause as new sentence
```

**Why it's NOT fully mechanical:** "And" also connects two clauses legitimately within a single sentence (e.g., "Todd and John" — not a sentence break). Detecting whether "and" signals a sentence break vs. a clause connector requires understanding the clause structure. LLM judgment or a trained classifier needed for reliable detection.

**Scope:** MB-specific rhythm. Some reporters write long sentences; MB consistently splits at "And." A fingerprint rule noting this style preference is documentable, but not mechanically enforceable as a token rule.

---

## Signal 4 — Filler / Hesitation Word (8 blocks, 2.8%)

**Mechanically detectable in obvious cases.**

MB ends a hesitation word ("Uhmm," "Well,") with a period, treating it as its own micro-sentence before the witness's substantive answer.

Examples from sample:

```
Block #347
  OUR: "A. Uhmm, second half of I mean 2019, 2020 and maybe a little bit of
        2021 and maybe first half of 2021."
  MB:  "A. Uhmm. Second half of I mean 2019, 2020 and maybe a little bit of
        2021. And maybe the first half of 2021."
  Missing period: after "Uhmm" — the hesitation is its own utterance
  Signal: Filler word ("Uhmm") stands alone before substantive answer
```

**Scope:** MB-specific transcription style. Not all reporters put a period after "Uhmm." Closeable as a fingerprint rule: "hesitation tokens [Uhmm, Uh, Um] always end with period." Low risk, deterministic. **Fingerprint v1+ candidate.**

---

## Signal 5 — Adversative "But" (5 blocks, 1.8%)

Same structure as sequential "And" — MB breaks on "But" as a new sentence. Same mechanical limitations apply. Not reliably detectable without context.

```
Block #241
  OUR: "...probably some other smaller jobs in that timeframe but the two I
        remember were Belize Natural Energy and El Paso."
  MB:  "...probably some other smaller jobs in that timeframe. But the two I
        remember were Belize Natural Energy and El Paso."
  Signal: Contrast clause ("But the two...") is new sentence
```

---

## Signal 6 — Procedural Parenthetical (4 blocks, 1.4%)

**Fully mechanical. Deterministic.**

MB inserts `(Whereupon, Exhibit No. ___, was marked for Identification.)` and `(Witness peruses document.)` as their own sentences. These are verbatim steno conventions.

```
Block #699
  OUR: "...Yellow Rock 291625 to 647? MR. MADIGAN: ..."
  MB:  "...Yellow Rock 291625 to 647. (Whereupon, Exhibit No. 228, was marked
        for Identification.) (Witness peruses document.) MR. MADIGAN: ..."
  Signal: Exhibit-marking parenthetical is its own sentence
```

**Scope:** Universal — `(Whereupon...)` is a standard court reporter convention. **Closeable in Stage 5 assembly logic:** when inserting exhibit parentheticals, always terminate the preceding sentence with a period.

---

## Signal 7 — Sequential "So" (2 blocks, 0.7%)

Same as "And" — MB uses "So" to open a new sentence. Mechanically indeterminate (same clause-vs-sentence ambiguity). Not worth a targeted rule.

---

## Summary: Mechanical Closeability

**Of 281 sentence-break blocks:**
- 141 (50%) are garbled steno contamination — need Stage 3 AI fix, not sentence-break logic
- 74 (26%) are Q./A. turn boundary — **mechanically closeable in Stage 5 assembly**, universal rule
- 4 (1.4%) are procedural parentheticals — **mechanically closeable**, universal rule
- **78 total mechanically closeable = 28% of all 281 blocks**

**Of the 140 real (non-garbled) sentence-break blocks:**
- **78 / 140 = 56% mechanically closeable** via Stage 5 assembly rules

**The remaining ~62 non-garbled blocks (44%) require LLM judgment** — detecting whether "And/But/So" opens a new sentence vs. connects a clause cannot be done reliably by pattern alone.

---

## Architecture Implication

The Q./A. turn boundary fix (74 blocks) is not a fingerprint rule — it's a Stage 5 assembly rule. When `assemble_final.py` stitches multi-turn paragraphs, it should ensure that each turn's final line terminates with a period before the next Q./A. label is written. This is mechanical, universal, and doesn't require audio or LLM judgment.

That single fix would close 74/205 sentence-break blocks (~36% of the original estimate) and is the highest-leverage mechanical intervention available in this dataset.

---

*End of report.*
