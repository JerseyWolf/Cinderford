# spells-p2

SOURCE: 09_spells_v3.md | version=3 | bytes=41726 | sha256=fe16321c60d69f8c | part 2 of 3 | page_bytes=14181

````text
Effects by step:
- Basic: Marks one object (not a person) until sunset.
- Novice: One person or object until their next full sleep.
- Beginner: Two Marks at once.
- Apprentice: Marks last 2 days; he can see the marked state like a memory.
- Journeyman: Marks last a week, up to 4 at once.
- Expert: He senses when a marked target's condition changes, anywhere in the valley.
- Master: A Mark can be taken by touch after the fact, back to that morning.
- Grandmaster: Permanent Marks on up to 10 targets, each keeping a history of every change.

### Diff
- Subject: Git/Gerrit (Runa Kettleby)
- Language: Git CLI
- Phrase: "Show me what was taken."
- Real task: Use log/diff to find and explain a change
- Code path: one git diff read aloud → --staged, rename detection, whitespace noise ignored, log -p/bisect tooling with a written explanation

Effects by step:
- Basic: Yes or no to "has this changed since I last saw it?" for one object.
- Novice: Names one change (a new wound, a moved item).
- Beginner: Lists every change against a Mark: wounds, poison, tampering.
- Apprentice: Also roughly when each change happened.
- Journeyman: Works without a Mark on anything he has seen before, from memory.
- Expert: Names the cause in general terms ("a blade", "nightshade", "a second key").
- Master: Bisect: points to the moment and the hand, a glimpse of who did it.
- Grandmaster: Legendary: reads a room's or a body's full history of change back a year, like turning pages.

### Revert
- Subject: Git/Gerrit (Runa Kettleby)
- Language: Git CLI
- Phrase: "Death, give back what you took."
- Real task: Safely undo a bad commit (revert vs reset)
- Code path: git revert HEAD → revert vs reset reasoning, conflicts, shared history, scripted tested recovery

Effects by step:
- Basic: Takes the −5 penalty off one Bruised wound for an hour; the wound stays. Needs a Mark.
- Novice: Turns a Bruised wound into a scratch. Needs a Mark; once per person per day.
- Beginner: Undoes one Bruised level. Needs a Mark; once per person per day.
- Apprentice: Undoes Bruised; can also restore a broken object to its marked state.
- Journeyman: Undoes Hurt to Bruised, or two Bruised.
- Expert: Twice per person per day; works from a Mark up to a week old.
- Master: No Mark needed if the injury is less than an hour old.
- Grandmaster: Legendary: undoes Badly hurt to Hurt, once per person per day; can reverse a poison or curse back to the last Mark.

Notes:
- Healing spell (section 7). Mark and daily limits as section 7.

## Cybersecurity (Zofia Drell)

### Whisper Lock
- Subject: Cybersecurity (Zofia Drell)
- Language: Python (secrets)
- Phrase: "Only the dead know the way in."
- Real task: Passphrase generator
- Code path: 4 words with secrets.choice → wordlist file, entropy shown, no random module, length/policy arguments, distribution tests, packaged CLI

Effects by step:
- Basic: Seals one small container (box, purse) until sunset; a firm tug breaks it.
- Novice: One door or chest until sunset; opens to the word, or to forcing against his Cybersecurity rank.
- Beginner: Holds a day; forcing it is Hard; he feels attempts.
- Apprentice: Holds a week; he can give the word to one person.
- Journeyman: Up to 3 seals; each tells him who tried it (a face, as a feeling).
- Expert: A seal can hold a room's windows and doors as one; forcing is Extreme.
- Master: Up to 5 keyholders per seal with different words; any word can be revoked from afar.
- Grandmaster: Legendary: permanent wards on up to 3 places; only the named living or dead pass; breaking one takes a ritual, not a crowbar.

### Door Census
- Subject: Cybersecurity (Zofia Drell)
- Language: Bash (ss, nmap localhost)
- Phrase: "No exit escapes my sight."
- Real task: Listening-ports report on own machine only
- Code path: ss -tulpn to a list → process names, allowlist of expected vs surprising, nmap localhost cross-check, stderr, bats tests, scheduled change report

Effects by step:
- Basic: Names how many exits the room he stands in has.
- Novice: Shows every door and window of one room, including the obvious hidden ones.
- Beginner: A whole floor, including hatches and loose panels.
- Apprentice: A whole building; flags exits watched or in use right now.
- Journeyman: Marks surprising exits not on the builder's plan (priest hole, tunnel).
- Expert: Shows how each exit is secured: locked, barred, warded, guarded.
- Master: A keep and its grounds; routes between exits ranked for a quiet escape.
- Grandmaster: Legendary: a standing map of one place for a week; he feels each exit open.

### Seal-Sniffer
- Subject: Cybersecurity (Zofia Drell)
- Language: Python (regex)
- Phrase: "Your secrets reek of rot."
- Real task: Secret scanner over files
- Code path: one regex for password= over one file → several patterns, directory walk, binary skip, false-positive suppression, entropy, tests, CI, git-history scan

Effects by step:
- Basic: A vague smell of rot near one trap or hidden compartment within arm's reach.
- Novice: Finds one trap or compartment in a small room.
- Beginner: All of them in a room, and which are traps.
- Apprentice: Each trap's type (needle, blade, alarm, poison) and the safe way to trigger it.
- Journeyman: Works on people by touch: hidden blades, poisons, forged papers.
- Expert: A whole building, including old sealed-over hiding places.
- Master: Follows the rot: a direction and a feeling toward who placed the trap.
- Grandmaster: Legendary: no mechanical trap can surprise him; magical traps sensed within 50 m.

## Docker/Kubernetes (Hedda Stroud)

### Bottled Hearth
- Subject: Docker/K8s (Hedda Stroud)
- Language: docker CLI
- Phrase: "Wake the hearth in the glass."
- Real task: Run and reach a web-server container
- Code path: docker run -d -p + curl → pinned tag, --name, health check, logs, clean stop and rm, restart policy, Compose with script and tests

Effects by step:
- Basic: A candle-sized flame in a bottle for one hour; warms his hands.
- Novice: A small fire for one person for a night; cooks one pot.
- Beginner: A camp fire plus a one-person shelter (dry, windproof) for a night.
- Apprentice: Shelter for 3; won't burn out in rain or wind.
- Journeyman: Shelter for 6, a light only allies see; re-bottled in the morning.
- Expert: A small sealed room with door, lock and warmth that stands a blizzard.
- Master: A hut with beds, cookfire and privy that keeps Danger 10 animals out.
- Grandmaster: Legendary: a field hall that feeds and dries 12, holds one night against Danger 25, and fits in a coat pocket.

### Calling Post
- Subject: Docker/K8s (Hedda Stroud)
- Language: docker CLI (ports)
- Phrase: "I summon thee from beyond."
- Real task: Port mapping and reaching a service
- Code path: one -p 8080:80 + curl → binding address, port-conflict check, docker port check, 127.0.0.1-only option, scripted check-and-retry

Effects by step:
- Basic: His hired or owned mount within 100 m hears him and looks up; it may come.
- Novice: Within 500 m it comes, at its own pace.
- Beginner: Within 2 km, at a trot; it can leave an unlatched stall.
- Apprentice: Within 5 km; comes even when frightened, avoiding danger on the way.
- Journeyman: He can call any animal he has handled, not just his own.
- Expert: A tethered or locked-in mount slips its bonds, quietly.
- Master: Brings a cart or a led horse; he can call a whole stable.
- Grandmaster: Legendary: his mount reaches him anywhere in the valley within the hour, fresh, as if it came through the dark between places.

### Sealed Vessel
- Subject: Docker/K8s (Hedda Stroud)
- Language: Dockerfile
- Phrase: "Rot shall not take you."
- Real task: Dockerfile for a Python CLI
- Code path: FROM, COPY, CMD → pinned base, non-root, .dockerignore, no ENV secrets, layer caching, multi-stage, healthcheck, Trivy scan, size budget

Effects by step:
- Basic: Keeps one meal fresh for a day.
- Novice: One day's rations for a week.
- Beginner: A pack's food and water for a month; water stays clean.
- Apprentice: Also medicine and potions; wounds kept in it don't fester (no infection).
- Journeyman: A cart's stores for a season, through damp and heat.
- Expert: Keeps a body from rotting for a month (for burial, or for the dead to speak).
- Master: Poisoned food in the vessel shows itself.
- Grandmaster: Legendary: anything sealed stays exactly as it was for a year, even fresh flowers.

## IaC (Tamsin Oake)

### Boundary Chart
- Subject: IaC (Tamsin Oake)
- Language: YAML + JSON Schema
- Phrase: "The border of my domain."
- Real task: YAML description validated with yamllint + JSON Schema
- Code path: 10-line YAML ward + yamllint → schema with types and required fields, Norway problem, duplicate keys, tests over bad files, validated boundary library

Effects by step:
- Basic: A line about 3 m long that tingles in his palm if crossed, for an hour.
- Novice: A 10 m line for a night; he wakes if it is crossed.
- Beginner: A closed ring round a small camp (20 m) for a night.
- Apprentice: A 50 m ring; tells where and how many crossed.
- Journeyman: Up to 3 rings, each with its own rules ("ignore sheep").
- Expert: A 200 m ring; tells what crossed (person, animal, the dead).
- Master: A whole yard or village edge for a week, with an allowlist of named people.
- Grandmaster: Legendary: a standing border for a season; denylisted crossers feel cold dread and need a Deathspeech or Insight check to keep going.

### Lint Eye
- Subject: IaC (Tamsin Oake)
- Language: yamllint config
- Phrase: "Find the crack before the frost does."
- Real task: Write a yamllint config and fix a broken file
- Code path: default yamllint on one file → custom config (indentation, truthy, line length), tabs and quoting fixed, CI lint, pre-commit and team config with rationale

Effects by step:
- Basic: Points to the single worst crack in one touched object (a rope, a plank).
- Novice: One wall, bridge or ice patch: will it hold him, yes or no.
- Beginner: Every weak point and roughly how much weight each takes.
- Apprentice: Whole structures (a house, a stairwell); +5 to the next Athletics check to climb or cross it.
- Journeyman: Warns an hour before a structure fails, and why.
- Expert: Armour and gear too: flaws show before they break (scratches instead of failures for a day).
- Master: A keep or ruin: marks a safe path through a collapsing place (collapse Danger one tier lower).
- Grandmaster: Legendary: no failing structure surprises him; one named point is frost-proofed and holds for a day whatever happens.

### Standing Stone
- Subject: IaC (Tamsin Oake)
- Language: Ansible
- Phrase: "Obey the law of the stone."
- Real task: Idempotent playbook
- Code path: one task run twice → several tasks, handlers, variables and facts, second run changes nothing, --check dry run, roles, vault, Molecule tests

Effects by step:
- Basic: Puts one small item back in its declared place (a dropped knife to its sheath).
- Novice: Tidies one pack to its declared state.
- Beginner: A whole camp back in order (tents, fire ring, kit) in one exchange.
- Apprentice: Also small damage: torn straps, a bent buckle, an edge back to its last sharpening.
- Journeyman: One worn armour layer repaired from a scratch or minor tear.
- Expert: A room or yard back as declared, including salt lines patched and turf set.
- Master: A broken weapon or armour piece restored once per day; declared state kept for 5 objects.
- Grandmaster: Legendary: up to 3 declared places return to their state every dawn; a declared grave never stays disturbed.

## Azure (Calla Mirelle)

### Tower Census
- Subject: Azure (Calla Mirelle)
- Language: Azure CLI
- Phrase: "Your hoard is laid bare."
- Real task: List, tag and cost-check resources; delete; prove zero bill
- Code path: az group list → subscription check first, tag filters, cost query, confirmed delete, zero-bill proof, scheduled report with alerts

Effects by step:
- Basic: A rough total value of one touched purse or pack.
- Novice: Every item in one pack, with rough values.
- Beginner: A whole party's inventory, including forgotten items.
- Apprentice: Who owns what; borrowed, stolen or pawned items show.
- Journeyman: Debts and promises owed, as threads ("owes Calla 5").
- Expert: A whole household or shop: stock, cash and hidden reserves.
- Master: Follows money: a payment traced back two steps.
- Grandmaster: Legendary: a standing ledger of one organisation (guild, council) for a week; every coin in or out tugs at him.

### Budget Bell
- Subject: Azure (Calla Mirelle)
- Language: Azure CLI + JSON
- Phrase: "Toll for the spent."
- Real task: Create a budget with alerts
- Code path: one budget create with one threshold → several thresholds, currency and scope checks, JSON from file, action groups, IaC-managed budgets with tests

Effects by step:
- Basic: A faint chime when his own mana falls to a threshold he sets, until sunset.
- Novice: Mana or coins, one threshold, for a day.
- Beginner: Two thresholds, mana and coins, for a day.
- Apprentice: Also one other person's health level (set by touch); chimes when they get worse.
- Journeyman: Up to 3 people or stores (a larder, a quiver's bolts) for a week.
- Expert: Forecast: warns an hour before a threshold will be crossed at the current rate.
- Master: The whole party's mana, health and supplies, as tones only he hears.
- Grandmaster: Legendary: when it tolls it gives back 2 mana to the one it warns for, once per day each.

### Rented Vault
- Subject: Azure (Calla Mirelle)
- Language: Azure CLI
- Phrase: "Keep this beyond the veil."
- Real task: Storage account + private blob container
- Code path: create account, upload one file → keys out of scripts, public access off, expiring SAS, managed identity, soft-delete and versioning, lifecycle rules, IaC, tests

Effects by step:
- Basic: One coin-sized object kept beyond the veil until sunset, then it drops back into his hand.
- Novice: One palm-sized item for a day.
- Beginner: About 1 kg for a week, retrievable anywhere.
- Apprentice: About 5 kg; one person may get a token to take out one item.
- Journeyman: About 20 kg; keeps a copy of any letter or paper put in.
````

===== END PAGE: 09_spells_v3.md | part 2 of 3 =====
