# SONNET HANDOFF — Sunday 2026-05-03 evening

To: Fresh Sonnet, Sunday evening session
From: Sonnet, Sunday afternoon session
Owner: Scott

## Read before doing anything

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-03_EVENING.md ← read this so you know what Opus was told
4. This handoff in full

After reading: confirm in ONE LINE: "Ramped Sunday evening. Ready."
Then wait for Opus to assign the first task. Do NOT start coding unprompted.

## What shipped today (you built all three)

1. **D-COMPOSER-SILENT-TRUNCATE** — engine commit `1c601fd` (morning)
2. **D-DOUBLED-WORD** — engine commit `ff1fc17` (midday)
   - 35 real engine doubles fixed, 14 new tests
3. **D-WRITER-WORD-DROP validator** — engine commits `2df5dce` + `db3dff8` (afternoon)
   - `src/mrx_engine_v1/validate_ops/word_preservation.py` — validator logic
   - `src/stage5/assemble_final.py` — Stage 5 integration via `word_preservation_rejections_path`
   - 194 silent word-drop proposals now blocked
   - 582+ regression tests still passing

## Critical technical context you must hold

### word_preservation.py — the validator

Two gates before flagging a proposal as a word drop:
- **Rule 1**: `if len(before_words) <= 1: return None` — single-word before = pure substitution, skip
- **Majority threshold**: `if accounted_count / len(before_words) < 0.5: return None` — skip if fewer than 50% of before-words are accounted for in after (avoids false positives on rewrites)

### assemble_final.py — Stage 5 integration

New optional param: `word_preservation_rejections_path: Path | None = None`

Loads `_word_preservation_rejections.jsonl`, builds `rejected_keys: set[tuple]` of
`(turn_idx, proposal_id)` pairs, then patches the decisions list in-memory:

```python
decisions = [
    dict(d, outcome="word_preservation_rejected")
    if (proposals[i].get("turn_idx"), d.get("proposal_id")) in rejected_keys
    else d
    for i, d in enumerate(decisions)
]
```

**Critical**: composite key `(turn_idx, proposal_id)` is required — `proposal_id` alone
is not globally unique (values like `p_0001` repeat ~60x across batches).

### The new scoreboard (not the diff count)

The raw diff count (740) is NOT the engine bug count. True picture:

| Bucket | Name | Count | % |
|--------|------|-------|---|
| A | Engine bug | 161 | 22% |
| B | MB editorial addition | 518 | 70% |
| C | Validator-protected | ~50 | ~7% |
| D | Unknown | 61 | 8% |

Bucket B (em_dash 264, cap_proper 191, quote_marks 62) will NOT close until
Aligner+Differ ships. Do not treat 740 as the score.

### OUR_FINAL versioning

- v3 = post-word-preservation render, 491KB — stays LOCAL, gitignored
- `_run_halprin_full_stage5.py` — gitignored runner that passes rejections path

## Afternoon bugs you fixed — know these cold

### Proposal ID collision (fatal bug, fixed)
First attempt used only `proposal_id` for matching. Result: 965/981 proposals
incorrectly rejected (REWORD applied: 5 instead of ~350). Fix: composite key
`(turn_idx, proposal_id)`. Correct output: REWORD 351, FLAG 436, Rejected 194.

### classifier_blocks.py classification bugs (analysis only, not engine)
- Bucket 3 (steno fragment) initially caught real English words ("in", "of", "a")
  due to 2-char threshold. Fixed with `REAL_SHORT` set.
- B2 (phonetic) count collapsed to 1 when T9-pattern detection had priority.
  Fixed by giving phonetic detection priority.

## Your standing rules — non-negotiable

- **Never commit or push independently** — Scott does all commits and pushes
- **Halprin OUR_FINAL files NEVER go to the public repo** — gitignore enforces, verify before any push
- **Spot-check before every spec** — Opus leads this, you build
- **Rule sheet header on every spec** — Universal/MB-specific? Code/Prompt? location? prefix?
- **Full absolute paths** always
- **Code-fenced blocks** for any content Scott copies between AIs
- **Never go silent** — ping at every logical break or every 10 min
- Plain English, 12-year-old reading level, ONE question at a time, short answers

## What Opus will likely assign this evening

Pick from Bucket A targets (Opus decides which):

| Priority | Sub-category | Count |
|----------|-------------|-------|
| 1 | hyphenation | 41 |
| 2 | phonetic_error | 28 |
| 3 | doubled_word (residual) | 28 |
| 4 | word_drop (residual) | 17 |
| 5 | acronym_mangle | 17 |
| 6 | objection_style | 12 |
| 7 | pronoun_swap | 10 |
| 8 | number_style | 8 |

Pattern: spot-check (Opus leads, 15 min) → spec (Opus writes) → build (you) →
verification (you, BEFORE push) → Opus reviews → Scott pushes.

**Hyphenation note**: spot-check carefully before speccing. Some hyphenation diffs
were tag-span artifacts killed by the word-drop validator. Confirm what remains
is real engine bugs before writing a line of code.

## Reports committed today (mrx-context repo)

- `reports/2026-05-03/word_drop_rejection_classification.md` — commit `bf394ce`
  194 rejections: B1=160 context leaks, B2=19 phonetic corrections, B4=15 unclear
- `reports/2026-05-03/halprin_full_scoreboard_v1.md` — commit `b41b7e7`
  740-block diff scoreboard with full D-block verbatim list
- `handoffs/HANDOFF_OPUS_2026-05-03_EVENING.md` — commit `c54176c`

## Classifier source (local only, gitignored)

`io/analysis/halprin_full/classify_blocks.py` — 740-block heuristic classifier
`io/analysis/halprin_full/_diff_out/block_classification.json` — output

## Scott's state at handoff

Dinner break. 11+ hours today. Calm, methodical, on a roll. He shipped 3
universal fixes today and wants to keep the streak. Walk in calm, don't
fire-hose, let Opus drive the pace.

— End of Sonnet evening ramp —
