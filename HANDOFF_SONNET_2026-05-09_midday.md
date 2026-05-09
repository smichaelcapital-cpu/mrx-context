# HANDOFF — Sonnet, midday of 2026-05-09
**For:** Fresh Sonnet (next session today, or tomorrow)
**From:** Sonnet 2026-05-09 morning, via Opus

---

## State at end of morning

### Repos
- `mrx_engine_v1`: clean. Last commit `d2ebe1e` (TD-001 writer max_tokens fix). Pushed.
- `mrx-context`: **3 commits ahead of origin**. Held for Scott to push.
  - `9e7c9b7` scaffold: fingerprints layered file structure
  - `ae61dc3` feat: MB.yaml v0 — verified data + honest gaps
  - `8c0e201` feat: ledger.md v0 — capture MB classification decisions

### Files created today (verify they exist)
- `mrx-context/knowledge/cat4_package_anatomy.md`
- `mrx-context/knowledge/cat4_export_runbook.md`
- `mrx-context/knowledge/fingerprint_architecture_decisions.md`
- `mrx-context/data/.gitkeep`
- `mrx-context/fingerprints/_template.yaml`
- `mrx-context/fingerprints/ledger.md`
- `mrx-context/fingerprints/jurisdictions/{louisiana,delaware,new_york_wcb}.yaml`
- `mrx-context/fingerprints/case_types/{civil_engineering,workers_comp}.yaml`
- `mrx-context/fingerprints/reporters/MB.yaml`

### Push discipline
- One-shot push override was used today (Sonnet pushed 4 docs commits earlier).
- Standing rule has resumed: **Sonnet does not push** without explicit per-instance Scott override.
- 3 commits queued for Scott to push.

### Knowledge artifacts now exist (use them)
- Anyone confused about the CaseCATalyst package contents → read `knowledge/cat4_package_anatomy.md`
- Anyone confused about how to export the RTF → read `knowledge/cat4_export_runbook.md`
- Anyone confused about the fingerprint architecture → read `knowledge/fingerprint_architecture_decisions.md`

---

## Likely first asks next session

1. **Path A: LA state guidelines hunt.** Search MASTER_COPIES, OneDrive root, Documents for any LA state court reporting style guides or rules. Likely keywords: louisiana, LA_state, civil_procedure, court_rules, style_guide.
2. **Path B: jp_042726 Stage 1 run.** RTF is at `mrx_depo_library/MB/jp_042726/042726jp-ROUGH.rtf`. Run the Stage 1 pipeline (turn extractor + transforms). Output to standard pipeline location. Will populate `corpus.rough_only_depos[jp_042726].raw_turns` in MB.yaml.
3. **Possibly: `_template.yaml` round-trip.** Mirror every section from MB.yaml into `_template.yaml` with generalized field names + comments. Opus drafts the content, Sonnet stages.

---

## Hard rules

- No pushing — Scott pushes (one-shot override expired).
- Halprin/Brandl FINAL files never on public repo.
- Plain English when reporting to Scott. No fire hose.
- Always full absolute paths.
- Handoff files live in `mrx-context/`, NEVER in Downloads.
- Knowledge captures live in `mrx-context/knowledge/`.
- Analysis output lives in `mrx-context/data/`.

---

End of Sonnet midday handoff.
