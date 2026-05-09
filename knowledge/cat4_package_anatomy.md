# CaseCATalyst Package Anatomy

Documents the file formats present in a CaseCATalyst (Cat4) deposition package,
their readability without Cat4, and their value for fingerprinting.

## Format table — verified

| Extension | Magic bytes | Format | Readable without Cat4? | Fingerprint value |
|---|---|---|---|---|
| .sgxml | <?xml | Plain XML, UTF-8 | YES — fully | HIGH (job metadata, jurisdiction, parties, witness, save path) |
| .tlx | #LID | Plain text, tab-delimited | YES — fully | MEDIUM (case word list / proper nouns) |
| .sgglb | SGCAT32 | Binary proprietary | PARTIAL (ASCII strings recoverable via binary grep) | MEDIUM (global dict — names, entities) |
| .sgdct | SGCAT32 | Binary proprietary | NO | HIGH if accessible (MB's personal dict — Cat4 export needed) |
| .sgdcg | SGCAT32 | Binary proprietary | NO | LOW (untranslates) |
| .sgdcx | SGCAT32 | Binary proprietary | NO | LOW (index) |
| .rtf | RTF | Rich Text Format (exported) | YES | PRIMARY engine input |
| .opus | OPUS | Audio | YES (with Whisper) | Stage 4 only |
| .sgstn | Steno | Cat4 binary | NO | Pre-translation truth, debug only |
| .sgngl | Text | Cat4 internal | Same data as RTF | Use RTF instead |
| .sgxr2 | (often empty) | Cat4 internal | N/A — observed 0 KB | IGNORE if 0 KB |

## Verified findings — jp_042726 package

- `.sgxml` contains: job history, audio timestamps, speaker definitions, save history (`C:\Cat4\usr\Mary Beth`, 3 saves), 212 pages / 424 folios, `Creation-PLO` field = `CRLA` confirming Louisiana jurisdiction
- `.tlx` header: `#LID 24941`, then tab-separated word list (`Abar\ti`, `Bannergy\ti` format)
- `.sgglb` embedded ASCII strings recoverable: Yellow Rock, JP Morgan, JP Morgan Chase, MR. SLOCUM, MR. ANDRADE, MR. TSCHUMI, MR. LORIO, MR. FILIP, Sulphur Dome LLC, Verisk, Compra Media, Stilwicki
- Recon method: PowerShell `Get-Content -Encoding Byte -TotalCount 8` for magic bytes; binary grep for ASCII strings in SGCAT32 files
