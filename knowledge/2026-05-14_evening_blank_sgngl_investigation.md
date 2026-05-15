# Blank .sgngl Investigation — 2026-05-14 Evening

## Summary

All three files that loaded blank in CATalyst tonight were **opened from the wrong location** — AutoArchive backups that are missing their companion files. Two have confirmed good copies. One (Yocke) is more complex.

---

## File 1 — Stutz (072821PROG-FINAL MATTHEW STUTZ)

**Opened from:** `C:\Cat4\usr\scott\AutoArchive\ASAP\072821PROG-FINAL MATTHEW STUTZ.sgngl`
**File size:** 659,286 bytes (not empty — content is there)

**Root cause:** AutoArchive only saves the `.sgngl` binary. No companion files exist in that folder. CATalyst needs the full family (.sgdct, .sgxml, .sgglb, .sgstn, etc.) to render the transcript. Without them = blank screen.

**Good copy exists:**
`C:\Cat4\usr\scott\ASAP\072821PROG-F. MATTHEW STUTZ.sgngl`
- Same size: 659,286 bytes
- Has full sibling set: .sgdcg, .sgdct, .sgdcu (0 bytes — normal), .sgdcx, .sgglb, .sgstn, .sgxml, .tlx
- SGXML confirms: State=7 "ASCII Created", 185 pages, GUID: d27c4733-9c67-451e-bba5-9507f81c7134
- Edit-User: `C:\Cat4\usr\Mary Beth` (MB's job — expected)

**Action for Scott:** Open `C:\Cat4\usr\scott\ASAP\072821PROG-F. MATTHEW STUTZ.sgngl` instead.

---

## File 2 — Yocke (072921ROUGHDRAFT M. YOCKE)

**Opened from:** `C:\Cat4\usr\scott\ASAP\072921ROUGHDRAFT M. YOCKE.sgngl`
**File size:** 1,202,554 bytes

**Different problem.** This file HAS its companion files. They are all present:

| File | Size |
|------|------|
| .sgdcg | 22,524 |
| .sgdct | 640 (small but present) |
| .sgglb | 82,587 |
| .sgngl | 1,202,554 |
| .sgstn | 530,440 |
| .sgxml | 15,882 |
| .tlx | 243 |
| .sgdcu | **MISSING** (no file at all) |

**SGXML anomaly:** State = 5 "Final Printed" — but the file is named ROUGHDRAFT. This mismatch suggests the status field was updated after a final-print run, even though the content is a rough.

**Dictionary paths in SGXML:** All hardcoded to `C:\Cat4\usr\Mary Beth\` — those paths don't exist on Scott's machine. This can cause CATalyst to open the job but fail to load steno context, though it shouldn't make the *text* blank.

**Most likely cause:** CATalyst is opening the file but finding a GUID or user-lock conflict with Scott's user profile. The .sgdcu (user customization file) is completely absent — this is the one file CATalyst expects to write per-user state to, and its total absence (not 0 bytes) may be causing a display failure.

**Possible fixes (in order of ease):**
1. Create an empty `.sgdcu` file in the same folder: `072921ROUGHDRAFT M. YOCKE.sgdcu` — CATalyst may then generate it fresh and display correctly
2. Try File > Open Read-Only in CATalyst
3. Re-import: CATalyst → File → Import from .sgngl

**Note:** An AutoArchive copy also exists at `C:\Cat4\usr\scott\AutoArchive\ASAP\072921ROUGHDRAFT M. YOCKE.sgngl` (1,202,553 bytes — 1 byte smaller). The live copy is authoritative.

---

## File 3 — Hornbeck FINAL (111517hornbeck-FINAL)

**Opened from:** `C:\Cat4\usr\scott\AutoArchive\FOR MB\111517hornbeck.SGNGL`
**File size:** 931,335 bytes (not empty)

**Root cause:** Same as Stutz. AutoArchive backup — only `.sgngl`, no companion files in that folder.

**Good copy exists:**
`C:\Cat4\usr\scott\FOR MB\111517hornbeck-FINAL.SGNGL`
- Same size: 931,335 bytes
- Has full sibling set: .SGDCT (15,680), .SGNGL (931,335), .SGSTN (415,840), .SGXML (18,757), .sgdcg (0 bytes — normal), .sgdcu (1,916), .sgdcx (16,212), .sgglb (78,368), .tlx (592)
- This is the complete, healthy copy

**Action for Scott:** Open `C:\Cat4\usr\scott\FOR MB\111517hornbeck-FINAL.SGNGL` instead.

Also exists at: `C:\Cat4\usr\scott\before 2019\111517hornbeck.SGNGL` (919,206 bytes — slightly smaller, probably an earlier version).

---

## Pattern Summary

| Depo | Root Cause | Has Good Copy? | Good Copy Path |
|------|-----------|----------------|----------------|
| Stutz | AutoArchive backup — no sibling files | YES | `C:\Cat4\usr\scott\ASAP\072821PROG-F. MATTHEW STUTZ.sgngl` |
| Yocke | Siblings present but .sgdcu missing; user-lock conflict likely | MAYBE | Try fix steps above |
| Hornbeck | AutoArchive backup — no sibling files | YES | `C:\Cat4\usr\scott\FOR MB\111517hornbeck-FINAL.SGNGL` |

**Rule of thumb going forward:** Never open directly from `AutoArchive\` — it's a backup store. The live versions in `ASAP\`, `FOR MB\`, or `Billable\` are the ones with full sibling sets.

---

*Investigation by Sonnet #2 Recon Agent — 2026-05-14 evening*
*Job 1 (11-pair Stage A analysis) pending Sonnet #1 output file*
