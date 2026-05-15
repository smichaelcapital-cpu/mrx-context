# B1 AUDIO_SYNC_RECON — Halprin 040226
**Date:** 2026-05-15
**Builder:** Sonnet #2 (Lane B, Tile B1)
**Branch:** NONE — recon only, no engine commits
**Status:** COMPLETE — ready for Opus review

---

## Section 1 — Files Used

| File | Full Path | Size |
|---|---|---|
| .sgxml | `C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\input\040226yellowrock-ROUGH.sgxml` | 23 KB |
| .opus (audio) | `C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\input\040226yellowrock-ROUGH.opus` | 76 MB |
| RTF (ROUGH) | `C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\input\040226yellowrock-ROUGH_Tsmd.rtf` | 1.7 MB |
| RTF (FINAL) | `C:\Users\scott\OneDrive\Documents\mrx_depo_library\MB\halprin_040226\oracle\040226yellowrock-FINAL_T.rtf` | 1.7 MB |

**NOTE:** The .sgxml was NOT found in `C:\Cat4\usr\scott\ASAP\`. It lives in the mrx_depo_library. The Cat4 ASAP folder had no Halprin files visible. All recon used the library copy.

**Depo metadata (from .sgxml):**
- Session: 2026-02-04, 08:50:19 → 16:27:40 (7h 37m session window)
- Pages: 289
- Total strokes: 50,363
- Has-Audio flag: 1 (confirmed)
- Audio-Sync flag: 1 (confirmed)

---

## Section 2 — Question 1: Does .sgxml contain per-stroke timestamps?

**Short answer: NO.**

The .sgxml is a CATalyst preferences/metadata file (root tag: `SGXML_Preferences`). It does NOT contain per-stroke transcript data. That lives in the binary `.sgngl` file.

What IS present:
- `Read-Audio-Timestamp-0` through `Read-Audio-Timestamp-87` — **88 entries**
- `Read-Audio-ElapsedTime-0` through `Read-Audio-ElapsedTime-87` — **88 entries**
- `Read-Audio-Pause-0` through `Read-Audio-Pause-87` — **88 entries**
- `Has-Audio`: `sgpref-val="1"` (audio sync is on)
- `Audio-Sync`: `sgpref-val="1"`
- `AudioInputSource`: `"Default"`

These are CATalyst **read-back sync points** — positions saved when MB played back audio during a review session. They are NOT recorded at steno write time. They are NOT per-stroke.

**5 sample timestamp values verbatim (sgpref-val attribute):**

| Index | Raw value | Converted |
|---|---|---|
| 0 | `3182063` | 3182.1 sec (53.0 min) |
| 22 | `4068159` | 4068.2 sec (67.8 min) |
| 43 | `4700210` | 4700.2 sec (78.3 min) |
| 65 | `5334777` | 5334.8 sec (88.9 min) |
| 87 | `5886351` | 5886.4 sec (98.1 min) |

Units are **milliseconds** from the start of the audio file.

---

## Section 3 — Question 2: Granularity?

**Granularity: approximately per-3.3-pages, but wildly irregular. NOT usable for per-token lookup.**

| Metric | Value |
|---|---|
| Total timestamps | 88 |
| Pages in depo | 289 |
| Strokes in depo | 50,363 |
| Avg pages per timestamp | ~3.3 |
| Avg strokes per timestamp | ~572 |
| Smallest unit | ~page-group (irregular) |
| Min gap between consecutive timestamps | -5 ms (essentially simultaneous — two entries at same position) |
| Max gap between consecutive timestamps | 451,916 ms (7.5 minutes) |
| Avg gap | ~31,084 ms (31 seconds) |

**Coverage problem:** Timestamps range from 3,182 sec to 5,886 sec (53 min to 98 min). Audio total duration is **20,440 seconds (340 minutes)**. The sync points cover only ~45 minutes out of 340 minutes total — **13% of the audio**. The first 53 minutes and the last 242 minutes have no sync coverage at all.

**Interpretation:** MB did a partial read-back session, manually setting sync points as she went. The session covered roughly pages X through Y (unknown without .sgngl) and then stopped. Most of the depo has no sync data.

---

## Section 4 — Question 3: Do timestamps align to the audio?

**Extraction:** 5 x 3-second .wav slices extracted at the 5 timestamp positions using ffmpeg. All extractions succeeded (rc=0, each 96 KB).

| Slice | Start timestamp | Audio position | Extracted to |
|---|---|---|---|
| q1_idx0 | 3,182,063 ms | 53:02 | `knowledge/slice_q1_idx0.wav` |
| q2_idx22 | 4,068,159 ms | 67:48 | `knowledge/slice_q2_idx22.wav` |
| q3_idx43 | 4,700,210 ms | 78:20 | `knowledge/slice_q3_idx43.wav` |
| q4_idx65 | 5,334,777 ms | 88:54 | `knowledge/slice_q4_idx65.wav` |
| q5_idx87 | 5,886,351 ms | 98:06 | `knowledge/slice_q5_idx87.wav` |

**IMPORTANT LIMITATION:** Sonnet cannot listen to audio. The slices are on disk and ready. Scott or MB must open them and verify whether spoken content matches the expected transcript text at those positions.

**What is already known regardless of alignment:**
- Even if 5/5 align, granularity is ~572 strokes per sync point — not usable for per-token lookup
- Coverage is 13% of the file — most of the depo cannot be synced
- This path cannot support "slice on demand" at the token level

**Practical verdict:** Alignment test outcome does NOT change the architecture recommendation (see Section 7). Document for the record, but it's not the decision gate.

---

## Section 5 — Question 4: Can we extract a 3-second audio slice?

**YES. Proven. 10-line Python using ffmpeg subprocess:**

```python
import subprocess, os

AUDIO = r'C:\...\040226yellowrock-ROUGH.opus'
OUT_DIR = r'C:\...\knowledge\\'

def extract_slice(start_ms, end_ms, label):
    out = os.path.join(OUT_DIR, f'slice_{label}.wav')
    cmd = ['ffmpeg', '-y', '-ss', str(start_ms/1000), '-to', str(end_ms/1000),
           '-i', AUDIO, '-ar', '16000', '-ac', '1', out]
    r = subprocess.run(cmd, capture_output=True)
    size = os.path.getsize(out) if os.path.exists(out) else 0
    return out, size, r.returncode
```

All 5 test calls returned `rc=0`. Output is 16kHz mono WAV, ready for Whisper ingestion.

**Dependency:** ffmpeg must be on PATH (confirmed present on this machine).
**No pydub or librosa needed** — ffmpeg subprocess is cleaner, no extra packages.

---

## Section 6 — Question 5: Whole-file Whisper cost

**Audio duration:** 20,440.5 seconds = **340.7 minutes**

**Pricing (OpenAI, as of May 2026):**
- Whisper-1: **$0.006/min** → $0.36/hr ([source](https://tokenmix.ai/blog/whisper-api-pricing))
- GPT-4o Mini Transcribe: **$0.003/min** → $0.18/hr
- GPT-4o Transcribe (with diarization): **$0.006/min**

**Cost for Halprin (340.7 min):**

| Model | Cost |
|---|---|
| Whisper-1 | $2.04 |
| GPT-4o Transcribe | $2.04 |
| GPT-4o Mini Transcribe | $1.02 |

**Extrapolated: typical 5-hour depo (300 min):**

| Model | Cost |
|---|---|
| Whisper-1 | $1.80 |
| GPT-4o Mini Transcribe | $0.90 |

**CRITICAL CONSTRAINT — FILE SIZE LIMIT:**
OpenAI Whisper API has a **25 MB per-file limit**. Halprin audio is **76 MB**. The file must be chunked before upload (3 chunks minimum). ffmpeg chunking is straightforward but adds pipeline complexity. This cost should be factored into architecture.

**Alternative:** Groq Whisper API has no stated file-size limit and may be faster/cheaper. Worth checking if file-size constraint becomes a bottleneck.

---

## Section 7 — Recommended Path Forward

**Decision tree outcome: WHOLE-FILE WHISPER path.**

Evidence:
1. The .sgxml does NOT contain per-stroke timestamps. It contains read-back sync points only.
2. 88 sync points for 50,363 strokes = ~572 strokes per sync point. Far too coarse for per-token lookup.
3. Coverage is 13% of the audio (45 min out of 340 min). No sync data for 87% of the file.
4. Even the covered sections have gaps up to 7.5 minutes between sync points.

The "slice on demand" architecture path is **not viable** with the data that exists in the .sgxml.

**Cost confirmed:** ~$1.02–$2.04 per Halprin-sized depo. The VC auditor's estimate of $2-3 was correct (high end). GPT-4o Mini Transcribe at $0.003/min brings it to ~$1.

**One open question for Opus:**
The binary `.sgngl` file was NOT examined. CATalyst may embed per-stroke audio offsets in the binary that are not exposed in the .sgxml. If Opus believes per-stroke data lives in the .sgngl, a separate B1b recon with a hex/binary parser would be needed. Sonnet's recommendation: park that as a future investigation and proceed with whole-file Whisper now. The cost is acceptable and the path is proven.

**File size constraint to design around:** 76 MB .opus > OpenAI 25 MB limit. Architecture must include pre-chunking step (ffmpeg, ~3 chunks for Halprin, proportionally more for longer depos).

---

*Generated by Sonnet #2, 2026-05-15. No engine commits. Knowledge capture only.*
*Scott reviews → Scott pushes to repo.*
