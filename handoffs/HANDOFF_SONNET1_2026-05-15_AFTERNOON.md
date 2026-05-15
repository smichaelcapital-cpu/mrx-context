# HANDOFF — SONNET #1 — 2026-05-15 AFTERNOON

**For:** Fresh Sonnet #1, next session
**From:** Sonnet #1, 2026-05-15 morning + afternoon session
**Owner:** Scott
**Architect:** Opus
**Lane:** A — pipeline

---

## STANDING RULES
Same as Opus handoff. Read these first:
1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md

## WHAT SHIPPED THIS SESSION

Commit bd17695 on feature/appearances-renderer-fix:
- is_first_page fix (pages 6-10 indent correction)
- Bug C fix (ALSO PRESENT layout, page 10 line 13-14)
- Bug D fix (Reporter sub-row anchor, page 10 line 19-21)
- 472 pytest passing, 2 pre-existing failures expected

## WHAT WAS ATTEMPTED AND ROLLED BACK

A1.5.1.1 Bug B-new fix (FULL → HALF separator). Tried Option 2 variant (emit HALF-A in pending=False blank case).
Result: pages 6-7 cascade eliminated, but pages 8-10 broke (wrong page break shift).
Verdict: Bug B-new cannot be fixed at code level alone.
Reason: Halprin oracle has 2 FULL-blank transitions (G1→G2 and OLD REPUBLIC→TIG) with no algorithmic distinction from HALF cases. Same data shape, different rendering. MB hand-typed inconsistently with her own standard.
Code reverted to A1.5.1 v1 state. Working tree clean at bd17695.

## KEY INSIGHT FROM TODAY

Bug B-new diagnosis revealed bigger pattern: we've been byte-chasing Halprin's hand-typed quirks. Sonnet #2's cross-depo audit (knowledge/2026-05-15_INDEX_RENDERER_DEEP_RECON.md and the blank-separator audit findings in the conversation) shows MB's standard is HALF blank between firms. Halprin has 2 outlier FULL blanks that don't match her own standard.

The way forward is multi-depo render data, not more Halprin patches. A pivot conversation is in flight between Scott + Opus.

## BRANCH STATE

- Branch: feature/appearances-renderer-fix
- Latest commit: bd17695
- Backup branches: backup/appearances-renderer-fix-pre-bugB, backup/appearances-renderer-fix-pre-CD
- Working tree: clean
- Not yet merged to feature/appearances-wire-in or main

## DEFERRED ITEMS

1. **Bug A** (middle dot in halprin/appearances.json) — data-fix spec needed (A1.5.2)
2. **Bug B-new** (FULL/HALF blank separator) — requires data-driven approach with JSON "separator_after" flag, or deferral if multi-depo data shows it's Halprin-only
3. **ESQ. double-space** (BENNETT MATSON, SALLY CLEMENTS, KEVIN MCGLONE) — oracle artifact, accepted

## ENGINE INFRASTRUCTURE GAP DISCOVERED

Only Halprin has a stage5 runner (io/analysis/halprin_full/_run_halprin_full_stage5.py). No runner exists for any other MB depo. Williams data is present and ready in src/profiles/mb/data/front_matter/060122williams/ but cannot be rendered without a runner. Sonnet #2 is recon-ing Williams runner buildability as of session end.

## RAMP CONFIRMATION

After reading: "Ramped Sonnet #1 [datetime]. Ready." plus one sentence on state + one question for Scott.

— End of Sonnet #1 2026-05-15 afternoon handoff —
