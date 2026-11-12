#!/usr/bin/env python3
"""
Build the Synapse folder index shown on the "All Synapse folders" page.

Reads data/statfungen_synapse_staging_folder_structure.yml (the staged folder tree; folder IDs are
written as comments, e.g. "eQTL: #syn69865689") and the content pages, and writes a JSON tree:
every staged folder with its Synapse ID(s), its listed files, and the catalog pages that cite it
(or, when no page cites it directly, the nearest parent folder that is cited).

  python3 scripts/staging_index.py --repo . --out website/data/staging.json
  python3 scripts/staging_index.py --repo . --report      # list staged folders no page cites

hugo_generator.py runs this on every build, so the page always matches the YAML.
"""
import re, os, sys, glob, json, argparse

SYN = re.compile(r"\bsyn\d{5,}\b")

def expand(s):
    """Expand the Synapse IDs written in a comment.
    Handles plain lists ('syn1, syn2'), ranges ('syn726677{15..21}') and mixed braces
    ('syn754273{57,59..66,58}' -> syn75427357, syn75427359 .. syn75427366, syn75427358)."""
    out = []
    for m in re.finditer(r"(syn\d*)(\{[^}]*\})?", s):
        pre, br = m.group(1), m.group(2)
        if not br:
            if re.fullmatch(r"syn\d{5,}", pre): out.append(pre)
            continue
        for item in br[1:-1].split(","):
            item = item.strip()
            r = re.fullmatch(r"(\d+)\.\.(\d+)", item)
            if r:
                a, b = r.group(1), r.group(2)
                out += [f"{pre}{str(i).zfill(len(a))}" for i in range(int(a), int(b) + 1)]
            elif item.isdigit():
                out.append(pre + item)
    return out

def independent_ids(path):
    """Second, separate count of the IDs in the YAML: every syn token in a comment, with each
    brace item spelled out by string handling only (no shared code with expand)."""
    ids = set()
    for line in open(path, encoding="utf-8"):
        if "#" not in line: continue
        c = line.split("#", 1)[1]
        while "{" in c:
            i = c.index("{"); j = c.index("}", i)
            k = i
            while k > 0 and (c[k - 1].isdigit() or c[k - 3:k] == "syn"):
                k -= 1 if c[k - 1].isdigit() else 3
            stem = c[k:i]
            items = []
            for it in c[i + 1:j].split(","):
                it = it.strip()
                if ".." in it:
                    a, b = it.split("..")
                    items += [stem + str(n).zfill(len(a)) for n in range(int(a), int(b) + 1)]
                else:
                    items.append(stem + it)
            c = c[:k] + " " + " ".join(items) + " " + c[j + 1:]
        ids |= {w.strip(" ,") for w in c.split() if w.strip(" ,").startswith("syn") and w.strip(" ,")[3:].isdigit() and len(w.strip(" ,")) > 8}
    return ids

def parse(path):
    root = {"name": "", "ids": [], "files": [], "children": [], "depth": -1}
    stack = [(-1, root)]
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip()
        if not line.strip() or line.strip() == "README":
            continue
        ind = len(line) - len(line.lstrip(" "))
        text = line.strip()
        while stack and stack[-1][0] >= ind:
            stack.pop()
        parent = stack[-1][1]
        if text.startswith("- "):
            name, _, c = text[2:].partition("#")
            fid = expand(c)
            parent["files"].append([name.strip()] + fid)
            parent.setdefault("fileids", []).extend(fid)
            continue
        name, _, rest = text.partition(":")
        ids = expand(rest.split("#", 1)[1]) if "#" in rest else []
        node = {"name": name.strip(), "ids": ids, "files": [], "children": []}
        parent["children"].append(node)
        stack.append((ind, node))
    return root

def page_ids(repo):
    pages = {}
    for p in glob.glob(os.path.join(repo, "content", "**", "*.md"), recursive=True):
        rel = os.path.relpath(p, os.path.join(repo, "content"))
        t = open(p, encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", t, re.M)
        title = m.group(1).strip() if m else os.path.basename(p)[:-3]
        for i in set(SYN.findall(t)):
            g = "/" + re.sub(r"/?README$", "", rel[:-3])
            pages.setdefault(i, []).append({"t": re.sub(r"[*_`]", "", title), "g": g or "/"})
    return pages

def annotate(node, pages, inherited, path, out_rows):
    direct = []
    for i in node["ids"] + node.get("fileids", []):
        for pg in pages.get(i, []):
            if pg not in direct: direct.append(pg)
    node["pages"] = direct
    node["via"] = [] if direct else inherited
    node["path"] = "/".join(path)
    if node["name"]:
        out_rows.append((node["path"], ",".join(node["ids"]), "cited" if direct else ("parent" if inherited else "none")))
    for c in node["children"]:
        annotate(c, pages, direct or inherited, path + [c["name"]], out_rows)

def strip(node):
    d = {"n": node["name"], "id": node["ids"], "f": node["files"], "p": node["pages"], "v": node["via"][:3]}
    if node["children"]: d["c"] = [strip(c) for c in node["children"]]
    return d

COHORT = {"ROSMAP": ["ROSMAP"], "MSBB": ["MSBB", "BM_"], "Knight-ADRC": ["KNIGHT", "Knight"],
          "MiGA": ["MiGA"], "STARNET": ["STARNET"], "MetaBrain": ["MetaBrain", "Metabrain"]}
OMICS2QTL = {"expression": "eQTL", "splicing": "sQTL", "methylation": "mQTL", "proteomics": "pQTL",
             "glycoproteomics": "glycoQTL", "metabolomics": "metQTL", "histone_ChIPSeq": "haQTL",
             "snATAC": "caQTL", "snRNA_seq": "eQTL"}
QTLS = ["glycoQTL", "metQTL", "haQTL", "caQTL", "tpQTL", "eQTL", "sQTL", "pQTL", "mQTL"]
SNUC = ["snuc", "Ast", "Exc", "Inh", "Mic", "OPC", "Oli", "MIT", "CUIMC1", "mega"]
CTX = ["DLPFC", "AC", "PCC", "monocyte", "microglia"] + SNUC
GWAS = {"Bellenguez": "Bellenguez", "Jansen": "Jansen", "Kunkle": "Kunkle", "Wightman": "Wightman"}

def tokens(name):
    return set(re.split(r"[_.\-]", name))

ALIAS = {"metabolome": "metQTL", "metabolomics": "metQTL", "glyco": "glycoQTL", "tpQTL": "tpQTL"}

def qtl_of(name):
    """Data types named in a folder or file name (several for joint names such as ROSMAP_eQTL_pQTL)."""
    found = {q for q in QTLS if re.search(r"(^|[_.\-])" + q + r"($|[_.\-])", name)}
    found |= {v for k, v in ALIAS.items() if re.search(r"(^|[_.\-])" + k, name)}
    return found

def front(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("---"): return {}
    head = t[3:t.find("\n---", 3)]
    return {k.strip(): v.strip().strip('"') for k, _, v in (l.partition(":") for l in head.split("\n")) if k.strip()}

def page_spec(repo, rel):
    f = front(os.path.join(repo, "content", rel))
    kind = f.get("type", "")
    spec = {"kind": kind, "cohort": f.get("cohort", ""), "qtl": None, "ctx": set(), "gwas": None}
    if kind in ("qtl", "omics"):
        m = f.get("modality", "")
        spec["qtl"] = m if m in QTLS else OMICS2QTL.get(rel.split("/")[2] if kind == "omics" else "", None) or OMICS2QTL.get(m)
        base = os.path.basename(rel)
        ctx = f.get("context", "") + " " + base
        spec["ctx"] = {c for c in CTX if re.search(r"(^|[^A-Za-z])" + c + r"($|[^A-Za-z])", ctx)}
        if re.search(r"snRNA|snuc|pseudo_bulk|cell types", ctx): spec["ctx"] |= set(SNUC)
    if kind == "gwas":
        for k in GWAS:
            if k.lower() in rel.lower(): spec["gwas"] = k
    return spec

REGION = ["DLPFC", "AC", "PCC", "monocyte", "microglia"]
ROSMAP_ONLY = {"CUIMC1", "MIT", "mega", "DLPFC", "AC", "PCC", "monocyte"}

def match(spec, name, anc_qtl):
    """True when a staged folder or file name belongs to the page's dataset.
    Rules: same cohort (a name without a cohort but with ROSMAP-only context tokens such as
    CUIMC1, MIT or DLPFC counts as ROSMAP), same data type (from the name or a parent folder),
    and for ROSMAP the same kind of data (single-nucleus names only on the single-nucleus page,
    bulk region names only on that region's page)."""
    if spec["kind"] == "gwas":
        return bool(spec["gwas"]) and spec["gwas"] in name
    cos = COHORT.get(spec["cohort"], [])
    tk = tokens(name)
    named = any(name.startswith(c) or ("_" + c) in name for cohort in COHORT.values() for c in cohort)
    mine = any(name.startswith(c) or ("_" + c) in name for c in cos)
    implied = spec["cohort"] == "ROSMAP" and not named and bool(tk & ROSMAP_ONLY) and bool(anc_qtl)
    if not cos or not (mine or implied): return False
    if spec["kind"] == "study": return True
    # single-group outputs name their one input after the gene wildcard, e.g.
    # ROSMAP_eQTL_pQTL.*.DLPFC_Bennett_pQTL.ctwas_single_group_...: judge by that input
    if ".*." in name and qtl_of(name.split(".*.", 1)[1]):
        tail = name.split(".*.", 1)[1]
        tk = tokens(tail)
        q = qtl_of(tail)
    else:
        q = qtl_of(name) or anc_qtl
    if q and spec["qtl"] not in q: return False
    if spec["cohort"] == "ROSMAP":
        name_sn = bool(tk & set(SNUC))
        page_sn = bool(spec["ctx"] & set(SNUC))
        regions = tk & set(REGION)
        if name_sn and not page_sn: return False
        if page_sn and regions and not name_sn: return False
        if regions and not (regions <= spec["ctx"]): return False
    return True

def by_page(tree, repo):
    """For each dataset page: the staged folders and files whose names carry that dataset's cohort,
    data type and context (outermost match only), grouped under their parent folder path."""
    out = {}
    pages = [os.path.relpath(p, os.path.join(repo, "content")) for p in glob.glob(os.path.join(repo, "content", "xqtl-data", "**", "*.md"), recursive=True)]
    for rel in pages:
        if os.path.basename(rel) == "README.md": continue
        spec = page_spec(repo, rel)
        # omics pages describe the source data; QTL results derived from it are listed on the QTL page
        if spec["kind"] not in ("qtl", "gwas", "study"): continue
        hits = []
        def walk(node, path, anc_qtl):  # anc_qtl: data types named by a parent folder
            for c in node["children"]:
                q = qtl_of(c["name"]) or anc_qtl
                if match(spec, c["name"], anc_qtl):
                    hit = {"at": "/".join(path), "d": strip(c)}
                    j = sorted(qtl_of(c["name"]) or q)
                    if len(j) > 1: hit["j"] = j
                    hits.append(hit)
                    continue
                files = [f for f in c["files"] if match(spec, f[0], q)]
                if files:
                    hit = {"at": "/".join(path + [c["name"]]), "id": c["ids"][:1], "f": files}
                    j = sorted({t for f in files for t in qtl_of(f[0]) if not (".*." in f[0] and qtl_of(f[0].split(".*.", 1)[1]))} | (q if len(q) > 1 else set()))
                    if len(j) > 1: hit["j"] = j
                    hits.append(hit)
                walk(c, path + [c["name"]], q)
        walk(tree, [], set())
        if hits: out[rel[:-3]] = hits
    return out

def count(node):
    n = 1 if node["name"] else 0; f = len(node["files"])
    for c in node["children"]:
        a, b = count(c); n += a; f += b
    return n, f

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out", default=None)
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    y = os.path.join(a.repo, "data", "statfungen_synapse_staging_folder_structure.yml")
    tree = parse(y)
    rows = []
    annotate(tree, page_ids(a.repo), [], [], rows)
    nf, nfiles = count(tree)
    ids = [i for r in rows for i in r[1].split(",") if i]
    def fids(n): return n.get("fileids", []) + [i for c in n["children"] for i in fids(c)]
    ids += fids(tree)
    raw = independent_ids(y)
    if a.out:
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        json.dump({"folders": nf, "files": nfiles, "ids": len(set(ids)),
                   "cited": sum(r[2] == "cited" for r in rows),
                   "tree": [strip(c) for c in tree["children"]],
                   "bypage": by_page(tree, a.repo)}, open(a.out, "w"), separators=(",", ":"))
    if a.report:
        for r in rows:
            if r[2] != "cited": print("\t".join(r))
    print(f"{nf} folders, {nfiles} file entries, {len(set(ids))} Synapse IDs; "
          f"{sum(r[2]=='cited' for r in rows)} cited by a page, {sum(r[2]=='parent' for r in rows)} under a cited parent, "
          f"{sum(r[2]=='none' for r in rows)} not under any cited folder")
    unparsed = sorted(raw - set(ids))
    extra = sorted(set(ids) - raw)
    if unparsed or extra:
        print("ID check FAILED. In the YAML but not on the page:", " ".join(unparsed) or "none",
              "| on the page but not in the YAML:", " ".join(extra) or "none", file=sys.stderr)
        sys.exit(1)
    print(f"ID check passed: all {len(raw)} Synapse IDs in the YAML are on the page")
