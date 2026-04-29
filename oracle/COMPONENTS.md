# COMPONENTS.md — Front-Matter Component Templates

**Date:** 2026-04-29
**Architect:** Opus
**Source files:**
- `oracle/frontmatter/halprin_frontmatter.txt` (FORMATTED — has line numbers + page numbers, full visual layout)
- `oracle/frontmatter/brandl_frontmatter.txt` (TEXT-ONLY — content stripped of formatting)

**KNOWN GAP — REVISIT TOMORROW:**
Brandl source was a text-only export. Need to extract `032626YELLOWROCK-FINAL.sgxr2`
from `MASTER_COPIES\ORACLES\BRANDL_MB_DELIVERABLE_ORIGINAL.zip`, open in
CaseCATalyst, export to formatted text. Then re-validate component visual
templates against true 2-example formatted comparison. Today's templates
are derived from 1 visual example (Halprin) + 1 content example (Brandl),
which is sufficient to identify slot variables but not 100% locked on
visual edge cases.

---

## METHOD

For each front-matter component, identify:
1. **TEMPLATE** — text/structure that's identical across both depos
2. **SLOT VARIABLES** — values that change per depo
3. **VISUAL FORMAT** — line/page numbering rules (from Halprin only, since Brandl is text-only)
4. **CURRENT DEFECT** — what's wrong in OUR_FINAL today
5. **DATA SOURCE** — where the slot values come from (RTF, .sgxml, or derived)

---

## COMPONENT 1 — COVER PAGE

### Template (identical text across both depos)

```
                  STATE OF LOUISIANA

                  PARISH OF CALCASIEU

                 14TH JUDICIAL DISTRICT

   * * * * * * * * * * * * * * * * * * * * * * * *
       <CASE_CAPTION_BLOCK>
   * * * * * * * * * * * * * * * * * * * * * * * *


                   VIDEOTAPED DEPOSITION
                           OF
                       <WITNESS_NAME>

                          taken on
                       <WITNESS_DATE>

                  commencing at <START_TIME>

                  <LOCATION_BLOCK>

           Reported By:  MARYBETH E. MUIR, CCR, RPR

   * * * * * * * * * * * * * * * * * * * * * * * *
```

### Slot Variables

| Slot | Halprin value | Brandl value | Source |
|------|---------------|--------------|--------|
| WITNESS_NAME | `RICHARD HALPRIN` | `BRAD SHAY BRANDL` | .sgxml metadata |
| WITNESS_DATE | `Thursday, April 2, 2026` | `Thursday, March 26, 2026` | .sgxml metadata |
| START_TIME | `9:04 a.m.` | `9:25 a.m.` | .sgxml metadata or videographer block |
| LOCATION_BLOCK | `at the offices of`<br>`SHER GARNER`<br>`909 Poydras Street`<br>`New Orleans, Louisiana` | `at the`<br>`THE POST OAK HOTEL`<br>`1600 West Loop South`<br>`Houston, Texas 77027` | .sgxml metadata |

### CASE_CAPTION_BLOCK (sub-component)

This is the YellowRock case caption. **Identical text** across Halprin and Brandl:

```
   YELLOW ROCK, LLC, et               Docket No.
   al,                                202-001594
              Plaintiffs,             Division "H"
       v.
   WESTLAKE US 2 LLC f/k/a
   EAGLE US 2 LLC et al.,
              Defendants.
```

**This is a per-CASE constant**, not per-depo. Same case = same caption.
For YellowRock case, this is fixed text. For other cases, this becomes a
template with its own slots (parties, docket, division).

### Visual Format Rules (from Halprin)

- Page 1, line numbers 1-25 down left margin
- Page number at top-right of each page
- Caption block: 2-column layout (party names left, docket info right)
- Headers (STATE OF / PARISH / DISTRICT) centered
- VIDEOTAPED DEPOSITION block centered

### Current Defect (from defect log)

**0428-1, 0428-2** — Caption block layout broken in OUR_FINAL.
The 2-column caption layout (party names left + docket right) is
currently rendering wrong. Cascade affects videotaped block and
appearances downstream.

### Data Source

- Witness, date, time, location: `.sgxml` metadata header
- Case caption text: per-case constant (today, hardcode YellowRock; later, per-case file)
- Court info (STATE/PARISH/DISTRICT): per-case constant

---

## COMPONENT 2 — INDEX

### Template (identical structure across both depos)

```
                       I N D E X
                                                Page
   Caption                                       <P>

   Appearances                                   <P>

   Stipulation                                   <P>

   Examination
        <COUNSEL_NAME>                           <P>


    Reporter's Certificate                      <P>

    Witness's Certificate                       <P>
                       * * * * * * * *

                      EXHIBITS

   <EXHIBIT_LIST>
```

### Slot Variables

| Slot | Halprin value | Brandl value | Source |
|------|---------------|--------------|--------|
| Caption page | `1` | `1` (always) | computed |
| Appearances page | `5` | (early) | computed |
| Stipulation page | `11` | `10` | computed |
| Examination counsel | `Mr. Caughey` | `Mr. Peacock` | first examiner from body |
| Examination page | `13` | `13` | computed |
| Reporter cert page | `296` | (end) | computed |
| Witness cert page | `298` | (end) | computed |
| EXHIBIT_LIST | (see C2a) | (see C2a) | exhibit metadata |

### Sub-component C2a — EXHIBIT entry

Each exhibit is one block:

```
Exhibit No. <N>  <DESCRIPTION>
                 <BATES_RANGE>            <PAGE>
```

Multi-line descriptions wrap with continued indent.

When exhibits overflow a page, repeat header on next page:

```
                       E X H I B I T S
   <continued exhibit list>
```

### Visual Format Rules (from Halprin)

- Page 2 of front-matter
- `I N D E X` centered with letter-spacing (one space between letters)
- Right-aligned page numbers in column
- `* * * * * * * *` separator before EXHIBITS section
- Multi-page exhibits use `E X H I B I T S` (letter-spaced) header on continuation pages
- Standard 25 lines per page, line numbers 1-25 down left margin

### Current Defect

Per Scott last night: "section exhibit index our appearances were a crime scene"
Index/exhibits is where you left off. Component spec covers this.
Specific defect lines TBD when we diff OUR_FINAL against this template.

### Data Source

- Page numbers: computed at finalization stage (after body is laid out)
- Examination counsel: first speaker after `EXAMINATION` marker in body
- Exhibit list: from `.sgxml` exhibit metadata + body markers
- Standard sections (Caption/Appearances/Stipulation/Certs): hardcoded labels

---

## COMPONENT 3 — APPEARANCES

### Template (identical structure across both depos)

```
   A P P E A R A N C E S:

   <APPEARANCE_BLOCK_1>

   <APPEARANCE_BLOCK_2>

   ...

   <APPEARANCE_BLOCK_N>

   ALSO PRESENT:

       <ALSO_PRESENT_LIST>

   Reported by:  Marybeth E. Muir,
                 Certified Court Reporter
                 In and for the State of
                 Louisiana and Registered
                 Professional Reporter
```

### Sub-component C3a — APPEARANCE_BLOCK

Each party representation is one block:

```
   <PARTY_LABEL>:
       <FIRM_NAME>
       <FIRM_ADDRESS_LINES>
       <FIRM_CITY_STATE_ZIP>
       <FIRM_PHONE>
       <ATTORNEY_EMAIL_LINES>
       BY: <ATTORNEY_NAME>, ESQ.<REMOTE_FLAG>
           <ADDITIONAL_ATTORNEY>, ESQ.<REMOTE_FLAG>
           ...
```

OR if no one attended for that party:

```
   <PARTY_LABEL>:
       <FIRM_NAME>
       <FIRM_ADDRESS_LINES>
       <FIRM_CITY_STATE_ZIP>
       <FIRM_PHONE>
       NOT PRESENT
```

### Slot Variables (per APPEARANCE_BLOCK)

| Slot | Example (Halprin) |
|------|-------------------|
| PARTY_LABEL | `ATTORNEY FOR PLAINTIFF` or `FOR THE DEFENDANTS, WESTLAKE US 2 LLC...` |
| FIRM_NAME | `SHER GARNER CAHILL RICHTER KLEIN & HILBERT, L.L.C.` |
| FIRM_ADDRESS_LINES | `909 Poydras Street` / `Suite 2800` |
| FIRM_CITY_STATE_ZIP | `New Orleans, Louisiana 70112` |
| FIRM_PHONE | `504.299.2100` |
| ATTORNEY_EMAIL_LINES | one or more email addresses |
| ATTORNEY_NAME | `THOMAS J. MADIGAN` |
| REMOTE_FLAG | empty, ` (Zoom)`, or ` (Via Zoom)` |

### Visual Format Rules (from Halprin)

- `A P P E A R A N C E S:` (letter-spaced) is a **header that repeats at the top of EVERY page** until appearances section ends
- Each `APPEARANCE_BLOCK` is kept together (no page split mid-block when possible)
- `BY:` line uses hanging indent — first attorney inline with `BY:`, additional attorneys aligned under first attorney name
- `(Zoom)` and `(Via Zoom)` both observed — should normalize to one form
- `Reported by:` block at end uses hanging indent for reporter description
- Standard 25 lines per page, line numbers down left margin

### Current Defect

**0428-3** — Appearances section is a "crime scene" in OUR_FINAL.
Likely failures:
1. Repeating `A P P E A R A N C E S:` header on continuation pages
2. Block-keep-together (no mid-block page splits)
3. Hanging indent on `BY:` lines
4. (Via Zoom) vs (Zoom) inconsistency — both observed in MB output, normalize
5. Email line grouping (one block per attorney's email under firm)

### Data Source

- All appearance data: `.sgxml` metadata + manually-entered MB appearance block
- `.sgxml` should have a `<appearances>` node with party/firm/attorney structure
- If not in `.sgxml`, source is the raw RTF appearances section

---

## COMPONENT 4 — STIPULATION

### Template (NEAR-IDENTICAL across both depos — Louisiana standard)

```
                S T I P U L A T I O N


           It is stipulated and agreed by and between

   Counsel that the testimony of the witness, <WITNESS_NAME>,

   is hereby being taken pursuant to Notice under the

   Louisiana Code of Civil Procedure for all purposes

   permitted under law.


           The witness <READ_SIGN_LANG>.  The original is to be

   delivered to and retained by <RETAINING_COUNSEL>, for

   proper filing with the Clerk of Court.


           All objections, except those as to the form

   of the questions and/or responsiveness of the

   answers, are reserved until the time of the trial of

   this cause.

                       *  *  *  *  *

           Marybeth E. Muir, Certified Court Reporter

   in and for the State of Louisiana and Registered

   Professional Reporter, officiated in administering

   the oath to the witness.
```

### Slot Variables

| Slot | Halprin value | Brandl value |
|------|---------------|--------------|
| WITNESS_NAME | `RICHARD HALPRIN` | `BRAD SHAY BRANDL` |
| READ_SIGN_LANG | `reserves the right to read and sign the deposition` | `waives the right to read and sign the deposition` |
| RETAINING_COUNSEL | `RYAN CAUGHEY, ESQ.` | `"TREY" PEACOCK, ESQ.` |

### Visual Format Rules (from Halprin)

- `S T I P U L A T I O N` (letter-spaced) header centered
- Body text indented from line numbers
- `*  *  *  *  *` separator before reporter swearing-in paragraph
- Standard 25 lines per page

### State-specific Note

This is the **Louisiana standard stipulation** language. State module
(`MASTER_DEPOSITION_ENGINE_v4` Louisiana module) should own this template.
For NJ Workers' Comp module, this would be different boilerplate.

### Current Defect

**0428-5 (P1 in defect log)** — Stipulation paragraph **STRIPPED OUT** by pipeline.
Pipeline bug: text exists in raw RTF, gone in OUR_FINAL. Need Stage 1to5
trace to find which stage drops it. **Independent of component template work
— this is a pipeline bug.**

### Data Source

- Boilerplate text: state module constant
- WITNESS_NAME: from .sgxml or first capitalized witness mention
- READ_SIGN_LANG: from raw RTF (parse "reserves" vs "waives")
- RETAINING_COUNSEL: from raw RTF

---

## COMPONENT 5 — VIDEOGRAPHER OPENING (post-stipulation)

### Template (similar structure across both depos)

```
              MR. <STIP_COUNSEL>:  <STIP_REMARKS>

              THE VIDEOGRAPHER:  We are now on the
           record.  Today's date is <DATE>.
           The time is approximately <TIME>.  My
           name is <VIDEOGRAPHER_NAME> with <VIDEO_FIRM>
           and the court reporter is Marybeth Muir,
           also with <REPORTER_FIRM>.  This is the video
           deposition of <WITNESS_SHORT_NAME> in the matter
           of <CASE_NAME>,
           in the State of Louisiana, Parish of
           Calcasieu, Docket No. <DOCKET_NO>
           Division "<DIVISION>".

              Counsel, please identify themselves
           for the record, after which the court
           reporter will swear in the witness and we
           may continue.

              THE COURT REPORTER:  All appearances
           are noted for the stenographic record.


                      <WITNESS_FULL_NAME>,
              <WITNESS_ADDRESS>, <WITNESS_EMAIL>,
              having been first duly sworn, was
              examined and testified as follows:
```

### Slot Variables

| Slot | Halprin value | Brandl value |
|------|---------------|--------------|
| STIP_COUNSEL | `GARNER` | `MADIGAN`, `GUILLOT`, etc. (multi-counsel) |
| STIP_REMARKS | `The usual stipulations. We disagree with the Reservation of Rights of the insurers.` | (multiple back-and-forth) |
| DATE | `April 2nd, 2026` | `March 26th, 2026` |
| TIME | `9:09 a.m.` | `9:25 a.m. Central` |
| VIDEOGRAPHER_NAME | `Darrein Guastella` | `Brian Smith` |
| VIDEO_FIRM | `Lexitas` | `Lexitas` |
| REPORTER_FIRM | `Lexitas` | `Lexitas` |
| WITNESS_SHORT_NAME | `Rick Halprin` | `Brad Brandl` |
| WITNESS_FULL_NAME | `RICHARD HALPRIN` | `BRAD SHAY BRANDL` |
| WITNESS_ADDRESS | `9757 Lemonwood Terrace, Boynton Beach, Florida, 33437` | `32 County Road 269, Moulton, Texas 77975` |
| WITNESS_EMAIL | `rhalprin@whitetopllc.com` | `brad.brandl@yahoo.com` |
| CASE_NAME | `Yellow Rock, LLC, et al. v. Westlake US 2, LLC, f/k/a Eagle US 2, LLC, et al` | (same) |
| DOCKET_NO | `202-001594` | `202-001594` |
| DIVISION | `H` | `H` |

### IMPORTANT FINDING — Brandl shows MULTI-PARTY STIPULATION DIALOG

Brandl front-matter shows several attorneys exchanging stipulations BEFORE
the videographer reads the record. Halprin shows just ONE counsel making a
brief stipulation statement.

This means the post-stipulation block isn't a fixed template — it's a
**variable-length dialog** where each speaker block follows the standard
speaker turn pattern from the body. Component should treat this as
"continuation of pre-record discussion" rather than a fixed template.

### Current Defect

Not directly in defect log, but cascade from 0428-1/2/3 (cover/videotaped/appearances).
Once cover + appearances are right, videographer opening should fall into place.

### Data Source

- All speaker turns: raw RTF body content (just the part before formal Q&A)
- Witness sworn block: standard pipeline output (already works in OUR_FINAL)

---

## COMPONENT 6 & 7 — REPORTER'S CERTIFICATE / WITNESS'S CERTIFICATE

**NOT IN FRONT-MATTER FILES** (they appear at end of depo, not page 1-12).
Deferred — handle in separate component spec when we get to back-matter.
Both are state-specific boilerplate (Louisiana R.S. 37:2554 territory).

---

## SUMMARY — WHAT WE LEARNED FROM 2 DEPOS

### Confirmed templates (high confidence)
1. **Cover page** — fixed structure, witness/date/location/counsel are slots
2. **Case caption block** — per-case constant (YellowRock = identical text)
3. **Index** — fixed structure, page numbers + counsel name + exhibit list are slots
4. **Stipulation** — Louisiana standard language with 3 small slots (witness, read/sign verb, retaining counsel)
5. **Appearances** — fixed `BY:` indent pattern, hanging indents, repeated `A P P E A R A N C E S:` header per page

### Variables (per depo)
- Witness identity (name, address, email, date, time)
- Examining counsel (drives index entries + first speaker block)
- Retaining counsel (in stipulation)
- Read/sign vs reserve/sign (witness's choice)
- Appearance blocks (ordered list of party representations)
- Exhibit list (variable count + descriptions)
- Page numbers (all computed)

### Per-CASE constants (YellowRock specific)
- Case caption text (parties, docket, division)
- Court venue (LA / Calcasieu / 14th JD)
- The list of parties/firms/insurers (subset of these will appear in any given depo's appearances)

### Per-CR constants (MB specific)
- Reported By: `MARYBETH E. MUIR, CCR, RPR`
- Reporter's signature block boilerplate
- Index format style (Halprin shown — need formatted Brandl to confirm)

### Per-STATE constants (Louisiana specific)
- Stipulation boilerplate language ("Louisiana Code of Civil Procedure for all purposes permitted under law")
- Reporter's certificate format (R.S. 37:2554)
- Court reporter swearing-in language

---

## NEXT STEPS — BUILD ORDER FOR SONNET

Tier 1 (today, in order):
1. **Cover component** — most visible, simplest data sources, biggest visual win
2. **Stipulation component** — fix the strip-out bug (P1) AND build the template
3. **Appearances component** — most complex, biggest cascade impact

Tier 2 (after Tier 1 ships):
4. **Index component** — needs page numbers, depends on body finalization
5. **Videographer opening** — cascade from 1-3 above
6. **Certificates** — back-matter, separate work

---

— End of COMPONENTS.md —
