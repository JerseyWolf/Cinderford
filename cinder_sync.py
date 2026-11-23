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
        sources[p.name] = add(p.name, raw, sl, "gm" if gm else "", nav_gm if gm else nav_pub,
                              ver(p.name) if ver(p.name) >= 0 else "-")
    scripts = {q.name: q for q in list(root.glob("*.py")) + list(out.glob("*.py"))}
    for name, q in sorted(scripts.items()):
        sources[name] = add(name, q.read_bytes(), "script-" + Path(name).stem.replace("_", "-"), "scripts", nav_scr, "-")

    latest_n = saves[-1] if saves else -1
    latest = f"save-{latest_n:03d}" if saves else "save-none"
    nav_tmp, slot_rows = [], []
    for sname in SLOTS:
        sp = out / "temp" / f"{sname}.md"
        txt = sp.read_text(encoding="utf-8") if sp.exists() else ""
        body = re.sub(r"^# .*\n", "", txt).strip()
        state = "NONE" if (not body or body.startswith("NONE")) else "FILLED"
        if state == "FILLED":
            sn = slot_number(body)
            if sn is None and sname != "pending-hotfix":
                warns.append(f"temp/{sname}.md: first line is not a SAVE/STATUS NNN header")
            elif sn:
                root_n = latest_n if sn[0] == "save" else status_n
                root_file = root / f"{sn[0]}_{sn[1]:03d}.md"
                if sn[1] < root_n:
                    warns.append(f"temp/{sname}.md holds {sn[0]}_{sn[1]:03d}, older than root; check, then clear (NONE)")
                elif sn[1] == root_n and root_file.exists():
                    same = norm(root_file.read_bytes()).strip() == body.strip()
                    warns.append(f"temp/{sname}.md holds {sn[0]}_{sn[1]:03d}: " +
                                 ("identical to root, clear it (NONE)" if same else "DIFFERS from root copy: repair or conflict, resolve by hand"))
        nav_tmp.append(f"* [temp/{sname}](temp/{sname}.md)")
        slot_rows.append(f"- {BASE_URL}/{sname}.md | phone slot | {state} at last PC sync")

    readme = ["CINDERFORD SITE INDEX",
              "Each page is a verbatim copy of one source file (or one part) inside a code block.",
              "A file counts as read in full only if every part arrived, each ends with its END line,",
              "and page_bytes of all parts add up to bytes. Missing or mismatched = Rule 0.",
              "Split files: page name + -p1, -p2 ... (see PAGES for the exact list).",
              f"Page URL = {BASE_URL}/<page>.md  (GM pages: {BASE_URL}/gm/<page>.md). Append ?x=NNN (a new random three-digit number for every fetch).", "",
              f"LATEST SAVE: {latest}",
              "PHONE SLOTS are edited on the phone after this sync and may be newer than this README.",
              f"Always fetch all three at {BASE_URL}/<slot>.md (no temp/). A slot whose first line is",
              "SAVE/STATUS NNN higher than LATEST SAVE is the current one. Slot pages are not code-wrapped:",
              "read to the end of the page.", "",
              "LOAD LISTS"]
    for k, v in LOAD_LISTS.items():
        readme.append(f"{k}: " + ", ".join(latest if x == "SAVE" else x for x in v))
    readme += ["", "PAGES"] + rows + ["", "PHONE SLOTS"] + slot_rows
    if skipped: readme += ["", "SKIPPED (stale or superseded)"] + [f"- {x}" for x in skipped]
    readme += ["", "END OF INDEX"]
    body = "\n".join(readme) + "\n"
    f = fence_for(body)
    pages["README.md"] = f"# Index\n\n{f}text\n{body}{f}\n\n===== END FILE: README =====\n"
    pages["SUMMARY.md"] = "# Summary\n\n* [Index](README.md)\n" + "\n".join(nav_pub + nav_tmp + nav_scr + nav_gm) + "\n"
    if len(pages["README.md"].encode("utf-8")) > max_page:
        warns.append(f"README.md is {len(pages['README.md'].encode('utf-8'))} bytes, over {max_page} (it is never split)")
    return pages, sources, skipped, latest

def self_check(pages, sources, fails):
    by_src = {}
    for rel, txt in pages.items():
        if rel in ("README.md", "SUMMARY.md"): continue
        m = re.search(r"^SOURCE: (.+?) \|", txt, re.M)
        body = unwrap(txt)
        if not m or body is None:
            fails.append(f"{rel}: missing SOURCE or END line"); continue
        by_src.setdefault(m.group(1), []).append((rel, body))
        if is_gm(m.group(1)) and not rel.startswith("gm/"):
            fails.append(f"{rel}: GM file outside gm/")
    for name, (text, n) in sources.items():
        def part_no(r):
            mm = re.search(r"-p(\d+)\.md$", r[0])
            return int(mm.group(1)) if mm else 0
        parts = sorted(by_src.get(name, []), key=part_no)
        if n == 0:
            continue
        if len(parts) != n:
            fails.append(f"{name}: expected {n} pages, found {len(parts)}"); continue
        if "".join(b for _, b in parts) != text:
            fails.append(f"{name}: pages do not rebuild the source exactly")
    for link in re.findall(r"\]\(([^)]+)\)", pages["SUMMARY.md"]):
        if link not in pages and not link.startswith("temp/"):
            fails.append(f"SUMMARY link to missing page: {link}")

def git(root, *args, check=True):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(r.stdout + r.stderr); sys.exit(f"git {' '.join(args)} failed - nothing committed")
    return r.stdout.strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--max-page-bytes", type=int, default=15000,
                    help="largest published page, wrapper included (default 15000)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--no-git", action="store_true")
    a = ap.parse_args()
    here = Path(__file__).resolve().parent
    root = Path(a.root).resolve() if a.root else (here.parent if here.name == "site" else here)
    out = root / "site"
    out.mkdir(exist_ok=True)
    warns, fails = [], []

    if not a.no_git and not a.dry_run:
        git(root, "pull", "--rebase", "--autostash")
    pages, sources, skipped, latest = build(root, out, a.max_page_bytes, warns, fails)
    self_check(pages, sources, fails)

    yaml = root / "gitbook-docs.yaml"
    if not yaml.exists() or "directory: ./site" not in yaml.read_text(encoding="utf-8"):
        fails.append("gitbook-docs.yaml missing or not pointing at ./site")
    for stray in ("README.md", "SUMMARY.md"):
        if (root / stray).exists():
            warns.append(f"stray {stray} in repo root (delete it)")
    if (out / "gitbook-docs.yaml").exists():
        warns.append("extra site/gitbook-docs.yaml (delete it)")
    if (out / "temp").exists():
        for p in (out / "temp").glob("*.md"):
            if p.stem not in SLOTS:
                warns.append(f"site/temp/{p.name} is not a slot; GitBook will not show it")

    old = {str(p.relative_to(out)).replace("\\", "/"): p.read_text(encoding="utf-8")
           for p in out.rglob("*.md") if not str(p.relative_to(out)).replace("\\", "/").startswith("temp/")}
    added = sorted(set(pages) - set(old))
    removed = sorted(set(old) - set(pages))
    changed = sorted(k for k in set(pages) & set(old) if pages[k] != old[k])
    new_slots = [s for s in SLOTS if not (out / "temp" / f"{s}.md").exists()]

    print(f"Repo: {root}\nSources: {len(sources)} | pages: {len(pages)} | latest: {latest}")
    for t, lst in (("ADDED", added), ("UPDATED", changed), ("REMOVED", removed)):
        for x in lst: print(f"{t:8} {x}")
    for x in new_slots: print(f"SLOT     temp/{x}.md created")
    for x in skipped: print(f"SKIPPED  {x}")
    for w in warns: print(f"WARN     {w}")
    for x in fails: print(f"FAIL     {x}")
    if fails:
        sys.exit("\nSelf-check FAILED: nothing written, nothing committed.")
    if a.dry_run:
        print("\nDry run: nothing written."); return

    if added or changed or removed or new_slots:
        for k in removed:
            (out / k).unlink()
        for k, v in pages.items():
            dest = out / k
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(v, encoding="utf-8", newline="\n")
        for sname in new_slots:
            sp = out / "temp" / f"{sname}.md"
            sp.parent.mkdir(parents=True, exist_ok=True)
            sp.write_text(SLOT_EMPTY.format(s=sname), encoding="utf-8", newline="\n")
        for d in sorted(out.rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()): d.rmdir()
        print("\nSite written. Self-check PASS.")
    else:
        print("\nNo page changes.")
    if a.no_git: return

    git(root, "add", "-A", "--", *STAGE)
    if not git(root, "diff", "--cached", "--name-only"):
        print("Git: nothing to commit."); return
    msg = [f"Site sync: {len(added)} added, {len(changed)} updated, {len(removed)} removed (latest {latest})", ""]
    msg += [f"added {x}" for x in added] + [f"updated {x}" for x in changed] + [f"removed {x}" for x in removed]
    msg += [f"warn {w}" for w in warns]
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt", encoding="utf-8") as fh:
        fh.write("\n".join(msg) + "\n")
    git(root, "commit", "-F", fh.name)
    Path(fh.name).unlink()
    print("Committed:", git(root, "rev-parse", "--short", "HEAD"))
    if not a.no_push:
        git(root, "push")
        print("Pushed.")

if __name__ == "__main__":
    main()
