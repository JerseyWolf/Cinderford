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

12 SAVE SYSTEM
INHERITED from Thornwall 12 (status + immutable saves, numbering by checkpoint not day, style and retention, templates, checklist, retrieval and merge), with these changes:
- Templates: "awake/asleep" becomes "bright/flickering/low/guttering/embers".
- VITALS: health level, mana/max, act/sense/road range, coin held for the fire, dim clock if running.
- Add: SITE (buildings, under construction, resources), SETTLERS (current roster and who is away).
- Drop: GRAVES+, salt, Parson feed, contracts, orders, guild/pool.
- 12.4 abbreviations: new list for Cinderford, written with 06_settlers.

FOOTER (Q36 a): Dn · weekday date 753 · time · mana now/max · act/sense m

ANNEX A - VERBATIM FROM 02_RULES_THORNWALL v7 (sections 6.1, 6.2, 6.3, 6.5, 8, 12). Thornwall-only items inside it (announce format, armour, crossbow, graves, salt, Parson feed, guild, abbreviations, startup list) do not apply; Cinderford sections 5.2, 8 and 12 replace them.
6.1 Roll only for consequential uncertainty outside code. Chance = base + approach + difficulty + injury/action mods, clamp 5-95.
Physical approach: Weak -20, Plain 0, Good +15, Brilliant +30. A spell uses its step's check modifier per 09_spells instead of a physical approach (physical Good +15 is not a spell value).
Difficulty (obstacle vs relevant full rank): one lower Easy +20; equal Normal 0; one higher Hard -20; two+ higher Extreme -40.
Announce BEFORE the d100: <Check>: <skill/base> · <approach> · <difficulty/reason> · <mods> -> <chance>; <stakes>; <bands>; Danger <n>. Never tune difficulty to the die. Bare number answers the pending check.
Pre-rolls ALLOWED (speed). FIRST roll counts. Blind rolls: calculate honestly after; result stands. Narrator rolls when the player can't. Player may choose a Danger level for risky work.
6.2 Bands: 01 critical within scope; <=1/5 chance very big; <=1/2 big; <=chance success; miss 1-10 OUTSIDE Danger zone = success at a cost (time, noise, ground, fatigue, small loss; never fresh injury); larger miss outside zone = failure + fitting setback; failed roll INSIDE zone = failure w harm. A success never takes harm because its number is in the zone.
6.3 Danger zones: 0 none; 10 = 91-100 (lean wolf, wasters, restless corpse); 25 = 76-100 (boar, trained fighter, three wolves, flooded stairwell); 40 = 61-100 (veteran killer, pack, keep guardian); 60 = 41-100 (dragon, a dozen armed men, collapsing ruin). Failed roll in zone: lower half Bruised, upper half Hurt on the affected part. Badly hurt needs Danger 40+; Down needs 60 or accumulated wounds. Outside combat harm may be kit damage or mishap.
100 exception: at NONZERO Danger a failed 100 is one level worse than its zone result, THEN armour reduces. DANGER 0 NEVER INJURES. No trading damage for injury; no trading injury for information (a riskier approach = a fresh check).
6.5 Exchange ~6 s = one MAIN + one OFFHAND. Main: attack, scripted spell, sprint/climb/grapple/lift/mechanism. Offhand: block or parry, a spell whose step 09_spells allows as offhand, quick draw/drop, shout, step, lever, potion, pass item, or second main-type at -20 where allowed. One scripted spell per exchange. A spell 09_spells marks slow takes both slots and is interrupted by a hit. One successful block per exchange. Loom's Thread makes crossbow reload offhand. Multiple opponents: at least Hard, one die each, all must succeed.
8 HEALTH
Fine -> Bruised (-5 that part, a day or two) -> Hurt (-20 or impossible; no sparring; ~a week cuts, a month breaks) -> Badly hurt (no fighting/travel; casting double) -> Down (retrieval and recovery). Scratch = narrative. Name part and injury. Two on one part stack one level. Injury needs a failed Danger roll, chosen risk or earned consequence. Scheduled care assumed; clearance required to fight. F can't permanently die or be expelled; retrieval set before unrecoverable danger. NPCs unprotected.
12 SAVE SYSTEM (compact; LLM-facing)
12.0 FILES AND NUMBERING
ONE status_NNN.md=current/pending snapshot replacing older status. Immutable save_NNN.md=lasting events since preceding checkpoint.14_history=merged older events;14_history_addendum=recovered legacy until next merge. Domain bases remain authoritative, ledger alone for progression. No current fact depends on older status.
N is checkpoint sequence, NOT day arithmetic:001 beganD26,007 endsD33. Increment once on new played sleep/OOC checkpoint; save+status share N. Retry/repair no increment, no duplicate fee. Index not edited at routine saves. Player-authorized16 Nov2026 rewrite001-007 is one-time exception; future saves append-only.
12.1 STYLE AND RETENTION
CAPS tags, no tables/bold/decorative headings. One fact/line; clear abbreviations12.4, not cryptic compression. Exact meaningful clue/promise/joke wording with speaker/context. Protect ALL jokes, firsts, disclosures/recipients, habits, consequential outings/jobs, relationship milestones, promises/effects; intimacy short FACT only, never replay.
Drop redundant recaps, inconsequential routine detail/rolls, expired unaccepted cards, cleared health bookkeeping. Accepted incidental spending may remain unitemized; never invent purchase to balance arithmetic. Unknown dates/knowledge stay uncertain. Size target never licenses protected-data loss.
12.2 STATUS TEMPLATE
STATUS NNN | follows status_NNN-1 | actual day/date/time | place | awake/asleep
RULE0: verbatim above.
RESUME: exact pause/present/first pending, no replay. For a played sleep this is the wake-up point the save declares.
VITALS: current health/restrictions,mana/ledger max,coins,salt,sleep;guild/pool from ledger. No former values alongside replacements.
WEATHER: current/forecast.
NEXT: actual deadlines/duties/appointments; separate choices/projects. No invented chores.
RULINGS+: operative new rulings not integrated into bases; replace superseded wording. Integrate only at authorized maintenance.
GEAR: current ownership/location/custody/loans/gifts(giver+occasion)/outstanding orders, no transaction narrative.
HOME: current condition/projects/permissions.
MONEY: balances/debts/terms,last routine-fee checkpoint,genuine unresolved accounting only.
CONTRACTS: open work/receivables/returns; completed job gone except continuing obligation.
ORDERS: operative giver/scope, no breach history.
PEOPLE: current standing/relationship,last established contact,knowledge boundaries/open promises,short historical pointers. No dialogue timeline or neutral resets. New identity/appearance/first meeting lives in originating save until merged into cast.
THREADS: F current knowledge/inference,evidence+holder,restriction/next step,source for historical exact wording. Separate observation/rumour/inference/GM truth.
GRAVES+: current counts/permissions against12; exact known total and completed/remaining subset. IDs label existing members, never add graves. No approximate halves or blanket completion. Estimated salt arithmetic reconciled.
MEMORY SOURCES: short unmerged-save interval/topic map and references for active people/threads, not accumulating event catalogue. Current fact explicit; pointer explains provenance. No COLOUR14 archive.
END OF PUBLIC
GM: current clocks/scheduled events/private live facts/knowledge boundaries. No layers of old updates/resolved scene scripts. Base secrets require retrieval; unsupported "unset" doesn't erase established secret. Explicit player retcons distinguished from draft errors.
END OF GM
12.3 SAVE TEMPLATE
SAVE NNN | follows save_NNN-1 | actual start/end day/date | pause/sleep (+ wake-up point if slept)
RULE0: verbatim above.
BRIEF: short orientation, no second event transcript.
EVENTS: topic lines:what happened/result/persistent evidence/exact work counts;material clue wording once.
PEOPLE: firsts/disclosures/recipients/new identities/relationship changes/promises/habits/intimacy factual. No evergreen state copied unchanged.
JOKES: every protected gag with speaker/setup/punchline; avoid needless quotation duplicates elsewhere.
DELTA: opening->closing coins/all changes(incl accepted unitemized incidentals),routine-fee checkpoint,items/custody/salt/health/contracts. Reconcile arithmetic.
RULINGS: new player rulings, not invented promotions.
END OF PUBLIC
GM: interval hidden consequences/clock moves, not full private-world copy.
END
Named detail tags allowed; references must match actual filename/tag/topic. Preserve unique historical detail removed from status; never depend on discarded status. Usually<=15000 UTF-8 bytes: review threshold, not deletion limit. Split only with explicit approval and checkpoint mapping.
HEADER CHECK: the first line of every save/status is exactly its template header above; "follows" names the previous checkpoint of the same kind. Saves 000-017 keep their old headers (no rewrite).
12.4 ABBREVIATIONS
F Florence; Fn Fenna (+Ash); G Gary; H Harrow; Hd Hedda; Tm Tamsin; Rn Runa; Kt Katla; Cl Calla; Zf Zofia; Is Isaura; W Old Wim; Tl Tull; Md Maud; Br Bram; M Marrow; Dc Corwen Dace; D# day; -> caused; ~ open; w with; GM gm-only. Add new ones here first.
12.5 SAVE CHECKLIST
1 Retrieve full needed source sections; missing/truncated means Rule0.
2 Preserve new events/protected facts once in new save; actual dates, checkpoint not day number.
3 Rebuild snapshot, REPLACE earlier facts. Never append dated update layers or retain superseded positive/negative knowledge lists.
4 Verify coins/salt/debts/custody/grave counts/clocks/sleep/fee idempotency; ledger for its domain. Duplicated state must agree, prefer one location+pointer.
5 Verify every removed unique protected fact survives in save/history. Pre-period/undated material never falsely assigned current day; preserve uncertainty.
6 Validate references/names/firsts/recipients/GM-public separation. No private fields in footer/commentary.
7 Verify files exist/nonempty and measure sizes. Delete old status only when replacement complete; retain all unmerged saves.
12.6 RETRIEVAL AND MERGE
Startup per 00_index (README, index, entire current status incl GM, newest save in full, phone slots, narration/rules/latest ledger; 01b_intimacy before intimate beats). Then fully retrieve scene-relevant cast/history/save/base sections BEFORE reliance. Filename/summary/pointer is not retrieval. Check relevant firsts,last encounter,disclosures,habits before NPC speech; older history is targeted, not automatically all loaded. Already-present full source text needn't be reread unnecessarily.
Merge only on player request per consolidation_rules: fold history/protected detail/legacy addendum into new history,stable facts into bases,current-only status regenerated. Update references to surviving destinations before retiring sources. A repair never becomes play.
END OF ANNEX A

END OF RULES CINDERFORD v1
