# 2026-05-16 FINGERPRINT 13-DEPO FREQUENCY ANALYSIS
Sonnet #1 laneA — evening session

Extension of D-2/D-4/D-5 oracle audits from 6-depo set to 13 depos.
Data only. No fix recommendations.

**13-depo set:**
6 oracle/finals (halprin, olsen, williams, butler, blanks, black_bp) +
3 Group-A MB library (easley, fountain, hebert) +
2 Group-B staging (simon, garcia) +
2 parseable cache finals (griffin, martin).

---

## STEP 1 — INGESTION STATUS (9 missing depos)

Target: add to `fingerprints/stage_a/mb_evidence_raw.json`.

| Depo | Status | Reason |
|------|--------|--------|
| olsen_032025 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| black_bp_0525 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| williams_060122 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| butler_082222 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| blanks_101322 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| simon_011723 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| garcia_082322 | **FAIL** | no raw ROUGH .txt source — only formatted FINAL exists |
| zannetti_080221 | **FAIL** | raw+final cache exist but church/zannetti flagged: church 12x ratio anomaly; difflib hangs on mismatched pair; pipeline script not on main |
| church_073124 | **FAIL** | raw(35KB)+final(377KB) = 12x ratio anomaly (flagged 2026-05-14); difflib intractable on size mismatch; pipeline script not on main |

**Result:** 0 ingested, 9 failed.

**Root cause summary:**

- 7 depos (olsen, black_bp, williams, butler, blanks, simon, garcia):
  ROUGH draft was never exported to a plain-text `.txt` cache file.
  These depos exist only as formatted FINAL transcripts.
  Ingestion into the habit-frequency pipeline requires a RAW source.

- 2 depos (zannetti, church) have raw+final cache files but cannot
  be ingested because:
  (a) The aligner/differ script (`feature/stage-a-aligner-differ-v0`)
      is not on `main` — not accessible from laneA session.
  (b) Church is the 12x ratio anomaly flagged 2026-05-14: raw=35 KB,
      final=377 KB. Wrong raw file is almost certainly paired.
      Zannetti raw/final are legitimate but same script-missing blocker.

**Action required (not in scope for Sonnet):**
- Export ROUGH drafts to .txt for the 7 no-raw depos.
- Merge or cherry-pick `feature/stage-a-aligner-differ-v0` to `main`.
- Resolve church raw-file pairing before ingesting.

---

## QUERY A — Firm-Group Separator Blank Slots (D-2)

Method: count fully-blank slots (MAIN='' AND SUB='') strictly between
consecutive firm-group headers on appearances pages.
Header patterns: `FOR THE`, `ATTORNEY FOR`, `Attorney for`.

### Full Transition Table

| depo | pg | prev_end | next_start | blank_slots |
|------|----|----------|------------|-------------|
| halprin | 5 | 10 | 12 | **1** |
| halprin | 5 | 16 | 17 | **0** |
| halprin | 6 | 1 | 2 | **0** |
| halprin | 6 | 6 | 7 | **0** |
| halprin | 6 | 12 | 13 | **0** |
| halprin | 6 | 16 | 17 | **0** |
| halprin | 7 | 1 | 2 | **0** |
| halprin | 7 | 6 | 7 | **0** |
| halprin | 7 | 10 | 11 | **0** |
| halprin | 7 | 15 | 16 | **0** |
| halprin | 7 | 19 | 20 | **0** |
| halprin | 8 | 1 | 2 | **0** |
| halprin | 8 | 5 | 7 | **1** |
| halprin | 8 | 10 | 11 | **0** |
| halprin | 8 | 15 | 16 | **0** |
| halprin | 9 | 1 | 2 | **0** |
| halprin | 9 | 6 | 7 | **0** |
| halprin | 9 | 11 | 12 | **0** |
| halprin | 9 | 16 | 17 | **0** |
| halprin | 10 | 1 | 2 | **0** |
| halprin | 10 | 7 | 8 | **0** |
| olsen | 4 | 6 | 7 | **0** |
| williams | 4 | 5 | 7 | **1** |
| williams | 4 | 12 | 13 | **0** |
| williams | 4 | 17 | 18 | **0** |
| butler | 3 | 5 | 6 | **0** |
| butler | 3 | 11 | 12 | **0** |
| butler | 3 | 16 | 17 | **0** |
| blanks | 3 | 5 | 6 | **0** |
| blanks | 3 | 11 | 12 | **0** |
| blanks | 3 | 16 | 17 | **0** |
| black_bp | 5 | 5 | 6 | **0** |
| black_bp | 5 | 11 | 12 | **0** |
| black_bp | 5 | 16 | 17 | **0** |
| easley | 5 | 9 | 11 | **1** |
| easley | 5 | 15 | 17 | **1** |
| easley | 5 | 20 | 22 | **1** |
| easley | 6 | 1 | 3 | **1** |
| easley | 6 | 7 | 9 | **1** |
| easley | 6 | 12 | 14 | **1** |
| easley | 6 | 20 | 22 | **1** |
| easley | 7 | 1 | 3 | **1** |
| easley | 7 | 6 | 8 | **1** |
| easley | 7 | 11 | 13 | **1** |
| easley | 7 | 16 | 18 | **1** |
| easley | 7 | 21 | 23 | **1** |
| easley | 8 | 2 | 4 | **1** |
| easley | 8 | 7 | 9 | **1** |
| easley | 8 | 12 | 14 | **1** |
| easley | 8 | 18 | 20 | **1** |
| easley | 9 | 1 | 2 | **0** |
| easley | 9 | 5 | 7 | **1** |
| easley | 9 | 11 | 13 | **1** |
| easley | 9 | 16 | 18 | **1** |
| easley | 9 | 22 | 24 | **1** |
| fountain | 3 | 5 | 6 | **0** |
| fountain | 3 | 10 | 11 | **0** |
| fountain | 3 | 15 | 16 | **0** |
| hebert | 3 | 5 | 6 | **0** |
| hebert | 3 | 12 | 13 | **0** |
| hebert | 3 | 16 | 17 | **0** |
| hebert | 4 | 1 | 2 | **0** |
| simon | 3 | 5 | 6 | **0** |
| simon | 3 | 12 | 13 | **0** |
| simon | 3 | 17 | 18 | **0** |
| garcia | 3 | 5 | 6 | **0** |
| garcia | 3 | 11 | 12 | **0** |
| garcia | 3 | 16 | 17 | **0** |
| griffin | 3 | 5 | 6 | **0** |
| griffin | 3 | 11 | 12 | **0** |
| griffin | 3 | 16 | 17 | **0** |
| martin | 3 | 5 | 6 | **0** |
| martin | 3 | 11 | 12 | **0** |
| martin | 3 | 16 | 17 | **0** |

### Summary

```
Total transitions: 74

  0 blank(s):  51 transitions (68%)  ← dominant
  1 blank(s):  23 transitions (31%)

Dominant pattern: 0 blank slot(s) between firm groups
```

### Per-Depo D2 Summary

| depo | transitions | 0-blank | 1-blank | 2+-blank | note |
|------|------------|---------|---------|----------|------|
| halprin | 21 | 19 | 2 | 0 |  |
| olsen | 1 | 1 | 0 | 0 |  |
| williams | 3 | 2 | 1 | 0 |  |
| butler | 3 | 3 | 0 | 0 |  |
| blanks | 3 | 3 | 0 | 0 |  |
| black_bp | 3 | 3 | 0 | 0 |  |
| easley | 21 | 1 | 20 | 0 |  |
| fountain | 3 | 3 | 0 | 0 |  |
| hebert | 4 | 4 | 0 | 0 |  |
| simon | 3 | 3 | 0 | 0 |  |
| garcia | 3 | 3 | 0 | 0 |  |
| griffin | 3 | 3 | 0 | 0 |  |
| martin | 3 | 3 | 0 | 0 |  |

---

## QUERY B — Reporter's Certificate Slot on INDEX Page (D-4)

Method: parse INDEX page with slot regex.
Cert search: `reporter'?s? certif` (case-insensitive).

| depo | cert_slot | cert_pos | index_page |
|------|-----------|----------|------------|
| halprin | 7 | SUB | 2 |
| olsen | 6 | SUB | 2 |
| williams | 8 | MAIN | 2 |
| butler | 7 | MAIN | 2 |
| blanks | 7 | MAIN | 2 |
| black_bp | 8 | SUB | 2 |
| easley | 13 | MAIN | 2 |
| fountain | 7 | MAIN | 2 |
| hebert | 7 | MAIN | 2 |
| simon | 7 | MAIN | 2 |
| garcia | 7 | MAIN | 2 |
| griffin | 8 | MAIN | 2 |
| martin | 8 | MAIN | 2 |

### Summary

```
Depos with cert data: 13
  MAIN: 10 (76%)
  SUB:  3  (23%)

  Slot distribution:
    slot 6: 1x  positions seen: [SUB]
    slot 7: 7x  positions seen: [MAIN, SUB]
    slot 8: 4x  positions seen: [MAIN, SUB]
    slot 13: 1x  positions seen: [MAIN]
```

---

## QUERY C — Exhibits Index Start Position (D-5)

Method: find EXHIBITS header on INDEX page, then first `Exhibit No.` entry.

| depo | exhibits_hdr_slot | exhibits_hdr_pos | first_ex_slot | first_ex_pos |
|------|------------------|-----------------|--------------|--------------|
| halprin | 11 | MAIN | 12 | MAIN |
| olsen | 9 | MAIN | 10 | MAIN |
| williams | 11 | SUB | 12 | SUB |
| butler | 10 | SUB | 11 | SUB |
| blanks | 10 | SUB | 11 | SUB |
| black_bp | 12 | MAIN | 13 | MAIN |
| easley | 19 | MAIN | 21 | MAIN |
| fountain | — | — | — | *No exhibit entries after EXHIBITS header* |
| hebert | — | — | — | *No EXHIBITS header* |
| simon | — | — | — | *No EXHIBITS header* |
| garcia | 10 | SUB | 11 | SUB |
| griffin | — | — | — | *No EXHIBITS header* |
| martin | — | — | — | *No EXHIBITS header* |

### Summary

```
Depos with exhibit data: 8
  First exhibit in MAIN: 4 (50%)
  First exhibit in SUB:  4  (50%)
```

---

*Generated by run_13depo_analysis.py — Sonnet #1 laneA 2026-05-16 evening*