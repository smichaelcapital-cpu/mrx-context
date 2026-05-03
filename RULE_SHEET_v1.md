# WHERE DOES THIS FIX GO? — Rule Sheet v1
Date: 2026-05-03

Before any fix, answer two questions:

Q1: Will this rule apply to EVERY court reporter, forever?
   YES → Universal
   NO  → MB-specific
   UNSURE → Treat as MB-specific (default to caution)

Q2: Is the rule deterministic, or does it require judgment?
   Deterministic → CODE
   Judgment → AI PROMPT

| | Universal | MB-specific |
|---|---|---|
| Code | src/transforms/, src/validate_ops/ | src/profiles/mb/ |
| Prompt | prompts/core/ | prompts/profiles/mb/ |

LABELING REQUIRED on every commit:
- Universal commits: prefix "universal:"
- MB-specific commits: prefix "mb-specific:"
- MB-specific code: filename contains "mb_" OR lives in profiles/mb/
- MB-specific prompt blocks: wrap in
    # ═══ MB TAILORING — NOT UNIVERSAL ═══
    [rules]
    # ═══ END MB TAILORING ═══

EVERY SPEC MUST INCLUDE THIS HEADER:
- Universal? YES / NO
- Code or prompt? CODE / PROMPT
- File location: <exact path>
- Commit prefix: universal: / mb-specific:

When in doubt: default to MB-specific. Easier to promote later than to demote.
