# Thornwall — Curriculum, v4 (security-led, three lenses)

Replaces 04_curriculum_v3.md (18 Nov 2026 planning repair: grade wording removed, guild formula pointer, lesson instructions pointer; nothing else changed), which replaced 04_curriculum_v2.md. Written from 04_curriculum_v3_change_spec_v2 (final, player-confirmed). Where v3 and v2 differ, v3 wins. No tables anywhere in this file (project-wide ruling, ledger v6).

Purpose: the lessons are real interview preparation for DevOps, DevSecOps and cybersecurity roles. Every unit must let the player honestly claim three things, in this order of importance: he knows enough security to make AI-assisted code secure and to use AI tools securely; he can review and judge code someone else wrote with AI; he can write good code with AI. Nothing is skipped on the assumption that he already knows it.

## A. Rules amendments (these override 02_rules where they conflict)

- §1.1 Ladder: full ranks only. Novice 20, Beginner 30, Apprentice 45, Journeyman 60, Expert 75, Master 85, Grandmaster 95. There is no "+" step, and the base changes only on promotion. (Unchanged from v2.)
- A promotion does all of the following at once: new roll base, gear cap, spell step cap (09_spells steps; grades abolished), and +3 maximum mana. (Unchanged.)
- §1.3 Guild rank: formula in 02_rules 1.3. (Unchanged.)
- §2 Lessons: units can be taken in any order within a rank's course, subject to the security gate below. Every unit must be Clean or Rough before the exam. Lessons follow the unit format in section C and 11_lesson_chat_instructions (latest).
- §2a Security gate (NEW, hard rule). No unit of a subject's rank-N course may be started, and its exam may not be sat, until Cybersecurity is at rank N or higher. Example: any Beginner course (the course taken at Beginner, leading to Apprentice) needs Cybersecurity Beginner first. Novice courses are always open. Cybersecurity itself is exempt and always leads.
- §2a interpretations: the gate covers units and exams only. Spell tasks within the subject's current full-rank cap are not course units and stay allowed. A unit ticked before the gate existed stays ticked (none exist). The mentor checks the gate at the start of every lesson chat and refuses in character, with one OOC line, if it is not met.
- §2b What the gate buys: inside a rank-N course, S items and exam security items may assume everything in the Cybersecurity courses below rank N, applied to the subject. They teach the subject-specific application and do not re-teach the basics.
- §2c Other subjects in snippets: the player is assumed to raise every subject to rank N before starting any rank-N course, so snippets in a rank-N course may use other subjects' material from courses below rank N. This is a working assumption, not a gate: if the ledger shows a subject lower, the mentor limits snippets in that language to the rank actually held.
- §3 Exams: one exam per rank, covering every unit of the course (including unit T where it exists). Blueprints are in section D. Retained sets are in section F. From Beginner → Apprentice up, the mentor writes the set at exam time; no keys are stored here. A third attempt at Novice → Beginner uses fresh questions to the same blueprint.
- Contract gates written as "X Beginner+" read as "X Beginner". (Unchanged.)
- Skills never grow by use; only lessons and exams change the ledger. (Unchanged project rule, restated.)

## B. Courses

Conventions:
- [T] means theory, [H] means hands-on. Until Journeyman, everything is taught and examined in chat. From Journeyman, exams also include a PC task. Ranks marked OUTLINE wait for an approved syllabus.
- v2 unit numbers are kept. New units take the next free number and are marked NEW.
- Every unit carries three lenses on top of its topic: S (Secure), R (Review an oracle-written artefact), O (Oracle practice). "S:" below gives the unit's security focus; R and O always apply and are not listed. Where a v2 unit has no S: listed, the mentor sets an S item at the gate level for that topic.
- Unit T, the top-up, opens the Git, AI and Docker Beginner courses only. It applies the three lenses to the completed Novice course. It is recommended first, counts as one unit, and must be Clean or Rough before the exam.
- "Oracle-built project": the player writes the specification and acceptance checks, the mentor shows what the oracle produced, and the player reviews, corrects and signs it off. All in chat.
- "Oracle review": replaces v2's "review peers'" units. Three oracle-written artefacts judged with the review rubric (section C).
- From the Apprentice course up, questions ask for the decision and the trade-off as well as the fact.

### Cybersecurity — Zofia Drell (lead subject)
- Novice (9): 1 CIA triad; risk = likelihood × impact · 2 Threat actors and motives · 3 Common attacks: phishing, malware, credential stuffing · 4 Passwords, hashing, MFA, managers · 5 [H] Secrets out of code; .env, .gitignore · 6 Networking: IP, ports, TCP/UDP, DNS, HTTP/HTTPS · 7 Encryption: symmetric, asymmetric, TLS · 8 [H] Scan your own machine: ss, nmap localhost · 9 [H] NEW AI tools and security first look: what never to paste (secrets, personal data, customer data, internal code without approval), redaction, AI output is untrusted, hallucinated and typosquatted packages, the review rubric named. Recommended early: every other subject's O lens leans on it.
- Beginner (12): 1 OWASP Top 10, current edition, as a map; CWE; reading CVE and CVSS · 2 [H] SQL injection; command injection; path traversal; parameterisation · 3 [H] XSS; CSRF; SSRF; output encoding · 4 AuthN vs AuthZ; sessions and cookie flags; tokens and JWT pitfalls · 5 STRIDE; data-flow diagrams; trust boundaries · 6 [H] pip-audit; dependency scanning; pinning and lockfiles; slopsquatting · 7 [H] gitleaks; rotation; secret managers · 8 Logging: what to log, what never to log · 9 [H] Project: threat model and fixes for an oracle-written service · 10 NEW Secure-by-default principles: least privilege, defence in depth, fail closed, attack surface · 11 NEW AI-assisted work security I: data classification and policy, insecure-by-default AI output patterns, licences, the review rubric in full · 12 NEW LLM application risks first look: OWASP LLM Top 10, direct and indirect prompt injection, improper output handling, excessive agency
- Apprentice (11): 1 Least privilege, IAM; service accounts; short-lived credentials · 2 Segmentation, firewalls; TLS and mTLS; egress control · 3 [H] Semgrep, Bandit; triage and false positives · 4 [H] Trivy and checkov; triage by exploitability · 5 [H] Secure CI (with Katla): OIDC, pinned actions, least-privilege tokens, untrusted pull requests · 6 Crypto in practice: authenticated encryption, key management, certificates, what never to hand-roll · 7 [H] Linux hardening review (with Runa) · 8 [H] Secure code review method on oracle code: sources to sinks, severity, writing findings · 9 [H] Red/blue drill on an oracle-built service · 10 NEW AI-assisted work security II: coding agents, permissions and approval modes, sandboxing, rules files and MCP servers as attack surface, OWASP Agentic Top 10 as a map · 11 NEW Vulnerability management: SLAs, risk acceptance, patching, SBOM first look
- Journeyman (9): 1 Cloud security · 2 [H] Azure RBAC, Key Vault, Defender (with Calla) · 3 Supply chain: SBOM, cosign · 4 [H] Kubernetes security · 5 Incident response · 6 [H] Incident drill · 7 Compliance basics · 8 NEW Detection: log pipelines, SIEM, MITRE ATT&CK · 9 [H] NEW LLM application security in depth (with Fenna): injection defence patterns, output handling, RAG poisoning, guardrails (moved down from v2 Expert 1–2)
- Expert (5): 1 [H] Securing MCP and agents at scale (v2 Expert 3) · 2 [H] Threat-model an AI system (v2 Expert 4) · 3 [H] Lead the blue team (v2 Expert 5) · 4 NEW AI governance and acceptable-use policy for engineering teams · 5 NEW Security architecture review and design defence

### Python — Isaura Venn
- Novice (11): 1 [T] What a program is; interpreter vs compiler; CPython source → bytecode → VM — S: the interpreter runs whatever it is given; never run untrusted scripts · 2 [H] Install Python; venv, pip, uv; REPL; run scripts — S: install only known packages; typosquatting; never `sudo pip`; venv isolation · 3 [T] Values and types — S: converting untrusted input fails loudly; validate types · 4 [T] Variables, naming, expressions, operators — S: no secrets in code; constants vs environment · 5 [H] Strings: slicing, methods, f-strings — S: strings built into shell or SQL commands are injection · 6 [T] Conditions, truthiness, comparison — S: fail closed: the default branch denies; `is` vs `==` in checks · 7 [T] Loops: for, while, range, break/continue — S: bound loops and retries on input · 8 [H] Lists and tuples — S: aliasing leaks shared data · 9 [T] Functions: parameters, return, scope — S: validate at the function boundary; `eval`, `exec` and `input` · 10 [H] Reading tracebacks; print debugging — S: tracebacks leak paths and secrets; never show them to users · 11 [H] Small project: number guessing or unit converter — S: project validates input and uses no `eval`
- Beginner (11): 1 Dicts and sets · 2 Comprehensions; enumerate, zip · 3 [H] Files, with, pathlib — S: path traversal, permissions, temp files · 4 [H] JSON and CSV — S: untrusted data, safe YAML loading, never unpickle untrusted data, CSV injection · 5 Exceptions — S: fail closed, no bare except, no secrets in error text · 6 Modules, imports, stdlib tour — S: pinning, lockfiles, hallucinated imports · 7 [H] argparse, plus subprocess — S: input validation, no shell=True · 8 [H] pytest — S: negative and abuse-case tests; testing oracle code · 9 Style: PEP 8, docstrings, ruff — S: Bandit first look · 10 [H] Git-tracked project with tests (with Runa) · 11 [H] Oracle-built project: log-file analyser CLI
- Apprentice (13): 1 OOP · 2 Inheritance vs composition; dunders · 3 Dataclasses, enums — S: validation with pydantic first look · 4 Type hints, mypy · 5 [H] ruff/black, pre-commit — S: pre-commit with gitleaks and Bandit hooks · 6 Iterators, generators, context managers · 7 Decorators · 8 [H] httpx, REST — S: timeouts, TLS verification, SSRF · 9 [H] Logging, env config — S: redaction, log injection · 10 [H] pyproject packaging — S: pins, hashes, publishing · 11 Secure coding: validation, injection, secrets, deserialisation, standard crypto libraries · 12 [H] Oracle review: three scripts · 13 [H] Oracle-built project: typed, tested API-client library
- Journeyman (11), lenses applied: 1 Concurrency, GIL · 2 asyncio · 3 [H] FastAPI, pydantic, DI · 4 [H] SQL, SQLAlchemy, migrations · 5 [H] Testing strategy · 6 [H] Profiling · 7 SOLID, error architecture · 8 [H] Containerise the service (with Hedda) · 9 [H] numpy, pandas · 10 Auth: tokens, OAuth, password hashing · 11 [H] Project: secured, tested, containerised API
- Expert (8), lenses applied: 1 Architecture: services, queues, caching · 2 [H] Background jobs · 3 [H] Observability · 4 Internals for performance and memory · 5 [H] Data pipelines and model serving (with Fenna) · 6 [H] Library design, API stability · 7 [H] Teach a Novice unit · 8 [H] Audit legacy module
- Master: OUTLINE (production system, public defence)

### Linux/Bash — Runa Kettleby
- Novice (10): 1 OS, kernel, shell, terminal — S: root vs user; the kernel enforces permissions · 2 [H] pwd, ls, cd, paths — S: hidden files where secrets live (`~/.ssh`, dotfiles) · 3 [H] cp, mv, rm, mkdir, touch; globbing — S: `rm -rf` with variables and globs; umask on new files · 4 [H] cat, less, head, tail — S: logs contain secrets; why `/etc/shadow` needs root · 5 Users, groups, permissions; chmod/chown; sudo — S: least privilege, 600 and 700, sudo vs a root shell, setuid first look · 6 [H] nano, vim basics — S: editor swap and backup files leak secrets; sudoedit · 7 [H] Pipes and redirection — S: secrets in shell history and process arguments; `curl | bash` · 8 [H] grep, find, wc, sort, uniq — S: grep for leaked keys; find world-writable files · 9 Processes: ps, top, kill, signals — S: process arguments are visible to every user in `ps` · 10 [H] apt — S: trusted repositories, signed packages, unattended upgrades
- Beginner (6): 1 [H] Scripting: shebang, variables, quoting — S: quoting as injection defence · 2 [H] Conditionals, loops, functions · 3 [H] Exit codes; set -euo pipefail; traps — S: mktemp, cleanup · 4 [H] shellcheck · 5 Env vars, PATH, dotfiles — S: PATH hijack, secrets in env and history · 6 [H] Oracle-built project: backup script with logging, in git
- Apprentice (10): 1 [H] sed, awk, cut, tr, xargs · 2 [H] jq · 3 [H] ssh, keys, scp/rsync — S: sshd hardening, agent forwarding, known_hosts · 4 [H] systemd, journald — S: unit sandboxing options · 5 [H] cron, timers · 6 FHS, mounts, disks — S: mount options · 7 Operator networking: ip, ss, curl, dig — S: host firewall · 8 [H] Oracle review: three scripts · 9 [H] Oracle-built project: service under systemd · 10 [H] NEW Users and access: sudoers, auditd, file capabilities
- Journeyman (4), lenses applied: 1 [H] Troubleshoot live systems · 2 [H] Hardening · 3 [H] strace, lsof, iostat · 4 [H] Project: recover a broken and compromised server
- Expert: OUTLINE

### Git/Gerrit — Runa Kettleby
- Novice (5): COMPLETE.
- Beginner (T + 6): T [H] Top-up: secrets and identity in git; rotate first, then clean history; reading a diff; reviewing oracle commits; also revisits the ledger weak points (snapshot model, the three areas, diff variants, never `git add .` blindly) · 1 [H] Branches and switching · 2 [H] Merging and resolving conflicts · 3 [H] Remotes: GitHub, clone, push, pull · 4 [H] .gitignore; secrets out of history · 5 [H] Undoing: restore, reset, revert, and which is safe · 6 [H] Project: feature branch, conflict, merge, push, with an oracle that resolves a conflict wrongly for the player to catch. GATED: blocked until Cybersecurity Beginner.
- Apprentice (7): 1 Rebase vs merge; interactive rebase · 2 [T] Force-push and reflog recovery · 3 [H] Gerrit: change-ids, patch sets, +2/verify · 4 [H] PR review etiquette, including writing review findings with severity · 5 [H] Oracle review: commits and pull requests · 6 [H] Project: clean a messy branch · 7 [H] NEW Signed commits, protected branches, removing a leaked secret from history
- Journeyman (4), lenses applied: 1 [H] Internals: objects, refs, reflog · 2 [H] Hooks; signing policy and verification in CI · 3 Branching strategies; mono vs poly · 4 [H] Project: recover a broken repo
- Expert: OUTLINE

### Docker/Kubernetes — Hedda Stroud
- Novice (7): COMPLETE (passed by exam).
- Beginner (T + 8): T [H] Top-up: image trust and pinning by digest; the docker group and docker.sock are root; published ports bypass ufw and 0.0.0.0 exposure; --privileged; reading oracle docker commands · 1 [H] Dockerfile; layers, caching — S: secrets left in layers, ARG and ENV · 2 [H] build/tag/push — S: registry login, immutable tags · 3 [H] Volumes, bind mounts — S: host paths, read-only mounts, socket mounts · 4 [H] Networks — S: exposure, internal networks · 5 [H] Compose — S: env files, secrets, port binding, privileged and added capabilities · 6 Image size, base images, .dockerignore — S: minimal bases, attack surface, patch cadence · 7 [H] Env vs secrets; non-root — S: USER, read-only root filesystem, dropped capabilities · 8 [H] Oracle-built project: containerise your Python CLI. GATED: blocked until Cybersecurity Beginner.
- Apprentice (10): 1 [H] Multi-stage, healthchecks · 2 [H] Trivy; hadolint; triage · 3 K8s architecture — S: the API server as the perimeter · 4 [H] kind/k3d · 5 [H] kubectl: pods, deployments, services — S: kubeconfig handling, namespaces are a soft boundary · 6 [H] ConfigMaps, Secrets — S: base64 is not encryption; encryption at rest; external secret stores · 7 [H] Oracle review: Dockerfiles and manifests · 8 [H] dive/history — S: recovering secrets from layers · 9 Oracle-built practical · 10 [H] NEW Pod security context first look: non-root, read-only root filesystem, drop all capabilities, resource limits, Pod Security Standards
- Journeyman (8), lenses applied: 1 [H] Ingress, probes, limits · 2 [H] Helm · 3 [H] Rolling updates, rollback · 4 [H] Persistent volumes · 5 [H] Debug failing pods · 6 [H] GPU workloads · 7 [H] Project: deploy your FastAPI service · 8 [H] NEW RBAC, NetworkPolicy, Pod Security Admission (moved down from v2 Expert 1)
- Expert (4), lenses applied: 1 [H] Admission policy, runtime detection, image signature verification · 2 [H] Autoscaling · 3 [H] GitOps · 4 [H] Prometheus/Grafana

### IaC — Tamsin Oake
- Novice (7): 1 Declarative vs imperative; idempotence — S: idempotence and blast radius; drift from desired state · 2 YAML syntax — S: secrets do not belong in YAML · 3 [H] Pitfalls: Norway, indentation, tabs, quoting — S: parsing traps that silently change security settings (`enabled: no`, `on`) · 4 [H] yamllint — S: lint in CI; a linter does not check meaning · 5 [H] Read others' YAML: compose, workflow, playbook — S: spotting `privileged: true`, hardcoded secrets and 0.0.0.0 ports in others' YAML · 6 JSON vs YAML vs TOML — S: safe loaders (`yaml.safe_load`); JSON for untrusted input · 7 [H] Project: ward system in YAML, validated — S: validate against a schema; no secrets in the file
- Beginner (8): 1 Ansible concepts — S: the control node and its keys; become · 2 [H] Ad-hoc commands — S: modules over raw commands · 3 [H] Playbooks against local container/VM — S: check mode and diff before apply; limiting hosts · 4 [H] Variables, facts, Jinja2 — S: no_log, secrets in vars, template injection · 5 [H] Handlers · 6 [H] Idempotence test · 7 [H] Oracle-built project: configure and harden a server idempotently · 8 [H] NEW Ansible Vault and secret lookups first look (moved down from v2 Apprentice 1)
- Apprentice (9): 1 [H] Roles; trust and pinning of Galaxy roles and collections · 2 Terraform concepts — S: state holds secrets · 3 [H] init/plan/apply/destroy — S: reading the plan as a review; provider lock file · 4 [H] Variables, outputs, locals — S: sensitive values, tfvars out of git · 5 [H] Docker provider · 6 [H] Oracle review: playbooks and Terraform; ansible-lint · 7 [H] State drift — S: drift as a security signal · 8 Oracle-built practical · 9 [H] NEW Static checks first look: tflint, checkov; reading findings
- Journeyman (7), lenses applied: 1 [H] Modules · 2 [H] Remote state, locking · 3 [H] Drift detection · 4 [H] Terraform with Azure (with Calla) · 5 [H] validate, tflint, checkov, deepened to custom policy and CI gating · 6 [H] Policy as code · 7 [H] Project: full environment from code
- Expert: OUTLINE

### Azure — Calla Mirelle
- Novice (7): 1 Cloud concepts: IaaS/PaaS/SaaS, regions, availability, SLA, shared responsibility — S: what stays yours on IaaS, PaaS and SaaS · 2 Subscriptions, resource groups, tags — S: tags for ownership and accountability; resource groups as an RBAC scope · 3 Pricing, budgets; forgotten resources — S: a cost spike can mean a compromise (cryptomining) · 4 [H] Free account; budget alerts — S: MFA on the account; no shared logins · 5 [H] Azure CLI basics — S: `az login` token storage; never a password in a script; output can leak secrets · 6 Identity first look: tenant, account — S: MFA, guest accounts, who is in your tenant · 7 [H] Project: create, tag, cost-estimate, delete a resource group — S: deletion leaves nothing orphaned or exposed
- Beginner (8): 1 Entra ID — S: MFA, Conditional Access first look, break-glass accounts, guests · 2 RBAC and scope — S: least privilege, Owner vs Contributor, inheritance · 3 [H] Storage, blobs — S: public access off, SAS vs RBAC, key rotation · 4 [H] Small VM, then delete — S: no public SSH, Bastion or just-in-time access, patching · 5 [H] VNets, subnets, NSGs — S: default deny, flow logs · 6 [H] Monitor — S: activity log, diagnostic settings, alerts on role changes · 7 [H] Oracle-built project: secure static site · 8 [H] NEW Managed identities and Key Vault first look
- Apprentice (8): 1 [H] Key Vault in depth: access model, rotation, private access, workload identity · 2 [H] App Service / Container Apps — S: managed identity, ingress restriction, HTTPS only · 3 [H] ACR — S: admin user off, pull by identity, scanning · 4 [H] Log Analytics, KQL — S: sign-in and activity queries · 5 [H] Cost analysis · 6 [H] Oracle review: a deployment · 7 Oracle-built practical · 8 NEW Azure Policy and Defender for Cloud first look
- Journeyman (6), lenses applied: 1 [H] AKS · 2 [H] Azure OpenAI / AI Foundry · 3 [H] Deploy via Terraform · 4 Policy, Defender for Cloud, deepened to initiatives, compliance views and remediation · 5 Well-Architected · 6 [H] Project: secure AI-backed service
- Expert: OUTLINE

### AI — Fenna Lark
- Novice (6): COMPLETE.
- Beginner (T + 10): T Top-up: what data may be sent to a model; retention; local vs hosted; the review rubric applied; also revisits the ledger weak points (prompt template vs logic, delimiters, never label unchecked output "verified") · 1 [H] Call a local model from Python · 2 [H] Structured output: JSON, schemas — S: model output is untrusted input · 3 System prompts, few-shot — S: prompt injection first look; a system prompt is not a security boundary or a secret store · 4 [H] Chat CLI with history · 5 Costs and limits of hosted APIs — S: runaway cost; API key handling · 6 [H] Review three oracle-written scripts · 7 [H] Familiar Bond: grounded assistant · 8 Sycophancy, seeds/temperature, testing an oracle · 9 [H] NEW Working with a coding oracle I: task specification, context, acceptance checks, small diffs, tests first, the verify loop, when not to use it · 10 NEW Coding assistants and agents first look: completion vs chat vs agent; approval modes; rules files; what an agent can read. GATED: blocked until Cybersecurity Beginner.
- Apprentice (8): 1 Embeddings · 2 [H] Chunking · 3 [H] Vector store · 4 [H] RAG over your grimoire · 5 [H] Evaluation: groundedness, citations — S across 1–5: poisoned sources, access control on retrieval, embedding weaknesses, personal data · 6 [H] Oracle review: RAG pipelines · 7 [H] NEW Working with a coding oracle II: plan, implement, review workflows; generated tests and their traps; AI reviewers as a second pair of eyes; commit hygiene · 8 [H] NEW Tool use and MCP first look: tool calls, trusting MCP servers, tool poisoning, least privilege
- Journeyman (7), lenses applied: 1 Agents, tool use · 2 MCP · 3 [H] Write a safe MCP server · 4 [H] Permissions, sandboxing · 5 [H] Prompt-injection defence (with Zofia) · 6 [H] Eval harness · 7 [H] Project: grounded assistant with tools
- Expert (4), lenses applied: 1 [H] LoRA locally · 2 [H] Serving, scaling · 3 [H] Review AI code at scale · 4 AI governance

### CI/CD — Katla Rusk
- Novice (6): 1 Why automate; CI vs CD — S: a pipeline runs code with privileges on every push · 2 Pipelines, stages, jobs, artefacts, runners — S: runners hold credentials; artefacts can leak secrets · 3 [H] Read a workflow — S: read for echoed secrets, unpinned actions and broad permissions · 4 [H] First GitHub Actions workflow — S: `permissions: contents: read`; pin actions · 5 [H] Failed run: log, step, fix — S: debug logs leak secrets; redact logs before pasting them anywhere, including AI · 6 Pipeline hazards: secrets, latest, success masking, force flags (already a security unit)
- Beginner (7): 1 [H] Lint and test on push — S: least-privilege `permissions`, actions pinned by SHA · 2 [H] Matrix · 3 [H] Caching — S: cache poisoning, never cache secrets · 4 [H] Secrets in CI — S: limits of masking, environments, OIDC named, fork pull requests · 5 [H] PR status checks — S: required checks, the pull_request_target trap · 6 [H] Oracle-built project: CI for your Python project · 7 [H] NEW Security checks in CI first look: gitleaks, pip-audit, Bandit as jobs; fail vs warn
- Apprentice (6): 1 [H] Build and push images — S: OIDC to the registry, digests, provenance named · 2 [H] Security gates: triage, thresholds, reports · 3 [H] Branch protection — S: code owners, signed commits, no bypass · 4 [H] Oracle review: workflows · 5 Oracle-built practical · 6 [H] NEW Script injection and untrusted input in workflows; third-party actions
- Journeyman (6), lenses applied: 1 [H] Deploy · 2 Environments, approvals · 3 [H] Versioning, releases · 4 [H] Rollback · 5 [H] Self-hosted runner · 6 [H] Project: full delivery chain
- Expert: OUTLINE

## C. Unit format (summary; full procedure in 11_lesson_chat_instructions (latest))

- Flow: gate check and greeting → two downloadable note files (theory and index) → player reads outside the chat and says he is ready → scenario pack → three question batches → unit verdict → end-of-lesson steps.
- Theory lives in the files, not the chat. The chat holds only scenario data, questions, grades and comments.
- 11 questions per unit. Batch 1, items 1–4: recall and concepts (multiple choice, true/false with a reason of 8 words or fewer, matching). Batch 2, items 5–7: applied (predict output, spot the faulty line, pick a decision, order the steps), answered with a letter, a line number or one line. Batch 2, item 8: the O item (multiple choice). Batch 3, item 9: the S item (line number plus fix letter). Batch 3, item 10: the R item (verdict letter plus `line:tag` pairs). Batch 3, item 11: the interview line (2–3 sentences).
- Typing budget: 40 words or fewer per batch, except item 11 (60 words or fewer). At most one typed-code item per unit, never more than one line.
- R tags: B bug, S security, H hallucinated API/flag/package, M maintainability, T missing validation or test, P pinning or supply chain.
- Review rubric (every R item and review unit): 1 Does it do what was asked? 2 Does it run, and do the APIs, flags and packages exist? 3 Inputs and trust boundaries. 4 Secrets and permissions. 5 Dependencies and pinning. 6 Failure behaviour and tests. Answer: verdict (approve / request changes / reject), issues found, and what he would verify before merging. Introduced in Cybersecurity Novice 9; taught in full in Cybersecurity Beginner 11 and AI Beginner T.
- Unit verdict: Clean = no item Missed and at most 2 Rough. Rough = at most 2 Missed, neither of them item 9 or item 10. Otherwise one retry batch of fresh variants of the Missed items; if that does not reach Rough, the unit stays open.

## D. Exam blueprints

- Novice → Beginner: 11 items: 8 theory, 1 short code, 1 output prediction, 1 flawed review (at least 3 issues).
- Beginner → Apprentice: 13 items: 10 theory, 1 short code, 1 output prediction, 1 flawed review (at least 4 issues, at least 2 of them security issues, verdict required).
- Apprentice → Journeyman: 14 items: as Beginner → Apprentice, plus a design question with trade-offs and a short threat sketch.
- Journeyman → Expert and up: as Apprentice → Journeyman, plus one PC task with real pasted output. Expert and up add design defence; Master adds teaching; Grandmaster adds major project and public defence.

Rules for all exams:
- One item at a time, in character, wrapped in a dream-room scene. Free-form answers. Each item graded Clean, Rough or Missed. Keys are for the examiner; grade on the idea, not the wording.
- Theory items are phrased as interview questions, in an even mix of fact, scenario or incident, design or decision, and behavioural. A behavioural item still needs technical substance (for example, handling a colleague who wants to merge unreviewed oracle output).
- Composition of theory items, Beginner → Apprentice and up: about half on the subject, at least 3 security-applied (Cybersecurity at the gate level, applied to this subject), at least 2 on oracle practice.
- The flawed-review item is an oracle-written artefact.
- Every exam from Beginner → Apprentice up is written by the mentor at exam time to this blueprint, covering every unit including unit T. No keys are stored here.
- Verdicts: Strong pass = at least half the items Clean and none Missed. Pass = no more than 2 Missed, none of them the code item, the review item not Missed, and at most one security-applied item Missed. Anything else is Not yet. These apply to every exam, Novice → Beginner included.
- Familiar hints: 1 allowed at Novice–Apprentice; any hint caps the verdict at Pass.
- In the retained Novice → Beginner sets (section F), "security-applied" means any item whose key turns mainly on a security point (all items in the Cybersecurity sets).

## E. Migration notes (v2 → v3)

- All v2 ticks stand under the same unit numbers. Only Cybersecurity Novice 1 and 2 are ticked (both Rough).
- Course totals now read: Cybersecurity Novice 2/9; Git/Gerrit Beginner 0/7; AI Beginner 0/11; Docker/K8s Beginner 0/9; Python Novice 0/11; Linux/Bash Novice 0/10; IaC Novice 0/7; Azure Novice 0/7; CI/CD Novice 0/6.
- Gate status now: the Git/Gerrit, AI and Docker/K8s Beginner courses are BLOCKED until Cybersecurity reaches Beginner. No lesson chat may start them, or their exams, early. Spell tasks within current caps remain allowed.
- The five unstarted Novice courses (Python, Linux/Bash, IaC, Azure, CI/CD) keep their unit lists and are taught with the three lenses from the start. They need no unit T.
- Moved units (none ticked): Cybersecurity v2 Expert 1–2 → Journeyman 9; v2 Expert 3, 4, 5 → Expert 1, 2, 3. Docker v2 Expert 1 → Journeyman 8 (v3 Expert 1 is new content). IaC v2 Apprentice 1 vault part → Beginner 8.
- Exam sets: Novice → Beginner sets for Python, Linux/Bash, Docker/K8s, IaC, Azure and CI/CD are copied unchanged. Cybersecurity sets are copied with item 2 of each replaced by a unit 9 item. The v2 Git and AI Beginner → Apprentice sets are withdrawn.
- 11_lesson_chat_instructions_v1 is replaced by v2.

## F. Exam sets (Novice → Beginner, retained)

Copied from v2. Cybersecurity item 2 in each set replaced by a unit 9 item. Docker/K8s sets are kept for the record; that exam is already passed.

### Python Novice → Beginner (Isaura)

Set A
1. (u1) What is the difference between an interpreter and a compiler? What does CPython actually do with `graves.py`? — Key: CPython compiles source to bytecode (cached as .pyc in __pycache__) and the CPython VM runs it. It does not produce native machine code.
2. (u2) Why use a virtual environment? Give the commands to create and activate one and install `requests`. What is uv? — Key: it isolates each project's packages; `python3 -m venv .venv`, `source .venv/bin/activate`, `pip install requests`. uv is a fast installer and project manager (`uv venv`, `uv add`, `uv pip install`).
3. (u3) Give the type of `7`, `7.0`, `"7"`, `True`, `None`, and of `3 / 2`. — Key: int, float, str, bool, NoneType; `3 / 2` gives float 1.5.
4. (u4) Evaluate `7 // 2`, `7 % 2`, `2 ** 3`, `10 / 5`. Which names are valid: `2nd_grave`, `grave_count`, `class`, `_tmp`? — Key: 3, 1, 8, 2.0. `2nd_grave` is invalid (starts with a digit) and `class` is a keyword.
5. (u6) Which of these are falsy: `0`, `"0"`, `[]`, `" "`, `None`, `0.0`? What is the difference between `==` and `is`? — Key: 0, [], None, 0.0. `==` compares value; `is` compares identity (use it for None).
6. (u7) When do you pick `for` over `while`? What do `break` and `continue` do? What does `range(2, 10, 3)` produce? — Key: `for` iterates over a known sequence; `while` runs until a condition changes. 2, 5, 8.
7. (u8) Compare list and tuple: mutability, and when to choose each. — Key: lists are mutable; tuples are immutable, used for fixed records, hashable when their contents are, and good for unpacking.
8. (u10) The traceback ends `File "lab.py", line 4 ... TypeError: can only concatenate str (not "int") to str`. Where do you look, what is wrong, and how do you fix it? — Key: read from the bottom up, line 4; a str is being added to an int; use an f-string or `str()`.
9. Code (u5, u9, u11): write `to_feet(metres)` returning feet rounded to 1 decimal (1 m = 3.28084 ft), then loop over 1 to 3 printing `"2 m = 6.6 ft"`. — Key: `return round(m*3.28084, 1)`; `for m in range(1, 4): print(f"{m} m = {to_feet(m)} ft")`.
10. Predict (u5, u8):
```
s = "Thornwall"
print(s[0:5], s[-4:], s[::3])
words = ["spade", "lamp"]
words.append("rope")
print(len(words), words[-1].title())
```
— Key: `Thorn wall Tra` / `3 Rope`
11. Review (u7, u9) — find at least 3 issues:
```
def average(nums):
    total = 0
    for n in range(nums):
        total =+ n
    print(total / len(nums))

result = average([3, 4, 5])
if result = 4:
    print("ok")
```
— Key: `range(nums)` on a list raises TypeError (iterate over `nums`); `=+` should be `+=`; it prints instead of returning, so `result` is None; `=` in the `if` is a SyntaxError; an empty list causes ZeroDivisionError.

Set B
1. (u1) What is bytecode? Is Python "only interpreted"? Why does `__pycache__` appear? — Key: compiled instructions for the VM. It is compiled to bytecode and then interpreted; the cache speeds up later imports.
2. (u2) REPL vs `python3 script.py` vs `python3 -i script.py`. What does `pip freeze > requirements.txt` give you? — Key: interactive session; run and exit; run, then drop into the REPL. It records pinned versions so the environment can be reproduced.
3. (u3) Results: `int("12") + 3`, `"12" + "3"`, `float("2.5") * 2`, `bool("False")`. — Key: 15, "123", 5.0, True (any non-empty string is truthy).
4. (u4) Evaluate `2 + 3 * 4 ** 2`, `(2 + 3) * 4`, `17 % 5 == 2 and not False`. Which naming conventions do variables and constants follow? — Key: 50, 20, True. snake_case for variables, UPPER_CASE for constants.
5. (u6) This code labels every score above 50 as "pass", including 90: `if s >= 50: ... elif s >= 80: "merit"`. Why, and what is the fix? — Key: the first true branch wins; check the highest threshold first.
6. (u7) `n = 5; while n > 0: print(n)` never ends. Why, and how do you fix it? — Key: n never changes; add `n -= 1`.
7. (u8) What does `a, b = (1, 2)` do? `append` vs `extend`? After `b = a` with a list, what happens to `b` when you append to `a`? — Key: unpacking; append adds one item, extend adds each item; `b` changes too because both names point to the same list (aliasing).
8. (u9) Default and keyword arguments; `print` vs `return`; what a function returns without a `return`. — Key: `def f(x, y=2)`, `f(x=1)`; return hands back a value, print only displays it; None.
9. Code (u11): a number-guessing loop with `secret = 7`. Read input, convert to int, print "higher"/"lower", stop on a correct guess. ≤8 lines. — Key: `while True`, `int(input())`, compare, `break`.
10. Predict (u7, u9):
```
def f(x, y=2):
    return x * y
total = 0
for i in range(1, 4):
    if i == 2:
        continue
    total += f(i)
print(total, f(3, y=3), f"{total/4:.1f}")
```
— Key: `8 9 2.0`
11. Review (u5, u10) — what is raised first, and what else is wrong?
```
names = ["ada", "bram", "wim"]
for i in range(len(names) + 1):
    print("Grave " + i + ": " + names[i].capitalise())
```
— Key: TypeError first (str + int); `capitalise` should be `capitalize` (AttributeError); `+ 1` is an off-by-one (IndexError); use `enumerate` and an f-string.

### Linux/Bash Novice → Beginner (Runa)

Set A
1. (u1) Kernel vs shell vs terminal: one line each. — Key: the kernel manages hardware and processes; the shell interprets commands (bash); the terminal is the window or device that carries text to and from the shell.
2. (u2) Absolute vs relative path; what `.`, `..` and `~` mean. From `/home/flo/graves`, where does `cd ../../../etc` land? — Key: `/etc`.
3. (u3) With files `a.txt b.txt ab.log c1.log`: what do `*.txt`, `?.txt`, `[ab]*` and `c?.log` match? Why is `rm -r` dangerous? — Key: a.txt b.txt; a.txt b.txt; a.txt b.txt ab.log; c1.log. There is no undo or bin, and globs can expand wider than you meant.
4. (u4) When do you use `cat`, `less`, `head -n 5` and `tail -f`? — Key: dump a short file; page through a long one; first lines; follow a growing log.
5. (u5) Read `-rwxr-x--- flo graves run.sh`. What does `chmod 640` set? What do `chown` and `sudo` do? — Key: owner rwx, group r-x, others nothing. 640 = rw-r-----. chown changes owner/group; sudo runs a command as root, with your password, logged.
6. (u6) vim: enter insert mode, save and quit, quit without saving. How do you save in nano? — Key: `i`, `Esc :wq`, `:q!`; Ctrl+O, then Ctrl+X to exit.
7. (u7) What do `>`, `>>`, `|` and `2>` do? — Key: overwrite stdout to a file; append; pipe stdout into the next command's stdin; redirect stderr.
8. (u9) `ps aux`, `top`; `kill` vs `kill -9`; what Ctrl+C sends. — Key: snapshot vs live view; SIGTERM asks the process to exit cleanly, SIGKILL cannot be caught; Ctrl+C sends SIGINT.
9. Code (u7, u8): one pipeline that prints the 5 most frequent IPs (field 1) in `access.log`, with counts. — Key: `cut -d' ' -f1 access.log | sort | uniq -c | sort -rn | head -5` (awk is also fine). `uniq` needs sorted input.
10. Predict (u7, u8):
```
echo grave > a
echo spade >> a
echo lamp > a
wc -l < a
grep -c a a
```
— Key: `1` and `1` ("lamp" contains an a).
11. Review (u3, u5, u7, u10) — find at least 3 issues:
```
sudo apt upgrade
chmod 777 secrets.txt
grep error app.log > app.log
rm -rf / home/flo/tmp
```
— Key: run `apt update` first; 777 gives everyone write access to secrets (use 600); redirecting into the input file truncates it before grep reads it; the stray space makes rm target `/`.

Set B
1. (u1) What is an OS for? Name two shells. Why is "terminal" not the same as "shell"? — Key: it shares and protects hardware; bash and zsh; a terminal can host any shell.
2. (u2) What do `ls -la` and `pwd` show? From `/var/log`, what is the relative path to `/var/www`? — Key: long listing including hidden files; current directory; `../www`.
3. (u3) `cp -r src dst` vs `mv old new`; `mkdir -p a/b/c`; what `touch` does to an existing file. — Key: recursive copy; move or rename; create parents; update its timestamp.
4. (u4) Show lines 1–3, then the last 20, and how to search inside `less`. — Key: `head -n 3`, `tail -n 20`, `/pattern` then `n`.
5. (u5) A user is in group `diggers`; the file is `-rw-r----- root diggers log`. Can they read it? Write it? Give the command to add the user to a group. — Key: read yes, write no; `sudo usermod -aG diggers flo`.
6. (u6) In vim, how do you delete a line, undo, and search? Why do people get "stuck" in vim? — Key: `dd`, `u`, `/word`; it is modal, so they type in normal mode.
7. (u7) What does `cmd > out.txt 2>&1` do? What about `cmd 2>/dev/null`? — Key: both stdout and stderr go to the file; errors are discarded.
8. (u8) Find all `.md` files under home; count lines containing "TODO" across them. — Key: `find ~ -name '*.md'`; `grep -r TODO --include='*.md' ~ | wc -l` (or `grep -c` per file).
9. Code (u10, u7): install `htop` properly and save the list of installed packages to `pkgs.txt`. — Key: `sudo apt update && sudo apt install htop`; `apt list --installed > pkgs.txt` (or dpkg -l).
10. Predict (u3, u8): with files `x1.log x2.log y.txt`:
```
ls *.log | wc -l
echo *.txt
printf "b\na\nb\n" | sort | uniq
```
— Key: `2` / `y.txt` / `a` and `b` on separate lines.
11. Review (u9, u5, u7) — find at least 3 issues:
```
kill -9 1
sudo chown root ~/notes.txt
cat big.log | grep ERR | sort | uniq | wc
ps aux | grep python | kill
```
— Key: PID 1 is init/systemd, so -9 on it is fatal; giving your own file to root locks you out of it; useless `cat` and `uniq -c` is probably what was wanted, and `wc` without `-l`; `kill` does not read PIDs from stdin (use `pkill python` or `pgrep`).

### Cybersecurity Novice → Beginner (Zofia)

Set A
1. (u1) Ransomware encrypts the guild archive and the attackers threaten to publish it. Which CIA corners are hit, and how? — Key: availability (locked), confidentiality (leak), integrity (data changed, and nothing is trusted after the breach).
2. (u9) A colleague pastes a failing script into a public chatbot. The script contains a database connection string. The bot's fix says to run `pip install requets-helper`. Name two problems and what to do about each. — Key: The secret has been disclosed to a third party, so rotate it now and use an approved tool with redaction in future. The suggested package may be hallucinated or typosquatted (note the spelling), so check that it exists, who publishes it and whether it is needed, and prefer the known library (`requests`).
3. (u2) Name the actor and motive: a mass "account locked" text; a defaced guild page reading "Free Brackenford"; a clerk who emails the roster to the wrong person. — Key: opportunistic criminal, money; hacktivist, attention; careless insider, a mistake with no motive.
4. (u3) What is credential stuffing, and why does password reuse make it work? Give two defences. — Key: leaked username/password pairs tried on other sites. Defences: unique passwords, MFA, rate limiting, breached-password checks.
5. (u4) Hashing vs encryption for stored passwords. Why salt? Why a slow hash (bcrypt/argon2)? — Key: a hash is one-way and encryption is reversible; a salt defeats rainbow tables and identical-hash matching; slow hashing makes brute force expensive.
6. (u6) What does DNS do? Why is HTTPS port 443 and HTTP 80? TCP vs UDP in one line each. — Key: names to IPs; those are the default ports; TCP is reliable, ordered and connection-based, UDP is connectionless and fast (DNS, video).
7. (u7) Symmetric vs asymmetric encryption. What does TLS use each one for? — Key: one shared key vs a public/private pair. TLS uses asymmetric crypto to authenticate (certificate) and agree a key, then symmetric crypto for the bulk data.
8. (u8) `ss -tulpn` shows `0.0.0.0:5432` and `127.0.0.1:8000`. Which is exposed and what is it? What does `nmap localhost` add? — Key: 5432 is Postgres listening on all interfaces, so it is exposed; 8000 is local only. nmap shows what answers from a client's point of view.
9. Code (u5): write the `.env`, the `.gitignore` line, and Python that reads `DB_PASS` from the environment. — Key: `DB_PASS=...`; `.env` in .gitignore; `os.environ["DB_PASS"]` or `os.getenv`; commit a `.env.example` instead.
10. Predict (u5): `git status` after creating `.env` when `.gitignore` already contains `.env`, but `.env` was committed last week. — Key: it is still tracked, so changes appear as modified. The ignore rule only affects untracked files: `git rm --cached .env`, and rotate the secret.
11. Review (u3, u4, u5, u7) — find at least 3 issues in this login design: passwords stored as MD5 without salt; API key hardcoded in `app.py`; login over `http://`; unlimited attempts; same admin password on three servers. — Key: weak, unsalted, fast hash; secret in code; plaintext transport; no rate limiting or lockout (stuffing); reuse widens the blast radius. Add MFA.

Set B
1. (u1) Give an example of each CIA corner from Florence's graveyard register. Then: "we keep one backup on the same disk." What is wrong? — Key: any sensible examples; the backup shares a failure point with the original, so keep it offline or immutable.
2. (u9) Under a typical company policy, which of these may go into a hosted AI assistant? (a) a snippet from public documentation, (b) a list of customer email addresses, (c) a stack trace containing a token, (d) your own function with names anonymised. Then say why AI output is treated as untrusted. — Key: (a) yes; (d) yes if policy allows internal code; (b) no, it is personal data; (c) no, redact it, and rotate the token if it was already sent. AI output can be wrong, insecure by default, or invented (APIs, flags, packages), so it is reviewed and tested like a stranger's code.
3. (u2) Motive vs technique: give one motive and one technique for a nation-state actor and for a disgruntled insider. — Key: espionage, persistent intrusion; revenge, data theft or sabotage using existing access.
4. (u3) Phishing vs spear-phishing. What does malware do after a user runs an attachment? Name two red flags. — Key: mass vs targeted; persistence, theft, encryption; urgency, a mismatched sender or link.
5. (u4) Why use a password manager? What makes a strong password? Rank SMS, TOTP and hardware keys for MFA. — Key: unique random passwords for everything; length beats symbols; hardware key > TOTP > SMS.
6. (u6) What are an IP address and a port? What happens step by step when you open `https://guild.example`? — Key: host address and service endpoint; DNS lookup, TCP connect to 443, TLS handshake, HTTP request.
7. (u7) What does a certificate prove, and who vouches for it? What does a browser warning mean? — Key: that the server owns the name; a certificate authority; the chain failed or the name didn't match, so the connection may be intercepted.
8. (u8) Why scan only your own machine? Which `nmap` command lists open TCP ports on localhost, and what next if you find an unknown one? — Key: legality and consent; `nmap localhost` (or `-p-`); identify it with `ss -tulpn`, then stop it or firewall it.
9. Code (u5): write a `.gitignore` covering `.env`, `*.key`, `__pycache__/` and `secrets/`, plus a one-line check that nothing secret is staged. — Key: four lines; `git status` or `git diff --staged --name-only`.
10. Predict (u6): `dig guild.example +short` returns `203.0.113.7`; `curl -I http://guild.example` returns `301 Location: https://...`. What does each tell you? — Key: the A record IP; the site redirects HTTP to HTTPS.
11. Review (u5, u6, u7, u8) — find at least 3 issues: "We push `.env` to a private repo, it's private so it's fine; SSH is open on 0.0.0.0:22 with password login; we use a self-signed certificate and tell users to click through warnings; we encrypt backups and keep the key in the same bucket." — Key: private repos leak and history is permanent; password SSH should use keys only, or be limited; click-through trains users to accept MITM; the key next to the data defeats the encryption (custody).

### Docker/K8s Novice → Beginner (Hedda)

Set A
1. (u1) Containers vs VMs: kernel, isolation mechanisms, start time. — Key: containers share the host kernel and are isolated by namespaces and cgroups; VMs run a full guest OS on a hypervisor; seconds vs minutes.
2. (u1) Image vs container. One image, three containers; a file is written in container 2. Who has it? — Key: only container 2, in its writable layer. The image is read-only.
3. (u2) What does installing Docker give you (engine/daemon, CLI)? How do you check it works without sudo? — Key: dockerd and the docker CLI; add the user to the `docker` group (root-equivalent!); `docker run hello-world`.
4. (u3) `docker ps` vs `docker ps -a`; `stop` vs `rm`; reading logs and following them. — Key: running vs all; stop halts it, rm deletes it; `docker logs -f`.
5. (u4) What is a tag? Why isn't `latest` a version? What makes a pull reproducible? — Key: a movable label; `latest` is just the default name and moves; pin a version tag or digest (`@sha256:`).
6. (u5) What is a registry? What does `ghcr.io/hedda/stable:2.1` break down into? Public vs private. — Key: storage for images; registry host / namespace / repository : tag; private needs `docker login`.
7. (u6) What does `-p 8080:80` mean? Why might `localhost:80` show nothing? — Key: host 8080 maps to container 80; you mapped 8080, not 80.
8. (u7) The web container runs but the browser can't reach it. List three things to check. — Key: port mapping, the app listening on 0.0.0.0 rather than 127.0.0.1 inside the container, logs, host firewall, the right URL and port.
9. Code (u3, u6, u7): commands to run nginx 1.27 detached, named `stall`, on host port 8080; check it; open a shell inside it; remove it. — Key: `docker run -d --name stall -p 8080:80 nginx:1.27`; `docker ps` / `curl localhost:8080`; `docker exec -it stall sh`; `docker rm -f stall`.
10. Predict (u3) (simulated):
```
docker run --name t alpine echo hi
docker ps
docker ps -a --format '{{.Names}} {{.Status}}'
```
— Key: prints `hi`; `docker ps` shows no row for t; `t Exited (0) ...`
11. Review (u3, u4, u6) — find at least 3 issues:
```
docker run nginx:latest -p 80:8080
docker exec stall bash
docker rm stall
```
— Key: options after the image are passed to the container, so `-p` is ignored; the mapping is backwards for nginx (80:80 or 8080:80); `latest` isn't pinned; no `--name stall`, so exec targets nothing; the nginx image may lack bash (`sh`), and needs `-it`; rm on a running container fails without `-f` or a stop first.

Set B
1. (u1) Why does "works on my machine" go away with containers? What *doesn't* a container package? — Key: the image ships the userland and dependencies; it does not ship the kernel, hardware or host configuration.
2. (u1) What is an image layer? What happens to a container's data when it is removed? — Key: read-only filesystem diffs stacked together; the writable layer is lost unless you use a volume.
3. (u2) Docker Desktop vs Docker Engine. Why is being in the `docker` group a security matter? — Key: VM-backed GUI bundle vs native Linux daemon; the group is effectively root.
4. (u3) How do you run a command in a running container vs start a new one? What does `--rm` do? — Key: `exec` vs `run`; the container is auto-removed when it exits.
5. (u4) What do `docker image inspect` and `docker history` show? What is a digest? — Key: config, env, entrypoint and layers; how the layers were built; an immutable content hash.
6. (u5) Docker Hub "official image" vs a random user image. What risk comes with pulling unknown images? — Key: curated and maintained vs untrusted; malware, cryptominers, stale CVEs.
7. (u6) Two containers both want port 80 on the host. What happens, and what is the fix? — Key: the second fails because the port is already allocated; map different host ports.
8. (u7) In your web-server project, how do you prove you reached the container and not something else on the host? — Key: check the logs for the request, a custom page, `docker port`, curl the headers.
9. Code (u4, u5): pull `httpd` at a pinned version, list your images, show its exposed port and default command. — Key: `docker pull httpd:2.4`; `docker images`; `docker image inspect httpd:2.4` (ExposedPorts, Cmd).
10. Predict (u6) (simulated): after `docker run -d -p 127.0.0.1:9000:80 nginx:1.27`, which of these answer: `curl localhost:9000`, a curl from another machine to the host's LAN IP on 9000, and `curl localhost:80`? — Key: yes; no (bound to loopback); no.
11. Review (u3, u4, u5, u7) — find at least 3 issues in this note: "Pull `someuser/nginx-fast:latest`, run it with `docker run -d nginx-fast`, check it with `docker ps -a` showing Exited (1) — fine, it's started. Data written inside the container is our database." — Key: untrusted image; unpinned tag; wrong image name (the namespace is missing); Exited (1) means it crashed, so check the logs; data in the container layer dies with the container.

### IaC Novice → Beginner (Tamsin)

Set A
1. (u1) Declarative vs imperative. What is idempotence, and how do you test it? — Key: describe the end state vs list the steps; repeated runs give the same result; run it twice and expect no changes.
2. (u2) Write the YAML for a mapping with a list and a multiline string. What do `|` and `>` do? — Key: `|` keeps newlines, `>` folds them into spaces.
3. (u2) What are anchors and aliases (`&base`, `*base`, `<<:`)? Why be careful with them? — Key: reuse a block; merge keys are YAML 1.1 and not every parser supports them; they hide where values come from.
4. (u3) The Norway problem. What do `country: NO`, `version: 1.10` and `time: 22:30` parse as in YAML 1.1? — Key: false; 1.1 (a float); 81000 (sexagesimal). Quote them.
5. (u3) Tabs vs spaces in YAML; two indentation bugs. — Key: tabs are forbidden; misaligned list items and inconsistent nesting change the structure without an error.
6. (u4) What does yamllint catch that a parser doesn't? How do you configure it? — Key: style, duplicate keys, truthy values, line length; a `.yamllint` file.
7. (u5) In a compose file, what are `services`, `image`, `ports` and `volumes`? In a GitHub workflow, what are `on` and `jobs`? — Key: brief, correct roles.
8. (u6) JSON vs YAML vs TOML: one strength each, and where you see them. — Key: JSON is strict and suited to machines/APIs; YAML is readable config (k8s, CI); TOML is explicit types (pyproject).
9. Code (u7): YAML for a ward system: two wards, each with name, strength (int), runes (list) and an active flag. — Key: valid structure, real booleans, consistent indentation.
10. Predict (u2, u3):
```
a: yes
b: "yes"
c: 010
d: ~
e: [1, two, 3.0]
```
What does each value parse as (YAML 1.1 loader)? — Key: true; "yes" string; 8 (octal) in 1.1; null; [1, "two", 3.0].
11. Review (u3, u4, u5) — find at least 3 issues:
```
wards:
	- name: north
    strength: "9"
  - name: NO
    active: Yes
    active: no
```
— Key: tab character; misaligned list/key indentation; strength quoted as a string; `NO`/`Yes`/`no` parse as booleans; duplicate key `active`.

Set B
1. (u1) Is `mkdir graves` idempotent? Is `mkdir -p graves`? Is `echo x >> file`? — Key: no; yes; no.
2. (u2) Scalars: give examples of string, int, float, bool, null and date in YAML. — Key: correct examples.
3. (u2) Flow vs block style, using the same list written both ways. — Key: `[a, b]` vs dashes.
4. (u3) When must you quote in YAML? Give three cases. — Key: leading `*`, `&`, `@` or `:`; values like yes/no/on/off; leading zeros; a colon-space inside a string; `#`.
5. (u4) yamllint reports `truthy value should be one of [false, true]`. What does it mean and how do you fix it? — Key: a yes/on-style value; use true/false, or quote it if a string was meant.
6. (u5) Read an Ansible task: `- name: install nginx / ansible.builtin.apt: name=nginx state=present`. What does `state=present` express? — Key: the desired state (declarative), so it is idempotent.
7. (u6) Convert `{"name": "north", "runes": ["ash", "oak"]}` to YAML and TOML. — Key: correct forms.
8. (u7) How did you validate your ward file, and what's the difference between "valid YAML" and "valid ward system"? — Key: yamllint or a parser vs a schema/semantic check.
9. Code (u2, u5): a compose snippet for one service `stable` using `nginx:1.27`, port 8080:80, and a volume `./html:/usr/share/nginx/html:ro`. — Key: correct nesting; quote the ports.
10. Predict (u2): a block using `&defaults {strength: 3, active: true}` and a ward with `<<: *defaults` plus `strength: 5`. Give the resulting ward. — Key: strength 5, active true (local keys override the merged ones).
11. Review (u1, u3, u5) — find at least 3 issues: a workflow with `on: push` written as `on: yes`, `runs-on: ubuntu-latest` indented under steps, `version: 3.10` unquoted, and a shell step that appends to a file on each run. — Key: `on` key confusion and a boolean value; wrong nesting; 3.10 parses as 3.1; non-idempotent append.

### Azure Novice → Beginner (Calla)

Set A
1. (u1) Classify IaaS/PaaS/SaaS: VM, App Service, Microsoft 365. Under shared responsibility, who patches the VM's OS? — Key: IaaS, PaaS, SaaS; you do.
2. (u1) Region vs availability zone. What does a 99.9% SLA allow per month, roughly? — Key: geography vs separate datacentres within a region; about 43 minutes.
3. (u2) Hierarchy: tenant, subscription, resource group, resource. Why tag? — Key: nesting and scope; cost tracking, ownership, automation.
4. (u3) Name three ways an unattended resource keeps billing you. — Key: a stopped-but-not-deallocated VM, disks, public IPs, storage, logs.
5. (u4) What does a budget alert do, and what doesn't it do? — Key: it notifies at thresholds; it does NOT stop spending by itself.
6. (u5) `az login`, `az account show`, `az account set`, `az group list -o table`: what does each do? — Key: brief, correct.
7. (u6) Tenant vs subscription vs account. Can one account access several tenants? — Key: identity directory vs billing/resource container vs user identity; yes.
8. (u7) Why delete the resource group rather than the resources one by one? — Key: everything goes in one action and nothing is orphaned.
9. Code (u5, u7): CLI to create `rg-ward-dev` in westeurope with tags `owner=florence env=dev`, list it, then delete it without a prompt. — Key: `az group create -n rg-ward-dev -l westeurope --tags owner=florence env=dev`; `az group show`/`list`; `az group delete -n rg-ward-dev --yes --no-wait`.
10. Predict (u5) (simulated): `az group list --query "[].name" -o tsv` with two groups. — Key: two names, one per line, without quotes.
11. Review (u2, u3, u4, u7) — find at least 3 issues: "Everything goes in one resource group called `stuff`, no tags; the budget alert is set at 100% only; the VM was 'stopped' from inside the OS; the free credit means we can't be charged." — Key: no organisation or tags; alerts too late (add 50/80%); an OS shutdown still bills, so deallocate; once credit ends or the account is upgraded, pay-as-you-go charges apply.

Set B
1. (u1) Give an example of horizontal vs vertical scaling and say why the cloud makes it cheap to try. — Key: more instances vs a bigger one; pay as you go.
2. (u1) Availability set vs zone vs region pair: what each one protects against. — Key: rack failure; datacentre failure; regional disaster.
3. (u2) What can you NOT do with resource groups (nesting)? Which tag naming scheme do you prefer, and why? — Key: groups cannot nest; any consistent scheme, enforceable with policy.
4. (u3) Name the Pricing calculator vs Cost Management, and one cost trap of egress. — Key: estimate before vs track after; data leaving Azure is charged.
5. (u4) Which free-account limits matter, and what happens after 30 days or when the credit runs out? — Key: credit plus 12 months of some free services; resources are disabled unless you upgrade.
6. (u5) How do you change the output format, and why use `--query`? — Key: `-o table/json/tsv`; JMESPath filtering.
7. (u6) What is Entra ID's role in a first login? Personal vs work accounts. — Key: it authenticates identities for the tenant; Microsoft account vs organisational account.
8. (u7) How do you cost-estimate a resource group before creating anything? — Key: Pricing calculator with SKU/region/hours.
9. Code (u5): CLI to add tag `cost=low` to an existing group without erasing other tags, then show its tags. — Key: `az group update -n X --set tags.cost=low` (or `az tag update --operation merge`); `az group show --query tags`.
10. Predict (u2, u7): you delete `rg-a`, which holds a VM whose disk lives in `rg-b`. What remains billing? — Key: the disk in rg-b.
11. Review (u1, u3, u5, u6) — find at least 3 issues: "We're on PaaS, so security is all Microsoft's job; we left a dev VM running all weekend 'just in case'; scripts call `az login` with a password hardcoded; a single region is fine for our 99.99% promise." — Key: shared responsibility still covers your code, data and access; idle cost (auto-shutdown); a credential in the script (use a service principal or managed identity); a single region can't back that SLA.

### CI/CD Novice → Beginner (Katla)

Set A
1. (u1) CI vs continuous delivery vs continuous deployment. — Key: integrate and test every change; always releasable, with a manual gate; automatic to production.
2. (u2) Define pipeline, stage, job, step, artefact and runner. — Key: brief, correct.
3. (u2) Why do jobs not share files unless you pass artefacts? — Key: each runs on a fresh runner/VM.
4. (u3) In a workflow, what do `on: [push, pull_request]`, `runs-on`, `uses` and `run` mean? — Key: triggers; runner image; a reusable action; a shell command.
5. (u5) A run fails. How do you find the failing step, and what's the first thing to read? — Key: open the run, find the red step, read the first error rather than the last line.
6. (u6) What is success masking? Give two examples. — Key: `|| true`, `continue-on-error`, a test command whose exit code is ignored.
7. (u6) Why are `latest` tags and force flags hazards in pipelines? — Key: builds aren't reproducible; history or safety checks get destroyed.
8. (u6) Where should secrets live, and what must you never do with them in logs? — Key: repo/environment secrets; never echo or print them, and be careful with debug logging.
9. Code (u4): a workflow that runs on push, checks out the code, sets up Python 3.12 and runs `python -m pytest`. — Key: on/jobs/runs-on/steps with checkout@v4, setup-python@v5 `python-version: "3.12"`, run pytest.
10. Predict (u5) (simulated): a step runs `pytest || echo "tests done"` and tests fail. Is the step red or green, and why? — Key: green; echo's exit 0 masks the failure.
11. Review (u3, u4, u6) — find at least 3 issues:
```
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo ${{ secrets.TOKEN }}
      - run: pip install -r requirements.txt
      - run: pytest || true
      - run: git push --force
```
— Key: echoing the secret; no checkout step; no Python setup or version pinning; `|| true` masks failures; force-push from CI.

Set B
1. (u1) Why automate checks you could run by hand? — Key: people forget; it's consistent and fast feedback, and the loom remembers.
2. (u2) Hosted vs self-hosted runners: one advantage and one risk each. — Key: clean and managed vs custom hardware but a persistence/security risk.
3. (u2) What is an artefact used for between jobs and after a run? — Key: passing build outputs along; downloads and records.
4. (u3) What is the difference between `on: push` with `branches: [main]` and `on: pull_request`? — Key: post-merge pushes to main vs proposed changes.
5. (u4) Where does a workflow file live, and why must it be valid YAML? — Key: `.github/workflows/*.yml`; otherwise it never runs.
6. (u5) A step shows `ModuleNotFoundError: requests`. Diagnose it and give the fix. — Key: dependencies were never installed; add an install step or check requirements.txt.
7. (u6) What does `actions/checkout@main` risk compared with `@v4` or a SHA? — Key: unpinned upstream changes; supply-chain risk.
8. (u6) Give an example of a force flag in CI, and say what it can destroy. — Key: `git push -f`, `docker rm -f`, `--force` deploy; history or running services.
9. Code (u4, u5): add a job step that runs `ruff check .` and makes the job fail on lint errors. — Key: install ruff, `run: ruff check .`; no masking.
10. Predict (u3): with `on: pull_request: branches: [main]`, does a push to a feature branch with no PR trigger it? Does opening a PR into main? — Key: no; yes.
11. Review (u2, u3, u6) — find at least 3 issues: two jobs where `test` reads `dist/` that `build` created, with no `needs` and no artefact; a `continue-on-error: true` on tests; image pushed as `:latest` only; a token in `env:` printed with `set -x`. — Key: missing `needs` and artefact upload/download; failures masked; unversioned tag; the secret leaks through the trace.

END OF CURRICULUM V4
