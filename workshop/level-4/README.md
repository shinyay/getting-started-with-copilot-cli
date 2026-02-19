# Level 4: Create — Make Your First Changes

> **Risk level:** 🟡 Low — You will modify files for the first time. All changes are to workshop sample code and can be reverted with `git checkout`.

## Learning Objectives

By the end of this level, you will be able to:

1. Approve write operations through Copilot's tool approval flow
2. Distinguish between read tools and write tools in approval prompts
3. Create new files from scratch with Copilot
4. Use `/diff` to see exactly what changed in your working directory
5. Use `/review` for AI-powered pre-commit self-review
6. Cross-check Copilot's changes with `!git diff`
7. Fix real bugs by approving Copilot's edits
8. Make incremental edits to the same file across multiple turns
9. Revert unwanted changes using git
10. Execute the complete plan → implement → diff → review cycle
11. Use session-scoped auto-approval effectively and safely
12. Build confidence in the Copilot write workflow

---

## Prerequisites

- [ ] Completed **Levels 1–3** (UI navigation, code understanding, planning)
- [ ] Comfortable with `/plan`, `@`, `!`, `/diff`, `/review`
- [ ] The Level 3 planning exercises are fresh in your mind

---

## About the Sample App

Level 4 uses an **identical copy** of the Level 3 Quick Notes app. The difference: **you will actually modify these files.**

```
sample-app/
├── notes.py        ← CLI entry (bugs: no pinned sort, edit validation bypass)
├── storage.py      ← JSON storage (bugs: no JSON error handling, no thread safety)
├── models.py       ← Note model (bug: tags not normalized)
├── search.py       ← Search (bug: case-sensitive)
├── export.py       ← Export (bugs: XSS, no <br> for newlines)
├── config.py       ← Configuration
└── requirements.txt
```

### Safety Net

If anything goes wrong, reset all changes:

```bash
git checkout -- workshop/level-4/sample-app/
```

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **60–90 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Creating a New File | 5 min |
| 2 | The Approval Flow Deep Dive | 7 min |
| 3 | Your First `/diff` | 5 min |
| 4 | Your First `/review` | 5 min |
| 5 | Fix Bug #1 — Case-Sensitive Search | 7 min |
| 6 | Fix Bug #2 — Tag Normalization | 7 min |
| 7 | Fix Bug #3 — XSS Vulnerability | 7 min |
| 8 | Fix Bug #4 — Pinned Notes Sorting | 5 min |
| 9 | Incremental Edits | 7 min |
| 10 | Reverting Changes | 5 min |
| 11 | The Full Cycle — Plan → Implement → Diff → Review | 10 min |
| 12 | Multi-File Changes | 7 min |

---

## Exercise 1: Creating a New File

### Goal
Start with the simplest write operation — creating a brand new file. Nothing existing is at risk.

### Steps

**1.1** Navigate to the sample app and launch Copilot:

```bash
cd workshop/level-4/sample-app
copilot
```

**1.2** Ask Copilot to create a new file:

```
Create a file called CHANGELOG.md with a header "# Changelog" 
and one entry: "## v0.1.0" with bullet "- Initial release with add, list, show, edit, delete, search, and export commands"
```

**1.3** Watch the approval prompt carefully:

```
🔧 Tool: create
   Path: CHANGELOG.md
   [Allow] [Deny] [Allow for session]
```

> 💡 **This is the first time you're approving a write.** Read the tool name (`create`) and the path. Confirm it's what you expect, then **Allow**.

**1.4** Verify the file was created:

```
!cat CHANGELOG.md
```

**1.5** Check with git:

```
!git status
```

> You should see `CHANGELOG.md` as an untracked file.

### Key Concept: Write Tool Approval

| Tool | Risk Level | Example |
|------|------------|---------|
| `view`, `grep`, `ls` | 🟢 Read-only | Viewing files |
| `create` | 🟡 Creates new file | Won't overwrite existing |
| `edit` | 🟡 Modifies existing file | Changes content in place |
| `bash` | 🔴 Runs any command | Could do anything — read carefully |

### ✅ Checkpoint
You approved your first write operation and verified the result.

---

## Exercise 2: The Approval Flow Deep Dive

### Goal
Understand every option in the approval flow and when to use each one.

### Steps

**2.1** Ask Copilot to make a change and observe the approval prompt:

```
Add a comment at the top of config.py: "# Quick Notes Configuration"
```

**2.2** When the approval appears, **choose "Deny"** this time:

> Observe what happens: Copilot acknowledges the denial and may try an alternative approach or ask what you'd prefer.

**2.3** Ask for the same change again:

```
Go ahead and add that comment to config.py
```

**2.4** This time, **choose "Allow"** (single approval).

**2.5** Now ask for another edit to the same file:

```
Add a comment "# Limits" above the MAX_NOTES line in config.py
```

**2.6** Notice: you're prompted **again** for the same tool. Now try **"Allow for session"**:

> This auto-approves the `edit` tool for the rest of your session. All future edits will proceed without asking.

**2.7** Test that auto-approval is active:

```
Add a comment "# Display" above the PREVIEW_LENGTH line in config.py
```

> This should proceed without an approval prompt.

### Key Concept: The Three Approval Choices

| Choice | Scope | When to Use |
|--------|-------|-------------|
| **Allow** | This one call only | When you want to verify each change individually |
| **Deny** | This one call only | When the proposed change is wrong |
| **Allow for session** | All future calls of this tool | When you trust a tool type and want speed |

### When to Use Each

| Situation | Best Choice |
|-----------|-------------|
| First time Copilot edits a file | **Allow** (verify first) |
| Making many small edits to one file | **Allow for session** after the first one |
| Copilot wants to run `bash rm -rf` | **Deny** (obviously) |
| Copilot wants to run `cat file.py` | **Allow for session** (safe read) |
| You're in a sandbox you can reset | **Allow for session** is fine for most tools |

### ✅ Checkpoint
You've used Allow, Deny, and Allow-for-session, and understand when each is appropriate.

---

## Exercise 3: Your First `/diff`

### Goal
Learn to inspect exactly what changed before committing.

### Steps

**3.1** After the edits in Exercises 1–2, run:

```
/diff
```

**3.2** Observe what `/diff` shows:
- **Which files** changed (config.py, plus CHANGELOG.md if still untracked)
- **What lines** were added/modified/removed
- The diff format (similar to `git diff`)

**3.3** Compare with `!git diff`:

```
!git diff
```

> 💡 Both show the same information. `/diff` is formatted by Copilot for readability; `!git diff` is the raw git output. Use whichever you prefer.

**3.4** Check the untracked file separately:

```
!git status
```

> Note: `git diff` only shows changes to tracked files. New files (like CHANGELOG.md) show up in `git status` but not in `git diff` unless staged.

**3.5** Use `/diff` as a habit check:

```
Are the changes shown in /diff exactly what I asked for? Is there anything unexpected?
```

### Key Concept: The `/diff` Habit

**Rule: Always run `/diff` after every set of changes.** It takes 2 seconds and catches:
- Unintended changes to files you didn't ask about
- Incomplete changes (half-done edits)
- Formatting issues or broken syntax

### ✅ Checkpoint
You can inspect changes with `/diff` and `!git diff` and spot expected vs unexpected modifications.

---

## Exercise 4: Your First `/review`

### Goal
Use Copilot's AI-powered review to evaluate changes before committing.

### Steps

**4.1** With the changes from Exercises 1–3 still in place, run:

```
/review
```

**4.2** Observe what `/review` produces:
- A summary of all changes
- Assessment of each change (correctness, completeness)
- Potential issues or suggestions

**4.3** Ask for a focused review:

```
/review Focus on: are there any changes that could break existing functionality?
```

**4.4** Compare `/diff` vs `/review`:

| `/diff` | `/review` |
|---------|-----------|
| Shows **what** changed (raw diff) | Explains **whether** the changes are correct |
| Instant, no AI | Uses AI to analyze |
| Factual — no opinions | Evaluative — gives feedback |
| Use for: verification | Use for: quality assessment |

**4.5** Clean up before the bug-fixing exercises — reset everything:

```
!git checkout -- .
!rm -f CHANGELOG.md
```

Verify:

```
!git status
```

> Should show "nothing to commit, working tree clean".

### ✅ Checkpoint
You can use `/review` for AI-powered assessment and know when to use `/diff` vs `/review`.

---

## Exercise 5: Fix Bug #1 — Case-Sensitive Search

### Goal
Fix your first real bug using the plan → implement → verify workflow.

### Steps

**5.1** First, understand the bug (Level 2 skill):

```
@ search.py

Explain the case-sensitivity bug. What input demonstrates it?
```

**5.2** Plan the fix (Level 3 skill):

```
/plan Fix the case-sensitive search in search.py. 
Make search case-insensitive for title, body, and tag matching.
```

**5.3** Now — approve the plan and let Copilot implement it:

> This is the moment: you're letting Copilot actually modify `search.py`. Watch the approval prompts carefully. Approve the edits.

**5.4** Verify with `/diff`:

```
/diff
```

> Check: did Copilot only modify `search.py`? Are the changes limited to what the plan described?

**5.5** Verify with `/review`:

```
/review
```

**5.6** Verify manually — test the fix:

```
!python notes.py add "Python Tutorial" --tags python,tutorial
!python notes.py search "python"
!python notes.py search "PYTHON"
!python notes.py search "Python"
```

> All three searches should now find the note.

**5.7** Check the diff one more time:

```
!git diff search.py
```

### Key Concept: The Bug Fix Workflow

```
1. Understand (@ file + question)
2. Plan (/plan fix description)
3. Approve (let Copilot implement)
4. Diff (/diff — verify changes match plan)
5. Review (/review — quality check)
6. Test (!command — manual verification)
```

### ✅ Checkpoint
You fixed a real bug through the complete plan → implement → diff → review → test workflow.

---

## Exercise 6: Fix Bug #2 — Tag Normalization

### Goal
Fix a bug that requires understanding both the code and the data implications.

### Steps

**6.1** Plan the fix:

```
/plan Fix the tag normalization bug in models.py.
Tags should be lowercased and stripped during Note initialization.
Make sure the fix is applied in __post_init__ before validation.
```

**6.2** Approve and let Copilot implement.

**6.3** Verify with `/diff`:

```
/diff
```

**6.4** Test the fix:

```
!python notes.py add "Test Tags" --tags "Python, JAVASCRIPT, react "
!python notes.py list --tag python
```

> The note should appear because "Python" was normalized to "python".

**6.5** Think about existing data (Level 3 insight):

```
If we had existing notes with mixed-case tags, would this fix normalize them?
Or only new notes going forward?
```

> 💡 This fix only normalizes on creation. Existing data in `notes.json` would keep old tags. A migration would need separate handling.

### ✅ Checkpoint
You can fix bugs that have data implications and verify both code and behavior.

---

## Exercise 7: Fix Bug #3 — XSS Vulnerability

### Goal
Fix a security vulnerability — the most critical type of bug.

### Steps

**7.1** Understand the vulnerability:

```
@ export.py

Explain the XSS vulnerability in _to_html(). 
Show me an example: what happens if a note title contains <script>alert('xss')</script>?
```

**7.2** Plan a secure fix:

```
/plan Fix the XSS vulnerability in export.py by HTML-escaping all user content 
(title, body, tags) before inserting into HTML. Use the html module from stdlib.
Also fix the newline-to-<br> conversion in the body.
```

**7.3** Approve and implement.

**7.4** Verify with `/diff`:

```
/diff
```

> Check: does the diff show `import html` and usage of `html.escape()`?

**7.5** Test with a malicious note:

```
!python notes.py add "<script>alert('xss')</script>" --body "Hello<br>World\nNew line"
!python notes.py export --format html
```

> The HTML output should show escaped `&lt;script&gt;`, not executable `<script>` tags.

**7.6** Review the security fix:

```
/review Focus on: is the XSS fix complete? Are ALL user inputs escaped?
```

### ✅ Checkpoint
You can fix security vulnerabilities and verify the fix is complete using both `/diff` and targeted testing.

---

## Exercise 8: Fix Bug #4 — Pinned Notes Sorting

### Goal
Fix a UX bug and verify with the actual CLI output.

### Steps

**8.1** Create test data:

```
!python notes.py add "Regular note 1"
!python notes.py add "Pinned note" --pin
!python notes.py add "Regular note 2"
!python notes.py list
```

> Observe: pinned note is NOT at the top — it's in creation order.

**8.2** Fix it:

```
Fix the list command in notes.py so that pinned notes always appear before unpinned notes.
```

**8.3** Approve the edit, then verify:

```
!python notes.py list
```

> The pinned note should now appear first.

**8.4** Verify with `/diff` that only `notes.py` changed:

```
/diff
```

### ✅ Checkpoint
You can fix UX bugs and verify through actual CLI usage.

---

## Exercise 9: Incremental Edits

### Goal
Make multiple small changes to the same file across several turns, building up a larger improvement.

### Steps

**9.1** Start with a small edit to `search.py`:

```
Add a docstring to the search_notes function explaining its parameters and return value.
```

**9.2** Approve the edit. Then add another:

```
Now add type hints to the search_notes function signature.
```

**9.3** Add another:

```
Now add a constant at the top of search.py: SEARCH_OPERATORS = ["tag:", "title:"]
```

**9.4** Check the cumulative diff:

```
/diff
```

> You should see three separate changes to `search.py`, all in one diff.

**9.5** Review all changes together:

```
/review Are these three changes consistent with each other? Any conflicts?
```

**9.6** Observe the conversation context — each edit built on the previous one:

```
/context
```

### Key Concept: Incremental Editing Strategy

| Approach | When to Use |
|----------|-------------|
| **One big edit** | Simple, contained change (1–2 lines) |
| **Incremental edits** | Building up a feature step by step |
| **Plan then execute** | Complex multi-step change |

> 💡 **Incremental edits give you a `/diff` checkpoint after each step.** If step 3 goes wrong, you can revert just that step.

### ✅ Checkpoint
You can make multiple incremental edits and review the cumulative result.

---

## Exercise 10: Reverting Changes

### Goal
Learn to undo changes when something goes wrong — the essential safety skill.

### Steps

**10.1** Make an intentionally bad change:

```
Replace the entire search_notes function with a version that always returns an empty list.
```

**10.2** Approve it (we want to see it go wrong).

**10.3** Test — it's broken:

```
!python notes.py search "anything"
```

> Should always return "No notes matching..." even if there are matching notes.

**10.4** Revert the specific file:

```
!git checkout -- search.py
```

**10.5** Verify the revert worked:

```
!git diff search.py
!python notes.py search "anything"
```

> The file should be back to its original state (or the state of your last commit).

**10.6** Practice a targeted revert — undo only the last change:

```
!git diff
```

If you have changes in multiple files and only want to revert one:

```
!git checkout -- storage.py
```

**10.7** Nuclear option — revert everything:

```
!git checkout -- .
```

### Key Concept: Revert Strategies

| Scope | Command | Effect |
|-------|---------|--------|
| **One file** | `!git checkout -- search.py` | Reset that file to last commit |
| **All files** | `!git checkout -- .` | Reset all tracked files |
| **Unstage** | `!git reset HEAD file.py` | Unstage but keep changes |
| **Clean untracked** | `!git clean -fd` | Remove new (untracked) files |

> 💡 **Always verify after reverting** — run `!git status` and `!git diff` to confirm you're in the expected state.

### ✅ Checkpoint
You can revert changes at any granularity — single file, all files, or selective.

---

## Exercise 11: The Full Cycle — Plan → Implement → Diff → Review

### Goal
Execute the complete workflow for a non-trivial change, demonstrating all skills from Levels 1–4.

### Steps

**11.1** Reset to a clean state:

```
!git checkout -- .
!rm -f notes.json CHANGELOG.md
```

**11.2** Plan a feature (Level 3 skill):

```
/plan Add error handling for corrupted JSON files in storage.py.
When the JSON file is corrupt:
1. Log a warning to stderr
2. Create a backup of the corrupt file as notes.json.corrupt
3. Start with empty data
4. Do not crash or lose the corrupted file
```

**11.3** Review the plan (Level 3 skill):

```
Does this plan handle the case where notes.json.corrupt already exists?
```

**11.4** Approve and implement (Level 4 skill):

> Watch each approval. Copilot should modify `storage.py` — specifically the `_read` method.

**11.5** Inspect the changes:

```
/diff
```

**11.6** AI review:

```
/review Focus on: does the error handling actually work? What edge cases could still crash?
```

**11.7** Manual test — create a corrupt file and test recovery:

```
!echo "this is not valid json" > notes.json
!python notes.py list
!ls notes.json*
```

> Expected: a warning printed to stderr, `notes.json.corrupt` created, and an empty list shown.

**11.8** Verify the backup file:

```
!cat notes.json.corrupt
```

> Should contain "this is not valid json".

**11.9** Final check:

```
!git diff storage.py
```

### Key Concept: The Complete Cycle

```
/plan [task]              ← 1. Plan
  ↓
Review plan               ← 2. Evaluate before approving
  ↓
Approve → implement       ← 3. Let Copilot write code
  ↓
/diff                     ← 4. See what changed
  ↓
/review                   ← 5. AI quality check
  ↓
!test manually            ← 6. Verify behavior
  ↓
!git diff                 ← 7. Final cross-check
```

> 💡 **This 7-step cycle is your workflow for every future change.** It becomes automatic with practice.

### ✅ Checkpoint
You executed the complete plan → implement → diff → review → test cycle for a non-trivial feature.

---

## Exercise 12: Multi-File Changes

### Goal
Make a coordinated change across multiple files — the most complex write operation.

### Steps

**12.1** Plan a cross-file change:

```
/plan Add a "word count" field to the list command output.
Changes needed:
- models.py already has a word_count property — no changes needed
- notes.py: include word count in the list output next to each note's preview
- storage.py: include total word count in the stats() output
```

**12.2** Approve and implement. Watch which files are modified:

> Copilot should request approval for edits to `notes.py` and `storage.py`. Verify it does NOT modify `models.py` (since the property already exists).

**12.3** Verify each file independently:

```
/diff
```

Then check each changed file:

```
!git diff notes.py
```

```
!git diff storage.py
```

**12.4** Test the combined changes:

```
!python notes.py add "Hello world" --body "This is a test note with some words"
!python notes.py list
!python notes.py stats
```

> List should show word count. Stats should include total word count.

**12.5** Review the cross-file consistency:

```
/review Are the changes to notes.py and storage.py consistent with each other?
Do they both use the word_count property from models.py the same way?
```

**12.6** Reflect on the multi-file workflow:

```
Which file did Copilot change first? Was that the right order?
If it had changed storage.py first and notes.py second, would the app still work between those changes?
```

### Key Concept: Multi-File Change Safety

| Check | Why |
|-------|-----|
| Verify which files changed | Catch unintended modifications |
| Check each file's diff separately | Ensure changes are correct per file |
| Test after all changes | Combined behavior might differ from individual changes |
| Review cross-file consistency | Ensure files agree on data shapes and names |

### ✅ Checkpoint
You can make coordinated multi-file changes and verify their combined correctness.

---

## 🏆 Level 4 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Approve write operations (Allow/Deny/Session) | ☐ | ☐ | ☐ |
| 2 | Create new files through Copilot | ☐ | ☐ | ☐ |
| 3 | Use `/diff` to inspect changes | ☐ | ☐ | ☐ |
| 4 | Use `/review` for AI-powered self-review | ☐ | ☐ | ☐ |
| 5 | Fix bugs by approving Copilot's edits | ☐ | ☐ | ☐ |
| 6 | Fix security vulnerabilities with verification | ☐ | ☐ | ☐ |
| 7 | Make incremental edits to the same file | ☐ | ☐ | ☐ |
| 8 | Revert changes at any granularity | ☐ | ☐ | ☐ |
| 9 | Execute the full plan → implement → diff → review cycle | ☐ | ☐ | ☐ |
| 10 | Make coordinated multi-file changes | ☐ | ☐ | ☐ |
| 11 | Test changes manually after implementation | ☐ | ☐ | ☐ |
| 12 | Cross-check with `!git diff` and `!git status` | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 5
- **22–29:** Repeat exercises 5–12 on different bugs
- **Below 22:** Go back to Level 3 planning, then retry

---

## Key Takeaways

1. **Approve thoughtfully** — read the tool name and path before allowing writes
2. **`/diff` after every change** — it takes 2 seconds and catches surprises
3. **`/review` before committing** — AI catches what you might miss
4. **Test manually** — `/diff` and `/review` are not substitutes for running the code
5. **Incremental beats monolithic** — small changes with `/diff` checkpoints are safer
6. **You can always revert** — `git checkout -- file` is your safety net
7. **The 7-step cycle** — plan → evaluate → implement → diff → review → test → git check
8. **Multi-file changes need extra scrutiny** — verify each file individually AND together

---

## What's Next

**Level 5: Execute — Run Commands Through Copilot** lets Copilot run tests, builds, and linters, then interpret the results and make targeted fixes. You'll learn how tool execution chains work.

→ Continue to `workshop/level-5/README.md`
