# MB Style Profile — Tight Collapse Frequency Recon #1

**Date:** 2026-05-02
**Author:** Sonnet (builder)
**Status:** RECON ONLY — no rule decisions made, no engine code touched
**Oracle Covenant:** Input files read-only. No fixtures derived. No runtime imports.

---

## 1. METHOD

### Files Scanned

| File | Path | Status |
|---|---|---|
| Halprin MB FINAL | `oracle/finals/halprin/040226yellowrock-FINAL.txt` | 300 pages, properly formatted transcript, 16,200 lines |
| Brandl MB FINAL | `oracle/finals/brandl/BRANDL_MB_FINAL.txt` | See note below |
| Third depo | — | None exists in oracle/finals/ |

**Critical finding about Brandl file:** `BRANDL_MB_FINAL.txt` is not a properly formatted final transcript. The last line of the file contains: `C:\Cat4\usr\Mary Beth\032626YELLOWROCK-ROUGH.opus` — confirming this is a raw CAT software export from MB Muir's workstation, not a finished final. The format shows raw steno output and MB's corrections concatenated inline without separators (e.g., `Sam danSamedan`, `Aspect energyAspect Energy`, `peacockTrey Peacock`). Page-count analysis is unreliable for this file; estimated ~79 pages of equivalent content based on line density vs Halprin.

**Raw steno available:** The halprin_mini pipeline has Stage 1 turn data (`halprin_mini.stage1.turns.json`) covering turns 76–636 (~pages 13–54, 41 pages of raw steno window). No rough RTF was found at the spec'd path (`040226yellowrock-ROUGH_Tsmd.rtf`) — it does not exist in the engine repo. The `halprin_mini.rtf` in the analysis dir is the formatted mini input, not the rough.

### Sampling Approach

- **Halprin:** Exhaustive search across all 300 pages for acronym/compound patterns via regex. For raw→final confirmation, cross-referenced the 41-page Stage 1 window with MB FINAL lines.
- **Brandl:** Mined camelCase concatenation pairs (`lowercaseCAPDATA` boundaries) to extract visible steno→correction transitions directly. This is a feature of the raw CAT format, not a limitation.
- **Limitation:** For 259 of 300 Halprin pages (beyond the mini window), raw steno is not available — cannot confirm whether acronyms like E&P, g&g, CFO were "letters as words" in steno or were already in the steno dictionary as pre-defined briefs.

---

## 2. PER-DEPO RESULTS

### Halprin — 300 pages, Yellow Rock v. Westlake, deposed April 2, 2026

#### Category A — Proper-Noun Acronyms (letters-as-words steno → collapsed form)

| Form in FINAL | Count | Confirmed from raw? | Steno form | Src tokens | Tgt tokens | Ratio |
|---|---|---|---|---|---|---|
| W&T | 9 | YES | "with and T" | 3 | 1 | 0.33 |
| W&T Offshore | 2 | YES | "with and T offshore" | 4 | 2 | 0.50 |
| E&P | 6 | probable | "E and P" (not in raw window) | 3 | 1 | 0.33 |
| g&g | 14 | probable | "g and g" (not in raw window) | 3 | 1 | 0.33 |
| DD&A | 3 | probable | "D D and A" (not in raw window) | — | 1 | — |
| M&M | 1 | YES | "M and M" | 3 | 1 | 0.33 |
| D&O | 1 | probable | "D and O" | 3 | 1 | 0.33 |
| O&G | 1 | probable | "O and G" | 3 | 1 | 0.33 |
| P&E | 1 | probable | "P and E" | 3 | 1 | 0.33 |
| **Subtotal &-acronyms** | **38** | | | | | |
| CFO | 11 | unconfirmed | may be steno brief already | — | 1 | — |
| CPA | 5 | unconfirmed | may be steno brief already | — | 1 | — |
| CEO | 3 | unconfirmed | may be steno brief already | — | 1 | — |
| AFE | 4 | unconfirmed | may be steno brief already | — | 1 | — |

**Confirmed &-acronyms (raw verified):** 12 events (W&T × 9, W&T Offshore × 2, M&M × 1)
**Total probable Cat A tight collapses:** 38 events = **12.7 per 100 pages**
**Including role titles (CFO, CPA, CEO, AFE):** 59 events = **19.7 per 100 pages**

Representative examples (all confirmed from raw):
- `"with and T offshore"` (4 tokens) → `"W&T Offshore"` (2 words) — turn 110 and 201
- `"with and T"` (3 tokens) → `"W&T"` (1 word) — turns 111, 113, 202, 204, 206, 208, 210
- `"M and M"` (3 tokens) → `"M&M"` (1 word) — turn 449
- `"E and P"` (3 tokens, probable) → `"E&P"` — appears 6x in testimony: _"E&P, exploration and production"_

**Consistency check:** W&T appears in two distinct sections of testimony (turns 110–113, early depo, and turns 201–210, later Q&A). MB applied the same collapse both times. The pattern held across both the "long turn" context (full sentence about W&T Offshore) and the "short turn" context (punchy Q&A: "With and T offshore." → "W&T Offshore.").

#### Category B — Named-Entity Compounds (multi-word raw → proper noun in FINAL)

**True compressions (token count decreases):**

| Form in FINAL | Count | Steno form | Src tokens | Tgt tokens | Ratio |
|---|---|---|---|---|---|
| Lemonwood Terrace | 2 | "lemon wood terrace" | 3 | 2 | 0.67 |

**Capitalization-only (token count unchanged):**

| Form in FINAL | Count | Steno form | Ratio |
|---|---|---|---|
| Warren Seal | 1 | "Warren seal" | 1.00 |
| Yellow Rock | 191 | "yellow rock" (lower) | 1.00 |
| White Top | 153 | "white top" (lower) | 1.00 |
| Sulphur Mines | ~15 | "sulphur mines" (lower) | 1.00 |

**True Cat B compressions:** 2 events = **0.7 per 100 pages**
**Cap-only corrections (not tight collapse):** hundreds — not counted as collapses

Representative example:
- `"lemon wood terrace"` (3 tokens) → `"Lemonwood Terrace"` (2 words), ratio 0.67 — confirmed at turn 96

**Notable non-collapse:** "salt dome" (raw: "salt domes" at turns 263–264) — MB kept as 2 words in FINAL. `saltdome` (1 word) appears 0 times. MB does NOT systematically collapse compound geography terms.

#### Category C — Common-Noun Compressions (generic split compounds → single word)

| Form in FINAL | Count | Confirmed from raw? | Steno form | Src tokens | Tgt tokens | Ratio |
|---|---|---|---|---|---|---|
| underpaid | 1 | YES | "under paid" | 2 | 1 | 0.50 |
| landmen | 1 | YES | "land men" | 2 | 1 | 0.50 |
| landman | 1 | unconfirmed | probably "land man" | 2 | 1 | 0.50 |
| wellbore | 1 | unconfirmed | probably "well bore" | 2 | 1 | 0.50 |
| workover | 3 | unconfirmed | probably "work over" | 2 | 1 | 0.50 |
| overriding | 1 | unconfirmed | overriding royalty, probably fine | — | — | — |
| downhole | 1 | unconfirmed | probably "down hole" | 2 | 1 | 0.50 |

**Total Cat C:** 9 events = **3.0 per 100 pages**

Representative examples:
- `"under paid"` (2 tokens) → `"underpaid"` (1 word) — turn 114
- `"land men"` (2 tokens) → `"landmen"` (1 word) — turn 297

#### Category D — Em-dash Self-Corrections (witness restarts, phonetic fixes)

These are not compressions — they expand or maintain token count.

| Form in FINAL | Raw form | Src tokens | Tgt tokens | Ratio |
|---|---|---|---|---|
| No -- no | "No no" | 2 | 3 | 1.50 |
| whether -- whether | "whether whether" | 2 | 3 | 1.50 |
| to -- to | "to to to" | 3 | 3 | 1.00 |
| permanent | "permit" | 1 | 1 | 1.00 |
| flew in to give | "flew into give" | 3 | 4 | 1.33 |

**Total Cat D in 41-page raw window:** 5 events = ~**12.2 per 100 pages** (raw window only, not extrapolated)

---

### Brandl — ~79 page equivalent, Yellow Rock v. Westlake, deposed March 26, 2026

**NOTE:** File is a raw CAT export, not a formatted final. Page count unreliable. Rates below are rough estimates only.

#### Category A — Acronyms

| Form in FINAL | Count |
|---|---|
| A&M | 3 |

No "letters as words" steno pattern detected for Brandl. The Brandl depo does not heavily feature acronym-named companies. A&M (Texas A&M) appears to be used directly, not as a steno expansion.

**Total Cat A:** 3 events. **Rate unreliable due to format.**

#### Category B — Named-Entity Compressions

These are directly visible as camelCase steno→correction pairs:

| Steno form (raw) | Final form | Count | Src tokens | Tgt tokens | Ratio | Notes |
|---|---|---|---|---|---|---|
| "Sam dan" | Samedan | 45 | 2 | 1 | 0.50 | Oil company, 45 occurrences = dominant pattern |
| "Jude off" | Juliff | 1 | 2 | 1 | 0.50 | Salt water well name |
| "nobile energy" | Noble Energy | 1 | 2 | 2 | 1.00 | Phonetic correction |
| "Aspect energy" | Aspect Energy | 24 | 2 | 2 | 1.00 | Cap-only |
| "Noble energy" | Noble Energy | 7 | 2 | 2 | 1.00 | Cap-only |
| "peacock" | Trey Peacock | 1 | 1 | 2 | 2.00 | Expansion (name recovery) |
| "mad dan" | Mr. Madigan | 1 | 2 | 2 | 1.00 | Phonetic+title fix |
| "client, Texas" | Klein, Texas | 1 | 2 | 2 | 1.00 | Phonetic fix |

**True compressions (ratio < 1.0):** Sam dan→Samedan (45) + Jude off→Juliff (1) = **46 events**
**Estimated rate:** 46/79 = ~**58 per 100 pages** — but this is dominated entirely by one entity (Samedan) that appears throughout the depo. Not a general rate; it reflects how often the witness worked at that specific company.

Representative examples:
- `"Sam dan"` (2 tokens) → `"Samedan"` (1 word), ratio 0.50 — visible 45 times; confirmed from camelCase pattern `Sam danSamedan`
- `"Jude off"` (2 tokens) → `"Juliff"` (1 word), ratio 0.50 — `Jude offJuliff Salt Water Disposal Well`

#### Category C — Common-Noun Compressions

| Split form visible in file | Final form | Instances visible | Notes |
|---|---|---|---|
| "work over" | workover | 1 split + 16 in final | final form dominant |
| "well bore" | wellbore | 1 split + 35 in final | final form dominant |
| "time sheet" | timesheet | 3 splits | |
| "salt water" | Salt Water | 7 instances (kept 2 words) | MB did NOT collapse |

**Notable non-collapse:** "salt water" appears 7 times as two words in Brandl. MB consistently keeps it as two words, same as Halprin. This is a deliberate style choice — `saltwater` is not MB's form.

**Total Cat C:** 4 distinct event types, ~5 split instances visible. **Rate unreliable.**

---

## 3. CROSS-DEPO PATTERN

| Category | Halprin (300 pp) | Brandl (~79 pp est.) | Consistent? |
|---|---|---|---|
| A — &-acronyms | 38 events = 12.7/100 pp | 3 (A&M only) | NO — rate is corpus-dependent |
| B — true compressions | 2 = 0.7/100 pp | 46 (Samedan-dominated) = ~58/100 pp est. | NO — entity-dependent |
| C — common compounds | 9 = 3.0/100 pp | ~5 visible = ~6/100 pp est. | ROUGHLY YES |
| D — em-dash/phonetic | ~12/100 pp (raw window) | visible throughout | YES (qualitative) |

**Cross-depo headline:** Category A and B rates are NOT consistent across depos — they are **entity-dependent**. A depo about W&T Offshore will have many W&T collapses; one about Samedan will have many Samedan collapses. The underlying **rule** is consistent (when steno writes letters-as-words, MB collapses to acronym), but the **frequency** varies with how often the entity is mentioned.

Category C (common compounds) is the most consistent cross-depo rate (~3–6/100 pages), because these compound words appear throughout any oil-field depo.

The **category mix** is NOT consistent: Halprin is Cat A-dominant; Brandl is Cat B-dominant. This reflects which type of entity appears most in the testimony, not a difference in MB's style.

---

## 4. RAW SHAPE ANALYSIS

Based on confirmed events with visible raw steno (41-page Halprin window + Brandl CAT pairs):

### Source token count distribution

| Src tokens | Events | Examples |
|---|---|---|
| 1 | 1 | "peacock" → Trey Peacock (expansion, not collapse) |
| 2 | 13 | "Sam dan"→Samedan, "under paid"→underpaid, "land men"→landmen, "No no"→No--no, "lemon wood"→Lemon(wood), etc. |
| 3 | 10 | "with and T"→W&T, "E and P"→E&P, "M and M"→M&M, "I no one"→I know one, "flew into give"→flew in to give |
| 4 | 2 | "with and T offshore"→W&T Offshore, "to to to"→to--to |

**Most common source size: 2–3 tokens.** All confirmed tight collapses come from 2–4 token spans.

### Ratio distribution (target tokens / source tokens)

| Ratio bucket | Events | Pattern type |
|---|---|---|
| 0.25 | 1 | 4→1 (with and T offshore → W&T — only if counting "W&T" as 1) |
| 0.33 | 7 | 3→1 (with and T → W&T, M and M → M&M, etc.) |
| 0.50 | 14 | 2→1 (Sam dan → Samedan, under paid → underpaid, 4→2 W&T Offshore) |
| 0.67 | 1 | 3→2 (lemon wood terrace → Lemonwood Terrace) |
| 1.00 | 6 | 1→1 or 2→2 (phonetic, capitalization) |
| 1.33–1.50 | 3 | expansion (em-dash insertions) |

**Most common ratio bucket: 0.50.** Confirmed tight collapses cluster at 0.33–0.50.

**Critical implication:** Every confirmed tight collapse has a ratio ≤ 0.67. The engine's current `WORD_BUDGET_HARD = 0.80` would reject ALL of them if the span covers a large fraction of a short turn. This is mathematically confirmed: turn 201 ("With and T offshore." = 4 tokens total, span [0,3], REWORD to "W&T Offshore" = 2 words → ratio 2/4 = 0.50, below 0.80).

---

## 5. NAMES_LOCK CORRELATION

| Category | Targets | NAMES_LOCK candidates? | Notes |
|---|---|---|---|
| A — case-specific acronyms | W&T, W&T Offshore, M&M | YES — 100% | Company names appearing in case caption or depo context |
| A — domain abbreviations | E&P, g&g, DD&A, CFO, CEO, CPA, AFE | NO / MAYBE | Industry standard terms; belong in `kb` or `case_dict`, not NAMES_LOCK |
| B — case specific | Lemonwood Terrace, Warren Seal, Samedan, Juliff | YES — 100% | All are case-specific proper nouns |
| C — common compounds | underpaid, landmen, wellbore, workover | NO | Generic oil-field terms; belong in general dictionary or `kb` |

**For the subset of tight collapses that ARE NAMES_LOCK candidates (Cat A company acronyms + Cat B proper nouns):**
- Halprin: ~14 events (W&T × 11, M&M × 1, Lemonwood Terrace × 2) = 4.7/100 pages
- Brandl: ~47 events (Samedan × 45, Juliff × 1, A&M × 1) = ~59/100 pages (entity-dependent)

The pattern: **every confirmed company-acronym collapse target would go in NAMES_LOCK.** No exception found. The distinction between "belongs in NAMES_LOCK" vs "belongs in case_dict" maps cleanly onto "case-specific entity" vs "industry-standard abbreviation."

---

## 6. CANDIDATE RULE SHAPES

### Option 1: Consistent MB rule — encode as REWORD with NAMES_LOCK anchor

**Statement:** When steno writes a known company acronym as letters-and-connectors ("with and T", "E and P"), MB always collapses to the acronym. This is a deterministic style rule, not a judgment call. The evidence is: 11 W&T collapses in Halprin, zero instances of MB leaving "with and T" intact in the final; 45 Samedan collapses in Brandl with zero instances left as "Sam dan."

**Encode as:** REWORD with `source=names_lock` when the acronym is in NAMES_LOCK, and `source=case_dict` when it's a domain term. The Reader flags the steno artifact; the Writer produces the REWORD. No FLAG needed when the target is unambiguous.

**Evidence needed to pick this option:** Confirmation that the ratio threshold in `check_word_budget` is adjusted or made turn-length-aware (because all confirmed collapses produce ratios of 0.33–0.50, below the current 0.80 hard floor). Without that fix, this option cannot function even if the model behavior is correct.

---

### Option 2: Consistent rule with NAMES_LOCK-gated confidence

**Statement:** MB's collapse rule is real and consistent, but the engine should only auto-REWORD when the target acronym is in NAMES_LOCK. For cases where the Reader flags a letters-as-words steno pattern but the target acronym is NOT in NAMES_LOCK, produce FLAG instead of REWORD. This prevents the engine from guessing acronym expansions it hasn't been told about.

**Encode as:** Writer REWORD when `source=names_lock` is resolvable; Writer FLAG when the Reader's note says "probably an acronym" but the target isn't in the locked list. This is the current behavior for W&T (REWORD when NAMES_LOCK has "W&T Offshore") vs "crescent" company (silent — should be FLAG).

**Evidence needed to pick this option:** Same word_budget threshold fix. Also requires that the Reader's anomaly note reliably identifies the steno-artifact pattern and the NAMES_LOCK entry provides the canonical form.

---

### Option 3: Too noisy to auto-correct — FLAG only

**Statement:** The confirmed collapse events are real, but they require case-specific knowledge to execute safely (the engine must know "W&T" not "W and T" not "WT"). Auto-correction risks introducing errors that are harder to detect than the original steno artifact. Recommend FLAG-only for all category A and B tight collapses; let the human accept with the correct form.

**Evidence needed to pick this option:** Any instance where MB's collap correction was wrong (e.g., she wrote "W&T" but the steno actually meant a different acronym). No such counterexample was found in this recon. This option is the most conservative and most defensible if the word_budget issue is not addressed — a FLAG at least surfaces the anomaly, whereas a failed REWORD with validation rejection produces nothing.

---

## 7. WHAT YOU CANNOT TELL FROM THIS DATA

1. **E&P, g&g, DD&A steno form unknown.** These appear 23 times in Halprin FINAL but our raw window (turns 76–636) never captured a turn where the witness discussed "E and P" — those turns are in the pages 55–300 portion outside the mini. We cannot confirm whether the steno wrote "E and P" or whether MB's steno dictionary already defines a brief that translates directly to "E&P." If the latter, there is no tight collapse event — it's already correct steno output.

2. **Brandl is not a formatted final.** The file is MB's raw CAT export. The "Sam danSamedan" pattern tells us what MB's global dictionary did in real time, but we cannot confirm this is how MB's final transcript would read after formatting, editing, and submission. The camelCase pairs suggest these corrections were applied, but a formatted final might present them differently.

3. **Category C confidence is low for unchecked turns.** "wellbore," "workover," "downhole" appear in the FINAL but we could not confirm the raw steno form for most. It's possible steno had these as single-word briefs already and MB didn't need to collapse anything.

4. **No negative examples for Cat A.** We do not have a case where steno wrote "with and T" and MB left it as "with and T" in the final. The sample size (11 confirmed W&T events) is large enough to call it a rule, but without a counterexample it's possible the rule applies only when the acronym is in the NAMES_LOCK and MB consciously chose to REWORD.

5. **Page-rate normalization is approximate for Cat D.** The em-dash / self-correction count is drawn only from the 41-page raw window. The rate of ~12/100 pages may not hold across the full depo.

6. **Only two depos, one case.** Both Halprin and Brandl are from the same Yellow Rock v. Westlake litigation, scoped by the same reporter (MB Muir). Cross-depo patterns reflect one reporter's style on one case, not MB's general style across all cases.

---

*Recon produced: 2026-05-02. No engine code touched. No fixtures created. Oracle files read-only.*
