# SPEC — Stage A: Aligner + Differ (v0)
Date: 2026-05-13 evening
Architect: Opus
Builder: Sonnet
Owner: Scott

AMENDMENT 01 (2026-05-13 evening): Path correction applied. FINAL files live in oracle/ subfolders of mrx_depo_library packages, not input/. Church RAW is .txt not .rtf — normalizer handles both. Input table below is corrected from recon findings.

## Universal? NO — MB-specific output for now (tool itself is universal-ready)
## Code or prompt? CODE
## Commit prefix: mb-specific:

## File location:
- Tool code: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\aligner_differ\
  - __init__.py
  - normalize.py
  - tokenize.py
  - align.py
  - diff.py
  - categorize.py
  - frequency.py
  - run_stage_a.py (entry point)
- Tests: C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\tests\aligner_differ\
- Output: C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\
  - mb_frequency_summary.json
  - mb_evidence_raw.json

---

## PRIME DIRECTIVE CHECK

Could this reduce transcript accuracy or credibility?
- Accuracy: NO. Tool only READS RAW + FINAL pairs and writes a frequency report. Does not modify any transcript.
- Credibility: NO. Output is data, not a transcript change. Safe by design.

Safe to proceed.

---

## NORTH STAR

The tool is DETERMINISTIC. No AI in the diff loop. We are NOT asking a model to judge anything during this stage. We are counting MB's habits.

Product belief Scott named 2026-05-13 evening:
> "If MB does it 97 out of 100 times, on depo #101 the engine should do it for her."

Stage A produces the COUNTS. A separate later pass (with Scott in the loop) decides which counts get written into MB.yaml.

Frequency tiers (informational, not enforced by this tool):
| Frequency        | Engine behavior later        |
| ---------------- | ---------------------------- |
| 100% (all depos) | Auto-apply, no flag          |
| 90–99%           | Auto-apply, log to PoW       |
| 70–89%           | Suggest, flag for review     |
| <70%             | Don't act. Not enough signal |

---

## INPUT — THE 4 PAIRS (CORRECTED)

| # | Depo | RAW path | FINAL path |
|---|---|---|---|
| 1 | halprin_040226 | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\input\040226yellowrock-ROUGH_Tsmd.rtf | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\oracle\040226yellowrock-FINAL.txt |
| 2 | easley_031326 | C:\Cat4\usr\scott\031326yellowrock-ROUGH_T.rtf | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\easley_031326\oracle\Easley_YellowRock_FINAL_TRANSCRIPT.txt |
| 3 | brandl_032626 | C:\Users\scott\Downloads\depofiles\032626YELLOWROCK TO SCOTT\032626YELLOWROCK_smd_T.rtf | C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\brandl_032626\oracle\BRANDL_MB_FINAL.txt |
| 4 | church_073124 | C:\Cat4\usr\scott\073124CHURCH-ROUGH.txt | C:\Cat4\usr\scott\073124church3-FINAL.txt |

Tool must accept N pairs via a config or argument — do NOT hardcode 4.

---

## PIPELINE — 6 STEPS

### STEP 1 — NORMALIZE
For each file (RAW or FINAL):
- If .rtf: convert to plain text using Python `striprtf` library (pip install striprtf if needed)
- If .txt: read directly, no RTF strip
- Normalize line endings to \n
- Preserve all whitespace within lines (do NOT collapse multiple spaces — those are MB's choices)
- Preserve case (do NOT lowercase — case is a fingerprint signal)
- Keep ALL punctuation
- Output cache file: C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\cache\<depo_id>_<raw|final>.txt
- Cache so we don't re-normalize on every run

### STEP 2 — TOKENIZE (WORD-LEVEL)
For each normalized file, produce a list of tokens. Token types:
- Word (alphanumeric run including apostrophes and internal hyphens, e.g., "don't", "co-counsel")
- Punctuation (one char: . , ; : ? ! " ' ( ) — and any others encountered)
- Number (digit run, including decimals)
- Whitespace (one token per run, encoding what kind: " ", "\n", "\t", "  ")
- Line break ("\n" as its own token)

Each token gets a position index (0-based offset in token stream).

### STEP 3 — ALIGN
Use word-level diff via Python `difflib.SequenceMatcher` (or `diff-match-patch` if needed for performance). Output is a list of ops:
- `equal` — RAW token N matches FINAL token M
- `replace` — RAW token N became FINAL token M
- `delete` — RAW token N was removed
- `insert` — FINAL token M was added

### STEP 4 — DIFF (record every change)
For every non-`equal` op, record a diff event with:
- `depo_id` (e.g., "halprin_040226")
- `op_type` ("replace" / "delete" / "insert")
- `raw_token` (original, or null for insert)
- `final_token` (new, or null for delete)
- `raw_position`
- `final_position`
- `context_before` (last 5 raw tokens before this op)
- `context_after` (next 5 raw tokens after this op)

Write every diff event to mb_evidence_raw.json — one record per event.

### STEP 5 — CATEGORIZE
Deterministic rules — no AI:

| Category | Detection rule |
|---|---|
| `capitalization_only` | RAW and FINAL tokens differ ONLY in case |
| `abbreviation_expansion` | known long<->short pairs (see ABBREVIATION_MAP below) |
| `punctuation_added` | insert of a punctuation token |
| `punctuation_removed` | delete of a punctuation token |
| `punctuation_changed` | replace where both are punctuation |
| `em_dash_inserted` | insert of "--" or "—" |
| `em_dash_removed` | delete of "--" or "—" |
| `filler_word_removed` | delete of: uh, um, er, ah, "like" standalone, "you know" multi-token |
| `word_substitution` | replace where both are words and not in any other category |
| `whitespace_changed` | both whitespace but different (e.g., single space -> double after period) |
| `line_break_changed` | insert/delete/replace of \n |
| `number_normalization` | both numbers, formatted differently ("twenty-five" -> "25") |
| `proper_noun_change` | word substitution where both start with capital letter |
| `other` | anything not matching above |

ABBREVIATION_MAP:
- mister <-> Mr.
- missus <-> Mrs.
- doctor <-> Dr.
- versus <-> vs.
- and <-> &

### STEP 6 — FREQUENCY ROLL-UP
Group categorized diffs by (category, raw_token, final_token). For each unique pattern, count:
- `total_occurrences` (across all depos)
- `depos_seen_in` (unique depo count)
- `pct_of_depos` (depos_seen_in / total_depos)
- `examples` (up to 3 verbatim context snippets, one per depo)

Sort by `pct_of_depos` DESC, then `total_occurrences` DESC.

Output mb_frequency_summary.json:
```json
{
  "stage_a_version": "v0",
  "generated_at": "<ISO timestamp>",
  "total_depos_analyzed": 4,
  "total_diff_events": "<int>",
  "depo_ids": ["halprin_040226", "easley_031326", "brandl_032626", "church_073124"],
  "patterns": [
    {
      "category": "em_dash_inserted",
      "raw_token": null,
      "final_token": "--",
      "total_occurrences": "<int>",
      "depos_seen_in": "<int>",
      "pct_of_depos": "<float>",
      "examples": ["..."]
    }
  ]
}
```

---

## TESTS

Unit tests (tests/aligner_differ/):
1. test_normalize_strips_rtf — tiny known .rtf -> plain text
2. test_tokenize_words — "Hello, world." -> 4 tokens
3. test_align_simple — RAW "the cat sat" / FINAL "the big cat sat" -> one insert op
4. test_categorize_em_dash_insert — "--" insert lands in em_dash_inserted bucket
5. test_categorize_capitalization — "exhibit" -> "Exhibit" lands in capitalization_only
6. test_frequency_rollup — 3 fake diff events of same pattern roll up to 1 pattern with count 3

Integration test:
7. test_full_pipeline_halprin_only — full pipeline on Halprin alone, verify JSON structure + em-dash pattern present

DO NOT test against MB's expected values for the 4-depo run. The run IS the test.

---

## ROLLOUT

Branch: feature/stage-a-aligner-differ-v0 off main
Backup: backup/pre-stage-a-2026-05-13 off main first

1. RECON gate completed — paths confirmed per recon report 2026-05-13 evening.
2. Build incrementally: normalize -> tokenize -> align -> diff -> categorize -> frequency. Test each.
3. 30-min wall on each sub-step.
4. Run full pipeline on the 4 pairs.
5. Output two JSON files.
6. Sonnet reports: top 20 patterns by pct_of_depos, total diff events count, any errors.
7. Scott eyeballs output.
8. NO commits until Scott approves.

---

## SHAPE MATCH ONLY — APPLIED

Not byte-matching any fixture. Frequency table is what it is. Don't tune the categorizer to produce a pre-imagined result. Surprises are real findings, not bugs.

---

## RULE-INPUT-IS-SACRED

Tool only READS. Writes output to fingerprints/stage_a/. NEVER modifies any RAW or FINAL transcript.

---

## SHIP CRITERIA

Done when:
1. All 4 pairs process without error
2. mb_evidence_raw.json contains every diff event
3. mb_frequency_summary.json shows patterns sorted by pct_of_depos
4. Em-dash absence pattern is detectable (sanity check)
5. Scott eyeballs top 20 and confirms reasonable

---

## OPEN ITEMS — SCOTT SIGNED OFF 2026-05-13 EVENING

1. 4-pair input acceptable — YES
2. Word-level tokenization — YES
3. Two-file output (summary + raw evidence) — YES
4. Sonnet confirms filenames via recon before build — DONE
5. No commits until Scott eyeballs output — YES

— End of Stage A v0 spec —
