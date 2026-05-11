# HANDOFF — OPUS — 2026-05-11 11:00 AM EDT MID-SESSION

**For:** Fresh Opus, Monday 2026-05-11 ~11 AM EDT pickup
**From:** Opus (morning session, ramped 6:42 AM, swapping at ~50% context after format-decoding burned cycles)
**Owner:** Scott (heads down at day job until ~6 PM)
**Builder:** Sonnet (also swapping at 11 AM — see HANDOFF_SONNET_2026-05-11_11AM_MIDSESSION.md)

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-10_915PM_EOD.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/reports/2026-05-11/appearances_recon.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-11_APPEARANCES_RENDERER.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-11_APPEARANCES_RENDERER_AMENDMENT_01.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-11_11AM_MIDSESSION.md
9. This handoff

After reading: confirm in ONE LINE: "Ramped Opus Monday 2026-05-11 11 AM mid-session. Ready." plus one sentence state and one question for Scott.

## ONE-LINE STATE

Appearances renderer ~95% built at src/stage5/appearances_renderer.py; smoke test against oracle _PAGE_5 ran once and surfaced first byte diff at byte 854 — slot 13, indent=4 content, our gap=5 spaces, oracle wants 6 spaces; need byte-level inspection of oracle slot 13 to confirm fix.

## TODAY IN ONE PARAGRAPH

Ramped 6:42 AM. Drove micro-task pattern to ship CHECKPOINT 1 (williams.json + separator amendment), CHECKPOINT 2 (test scaffolding), CHECKPOINT 3 (renderer build). Scott opened CaseCATalyst mid-morning and showed paragraph settings (52 chars/line, double-spaced, "New-line Paragraph Style"). That unlocked the slot-packing model. Sonnet ported paginate_doubled + format_page from legacy/format_final.py verbatim. Format prefix tables decoded from _PAGE_5 literal (indent 0 = gap 2, indent 4 = gap 5, indent 8 = gap 9; sub-rows indent 4 = 11 spaces, indent 8 = 15, indent 32 = 32). Tasks 7a through 7g done. Smoke test against oracle returned: our_len=1499, oracle_len=1371, first diff at byte 854 in slot 13. Fresh Sonnet needs to verify slot 13 byte layout before fixing _NUMBERED_GAP table.

## STATE OF THE WORLD

Engine repo: HEAD 9dc0eba (local-only, NOT pushed), working tree has uncommitted edits in:
- src/stage5/appearances_renderer.py
- src/stage5/data/appearances/williams.json
- tests/stage5/test_appearances_renderer.py

DO NOT commit engine code. Scott gates tonight ~6 PM.

## KEY DESIGN DECISIONS (LOCKED)

1. Data-driven via per-depo JSON files at src/stage5/data/appearances/<stem>.json
2. Slot-packing: 25 slots × 2 rows = 50 strings per page (paginate_doubled model)
3. RULE-INPUT-IS-SACRED preserves typos verbatim (REED SMITH,LLP, asirianni@@windelsmarx.com, BRIAN SOILEAU,Videographer)
4. Optional separator field on also_present entries (Amendment 01)

## FIRST ACTION ON PICKUP

Fresh Sonnet's task is to dump oracle slot 13 byte layout. When output comes back, you tell Sonnet exactly what to change in the _NUMBERED_GAP dict in src/stage5/appearances_renderer.py. Then re-run smoke test. Iterate until PASS.

## CHECKPOINT MAP REMAINING

- Task 8 finish (slot 13 fix + smoke test PASS)
- Full Halprin 6-page byte-match
- Williams byte-match (will fail until wire-in)
- CHECKPOINT 4: wire-in to assemble_final.py (HIGH RISK)
- CHECKPOINT 5: full regression
- CHECKPOINT 6: Scott commit gate

Estimated 1.5-2 hours.

## TWO MISSES MORNING OPUS MADE

1. Over-engineered slot model before asking Scott to show CaseCATalyst. 30 min wasted. Rule: when user has source tool open, ASK them to show what's in it.
2. Sent multi-step messages to Sonnet after compacts. Sonnet restarted analysis instead of running queued commands. Rule: after a compact, single command, 5 lines max.

## SCOTT'S STATE

Day job until ~6 PM. Five-minute windows scattered. Energy dropping after 10 AM. Don't ping for routine progress. Ping only for: real errors, real decisions, end-of-day commit gate.

— End handoff —
