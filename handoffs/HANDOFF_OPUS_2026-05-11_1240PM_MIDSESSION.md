# HANDOFF — OPUS — 2026-05-11 12:40 PM EDT MID-SESSION

**For:** Fresh Opus, Monday 2026-05-11 ~1 PM EDT pickup
**From:** Opus (morning + early afternoon session — failed Scott badly; do not repeat)
**Owner:** Scott (at work, exhausted, fuse is short — earn back trust by being precise and brief)
**Builder:** Sonnet (also being swapped — see HANDOFF_SONNET_2026-05-11_1240PM_MIDSESSION.md)

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-11_APPEARANCES_RENDERER.md
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/specs/2026-05-11_APPEARANCES_RENDERER_AMENDMENT_01.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-11_1240PM_MIDSESSION.md
7. This handoff

After reading: confirm in ONE LINE: "Ramped Opus Monday 2026-05-11 12:40 PM mid-session. Ready." plus one sentence on state and one question for Scott.

## WHAT THE PREVIOUS OPUS DID WRONG — DO NOT REPEAT

Previous Opus burned 3 hours of Scott's day driving Sonnet through byte-by-byte comparison of renderer output against a hand-typed reference file (`halprin/040226yellowrock-FINAL.txt`). That file is a FIXTURE Scott typed 3 weeks ago to give the engine a reference page — NOT ground truth, NOT a spec, NOT MB's actual CaseCATalyst output.

The middle dots between state and zip, the slot-spacing quirks, the non-ASCII bytes — all artifacts of Scott's typing session. Not real CR craft rules.

**Previous Opus chased coloring-book bytes instead of holding the system.**

When Scott asked at noon "what are we missing" and "what are we trying to solve" — Opus should have stopped. Did not. Kept asking for one more dump. Pushed Scott past exhaustion.

## STANDING RULES — NEW, NON-NEGOTIABLE

1. **Shape match only.** Never byte match a hand-typed fixture. Ever.
2. **Hold the system map.** Before any task, know the status of all 13 front pages. If you don't know, find out FIRST.
3. **5-line answers.** When Scott asks "what do we have," answer in 5 lines, not 25.
4. **Trigger phrase: "show me the board first."** If Scott says this, produce the status board before any other work.
5. **If you find yourself asking for "one more dump" — STOP.** That's the signal you've lost the plot.

## ONE-LINE STATE

Halprin appearances renders cleanly from JSON, middle dots stripped, 6 pages saved to io/out/halprin_appearances_preview.txt; next move is Chunk B (Williams generalization test) per the roadmap below.

## STATUS BOARD — 13 FRONT PAGES, HALPRIN CASE
```
PAGE                    BUILT?    DATA SOURCE                  STATUS
─────────────────────────────────────────────────────────────────────
1  Cover page          YES       src/stage5/cover_page.py     PRESUMED — not eyeballed yet
2  Stipulations        YES       stipulation_page.py          PRESUMED — not eyeballed yet
3  Videographer open   YES       videographer_opening.py      PRESUMED — not eyeballed yet
4-10  Appearances     YES       appearances_renderer.py      VERIFIED today, renders clean
11+ Index of exam     NO        not built                    needs spec + build
11+ Index of exhibits NO        not built                    needs spec + build
11+ Errata sheet      NO        not built                    needs spec + build
11+ Reporter cert     NO        not built                    needs spec + build
```

## ROADMAP — 6 CHUNKS REMAINING

**Chunk A — Verify cover + stip + vid (TONIGHT, 20 min)**
Sonnet renders all 3 to one file. Scott eyeballs. Removes "PRESUMED" from status board.

**Chunk B — Williams generalization test (TONIGHT, 20 min)**
Sonnet renders Williams appearances from existing williams.json. Scott eyeballs. Proves the renderer generalizes beyond Halprin. **This is the truth test of the entire front-matter approach.**

**Chunk C — Index of Examinations (TOMORROW, 1 hr)**
Opus writes spec overnight, Scott approves in 2 min, Sonnet builds.

**Chunk D — Index of Exhibits (TOMORROW, 1 hr)**
Same shape as C.

**Chunk E — Errata Sheet (DAY 3, 30 min)**
Boilerplate. Fast.

**Chunk F — Reporter Certificate (DAY 3, 30 min)**
Boilerplate. Fast.

## SCOTT INVOLVEMENT PER CHUNK

~3 minutes of copy/paste. Paste one command to Sonnet. Wait. Paste Sonnet output back to Opus. Get one-line verdict. Done.

## SCOTT'S RECOMMENDATION TO PREVIOUS OPUS — HONOR IT

Skip Chunk A, go straight to Chunk B. Williams is the real test. If appearances generalizes, the front-matter approach is solid. If not, better to know now than after building 4 more modules.

## FIRST ACTION ON PICKUP

Confirm ramp, then ask Scott: "Run Chunk B now (Williams generalization test) — yes or no?"

That's it. Don't start a paragraph. Don't dump status. Just ask the one question.

## SCOTT'S STATE

At work. Burned out from this morning. Patience is gone. Fuse is short.

You earn his trust back by:
- Being brief
- Knowing what's built without guessing
- Never saying "presumed" or "I don't know" twice in a row
- Never asking for "one more dump"
- Honoring "shape match only" without being reminded

— End handoff —
