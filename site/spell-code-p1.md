# spell-code-p1

SOURCE: 13_spell_code_v3.md | version=3 | bytes=21963 | sha256=d1c41978096fdbf4 | part 1 of 2 | page_bytes=11187

````text
# Thornwall — Spell code, v3

Supersedes v2 (18 Nov 2026 planning repair): starter rule aligned with the ledger v8 spell ruling; the 11 spells granted at Basic marked as known. No code changed.

AUTHORITY: the exact code of every spell, one entry per spell, current version only. Spell meaning, steps and effects live in 09_spells (read only). Which spell Florence knows, and at which step, lives in the skills ledger. Creating this file advances no time and grants nothing.

Format: lists and code blocks only, no tables (player ruling).

## How this file works

- Every entry starts as a STARTER at Basic, version 0. Ledger v8 spell ruling: every spell of a subject at full rank Beginner or higher is KNOWN at Basic automatically, and its starter (version 0) is its Basic code; no approval session is needed. Starters of Novice subjects are not known and cannot be cast. Dream sessions are only for reviews and upgrades above Basic. Which spells are known: the ledger alone.
- On approval the entry becomes: `### <Name> — <step> · version <n>`, with the approved code, the ledger version, the reviewer and review notes. The ledger gets the spell's name, phrase, step, mana and current effect.
- On each upgrade the code here is REPLACED by the newly approved code and the version goes up by one. Older versions are not kept.
- Starters aim at the Basic bar: about 20 lines, normal input only, no guards. That is deliberate: the guards, tests and lint are what the next steps ask for (09_spells §4).
- Second Voice, Echo Chamber and Familiar Bond restarted at Basic (player ruling, spells v3; ledger v8). Their old Plain code in ledger v6 is retired; its grading notes are still useful as hints for later steps.
- Commands marked "commands" are the spell for CLI-only subjects (Git, Docker, Azure); a file name shows where a file goes.
- Real-world care: Door Census on your own machine only; Azure spells create real resources, so delete what you make; Haunt is a real network listener, so bind it to your tunnel address only.

## Entry format

```
### <Name> — <step> · version <n>
Subject: <subject> · Language: <language> · Approved: <ledger version> · Reviewed by: <mentor>
Review notes: <what passed; what the next step needs>
<exact code>
```

## Python (Isaura Venn)

### Tally Stone — Basic · version 0 (starter)
Subject: Python · Language: Python · Approved: — (not known) · Reviewed by: Isaura Venn (when brought)
What to learn from it: sys.argv, with-open, len(). Run: python tally.py notes.txt
File: tally.py
```python
import sys

path = sys.argv[1]

with open(path, encoding="utf-8") as text_file:
    lines = text_file.readlines()

print(f"{path}: {len(lines)} lines")
```

### Hearth-Reckoner — Basic · version 0 (starter)
Subject: Python · Language: Python · Approved: — (not known) · Reviewed by: Isaura Venn (when brought)
What to learn from it: float conversion, a named constant, f-string formatting. Run: python reckoner.py 12
File: reckoner.py
```python
import sys

FEET_PER_METRE = 3.28084

metres = float(sys.argv[1])
feet = metres * FEET_PER_METRE

print(f"{metres} m = {feet:.1f} ft")
```

### Read the Fight — Basic · version 0 (starter)
Subject: Python · Language: Python · Approved: — (not known) · Reviewed by: Isaura Venn (when brought)
What to learn from it: looping over a file line by line, a counter, a condition. Run: python read_fight.py app.log
File: read_fight.py
```python
import sys

path = sys.argv[1]
error_count = 0

with open(path, encoding="utf-8") as log_file:
    for line in log_file:
        if "ERROR" in line:
            error_count += 1

print(f"{path}: {error_count} ERROR lines")
```

## Linux/Bash (Runa Kettleby)

### Lantern Sweep — Basic · version 0 (granted starter)
Subject: Linux/Bash · Language: Bash · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Runa Kettleby (for upgrades)
What to learn from it: shebang, a quoted variable, a pipeline, hiding errors with 2>/dev/null. Run: bash lantern.sh ~/graves
File: lantern.sh
```bash
#!/usr/bin/env bash

target="$1"

echo "The five biggest things in $target:"
du -ah "$target" 2>/dev/null | sort -rh | head -n 5
```

### Quiet Watch — Basic · version 0 (granted starter)
Subject: Linux/Bash · Language: Bash · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Runa Kettleby (for upgrades)
What to learn from it: tail -f follows a growing file; --line-buffered makes grep print at once. Stop with Ctrl+C. Run: bash watch.sh camp.log wolf
File: watch.sh
```bash
#!/usr/bin/env bash

log_file="$1"
pattern="$2"

echo "Watching $log_file for: $pattern"
tail -f "$log_file" | grep --line-buffered "$pattern"
```

### Night Shift — Basic · version 0 (granted starter)
Subject: Linux/Bash · Language: Bash + systemd (user units) · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Runa Kettleby (for upgrades)
What to learn from it: a service says WHAT runs, a timer says WHEN; %h means your home directory; user units need no sudo.
File: ~/bin/night-shift.sh
```bash
#!/usr/bin/env bash
echo "$(date '+%F %T') the fire is fed" >> "$HOME/night-shift.log"
```
File: ~/.config/systemd/user/night-shift.service
```ini
[Unit]
Description=Night Shift: feed the fire

[Service]
Type=oneshot
ExecStart=%h/bin/night-shift.sh
```
File: ~/.config/systemd/user/night-shift.timer
```ini
[Unit]
Description=Night Shift every hour

[Timer]
OnCalendar=hourly

[Install]
WantedBy=timers.target
```
File: commands
```bash
chmod +x ~/bin/night-shift.sh
systemctl --user daemon-reload
systemctl --user enable --now night-shift.timer
systemctl --user list-timers
```

## Git/Gerrit (Runa Kettleby)

### Mark — Basic · version 0 (granted starter)
Subject: Git/Gerrit · Language: Git CLI · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Runa Kettleby (for upgrades)
What to learn from it: status first, stage one named file (never git add . blindly), an imperative commit message.
File: commands
```bash
# condition.txt describes the person or object right now
git status
git add condition.txt
git commit -m "Mark Wim's left arm before the wolf hunt"
git log --oneline -n 1
```

### Diff — Basic · version 0 (granted starter)
Subject: Git/Gerrit · Language: Git CLI · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Runa Kettleby (for upgrades)
What to learn from it: HEAD~1 is the commit before HEAD; read the hunk: lines with - were removed, lines with + were added.
File: commands
```bash
# compare the last Mark with the one before it
git log --oneline -n 2
git diff HEAD~1 HEAD -- condition.txt
```

### Revert — Basic · version 0 (granted starter)
Subject: Git/Gerrit · Language: Git CLI · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Runa Kettleby (for upgrades)
What to learn from it: revert makes a NEW commit that undoes the last one, so shared history stays safe (unlike reset).
File: commands
```bash
git log --oneline -n 3
git revert --no-edit HEAD
git log --oneline -n 3
```

## Cybersecurity (Zofia Drell)

### Whisper Lock — Basic · version 0 (starter)
Subject: Cybersecurity · Language: Python (secrets) · Approved: — (not known) · Reviewed by: Zofia Drell (when brought)
What to learn from it: secrets, not random, for anything that guards a door; a list comprehension; join. Run: python whisper_lock.py
File: whisper_lock.py
```python
import secrets

WORDS = [
    "grave", "spade", "yew", "lantern", "salt", "thorn",
    "ferry", "snowdrop", "raven", "barrow", "moss", "bell",
]

chosen = [secrets.choice(WORDS) for _ in range(4)]

print("-".join(chosen))
```

### Door Census — Basic · version 0 (starter)
Subject: Cybersecurity · Language: Bash (ss) · Approved: — (not known) · Reviewed by: Zofia Drell (when brought)
What to learn from it: ss lists listening sockets (-t TCP, -u UDP, -l listening, -n numbers); tail skips the header; awk picks columns. 0.0.0.0 means open to everyone, 127.0.0.1 means this machine only.
File: door_census.sh
```bash
#!/usr/bin/env bash
# Own machine only.

echo "Listening doors on this machine:"
ss -tuln | tail -n +2 | awk '{print $1, $5}'
```

### Seal-Sniffer — Basic · version 0 (starter)
Subject: Cybersecurity · Language: Python (re) · Approved: — (not known) · Reviewed by: Zofia Drell (when brought)
What to learn from it: a compiled regex, enumerate for line numbers, and never printing the secret itself. Run: python seal_sniffer.py app.py
File: seal_sniffer.py
```python
import re
import sys

path = sys.argv[1]
pattern = re.compile(r"password\s*=\s*\S+", re.IGNORECASE)

with open(path, encoding="utf-8") as source:
    for number, line in enumerate(source, start=1):
        if pattern.search(line):
            print(f"{path}:{number}: possible secret")
```

## Docker/Kubernetes (Hedda Stroud)

### Bottled Hearth — Basic · version 0 (granted starter)
Subject: Docker/K8s · Language: docker CLI · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Hedda Stroud (for upgrades)
What to learn from it: flags before the image name; -p HOST:CONTAINER; check with ps, curl and logs; stop, then remove.
File: commands
```bash
docker run -d --name hearth -p 8080:80 nginx
docker ps
curl http://localhost:8080
docker logs hearth
docker stop hearth
docker rm hearth
```

### Calling Post — Basic · version 0 (granted starter)
Subject: Docker/K8s · Language: docker CLI (ports) · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Hedda Stroud (for upgrades)
What to learn from it: binding to 127.0.0.1 keeps the post private to this machine; docker port shows container side first, then host side.
File: commands
```bash
docker run -d --name post -p 127.0.0.1:8081:80 nginx
docker port post
curl http://127.0.0.1:8081
docker rm -f post
```

### Sealed Vessel — Basic · version 0 (granted starter)
Subject: Docker/K8s · Language: Dockerfile · Approved: granted at Basic, ledger v8 spell ruling · Reviewed by: Hedda Stroud (for upgrades)
What to learn from it: FROM, WORKDIR, COPY, ENTRYPOINT; it seals Tally Stone in a container (it counts its own lines here).
File: Dockerfile
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY tally.py .

ENTRYPOINT ["python", "tally.py"]
```
File: commands
```bash
docker build -t vessel .
docker run --rm vessel tally.py
```

## IaC (Tamsin Oake)

### Boundary Chart — Basic · version 0 (starter)
Subject: IaC · Language: YAML + yamllint · Approved: — (not known) · Reviewed by: Tamsin Oake (when brought)
What to learn from it: mappings, a list, integers vs strings, the --- document start. The JSON Schema comes at a later step.
File: ward.yaml
```yaml
---
ward:
  name: camp ring
  length_m: 3
  alarm: palm tingle
  lasts_hours: 1
  watch_for:
    - wolf
    - stranger
```
File: commands
```bash
yamllint ward.yaml
```

### Lint Eye — Basic · version 0 (starter)
Subject: IaC · Language: yamllint config · Approved: — (not known) · Reviewed by: Tamsin Oake (when brought)
What to learn from it: yamllint finds .yamllint in the folder by itself; truthy catches the Norway problem (yes, no, on, off).
File: .yamllint
```yaml
---
````

===== END PAGE: 13_spell_code_v3.md | part 1 of 2 =====
