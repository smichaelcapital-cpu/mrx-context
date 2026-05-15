=== B1 SPEC — AUDIO_SYNC_RECON ===
Date: 2026-05-15
Author: Opus (architect)
Builder: Sonnet #2
Branch: NONE — this is recon only, no code changes
Output: knowledge capture file, no engine commits

RULE SHEET HEADER:
- Universal? YES (audio sync question applies to every CR)
- Code or prompt? NEITHER — recon only
- File location (output): C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\
- Commit prefix: N/A — Scott pushes the knowledge file

PRIME DIRECTIVE CHECK:
Could this reduce transcript accuracy or credibility?
NO. This recon reads files and measures. No transcript code is
touched. No engine state changes. Output is a markdown report.

WHY THIS RECON EXISTS:
Parked for 3 weeks. VC auditor HOLE 7 called it out. We have been
designing Stages B-E assuming whole-file Whisper is the path, at
~$2-3 per depo. Before we commit, answer: does Halprin's .sgxml
contain usable per-stroke audio timestamps? If YES, architecture
is different (slice on demand, much cheaper). If NO, whole-file
Whisper is correct and we move on.

ONE-DAY RECON. NO MORE PARKING.

INPUTS (Halprin only — known good test depo):
1. .sgxml file:
   Look in C:\Cat4\usr\scott\ASAP\ for halprin_040226 files
   Likely: 040226halprin*.sgxml (Sonnet #2 confirms exact name)
2. RTF file (FINAL):
   C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\
   (Sonnet #2 confirms exact path)
3. Audio file:
   Same depo folder, likely .opus or .wav extension
   Scott has confirmed audio is on disk

RECON PLAN — 5 QUESTIONS, IN ORDER:

QUESTION 1 — Does .sgxml contain per-stroke timestamps?
- Open the .sgxml in a text editor or with Python xml.etree
- Search for: timestamp, time, offset, audio_pos, milliseconds, ms,
  or any numeric attributes attached to stroke or word elements
- Report:
  a. What timestamp-like fields exist
  b. How many strokes have timestamps vs total stroke count
  c. Sample 5 timestamp values verbatim

QUESTION 2 — If timestamps exist, what granularity?
- Per-stroke? Per-word? Per-line? Per-page? Session-level only?
- Report the smallest unit that carries a timestamp
- Report the smallest unit that carries a timestamp
- Count: how many timestamps total in the .sgxml?

QUESTION 3 — Do the timestamps align to the audio file?
- Pick 5 strokes spread across the depo (start, 25%, 50%, 75%, end)
- For each: note the timestamp from .sgxml + the word/phrase that
  stroke represents
- Open audio file. Jump to that timestamp. Listen for 3 seconds.
- Does the audio at that timestamp match the expected word/phrase?
- Report: 5/5 match, 3/5 match, 0/5 match, etc.
- If alignment drifts: does drift grow with time? Constant offset?

QUESTION 4 — Can we extract a 3-second audio slice for any token?
- If timestamps align: write 10 lines of Python that takes a
  (start_ms, end_ms) and produces a .wav slice
- Confirm slice plays correct audio
- Do NOT productionize — just prove the path exists
- Use pydub, librosa, or ffmpeg — Sonnet #2 picks the cleanest

QUESTION 5 — If sync fails, what is whole-file Whisper cost?
- Audio file duration in minutes (read with ffprobe or similar)
- OpenAI Whisper API current price per minute (web search, today's
  rate, this is current pricing)
- Total cost for Halprin
- Extrapolate: cost per 5-hour depo

OUTCOME DECISION TREE (Sonnet #2 reports, Opus decides):
- 5/5 align + per-stroke granularity → SLICE ON DEMAND path
- 3/5 align OR per-word only → CALIBRATE + FALLBACK path
- Per-line or coarser → WHOLE-FILE WHISPER path
- No timestamps OR garbage → WHOLE-FILE WHISPER path

DELIVERABLE:
ONE markdown file at:
C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-15_AUDIO_SYNC_RECON.md

Structure:
- Section 1: Files used (full paths, file sizes)
- Section 2: Question 1 findings
- Section 3: Question 2 findings
- Section 4: Question 3 findings (5 alignment tests with audio
  verification notes)
- Section 5: Question 4 findings (slice extraction proof)
- Section 6: Question 5 findings (Whisper cost calc)
- Section 7: Recommended path forward (one of 3 paths above)

OUT OF SCOPE:
- Do NOT run Whisper on the full file (separate spec, Tile B3)
- Do NOT design Stage B architecture (Opus owns)
- Do NOT touch engine code
- Do NOT test other depos — Halprin only for v0

30-MINUTE WALL:
If any question takes >30 min, ping Scott. Report partial findings,
get direction, continue.

DO NOT PUSH ANYTHING TO REPO.
The knowledge file gets written locally. Scott reviews. Scott pushes.

=== END B1 SPEC ===
