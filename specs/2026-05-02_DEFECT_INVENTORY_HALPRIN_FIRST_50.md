# DEFECT INVENTORY — Halprin mini, first 50 pages
**Date:** 2026-05-02
**Analyst:** Sonnet (at Opus direction)
**Scope:** Pages 13–50 of Halprin mini OUR_FINAL vs MB FINAL
  (Pages 1–12 are caption/appearances — skipped per spec)

**Method:** Targeted pattern search (difflib alignment proves unreliable due to
line-wrapping shifts caused by corrections; pattern search is authoritative).

**Oracle:** `oracle/finals/halprin/040226yellowrock-FINAL.txt`
**OUR_FINAL:** `io/analysis/halprin_mini/_stage5_out/halprin_mini.OUR_FINAL.txt`

---

## ENGINE ACTIVITY SUMMARY

Engine touched **114 turns** across first 50 pages:
- `{{MB_REVIEW-FIX}}` (high-confidence corrections): **63**
- `{{MB_REVIEW-VERIFY}}` (medium-confidence):         **10**
- `{{MB_REVIEW-FLAG}}` (needs human review):          **41**

Note: these are the engine's proposals that passed validate_ops and were
written to OUR_FINAL. Does NOT count proposals silently dropped by
check_word_budget or check_coverage.

---

## DEFECT INVENTORY BY CATEGORY

### CAT-1: STYLE GAP — sentence spacing (OUT OF ENGINE SCOPE)

| | Count |
|---|---|
| MB double-space after period | **158 instances** |
| OUR double-space after period | **0** |
| OUR single-space after period | **133** |

MB consistently uses two spaces after sentence-ending periods (house style).
Engine produces single-space throughout.

**Verdict: STYLE GAP.** Not engine scope. Requires post-processing pass or
output formatter option. Zero embarrassment risk — MB will recognize this
as a formatting pass, not a content error.

---

### CAT-2: ENGINE MISS — W&T steno-acronym (word-budget silent failure)

| | Count |
|---|---|
| "W&T" instances in MB first 50 pages | **9** |
| Engine correctly annotated (batch 1) | **3** |
| Still "with and T" in OUR (uncorrected) | **6** |

Correct: lines 728, 730, 738 (MB) → engine annotated at lines 748, 754, 768 (OUR).
Missed: lines 1032, 1034, 1040, 1044, 1050, 1052 (MB) → still "with and T"
  at lines 1096, 1098, 1104, 1108, 1114, 1120 (OUR).

**Root cause:** `check_word_budget` WORD_BUDGET_HARD=0.80 blocks all
tight-collapse proposals. W&T ratio = 1/3–2/8 = 0.33–0.50 (well below 0.80).
Confirmed in MB_TIGHT_COLLAPSE_RECON.md: 9 W&T events, all consistent rule,
all below threshold.

**Verdict: ENGINE MISS (fixable).** Root cause diagnosed and fix designed.
After fix ships: word-budget exemption for NAMES_LOCK targets → 6/6 should pass.

---

### CAT-3: ENGINE MISS — em-dash self-corrections (partial; 39 gaps)

| | Count |
|---|---|
| Lines with "--" in MB | **49** |
| Lines with "--" in OUR | **10** |
| Gap (present in MB, absent in OUR) | **~39** |

Engine got: "No -- no," and several other self-corrections.
MB has 49 em-dash lines; engine produced only 10.

Sample MB em-dashes the engine missed:
- `I want to say -- I don't recall.`
- `billings came out -- should have come out versus`
- `And I don't -- you've done this before,`
- `You have --and we'll get into it, but`
- `-- oil barrels being paid to one of the companies`

**Root cause (partial):** Reader likely flagged many of these as anomalies.
Cannot confirm without re-running with fixed validate_ops. Some may be:
- Dropped by word-budget check (if turn had multiple ops including em-dash)
- Missed by Reader entirely (audio-dependent self-corrections)
- MB judgment calls (not deterministic from text alone)

**Verdict: ENGINE MISS (partially fixable, partially MB judgment).** After
validate_ops fix, re-run and re-count. Some em-dashes are MB editorial
(cannot automate) — these will remain FLAG items.

---

### CAT-4: ENGINE MISS — Warren Seal capitalization (overlapping spans)

| | |
|---|---|
| MB | "Warren Seal" (both words capitalized) — 1 instance |
| OUR | "warren seal" (lowercase 's') — 1 instance |

**Root cause:** Reader produced two anomalies on turn 124 with overlapping
token spans (a_0013 [8,15] and a_0014 [8,10]). `check_coverage` silently
dropped the entire turn's ops. Neither correction applied.

**Verdict: ENGINE MISS (fixable).** Fix: `check_coverage` should pick longer
span over shorter (or log the drop), not silently kill the whole turn.
After fix: "Warren Seal" correction should pass.

---

### CAT-5: ENGINE PARTIAL MISS — Crescent Exploration capitalization

| | Count |
|---|---|
| "Crescent" (correct case) in MB | **4 instances** |
| "Crescent" (correct case) in OUR | **2 instances** |
| "crescent" (wrong case) in OUR | **2 instances** |

MB lines 980, 982, 990, 998 — all correct "Crescent" / "Crescent's".
OUR lines 1038, 1040 — correct "Crescent Exploration", "Crescent".
OUR lines 1052, 1060 — lowercase "crescent business", "stay at crescent".

The section IS present in OUR (content not missing). Capitalization wrong
on 2 of 4 instances.

**Root cause:** Writer Rule 8 mis-interpretation. Rule says "Names not in
names_lock — FLAG. Never guess." Writer interprets this as "produce no op"
rather than "produce a FLAG op." Result: no op generated, no annotation,
original (wrong-case) text passes through unchanged.

**Verdict: ENGINE MISS (fixable).** Fix: clarify Rule 8 in Writer prompt —
"produce a FLAG op with to='' and source='house_style'. Do not omit the op."
After fix: FLAGs will appear in OUR for human review (correct behavior).

---

### CAT-6: ENGINE MISS — Senior Vice President capitalization

| | Count |
|---|---|
| "Senior Vice President" (correct) in MB | **3 instances** |
| "Senior vice president" (wrong case) in OUR | **3 instances** |

MB: "Senior Vice President" at lines 1360, 1392, 1394.
OUR: "Senior vice president" at lines 1468, 1504, 1506.
(Line offset difference = ~108 lines = page wrapping shift from earlier corrections.)

**Root cause:** Job-title capitalization is not in NAMES_LOCK, not caught by
check_names (which only checks title-preceded names like "Mr. Smith"). Engine
has no rule for capitalizing official job titles.

**Verdict: SCOPE DECISION.** Not a current-engine defect per se — engine was
never told "Senior Vice President" is a capitalized proper title. After Crescent
FLAG fix ships: job-title flagging becomes a follow-on rule to encode.

---

### CAT-7: ENGINE PARTIAL MISS — "permanent address" phonetic fix

| | |
|---|---|
| MB | "permanent address" × 2 (Q: line 684, A: line 686) |
| OUR | 0 instances of "permanent address" |
| OUR | 1 engine annotation: `{{MB_REVIEW-FIX: 'permit'→'permanent'}}` (line 688) |
| OUR | 1 unfixed: "That is my permission" (line 692) |

Engine caught the steno collision on the Q: line (turn 97) and annotated it.
The A: line (turn 98) — "permission" — was flagged as MEDIUM confidence in
recon but Reader may have produced a lower-confidence anomaly or the word
"permission" wasn't recognized as the same error.

**Verdict: ENGINE PARTIAL (partially fixable).** Turn 97 FIX annotation is
correct. Turn 98 "permission" may need higher-confidence Reader output on
that anomaly, or human review.

---

### CAT-8: ENGINE CORRECT — "flew in to give" (steno merge fix)

| | |
|---|---|
| MB | "flew in to give testimony today" |
| OUR | `{{MB_REVIEW-FIX: confident — Steno merged 'in to' into 'into'...}}in to give testimony` |

Engine correctly identified "flew into give" → "flew in to give" and annotated
with high confidence.

**Verdict: WIN.**

---

### CAT-9: ENGINE CORRECT — "No -- no" (em-dash self-correction)

| | |
|---|---|
| MB | "No -- no, yes, I have one time." |
| OUR | `{{MB_REVIEW-FIX: ...em-dash added per house style...}}No -- no,` |

Engine correctly added em-dash for witness self-correction.

**Verdict: WIN.**

---

### CAT-10: ENGINE CORRECT — "underpaid" compound

| | |
|---|---|
| MB | "being underpaid for the" |
| OUR | `{{MB_REVIEW-VERIFY: ...split compound...}}underpaid` |

Engine produced "underpaid" at VERIFY confidence (correct). MB matches.

**Verdict: WIN (VERIFY level — human confirms, not auto-apply).**

---

### CAT-11: NUMBER FORMAT — "Twenty-five years ago" vs "25 years"

| | |
|---|---|
| MB | "Twenty-five years ago potentially." |
| OUR | `{{MB_REVIEW-FLAG: Medium confidence; state convention may require spelled-out number...}}` |

Engine correctly FLAGged this for human review (can't determine from text
whether MB spell-writes small numbers or leaves digits). MB wrote "Twenty-five".

**Verdict: CORRECT BEHAVIOR (FLAG).** When rule is decided, encode it.

---

## OVERALL CONFIDENCE NUMBERS

| Category | MB instances | Engine correct | Engine wrong | Coverage |
|---|---|---|---|---|
| W&T acronym | 9 | 3 | 6 missed | 33% |
| Em-dash | 49 | 10 | ~39 missed | 20% |
| Warren Seal | 1 | 0 | 1 missed | 0% |
| Crescent case | 4 | 2 | 2 wrong case | 50% |
| SVP title case | 3 | 0 | 3 wrong | 0% |
| Sentence spacing | 158 | 0 | N/A (out of scope) | — |
| flew in to give | 1 | 1 | 0 | 100% |
| No -- no | 1 | 1 | 0 | 100% |
| underpaid | 1 | 1 | 0 | 100% |
| Number FLAG | 1 | 1 (FLAG) | 0 | 100% |

**High-confidence engine wins (out of scope items excluded): ~6 correct of ~20 tracked
content changes = ~30% gross coverage.**

**Post-fix projection (word-budget + check_coverage + Writer Rule 8 fixes):**
- W&T: 3→9 (6 recovered)
- Warren Seal: 0→1 (1 recovered)
- Crescent FLAGs: 2 additional FLAGs generated
- Em-dash: unclear — depends on Reader quality; likely 10→20+ range

**After fixes: projected ~50–60% of tracked content issues handled correctly.**
The remaining ~40% fall into:
- Sentence spacing (out of scope, formatting pass)
- Em-dash (audio-dependent, MB editorial)
- Title capitalization (new rule needed)
- Other MB judgment calls

---

## ZERO-EMBARRASSMENT ASSESSMENT

**Safe to demo with current state?** Conditional yes, with framing:

DO say: "The engine identifies and annotates corrections for reviewer approval.
Currently it catches high-confidence phonetic errors and steno artifacts in
batch 1 (first ~10 pages of testimony). We have diagnosed why batches 2+
miss the W&T acronym — that fix is next."

DON'T say: "Engine handles X% of MB's corrections" without noting the
validate_ops silent-failure issue distorts the number.

---

## RAW DATA ARTIFACTS

- `C:\Users\scott\defect_inventory_v3_raw.txt` — full pattern search output
- `C:\Users\scott\defect_inventory_v2_raw.txt` — difflib alignment output (context)
- Spec `specs/2026-05-02_MB_TIGHT_COLLAPSE_RECON.md` — W&T tight-collapse data
