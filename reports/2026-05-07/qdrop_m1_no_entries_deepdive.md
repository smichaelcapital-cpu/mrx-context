# Q-DROP M1 NO-Entry Deep Dive

---

## PULL A — Entry 216 (rough_idx 2208, Expected FINAL line 4391)

### FINAL lines 4381–4401

```
  4381	Q.	Okay?
  4382
  4383	A.	Yes, sir.
  4384
  4385	Q.	We've been going about an hourandahalf, so I apologize. So why don't we take a short break?
  4386
  4387	A.	Sounds good.
  4388
  4389	COLLOQUY	MR. MADIGAN: Sounds good.
  4390
  4391	COLLOQUY	THE VIDEOGRAPHER: The time is 2:20 p.m. and we are now off the record.
  4392
  4393	COLLOQUY	(Recess.)
  4394
  4395	COLLOQUY	THE VIDEOGRAPHER: The time is 2:40 p.m. and we are now back on the record.
  4396
  4397	BYLINE	BY MR. PEACOCK:
  4398
  4399	Q.	Oh, one thing I wanted to go back to from my notes. When you were talking about the 1031, you described that in the deepest two of the five targeted zones in that well, that once you got to them, both were tight. I think is the word that you used, correct?
  4400
  4401	A.	Yes, sir.
```

### Rough turns: idx 2207, 2208, 2209

```json
{
  "idx": 2207,
  "speaker": "Q.",
  "speaker_raw": "Q.",
  "text": "Okay.",
  "paragraph_style": "s1",
  "continuation_of": null,
  "rtf_source_offset": 1177478,
  "transforms_applied": [
    "rtf_parse"
  ]
}

{
  "idx": 2208,
  "speaker": "Q.",
  "speaker_raw": "Q.",
  "text": "You can still get around whatever is the pipe that's still down in the earth?",
  "paragraph_style": "s2",
  "continuation_of": 2207,
  "rtf_source_offset": 1177645,
  "transforms_applied": [
    "rtf_parse"
  ],
  "strokes": [
    {"word": "You", "stroke": "STEUL"},
    {"word": "get", "stroke": "TKPWET"},
    {"word": "around", "stroke": "ARPBD"},
    {"word": "whatever", "stroke": "WHAFR"},
    {"word": "is", "stroke": "ST"},
    {"word": "pipe", "stroke": "PAOEUP"},
    {"word": "that's", "stroke": "AE"},
    {"word": "still", "stroke": "STEUL"},
    {"word": "down", "stroke": "TKOUPB"},
    {"word": "in", "stroke": "TPH-T"},
    {"word": "earth", "stroke": "ERT"}
  ]
}

{
  "idx": 2209,
  "speaker": "A.",
  "speaker_raw": "A.",
  "text": "Yes, the part of the rig being now is it on the property that the welloccupied.",
  "paragraph_style": "s3",
  "continuation_of": null,
  "rtf_source_offset": 1178156,
  "transforms_applied": [
    "rtf_parse"
  ],
  "strokes": [
    {"word": "the", "stroke": "-T"},
    {"word": "part", "stroke": "PART/-FT"},
    {"word": "rig", "stroke": "REUG"},
    {"word": "being", "stroke": "-BG"},
    {"word": "now", "stroke": "TPHOU"},
    {"word": "is", "stroke": "SEUT"},
    {"word": "on", "stroke": "OT"},
    {"word": "property", "stroke": "PROT"},
    {"word": "that", "stroke": "THA"},
    {"word": "the", "stroke": "-T"},
    {"word": "well", "stroke": "PAOEUD"}
  ],
  "deletions": [
    {
      "position": 20,
      "strokes": ["REUG", "-BG/TPHROU", "SEUL", "SEUT/*/*/*/*"]
    }
  ]
}
```

---

## PULL B — Entry 324 (rough_idx 3496, Expected FINAL line 7059)

### FINAL lines 7049–7069

```
  7049	A.	I don't recall.
  7050
  7051	Q.	As best you know though, this is not a location that's ever been developed during Yellow Rock's tenure?
  7052
  7053	A.	This is the location that has never been developed.
  7054
  7055	COLLOQUY	MR. PEACOCK: Okay.
  7056
  7057	COLLOQUY	Is this a good stopping point?
  7058
  7059	COLLOQUY	MR. MADIGAN: I don't mind letting you go a little longer.
  7060
  7061	COLLOQUY	MR. PEACOCK: I don't want to make y'all miss a plane either.
  7062
  7063	COLLOQUY	MR. MADIGAN: I'm not worried about timing.
  7064
  7065	COLLOQUY	MR. PEACOCK: I have more. Y'all have to be the ones to tell me when to stop. I told you I'm not going to finish today.
  7066
  7067	COLLOQUY	MR. MADIGAN: I imagine that you're going to put a Reservation of Rights on that on the record and we're going to object to that and take it from there. Yeah, I mean I don't mind you taking a few more minutes if you have something important that you want to cover.
  7068
  7069	COLLOQUY	How much time have we been on the record?
```

### Rough turns: idx 3495, 3496, 3497

```json
{
  "idx": 3495,
  "speaker": "Q.",
  "speaker_raw": "Q.",
  "text": "Okay.",
  "paragraph_style": "s1",
  "continuation_of": null,
  "rtf_source_offset": 1955993,
  "transforms_applied": [
    "rtf_parse"
  ],
  "strokes": [
    {"word": "Okay.", "stroke": "OE/KAEUFPLT"}
  ]
}

{
  "idx": 3496,
  "speaker": "Q.",
  "speaker_raw": "Q.",
  "text": "Once Yellow Rock 943 point on essentially as I understand it stopped paying attention to the reprocess data that happened in 2018, did they ever go back and look at this location in the context of the tome [owe|oh] seismic?",
  "paragraph_style": "s2",
  "continuation_of": 3495,
  "rtf_source_offset": 1956250,
  "transforms_applied": [
    "rtf_parse"
  ],
  "strokes": [
    {"word": "Once", "stroke": "WOPBS"},
    {"word": "Yellow", "stroke": "KAT"},
    {"word": "943", "stroke": "3#"},
    {"word": "point", "stroke": "POEUPT"},
    {"word": "on", "stroke": "O"},
    {"word": "essentially", "stroke": "SEPBGS/HREU"},
    {"word": "as", "stroke": "AS"},
    {"word": "I", "stroke": "EU"},
    {"word": "understand", "stroke": "-PBD/STAPBD"},
    {"word": "it", "stroke": "EUT"},
    {"word": "stopped", "stroke": "STOPD"},
    {"word": "paying", "stroke": "PAEUG"},
    {"word": "attention", "stroke": "A/TEPBGS"},
    {"word": "to", "stroke": "TOT"},
    {"word": "reprocess", "stroke": "SES"},
    {"word": "data", "stroke": "TKAEUT/A"},
    {"word": "that", "stroke": "THA"},
    {"word": "happened", "stroke": "HAPD"},
    {"word": "in", "stroke": "TPH"},
    {"word": "2018", "stroke": "1-8#"},
    {"word": ",", "stroke": "-RBGS"},
    {"word": "did", "stroke": "TK"},
    {"word": "they", "stroke": "THE"},
    {"word": "ever", "stroke": "-FR/-G"},
    {"word": "back", "stroke": "PWABG"},
    {"word": "and", "stroke": "APD"},
    {"word": "look", "stroke": "HRAO"},
    {"word": "at", "stroke": "AT"},
    {"word": "this", "stroke": "TH"},
    {"word": "location", "stroke": "HROEBGS"},
    {"word": "in", "stroke": "TPH-T"},
    {"word": "context", "stroke": "KOPB/TEBGS"},
    {"word": "of", "stroke": "-FT"},
    {"word": "tome", "stroke": "TOEPL"},
    {"word": "[", "stroke": "OE"},
    {"word": "seismic", "stroke": "PHEUBG"}
  ],
  "deletions": [
    {
      "position": 68,
      "strokes": ["PAEULG/A", "*"]
    }
  ]
}

{
  "idx": 3497,
  "speaker": "COLLOQUY",
  "speaker_raw": "COLLOQUY",
  "text": "MR. MADIGAN: Object to form.",
  "paragraph_style": "s5",
  "continuation_of": null,
  "rtf_source_offset": 1957579,
  "transforms_applied": [
    "rtf_parse"
  ],
  "strokes": [
    {"word": "Object", "stroke": "OB"},
    {"word": "to", "stroke": "TPORPL"},
    {"word": ".", "stroke": "-FPLT"}
  ]
}
```
