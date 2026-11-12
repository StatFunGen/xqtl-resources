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
import re, os, glob, json, argparse

SYN = re.compile(r"\bsyn\d{5,}\b")

def expand(s):
    """'syn726677{15..21}' -> [syn72667715 .. syn72667721]; also plain comma lists."""
    out = []
    for part in [p.strip() for p in s.split(",") if p.strip()]:
        m = re.match(r"(syn\d*)\{(\d+)\.\.(\d+)\}$", part)
        if m:
            pre, a, b = m.group(1), m.group(2), m.group(3)
            out += [f"{pre}{str(i).zfill(len(a))}" for i in range(int(a), int(b) + 1)]
        elif re.match(r"syn\d{5,}$", part):
            out.append(part)
    return out

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
    raw = {i for line in open(y) if "#" in line for i in expand(line.split("#", 1)[1])}
    if a.out:
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        json.dump({"folders": nf, "files": nfiles, "ids": len(set(ids)),
                   "cited": sum(r[2] == "cited" for r in rows),
                   "tree": [strip(c) for c in tree["children"]]}, open(a.out, "w"), separators=(",", ":"))
    if a.report:
        for r in rows:
            if r[2] != "cited": print("\t".join(r))
    print(f"{nf} folders, {nfiles} file entries, {len(set(ids))} Synapse IDs; "
          f"{sum(r[2]=='cited' for r in rows)} cited by a page, {sum(r[2]=='parent' for r in rows)} under a cited parent, "
          f"{sum(r[2]=='none' for r in rows)} not under any cited folder")
    unparsed = sorted(i for i in raw if i not in set(ids))
    if unparsed: print("IDs in the YAML the parser did not attach to a folder:", " ".join(unparsed))
