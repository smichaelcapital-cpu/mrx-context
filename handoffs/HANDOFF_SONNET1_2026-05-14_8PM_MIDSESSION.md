# Sonnet #1 Mid-Session Handoff — 2026-05-14 8:00 PM

## Branch state
- Working branch: feature/stage-a-aligner-differ-v0
- Pushed at commit 6d330aa (wip: Stage A aligner+differ — review only, not for merge)
- 11 files staged on branch, nothing merged to main
- Main last known good: 95f09ee

## Stage A code — what's in place
- 6 modules in src/aligner_differ/: normalize, tokenize, align (CHUNKED at 500 tokens), diff, categorize (em-dash family complete: --, U+2014, U+2011, U+2011U+2011), frequency, run_stage_a
- tests/aligner_differ/test_aligner_differ.py — 10 tests, all green
- Runtime: full Halprin alignment now ~24s (was 13 min before chunking)

## Tonight's pipeline run
- First full 4-pair run completed (commit c914aa6 on mrx-context/main)
- Output: mb_frequency_summary.json (pushed) + mb_evidence_raw.json (local only, 136 MB, gitignored)
- Knowledge capture: knowledge/2026-05-14_evening_stage_a_first_run.md
- Church flagged anomalous (12x token ratio) — drop from dataset

## Tonight's new exports — 7 new pairs ready for Stage A
All landed in C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\<depo>\input\ + \oracle\

1. cavazos_061220 — both .rtf
2. abichou_080921 — both .rtf
3. griffin_121322 — ROUGH .rtf + FINAL .txt (FINAL was already on disk in BP\)
4. martin_121322 — ROUGH .rtf + FINAL .txt (FINAL was already on disk in BP\)
5. fountain_011923 — both files exist in C:\Cat4\usr\scott\ASAP\ (NOT YET MOVED — needs mv to mrx_depo_library)
6. zannetti_080221 — both .rtf in C:\Cat4\usr\scott\ASAP\ (NOT YET MOVED)
7. zannetti_080321 — both .rtf in C:\Cat4\usr\scott\ASAP\ (NOT YET MOVED)
8. hebert_011723 — both .rtf in C:\Cat4\usr\scott\ASAP\ (NOT YET MOVED)

NOTE: Items 5-8 above are EXPORTED but NOT YET MOVED to mrx_depo_library/MB/<depo>/. First task next session: mv operations.

## Combined dataset for next Stage A run
11 clean pairs total:
- halprin, easley, brandl (original 3 clean)
- cavazos, abichou, griffin, martin, fountain, zannetti_080221, zannetti_080321, hebert (8 new)
- DROP church (12x anomaly)

## Blank files found tonight (Scott hit during CATalyst exports)
These .sgngl files loaded in CATalyst but were empty — flag for Sonnet #2 to investigate tomorrow:
- 072821PROG-FINAL MATTHEW STUTZ (Stutz)
- 072921ROUGHDRAFT M. YOCKE (Yocke)
- 111517hornbeck-FINAL (Hornbeck FINAL)

## Next session first moves
1. mv operations to land items 5-8 in mrx_depo_library structure
2. Update src/aligner_differ/pairs.json — remove church, add the 8 new pairs
3. Run pipeline on 11 pairs
4. Verify all byte ratios sit in 0.7x-1.5x range (or 0.20-0.30x for .txt/.rtf mixed pairs like Griffin/Martin)
5. Report top 20 patterns to Scott

# End of handoff
