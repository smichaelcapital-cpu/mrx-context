# Repo Inventory — Audio + Fingerprint Design Discovery
Date: 2026-05-13
Captured by: Sonnet at Opus's request
Purpose: Source-of-truth inventory of all design docs, raw/FINAL/audio assets, and dated artifacts as of 2026-05-13. Used by Opus to ramp on the audio + fingerprint architecture without flying blind.

---

## DIRECTORY FILE COUNTS (mrx-context)

| Directory | File Count |
|---|---|
| `backlog/` | 1 |
| `design/` | 1 |
| `fingerprints/` | 8 (incl. .gitkeep placeholders) |
| `knowledge/` | 11 |
| `reports/` | 38 |
| `specs/` | 42 (incl. `specs/results/` subfolder) |
| `handoffs/` | 78 total |

---

## DESIGN / SPEC / ARCHITECTURE FILES (named themes)

- `backlog/THREE_SEALED_PHASES.md` (1,897 bytes)
- `design/fingerprint_architecture_copilot_2026-05-08.md` (9,051 bytes)
- `knowledge/FINGERPRINT_DATA_ARCHITECTURE.md` (30,974 bytes)
- `knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md` (8,665 bytes)
- `knowledge/FUTURE_STATE_AGENT_AGENCY.md` (8,812 bytes)
- `knowledge/PRODUCT_VISION_GOLDEN_CIRCLE.md` (7,293 bytes)
- `knowledge/fingerprint_architecture_decisions.md` (4,152 bytes)
- `handoffs/SPEC — Overnight Fingerprint Recon Run.md` (21,190 bytes) — untracked, not committed
- `mrx_depo_library/_design/fingerprint_architecture_chatgpt_2026-05-08.md` (9,051 bytes) — outside mrx-context
- `specs/2026-05-09_FINGERPRINT_V0_SPEC.md` (13,856 bytes)
- `specs/2026-05-10_OVERNIGHT_RECON_SPEC.md` (21,656 bytes)
- `specs/STAGE_5_v01_BUILD_SPEC.md` (16,828 bytes) + all STAGE_5_MODULE_*.md files

---

## RAW RTF + FINAL PAIR INVENTORY

### MB (Marybeth E. Muir) — canonical library at `mrx_depo_library/MB/`

| Depo | Raw RTF | FINAL .txt | Audio | Triple? |
|---|---|---|---|---|
| halprin_040226 | `040226yellowrock-ROUGH_Tsmd.rtf` | `040226yellowrock-FINAL.txt` | `040226yellowrock-ROUGH.opus` (79MB) | **YES — full triple** |
| brandl_032626 | `032626YELLOWROCK-FINAL_T.rtf` (this is the FINAL rtf, no separate rough) | `BRANDL_MB_FINAL.txt` | `032626YELLOWROCK-FINAL.opus` (99MB) | FINAL+audio only (no rough) |
| easley_031326 | `031326yellowrock-ROUGH_T_1.rtf` | `Easley_YellowRock_FINAL_TRANSCRIPT.txt` + PDF | none | **Pair only** |
| jp_042726 | `042726jp-ROUGH.rtf` | none | `042726jp-ROUGH.opus` (59MB) | **Raw+audio only — no FINAL** |

### AD (cross_depo_scan reporters — not MB)

| Depo | Raw RTF | FINAL |
|---|---|---|
| brandl/032626YELLOWROCK_smd_T | RTF in cross_depo_scan | none in library |
| easley/031326yellowrock-ROUGH_T_1 | RTF | none |
| fourman/0324Fourman2026_T | RTF | none |
| leon/0313Leon2026_T | RTF | none |
| wade/0323Wade2026_T | RTF | none |

AD depos: raw RTF only in cross_depo_scan. No FINALs present. Reporter identity not confirmed from this scan (could be AD or other).

### oracle/finals (mrx-context, shape-match targets — FINAL only, no raws)

- `halprin/040226yellowrock-FINAL.txt` + `.rtf`
- `032025olsen/032025olsen-FINAL.txt`
- `0525black_bp/0525black-bp-FINAL.txt`
- `060122williams/060122williams-FINAL.txt`
- `082222butler/082222butler-FINAL.txt`
- `101322blanks/101322blanks-FINAL.txt`
- `brandl/BRANDL_MB_FINAL.txt`

---

## AUDIO FILE INVENTORY

| Location | File | Format | Size | Notes |
|---|---|---|---|---|
| `mrx_depo_library/MB/halprin_040226/input/` | `040226yellowrock-ROUGH.opus` | Opus | 79MB | Real depo audio |
| `mrx_depo_library/MB/brandl_032626/input/` | `032626YELLOWROCK-FINAL.opus` | Opus | 99MB | Real depo audio |
| `mrx_depo_library/MB/jp_042726/input/` | `042726jp-ROUGH.opus` | Opus | 59MB | Real depo audio |
| `mrx_engine_v1/io/analysis/brandl_50pp/audio/` | `brandl_0-40min.opus` | Opus | 9MB | 40-min extract |
| `mrx_engine_v1/io/analysis/brandl_50pp/audio/` | `brandl_full.opus` | Opus | 99MB | Full brandl audio |
| `mrx_engine_v1/io/analysis/brandl_50pp/audio/` | `brandl_0-40min.json/.srt/.tsv/.txt/.vtt` | Whisper outputs | varies | Already transcribed |
| `Documents/25-60108_01-08-2026.mp3` | MP3 | 1 file | loose | Unknown depo — not in library |
| `mb_demo_engine_v4/test_audio/` | `sample_depo.mp3` | MP3 | multiple copies in worktrees | Synthetic sample |

**No `.wav` or `.m4a` files found.** All real audio is `.opus`. One mystery `.mp3` at root of Documents (`25-60108_01-08-2026.mp3`).

---

## INVENTORY COUNTS (summary)

| Category | Count |
|---|---|
| Raw+FINAL+Audio triple | 1 (Halprin/MB) |
| Raw+FINAL pair (no audio) | 1 (Easley/MB) |
| FINAL+Audio (no raw rough) | 1 (Brandl/MB) |
| Raw+Audio (no FINAL) | 1 (jp_042726/MB) |
| Raw only (cross_depo_scan) | 5 (AD/other reporters) |
| FINAL only (oracle targets) | 7 (mrx-context/oracle/finals) |

---

## FINGERPRINT/AUDIO/COMPREHENSION FILES DATED 2026-05-08 THROUGH 2026-05-12

- `design/fingerprint_architecture_copilot_2026-05-08.md`
- `knowledge/FINGERPRINT_DATA_ARCHITECTURE.md`
- `knowledge/FINGERPRINT_FACTORY_REQUIREMENTS.md`
- `knowledge/FUTURE_STATE_AGENT_AGENCY.md`
- `knowledge/fingerprint_architecture_decisions.md`
- `reports/2026-05-08/steno_ceiling_triage_clean95.md` (133KB — revised bucket counts)
- `reports/2026-05-09/brandl_v0_fingerprint_run.md`
- `reports/2026-05-10/fingerprint_spot_check_summary.md`
- `reports/2026-05-10/eval_run_v1_pattern_level.md`
- `reports/2026-05-11/overnight_recon_summary.md` (mentions audio/comprehension context)
- `reports/2026-05-11/lexical_layer_verdict.md`
- `specs/2026-05-09_FINGERPRINT_V0_SPEC.md`
- `specs/2026-05-10_OVERNIGHT_RECON_SPEC.md`
- `knowledge/2026-05-12_NY_workers_comp_pipeline.md`
- Whisper outputs already run on Brandl 0-40min: `.json/.srt/.tsv/.txt/.vtt` in `mrx_engine_v1/io/analysis/brandl_50pp/audio/`
