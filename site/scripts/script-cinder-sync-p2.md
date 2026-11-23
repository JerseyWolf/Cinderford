# script-cinder-sync-p2

SOURCE: cinder_sync.py | version=- | bytes=18885 | sha256=bcd5f38e5be0feb6 | part 2 of 2 | page_bytes=9277

````text
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
````

===== END FILE: cinder_sync.py =====
