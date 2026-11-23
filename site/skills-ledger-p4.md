# skills-ledger-p4

SOURCE: 05_skills_ledger_v10.md | version=10 | bytes=46071 | sha256=e9756a15d5a44928 | part 4 of 4 | page_bytes=11731

````text
== UNIT CHECKLIST (current courses; curriculum v3 titles; S = security focus; R and O lenses always apply) ==
PYTHON - Novice (OPEN, 0/11)
[ ] 1 [T] What a program is; interpreter vs compiler; CPython source -> bytecode -> VM. S: the interpreter runs whatever it is given; never run untrusted scripts.
[ ] 2 [H] Install Python; venv, pip, uv; REPL; run scripts. S: install only known packages; typosquatting; never sudo pip; venv isolation.
[ ] 3 [T] Values and types. S: converting untrusted input fails loudly; validate types.
[ ] 4 [T] Variables, naming, expressions, operators. S: no secrets in code; constants vs environment.
[ ] 5 [H] Strings: slicing, methods, f-strings. S: strings built into shell or SQL commands are injection.
[ ] 6 [T] Conditions, truthiness, comparison. S: fail closed, the default branch denies; is vs in checks.
[ ] 7 [T] Loops: for, while, range, break/continue. S: bound loops and retries on input.
[ ] 8 [H] Lists and tuples. S: aliasing leaks shared data.
[ ] 9 [T] Functions: parameters, return, scope. S: validate at the function boundary; eval, exec and input.
[ ] 10 [H] Reading tracebacks; print debugging. S: tracebacks leak paths and secrets; never show them to users.
[ ] 11 [H] Small project: number guessing or unit converter. S: validates input, uses no eval.
LINUX/BASH - Novice COMPLETE (promoted to Beginner, v8)
[x] 1 OS, kernel, shell, terminal - Rough (weak: kernel enforces, shell interprets; nested shells; $SHELL vs ps -p "$$"; SIGHUP)
[x] 2 [H] pwd, ls, cd, paths - Clean
[x] 3 [H] cp, mv, rm, mkdir, touch; globbing - Rough (weak: space vs slash; cp -r into an existing directory)
[x] 4 [H] cat, less, head, tail - Clean
[x] 5 Users, groups, permissions; chmod/chown; sudo - Rough (weak: '-' is an ordinary file; directory 700; 640+u+x = 740; fresh login for groups)
[x] 6 [H] nano, vim basics - Rough (weak: S E325 running vs not; :q! keeps saved edits; O never paste swap/.env; R line:tag pairs)
[x] 7 [H] Pipes and redirection - Rough (weak: pipe is stdout only; wc -l prints a number; redirect truncates first, give the fix; S ps shows arguments)
[x] 8 [H] grep, find, wc, sort, uniq - Rough (weak: read the chain link by link, -f picks the field; S no hits is not clean; R uploads of findings)
[x] 9 Processes: ps, top, kill, signals - Rough (weak: verdict letter; True/False word; kill -9 method, when, trade-off)
[x] 10 [H] apt - Rough (weak: install shows its plan before Y/n; --installed; S trusted=yes and http mirrors; R line numbers and typo packages)
LINUX/BASH - Beginner (BLOCKED until Cybersecurity Beginner, 0/6; no unit T)
[ ] 1 [H] Scripting: shebang, variables, quoting. S: quoting as injection defence.
[ ] 2 [H] Conditionals, loops, functions
[ ] 3 [H] Exit codes; set -euo pipefail; traps. S: mktemp, cleanup.
[ ] 4 [H] shellcheck
[ ] 5 Env vars, PATH, dotfiles. S: PATH hijack, secrets in env and history.
[ ] 6 [H] Oracle-built project: backup script with logging, in git
GIT/GERRIT - Novice COMPLETE (promoted to Beginner, v3)
[x] 1 [T] What version control is; snapshots vs diffs - Rough (weak: storage detail, referenced vs stored)
[x] 2 [T] The Git model: commits, the three areas - Rough (weak: status columns)
[x] 3 [H] git init, add, commit, status - Rough (weak: reading status output)
[x] 4 [H] git log and git diff; reading history - Rough (weak: both diff halves, hunk header, context lines)
[x] 5 [H] Project: small repo, five meaningful commits - Rough (credited on player's statement; unseen)
GIT/GERRIT - Beginner (BLOCKED until Cybersecurity Beginner, 0/7)
[ ] T [T/H] Top-up: secrets and identity in git (rotate first, then clean history); reading a diff; reviewing oracle commits; revisits ledger weak points (snapshot model, the three areas, diff variants, never git add . blindly). Recommended first.
[ ] 1 [H] Branches and switching
[ ] 2 [H] Merging and resolving conflicts
[ ] 3 [H] Remotes: GitHub, clone, push, pull
[ ] 4 [H] .gitignore; secrets out of history
[ ] 5 [H] Undoing: restore, reset, revert, and which is safe
[ ] 6 [H] Project: feature branch, conflict, merge, push, w an oracle that resolves a conflict wrongly for the player to catch
CYBERSECURITY - Novice (OPEN, lead; 2/9; one-pass course, single exam)
[x] 1 [T] CIA triad; risk = likelihood x impact - Rough (weak: integrity after breach, arithmetic shown, avoid/mitigate/accept usage, knock-on impact, key custody)
[x] 2 [T] Threat actors and motives - Rough (weak: motive vs technique, insider mistakes vs attacker techniques, spoofing vs elevation of privilege, naming actors, attack surface)
[ ] 3 [T] Common attacks: phishing, malware, credential stuffing
[ ] 4 [T] Passwords, hashing, MFA, managers
[ ] 5 [H] Secrets out of code: .env, .gitignore
[ ] 6 [T] Networking: IP, ports, TCP/UDP, DNS, HTTP/HTTPS
[ ] 7 [T] Encryption: symmetric, asymmetric, TLS
[ ] 8 [H] Scan your own machine: ss, nmap localhost
[ ] 9 [H] NEW AI tools and security, first look: what never to paste (secrets, personal data, customer data, internal code without approval), redaction, AI output is untrusted, hallucinated and typosquatted packages, the review rubric named. RECOMMENDED NEXT.
DOCKER/K8S - Novice COMPLETE (promoted to Beginner, v5)
[x] 1 Containers vs VMs; images vs containers - Rough (weak: copy-on-write, tag does not make an image read-only)
[x] 2 [H] Install Docker - Rough (weak: daemon/CLI socket, docker group is root-equivalent, install source, rm -rf /var/lib/docker)
[x] 3 [H] run, ps, logs, exec, stop, rm - Clean (weak: run creates vs start restarts; PID 1 must stay in the foreground)
[x] 4 [H] Pull and inspect images; tags; why latest isn't a version - Rough (weak: digest syntax, pinning blocks updates, inspect format, shared IMAGE ID)
[x] 5 Registries - Rough (weak: name the repository, push needs registry host and docker push, --password-stdin)
[x] 6 [H] Port mapping - Rough (weak: --name, 0.0.0.0 inside the container, docker port output, databases on 127.0.0.1)
[x] 7 [H] Project: web-server container - Rough (weak: no -p means nothing published, docker cp dies w the container, three verification levels)
DOCKER/K8S - Beginner (BLOCKED until Cybersecurity Beginner, 0/9)
[ ] T [T/H] Top-up: image trust and pinning by digest; the docker group and docker.sock are root; published ports bypass ufw and 0.0.0.0 exposure; --privileged; reading oracle docker commands. Recommended first.
[ ] 1 [H] Dockerfile; layers, caching. S: secrets left in layers, ARG and ENV.
[ ] 2 [H] build/tag/push. S: registry login, immutable tags.
[ ] 3 [H] Volumes, bind mounts. S: host paths, read-only mounts, socket mounts.
[ ] 4 [H] Networks. S: exposure, internal networks.
[ ] 5 [H] Compose. S: env files, secrets, port binding, privileged and added capabilities.
[ ] 6 Image size, base images, .dockerignore. S: minimal bases, attack surface, patch cadence.
[ ] 7 [H] Env vs secrets; non-root. S: USER, read-only root filesystem, dropped capabilities.
[ ] 8 [H] Oracle-built project: containerise your Python CLI.
IAC - Novice (OPEN, 0/7)
[ ] 1 Declarative vs imperative; idempotence. S: idempotence and blast radius; drift from desired state.
[ ] 2 YAML syntax. S: secrets do not belong in YAML.
[ ] 3 [H] Pitfalls: Norway, indentation, tabs, quoting. S: parsing traps that silently change security settings (enabled: no, on).
[ ] 4 [H] yamllint. S: lint in CI; a linter does not check meaning.
[ ] 5 [H] Read others' YAML: compose, workflow, playbook. S: spot privileged: true, hardcoded secrets, 0.0.0.0 ports.
[ ] 6 JSON vs YAML vs TOML. S: safe loaders (yaml.safe_load); JSON for untrusted input.
[ ] 7 [H] Project: ward system in YAML, validated. S: validate against a schema; no secrets in the file.
AZURE - Novice (OPEN, 0/7)
[ ] 1 Cloud concepts: IaaS/PaaS/SaaS, regions, availability, SLA, shared responsibility. S: what stays yours on IaaS, PaaS, SaaS.
[ ] 2 Subscriptions, resource groups, tags. S: tags for ownership and accountability; resource groups as an RBAC scope.
[ ] 3 Pricing, budgets; forgotten resources. S: a cost spike can mean a compromise (cryptomining).
[ ] 4 [H] Free account; budget alerts. S: MFA on the account; no shared logins.
[ ] 5 [H] Azure CLI basics. S: az login token storage; never a password in a script; output can leak secrets.
[ ] 6 Identity first look: tenant, account. S: MFA, guest accounts, who is in your tenant.
[ ] 7 [H] Project: create, tag, cost-estimate, delete a resource group. S: deletion leaves nothing orphaned or exposed.
AI - Novice COMPLETE (promoted to Beginner, v2)
[x] 1 [T] What an LLM is: tokens, training, next-token prediction - Clean
[x] 2 [T] Context windows and temperature - Clean (weak: temperature extremes)
[x] 3 [T] Hallucination and why - Rough (weak: checking summaries against source)
[x] 4 [T] Prompting basics - Rough (weak: delimiters, source rules, assumed-agreement wording)
[x] 5 [H] Ollama: run a local model - credited (player's prior pass)
[x] 6 [H] Compare two models on the same question - credited (player's prior pass)
AI - Beginner (BLOCKED until Cybersecurity Beginner, 0/11)
[ ] T [T] Top-up: what data may be sent to a model; retention; local vs hosted; the review rubric applied; revisits ledger weak points (prompt template vs logic, delimiters, never label unchecked output verified). Recommended first.
[ ] 1 [H] Call a local model from Python
[ ] 2 [H] Structured output: JSON, schemas. S: model output is untrusted input.
[ ] 3 System prompts, few-shot. S: prompt injection first look; a system prompt is not a security boundary or a secret store.
[ ] 4 [H] Chat CLI with history
[ ] 5 Costs and limits of hosted APIs. S: runaway cost; API key handling.
[ ] 6 [H] Review three oracle-written scripts
[ ] 7 [H] Familiar Bond: grounded assistant (spell known v6; unit lesson still open)
[ ] 8 Sycophancy, seeds/temperature, testing an oracle (Echo Chamber known v6; unit lesson still open)
[ ] 9 [H] NEW Working with a coding oracle I: task specification, context, acceptance checks, small diffs, tests first, the verify loop, when not to use it
[ ] 10 NEW Coding assistants and agents first look: completion vs chat vs agent; approval modes; rules files; what an agent can read
CI/CD - Novice (OPEN, 0/6)
[ ] 1 Why automate; CI vs CD. S: a pipeline runs code w privileges on every push.
[ ] 2 Pipelines, stages, jobs, artefacts, runners. S: runners hold credentials; artefacts can leak secrets.
[ ] 3 [H] Read a workflow. S: echoed secrets, unpinned actions, broad permissions.
[ ] 4 [H] First GitHub Actions workflow. S: permissions: contents: read; pin actions.
[ ] 5 [H] Failed run: log, step, fix. S: debug logs leak secrets; redact logs before pasting anywhere, including AI.
[ ] 6 Pipeline hazards: secrets, latest, success masking, force flags (already a security unit).

GRAVESONG - Novice (OPEN, 0/12; 04b_gravesong_curriculum v1; S focus per unit as written there)
[ ] 1 [T] Network models: OSI and TCP/IP layers, encapsulation
[ ] 2 [H] IPv4 addressing: CIDR, private ranges, NAT, port forwarding; IPv6 first look
[ ] 3 [H] DNS in practice
[ ] 4 [H] HTTP for operators
[ ] 5 [H] TLS for operators
[ ] 6 [H] Sockets by hand
[ ] 7 [H] Web servers and reverse proxies
[ ] 8 [H] Firewalls
[ ] 9 [H] SSH and tunnels
[ ] 10 [H] Observability first look
[ ] 11 [T] SRE first look
[ ] 12 [H] Project, troubleshooting: "the site is down"

== MIGRATION NOTE (v6 -> v7) ==
All v2/v6 ticks stand under the same unit numbers. Moved units (none ticked): Cybersecurity v2 Expert 1-2 -> Journeyman 9; v2 Expert 3, 4, 5 -> Expert 1, 2, 3. Docker v2 Expert 1 -> Journeyman 8. IaC v2 Apprentice 1 (vault part) -> Beginner 8. The five unstarted Novice courses keep their unit lists, taught w the three lenses from the start; no unit T.
END OF LEDGER v10
````

===== END FILE: 05_skills_ledger_v10.md =====
