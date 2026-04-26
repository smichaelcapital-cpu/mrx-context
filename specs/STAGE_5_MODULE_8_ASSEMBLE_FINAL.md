# STAGE 5 — MODULE 8: assemble_final.py
Status: BUILT — commit ca419fc
Author: Opus, 2026-04-27
Build target: Sonnet
Repo: mrx_engine_v1
Spec path: docs/STAGE_5_MODULE_8_ASSEMBLE_FINAL.md
Mirror to mrx-context: specs/STAGE_5_MODULE_8_ASSEMBLE_FINAL.md

## 1. Purpose
Wire all of Stage 5 together. Load inputs from disk, run the pipeline (Modules 2 → 3 → 6 → 7), write three output files, return a summary. This is the entry point Scott runs from the command line to produce the final document.
This is the orchestration layer described in parent spec §7 (entry point + CLI).

## 2. Non-Goals

- No new logic — every transformation lives in Modules 2–7.
- No new format decisions — Module 7 owns layout, Module 4 owns markers.
- No retry / recovery logic for partial failures.
- No parallelism — single-threaded, sequential.
- No progress bars or live output (deferred to v0.2).
- No validation of output against MB's FINAL — that's a human-eye step.

## 3. Inputs
Six input file paths plus an output directory:

| Param | Type | Source |
|---|---|---|
| corrected_turns_path | Path | Stage 2 output |
| proposals_path | Path | Block H output |
| decisions_path | Path | Block H output |
| anomalies_path | Path | Block H output |
| case_info_path | Path | Hand-built fixture for Halprin |
| output_dir | Path | Where to write outputs (created if missing) |

## 4. Outputs

### 4.1 Three files written to output_dir

| File | Content |
|---|---|
| halprin_mini.OUR_FINAL.txt | The paginated plain-text deposition (from Module 7) |
| halprin_mini.review_queue.json | The review queue with page+line filled in |
| stage5.summary.json | Run statistics |

Filename note: halprin_mini is the deposition stem name. For v0.1, hardcode it to "halprin_mini". v0.2 derives from case_info.deposition.witness or input path. Track in revisit list. Comment with `# HARDCODE-HALPRIN-V01`.

### 4.2 Function return
```python
@dataclass(frozen=True)
class Stage5Summary:
    input_paths: dict[str, str]      # all 5 input paths as strings
    output_paths: dict[str, str]     # all 3 output paths as strings
    case_info_path: str
    duration_sec: float
    totals: Stage5Totals
    warnings: list[str]              # human-readable warnings from any stage
```

```python
@dataclass(frozen=True)
class Stage5Totals:
    turns_rendered: int
    proposals_applied_REWORD: int
    proposals_applied_FLAG: int
    proposals_rejected: int
    review_tags_emitted: dict[str, int]   # {"TAG_TYPE_subtype": N}
    pages_rendered: int
    lines_rendered: int
    skipped_entries_count: int            # from Module 5 / Module 6
    review_entries_orphaned: int          # from Module 7
```

Both in schemas.py.

## 5. Algorithm — Eight Steps

### 5.1 Step 1: Validate inputs exist
For each of the 5 input paths: check path.exists(). If any is missing, raise FileNotFoundError with the offending path. Fail fast before doing any work.

### 5.2 Step 2: Create output directory
`output_dir.mkdir(parents=True, exist_ok=True)`. Idempotent.

### 5.3 Step 3: Load Block H artifacts
Call existing Module 3 loaders:
```python
proposals = load_proposals(proposals_path)
decisions = load_decisions(decisions_path)
anomalies = load_anomalies(anomalies_path)
```
Load corrected_turns.json directly:
```python
with open(corrected_turns_path, encoding="utf-8") as f:
    corrected_turns = json.load(f)
```
Also read proposals.json raw to extract `metadata.saved_at` for review_queue `source_run.stage3_1_run_at`.

### 5.4 Step 4: Load case_info
```python
case_info = load_case_info(case_info_path)   # Module 2
```

### 5.5 Step 5: Build application map
```python
application_map, mapper_warnings = build_application_map(
    proposals, decisions, anomalies
)
```
Accumulate mapper_warnings into the running warnings list.

### 5.6 Step 6: Compose document
```python
composed = compose_document(corrected_turns, application_map, case_info)   # Module 6
```
Module 6 returns ComposedDocument which has its own .skipped_entries and stats. Surface skipped count into warnings if > 0.

### 5.7 Step 7: Lay out pages
```python
paginated = lay_out_pages(composed)   # Module 7
```
Module 7 returns PaginatedDocument. Surface review_entries_orphaned into warnings if > 0 (this should be zero — if it isn't, something is wrong).

### 5.8 Step 8: Write three output files

**File 1 — halprin_mini.OUR_FINAL.txt:**
```python
out_txt = output_dir / "halprin_mini.OUR_FINAL.txt"
out_txt.write_text(paginated.text, encoding="utf-8", newline="\n")
```
Critical: `newline="\n"` is required to prevent Python on Windows from converting `\n` to `\r\n`. Module 7 produces LF-only output by contract; we honor that on write.

**File 2 — halprin_mini.review_queue.json:**
```python
review_queue = {
    "schema_version": "1.0",
    "deposition_name": "halprin_mini",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "source_run": {
        "stage3_1_run_at": <pulled from proposals.json metadata.saved_at>,
        "total_proposals": len(proposals),
        "applied": <sum of application_map entry counts>,
        "rejected": <count where decision.outcome != "apply">,
    },
    "review_items": [asdict(entry) for entry in paginated.review_entries],
}
```

**File 3 — stage5.summary.json:** `json.dumps(asdict(summary), indent=2)`

### 5.9 Step 9: Return Stage5Summary
Build the Stage5Summary dataclass with all populated fields and return.

## 6. Public API
```python
def assemble_final(
    corrected_turns_path: Path,
    proposals_path: Path,
    decisions_path: Path,
    anomalies_path: Path,
    case_info_path: Path,
    output_dir: Path,
) -> Stage5Summary:
    """Stage 5 v0.1 — assemble human-readable depo from Block H output."""
```

## 7. CLI
```bash
python -m src.stage5.assemble_final \
    --corrected-turns io/analysis/halprin_mini/_stage3_1_out/corrected_turns.json \
    --proposals       io/analysis/halprin_mini/_stage3_1_out/proposals.json \
    --decisions       io/analysis/halprin_mini/_stage3_1_out/decisions.jsonl \
    --anomalies       io/analysis/halprin_mini/_stage3_1_out/anomalies.jsonl \
    --case-info       tests/stage5/fixtures/case_info_halprin_valid.json \
    --output-dir      io/analysis/halprin_mini/_stage5_out
```

## 8. Error Handling Contract

| Condition | Action |
|---|---|
| Missing input file | FileNotFoundError with path; fail fast in Step 1 |
| Invalid JSON in any input | Bubble up Python's json.JSONDecodeError |
| case_info.json schema invalid | Module 2 raises; bubble up |
| Block H artifacts have shape mismatch | Module 3 raises; bubble up |
| Module 5 / 6 / 7 raises ValueError | Bubble up |
| Unknown paragraph_style | Module 6 raises ValueError; bubble up |
| Output directory not writable | PermissionError; bubble up |
| Disk full mid-write | I/O error; bubble up |

No silent recovery. Warnings (non-fatal) are accumulated in the warnings list.

## 9. Test Plan (21 tests)

### 9.1 Happy path (1): test 01
### 9.2 File outputs (5): tests 02–06
### 9.3 Review queue contents (4): tests 07–10
### 9.4 Summary contents (4): tests 11–14
### 9.5 Error handling (5): tests 15–19
### 9.6 CLI smoke (1): test 20
### 9.7 Idempotency (1): test 21

## 10. Build Notes

- All 4 loaders (load_proposals, load_decisions, load_anomalies, load_case_info) accept Path — no str-coercion needed.
- proposals.json metadata.saved_at used for stage3_1_run_at in review_queue source_run.
- `QA_Q_CONTINUATION ... no preceding QA_Q` warnings are expected Halprin data behavior (s2 turns that follow answers, not a pipeline bug). 28 such warnings on Halprin data.
- Stage5Totals and Stage5Summary changed from mutable to frozen=True; review_tags_emitted changed from TagCounts to dict.

## 11. Revisit List (post-v0.1)

- [ ] Replace hardcoded "halprin_mini" filename stem with derivation from case_info or input path.
- [ ] Progress reporting / logging during long pipeline runs.
- [ ] Optional --strip-tags flag.
- [ ] Multi-deposition batch mode.
- [ ] --dry-run flag.
- [ ] Structured logging (JSON lines).

## 12. CLI Run Output (2026-04-27)

```
turns_rendered: 551
proposals_applied_REWORD: 12
proposals_applied_FLAG: 18
proposals_rejected: 0
review_tags_emitted: {"MB_REVIEW-FLAG_flag": 18, "MB_REVIEW-FIX_confident": 11, "MB_REVIEW-VERIFY_verify": 1}
pages_rendered: 45
lines_rendered: 1117
skipped_entries_count: 0
review_entries_orphaned: 0
```

Output files:
- `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt`
- `io/analysis/halprin_mini/_stage5_out/halprin_mini.review_queue.json`
- `io/analysis/halprin_mini/_stage5_out/stage5.summary.json`

## 13. Acceptance — COMPLETE ✅

- [x] schemas.py has Stage5Summary (frozen=True), Stage5Totals (frozen=True, with skipped_entries_count, review_entries_orphaned, review_tags_emitted: dict)
- [x] src/stage5/assemble_final.py exists with both assemble_final() API and CLI
- [x] All 21 tests pass
- [x] Full repo suite: 491 passing (470 + 21)
- [x] CLI run on real Halprin produces three output files
- [x] Summary shows zero orphaned review entries, zero skipped entries
- [x] Spec committed to docs/ in engine repo and specs/ in mrx-context
