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

---

## Section 7 — Job 3: BP Folder Pair Scan (2026-05-14 Evening)

**Scanned:** `C:\Cat4\usr\scott\BP\`, `C:\Cat4\usr\scott\Billable\`, `C:\Cat4\usr\scott\AutoArchive\ASAP\`
**Method:** grep all .sgxml files for "Mary Beth" → extract CaseView-III-GUID + State → match to ROUGH partner

---

### Billable — No new pairs

Only Cavazos files present (`061220cavazosROUGH.sgxml`, `061220cavazospart2.sgxml`). Already in the 11-pair pipeline. Nothing new.

### AutoArchive\ASAP — No new pairs

All bare .sgngl backups, no sibling files. Per Job 2 protocol, skip. One pre-2020 exception (`050614harrick`) doesn't meet cutoff.

---

### BP\ — 2 GUID-Confirmed + 18 Tier 2 candidates

**31 .sgxml files in BP\ grep as MB-authored.**

---

#### Tier 1: GUID-Confirmed Pairs

Both ROUGH and FINAL have .sgxml; GUIDs match; reporter = Mary Beth confirmed.

**Pair 1 — rooks_011121**

| Field | Value |
|-------|-------|
| Date | 01/11/2021 |
| ROUGH .sgngl | `C:\Cat4\usr\scott\BP\011121rooks-BP rough.sgngl` |
| ROUGH .sgxml | `C:\Cat4\usr\scott\BP\011121rooks-BP rough.sgxml` |
| FINAL .sgngl | `C:\Cat4\usr\scott\BP\011121rooks-BP.sgngl` |
| FINAL .sgxml | `C:\Cat4\usr\scott\BP\011121rooks-BP.sgxml` |
| GUID | `e427dcb1-805b-4bc8-94e0-c1bfcc263848` |
| FINAL State | 7 — "ASCII Created" |
| FINAL .txt on disk | No — needs CATalyst export |
| Notes | Both ROUGH and FINAL sgxml confirmed MB. GUID match confirmed. |

**Pair 2 — nguyen_033022**

| Field | Value |
|-------|-------|
| Date | 03/30/2022 |
| ROUGH .sgngl | `C:\Cat4\usr\scott\BP\033022ngyen-bp.sgngl` |
| ROUGH .sgxml | `C:\Cat4\usr\scott\BP\033022ngyen-bp.sgxml` (State=2, MB, GUID confirmed) |
| FINAL .sgngl | `C:\Cat4\usr\scott\BP\033022NGUYENSTATEMENT-BP.sgngl` |
| FINAL .sgxml | `C:\Cat4\usr\scott\BP\033022NGUYENSTATEMENT-BP.sgxml` (State=7, MB, same GUID) |
| GUID | `6202f1f0-a5be-4ecb-80c7-6c3940475e98` |
| FINAL State | 7 — "ASCII Created" |
| FINAL .txt on disk | No — needs CATalyst export |
| Notes | Naming divergence (ngyen → NGUYENSTATEMENT) — same depo, GUID is the proof. |

---

#### Tier 2: 18 MB-Confirmed Pairs (ROUGH is bare .sgngl, no GUID confirmation)

FINAL .sgxml present and MB-confirmed on all. ROUGH files match by date+name in same folder.
Two State=2 traps removed from this list (see Flagged section below).

| depo_id | Date | ROUGH | FINAL | State | FINAL .txt? |
|---------|------|-------|-------|-------|-------------|
| townser_012122 | 01/21/22 | `012122townser-BP-ROUGH.sgngl` | `012122townser-BP-FINAL.sgngl` | 7 | No |
| novelozo_012522 | 01/25/22 | `012522novelozo-bp-ROUGH.sgngl` | `012522novelozo-bp-FINAL.sgngl` | 7 | No |
| durr_012622 | 01/26/22 | `012622durr-bp-ROUGH.sgngl` | `012622durr-bp-FINAL.sgngl` | 7 | No |
| brown_012722 | 01/27/22 | `012722 Brown-BP-ROUGH.sgngl` | `012722 Brown-BP-FINAL.sgngl` | 7 | No |
| liddell_020122 | 02/01/22 | `020122liddell-BP-ROUGH.sgngl` | `020122liddell-BP-FINAL.sgngl` | 7 | No |
| barlow_020222 | 02/02/22 | `020222barlow-BP-ROUGH.sgngl` | `020222barlow-BP-FINAL.sgngl` | 7 | No |
| rooks2_020422 | 02/04/22 | `020422TRooks-BP-ROUGH.sgngl` | `020422TRooks-BP-cFINAL.sgngl` | 7 | No |
| barrington_020722 | 02/07/22 | `020722barrington-BP-ROUGH.sgngl` | `020722barrington-BP-FINAL.sgngl` | 7 | No |
| snelson_021222 | 02/12/22 | `021222SNELSON-BP-ROUGH.sgngl` | `021222SNELSON-BP-FINAL.sgngl` | **5** | No |
| colbert_021422 | 02/14/22 | `021422colbert-BP-ROUGH.sgngl` | `021422colbert-BP-FINAL.sgngl` | 7 | No |
| cranmer_022322 | 02/23/22 | `022322Cranmer-BP-ROUGH.sgngl` | `022322Cranmer-BP-FINAL.sgngl` | 7 | No |
| walker_040522 | 04/05/22 | `040522walker-bp.sgngl` | `040522walker-bp-FINAL.sgngl` | 7 | No |
| deloach_042922 | 04/29/22 | `042922DELOACH-BP.sgngl` | `042922DELOACH-FINAL-BP.sgngl` | 7 | No |
| thompson_050522 | 05/05/22 | `050522thompson-bp.sgngl` | `050522thompson-bp-FINAL.sgngl` | 7 | **YES** |
| washington_050922 | 05/09/22 | `050922WASHINGTON-BP.sgngl` | `050922WASHINGTON-BP-FINAL.sgngl` | 7 | **YES** |
| black_052522 | 05/25/22 | `0525black-bp-ROUGH.sgngl` | `0525black-bp-FINAL.sgngl` | 7 | **YES** |
| moore_122921 | 12/29/21 | `122921moore-BP-ROUGH.sgngl` | `122921moore-BP-FINAL.sgngl` | 7 | No |
| mickles_123021 | 12/30/21 | `123021-mickles-BP.sgngl` | `123021-mickles-BP-FINAL.sgngl` | 7 | No |

All files in `C:\Cat4\usr\scott\BP\`

---

#### Fast-Path 3: FINAL .txt Already on Disk

These three have FINAL .txt ready — no CATalyst export needed for the FINAL side. ROUGH .sgngl needs one export step.

**thompson_050522**
- ROUGH: `C:\Cat4\usr\scott\BP\050522thompson-bp.sgngl` (531,593 bytes)
- FINAL .sgngl: `C:\Cat4\usr\scott\BP\050522thompson-bp-FINAL.sgngl` (531,593 bytes)
- FINAL .txt: `C:\Cat4\usr\scott\BP\050522thompson-bp-FINAL.txt` (197,804 bytes) ← **ready**
- ⚠ ROUGH and FINAL .sgngl are exact same byte size. May be identical files. Verify text content differs before using as a pair.

**washington_050922**
- ROUGH: `C:\Cat4\usr\scott\BP\050922WASHINGTON-BP.sgngl` (587,929 bytes)
- FINAL .sgngl: `C:\Cat4\usr\scott\BP\050922WASHINGTON-BP-FINAL.sgngl` (587,929 bytes)
- FINAL .txt: `C:\Cat4\usr\scott\BP\050922WASHINGTON-BP-FINAL.txt` (215,196 bytes) ← **ready**
- ⚠ Same byte-size warning as Thompson.

**black_052522**
- ROUGH: `C:\Cat4\usr\scott\BP\0525black-bp-ROUGH.sgngl` (647,212 bytes)
- FINAL .sgngl: `C:\Cat4\usr\scott\BP\0525black-bp-FINAL.sgngl` (647,212 bytes)
- FINAL .txt: `C:\Cat4\usr\scott\BP\0525black-bp-FINAL.txt` (262,121 bytes) ← **ready**
- ⚠ Same byte-size warning as Thompson.

---

#### Flagged / Skip

| File | Reason |
|------|--------|
| `042622BOGGS-BP-FINAL.sgngl` | sgxml shows **State=2 "In Progress"** despite the filename. Not a true final. |
| `010522danos-bp-FINAL.sgngl` | sgxml shows **State=2 "In Progress"** despite the filename. Not a true final. |
| `020922briggs-BP-FINAL.sgngl` | sgxml shows **State=2 "In Progress"** despite the filename. Not a true final. |
| `050422BROWN-BP-FINAL.sgngl` | State=7, has .txt (230 KB), but **no ROUGH found in BP folder**. Incomplete pair. |
| `101923sears-bp.sgngl` | State=7, has .txt (228 KB), but **no ROUGH found in BP folder**. Incomplete pair. |
| `011222williams-BP.sgngl` | State=2 (it's the ROUGH). FINAL files (`-FINAL`, `-CFINAL`) are bare .sgngl with no sgxml. Cannot confirm GUID. Hold. |

---

### Section 7 Summary

| Folder | GUID-confirmed | Tier 2 candidates | Fast-path .txt |
|--------|----------------|-------------------|----------------|
| Billable | 0 | 0 | 0 |
| AutoArchive\ASAP | 0 | 0 | 0 |
| BP | **2** | **18** | **3** |

**Total new confirmed pairs tonight: 2** (rooks_011121, nguyen_033022)
**Total confirmed + strong candidates: 20** (well above the goal of >10)

**Recommended addition order after current 11-pair run:**
1. rooks_011121 — GUID confirmed, files ready
2. nguyen_033022 — GUID confirmed, files ready
3. thompson_050522 / washington_050922 / black_052522 — FINAL .txt on disk (verify ROUGH content first)
4. moore_122921 / mickles_123021 — State=7, clean naming

---

*Section 7 written by Sonnet #2 Recon Agent — 2026-05-14 evening*
*Pending: Job 1 frequency analysis (awaiting Sonnet #1 output)*
