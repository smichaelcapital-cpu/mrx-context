# Front Matter Recon Report — Phase 1

**Date:** 2026-05-10 (evening)
**Author:** Sonnet (evening instance)
**Status:** COMPLETE — hard checkpoint, awaiting Scott's go for Phase 2

---

## 1. Depos Sampled

7 training depos, different cases, 2022–2025 spread. All `.txt` finals from `C:\Cat4\usr\scott\`. Non-yellowrock.

| Stem | Year | Court Type | State/Federal |
|---|---|---|---|
| 101322blanks | 2022 | USDC Eastern District of Louisiana | Federal |
| 102622moore | 2022 | USDC Eastern District of Louisiana | Federal |
| 051823krunchy | 2023 | USDC Western District (Lafayette Div) | Federal |
| 061824calhoun | 2024 | — (pdf, skipped for .txt study) | — |
| 091724ketchand | 2024 | 21st Judicial District, Tangipahoa | State |
| 051524church | 2024 | USDC Eastern District of Louisiana | Federal |
| 021225barnett | 2025 | USDOL Office of Administrative Law Judges | Federal |
| 021725allen2 | 2025 | 23rd Judicial District, St. James Parish | State |

Halprin (yellowrock, 14th Judicial Calcasieu, state) used as reference.

---

## 2. Section-by-Section Classification

### Cover Page (Page 1)

**Structure is consistent across all 8 depos.** All use: two leading blanks + page number at col 60 + 25 numbered content lines (with continuation lines).

| Line range | Content | Classification |
|---|---|---|
| Lines 1–3 | Court name and jurisdiction (e.g. "21ST JUDICIAL DISTRICT COURT / FOR THE PARISH OF TANGIPAHOA / STATE OF LOUISIANA") | **PER-CASE** |
| Lines 3–9 (caption block) | Parties, docket/case number, judge, division | **PER-CASE** |
| Star separators | `* * * * * ...` — same character, same width across all | **PER-CR** (layout constant) |
| Lines 13–15 | Deposition type + OF + witness name | **PER-DEPO** |
| Lines 15–16 | "taken on" + date | **PER-DEPO** (see surprise #1) |
| Lines 16–17 | "commencing at" + time | **PER-DEPO** |
| Lines 17–20 | Location prefix + firm + address + city/state | **PER-DEPO** |
| "Reported By: MARYBETH E. MUIR, CCR, RPR" | Identical across all 8 depos | **PER-CR** |

### Index Page (Page 2)

**Structure consistent, content varies by depo.**

| Element | Classification |
|---|---|
| `I N D E X` header | **PER-CR** (layout constant) |
| Section entries (Caption, Appearances, Stipulation, Examination) | **PER-DEPO** (page numbers) |
| Presence/absence of Stipulation entry | **PER-DEPO** (barnett: stipulation page exists but not in index — inconsistency in source) |
| Exhibit list | **PER-DEPO** / **PER-CASE** (Halprin: 20+ exhibits; most others: 0–5) |
| Reporter's/Witness's Certificate entries | **PER-DEPO** (present in some, absent in others) |

### Appearances Section (Pages 3–N)

**Page count varies significantly: 1 page (ketchand) to 6 pages (Halprin).**

| Element | Classification |
|---|---|
| `A P P E A R A N C E S:` header, repeated on each page | **PER-CR** (layout constant) |
| Party labels, firms, addresses, phones, emails, attorneys | **PER-CASE** |
| `(Zoom)` / `(Via Zoom)` / `NOT PRESENT` flags | **PER-DEPO** |
| Last appearances page "Reported by: Marybeth E. Muir, / Certified Court Reporter / In and for the State of / Louisiana and Registered / Professional Reporter" block | **PER-CR** |
| Videographer entry ("ALSO PRESENT: Antonio Woodward, Videographer") | **PER-DEPO** |

### Stipulation Page

**Present in all 8 depos. One page in all sampled cases.**

| Element | Classification |
|---|---|
| `S T I P U L A T I O N` title | **PER-STATE** (Louisiana boilerplate) |
| Para 1: "It is stipulated and agreed... testimony of the witness, [NAME], is hereby being taken pursuant to Notice under the Louisiana Code of [Civil/Federal] Procedure..." | **PER-STATE** (boilerplate frame) + **PER-DEPO** (witness name, "Civil" vs "Federal" — see surprise #3) |
| Para 2: "[Witness] [reserves/waives] the right to read and sign... delivered to and retained by [ATTORNEY], ESQ..." | **PER-DEPO** (read/sign choice + retaining attorney) |
| Para 3: "All objections, except those as to the form of the questions and/or responsiveness of the answers, are reserved until the time of the trial of this cause." | **PER-STATE** (Louisiana boilerplate, appears identical across all) |
| Reporter line: "Marybeth E. Muir, Certified Court Reporter in and for the State of Louisiana..." | **PER-CR** |

### Videographer Opening Page

**Optional — present in 3 of 8 depos (Halprin, blanks, krunchy). Absent in others.**

| Element | Classification |
|---|---|
| Presence/absence of this page | **PER-DEPO** (videotaped depos only) |
| Pre-record counsel remarks block (e.g. "MR. GARNER: The usual stipulations...") | **PER-DEPO** (variable speaker, variable length) |
| Videographer monologue (date, time, video firm, case name, docket, division, court venue) | **PER-DEPO** slots + **PER-CASE** constants |
| Witness sworn-in block (full name, address, email) | **PER-DEPO** |

---

## 3. Surprises

### Surprise #1: Cover page layout varies around "taken on"

6 of 7 sampled depos have `taken on` on a separate line before the date. Church (051524) goes directly to the date without `taken on`. This is a per-depo formatting variation. The cover page template needs to handle optional `taken on` text — it cannot be hardcoded as always present.

**Impact:** Minor. The `taken on` flag needs to be a per-depo data field.

### Surprise #2: Videographer section is optional and highly variable

Halprin has a full videographer page with pre-record counsel discussion. Blanks has a videographer page with a different opening (no pre-record discussion, direct videographer monologue). Non-videotaped depos have no videographer page at all.

The pre-record counsel block (e.g. "MR. GARNER: The usual stipulations. We disagree with the Reservation of Rights...") is unique to each depo. It cannot be templated — it must be pulled from the raw RTF.

**Impact:** Significant. The videographer opening cannot be generalized as a single slot-based template. The counsel-pre-record block needs to come from the raw RTF. The videographer monologue block has predictable slots (date, time, videographer name, firm, witness, case, docket, division, court) but the pre-record discussion does not.

**This does NOT fail the model** — but it pushes the videographer component from "slot template" to "hybrid: raw RTF pre-record + slot-based videographer monologue."

### Surprise #3: "Code of Civil Procedure" vs "Code of Federal Procedure" varies

The stipulation para 1 contains "pursuant to Notice under the Louisiana Code of [X] Procedure." Two depos say "Federal Procedure" (blanks, ketchand); barnett says "Civil Procedure." This variation does not correlate clearly with court type (ketchand is state court but uses "Federal"). This text is NOT reliably per-state boilerplate — it's a per-depo slot. The prior treatment as a frozen per-state literal is wrong.

**Impact:** The `per-state/louisiana.json` should NOT include the full paragraph 1 as a literal. It should include the frame and expose `procedure_code` (either "Civil" or "Federal") as a per-depo slot. In practice this is likely always in the source RTF.

### Surprise #4: Caption block format differs between federal and state cases

Federal cases (USDC, USDOL) use a two-column layout with party info on the left and CIVIL ACTION NO/JUDGE/MAGISTRATE on the right. State cases (14th, 21st, 23rd Judicial) use a different layout with DOCKET NO and DIVISION. Both formats appear in MB's work. These are both per-case, but they have different layout templates — not just different slot values.

**Impact:** Phase 2 per-case JSON structure needs a `court_type` field (`federal` vs `state`) to select the right caption layout template. The caption block itself is not a single universal template.

### Surprise #5: Appearances page count is highly variable

Halprin: 6 pages (pages 5–10). Blanks: 2 pages. Ketchand: 1 page. Barnett: 2 pages. The spec's `appearances.json` data file must store the full set of appearance blocks (variable count), and the template must paginate them, not assume a fixed page count.

**Impact:** Phase 2 design for `appearances` data needs to be a list of blocks, not a fixed structure. Phase 3 template must implement pagination. This was already noted in the TODOs in `appearances_page.py`.

---

## 4. What Fits the Four-Kind Model

| Section | Model fit |
|---|---|
| Per-state: LA objections clause (para 3 of stipulation) | HOLDS — identical across all LA depos |
| Per-state: `S T I P U L A T I O N` title | HOLDS |
| Per-CR: Reporter name/credentials line | HOLDS — identical across all 8 |
| Per-CR: `A P P E A R A N C E S:` header | HOLDS |
| Per-CR: Reported by block on last appearances page | HOLDS |
| Per-CR: Star separator format | HOLDS |
| Per-case: Court name/jurisdiction (lines 1–3) | HOLDS |
| Per-case: Caption block (parties, docket, division) | HOLDS — but needs federal vs state layout flag |
| Per-case: Appearances blocks (firms, attorneys, etc.) | HOLDS |
| Per-depo: Witness, date, time, location | HOLDS |
| Per-depo: Read/sign choice + retaining attorney | HOLDS |
| Per-depo: Videographer presence/absence | HOLDS |
| Per-depo: `taken on` presence/absence | HOLDS (with that slot in data) |
| Per-depo: Procedure code ("Civil" vs "Federal") | HOLDS (with that slot in data) |

**Every line in every depo classifies into one of the four kinds.** The model is sound.

---

## 5. Verdict

**MODEL HOLDS.**

The four-kind classification covers all front matter lines across 7 diverse MB depos spanning 2022–2025 and multiple court types. No depo has a section that doesn't fit the model.

Five surprises documented (Surprises #1–5). None breaks the model. All are refinements: optional fields, variable-length lists, and one layout fork (federal vs state caption). The biggest architectural note is that the videographer pre-record discussion cannot be templated — it must come from the raw RTF.

The model is sound enough to proceed to Phase 2.

---

## Appendix: File Paths Checked

```
C:\Cat4\usr\scott\101322blanks-FINAL.txt        (USDC E/LA, 2022)
C:\Cat4\usr\scott\102622moore-FINAL.txt         (USDC E/LA, 2022)
C:\Cat4\usr\scott\051823krunchy-FINAL.txt       (USDC W/LA, 2023)
C:\Cat4\usr\scott\091724ketchand-FINAL.txt      (21st Jud, 2024)
C:\Cat4\usr\scott\051524church-FINAL.txt        (USDC E/LA, 2024)
C:\Cat4\usr\scott\021725allen2.txt              (23rd Jud, 2025)
C:\Cat4\usr\scott\021225barnett-FINAL.txt       (USDOL ALJ, 2025)
Halprin (reference): io/analysis/halprin_full/_stage5_out/halprin_full.OUR_FINAL.txt
```
