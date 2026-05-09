# Project Knowledge Inventory
**Purpose:** Reference list for loading into Claude Project Knowledge UI — files fresh Opus or Sonnet should read at session start.
**Generated:** 2026-05-09
**Scope:** Root .md files, knowledge/ .md files, latest handoffs, README/MANIFEST matches.

> **Note on handoffs:** The two most recent handoffs (2026-05-09 midday) live in the **root** of mrx-context/, not in handoffs/. This appears to be a location drift. The handoffs/ subfolder is current only through 2026-05-05. Section 3 reports both.

---

## 1. Root-level .md files (mrx-context/)

| File | Size (KB) | Last Modified | Description |
|---|---|---|---|
| `CODER_MINDSET.md` | 7.2 | 2026-04-26 | Master operating mindset for all Claude sessions — core identity, rules, and working principles. |
| `CODER_MINDSET_ADDENDUM.md` | 13.1 | 2026-04-26 | MyReporterX-specific overrides that stack on CODER_MINDSET; wins over base file on conflicts. |
| `HANDOFF_OPUS_2026-05-09_midday.md` | 6.0 | 2026-05-09 | **Most recent Opus handoff** — morning wins, queued paths (A/B), open uncertainties, hard rules. |
| `HANDOFF_SONNET_2026-05-09_midday.md` | 2.7 | 2026-05-09 | **Most recent Sonnet handoff** — repo state, files created this morning, likely first asks. |
| `HANDOFF_OPUS_2026-05-09_morning.md` | 7.0 | 2026-05-08 | Opus morning handoff (predecessor to midday; superseded but retained). |
| `HANDOFF_SONNET_2026-05-09_morning.md` | 3.2 | 2026-05-08 | Sonnet morning handoff (predecessor to midday; superseded but retained). |
| `HOUSE_OF_STYLE_v01.md` | 2.6 | 2026-04-28 | Locked naming conventions for MyReporterX architecture and product naming. |
| `LEGACY_FORMAT_REFERENCE_v01.md` | 5.1 | 2026-04-27 | Production-tested format_final.py reference — primary source for House of Style v0.2 work. |
| `PREFLIGHT_CHECK_v1.md` | 4.4 | 2026-05-05 | Locked pre-flight checklist required before every full pipeline run. |
| `README.md` | 1.2 | 2026-04-26 | Root repo overview — what mrx-context is and how Claude agents use it. |
| `RULE_SHEET_v1.md` | 1.1 | 2026-05-03 | Decision tree for categorizing any fix: universal vs. MB-specific vs. jurisdiction vs. case-type. |
| `tech_debt.md` | 1.6 | 2026-05-09 | Running tech debt log — current entries TD-001 (writer truncation, fixed) and TD-002 (stale e2e test). |
| `CURRENT.md` | 0.4 | 2026-04-27 | Pointer file to latest handoffs — **STALE** (references 2026-04-26 handoff; not maintained). |
| `OPUS_TO_OPUS_2026-04-29_RESUME.md` | 9.1 | 2026-04-28 | Informal raw Opus-to-Opus session resume note from 2026-04-29 — not structured, low load value. |
| `ARCHITECTURE_DECISIONS.md` | 0.1 | 2026-04-26 | Placeholder stub — Opus to draft; currently empty. |
| `ONBOARDING_REQUIREMENTS.md` | 0.1 | 2026-04-26 | Placeholder stub — Opus to draft; currently empty. |
| `ORACLE_COVENANT.md` | 0.1 | 2026-04-26 | Placeholder stub — Opus to draft; currently empty. |

---

## 2. knowledge/ files (mrx-context/knowledge/)

| File | Size (KB) | Last Modified | Description |
|---|---|---|---|
| `knowledge/fingerprint_architecture_decisions.md` | 4.1 | 2026-05-09 | Locked four-layer fingerprint model (universal / jurisdiction / case_type / reporter) with rationale, AD caveat, and ceiling estimates. |
| `knowledge/cat4_export_runbook.md` | 2.7 | 2026-05-09 | Step-by-step RTF export from CaseCATalyst — captured live during jp_042726 export; avoids repeated pain. |
| `knowledge/cat4_package_anatomy.md` | 1.9 | 2026-05-09 | Format report on every file type in a Cat4 depo package — magic bytes, readability without Cat4, fingerprint value. |

---

## 3. Latest handoffs from mrx-context/handoffs/

> Latest files in the handoffs/ subfolder are from 2026-05-05. The **actual latest** handoffs (2026-05-09) live in the repo root — see Section 1.

| File | Size (KB) | Last Modified | Description |
|---|---|---|---|
| `handoffs/HANDOFF_OPUS_2026-05-05_TUESDAY.md` | 7.1 | 2026-05-04 | Latest Opus handoff archived in handoffs/ — Tuesday session notes and next-day plan (superseded by root midday files). |
| `handoffs/HANDOFF_SONNET_2026-05-05_TUESDAY.md` | 0.5 | 2026-05-04 | Latest Sonnet handoff archived in handoffs/ — Tuesday phone-only-day note (superseded by root midday files). |

---

## 4. README / MANIFEST / STARTUP / NOMENCLATURE matches

| File | Size (KB) | Last Modified | Description |
|---|---|---|---|
| `README.md` | 1.2 | 2026-04-26 | Root repo overview — listed in Section 1 above. |
| `oracle/README.md` | — | — | README inside oracle/ subdirectory — not inventoried (scope: root only per task). |

No MANIFEST, STARTUP, or NOMENCLATURE files found anywhere in mrx-context/.

---

## Recommended load set for Project Knowledge UI

Priority order — load all of these:

1. `CODER_MINDSET.md`
2. `CODER_MINDSET_ADDENDUM.md`
3. `RULE_SHEET_v1.md`
4. `PREFLIGHT_CHECK_v1.md`
5. `HOUSE_OF_STYLE_v01.md`
6. `knowledge/fingerprint_architecture_decisions.md`
7. `knowledge/cat4_package_anatomy.md`
8. `knowledge/cat4_export_runbook.md`
9. `tech_debt.md`
10. `README.md`

**Rotate each session (too volatile for static load):**
- Latest `HANDOFF_OPUS_*` and `HANDOFF_SONNET_*` — paste manually or Scott loads at session start.

**Skip loading (stale / placeholder / low value):**
- `CURRENT.md` (stale pointer)
- `ARCHITECTURE_DECISIONS.md`, `ONBOARDING_REQUIREMENTS.md`, `ORACLE_COVENANT.md` (empty stubs)
- `OPUS_TO_OPUS_2026-04-29_RESUME.md` (informal, superseded)
- `LEGACY_FORMAT_REFERENCE_v01.md` (reference doc — load only when doing House of Style work)
