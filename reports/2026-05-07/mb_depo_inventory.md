# MB Depo Inventory + Library Proposal

**Date:** 2026-05-07
**Scope:** All MB deposition packages found in `C:\Users\scott\OneDrive\Documents` and `C:\Users\scott\Downloads`

---

## Part 1 — Inventory

### Summary Table

| Depo | Date | Witness | Case | Raw RTF | Audio | FINAL | Current Home |
|---|---|---|---|---|---|---|---|
| Brandl | 032626 | Brad Brandl | YellowRock | ✅ 2.1MB | ✅ 99MB opus | ✅ RTF + TXT | `mb_Yellow_Brad_Brandl/` + ORACLES |
| Halprin | 040226 | Halprin | YellowRock | ✅ 1.7MB | ✅ 76MB opus | ✅ RTF + TXT | `mb_040226_halprin_yellowrock/` + oracle/finals |
| Easley | 031326 | Easley | YellowRock | ✅ 1.3MB | ✅ 86MB opus | ✅ PDF only | scattered (5+ folders) |
| Hammond | 020926 | Hammonds/Montz | LA | ❌ PDF only | ❌ none | ✅ PDF | `MD_demo_engine_LA_hammond/` |
| Wade | 0323 | Wade/Pearce | NY WCB | ✅ 44KB | ❌ none | ✅ PDF + TXT | `AD_wade_0323/` |
| Fourman | 0324 | Fourman | NY WCB | ✅ 103KB | ❌ none | ✅ PDF + TXT | `ad_foreman_0324/` |
| Soyer | 0320 | Soyer/Pearce | NY WCB | ❌ missing | ❌ none | ✅ TXT + PDF | `TestHarness_Run_NY1/` |
| Gotesman | 0316 | Gotesman | NY WCB | ⚠️ unclear | ⚠️ MP3 6.5MB | ✅ PDF only | `alicia_demo/` |
| Bertolet | unknown | Todd Bertolet | unknown | ❌ missing | ❌ none | ✅ PDF | Downloads only |

---

### Depo 1 — Brandl (YellowRock 032626)

**Status:** CANONICAL — active in mrx_engine_v1 pipeline

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF (smd_T) | `Documents/mb_Yellow_Brad_Brandl/032626YELLOWROCK_smd_T.rtf` | 2.1MB | Mar 27 |
| CaseCATalyst bundle | `Downloads/depofiles/032626YELLOWROCK TO SCOTT/` | ~141MB | Apr 2 |
| CaseCATalyst extracted | `Downloads/brandl_extracted/` | ~141MB | Apr 7–19 |
| FINAL_T.RTF (oracle) | `Documents/MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE/032626YELLOWROCK-FINAL_T.rtf` | 2.2MB | Apr 19 |
| Audio (oracle) | `Documents/MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE/032626YELLOWROCK-FINAL.opus` | 99MB | Mar 26 |
| Original zip | `Documents/MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE_ORIGINAL.zip` | 129MB | Apr 19 |
| FINAL.txt (mrx-context) | `Documents/mrx-context/oracle/finals/brandl/BRANDL_MB_FINAL.txt` | 278KB | Apr 29 |
| Raw rough PDF | `Downloads/depofiles/032626YELLOWROCK-ROUGH.pdf` | 1.4MB | Mar 30 |

**Notes:**
- Most complete package of any depo. Two copies of the CaseCATalyst bundle (Downloads/depofiles and brandl_extracted).
- FINAL_T.RTF is the authoritative oracle input for the engine pipeline.
- The `mb_Yellow_Brad_Brandl/` folder also contains v4 engine scaffolding (ai_engine.py, style modules) — NOT part of the oracle package.

---

### Depo 2 — Halprin (YellowRock 040226)

**Status:** Active in mrx_engine_v1 pipeline (second depo after Brandl)

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF stub | `Documents/mb_040226_halprin_yellowrock/040226yellowrock-ROUGH.rtf` | 5.2KB | Apr 25 |
| Raw RTF (smd_T) | `Documents/mb_040226_halprin_yellowrock/040226yellowrock-ROUGH_Tsmd.rtf` | 1.7MB | Apr 3 |
| Audio | `Documents/mb_040226_halprin_yellowrock/040226yellowrock-ROUGH.opus` | 76MB | Apr 3 |
| CaseCATalyst xml | `Documents/mb_040226_halprin_yellowrock/040226yellowrock-ROUGH.sgxml` | 23KB | Apr 30 |
| FINAL_T.RTF (oracle) | `Documents/mrx-context/oracle/finals/halprin/040226yellowrock-FINAL_T.rtf` | 1.7MB | Apr 28 |
| FINAL.txt (oracle) | `Documents/mrx-context/oracle/finals/halprin/040226yellowrock-FINAL.txt` | 389KB | Apr 28 |
| FINAL PDF | `Documents/mb_040226_halprin_yellowrock/Easley_YellowRock_FINAL.pdf` | 334KB | Apr 3 |

**Notes:**
- `040226yellowrock-ROUGH.rtf` at 5.2KB is a stub — not the real rough. Real rough is `040226yellowrock-ROUGH_Tsmd.rtf` (1.7MB).
- FINAL oracle files are in mrx-context/oracle/finals/halprin — correct location per protocol.
- The Easley FINAL PDF was placed here (mb_040226_halprin_yellowrock/) — misplaced. Should be in Easley's own folder.
- The `mb_040226_halprin_yellowrock/` folder also holds the full CaseCATalyst bundle for Halprin, including 76MB audio. Not the Easley audio.

---

### Depo 3 — Easley (YellowRock 031326)

**Status:** Pre-engine reference; v4 engine era

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF (copies) | scattered across `marybeth_demo/`, `mb_demo_engine_v4/`, `mb_040226_halprin_yellowrock/`, `court_report_project/` | 1.3MB | various |
| Audio | `Documents/marybeth_demo/030526yellowrock-FINAL.opus` | 86MB | (Mar) |
| FINAL PDF (copy 1) | `Documents/mb_040226_halprin_yellowrock/Easley_YellowRock_FINAL.pdf` | 334KB | Apr 3 |
| FINAL PDF (copy 2) | `Documents/mb_demo_engine_v4/FINAL_DELIVERY/Easley_YellowRock_FINAL.pdf` | 334KB | (Mar) |
| FINAL PDF (Downloads) | `Downloads/depofiles/031326yellowrock-FINAL.pdf` | 916KB | Mar 30 |

**Notes:**
- Most scattered of all depos. Raw RTF in at least 4 different folders. No canonical home.
- No FINAL_T.RTF (CaseCATalyst transcript RTF) found — only FINAL PDF. Cannot be used as engine oracle without it.
- Note: audio date code is `030526` (Mar 5) vs depo date code `031326` (Mar 13) — possible naming inconsistency.

---

### Depo 4 — Hammond / Montz (020926)

**Status:** Pre-engine demo (v4 engine era); no steno RTF available

| File | Path | Size | Date |
|---|---|---|---|
| Rough PDF | `Downloads/020926hammonds-SCOTTYd.pdf` | 451KB | Feb 16 |
| Rough PDF (copy) | `Documents/MD_demo_engine_LA_hammond/020926hammonds-SCOTTYd (3).pdf` | 451KB | Mar 23 |
| FINAL PDF | `Documents/MD_demo_engine_LA_hammond/FINAL_DELIVERY/Montz_Hammonds_FINAL.pdf` | — | (Mar) |
| FINAL TXT | `Documents/MD_demo_engine_LA_hammond/FINAL_DELIVERY/Montz_Hammonds_FINAL_FORMATTED.txt` | — | (Mar) |

**Notes:**
- Input was a rough transcript PDF (not steno RTF). Cannot be used in mrx_engine_v1 pipeline.
- No audio found. v4 engine worked from PDF extraction alone.
- MD_demo_engine_LA_hammond is a git repo. Contains engine v4 scaffolding.

---

### Depo 5 — Wade (0323)

**Status:** v4 engine era, NY WCB jurisdiction

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF | `Documents/AD_wade_0323/0323Wade2026_T.rtf` | 44KB | Mar 28 |
| FINAL PDF | `Documents/AD_wade_0323/FINAL_DELIVERY/Wade_Pearce_FINAL.pdf` | 22KB | Mar 30 |
| FINAL TXT | `Documents/AD_wade_0323/FINAL_DELIVERY/Wade_Pearce_FINAL_TRANSCRIPT.txt` | 15KB | Mar 30 |
| FINAL PDF (Downloads) | `Downloads/0323Wade2026wcbg3097551.pdf` | 472KB | Mar 30 |

**Notes:**
- RTF present (44KB — shorter depo or partial). FINAL_T.RTF not found; FINAL PDF only.
- No CaseCATalyst bundle found — RTF likely provided raw from AD's steno software, not full CaseCATalyst export.
- Naming note: folder uses "wade" lowercase, filename uses "Wade2026" with year. AD reporter.

---

### Depo 6 — Fourman (0324)

**Status:** v4 engine era, NY WCB jurisdiction

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF | `Documents/ad_foreman_0324/0324Fourman2026_T.rtf` | 103KB | Mar 28 |
| FINAL PDF | `Documents/ad_foreman_0324/FINAL_DELIVERY/Fourman_WCB_FINAL.pdf` | 37KB | Mar 29 |
| FINAL TXT | `Documents/ad_foreman_0324/FINAL_DELIVERY/Fourman_WCB_FINAL_TRANSCRIPT.txt` | 34KB | Mar 29 |

**Notes:**
- Folder name uses "foreman" spelling; filename uses "Fourman" — inconsistency flagged.
- RTF at 103KB — larger than Wade, more complete.
- No CaseCATalyst bundle. No audio. No FINAL_T.RTF.

---

### Depo 7 — Soyer (0320)

**Status:** v4 test harness era, NY WCB jurisdiction

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF | ❌ NOT FOUND | — | — |
| FINAL TXT (Pass1) | `Documents/TestHarness_Run_NY1/FINAL_DELIVERY_Pass1/Soyer_PearceWC_FINAL_TRANSCRIPT.txt` | — | Mar 21 |
| FINAL TXT (Pass3) | `Documents/TestHarness_Run_NY1/FINAL_DELIVERY_Pass3/Soyer_Pearce_FINAL_TRANSCRIPT.txt` | — | Mar 21 |
| FINAL PDF (Downloads) | `Downloads/0320Soyer2026wcbG3097551.pdf` | 519KB | Apr 4 |

**Notes:**
- No raw RTF found anywhere on disk. Either never received as RTF, or extracted from a PDF that was discarded.
- Two pass versions in TestHarness_Run_NY1 suggest iterative testing. Folder naming confirms NY WCB context.
- No audio. Cannot be onboarded to mrx_engine_v1 without raw steno RTF.

---

### Depo 8 — Gotesman (0316)

**Status:** v4 demo era ("alicia_demo"), NY WCB jurisdiction

| File | Path | Size | Date |
|---|---|---|---|
| Raw RTF (unclear) | `Documents/alicia_demo/0313Leon2026_T.rtf` | 54KB | Mar 20 — DIFFERENT WITNESS |
| Raw RTF (alias?) | `Documents/alicia_demo/alicia.txt.rtf` | 54KB | Mar 20 |
| Audio (MP3) | `Documents/alicia_demo/-7849480339599919352.mp3` | 6.5MB | Mar 17 |
| FINAL PDF | `Documents/alicia_demo/0316Gotesman2026wcbG1917209.pdf` | 462KB | Mar 18 |
| FINAL PDF (Downloads) | `Downloads/0316Gotesman2026wcbG1917209.pdf` | 462KB | Mar 23 |

**Notes:**
- `alicia_demo/` contains an RTF for "Leon" (0313), not Gotesman — likely a different witness processed in the same demo run.
- `alicia.txt.rtf` at same size as the Leon RTF may be the same file renamed.
- Audio is an MP3 (not CaseCATalyst .opus) — small at 6.5MB, may be a phone recording or clip, not the full depo.
- No FINAL_T.RTF (CaseCATalyst transcript). FINAL PDF only.

---

### Depo 9 — Bertolet / Todd (date unknown)

**Status:** Reference/demo only

| File | Path | Size | Date |
|---|---|---|---|
| FINAL PDF | `Downloads/Bertolet, Todd - 1014795 - FINAL_Corrected.pdf` | 1012KB | Apr 4 |
| FINAL PDF (copy) | `Downloads/Bertolet, Todd - 1014795 - FINAL_Corrected (1).pdf` | — | Apr 4 |

**Notes:**
- No raw RTF, no audio, no case folder, no date code. Only two copies of the same corrected FINAL PDF in Downloads.
- Naming pattern is different from all other depos (no date prefix, case number format 1014795).
- Cannot determine reporter or jurisdiction from available files.

---

## Part 2 — Library Proposal

### Problem Statement

The nine depos above are spread across approximately 15 different folders with no consistent naming, no canonical locations, and no clear separation between:
- Input files (steno RTF, audio, CaseCATalyst bundles)
- Working files (v4 engine scaffolding, intermediate outputs)
- Oracle files (MB's actual FINAL deliverables — the ground truth)

The oracle files in particular are the most critical and the most at risk. They need a permanent, predictable home that is:
- Outside the engine repo (never pushed to public)
- Outside mrx-context (public repo)
- On OneDrive (survives disk wipe)
- Predictable by name alone

### Proposed Library Structure

```
C:\Users\scott\OneDrive\Documents\mrx_depo_library\
│
├── README.md                    (index of depos, dates, reporters, status)
│
├── MB\                          (Marybeth Muir packages)
│   ├── brandl_032626\
│   │   ├── input\
│   │   │   ├── 032626YELLOWROCK-FINAL_T.rtf          (2.2MB — steno+transcript RTF)
│   │   │   ├── 032626YELLOWROCK-FINAL.sgngl           (steno stroke file)
│   │   │   ├── 032626YELLOWROCK-FINAL.sgxml           (CaseCATalyst XML)
│   │   │   └── 032626YELLOWROCK-FINAL.opus            (audio — 99MB, gitignored)
│   │   ├── oracle\
│   │   │   └── BRANDL_MB_FINAL.txt                   (MB's final transcript, plain text)
│   │   └── meta\
│   │       └── package_info.json                     (date, reporter, case, file hashes)
│   │
│   ├── halprin_040226\
│   │   ├── input\
│   │   │   ├── 040226yellowrock-ROUGH_Tsmd.rtf        (1.7MB)
│   │   │   ├── 040226yellowrock-ROUGH.sgxml
│   │   │   └── 040226yellowrock-ROUGH.opus            (76MB, gitignored)
│   │   ├── oracle\
│   │   │   ├── 040226yellowrock-FINAL_T.rtf           (1.7MB — MB's final RTF)
│   │   │   └── 040226yellowrock-FINAL.txt             (389KB)
│   │   └── meta\
│   │       └── package_info.json
│   │
│   └── easley_031326\
│       ├── input\
│       │   ├── 031326yellowrock-ROUGH_T.rtf           (consolidate from scatter)
│       │   └── [audio if recoverable]
│       ├── oracle\
│       │   └── 031326yellowrock-FINAL.pdf             (PDF only — no FINAL_T.RTF)
│       └── meta\
│           └── package_info.json
│
├── AD\                          (AD reporter packages — Wade, Fourman)
│   ├── wade_0323\
│   │   ├── input\
│   │   │   └── 0323Wade2026_T.rtf                    (44KB)
│   │   ├── oracle\
│   │   │   ├── Wade_Pearce_FINAL.pdf
│   │   │   └── Wade_Pearce_FINAL_TRANSCRIPT.txt
│   │   └── meta\
│   │       └── package_info.json
│   │
│   └── fourman_0324\
│       ├── input\
│       │   └── 0324Fourman2026_T.rtf                 (103KB)
│       ├── oracle\
│       │   ├── Fourman_WCB_FINAL.pdf
│       │   └── Fourman_WCB_FINAL_TRANSCRIPT.txt
│       └── meta\
│           └── package_info.json
│
└── UNKNOWN_REPORTER\            (depos with no confirmed reporter match)
    ├── soyer_0320\
    │   └── oracle\
    │       ├── 0320Soyer2026wcbG3097551.pdf
    │       └── Soyer_Pearce_FINAL_TRANSCRIPT.txt
    ├── gotesman_0316\
    │   └── oracle\
    │       └── 0316Gotesman2026wcbG1917209.pdf
    ├── hammond_020926\
    │   └── oracle\
    │       ├── Montz_Hammonds_FINAL.pdf
    │       └── Montz_Hammonds_FINAL_FORMATTED.txt
    └── bertolet_unknown\
        └── oracle\
            └── Bertolet_Todd_1014795_FINAL_Corrected.pdf
```

### Naming Conventions

| Element | Rule | Example |
|---|---|---|
| Reporter folder | Uppercase abbreviation of reporter's name | `MB`, `AD`, `UNKNOWN_REPORTER` |
| Depo subfolder | `witness_lastname_MMDDYY` (all lowercase, underscores) | `brandl_032626` |
| Input files | Preserve original CaseCATalyst filename unchanged | `032626YELLOWROCK-FINAL_T.rtf` |
| Oracle files | Preserve original filename if MB-provided; use `*_FINAL.txt` if converted | `BRANDL_MB_FINAL.txt` |
| Meta file | Always `package_info.json`, same keys across all depos | see below |

**package_info.json schema (minimal):**
```json
{
  "witness": "Brad Brandl",
  "date_code": "032626",
  "reporter": "Marybeth Muir",
  "case": "YellowRock",
  "jurisdiction": "LA",
  "has_steno_rtf": true,
  "has_audio": true,
  "has_final_rtf": true,
  "has_final_txt": true,
  "engine_status": "active",
  "notes": ""
}
```

### What Moves Where

| Current location | Move to | Action |
|---|---|---|
| `MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE/` | `mrx_depo_library/MB/brandl_032626/input/` + `oracle/` | Move (keep zip as backup) |
| `mrx-context/oracle/finals/brandl/` | `mrx_depo_library/MB/brandl_032626/oracle/` | Move (remove from mrx-context — it's public) |
| `mrx-context/oracle/finals/halprin/` | `mrx_depo_library/MB/halprin_040226/oracle/` | Move (same reason) |
| `mb_040226_halprin_yellowrock/*.rtf + .opus` | `mrx_depo_library/MB/halprin_040226/input/` | Move |
| `mb_Yellow_Brad_Brandl/032626YELLOWROCK_smd_T.rtf` | `mrx_depo_library/MB/brandl_032626/input/` | Copy or symlink |
| `Downloads/brandl_extracted/` | `mrx_depo_library/MB/brandl_032626/input/` (merge) | Move and merge |
| `AD_wade_0323/*.rtf` | `mrx_depo_library/AD/wade_0323/input/` | Move |
| `ad_foreman_0324/*.rtf` | `mrx_depo_library/AD/fourman_0324/input/` | Move |
| Easley RTF (scattered) | `mrx_depo_library/MB/easley_031326/input/` | Consolidate (pick one copy) |

### What Does NOT Move

- `mrx_engine_v1/io/analysis/brandl_50pp/` — engine I/O paths; leave in place, engine reads from known paths
- v4 engine folders (`mb_Yellow_Brad_Brandl/`, `AD_wade_0323/`, etc.) — leave as-is; they contain engine scaffolding, not just depo files
- Working files (cleaned_text.txt, corrected_text.txt, etc.) — these belong in their engine folder

### Engine Path Integration

The engine currently reads Brandl from a hardcoded path inside `io/analysis/brandl_50pp/`. The library does not break this. Instead, the library is the canonical long-term storage; `io/analysis/` can contain softlinks or a `case_package.json` that points into the library.

When onboarding a new depo to mrx_engine_v1:
1. Place all files in `mrx_depo_library/[REPORTER]/[depo_folder]/`
2. Create a `case_package.json` in `io/analysis/[depo_case_name]/` that references the library paths
3. Engine reads from `io/analysis/` as before — library is the source of truth, not the runtime path

### Priority Actions (do these Friday or next build session)

1. **Highest:** Move `mrx-context/oracle/finals/` out of the public repo. Those FINAL files must not be on GitHub. Create `mrx_depo_library/MB/` and move them there.
2. **High:** Consolidate Brandl's two CaseCATalyst bundles (ORACLES vs Downloads/brandl_extracted) — they are duplicates; keep one.
3. **Medium:** Consolidate Easley RTF copies — pick one canonical copy for the library; delete the rest.
4. **Low:** Investigate Soyer — no raw RTF found. If it exists somewhere, find and add it.

---

*Generated: 2026-05-07*
*Oracle Covenant honored. No FINAL RTF opened.*
