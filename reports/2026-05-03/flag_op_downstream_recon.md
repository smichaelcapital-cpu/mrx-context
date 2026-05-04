# Q1 Recon — FLAG Op Handling Downstream
**Date:** 2026-05-03 evening session
**Analyst:** Claude Sonnet (mrx-context session)
**Scope:** End-to-end trace of FLAG op: apply layer → Stage 5 → MB review artifact
**Blocking:** D-WRITER-FLAG-NOT-REWORD spec (Finding 2)
**Verdict:** YES_ROBUST (for properly-emitted FLAG ops) — with critical caveat for blocks 537/540

---

## Section 1 — Apply Layer

**File:** `src/mrx_engine_v1/stage3/apply.py` (L284–287)

```python
elif proposal.op_type == "FLAG":
    # Keep span verbatim, insert review marker immediately after span end.
    review = f"[[REVIEW: {proposal.reason}]]"
    tokens = tokens[:e + 1] + [review] + tokens[e + 1:]
```

FLAG op behavior:
- Span text is **not changed** — the original steno tokens stay in place verbatim
- A `[[REVIEW: reason]]` token is inserted immediately after the span's end index
- No word_preservation check is triggered — `word_preservation.check_proposal()` at L136 returns `None` for any op_type != "REWORD"
- No I-9 explosion guard applies (that guard is on REWORD's token replacement)

REWORD contrast: replaces tokens with `proposal.after.split()`; word_preservation checks before/after word counts.

**Finding A1:** FLAG ops are structurally immune to word_preservation rejection. The check is gated on op_type == "REWORD".

---

## Section 2 — Stage 5 / Composer Layer

**Files:** `src/stage5/review_tags.py`, `src/stage5/assemble_final.py`, `src/stage5/proposal_mapper.py`

### review_tags.py
```python
TAG_TYPE_FLAG = "MB_REVIEW-FLAG"
SUBTYPE_FLAG = "flag"

def render_flag_marker(reason: str) -> str:
    return f"{{{{MB_REVIEW-FLAG: {reason}}}}}"

def make_review_queue_entry(...):
    # FLAG → after_text="", tag_type="MB_REVIEW-FLAG"
```

FLAG ops render as `{{MB_REVIEW-FLAG: reason}}` inline in the transcript text. REWORD high-confidence renders as `{{MB_REVIEW-FIX: ...}}`; medium/low as `{{MB_REVIEW-VERIFY: ...}}`.

### proposal_mapper.py
`build_application_map()` filters to `outcome == "apply"` only. Any proposal downgraded to `outcome="word_preservation_rejected"` is **excluded** from the application map and does not appear in review_queue.

### assemble_final.py
Writes three output artifacts:
- `{name}.OUR_FINAL.txt` — transcript with inline `{{MB_REVIEW-*}}` markers
- `{name}.review_queue.json` — structured list of all review items
- `stage5.summary.json` — counts, including `proposals_applied_FLAG` separately

FLAG ops that clear word_preservation (i.e., all of them, since they bypass it entirely) reach `outcome="apply"` and are written to all three artifacts.

**Finding A2:** Properly-emitted FLAG ops produce a visible inline marker in OUR_FINAL.txt AND a structured entry in review_queue.json. They are not silently dropped.

---

## Section 3 — Proof of Work

**File:** `io/analysis/halprin_full/_stage5_out/halprin_full.review_queue.json`
- 762 review_items total in actual halprin_full run
- Confirmed: MB_REVIEW-FLAG entries present in the file (e.g., turn 2659 — self-correction unclear FLAG)
- Confirmed: `proposals_applied_FLAG` counter is non-zero in stage5.summary.json

**Finding A3:** The review_queue.json is the MB-facing review artifact. In the actual halprin_full run, FLAG ops do surface there. The mechanism is live, not theoretical.

---

## Section 4 — Blocks 537/540 Trace

### What happened

**Anomaly records** (anomalies.jsonl):
```json
{"anomaly_id": "a_0012", "turn_idx": 2657, "category": "steno_artifact",
 "reader_note": "'named from an Schneider' — 'from an' is likely a steno artifact; probable reading is 'named Fran Schneider'",
 "confidence": "high"}
{"anomaly_id": "a_0015", "turn_idx": 2659, "category": "steno_artifact",
 "reader_note": "same artifact as turn 2657; 'from an' likely steno error for 'Fran' (Fran Schneider per dictionary)",
 "confidence": "high"}
```

Note: Reader used `category="steno_artifact"`, not `name_uncertain`. This matters for Writer Rule 8 (name_uncertain triggers FLAG); steno_artifact does not.

**Writer proposals** (proposals.json):
```json
{"proposal_id": "p_0012", "turn_idx": 2657, "op_type": "REWORD",
 "before": "named from an Schneider", "after": "named Fran Schneider",
 "source": "case_dict"}
{"proposal_id": "p_0015", "turn_idx": 2659, "op_type": "REWORD",
 "before": "named from an Schneider", "after": "named Fran Schneider",
 "source": "case_dict"}
```

Writer emitted REWORD, not FLAG. Source is `case_dict` — Writer found "Fran Schneider" in the case dictionary and used it as the target. Writer Rule 8 requires category=name_uncertain OR "context indicates a proper noun" to trigger FLAG; Writer did not apply that logic here.

**word_preservation rejection** (_word_preservation_rejections.jsonl):
- turn=2657: span="named from an Schneider", proposed="named Fran Schneider", dropped=['from', 'an'] — REJECTED
- turn=2659: same pattern — REJECTED

**Stage 5 result:**
- Proposals p_0012 / p_0015 downgraded to `outcome="word_preservation_rejected"`
- `build_application_map()` excludes them
- MB sees turn 2657 text: "...someone named from an Schneider in December of 2022, right?" — uncorrected steno, NO review marker of any kind

**Additional error:** The dictionary itself contains "Fran Schneider" (wrong). The correct name per MB transcript is "Fran Snyder". Neither "Snyder" nor "Fran Snyder" appears in the dictionary. So even if the REWORD had been applied, MB would have received the wrong name.

### What FLAG would have done

If Writer had emitted `op_type="FLAG"` on these turns:
1. `word_preservation.check_proposal()` would return `None` (L136: non-REWORD exits immediately)
2. No rejection would occur
3. apply.py would insert `[[REVIEW: unknown name — human review required]]` after the span
4. Stage 5 would render `{{MB_REVIEW-FLAG: unknown name — human review required}}` inline
5. review_queue.json would contain a MB_REVIEW-FLAG entry for turns 2657 and 2659
6. MB would see the garbled steno AND a clear signal to review it

The current path: silent failure. The FLAG path: visible, actionable signal.

---

## Section 5 — Verdict

**For properly-emitted FLAG ops: YES_ROBUST**

When Writer correctly emits `op_type="FLAG"`:
- FLAG bypasses word_preservation entirely (architectural guarantee, not coincidence)
- FLAG renders as `{{MB_REVIEW-FLAG: reason}}` inline in OUR_FINAL.txt
- FLAG produces a structured MB_REVIEW-FLAG entry in review_queue.json
- The mechanism is confirmed live in the halprin_full run (762 items, FLAG entries present)

**For blocks 537/540 specifically: the FLAG path was never taken**

The failure chain:
1. Reader used `steno_artifact` instead of `name_uncertain` → bypassed Writer Rule 8 trigger
2. Writer found "Fran Schneider" in case_dict → emitted REWORD (wrong target, wrong op_type)
3. word_preservation rejected REWORD (dropped 'from', 'an')
4. Rejected REWORD is silenced — MB sees raw steno, zero review signal

This is not a FLAG infrastructure failure. FLAG works. The failure is upstream: Writer emitted the wrong op_type.

---

## Section 6 — Implications for Finding 2 Spec

The Q1 answer confirms that D-WRITER-FLAG-NOT-REWORD is worth speccing. Key points:

1. **FLAG ops reach MB robustly.** The downstream plumbing is solid. A FLAG emitted by Writer will appear in both the inline transcript and the review_queue. No new infrastructure needed.

2. **word_preservation is the gatekeeper Writer must route around.** Any REWORD on a multi-word steno garble that includes context words will be rejected and silenced. FLAG bypasses this entirely. For uncertain proper nouns, FLAG is not just correct — it's the only path that guarantees MB visibility.

3. **Three-layer failure root cause (from writer_flag_not_reword_recon.md):**
   - Layer 1 (Dictionary): "Fran Schneider" in dictionary is wrong
   - Layer 2 (Reader): Used steno_artifact instead of name_uncertain, so Rule 8 trigger was inactive
   - Layer 3 (Writer): Rule 8's "context indicates a proper noun" fallback not applied when reader_note names a person

4. **Recommended fix (Option D from Finding 2 recon):** When source=case_dict AND proposed-to contains a proper noun NOT in NAMES_LOCK → emit FLAG instead of REWORD. This fixes Layer 3 without touching the dictionary or Reader prompt.

5. **Scope of FLAG spec:** The spec need only address Writer behavior. No changes to apply.py, Stage 5, or review_tags.py are needed — FLAG handling there is complete and correct.

---

## Open Questions (carry to Monday spec)

1. Should the spec also address Layer 2 (Reader using steno_artifact when name_uncertain is the semantically correct category)? Or is the Writer-side safety net sufficient without fixing the Reader?

2. Rule 8's trigger condition ("context indicates a proper noun") — what signals should Writer use to evaluate this? Proposed signals: reader_note contains a capitalized multi-word phrase, or the token_span straddles what looks like FirstName LastName structure.

3. Should FLAG on uncertain proper nouns include the candidate name in the reason field (e.g., "possible proper noun: Fran Schneider — verify spelling")? That would let MB resolve the garble without audio in cases where the dictionary name is at least phonetically plausible.
