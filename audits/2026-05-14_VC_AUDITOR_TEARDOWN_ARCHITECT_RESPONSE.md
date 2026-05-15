# Architect Response to VC Auditor Teardown — 2026-05-14

**Frame:** Architect's hole-by-hole response to the 10-hole VC auditor teardown captured earlier this evening. Code-side only. Business-side responses (HOLE 5 CR#2, HOLE 8 business case, HOLE 10 moat narrative) parked for separate work.

**Operating principle Scott set tonight:**
> "I don't want to hear good news until it's good news. Until then we grind, we disrupt, we stay paranoid. We assume we suck until we don't."

This response does not soften the auditor. Where the hole is fair, we say so and queue the fix.

---

## HOLE 1 — "You don't have an engine, you have a pile of fixes."

**Verdict: Fair today.** 5 weeks into a 6-month build. Halprin was the learning phase. Stage A is the foundation phase. Auditor is evaluating a half-poured foundation as if it were a house. Counter is structural, not defensive: evaluate at month 6, not month 5. Until then we accept the criticism and keep building.

---

## HOLE 2 — "Stage A measures noise, not skill."

**Verdict: Partially answered tonight, mostly still open.** When audit was written we only had the 4-pair run dominated by whitespace. Tonight's 9-pair hunt with anti-fail filters surfaced em_dash_inserted at 100% across all depos, all '--' form. That is not noise — that is a habit. But one pattern is not an engine. Round 2 (14 pairs) tells us if the method scales. Round 3 (CR #2 data) tells us if it generalizes.

**Action:** Run round 2 on 14 pairs Friday. Re-evaluate this hole after.

---

## HOLE 3 — "Comprehension Agent is one expensive call from being a hallucination machine."

**Verdict: Sharpest hit. Fully fair.** No verification layer on the Brief is a real gap. The Brief becomes source of truth for 60 downstream batches. If wrong on a witness name, firm name, or key term, every downstream batch silently propagates the error.

**Mitigations to design into Stage C spec:**
1. **Brief validator** — second cheaper call that checks each Brief claim against source documents before it locks
2. **Human-in-the-loop checkpoint** — Scott or MB eyeballs the Brief before downstream batches consume it (cheap, slow)
3. **Per-claim confidence scores** in the Brief — high-confidence claims auto-trust, low-confidence flagged for review

**Action:** Stage C spec must include Brief validator design before any build starts. Hole stays open until spec ships.

---

## HOLE 4 — "Three-agent separation is a slogan."

**Verdict: Half FUD, half fair.** The slogan part is fair — three agents don't enforce a wall just by existing. Fair part is the test harness. No proof the wall holds under adversarial inputs.

**Mitigations:**
1. **Adversarial test harness** — feed Reader bad input, prove Arbiter doesn't propagate, prove Writer can't reinterpret
2. **Output file separation** — each gate writes its own file; no in-memory state passed between agents
3. **Independent prompt review** — Reader/Arbiter/Writer prompts reviewed by different sessions to surface shared blind spots

**Action:** Adversarial test harness is a v0.2 deliverable. Cannot ship Stage C without it.

---

## HOLE 5 — "Market of one."

**Verdict: Fair short term, FUD medium term.** MB is the calibration source, not the customer base. Architecture was explicitly built so CR #2 onboards by running the same Aligner+Differ on their pairs. Legitimate criticism: CR #2 onboarding hasn't started.

**Code-side action:** Run Stage A on AD data (already have it) once MB.yaml v0.1 ships. Prove the fingerprint transfers — or learn what we got wrong. This is a Stage A v0.2 task, not a future task.

Business-side (CR #2 timeline) parked.

---

## HOLE 6 — "Whisper is not the safety net you think it is."

**Verdict: Fair, but auditor strawmanned our use case.** Whisper on cross-talk + accents + legal jargon will fail. Counter: Whisper does not have to be the oracle. It has to be a *second source* for disagreement detection. When steno and Whisper agree, trust. When they disagree, flag for human review. That is a much lower bar than "Whisper must be accurate."

**Open question:** What is Whisper's actual disagreement rate on deposition audio? We don't know. The AUDIO_SYNC_RECON parked for 3 weeks would answer part of this.

**Action:** Run Whisper on Halprin audio as part of AUDIO_SYNC_RECON. Measure disagreement rate against steno. Hole stays partially open until measured.

---

## HOLE 7 — "AUDIO_SYNC_RECON parked for 3 weeks."

**Verdict: Fully fair.** We committed to whole-file Whisper without measuring the alternative. Reason was whole-file is acceptable worst case (~$2-3/depo). Auditor's point: know before commit. He's right. One-day recon task. No excuse to keep parking.

**Action:** Run AUDIO_SYNC_RECON before any Stage B build. Friday or Saturday work.

---

## HOLE 8 — "No business model in this conversation."

Parked. Business-side response owed separately.

---

## HOLE 9 — "Founder is the bottleneck."

**Verdict: Brutally fair. Most dangerous hole because it's structural.**

**Code-side mitigations already in place:**
- Every spec in repo, not Scott's head
- Every decision has a ledger row with rationale
- Every handoff captures state so fresh agent can resume
- MANIFEST.md (planned, not yet built) will index all critical files

**Code-side mitigations still needed:**
- Decision criteria documentation — when does Scott's judgment kick in vs auto-apply? Currently undocumented.
- Calibration playbook — step-by-step how to onboard CR #2 without Scott in the loop
- Test coverage that proves the system behaves correctly without architect intervention

**Open structural question:** The *judgment* layer (is this MB style or LA jurisdiction? does this signal matter?) currently only Scott can make. That needs to become teachable. Either MB becomes co-pilot, or we encode judgment into the system, or we accept bus-factor risk and disclose it. No quick fix. Acknowledge and plan.

**Action:** Calibration playbook is a Stage A v0.2 deliverable. Bus-factor disclosure goes in investor conversations.

---

## HOLE 10 — "Your moat is a frequency table."

**Verdict: Partially FUD, partially fair.** Frequency table is not the moat — agreed, anyone can build one. The moat is workflow trust + per-CR calibration history + audit trail. Veritext cannot replicate the trust relationship overnight. But auditor is right that the *code* is not the moat.

Business-side narrative owed separately.

---

## Summary

| Hole | Verdict | Code action |
|---|---|---|
| 1 | Fair today | Keep building; evaluate at month 6 |
| 2 | Partially answered | Round 2 on 14 pairs Friday |
| 3 | Fully fair | Brief validator in Stage C spec |
| 4 | Half FUD, half fair | Adversarial test harness for v0.2 |
| 5 | Fair short term | Run Stage A on AD data after MB.yaml v0.1 |
| 6 | Fair, strawmanned | Measure Whisper disagreement rate in AUDIO_SYNC_RECON |
| 7 | Fully fair | Run AUDIO_SYNC_RECON before Stage B build |
| 8 | Business — parked | n/a |
| 9 | Brutally fair | Calibration playbook + decision criteria docs |
| 10 | Partially FUD | Business — parked |

**Code-side queue added tonight:**
1. Brief validator design (Stage C spec gate)
2. Adversarial test harness for 3-agent wall (v0.2)
3. AUDIO_SYNC_RECON run (Friday or Saturday)
4. Stage A run on AD data after MB.yaml v0.1
5. Whisper disagreement rate measurement
6. Calibration playbook for CR #2 onboarding
7. Decision criteria documentation

**Operating principle going forward:**
Iron trap stays shut. Assume we suck until the data says otherwise. We grind, we disrupt, we stay paranoid.

— End of architect response —
