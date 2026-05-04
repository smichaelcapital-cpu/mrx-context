# RECON — D-WRITER-FLAG-NOT-REWORD (Finding 2)
**Date:** 2026-05-03 evening session
**Analyst:** Claude Sonnet (mrx-context session)
**Scope:** Ground spec for the proper-noun FLAG rule in Writer prompt.
**DO NOT SPEC. DO NOT CODE. Recon findings only.**

---

## 1. Walk of WRITER_PROMPT_V1 (rule-by-rule)

WRITER_PROMPT_V1 lives at `suggester.py:408–503`. Nine hard rules plus
output format and schema example. All rules quoted verbatim below.

| # | Short summary | Proper nouns? | FLAG/REWORD? | Uncertainty? | Relation to new rule |
|---|--------------|---------------|--------------|--------------|----------------------|
| 1 | Every op must reference an anomaly_id from AnomalyList | — | — | — | NEUTRAL |
| 2 | Only two op types: REWORD and FLAG | — | YES — defines both modes | — | SUPPORTS (FLAG exists) |
| 3 | Every REWORD must include a `source` from closed list (raw_steno, case_dict, kb, names_lock, phonetic_match, house_style) | — | — | — | KEY — `case_dict` is the bug pathway |
| 4 | `to` field must contain ONLY corrected text — reasoning in `reason` | — | — | — | NEUTRAL |
| 5 | VERBATIM RULE (KB-010): if anomaly note suggests witness may have said it, FLAG instead of REWORD. "When in doubt — FLAG." | — | YES | YES | SUPPORTS |
| 6 | If category is "unclear" — always FLAG | — | YES | YES | SUPPORTS |
| 7 | If confidence is "low" — strongly prefer FLAG; use REWORD only when anomaly note + dictionary + state module make correction unambiguous | — | YES | YES | SUPPORTS |
| 8 | Unknown names MUST produce FLAG: "When the Reader flags an anomaly on a name (category=name_uncertain OR context indicates a proper noun), and that name is NOT in NAMES_LOCK — FLAG, after='', reason='unknown name not in NAMES_LOCK — human review required.'" | YES — named directly | YES | YES | SUPPORTS but has trigger gap (see §5) |
| 9 | `to` word count should be close to span input length; REWORD expanding 3→12 words is suspicious | — | — | — | NEUTRAL |

**Critical observation:** Rule 8 already exists. The bug is not its
absence — it's that its trigger condition was bypassed. See §5.

---

## 2. FLAG Mechanism (current state)

**Does a FLAG output mode exist?** YES. Defined at Rule 2 (L429):
> "FLAG: leave the span verbatim, mark for human review"

**What does FLAG produce?**
A JSON op with `op_type="FLAG"`, `to=""`, and a reason. The span text
is left unchanged in the final transcript. The FLAG records appear in
`decisions.jsonl` and `rejections.jsonl` downstream.

**Example FLAG op (from prompt schema, L487–494):**
```json
{
  "anomaly_id": "a_0002",
  "op_type": "FLAG",
  "turn_idx": 18,
  "token_span": [3, 5],
  "from": "[from-omitted]",
  "to": "",
  "source": "raw_steno",
  "reason": "uncertain witness phrasing — needs audio review"
}
```

**What triggers a FLAG today?**
- Rule 5: verbatim rule — witness may have said it that way
- Rule 6: category=`unclear` → always FLAG
- Rule 7: confidence=`low` → strongly prefer FLAG
- Rule 8: name not in NAMES_LOCK → must FLAG
- Implicit: "If you don't have enough information to be confident, your only correct move is FLAG" (L417–419)

**How does "do nothing / hand back to human" work?**
FLAG with `to=""` is the only human-deferral op. There is also a
`REJECT` pseudo-op mentioned once (L465: "Even then, produce
op_type='REJECT' with a reason") for Reader false-positives, but this
is undocumented in the schema example — `REJECT` appears nowhere else
in the prompt or schema.

---

## 3. Signals Available to Writer (schema walk)

**What the Writer receives per anomaly** (`_build_writer_user_message`, L696–727):

```json
{
  "anomaly_id": "a_0012",
  "turn_idx": 2657,
  "token_span": [13, 16],
  "raw_token_count_in_turn": <int>,
  "category": "steno_artifact",
  "reader_note": "...",
  "confidence": "high"
}
```

**Writer's system prompt also includes:**
- `NAMES_LOCK` — sorted JSON list of attorney-verified proper nouns
- Case `DICTIONARY` — RTF-derived steno translations (116 entries for halprin_full)
- `STATE MODULE` — jurisdiction-specific rules

**Field-by-field assessment for detecting "uncertain proper noun":**

| Field | Available? | Useful for detecting uncertain proper noun? | Notes |
|-------|-----------|---------------------------------------------|-------|
| `category` | YES | YES if `name_uncertain`; UNRELIABLE if `steno_artifact` | The trigger gap: Reader can categorize a proper noun reconstruction as `steno_artifact` |
| `confidence` | YES | PARTIAL — low confidence suggests uncertainty, but high confidence blocks Rule 7 | In block 537/540 confidence was "high" — Rule 7 didn't fire |
| `reader_note` | YES | YES — free text often names the proposed correction explicitly | In block 537 note said: "probable reading is 'named Fran Schneider'". Proper noun signal is IN the note. |
| `token_span` | YES | VERY LIMITED — only position, no content | Cannot detect capitalization from coordinates alone |
| `raw_token_count_in_turn` | YES | NO — count only |  |
| NAMES_LOCK | YES (system prompt) | YES — check if proposed name is in it | Neither "Fran" nor "Schneider" is in NAMES_LOCK |
| Case dictionary | YES (system prompt) | MISLEADING — dictionary had wrong name | Dictionary had "Fran Schneider"; correct form is "Fran Snyder" |

**What the Writer does NOT have:**
- Raw token text (read-write separation enforced)
- Capitalization of original span tokens
- Any independent source to verify if the Reader's named correction is right
- A mechanism to distinguish "sentence-initial capital" from "proper noun capital"

**Key deduction:** The Writer's only reliable signal for "this is an uncertain proper noun" is:
(A) category=`name_uncertain`, or
(B) the proposed `to` text it is about to write contains a Title Case word not in NAMES_LOCK.

Signal (A) depends on the Reader categorizing correctly. Signal (B) is
self-generated — the Writer can check its own proposed output before
emitting it.

---

## 4. Contradiction Hunt Results

Pattern searched across WRITER_PROMPT_V1 (L408–503). Line numbers are
absolute (in suggester.py).

| Line | Text (condensed) | Verdict |
|------|-----------------|---------|
| L414–415 | "Your job is to produce one OP per anomaly: either REWORD (propose a corrected text) or FLAG (propose human review)." | NEUTRAL — defines both modes correctly |
| L417–419 | "YOU DO NOT SEE THE RAW TEXT...If you don't have enough information to be confident, your only correct move is FLAG." | SUPPORTS — the principle is right; not applied to name case |
| L432–438 | Source closed list includes `case_dict` and `names_lock` as separate options | CONFLICTS — Writer can use `case_dict` as a source for a REWORD even for proper nouns. Nothing in the source-list definition requires proper-noun-bearing REWORD ops to use `names_lock` source. |
| L446–447 | "When in doubt — FLAG." | SUPPORTS |
| L449 | "If the Reader's category is 'unclear' — always FLAG." | SUPPORTS — but category was `steno_artifact`, not `unclear` |
| L452–454 | "If the Reader's confidence is 'low' — strongly prefer FLAG. Use REWORD only when...correction unambiguous." | NEUTRAL — confidence was "high"; Rule 7 did not fire |
| L456–461 | **Rule 8**: "Unknown names MUST produce a FLAG op: When the Reader flags an anomaly on a name (category=name_uncertain OR context indicates a proper noun), and that name is NOT in NAMES_LOCK, you MUST produce a FLAG op..." | SUPPORTS — exists. **The trigger gap is "context indicates a proper noun" — too vague to reliably fire when category=steno_artifact** |
| L499–500 | "You do NOT know the raw text; do not guess it." | SUPPORTS FIX — by inference, the Writer is "guessing" a proper noun name when it adopts a name from the reader_note that is in neither NAMES_LOCK nor the raw text |
| L434 | `case_dict` in source closed list | NEUTRAL/CONFLICTS — no rule says "if source=case_dict and proper noun → FLAG". This is the missing guard. |

**No direct conflicts found.** The existing rules are consistent with a
new proper-noun FLAG rule. The problem is a **gap**, not a contradiction:
Rule 8 exists but its `steno_artifact` bypass is not closed.

---

## 5. Blocks 537 and 540 — Verbatim Records

### Reader anomaly records (from `anomalies.jsonl`)

**Block 537 — turn_idx=2657:**
```json
{
  "anomaly_id": "a_0012",
  "turn_idx": 2657,
  "token_span": [13, 16],
  "category": "steno_artifact",
  "reader_note": "'named from an Schneider' — 'from an' is likely a steno artifact; probable reading is 'named Fran Schneider' (Fran Schneider appears in dictionary). 'from an' makes no grammatical sense in this slot.",
  "confidence": "high"
}
```

**Block 540 — turn_idx=2659:**
```json
{
  "anomaly_id": "a_0015",
  "turn_idx": 2659,
  "token_span": [16, 19],
  "category": "steno_artifact",
  "reader_note": "'named from an Schneider' — same artifact as turn 2657; 'from an' likely steno error for 'Fran' (Fran Schneider per dictionary)",
  "confidence": "high"
}
```

### Writer proposal records (from `proposals.json`)

**Block 537 — proposal p_0012:**
```json
{
  "proposal_id": "p_0012",
  "turn_idx": 2657,
  "op_type": "REWORD",
  "token_span": [13, 16],
  "before": "named from an Schneider",
  "after": "named Fran Schneider",
  "reason": "High-confidence steno artifact: 'from an' is a steno misread; 'named from an Schneider' → 'named Fran Schneider' per dictionary entry for Fran Schneider",
  "source": "case_dict",
  "specialist_hint": "grammar",
  "anomaly_id": "a_0012",
  "batch_id": "b_0043"
}
```

**Block 540 — proposal p_0015:**
```json
{
  "proposal_id": "p_0015",
  "turn_idx": 2659,
  "op_type": "REWORD",
  "token_span": [16, 19],
  "before": "named from an Schneider",
  "after": "named Fran Schneider",
  "reason": "High-confidence steno artifact: same as turn 2657; 'named from an Schneider' → 'named Fran Schneider' per dictionary entry for Fran Schneider",
  "source": "case_dict",
  "specialist_hint": "grammar",
  "anomaly_id": "a_0015",
  "batch_id": "b_0043"
}
```

### Failure chain reconstruction

```
Dictionary (halprin_mini/dictionary.rtf)
  └── contains "Fran Schneider"   ← DATA ERROR (correct: "Fran Snyder")

Reader
  ├── sees: "named from an Schneider"
  ├── detects: "from an" is a steno split of "Fran" (correct observation)
  ├── looks up dictionary → finds "Fran Schneider"
  ├── embeds in reader_note: "Fran Schneider appears in dictionary"
  └── sets category: "steno_artifact"  ← RULE FAILURE (should be "name_uncertain")
        (Reader's own Rule 8 says: "if token resembles a name in the dictionary
        or appears to be a proper noun missing capitalization, flag name_uncertain")

Writer
  ├── receives: category=steno_artifact, confidence=high, note mentioning "Fran Schneider"
  ├── Rule 8 check: category ≠ name_uncertain
  │   → "context indicates a proper noun"? — note names a person. But Writer
  │     apparently resolved this as a steno-decompaction fix, not a name fix.
  ├── produces: REWORD "named Fran Schneider", source=case_dict
  └── RESULT: wrong name lands in transcript

NAMES_LOCK check: neither "Fran" nor "Schneider" nor "Snyder" is in NAMES_LOCK.
Rule 8 should have fired on "context indicates proper noun" ground but did not.

Word preservation validator rejects proposal (drops "from", "an") — but this
is downstream; the wrong-name REWORD was already proposed.
```

### Three-layer bug

1. **Data layer**: Dictionary has "Fran Schneider" (wrong). Correct name is "Fran Snyder".
2. **Reader layer**: Reader chose `steno_artifact` instead of `name_uncertain` for a proper-noun reconstruction, bypassing Rule 8 entirely.
3. **Writer layer**: Rule 8's "context indicates a proper noun" condition was not applied despite the reader_note explicitly naming a person.

**The dictionary error is the original cause. But even with a correct dictionary, layers 2 and 3 represent structural weaknesses that would let wrong names through on any future deposition.**

---

## 6. Recommended "Uncertain Proper Noun" Definition

### Options evaluated

**Option A — Capitalization-based (Writer checks its own `to` output):**
"If the proposed `to` text contains a word beginning with a capital letter
that is NOT in NAMES_LOCK AND is not the first word of the proposed text,
treat as uncertain proper noun → FLAG."

Status: **Cannot be used as specified.** The Writer doesn't know if a
capitalized word in its `to` is sentence-initial without raw text. A REWORD
correcting the first word of a sentence would always have a capital there.

**Option B — Reader-confidence-based:**
"If confidence < threshold on a span containing a capitalized token → FLAG."

Status: **Rejected.** In blocks 537/540, confidence was "high" — this option
would not have fired. More generally, confidence=high on a wrong name is
exactly the failure mode we need to catch.

**Option C — Phonetic-distance-based:**
"If phonetic distance > N from original token AND token is capitalized → FLAG."

Status: **Rejected.** Writer has no phonetic-distance calculator. This is a
code-side rule, not a prompt rule. Would require a new validator, not a prompt
change.

**Option D — source=case_dict + proper noun in `to` → FLAG:**

**RECOMMENDED.**

The Writer already knows what `source` it is about to use and what `to` it
is about to write. The following rule is fully mechanical given available signals:

> "If your source would be `case_dict` or `phonetic_match`, AND your proposed
> `to` contains what appears to be a personal name or company name (a sequence
> of one or more Title Case words that would sit in a person/company name slot,
> not just sentence-initial capitalization), AND the proposed name or any token
> of it is NOT in NAMES_LOCK — produce FLAG instead of REWORD.
>
> Reason: the case dictionary may contain incorrect proper noun spellings that
> have not been attorney-verified. Only NAMES_LOCK entries are case-verified.
> When in doubt whether a capitalized word is sentence-initial vs. a proper
> noun: if the reader_note names a specific person or company, that is a proper
> noun — check NAMES_LOCK."

**Why this option works:**
- In blocks 537/540: source=case_dict, proposed to="named Fran Schneider",
  "Fran Schneider" not in NAMES_LOCK → would FLAG.
- Does not affect REWORD ops using `source=names_lock` (verified names).
- Does not affect `source=house_style` (formatting, no proper noun risk).
- Does not affect `source=raw_steno` (steno decompaction, no name invention).
- Carves out sentence-initial capitals by requiring the reader_note to name
  a person/company explicitly — if the note says "probable reading is 'named
  Fran Schneider'", that is an explicit name, not sentence-initial capitalization.

**Complementary Reader-side fix (OPTIONAL but high-value):**

Rule 8 (READER_PROMPT_V1, line ~249) says: "if a token resembles a name in
the dictionary or appears to be a proper noun missing capitalization, flag
name_uncertain."

The Reader violated this in blocks 537/540 by choosing `steno_artifact` over
`name_uncertain`. Adding an explicit carve-out to the Reader would be defense
in depth: "When the steno artifact is the mechanism but the correction
produces a proper noun (personal name, company name), use category=
`name_uncertain`, not `steno_artifact`. The steno mechanism explains how the
error happened, but the category must reflect that the CORRECTION is a proper
noun — so the Writer knows to check NAMES_LOCK."

This complementary Reader fix does not replace the Writer fix. Both can coexist.

---

## 7. Open Questions for Opus

### Q1 — FLAG op downstream handling
What happens to FLAG ops after Writer produces them?
- Do they appear in corrected_turns.json (as verbatim text)?
- Are they surfaced to MB as a reviewable list?
- Does the Proof of Work output include FLAG entries?
- Does the apply.py layer do anything special with FLAG vs. ignoring it?

**Why it matters:** If FLAG ops are invisible to MB (just silently skipped),
adding more FLAGs is useless — MB never sees them. If they surface as a
reviewable queue, adding FLAGs is exactly right for uncertain proper nouns.
**This needs to be confirmed before speccing the rule.**

### Q2 — NAMES_LOCK completeness and ownership
"Fran Snyder" was NOT in NAMES_LOCK for the halprin_full run. NAMES_LOCK had
only 15 entries (attorneys, firms, geography). Who is responsible for populating
NAMES_LOCK with deponent names, witnesses, and third parties mentioned?

The correct fix for blocks 537/540 might be: add "Fran Snyder" to NAMES_LOCK
(data fix) + add the Writer rule (structural fix) + fix the dictionary (data fix).

**Why it matters:** If NAMES_LOCK is routinely incomplete, the Writer FLAG rule
will fire constantly on valid names (e.g., every new name mentioned in testimony).
That's probably right behavior — but Opus should confirm the expected FLAG rate.

### Q3 — Two-layer fix: Reader OR Writer OR both?
The Reader violated its own rule (should have used `name_uncertain`). The Writer
did not apply Rule 8 fully. Both fixes are independent and can coexist.

Should this spec produce:
  (a) Writer prompt change only (tighten Rule 8 + Option D rule)?
  (b) Reader prompt change only (force `name_uncertain` on proper-noun corrections)?
  (c) Both?

Option (b) alone is more elegant but requires Reader to correctly classify every
proper noun reconstruction — a high bar. Option (a) alone is defensive but
requires the Writer to detect proper nouns from its own output.
Option (c) (both) provides defense in depth.

### Q4 — False-FLAG rate estimate
If the new rule says "any REWORD using case_dict that introduces a capitalized
word not in NAMES_LOCK → FLAG", how many currently-correct REWORD ops would
be incorrectly flagged?

Quick estimation from the data: the dictionary has 116 entries including proper
nouns like "Marshall Smith", "Jonathan Barrett", "Harman Singh", "Rahul Bhasin",
"Tim Morton", "Tom Easley" — none of which are in NAMES_LOCK. Any correction
referencing these would be FLAG'd under the new rule.

Is that acceptable? These names could be wrong too. FLAG on all of them may
actually be the right behavior — MB should verify any name the engine hasn't
confirmed via NAMES_LOCK.

**Opus should decide whether the false-FLAG rate is acceptable or whether a
per-name whitelist approach is needed.**

### Q5 — `REJECT` op type (undocumented)
Rule 8 mentions `op_type="REJECT"` for Reader false positives (L465), but
this op type does not appear in the schema example (L473–496) and is not in
the closed list of op types defined at Rule 2. Is REJECT a live op type or a
dead branch? The validate_ops code should be checked before any spec that relies on it.
