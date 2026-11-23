# skills-ledger-p2

SOURCE: 05_skills_ledger_v10.md | version=10 | bytes=46071 | sha256=e9756a15d5a44928 | part 2 of 4 | page_bytes=14655

````text
== SUBJECTS ==
PYTHON (Isaura) - Rank Novice · Base 20 · Caps Novice · Course Novice 0/11 (OPEN) · Derived: Arms · Lens S 0/0 R 0/0 O 0/0 · Weak points: none · Last exam: none.
LINUX/BASH (Runa) - Rank Beginner · Base 30 · Caps Beginner · Course Beginner 0/6 (BLOCKED until Cybersecurity Beginner) · Derived: Fieldcraft · Lens S 5/6 R 0/5 O 5/6 (units 6-10; units 1-5 taught before the v3 batch format, no lens items; retry items counted as asked) · Last exam: Novice -> Beginner Pass (dream-lesson 7).
Weak points: Kernel manages resources and enforces permissions; the shell interprets (the kernel never translates or interprets commands or scripts). Nested shells: the parent waits, exit ends the shell that ran it, the parent takes the next command. $SHELL is the login shell; use ps -p "$$" for the running shell. Closing a terminal sends SIGHUP, but not every process dies. An absolute path starts at / and only there (~ expands to one; 'from home' is not a kind of absolute path). A space separates arguments, a slash joins path parts (mkdir -p camp/maps old made two dirs). cp -r into an EXISTING directory nests (dst/src/...). [ab]* means 'starts with a or b'. '-' in ls -l is an ordinary file, not a text file. Private directory = 700 (owner needs x to enter), not 600; 640 plus u+x = 740. New group membership needs a fresh login session. Esc before :wq. A pipe carries stdout only, from left stdout into right stdin. The last command in a pipe decides the output: wc -l prints a number, and empty input prints 0, not nothing. A redirect empties the target before the command runs; always give the fix (write to a new file). apt install shows its plan before [Y/n]. Long options take two dashes (--installed). Check filenames in your own code. Answer format: write True/False as a word first; line number in front of fixes; verdict letter AND line:tag pairs on review items. Interview answers: direct answer first, then method, then the named trade-off.
S: E325 swap warning: STILL RUNNING = go to the other session; not running = recover, check, save, then delete the swap file. Swap/backup files (.swp, .save, ~) are copies holding secrets: ignore them in git and stage by name. sudoedit, not sudo vim (a root editor can run commands and plugins as root). Secrets on the command line leak to history and to every user via ps (tokens as much as passwords); pass by prompt, 600 file, stdin or a secret manager. Hidden is not protected; permissions are. No grep hits does not mean clean (patterns, git history, encodings); use a real scanner (gitleaks) and rotate anything real. Private keys need 600. cd "$EMPTY" goes home, so cd $X && rm -rf * wipes home. find -delete goes last, after a dry run. trusted=yes and plain-http unknown mirrors are not trustworthy; the signature proves the package lists are signed and each package checked against them. update before upgrade; auto-install security updates, review bigger ones. kill -9 only after SIGTERM has failed (method, when, trade-off).
O: never paste swap files or .env into an oracle; if it happens, rotate. Give the command, the behaviour and harmless values only.
R: give line:tag pairs, put each finding on the right line; catch hallucinated flags (--save-backup, --secrets) and typo packages (H/P); catch success messages printed without a check; catch lines that upload or publish findings.
GIT/GERRIT (Runa) - Rank Beginner · Base 30 · Caps Beginner · Course Beginner 0/7 (BLOCKED until Cybersecurity Beginner) · Derived: First aid · Lens S 0/0 R 0/0 O 0/0 · Last exam: Novice -> Beginner Pass (dream-lesson 3).
Weak points: snapshot vs diff (a commit points to a full tree, not a list of changes; unchanged files referenced by content hash, not re-stored); area names (working tree, index/staging area, repository) rather than file states; commit contents (snapshot, parent, author/committer, date, message; ID is a hash of all of it incl parent); staged files still appear in git status (under Changes to be committed); staging exists to build focused commits; git status -s two-column reading and exact spacing (' M a.txt', 'A  b.txt'); plain git diff = working tree vs index, --staged = index vs last commit, HEAD = working tree vs last commit; hunk header @@ -1,2 +1,3 @@ with context lines; commit messages: capitalised, imperative, one logical change, blank line, body explains why; git diff does not show untracked files, use git status first and never git add . blindly; check -am/-a redundancy.
CYBERSECURITY (Zofia) - Rank Novice · Base 20 · Caps Novice · Course Novice 2/9 (units 1, 2 Rough; OPEN; lead subject) · Derived: Awareness, Stealth · Lens S 0/0 R 0/0 O 0/0 · Last exam: none (Sets A and B unspent; item 2 of each now examines unit 9).
Weak points: Unit 1 (Rough): integrity also covers encryption-as-modification and not trusting files after a breach; a comparison is only as good as the trusted copy (offline/immutable backups, stored hashes, signed manifests); show the arithmetic for risk = likelihood x impact; 'avoid' means stopping the activity, a safer tin is 'mitigate'; 'accept' means weighed and written down, not 'don't care'; count knock-on effects when scoring impact; encryption shifts the problem to key custody and can cost availability if the key is lost. Unit 2 (Rough): state the motive as well as the technique; careless insiders make mistakes, while tailgating and shoulder-surfing are attacker techniques; hacktivists want to be seen (attention, not money); spoofing attacks authentication, elevation of privilege gives a real account more rights than it should have; name the actor from the table ('anyone' is not one); publishing details enlarges the attack surface (information disclosure); give one-line examples when asked.
DOCKER/K8S (Hedda) - Rank Beginner · Base 30 · Caps Beginner · Course Beginner 0/9 (BLOCKED until Cybersecurity Beginner) · Derived: Riding, handling · Lens S 0/0 R 0/0 O 0/0 · Last exam: Novice -> Beginner Pass (dream-lesson 5).
Weak points: Kernel and isolation: containers share the host kernel; namespaces limit what a process can see, cgroups limit what it can use; Docker Desktop on macOS/Windows runs a hidden Linux VM because containers need a Linux kernel. Images and layers: image layers are read-only and shared; each container has its own writable layer (copy-on-write); a removed container's changes die with it; a new container always starts fresh from the image; a tag does not make an image read-only. Install: dockerd (root daemon, via containerd/runc) vs docker CLI talking over a Unix socket; permission denied means the user is not in the docker group, and the docker group is root-equivalent (not 'sudo'); install from Docker's apt repository, never mix docker.io with docker-ce, convenience script is for dev/test; removing packages leaves /var/lib/docker, so never rm -rf it casually; published ports can bypass ufw; json-file logs need rotation. Lifecycle: run creates, start restarts; stop sends SIGTERM then SIGKILL (it does not 'freeze'); exit 137 = SIGKILL; a container lives as long as PID 1, so the app must stay in the foreground (-d only detaches your terminal); flags go BEFORE the image name; --name, not -n; exec needs -it and a running container; rm needs a stopped container or -f. Tags and digests: latest is only the default tag, not 'newest'; pin a version tag or image@sha256:<hash> (pinning blocks updates); docker image inspect -f '{{.Config.Cmd}}' is case-sensitive; two tags can share one IMAGE ID. Registries: registry vs namespace vs repository vs tag; a push needs the registry host in the image name and an actual docker push; log in with a token via --password-stdin; config.json is base64, not encryption; log out of a named server. Ports: -p HOST:CONTAINER; docker port prints the container side first; EXPOSE only records, -P publishes exposed ports to random host ports; 127.0.0.1:... means host-only; apps must listen on 0.0.0.0 inside; databases belong on 127.0.0.1; a failed run leaves a Created container behind. Project: files added with docker cp die with the container; verify with ps (state, PORTS), port/curl, and logs (proves the request reached this container); no -p means nothing is published.
IAC (Tamsin) - Rank Novice · Base 20 · Caps Novice · Course Novice 0/7 (OPEN) · Derived: Athletics · Lens S 0/0 R 0/0 O 0/0 · Weak points: none · Last exam: none.
AZURE (Calla) - Rank Novice · Base 20 · Caps Novice · Course Novice 0/7 (OPEN) · Derived: Persuasion · Lens S 0/0 R 0/0 O 0/0 · Weak points: none · Last exam: none.
AI (Fenna) - Rank Beginner · Base 30 · Caps Beginner · Course Beginner 0/11 (BLOCKED until Cybersecurity Beginner; spell tasks within cap allowed) · Derived: Insight · Lens S 0/0 R 0/0 O 0/0 · Last exam: Beginner Pass (dream-lesson 2).
Weak points: library/database misconception (models have parameters, not lookups); pretraining vs instruction tuning/RLHF; context-budget arithmetic and what happens on overflow; checking summaries against source (model cannot "confirm" or cite what it was not given); prompt template vs logic code (rules must be instructions to the model); delimiters and explicit source-only rules; never label unchecked output "verified"; sampling follows probabilities. Added v6 (spell tasks): unquoted variables in Bash tests ([ $var == "" ] breaks on empty or spaced input; use [ -z "$var" ]); error messages belong on stderr (>&2, file=sys.stderr), repeated three times; injected source text needs delimiters the source cannot fake (prompt injection via the notes file); answers passed through with no check against the notes; scoring must compare like with like (pushback answer format must match the first answer); a model that ignores the format rule should count as unreadable, not flipped; six questions is a hint, not a measurement.
CI/CD (Katla) - Rank Novice · Base 20 · Caps Novice · Course Novice 0/6 (OPEN) · Derived: Crossbow · Lens S 0/0 R 0/0 O 0/0 · Weak points: none · Last exam: none.
GRAVESONG (self-taught) - Rank Novice · Base 20 · Caps Novice · Course Novice 0/12 (OPEN; 04b_gravesong_curriculum v1) · Derived: Deathspeech (Thornwall) / Roads (Cinderford) · Lens S 0/0 R 0/0 O 0/0 · Weak points: none · Last exam: none.

== GEAR CAPS (by full rank) ==
Blade: Python Novice. Trail/camp kit: Linux/Bash Beginner (raised v8). Healer's kit, potions: Git/Gerrit Beginner. Outer shell: Cybersecurity Novice (thick hide jerkin). Mount, cart: Docker/K8s Beginner. Underlayer: IaC Novice (heavy wool and linen). Mana items, hired services: Azure Novice. Familiar: AI Beginner (skill follows AI rank; power follows Familiar Bond step; 02_rules 5). Crossbow: CI/CD Novice. Cinderford: gear caps are not used; each subject's rank unlocks buildings and levels per 07_buildings.

== KNOWN SPELLS ==
All known spells are at step BASIC except Familiar Bond (NOVICE from v9: 8 mana · one exchange, main action · check modifier -10). Basic: 10 mana each · slow (takes both action slots; interrupted by a hit) · check modifier -20 (09_spells v3 section 3). Code: 13_spell_code v2 (version 0 starters; Familiar Bond version 1) (Basic bar, about 20 lines). Upgrades above Basic need an OOC dream session and approval (09_spells v3 section 5), capped at the subject's full rank (Beginner step at most for all four subjects).
Casting rule: every cast makes F speak the phrase aloud, word for word, in a voice not quite his own: lower, slower, graveside. It cannot be whispered, mouthed or skipped. Everyone in earshot hears it and reacts (09_spells v3 section 6; 02_rules 4).

LINUX/BASH (Runa)
### Lantern Sweep - Basic · 10 mana
Subject: Linux/Bash (Runa Kettleby) · Language: Bash
Phrase: "Rise, you hidden things."
Effect (current step): The single biggest hidden object in a small room glows faintly for a breath.
Real task: find/du/sort size report
Learned: ledger v8 (granted at Basic by the v8 spell ruling) · Last upgraded: - · Reviewed by: - (none yet; upgrades reviewed by Runa)
### Quiet Watch - Basic · 10 mana
Subject: Linux/Bash (Runa Kettleby) · Language: Bash
Phrase: "The dead keep watch for me."
Effect (current step): One named thing (for example "wolf") within 20 m wakes him with a chill; lasts 2 hours.
Real task: tail -F + grep follower
Learned: ledger v8 (granted at Basic by the v8 spell ruling) · Last upgraded: - · Reviewed by: - (none yet; upgrades reviewed by Runa)
### Night Shift - Basic · 10 mana
Subject: Linux/Bash (Runa Kettleby) · Language: Bash + systemd
Phrase: "The dead do not sleep."
Effect (current step): A shade feeds the fire for one hour, nothing else.
Real task: systemd service + timer via script
Learned: ledger v8 (granted at Basic by the v8 spell ruling) · Last upgraded: - · Reviewed by: - (none yet; upgrades reviewed by Runa)

GIT/GERRIT (Runa)
### Mark - Basic · 10 mana
Subject: Git/Gerrit (Runa Kettleby) · Language: Git CLI
Phrase: "This moment is mine forever."
Effect (current step): Marks one object (not a person) until sunset.
Real task: Commit a state snapshot with a meaningful message
Learned: ledger v8 (granted at Basic by the v8 spell ruling) · Last upgraded: - · Reviewed by: - (none yet; upgrades reviewed by Runa)
Note: one Mark per person or object unless a step allows more (09_spells v3 section 7).
### Diff - Basic · 10 mana
Subject: Git/Gerrit (Runa Kettleby) · Language: Git CLI
Phrase: "Show me what was taken."
Effect (current step): Yes or no to "has this changed since I last saw it?" for one object.
Real task: Use log/diff to find and explain a change
Learned: ledger v8 (granted at Basic by the v8 spell ruling) · Last upgraded: - · Reviewed by: - (none yet; upgrades reviewed by Runa)
### Revert - Basic · 10 mana
Subject: Git/Gerrit (Runa Kettleby) · Language: Git CLI
Phrase: "Death, give back what you took."
Effect (current step): Takes the −5 penalty off one Bruised wound for an hour; the wound stays. Needs a Mark.
Real task: Safely undo a bad commit (revert vs reset)
Learned: ledger v8 (granted at Basic by the v8 spell ruling) · Last upgraded: - · Reviewed by: - (none yet; upgrades reviewed by Runa)
Note: needs a valid Mark made before the injury. Mark at Basic marks objects only (not people), so Revert cannot help a person until Mark reaches Novice. Healing clause and daily limits: 09_spells v3 section 7.

DOCKER/K8S (Hedda)
### Bottled Hearth - Basic · 10 mana
Subject: Docker/K8s (Hedda Stroud) · Language: docker CLI
Phrase: "Wake the hearth in the glass."
Effect (current step): A candle-sized flame in a bottle for one hour; warms his hands.
Real task: Run and reach a web-server container
````

===== END PAGE: 05_skills_ledger_v10.md | part 2 of 4 =====
