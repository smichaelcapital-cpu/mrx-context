# Q-DROP M1 Evidence -- All 339 s2 Continuation Turns

**Date:** 2026-05-07
**Source:** Brandl deposition (032626YELLOWROCK), MB Halprin court reporter
**Purpose:** Side-by-side evidence for all 339 s2 Q. continuation turns in rough.

## Methodology

FINAL source: `032626YELLOWROCK-FINAL_T.stage1.txt` (1,922 Q. turns).

Stage 1 maps both `\pard\s1` and `\pard\s2` FINAL Q. paragraphs to `Q.\t<text>`.
This means we **cannot** distinguish 'MB converted to new s1' from 'MB kept as s2'
from this file alone. What we CAN determine is whether the s2 text appears as its
own standalone `Q.` line in FINAL, or not.

**STANDALONE Q. IN FINAL** = s2 text appears as its own Q. line. Our Stage 5 merges
this into the parent Q. paragraph, creating a Q-DROP diff vs MB.

**NOT STANDALONE** = s2 text is absent as a standalone Q. line. Either merged into
the parent Q. turn in FINAL, or deleted. Our Stage 5 merge is correct here.

Alignment: SequenceMatcher on rough Q. sequence vs FINAL Q. sequence.
  - `equal` opcode -> STANDALONE (exact, high confidence)
  - `delete` opcode -> NOT STANDALONE (confirmed absent)
  - `replace` opcode, text > 30 chars, sim >= 85% -> STANDALONE (text-corrected)
  - `replace` opcode, short text or low sim -> AMBIGUOUS

## Summary

| Status | Count |
|---|---:|
| STANDALONE Q. IN FINAL (Q-DROP if we merge) | 249 |
| NOT STANDALONE (our merge is correct) | 5 |
| AMBIGUOUS (short text, needs position context) | 39 |
| EMPTY (no content) | 46 |
| **Total** | **339** |

---

## Evidence Table

Columns:
- `rough_idx` / `parent_idx`: turn indices in corrected_turns.json
- `parent s1`: the s1 Q. turn that owns this s2 (typically an acknowledgment)
- `s2 continuation`: the continuation Q. text in rough
- `FINAL line #`: line number in 032626YELLOWROCK-FINAL_T.stage1.txt
- `MB FINAL`: MB's text at the aligned position
- `status`: STANDALONE / NOT STANDALONE / AMBIGUOUS / EMPTY

### 1. idx 111 (parent 110)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 53 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 2. idx 112 (parent 110)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Have you been deposed before?` |
| FINAL line # | 55 |
| MB FINAL Q. | `Have you been deposed before?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 3. idx 115 (parent 114)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Approximately how many times?` |
| FINAL line # | 61 |
| MB FINAL Q. | `Approximately how many times?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 4. idx 120 (parent 119)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what kind of matter was that?` |
| FINAL line # | 71 |
| MB FINAL Q. | `And what kind of matter was that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 5. idx 125 (parent 124)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And were you giving factual testimony or expert testimony?  And if you don't understand the different between those two I'm happy to explain it.` |
| FINAL line # | 81 |
| MB FINAL Q. | `And were you giving factual testimony or expert testimony? And if you don't understand the difference between those two, I'm happy to explain it.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 6. idx 130 (parent 129)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was the other deposition before that?` |
| FINAL line # | 91 |
| MB FINAL Q. | `And what was the other deposition before that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 7. idx 148 (parent 147)

| Field | Text |
|---|---|
| Rough parent s1 | `Got it, okay.` |
| Rough s2 continuation | `And were you a defendant in the case?` |
| FINAL line # | 129 |
| MB FINAL Q. | `And were you a defendant in the case?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 8. idx 159 (parent 158)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Where did the incident happen?` |
| FINAL line # | 155 |
| MB FINAL Q. | `Where did the incident happen?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 9. idx 168 (parent 167)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `All right.  We got on a little diversion with that so let me go back to some of the basics.  Let me go over a few rules about the deposition.  I'm sure you've geneos over a lot of this with your counsel but I always like to make sure you and I are on the same page as we spend the day together, okay?` |
| FINAL line # | 203 |
| MB FINAL Q. | `Okay. All right. We talked about your prior depo's. Have you been I'm going to walk through these questions carefully. And some of them are yes or no questions because I know there's things I may not be allowed to get into.` |
| **Status** | **AMBIGUOUS (sim 28%, text len 300)** (sim 28%) |

### 10. idx 173 (parent 172)

| Field | Text |
|---|---|
| Rough parent s1 | `All right.` |
| Rough s2 continuation | `Second rule is our court reporter can only take down answers that are verbal.  So if you nod your head or shake your head or if you give an uh-huh or an uhuh, one of us, either her or I are going to ask you to clarify that, was this a yes or no and we are not let me be very clear to try to badger you or harass you we're trying to make sure the written record she's preparing, the transcript is clear, okay?` |
| FINAL line # | 203 |
| MB FINAL Q. | `Okay. All right. We talked about your prior depo's. Have you been I'm going to walk through these questions carefully. And some of them are yes or no questions because I know there's things I may not be allowed to get into.` |
| **Status** | **AMBIGUOUS (sim 30%, text len 408)** (sim 30%) |

### 11. idx 180 (parent 179)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `All right.  We talked about your prior depo's, have you been I'm going to walkthrough these questions carefully.  And some of them are yes or no questions because I know there's thing I may not be allowed to get into.` |
| FINAL line # | 217 |
| MB FINAL Q. | `Let's start with your background. Where did you grow up, sir?` |
| **Status** | **AMBIGUOUS (sim 20%, text len 217)** (sim 20%) |

### 12. idx 181 (parent 179)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Have you ever testified as a retained or expert witness?` |
| FINAL line # | 211 |
| MB FINAL Q. | `Have you ever been retained to provide consulting expert or other expert testimony?` |
| **Status** | **AMBIGUOUS (sim 58%, text len 56)** (sim 58%) |

### 13. idx 186 (parent 185)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let's start with your background.  Where did you grow up, sir?` |
| FINAL line # | 217 |
| MB FINAL Q. | `Let's start with your background. Where did you grow up, sir?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 14. idx 201 (parent 200)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And you got that degree in 1992?` |
| FINAL line # | 249 |
| MB FINAL Q. | `And you got that degree in 1992?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 15. idx 222 (parent 221)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `After you graduated from Texas A&M, where did you go to work?` |
| FINAL line # | 293 |
| MB FINAL Q. | `After you graduated from Texas A&M, where did you go to work?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 16. idx 245 (parent 244)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 339 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 17. idx 246 (parent 244)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And in your role as an area engineer, what portion was there a geographic portion of the Gulf that you were looking at?` |
| FINAL line # | 341 |
| MB FINAL Q. | `And in your role as an area engineer, what portion was there a geographic portion of the Gulf that you were looking at?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 18. idx 251 (parent 250)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When and you left Conoco in 1994?` |
| FINAL line # | 351 |
| MB FINAL Q. | `When and you left Conoco in 1994?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 19. idx 268 (parent 267)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And how long were you involved with that location in San Angelo?` |
| FINAL line # | 385 |
| MB FINAL Q. | `And how long were you involved with that location in San Angelo?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 20. idx 285 (parent 284)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 417 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 21. idx 286 (parent 284)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was your position what were your positions at Ballard?` |
| FINAL line # | 419 |
| MB FINAL Q. | `And what was your position what were your positions at Ballard?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 22. idx 297 (parent 296)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And the drill that you were maintaining, was it let's step back because we're going to talk a lot about this day so I want to get some terminology that you're comfortable with so we can agree to use.` |
| FINAL line # | 441 |
| MB FINAL Q. | `And the drill that you were maintaining, was it let's step back because we're going to talk a lot about this today, so I want to get some terminology that you're comfortable with so we can agree to use it.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 23. idx 298 (parent 296)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So there are instances in oil and gas where you drill new wells, correct?` |
| FINAL line # | 443 |
| MB FINAL Q. | `So there are instances in oil and gas where you drill new wells, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 24. idx 303 (parent 302)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I've seen a variety of different terms used for work on existing wells from recompletions to side tracks to just reworking them.  I'm going to work with you to come up with some terms for that.  But for work done on existing wells of whatever nature, can we just call that existing wells or is there a term that you're more comfortable?` |
| FINAL line # | 455 |
| MB FINAL Q. | `I've seen a variety of different terms used for work on existing wells from recompletions to side tracks to just reworking them. I'm going to work with you to come up with some terms for that. But for work done on existing wells of whatever nature, can we just call that existing wells or is there a term that you're more comfortable with?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 25. idx 306 (parent 305)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And are there different are there some broad categories of types of work you can do on an existing well?` |
| FINAL line # | 461 |
| MB FINAL Q. | `And are there different are there some broad categories of types of work you can do on an existing well?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 26. idx 325 (parent 324)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 485 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 27. idx 330 (parent 329)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So in a recompletion absent some complication, you are not needing a drilling rig.  You node a rig to work with tubing an tools, but not to drill, because you're not you're using just the wellbore that was there before?` |
| FINAL line # | 515 |
| MB FINAL Q. | `So in a recompletion, absent some complication, you are not needing a drilling rig. You need a rig to work with tubing and tools, but not to drill, because you're not you're using just the wellbore that was there before?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 28. idx 333 (parent 332)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let's talk about a workover.  What is a workover?` |
| FINAL line # | 521 |
| MB FINAL Q. | `Let's talk about workover. What is workover?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 29. idx 340 (parent 339)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And again with a workover you don't necessarily need a drilling rig because you're not drilling a new whole or adding any new pipe, correct?` |
| FINAL line # | 535 |
| MB FINAL Q. | `And again, with workover you don't necessarily need a drilling rig because you're not drilling a new hole or adding any new pipe, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 30. idx 343 (parent 342)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And let's talk about a sidetrack.  Now on a sidetrack well, what is a sidetrack?` |
| FINAL line # | 541 |
| MB FINAL Q. | `And let's talk about a sidetrack. Now on a sidetrack well, what is a sidetrack?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 31. idx 350 (parent 349)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Trust me, that understanding is going to make things a lot smoother as we start talking about Sulphur Mines, okay?` |
| FINAL line # | 555 |
| MB FINAL Q. | `Trust me, that understanding is going to make things a lot smoother as we start talking about Sulphur Mines.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 32. idx 359 (parent 358)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Were you involved in identifying the locations to be drilled?` |
| FINAL line # | 577 |
| MB FINAL Q. | `Were you involved in identifying the locations to be drilled?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 33. idx 362 (parent 361)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was the nature of your role on that?` |
| FINAL line # | 583 |
| MB FINAL Q. | `And what was the nature of your role on that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 34. idx 367 (parent 366)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I haven't asked you this, sir, but your training is in petroleum engineering correct your education is in petroleum engineering?` |
| FINAL line # | 595 |
| MB FINAL Q. | `I haven't asked you this, sir, but your training is in petroleum engineering, correct your education is in petroleum engineering?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 35. idx 384 (parent 383)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Do you hold yourself out as an expert in petrophysics?` |
| FINAL line # | 631 |
| MB FINAL Q. | `Do you hold yourself out as an expert in petrophysics?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 36. idx 391 (parent 390)

| Field | Text |
|---|---|
| Rough parent s1 | `That's what I wanted to know.  Okay, good.` |
| Rough s2 continuation | `Are there other let me just ask that generally.  Do you hold yourself out as an expert in seismic interpretation?` |
| FINAL line # | 645 |
| MB FINAL Q. | `Are there other let me just ask that generally. Do you hold yourself out as an expert in seismic interpretation?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 37. idx 396 (parent 395)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  Okay.` |
| Rough s2 continuation | `Do you hold yourself out as an expert in petroleum or oil and gas drilling operations?` |
| FINAL line # | 655 |
| MB FINAL Q. | `Do you hold yourself out as an expert in petroleum or oil and gas drilling operations?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 38. idx 403 (parent 402)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I assume part of that is while I think a lot of lay people view directional drilling as hey you can curve, you can go horizontally, it's not without limits being correct?` |
| FINAL line # | 669 |
| MB FINAL Q. | `And I assume part of that is while I think a lot of lay people view directional drilling as hey, you can curve, you can go horizontally, it's not without limits, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 39. idx 419 (parent 418)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And once either of those problems arise, I assume there are various things the drilling operator can try to do to get past that problem, to unstick the pipe, correct?` |
| FINAL line # | 699 |
| MB FINAL Q. | `And once either of those problems arise, I assume there are various things the drilling operator can try to do to get past that problem, to unstick the pipe, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 40. idx 454 (parent 453)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So while you were at Ballard, roughly if you recall, how many new drills did sorry that wasn't good phrasing.` |
| FINAL line # | 773 |
| MB FINAL Q. | `So while you were at Ballard, roughly, if you recall, how many new drills did sorry, that wasn't good phrasing.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 41. idx 455 (parent 453)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `While you were at Ballard from '94 to 98 approximately how many new wells do you recall overseeing in there drilling operations in southeast Texas and southwest Louisiana approximately?` |
| FINAL line # | 775 |
| MB FINAL Q. | `While you were at Ballard from '94 to '98, approximately how many new wells do you recall overseeing in their drilling operations in Southeast Texas and Southwest Louisiana approximately?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 42. idx 458 (parent 457)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And during that period, did you were those mostly vertical wells, directional wells, a mixture of both?` |
| FINAL line # | 781 |
| MB FINAL Q. | `And during that period, did you were those mostly vertical wells, directional wells, a mixture of both?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 43. idx 465 (parent 464)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What was the major field or fields that this work was being done in?` |
| FINAL line # | 795 |
| MB FINAL Q. | `What was the major field or fields that this work was being done in?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 44. idx 474 (parent 473)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And are there any fields of note, oil fields of note that those were in that had became more prolific since your time there?` |
| FINAL line # | 813 |
| MB FINAL Q. | `And are there any fields of note, oil fields of note, that those were in that had became more prolific since your time there?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 45. idx 483 (parent 482)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  All right.` |
| Rough s2 continuation | `When did you leave Ballard?` |
| FINAL line # | 833 |
| MB FINAL Q. | `When did you leave Ballard?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 46. idx 510 (parent 509)

| Field | Text |
|---|---|
| Rough parent s1 | `Good job.` |
| Rough s2 continuation | `And was that on shore or offshore?` |
| FINAL line # | 891 |
| MB FINAL Q. | `And was that onshore or offshore?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 47. idx 513 (parent 512)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was your job generally?` |
| FINAL line # | 897 |
| MB FINAL Q. | `And what was your job generally?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 48. idx 516 (parent 515)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Why did you leave Union Gas?` |
| FINAL line # | 903 |
| MB FINAL Q. | `Why did you leave Union Gas?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 49. idx 523 (parent 522)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `During that five were you allowed to take another job during that fiveyear period?` |
| FINAL line # | 917 |
| MB FINAL Q. | `During that five were you allowed to take another job during that fiveyear period?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 50. idx 532 (parent 531)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And where are they in Houston or were they in Houston?` |
| FINAL line # | 935 |
| MB FINAL Q. | `And where are they in Houston or were they in Houston?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 51. idx 535 (parent 534)

| Field | Text |
|---|---|
| Rough parent s1 | `Denver, okay.` |
| Rough s2 continuation | `And what did you do for them?` |
| FINAL line # | 941 |
| MB FINAL Q. | `And what did you do for them?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 52. idx 548 (parent 547)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 961 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 53. idx 549 (parent 547)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I'm sensing that meant you stayed here in Houston during this job?` |
| FINAL line # | 969 |
| MB FINAL Q. | `And I'm sensing that meant you stayed here in Houston during this job?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 54. idx 567 (parent 566)

| Field | Text |
|---|---|
| Rough parent s1 | `I have the resume but it doesn't begin until 2009.  And that may be because of the weighty printed it or I don't have access to see the rest of it.  Because then I'll hopefully go through this a little more quickly.` |
| Rough s2 continuation | `Okay.  So from 99 to end of 2005 early 2005 you were at Aspect Resources or it's successor acquiring so Samedan or Noble.  Generally speaking, did your geographic responsibilities stay southeast Texas an southwest Louisiana at that time?` |
| FINAL line # | 1011 |
| MB FINAL Q. | `So from '99 till the end of 2004, early 2005, you were at Aspect Resources or its successor acquiring company, Samedan or Noble. Generally speaking, did your geographic area of responsibilities stay Southeast Texas and Southwest Louisiana at that time?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 92%) |

### 55. idx 570 (parent 569)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I just want to make sure I understood that.  Because I thought you said the geography is that rank to southeast Texas but you said that you evolved into the production engineer for southwest Louisiana?` |
| FINAL line # | 1017 |
| MB FINAL Q. | `I just want to make sure I understood that. Because I thought you said the geography shrank to Southeast Texas. But you just said you evolved into the production engineer for Southwest Louisiana?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 56. idx 573 (parent 572)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1015 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 57. idx 578 (parent 577)

| Field | Text |
|---|---|
| Rough parent s1 | `You're in my neck of the woods now but I was born in Beaumont, Texas and lived and breathed the Neches River, so...` |
| Rough s2 continuation | `When you were the production foreman and I think we talked about that, that's when you were Well, no, we didn't.  Sorry.  What was your role let me step back.  Between that fiveyear period approximately from 99 to 2005, were your principal jobs either production foreman or production engineer?` |
| FINAL line # | 1017 |
| MB FINAL Q. | `I just want to make sure I understood that. Because I thought you said the geography shrank to Southeast Texas. But you just said you evolved into the production engineer for Southwest Louisiana?` |
| **Status** | **AMBIGUOUS (sim 29%, text len 294)** (sim 29%) |

### 58. idx 581 (parent 580)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Generally speaking, when you were production foreman over the larger geographic area, southeast Texas and southwest Louisiana, what was your general job?` |
| FINAL line # | 1037 |
| MB FINAL Q. | `Generally speaking, when you were production foreman over the larger geographic area, Southeast Texas and Southwest Louisiana, what was your general job?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 59. idx 588 (parent 587)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I'm going to ask you this periodically, did at this point in your career have any of the fields that you've been involved in or drilling operations, have any of those in your career up to 2005 involved salt domes?` |
| FINAL line # | 1051 |
| MB FINAL Q. | `And I'm going to ask you this periodically, did at this point in your career have any of the fields that you've been involved in or drilling operations, have any of those in your career up to 2005 involved salt domes?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 60. idx 633 (parent 632)

| Field | Text |
|---|---|
| Rough parent s1 | `Working, okay.` |
| Rough s2 continuation | `Do you do any of your consulting work through shine er?` |
| FINAL line # | 1153 |
| MB FINAL Q. | `Do you do any of your consulting work through Shiner?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 61. idx 638 (parent 637)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And when did you stop doing consulting work for that involved the Sulphur Mines Field?` |
| FINAL line # | 1163 |
| MB FINAL Q. | `And when did you stop doing consulting work for that involved the Sulphur Mines Field?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 62. idx 642 (parent 641)

| Field | Text |
|---|---|
| Rough parent s1 | `I need to deal with that objection.` |
| Rough s2 continuation | `Are you still working doing consulting work that volumes Sulphur Mines?` |
| FINAL line # | 1171 |
| MB FINAL Q. | `Are you still working doing consulting work that involves Sulphur Mines?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 63. idx 645 (parent 644)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  I have to tread carefully here because he's going to have an issue potentially.` |
| Rough s2 continuation | `Are you this is a yes or no question and I'm not trying to badger you.  I'm trying to make sure I don't get in trouble with TJ.` |
| FINAL line # | 1177 |
| MB FINAL Q. | `Are you this is a yes or no question and I'm not trying to badger you. I'm trying to make sure I don't get in trouble with TJ.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 64. idx 646 (parent 644)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  I have to tread carefully here because he's going to have an issue potentially.` |
| Rough s2 continuation | `Okay?` |
| FINAL line # | 1179 |
| MB FINAL Q. | `Okay?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 65. idx 647 (parent 644)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  I have to tread carefully here because he's going to have an issue potentially.` |
| Rough s2 continuation | `Are you doing any consulting work with other experts involving Sulphur Mines?` |
| FINAL line # | 1181 |
| MB FINAL Q. | `Are you doing any consulting work with other experts involving Sulphur Mines?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 66. idx 652 (parent 651)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Are you doing consulting work still for that involves Sulphur Mines as you sit here today, other than giving your deposition?` |
| FINAL line # | 1191 |
| MB FINAL Q. | `Are you doing consulting work still for that involves Sulphur Mines as you sit here today, other than giving your deposition?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 67. idx 655 (parent 654)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I should ask this, sir.  Are you being paid for your time today by Yellow Rock?` |
| FINAL line # | 1197 |
| MB FINAL Q. | `I should ask this, sir. Are you being paid for your time today by Yellow Rock?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 68. idx 664 (parent 663)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Roughly well, at some point as I understand it in the last 18 months, Yellow Rock has either dramatically cutback on its work force or stopped operations generally.  Let me ask it this way: In 2023 roughly how many hours do you think you were in a year were you doing consulting work for Yellow Rock?` |
| FINAL line # | 1215 |
| MB FINAL Q. | `Roughly well, at some point as I understand it in the last 18 months, Yellow Rock has either dramatically cut back on its work force or stopped operations generally. Let me ask it this way: In 2023, roughly how many hours do you think you were in a year were you doing consulting work for Yellow Rock?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 69. idx 695 (parent 694)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `We've been going about an hour and I'll first I didn't tell you this earlier but at any time today you want to take a break just hold your hand up and say can we take a break.  You just can't do it when there is a question pending, okay?  But sometimes I may need a break or somebody else needs a break particularly TJ.  So if this is a good time let's take a short break?` |
| FINAL line # | 1283 |
| MB FINAL Q. | `We've been going about an hour. And I first I didn't tell you this earlier, but at any time today you want to take a break, just hold your hand up and say can we take a break. You just can't do it when there is a question pending, okay? But sometimes I may need a break or somebody else needs a break, particularly TJ. So if this is a good time, let's take a short break.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 70. idx 704 (parent 703)

| Field | Text |
|---|---|
| Rough parent s1 | `All right.` |
| Rough s2 continuation | `Mr. Brandl, we were talking about your work and we jumped ahead to how you're currently doing consulting work and I want to go back and working chronologically through your career.  We were talking about the period from 1999 until late 2004 when you had worked for Aspect Resources then Samedan and then Noble.  And you've told me I think generally about your job as a production foreman overlooking southwest Louisiana, southeast Texas and then at some point you said that you became more focused on suit east Texas and you were the project engineer.  Approximately when was that change?` |
| FINAL line # | 1301 |
| MB FINAL Q. | `Mr. Brandl, we were talking about your work and we jumped ahead to how you're currently doing consulting work. And I want to go back and working chronologically through your career. We were talking about the period from 1999 until late 2004 when you had worked for Aspect Resources, then Samedan and then Noble. And you've told me, I think, generally about your job as a production foreman overlooking Southwest Louisiana, Southeast Texas. And then at some point you said that you became more focused on Southeast, Texas and you were the project engineer. Approximately when was that change?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 71. idx 707 (parent 706)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1305 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 72. idx 714 (parent 713)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And again just generally can you describe for me what was different other than the geography when you moved from being the production foreman to production engineer?` |
| FINAL line # | 1319 |
| MB FINAL Q. | `And again, just generally, can you describe for me what was different other than the geography when you moved from being the production foreman to production engineer?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 73. idx 719 (parent 718)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And did your offers location change once Noble completed the Samedan acquisition or did it stay where it was?` |
| FINAL line # | 1329 |
| MB FINAL Q. | `And did your office location change once Noble completed the Samedan acquisition or did it stay where it was?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 74. idx 726 (parent 725)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `My understanding that's the first time in your career at this point again still 20 years ago, when you had started looking at locations to do workovers an recompletions on?` |
| FINAL line # | 1343 |
| MB FINAL Q. | `And my understanding, that's the first time in your career at this point, again still 20 years ago when you had started looking at locations to do workovers and recompletions on?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 75. idx 729 (parent 728)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1347 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 76. idx 738 (parent 737)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `The recompletion work that we talked about or side tracks as I understand it, is looking to identify new locations beyond the existing perforation is that might produce oil in the wellbore with new perforation is, correct?` |
| FINAL line # | 1367 |
| MB FINAL Q. | `The recompletion work that we talked about or sidetracks as I understand it, is looking to identify new locations beyond the existing perforations that might produce oil in the wellbore with new perforations, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 77. idx 752 (parent 751)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And these folks I think you described them as petroleum geologist the?` |
| FINAL line # | 1399 |
| MB FINAL Q. | `And these folks, I think you described them as petroleum geologists?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 78. idx 768 (parent 767)

| Field | Text |
|---|---|
| Rough parent s1 | `Got it.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1431 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 79. idx 771 (parent 770)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1437 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 80. idx 772 (parent 770)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When you would prepare these AFE'S, obviously one Aspect of that is the cost of doing the recompletion, for example?` |
| FINAL line # | 1439 |
| MB FINAL Q. | `When you would prepare these AFE'S, obviously one aspect of that is the cost of doing the recompletion, for example?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 81. idx 785 (parent 784)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When did you prepare AFE'S for Aspect Resources to do recompletions?` |
| FINAL line # | 1467 |
| MB FINAL Q. | `When did you prepare AFE'S for Aspect Resources to do recompletions?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 82. idx 788 (parent 787)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When do you recall doing your first AFE during the timeframe that you were at Aspect Resources, Aspect Energy, Samedan, Noble?` |
| FINAL line # | 1473 |
| MB FINAL Q. | `When do you recall doing your first AFE during the timeframe that you were at Aspect Resources, Aspect Energy, Samedan, Noble?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 83. idx 793 (parent 792)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And when you prepared your first AFE for was it for a recompletion as best you can recall?` |
| FINAL line # | 1483 |
| MB FINAL Q. | `And when you prepared your first AFE for was it for a recompletion as best you can recall?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 84. idx 800 (parent 799)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1497 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 85. idx 812 (parent 811)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And again it's company and you go to them and say let's step back.  A recompletions usually an issue because whatever production was taking place in the existing original perforation is has reached its end of life so to speak, it's petered out?` |
| FINAL line # | 1519 |
| MB FINAL Q. | `And again, it's a company and you go to them and say let's step back. A recompletion is usually an issue because whatever production was taking place in the existing original perforations has reached its end of life so to speak, it's petered out?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 86. idx 817 (parent 816)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And when you put together an AFE you're saying to your bosses, hey to get an appropriate drilling apparatus out there, to go back down, place the plug, seal off the old perforation is, drill the new ones it's going to cost "X" being correct that's part of what you were putting together?` |
| FINAL line # | 1529 |
| MB FINAL Q. | `And when you put together an AFE, you're saying to your bosses, hey, to get an appropriate drilling apparatus out there, to go back down, place the plug, seal off the old perforations, drill the new ones, it's going to cost "X", correct? That's part of what you were putting together?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 87. idx 822 (parent 821)

| Field | Text |
|---|---|
| Rough parent s1 | `And in that timeframe did you have a sense of what their return was being targeted at?  And I want to make sure you understand that question.  In fact, let me start over.  Let me give you an example if I could.` |
| Rough s2 continuation | `Let's say you put together the cost to do a recompletion on a given well, and the estimated cost was $100,000, okay is that out of whack or?` |
| FINAL line # | 1539 |
| MB FINAL Q. | `Let's say you put together the cost to do a recompletion on a given well, and the estimated cost was $100,000, okay? Is that out of whack or?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 88. idx 827 (parent 826)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And your going to your bosses and saying my proposal here is we're going to spend $50,000.  Did you have a sense of return they would be expecting to get back?  I mean obviously let's step back. *REPORTER CHECK HERE* there's only $20,000 worth of revenue in this other location, you wouldn't have even proposed it, right?` |
| FINAL line # | 1549 |
| MB FINAL Q. | `And you are going to your bosses to say my proposal here is we're going to spend $50,000. Did you have a sense of return they would be expecting to get back? I mean obviously let's step back. If you were saying you wouldn't do this hey, I only think there's $20,000 worth of revenue in this other location, you wouldn't have even proposed it, right?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 89%) |

### 89. idx 850 (parent 849)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1595 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 90. idx 855 (parent 854)

| Field | Text |
|---|---|
| Rough parent s1 | `I'll go to Samedan and *REPORTER CHECK HERE* in a moment because I suspected that might be different but I want to make sure we're talk you go about the economics because this is going to come up a lot today.` |
| Rough s2 continuation | `At Ballard and the example we used $50,000 as the cost in the AFE, Mr. Ballard's expectation would be to get 200,000 back, correct?` |
| FINAL line # | 1607 |
| MB FINAL Q. | `At Ballard, and the example we used was $50,000 as the cost in the AFE, Mr. Ballard's expectation would be to get $200,000 back, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 91. idx 864 (parent 863)

| Field | Text |
|---|---|
| Rough parent s1 | `Fair enough.` |
| Rough s2 continuation | `*REPORTER CHECK HERE* was the volume of oil or gas that location would produce and he made a decision or an assumption about what the price of that oil or gas would be.  He multiplied those and he may have made an adjustment for present value.  He deducted 25 percent for royalties an that was his number?` |
| FINAL line # | 1625 |
| MB FINAL Q. | `And I'm sensing he was then, as you understood it, looking at what he thought was the volume of oil or gas that location would produce, he made a decision or an assumption about what the price of that oil or gas would be. He multiplied those and he may have made an adjustment for present value. He deducted 25 percent for royalties and that was his number?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 86%) |

### 92. idx 868 (parent 867)

| Field | Text |
|---|---|
| Rough parent s1 | `Go ahead.  I know we've been going for a bit no, I'll keep going.  I'm just going to have to go to the bathroom in about the next 15 minutes, sorry.` |
| Rough s2 continuation | `Let's talk about at Samedan and Noble.  Can we use the same starting point of 50,000 in the AFE for the example?` |
| FINAL line # | 1635 |
| MB FINAL Q. | `Let's talk about at Samedan and Noble. Can we use the same starting point of 50,000 in the AFE for the example?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 93. idx 873 (parent 872)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `If we used the 50,000 number that you would have put together in the AFE what did you understand let's step back I'm not trying to ask you to guess.  But when you were doing this for job for Samedan and Noble, you had a general understanding because you needed to understand what they were looking for in return so you could understand whether when you ran up the numbers was this a location that made sensor not, right?` |
| FINAL line # | 1645 |
| MB FINAL Q. | `If we used the 50,000 number that you would have put together in the AFE, what did you understand let's step back. I'm not trying to ask you to guess. But when you were doing this job for Samedan and Noble, you had a general understanding because you needed to understand what they were looking for in return so you could understand whether when you ran up the numbers, was this a location that made sense or not, right?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 94. idx 878 (parent 877)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So again going back T my example you're put together an AFE for Samedan or Noble and the cost for doing the recompletions $50,000 by your calculation.  What did you understand base on your action with the other experts what the return needed to be in order to get that proved?` |
| FINAL line # | 1655 |
| MB FINAL Q. | `So again going back to my example, you're putting together an AFE for Samedan or Noble and the cost for doing the recompletion is $50,000 by your calculation. What did you understand based on your action with the other experts what the return needed to be in order to get that approved?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 95. idx 931 (parent 930)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Mr. Cranburg also owned Aspect Resources which had 50 percent of the interest in the production assets that were sold to Samedan and then Noble, correct?` |
| FINAL line # | 1769 |
| MB FINAL Q. | `Mr. Cranberg also owned Aspect Resources which had 50 percent of the interest in the production assets that were sold to Samedan and then Noble, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 96. idx 938 (parent 937)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Was your work as a production manager limited to overseeing production assets that were within Aspect Energy?` |
| FINAL line # | 1783 |
| MB FINAL Q. | `Was your work as a production manager limited to overseeing production assets that were within Aspect Energy?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 97. idx 943 (parent 942)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And again something you and I both know but we need to make sure we're clear with the jury some day.  In Louisiana and in Texas at any given time an oil and gas well has a designated operator, correct?` |
| FINAL line # | 1793 |
| MB FINAL Q. | `And again, something you and I both know, but we need to make sure we're clear with the jury some day. In Louisiana and in Texas at any given time an oil and gas well has a designated operator, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 98. idx 954 (parent 953)

| Field | Text |
|---|---|
| Rough parent s1 | `It was the operator?  Okay.` |
| Rough s2 continuation | `Generally speaking, where were these assets located?` |
| FINAL line # | 1817 |
| MB FINAL Q. | `And generally speaking, where were these assets located?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 99. idx 961 (parent 960)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 1829 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 100. idx 962 (parent 960)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And were these generally speaking existing producing assets that Aspect Energy an Mr. Cranburg acquired or were they I think the word you used exploratory?` |
| FINAL line # | 1831 |
| MB FINAL Q. | `And were these, generally speaking, existing producing assets that Aspect Energy and Mr. Cranberg acquired or were they I think the word you used was exploratory?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 101. idx 965 (parent 964)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was your role in connection with those assets as production manager?` |
| FINAL line # | 1837 |
| MB FINAL Q. | `And what was your role in connection with those assets as production manager?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 102. idx 974 (parent 973)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And roughly how many during that yearandahalf you were there, how many boat end of the job, how many wells were you overseeing?` |
| FINAL line # | 1855 |
| MB FINAL Q. | `And roughly how many during that yearandahalf you were there, how many by the end of the job, how many wells were you overseeing?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 103. idx 987 (parent 986)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What was different, if anything, about the job that you had as production manager or for Aspect Energy from 2005 through some part of 2006 as compared to your duties when you had been at Samedan and Noble other than the location of the wells?` |
| FINAL line # | 1881 |
| MB FINAL Q. | `What was different, if anything, about the job that you had as production manager for Aspect Energy from 2005 through some part of 2006, as compared to your duties when you had been at Samedan and Noble other than the location of the wells?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 104. idx 991 (parent 990)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Where did you go after Aspect Energy?` |
| FINAL line # | 1887 |
| MB FINAL Q. | `Where did you go after Aspect Energy?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 105. idx 1004 (parent 1003)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was your position?` |
| FINAL line # | 1913 |
| MB FINAL Q. | `And what was your position?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 106. idx 1013 (parent 1012)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Smaller company?` |
| FINAL line # | 1931 |
| MB FINAL Q. | `Smaller company?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 107. idx 1018 (parent 1017)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did you have was it like Ballard where the guy who ran the show was your boss?` |
| FINAL line # | 1941 |
| MB FINAL Q. | `Did you have was it like Ballard where the guy who ran the show was your boss?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 108. idx 1021 (parent 1020)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And did he do his own economics or you supply them to him or did others?` |
| FINAL line # | 1947 |
| MB FINAL Q. | `And did he do his own economics or you supplied them to him or did others?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 109. idx 1024 (parent 1023)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I should ask who was the owner?` |
| FINAL line # | 1953 |
| MB FINAL Q. | `I should ask who was the owner?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 110. idx 1039 (parent 1038)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And so you did did youall part ways amicably?` |
| FINAL line # | 1983 |
| MB FINAL Q. | `And so you did did youall part ways amicably?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 111. idx 1044 (parent 1043)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Why did you leave Louisiana Gas Development Corporation in 2007?` |
| FINAL line # | 1993 |
| MB FINAL Q. | `Why did you leave Louisiana Gas Development Corporation in 2007?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 112. idx 1062 (parent 1061)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I'm sensing what you were about to tell me but please correct me if I'm wrong, but from mid 2007 weight hold O you told me.  So mid 2007 when you moved and left Shreveport an you went to where, back to Houston?` |
| FINAL line # | 2033 |
| MB FINAL Q. | `So I'm sensing what you were about to tell me, but please correct me if I'm wrong, so from mid2007 when you left wait. Hold on. You told me. So mid2007 when you moved and left Shreveport and you went to where, back to Houston?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 93%) |

### 113. idx 1069 (parent 1068)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And approximately how many different companies would that have been?` |
| FINAL line # | 2047 |
| MB FINAL Q. | `And approximately how many different companies would that have been?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 114. idx 1072 (parent 1071)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Who were those?` |
| FINAL line # | 2053 |
| MB FINAL Q. | `Who were those?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 115. idx 1087 (parent 1086)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 2069 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 116. idx 1120 (parent 1119)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `In 2011, you left El Paso and went to work for interest er investigate, corrects?` |
| FINAL line # | 2159 |
| MB FINAL Q. | `In 2011, you left El Paso and went to work for Intervest, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 90%) |

### 117. idx 1146 (parent 1145)

| Field | Text |
|---|---|
| Rough parent s1 | `And ended as senior completion engineer [knowledge\|acknowledge] [know\|no] senior completion manage SFLER senior completion manager.  Sorry that's what happens when I look away.` |
| Rough s2 continuation | `Okay.  What generally speaking, you were working in Houston?` |
| FINAL line # | 2219 |
| MB FINAL Q. | `And what, generally speaking you were working in Houston?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 93%) |

### 118. idx 1153 (parent 1152)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `It was it is located knead east Texas?` |
| FINAL line # | 2233 |
| MB FINAL Q. | `It was it is located in East Texas?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 93%) |

### 119. idx 1178 (parent 1177)

| Field | Text |
|---|---|
| Rough parent s1 | `Why did you leave [owe\|oh] [weight\|wait], sorry.` |
| Rough s2 continuation | `How did your job change at interest er investigate when you became senior completion manager?` |
| FINAL line # | 2283 |
| MB FINAL Q. | `How did your job change at Intervest when you became senior completion manager?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 92%) |

### 120. idx 1197 (parent 1196)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And so it says here here that you formed fer Rick's in October 2007; is that correct to the best of your recollection?` |
| FINAL line # | 2325 |
| MB FINAL Q. | `And so it says here that you formed Frerichs in October 2007; is that correct to the best of your recollection?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 95%) |

### 121. idx 1208 (parent 1207)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And jumping ahead, your next well, let's step back.  So from 2013 at some point after 2013 did you start doing more contract work?` |
| FINAL line # | 2351 |
| MB FINAL Q. | `And jumping ahead, your next well, let's step back. So from 2013. At some point after 2013 did you start doing more contract work?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 122. idx 1215 (parent 1214)

| Field | Text |
|---|---|
| Rough parent s1 | `Thank you.` |
| Rough s2 continuation | `And you weren't doing any contracting consulting work during that period?` |
| FINAL line # | 2365 |
| MB FINAL Q. | `And you weren't doing any contracting consulting work during that period?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 123. idx 1218 (parent 1217)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You were enjoying the fruits of your investment in oil and goods production and fer Rick's?` |
| FINAL line # | 2371 |
| MB FINAL Q. | `You were enjoying the fruits of your investment in oil and gas production and Frerichs?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 124. idx 1225 (parent 1224)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I have to ask: Did you and he make piece?` |
| FINAL line # | 2385 |
| MB FINAL Q. | `I have to ask: Did you and he make peace?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 125. idx 1232 (parent 1231)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 2389 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 126. idx 1235 (parent 1234)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So how did you come to work again for Mr. Cranburg?` |
| FINAL line # | 2399 |
| MB FINAL Q. | `(not present as Q. in FINAL)` |
| **Status** | **NOT STANDALONE (absent from FINAL region)** (sim 0%) |

### 127. idx 1239 (parent 1238)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `But they then in 2017 wanted to do more east Texas drilling?` |
| FINAL line # | 2421 |
| MB FINAL Q. | `But they then in 2017 wanted to do more East Texas drilling?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 128. idx 1248 (parent 1247)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So starting we're about to get to the period of time that you also whacked for Yellow Rock, correct?` |
| FINAL line # | 2439 |
| MB FINAL Q. | `So starting because we're about to get to the period of time that you also worked for Yellow Rock, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 129. idx 1254 (parent 1253)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Okay.` |
| FINAL line # | 2467 |
| MB FINAL Q. | `Okay.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 130. idx 1255 (parent 1253)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `During the period do you recall specifically what time what month in 2018 you began starting work for Yellow Rock?` |
| FINAL line # | 2479 |
| MB FINAL Q. | `And since 2024 to the present, your main contract work has been for Yellow Rock?` |
| **Status** | **AMBIGUOUS (sim 45%, text len 114)** (sim 45%) |

### 131. idx 1274 (parent 1273)

| Field | Text |
|---|---|
| Rough parent s1 | `I've killed too many of those in my life.  Okay.` |
| Rough s2 continuation | `I'm just curious looking at Exhibit No. 221, Yellow Rock is not identified on here.  Is there a reason for that?` |
| FINAL line # | 2497 |
| MB FINAL Q. | `I'm just curious. Looking at Exhibit No. 221, Yellow Rock is not identified on here. Is there a reason for that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 132. idx 1277 (parent 1276)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  All right.` |
| Rough s2 continuation | `How did you come to work for Yellow Rock?` |
| FINAL line # | 2503 |
| MB FINAL Q. | `How did you come to work for Yellow Rock?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 133. idx 1285 (parent 1284)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What do you recall did she hire you or did you have to go talk to somebody else?` |
| FINAL line # | 2521 |
| MB FINAL Q. | `What do you recall did she hire you or did you have to go talk to somebody else?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 134. idx 1288 (parent 1287)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And at this initial meeting with her, was it let me ask it this way: When did you first become aware of an opportunity work at what is known as the Sulphur Mines Field?` |
| FINAL line # | 2527 |
| MB FINAL Q. | `And at this initial meeting with her, was it let me ask it this way: When did you first become aware of an opportunity work at what is known as the Sulphur Mines Field?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 135. idx 1307 (parent 1306)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When you came to work in April 2018 for Yellow Rock, who did you have a sense who was the person in charge?` |
| FINAL line # | 2567 |
| MB FINAL Q. | `When you came to work in April 2018 for Yellow Rock, who did you have a sense who was the person in charge?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 136. idx 1314 (parent 1313)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I have marked an put in front of you Exhibit No. 222, which is a document that's been produced to me, Yellow Rock 94323 on '02 and is titled White Top Energy, LLC functional organization chart.  Did I describe that correctly?` |
| FINAL line # | 2581 |
| MB FINAL Q. | `I have marked and put in front of you Exhibit No. 222, which is a document that's been produced to me, Yellow Rock 323002. And is titled "White Top Energy, LLC Functional Organization Chart".` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 90%) |

### 137. idx 1321 (parent 1320)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 2595 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 138. idx 1330 (parent 1329)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 2619 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 139. idx 1333 (parent 1332)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And the first time I met William Green was in probably the second quarter of 2019.` |
| FINAL line # | 2623 |
| MB FINAL Q. | `(not present as Q. in FINAL)` |
| **Status** | **NOT STANDALONE (absent from FINAL region)** (sim 0%) |

### 140. idx 1335 (parent 1334)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Who did you we're going to go talk in a moment or probably after lunch, a good bit about your job responsibilities.  But when you came to work in January 2018, who did you plans ly interact with on this chart?` |
| FINAL line # | 2629 |
| MB FINAL Q. | `Who did you we're going to go talk in a moment or probably after lunch, a good bit about your job responsibilities. But when you came to work in January 2018, who did you presently interact with on this chart?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 141. idx 1340 (parent 1339)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I want to go briefly to the top of the chart.  It's called the White Top energy LLC chart.  Let's talk about some corporate names before we get too confused.  We talked earlier there is a company called Yellow Rock that becomes that is the operator of the wells at Sulphur Mines Field, correct?` |
| FINAL line # | 2639 |
| MB FINAL Q. | `I want to go briefly to the top of the chart. It's called the "White Top Energy, LLC Functional Organization Chart". Let's talk about some corporate names before we get too confused. We talked earlier there is a company called Yellow Rock that becomes that is the operator of the wells at Sulphur Mines Field, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 142. idx 1347 (parent 1346)

| Field | Text |
|---|---|
| Rough parent s1 | `I didn't ask that very well.  Sorry.  Let me step back.` |
| Rough s2 continuation | `I would just represent to you that Yellow Rock was formed in roughly 2003 as a rule [by\|buy] Mr. Bertelot and Mr. Cox.  And they operated it, that company, and oversaw the development of the field at Sulphur Mines until approximately late 2018 as I understand it.  Does that sound about right?` |
| FINAL line # | 2653 |
| MB FINAL Q. | `I would just represent to you that Yellow Rock was formed in roughly 2003 as I recall by Mr. Bertelot and Mr. Cox. And they operated it, that company, and oversaw the development of the field at Sulphur Mines until approximately late 2018 as I understand it. Does that sound about right?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 143. idx 1381 (parent 1380)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What I'm trying to understand is if it's consistent with what you recall is, when you first came to work for Yellow Rock well for Patricia Henderson in 2018, Yellow Rock was not the operator at Sulphur Mines at that point, correct?` |
| FINAL line # | 2719 |
| MB FINAL Q. | `What I'm trying to understand is if it's consistent with what you recall is, when you first came to work for Yellow Rock well, for Patricia Henderson in 2018, Yellow Rock was not the operator at Sulphur Mines at that point, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 144. idx 1414 (parent 1413)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 2727 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 145. idx 1449 (parent 1448)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you well, Mr. French goes by the way side, correct?` |
| FINAL line # | 2873 |
| MB FINAL Q. | `Can you well, Mr. French goes by the wayside, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 146. idx 1465 (parent 1464)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Mr. green?` |
| FINAL line # | 2909 |
| MB FINAL Q. | `Mr. Green?` |
| **Status** | **AMBIGUOUS (sim 100%, text len 10)** (sim 100%) |

### 147. idx 1478 (parent 1477)

| Field | Text |
|---|---|
| Rough parent s1 | `All right.` |
| Rough s2 continuation | `And in terms of his role as senior VP would Mr. Easley have left that position in late 2021?` |
| FINAL line # | 2935 |
| MB FINAL Q. | `And in terms of his role as senior VP, would Mr. Easley have left that position in late 2021?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 148. idx 1481 (parent 1480)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you put late 2021 by him in that position.` |
| FINAL line # | 2941 |
| MB FINAL Q. | `Can you put late 2021 by him in that position.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 149. idx 1482 (parent 1480)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Now and then we'll move on, are there any names on this list excuse me that's not right.` |
| FINAL line # | 2943 |
| MB FINAL Q. | `Now, and then we'll move on, are there any names on this list excuse me. That's not right.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 150. idx 1483 (parent 1480)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `In the period leading up to and before the transition to 3.0 in late 2021, were there any other folks specifically in geoscience or operations who were working for Yellow Rock who were not listed here?` |
| FINAL line # | 2945 |
| MB FINAL Q. | `In the period leading up to and before the transition to 3.0 in late 2021, were there any other folks specifically in "Geoscience" or "Operations" who were working for Yellow Rock who were not listed here?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 151. idx 1498 (parent 1497)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And he would have been there from roughly when to when?` |
| FINAL line # | 2977 |
| MB FINAL Q. | `And he would have been there from roughly when to when?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 152. idx 1501 (parent 1500)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Remind me next to Mr. Metcalf we were 20, what?` |
| FINAL line # | 2983 |
| MB FINAL Q. | `Remind me, next to Mr. Metcalf you wrote 20what?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 88%) |

### 153. idx 1508 (parent 1507)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Would he were talking about other people in geo *REPORTER CHECK HERE* who are not listed here.  You've given me a number of names are there any others?` |
| FINAL line # | 2997 |
| MB FINAL Q. | `We were talking about other people in "Geoscience" or "Operations" who worked that are not listed here. You've given me a number of names. Are there any others?` |
| **Status** | **AMBIGUOUS (sim 82%, text len 151)** (sim 82%) |

### 154. idx 1511 (parent 1510)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And he lives in Baton Rouge and was he was doing he was helping her out on the geology side?` |
| FINAL line # | 3001 |
| MB FINAL Q. | `(not present as Q. in FINAL)` |
| **Status** | **NOT STANDALONE (absent from FINAL region)** (sim 0%) |

### 155. idx 1513 (parent 1512)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I don't remember the name.  I think it's somebody named Judy who helped with permitting.  Does that ring a bell?` |
| FINAL line # | 3007 |
| MB FINAL Q. | `I don't remember the name. I think it's somebody named Judy who helped with permitting. Does that ring a bell?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 156. idx 1522 (parent 1521)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 3023 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 157. idx 1533 (parent 1532)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay, that's fine. /lost my train of thought.  Hang O.` |
| Rough s2 continuation | `When you first came to work to do work involving Sulphur Mines, was there somebody that you were reporting to?  And this was in I think you told me April of 2019.` |
| FINAL line # | 3047 |
| MB FINAL Q. | `When you first came to work to do work involving Sulphur Mines, was there somebody that you were reporting to? And this was in I think you told me April of 2019.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 158. idx 1536 (parent 1535)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 3051 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 159. idx 1539 (parent 1538)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And at some point around that time or shortly thereafter, Yellow Rock become the operator in the field?` |
| FINAL line # | 3057 |
| MB FINAL Q. | `And at some point around that time or shortly thereafter, Yellow Rock become the operator in the field?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 160. idx 1548 (parent 1547)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And did that remain during the period of 2.0, Yellow Rock 2.0, how did your who did you principally how did the people that you interacted with regularly changeover that period of time if at all?` |
| FINAL line # | 3075 |
| MB FINAL Q. | `And did that remain during the period of 2.0, Yellow Rock 2.0, how did your who did you principally how did the people that you interacted with regularly change over that period of time, if at all?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 161. idx 1559 (parent 1558)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 3095 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 162. idx 1581 (parent 1580)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And some of those go way back in time to Burlington and some of them were done by Yellow Rock 1.0?` |
| FINAL line # | 3139 |
| MB FINAL Q. | `And some of those go way back in time to Burlington and some of them were done by Yellow Rock 1.0?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 163. idx 1586 (parent 1585)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `At this point in 2020, Yellow Rock while you were there had drilled a few new wells, correct?` |
| FINAL line # | 3149 |
| MB FINAL Q. | `At this point in 2020, Yellow Rock, while you were there, had drilled a few new wells, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 164. idx 1589 (parent 1588)

| Field | Text |
|---|---|
| Rough parent s1 | `Let's just make sure you and I are on the same page because I can't remember it so I'm having trouble.` |
| Rough s2 continuation | `That would have been the hold on it the print is not big.  I don't know why I can't read this.  Sorry.  Hold O oh here we go.  Sorry I I was looking at wrong placement.` |
| FINAL line # | 3155 |
| MB FINAL Q. | `That would have been the hold on it the print is not big. I don't know why I can't read this. Sorry. Hold on. Oh, here we go. Sorry, I was looking at the wrong place.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 165. idx 1590 (parent 1588)

| Field | Text |
|---|---|
| Rough parent s1 | `Let's just make sure you and I are on the same page because I can't remember it so I'm having trouble.` |
| Rough s2 continuation | `The one on 27, the 1028, 1029 and the 1030; is that correct?` |
| FINAL line # | 3157 |
| MB FINAL Q. | `The 1027, the 1028, 1029 and the 1030; is that correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 92%) |

### 166. idx 1597 (parent 1596)

| Field | Text |
|---|---|
| Rough parent s1 | `Sorry.  I didn't say that right.  I don't think I did.` |
| Rough s2 continuation | `I'm again if you can't remember the dates you're free to tell me I can't remember exactly.  I'm showing the 1028 was drilled initially in May and June of 2019.` |
| FINAL line # | 3171 |
| MB FINAL Q. | `I'm again, if you can't remember the dates, you're free to tell me I can't remember exactly. I'm showing the 1028 was drilled initially in May and June of 2019.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 167. idx 1602 (parent 1601)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And then was there a subsequent sidetrack of the 1028?` |
| FINAL line # | 3181 |
| MB FINAL Q. | `And then was there a subsequent sidetrack of the 1028?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 168. idx 1623 (parent 1622)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And do you recall we talked about the four new wells and they were all done in 2019, correct?` |
| FINAL line # | 3225 |
| MB FINAL Q. | `And do you recall we talked about the four new wells and they were all done in 2019, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 169. idx 1650 (parent 1649)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Are there any others that you recall in 2020 during the height of COVID?` |
| FINAL line # | 3277 |
| MB FINAL Q. | `Are there any others that you recall in 2020 during the height of COVID?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 170. idx 1665 (parent 1664)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `We'll talk later.  There was some further work particularly I think no we'll get to that.  There was some further work done on some of those but that's still I think was in early 2020 before COVID.  I'm showing some recompletions on the 1030 and the 1029 in early 2020.` |
| FINAL line # | 3311 |
| MB FINAL Q. | `There was some further work done on some of those, but that's still I think, was in early 2020 before COVID. I'm showing some recompletions on the 1030 and the 1029 in early 2020.` |
| **Status** | **AMBIGUOUS (sim 80%, text len 269)** (sim 80%) |

### 171. idx 1726 (parent 1725)

| Field | Text |
|---|---|
| Rough parent s1 | `When you came to work as an independent contractor, did you have a company E-mail let me start over.` |
| Rough s2 continuation | `Did you ever have a company E-mail address at Yellow Rock?` |
| FINAL line # | 3425 |
| MB FINAL Q. | `Did you ever have a company Email address at Yellow Rock?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 172. idx 1729 (parent 1728)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what is that E-mail address?` |
| FINAL line # | 3431 |
| MB FINAL Q. | `And what is that Email address?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 173. idx 1757 (parent 1756)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you tell me the name of that vendor?` |
| FINAL line # | 3491 |
| MB FINAL Q. | `Can you tell me the name of that vendor.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 174. idx 1764 (parent 1763)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 3501 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 175. idx 1774 (parent 1773)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And do you have a rough idea in terms of when you populated that at Yellow Rock folder, whether it had dozens, hundreds, thousands of E-mails in it?` |
| FINAL line # | 3525 |
| MB FINAL Q. | `And do you have a rough idea in terms of when you populated that at Yellow Rock folder, whether it had dozens, hundreds, thousands of Emails in it?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 176. idx 1779 (parent 1778)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What was your what was your rate of compensation when you started working for Yellow Rock, do you recall?` |
| FINAL line # | 3535 |
| MB FINAL Q. | `What was your what was your rate of compensation when you started working for Yellow Rock, do you recall?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 177. idx 1786 (parent 1785)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And do you create that invoice or do you have somebody who helps you with that?` |
| FINAL line # | 3551 |
| MB FINAL Q. | `And do you create that invoice or do you have somebody who helps you with that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 178. idx 1789 (parent 1788)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And would those be in the E-mail you provided as best you would know?  I'm only asking because I saw a few but I didn't see a comprehensive set but I could have missed it.` |
| FINAL line # | 3557 |
| MB FINAL Q. | `And would those be in the Email you provided as best you would know? I'm only asking because I saw a few, but I didn't see a comprehensive set, but I could have missed it.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 179. idx 1804 (parent 1803)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And is this how you would have normally kept your time sheet, the second page, you would have a description and a number of hours by day in a given month on the invoice?` |
| FINAL line # | 3591 |
| MB FINAL Q. | `And is this how you would have normally kept your timesheet, the second page, you would have a description and a number of hours by day in a given month on the invoice?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 180. idx 1807 (parent 1806)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 3595 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 181. idx 1814 (parent 1813)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I'm just trying to make sure.  Was that agreement kept?` |
| FINAL line # | 3609 |
| MB FINAL Q. | `And I'm just trying to make sure. Was that agreement kept?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 182. idx 1827 (parent 1826)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 3635 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 183. idx 1828 (parent 1826)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `But in the initial period of Yellow Rock 943 point on until early 2025 you just got paid monthly $8,00080033?` |
| FINAL line # | 3637 |
| MB FINAL Q. | `But in the initial period of Yellow Rock 3.0 until early 2025, you just got paid monthly $8,833?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 91%) |

### 184. idx 1833 (parent 1832)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Just so I understand that was the gross amount that you were paid as an independent contractor.  They weren't with all the taxes an Social Security that was all on you as an independent contractor?` |
| FINAL line # | 3647 |
| MB FINAL Q. | `Just so I understand, that was the gross amount that you were paid as an independent contractor. They weren't with all the taxes and Social Security, that was all on you as an independent contractor?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 185. idx 1836 (parent 1835)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `All right.` |
| FINAL line # | 3677 |
| MB FINAL Q. | `All right.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 186. idx 1837 (parent 1835)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `.  Do you have a sense of how much money you've been paid by Yellow Rock or it's affiliates in total approximately for the work you've done at Sulphur Mines?` |
| FINAL line # | 3741 |
| MB FINAL Q. | `And who would have performed the reserve analysis in connection with each of those workover counts?` |
| **Status** | **AMBIGUOUS (sim 38%, text len 157)** (sim 38%) |

### 187. idx 1842 (parent 1841)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Okay.` |
| FINAL line # | 4033 |
| MB FINAL Q. | `Okay.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 188. idx 1843 (parent 1841)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did your role and job responsibilities at Yellow Rock stay pretty condition cyst tent over the time period that you worked there or did they vary meaning flea depending on the timeframe?` |
| FINAL line # | 4035 |
| MB FINAL Q. | `You described this is one of the issues when petroleum engineers talk about shallow and deep is, you, I thought said, the 1031 had been planned in part to target the top two zones.` |
| **Status** | **AMBIGUOUS (sim 27%, text len 186)** (sim 27%) |

### 189. idx 1846 (parent 1845)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `How would you describe the portion of your responsibilities that you had at Yellow Rock that remained largely unchanged over time that you worked there?` |
| FINAL line # | 4049 |
| MB FINAL Q. | `And then you said you first did a recompletion in the first zone. And I'm trying to understand. This is where things get confusing. You meant the second from the top?` |
| **Status** | **AMBIGUOUS (sim 31%, text len 152)** (sim 31%) |

### 190. idx 1851 (parent 1850)

| Field | Text |
|---|---|
| Rough parent s1 | `All right.` |
| Rough s2 continuation | `And we talked about this at some of your prior jobs.  I'll ask it here.  Were you involved in making decision about which wells upon which to do workovers or I'll ask that question first.  For the wells that youall decided to do workovers on, was that decision made unilaterally by you or did it involve others?` |
| FINAL line # | 4043 |
| MB FINAL Q. | `When you said "top two zones", were you meaning top in terms of shallow shallowest, or did you mean most top like our favorites?` |
| **Status** | **AMBIGUOUS (sim 29%, text len 311)** (sim 29%) |

### 191. idx 1864 (parent 1863)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what is his job title, area of responsibility, area of expertise?` |
| FINAL line # | 4077 |
| MB FINAL Q. | `You said the "bridge plug". Is this now to go test the top shallowest zone or are you still in the second from the top?` |
| **Status** | **AMBIGUOUS (sim 36%, text len 69)** (sim 36%) |

### 192. idx 1872 (parent 1871)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `During that period did he report to you?` |
| FINAL line # | 4065 |
| MB FINAL Q. | `Just so I understand, the bottom, not the very bottom?` |
| **Status** | **AMBIGUOUS (sim 36%, text len 40)** (sim 36%) |

### 193. idx 1875 (parent 1874)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Okay.  Have we covered how it work with the team you were describe to go me the participants in the team effort overseeing workovers and completion is.  What we were just talking about workovers in 2020.  No, sorry.` |
| FINAL line # | 4077 |
| MB FINAL Q. | `You said the "bridge plug". Is this now to go test the top shallowest zone or are you still in the second from the top?` |
| **Status** | **AMBIGUOUS (sim 32%, text len 215)** (sim 32%) |

### 194. idx 1876 (parent 1874)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You were describing to me the team efforts for workovers in two point on and you said there weren't any workovers in 2020 that you recall and post COVID there were and that team was client Kip key and *REPORTER CHECK HERE* was there anybody else involved in 2.0 and myself?` |
| FINAL line # | 4061 |
| MB FINAL Q. | `I'm sorry, you said "two wells". I don't think you meant two wells.` |
| **Status** | **AMBIGUOUS (sim 26%, text len 273)** (sim 26%) |

### 195. idx 1895 (parent 1894)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `In 2019 Yellow Rock undertook to drilling and early 2020 to drilling of four new wells.  We talk about that?` |
| FINAL line # | 4065 |
| MB FINAL Q. | `Just so I understand, the bottom, not the very bottom?` |
| **Status** | **AMBIGUOUS (sim 30%, text len 108)** (sim 30%) |

### 196. idx 1910 (parent 1909)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did you use any type of software to do your reserve analyses for Sulphur Mines?` |
| FINAL line # | 4061 |
| MB FINAL Q. | `I'm sorry, you said "two wells". I don't think you meant two wells.` |
| **Status** | **AMBIGUOUS (sim 34%, text len 79)** (sim 34%) |

### 197. idx 1925 (parent 1924)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | ? |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 198. idx 1943 (parent 1942)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | ? |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 199. idx 1986 (parent 1985)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `But that well was permitted and you could have drilled it correct?` |
| FINAL line # | 4061 |
| MB FINAL Q. | `I'm sorry, you said "two wells". I don't think you meant two wells.` |
| **Status** | **AMBIGUOUS (sim 32%, text len 66)** (sim 32%) |

### 200. idx 2022 (parent 2021)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | ? |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 201. idx 2046 (parent 2045)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay that's what I want to make sure.` |
| Rough s2 continuation | `What did the provided to the stat [by\|buy] Yellow Rock show the level of chlorides in the 109431 well, an I'll get to a moment what formation it was?` |
| FINAL line # | 4077 |
| MB FINAL Q. | `You said the "bridge plug". Is this now to go test the top shallowest zone or are you still in the second from the top?` |
| **Status** | **AMBIGUOUS (sim 36%, text len 149)** (sim 36%) |

### 202. idx 2053 (parent 2052)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You described this is one of the issues when petroleum engineers talk about shallow an deep is you I thought said the 109431 had been planned in part to target the top two zones, do you remember that?` |
| FINAL line # | 4077 |
| MB FINAL Q. | `You said the "bridge plug". Is this now to go test the top shallowest zone or are you still in the second from the top?` |
| **Status** | **AMBIGUOUS (sim 34%, text len 200)** (sim 34%) |

### 203. idx 2056 (parent 2055)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When you said top two zones, were you meaning top in terms of shallow shallow he is, or did you mean most top like our favorites?` |
| FINAL line # | 4043 |
| MB FINAL Q. | `When you said "top two zones", were you meaning top in terms of shallow shallowest, or did you mean most top like our favorites?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 204. idx 2079 (parent 2078)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 4081 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 205. idx 2087 (parent 2086)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 4085 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 206. idx 2092 (parent 2091)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you help me understand in this particular well in the 109431, the bottom two, the deepest of the two, formation goes that you talked about that were tight in the 109431 Well, were they in a particular formation?` |
| FINAL line # | 4093 |
| MB FINAL Q. | `Did you end up taking those two samples from your memory from one of each of the shallowest and next shallowest layers or were all of those samples taken from one of the layers?` |
| **Status** | **AMBIGUOUS (sim 29%, text len 215)** (sim 29%) |

### 207. idx 2095 (parent 2094)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `That's what I was looking for?` |
| FINAL line # | 4117 |
| MB FINAL Q. | `Okay, that's what I was looking for.` |
| **Status** | **AMBIGUOUS (sim 88%, text len 30)** (sim 88%) |

### 208. idx 2100 (parent 2099)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what was the depth of the shallow you talked about the two shallow zones.  What was the top of that in terms of depth?` |
| FINAL line # | 4125 |
| MB FINAL Q. | `And what was the depth of the shallow you talked about the two shallow zones. What was the top of that in terms of depth?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 209. idx 2103 (parent 2102)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So the depth range that y'all were focused on in your drilling plan was on five Formations spank the depth of 3,600 to 4,000 feet approximately?` |
| FINAL line # | 4131 |
| MB FINAL Q. | `So the depth range that y'all were focused on in your drilling plan was on five formations spanning the depth of 3,600 to 4,000 feet approximately?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 210. idx 2106 (parent 2105)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I'm shot sure I let you finish your explanation because we talked about the chloride.  How is it that you believe that Westlake has responsibility for the level of correspondence rides that were detected by check check in the 109431 *REPORTER CHECK HERE*?` |
| FINAL line # | 4137 |
| MB FINAL Q. | `I'm not sure I let you finish your explanation because we've talked about the chlorides. How is it that you believe that Westlake bears responsibility for the level of chlorides that were detected by Yellow Rock in the shallowest two formations in the 1031 well?` |
| **Status** | **AMBIGUOUS (sim 81%, text len 255)** (sim 81%) |

### 211. idx 2131 (parent 2130)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Any experience on salt domes other than Sulphur Mines we've already covered there?` |
| FINAL line # | 4181 |
| MB FINAL Q. | `Any experience on salt domes other than Sulphur Mines? We've already covered this.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 95%) |

### 212. idx 2141 (parent 2140)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let me because we need to be able to talk about maps and locations because you just mentioned one.  Let me show you what I'm going to mark as Exhibit No. 224 which has been marked as Yellow Rock 94336537 and this is just a map that Yellow Rock has produced.  Does this look familiar to you?` |
| FINAL line # | 4197 |
| MB FINAL Q. | `Let me because we need to be able to talk about maps and locations because you just mentioned one. Let me show you what I'm going to mark as Exhibit No. 224, which has been marked as Yellow Rock 336537. And this is just a map that Yellow Rock has produced.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 93%) |

### 213. idx 2150 (parent 2149)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 4207 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 214. idx 2159 (parent 2158)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Looking at that picture, can you tell me approximately where the 109431 was located?` |
| FINAL line # | 4237 |
| MB FINAL Q. | `Looking at that picture, can you tell me approximately where the 1031 was located?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 215. idx 2193 (parent 2192)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I'll get to the bottom.  Can you remind us there are some other there are surface locations for some other wells in that location, correct?` |
| FINAL line # | 4301 |
| MB FINAL Q. | `And I'll get to the bottom. Can you remind us, there are some other there are surface locations for some other wells in that location, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 216. idx 2208 (parent 2207)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You can still get around whatever is the pipe that's still down in the earth?` |
| FINAL line # | 4333 |
| MB FINAL Q. | `You can still get around whatever is the pipe that's still down in the earth?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 217. idx 2211 (parent 2210)

| Field | Text |
|---|---|
| Rough parent s1 | `Got it, okay.` |
| Rough s2 continuation | `It looks like and I know it's small but there's like four yellow numbers on there and I see 1014, 1028 but the other two I can't read them.  Can you?` |
| FINAL line # | 4339 |
| MB FINAL Q. | `It looks like, and I know it's small, but there's like four yellow numbers on there. And I see 1014, 1028, but the other two I can't read them. Can you?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 218. idx 2214 (parent 2213)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 4345 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 219. idx 2221 (parent 2220)

| Field | Text |
|---|---|
| Rough parent s1 | `Great.` |
| Rough s2 continuation | `Where would the bottom hole have been approximately?` |
| FINAL line # | 4359 |
| MB FINAL Q. | `Where would the bottom hole have been approximately?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 220. idx 2227 (parent 2226)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you draw a little line for that?` |
| FINAL line # | 4367 |
| MB FINAL Q. | `Can you draw a little line for that.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 221. idx 2232 (parent 2231)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Keep these handy because as we work on your waist through well, we'll try to use these.  And if I find a better map that's easier to read perhaps we'll switch to that one.  Okay?` |
| FINAL line # | 4379 |
| MB FINAL Q. | `Keep these handy. Because as we work our way through the wells, we'll try to use these. And if I find a better map that's easier to read, perhaps we'll switch to that one.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 222. idx 2288 (parent 2287)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I want to go back to the time period when you first came to Yellow Rock?` |
| FINAL line # | 4501 |
| MB FINAL Q. | `I want to go back to the time period when you first came to Yellow Rock.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 223. idx 2295 (parent 2294)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And you interacted with them particularly in the late 2018 early 2019 timeframe after the changeover in control of Yellow Rock, correct?` |
| FINAL line # | 4515 |
| MB FINAL Q. | `And you interacted with them particularly in the late 2018, early 2019 timeframe, after the changeover in control of Yellow Rock, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 224. idx 2317 (parent 2316)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And ultimately [some time\|sometime] in early 2019 Spring or so, Mr. Cox or Mr. Bertelot said think finished getting it all scanned and gave it to you all, okay in I'm sensing that youall never got the physical boxes or did you?` |
| FINAL line # | 4557 |
| MB FINAL Q. | `And ultimately, sometime in early 2019, the Spring or so, Mr. Cox or Mr. Bertelot said they finished getting it all scanned and gave it to you all. Okay? I'm sensing that youall never got the physical boxes or did you?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 93%) |

### 225. idx 2335 (parent 2334)

| Field | Text |
|---|---|
| Rough parent s1 | `That's fine I've got a wife and PARNS who are in that camp.  Okay.` |
| Rough s2 continuation | `First off when you said that you would go to your computer is this your computer in your office at bearing or would it also apply [well,\|well] let me step back.  Did they issue you a computer when you came to work?` |
| FINAL line # | 4599 |
| MB FINAL Q. | `First off, when you said that you would go to your computer, is this your computer in your office at Bering or would it also apply well, let me step back. Did they issue you a computer when you came to work?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 226. idx 2349 (parent 2348)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `AMGD you never had your own copy of that?` |
| FINAL line # | 4629 |
| MB FINAL Q. | `And you never had your own copy of that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 227. idx 2352 (parent 2351)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And again to your knowledge perception, did you have to be connected to the Internet in order to access what was in that drive?` |
| FINAL line # | 4635 |
| MB FINAL Q. | `And again to your knowledge or perception, did you have to be connected to the Internet in order to access what was in that drive` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 228. idx 2366 (parent 2365)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And again I'm just making sure you and I are on the same page?` |
| FINAL line # | 4697 |
| MB FINAL Q. | `Is that project file still on your machine?` |
| **Status** | **AMBIGUOUS (sim 32%, text len 62)** (sim 32%) |

### 229. idx 2415 (parent 2414)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did you ever open the kingdom project time that was on the hard drive that you got from Ms. Henderson on your computer?` |
| FINAL line # | 4775 |
| MB FINAL Q. | `Did you ever open the Kingdom project file that was on the hard drive that you got from Ms. Henderson on your computer?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 230. idx 2425 (parent 2424)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 4789 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 231. idx 2451 (parent 2450)

| Field | Text |
|---|---|
| Rough parent s1 | `Thank you.` |
| Rough s2 continuation | `Any other software that you can recall that you would have used in connection with your work?` |
| FINAL line # | 4845 |
| MB FINAL Q. | `Any other software that you can recall that you would have used in connection with your work?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 232. idx 2456 (parent 2455)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When you first got involved and started interacting with Ms. Henderson at Yellow Rock, generally speaking can you describe for me the nature of the material and information about Sulphur Mines that was available to you?` |
| FINAL line # | 4855 |
| MB FINAL Q. | `When you first got involved and started interacting with Ms. Henderson at Yellow Rock, generally speaking, can you describe for me the nature of the material and information about Sulphur Mines that was available to you?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 233. idx 2468 (parent 2467)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So now I've got the second is let's call it the well files at 1.0?` |
| FINAL line # | 4879 |
| MB FINAL Q. | `So now I've got the second let's call it the well files at 1.0?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 234. idx 2475 (parent 2474)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 4891 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 235. idx 2491 (parent 2490)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Would you I'm just trying to understand and we'll nothing to this with some documents in a moment and I can process but if you needed something for your PowerPoint showing a location in seismic depicts is of it, would you decide where in the project file to take that snapshot or would you get from it her in whatever way and you would pays in what she gave you?` |
| FINAL line # | 4925 |
| MB FINAL Q. | `Would you I'm just trying to understand and we'll go into this with some documents in a moment and I can process, but if you needed something for your PowerPoint, showing a location in seismic depictions of it, would you decide where in the project file to take that snapshot or would you get it from her in whatever way and you would paste in what she gave you?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 236. idx 2496 (parent 2495)

| Field | Text |
|---|---|
| Rough parent s1 | `I again because I don't do this for a living, sir, so I appreciate you bearing with me.` |
| Rough s2 continuation | `She would give you a map by E-mail or she would again just say here's the copy of the project time you can take it home today and you would open it and take a snippety of the map in the project file?` |
| FINAL line # | 4935 |
| MB FINAL Q. | `She would give you a map by Email or she would again just say here's the copy of the project file, you can take it home today. And you would open it and take a snippet of the map in the project file?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 237. idx 2512 (parent 2511)

| Field | Text |
|---|---|
| Rough parent s1 | `You're do fine, sir.` |
| Rough s2 continuation | `We're going to go to go nothing to this in some mere detail later and when you started in 2018, did you have an understanding of generally speaking, of the seismic data sets that Yellow Rock had access to?` |
| FINAL line # | 4971 |
| MB FINAL Q. | `We're going to go into this in some more detail later, but when you started in 2018, did you have an understanding of generally speaking, of the seismic datasets that Yellow Rock had access to?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 238. idx 2525 (parent 2524)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Do you understand RPM to understand time migration?` |
| FINAL line # | 4993 |
| MB FINAL Q. | `Do you understand RTM to involve time migration?` |
| **Status** | **AMBIGUOUS (sim 85%, text len 51)** (sim 85%) |

### 239. idx 2528 (parent 2527)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay that's what I think it is but I'm not an expert.` |
| Rough s2 continuation | `It's fair to say that you are not involved in a substantive [way\|with a] in the gathering of the seismic data, the processing of the seismic data or the interpretation of the seismic data, correct?` |
| FINAL line # | 4999 |
| MB FINAL Q. | `It's fair to say that you are not involved in a substantive way in the gathering of the seismic data, the processing of the seismic data, or the interpretation of the seismic data, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 240. idx 2531 (parent 2530)

| Field | Text |
|---|---|
| Rough parent s1 | `That saves you some questions today, sir.` |
| Rough s2 continuation | `Would you agree with me that in oil and gas exploration identification and drilling of new prospects or new wells is capital intensive?` |
| FINAL line # | 5005 |
| MB FINAL Q. | `Would you agree with me that in oil and gas exploration identification and drilling of new prospects or new wells is capital intensive?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 241. idx 2566 (parent 2565)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When you got to Yellow Rock 2.0 did there come a point in time where you came to understand the amount of capital that was available to Yellow Rock 2.0 to be used for new wells or new drilling activity?` |
| FINAL line # | 5065 |
| MB FINAL Q. | `When you got to Yellow Rock 2.0, did there come a point in time where you came to understand the amount of capital that was available to Yellow Rock 2.0 to be used for new wells or new drilling activity?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 242. idx 2581 (parent 2580)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Have you had any subsequent conversation at that time?` |
| FINAL line # | 5095 |
| MB FINAL Q. | `Have you had any subsequent conversation at that time?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 243. idx 2596 (parent 2595)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And had you worked with Mr. Love prior to that?` |
| FINAL line # | 5125 |
| MB FINAL Q. | `And had you worked with Mr. Love prior to that?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 244. idx 2603 (parent 2602)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You did not interact with Mr. Love at any point while you were at 2.0?` |
| FINAL line # | 5139 |
| MB FINAL Q. | `You did not interact with Mr. Love at any point while you were at 2.0?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 245. idx 2620 (parent 2619)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And do you recall there was a period of time well, do you recall sort of routinely going to Mr. Cox and interacting with him about potential prospects at Sulphur Mines or were there periods where that stopped happening?` |
| FINAL line # | 5173 |
| MB FINAL Q. | `And do you recall there was a period of time well, do you recall sort of routinely going to Mr. Cox and interacting with him about potential prospects at Sulphur Mines or were there periods where that stopped happening?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 246. idx 2629 (parent 2628)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And have you read any of those communications?` |
| FINAL line # | 5191 |
| MB FINAL Q. | `And have you read any of those communications?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 247. idx 2647 (parent 2646)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `When you first gotten gauged at Yellow Rock, I'm sensing part of your job was to go through the records for I sense all of the legacy wells looking for potential opportunities both for new wells and recompletions and workovers; is that fair?` |
| FINAL line # | 5227 |
| MB FINAL Q. | `When you first got engaged at Yellow Rock, I'm sensing part of your job was to go through the records for I sense all of the legacy wells looking for potential opportunities, both for new wells and recompletions and workovers; is that fair?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 248. idx 2650 (parent 2649)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 5231 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 249. idx 2653 (parent 2652)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 5235 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 250. idx 2660 (parent 2659)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `How did you and the team approach how to divide all that up?` |
| FINAL line # | 5249 |
| MB FINAL Q. | `How did you and the team approach how to divide all that up?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 251. idx 2703 (parent 2702)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  I'm going to again I'm going to caution you these are yes or no questions so I don't get into what was talked about, okay?` |
| Rough s2 continuation | `When did y'all meet?` |
| FINAL line # | 5343 |
| MB FINAL Q. | `When did y'all meet?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 252. idx 2710 (parent 2709)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And yesterday?` |
| FINAL line # | 5357 |
| MB FINAL Q. | `And yesterday?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 253. idx 2729 (parent 2728)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Any that you recall that you had forgotten about that it refreshed your memory looking at them?` |
| FINAL line # | 5399 |
| MB FINAL Q. | `Any that you recall that you had forgotten about that it refreshed your memory looking at them?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 254. idx 2738 (parent 2737)

| Field | Text |
|---|---|
| Rough parent s1 | `Time takes a toll on all of us, sir.` |
| Rough s2 continuation | `I need to talk to you about this.  This would have been a document I think that's early time in your tenure working for Yellow Rock; is that fair?` |
| FINAL line # | 5415 |
| MB FINAL Q. | `(not present as Q. in FINAL)` |
| **Status** | **NOT STANDALONE (absent from FINAL region)** (sim 0%) |

### 255. idx 2741 (parent 2740)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `First I want to ask we've talked about Ms. Henderson.  Let me see on here.  It's to the on here or maybe you told me about it.  Who is John Miller?` |
| FINAL line # | 5425 |
| MB FINAL Q. | `First I want to ask we've talked about Ms. Henderson. Let me see on here. It's not on here or maybe you told me about it. Who is John Miller?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 256. idx 2754 (parent 2753)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What the document that's attached and that you sent to Patricia and she sent to John, how would you describe what this document is?` |
| FINAL line # | 5455 |
| MB FINAL Q. | `What the document that's attached and that you sent to Patricia and she sent to John, how would you describe what this document is?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 257. idx 2761 (parent 2760)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And what looking at the map that we talked about at Exhibit No. 225, can you give me some sense of where this are you looking here at what I can call a prospect location?` |
| FINAL line # | 5469 |
| MB FINAL Q. | `And what looking at the map that we talked about at Exhibit No. 225, can you give me some sense of where this are you looking here at what I can call a prospect location?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 258. idx 2766 (parent 2765)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you tell me where this lead would have been located on Exhibit No. 225?` |
| FINAL line # | 5483 |
| MB FINAL Q. | `Can you tell me where this lead would have been located on Exhibit No. 225?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 259. idx 2779 (parent 2778)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `In the CIB HAZ formation?` |
| FINAL line # | 5507 |
| MB FINAL Q. | `In the CIB HAZ formation?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 260. idx 2820 (parent 2819)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 5595 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 261. idx 2839 (parent 2838)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `The dotted lines and the bold lines that are in the circle that are on both of these, did those come from Ms. Henderson?` |
| FINAL line # | 5641 |
| MB FINAL Q. | `The dotted lines and the bold lines that are in the circle that are on both of these, did those come from Ms. Henderson?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 262. idx 2850 (parent 2849)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `What is Page No. 426?  Is this using snapshots to figure the acreage of the 943 leads?` |
| FINAL line # | 5665 |
| MB FINAL Q. | `What is Page No. 426? Is this using snapshots to figure the acreage of the three leads?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 95%) |

### 263. idx 2862 (parent 2861)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `On Page No. 427 there is a table.  Did you create this table?` |
| FINAL line # | 5689 |
| MB FINAL Q. | `On Page No. 427 is a table. Did you create this table?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 95%) |

### 264. idx 2881 (parent 2880)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You calculated the acreage, correct?` |
| FINAL line # | 5735 |
| MB FINAL Q. | `You calculated the acreage, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 265. idx 2886 (parent 2885)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let me step become.  What is the intended end result of this spreadsheet?` |
| FINAL line # | 5745 |
| MB FINAL Q. | `What is the intended end result of this spreadsheet?` |
| **Status** | **AMBIGUOUS (sim 84%, text len 73)** (sim 84%) |

### 266. idx 2901 (parent 2900)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And who set those values, you?` |
| FINAL line # | 5779 |
| MB FINAL Q. | `And who set those values, you?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 267. idx 2926 (parent 2925)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay U.` |
| Rough s2 continuation | `What I'm trying to understand is there came a point in time when youall were seriously evaluating and making a decision whether to drill the 1027 or the 102 or the 1029, right?` |
| FINAL line # | 5829 |
| MB FINAL Q. | `What I'm trying to understand is there came a point in time when youall were seriously evaluating and making a decision whether to drill the 1027 or the 1028 or the 1029, right?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 268. idx 2958 (parent 2957)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `The next page is 428.  What is this?` |
| FINAL line # | 5881 |
| MB FINAL Q. | `The next page is 428. What is this?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 269. idx 2961 (parent 2960)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 5887 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 270. idx 2973 (parent 2972)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Would others have been involved or came from?` |
| FINAL line # | 5913 |
| MB FINAL Q. | `Would others have been involved or it came from you?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 93%) |

### 271. idx 2978 (parent 2977)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 5921 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 272. idx 3005 (parent 3004)

| Field | Text |
|---|---|
| Rough parent s1 | `And it says not sure about this Q see last part of E-mail plough but sending this E-mail to inquire.  An investor wanted an engineered reserve report and this was my reply [below\|blow].  He wrote we developed economics for future development business had on historical production averages per well from each pay and on historical [success\|is being] rates in drilling.  And on estimations of the undeveloped area around the salt dome.  Then we applied various risking factors to the formation goes for building a base case of economics.  Going forward [on your\|our] *REPORTER CHECK HERE* 3D seismic data.  Reserve report based odd 3D.  For each salt block will be generated as we drill wells.  As we get each salt bock evaluated from each pay zone *REPORTER CHECK HERE* independently engineered drilling locations will be available on a spreadsheet with a priority drilling schedule for all of the wells.  As we drill wells, we'll continuously update the priority drilling schedule.  For each block fully evaluated with 3D seismic, any drilling locations would likely be categorized as probable well location is until the first well, is drilled and each [if all the\|fault] pluck then proof reserves might be established for subsequent well location is after the first well, meets fault block.  We'll continue to make available our work with independent consultants to assess an categories reserves with interpreting 3D data an drilling wells.  He then writes the request came back from an investor can you if you are your reservoir engineers spreadsheets an calculations with his assumptions an notes for the first fault block.  John S thoughts enjoyed ["\|quote].` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 5995 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 273. idx 3010 (parent 3009)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `First off, I think you already told me who Mr. Miller was.  Does this indicate to you that he was unlike you interacting with investors?` |
| FINAL line # | 6007 |
| MB FINAL Q. | `First off, I think you already told me who Mr. Miller was. Does this indicate to you that he was, unlike you, interacting with investors?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 274. idx 3016 (parent 3015)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And do you recall hearing that investors or someone in the company wanted to share with investors any type of reserve spreadsheets that you or others had created for anything all the Sulphur Mines?` |
| FINAL line # | 6015 |
| MB FINAL Q. | `And do you recall hearing that investors or someone in the company wanted to share with investors any type of reserve spreadsheets that you or others had created for anything at the Sulphur Mines?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 275. idx 3033 (parent 3032)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `At this point the references that he has in here about going forward, the economics and reserve estimation goes will be all from 3D seismic data this is the Geotomo data at this point?` |
| FINAL line # | 6047 |
| MB FINAL Q. | `At this point the references that he has in here about going forward, are economics and reserve estimations will be all from 3D seismic data. This is the Geotomo data at this point?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 276. idx 3045 (parent 3044)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `After you all drill any of the 1027 to the 109431 wells, did you ever do a reserve report like you just described or had a thirdparty do one?` |
| FINAL line # | 6079 |
| MB FINAL Q. | `After youall drill any of the 1027 to the 1031 wells, did you ever do a reserve report like you just described or had a thirdparty do one?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 277. idx 3077 (parent 3076)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You go on to write in the E-mail, I think your response was accurate and well written.  Having reread think the morning, do you still believe this is a correct statement?` |
| FINAL line # | 6149 |
| MB FINAL Q. | `You go on to write in the Email: "I think your response was accurate and well written." Having reread it this morning, do you still believe this is a correct statement?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 278. idx 3089 (parent 3088)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You then say: We are striving excuse me you then write: [With another\|We are] stim reply providing estimates of possible reserves based upon new 3D mapping and volume metric calculations.` |
| FINAL line # | 6169 |
| MB FINAL Q. | `You then say: "We are striving" excuse me. You then write: "We are simply providing estimates of possible reserves based upon new 3D mapping and volumetric calculations."` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 92%) |

### 279. idx 3090 (parent 3088)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Is the new 3D map referencing the Geotomo work or something else?` |
| FINAL line # | 6171 |
| MB FINAL Q. | `Is the new 3D map referencing the Geotomo work or something else?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 280. idx 3093 (parent 3092)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You then write: [With another\|We are] striving for accuracy and to assign a risk variable on each prospect [well,\|well] after a discovery is made perhaps you will want an actual thirdparty reserve report made, but that would be better coming from a firm. "` |
| FINAL line # | 6177 |
| MB FINAL Q. | `You then write: "We are striving for accuracy and to assign a risk variable on each prospect/well. After a discovery is made, perhaps you will want an actual thirdparty reserve report made, but that would be better coming from a firm."` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 281. idx 3094 (parent 3092)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 6179 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 282. idx 3099 (parent 3098)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `You then say: We can discuss at length if you would like, but the PowerPoint fairly accurately describes what I am doing.  And I do have the spreadsheet with my work in it. "` |
| FINAL line # | 6191 |
| MB FINAL Q. | `You then say: "We can discuss at length if you would like, but the PowerPoint fairly accurately describes what I am doing. I do have a spreadsheet with my work in it."` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 283. idx 3100 (parent 3098)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 6193 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 284. idx 3103 (parent 3102)

| Field | Text |
|---|---|
| Rough parent s1 | `And Ms. Henderson wrote I agree with you Brad all the calculations and parameters for those calculations are on the PowerPoint. "` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 6201 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 285. idx 3106 (parent 3105)

| Field | Text |
|---|---|
| Rough parent s1 | `And if I sense we don't fully [know\|no], the PowerPoint at issue that they shared with the investor looked like the one in Exhibit No. 226, that would have been the correct statement as well, correct tomorrow top Object to form.` |
| Rough s2 continuation | `Go ahead.` |
| FINAL line # | 6221 |
| MB FINAL Q. | `Okay.` |
| **Status** | **AMBIGUOUS (sim 43%, text len 9)** (sim 43%) |

### 286. idx 3112 (parent 3111)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let me show you what I've marked as Exhibit No. 228.  Sorry.  Yellow Rock 291625 to 647?` |
| FINAL line # | 6223 |
| MB FINAL Q. | `Let me show you what I've marked as Exhibit No. 228. Sorry. Yellow Rock 291625 to 647.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 287. idx 3124 (parent 3123)

| Field | Text |
|---|---|
| Rough parent s1 | `All right.` |
| Rough s2 continuation | `This is an E-mail if you look at the bottom from John Miller to Steve Wipple and Patricia Henderson saying Patricia I wondered if you had ever seen this PowerPoint.  My understanding is that this is the mapping put together by Burlington Resources off of the old 19923D seismic data for the CIB HAZ formation.  CV I believe that's Steve with Wipple *REPORTER CHECK HERE* did I read that correctly?` |
| FINAL line # | 6253 |
| MB FINAL Q. | `This is an Email if you look at the bottom from John Miller to Steve Wippel and Patricia Henderson saying: "Patricia, I wondered if you had ever seen this PowerPoint. My understanding is that this is the mapping put together by Burlington Resources off of the old 1992 3D seismic data for the CIB HAZ formation. Steve W" I assume that means Steve Wippel "would know more about this and how they came to the reserve projections."` |
| **Status** | **AMBIGUOUS (sim 84%, text len 397)** (sim 84%) |

### 288. idx 3137 (parent 3136)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Have you seen this PowerPoint before today?` |
| FINAL line # | 6285 |
| MB FINAL Q. | `Have you seen this PowerPoint before today?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 289. idx 3140 (parent 3139)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `If you can take a moment and just look through it.  Some of it particularly at I'm going to use the page numbers in the PowerPoint not the bathe numbers, at pages two and 943 are historical. ; is that fair?` |
| FINAL line # | 6291 |
| MB FINAL Q. | `If you can take a moment and just look through it. Some of it, particularly at I'm going to use the page numbers in the PowerPoint, not the Bates numbers at Pages 2 and 3 are historical; is that fair?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 290. idx 3151 (parent 3150)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `The first one is ache rears, the second number is BP an if?` |
| FINAL line # | 6317 |
| MB FINAL Q. | `(not present as Q. in FINAL)` |
| **Status** | **NOT STANDALONE (absent from FINAL region)** (sim 0%) |

### 291. idx 3177 (parent 3176)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Can you turn to slide 20.` |
| FINAL line # | 6359 |
| MB FINAL Q. | `Can you turn to Slide 20.` |
| **Status** | **AMBIGUOUS (sim 100%, text len 25)** (sim 100%) |

### 292. idx 3180 (parent 3179)

| Field | Text |
|---|---|
| Rough parent s1 | `It I'll use the Bates No.. it ends in 646.  It's 943 from the back.  There you go.` |
| Rough s2 continuation | `If you look at the last hold O I give me a second.  Oh.  If you look at last page, 647 you can see there are some economic projections and they have a date in late 2017.  Do you see that?` |
| FINAL line # | 6367 |
| MB FINAL Q. | `If you look at the last hold on. Give me a second. Oh. If you look at last page, 647, you can see there are some economic projections and they have a date in late 2017.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 293. idx 3189 (parent 3188)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So just so I understand [math\|mat], one point # million?` |
| FINAL line # | 6391 |
| MB FINAL Q. | `So just so I understand the math, like 1.8 million?` |
| **Status** | **AMBIGUOUS (sim 77%, text len 56)** (sim 77%) |

### 294. idx 3202 (parent 3201)

| Field | Text |
|---|---|
| Rough parent s1 | `All right.` |
| Rough s2 continuation | `Did youall ever drill a well anywhere at Yellow Rock and Sulphur Mines let me ie fries that.  Did awe you will of drill a well at Sulphur Mines that had a cash flow ultimately of one point # 5 million per well?` |
| FINAL line # | 6421 |
| MB FINAL Q. | `Did youall ever drill a well at Sulphur Mines that had a cash flow ultimately of 8.15 million per well?` |
| **Status** | **AMBIGUOUS (sim 64%, text len 210)** (sim 64%) |

### 295. idx 3236 (parent 3235)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 6465 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 296. idx 3258 (parent 3257)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Would those inputs without having been identified here, have been the source of the numbers on this page for gross oil and gas from over over the tenyear cycle of the projection?` |
| FINAL line # | 6533 |
| MB FINAL Q. | `Would those inputs, without having been identified here, have been the source of the numbers on this page for gross oil and gas from over over the 10year cycle of the projection?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 297. idx 3272 (parent 3271)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let me show you what I'm marking as 229.  This is an E-mail chain in early 2019, February 6th of 2019 between you and some others and the RE:line is cc credit screen CAP. # do you remember what [owe\|oh] sorry.  I didn't tell everybody Exhibit No. 229 is Yellow Rock 292961 through 965.  Do you recall what cc credit all CAP credits, screen CAP is describing?` |
| FINAL line # | 6559 |
| MB FINAL Q. | `Let me show you what I'm marking as 229. This is an Email chain in early 2019, February 6th of 2019, between you and some others. And the RE: line is "CCC Screen CAP". Do you remember what oh, wait. Sorry. I didn't tell everybody. Exhibit No. 229 is Yellow Rock 292961 through 965.` |
| **Status** | **AMBIGUOUS (sim 84%, text len 358)** (sim 84%) |

### 298. idx 3275 (parent 3274)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  So this is another lead and you're asking a question at the bottom about you say on a directional [well,\|well] how far does the about H L bottom whole location of the well need to be from a lease line to get a permit in Louisiana and then you ask how far does the producing horizon need to be from the least line in different than question one chatty".` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 6575 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 299. idx 3278 (parent 3277)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And you copy Mr. Easley who is the CFO, correct?` |
| FINAL line # | 6583 |
| MB FINAL Q. | `And you copy Mr. Easley, who is the CFO, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 300. idx 3285 (parent 3284)

| Field | Text |
|---|---|
| Rough parent s1 | `Sorry I got confused.  He writes back and copies a person we talked about Jo Beth Taylor and says: Joe, by copy of this E-mail I am introducing Brad Brandl who has been working for the past few months with White Top Energy, LLC and Yellow Rock on Sulphur Mines Field production issues on existing wells and in identifying well location is for the initialization of our upcoming drilling program in the field. "` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 6599 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 301. idx 3306 (parent 3305)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.  I think I have time for one more.  We'll begin our segue a bit more into seismic data.  Let me show you what I'm marking as Exhibit 230.  Thank you, Marybeth.  I always think you're keeping your eyes on me the whole time that I stick my arm out.` |
| Rough s2 continuation | `By the way who gets credit for fixing the noise?  You?  You?` |
| FINAL line # | 6639 |
| MB FINAL Q. | `And she's the person that youall would go through to get permits, for example, from LDNR before engaging in certain drilling operations?` |
| **Status** | **AMBIGUOUS (sim 35%, text len 60)** (sim 35%) |

### 302. idx 3326 (parent 3325)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `This is an E-mail from you to a series of people within the company an copying a gentleman named [math\|mat] carat QI Petrophysics, correct?` |
| FINAL line # | 6691 |
| MB FINAL Q. | `This is an Email from you to a series of people within the company and copying a gentleman named Matt Carr at QI Petrophysics, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 303. idx 3338 (parent 3337)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `First is there is a difficulties can you also reference here that there was a meeting between Patricia, [yourself\|yours] and math [car have\|carve] QI Petrophysics towings over candidate selection for analysis.  Did I read that correctly?` |
| FINAL line # | 6717 |
| MB FINAL Q. | `First is, there's a discussion a reference here that there was a meeting between Patricia, yourself and Matt Carr of QI Petrophysics to go over candidate selection for analysis. Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 87%) |

### 304. idx 3343 (parent 3342)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `How were you how was Yellow Rock using Dr. Carr?` |
| FINAL line # | 6729 |
| MB FINAL Q. | `How were you how was Yellow Rock using Dr. Carr?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 305. idx 3350 (parent 3349)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And am I sensing the discussion that took place in September of 2018 was you and Ms. Henderson and he discussing specific wells that he ought to prioritize doing his well log analysis?` |
| FINAL line # | 6743 |
| MB FINAL Q. | `And am I sensing the discussion that took place in September of 2018 was you and Ms. Henderson and he discussing specific wells that he ought to prioritize doing his well log analysis?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 306. idx 3353 (parent 3352)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `I would like you to take a moment and tell me big picture, which of the list of wells that are identified here of ended up leading to a new well or any type of other development first during the period of 2.0?` |
| FINAL line # | 6749 |
| MB FINAL Q. | `I would like you to take a moment and tell me big picture, which of the list of wells that are identified here ever ended up leading to a new well or any type of other development, first during the period of 2.0?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 307. idx 3358 (parent 3357)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So and maybe I misunderstanding I'm looking at PowerPoint for a moment?` |
| FINAL line # | 6759 |
| MB FINAL Q. | `And so maybe I'm misunderstanding. I'm looking at the PowerPoint for a moment.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 90%) |

### 308. idx 3365 (parent 3364)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 6771 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 309. idx 3368 (parent 3367)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 6775 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 310. idx 3379 (parent 3378)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 6819 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 311. idx 3393 (parent 3392)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 6823 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 312. idx 3396 (parent 3395)

| Field | Text |
|---|---|
| Rough parent s1 | `And do you know at the bottom she explains please set up pro eat you're for pet trois failing we should never all caps [be\|been] done boy more than one hour as there is on line help".` |
| Rough s2 continuation | `Do you know what she's referring to there?` |
| FINAL line # | 6835 |
| MB FINAL Q. | `Do you know what she's referring to there?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 313. idx 3399 (parent 3398)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And Item No.  Three on here it says first go to the DropBox of logs that tomorrow met calf has been putting together since Randy left the project. ".` |
| FINAL line # | 6841 |
| MB FINAL Q. | `And Item No. 3 on here it says: "First go to the DropBox of logs that Tom Metcalf has been putting together since Randy left the project."` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 314. idx 3400 (parent 3398)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Let me just check here.  Who is Randy, if you recall?` |
| FINAL line # | 6843 |
| MB FINAL Q. | `Let me just check here. Who is Randy, if you recall?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 315. idx 3405 (parent 3404)

| Field | Text |
|---|---|
| Rough parent s1 | `Got it.  Okay.` |
| Rough s2 continuation | `What is this DropBox of logs that's being referenced?` |
| FINAL line # | 6853 |
| MB FINAL Q. | `And what is this "DropBox of logs" that's being referenced?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 95%) |

### 316. idx 3412 (parent 3411)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Do you recall ever being on a DropBox do you know whether a DropBox is?` |
| FINAL line # | 6867 |
| MB FINAL Q. | `Do you recall ever being on a DropBox do you know what a DropBox is?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 96%) |

### 317. idx 3417 (parent 3416)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 6875 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 318. idx 3435 (parent 3434)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Are you like on a mission that was my ultimate question.  I'm trying to figure out was this youall use I'm not trying to be disrespectful.  The nomenclature about the *REPORTER CHECK HERE* does not always notch up tal drill number [if it\|fit] ended up being drilled, fair?` |
| FINAL line # | 6911 |
| MB FINAL Q. | `Are you like on a mission? That was my ultimate question. I'm trying to figure out was this youall use I'm not trying to be disrespectful. The nomenclature implied the company about the potential prospects does not always match up to the drill number if it ended up being drilled.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 87%) |

### 319. idx 3446 (parent 3445)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Oh wait.  That's one of the ones you told me didn't do so well.  The 1029?` |
| FINAL line # | 6937 |
| MB FINAL Q. | `Oh, wait. That's one of the ones you told me didn't do so well, the 1029?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 320. idx 3464 (parent 3463)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Lastly [ill\|I'll\|I will] let everyone go catch plans which awful a already given to you is Yellow Rock *REPORTER CHECK HERE* on '05 and this is a short discussion that you had in November 2018 with Ms. Henderson, Dr. Carr, Steve Wipple, about Burlington 301 which I'll remind you was on the list of wells from Exhibit 230 that we talked about for use with the seismic work, correct I think this is one of the moments where you didn't hear my question?` |
| FINAL line # | 6973 |
| MB FINAL Q. | `Lastly, and then I will let everyone go catch planes, which I've already given to you is Yellow Rock 292005. And this is a short discussion that you had in November 2018 with Ms. Henderson, Dr. Carr, Steve Wippel, about Burlington 301, which I'll remind you was on the list of wells from Exhibit 230 that we talked about for use with the seismic work, correct? I think this is one of the moments where you didn't hear my question.` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 92%) |

### 321. idx 3474 (parent 3473)

| Field | Text |
|---|---|
| Rough parent s1 | `You're sending information to Ms. Henderson and others an you write there is a bunch of document attached the Burlington 301 is a nobrainer.  It's deviated but recent with modern logs and away from the dome".` |
| Rough s2 continuation | `When you say the 301 is a nobrainer, what did you mean *REPORTER CHECK HERE*?` |
| FINAL line # | 6997 |
| MB FINAL Q. | `When you said the Burlington 301 is a nobrainer, what did you mean?` |
| **Status** | **AMBIGUOUS (sim 75%, text len 77)** (sim 75%) |

### 322. idx 3477 (parent 3476)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `The 301 is a reference to a legacy well?` |
| FINAL line # | 7003 |
| MB FINAL Q. | `The 301 is a reference to a legacy well?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 323. idx 3480 (parent 3479)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And is that how I would find it if I wanted to to look it up it's Burlington 301?` |
| FINAL line # | 7009 |
| MB FINAL Q. | `And is that how I would find it if I wanted to look it up, it's Burlington 301?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 98%) |

### 324. idx 3496 (parent 3495)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Once Yellow Rock 943 point on essentially as I understand it stopped paying attention to the reprocess data that happened in 2018, did they ever go back and look at this location in the context of the tome [owe\|oh] seismic?` |
| FINAL line # | 7043 |
| MB FINAL Q. | `Once Yellow Rock 3.0, essentially, as I understand it, stopped paying attention to the reprocess data that happened in 2018, did they ever go back and look at this location in the context of the tomo seismic?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 325. idx 3504 (parent 3503)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Is this a good stopping point?` |
| FINAL line # | 7085 |
| MB FINAL Q. | `So this is in July, late July, July 30th, 2019, from you to Mr. Wippel, Mr. Easley, Robin French, John Miller, correct?` |
| **Status** | **AMBIGUOUS (sim 31%, text len 30)** (sim 31%) |

### 326. idx 3517 (parent 3516)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `So this is in July, late July 30th, 2019, from you to Mr. Wipple, Mr. Easley, Robin French, John Miller, correct?` |
| FINAL line # | 7085 |
| MB FINAL Q. | `So this is in July, late July, July 30th, 2019, from you to Mr. Wippel, Mr. Easley, Robin French, John Miller, correct?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 327. idx 3520 (parent 3519)

| Field | Text |
|---|---|
| Rough parent s1 | `And it's prospect generation PowerPoint E-mail says here is my first past at creating a process for our generation of prospects. "` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 7091 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 328. idx 3547 (parent 3546)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I forgot to ask this: On the first page Ms. Hand er done sos not copied on this E-mail?` |
| FINAL line # | 7149 |
| MB FINAL Q. | `And I forgot to ask this: On the first page Ms. Henderson is not copied on this Email?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 94%) |

### 329. idx 3565 (parent 3564)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `It says here the primary objective is to get the # 71 S T one, Sidetrack, drilled and that happens from July, correct?` |
| FINAL line # | 7185 |
| MB FINAL Q. | `It says here: "The primary objective is to get the 871 ST1" Sidetrack 1 "drilled."` |
| **Status** | **AMBIGUOUS (sim 72%, text len 118)** (sim 72%) |

### 330. idx 3570 (parent 3569)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Do you know why that didn't get done?` |
| FINAL line # | 7197 |
| MB FINAL Q. | `Do you know why that didn't get done?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 331. idx 3573 (parent 3572)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And I'm asking you because here, it's saying the primary objective is to get the sidetrack drilled an then based upon the results of that we'll want to quickly give additional CIB HAZ locations. "` |
| FINAL line # | 7203 |
| MB FINAL Q. | `And I'm asking you because here it's saying the primary objective is to get the sidetrack drilled. And then: "Based upon the results of that, we will want to quickly give additional CIB HAZ locations."` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 97%) |

### 332. idx 3574 (parent 3572)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Did I read that correctly?` |
| FINAL line # | 7205 |
| MB FINAL Q. | `Did I read that correctly?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 333. idx 3577 (parent 3576)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `The pored point says provide advice, mapping and aisles [owe\|oh] packs I is on PA credit H S for pay found in the 1027 and 1028 wellbores [by\|buy] September 30th. "` |
| FINAL line # | 7213 |
| MB FINAL Q. | `The third point says: "Provide revised mapping and Isopachs" Isopachs for pay found in the 1027 and 1028 wellbores by September 30th. "` |
| **Status** | **AMBIGUOUS (sim 83%, text len 164)** (sim 83%) |

### 334. idx 3578 (parent 3576)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Is this work to be done based on the initial drilling of 1027 and 1028?` |
| FINAL line # | 7215 |
| MB FINAL Q. | `Is this work to be done based on the initial drilling of 1027 and 1028?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 335. idx 3604 (parent 3603)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And then after that was there another recompletion of that in the CIB HAZ in July?` |
| FINAL line # | 7271 |
| MB FINAL Q. | `And then after that was there another recompletion of that in the CIB HAZ in July?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 100%) |

### 336. idx 3607 (parent 3606)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 7275 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |

### 337. idx 3610 (parent 3609)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `And then north team objectives and it's No.  Two, secondary objective is to map the there also a a bunch of X's.  Do you remember what that is about?` |
| FINAL line # | 7281 |
| MB FINAL Q. | `And then north team objectives, and it's No. 2, secondary objective is to map the there's a bunch of X's. Do you remember what that's about?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 95%) |

### 338. idx 3654 (parent 3653)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `Since that happened when in July of?` |
| FINAL line # | 7379 |
| MB FINAL Q. | `Since that happened when, in July of?` |
| **Status** | **STANDALONE Q. IN FINAL** (sim 99%) |

### 339. idx 3663 (parent 3662)

| Field | Text |
|---|---|
| Rough parent s1 | `Okay.` |
| Rough s2 continuation | `(empty)` |
| FINAL line # | 7395 |
| MB FINAL Q. | `(empty s2 - no content)` |
| **Status** | **EMPTY** (sim n/a) |
