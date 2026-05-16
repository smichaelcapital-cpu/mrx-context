# MB OPEN QUESTION — D-5: EXHIBITS INDEX START POSITION
# 2026-05-16 — Sonnet #1 laneA evening session

## The Question

On the INDEX page, does the first `Exhibit No.` entry land in MAIN or SUB?

The frequency data shows a 50/50 split across the 8 depos with exhibit data.
This is an open design question: what should the renderer do when it cannot
determine position from document structure alone?

**Locked default: MAIN-first.**

---

## Frequency Data (13-Depo Set)

Source: `knowledge/2026-05-16_FINGERPRINT_13_DEPO_FREQ.md` — Query C (D-5).

### Full Table

| depo | exhibits_hdr_slot | exhibits_hdr_pos | first_ex_slot | first_ex_pos |
|------|------------------|-----------------|--------------|--------------|
| halprin | 11 | MAIN | 12 | **MAIN** |
| olsen | 9 | MAIN | 10 | **MAIN** |
| williams | 11 | SUB | 12 | **SUB** |
| butler | 10 | SUB | 11 | **SUB** |
| blanks | 10 | SUB | 11 | **SUB** |
| black_bp | 12 | MAIN | 13 | **MAIN** |
| easley | 19 | MAIN | 21 | **MAIN** |
| garcia | 10 | SUB | 11 | **SUB** |
| fountain | — | — | — | *No exhibit entries after EXHIBITS header* |
| hebert | — | — | — | *No EXHIBITS header* |
| simon | — | — | — | *No EXHIBITS header* |
| griffin | — | — | — | *No EXHIBITS header* |
| martin | — | — | — | *No EXHIBITS header* |

### Summary

```
Depos with exhibit data: 8
  First exhibit in MAIN: 4 (50%)  <- halprin, olsen, black_bp, easley
  First exhibit in SUB:  4 (50%)  <- williams, butler, blanks, garcia
```

---

## Structural Observation

The first exhibit position is NOT random — it is determined entirely by
the EXHIBITS header position:

- When EXHIBITS header lands in **MAIN**: first exhibit is in **MAIN** (next slot MAIN).
- When EXHIBITS header lands in **SUB**: first exhibit is in **SUB** (next slot SUB).

This means the MAIN/SUB position of the first exhibit entry is a consequence
of the MAIN/SUB cycling state at the point where EXHIBITS appears, not a
separate design choice.

The deeper question is: **what determines where the EXHIBITS header lands?**
Answer: it depends on slot count parity of the nav section above it (cert +
separators + witness cert, etc.). That count varies by depo.

---

## Why MAIN-First Is the Locked Default

1. **Tie-breaker**: 50/50 split provides no statistical preference. Default
   must be chosen on other grounds.

2. **MAIN is the primary column**: In the two-column (MAIN/SUB) slot layout,
   MAIN is the structurally "heavier" position. Section headers that start a
   new visual block conventionally land in MAIN.

3. **Simplicity**: A MAIN-first default means the renderer does not need to
   track sub-column parity through the cert/separator block to determine
   the EXHIBITS position. It resets to MAIN when it encounters EXHIBITS.

4. **Affected depos**: The 4 SUB-first depos (williams, butler, blanks, garcia)
   will drift by 1 slot at the EXHIBITS boundary. This is acceptable as a
   known, bounded cosmetic deviation pending a full parity-tracking fix.

---

## Open Sub-Questions (Not Blocking D-5 Fix)

1. **Is the 50/50 split stable?** The 13-depo set is small. A larger sample
   could shift the distribution. The MAIN-first default should be revisited
   if additional oracle data shows a strong SUB-first majority.

2. **Can the EXHIBITS position be derived from nav parity?** In principle yes
   — if the renderer tracks MAIN/SUB cycle state continuously from slot 1
   through all nav entries, cert, and separator, it would naturally place
   EXHIBITS in the correct column without a hardcoded default. This is the
   long-term fix but requires the parity-tracking work from D-4.

3. **Fountain anomaly**: Fountain has an EXHIBITS header (slot 7 MAIN) but no
   exhibit entries after it. Either the exhibits section is empty in this
   depo or the exhibit pattern does not match. Not blocking.

---

## Design Decision Record

| Field | Value |
|-------|-------|
| Question ID | D-5 |
| Decided | 2026-05-16 |
| Decided by | Sonnet #1 laneA (operator instruction) |
| Default | MAIN-first |
| Rationale | 50/50 tie; MAIN is primary column; simplifies renderer logic |
| Revisit trigger | Larger oracle sample shows SUB-first majority (>65%) |
| Related defect | B1.9.x (INDEX page rendering, to be numbered) |
| Related audit | `handoffs/SONNET1_D5_AUDIT_2026-05-16.md` |
