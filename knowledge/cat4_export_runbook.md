# CaseCATalyst RTF Export Runbook
**Captured:** 2026-05-09
**Source:** Live walkthrough of jp_042726 export (Scott + Opus session)
**Status:** First pass — captured during the actual export, refine on next run

## Purpose
Exporting an RTF from a CaseCATalyst package has been a recurring pain point. This runbook documents the steps so the export takes 5 minutes, not a day.

## Pre-flight: package contents
A CR sends a zip containing files like 042726jp-ROUGH.sgngl, .sgstn, .sgdct, .sgxml, .opus, etc. The RTF is NOT in the original package — the CR exports it OR you export it yourself if you have Cat4.

## Step-by-step export

1. **Extract the zip** to a working folder. Cat4 cannot read files inside a zip.
   - Example: C:\Users\scott\Downloads\042726 to scott\

2. **Open Cat4.** Go to Function menu (top toolbar) → Export.
   - NOT Export ASCII (that strips style codes the engine needs).

3. **The Export dialog appears with tabs.** Select the **RTF/CRE** tab. This is the only correct format — RTF preserves the style codes (\s1, \s3, \s5, \s7) the engine reads.

4. **The dialog shows files from a default Cat4 user folder** (e.g., C:\Cat4\usr\scott\...). You need to point it at YOUR extracted folder.
   - Click the folder browser icon, navigate up the tree to reach C:\Users\scott\Downloads\, then into the extracted package folder.

5. **Once pointed at the right folder**, the dialog lists the package files. Check the box next to the **.sgngl** file (the transcript text file, typically ~700 KB).

6. **Take all defaults** in the Options. Do not customize.

7. **Click Export.** A "Show Export Complete message box" confirmation appears.

8. **Output:** an RTF file is created (typically named with `_T` suffix, e.g., 042726jp-ROUGH_T.rtf, ~1.3 MB).

## Post-export: rename and file
- Drop the `_T` suffix on rename → 042726jp-ROUGH.rtf
- Move to depo library: C:\Users\scott\OneDrive\Documents\mrx_depo_library\<CR>\<job>\

## Common pitfalls (captured during the actual walkthrough)
- The default folder in the Export dialog is NOT where your package lives. You must navigate.
- The .sgxr2 file may be 0 KB — that's normal, ignore it.
- "Export ASCII" is a sibling menu item — DO NOT click it. Plain ASCII strips the style codes.
- The RTF/CRE tab must be selected in the Export dialog. Other tabs (Stentura, HTML, ASCII, etc.) produce wrong formats.
- If the file tree only shows Cat4 user folders, scroll up past the `scott` Cat4 user folder to reach This PC / C: drive level, then navigate.

## Open questions for next refinement
- Does Cat4 have a default-folder setting we can change to skip the navigation step?
- Are there hotkeys or scripted exports for batch processing?
- Does Cat4 produce different RTF flavors based on Options? (Took defaults this time.)
