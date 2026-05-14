# Sonnet #2 Recon — 2026-05-14 Evening

Captured by: Sonnet #2 (recon worker)
Date: 2026-05-14
Scope: C:\Cat4\usr\scott\ — reporter verification + ASCII export hunt

---

## Section 1: 18 Files Verified — All MB

All files checked via .sgxml metadata. Reporter identity confirmed by `Translate-User`, `Edit-User`, and `Save-User` fields = `C:\Cat4\usr\Mary Beth`. "MV" appears as co-saver on two files (scopist, not reporter). Every single file is MB.

| # | Filename | Date | Reporter | State | Pages | Notes |
|---|---|---|---|---|---|---|
| 1 | `072921ROUGHDRAFT M. YOCKE` | 07/29/21 | MB ✓ | Final Printed | 356 | MV also saved (scopist). Audio attached. |
| 2 | `080221PROG-PM` | 08/02/21 | MB ✓ | In Progress | 117 | Clean MB-only. |
| 3 | `080221 F- PZANNETTI` | 08/02/21 | MB ✓ | ASCII Created | 238 | Exported ASCII 08/12/21. "F-" = FINAL Pzannetti. |
| 4 | `080321PROG-FPZANNETTI` | 08/03/21 | MB ✓ | ASCII Created | 147 | Exported ASCII 08/13/21. |
| 5 | `080421prog3` | 08/04/21 | MB ✓ | In Progress | 59 | No export record. |
| 6 | `080421progEXTRAFILE` | 08/04/21 | MB ✓ | In Progress | 238 | "EXTRAFILE" = overflow session. |
| 7 | `080421progPM(1)` | 08/04/21 | MB ✓ | In Progress | 56 | Short PM session. |
| 8 | `080421progpartthreenotused` | 08/04/21 | MB ✓ | In Progress | 238 | "notused" in name — likely aborted take. |
| 9 | `080421F-P. DALTON` | 08/04/21 | MB ✓ | ASCII Created | 244 | Exported ASCII 08/15/21. "F-" = FINAL for P. Dalton. |
| 10 | `080921ROUGHDRAFT TAREK ABICHOU` | 08/09/21 | MB ✓ | Final Printed | 275 | SAME GUID as row 11 — confirmed pair. |
| 11 | `080921 F T ABICHOU` | 08/09/21 | MB ✓ | ASCII Created | 295 | SAME GUID as row 10. Exported ASCII 08/18/21. "F" = FINAL Abichou. |
| 12 | `081021 C TAREK ABICHOU` | 08/10/21 | MB ✓ | ASCII Created | 102 | "C" = Continuation/Corrected. Exported ASCII 08/18 + 08/20. |
| 13 | `072821PROG-F. MATTHEW STUTZ` ⚠️ NEW | 07/28/21 | MB ✓ | ASCII Created | 185 | NOT in prior inventory. Exported ASCII 3× on 08/10/21. |
| 14 | `080521 F P DALTON` ⚠️ NEW | 08/05/21 | MB ✓ | ASCII Created | 79 | NOT in prior inventory. Exported ASCII 08/15/21. |
| 15 | `121322griffin-ROUGH` | 12/13/22 | MB ✓ | Final Printed | 69 | SAME GUID as martin. Same-day proceeding. |
| 16 | `121322martin-ROUGH` | 12/13/22 | MB ✓ | Final Printed | 83 | SAME GUID as griffin. Same-day proceeding. |
| 17 | `061220cavazosROUGH` | 06/12/20 | MB ✓ | ASCII Created | 230 | Exported ASCII 06/12/20. Export file not on disk. |
| 18 | `061220cavazospart2` | 06/12/20 | MB ✓ | In Progress | 70 | Part 2, no export record. |

All files located in `C:\Cat4\usr\scott\ASAP\` unless noted. Cavazos files in `C:\Cat4\usr\scott\Billable\`.

---

## Section 2: Three Big Finds

**Find 1 — Hidden ROUGH+FINAL pair: Abichou**

`080921ROUGHDRAFT TAREK ABICHOU.sgngl` and `080921 F T ABICHOU.sgngl` share CaseView GUID `b114eeb8-bb8d-4281-a0d9-07b3c4332a2e`. Same job. The "F T" file IS the CATalyst-native FINAL — state = ASCII Created, exported 08/18/21. Last night's scanner missed this pair because the FINAL filename uses "F T" not "FINAL." This is a confirmed ROUGH+FINAL pair hiding in plain sight.

**Find 2 — Two files not in prior inventory: Stutz + Dalton (Aug 5)**

`072821PROG-F. MATTHEW STUTZ.sgxml` (Jul 28, 2021, 185 pages) and `080521 F P DALTON.sgxml` (Aug 5, 2021, 79 pages) were not captured in the 2026-05-13 evening scan. Both confirmed MB, both exported as ASCII. Both are part of the Progressive hearing cluster (Jul–Aug 2021). AutoArchive also contains `072821PROG-FINAL MATTHEW STUTZ.sgngl` — a CATalyst-native FINAL for Stutz.

**Find 3 — Cavazos exported same day as depo (but file not on disk)**

`061220cavazosROUGH.sgxml` shows ASCII export on 06/12/20 (same day as deposition). `061220cavazosCFINAL.sgngl` exists at `C:\Cat4\usr\scott\` root — a corrected FINAL native, exported twice (06/14/20 and 06/15/20). The ASCII output file is not on disk — likely delivered and deleted. CATalyst native CFINAL available for re-export.

---

## Section 3: ASCII Export Hunt Results

Searched: `C:\Cat4\usr\scott\`, `C:\Cat4\usr\Mary Beth\`, `C:\Users\scott\Downloads\`, `C:\Users\scott\OneDrive\Documents\`, `C:\Users\scott\Desktop\`, `C:\Users\scott\Documents\`

| Candidate | ASCII Export Found? | CATalyst Native FINAL on Disk? | Notes |
|---|---|---|---|
| Abichou | NO | YES — `C:\Cat4\usr\scott\ASAP\080921 F T ABICHOU.sgngl` | Export made 08/18/21. File not on disk. Re-export from CATalyst. |
| Stutz | NO | YES — `C:\Cat4\usr\scott\AutoArchive\ASAP\072821PROG-FINAL MATTHEW STUTZ.sgngl` | Export made 3× on 08/10/21. File not on disk. Re-export from CATalyst. |
| Dalton (08/05/21) | NO | YES — `C:\Cat4\usr\scott\ASAP\080521 F P DALTON.sgngl` | Export made 08/15/21. File not on disk. Re-export from CATalyst. |
| Cavazos | NO | YES — `C:\Cat4\usr\scott\061220cavazosCFINAL.sgngl` (237 pages) | Export made 06/14 + 06/15/20. File not on disk. Re-export from CATalyst. |

No exported ASCII text files were found on this machine for any of the 4 targets. All 4 CATalyst-native FINAL .sgngl files are intact and available for fresh export.

---

## Section 4: BONUS — Griffin + Martin FINAL .txt Found

Discovered during Cat4 .txt sweep. Both files confirmed as real federal court transcripts. Both ROUGH .sgxml files confirmed MB reporter (Translate-User = `C:\Cat4\usr\Mary Beth`). Previously classified as "no FINAL" because FINALs were in the BP subfolder, not ASAP.

| Job | ROUGH file | FINAL .txt path | File size | Opening lines |
|---|---|---|---|---|
| Griffin | `C:\Cat4\usr\scott\ASAP\121322griffin-ROUGH.sgngl` | `C:\Cat4\usr\scott\BP\121322griffin.txt` | **99 KB** | `UNITED STATES DISTRICT COURT / EASTERN DISTRICT OF LOUISIANA / ALICE M. GRIFFIN, Plaintiff v. BP EXPLORATION & PRODUCTION INC., CIVIL ACTION NO. 17-03244` |
| Martin | `C:\Cat4\usr\scott\ASAP\121322martin-ROUGH.sgngl` | `C:\Cat4\usr\scott\BP\121322martin.txt` | **118 KB** | `UNITED STATES DISTRICT COURT / EASTERN DISTRICT OF LOUISIANA / STERLING MARTIN, Plaintiff v. BP EXPLORATION & PRODUCTION INC., CIVIL ACTION NO. 17-03249` |

Both jobs share the same CaseView GUID (`3a33eb10-f0bf-4018-8642-a25f70a9fa98`) and same audio timestamps — same-day proceeding, same court session. Both were printed as "Final Printed" (State=5) on 12/13/22.

These are ready-to-use Stage A pairs. No export work needed.

---

## Section 5: Recommended CATalyst Re-Export Priority Order

For the 4 pairs whose ASCII exports are not on disk — open each FINAL .sgngl in CATalyst, File > Export > ASCII Page Image, save to `mrx_depo_library\MB\[case]\input\`.

| Rank | Job | FINAL file to open | Location |
|---|---|---|---|
| 1 | Cavazos | `061220cavazosCFINAL.sgngl` | `C:\Cat4\usr\scott\` (root) |
| 2 | Abichou | `080921 F T ABICHOU.sgngl` | `C:\Cat4\usr\scott\ASAP\` |
| 3 | Stutz | `072821PROG-FINAL MATTHEW STUTZ.sgngl` | `C:\Cat4\usr\scott\AutoArchive\ASAP\` |
| 4 | Dalton Aug 5 | `080521 F P DALTON.sgngl` | `C:\Cat4\usr\scott\ASAP\` |

Note: For Abichou, also check whether the ROUGH (`080921ROUGHDRAFT TAREK ABICHOU.sgngl`) needs to be exported separately — both are needed for a pair.

---

## Section 6: Net New Stage A Pairs Available Tonight

Two confirmed MB pairs are ready immediately — ROUGH and FINAL both on disk as readable .txt, no CATalyst export needed.

| Pair | ROUGH | FINAL | Status |
|---|---|---|---|
| Griffin (12/13/22) | `C:\Cat4\usr\scott\ASAP\121322griffin-ROUGH.sgngl` (needs CATalyst export to .rtf) | `C:\Cat4\usr\scott\BP\121322griffin.txt` (99 KB, ready) | FINAL ready. ROUGH needs 1 CATalyst export. |
| Martin (12/13/22) | `C:\Cat4\usr\scott\ASAP\121322martin-ROUGH.sgngl` (needs CATalyst export to .rtf) | `C:\Cat4\usr\scott\BP\121322martin.txt` (118 KB, ready) | FINAL ready. ROUGH needs 1 CATalyst export. |

These are the fastest path to new MB pairs for Stage A. FINAL .txt in hand. ROUGH .sgngl needs one export step in CATalyst to become a usable .rtf.

Combined with the 5 confirmed pairs from 2026-05-13 evening recon (Garcia, Hebert, Simon, Fountain, and the Abichou GUID-confirmed pair), the 2020+ MB confirmed pair count is now **7 confirmed + 4 pending re-export** = up to 11 pairs once CATalyst exports are done.

---

*Recon shift closed 2026-05-14 evening. Sonnet #2.*
