# rules-p2

SOURCE: 02_rules_cinderford_v1.md | version=1 | bytes=21197 | sha256=adb5c1ac9313b54b | part 2 of 2 | page_bytes=10750

````text
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
````

===== END FILE: 02_rules_cinderford_v1.md =====
