# PRE-FLIGHT CHECK SPEC v1
**Locked:** 2026-05-05
**Owner:** Scott
**Scope:** Every full pipeline run, every single time.

## Why this exists
On 2026-05-04 we burned an evening and $6 of API spend running Brandl
against the wrong input file (a FINAL, not a ROUGH). The diff results
were worthless. We will not do that again. Before any pipeline run we
run this checklist. No exceptions.

## The Rule
NO Stage 2 / Stage 3 / Stage 4 / Stage 5 run starts before pre-flight
returns READY. If pre-flight returns NOT READY, the gaps close first.
Stage 1 dry runs are allowed (free, local, recon only) and are part of
the pre-flight itself.

## Locked context (current scope)
- Reporter: MB (Mary Beth Muir, CCR RPR)
- State: Louisiana
- Profile flag: --profile mb
- Stage 1 calibration: CaseCATalyst v22.13 RTF, smd suffix family

When scope expands (new reporter or new state), this spec versions up
BEFORE that reporter's first run.

## Required inputs (both must be present)

### 1. ROUGH RTF — the engine input
- File type: .rtf
- Source: CaseCATalyst export, version 22.13 or compatible
- Suffix family: must contain `smd` (e.g., `_Tsmd`, `_smd_T`)
- State: pre-edit, raw steno output BEFORE reporter scoping
- NOT accepted: any file with `FINAL` in the name, scoped/edited files,
  .txt, .pdf, .sgxr2, .docx, .sgngl
- Reference shape: matches Halprin working file
  `040226yellowrock-ROUGH_Tsmd.rtf`

### 2. FINAL RTF — the diff oracle
- File type: .rtf
- Source: CaseCATalyst export of the MB-finalized transcript
- Purpose: gold standard the engine output is compared against
- Required for: any diff / scoring / analysis run
- NEVER used as engine input — only as diff target

## Optional inputs (improve quality if present, do not block)
- `.sgxml` — CaseCAT job metadata
- `.opus` — session audio (saved for Stage 4 future)
- `.sgdct` — MB's job dictionary
- `case_info` package — names, attorneys, dates, exhibits
- `NAMES_LOCK` — proper nouns to preserve verbatim

## The pre-flight procedure

Sonnet runs these four checks in order. Reports back one verdict:
READY or NOT READY (with gaps and lightest fix per gap).

### CHECK 1 — Required files present
- ROUGH RTF exists at expected path
- FINAL RTF exists at expected path
- Both filenames match the format spec above
- FAIL = NOT READY

### CHECK 2 — Stage 1 dry run on the ROUGH
- Run Stage 1 only (no API spend, no commits)
- Report: unknown-style-code warning count, turn count, reconciliation result
- Pass criteria: 0 unknown style code warnings AND reconciled = True
- FAIL = NOT READY

### CHECK 3 — Run-script audit
- All run scripts (Stage 1, 2, 3, 5, diff) point at the correct ROUGH as input
- All diff / oracle paths point at the correct FINAL
- Profile flag = --profile mb
- Pass criteria: zero edits required
- FAIL = NOT READY (list edits needed)

### CHECK 4 — Halprin parity
- For each Halprin asset in the working setup (case_info, NAMES_LOCK, custom dicts, config flags), confirm new-depo equivalent exists
- List any Halprin asset with no counterpart
- Each missing counterpart = NOT READY

### VERDICT
One line: READY OR NOT READY — gaps: [list]
For each gap, lightest fix (file to obtain, script to edit, etc).

## Gap remediation playbook

| Missing item     | Scott's job                                              | Sonnet's job                                       |
|------------------|----------------------------------------------------------|----------------------------------------------------|
| ROUGH RTF        | Get smd-suffix RTF from MB or re-export from CaseCAT     | (waits)                                            |
| FINAL RTF        | Get from MB's delivery package                           | (waits)                                            |
| case_info        | Confirm whether this depo needs custom case_info         | Build it from FINAL if missing, await approval     |
| NAMES_LOCK       | Provide names/attorneys list                             | Auto-extract candidates from FINAL, Scott approves |
| Run-script paths | (waits)                                                  | Edit scripts in place, no commits, await approval  |

## When this spec gets bypassed
NEVER. If Scott explicitly says "skip pre-flight," Sonnet still runs the checklist silently and reports the verdict before any spend. The point is to never burn money on a known-bad setup.

---
PREFLIGHT_CHECK_v1.md — Built 2026-05-05 from lessons learned in the Brandl FINAL_T mistake.
