#!/usr/bin/env python3
"""
READ-ONLY audit of the xqtl-resources website pages (content/**/*.md).
Offline checks (default) and optional Synapse checks (--synapse; needs synapseclient login).
Nothing is modified.

  python3 audit_catalog.py --repo /path/to/xqtl-resources                # offline
  python3 audit_catalog.py --repo /path/to/xqtl-resources --synapse      # also verify every synID on Synapse
Writes audit_catalog_report.tsv (page, check, detail) and prints a summary.
"""
import re, sys, os, glob, argparse, collections

ap = argparse.ArgumentParser()
ap.add_argument("--repo", default=".")
ap.add_argument("--synapse", action="store_true")
ap.add_argument("--out", default="audit_catalog_report.tsv")
ap.add_argument("--catalog", default=None, help="catalog page to check coverage against (default content/xqtl-data/README.md)")
ap.add_argument("--fail-on-drift", action="store_true", help="exit 1 only if a dataset page is missing from the catalog")
ap.add_argument("--strict", action="store_true", help="exit 1 if any blocking finding exists (default is warning mode, always exit 0)")
a = ap.parse_args()
C = os.path.join(a.repo, "content")
pages = sorted(glob.glob(os.path.join(C, "**/*.md"), recursive=True))
rel = lambda p: os.path.relpath(p, a.repo)

rows = []
titles = {}
coverage = {"total": 0, "with_header": 0}
def flag(p, check, detail=""): rows.append((rel(p), check, detail))

SYN = re.compile(r"\bsyn\d{5,}\b")
PLACEHOLDER = re.compile(r"(?<![A-Za-z])(TBD|TODO|nan|N/A|to be added|In Construction)(?![A-Za-z])")
INTERNAL = re.compile(r"(/sc/arion/|/mnt/vast/|/restricted/|/home/\w+/|s3://|/hpc/|/ftp_fgc_xqtl/)")
PERSONAL = re.compile(r"\b(I have|I've|we have included|my |please ask me)\b", re.I)
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")

ids_by_page = {}
for p in pages:
    t = open(p, encoding="utf-8").read()
    lines = t.split("\n")
    title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("#") else ""
    if not title: flag(p, "no_title")
    titles.setdefault(title, []).append(p)
    has_header = t.startswith("---\n")
    if ("/qtl/" in p or "/omics/" in p or "/gwas/" in p or "/study_info/" in p or "/reference_data/" in p) and os.path.basename(p) != "README.md":
        coverage["total"] += 1
        if has_header: coverage["with_header"] += 1
        else: flag(p, "missing_header", "no YAML metadata header")
    ids = sorted(set(SYN.findall(t)))
    ids_by_page[rel(p)] = ids
    for m in PLACEHOLDER.finditer(t):
        ctx = t[max(0, m.start()-25):m.end()+25].replace("\n", " ")
        flag(p, "placeholder", ctx)
    n = len(INTERNAL.findall(t))
    if n and "/qtl/" in p or n and "/omics/" in p or n and "/gwas/" in p:
        flag(p, "internal_path", f"{n} internal path(s), first: {INTERNAL.search(t).group(0)}")
    if PERSONAL.search(t): flag(p, "personal_voice", PERSONAL.search(t).group(0))
    # empty sections: heading followed directly by another heading or end
    for i, l in enumerate(lines):
        if l.startswith("#"):
            nxt = next((x for x in lines[i+1:] if x.strip()), None)
            if nxt is None or nxt.startswith("#"):
                if not (nxt and nxt.startswith("#") and len(nxt) - len(nxt.lstrip("#")) > len(l) - len(l.lstrip("#"))):
                    flag(p, "empty_section", l.strip())
    # relative links that do not resolve
    for m in LINK.finditer(t):
        u = m.group(1)
        if u.startswith(("http", "mailto:", "/")): continue
        tgt = os.path.normpath(os.path.join(os.path.dirname(p), u))
        if not (os.path.exists(tgt) or os.path.exists(tgt + ".md") or os.path.exists(os.path.join(tgt, "README.md"))
                or os.path.exists(os.path.join(C, u)) or os.path.exists(os.path.join(C, u + ".md"))):
            flag(p, "broken_relative_link", u)
    # modality/title consistency for QTL/omics pages
    low = title.lower()
    fn = os.path.basename(p).lower()
    if "glyco" in fn and "glyco" not in low: flag(p, "title_vs_filename", f"{title} / {fn}")
    if "methylation" in fn and "methyl" not in low: flag(p, "title_vs_filename", f"{title} / {fn}")
    if "metabol" in fn and "metabol" not in low: flag(p, "title_vs_filename", f"{title} / {fn}")
    # dataset pages should say which release/status they belong to
    if ("/qtl/" in p or "/omics/" in p) and os.path.basename(p) != "README.md" and not re.search(r"(release|20\d\d)", t):
        pass

for tt, ps in titles.items():
    if tt and len(ps) > 1 and "/xqtl-data/" in ps[0] and not all(os.path.basename(x) == "README.md" for x in ps):
        for x in ps:
            if os.path.basename(x) != "README.md": flag(x, "duplicate_title", tt)

# Synapse IDs used by several pages with different roles are fine; list the distinct set
allids = collections.Counter(i for v in ids_by_page.values() for i in v)

# staging YAML cross-check (is every synID on the site also known to the staging structure file?)
y = os.path.join(a.repo, "data", "statfungen_synapse_staging_folder_structure.yml")
if os.path.exists(y):
    yids = set(SYN.findall(open(y).read()))
    for pg, ids in ids_by_page.items():
        for i in ids:
            if i not in yids: rows.append((pg, "synid_not_in_staging_yaml", i))

# README catalog vs files
cat = a.catalog or os.path.join(C, "xqtl-data", "README.md")
if os.path.exists(cat):
    ct = open(cat).read()
    listed = set(re.findall(r"content/xqtl-data/([^)\s]+\.md)", ct))
    onsite = {os.path.relpath(p, os.path.join(C, "xqtl-data")) for p in pages
              if p.startswith(os.path.join(C, "xqtl-data")) and os.path.basename(p) != "README.md"
              and os.path.relpath(p, os.path.join(C, "xqtl-data")).split(os.sep)[0] in ("gwas", "omics", "qtl", "study_info", "reference_data")}
    for m in sorted(onsite - listed): rows.append(("content/xqtl-data/README.md", "page_missing_from_catalog", m))
    for m in sorted(listed - onsite): rows.append(("content/xqtl-data/README.md", "catalog_entry_without_page", m))

if a.synapse:
    import synapseclient
    syn = synapseclient.login(silent=True)
    for i in sorted(allids):
        try:
            e = syn.get(i, downloadFile=False)
            parent = e.properties.get("parentId", "")
            rows.append(("(synapse)", "synid_ok", f"{i}\t{e.name}\tparent={parent}"))
        except Exception as ex:
            msg = str(ex)[:80]
            rows.append(("(synapse)", "synid_unreachable", f"{i}\t{msg}"))
            for pg, ids in ids_by_page.items():
                if i in ids: rows.append((pg, "synid_unreachable", i))

with open(a.out, "w") as f:
    f.write("page\tcheck\tdetail\n")
    for r in rows: f.write("\t".join(r) + "\n")
cnt = collections.Counter(r[1] for r in rows if r[1] != "synid_ok")
print(f"{len(pages)} pages, {len(allids)} distinct synIDs")
for k, v in cnt.most_common(): print(f"{v:5d}  {k}")
print(f"header coverage: {coverage['with_header']}/{coverage['total']} dataset pages")
print("details in", a.out)
BLOCKING = {"missing_header", "placeholder", "internal_path", "broken_relative_link", "synid_unreachable", "page_missing_from_catalog"}
if a.strict and any(r[1] in BLOCKING for r in rows): sys.exit(1)
if a.fail_on_drift and any(r[1] in ("page_missing_from_catalog", "catalog_entry_without_page") for r in rows): sys.exit(1)
