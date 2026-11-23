# curriculum-p3

SOURCE: 04_curriculum_v4.md | version=4 | bytes=63617 | sha256=83ae10974c91182b | part 3 of 5 | page_bytes=12929

````text
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
````

===== END PAGE: 04_curriculum_v4.md | part 3 of 5 =====
