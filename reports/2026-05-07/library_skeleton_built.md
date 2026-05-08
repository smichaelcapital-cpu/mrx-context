# Library Skeleton Build Report

**Date:** 2026-05-07
**Root:** `C:\Users\scott\OneDrive\Documents\mrx_depo_library\`
**Scope:** MB/ folder only. AD/ and UNKNOWN_REPORTER/ deferred.

---

## Tree — Files Created (with sizes)

```
mrx_depo_library/
├── README.md                                                              85 B
└── MB/
    ├── brandl_032626/
    │   ├── input/
    │   │   ├── 032626YELLOWROCK-FINAL.opus          99.0 MB  (source: MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE)
    │   │   ├── 032626YELLOWROCK-FINAL.sgngl          1.2 MB
    │   │   ├── 032626YELLOWROCK-FINAL.sgxml          20.3 KB
    │   │   └── 032626YELLOWROCK-FINAL_T.rtf           2.1 MB
    │   ├── oracle/
    │   │   └── BRANDL_MB_FINAL.txt                  277.1 KB (source: mrx-context/oracle/finals/brandl)
    │   └── meta/
    │       └── package_info.json                       487 B
    │
    ├── halprin_040226/
    │   ├── input/
    │   │   ├── 040226yellowrock-ROUGH.opus           75.9 MB  (source: mb_040226_halprin_yellowrock)
    │   │   ├── 040226yellowrock-ROUGH.sgxml          22.5 KB
    │   │   └── 040226yellowrock-ROUGH_Tsmd.rtf        1.6 MB
    │   ├── oracle/
    │   │   ├── 040226yellowrock-FINAL.txt            388.5 KB (source: mrx-context/oracle/finals/halprin)
    │   │   └── 040226yellowrock-FINAL_T.rtf           1.7 MB
    │   └── meta/
    │       └── package_info.json                       524 B
    │
    └── easley_031326/
        ├── input/
        │   └── 031326yellowrock-ROUGH_T_1.rtf         1.3 MB  (source: MASTER_COPIES/mb_demo_engine_v4)
        ├── oracle/
        │   ├── Easley_YellowRock_FINAL.pdf           333.6 KB (source: mb_demo_engine_v4/FINAL_DELIVERY)
        │   └── Easley_YellowRock_FINAL_TRANSCRIPT.txt 263.7 KB
        └── meta/
            └── package_info.json                       629 B
```

**Total: 193,000,525 bytes (184.1 MB)**

---

## File Counts

| Depo | Input files | Oracle files | Meta | Total files |
|---|---|---|---|---|
| brandl_032626 | 4 | 1 | 1 | 6 |
| halprin_040226 | 3 | 2 | 1 | 6 |
| easley_031326 | 1 | 2 | 1 | 4 |
| README.md | — | — | — | 1 |
| **Total** | **8** | **5** | **3** | **17** |

---

## Anomalies

### Easley audio not copied
Easley audio file `030526yellowrock-FINAL.opus` (86MB) exists in `marybeth_demo/` but its date code is `030526` (March 5) while the depo date code is `031326` (March 13). Possible naming inconsistency — unclear if this is Easley's audio or a different depo. Not copied. Flag for manual verification before adding to library.

### Easley has no FINAL_T.RTF
As noted in the proposal, no CaseCATalyst FINAL transcript RTF found for Easley. Oracle folder contains PDF + plain-text transcript from the v4 engine delivery instead. `has_final_rtf: false` in package_info.json.

### Brandl oracle txt still in mrx-context (public)
`mrx-context/oracle/finals/brandl/BRANDL_MB_FINAL.txt` was copied but not removed (per job spec: copy only). This file is on a public GitHub repo. Cleanup is tomorrow's task.

### Halprin oracle files still in mrx-context (public)
Same as Brandl. `mrx-context/oracle/finals/halprin/` was copied but not removed.

---

## Originals Confirmation

No original files were modified, moved, or deleted. All operations were `cp` (copy) only.

Sources verified:

| Copied from | Still present | Check |
|---|---|---|
| `MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE/032626YELLOWROCK-FINAL_T.rtf` | ✅ | untouched |
| `MASTER_COPIES/ORACLES/BRANDL_MB_DELIVERABLE/032626YELLOWROCK-FINAL.opus` | ✅ | untouched |
| `mrx-context/oracle/finals/brandl/BRANDL_MB_FINAL.txt` | ✅ | untouched |
| `mb_040226_halprin_yellowrock/040226yellowrock-ROUGH_Tsmd.rtf` | ✅ | untouched |
| `mb_040226_halprin_yellowrock/040226yellowrock-ROUGH.opus` | ✅ | untouched |
| `mrx-context/oracle/finals/halprin/040226yellowrock-FINAL_T.rtf` | ✅ | untouched |
| `mrx-context/oracle/finals/halprin/040226yellowrock-FINAL.txt` | ✅ | untouched |
| `MASTER_COPIES/mb_demo_engine_v4/031326yellowrock-ROUGH_T_1.rtf` | ✅ | untouched |
| `mb_demo_engine_v4/FINAL_DELIVERY/Easley_YellowRock_FINAL.pdf` | ✅ | untouched |
| `mb_demo_engine_v4/FINAL_DELIVERY/Easley_YellowRock_FINAL_TRANSCRIPT.txt` | ✅ | untouched |

---

## Deferred (not built tonight)

- `mrx_depo_library/AD/` — Wade, Fourman folders not created
- `mrx_depo_library/UNKNOWN_REPORTER/` — Hammond, Soyer, Gotesman, Bertolet not created
- mrx-context/oracle/ cleanup (move → delete originals) — tomorrow's task

---

*Oracle Covenant honored. No FINAL RTF opened.*
*Generated: 2026-05-07*
