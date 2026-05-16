"""
13-Depo Fingerprint Frequency Analysis
Sonnet #1 laneA — 2026-05-16 evening

Step 1: Ingestion status report only (no difflib — see notes below).
Step 2: D2/D4/D5 oracle analysis on all 13 parseable FINAL.txt files.
"""

import re, json
from pathlib import Path
from collections import defaultdict

BASE     = Path("C:/Users/scott/OneDrive/Documents/mrx-context")
DEPO_LIB = Path("C:/Users/scott/OneDrive/Documents/mrx_depo_library")
CACHE    = BASE / "fingerprints/stage_a/cache"

DEPO_FILES = {
    "halprin":  BASE / "oracle/finals/halprin/040226yellowrock-FINAL.txt",
    "olsen":    BASE / "oracle/finals/032025olsen/032025olsen-FINAL.txt",
    "williams": BASE / "oracle/finals/060122williams/060122williams-FINAL.txt",
    "butler":   BASE / "oracle/finals/082222butler/082222butler-FINAL.txt",
    "blanks":   BASE / "oracle/finals/101322blanks/101322blanks-FINAL.txt",
    "black_bp": BASE / "oracle/finals/0525black_bp/0525black-bp-FINAL.txt",
    "easley":   DEPO_LIB / "MB/easley_031326/oracle/Easley_YellowRock_FINAL_TRANSCRIPT.txt",
    "fountain": DEPO_LIB / "MB/fountain_011923/oracle/011923fountain FINAL.txt",
    "hebert":   DEPO_LIB / "MB/hebert_011723/oracle/011723hebertFINAL.txt",
    "simon":    DEPO_LIB / "_staging_for_export_2026-05-13/011723hebert/011723simonFINAL.txt",
    "garcia":   DEPO_LIB / "_staging_for_export_2026-05-13/082322garcia-ROUGH/082322garcia-FINAL.txt",
    "griffin":  CACHE / "griffin_121322_final.txt",
    "martin":   CACHE / "martin_121322_final.txt",
}

# Step 1 status (pre-assessed, no difflib execution)
INGEST_STATUS = {
    "olsen_032025":    ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "black_bp_0525":   ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "williams_060122": ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "butler_082222":   ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "blanks_101322":   ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "simon_011723":    ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "garcia_082322":   ("FAIL", "no raw ROUGH .txt source — only formatted FINAL exists"),
    "zannetti_080221": ("FAIL", "raw+final cache exist but church/zannetti flagged: church 12x ratio anomaly; difflib hangs on mismatched pair; pipeline script not on main"),
    "church_073124":   ("FAIL", "raw(35KB)+final(377KB) = 12x ratio anomaly (flagged 2026-05-14); difflib intractable on size mismatch; pipeline script not on main"),
}

SLOT_RE        = re.compile(r'^( {0,6})(\d{1,2})(  .*|\s*$)')   # 0-6 leading spaces (easley 2-digit slots have 0)
PAGE_A_RE      = re.compile(r'^\s{40,}\d+\s*$')
INDEX_RE       = re.compile(r'\bI\s*N\s*D\s*E\s*X\b', re.IGNORECASE)
FIRM_RE        = re.compile(r'^(FOR THE [A-Z]|ATTORNEY FOR|Attorney for)')  # case-sensitive to exclude "for the record"
CERT_RE        = re.compile(r"reporter'?s?\s+certif", re.IGNORECASE)
EXHIBITS_RE    = re.compile(r'^EXHIBITS?\s*$', re.IGNORECASE)
EXHIBIT_EN_RE  = re.compile(r'Exhibit\s+No\.?\s*\w+', re.IGNORECASE)
MAX_APP_PAGE   = 20   # appearances pages never deeper than p20 in MB depos

def is_page_break(line):
    if PAGE_A_RE.match(line): return True
    # Format B bare page number: no leading space AND just digits (SLOT_RE now accepts 0 spaces,
    # so we distinguish: bare page has no trailing content after the number, slot lines do)
    stripped = line.rstrip('\n\r')  # keep trailing spaces — '12  ' must NOT match page '12'
    if re.match(r'^\d{1,3}$', stripped) and not line.startswith(' '):
        return True
    return False

def page_num_from(line):
    m = re.search(r'(\d+)', line)
    return int(m.group(1)) if m else None

def parse_slots(path):
    text  = Path(path).read_text(encoding='utf-8', errors='replace') \
                      .replace('\r\n','\n').replace('\r','\n')
    lines = text.split('\n')
    result, cur_page, i = [], 1, 0
    while i < len(lines):
        line = lines[i]
        if is_page_break(line):
            n = page_num_from(line)
            if n and n >= cur_page:
                cur_page = n
            i += 1; continue
        m = SLOT_RE.match(line)
        if m:
            slot_num = int(m.group(2))
            main_c   = line[m.end(2):].strip()
            sub_c    = ''
            if i+1 < len(lines):
                nxt = lines[i+1]
                if (nxt and not SLOT_RE.match(nxt) and not is_page_break(nxt)
                        and nxt.strip() and nxt[0] in (' ','\t')):
                    sub_c = nxt.strip(); i += 1
            result.append({"page": cur_page, "slot": slot_num,
                           "main": main_c, "sub": sub_c})
        i += 1
    return result

def analyze_d2(depo_id, slots):
    firm_pages = {s['page'] for s in slots
                  if s['page'] <= MAX_APP_PAGE and
                  (FIRM_RE.search(s['main']) or FIRM_RE.search(s['sub']))}
    if not firm_pages:
        return [], "No firm-group headers found"
    app = [s for s in slots if s['page'] in firm_pages]
    firm_idx = [i for i,s in enumerate(app)
                if FIRM_RE.search(s['main']) or FIRM_RE.search(s['sub'])]
    if len(firm_idx) < 2:
        return [], f"Only {len(firm_idx)} firm group(s)"
    transitions = []
    for j in range(len(firm_idx)-1):
        ci, ni = firm_idx[j], firm_idx[j+1]
        last_c = next((k for k in range(ni-1, ci-1, -1)
                       if app[k]['main'] or app[k]['sub']), None)
        if last_c is None: continue
        blank = sum(1 for k in range(last_c+1, ni)
                    if not app[k]['main'] and not app[k]['sub'])
        lc, nf = app[last_c], app[ni]
        transitions.append({"page": lc['page'],
                             "prev_end_slot":   lc['slot'],
                             "next_start_slot": nf['slot'],
                             "blank_slots":     blank})
    return transitions, None

def analyze_d4(depo_id, slots):
    idx_page = next((s['page'] for s in slots
                     if INDEX_RE.search(s['main']) or INDEX_RE.search(s['sub'])), None)
    if idx_page is None: return None, "No INDEX section"
    for s in slots:
        if not (idx_page <= s['page'] <= idx_page+1): continue
        if CERT_RE.search(s['main']): return {"slot":s['slot'],"position":"MAIN","page":s['page']}, None
        if CERT_RE.search(s['sub']):  return {"slot":s['slot'],"position":"SUB", "page":s['page']}, None
    return None, "Cert not found on index page"

def analyze_d5(depo_id, slots):
    idx_page = next((s['page'] for s in slots
                     if INDEX_RE.search(s['main']) or INDEX_RE.search(s['sub'])), None)
    if idx_page is None: return None, "No INDEX section"
    ex_i = next((i for i,s in enumerate(slots)
                 if s['page'] >= idx_page and
                 (EXHIBITS_RE.search(s['main']) or EXHIBITS_RE.search(s['sub']))), None)
    if ex_i is None: return None, "No EXHIBITS header"
    ex_s  = slots[ex_i]
    ex_pos = "MAIN" if EXHIBITS_RE.search(ex_s['main']) else "SUB"
    for i in range(ex_i+1, min(ex_i+60, len(slots))):
        s = slots[i]
        if EXHIBIT_EN_RE.search(s['main']):
            return {"exhibits_slot":ex_s['slot'], "exhibits_pos":ex_pos,
                    "first_exhibit_slot":s['slot'], "first_exhibit_pos":"MAIN",
                    "page":s['page']}, None
        if EXHIBIT_EN_RE.search(s['sub']):
            return {"exhibits_slot":ex_s['slot'], "exhibits_pos":ex_pos,
                    "first_exhibit_slot":s['slot'], "first_exhibit_pos":"SUB",
                    "page":s['page']}, None
    return None, "No exhibit entries after EXHIBITS header"

def run_analysis():
    d2r, d4r, d5r = {}, {}, {}
    for dep, fpath in DEPO_FILES.items():
        if not fpath.exists():
            d2r[dep]=([],"file not found"); d4r[dep]=(None,"file not found"); d5r[dep]=(None,"file not found")
            continue
        slots = parse_slots(fpath)
        d2r[dep] = analyze_d2(dep, slots)
        d4r[dep] = analyze_d4(dep, slots)
        d5r[dep] = analyze_d5(dep, slots)
    return d2r, d4r, d5r

def build_report(d2r, d4r, d5r):
    L = []
    def a(s=""): L.append(s)

    a("# 2026-05-16 FINGERPRINT 13-DEPO FREQUENCY ANALYSIS")
    a("Sonnet #1 laneA — evening session")
    a("")
    a("Extension of D-2/D-4/D-5 oracle audits from 6-depo set to 13 depos.")
    a("Data only. No fix recommendations.")
    a("")
    a("**13-depo set:**")
    a("6 oracle/finals (halprin, olsen, williams, butler, blanks, black_bp) +")
    a("3 Group-A MB library (easley, fountain, hebert) +")
    a("2 Group-B staging (simon, garcia) +")
    a("2 parseable cache finals (griffin, martin).")
    a("")

    # Step 1
    a("---")
    a("")
    a("## STEP 1 — INGESTION STATUS (9 missing depos)")
    a("")
    a("Target: add to `fingerprints/stage_a/mb_evidence_raw.json`.")
    a("")
    a("| Depo | Status | Reason |")
    a("|------|--------|--------|")
    ok_n = fail_n = 0
    for dep, (st, msg) in INGEST_STATUS.items():
        a(f"| {dep} | **{st}** | {msg} |")
        if st=="OK": ok_n+=1
        else: fail_n+=1
    a("")
    a(f"**Result:** {ok_n} ingested, {fail_n} failed.")
    a("")
    a("**Root cause summary:**")
    a("")
    a("- 7 depos (olsen, black_bp, williams, butler, blanks, simon, garcia):")
    a("  ROUGH draft was never exported to a plain-text `.txt` cache file.")
    a("  These depos exist only as formatted FINAL transcripts.")
    a("  Ingestion into the habit-frequency pipeline requires a RAW source.")
    a("")
    a("- 2 depos (zannetti, church) have raw+final cache files but cannot")
    a("  be ingested because:")
    a("  (a) The aligner/differ script (`feature/stage-a-aligner-differ-v0`)")
    a("      is not on `main` — not accessible from laneA session.")
    a("  (b) Church is the 12x ratio anomaly flagged 2026-05-14: raw=35 KB,")
    a("      final=377 KB. Wrong raw file is almost certainly paired.")
    a("      Zannetti raw/final are legitimate but same script-missing blocker.")
    a("")
    a("**Action required (not in scope for Sonnet):**")
    a("- Export ROUGH drafts to .txt for the 7 no-raw depos.")
    a("- Merge or cherry-pick `feature/stage-a-aligner-differ-v0` to `main`.")
    a("- Resolve church raw-file pairing before ingesting.")
    a("")

    # D2
    a("---")
    a("")
    a("## QUERY A — Firm-Group Separator Blank Slots (D-2)")
    a("")
    a("Method: count fully-blank slots (MAIN='' AND SUB='') strictly between")
    a("consecutive firm-group headers on appearances pages.")
    a("Header patterns: `FOR THE`, `ATTORNEY FOR`, `Attorney for`.")
    a("")
    a("### Full Transition Table")
    a("")
    a("| depo | pg | prev_end | next_start | blank_slots |")
    a("|------|----|----------|------------|-------------|")

    all_t = []
    for dep in DEPO_FILES:
        trans, err = d2r.get(dep, ([], "not run"))
        if trans:
            all_t.extend(trans)
            for t in trans:
                a(f"| {dep} | {t['page']} | {t['prev_end_slot']} | {t['next_start_slot']} | **{t['blank_slots']}** |")
        else:
            a(f"| {dep} | — | — | — | *{err}* |")

    counts = defaultdict(int)
    for t in all_t:
        counts[t['blank_slots']] += 1
    total_t = len(all_t)

    a("")
    a("### Summary")
    a("")
    a("```")
    a(f"Total transitions: {total_t}")
    a("")
    if total_t:
        dom_val = max(counts.values())
        for k in sorted(counts):
            pct = 100*counts[k]//total_t
            flag = "  ← dominant" if counts[k] == dom_val else ""
            a(f"  {k} blank(s): {counts[k]:3d} transitions ({pct}%){flag}")
        a("")
        dom = max(counts, key=counts.get)
        a(f"Dominant pattern: {dom} blank slot(s) between firm groups")
    a("```")
    a("")

    a("### Per-Depo D2 Summary")
    a("")
    a("| depo | transitions | 0-blank | 1-blank | 2+-blank | note |")
    a("|------|------------|---------|---------|----------|------|")
    for dep in DEPO_FILES:
        trans, err = d2r.get(dep, ([], ""))
        if not trans:
            a(f"| {dep} | 0 | — | — | — | {err} |")
        else:
            z = sum(1 for t in trans if t['blank_slots']==0)
            o = sum(1 for t in trans if t['blank_slots']==1)
            p = sum(1 for t in trans if t['blank_slots']>=2)
            a(f"| {dep} | {len(trans)} | {z} | {o} | {p} |  |")
    a("")

    # D4
    a("---")
    a("")
    a("## QUERY B — Reporter's Certificate Slot on INDEX Page (D-4)")
    a("")
    a("Method: parse INDEX page with slot regex.")
    a("Cert search: `reporter'?s? certif` (case-insensitive).")
    a("")
    a("| depo | cert_slot | cert_pos | index_page |")
    a("|------|-----------|----------|------------|")

    cert_main = cert_sub = cert_total = 0
    sc_d4 = defaultdict(int)
    pb_d4 = defaultdict(list)

    for dep in DEPO_FILES:
        r, err = d4r.get(dep, (None, "not run"))
        if r:
            cert_total += 1
            if r['position']=='MAIN': cert_main+=1
            else: cert_sub+=1
            sc_d4[r['slot']] += 1
            pb_d4[r['slot']].append(r['position'])
            a(f"| {dep} | {r['slot']} | {r['position']} | {r['page']} |")
        else:
            a(f"| {dep} | — | — | *{err}* |")

    a("")
    a("### Summary")
    a("")
    a("```")
    a(f"Depos with cert data: {cert_total}")
    if cert_total:
        a(f"  MAIN: {cert_main} ({100*cert_main//cert_total}%)")
        a(f"  SUB:  {cert_sub}  ({100*cert_sub//cert_total}%)")
        a("")
        a("  Slot distribution:")
        for sl in sorted(sc_d4):
            positions = sorted(set(pb_d4[sl]))
            a(f"    slot {sl}: {sc_d4[sl]}x  positions seen: [{', '.join(positions)}]")
    a("```")
    a("")

    # D5
    a("---")
    a("")
    a("## QUERY C — Exhibits Index Start Position (D-5)")
    a("")
    a("Method: find EXHIBITS header on INDEX page, then first `Exhibit No.` entry.")
    a("")
    a("| depo | exhibits_hdr_slot | exhibits_hdr_pos | first_ex_slot | first_ex_pos |")
    a("|------|------------------|-----------------|--------------|--------------|")

    ex_main = ex_sub = ex_total = 0

    for dep in DEPO_FILES:
        r, err = d5r.get(dep, (None, "not run"))
        if r:
            ex_total += 1
            pos = r['first_exhibit_pos']
            if pos=='MAIN': ex_main+=1
            else: ex_sub+=1
            a(f"| {dep} | {r['exhibits_slot']} | {r['exhibits_pos']} | {r['first_exhibit_slot']} | {pos} |")
        else:
            a(f"| {dep} | — | — | — | *{err}* |")

    a("")
    a("### Summary")
    a("")
    a("```")
    a(f"Depos with exhibit data: {ex_total}")
    if ex_total:
        a(f"  First exhibit in MAIN: {ex_main} ({100*ex_main//ex_total}%)")
        a(f"  First exhibit in SUB:  {ex_sub}  ({100*ex_sub//ex_total}%)")
    a("```")
    a("")
    a("---")
    a("")
    a("*Generated by run_13depo_analysis.py — Sonnet #1 laneA 2026-05-16 evening*")

    return "\n".join(L)

if __name__ == "__main__":
    print("Running D2/D4/D5 analysis on 13-depo set...", flush=True)
    d2r, d4r, d5r = run_analysis()

    print("Results:")
    for dep in DEPO_FILES:
        t2, e2 = d2r.get(dep,([],""))
        r4, e4 = d4r.get(dep,(None,""))
        r5, e5 = d5r.get(dep,(None,""))
        print(f"  {dep}: D2={len(t2)}t | D4={r4 or e4} | D5={r5 or e5}", flush=True)

    report = build_report(d2r, d4r, d5r)
    out = BASE / "knowledge/2026-05-16_FINGERPRINT_13_DEPO_FREQ.md"
    out.write_text(report, encoding='utf-8')
    print(f"\nReport written: {out}", flush=True)
