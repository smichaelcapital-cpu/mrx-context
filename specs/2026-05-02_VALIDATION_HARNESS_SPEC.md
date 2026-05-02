# VALIDATION HARNESS SPEC — MB Calibration Thermos
**Date:** 2026-05-02
**Author:** Opus (architect)
**Builder:** Sonnet (next)
**Status:** SHIPPED — built same session

---

## 1. PURPOSE (the thermos)

A reusable, depo-agnostic-in-mechanics, MB-specific-in-calibration tool that answers ONE question every time it runs:

> **"On this depo, what % of the changes MB made did the engine also make?"**

Pour in OUR_FINAL + MB FINAL. Out comes a number, a 5-bucket breakdown, and a list of candidate new MB rules.

Six depos to calibrate. Seventh is bet-your-life.

---

## 2. INPUTS

| Input | Path pattern | Notes |
|---|---|---|
| OUR_FINAL | `io/analysis/<depo>/_stage5_out/<depo>.OUR_FINAL.txt` | Engine output |
| MB FINAL | `io/analysis/<depo>/<depo-FINAL>.txt` | MB ground truth |
| Pattern catalog | `harness/patterns/MB_PROFILE.yaml` | MB's growing rule set |
| Scope config | CLI args | `--start-page N --end-page M` (default: full file) |

---

## 3. METHOD — pattern catalog (Option 1, locked)

NOT difflib. Difflib breaks on line-wrap drift (proven yesterday).

Approach: **targeted pattern search**, same method Sonnet hand-built yesterday, now scripted.

Pattern catalog = YAML file with entries like:

```yaml
- id: WT_ACRONYM
  category: tight_collapse
  mb_form: "W&T"
  raw_form: "with and T"
  scope: case_specific  # or generic
  source: names_lock
- id: WARREN_SEAL_CAP
  category: capitalization
  mb_form: "Warren Seal"
  wrong_form: "Warren seal"
  scope: case_specific
- id: EM_DASH_SELF_CORRECT
  category: punctuation
  mb_pattern: "(\w+) -- \1"
  scope: generic
```

Catalog grows organically: every miss found becomes a candidate entry (reviewed by Scott before merge).

---

## 4. THE 5-BUCKET LENS (Scott's framing, locked)

For every pattern in the catalog, the harness counts:

| Bucket | Definition |
|---|---|
| **WIN** | MB made this change AND engine made it correctly |
| **MISS** | MB made this change AND engine did not (real defect) |
| **OVER-REACH** | Engine made this change AND MB did not (regression risk) |
| **STYLE GAP** | Engine could fix this with a new rule but doesn't have one yet |
| **SCOPE DECISION** | MB judgment call, engine should not auto-fix (FLAG only) |

---

## 5. OUTPUT FORMAT

Single markdown report at `io/analysis/<depo>/harness_report_<timestamp>.md`:

```
Harness Report — <depo>, pages X–Y
Run: <timestamp>
Engine commit: <git hash>
OUR_FINAL bytes: <n>
MB FINAL bytes: <n>

HEADLINE
Engine matched MB on X / Y trackable changes (Z%)
Status: [GREEN >=85% | YELLOW 60-85% | RED <60%]

BUCKET COUNTS
Bucket | Count
WIN    | n
MISS   | n
OVER-REACH | n
STYLE GAP  | n
SCOPE DECISION | n

DEFECTS BY PATTERN
[per-pattern table: pattern_id | mb_count | engine_correct | engine_wrong | bucket]

EDITORIAL RESTRAINT WATCH (paranoid)
[see EDITORIAL_RESTRAINT_WATCH_SPEC.md]

CANDIDATE NEW MB RULES
[any miss that doesn't match an existing pattern → flagged here for Scott review]

RAW EVIDENCE
[file paths to line-by-line evidence dumps for each bucket]
```

---

## 6. SCOPE TODAY

- **Input:** Halprin mini OUR_FINAL (89,398 bytes, commit 83d5199) + MB FINAL
- **Pages:** 13–50 (skip caption/appearances 1–12)
- **Patterns:** seed catalog with the 11 categories from yesterday's defect inventory
- **Output:** one report; we read it together, decide ship/no-ship for MB demo

---

## 7. INDUSTRIAL vs. SCAFFOLD MARKERS

Every file Sonnet writes must mark each function with one of:

```python
# INDUSTRIAL: production-grade, depo-agnostic, no hardcoding
# SCAFFOLD: temporary, will be replaced before depo 7
# TODO-INDUSTRIAL: works for now, needs upgrade — see comment
```

Scaffold acceptable today: hardcoded path to halprin_mini, hardcoded page range.
Industrial required today: pattern matching engine, bucket counting, report formatter, YAML catalog loader.

---

## 8. FILE LAYOUT

```
mrx_engine_v1/
  harness/
    __init__.py
    run_harness.py          # entry point — INDUSTRIAL
    pattern_engine.py       # YAML loader + pattern matcher — INDUSTRIAL
    bucket_classifier.py    # 5-bucket logic — INDUSTRIAL
    report_writer.py        # markdown report — INDUSTRIAL
    restraint_watch.py      # editorial restraint tracking — INDUSTRIAL
    patterns/
      MB_PROFILE.yaml       # MB's growing catalog — DATA
    watch/
      EDITORIAL_RESTRAINT_LOG.md  # append-only watch log
  tests/
    test_pattern_engine.py
    test_bucket_classifier.py
    test_e2e_halprin_mini.py
    test_restraint_watch.py
```

---

## 9. CLI

```bash
python -m harness.run_harness \
  --our-final io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt \
  --mb-final  io/analysis/halprin_mini/040226yellowrock-FINAL.txt \
  --catalog   harness/patterns/MB_PROFILE.yaml \
  --start-page 13 --end-page 50 \
  --report-out io/analysis/halprin_mini/harness_report_$(date +%Y%m%d_%H%M).md
```

---

## 10. TEST PLAN

| Test | Validates |
|---|---|
| `test_pattern_engine.py` | YAML loads, regex compiles, finds known patterns in fixture |
| `test_bucket_classifier.py` | Each bucket assigned correctly for synthetic OUR/MB pairs |
| `test_e2e_halprin_mini.py` | Full run on halprin_mini produces report, bucket counts within ±1 of yesterday's hand-built inventory |
| `test_restraint_watch.py` | Restraint events captured, log appends, empty section renders |

Acceptance: yesterday's hand-built numbers (W&T 3/9, Warren Seal 1/1 post-fix, Crescent 2/4, etc.) reproduced ±1 by the harness.

---

## 11. ROLLOUT

1. Sonnet builds files in section 8
2. Sonnet seeds `MB_PROFILE.yaml` with 11 patterns from yesterday's inventory
3. Sonnet runs all tests — green
4. Sonnet runs harness on current OUR_FINAL — produces first report
5. Scott + Opus read report — decide if numbers match expectations
6. If green: harness is now the ship/no-ship gate going forward
7. If miss: iterate catalog or method until aligned with Scott's eye

**SHIPPED:** Engine at 4f22ea8, 565 tests, 52.4% confidence on Halprin mini pages 13-50.

---

## 12. PRIME DIRECTIVE CHECK

> "Could this change reduce transcript accuracy or credibility?"

**No.** The harness is read-only. It does not modify OUR_FINAL, MB FINAL, or any engine code. It is a measurement tool. Worst case: bad measurement → caught by Scott's review of the first report.

---

## 13. OPEN ITEMS (resolved)

1. 5-bucket names — confirmed as written
2. `harness/` lives in mrx_engine_v1 repo — confirmed
3. GREEN/YELLOW/RED thresholds — deferred, no threshold set until 2-3 reports
4. Pattern catalog at `harness/patterns/MB_PROFILE.yaml` — confirmed

---

*End of spec.*
