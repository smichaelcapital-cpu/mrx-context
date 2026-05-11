# CR Generalization Ledger
# Tracks every MB-specific decision + its generalizable counterpart.
# When CR #2 onboards, this ledger drives what gets templated vs. re-derived.

## Decision log

| # | Decision | MB-specific value | Generalized rule | Notes | Date | Source |
|---|---|---|---|---|---|---|
| 1 | File layout for fingerprints | reporters/MB.yaml | reporters/<reporter_id>.yaml | One personal-style file per CR. Layered behind jurisdiction + case_type files. | 2026-05-09 | architecture lock |
| 2 | Identity layer software field | Case CATalyst 22.13 build 45255 | software.{name, version, build, vendor} — populate from any CR | Most CRs use Case CATalyst, but field is software-agnostic | 2026-05-09 | MB.yaml v0 |
| 3 | Identity layer certifications | CCR + RPR | certifications: [list of strings] | Generalized — accept any CR's cert set | 2026-05-09 | MB.yaml v0 |
| 4 | Jurisdiction sub-fields | primary: louisiana, secondary: delaware | primary: [list], secondary: [list] | One CR can practice across jurisdictions; structure must support multiple | 2026-05-09 | MB.yaml v0 |
| 5 | Translation artifact: q_label_s2 | counts brandl/halprin/easley + classification mb_specific_OR_louisiana | Pattern-by-pattern slot in any reporter file | Classification ambiguous until LA state guidelines parsed; flag as `mb_specific_OR_<jurisdiction>` | 2026-05-09 | cross-depo scan |
| 6 | Translation artifact: doubled_pure | classified universal | Universal patterns belong in jurisdictions/_universal.yaml NOT reporters/<id>.yaml | Future move — for v0 left in MB.yaml as observed data | 2026-05-09 | cross-depo scan |
| 7 | Translation artifact: speaker_in_body | classified universal | Same as above | Future move to universal layer | 2026-05-09 | cross-depo scan |
| 8 | Negative fingerprint: em_dash_double_hyphen | verified zero across 6 depos | verified_absences slot in any reporter file | Highest-leverage suppressor type. Should also exist as universal entry once confirmed across more CRs. | 2026-05-09 | cross-depo scan |
| 9 | AD control data treatment | counts kept in MB.yaml as ad_control_counts | Per-pattern, retain control-group data in originating CR file ONLY UNTIL classification resolved | Once jurisdiction guidelines parsed, control data moves out of CR files | 2026-05-09 | architecture call |
| 10 | jurisdiction_OR_personal classification | flag as mb_specific_OR_louisiana | flag as <reporter_id>_specific_OR_<jurisdiction> | Honest gap marker — forces resolution when guidelines arrive | 2026-05-09 | architecture call |
| 11 | Pending-evidence slots | pending_evidence: true | pending_evidence: true (universal pattern) | Better than fake content. All deferred slots use this marker. | 2026-05-09 | architecture call |
| 12 | Push discipline (one-time override) | Sonnet pushed today's docs commits per Scott | Standing rule resumes after one-shot override | Capture in comm rules later, not here | 2026-05-09 | session decision |
| 13 | Front-matter renderer architecture | src/profiles/mb/data/<block>.json per depo | src/profiles/<reporter_id>/data/<block>.json; renderer code stays universal | 5 blocks — cover, index, appearances, stipulation, reporter cert. Renderer is data-driven. Next CR onboards by adding profile folder only. | 2026-05-11 | front_matter_dump + APPEARANCES spec + amendment 01 |
| 14 | Stipulation read/sign vs waive | per-depo boolean in stipulation.json | stipulation block has a witness_reserves_signature: true/false field | Observed both variants across 6 MB depos. Halprin/Williams/Olsen reserve. Blanks/Butler waive. Not MB style — case-by-case. | 2026-05-11 | front_matter_dump + APPEARANCES spec + amendment 01 |
| 15 | also_present separator field | omitted (default ", ") or explicit "," for no-space case | appearances JSON entry has optional separator field; renderer emits verbatim | From APPEARANCES_RENDERER_AMENDMENT_01. RULE-INPUT-IS-SACRED. Williams Soileau entry has no space after comma. | 2026-05-11 | front_matter_dump + APPEARANCES spec + amendment 01 |

## Generalization questions queued for resolution

1. **LA state guidelines parsing** — required to resolve all `mb_specific_OR_louisiana` entries
2. **Universal layer extraction** — patterns currently classified `universal` (doubled_pure, speaker_in_body) should migrate from MB.yaml to jurisdictions/_universal.yaml when that file is built
3. **Stylistic prohibitions extraction** — raw-vs-final diff analysis to populate negative_fingerprint.stylistic_prohibitions
4. **Multi-CR validation** — em_dash absence is verified across MB + AD only. Confirm across additional CRs before promoting to universal-layer rule.
