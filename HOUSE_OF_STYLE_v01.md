# HOUSE OF STYLE — Architecture Naming Convention
**Established:** 2026-04-28 v01
**Status:** Naming locked. Architecture deferred to v0.2 design phase.

## The Name
"House of Style" is the umbrella term for the layered formatting
architecture that drives transcript output. The phrase is industry-
native — every working CR talks about their work product as their
"house style." Adopting the term aligns the engine with how CRs
actually think about their craft.

## The Layers
House of Style
├── State Floor
│   └── Legal minimum every CR in the jurisdiction must meet.
│       Sourced from state regulations (LA Admin Code, 22 NYCRR
│       § 108.3, NJ AOC, etc.). Defines: lines per page, Q/A
│       indent positions, colloquy positions, cover page required
│       elements, certificate language, index requirements.
│
├── CR House Style
│   └── How each individual CR customizes within their state's
│       rules. Sourced from the CR's CaseCATalyst (or Eclipse,
│       ProCAT) format file. Defines: cover template, cert
│       template, errata template, errata wording, signature
│       block, preferred indent values within the state-allowed
│       ranges, header/footer text, etc.
│
└── Depo Overrides
    └── Per-job customizations. Rare. Defines: one-off client
        requests, multi-volume conventions, special exhibit
        handling, etc.

## How v0.2 Resolves a Format

For any given depo:

1. Look up StateProfile from case_info.case.jurisdiction.state +
   proceeding type (deposition / official court).
2. Layer CR's FormatProfile on top — overrides allowed only
   within state-permitted ranges.
3. Apply DepoOverride if specified in case_info.

Module 7 (page_layout) and Module 6 (document_composer cover/
appearances/cert/errata builders) read the resolved profile,
not hardcoded constants.

## Reference Material Already Gathered

- STATE_TRANSCRIPT_FORMAT_SPECS.md (LA, NY, NJ comparison —
  Scott shared this file 2026-04-28).
- Louisiana Engineering and NJ Workers' Comp state modules
  already exist in MASTER_COPIES (per memory).
- MB's actual CaseCATalyst format file — Scott extracts
  tomorrow from his licensed CAT install.

## Onboarding Implication

CR onboarding bundle now requires four artifacts (was three):
1. Raw RTF
2. Audio
3. FINAL.txt (gold standard)
4. CaseCATalyst format file (the CR's house style)

Item 4 unlocks the FormatProfile layer of House of Style.

## Pitch Language

"Send us your house style and your first depo. The next depo
we hand back will look like you wrote it."

— End House of Style note —
