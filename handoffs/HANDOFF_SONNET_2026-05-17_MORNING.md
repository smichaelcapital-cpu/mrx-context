# HANDOFF — SONNET — 2026-05-17 MORNING

You are fresh Sonnet on 2026-05-17 morning. You are the SOLE builder agent this session. Scott is founder and PM. Opus is solution architect in a separate chat.

## STANDING RULES — non-negotiable

Same 18 rules from 2026-05-16. Particular emphasis on Rule 18 (branch hygiene).

**NEW RULE — RULE-SINGLE-SONNET-PER-CLONE — in effect immediately:**
Only one Sonnet operates on the engine repo clone at a time. No parallel Sonnet work until dual-clone folder structure is designed and approved by Scott. If a second Sonnet is somehow active, STOP and flag to Scott immediately.

Your role: build per spec, recon thoroughly, push back with evidence, act only on Opus or Scott approval. You write files and run shell. Scott pushes (push relaxation per-session per Scott).

## RAMP — READ IN ORDER

1. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET.md
2. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/CODER_MINDSET_ADDENDUM.md
3. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/RULE_SHEET_v1.md
4. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/handoffs/HANDOFF_SONNET_2026-05-17_MORNING.md (this file)
5. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_SINGLE_CLONE_PARALLEL_INCIDENT.md
6. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-15_BRANCH_DRIFT_INCIDENT.md
7. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/build-reports/2026-05-16_VERIFICATION_ALL_6.md
8. https://raw.githubusercontent.com/smichaelcapital-cpu/mrx-context/main/knowledge/2026-05-16_OLSEN_ARBITRATION_COVER_RECON.md

## ORACLE FILE LOCATION

`C:/Users/scott/OneDrive/Documents/mrx-context/oracle/finals/`

Contains FINAL oracle .txt files for all 6 MB depos:
- halprin
- 060122williams
- 082222butler
- 101322blanks
- 032025olsen
- 0525black_bp

Use this path before searching elsewhere. Last session lost 30 minutes hunting for the Butler oracle.

## ENGINE REPO CLONE PATH

`/c/Users/scott/OneDrive/Documents/mrx_engine_v1/mrx_engine_v1`

You are the only Sonnet on this clone. No second Sonnet exists this session.

## CONTEXT REPO CLONE PATH

`/c/Users/scott/OneDrive/Documents/mrx-context`

## ONE-LINE STATE

5 of 6 MB depos render end-to-end on main commit 711eb26. black_bp is the last cover-renderer gap. Your top priority will likely be B1.7.5 (black_bp cover loc_len=4).

## LAST NIGHT'S SHIPS — for context

- B1.7.3 merged (waive-mode stipulation, unblocks Butler + Blanks)
- B1.7.4 merged (arbitration cover, unblocks Olsen)
- Both shipped via --no-ff merge commit 711eb26 after a branch-drift recovery
- Verification run confirmed 5/6 render clean, black_bp gracefully skipped

## 3 DEFERRED TILES — PRIORITY ORDER

**B1.7.5 — black_bp cover loc_len=4 (TOP PRIORITY)**
- Blocks: black_bp (1 of 6 depos)
- Same family as B1.7.4 — add new `elif label_in_main and loc_len == 4:` branch to cover.py
- Recon required: read black_bp oracle page 1, slot-by-slot mapping, propose layout
- Cover.json path: src/profiles/mb/data/front_matter/0525black_bp/cover.json
- Estimated 30-45 min after spec

**B1.7.6 — Olsen appearances reporter anchor**
- Cosmetic 1-line drift; not critical
- reporter_anchor_line=19 hardcoded in appearances_renderer.py; Olsen oracle shows line 18
- Likely solution: make per-depo data field

**B1.7.7 — Olsen appearances VIDEOGRAPHER slot**
- Cosmetic 1-slot drift; not critical
- VIDEOGRAPHER renders at slot 14 main, oracle shows slot 15 sub
- Investigation needed in inline_label handling

## PRE-FLIGHT — RUN EVERY SESSION

Before any code change, run these in order and post results in your first message:

```
git fetch origin main
cd /c/Users/scott/OneDrive/Documents/mrx_engine_v1/mrx_engine_v1
pwd
git rev-parse --git-dir
git branch --show-current
git log origin/main..HEAD --oneline
git status
```

If branch is not main or working tree is dirty — STOP and flag before touching anything.

## WHAT YOU DO FIRST

1. Read the 8 files above in order.
2. Run the pre-flight commands above.
3. Confirm in ONE LINE: "Ramped Sonnet 2026-05-17 [datetime]. Ready." plus pre-flight output + one sentence on state.
4. Do not start work until Opus or Scott responds.

## REMEMBER

- Slow is smooth, smooth is fast.
- Recon first, build second.
- Push back hard with evidence, act only on approval.
- Test cases designed BEFORE running any model.
- 30-min wall per build pass.
- One fix per branch.
- Branch cut FROM origin/main after git fetch — every time.
- You are the only Sonnet this session.
