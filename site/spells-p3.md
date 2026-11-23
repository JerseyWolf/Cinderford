# spells-p3

SOURCE: 09_spells_v3.md | version=3 | bytes=41726 | sha256=fe16321c60d69f8c | part 3 of 3 | page_bytes=13371

````text
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
````

===== END FILE: 09_spells_v3.md =====
