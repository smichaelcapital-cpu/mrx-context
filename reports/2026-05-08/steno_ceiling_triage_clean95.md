# Steno Ceiling Triage — Clean-95% Brandl Diff
**Generated:** 2026-05-08  
**Input:** `_diff_out_clean95/block_classification.json` — 746 blocks (clean 95% of Brandl depo)  
**Cobble contamination check:** Confirmed clean (bucket shape proportional to full 786-block diff)  
**Seam:** Truncated at OUR_FINAL page 348 / MB oracle line 7054 (turn_idx ~3500, below is_partial backup seam at 3565)  

---
## Headline Numbers
| Triage Bucket | Count | % of 746 | Description |
|---|---|---|---|
| **STAGE_2_RULE** | **390** | **52.3%** | Closeable by deterministic rule (M1-class) |
| **STAGE_3_LLM** | **97** | **13.0%** | Closeable by LLM prompting or dictionary |
| **AUDIO_REQUIRED** | **177** | **23.7%** | MB heard content steno cannot represent |
| **PER_CR_STYLE** | **82** | **11.0%** | MB-specific style choice, not steno-recoverable |
| **REPORTER_CRAFT** | **0** | **0.0%** | Pure judgment/craft, irreducible |
| **TOTAL** | **746** | 100% | |

## Ceiling Estimate
Of 746 clean-95% Brandl diff blocks, **487 (65.3%) are systematically closeable from steno alone** — 390 via Stage 2 deterministic rules and 97 via Stage 3 LLM/dictionary improvements — without requiring audio and without depending on MB-specific style codes. The remaining 259 blocks split between content MB heard from audio (177), MB editorial style choices (82), and irreducible reporter craft (0). This 65% ceiling is the upper bound of what the engine can close systematically given only the steno rough and a case-specific dictionary.

## Caveat
This triage is based on one deposition (Brandl, Yellow Rock v. Westlake) on a clean 95% slice (~3,500 of 3,691 turns). Brandl is a technical petroleum-engineering deposition with high proper-noun density (well names, formation codes, company names) and heavy exhibit use — both of which inflate AUDIO_REQUIRED and PER_CR_STYLE counts relative to a general deposition. The S2+S3 ceiling of 65% should be treated as a single-depo estimate pending validation against at least one more deposition (Halprin full run is the natural candidate). Additionally, the Q-label (M1 residual) blocks dominate Stage 2 — if M1 is rolled back pending MB's Brandl example, the S2 count shifts significantly.

---
## Cross-Tab: Original Bucket × Triage Bucket
| Orig | S2 | S3 | AU | PC | RC | Total |
|---|---|---|---|---|---|---|
| A | 122 | 36 | 17 | 0 | 0 | 175 |
| B | 244 | 27 | 151 | 81 | 0 | 503 |
| D | 24 | 34 | 9 | 1 | 0 | 68 |
| **ALL** | **390** | **97** | **177** | **82** | **0** | **746** |

---
## Original Sub-Category × Triage
| Sub-cat | Count | S2 | S3 | AU | PC | RC |
|---|---|---|---|---|---|---|
| cap_proper | 451 | 220 | 27 | 138 | 66 | 0 |
| unclear | 60 | 24 | 34 | 1 | 1 | 0 |
| word_drop | 51 | 42 | 0 | 9 | 0 | 0 |
| quote_marks | 51 | 24 | 0 | 13 | 14 | 0 |
| phonetic_error | 39 | 18 | 17 | 4 | 0 | 0 |
| doubled_word | 26 | 24 | 0 | 2 | 0 | 0 |
| acronym_mangle | 22 | 9 | 11 | 2 | 0 | 0 |
| hyphenation | 12 | 12 | 0 | 0 | 0 | 0 |
| number_style | 12 | 12 | 0 | 0 | 0 | 0 |
| pronoun_swap | 8 | 0 | 8 | 0 | 0 | 0 |
| objection_style | 5 | 5 | 0 | 0 | 0 | 0 |
| delete_only | 4 | 0 | 0 | 4 | 0 | 0 |
| insert_only | 4 | 0 | 0 | 4 | 0 | 0 |
| comma_punct | 1 | 0 | 0 | 0 | 1 | 0 |

---
## Worked Examples
### STAGE_2_RULE
- **Block #3** (orig A/word_drop)  
  MB:  `Q. Okay. **+Q.+** Have you been deposed before?`  
  OUR: `Q. Okay. Have you been deposed before?`  
  Reason: OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuation rule)  
  Fix: _Extend M1 rule to remaining s2 continuation edge cases; or tighten Q-drop classifier_  

- **Block #4** (orig A/word_drop)  
  MB:  `Q. Okay. **+Q.+** Approximately how many times?`  
  OUR: `Q. Okay. Approximately how many times?`  
  Reason: OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuation rule)  
  Fix: _Extend M1 rule to remaining s2 continuation edge cases; or tighten Q-drop classifier_  

- **Block #5** (orig B/cap_proper)  
  MB:  `A. **+Uhmm.+** I can't tell you the exact year, but I'll say it was 2017 or '18. Q. Okay. **+Q.+** A`  
  OUR: `A. **-Uhmm,-** I can't tell you the exact year, but I'll say it was 2017 or '18. Q. Okay. And what k`  
  Reason: OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuation rule)  
  Fix: _Extend M1 rule to remaining s2 continuation edge cases; or tighten Q-drop classifier_  

- **Block #7** (orig B/cap_proper)  
  MB:  `Q. Okay. **+Q.+** And were you giving factual testimony or expert testimony? And if you don't unders`  
  OUR: `Q. Okay. And were you giving factual testimony or expert testimony? And if you don't understand the `  
  Reason: OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuation rule)  
  Fix: _Extend M1 rule to remaining s2 continuation edge cases; or tighten Q-drop classifier_  

- **Block #8** (orig B/cap_proper)  
  MB:  `Q. Okay. **+Q.+** And what was the other deposition before that? A. 2003, it was a lawsuit between S`  
  OUR: `Q. Okay. And what was the other deposition before that? A. 2003, it was a lawsuit between Samedan a/`  
  Reason: OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuation rule)  
  Fix: _Extend M1 rule to remaining s2 continuation edge cases; or tighten Q-drop classifier_  


### STAGE_3_LLM
- **Block #6** (orig A/phonetic_error)  
  MB:  `Q. Was the legal dispute in court in LaFourche Parish or **+simply+** that's where the property was `  
  OUR: `Q. Was the legal dispute in court in LaFourche Parish or **-some-** **-ly-** that's where the proper`  
  Reason: Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover correct word  
  Fix: _Stage 3 writer prompt: flag phonetically-marked tokens for LLM rewrite with prior context_  

- **Block #28** (orig A/phonetic_error)  
  MB:  `A. I don't believe I am currently paying my dues to any **+professional+** **+organizations.+**`  
  OUR: `A. I don't believe I am currently paying my dues to any **-professionals-** **-organization.-**`  
  Reason: Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover correct word  
  Fix: _Stage 3 writer prompt: flag phonetically-marked tokens for LLM rewrite with prior context_  

- **Block #31** (orig A/pronoun_swap)  
  MB:  `Q. Onshore or offshore?`  
  OUR: `Q. **-On-** Onshore or offshore?`  
  Reason: Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence context recovers  
  Fix: _Stage 3 writer prompt: tighten function-word consistency in short Q./A. turns_  

- **Block #32** (orig B/cap_proper)  
  MB:  `Q. And how long were you first **+off,+** you started at Conoco in 1992?`  
  OUR: `Q. And how long were you first **-off-** you started at Conoco in 1992?`  
  Reason: Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary  
  Fix: _NAMES_LOCK expansion: add depo-specific proper nouns (Yellow Rock, CIB HAZ, etc.)_  

- **Block #34** (orig D/unclear)  
  MB:  `A. As an engineer or as an **+operator?+**`  
  OUR: `A. As an engineer or as an **-operator.-**`  
  Reason: Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from syntax  
  Fix: _Stage 3 prompt: normalize terminal punctuation via sentence-type classification_  


### AUDIO_REQUIRED
- **Block #1** (orig B/cap_proper)  
  MB:  `A. My name is Bradley **+Shay+** **+Brandl,+** but I go by Brad Brandl. Q. My name is Trey **+Peacoc`  
  OUR: `A. My name is Bradley **-Shea-** **-Brandl-** but I go by Brad Brandl. Q. My name is Trey **-Peacock`  
  Reason: Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from context/audio  

- **Block #9** (orig B/cap_proper)  
  MB:  `Q. What **+happened?+** **+Generally+** **+speaking.+** I don't need a lot of **+details.+** A. **+N`  
  OUR: `Q. What **-happened-** **-generally-** **-speaking-** I don't need a lot of **-details?-** A. **-No-`  
  Reason: Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from context/audio  

- **Block #10** (orig A/word_drop)  
  MB:  `Q. And you were **+the+** production engineer working for what company at that time?`  
  OUR: `Q. And you were production engineer working for what company at that time?`  
  Reason: MB has substantive words absent from OUR steno; reporter heard and filled from audio  

- **Block #16** (orig B/cap_proper)  
  MB:  `A. At that time I lived in **+Midtown+** no, the **+Museum+** **+District.+**`  
  OUR: `A. At that time I lived in **-midtown-** **-—-** no, the **-museum-** **-district.-**`  
  Reason: Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from context/audio  

- **Block #25** (orig B/cap_proper)  
  MB:  `Q. And do you keep **+this+** uptodate? A. I'll be **+honest,+** I can't remember when I last **+upd`  
  OUR: `Q. And do you keep **-up-to-date-** uptodate? A. I'll be **-honest-** I can't remember when I last *`  
  Reason: Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from context/audio  


### PER_CR_STYLE
- **Block #2** (orig B/cap_proper)  
  MB:  `Q. I'm going to go over some rules with you in just a moment, but first I've put in front of you Exh`  
  OUR: `Q. I'm going to go over some rules with you in just a moment, but first I've put in front of you Exh`  
  Reason: MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) from paper record  

- **Block #11** (orig B/cap_proper)  
  MB:  `Q. But the incident occurred after Noble **+completed+** its acquisition of Samedan? A. I am going t`  
  OUR: `Q. But the incident occurred after Noble its acquisition of Samedan? A. I am going to say I do not r`  
  Reason: Punctuation, structure, and capitalization combined; MB editorial style  

- **Block #24** (orig B/cap_proper)  
  MB:  `Q. I should go ahead and note we have marked Exhibit No. **+221,+** which I put in front of **+you.+`  
  OUR: `Q. I should go ahead and note we have marked Exhibit No. **-221-** which I put in front of **-you-**`  
  Reason: MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) from paper record  

- **Block #38** (orig B/cap_proper)  
  MB:  `A. So when **+I+** left **+I+** got they had another layoff at Conoco and I was transferred to San A`  
  OUR: `A. So when left got they had another layoff at Conoco and I was transferred to San **-San-** Angelo,`  
  Reason: Punctuation, structure, and capitalization combined; MB editorial style  

- **Block #47** (orig B/cap_proper)  
  MB:  `A. **+Uhmm.+** **+Maintain+** a drilling rig, being the drilling engineer for a drilling rig. I beli`  
  OUR: `A. **-Uhmm,-** **-maintain-** a drilling rig, being the drilling engineer for a drilling rig. I beli`  
  Reason: Punctuation, structure, and capitalization combined; MB editorial style  


### REPORTER_CRAFT

---
## Full Block-by-Block Table (746 rows)
| # | Orig | Sub | Triage | Reason | Fix Sketch |
|---|---|---|---|---|---|
| 1 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 2 | B | cap_proper | PER_CR_STYLE | MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) f |  |
| 3 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 4 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 5 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 6 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 7 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 8 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 9 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 10 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 11 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 12 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 13 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 14 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 15 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 16 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 17 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 18 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 19 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 20 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 21 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 22 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 23 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 24 | B | cap_proper | PER_CR_STYLE | MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) f |  |
| 25 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 26 | D | delete_only | AUDIO_REQUIRED | OUR has steno artifact (repeated text, miswrite) that MB corrected; requires aud |  |
| 27 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 28 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 29 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 30 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 31 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 32 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 33 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 34 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 35 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 36 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 37 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 38 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 39 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 40 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 41 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 42 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 43 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 44 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 45 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 46 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 47 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 48 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 49 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 50 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 51 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 52 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 53 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 54 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 55 | D | insert_only | AUDIO_REQUIRED | MB has content OUR lacks entirely; transcript content MB added from audio/notes |  |
| 56 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 57 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 58 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 59 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 60 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 61 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 62 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 63 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 64 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 65 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 66 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 67 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 68 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 69 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 70 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 71 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 72 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 73 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 74 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 75 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 76 | A | objection_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 77 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 78 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 79 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 80 | A | phonetic_error | AUDIO_REQUIRED | Large phonetic error (3+ tokens, structurally different); steno alone insufficie |  |
| 81 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 82 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 83 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 84 | A | objection_style | STAGE_2_RULE | Objection phrasing difference ('Objection' vs 'Object') or steno hyphen-run in o | Stage 2 rule: normalize 'Objection' → 'Object' in MR. colloq |
| 85 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 86 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 87 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 88 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 89 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 90 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 91 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 92 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 93 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 94 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 95 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 96 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 97 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 98 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 99 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 100 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 101 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 102 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 103 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 104 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 105 | D | unclear | STAGE_2_RULE | OUR has spurious repeated word/phrase; deduplication rule (Stage 2 dedupe_audit  | Stage 2: extend deduplicate rule to catch cross-sentence wor |
| 106 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 107 | D | insert_only | AUDIO_REQUIRED | MB has content OUR lacks entirely; transcript content MB added from audio/notes |  |
| 108 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 109 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 110 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 111 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 112 | A | hyphenation | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 113 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 114 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 115 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 116 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 117 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 118 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 119 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 120 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 121 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 122 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 123 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 124 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 125 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 126 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 127 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 128 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 129 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 130 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 131 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 132 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 133 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 134 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 135 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 136 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 137 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 138 | A | phonetic_error | AUDIO_REQUIRED | Large phonetic error (3+ tokens, structurally different); steno alone insufficie |  |
| 139 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 140 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 141 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 142 | A | objection_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 143 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 144 | A | objection_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 145 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 146 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 147 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 148 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 149 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 150 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 151 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 152 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 153 | A | objection_style | STAGE_2_RULE | Objection phrasing difference ('Objection' vs 'Object') or steno hyphen-run in o | Stage 2 rule: normalize 'Objection' → 'Object' in MR. colloq |
| 154 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 155 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 156 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 157 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 158 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 159 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 160 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 161 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 162 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 163 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 164 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 165 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 166 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 167 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 168 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 169 | A | number_style | STAGE_2_RULE | Digit vs word-form number mismatch (e.g. '6 to 1' vs 'six to one') | Stage 2 T5-NumberStyle rule extension: bidirectional digit/w |
| 170 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 171 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 172 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 173 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 174 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 175 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 176 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 177 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 178 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 179 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 180 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 181 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 182 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 183 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 184 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 185 | A | acronym_mangle | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 186 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 187 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 188 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 189 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 190 | B | comma_punct | PER_CR_STYLE | Comma/punctuation insertion by MB; editorial style not recoverable from steno |  |
| 191 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 192 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 193 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 194 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 195 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 196 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 197 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 198 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 199 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 200 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 201 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 202 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 203 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 204 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 205 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 206 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 207 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 208 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 209 | D | unclear | AUDIO_REQUIRED | Substantive multi-word difference; steno captured differently from audio; requir |  |
| 210 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 211 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 212 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 213 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 214 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 215 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 216 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 217 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 218 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 219 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 220 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 221 | A | number_style | STAGE_2_RULE | Digit vs word-form number mismatch (e.g. '6 to 1' vs 'six to one') | Stage 2 T5-NumberStyle rule extension: bidirectional digit/w |
| 222 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 223 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 224 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 225 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 226 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 227 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 228 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 229 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 230 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 231 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 232 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 233 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 234 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 235 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 236 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 237 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 238 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 239 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 240 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 241 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 242 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 243 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 244 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 245 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 246 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 247 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 248 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 249 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 250 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 251 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 252 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 253 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 254 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 255 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 256 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 257 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 258 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 259 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 260 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 261 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 262 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 263 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 264 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 265 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 266 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 267 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 268 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 269 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 270 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 271 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 272 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 273 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 274 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 275 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 276 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 277 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 278 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 279 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 280 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 281 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 282 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 283 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 284 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 285 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 286 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 287 | D | delete_only | AUDIO_REQUIRED | OUR has steno artifact (repeated text, miswrite) that MB corrected; requires aud |  |
| 288 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 289 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 290 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 291 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 292 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 293 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 294 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 295 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 296 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 297 | A | acronym_mangle | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 298 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 299 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 300 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 301 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 302 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 303 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 304 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 305 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 306 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 307 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 308 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 309 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 310 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 311 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 312 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 313 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 314 | B | cap_proper | PER_CR_STYLE | MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) f |  |
| 315 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 316 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 317 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 318 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 319 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 320 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 321 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 322 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 323 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 324 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 325 | D | unclear | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 326 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 327 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 328 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 329 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 330 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 331 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 332 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 333 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 334 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 335 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 336 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 337 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 338 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 339 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 340 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 341 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 342 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 343 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 344 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 345 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 346 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 347 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 348 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 349 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 350 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 351 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 352 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 353 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 354 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 355 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 356 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 357 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 358 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 359 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 360 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 361 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 362 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 363 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 364 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 365 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 366 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 367 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 368 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 369 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 370 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 371 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 372 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 373 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 374 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 375 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 376 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 377 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 378 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 379 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 380 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 381 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 382 | A | hyphenation | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 383 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 384 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 385 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 386 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 387 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 388 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 389 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 390 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 391 | D | delete_only | AUDIO_REQUIRED | OUR has steno artifact (repeated text, miswrite) that MB corrected; requires aud |  |
| 392 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 393 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 394 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 395 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 396 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 397 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 398 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 399 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 400 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 401 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 402 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 403 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 404 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 405 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 406 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 407 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 408 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 409 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 410 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 411 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 412 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 413 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 414 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 415 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 416 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 417 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 418 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 419 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 420 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 421 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 422 | A | phonetic_error | AUDIO_REQUIRED | Large phonetic error (3+ tokens, structurally different); steno alone insufficie |  |
| 423 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 424 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 425 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 426 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 427 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 428 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 429 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 430 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 431 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 432 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 433 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 434 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 435 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 436 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 437 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 438 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 439 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 440 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 441 | B | quote_marks | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 442 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 443 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 444 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 445 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 446 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 447 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 448 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 449 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 450 | A | doubled_word | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 451 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 452 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 453 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 454 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 455 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 456 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 457 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 458 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 459 | D | delete_only | AUDIO_REQUIRED | OUR has steno artifact (repeated text, miswrite) that MB corrected; requires aud |  |
| 460 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 461 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 462 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 463 | D | unclear | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 464 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 465 | B | quote_marks | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 466 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 467 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 468 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 469 | D | unclear | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 470 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 471 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 472 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 473 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 474 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 475 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 476 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 477 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 478 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 479 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 480 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 481 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 482 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 483 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 484 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 485 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 486 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 487 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 488 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 489 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 490 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 491 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 492 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 493 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 494 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 495 | A | doubled_word | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 496 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 497 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 498 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 499 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 500 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 501 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 502 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 503 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 504 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 505 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 506 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 507 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 508 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 509 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 510 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 511 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 512 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 513 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 514 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 515 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 516 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 517 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 518 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 519 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 520 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 521 | B | cap_proper | PER_CR_STYLE | MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) f |  |
| 522 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 523 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 524 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 525 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 526 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 527 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 528 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 529 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 530 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 531 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 532 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 533 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 534 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 535 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 536 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 537 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 538 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 539 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 540 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 541 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 542 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 543 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 544 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 545 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 546 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 547 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 548 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 549 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 550 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 551 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 552 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 553 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 554 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 555 | D | unclear | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 556 | D | unclear | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 557 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 558 | D | unclear | STAGE_3_LLM | Terminal punctuation mismatch (. vs ?); LLM can infer statement vs question from | Stage 3 prompt: normalize terminal punctuation via sentence- |
| 559 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 560 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 561 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 562 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 563 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 564 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 565 | A | number_style | STAGE_2_RULE | Digit vs word-form number mismatch (e.g. '6 to 1' vs 'six to one') | Stage 2 T5-NumberStyle rule extension: bidirectional digit/w |
| 566 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 567 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 568 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 569 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 570 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 571 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 572 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 573 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 574 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 575 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 576 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 577 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 578 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 579 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 580 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 581 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 582 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 583 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 584 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 585 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 586 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 587 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 588 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 589 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 590 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 591 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 592 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 593 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 594 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 595 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 596 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 597 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 598 | D | insert_only | AUDIO_REQUIRED | MB has content OUR lacks entirely; transcript content MB added from audio/notes |  |
| 599 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 600 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 601 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 602 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 603 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 604 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 605 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 606 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 607 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 608 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 609 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 610 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 611 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 612 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 613 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 614 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 615 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 616 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 617 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 618 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 619 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 620 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 621 | A | number_style | STAGE_2_RULE | Digit vs word-form number mismatch (e.g. '6 to 1' vs 'six to one') | Stage 2 T5-NumberStyle rule extension: bidirectional digit/w |
| 622 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 623 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 624 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 625 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 626 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 627 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 628 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 629 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 630 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 631 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 632 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 633 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 634 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 635 | A | acronym_mangle | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 636 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 637 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 638 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 639 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 640 | A | doubled_word | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 641 | D | unclear | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 642 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 643 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 644 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 645 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 646 | A | word_drop | AUDIO_REQUIRED | MB has substantive words absent from OUR steno; reporter heard and filled from a |  |
| 647 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 648 | A | hyphenation | STAGE_2_RULE | Compound word written split/joined by steno but MB normalizes (e.g. one-third vs | Stage 2 T-Compound rule: add compound word join/split normal |
| 649 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 650 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 651 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 652 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 653 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 654 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 655 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 656 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 657 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 658 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 659 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 660 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 661 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 662 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 663 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 664 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 665 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 666 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 667 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 668 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 669 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 670 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 671 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 672 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 673 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 674 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 675 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 676 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 677 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 678 | A | number_style | STAGE_2_RULE | Digit vs word-form number mismatch (e.g. '6 to 1' vs 'six to one') | Stage 2 T5-NumberStyle rule extension: bidirectional digit/w |
| 679 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 680 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 681 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 682 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 683 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 684 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 685 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 686 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 687 | A | number_style | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 688 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 689 | A | phonetic_error | STAGE_3_LLM | Near-phonetic substitution (1-3 tokens); LLM with sentence context can recover c | Stage 3 writer prompt: flag phonetically-marked tokens for L |
| 690 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 691 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 692 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 693 | A | phonetic_error | AUDIO_REQUIRED | Large phonetic error (3+ tokens, structurally different); steno alone insufficie |  |
| 694 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 695 | A | doubled_word | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 696 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 697 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 698 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 699 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 700 | A | phonetic_error | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 701 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 702 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 703 | A | doubled_word | STAGE_2_RULE | Doubled steno token in OUR; is_doubled classifier (3a) suppresses most, residual | Extend 3b D-DOUBLED-WORD rule to across-punct and cross-turn |
| 704 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 705 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 706 | B | quote_marks | PER_CR_STYLE | MB adds quotation marks as style choice; steno rough does not capture quote attr |  |
| 707 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 708 | A | pronoun_swap | STAGE_3_LLM | Function word / pronoun substitution (e.g. 'the'/'a' swap); LLM with sentence co | Stage 3 writer prompt: tighten function-word consistency in  |
| 709 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 710 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 711 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 712 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 713 | B | cap_proper | PER_CR_STYLE | MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) f |  |
| 714 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 715 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 716 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 717 | B | cap_proper | STAGE_3_LLM | Pure capitalization diff; proper noun known to NAMES_LOCK or per-depo dictionary | NAMES_LOCK expansion: add depo-specific proper nouns (Yellow |
| 718 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 719 | A | word_drop | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 720 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 721 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 722 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 723 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 724 | A | pronoun_swap | STAGE_3_LLM | Missing function word in OUR; LLM context can recover correct article/prepositio | Stage 3 prompt: flag single-token function-word drops for LL |
| 725 | D | insert_only | AUDIO_REQUIRED | MB has content OUR lacks entirely; transcript content MB added from audio/notes |  |
| 726 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 727 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 728 | B | quote_marks | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 729 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 730 | D | unclear | STAGE_3_LLM | Small word substitution; LLM with sentence context can recover correct phrasing | Stage 3 writer prompt: flag short substitution anomalies for |
| 731 | A | acronym_mangle | STAGE_3_LLM | Acronym or technical term mangled by steno; domain dictionary + LLM context can  | Stage 3: inject per-depo technical lexicon into writer promp |
| 732 | D | unclear | PER_CR_STYLE | MB adds exhibit colloquy (Whereupon, Exhibit No. X, marked for Identification) f |  |
| 733 | B | cap_proper | PER_CR_STYLE | Punctuation, structure, and capitalization combined; MB editorial style |  |
| 734 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 735 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 736 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 737 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 738 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 739 | B | cap_proper | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 740 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 741 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 742 | B | cap_proper | STAGE_2_RULE | OUR collapsed Q./A. turn boundary that MB preserves; M1 residual (s2-continuatio | Extend M1 rule to remaining s2 continuation edge cases; or t |
| 743 | B | quote_marks | AUDIO_REQUIRED | Steno left *REPORTER CHECK HERE* marker; MB filled from audio/tape |  |
| 744 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
| 745 | B | cap_proper | STAGE_2_RULE | Unknown RTF \sN style code (\s943/\s109431) leaking as literal text in OUR | RTF parser: map \s943, \s109431, \s2018/19/20/21 style codes |
| 746 | B | cap_proper | AUDIO_REQUIRED | Proper name spelling differs (e.g. Shay/Shea, Bertelot/Bertolet); MB knows from  |  |
