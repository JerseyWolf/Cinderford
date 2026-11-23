# script-cinder-sync-p1

SOURCE: cinder_sync.py | version=- | bytes=18885 | sha256=bcd5f38e5be0feb6 | part 1 of 2 | page_bytes=9608

````text
#!/usr/bin/env python3
r"""
cinder_sync.py v1 - one command after every Cinderford session (adapted from cinder_sync.py v4).
Put it in <repo>/site/cinder_sync.py (or the repo root) and run:
    python site\cinder_sync.py            # pull, build, check, commit, push
    python site\cinder_sync.py --dry-run  # show what would change, touch nothing
    python site\cinder_sync.py --no-push  # commit but don't push
    python site\cinder_sync.py --no-git   # build ./site only
Root *.md files are the master copies; the script never edits, moves or deletes them.
It builds ./site (pages split under --max-page-bytes, default 15000), writes README.md and SUMMARY.md
into ./site, puts gm_*.md under site/gm/, self-checks that every page rebuilds its source exactly,
then commits and pushes. Highest _vN of each file wins; older copies are skipped and listed.
Not published: the design brief and the hand-written cinderford_README (the generated README replaces it).
PHONE SLOTS: site/temp/pending-save.md, pending-status.md, pending-hotfix.md are created if missing and
never overwritten. Edit them on github.com; put NONE back once the file is in the repo root and synced.
Needs gitbook-docs.yaml in the repo root containing "directory: ./site".
"""
import argparse, hashlib, re, subprocess, sys, tempfile
from pathlib import Path

BASE_URL = "https://CHANGE-ME.gitbook.io/cinderford-docs"  # <- your Cinderford GitBook URL
SLOTS = ["pending-save", "pending-status", "pending-hotfix"]
SLOT_EMPTY = "# {s}\n\nNONE\n\nPhone slot. Replace NONE with the whole file (its own first line kept). Put NONE back once the file is in the repo root and synced.\n"
GM_PATTERNS = [r"^gm_"]
SKIP_PATTERNS = [r"^bundle_", r"^readme", r"^summary", r"^cinderford_readme", r"^cinderford_design_brief", r"^hearth_design_brief", r"_patch(_v\d+(-\d+)?)?\.md$"]
STAGE = ["site", ":(glob)*.md", ":(glob)*.py", "gitbook-docs.yaml"]
HEADING = re.compile(
    r"^(==+ .+ ==+|-- .+ --|END OF PUBLIC|END OF GM|GM( ONLY)?:?|"
    r"\d+(\.\d+)? [A-Z][A-Z0-9 /&()+-]{2,}|[A-Z][A-Z0-9 _/&()+-]{3,}:?|[A-Z][A-Z0-9_]+:.*|P\d .+|Q\d+ .+|C\d .+)\s*$")
LOAD_LISTS = {
    "STARTUP PLAY": ["index", "narration", "rules", "skills-ledger", "fire-powers", "hearth-spells", "buildings",
                     "settlers", "arrivals", "world", "status", "SAVE", "pending-save", "pending-status", "pending-hotfix",
                     "gm/world-gm", "gm/arrival-tables", "gm/settlers-gm", "gm/pantheon"],
    "STARTUP DREAM": ["index", "lesson-chat-instructions", "skills-ledger", "curriculum",
                      "gravesong-curriculum-p1", "gravesong-curriculum-p2", "spells", "hearth-spells", "spell-code",
                      "pending-hotfix"],
    "PLANNING": ["only the pages the task needs"],
}

def ver(name):
    m = re.search(r"_v(\d+)(?=\.md$)", name, re.I)
    return int(m.group(1)) if m else -1

def base_key(name):
    return re.sub(r"_v\d+(-\d+)?(?=\.md$)", "", name, flags=re.I).lower()

def slug(name):
    stem = Path(base_key(name)).stem
    m = re.match(r"^(save|status)_(\d{3})$", stem)
    if m:
        return "status" if m.group(1) == "status" else f"save-{m.group(2)}"
    stem = re.sub(r"_v\d+(?=_p\d+$)", "", stem)
    stem = re.sub(r"^gm_", "", re.sub(r"^\d+[a-z]?_", "", stem))
    stem = re.sub(r"_cinderford(?=$|_)", "", stem)
    return stem.replace("_", "-")

def is_gm(name):
    return any(re.search(x, name, re.I) for x in GM_PATTERNS)

def fence_for(t):
    n = 4
    while "`" * n in t:
        n += 1
    return "`" * n

def split_sections(text, limit):
    """Split into the fewest parts whose bodies fit `limit` bytes, sized as evenly as possible.
    Each break prefers the last heading in the part (if it falls past 40% of the part).
    Returns None if some single line is longer than `limit`."""
    total = len(text.encode("utf-8"))
    if total <= limit:
        return [text]
    if max(len(l.encode("utf-8")) for l in text.splitlines(keepends=True)) > limit:
        return None
    n = -(-total // limit)
    while True:
        for slack in (1.02, 1.05, 1.10, 1.20, 1.35):
            target = min(limit, int(total / n * slack))
            parts = _greedy(text, target)
            if len(parts) <= n and all(len(p.encode("utf-8")) <= limit for p in parts):
                return parts
        n += 1
        if n > total:
            return _greedy(text, limit)

def _greedy(text, limit):
    parts, cur, size, last_head = [], [], 0, None
    for line in text.splitlines(keepends=True):
        b = len(line.encode("utf-8"))
        if cur and size + b > limit:
            if last_head is not None and last_head > len(cur) * 0.4:
                parts.append("".join(cur[:last_head])); cur = cur[last_head:]
            else:
                parts.append("".join(cur)); cur = []
            size = sum(len(l.encode("utf-8")) for l in cur)
            last_head = None
        if cur and HEADING.match(line.strip()):
            last_head = len(cur)
        cur.append(line); size += b
    if cur:
        parts.append("".join(cur))
    return parts

def page_overhead(name, version, raw_len, sha, page):
    """Bytes the wrapper adds around a body, for the worst case (split, long fence, 2-digit parts)."""
    probe = render(name, version, raw_len, sha, "`" * 9 + "\n", 99, 99, page + "-p99")
    return len(probe.encode("utf-8")) - len(("`" * 9 + "\n").encode("utf-8")) + 8

def norm(raw):
    t = raw.decode("utf-8", errors="replace").replace("\r\n", "\n")
    return t if t.endswith("\n") else t + "\n"

def choose(root, warns):
    files = [p for p in root.glob("*.md") if not any(re.search(x, p.name, re.I) for x in SKIP_PATTERNS)]
    statuses = sorted([p for p in files if re.match(r"status_\d{3}\.md$", p.name, re.I)], key=lambda p: p.name.lower())
    if len(statuses) > 1:
        warns.append(f"{len(statuses)} status files in root; using {statuses[-1].name}")
    chosen, skipped = {}, []
    for p in files:
        if p in statuses[:-1]:
            skipped.append(f"{p.name} (older status)"); continue
        k = base_key(p.name)
        if k in chosen:
            keep, drop = (p, chosen[k]) if ver(p.name) > ver(chosen[k].name) else (chosen[k], p)
            chosen[k] = keep; skipped.append(f"{drop.name} (superseded by {keep.name})")
        else:
            chosen[k] = p
    return sorted(chosen.values(), key=lambda p: p.name.lower()), skipped

def render(name, version, raw_len, sha, chunk, i, n, page):
    tag = f" | part {i} of {n}" if n > 1 else ""
    end = f"===== END FILE: {name} =====" if i == n else f"===== END PAGE: {name} | part {i} of {n} ====="
    f = fence_for(chunk)
    return (f"# {page}\n\nSOURCE: {name} | version={version} | bytes={raw_len} | sha256={sha}{tag} | "
            f"page_bytes={len(chunk.encode('utf-8'))}\n\n{f}text\n{chunk}{f}\n\n{end}\n")

def unwrap(page_text):
    m = re.search(r"\n(`{4,})text\n(.*)\n\1\n\n===== END (FILE|PAGE):", page_text, re.S)
    return (m.group(2) + "\n") if m else None

def slot_number(body):
    for line in body.splitlines():
        line = line.strip().strip("`").strip()
        if not line or line.lower() == "text":
            continue
        m = re.match(r"^(save|status)[ _](\d{3})\b", line, re.I)
        return (m.group(1).lower(), int(m.group(2))) if m else None
    return None

def build(root, out, max_page, warns, fails):
    files, skipped = choose(root, warns)
    pages, rows, nav_pub, nav_gm, nav_scr, slugs = {}, [], [], [], [], {}
    saves = sorted(int(m.group(1)) for p in files if (m := re.match(r"save_(\d{3})\.md$", p.name, re.I)))
    status = [p for p in files if re.match(r"status_\d{3}\.md$", p.name, re.I)]
    status_n = int(status[0].name[7:10]) if status else -1
    if saves:
        gaps = sorted(set(range(saves[0], saves[-1] + 1)) - set(saves))
        if gaps: warns.append(f"missing saves: {', '.join(f'{g:03d}' for g in gaps)}")
        if status and status_n != saves[-1]:
            warns.append(f"{status[0].name} does not match newest save_{saves[-1]:03d}")

    def add(src_name, raw, sl, folder, nav, version):
        text = norm(raw)
        sha = hashlib.sha256(raw).hexdigest()[:16]
        body_limit = max_page - page_overhead(src_name, version, len(raw), sha, sl)
        chunks = split_sections(text, body_limit)
        if chunks is None:
            fails.append(f"{src_name}: a single line is longer than {body_limit} bytes; break that line in the source")
            return text, 0
        n = len(chunks)
        for i, c in enumerate(chunks, 1):
            page = sl if n == 1 else f"{sl}-p{i}"
            rel = f"{folder}/{page}.md" if folder else f"{page}.md"
            pages[rel] = render(src_name, version, len(raw), sha, c, i, n, page)
            if len(pages[rel].encode("utf-8")) > max_page:
                fails.append(f"{rel}: page is {len(pages[rel].encode('utf-8'))} bytes, over {max_page}")
            rows.append(f"- {BASE_URL}/{rel} | {src_name} | bytes={len(raw)} | sha256={sha}" + (f" | part {i}/{n}" if n > 1 else ""))
            nav.append(f"* [{rel[:-3]}]({rel})")
        return text, n

    sources = {}
    for p in files:
        raw = p.read_bytes()
        first = norm(raw).splitlines()[0] if raw else ""
        m = re.search(r"\bv(\d+)\b", first)
        if ver(p.name) >= 0 and m and int(m.group(1)) != ver(p.name):
            warns.append(f"{p.name}: filename v{ver(p.name)} but first line says v{m.group(1)}")
        sl = slug(p.name)
        if sl in slugs:
            fails.append(f"page name clash: {p.name} and {slugs[sl]}"); continue
        slugs[sl] = p.name
        gm = is_gm(p.name)
````

===== END PAGE: cinder_sync.py | part 1 of 2 =====
