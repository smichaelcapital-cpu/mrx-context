# WHERE DOES THIS FIX GO? — Rule Sheet v1
Date: 2026-05-03

Before any fix, answer two questions:

Q1: Will this rule apply to EVERY court reporter, forever?
   YES → Universal
   NO  → MB-specific
   UNSURE → Treat as MB-specific (default to caution)

Q2: Is the rule deterministic, or does it require judgment?
   Deterministic → CODE
   Judgment → AI PROMPT

| | Universal | MB-specific |
|---|---|---|
| Code | src/transforms/, src/validate_ops/ | src/profiles/mb/ |
| Prompt | prompts/core/ | prompts/profiles/mb/ |

LABELING REQUIRED on every commit:
- Universal commits: prefix "universal:"
- MB-specific commits: prefix "mb-specific:"
- MB-specific code: filename contains "mb_" OR lives in profiles/mb/
- MB-specific prompt blocks: wrap in
    # ═══ MB TAILORING — NOT UNIVERSAL ═══
    [rules]
    # ═══ END MB TAILORING ═══

EVERY SPEC MUST INCLUDE THIS HEADER:
- Universal? YES / NO
- Code or prompt? CODE / PROMPT
- File location: <exact path>
- Commit prefix: universal: / mb-specific:

When in doubt: default to MB-specific. Easier to promote later than to demote.

---

## RULE-19 — DUAL-LANE SONNET OPERATION

Added 2026-05-16. Supersedes the provisional single-Sonnet-per-clone rule from 2026-05-15 incident capture.

### Physical separation (the core rule)
- Lane A clone: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1_laneA\`
- Lane B clone: `C:\Users\scott\OneDrive\Documents\mrx_engine_v1_laneB\`
- Sonnet #1 only ever operates in laneA. Sonnet #2 only ever operates in laneB. No exceptions.

### Branch naming
- Lane A branches: `laneA/<ticket>-<short-desc>` (e.g. `laneA/B1.7.5-black-bp-cover`)
- Lane B branches: `laneB/<ticket>-<short-desc>` (e.g. `laneB/B1.7.6-olsen-reporter-anchor`)
- Branch prefix MUST match the folder name. If they don't match, STOP and flag Scott.

### Pre-flight check (every Sonnet runs before any commit)
pwd
git branch --show-current
git status
- `pwd` must end in `_laneA` or `_laneB`
- branch prefix must match the lane
- working tree must be clean before starting new work
- If any mismatch — STOP, flag Scott.

### Merge order to main
- Lanes merge to main one at a time, never simultaneously.
- Scott decides merge order based on dependency (usually: whichever ticket unblocks more depos first).
- Always `--no-ff` merge with explanatory message naming the lane.
- After one lane merges, the OTHER lane must `git pull origin main` and rebase its branch before continuing.

### Ramp confirmation
- Every Sonnet, on fresh session, confirms its lane in the ramp line:
  - "Ramped Sonnet #1 laneA [datetime]. Ready."
  - "Ramped Sonnet #2 laneB [datetime]. Ready."

### One-time setup (Scott runs once)
cd C:\Users\scott\OneDrive\Documents
git clone https://github.com/smichaelcapital-cpu/mrx_engine_v1.git mrx_engine_v1_laneA
git clone https://github.com/smichaelcapital-cpu/mrx_engine_v1.git mrx_engine_v1_laneB

---
