# Q./A. Turn-Boundary Period Bug — Recon
**Date:** 2026-05-09
**Based on:** `_diff_out_fingerprint/block_classification.json`, `_stage3_m1_out/corrected_turns.json`, source audit of `assemble_final.py`, `document_composer.py`, `page_layout.py`, `turn_renderer.py`

---

## Headline

**Root cause: intra-turn editorial splitting, not a period-insertion bug. MB manually separates multi-sentence Q. steno paragraphs into individual Q. labeled lines during final editing. The engine renders each steno turn as one Q. block — correctly. No period is dropped. The sentence boundary never existed in the steno. Fix size: ~30–50 lines in document_composer.py for the two high-confidence mechanical patterns (trailing "okay?", leading "Okay."). The general case requires Stage 3 judgment — not addressable in Stage 5.**

---

## Part 1: Five Broken Blocks — Raw Evidence

### Block #19 (turn 175)

```
corrected_turn 175 [s1]:
  "Last is if at any time today you don't understand my question,
   please ask me to rephrase it is that okay?"

Engine output:
  Q.    Last is if at any time today you don't understand my
        question, please ask me to rephrase it is that okay?

MB FINAL:
  Q.    Last is, if at any time today you don't understand my
        question, please ask me to rephrase it.
  Q.    Is that okay?

Drop point: The steno turn has ONE Q. paragraph containing
two sentences. Engine renders as one Q. line. MB splits at
"rephrase it." and gives "Is that okay?" its own Q. label.
```

### Block #32 (turn 234)

```
corrected_turn 234 [s1]:
  "Okay.  Did you hold any position other than area engineer
   while you were at Conoco?"

Engine output:
  Q.    Okay.  Did you hold any position other than area engineer
        while you were at Conoco?

MB FINAL:
  Q.    Okay.
  Q.    Did you hold any position other than area engineer while
        you were at Conoco?

Drop point: The steno turn has ONE Q. paragraph starting with
"Okay." acknowledgment then the real question. Engine renders
as one Q. line. MB splits "Okay." to its own Q. label.
```

### Block #64 (turn 350)

```
corrected_turn 350 [s1]:
  "Trust me, that understanding is going to make things a lot
   smoother as we start talking about Sulphur Mines, okay?"

Engine output:
  Q.    Trust me, that understanding is going to make things a
        lot smoother as we start talking about Sulphur Mines,
        okay?

MB FINAL:
  Q.    Trust me, that understanding is going to make things a
        lot smoother as we start talking about Sulphur Mines.
  Q.    Okay?

Drop point: The steno turn ends with ", okay?" as a trailing
confirmation. Engine renders as one Q. line. MB separates
"okay?" as its own Q. turn with a period replacing the comma.
```

### Block #122 (turn 552)

```
corrected_turn 552 [s1]:
  "And okay.  And how long were you there?"

Engine output:
  Q.    And okay.  And how long were you there?

MB FINAL:
  Q.    Okay.
  Q.    And how long were you there?

Drop point: Steno has garbled "And okay." filler. MB normalizes
to "Okay." and splits it from the real question as own Q.
```

### Block #134 (turn 602)

```
corrected_turn 602 [s1]:
  "I should have asked this, sir, earlier so let's just briefly
   divert.  How are you currently employed?"

Engine output:
  Q.    I should have asked this, sir, earlier so let's just
        briefly divert.  How are you currently employed?

MB FINAL:
  Q.    I should have asked this, sir, earlier, so let's just
        briefly divert.
  Q.    How are you currently employed?

Drop point: Two distinct sentences in one Q. steno paragraph.
Engine renders as one Q. line. MB gives each sentence its own
Q. label.
```

---

## Part 2: Code Path Trace

### The full path from turn to output line

```
corrected_turns.json (one dict per steno paragraph)
    ↓
document_composer._build_qa_body()           [document_composer.py:361–393]
    → for each turn in qa_start..qa_end:
        kind = _STYLE_TO_KIND[turn["paragraph_style"]]
            s1 → LineKind.QA_Q
            s3 → LineKind.QA_A
        rendered = render_turn(turn, entries)
        LogicalLine(text=rendered.rendered_text,
                    kind=kind, ...)            ← ONE LogicalLine per turn
    ↓
page_layout._wrap_line()                     [page_layout.py:139–240]
    → if line.kind == LineKind.QA_Q:
        prefix = "Q.    "                     ← Q. prepended here, once per turn
    → wraps text to PAGE_WIDTH, emits _PhysicalLine objects
    ↓
OUR_FINAL.txt written
```

### Where sentence termination is (or isn't) enforced

**It isn't.** There is no code anywhere in Stages 5, 6, or 7 that:
- Looks at whether a Q. turn text contains multiple sentences
- Splits a multi-sentence Q. turn into multiple Q.-labeled lines
- Inserts a period before a second sentence in the same Q. turn

`render_turn()` returns `turn["text"]` verbatim (with REWORD/FLAG markers applied). It has no sentence-awareness.

`_build_qa_body()` creates exactly one `LogicalLine` per corrected turn. No subdivision.

`_wrap_line()` adds `"Q.    "` once at the start of the first physical line, then wraps the remaining text. It never re-examines the text for sentence boundaries.

### Why it works for some turns and not others

It works exactly as designed for every single turn — the bug isn't intermittent. MB's FINAL matches the engine for Q. turns that contain only one sentence. The engine "fails" only where MB edits her final to split a multi-sentence Q. turn into multiple Q. paragraphs, because that editorial decision has no representation in the steno or in the corrected_turns.

### Common upstream condition

All five examples share the same condition: **one `s1` (Q.) steno paragraph containing more than one sentence**. Three sub-patterns observed:

| Sub-pattern | Example | Count in 74-block pool (est.) |
|---|---|---|
| Trailing confirmation: turn ends `, okay?` or `, all right?` | Block #64 | ~20 |
| Leading acknowledgment: turn starts `Okay. ` or `Okay, ` | Block #32, #122 | ~15 |
| Two-sentence Q. (neither filler): real question + follow-up | Block #19, #134 | ~35 |
| Other / mixed | — | ~4 |

---

## Part 3: Bug Classification

### What this is NOT

- **Not a missing-period bug.** No period is dropped. The period doesn't exist in the steno turn at all.
- **Not an assemble_final.py issue.** `assemble_final` correctly delegates to `compose_document`.
- **Not a turn-boundary issue.** The problem is WITHIN a single turn, not between adjacent turns.
- **Not a one-line fix anywhere in the Stage 5 pipeline.**

### What this IS

**Intra-turn editorial splitting.** MB's editing process includes a step where she manually divides Q. paragraphs that contain multiple sentences into separate Q. lines in her final. The steno machine wrote one RTF paragraph; MB's FINAL has two. The engine faithfully renders what the steno gave it (one paragraph → one Q. line).

The 74 blocks categorized as "Q./A. turn boundary" in the sentence_break_recon are therefore miscounted — they're not boundary issues, they're intra-turn splits. The 74-block category remains real and closeable, just via a different mechanism than originally suspected.

### Fix options by sub-pattern

**Sub-pattern A — Trailing "okay?" / "all right?" (est. ~20 blocks)**

Mechanical. Detectable without audio. Rule: if a Q. turn text ends with `, okay?` or `, all right?` (comma + confirmation question), split at the comma: first part ends with period, second part ("Okay?" / "All right?") becomes its own Q. label.

Fix location: new `_split_intra_turn_sentences()` pass in `document_composer._build_qa_body()`, called before `LogicalLine` creation. ~20–30 lines.

**Sub-pattern B — Leading acknowledgment "Okay." (est. ~15 blocks)**

Mechanical. Rule: if a Q. turn text starts with `Okay.` or `Okay,` followed by a real question, split: "Okay." becomes own Q. label, remainder is a new Q. label.

Same fix location as A. ~10–15 additional lines.

**Together A+B: ~35 of 74 blocks, ~50% mechanical coverage. Files touched: 1 (document_composer.py). Tests needed: ~6–8 new unit tests.**

**Sub-pattern C — Two-sentence Q. with no filler markers (est. ~35 blocks)**

Not mechanical. MB's judgment about where one question ends and the next begins within a single steno paragraph cannot be reliably detected by pattern matching. Would require:
- Stage 3: Writer emits turn-split proposals ("split this Q. at position N") — architectural change, multiple files, LLM calls
- Or: a trained sentence-boundary classifier applied post-render

This is the correct next-level problem to surface to Opus for architectural decision.

---

## Summary for Opus

| Finding | Value |
|---|---|
| Root cause class | Intra-turn editorial splitting |
| Code location | No bug in Stage 5 — missing capability |
| Lines of code to fix mechanical patterns (A+B) | ~35–45 lines in document_composer.py |
| Files touched (mechanical fix) | 1 (document_composer.py) + test file |
| Blocks closed by mechanical fix | ~35 of 74 (~47%) |
| Remaining blocks requiring Stage 3 / LLM | ~35 of 74 (~53%) |
| Fingerprint-closeable? | No — structural rule, not token rule |
| Scope | Universal (not MB-specific — Q. splitting is a general depo convention) |

---

*End of report.*
