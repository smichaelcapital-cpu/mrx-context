# Em-Dash Spot-Check: Raw .sgngl Files

**Date:** 2026-05-10 (evening)
**Author:** Sonnet (evening instance)
**Trigger:** Scott observed `--` in `011121rooks-BP-2 rough.sgngl`. Prior recon claimed "zero -- across 6 raw depos."
**Status:** COMPLETE — read-only spot-check, local report only

---

## Result

**Prior "zero em-dash in raws" claim is wrong. `--` appears in every single sampled raw file.**

---

## Summary

| Metric | Value |
|---|---|
| Files checked | 55 |
| Zero `--` | 0 |
| At least one `--` | 55 (100%) |
| Total `--` count across all files | 13,541 |
| Range per file | 55 – 675 |
| Median (approx.) | ~200 |

---

## File Table (sorted by count, descending)

| Filename | `--` count |
|---|---|
| 080921ROUGHDRAFT TAREK ABICHOU.sgngl | 675 |
| 030526yellowrock-ROUGH.sgngl | 608 |
| 012522novelozo-bp-ROUGH.sgngl | 570 |
| 062422danos-ROUGH.sgngl | 463 |
| 021422colbert-BP-ROUGH.sgngl | 445 |
| 020123Wunstell-ROUGH_Original.sgngl | 441 |
| 101822black-ROUGH.sgngl | 420 |
| 101222BINDER-ROUGH.sgngl | 388 |
| 102225CAM-ROUGH.sgngl | 379 |
| 081120CAPSTONE ROUGH DRAFT.sgngl | 371 |
| 032125olsen-ROUGH.sgngl | 369 |
| 020226pedersen-ROUGH.sgngl | 368 |
| 032025olsen-ROUGH DRAFT.sgngl | 366 |
| 040226yellowrock-ROUGH.sgngl | 360 |
| 080922robinson-ROUGH.sgngl | 344 |
| 030922barnes-rough_Original.sgngl | 344 |
| Copy(1) of 07821ROUGHDRAFT- MATT STUTZ.sgngl | 339 |
| 110322MARTIN-ROUGH.sgngl | 338 |
| 020323doj-ROUGH DRAFT.sgngl | 333 |
| 040825olsen-ROUGH DRAFT.sgngl | 315 |
| 012022HWILLIAMS-BP-ROUGH.sgngl | 301 |
| 021722BP30B6 -ROUGH.sgngl | 285 |
| 040825olsen-ROUGH DRAFT_Original.sgngl | 263 |
| 040325dent-ROUGH DRAFT.sgngl | 263 |
| 0525black-bp-ROUGH.sgngl | 219 |
| 112922KGriffin-ROUGH.sgngl | 215 |
| 102325CAM-ROUGH.sgngl | 209 |
| 120624farmers-ROUGH.sgngl | 208 |
| 111522RBlanks-ROUGH.sgngl | 202 |
| 0525black-bp-ROUGH_Original.sgngl | 199 |
| 012122townser-BP-ROUGH.sgngl | 192 |
| 011923fountainROUGH.sgngl | 188 |
| 110922LEE-ROUGH.sgngl | 176 |
| 041923addison-ROUGH.sgngl | 171 |
| 020122liddell-BP-ROUGH.sgngl | 169 |
| 080924LePlace-ROUGH.sgngl | 161 |
| 011122rough3.sgngl | 160 |
| 110917vthalter-ROUGH.sgngl | 144 |
| 092520seaman-ROUGH.sgngl | 129 |
| 121322martin-ROUGH.sgngl | 126 |
| 052824scottBP-ROUGH.sgngl | 114 |
| 020420taxotere-ROUGH.sgngl | 109 |
| **011121rooks-BP-2 rough.sgngl** | **105** |
| 052825olsen-ROUGH.sgngl | 100 |
| 042925olsen-clause-ROUGH.sgngl | 98 |
| 010523Aspen-ROUGH.sgngl | 98 |
| 092424leplace-ROUGH DRAFT.sgngl | 95 |
| 121322griffin-ROUGH.sgngl | 94 |
| 080521ROUGH DRAFT P DALTON.sgngl | 92 |
| 50324CHURCH-ROUGH.sgngl | 84 |
| 021222SNELSON-BP-ROUGH.sgngl | 72 |
| 021222SNELSON-BP-ROUGH_Original.sgngl | 72 |
| 021225barnett-ROUGH.sgngl | 70 |
| 060122Rogers-ROUGH.sgngl | 67 |
| 011121rooks-BP rough.sgngl | 55 |

---

## Context Samples (3 files)

The `--` appears in the middle of steno code streams — interspersed with steno shorthand characters (single letters, numbers, `@`, `?`, `{`, `\`, etc.) and partial words. It is a structural element of the steno output format, not only an interruption marker inserted by MB.

**Highest count file** (`080921ROUGHDRAFT TAREK ABICHOU.sgngl`, 675 occurrences):
```
for  D" a2 them   @ a2 to b2 0b2  --   0 Mb2 which is   @ eb2 to     {b2 0  b2
k2 k2 emissions   R  l2 from Ul2 {l2  --   l2 l2 \K  @ {m2 Mike   m
```

**Target file** (`011121rooks-BP-2 rough.sgngl`, 105 occurrences):
```
E ? that ? T ? A ? point in time  --  @ * ? H ? S ? 2011 P ? , @ ?
H ? S ? 2011 P ? , @ ? ? 2012  --  ? you ? were ? the
```

**Lowest count file** (`011121rooks-BP rough.sgngl`, 55 occurrences):
```
phone . $!@ 7 $!@ 7 if they happen to say something  --  unlikely, but if they chime in, P a 7 D 7 ` 7
n 4 ; 8 married @ \ 8 to s 8 8  --  0 8 I 8 8 have " 8 0 8
```

In all three files the `--` is surrounded by steno codes, not surrounded by ordinary English words the way a human-authored interruption marker would appear. This is consistent with `--` being a steno output artifact/continuation marker, not solely MB's deliberate em-dash insertion.

---

## Verdict

**Prior "zero em-dash in raws" claim is wrong.** Every one of 55 sampled raw .sgngl files contains `--`, with counts ranging from 55 to 675 per file. The prior claim was either from a different metric (e.g., checking extracted text after the printable-line filter, not the raw binary) or the 6-depo sample was misread.

---

## Fingerprint Implications

This finding has two consequences:

**1. `split_double_dash_interruption` interpretation shifts.**
This pattern (currently AUTO, 0.9624 training pairs_coverage) measures `--` at the end of Q/A turns in MB's *finals*. Since roughs also contain `--` throughout, what this pattern actually measures is: *MB preserves steno interruption markers as `--` in the final* rather than removing them. That is still a valid MB habit — many court reporters clean these up. The pattern remains valid but should be described as "preservation of interruption markers" not "insertion."

**2. `punct_emdash_addition` measurement is more suspect than the YELLOW audit already concluded.**
The training detection (`re.search(r'(—|--)', content)`) scans finals for `--` or `—`. Since roughs also contain `--` extensively, presence in finals is even weaker evidence of MB *adding* them. The SUGGEST demotion from Sunday cleanup is correct. Gap-alignment against clean (steno-filtered) roughs is the only way to measure actual addition events. This reinforces TD-001 and TD-002 as prerequisites.

**No fingerprint state changes made in this spot-check.** Read-only. The SUGGEST lane for `punct_emdash_addition` was already applied in the Sunday cleanup. No further action needed here beyond flagging for Scott.

---

— End of em-dash raw spot-check —
