# Front Matter Intake Package — TODO before 2026-05-13

Scott has been asking for this for 6 weeks. Locking it now.

## What it is
A bundle MB sends MRX before a new depo runs. Contains the 5 things MRX needs to produce front matter without a FINAL.

## The 5 inputs
1. Case metadata (court, case number, parties, date, location) — from Notice of Deposition
2. Witness info (name, role) — from Notice of Deposition
3. Appearances (lawyer names, firms, who they represent) — MB types or pulls from Notice
4. Proceeding type (deposition, arbitration, hearing) — from Notice of Deposition
5. Reporter profile (already in MRX, never changes per depo)

## Definition
Notice of Deposition = legal document sent by the lawyer scheduling the depo. Contains case info, witness, date, location, proceeding type. MB receives a copy before the depo.

## Deliverable
A Halprin intake sample folder showing MB what MRX needs. Real data, real shape. This becomes the template.

## Open decisions
- Format: Excel form, JSON, fillable PDF, or other
- Build owner: Sonnet (has Halprin data)
- Due: before 2026-05-13
