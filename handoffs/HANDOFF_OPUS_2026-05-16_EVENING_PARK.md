# HANDOFF — OPUS — 2026-05-16 EVENING PARK
# Written by Sonnet #1 laneA

## WHAT GOT DONE THIS AFTERNOON

Three read-only oracle audits, all committed to mrx-context main:

- **D-2 firm-group separator frequency** (SONNET1_D2_FREQ_AUDIT_2026-05-16.md)
  29 transitions across 6 depos. 26/29 (90%) = 0 blank slots between firm groups.
  3/29 (10%) = 1 blank slot — natural MAIN/SUB parity artifact, NOT an explicit separator.
  Key finding: renderer must NOT insert explicit blanks. The parity handles it.

- **D-4 Reporter's Certificate slot position** (SONNET1_D4_AUDIT_2026-05-16.md)
  6 depos. 4/6 correct (0 drift). 2/6 drift +1: olsen (cert slot 6 SUB → renderer slot 7 MAIN)
  and black_bp (cert slot 8 SUB → renderer slot 9 MAIN).
  Root cause: renderer does not carry MAIN/SUB cycle into the cert entry — inserts
  extra blank MAIN when cert should land in SUB.

- **D-5 exhibits index packing** (SONNET1_D5_AUDIT_2026-05-16.md)
  101 exhibits across 6 depos. 61/101 (60%) = 0 drift. All non-zero drift in 2 depos.
  Key finding: exhibits loop is CORRECT (halprin 23/23, black_bp 23/28). All drift
  is upstream contamination from nav section MAIN/SUB misalignment.

## STATE AT PARK

- mrx-context main: commits d2 (ee56f18), d4 (af27b7c), d5 (265a4d0)
- Both Sonnet lanes: parked clean on main
- No open branches, no WIP
- B1.9.2 attempted and reverted earlier in the day (narrow firm-separator fix broke
  halprin pagination)

## THE THREE-AUDIT UNIFIED PICTURE

D-2, D-4, D-5 are the same bug: **MAIN/SUB cycle state is not carried continuously
across section boundaries** in the index/appearances renderer.

Every defect traces to a transition point where the renderer either:
1. Inserts an explicit blank when the parity does not call for one, OR
2. Starts the next section's first content in MAIN when parity says SUB (or vice versa)

Section boundaries that must carry state:
```
firm group → next firm group        (D-2)
nav section → cert entry            (D-4)
cert → witness cert (if present)
witness cert → separator (* * *)
separator → EXHIBITS header
EXHIBITS header → first exhibit     (D-5)
```

For each boundary: the incoming section's first content must land at the next
available position in the running cycle. If prior section ended on MAIN, next content
goes in SUB. If prior section ended on SUB, next content goes in MAIN. No exceptions,
no explicit blank insertion.

## SxS EVIDENCE FOR EACH BOUNDARY (oracle vs renderer)

### halprin (CLEAN — use as canonical)

Page 2 nav → cert boundary:
```
slot 5 MAIN: Examination     slot 5 SUB: Mr. Caughey 13
slot 6 MAIN: [blank]         slot 6 SUB: [blank]
slot 7 MAIN: [blank]         slot 7 SUB: Reporter's Certificate 296
slot 8 MAIN: [blank]         slot 8 SUB: Witness's Certificate 298
```
Oracle and renderer both agree. Prior section ends at slot 5 SUB. Blank slot 6
(both MAIN and SUB blank). Cert lands at slot 7 SUB. This is MAIN parity at the
start of slot 7 (slot 7 MAIN = blank), so cert goes in SUB. Correct.

### 032025olsen (DRIFTS at cert → cascades to exhibits)

```
slot 5 MAIN: Examination     slot 5 SUB: Mr. Knight 7
slot 6 MAIN: [blank]         ORACLE slot 6 SUB: Reporter's Certificate 199
                             RENDERER slot 6 SUB: [blank]
slot 7 MAIN: [blank]         RENDERER slot 7 MAIN: Reporter's Certificate 199
```
Prior section ends at slot 5 SUB. Next available is slot 6 MAIN (blank) → slot 6 SUB.
Oracle places cert at slot 6 SUB. Renderer places cert at slot 7 MAIN (1 slot late).
This +1 cascades through the rest of the INDEX page, causing oscillating drift in
the exhibits section.

### 060122williams (Re-Exam nav misalignment → +2 on all 22 exhibits)

```
slot 5 MAIN: Examination     slot 5 SUB: Mr. Leefe 8
ORACLE  slot 6 MAIN: Mr. Gileson 198   slot 6 SUB: Re Examination
ORACLE  slot 7 MAIN: Mr. Leefe 204
RENDERER slot 6 MAIN: [blank]  slot 6 SUB: Mr. Gileson 198
RENDERER slot 7 MAIN: Re Examination   slot 7 SUB: Mr. Leefe 204
```
Prior section ends slot 5 SUB. Oracle starts next nav group (Re-Exam) at slot 6 MAIN.
Renderer starts it at slot 6 SUB — 1 position late. This 1-slot error persists through
cert → * * * → EXHIBITS → exhibits, arriving at exhibits 2 slots late (the cert+witness
accumulation adds 1 more shift).

### 082222butler and 101322blanks (exhibit-start position wrong)

```
slot 10 MAIN: [blank]        ORACLE slot 10 SUB: EXHIBITS
                             RENDERER slot 10 MAIN: EXHIBITS
slot 11 MAIN: [blank]        ORACLE slot 11 SUB: Exhibit No. 1...
                             RENDERER slot 11 MAIN: Exhibit No. 1...
```
Same slot number (11), different position. Oracle uses SUB-first for exhibit entries
(carrying from the parity established by EXHIBITS header in SUB). Renderer resets to
MAIN for exhibit entries. For short exhibits the slot count is equal; for multi-line
exhibits renderer uses 1 fewer slot (MAIN+SUB in one slot vs SUB+MAIN across two).

## FOR OPUS: WHAT B1.9.3 MUST DO

### The spec target

One fix: carry the MAIN/SUB cycle state as a single variable (`next_is_main: bool`)
through the entire front-matter section rendering — appearances section, nav section,
cert entries, separators, and exhibits entries — without ever resetting it at section
boundaries.

The only place `next_is_main` resets to True is at the START of a new page (slot 1).

### What to preserve (already correct)

- Halprin: 23/23 exhibits correct, cert correct, appearances correct — do NOT break.
- Black_bp: 23/28 correct — do NOT break.
- The main/sub cycle within exhibits entries (the loop itself works).

### Failure modes to avoid

- B1.9.2 failed because removing blank-insertion at firm boundaries changed total
  slot count → halprin front matter changed from 10 to 11 pages. Any fix that changes
  total slot count on a depo that currently works is wrong.
- Do not insert explicit blanks at section transitions. The cycle parity handles it.
- Do not "reset to MAIN" at section boundaries. Thread the state.

### Recommended implementation approach

In `src/stage5/front_matter/index.py` (or wherever the slot allocator lives):
1. Find where `next_is_main` (or equivalent) is reset at section boundaries.
2. Remove those resets.
3. Let each content item claim the next available position from the running cycle.
4. A content item that "starts" a section (cert, EXHIBITS header, first exhibit) simply
   takes whatever `next_is_main` says.

The blank MAIN slot before cert (in the 0-drift cases) emerges naturally because:
prior section ends at SUB → `next_is_main = True` → cert goes in MAIN of next slot.
Or if prior section ends at MAIN → `next_is_main = False` → cert goes in SUB of current
slot — no blank inserted.

### Test targets (in priority order)

1. halprin: must remain 23/23 exhibits, cert at slot 7 SUB, appearances unchanged
2. olsen: cert must move from slot 7 MAIN → slot 6 SUB; exhibits must start drifting
   toward 0 (some will still not match due to D-5 Mode C position parity — acceptable)
3. williams: first exhibit must move from slot 14 → slot 12 (remove +2 nav shift)
4. butler/blanks: exhibit 1 must move from MAIN → SUB
5. black_bp: must remain clean (23/28)

### What counts as a ship

Halprin (10 front pages, all sections correct) plus at least 2 of the 5 other depos
showing measurable drift reduction. Log remaining outliers as TODO in the commit.

## HANDOFF CHECKLIST FOR OPUS

- [ ] Read all 8 ramp files before writing a line of spec
- [ ] Confirm B1.9.3 scope in ONE sentence to Scott
- [ ] State the 3 standing rules (RULE-19, RULE-20, 80/20) before drafting
- [ ] Task Sonnet #2 in laneB only
- [ ] Pre-flight before every commit
- [ ] If halprin breaks on first test run, STOP and revert — do not iterate blind

## WHAT SCOTT DOESN'T WANT

- Re-auditing anything. The data is in the three files.
- Questions about what the oracle "really intends." We know.
- A fourth attempt at a narrow fix. B1.9.3 is the unified fix or nothing.
