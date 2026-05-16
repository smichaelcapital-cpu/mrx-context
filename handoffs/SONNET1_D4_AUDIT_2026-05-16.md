# D-4 REPORTER'S CERTIFICATE SLOT AUDIT
# Sonnet #1 laneA — 2026-05-16
# Read-only oracle audit. No code touched.

## Method

For each of the 6 MB depo oracle FINAL files, the INDEX page (page 2) was parsed
using the corrected MAIN/SUB slot regex:
  `r'^( {1,6})(\d{1,2})(  .*|\s*$)'`
  (matches both content-bearing MAIN lines AND blank-MAIN slots with no trailing text)

The slot number and position (MAIN vs SUB) of the Reporter's Certificate entry was
recorded from the oracle. Then the rendered SxS output (review/*_front_sxs.txt,
LEFT column = OURS / renderer) was checked for the same entry and its slot placement.

Cert search pattern: `reporter'?s?\s+certif` (case-insensitive)

Note: williams oracle also matched "Exhibit No. 3 Certification For Medical Records"
at slot 15 — excluded, not the Reporter's Certificate section.

---

## Oracle Index Page — All Slots

### halprin (040226yellowrock-FINAL.txt)
```
  slot  1 MAIN: 'I N D E X'
         SUB:   'Page'
  slot  2 MAIN: 'Caption                                       1'
  slot  3 MAIN: 'Appearances                                   5'
  slot  4 MAIN: 'Stipulation                                  11'
  slot  5 MAIN: 'Examination'
         SUB:   'Mr. Caughey                              13'
  slot  6 MAIN: ''   (blank)
  slot  7 MAIN: ''   (blank)
         SUB:   "Reporter's Certificate                      296"   <<<CERT
  slot  8 MAIN: ''   (blank)
         SUB:   "Witness's Certificate                       298"
  slot  9 MAIN: ''   (blank)
         SUB:   '* * * * * * * *'
  slot 10 MAIN: ''   (blank)
  slot 11 MAIN: 'EXHIBITS'
  ... (exhibit entries follow)
```
Oracle cert: **slot 7 SUB**

### 032025olsen (032025olsen-FINAL.txt)
```
  slot  1 MAIN: 'I N D E X'
         SUB:   'Page'
  slot  2 MAIN: 'Caption                                       1'
  slot  3 MAIN: 'Appearances                                   4'
  slot  4 MAIN: 'Stipulation                                   5'
  slot  5 MAIN: 'Examination'
         SUB:   'Mr. Knight                                7'
  slot  6 MAIN: ''   (blank)
         SUB:   "Reporter's Certificate                       199"  <<<CERT
  slot  7 MAIN: ''   (blank)
  slot  8 MAIN: '* * * * * * * * *'
  slot  9 MAIN: 'EXHIBITS'
  ... (exhibit entries follow)
```
Oracle cert: **slot 6 SUB**

### 060122williams (060122williams-FINAL.txt)
```
  slot  1 MAIN: 'I N D E X'
         SUB:   'Page'
  slot  2 MAIN: 'Caption                                       1'
  slot  3 MAIN: 'Appearances                                   4'
  slot  4 MAIN: 'Stipulation                                   6'
  slot  5 MAIN: 'Examination'
         SUB:   'Mr. Leefe                                 8'
  slot  6 MAIN: 'Mr. Gileson                             198'
         SUB:   'Re Examination'
  slot  7 MAIN: 'Mr. Leefe                               204'
  slot  8 MAIN: "Reporter's Certificate                      206"   <<<CERT
  slot  9 MAIN: 'Witness Certificate                         208'
  slot 10 MAIN: '* * * * * * * * *'
  slot 11 MAIN: ''   (blank)
         SUB:   'EXHIBITS'
  ... (exhibit entries follow)
```
Oracle cert: **slot 8 MAIN**

### 082222butler (082222butler-FINAL.txt)
```
  slot  1 MAIN: 'I N D E X'
         SUB:   'Page'
  slot  2 MAIN: 'Caption                                       1'
  slot  3 MAIN: 'Appearances                                   3'
  slot  4 MAIN: 'Stipulation                                   5'
  slot  5 MAIN: 'Examination'
         SUB:   'Mr. Bullock                               7'
  slot  6 MAIN: ''   (blank)
  slot  7 MAIN: "Reporter's Certificate                       109"  <<<CERT
  slot  8 MAIN: ''   (blank)
  slot  9 MAIN: '* * * * * * * * *'
  slot 10 MAIN: ''   (blank)
         SUB:   'EXHIBITS'
  ... (exhibit entries follow)
```
Oracle cert: **slot 7 MAIN**

### 101322blanks (101322blanks-FINAL.txt)
```
  slot  1 MAIN: 'I N D E X'
         SUB:   'Page'
  slot  2 MAIN: 'Caption                                       1'
  slot  3 MAIN: 'Appearances                                   3'
  slot  4 MAIN: 'Stipulation                                   5'
  slot  5 MAIN: 'Examination'
         SUB:   'Mr. McMillin                              7'
  slot  6 MAIN: ''   (blank)
  slot  7 MAIN: "Reporter's Certificate                        72"  <<<CERT
  slot  8 MAIN: ''   (blank)
  slot  9 MAIN: '* * * * * * * * *'
  slot 10 MAIN: ''   (blank)
         SUB:   'EXHIBITS'
  ... (exhibit entries follow)
```
Oracle cert: **slot 7 MAIN**

### 0525black_bp (0525black-bp-FINAL.txt)
```
  slot  1 MAIN: 'I N D E X'
         SUB:   'Page'
  slot  2 MAIN: 'Caption                                       1'
  slot  3 MAIN: 'Appearances                                   5'
  slot  4 MAIN: 'Stipulation                                   7'
  slot  5 MAIN: 'Examination'
         SUB:   'Mr. McNeal                               9'
  slot  6 MAIN: 'Mr. Falcon                              190'
         SUB:   'Re Examination'
  slot  7 MAIN: 'Mr. McNeal                              198'
  slot  8 MAIN: ''   (blank)
         SUB:   "Reporter's Certificate                      205"   <<<CERT
  slot  9 MAIN: ''   (blank)
  slot 10 MAIN: ''   (blank)
         SUB:   '* * * * * * * * *'
  slot 11 MAIN: ''   (blank)
  slot 12 MAIN: 'EXHIBITS'
  ... (exhibit entries follow)
```
Oracle cert: **slot 8 SUB**

---

## Summary Table

| depo | oracle_slot | oracle_pos | renderer_slot | renderer_pos | drift |
|------|-------------|------------|---------------|--------------|-------|
| halprin | 7 | SUB | 7 | SUB | **0** |
| 032025olsen | 6 | SUB | 7 | MAIN | **+1** |
| 060122williams | 8 | MAIN | 8 | MAIN | **0** |
| 082222butler | 7 | MAIN | 7 | MAIN | **0** |
| 101322blanks | 7 | MAIN | 7 | MAIN | **0** |
| 0525black_bp | 8 | SUB | 9 | MAIN | **+1** |

4/6 depos match oracle (67%). 2/6 depos drift +1 slot (33%).

---

## SxS Evidence for Drifting Depos

### 032025olsen — cert oracle slot 6 SUB, renderer slot 7 MAIN
```
SxS (LEFT=renderer, RIGHT=oracle):
  5  Examination                      |      5  Examination
        Mr. Knight                  7 |            Mr. Knight                 7
  6                                   |      6
                                      |         Reporter's Certificate       199   ← ORACLE slot 6 SUB
  7                                   |      7
     Reporter's Certificate       199 |                                            ← RENDERER slot 7 MAIN
  8                                   |      8  * * * * * * * * *
     * * * * * * * *                  |                                            ← pushed 1 slot late
  9                                   |      9  EXHIBITS
  10 EXHIBITS                         |     10  Exhibit No. 1...
```
Renderer places cert at slot 7 MAIN. Oracle places it at slot 6 SUB.
Everything following is pushed 1 slot in the renderer vs oracle.

### 0525black_bp — cert oracle slot 8 SUB, renderer slot 9 MAIN
```
SxS (LEFT=renderer, RIGHT=oracle):
  7  Re Examination                   |      7      Mr. McNeal              198
     Mr. McNeal                   198 |
  8                                   |      8
                                      |         Reporter's Certificate      205   ← ORACLE slot 8 SUB
  9                                   |      9
     Reporter's Certificate       205 |                                           ← RENDERER slot 9 MAIN
 10                                   |     10
     * * * * * * * *                  |                           * * * * * * * * *
 12  EXHIBITS                         |     12  EXHIBITS
```
Renderer places cert at slot 9 MAIN. Oracle places it at slot 8 SUB.

---

## Root Cause Analysis

### The +1 slot drift pattern

In both drifting depos, the nav section ends with an odd-parity entry (last nav item
lands in MAIN position), leaving the following SUB position available. Oracle places
the cert in that SUB. Renderer instead emits a blank SUB and starts cert at the
MAIN of the next slot.

**Trigger condition:** cert drifts when last nav entry is in MAIN position AND
cert is the immediate next entry (no blank separator between last nav MAIN and cert).
Oracle: `last_nav_MAIN → [blank SUB, cert]` treated as: slot N MAIN=last_nav, slot N SUB=cert.
Renderer: `last_nav_MAIN → [blank slot, cert MAIN]` — extra blank inserted, cert bumped.

**No drift when:**
- Cert lands in MAIN position naturally (williams, butler, blanks): parity forces it to MAIN, no ambiguity.
- Cert is in SUB but there are 2 blank MAINs between last nav and cert (halprin): the extra blank provides the offset and both sides agree.

### Affected depos

- 032025olsen: 1 examination (simple nav, ends at slot 5 SUB) → cert at slot 6 SUB (oracle), slot 7 MAIN (ours).
- 0525black_bp: 3 examination entries (ends at slot 7 MAIN) → cert at slot 8 SUB (oracle), slot 9 MAIN (ours).

### Non-affected pattern

butler and blanks: same simple nav structure as olsen (ends at slot 5 SUB), BUT cert
lands at slot 7 MAIN because oracle emits a blank at slot 6 MAIN before cert.
Renderer also emits blank slot 6, cert at slot 7 MAIN — 0 drift.

The difference: olsen cert lands immediately in slot 6 SUB (no blank slot 6 MAIN).
Butler/blanks have blank slot 6 MAIN, cert at slot 7 MAIN. The oracle is inconsistent
across these depos in whether it uses a blank-MAIN separator before the cert.

---

## Key Finding for Opus / D-4 Design

**Frequency distribution:**
- 4/6 depos: 0 drift — cert placement matches oracle exactly
- 2/6 depos: +1 drift — both are the "cert-in-SUB" cases with specific nav parity

**The drift is real but narrow.** It only manifests when:
1. Last nav entry lands in MAIN position (odd item count)
2. Oracle places cert immediately in the SUB of the following blank-MAIN slot
3. Renderer inserts an extra blank MAIN before the cert instead

**Implication for fix:**
- The renderer's cert placement logic does not track MAIN/SUB cycle correctly
  across the nav→cert boundary.
- Fix is to carry the MAIN/SUB cycle state from the nav section into the cert entry,
  so cert inherits the correct position (SUB when nav ends on MAIN).
- This is MB-specific (structural front-matter rendering). File: src/profiles/mb/ or
  src/stage5/front_matter/index.py cert placement logic.
- Do NOT add a universal blank-MAIN before every cert entry — that fixes
  olsen/black_bp but breaks butler/blanks (which already emit the blank correctly).

**D-4 scope:**
- Affects 2/6 depos: 032025olsen, 0525black_bp
- Severity: cert appears 1 slot late, cascades to shift * * * separator and
  potentially EXHIBITS header position in both depos

---

## Per-Depo Summary

| depo | nav_entries | last_nav_pos | cert_oracle | cert_renderer | drift | note |
|------|-------------|-------------|-------------|---------------|-------|------|
| halprin | 5 (exam+1 witness) | SUB | slot 7 SUB | slot 7 SUB | 0 | has Witness's Cert too; 2 blank MAINs before cert |
| 032025olsen | 4 | SUB | slot 6 SUB | slot 7 MAIN | +1 | single exam, no Re-Exam |
| 060122williams | 6 (2 Re-Exam rounds) | MAIN | slot 8 MAIN | slot 8 MAIN | 0 | cert in MAIN, no ambiguity |
| 082222butler | 4 | SUB | slot 7 MAIN | slot 7 MAIN | 0 | blank slot 6 separates, cert in MAIN |
| 101322blanks | 4 | SUB | slot 7 MAIN | slot 7 MAIN | 0 | same as butler |
| 0525black_bp | 6 (Re-Exam) | MAIN | slot 8 SUB | slot 9 MAIN | +1 | Re-Exam ends on MAIN, cert should be in SUB |
