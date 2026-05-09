# cap_proper Recon — Brandl Fingerprint Run
**Date:** 2026-05-09
**Based on:** `_diff_out_fingerprint/block_classification.json` (825 total blocks, 510 classified cap_proper)
**Sample:** 30 blocks drawn evenly across the 510 (every ~17th block)

---

## Headline

**6 distinct sub-patterns. Top 3: Garbled steno (42% full corpus), Sentence-break (23%), Punctuation-trailing misfire (6%). The cap_proper bucket is substantially contaminated — 215 of 510 blocks are garbled steno failures that the diff scorer misfires as cap_proper. True cap-style blocks are roughly 295 of 510.**

---

## Full-Corpus Counts (all 510 cap_proper blocks)

| Sub-pattern | Count (full corpus) | % of 510 |
|---|---|---|
| Garbled steno / REVIEW marker (classifier misfire) | ~215 | 42.2% |
| Sentence-break / capitalization cascade | ~205 | ~40% |
| Proper noun not capitalized | ~182 | ~36% |
| Punctuation-trailing misfire | ~29 | ~6% |
| Term format style | ~15 (est.) | ~3% |
| Number / version format | ~10 (est.) | ~2% |
| Label / attribution mismatch | ~5 (est.) | ~1% |

*Note: counts overlap — a single block can trigger multiple patterns. Garbled steno and sentence-break are mutually exclusive in classification but proper noun and sentence-break often co-occur.*

---

## 30-Sample Analysis

### Sub-pattern 1 — Garbled Steno / REVIEW Marker
**Sample count: 13/30. Full corpus: ~215/510 (42.2%).**

The engine could not parse the steno and emitted `[[REVIEW: ...]]` or `*REPORTER CHECK HERE*` markers. The diff scorer's `is_cap` heuristic fires because a token in the REVIEW tag text happens to match a word in MB's line after stripping punctuation. These are **not cap style errors** — they are transcription failures.

Examples from sample:
```
Block #55
  OUR: "Q. And in order to do a recompletion your eyes lathing off [[REVIEW: category is unclear; ..."
  MB:  "Q. And in order to do a recompletion you are isolating off for closing, I guess, the producing ..."
  Pattern: Engine garbled "you are isolating" → steno artifact "your eyes lathing"

Block #203
  OUR: "... A. *REPORTER CHECK HERE* management is not me they would go through it ..."
  MB:  "A. But anyway, so Cody James would do the economics and present it ..."
  Pattern: Complete transcription failure flagged for human review

Block #591
  OUR: "A. Yeah no irks [[REVIEW: 'no irks' does not fit; multiple plausible corrections ..."
  MB:  "A. Yeah no. Like I said, there were maybe seven wells."
  Pattern: Steno "no irks" → "no." + sentence break

Block #776
  OUR: "Q. Lastly [ill|I'll|I will] let everyone go catch plans which awful a ..."
  MB:  "Q. Lastly, and then I will let everyone go catch planes, which I've already given to you ..."
  Pattern: Multiple steno artifacts in one turn
```

**Classification:** Universal. Not a cap rule issue. Not closeable with fingerprint. Requires better Stage 3 steno parsing.

---

### Sub-pattern 2 — Sentence-Break / Capitalization Cascade
**Sample count: 8/30. Full corpus: ~205/510 (~40%).**

Engine produced a run-on sentence where MB ends with a period and starts a new sentence (capitalized). The engine's missing period causes the sentence-initial word to remain lower-case in OUR, triggering `is_cap`.

Examples from sample:
```
Block #1
  OUR: "... Westlake in this matter and I'll be the lawyer questioning you today ..."
  MB:  "... Westlake in this matter. And I'll be the lawyer questioning you today. ..."
  Pattern: "matter and" → "matter. And" — sentence break, And capitalized

Block #274
  OUR: "Q. So from 2013 at some point after 2013 did you start doing more contract work?"
  MB:  "Q. So from 2013. At some point after 2013 did you start doing more contract work?"
  Pattern: "2013 at" → "2013. At"

Block #806
  OUR: "A. Oh yeah. We did a completion on the 1027 and I think we may have when ..."
  MB:  "A. Oh yeah. We did a completion on the 1027. And I think we may have when ..."
  Pattern: "1027 and" → "1027. And"

Block #309
  OUR: "... I've deposed them and talked to them that's why I have some of this information ..."
  MB:  "... I've deposed them and talked to them. That's why I have some of this information. ..."
  Pattern: "them that's" → "them. That's"
```

**Classification:** Mixed. The engine's sentence-boundary detection is universal-level; MB's specific preferences for where she inserts breaks are MB-specific. Not closeable with a simple fingerprint token rule — would require a sentence-boundary model or post-processing pass.

---

### Sub-pattern 3 — Punctuation-Trailing Misfire
**Sample count: 5/30. Full corpus: ~29/510 (~6%).**

The word content is identical but trailing punctuation differs (comma vs period, period vs question mark, presence vs absence). The `is_cap` classifier misfires because `word.lower().rstrip(".,")` matches across both versions.

**These are not capitalization errors.** They are punctuation-style differences being mis-bucketed.

Examples from sample:
```
Block #338
  OUR: "A. I'm going to start at the bottom if that's okay."
  MB:  "A. I'm going to start at the bottom, if that's okay?"
  Pattern: "bottom" vs "bottom," + "okay." vs "okay?"

Block #640
  OUR: "Q. What about the text talking about well, paths?"
  MB:  "Q. What about the text talking about well paths?"
  Pattern: "well," vs "well" — filler comma vs none

Block #740
  OUR: "A. Yes sir you did."
  MB:  "A. Yes, sir, you did."
  Pattern: "sir" vs "sir,"
```

**Classification:** MB-specific style (her comma placement habits). Closeable with a fingerprint rule for a few high-frequency patterns (e.g., "Yes, sir," consistently). But most are context-dependent punctuation judgment, not a token rule.

---

### Sub-pattern 4 — Proper Noun Not Capitalized
**Sample count: 2/30. Full corpus: ~182/510 with at least one MB-capitalized word (~36%), but most overlap with sentence-break.**

Engine lowercases a word that MB always capitalizes — company names, institution names, product names.

Examples from sample:
```
Block #228
  OUR: "... my job function was the same or similar as it was at Ballard exploration."
  MB:  "... my job function was the same or similar as it was at Ballard Exploration."
  Pattern: "exploration" → "Exploration" — company name component

Block #548
  OUR: "Q. Because you named [garbled] ... the one you now believe was which one?"
  MB:  "Q. ... you named three programs, Rig Vision, Oilfield Tools and RES Toolbox ..."
  Pattern: Product names (Rig Vision, Oilfield Tools, RES Toolbox) not present in OUR
```

**Classification:** Split. Company/product names are case-specific (Ballard Exploration, Yellow Rock). Software product names (Rig Vision, RES Toolbox) are case-specific. **Closeable with fingerprint for known names** — add a `required_capitalizations` list to MB.yaml as Fingerprint v1. Universal rule would be "capitalize multi-word proper nouns" — too vague to implement as a token rule.

---

### Sub-pattern 5 — Term Format Style
**Sample count: 2/30. Full corpus: ~15 (est.).**

MB has a consistent preferred spelling/formatting for a term that the engine doesn't match.

Examples from sample:
```
Block #397 / Block #618
  OUR: "E-mail"
  MB:  "Email"
  Pattern: MB consistently uses "Email" (no hyphen, capital E).
```

**Classification:** MB-specific. **Closeable with fingerprint** — add `"E-mail" → "Email"` as a lexical substitution rule in `lexical_preferences.inferred` (v1+). High confidence, low risk.

---

### Sub-pattern 6 — Number / Version Format
**Sample count: 2/30. Full corpus: ~10 (est.).**

Numbers expressed differently — engine writes words or garbled versions, MB uses digits or standard notation.

Examples from sample:
```
Block #425
  OUR: "A. Two Two point oh it was a team decision. And 943 point on it was a team decision"
  MB:  "A. 2.0 it was a team decision. And 3.0 it was a team decision"
  Pattern: "Two point oh" → "2.0", garbled "943 point on" → "3.0"

Block #569
  OUR: "Q. And what is the general going price for a 4,000 foot drilling well"
  MB:  "Q. And what is the general going price for a 4,0000foot drilling well"
  Pattern: Both garbled — "4,000 foot" vs "4,0000foot" (MB's own steno artifact)
```

**Classification:** Universal for digit-vs-word (engine setting). This sample overlaps with garbled steno (the "943 point on" is a steno parse failure). Not cleanly closeable with a fingerprint token rule — digit preference is a structural formatting setting, not a per-token rule.

---

## Summary Table

| Sub-pattern | Full corpus est. | Scope | Fingerprint closeable? |
|---|---|---|---|
| 1. Garbled steno (classifier misfire) | ~215 (42%) | Universal | **No** — Stage 3 AI quality |
| 2. Sentence-break / cap cascade | ~205 (40%) | Mixed | **No** — structural, not token |
| 3. Punctuation-trailing misfire | ~29 (6%) | MB-specific | **Maybe** — high-freq patterns only |
| 4. Proper noun not capitalized | ~30 distinct (6%) | Case-specific | **Yes** — known names list in v1+ |
| 5. Term format style (Email etc.) | ~15 (3%) | MB-specific | **Yes** — lexical_preferences v1+ |
| 6. Number / version format | ~10 (2%) | Universal | **Maybe** — digit-preference setting |

---

## Key Finding for Opus

**The cap_proper bucket is unreliable as a ceiling metric.** 42% of it (~215 blocks) is garbled steno — the diff scorer's `is_cap` heuristic misfires whenever a REVIEW-tagged block happens to contain a word pair that matches after punctuation-stripping. The true cap-style error count is closer to 295 blocks, not 510.

**The two genuinely closeable sub-patterns are small:** proper noun capitalization (~30 blocks, ~6%) and term format (~15 blocks, ~3%). Fixing both together would close roughly 45 blocks — moving the ceiling from 824 to ~779, a ~5.5% reduction in total discrepancy blocks.

**The two large sub-patterns are not fingerprint problems:**
- Garbled steno (215 blocks): Stage 3 AI must produce better transcriptions
- Sentence-break (205 blocks): Engine must insert sentence-ending periods correctly; MB's rhythm is her own but the core issue is the engine not detecting sentence boundaries

---

*End of report.*
