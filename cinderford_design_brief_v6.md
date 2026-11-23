CINDERFORD - DESIGN BRIEF v6 (DRAFT, planning only; nothing here is canon until the player approves it)
Replaces brief v4 (and earlier). Written 23 Nov 2026 in a Thornwall planning chat. Grants nothing, advances no time, changes no ledger.
Format: lists only, no tables.

== 1 SOURCES THIS BRIEF RESTS ON (corrected in v3) ==
Correction: v1 and v2 said the GitBook README, 02_rules, ledger and 09_spells were read through their END lines. They were not: every GitBook fetch in the planning chat came back cut off after one line. 
Actually read, from the player's uploads:
- 05_skills_ledger_v9 (single file; reader returned excerpts; no END line seen)
- 09_spells_v3 (single file; through END OF SPELLS V3)
- 04b_gravesong_curriculum_v1 (parts 1-2, through END lines)
- 02_rules_thornwall_v7 (single file, through END OF RULES v7; read in brief v4)
Verified against 02_rules v7: check formula, clamp, approaches, difficulty, bands and Danger zones (6.1-6.3), mana recovery (7), health levels (8), familiar lockout (5), casting aloud (4). Not read in full: GitBook README (site version numbers unknown), 13_spell_code, 04_curriculum, 11_lesson_chat_instructions, status, saves, any gm/ file.

== 2 LOCKED BY THE PLAYER ==
World and seat
- Name: CINDERFORD. Separate world, separate project, separate GitBook.
- You are a sentient fire in a bare fire pit at a crossroads with a river ford, temperate valley, Polish climate and daylight.
- Origin: old tended fire + made thing; discovered in play.
- Three nations in a triangle; each 2-5 core species on a theme; monster peoples wander; some visitors are monsters, hostile or not.
- Mid magic; code-magic is yours alone. Gods real, act through champions; churches powerful; original pantheon.
- Politics soft and narrative, no visible meters; you barely matter at first. World pressure is GM-only.
People
- Arrivals: d100 arrival roll, scaled by site tier and reputation.
- Settlers: recurring adventurers with flaws and goals; cap by rooms, about 5 deep; they leave on adventures and return with loot, wounds, news. Clever ones can work out what you are. Death is permanent.
- Founder: orc cook from a mixed family, no nation; short temper, sharp tongue; wants one table for all three nations; drawn by a dream. GM writes the rest; player veto.
- No romance. No in-character mentors.
Fire
- Communication grows by tier: signs -> dreams -> voice.
- Never sleeps; time skips on request.
- Carried embers are remote eyes; how well they work depends on rank.
- Combat through the familiar and summons. Night Shift is the wisp line; no new spell.
- Gary the owl crosses over as he is.
- Casting: the phrase is heard in the crackle by everyone nearby. New incantations for this world (section 6).
- Mana: steady trickle plus offerings.
- Range now (4 promotions): act 10 m, sense 50 m. Sense spreads further along roads.
- Damage: five reskinned levels AND shrinking range and maximum mana.
- Failure: dim-day clock; if it fills, or the site is destroyed and the core taken, restart elsewhere with only skills and spells.
Play
- Checks: Thornwall d100 formula, one short line for your roll; other rolls hidden.
- Footer: day, time, mana, range.
- Calendar: year 753 from Thursday 25 March (Q-R2); real Gregorian dates, weekdays as 2027. Saves every few days early, daily later.
- Mostly ambient point of view. Early game: one first-building goal, otherwise slow and empty.
- Economy: guest coin + offerings. Buildings: skill tier unlocks the blueprint; resources + time build it.
Ledger
- A NEW ledger, copied from Thornwall's 05_skills_ledger v9, lives in the Cinderford project and is the authority there.
- Going back: the player hands Thornwall the Cinderford ledger and asks for the ranks and spell steps to be brought up to date.
- Ranks and spell steps travel. Buildings, in-world perks and incantations do not.
- Q63 (b): Gravesong is covered by the v8 spell ruling in both worlds; its three spells are granted at Basic on promotion to Beginner. Written into ledger v10 (patch v1.1).

== 3 TEN SUBJECTS (was nine in v0) ==
Tenth subject added: GRAVESONG = networking and the rest of DevOps the other nine do not cover (web servers and reverse proxies, firewalls and tunnels, observability, SRE practice).
State today, from ledger v9 and 04b_gravesong_curriculum v1:
- Beginner (base 30): Linux/Bash, Git/Gerrit, Docker/K8s, AI.
- Novice (base 20): Python, Cybersecurity, IaC, Azure, CI/CD, Gravesong.
- Gravesong has NO line in ledger v9 yet. Its curriculum gives the line to add: "Gravesong: Novice · base 20 · Novice course 0/12 (04b_gravesong_curriculum v1)". Proposed: add it when the Cinderford copy is made, without an examiner name.
- Examiner in Cinderford (Q62): a faceless dream-realm shaped by the subject, for all ten subjects.
- Gravesong Novice course: 12 units, always open. Its Beginner course needs Cybersecurity Beginner, like the others.
- Promotions so far: 4. Maximum mana: 32. Adding Gravesong at Novice changes neither.
- Possible promotions rise from 54 to 60 (10 subjects x 6).
- Spells known: 12 (11 Basic, Familiar Bond Novice). Novice subjects cast nothing, so 18 of the 30 catalogue spells are locked, including Gravesong's three: Speak, Sleeper; Grave-Tithe; Haunt (granted at Basic when Gravesong reaches Beginner, Q63).
"Misc" = the non-networking half of Gravesong (player, Q58). No eleventh subject.

== 4 TRANSFER LAYER (DRAFT) ==
4.1 One live ledger at a time. The copy starts as Cinderford ledger v10 with a header line "LIVE IN: Cinderford, copied from Thornwall v9 on <date>". Thornwall's v9 is frozen while Cinderford is live. On return, Thornwall's next ledger takes the Cinderford version number + 1.
4.2 What travels: subject ranks and bases, units and exam results, weak points, spell steps, spell code versions, maximum mana, familiar skill and power tier.
4.3 What stays behind in each world: mentors and examiners, guild rank, pool, gap pressure, gear caps, buildings, phrases, effect text, coins, standing.
4.4 Files to copy into Cinderford so dream chats work there: 05 ledger, 04_curriculum, 04b_gravesong_curriculum, 11_lesson_chat_instructions (needs an edit: no mentors, dream-realm shaped by the subject), 09_spells, 13_spell_code.
4.5 Housekeeping found while reading: ledger v9's REFERENCES section still names curriculum v3, lesson instructions v2 and spell code v1, while the site carries v4, v4 and v3. Fix at the copy.
4.6 Ladder and bases unchanged: Novice 20, Beginner 30, Apprentice 45, Journeyman 60, Expert 75, Master 85, Grandmaster 95. Promotion still gives +3 maximum mana.
4.7 Check formula unchanged: chance = base + approach + difficulty + mods, clamp 5-95; bands and Danger zones as 02_rules 6.2-6.3. Shown as:
    <skill> · chance N (base and the modifiers that applied) · rolled N · one-line result
4.8 Spell step costs unchanged: Basic 10 mana, slow, -20. Novice 8, main action, -10. Beginner 7, 0. Familiar summon 4 at Novice.

== 5 FIRE SKILLS (accepted names; Gravesong added) ==
Same subject, same base. Each also names a building line (contents to be written in 07_buildings).
- Python -> FLAME: direct force (shove, strike, burn). Line: the pit itself (stone ring, firebowl, forge-heart).
- Linux/Bash -> GROUND: reading land, weather, tracks inside sense range. Line: camp ground (cleared yard, well, woodstore).
- Git/Gerrit -> MENDING: warmth, easing wounds, repair. Line: sickbed and stillroom.
- Cybersecurity -> VIGIL and VEIL: noticing; hiding what you are. Line: walls, gate, watch post.
- Docker/K8s -> EMBERS: carried embers, vessels, beasts. Line: lanterns, stable, cart shed.
- IaC -> STRUCTURE: lifting, holding, building work. Line: the inn's frame (lean-to, hall, upper floor, rooms).
- Azure -> PRESENCE: aura, calm, sway, offerings. Line: common room, offering stone, market pitch.
- AI -> INSIGHT: reading people; the familiar's skill. Line: perch and roost.
- CI/CD -> SPARKS: ranged strike. Line: beacon and signal fires.
- Gravesong -> ROADS (NEW): reach along the roads, links between embers and hearths, word from travellers and from the crossroads dead. Line: signposts, waystones, the ford, the burial ground.

== 6 HEARTH EFFECTS AND INCANTATIONS FOR THE 12 KNOWN SPELLS (DRAFT) ==
Step, cost, speed, check modifier and code are shared and unchanged. Effect text and phrase below apply only in Cinderford and live in the hearth-effects file, never in the ledger. Spells act inside act range unless the line says otherwise.
- Lantern Sweep (Basic) · "Nothing hides from my light." · The single biggest hidden object inside act range glows faintly for a breath.
- Quiet Watch (Basic) · "I do not blink." · One named thing entering 20 m sends a chill through the flame; lasts 2 hours.
- Night Shift (Basic) · "Small flame, tend me." · One wisp carries deadwood from inside act range to the pit for one hour, nothing else. Gives no mana.
- Mark (Basic) · "I have seen you as you are." · Marks one object (not a person) inside act range until sunset.
- Diff (Basic) · "You are not as I left you." · Yes or no to "has this changed since I last saw it?" for one object.
- Revert (Basic) · "Be as you were by my light." · Takes the -5 off one Bruised wound for an hour; needs a Mark, so it cannot help a person until Mark reaches Novice.
- Bottled Hearth (Basic) · "Carry me, and be warm." · A candle-sized piece of you in a bottle or lantern for one hour; warms the carrier's hands; a weak remote eye while carried.
- Calling Post (Basic) · "Come back to the warm." · One creature that has slept by the fire, inside sense range, feels a tug toward it; it may come.
- Sealed Vessel (Basic) · "What I keep does not spoil." · Keeps one meal left at the fire fresh for a day.
- Second Voice (Basic) · "Speak, spark." · One thin voice in the crackle mumbles a guess, often wrong.
- Echo Chamber (Basic) · "Say it again, and mean it." · A faint, sometimes wrong sense of whether one sentence spoken at the fire was said to please its listener.
- Familiar Bond (Novice) · summon phrase "Out of the smoke, to me." · Gary: small-animal strength; hurts only Danger 10 foes; one harmful hit at Danger 10+ sends him away; carries 1 kg; ranges about 100 m, which is past your own senses.
Locked previews (Gravesong is Novice; nothing castable; text to be confirmed when the subject reaches Beginner):
- Speak, Sleeper · "Ash, answer me." · One yes-or-no question, answered as a feeling, to someone who died or lies buried at the crossroads within 5 years.
- Grave-Tithe · Take "Give me your cold." / Give "Take my warmth." · Moves the -5 of one Bruised wound between two people at the hearth for an hour.
- Haunt · "My light goes with you." · For an hour, the rough direction of one person who sat at the fire today, within 100 m.

== 6b DELIBERATE SCOPE CHANGES FROM THORNWALL (Cinderford only) ==
- Calling Post: Thornwall calls F's own mount within 100 m. Cinderford calls one creature that has slept by the fire, inside sense range.
- Grave-Tithe: Thornwall moves a wound between F and a touched person. Cinderford moves it between two people at the hearth (the fire has no body to take it).
- Familiar Bond Novice: reads "one harmful hit at Danger 10+" per 09_spells v3; ledger v9 reads "at Danger 10" (09_spells wins; patch v1.1 fixes the ledger).
- All phrases replaced by Cinderford incantations (section 6); Thornwall phrases stay in the ledger.

== 7 FIRE RULINGS THAT REPLACE BODY RULES (DRAFT NUMBERS) ==
7.1 Range (Q59: steeper). Act range = 2 + 2p + p(p-4)/8 metres, p = promotions, rounded. Sense range = 5 x act. Along a road, sense reaches 10 x act. Each promotion also gives +3 maximum mana.
- 0 promotions: act 2 m, sense 10 m, along roads 20 m
- 4 promotions: act 10 m, sense 50 m, along roads 100 m
- 6 promotions: act 16 m, sense 78 m, along roads 155 m
- 10 promotions: act 30 m, sense 148 m, along roads 295 m
- 20 promotions: act 82 m, sense 410 m, along roads 820 m
- 30 promotions: act 160 m, sense 798 m, along roads 1595 m
- 40 promotions: act 262 m, sense 1310 m, along roads 2620 m
- 50 promotions: act 390 m, sense 1948 m, along roads 3895 m
- 60 promotions: act 542 m, sense 2710 m, along roads 5420 m
Valley size is set in 10_world so that late-game sense covers the valley floor.
7.2 Mana. Trickle = maximum / 24 per hour, rounded down, minimum 1 (now 1 per hour). Fuel fed by a person: +1 that hour. A real offering (shared food, a coin, something given up): +3, once per giver per day. Never above maximum. Replaces sleep, breakfast and meditation recovery.
7.3 Health, five levels: Bright -> Flickering -> Low -> Guttering -> Embers.
- Flickering: -5 on checks; act and sense range at three quarters.
- Low: -20 on checks; range halved; maximum mana -5.
- Guttering: casting costs double; range at one quarter; maximum mana halved; no new summons.
- Embers: no casting; senses only inside the pit; the dim clock runs.
- Recovery by fuel, tending and time; amounts to be written in 02_rules_hearth.
7.4 Dim clock: 7 days (Q61). Each full day at Embers ticks once; at 7 the fire goes out and restarts elsewhere with only skills and spells. Being tended back to Guttering resets it.
7.5 Familiar: "sent away until full night sleep" becomes "until the next dawn".
7.6 Voice: every cast is heard in the crackle by everyone inside the hearth ring. No silent casting.
7.7 Coins: guest coin is held by the innkeeper on the fire's account; quoted before commitment, never spent automatically.
7.8 Gravesong (Roads) reach (Q60): its spells ACT inside act range and may TARGET or READ anything inside sense range, including the extended reach along roads. No spade tier.
7.9 Not carried: guild rank, pool, gap pressure, mentors, board, gate hours, gear caps, armour layers.

== 8 FILE PLAN (names provisional) ==
- README (site index, load lists, LATEST SAVE, phone slots)
- 00_index
- 01_narration_cinderford (fire point of view, ambient pacing, short roll line, footer)
- 02_rules_cinderford (inherits Thornwall check rules; section 7 rulings)
- 03_project_instructions
- 04_curriculum + 04b_gravesong_curriculum (copies)
- 05_skills_ledger (Cinderford v10, copied from v9, Gravesong line added)
- 06_settlers (public; founder first)
- 07_buildings (ten lines, costs, build times)
- 08_arrivals (public: how the roll works)
- 09_spells + 13_spell_code (copies) and 09h_hearth_effects (all 30 spells, 8 steps, phrases)
- 10_world (valley, ford, three nations, species, churches, calendar and daylight)
- 11_lesson_chat_instructions (copy, edited: faceless dream-realm shaped by the subject examines; no mentors, no named examiner)
- gm/ world-gm, gm/ arrival-tables, gm/ pantheon
- save_000 + status_000 (25 March)

== 9 OPEN ==
None from the design rounds. Status of next steps:
1 Ledger v10: DONE as a patch (05_skills_ledger_v10_cinderford_patch v1.1). Player applies it to a full copy of v9. REFERENCES version numbers still to fill from the live Thornwall README.
2 README skeleton and 00_index: DRAFTED (cinderford_README_v0, cinderford_00_index_v0).
3 02_rules_cinderford: DRAFTED (02_rules_cinderford_v0.1). Q-R1 a (one level per steady-fuel day, +1 if tended), Q-R2 year 753.
4 10_world public + gm/ world-gm, then the founder for veto
5 07_buildings, 08_arrivals + gm/ arrival-tables, 09h_hearth_effects for all 30 spells
6 01_narration_cinderford, save_000 + status_000 (25 March)

== 10 LATER RULINGS (after v5; these win over sections 4.5, 5 building lines, 6, 6b and 8 above) ==
- Founder approved as sketched (half-orc cook).
- Q64: speech follows the HIGHEST rank held in any subject (05h section 2).
- Native powers per fire skill and rank: 05h_fire_powers v1.
- Q65: ONE spell per subject in Cinderford, each anchored to a Thornwall spell: Fire Ring (Read the Fight), Wisp Crew (Night Shift), Mend (Revert), Blind Eye (Whisper Lock), Carried Ember (Bottled Hearth), Brace (Lint Eye), Sanctuary (Budget Bell), Familiar Bond, Spark Volley (Twelve Looms), Follow (Haunt). File: 09h_hearth_spells v1 (replaces 09h_hearth_effects v0).
- Q66: Thornwall keeps all 30 spells; not touched.
- Q67: three buildings per skill; building 1 at Novice, 2 at Beginner, 3 at Apprentice; each later rank opens the next level of each; minor add-ons at any time for resources. File: 07_buildings v1.
- Ledger v10 written in full (patch applied). Rules v1 carries Thornwall's inherited sections as Annex A.
- Current file set: README v1, 00 v1, 01 v1, 02 v1, 03 v1, 04 v4, 04b v1, 05 v10, 05h v1, 06 v0, 07 v1, 08 v0, 09 v3, 09h v1, 10 v0, 11 (patch v1 to apply), 13 v3, gm x4 v0, save_000, status_000.

END OF BRIEF v6
