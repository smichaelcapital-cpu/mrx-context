---
# STAGE 4 — Opus Context Document
Original location: io/analysis/_opus_context_stage4.md (gitignored)
Generated: 2026-04-24 by Sonnet
Moved to mrx-context: 2026-04-27
Status: Reference document — read at session start by Opus
---

# Opus Context: Stage 4 Audio Verifier — Design Input
# Generated: 2026-04-24
# Purpose: Read-only context for Opus to design 03_stage4_audio_verify_spec.md
# Gitignored. No commit.

---

## 0. EXECUTIVE SUMMARY FOR OPUS

Stage 4 has not been designed yet. This is raw material for writing
`design/03_stage4_audio_verify_spec.md`.

**Critical new findings (not in previous context doc):**

1. **The halprin_mini sgxml file HAS 88 audio timestamps** — the FINAL sgxml is
   parsed and confirmed to contain complete audio sync data. The sgxml_reader.py
   stub is the only thing blocking their use.

2. **Brandl audio transcript ALREADY EXISTS in the repo** at
   `io/analysis/brandl_50pp/audio/brandl_0-40min.json` — it is a 465-segment
   Whisper JSON transcript with per-word timestamps. This is Stage 4's prototype
   evidence base, already built.

3. **Brandl RTF has [REVIEW: steno gap -- verify audio] markers** — these are
   real Stage 3 FLAGS from a real deposition, showing exactly what Stage 4 must
   resolve.

4. **No "5-layer audio verification pipeline" exists** in any design doc.
   The term used in the task prompt does not correspond to any existing spec.
   The pattern is: sgxml timestamps → Whisper transcription → text matching →
   3-tier apply (AUTO/SUGGEST/LOW). Opus should design around what is real.

5. **No Deepgram code exists anywhere in the repo.** Zero grep matches.
   No Deepgram SDK installed.

6. **ad_foreman_0324 is not an audio test fixture folder** — it is a job
   directory for a separate deposition (Forman, March 2024) with no audio files.

---

## 1. DESIGN DOCS — ALL AUDIO / STAGE 4 REFERENCES

### 1a. MRX_ENGINE_V1_CHARTER.md (verbatim Stage 4 references)

```
## The 6 stages

| # | Stage | Input | Output | AI? |
|---|-------|-------|--------|-----|
| 4 | POLISH (suggestions) | stage3_sections.json + dictionary + audio | stage4_suggestions.json | Yes (caged) |

## Out of scope for v1
- Audio verification beyond MVP (Stage 4 audio hook is stubbed;
  full Deepgram/MFA integration is v1.1)

## What this charter does NOT commit to
- An assumption that any particular AI model is the right one for Stage 4 —
  to be decided on evidence during Stage 4 build.
```

**Note:** The charter's stage numbering (POLISH = Stage 4) maps to the current
architecture's Stage 3 (Multi-Pass Fixer). The charter predates the current
architecture renaming. The audio verification function is unchanged.

### 1b. design/00_architecture_overview.md (verbatim Stage 4 references)

```
Stage 4 — Audio Verifier. Uses sgxml timestamps and audio file to verify
uncertain corrections. Optional. Only runs if audio is provided.

*(Future: a 7th specialist — Audio — slots in here when Stage 4 audio is available.)*

| 8 | Stage 4 audio | Designed now, built later | Audio verification is
    high-value but not blocking |

4. *(later)* 03_stage4_audio_verify_spec.md
```

### 1c. design/01_stage1_rtf_build_spec.md (verbatim audio timestamp schema)

```
"job_metadata": {
    "audio_sync_enabled": bool,
    "has_audio": bool
},
"audio_timestamps": [
    {"idx": int, "elapsed_ms": int, "audio_ms": int, "pause": int}
]

Audio timestamps come from paired <Read-Audio-ElapsedTime-N> and
<Read-Audio-Timestamp-N> nodes. Pair them by index.
Pause values from <Read-Audio-Pause-N> are 0 or 1 (stop/start markers).
Pair with the same index.
The audio timestamp count should equal the elapsed time count; if they differ,
log a warning and truncate to the shorter list.

Not needed for Stage 1 RTF output — Stage 1 does not use audio timestamps itself.
This module exists so Stage 4 (audio verifier) and the Stage 1 report can use
the data. We implement it now to avoid rework.
```

### 1d. CODER_MINDSET_MYREPORTERX_ADDENDUM_v1.md (verbatim MB rule)

```
RULE-MB-IS-THE-CUSTOMER: Think Like the Court Reporter, Not the Engineer

"She doesn't care about MFA phoneme models or Deepgram confidence scores.
She cares about whether the transcript is right and whether she can tell it's
right at a glance."

"When engineering complexity leaks into MB's world, she loses trust.
When MB loses trust, the product dies."

"If a feature requires technical jargon in the UI or documentation, it's not done."
```

---

## 2. ad_foreman_0324 DIRECTORY — CONFIRMED NOT AN AUDIO FIXTURE

Location: `C:\Users\scott\OneDrive\Documents\ad_foreman_0324\`

This is a **job directory** for the Forman deposition (March 2024). It uses the
same mb_demo_engine_v4 scripts. **No audio files found.** Not an audio test fixture.

Contents (with sizes):
```
0324Fourman2026_T.rtf          (105KB) — Forman depo RTF
ELITE_CR_STANDARD.md           (9KB)
FINAL_DELIVERY/
GREGG_STYLE_MODULE.txt         (53KB)
HOUSE_STYLE_MODULE_dalotto.md  (7KB)
HOUSE_STYLE_MODULE_muir.md     (16KB)
KNOWLEDGE_BASE.txt             (34KB)
MARGIE_STYLE_MODULE.txt        (88KB)
MASTER_DEPOSITION_ENGINE_v4.1.md (48KB) — note: v4.1 not v4.2
ai_engine.py, specialist_verify.py, verify_agent.py ... [pipeline scripts]
corrected_text.txt, correction_log.json, specialist_verify_log.json
```

The specialist_verify_log.json (207KB) is a large output — this depo ran the full
three-pass correction pipeline. Potentially useful as a fixture for Stage 3 testing.

---

## 3. DEEPGRAM GREP — REPO-WIDE

**Zero matches in any source file.** Only matches found were in the two opus context
documents written in this session (`_opus_context_stage3_and_4.md` and this file).

```
# Command run:
grep -rn -i "deepgram|montreal.forced|phoneme|forced.align|mfa\b" \
  src/ tests/ design/ *.md 2>/dev/null

# Source file matches: 0
# Design doc matches: 0
# Charter match (1): "full Deepgram/MFA integration is v1.1"  ← aspirational
# Coder Mindset match (1): "She doesn't care about MFA phoneme models or
#                           Deepgram confidence scores."  ← warning against it
```

**Conclusion:** Deepgram is mentioned twice — once as a v1.1 aspiration, once as an
example of what NOT to surface to MB. It has never been designed, installed, or coded.

---

## 4. DEPENDENCIES — AUDIO LIBRARIES

### requirements.txt (full contents):
```
# mrx_engine_v1 — Stage 1 dependencies
# Stage 1 uses Python stdlib only. No external packages required.
# pytest is the only dev dependency.
pytest>=7.0
```

No audio libraries are in requirements.txt. The project currently has zero non-stdlib,
non-pytest dependencies.

### Installed on this machine (pip list audit):
```
faster-whisper     1.2.1    ← INSTALLED (local Whisper, no API key needed)
openai-whisper     20250625 ← INSTALLED (local Whisper via OpenAI's library)

deepgram-sdk       NOT installed
librosa            NOT installed
pydub              NOT installed
montreal-forced-aligner  NOT installed
ffmpeg             CHECK: required by Whisper for audio chunking
                          (not a Python package — check: ffmpeg -version)
```

Both `faster-whisper` and `openai-whisper` are installed. These are local Whisper
models — they run on-device without an API key or network. The demo engine used the
**OpenAI Whisper API** (cloud, via `openai` package + `OPENAI_API_KEY`), which is a
different approach.

---

## 5. AUDIO FILES IN io/analysis/halprin_mini/

**No audio files in the halprin_mini fixture directory.**

Full file listing:
```
040226yellowrock-FINAL.sgngl
040226yellowrock-FINAL.sgxml     ← CRITICAL: has 88 audio timestamps
040226yellowrock-FINAL.txt
040226yellowrock-FINAL_T.rtf
halprin_mini.rtf
_pipeline_out/
  halprin_mini.stage1.parse_log.jsonl
  halprin_mini.stage1.report.md
  halprin_mini.stage1.summary.json
  halprin_mini.stage1.turns.json
  halprin_mini.stage1.txt
_stage2_out/
  halprin_mini.stage2.summary.json
  halprin_mini.stage2.turns.json
  halprin_mini.stage2.txt
[probe scripts]
```

The audio file is **outside the repo** at:
`C:\Users\scott\OneDrive\Documents\mb_040226_halprin_yellowrock\040226yellowrock-ROUGH.opus`
(76MB opus file)

---

## 6. SGXML AUDIO TIMESTAMPS — CONFIRMED POPULATED

**The halprin_mini sgxml file (040226yellowrock-FINAL.sgxml) has 88 audio timestamp
entries.** This was parsed and confirmed. The sgxml_reader.py stub is the only thing
blocking their use.

### Parsed timestamp structure:
```
FINAL sgxml: 88 entries, 44 start events (pause=0), 44 stop events (pause=1)
Max elapsed: 2,043,567 ms = 34.1 min = 0.57 hr
```

### Sample pairs (first 6):
```
idx  pause  elapsed_ms  elapsed_min  cat_timestamp
  0      0           0        0.00    3,182,063
  1      1       4,794        0.08    3,186,857
  2      0       4,794        0.08    3,208,381
  3      1      13,778        0.23    3,217,365
  4      0      13,778        0.23    3,271,636
  5      1      17,490        0.29    3,275,348
  ...
 86      0   1,999,840       33.33    5,842,624
 87      1   2,043,567       34.06    5,886,351
```

### How to interpret:
- **pause=0**: Recording START at this elapsed_ms point
- **pause=1**: Recording STOP at this elapsed_ms point
- **elapsed_ms**: Milliseconds elapsed in the steno session (= position in the text)
- **cat_timestamp**: CaseCATalyst internal time value (NOT audio position in ms —
  requires calibration to convert to audio file seek position)
- **Pairs alternate**: 0→start, 1→stop, 2→start, 3→stop (even=start, odd=stop)

### Calibration insight from the data:
The gap between idx=0 and idx=1 (4,794ms elapsed, cat_ts delta=4,794) suggests
the cat_timestamp IS related to elapsed_ms but with an offset (3,182,063 base).

`cat_ts ≈ elapsed_ms + 3,182,063` — but this needs verification. The deltas are:
- Segment 0→1: elapsed=4,794ms, cat_delta=4,794ms → 1:1 ratio ✓
- Segment 2→3: elapsed=8,984ms, cat_delta=8,984ms → 1:1 ratio ✓
- BUT segment 1→2: elapsed same (4,794), cat_delta=21,524ms — this is the GAP
  between the stop and the next start (CR paused recording).

**Key insight:** The cat_timestamp delta during RECORDING equals elapsed_ms delta.
The audio file position for a given elapsed_ms point is:

```
audio_position_ms = elapsed_ms - [calibration_offset]
```

The calibration offset is the relationship between when the audio recorder started
and when CaseCATalyst started. This is the "depo-specific calibration" problem
mentioned in audio_targeted.py. The demo engine solved it via text-matching
(no calibration needed) — which is simpler and more robust.

### ROUGH sgxml for Halprin (mb_040226_halprin_yellowrock/040226yellowrock-ROUGH.sgxml):
This is the ROUGH version of the same depo. It likely has more timestamps because
the rough covers more of the session. Worth checking when implementing sgxml_reader.

---

## 7. BRANDL AUDIO — EXISTING WHISPER TRANSCRIPT IN REPO

**This is the most important Stage 4 design asset.** A Whisper transcript of the
Brandl 0-40min audio already exists at:

```
io/analysis/brandl_50pp/audio/
  brandl_0-40min.opus    (9.0MB) — audio file
  brandl_full.opus       (99MB)  — full depo audio
  brandl_0-40min.json    (859KB) — WHISPER TRANSCRIPT (already built)
  brandl_0-40min.srt     (38KB)  — SRT subtitle format
  brandl_0-40min.tsv     (29KB)  — TSV format
  brandl_0-40min.txt     (21KB)  — plain text
  brandl_0-40min.vtt     (36KB)  — WebVTT format
```

### Whisper transcript format (verbatim sample):
```json
{
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 18.88,
      "end": 19.6,
      "text": " I'm going to go.",
      "tokens": [...],
      "temperature": 0.0,
      "avg_logprob": -0.6867,
      "compression_ratio": 1.31,
      "no_speech_prob": 0.319,
      "words": [
        {"word": " I'm", "start": 18.88, "end": 19.24, "probability": 0.0875},
        {"word": " going", "start": 19.24, "end": 19.6, "probability": 0.1526},
        ...
      ]
    },
    ...
  ]
}
```

```
Total segments: 465
Duration: 2,395.4s = 39.9 min
First segment start: 18.88s (pre-roll before testimony begins)
Last segment end: 2,395.4s
Per-word timestamps: YES (each word has start, end, probability)
```

**This transcript was produced by local faster-whisper or openai-whisper** (not the
OpenAI Whisper API — the API returns a different schema without per-segment tokens
and without `no_speech_prob`). The schema matches faster-whisper's `word_timestamps=True`
output exactly.

**Stage 4 can use this transcript immediately as a proof-of-concept fixture.**

### Brandl RTF [REVIEW] markers — what Stage 4 must resolve:

From `io/analysis/brandl_50pp/Brandl_FINAL.rtf`, two types of audio flags found:

```
[REVIEW: steno gap -- verify audio]
```

Examples in context:
```
"Did you end up taking those two samples from your memory from one of each of the
[REVIEW: steno gap -- verify audio] layers or were all of those samples taken
from one of the layers?"

"So in this particular instance, the reason I'm saying it's tight is because they
have low permeability. I'm not sure how the important [REVIEW: steno gap --
verify audio] is impacted, but the permeability is impacted because of the water..."
```

These represent **steno gaps** — places where the steno machine produced nothing or
gibberish, and the AI corrector flagged them for audio verification. Stage 4's job
is to find what Whisper heard at these timestamps and surface it to MB.

---

## 8. NO "5-LAYER AUDIO VERIFICATION PIPELINE" IN ANY EXISTING DOC

The task prompt references: "dictionary → context → Deepgram → MFA → human"

This phrase **does not appear in any design document, charter, spec, or code** in
this repo. A full-repo grep for "5-layer", "five-layer", "dictionary.*context.*deepgram",
and "deepgram.*mfa" returned zero matches.

**What DOES exist (from mb_demo_engine_v4):**
The demo engine's audio approach is:
```
Stage 3 FLAG items → Whisper transcription → text matching → 3-tier apply → MB review
```

No dictionary step. No MFA. No phoneme verification. No forced alignment.
The demo engine achieved its results with Whisper + text matching alone.

**Opus should design Stage 4 around what has actually been proven to work,**
not around aspirational architecture that hasn't been designed or tested.

---

## 9. SGXML_READER STATUS — WHAT MUST BE BUILT BEFORE STAGE 4

`src/mrx_engine_v1/stage1_rtf/sgxml_reader.py` is a stub:
```python
def read_sgxml(path: str) -> dict | None:
    """Stub — returns None until fully implemented per design/01 section 4."""
    return None
```

**Consequence:** The halprin_mini pipeline produces `sgxml_metadata: null` in the
stage1.turns.json output. The 88 audio timestamps in the sgxml are not captured.

**What sgxml_reader must produce (per design/01 spec, Section 4):**
```python
{
  "job_metadata": {
    "audio_sync_enabled": bool,  # Audio-Sync sgpref-val
    "has_audio": bool,           # Has-Audio sgpref-val
    "pages": int,
    "total_strokes": int,
    ...
  },
  "audio_timestamps": [
    {"idx": int, "elapsed_ms": int, "audio_ms": int, "pause": int}
    # Note: "audio_ms" field name in spec may differ from "cat_timestamp"
    # in the actual sgxml — Opus must reconcile
  ],
  "dictionary_stack": list[str],  # list of .sgdcx paths
  "cvn_users": list[dict]
}
```

**The Halprin FINAL sgxml confirms the sgxml_reader can produce 88 timestamp entries
for the 34.1-minute depo.** The data is there. The reader just needs to be written.

**Decision for Opus:** Does Stage 4 depend on sgxml_reader being implemented first?
Or does it use the text-matching approach (no timestamps needed)? Or does it support
both, with timestamps as the preferred path and text-matching as fallback?

---

## 10. THE TWO CANDIDATE ARCHITECTURES

### Architecture A: sgxml-timestamp-based (precise but requires sgxml_reader)

```
Stage 3 FLAG turns
       ↓
sgxml_reader extracts elapsed_ms for each FLAG turn
       ↓
Map elapsed_ms → audio seek position (requires calibration)
       ↓
Cut audio window at seek position
       ↓
Whisper transcribes window
       ↓
Compare Whisper output to FLAG context
       ↓
3-tier decision: AUTO / SUGGEST / LOW
```

**Pro:** Precise audio seeking — knows exactly where in the audio each turn is.
**Con:** Requires implementing sgxml_reader. Requires audio calibration step.
         Timestamps are stroke-level (not turn-level) — mapping turns to timestamps
         is not straightforward.

### Architecture B: text-matching (demo engine pattern, proven)

```
Stage 3 FLAG turns
       ↓
Load Whisper transcript of full audio (once, cached)
       ↓
For each FLAG: extract text context window
       ↓
Text-match FLAG context against Whisper segments
       ↓
3-tier decision: AUTO / SUGGEST / LOW
```

**Pro:** No sgxml_reader dependency. No calibration. Already proven in demo engine.
         Whisper transcripts already exist in repo for Brandl.
**Con:** Text matching can fail on steno gaps (no text to match against).

### Architecture C: hybrid (preferred path is A, fallback is B)

For FLAG turns with steno gaps (no text context for matching):
- Architecture A required: seek to timestamp, cut window, transcribe.

For FLAG turns with text context:
- Architecture B preferred: match against cached transcript.

**Opus should evaluate which architecture fits v1 scope.** Architecture B alone
may be sufficient for v1 given that the charter says "Stage 4 audio hook is stubbed;
full integration is v1.1."

---

## 11. DEMO ENGINE AUDIO IMPLEMENTATION (KEY PATTERNS FOR REUSE)

See `_opus_context_stage3_and_4.md` Section B-5 for full verbatim code.

Summary of patterns:

**audio_validation.py — full-depo Whisper transcription:**
- Splits audio into ~15MB chunks via ffmpeg
- Sends each chunk to Whisper API (openai whisper-1 model, cloud)
- Caches as `audio_transcript.json` — never re-transcribes
- Segment format: `{"start": float, "end": float, "text": str}`
- Cost: $0.006/min. A 40-min depo = ~$0.25 via API.
  With local faster-whisper: $0.00 (but slower).

**Matching algorithm:**
```python
# Last 6 words of FLAG context as search terms
search_words = set(last_6_words)
# Score = matched_words / total_search_words
# Threshold: 0.5 for match
# 3-segment rolling window (handles phrases split across segments)
# Sequential cursor (never searches backwards)
# Proportional window: ±10% of total segments from estimated position
```

**3-tier apply:**
```python
AUTO    = score >= 0.9 AND not gap-fill keyword
SUGGEST = score >= 0.7 OR gap-fill at any score
LOW     = score < 0.7 (still surfaced — nothing silently discarded)
```

**Gap-fill keywords (prevent AUTO):**
```python
['steno gap', 'not captured', 'fragmented', 'missing', 'amount missing',
 'figure missing', 'percent', 'dollar', 'number missing', 'unclear',
 'answer unclear', 'steno fragment', 'beyond steno']
```

---

## 12. MB-FACING OUTPUT REQUIREMENTS (NON-NEGOTIABLE)

From RULE-MB-IS-THE-CUSTOMER:

Stage 4's CR review output must use plain language. Examples from the demo engine
(these worked for MB):

```
✓ "Audio confirmed: [word]"         → clear, actionable
✓ "Audio heard: [word] — please verify"   → honest, simple
✓ "Audio heard something here, low confidence — please verify"

✗ "Whisper confidence: 0.83"        → meaningless to MB
✗ "faster-whisper word probability 0.79" → jargon
✗ "MFA phoneme alignment: 0.65"     → MB would stop trusting the tool
```

The WAS / NOW / WHY format from the demo engine worked well:
```
── AUDIO-01 ──────────────────────────────────────────
WAS:  the important [?] is impacted
NOW:  the important clause is impacted
WHY:  Audio confirmed engine correction
```

---

## 13. DESIGN/DECISIONS AND DESIGN/ARCHIVE

```
design/
  archive/   ← exists, currently empty
  decisions/ ← exists, currently empty
  README.md  ← authoring rules (Opus writes, Scott reviews, Sonnet builds)
```

No Stage 4 decisions or archived Stage 4 content yet.

---

## 14. QUESTIONS FOR OPUS TO ANSWER IN 03_stage4_audio_verify_spec.md

1. **Architecture choice:** Text-matching (Architecture B, proven) vs. timestamp-based
   (Architecture A, requires sgxml_reader) vs. hybrid? For v1, B alone may be sufficient.

2. **sgxml_reader dependency:** Does Stage 4 depend on sgxml_reader being implemented?
   Or can it operate without it (text-matching fallback) and add timestamp-based seeking
   as a future enhancement?

3. **Which turn types get audio verification?**
   - All `flag_only` Stage 3 decisions?
   - Only turns where the FLAG reason contains audio-related keywords?
   - Only `steno_gap` flags (where the text is missing)?
   - Only Q./A. turns (not COLLOQUY or BYLINE)?

4. **Whisper model — local vs. API:**
   - Local `faster-whisper` (already installed, free, no API key, ~10x slower)
   - OpenAI Whisper API (requires `OPENAI_API_KEY`, $0.006/min, faster)
   - The demo engine used the API. For v1, local may be preferred to avoid
     adding a second API key dependency.

5. **Output format:** Does Stage 4 write a new `*.stage4.turns.json`? Or does it
   write a review document only? Or does it annotate Stage 3 turns in place?

6. **Optionality:** How is "optional — only runs if audio is provided" implemented?
   - Pipeline.run() accepts optional `audio_path: str | None = None`?
   - If None: Stage 4 no-ops and returns a summary with `audio_available: false`?

7. **7th specialist vs. separate stage:** Architecture overview mentions "a 7th specialist
   — Audio — slots in here when Stage 4 audio is available." Should Stage 4 be a
   specialist inside Stage 3 Pass 3, or a completely separate pipeline stage?

8. **Cost reporting:** Does Stage 4 evaluate.py include Whisper cost in the report?
   (Local faster-whisper = $0; API = $0.006/min)

9. **ffmpeg dependency:** Whisper chunking requires ffmpeg on PATH. Does the spec
   add this as a system dependency? Or does Stage 4 use local faster-whisper which
   can handle opus/mp3/wav natively?

10. **Acceptance fixture:** The Brandl audio + Brandl RTF flags form a natural Stage 4
    test fixture. The Whisper transcript already exists. Should the acceptance test use
    Brandl (known flags, known audio, pre-built transcript) or Halprin (larger, no
    pre-built transcript)?

---

## 15. COMPLETE INVENTORY — AUDIO ASSETS ON THIS MACHINE

| File | Location | Size | Notes |
|------|----------|------|-------|
| `brandl_0-40min.opus` | `io/analysis/brandl_50pp/audio/` | 9.0MB | In repo |
| `brandl_0-40min.json` | `io/analysis/brandl_50pp/audio/` | 859KB | Whisper transcript, IN REPO |
| `brandl_full.opus` | `io/analysis/brandl_50pp/audio/` | 99MB | In repo |
| `040226yellowrock-ROUGH.opus` | `mb_040226_halprin_yellowrock/` | 76MB | Halprin audio, outside repo |
| `040226yellowrock-FINAL.sgxml` | `io/analysis/halprin_mini/` | — | 88 timestamps, IN REPO |
| `040226yellowrock-ROUGH.sgxml` | `mb_040226_halprin_yellowrock/` | 23KB | ROUGH version, outside repo |
| `030526yellowrock-FINAL.opus` | `marybeth_demo/` | — | Final audio, outside repo |
| `sample_depo.mp3` | `mb_demo_engine_v4/test_audio/` | — | Demo test fixture |

**Immediately usable for Stage 4 proof-of-concept:**
1. `io/analysis/brandl_50pp/audio/brandl_0-40min.opus` + `brandl_0-40min.json` (transcript ready)
2. `io/analysis/brandl_50pp/Brandl_FINAL.rtf` (has `[REVIEW: steno gap -- verify audio]` flags)

These three files together enable a complete Stage 4 demonstration without any additional
audio transcription cost.

---

## 16. SGXML TIMESTAMP CALIBRATION — WHAT OPUS MUST DECIDE

The sgxml ElapsedTime values are steno-session-elapsed-ms (from the moment the
steno machine's session started). The audio file's time origin is when the recorder
was started — which may or may not coincide with the steno session start.

**The demo engine solved this problem by not using timestamps at all** — it
uses text-matching against a full-depo Whisper transcript. This avoids the
calibration problem entirely.

If Opus chooses Architecture A (timestamp-based), the spec must define:
- How calibration offset is determined (manual input? auto-detected from pre-roll?)
- What happens when calibration fails
- How to map stroke-level timestamps to turn-level positions

The sgxml data shows the CAT timestamp starts at 3,182,063 when elapsed=0.
This 3.18M base value is the CAT system clock at session start — it is NOT
audio position. The elapsed_ms IS the audio position offset FROM when audio
sync was enabled, which may or may not be at the start of the audio file.

**Recommendation for v1:** Use text-matching (Architecture B). Add timestamp-based
seeking in v1.1 when sgxml_reader is fully implemented and calibration is solved.

---

*End of Stage 4 context document.*
*Next step: Opus writes design/03_stage4_audio_verify_spec.md using this input.*
