# D-2 FIRM-GROUP SEPARATOR FREQUENCY AUDIT
# Sonnet #1 laneA — 2026-05-16
# Read-only oracle audit. No code touched.

## Method

For each of the 6 MB depo oracle FINAL files, every appearances page was parsed.
All firm-group transitions were identified. For each transition:
- `prev_firm_end_slot`: last slot with any content in the departing firm group
- `next_firm_start_slot`: first slot where the incoming firm header appears (MAIN or SUB)
- `blank_slots`: count of fully-blank slots (MAIN="" AND SUB="") strictly between
  prev_firm_end_slot and next_firm_start_slot

Firm header patterns matched: "FOR THE...", "Attorney for...", "ATTORNEY FOR..."

Oracle files used:
- halprin:        040226yellowrock-FINAL.txt
- 032025olsen:    032025olsen-FINAL.txt
- 060122williams: 060122williams-FINAL.txt
- 082222butler:   082222butler-FINAL.txt
- 101322blanks:   101322blanks-FINAL.txt
- 0525black_bp:   0525black-bp-FINAL.txt

---

## Full Transition Table

| depo | page | prev_firm_end_slot | next_firm_start_slot | blank_slots |
|------|------|--------------------|----------------------|-------------|
| halprin | 5 | 10 | 12 | **1** |
| halprin | 5 | 16 | 17 | 0 |
| halprin | 6 | 6 | 7 | 0 |
| halprin | 6 | 12 | 13 | 0 |
| halprin | 6 | 16 | 17 | 0 |
| halprin | 7 | 6 | 7 | 0 |
| halprin | 7 | 10 | 11 | 0 |
| halprin | 7 | 15 | 16 | 0 |
| halprin | 7 | 19 | 20 | 0 |
| halprin | 8 | 5 | 7 | **1** |
| halprin | 8 | 10 | 11 | 0 |
| halprin | 8 | 15 | 16 | 0 |
| halprin | 9 | 6 | 7 | 0 |
| halprin | 9 | 11 | 12 | 0 |
| halprin | 9 | 16 | 17 | 0 |
| halprin | 10 | 7 | 8 | 0 |
| 032025olsen | 4 | 6 | 7 | 0 |
| 060122williams | 4 | 5 | 7 | **1** |
| 060122williams | 4 | 12 | 13 | 0 |
| 060122williams | 4 | 17 | 18 | 0 |
| 082222butler | 3 | 5 | 6 | 0 |
| 082222butler | 3 | 11 | 12 | 0 |
| 082222butler | 3 | 16 | 17 | 0 |
| 101322blanks | 3 | 5 | 6 | 0 |
| 101322blanks | 3 | 11 | 12 | 0 |
| 101322blanks | 3 | 16 | 17 | 0 |
| 0525black_bp | 5 | 5 | 6 | 0 |
| 0525black_bp | 5 | 11 | 12 | 0 |
| 0525black_bp | 5 | 16 | 17 | 0 |

---

## Summary

```
Total separator instances:    29

Distribution of blank_slots values:
  0 blanks:  26 instances (90%)
  1 blank:    3 instances (10%)
  2+ blanks:  0 instances (0%)

Dominant pattern: 0 blank slots between firm groups

Outliers (1 blank slot):
  halprin   page 5  — slots 10→12  (slot 11 fully blank)
  halprin   page 8  — slots 5→7    (slot 6 fully blank)
  060122williams page 4 — slots 5→7 (slot 6 fully blank)
```

---

## What the 3 Outliers Look Like (oracle raw)

### halprin page 5, slot 10→12
```
    10         LESLIE PARTIDA DEPAZ,
                                Paralegal
    11                                        ← fully blank slot (MAIN="", SUB="")
                                              ← (blank SUB)
    12  FOR THE DEFENDANTS, WESTLAKE US 2 LLC, WESTLAKE
        CORPORATION AND WESTLAKE CHLOR-VINYLS CORPORATION:
```
Prior firm ends at slot 10 with content in both MAIN and SUB.
Slot 11 = blank (both MAIN and SUB empty).
Next firm starts at slot 12 MAIN.

### halprin page 8, slots 5→7
```
     5      sally.clements@kenndyslaw.com
            BY: SALLY CLEMENTS, ESQ.  (Via Zoom)
     6                                        ← fully blank slot (MAIN="", SUB="")
                                              ← (blank SUB)
     7  FOR THE DEFENDANT, TIG:
            MOULEDOUX, BLAND, LEGRAND & BRACKETT
```
Prior firm ends at slot 5 with content in both MAIN and SUB.
Slot 6 = blank. Next firm starts at slot 7 MAIN.

### 060122williams page 4, slots 5→7
```
     5      BY: SOREN GISLESON, ESQ.
                Jessica Quin
     6                                        ← fully blank slot (MAIN="", SUB="")
                                              ← (blank SUB)
     7  Attorney for DEFENDANT, BP EXPLORATION & PRODUCTION,
        INC.:
```
Prior firm ends at slot 5 with content in both MAIN and SUB.
Slot 6 = blank. Next firm starts at slot 7 MAIN.

---

## Key Finding for Opus / D-2 Design

**The blank slot is NOT an intentional separator.** All 3 outlier cases share the
same structural cause:

> The prior firm group ends with content in BOTH MAIN and SUB of the same slot
> (i.e., the last slot of the firm has a non-blank SUB). This exhausts both
> positions of that slot. The next available MAIN is slot+1, but the renderer
> places the firm header at slot+2 MAIN — leaving slot+1 fully blank.

In 90% of cases, the prior firm ends with content in MAIN only (SUB blank), and
the next firm header naturally lands in the SUB of the immediately following slot
(0 blank slots between them).

**This is a consequence of the MAIN/SUB alternating layout algorithm, not a
deliberate blank-line insertion rule.** The oracle does not add an explicit blank
between firm groups. The blank slot emerges from line-count parity at the end of
the prior firm group.

**Implication for D-2 fix:**
- Do NOT implement "insert a blank slot between every firm group."
- The correct fix is to ensure the MAIN/SUB cycling continues correctly across
  firm group boundaries, with no explicit gap insertion.
- The 90% case (0 blanks) is the dominant pattern. The 10% case (1 blank) is a
  natural side effect of the algorithm and will appear automatically when line
  counts align correctly.

**What "drift" D-2 is actually detecting:** The renderer is likely misaligning
the MAIN/SUB cycle at firm group boundaries (resetting it instead of continuing),
which produces different slot positioning for the same firm content. The fix is
to continue the cycle, not add blanks.

---

## Per-Depo Summary

| depo | appearances_pages | total_transitions | 0-blank | 1-blank |
|------|-------------------|-------------------|---------|---------|
| halprin | 6 (pp 5–10) | 16 | 14 | 2 |
| 032025olsen | 1 (p 4) | 1 | 1 | 0 |
| 060122williams | 1 (p 4) | 3 | 2 | 1 |
| 082222butler | 1 (p 3) | 3 | 3 | 0 |
| 101322blanks | 1 (p 3) | 3 | 3 | 0 |
| 0525black_bp | 1 (p 5) | 3 | 3 | 0 |

Note: 032025olsen (arbitration) has only 2 firm groups (Claimants + Respondents).
butler/blanks/black_bp have 3 firm groups each, all 0-blank separators.
