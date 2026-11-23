# spells-p1

SOURCE: 09_spells_v3.md | version=3 | bytes=41726 | sha256=fe16321c60d69f8c | part 1 of 3 | page_bytes=14174

````text
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

````

===== END PAGE: 09_spells_v3.md | part 1 of 3 =====
