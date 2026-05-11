# HANDOFF — SONNET — 2026-05-11 12:40 PM EDT MID-SESSION

**For:** Fresh Sonnet, Monday 2026-05-11 ~1 PM EDT pickup
**From:** Sonnet (morning + early afternoon session — burned 3 hours on byte-matching a hand-typed fixture; needs fresh start)
**Owner:** Scott (at work, exhausted, low patience — minimal pings, only for real blockers)
**Architect:** Opus (also being swapped — see HANDOFF_OPUS_2026-05-11_1240PM_MIDSESSION.md)

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_OPUS_2026-05-11_1240PM_MIDSESSION.md
5. This handoff

After reading: confirm in ONE LINE: "Ramped Sonnet Monday 2026-05-11 12:40 PM mid-session. Ready." plus one-line state.

## ONE-LINE STATE

Halprin appearances renderer is DONE and rendering cleanly to io/out/halprin_appearances_preview.txt; next task is verifying cover/stip/vid modules actually work, then running Williams through appearances renderer as the generalization truth test.

## WHAT WAS ACCOMPLISHED THIS MORNING

- Appearances renderer built (src/stage5/appearances_renderer.py)
- halprin.json data file built (src/stage5/data/appearances/halprin.json)
- williams.json data file built (src/stage5/data/appearances/williams.json)
- Spec at specs/2026-05-11_APPEARANCES_RENDERER.md + Amendment 01
- Renderer produces 6 clean pages of Halprin appearances on demand
- All middle dots (U+00B7) removed from halprin.json — they were artifacts of Scott's hand-typed fixture, not real CR formatting

## WHAT WAS WASTED THIS MORNING — DO NOT REPEAT

Sonnet and Opus spent 3 hours byte-matching the renderer output against a hand-typed reference file Scott created 3 weeks ago. That file is a FIXTURE, not ground truth. Middle dots, slot spacing quirks, and other byte-level artifacts came from the act of typing the fixture — NOT from MB or CaseCATalyst.

**THE RULE GOING FORWARD: shape match only. Never byte match a hand-typed fixture.**

## NEXT TASKS — WAIT FOR OPUS DIRECTION

Opus will issue Chunk A and Chunk B commands. Each is one focused task:

- **Chunk A:** Render Halprin cover + stip + vid opening to one file. Paste contents.
- **Chunk B:** Render Williams appearances from williams.json. Paste contents.

DO NOT freelance. DO NOT iterate on byte diffs. Render, paste, wait.

## RULES

- Slow is smooth. Smooth is fast.
- ONE task at a time. Run command, paste output, stop.
- If a task takes >5 min with no output, STOP and re-read the instruction.
- Shape match only. No byte comparisons.
- If something looks weird in output, paste it and FLAG to Opus — do not silently fix.

## KEY FILE PATHS

- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\data\appearances\halprin.json
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\src\stage5\data\appearances\williams.json
- C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\out\halprin_appearances_preview.txt

## SCOTT'S STATE

At work. Tired. Patience is gone. Minimum pings. Only escalate for: real blockers, real decisions. Otherwise: do the work, paste output, wait.

— End handoff —
