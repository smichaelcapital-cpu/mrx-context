# Sonnet #1 EOD Handoff — 2026-05-14 10:30 PM

## Branch state
- Working branch: feature/stage-a-aligner-differ-v0
- Pushed at commit 6d330aa
- Main last known good: 95f09ee
- NOT merged to main — pending Opus architect review of word_substitution + categorizer issues

## Tonight's work — chronological

### Move 1 complete
- Moved 3 export pairs from C:\Cat4\usr\scott\ASAP\ into mrx_depo_library structure: fountain_011923, zannetti_080221, hebert_011723
- Dropped zannetti_080321 (no FINAL on disk)
- Dropped zannetti_080221 (1.98x ratio — wrong pair, PROG-PM was partial session not full depo)
- Updated src/aligner_differ/pairs.json — dropped church, added 8 new, dropped zannetti_080221
- Final pairs.json count: 9

### Stage A 9-pair run
- 631,209 diff events, 125,851 patterns
- All ratios in range: 0.63x (hebert) to 1.31x (martin)
- Output: mb_evidence_raw.json + mb_frequency_summary.json at C:\Users\scott\OneDrive\Documents\mrx-context\fingerprints\stage_a\

### Move B hunt analysis
- Wrote: C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_stage_a_9pair_hunt.md
- Applied 8 anti-fail rules (filtered noise, normalized by rate, hunted 70-99% band, surfaced negative fingerprint)

## Key findings (signal vs noise)

### Real signal
- em_dash_inserted: 1,151 events, ALL 9 depos, ALL '--' form. Cleanest habit found. Candidate for MB.yaml v0.1 first entry.
- filler_word_removed: 286 events, 9/9 depos, mostly "like". Real but sparse. Caveat: CATalyst may suppress uh/um at steno time.

### Noise disguised as signal — flagged for Opus
- word_substitution (139,912 events) — alignment garbage. Aligner matched wrong tokens (mail→Top, mail→Raise). NOT habits. Differ v0.2 needs bounded matching or exclusion of this category.
- proper_noun_change top 3 are Q→A and A→Q — speaker label churn mislabeled. Categorizer v0.2 needs Q/A bucket before proper_noun classification.

### Architectural finding
The fingerprint cannot work at the token-pair level. It must operate at category+context level. MB.yaml v0.1 shape from April assumed token-pair patterns — needs redesign.

## Round 2 dataset queued (tomorrow)
Sonnet #2 found 2 new GUID-confirmed pairs + 3 fast-path candidates with FINAL .txt already on disk:
- Rooks_011121 (BP folder, GUID confirmed)
- Nguyen_033022 (BP folder, GUID confirmed)
- Thompson, Washington, Black (BP folder, FINAL .txt on disk, ROUGH needs CATalyst export)

See: C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_sonnet2_recon_results.md Section 7

## Next session first moves
1. Opus architect review of word_substitution + categorizer issues — decide v0.2 spec
2. CATalyst export of Rooks/Nguyen ROUGH + Thompson/Washington/Black ROUGH
3. Move all new pairs into mrx_depo_library structure
4. Re-run Stage A on 14 pairs
5. Decide: ship em_dash as MB.yaml v0.1 first entry?

## Files written tonight (Sonnet #1)
- C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\HANDOFF_SONNET1_2026-05-14_8PM_MIDSESSION.md (earlier)
- C:\Users\scott\OneDrive\Documents\mrx-context\audits\2026-05-14_VC_AUDITOR_TEARDOWN.md (commit 4f53b44)
- C:\Users\scott\OneDrive\Documents\mrx-context\knowledge\2026-05-14_evening_stage_a_9pair_hunt.md
- This handoff

# End of handoff
