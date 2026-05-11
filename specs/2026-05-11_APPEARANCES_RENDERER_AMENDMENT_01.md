# SPEC AMENDMENT — Appearances Renderer — also_present separator field

**Date:** 2026-05-11
**Author:** Opus
**Trigger:** Sonnet flagged byte-match risk at CHECKPOINT 1 spot-check — Williams oracle has `BRIAN SOILEAU,Videographer` (no space after comma) while Halprin oracle has `Darren Guastella, Videographer` (with space).
**Status:** APPROVED.

## CHANGE

Add optional `separator` field to `also_present.entries[]` objects.

### Updated schema
{
"name": "BRIAN SOILEAU",
"role": "Videographer",
"separator": ","
}

### Field rules

- `separator` (optional, string). Literal string joining `name` and `role`. Default is `", "` (comma + space) when omitted.
- Only applies when `also_present.kind == "header_block"` AND `role` is non-null.
- Renderer emits: `<name><separator><role>` at indent 4. Verbatim, no normalization.

## WHY

RULE-INPUT-IS-SACRED. Williams FINAL has `BRIAN SOILEAU,Videographer` with no space — same verbatim-preservation family as `REED SMITH,LLP`, `asirianni@@windelsmarx.com`, `kenndyslaw.com`, `nexsepruet.com`.

## OBSERVED VALUES

| Depo | Entry | Stored separator |
|---|---|---|
| Halprin | Darren Guastella, Videographer | default (omit) |
| Wunstell | BRIAN SOILEAU, Videographer | default (omit) |
| Wunstell | Kelly Wunstell | n/a (role null) |
| Williams | BRIAN SOILEAU,Videographer | `","` explicit |
| Butler | ADRIEL OLIVERA, Videographer | default |
| Black | MICHAEL BERGERON, Videographer | default |

## DATA FILE CHANGES

halprin.json: no change. williams.json: explicit `"separator": ","` on Soileau entry.

— End amendment —
