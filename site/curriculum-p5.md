# curriculum-p5

SOURCE: 04_curriculum_v4.md | version=4 | bytes=63617 | sha256=83ae10974c91182b | part 5 of 5 | page_bytes=12551

````text
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
````

===== END FILE: 04_curriculum_v4.md =====
