# Halprin Pages 1-13 — OUR_FINAL vs MB FINAL Diff

**Date:** 2026-04-29  
**Comparison range:** Pages 1-13  
**OURS:** `C:\Users\scott\OneDrive\Documents\mrx_engine_v1\mrx_engine_v1\io\analysis\halprin_mini\_stage5_out\halprin_mini.OUR_FINAL.txt`  
**MB:** `C:\Users\scott\OneDrive\Documents\mrx-context\oracle\finals\halprin\040226yellowrock-FINAL.txt` (read with cp1252)  

**Total lines compared:** 1404  
**Total diff lines:** 11  
**Pages with zero diffs:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12  
**Pages with diffs:** 13  

---

## PAGES 1-12 STATUS

**ALL CLEAN.** Pages 1-12 byte-match MB oracle (0 diffs).

- Pages 2-10: appearances/index/exhibits — literal template ✓

- Page 11: stipulation — literal template ✓

- Page 12: videographer opening — literal template ✓

- Page 1: cover page — literal template ✓


---

## PAGE 13 DIFFS

Page 13 has **11 diff lines** out of 54 total lines.

Page 13 is the transition page: lines 1-2 are sworn-in (literal), line 4+ is body Q&A.


### Category 1: EXAMINATION indentation

**Count:** 1  
**Cause:** Layout engine centers `EXAMINATION` in 55-char content area; MB has it at 3-space indent (same as BYLINE)  
**Severity:** Low — visual only, content correct  

  Page 13, line 4:  
    OUR: `'4                      EXAMINATION'`  
    MB:  `'4   EXAMINATION'`  

**Recommendation:** FIX — emit EXAMINATION as BYLINE (indent=3), not CENTERED


### Category 2: Single space after period (Q&A body)

**Count:** 4  
**Pattern:** OUR uses single space after `.`; MB uses double space  
**Cause:** CaseCATalyst (MB's tool) auto-inserts double space after sentence-ending periods. Our pipeline doesn't.  
**Severity:** Medium — cosmetically significant in direct comparison  

  Page 13, line 6:  
    OUR: `        Q.    Good morning, sir. My name is Ryan`  
    MB:  `        Q.    Good morning, sir.  My name is Ryan`  
  Page 13, line 7:  
    OUR: `   Caughey and we met a few minutes ago. I represent`  
    MB:  `   Caughey and we met a few minutes ago.  I represent`  
  Page 13, line 8:  
    OUR: `   the Westlake Defendants in this case. I'm in from`  
    MB:  `   the Westlake Defendants in this case.  I'm in from`  

**Recommendation:** FIX — post-process Q&A text to double-space after `[.!?]` followed by uppercase


### Category 3: Content differences (uncorrected steno / different corrections)

**Count:** 6  
**Cause:** Stage 3.1 LLM corrections differ from MB's manual corrections. Also wrapping cascade from upstream content diffs.  
**Severity:** High — transcript accuracy  

  Page 13, line 14:  
    OUR: `        A.    9757 lemon wood terrace, Boynton Beach,`  
    MB:  `        A.    9757 Lemonwood Terrace, Boynton Beach,`  
  Page 13, line 16:  
    OUR: `        Q.    And that's your permit address?`  
    MB:  `        Q.    And that's your permanent address?`  
  Page 13, line 17:  
    OUR: `        A.    That is my permission address.`  
    MB:  `        A.    That is my permanent address.`  

**Recommendation:** TIER 2 LATER — requires improved Stage 3.1 corrections or manual review queue


---

## SUMMARY

| Page range | Status | Diffs | Note |

|------------|--------|-------|------|

| Pages 1-12 | ✅ CLEAN | 0 | All literal template pages match oracle |

| Page 13, lines 1-2 | ✅ CLEAN | 0 | Sworn-in continuation matches oracle |

| Page 13, line 4 | ⚠️ DIFF | 1 | EXAMINATION centering — easy fix |

| Page 13, lines 5-25 | ❌ DIFF | 10 | Body Q&A content/spacing differences |


**The literal template strategy has fully succeeded for pages 1-12.** Body Q&A diffs start at page 13 line 5 (first Q&A line) and are caused by corrected_turns text diverging from MB's corrections.
