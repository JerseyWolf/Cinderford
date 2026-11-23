# curriculum-p4

SOURCE: 04_curriculum_v4.md | version=4 | bytes=63617 | sha256=83ae10974c91182b | part 4 of 5 | page_bytes=12733

````text
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
````

===== END PAGE: 04_curriculum_v4.md | part 4 of 5 =====
