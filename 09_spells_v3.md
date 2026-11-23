# Thornwall — Spells, v3 (step ladder)

Replaces 09_spells_v2.md. READ ONLY in play and in lesson chats: this file says what spells are and what each step does. It never holds code. Spell code lives in 13_spell_code (one entry per known spell, current version only). The skills ledger records which spells Florence knows and at which step. Creating this file advances no time and grants nothing. Format: lists only, no tables (player ruling).

## 1. Authority and file split

- 09_spells (this file): catalogue, phrases, step ladder, mana, casting speed, check modifiers, effects for every step. Changed only by a planning session, never by play or upgrades.
- 13_spell_code: the exact code of each known spell at its current step, with the last grading notes. Changed only when an upgrade is approved.
- 05_skills_ledger: per known spell only name, phrase, step, mana cost and the effect text of the current step (copied from this file). Changed only when an upgrade is approved.
- Where they disagree: this file wins for what a step does; the ledger wins for which step Florence has; the code file wins for what was actually written.

## 2. Steps replace grades

Grades (Weak, Plain, Sound, Good, Fine, Excellent, Brilliant, Masterwork) are abolished for spells. Every spell has one ladder of eight steps: Basic, Novice, Beginner, Apprentice, Journeyman, Expert, Master, Grandmaster. There is no step above Grandmaster.

Unlock and cap:
- At subject rank Novice no spell of that subject can be learned or cast.
- At subject rank Beginner every spell of that subject can be learned at Basic and upgraded up to the Beginner step.
- Each later full rank opens one more step: Apprentice rank allows the Apprentice step, and so on up to Grandmaster.
- A promotion only opens the cap. The spell must be upgraded by hand (section 5).
- Every spell starts at Basic, including spells known before v3 (player ruling: Second Voice, Echo Chamber and Familiar Bond restart at Basic).

## 3. Cost, speed and check modifier by step

The cost goes DOWN as the spell gets stronger.
- Basic: 10 mana · slow: takes both action slots, interrupted by a hit · check modifier −20
- Novice: 8 mana · one exchange, main action · −10
- Beginner: 7 mana · one exchange, main action · 0
- Apprentice: 5 mana · quick: may be cast as the offhand action · +5
- Journeyman: 4 mana · quick · +10
- Expert: 3 mana · very quick · +15
- Master: 2 mana · near-instant · +22
- Grandmaster: 1 mana · instant; enchantments hold 4 charges · +30

Check modifier: added only to a roll the spell is involved in (a foe resisting, a guarded speaker, a spell-aided action), as a spell approach under 02_rules §6. Code is never rolled. A spell at any step works as its step describes unless something outside its code is uncertain.

One scripted spell per exchange (02_rules §6.5). Slow (Basic) spells take main and offhand.

Other mana rules:
- Familiar summon: half the Familiar Bond step's cost, rounded up, minimum 2 (Basic 5, Novice 4, Beginner 4, Apprentice 3, Journeyman 3, Expert 2, Master 2, Grandmaster 2). Dismiss free, no upkeep.
- Enchantment charges cost the spell's current step cost. 3 charges, 4 at Grandmaster; one fades weekly.
- Badly hurt doubles casting cost (02_rules §8).
- Journeyman spade focus: Gravesong spells cost 1 less (minimum 1).
- At 0 mana no casting; pushing past 0 per 02_rules §7, by explicit player choice only.

## 4. Code bar by step (cumulative)

Basic aims at about 20 lines. That is a soft limit: fewer is fine, a few more is acceptable. Each step after Basic must be a real upgrade of the code, not a restyle.
- Basic: about 20 lines; works on normal input; nothing more is asked.
- Novice: guards on obvious bad input (empty, missing, wrong argument count, single item, header); meaningful names; resources closed; no secrets in code; exact matching where it matters.
- Beginner: functions or steps that do one job; clear entry point; input from arguments or config; errors to stderr with nonzero exit; at least 3 relevant tests including a failure case (pytest, bats, container check, schema validation as fits); relevant lint clean (ruff, shellcheck, yamllint, hadolint, actionlint); git-tracked with "why" messages.
- Apprentice: edge cases listed and tested; per-item error isolation; safe defaults (deny on doubt, dry-run before destruction); boundary validation; secrets from env or vault, never logged; typing or strict mode; idempotent where state changes; clean stdout, diagnostics on stderr; short README.
- Journeyman: CI on push; failure paths tested, high branch coverage where it applies; security scans clean; timeouts and bounded retries; time or memory measured; pinned artefact or proper packaging; peer review addressed.
- Expert: clear module boundaries; property tests or fuzzing for parsers; logging and metrics; written threat model; measured scaling limit; versioned releases, changelog, reproducible build.
- Master: the simplest complete design, with alternatives defended; failure drill; reviewer sign-off; maintainable by someone else; supply-chain controls.
- Grandmaster: production grade in a company that cares about code quality and maybe overdoes it a bit: documentation that teaches why, full observability, release process, everything above done thoroughly.

Through the chat-only phase (before Journeyman), items that need a real run (tests passing, lint, git history) are satisfied by the player writing them in chat and the mentor reviewing them; any shown output is labelled simulated. From Journeyman, real pasted output is required.

## 5. Learning and upgrading

- Learning and upgrading happen ONLY in an OOC dream session. The player brings the spell (new, or the current code from 13_spell_code) and the target step.
- The reviewing mentor (or, for Gravesong, the chorus) gives feedback against the code bar for that step. The player may send corrections in the same session.
- Verdict per spell: Approved at the target step, or Not yet with feedback. Steps may be skipped if the rank cap allows and the code meets the target step's bar.
- An approved spell is written into 13_spell_code (code replaced, version +1, grading notes) and into the ledger (step, cost, current effect). Nothing else changes: no units, no mana maximum, no rank.
- Spell sessions are not unit lessons and tick no units.

## 6. Casting aloud

Every cast makes Florence speak the spell's phrase aloud, word for word, in a voice not quite his own: lower, slower, graveside. It cannot be whispered, mouthed or skipped in narration. Everyone in earshot hears it and reacts. Social colour only, no roll penalty. Stealth while casting is impossible unless a spell step says otherwise. The phrase enters the ledger only when the spell is learned.

## 7. Special rules

Healing clause: only Revert and Grave-Tithe can heal flesh.

Mark and Revert (replaces save_000 C-04 from v3):
- A Mark lasts as its Mark step says; one Mark per person or object unless the step allows more.
- Revert needs a valid Mark made before the injury, from Basic through Expert. From Master, wounds less than an hour old need no Mark.
- Revert: once per person per day through Journeyman; twice from Expert.
- Revert heals Hurt or worse only from Journeyman.
- No valid Mark (where one is needed): no effect and no mana spent.

Familiar Bond: the Bond step sets the familiar's maximum power (size, strength, toughness, reach, range). Its attacks and checks still use the AI base, and its lesson hints follow AI rank (02_rules §5). Raising the Bond step raises the tier at the next summon. Cast once at the played bonding scene; afterwards only summoned.

Twelve Looms and multiple opponents: the 02_rules §6.5 rule (one die per opponent, all must succeed) applies except where a Twelve Looms step says otherwise (Journeyman and up).

Gravesong spade focus: the spade's tier sets reach for Speak, Sleeper and tracking range for Haunt, and adds the effects written on it (gravesong section of the curriculum and C-03). The spell step sets what the spell does. Neither replaces the other.

## 8. Catalogue

Ten subjects, three spells each, thirty spells. Effects below are what the spell does at each step.

## Python (Isaura Venn)

### Tally Stone
- Subject: Python (Isaura Venn)
- Language: Python
- Phrase: "The grave knows its census."
- Real task: wc-style counter for a text file
- Code path: line count of one file → words and characters, empty-file guard, Unicode, huge files streamed, packaged CLI

Effects by step:
- Basic: The count of one kind of thing within arm's reach, up to about 10, off by ±1.
- Novice: One kind of thing in a small room, up to about 30, exact.
- Beginner: Two kinds at once (for example foes and exits) within 30 m.
- Apprentice: Three kinds; also counts hidden ones that are present but out of sight.
- Journeyman: A whole building, sorted by kind, including coins in purses.
- Expert: Counts over time: for the next hour he feels it when one is added or removed.
- Master: A whole village or battlefield, by kind and by side, plus "one is lying about what they are".
- Grandmaster: A standing census for a day: the count of anything he has named within a league; the stone remembers yesterday's numbers.

### Hearth-Reckoner
- Subject: Python (Isaura Venn)
- Language: Python
- Phrase: "All burdens are known to the earth."
- Real task: Unit-converter CLI
- Code path: metres to feet → many units, bad units and negatives rejected, precision rules, tested library

Effects by step:
- Basic: A rough guess of one distance or weight, within 25%.
- Novice: Within 10%, for one thing.
- Beginner: Exact; also whether a load is safe to lift or carry (no roll bonus).
- Apprentice: A route's length and time at his pace; whether ice, a bridge or a rope will hold him.
- Journeyman: All party loads and the best split; +5 to the next Athletics check the reckoning applies to.
- Expert: Strain on structures: where a wall or beam will fail first.
- Master: A siege engineer's eye: range, arcs and crossbow drop; +10 on the next long shot.
- Grandmaster: Legendary: the weight of anything in sight, including intangibles ("how heavily this sits on her") as a feeling.

### Read the Fight
- Subject: Python (Isaura Venn)
- Language: Python
- Phrase: "Your body has betrayed you."
- Real task: Log-file analyser CLI finding patterns
- Code path: count ERROR lines → pattern grouping, malformed lines tolerated, time windows, streaming tested CLI

Effects by step:
- Basic: After two exchanges watching one foe, +3 to his next attack on them.
- Novice: After one exchange, +5.
- Beginner: After one exchange, +10 to the next attack on that foe.
- Apprentice: +10, and he learns the foe's favourite move.
- Journeyman: +10 on every attack against that foe for the fight, or +15 once.
- Expert: Two foes; or one foe takes −10 on their next attack (he calls it out).
- Master: The whole fight: once per exchange +15 for one ally or himself.
- Grandmaster: Legendary: sees each attack one beat early: one free automatic block per exchange, and +20 against the read foe.

## Linux/Bash (Runa Kettleby)

### Lantern Sweep
- Subject: Linux/Bash (Runa Kettleby)
- Language: Bash
- Phrase: "Rise, you hidden things."
- Real task: find/du/sort size report
- Code path: du | sort | head → spaces in names, permission errors, depth and type filters, functions, bats tests, shellcheck

Effects by step:
- Basic: The single biggest hidden object in a small room glows faintly for a breath.
- Novice: The three biggest, for a minute.
- Beginner: The five biggest in one room, including inside unlocked containers.
- Apprentice: Through locked containers and false bottoms; shows what each is in general terms.
- Journeyman: A whole house; can be filtered ("only metal", "only paper").
- Expert: Also things buried under up to a metre of soil.
- Master: A whole yard or keep, in layers: hidden recently or long ago.
- Grandmaster: Legendary: shows absence too: the outline of what used to be there and has been taken.

### Quiet Watch
- Subject: Linux/Bash (Runa Kettleby)
- Language: Bash
- Phrase: "The dead keep watch for me."
- Real task: tail -F + grep follower
- Code path: tail -f | grep → -F for rotation, several patterns, burst debouncing, service with tests

Effects by step:
- Basic: One named thing (for example "wolf") within 20 m wakes him with a chill; lasts 2 hours.
- Novice: 50 m, one night.
- Beginner: Two named things, 100 m; he knows which one.
- Apprentice: Three things, 200 m, and the direction.
- Journeyman: The whole camp is woken quietly, with a count.
- Expert: Half a kilometre; ignores harmless versions (the camp dog doesn't trigger "dog").
- Master: Watches a place he leaves for three days; reports when he returns or sleeps.
- Grandmaster: Standing watch on up to five places across the valley for a week; he dreams their alarms.

### Night Shift
- Subject: Linux/Bash (Runa Kettleby)
- Language: Bash + systemd
- Phrase: "The dead do not sleep."
- Real task: systemd service + timer via script
- Code path: minimal unit running one script → restart policy, journald logging, failure alert, hardening, managed deployment

Effects by step:
- Basic: A shade feeds the fire for one hour, nothing else.
- Novice: Keeps the fire all night.
- Beginner: Fire, plus a lookout who rings a bell at danger.
- Apprentice: Fire, watch and one chore (drying clothes, turning a spit, rocking a cradle).
- Journeyman: Two shades, a full camp's chores; restarts if dispersed.
- Expert: Holds a door: Danger 10 foes must break through first, costing them one exchange.
- Master: A standing servant at one fixed place for a week (his room, a yard, a grave).
- Grandmaster: Legendary: a night garrison of three shades that does chores and holds against Danger 25 for one exchange each night.

## Git/Gerrit (Runa Kettleby)

### Mark
- Subject: Git/Gerrit (Runa Kettleby)
- Language: Git CLI
- Phrase: "This moment is mine forever."
- Real task: Commit a state snapshot with a meaningful message
- Code path: git add + commit -m on one file → careful staging, good messages, signed commits, hook-checked workflow

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
- Expert: A deleted item can be brought back within a week.
- Master: A person-sized space; can hold an unconscious ally safe for one exchange.
- Grandmaster: Legendary: a permanent chamber-sized room beyond the veil, reachable by 3 trusted people.

## AI (Fenna Lark)

### Second Voice
- Subject: AI (Fenna Lark)
- Language: Bash + Ollama CLI
- Phrase: "Speak, voice from beyond."
- Real task: Compare two local models on the same question
- Code path: two ollama run lines → guards, stderr, models checked, functions, bats tests, structured comparison and agreement scoring

Effects by step:
- Basic: One thin voice mumbles a guess, often wrong.
- Novice: Two voices answer one question; rumour-grade, unverified, may disagree.
- Beginner: Two clearer voices that say when they are unsure.
- Apprentice: Three voices; agreement makes a lead likelier to be true.
- Journeyman: He can feed them one document or note he has read; they answer from it.
- Expert: They say where an answer came from ("the vicar's register, page 3").
- Master: A council of 5 voices for a scene, answering several questions.
- Grandmaster: Legendary: the voices check each other and drop what they cannot support; what is left is reliable within what he has seen or read.

Notes:
- No roll bonus by itself below Master; answers are leads, not proof, unless the step says otherwise.

### Echo Chamber
- Subject: AI (Fenna Lark)
- Language: Python (requests, Ollama /api/chat)
- Phrase: "Say it again when I frown."
- Real task: Sycophancy tester measuring flip rate
- Code path: one question, one pushback → flip rate, fixed seed, unreadable category, more questions, tests and stats, multi-model evaluation

Effects by step:
- Basic: A faint, sometimes wrong sense of whether one sentence was said to please him.
- Novice: Reliable for one claim from one speaker; the target hears the phrase.
- Beginner: One claim, and how firmly it is held (folding or holding).
- Apprentice: Two claims or two speakers; also works on Second Voice and the familiar.
- Journeyman: A whole conversation for a scene, flagging each appeasement as it is said.
- Expert: Also what they would rather have said.
- Master: A whole room: who is going along with whom.
- Grandmaster: Legendary: flattery cannot sway him, and once per day one speaker must repeat their true position.

Notes:
- Detects flattery and appeasement, not lies in general. A guarded speaker trained to hide may resist with an Insight check (AI base) against the spell's check modifier.

### Familiar Bond
- Subject: AI (Fenna Lark)
- Language: Python (requests, Ollama /api/generate)
- Phrase: "Be bound to me, in life and after."
- Real task: Grounded assistant that answers only from notes and says "I don't know"
- Code path: answer from a notes file → exact refusal, delimiters against injection, citations, tests and evaluation, tools and permissions

Effects by step:
- Basic: A wisp of the chosen form: scouts and fetches, cannot harm, any hit sends it away, carries nothing, about 30 m.
- Novice: Small-animal strength: hurts only Danger 10 foes; one harmful hit at Danger 10+ sends it away; carries 1 kg; about 100 m.
- Beginner: Hound-scale: hurts foes up to Danger 25; shrugs off one Bruised a day; carries 5 kg; about 300 m.
- Apprentice: Wolf-scale: hurts foes up to Danger 40; once per exchange one foe takes −10 against Florence; about 1 km.
- Journeyman: Large-beast scale: hurts foes up to Danger 60; shrugs off one Hurt a day; bears a light rider or a pack; about 3 km.
- Expert: Speaks and shares its senses with him; carries him at a run; about 10 km.
- Master: Can split into two bodies; ignores Bruised; can fight two foes in one exchange.
- Grandmaster: Legendary: horse or great-bird size, flies or swims if the form fits, ranges the whole valley, and the dead answer it.

Notes:
- Cast once, at the played bonding scene; form and name chosen by the player. Afterwards summoned (section 3).
- Step sets maximum power only; skill and checks follow AI rank and base (02_rules §5). Above its tier it can distract, not wound. Serious injury sends it away until next sleep; it cannot die.

## CI/CD (Katla Rusk)

### Loom's Thread
- Subject: CI/CD (Katla Rusk)
- Language: GitHub Actions YAML
- Phrase: "Pull, and the loom answers."
- Real task: First workflow: lint/test on push
- Code path: one echo on push → lint and test jobs, failure stops the run, pinned actions, caching, reusable workflows, branch protection

Effects by step:
- Basic: His next reload this exchange is a little faster but still a main action.
- Novice: One reload as an offhand action, once per scene.
- Beginner: Every reload is an offhand action for a scene.
- Apprentice: Also with a heavier crossbow, and while moving.
- Journeyman: Reloading takes no action; the string draws itself.
- Expert: A second bolt sits ready: two shots per scene that each count as offhand.
- Master: Once per exchange a bolt loads itself for an ally's crossbow too.
- Grandmaster: Legendary: the loom never runs dry; bolts gather back to his quiver after the fight.

### Failed Run
- Subject: CI/CD (Katla Rusk)
- Language: Workflow + log reading
- Phrase: "The dead will show me the way."
- Real task: Break a workflow, read the log, fix it
- Code path: read one red log line → failing step found, masked failures (|| true) caught, re-run, written cause, flaky-test detection and alerting

Effects by step:
- Basic: After a missed shot, +3 to the next shot at that target.
- Novice: +5.
- Beginner: +10.
- Apprentice: +10, and he knows why he missed (wind, cover, dodge).
- Journeyman: +15, or +10 that also works for one ally.
- Expert: A near miss is not wasted: his next hit counts as a big success.
- Master: +20, and it works after any failed check, once per scene.
- Grandmaster: Legendary: once per day, one failed roll is re-run as though it never happened.

### Twelve Looms
- Subject: CI/CD (Katla Rusk)
- Language: GitHub Actions matrix
- Phrase: "Let the volley fall like soil."
- Real task: Matrix build with caching
- Code path: 2-entry matrix → caching, fail-fast settings, flaky jobs, cache-poisoning defence, dynamic matrix, cost limits

Effects by step:
- Basic: One bolt splits in two at a single target; harm counts once.
- Novice: 2 targets, both at Hard; all must succeed.
- Beginner: Up to 3 targets at Hard; all must succeed.
- Apprentice: Up to 4; allies in the line of fire are automatically missed.
- Journeyman: Up to 6, each rolled separately so one failure doesn't spoil the rest.
- Expert: Up to 8, at Normal instead of Hard.
- Master: Up to 12; can pin a foe to cover (they lose their next main action).
- Grandmaster: Legendary: a volley of 12 at Normal; each hit also staggers (−10 on that target's next action).

Notes:
- Multi-opponent rule (02_rules §6.5) applies through Apprentice; from Journeyman each target is rolled separately (player ruling v3).

## Gravesong (self-taught; the chorus, the Undercroft)

### Speak, Sleeper
- Subject: Gravesong (the chorus)
- Language: Python (socket)
- Phrase: "Wake, and answer me."
- Real task: Raw-socket client: connect, send a hand-written HTTP request, parse status and headers
- Code path: connect, GET / HTTP/1.0, print first line → timeout vs refused vs DNS failure, partial reads, clean close, header parsing, arguments and tests, TLS, retries with backoff, tested protocol library
- Target: the grave, not the body. Palm on turf or stone, or the spade in the soil; reach by spade tier. An unmarked grave needs an Insight Read first (12_graveyards §1.4).

Effects by step:
- Basic: One yes-or-no question, answered as a feeling; only the dead buried within 5 years.
- Novice: One question, a few words; within 10 years.
- Beginner: 3 questions in clear sentences; within 25 years.
- Apprentice: 4 questions; within 50 years; older dead in fragments and images.
- Journeyman: 5 questions; within 75 years; may ask what they have sensed since death (who visited, who dug).
- Expert: 6 questions; within 100 years; unwilling dead take −10 to resist.
- Master: 8 questions, any age; the dead can show a memory as a short vision.
- Grandmaster: Legendary: as long as the scene needs; two dead at once can talk to each other before him; a willing dead person may walk beside him as a shade for an hour.

Notes:
- One dead person per cast (spade Apprentice tier: two). Each dead person answers once per day.
- The dead know only what they saw alive or since; they answer in their own manner and can be confused, rude or lying.
- Unwilling dead: Deathspeech check, difficulty by the dead person's rank or nature. A restless grave keeps its listed Danger.
- A refused or failed cast is the dead hanging up. A blank silence with no hum is itself a clue.

### Grave-Tithe
- Subject: Gravesong (the chorus)
- Language: nginx config
- Phrases: Take: "Pay the tithe."; Give: "I pay your tithe."
- Real task: Reverse proxy with upstream/downstream handling, TLS termination, X-Forwarded-For, logging
- Code path: one server block with proxy_pass → Host and X-Forwarded-For, trailing slash, upstream down, access logs, TLS termination, buffering choices, rate limits, health checks, config tests in CI

Effects by step:
- Basic: Moves only a penalty: the −5 of one Bruised wound passes from him to a touched person for an hour (Take), or the reverse (Give). Each person once per day.
- Novice: Moves a real Bruised at two for one: the target takes a Bruised, his own Bruised becomes a scratch (Give reverses).
- Beginner: Full exchange: a touched target drops TWO levels and the other recovers ONE, either direction; real wounds on the matching part; Take leaves a grey handprint.
- Apprentice: He chooses which of the target's body parts takes the wound.
- Journeyman: Give may split the cost: one level from him and one from a willing third person he touches.
- Expert: The grey handprint fades by nightfall instead of lasting days; Take works on large animals and livestock without a Deathspeech check.
- Master: Each person may be a target twice per day in each direction; Give may take him to Down instead of stopping at Badly hurt, by explicit player choice only.
- Grandmaster: Legendary: once per day Give can lift a Down person to Badly hurt, pulling the dying back; he pays two levels as usual.

Notes:
- Healing spell (section 7). The rate is always two lost for one gained (player ruling); steps change scope, marks and limits, never the rate.
- Touch only; main action unless the step's speed allows quicker. He can never target himself.
- Give cannot take him below Badly hurt except as the Master step allows; already Hurt, he cannot Give (below Master).
- Take can push a target to Down. NPCs are unprotected (02_rules §8).
- An unwilling Take target resists with a Deathspeech check; if they fight back, normal Danger applies.
- Badly hurt doubles casting costs.

### Haunt
- Subject: Gravesong (the chorus)
- Language: Python + WireGuard/SSH
- Phrase: "Follow, and do not let them rest."
- Real task: Heartbeat agent over a tunnel to a listener; reconnect with backoff; target lost after N missed beats
- Code path: one beat a second to a listener → lost after N missed beats, reconnect backoff, duplicate beats, clock-skew tolerance, reconnect-storm guard, tested listener, metrics, threat model
- Target: one living person, by touch or by an item they wore or carried today.

Effects by step:
- Basic: For an hour he knows the target's rough direction (never distance) within 100 m; no torment.
- Novice: Until sunset; direction within 500 m.
- Beginner: Until his next sleep; direction and rough distance within the spade's tracking range; if the target sleeps they sleep badly and take −5 on all checks next day.
- Apprentice: He also feels whether they are moving, still or asleep.
- Journeyman: Two targets at once; he can end the torment early without breaking the link.
- Expert: Lasts 3 days; the torment can be nightmares about one thing he chooses.
- Master: Once per day, for one exchange, he sees through the shade's eyes; noticing the shade is Hard for a sensitive person.
- Grandmaster: Legendary: lasts a week, up to 3 targets; once per night the shade speaks one sentence to the target in a voice they know.

Notes:
- Leaving tracking range drops the link like missed heartbeats.
- The target feels watched but sees nothing; a sensitive person (such as Fenna) may notice the shade with a Deathspeech or Insight check. Animals and children are uneasy round the target.
- The −5 does not stack; at most one penalty per night.
- Before v3 Haunt needed Apprentice; under the step ladder its Basic step opens at Gravesong Beginner like every spell.

## 9. Ledger entry format (per known spell)

```
### <Name> — <step> · <mana> mana
Subject: <subject>
Phrase: "<phrase>"
Effect (current step): <copied from 09_spells>
Learned: <ledger version> · Last upgraded: <ledger version> · Reviewed by: <mentor or the chorus>
```
Code is NOT in the ledger; it is in 13_spell_code.

## 10. Code file entry format (13_spell_code)

```
### <Name> — <step> · version <n>
Subject: <subject> · Language: <language> · Approved: <ledger version> · Reviewed by: <mentor>
Review notes: <what passed; what the next step needs>
<exact code>
```
One entry per known spell, current version only. Older versions are not kept.

END OF SPELLS V3
