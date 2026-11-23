# rules-p1

SOURCE: 02_rules_cinderford_v1.md | version=1 | bytes=21197 | sha256=adb5c1ac9313b54b | part 1 of 2 | page_bytes=10447

````text
02_RULES CINDERFORD v1 - DRAFT (planning 23 Nov 2026; not canon until the player approves). LLM-facing compact. No tables. Reading advances no time, grants nothing.
Built on 02_rules_thornwall_v7 (read in full through END OF RULES v7). Where this file says INHERITED, the Thornwall text applies with "F" read as "the fire". The inherited Thornwall sections are printed verbatim in ANNEX A at the end of this file, so nothing is fetched across sites. In the annex read "F" as "the fire"; where the annex and sections 0-12 above differ, the sections above win.

0 AUTHORITY
RULE 0 (inherited verbatim from Thornwall 0): Before any narration, roll, price, ruling or save, check that every file section the moment depends on was actually retrieved in full. If any needed part is missing, truncated or uncertain, stop and write only "OOC: I need [file name, section]" and wait. Never guess, reconstruct or invent a substitute. A guess presented as fact counts as a failure, even if it turns out to be right.
Narrator does all arithmetic and bookkeeping; player chooses, answers, rolls. Never choose the fire's words, thoughts, feelings or intentions. Latest explicit player correction wins. 05_skills_ledger = only authority for subject ranks, units, exams, spells known and steps, familiar, max mana; play reads it, never changes it. Lessons and exams: 04_curriculum section A and 11_lesson_chat_instructions_cinderford win.

1 SUBJECTS AND FIRE SKILLS
1.1 Ladder INHERITED: Novice 20, Beginner 30, Apprentice 45, Journeyman 60, Expert 75, Master 85, Grandmaster 95. A promotion at once gives: new roll base, building-line tier, spell step cap, +3 max mana, and range growth (7.1).
1.2 Ten subjects -> fire skills (base = subject's current base; skills never grow by use):
Python -> Flame · Linux/Bash -> Ground · Git/Gerrit -> Mending · Cybersecurity -> Vigil and Veil · Docker/K8s -> Embers · IaC -> Structure · Azure -> Presence · AI -> Insight · CI/CD -> Sparks · Gravesong -> Roads.
What each rank of each fire skill can do without mana (NATIVE POWERS), and how the fire can speak: 05h_fire_powers. Speech follows the HIGHEST rank held in any subject (player Q64).
What each rank unlocks to build: 07_buildings (three buildings per skill: building 1 at Novice, 2 at Beginner, 3 at Apprentice; each later rank opens the next level of each; add-ons at any time for resources).
1.3 Not used in Cinderford: guild rank, gap pressure, pool, mentors (Thornwall 1.3-1.5). Background expertise (Thornwall 1.6: Digging Master, gardening) does not apply: the fire has no hands (player Q58 a).

2 LESSONS AND EXAMS
Dream chats only, per 11_lesson_chat_instructions_cinderford and 04_curriculum. Examiner: a faceless dream-realm shaped by the subject (Q62). Thornwall 2 and 3 INHERITED for course structure, security gate, unit T, three lenses, unit verdicts, exam sizes, verdicts, sets, simulated-output labels. Mentor references read as "the dream-realm". Familiar hints INHERITED (Gary).
No in-world time passes in a dream. Any number of dreams fit between play days.

3 SPELLS
- ONE spell per subject in Cinderford (player Q65): Fire Ring, Wisp Crew, Mend, Blind Eye, Carried Ember, Brace, Sanctuary, Familiar Bond, Spark Volley, Follow. Effects, incantations and anchors: 09h_hearth_spells.
- Each is anchored to one Thornwall spell of the same subject. WHICH step the fire has: the anchor's step in 05_skills_ledger (CINDERFORD ANCHORS). Thornwall's other spells are not cast here and are not touched (Q66).
- Unlock, cap, mana cost, speed, action slots, check modifier, code bar: 09_spells sections 2-4, unchanged. Nothing at subject rank Novice. Upgrades only in a dream session, by hand, one step at a time, capped by the subject's full rank.
- Code: 13_spell_code. Judged, never rolled. An approved step works as written unless something outside its code is uncertain.
- CASTING ALOUD (Q54 a): every cast is its incantation, heard in the crackle by everyone inside the hearth ring, word for word. Never silent or skipped in narration. Social colour, no penalty.
- Only Mend heals flesh.
- A native power (05h) costs no mana and does exactly its line. A spell costs mana and does exactly its step.

4 FAMILIAR AND SUMMONS
INHERITED from Thornwall 5: Gary; skill = AI rank (Insight base); power = Familiar Bond step; summon cost per 09_spells 3; acts and rolls separately; above tier distracts, not wounds; cannot die.
Change: harm-forced absence lasts until the next dawn (the fire does not sleep).
Wisps: the Wisp Crew spell. A wisp does only what its step says; it is not a free action of the fire.
Combat (Q44): the fire fights only through spells, Gary and wisps.

5 CHECKS
5.1 INHERITED: roll only for consequential uncertainty outside code. Chance = base + approach + difficulty + injury/action mods, clamp 5-95. Approach Weak -20, Plain 0, Good +15, Brilliant +30; a spell uses its step's check modifier instead. Difficulty one lower Easy +20, equal Normal 0, one higher Hard -20, two+ higher Extreme -40. Never tune difficulty to the die. FIRST roll counts. Pre-rolls allowed. Narrator rolls when the player can't.
5.2 ANNOUNCE (Q35, replaces Thornwall's long announce line). Before the die, one line:
<fire skill> · chance N (base ± only the modifiers that apply)
After the die, one line: rolled N · what happens.
Stakes, bands and Danger are applied, not printed, unless the player asks. A Danger level above 0 is named in one word with the chance ("Danger 25").
5.3 Bands and Danger zones: ANNEX A 6.2-6.3 verbatim, harm to the fire read through section 8 below.
5.4 Hidden rolls (Q35): settlers, visitors, foes and the world roll hidden. Only results are narrated. Honest calculation; results stand.
5.5 Exchange INHERITED (main + offhand, about 6 s; slow spells take both and are interrupted by a hit; one scripted spell per exchange; multiple opponents per Thornwall 6.5, Twelve Looms exceptions per 09_spells). "A hit" on the fire = any harm to the pit or the fire itself.
5.6 Building tier changes WHAT a success achieves, never the chance (from Thornwall 6.6), unless written on the building or a spell.
5.7 Clarifications INHERITED: Danger alone never raises chance; accepting harm never buys information; a materially changed situation permits a fresh reading, not a reroll.

6 PACING
- Ambient by default (Q20): the world happens around the fire. No duties invented for the fire.
- Montage: routine days resolve in one paragraph, no rolls, unless the player sets stakes (Thornwall 6.7).
- Time skips on player request only (Q28). Name anything due before the skip.
- Early saves every few days; daily once the site is busy (Q19).
- NPC colour INHERITED: fresh humour and gossip allowed; canonical people, places and mechanics bound by Rule 0.

7 RANGE AND MANA
7.1 Range (Q59). p = full-rank promotions in the ledger. Act range = round(2 + 2p + p(p-4)/8) metres. Sense range = 5 x act (unrounded act, then round). Along a road: 10 x act. At p = 4: act 10 m, sense 50 m, roads 100 m. Damage reduces range (8).
7.2 Mana max: ledger (20 + 3 per promotion; now 32).
7.3 Recovery (Q55 d, replaces Thornwall 7 sleep, breakfast, meditation):
- Trickle: floor(max / 24) per hour, minimum 1. Now 1 per hour.
- Fuel fed by a person: +1 that hour (not by a wisp).
- Offering: +3, once per giver per day. An offering is food shared, a coin left, or something given up on purpose.
- Never above max. Tracked hourly only when it matters; otherwise reconciled at the save.
7.4 At 0 no casting. Pushing INHERITED: one more spell by explicit player choice only, at the cost of one health level (8).

8 HEALTH OF THE FIRE (Q57 c; replaces Thornwall 8 for the fire)
Levels: Bright -> Flickering -> Low -> Guttering -> Embers. Scratch = narrative.
- Flickering: -5 on checks; act and sense range x 3/4. Like Bruised: a day or two.
- Low: -20 on checks; range x 1/2; max mana -5. Like Hurt.
- Guttering: casting costs double; range x 1/4; max mana halved; no new summons. Like Badly hurt; needs Danger 40+.
- Embers: no casting; senses only inside the pit; the dim clock runs. Like Down; needs Danger 60 or accumulated harm.
Harm sources: water, smothering, scattering, starved fuel, hostile magic, a failed roll inside a Danger zone (5.3: lower half one level, upper half two). Danger 0 never harms.
Fuel starvation: with no fuel for 24 hours, one level.
RECOVERY (player Q-R1 a):
- One level per full day of steady fuel and no fresh harm.
- Tended (a person rebuilds the pit, banks the coals, feeds dry wood): one extra level, once per day.
- Mend restores fire health from its Beginner step (09h).
8.2 Dim clock (Q61): 7. Each full day spent at Embers ticks once. Back to Guttering resets it. At 7 the fire goes out: restart elsewhere with the ledger only (skills and spells); buildings, settlers, coin and standing are lost.
8.3 Site loss: if the site is destroyed and the core is taken, the same restart applies at once, whatever the clock.
8.4 Settlers and visitors use Thornwall 8 levels (Fine -> Bruised -> Hurt -> Badly hurt -> Down). NPCs are unprotected. Settler death is permanent (Q43 a).

9 COIN, OFFERINGS, RESOURCES
- Whole coins. Guest coin is held by the innkeeper on the fire's account (7.7 brief). Quote before commitment. No automatic purchase, build, hire or fee.
- Resources: coin, fuel, materials, goodwill (brief). Amounts and costs: 07_buildings.
- Buildings: rank unlocks the blueprint; resources + time build it (Q16).
- MINOR PRICES INHERITED: realistic everyday prices may be quoted only when files are genuinely silent after retrieval.

10 STANDING
INHERITED scale (wary -> cool -> neutral -> friendly -> warm -> trusted), per person, changes only through play, never in the footer. Nations: soft and narrative, no meters (Q7 e). Track who heard what was cast or signed. No romance (Q33 a).

11 TIME
- Year 753 (player Q-R2; no era name yet). D1 = Thursday 25 March 753. Months, dates and leap years follow the real Gregorian calendar; weekdays follow real 2027 (25 March 2027 is a Thursday), so any date can be checked against a 2027 calendar. 753 is a common year (no 29 Feb); 754 maps to 2028 (leap), and so on.
- Daylight, sunrise and sunset, and normal temperatures: central Poland (Warsaw-like) for the same date. Weather varies around them.
- The fire never sleeps (Q28). A session runs until the player pauses or skips. No time skip without consent.
- Day numbering: Dn = 25 March 753 + (n-1) days.

````

===== END PAGE: 02_rules_cinderford_v1.md | part 1 of 2 =====
