Here. Handoff is taking shape — was being careful with it given how much we covered tonight. Let me deliver what I have.
I'll send it in two parts because it's long:
Part 1 (this message): The Opus → Opus resume note (the "in my head" doc)
Part 2 (next message): The structured session findings doc + final tomorrow-morning checklist

PART 1 — OPUS → OPUS RESUME NOTE
Save to: C:\Users\scott\OneDrive\Documents\mrx-context\handoffs\OPUS_TO_OPUS_2026-04-29_RESUME.md
markdown# OPUS → OPUS — RESUME NOTE — written 2026-04-28 EOD

## TO YOU, FRESH OPUS, FROM ME, TIRED OPUS

Read this AFTER the standard ramp. Standard ramp tells you the state.
This note tells you what's IN MY HEAD that didn't fit the structured
handoff.

## SCOTT IS COOKED — AGAIN

Long session. He worked his day job, then 5+ hours on this. Pushed
through to a clean stopping point because he wanted tonight's work
SAFE for tomorrow. Honor that. Do not make him chase paths. Do not
ask him to re-source what he gave us tonight.

If he opens with "ramped" — your response is short, three things on
deck, ready to go. He hates fire-hose responses when tired.

## THE BIG REFRAME (DO NOT LOSE)

Late tonight Scott pushed back on my framing of front-page work as
"sub-row layout primitive." He was right.

THE REFRAME: MB's front-matter is NOT a layout problem. It is a
TEMPLATE problem.

- Cover, Stipulation, Appearances, Index, Witness Cert, Reporter Cert,
  Errata — these are COMPONENTS. Lego blocks.
- Each MB depo uses the same components with different variables
  filled in (case caption, attorneys, date, witness).
- Building a "general layout primitive" is overengineering. Building
  a component template library is right-sized.

This reframe came from Scott noticing he'd given us multiple MB
finals and that across them, the front-matter LOOKS THE SAME. Cover
is cover. Stipulation is stipulation. Pattern recognition.

THIS REFRAME LINES UP WITH:
1. The product thesis ("AI gets to ~90%, human polishes"). Templates
   correctly populated = that 90% on front-matter.
2. The onboarding plan ("every new CR supplies a complete training
   triplet"). The triplet's value isn't training data — it's
   COMPONENT EXTRACTION. We learn each new CR's component shapes.
3. The Louisiana Engineering / NJ Workers' Comp module work. Each
   state has its own boilerplate (Article 1434 stipulation, R.S.
   37:2554 certificate). State modules ARE the per-state component
   library.

DO NOT REVERT TO LAYOUT-PRIMITIVE FRAMING. If you find yourself
specifying CAPTION_ROW or sub-row helpers as the primary architecture,
STOP. The primitive is fine as an implementation detail INSIDE the
cover component. But the architecture is component templates.

## TONIGHT'S OTHER REAL WINS

1. Recon methodology proven. Structural recon (raw → MB → ours
   three-way diff) before any spec catches direction reversals. Saved
   us from shipping wrong direction multiple times tonight.

2. Dictionary thread RESOLVED.
   - Job dictionary located: 040226yellowrock-ROUGH.rtf, 5,289 bytes
   - Already byte-identical to our existing test fixture
   - dictionary_loader.py exists and works
   - BUT: NOT WIRED at runtime. Runner passes {} to LLM at line 267
     of _run_halprin_mini.py
   - Two-line fix available. Wire it tomorrow.
   - WARNING: Wiring will NOT fix B2 or B5. Those terms aren't in
     job dict. They're in MB's career-built system dict which we do
     not have access to. Wiring is correct housekeeping but not the
     silver bullet for anomalies.

3. Audio architecture decision deferred no longer needed urgently.
   - .sgxml has 88 paragraph-level timestamps
   - Sufficient for Scott's stated nav goal ("click flagged word →
     land within 2-3 sentences")
   - AUDIO_SYNC_RECON spec is collapsed. Not needed. We have the data.
   - This frees up tomorrow's bandwidth for the component work.

4. Defect log committed. specs/2026-04-28_DEFECT_LOG_HALPRIN_FRONT_PAGES.md.
   Comprehensive. Future you can read it cold.

5. Oracle folder established.
   - mrx-context/oracle/finals/halprin/ has Halprin FINAL files
   - mrx-context/oracle/frontmatter/halprin_frontmatter.txt has
     extracted front-matter (659 lines, pages 1-12)
   - README in oracle/ states the Oracle Covenant clearly
   - Brandl FINAL also on disk in MASTER_COPIES/ORACLES/
   - 030526 depo found, candidate for consolidation
   - Easley FINAL in mb_demo_engine_v4 folder, candidate

## TONIGHT'S FAILURE MODES — DO NOT REPEAT

1. I framed front-matter as a layout-primitive problem when it's a
   component-template problem. Scott pushed back, I caught it, but
   it took too long. FIX: when a problem looks like "render this
   structure," ask first "is this structure repeated across
   instances?" If yes → template, not primitive.

2. I let Sonnet's first audit conclude "dictionary is on MB's machine,
   we don't have it" when in fact the dictionary was sitting in
   Scott's OneDrive Halprin package the whole time. Scott had to
   prompt me with a screenshot of the package folder. FIX: when
   investigating something with files involved, FIRST ask "what
   folders/packages do we have?" before reasoning from metadata.

3. I told Scott "dictionary lookup is the answer to B5" before
   confirming the job dict had W&T in it. It didn't. The B5 root
   cause is NOT job dictionary gap — it's likely a Stage 1 stroke
   tokenization issue, OR it's in MB's system dict (which we don't
   have). FIX: do not declare root cause from one piece of evidence.
   Hold the hypothesis loosely until ALL three layers (raw, dict,
   pipeline output) are checked.

## FIRST THREE THINGS YOU DO TOMORROW

### 1. Component inventory pass (top priority)

Goal: extract front-matter components from MB finals we have on disk
and identify the reusable template structure.

Files available tomorrow morning:
- oracle/frontmatter/halprin_frontmatter.txt (659 lines, ready)
- MASTER_COPIES/ORACLES/Brandl/* (full files, need front-matter
  extraction)
- 030526 depo (need to confirm with Scott it's an MB depo, then
  consolidate)
- Easley from mb_demo_engine_v4 (consolidate if Scott confirms)

What to do:
- Spec for Sonnet: extract front-matter from Brandl + 030526 + Easley
  the same way Halprin was extracted (cutoff at EXAMINATION marker)
- Then: Opus does the comparison. Diff each section across depos.
  Identify what's identical (template), what's variable (slots).
- Output: COMPONENTS.md in oracle/ describing each component with
  its template + slot variables + state-specific variations
  observed.

This is where Scott wants energy spent. This is the work that gets
front-matter to "look like a fan."

### 2. Wire dictionary loader (housekeeping, but quick)

Two-line fix in _run_halprin_mini.py line 267 area. Sonnet can do
this in 10 minutes. Confirms dictionary is loaded into LLM context.
Not a silver bullet — won't fix B2/B5 — but it's correct and removes
a known gap.

### 3. (If energy) M3 stipulation strip-out localization

The stipulation paragraph is in raw RTF, gone in OUR_FINAL. Confirmed
pipeline bug. Leading hypothesis: Stage 1 RTF parse drops the block.

Sonnet trace: take the RTF text "It is stipulated and agreed", track
through Stage 1 → 2 → 3 → 4 → 5 outputs, find the stage where it
disappears.

This work is INDEPENDENT of the component template work. Could run
in parallel with #1 if Sonnet has bandwidth.

## WHAT NOT TO DO TOMORROW

- Do NOT spec the M0/M0a/M2 sub-row layout primitive. Component
  template work supersedes it.
- Do NOT design audio architecture. Paragraph timestamps in .sgxml
  are sufficient. Save audio work for after front-matter ships.
- Do NOT attempt to fix B2/B5 anomalies until the component work
  ships. They're parked. Scott explicitly deprioritized "MB Style
  Rules" tonight as future work after tech debt clears.
- Do NOT touch B1 dashes. 441 examples, parked.
- Do NOT chase MB's system dictionary. We can't access it without
  CaseCATalyst format reverse-engineering. Stop trying.
- Do NOT promise Scott a fix timeline. He's pushing for "look like
  fan" but he ALSO said tonight he doesn't want to push off MB.
  Keep momentum, but don't overcommit.

## WHAT I'M PROUD OF FROM TONIGHT

- The dictionary thread bottomed out. We KNOW where it stands now.
- Recon methodology became real. We have a process for not shipping
  wrong direction.
- Oracle folder structure exists. Truth sources are organized.
- Defect log is durable record — fresh architect can read cold.
- Component reframe came BEFORE we wrote spec for the wrong thing.
- Scott trusts the work. He pushed when I was wrong, and the
  pushbacks landed. That trust survived several of my errors tonight.

## SCOTT'S MOOD AT SESSION CLOSE

Tired. Calm. Optimistic. He stayed past where most people would have
stopped because he wanted tonight's work SAFE before signing off.
He literally said: "save and organize make it safe for the next opus
as anyone else seamless hand off tomorrow."

That's the bar. He gave us the trust to push through. Tomorrow's
seamless open is the deliverable.

— End of resume note —