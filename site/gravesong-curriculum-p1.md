# gravesong-curriculum-p1

SOURCE: 04b_gravesong_curriculum_v1_p1.md | version=- | bytes=5496 | sha256=2d080c2cc1a42727 | page_bytes=5496

````text
04b_GRAVESONG_CURRICULUM v1 - part 1 of 2: purpose, rules, courses. Created in planning 21 Nov 2026 (player rulings Q37, Q51, Q53). SHARED-CORE CANDIDATE: Dunmarrow-only until the player syncs it to Thornwall (Q71); in Thornwall the examiner would be the chorus, here Sable Nyx'ari. Everything in 04_curriculum v4 sections A, C and D (rules, unit format, exam blueprints, verdicts) applies unchanged; this file only adds the Gravesong course and its Novice exam sets. No tables.

PURPOSE
Gravesong is the subject for the DevOps knowledge the other nine courses do not cover: networking, web servers and reverse proxies, firewalls and tunnels, observability, and site reliability practice. Like every course it is interview preparation first, security-led, with the three lenses S, R, O on every unit.

RULES
- Gate: Novice always open. The Beginner course needs Cybersecurity Beginner (Dunmarrow gate; Thornwall's gate gives the same answer at this rank).
- Overlap with Cybersecurity Novice 6 (networking) and 7 (encryption): Gravesong assumes nothing from them but must not re-teach them as security topics. It teaches how the thing works and how to operate it; Cybersecurity teaches how it is attacked. Where a unit touches the same ground, the S item goes one step further.
- Linux/Bash Novice is assumed for commands (the ledger shows it passed). Python appears only at Novice level in snippets.
- [H] units before Journeyman are taught with commands and simulated output in chat. No PC required.
- Spells: Speak, Sleeper (raw socket HTTP), Grave-Tithe (nginx reverse proxy), Haunt (UDP heartbeat over a tunnel). Their real tasks sit inside units 6, 7 and 9-10.

### Gravesong - Sable Nyx'ari (Dunmarrow) / the chorus (Thornwall)
- Novice (12):
1 [T] Network models: OSI and TCP/IP layers, encapsulation, what a packet, frame and segment are - S: which layer each common attack lives on; "it's behind the firewall" is not a control.
2 [H] IPv4 addressing: CIDR, subnet masks, private ranges (RFC 1918), loopback, NAT and port forwarding; IPv6 first look; ip addr, ip route - S: private is not safe; a port forward or a 0.0.0.0/0 rule is exposure.
3 [H] DNS in practice: resolution path, record types (A, AAAA, CNAME, MX, TXT, NS, PTR), TTL and caching, /etc/hosts, dig and nslookup - S: dangling CNAMEs and subdomain takeover; DNS as a data-leak channel.
4 [H] HTTP for operators: methods, status codes, headers, keep-alive, HTTP/1.1 vs HTTP/2 first look, curl -v and -I - S: headers that leak (Server, X-Powered-By); security headers first look (HSTS, CSP named).
5 [H] TLS for operators: certificate chains, SAN, expiry, ACME and Let's Encrypt, openssl s_client, certificate renewal - S: curl -k and verify=False as incidents; private keys and their permissions.
6 [H] Sockets by hand: TCP handshake, UDP, ports, listening vs connected, nc, Python socket, ss -tulpn - S: binding 0.0.0.0 vs 127.0.0.1; services nobody meant to expose.
7 [H] Web servers and reverse proxies: nginx server and location blocks, proxy_pass, upstream, Host and X-Forwarded-For, nginx -t, reload vs restart; load balancing first look (round robin, health checks) - S: trusting client-supplied X-Forwarded-For; open proxies; default server catching stray hosts.
8 [H] Firewalls: stateful filtering, default deny, ufw and nftables basics, inbound vs egress, cloud security groups named - S: default-deny inbound, allowlisted egress; why "disable the firewall" is never the fix.
9 [H] SSH and tunnels: key auth, ssh config, local and remote port forwarding, jump hosts; WireGuard first look - S: key-only login, no root login, agent forwarding risk, tunnel as an unreviewed hole.
10 [H] Observability first look: logs, metrics, traces; journalctl; Prometheus pull model, exporters, a PromQL rate(); Grafana named; the four golden signals (latency, traffic, errors, saturation); heartbeats and dead-man's switches - S: logs leak secrets; exposed /metrics and dashboards.
11 [T] SRE first look: SLI, SLO, SLA, error budgets; toil; on-call; incident roles (commander, comms, ops); blameless postmortems - S: a security incident inside an outage; who may be told what.
12 [H] Project, troubleshooting: "the site is down". Method from the bottom up: link, IP, route, DNS, port, TLS, HTTP, app; ping, traceroute or mtr, dig, ss, curl, logs; a written incident note - S: oracle-suggested fixes that widen exposure (open the port to all, turn off TLS checks).
- Beginner (11) - OUTLINE awaiting player approval: 1 Subnetting and routing in depth; VLANs and VPCs · 2 [H] Load balancers: HAProxy and nginx, L4 vs L7, sticky sessions, health checks · 3 [H] Rate limiting, caching, CDNs · 4 [H] TLS termination, mTLS between services · 5 [H] WireGuard and site-to-site VPN design · 6 [H] Prometheus: exporters, recording and alerting rules, Alertmanager · 7 [H] Grafana dashboards; Loki and log pipelines · 8 [H] OpenTelemetry tracing first look · 9 SLO design and alert fatigue · 10 [H] Incident drill with postmortem · 11 [H] Oracle-built project: a monitored, proxied, firewalled service.
- Apprentice and up: OUTLINE (service mesh, eBPF and network observability, capacity planning, chaos engineering, multi-region DNS and failover, SRE practice at scale).

LEDGER LINE TO ADD at the next lesson chat that teaches Gravesong: "Gravesong: Novice · base 20 · Novice course 0/12 (04b_gravesong_curriculum v1) · examiner: Sable (Dunmarrow) / the chorus (Thornwall)".
END OF PART 1 OF 2 - 04b_GRAVESONG_CURRICULUM v1
````

===== END FILE: 04b_gravesong_curriculum_v1_p1.md =====
