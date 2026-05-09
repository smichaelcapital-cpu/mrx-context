# HANDOFF — Opus, midday of 2026-05-09
**For:** Fresh Opus (next session today, or tomorrow morning)
**From:** Opus 2026-05-09 morning session (clean wrap, ~11:30 AM)

---

## STOP. Before responding to Scott, answer these:

1. What artifact landed today? **(MB.yaml v0 — first fingerprint instance, on disk)**
2. What's the architecture? **(four-layer: universal / jurisdiction / case_type / reporter — locked)**
3. What's the next concrete deliverable? **(LA state guidelines parsing OR jp_042726 Stage 1 run — pending Scott's pick)**

If you cannot answer all three from this doc, RE-READ.

---

## What landed this morning (10 commits across mrx-context, all pushed except last 3)

### Knowledge captures (PUSHED)
- `knowledge/cat4_package_anatomy.md` — verified format report on every file in a CaseCATalyst package. Magic bytes, readable-without-Cat4 verdicts.
- `knowledge/cat4_export_runbook.md` — step-by-step RTF export from Cat4. Captured live during today's export.
- `knowledge/fingerprint_architecture_decisions.md` — four-layer model, MB-as-first-fitting framing, AD jurisdiction-confound caveat.

### Fingerprint scaffolding (NOT YET PUSHED)
- `fingerprints/_template.yaml` + `fingerprints/ledger.md` (skeleton)
- `fingerprints/jurisdictions/{louisiana,delaware,new_york_wcb}.yaml` (empty headers)
- `fingerprints/case_types/{civil_engineering,workers_comp}.yaml` (empty headers)
- `fingerprints/reporters/MB.yaml` — **v0 with verified data**
- `fingerprints/ledger.md` — 12 classification decisions logged

### Tech debt
- TD-002 logged: stale e2e test expectation `test_E2E3_wt_has_misses` — engine improved past test, fix is to update assertion. Defer.

---

## What was won today (preserve, do not lose)

1. **RTF export from Cat4 is documented.** The biggest recurring friction point now has a runbook.
2. **Cross-depo pattern table found.** The data was saved at `io/analysis/_cross_depo_scan/cross_depo_pattern_table.md` — Sonnet hunted it down. Used to populate MB.yaml translation_artifacts.
3. **AD jurisdiction-confound caught.** AD's near-zero counts cannot be cleanly attributed to "MB unique" — could be Louisiana convention. All ambiguous classifications flagged `mb_specific_OR_louisiana` until LA state guidelines parsed.
4. **Negative fingerprint anchor.** Em-dash double-hyphen verified absent across all 6 scanned depos (3 MB + 3 AD). First entry in `verified_absences`.
5. **jp_042726 metadata extracted.** From .sgxml: 212 pages, 424 folios, save history of 3, CRLA Louisiana code. From recon: which package files are reachable without Cat4 (.sgxml YES, .sgdct NO, .sgglb partial via binary grep).

---

## What's queued (in priority order)

### Immediate (next session)
1. **Decide between two paths:**
   - **Path A:** Hunt + parse LA state guidelines. Resolves 6 ambiguous classifications in MB.yaml. Unlocks `jurisdictions/louisiana.yaml` population.
   - **Path B:** Run Stage 1 pipeline on jp_042726 RTF. Generates first MB Delaware data point. Tests engine on a non-Louisiana case.
   - Scott will pick. Don't pre-commit.

2. **Push the 3 pending mrx-context commits** if not done by Scott already.

### Short-term (this weekend)
3. Raw-vs-final diff analysis to populate `negative_fingerprint.stylistic_prohibitions` (find words/punctuation MB strips during scoping).
4. `_template.yaml` round-trip — every section in MB.yaml needs a generalized counterpart in `_template.yaml`. Not yet done.
5. `jurisdictions/_universal.yaml` creation — migrate `doubled_pure` and `speaker_in_body` (currently classified universal) out of MB.yaml.

### Deferred
6. Stage Gate Acceptance Criteria spec (carried over from yesterday).
7. Reader Upgrade spec (post-ceiling work).
8. TD-002 fix (stale test).
9. 042726 Stage 5 verification (yesterday's known debt: 778 skipped proposals from tokenization_mismatch / span conflict).

---

## Open uncertainties

1. **LA state guidelines location unknown.** Scott has them somewhere ("we used to leverage them"). Hunt mission needed: MASTER_COPIES, OneDrive, anywhere.
2. **AD identity unconfirmed.** AD might be NY-WCB-only, which would mean cross-depo data is jurisdiction-confounded. Architecture caveat documented.
3. **MB still offline until 2026-05-13.** No verification of M1 against MB until then.
4. **Stretch goal status:** original "ship 042726 to MB by Sunday" is in question. Today's work was foundation, not pipeline. Scott has not formally un-set the goal — but architecturally, we're not on the path to ship Sunday. Worth a direct conversation early next session.

---

## Hard rules (carried forward)

- Plain English, 12-year-old reading level.
- One question at a time.
- All Sonnet-bound instructions in code blocks (the copy-button window).
- No fire hose. High level first. Detail on request.
- Sonnet runs shell. Scott runs decisions. Opus writes specs.
- Scott pushes commits (TODAY'S OVERRIDE WAS ONE-SHOT — standing rule resumed).
- Halprin/Brandl FINAL files NEVER push to public repo.
- All knowledge captures land in `mrx-context/knowledge/`. Handoff files land in `mrx-context/`. Never Downloads.

---

## Scott's state at handoff

- Worn morning, recovered. Hyperventilating moment around the Cat4 export, defused with a "park it" call. Then he beat the export under his own steam.
- Said: "Slow is smooth, smooth is fast" — held to it.
- Said: "this is the suit, MB is the first fitting" — that framing now drives the ledger philosophy.
- Said: "I don't wanna lose" the research data — drove the three knowledge captures.
- Multiple sessions expected today. This handoff covers the morning. More handoffs to follow.

---

## First thing fresh Opus should do

1. Read this doc top to bottom.
2. Read companion `HANDOFF_SONNET_2026-05-09_midday.md`.
3. Read `knowledge/fingerprint_architecture_decisions.md` (3-min read, locks in the architecture).
4. Confirm: "Opus ramped. Ready." + one sentence on current state + one question.
5. Most important question: **"Path A (LA state guidelines hunt) or Path B (jp_042726 Stage 1 run)?"**

Do not start work until Scott answers.

---

End of midday handoff.
