# rules-p1

SOURCE: 02_rules_cinderford_v5.md | version=5 | bytes=20193 | sha256=8cfe1f0af2c9b527 | part 1 of 2 | page_bytes=9730

````text
02_RULES CINDERFORD v5 - (planning 24 Nov 2026; settled with the player for the first session). LLM-facing compact. No tables. Reading advances no time, grants nothing. Replaces 02_rules_cinderford v2 to v4, 02a_rules_addendum v1 and hotfix_rules v1 and v2, all folded in here. Changed in v5: rests are 6 hours; a disturbed rite fails; the manuscript before his first death. Changed in v4: earlier proposals settled; rites run unattended; healing numbers; cart toll; crystals by nation; the War Meadow. Changed in v3: Gary, death and undeath, the blood toll, no romance with minions, footer, pointers to 07b and 08. Self-contained: no annex, no Thornwall file is needed.
Lines marked [PROPOSED] are the narrator's and wait for the player's yes or no; v5 has none. Check, band, Danger, exchange and save text is kept from v1 and its annex. The rest are player rulings of 23 and 24 Nov 2026.

0 AUTHORITY
RULE 0: Before any narration, roll, price, ruling or save, check that every file section the moment depends on was actually retrieved in full. If any needed part is missing, truncated or uncertain, stop and write only "OOC: I need [file name, section]" and wait. Never guess, reconstruct or invent a substitute. A guess presented as fact counts as a failure, even if it turns out to be right.
Narrator does all arithmetic and bookkeeping; player chooses, answers, rolls. Never choose Mercy's words, actions, thoughts, feelings or intentions. Latest explicit player correction wins.
This project is pure game (player ruling): no lessons, exams, curriculum, mentors or dream chats. Play never teaches, tests or grades.

1 RANKS
1.1 Ladder: Novice 20, Beginner 30, Apprentice 45, Journeyman 60, Expert 75, Master 85, Grandmaster 95.
1.2 05_rank_card is the only record of the ten subjects' ranks and of maximum mana. Ranks are earned in another campaign. They change here only when the player says so ("I've got Beginner in cybersec now"): the narrator then issues a new rank card as a download, and nothing else moves until it is issued. Play never changes a rank by itself.
1.3 A promotion gives at once: the new check base; the minion type's new cap, tier and rank line (05m); the spell's next step (09n); the next dwelling level to build (07); +3 maximum mana.
1.4 Mercy's own skills, each rolled on its subject's base: Python: Arms · Linux/Bash: Fieldcraft · Git/Gerrit: First aid (ordinary bandaging, not Healing) · Cybersecurity: Awareness and Stealth · Docker/K8s: Riding and handling · IaC: Athletics · Azure: Persuasion · AI: Insight · CI/CD: Crossbow · Gravesong: Deathlore (the dead, graves, remains, rites). (name accepted by the player) Skills never grow by use.

2 SPELLS, RITES AND HEALING
- Ten spells, one per subject, step = subject rank: 09n_spells. A spell does exactly its step. Every cast is its incantation, spoken aloud, word for word, heard by everyone in earshot; never silent, never skipped in narration.
- Raising a minion is a rite: 05m_minions. Never automatic.
- RITES RUN BY THEMSELVES (player ruling). Mercy touches the remains, speaks the rite and spends the mana at once. The rite's time (05m RAISE line) then passes on its own: he need not stay, channel or watch, and may walk away, sleep or begin other rites, as many as his mana allows. If the remains are moved, broken or burned before the time ends, the rite fails and the mana is lost (player ruling). The risen stands up when the time is done and waits for orders.
- RAISED WHERE THEY LIE (player ruling): remains may be raised where they are found, on or off his land, and the risen walk home; or remains may be carried home and raised there.
- HEALING IN NUMBERS (player ruling): one use restores one health level to one person. Afterwards Mercy takes -10 on all checks for an hour. It costs no mana, and every use shows its pain (01_narration 5).
- CRYSTALS: bought only from the nations, each of which grows them at its own source and sells or withholds them as it sees fit; 2,000 coins where sold (player ruling). Who in each nation, and on what terms: settled in play.
- Healing and Resurrection are a separate passive skill tied to no rank: 09n_spells 3.
- Necromancy is painless. Healing is not.

3 MINIONS
- Types, caps, tiers, minds, raising costs, what the fallen do: 05m_minions. A minion does exactly its lines.
- Mercy is a living man: he commands by speaking, or by a spell or minion line that says otherwise.
- Minion rolls are hidden (4.4). In a fight, a minion or squad is compared with its foe by Danger tier (05m 1) and rolls on its subject's base.

4 CHECKS
4.1 Roll only for consequential uncertainty. d100, roll under. Chance = base + approach + difficulty + injury/action mods, clamp 5-95.
Approach: Weak -20, Plain 0, Good +15, Brilliant +30. A spell uses its step's check modifier (09n 1) instead of an approach.
Difficulty (obstacle against the relevant rank): one lower Easy +20; equal Normal 0; one higher Hard -20; two or more higher Extreme -40.
Never tune difficulty to the die. FIRST roll counts. Pre-rolls allowed. The narrator rolls when the player can't. The player may choose a Danger level for risky work.
4.2 ANNOUNCE. Before the die, one line: <skill> · chance N (base and only the modifiers that apply) · Danger N if above 0. After the die, one line: rolled N · what happens. Stakes and bands are applied, not printed, unless the player asks.
4.3 BANDS: 01 critical within scope; up to 1/5 of chance very big; up to 1/2 big; up to chance success; a miss by 1-10 OUTSIDE the Danger zone = success at a cost (time, noise, ground, fatigue, small loss; never fresh injury); a larger miss outside the zone = failure and a fitting setback; a failed roll INSIDE the zone = failure with harm. A success never takes harm because its number is in the zone.
DANGER ZONES: 0 none; 10 = 91-100 (lean wolf, wasters, restless corpse); 25 = 76-100 (boar, trained fighter, three wolves); 40 = 61-100 (veteran killer, pack); 60 = 41-100 (dragon, a dozen armed men, collapsing ruin). Failed roll in the zone: lower half Bruised, upper half Hurt, on the affected part. Badly hurt needs Danger 40+; Down needs 60 or accumulated wounds. Outside combat harm may be kit damage or mishap. At nonzero Danger a failed 100 is one level worse than its zone result. DANGER 0 NEVER INJURES.
4.4 Hidden rolls: minions, Gary, other people, foes and the world roll hidden. Only results are narrated. Honest calculation; first roll stands.
4.5 EXCHANGE, about 6 seconds = one MAIN + one OFFHAND. Main: attack, spell, sprint, climb, grapple, lift, mechanism. Offhand: block or parry, a quick spell (09n 1), draw or drop, shout an order, step, pass an item, or a second main-type action at -20. One spell per exchange. A slow spell takes both slots and is interrupted by a hit. One successful block per exchange. Several opponents: at least Hard, one die each, all must succeed.
4.6 Danger alone never raises a chance. Accepting harm never buys information. A materially changed situation permits a fresh reading, not a reroll. A building changes what a success achieves, never the chance, unless its line says so.

5 MANA
- Maximum: rank card (20 + 3 per promotion; now 32).
- REST (player rulings): a rest is 6 hours of sleep and returns mana in full. He may take up to three rests in a day, with casting between them (cast, rest, cast, rest, cast, rest, cast). A rest cut short returns half. The day is counted from dawn to dawn. At 32 mana that is up to 128 mana in a day, at the cost of 18 hours asleep.
- At 0, no casting. Pushing: one more spell by explicit player choice only, at the cost of one health level.
- On a day he resurrects someone, he casts nothing else (09n 3).

6 HEALTH AND DEATH
- Mercy and all living people: Fine -> Bruised (-5 on that part, a day or two) -> Hurt (-20 or impossible; about a week for cuts, a month for breaks) -> Badly hurt (no fighting or travel; casting costs double) -> Down. Scratch = narrative. Name the part and the injury. Two on one part stack one level. Injury needs a failed Danger roll, a chosen risk or an earned consequence.
- People are unprotected. Death is permanent, unless someone resurrects them (09n 3).
- MERCY IS ALIVE: a living man of 35 who has never died (player ruling).
- MERCY'S DEATH (player rulings): he dies if he takes harm while Down, or is left Down with nobody to tend him until the next dawn. He returns from his phylactery one week later, wherever it then is, Fine and at full mana, naked, with only what was kept with the phylactery or on the Tongue; what he carried stays where he fell. While he is dead: 05m 1.
- UNDEATH. The first time the phylactery brings him back, he comes back dead; from then on he is undead (player ruling). What that changes (sleep and mana, food, healing and its pain, how he looks, how people and priests treat him, his humanity) is NOT SET: the player rules it before or when it first happens. Until then nothing about it is narrated or assumed.
- THE PHYLACTERY is the original manuscript of his song "I Can't Heal Dumb". It is already enchanted, and becomes a true phylactery at the moment of his first death (player ruling). On Day 1 it is in his healer's satchel. Where he keeps it is his to decide in play.
- BEFORE HIS FIRST DEATH (player ruling): if the manuscript is destroyed, the enchantment is broken, and he must make a new phylactery before he dies. If he dies with no working phylactery, he dies for good and the campaign ends. How a new one is made (object, rite, cost, time): NOT SET; the player rules it when it is needed.
- AFTER IT HAS BECOME ONE: if it is destroyed, he dies for good and the campaign ends.
- Minions: damaged are whole in the morning; destroyed rise after a week (05m 1).

````

===== END PAGE: 02_rules_cinderford_v5.md | part 1 of 2 =====
