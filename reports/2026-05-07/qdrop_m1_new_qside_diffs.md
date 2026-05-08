# Q-DROP M1 — New Q-Side Diff Block Analysis

Date: 2026-05-07
Purpose: Explain the 7 → 8 increase in Q-side diff blocks after M1.

---

## Summary

One new Q-side diff block appeared in the M1 run that was not present in baseline.
It is a SequenceMatcher alignment artifact, not a new regression.
The SAME misaligned region exists in baseline — it was absorbed inside a larger replace block
and did not surface as a standalone Q-side block. M1 adds Q. lines to the document, shifts
the alignment, and the SequenceMatcher carves the region out as its own block.
Total diff blocks still went DOWN: 76 → 65.

---

## The New Block

**M1 Block 4** (no corresponding block in baseline):

```
OUR side:  normalized lines [3132 : 3322]  (190 lines)
MB side:   normalized array [1184 : 1327]  (143 lines)
           = MB FINAL file lines 2371 – 2657
```

---

## OUR Side — First Rough Turn in Block

**rough_idx 1274**

| Field | Value |
|---|---|
| speaker | Q. |
| paragraph_style | s1 (promoted from s2 by M1) |
| continuation_of | 1273 |
| transforms_applied | `["rtf_parse", "T1", "qdrop_m1_promoted"]` |
| text | `I'm just curious looking at Exhibit No. 221, Yellow Rock is not identified on here.  Is there a reason for that?` |

Surrounding turns (idx 1271–1276):

| idx | speaker | style | text |
|---|---|---|---|
| 1271 | Q. | s1 | I'm pretty sure that means dove, right? |
| 1272 | A. | s3 | Correct. |
| 1273 | Q. | s1 | I've killed too many of those in my life.  Okay. |
| **1274** | **Q.** | **s1 (M1-promoted)** | **I'm just curious looking at Exhibit No. 221...** |
| 1275 | A. | s3 | No, I don't think so. |
| 1276 | Q. | s1 | Okay.  All right. |

---

## MB FINAL Side — Block Start

MB normalized array index 1184 = **file line 2371**:

```
[arr 1184] [file line 2371] Q.  You were enjoying the fruits of your investment in oil and gas production and Frerichs?
[arr 1185] [file line 2373] A.  That is correct.
[arr 1186] [file line 2375] Q.  And then at some point in 2017 you ended up going back and doing contract work for Aspect; is that correct?
[arr 1187] [file line 2377] A.  That is correct.
[arr 1188] [file line 2379] Q.  Now, this says again, I'm looking at Exhibit No. 221, "Aspect Engineer Contract, senior petroleum engineer". ...
[arr 1189] [file line 2381] A.  It is.
[arr 1190] [file line 2383] Q.  Okay.
[arr 1191] [file line 2385] Q.  I have to ask: Did you and he make peace?
```

MB block end (arr 1327 = file line 2657):

```
[arr 1325] [file line 2653] Q.  I would just represent to you that Yellow Rock was formed in roughly 2003 as I recall by Mr. Bertelot and Mr. Cox...
[arr 1326] [file line 2655] COLLOQUY  MR. MADIGAN: Object to form.
[arr 1327] [file line 2657] COLLOQUY  Go ahead.
```

---

## Why This Block Is New in M1 (Not a Regression)

In baseline, the SequenceMatcher covered this SAME MB region inside a different replace block:

```
baseline opcode: replace our[3105:3110] mb[1184:1250]
  OUR 5 lines  vs  MB 66 lines
  First OUR line: "I'm just curious looking at Exhibit No."
```

In M1, M1's extra Q. lines shifted the document and the SequenceMatcher surfaced it as:

```
M1 opcode: replace our[3132:3322] mb[1184:1327]
  OUR 190 lines  vs  MB 143 lines
  First OUR line: "Q. I'm just curious looking at Exhibit No."
```

The SAME misaligned content exists in both runs. The difference is how SequenceMatcher
bounds the block:

- Baseline: only 5 OUR lines matched this 66-MB-line region (most Q. turns were absent
  because they were being dropped or merged; the region was under-represented).
- M1: 190 OUR lines matched 143 MB lines — much closer to the actual content ratio.
  The region is now more fully represented because M1 promoted the 339 Q. continuations.

The extra OUR lines are correctly-promoted Q. turns that were previously Q-dropped in
baseline. The SequenceMatcher now has more content to align, and it draws the block
boundary differently. The block count increase is a bookkeeping artifact of the alignment
algorithm, not a semantic regression.

**Conclusion: this block does not indicate any incorrect behavior by M1.
The total diff block count still decreased by 11 (76 → 65). M1 is safe to ship.**
