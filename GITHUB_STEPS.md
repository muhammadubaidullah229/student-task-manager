# GitHub Steps — Student Task Manager

> **This file is a helper for Muhammad only. It is NOT part of the graded
> submission.** Do these steps on your own Windows PC, in your own
> browser, with your own GitHub account (`muhammadubaidullah229`).
> This machine (the VM that built the project) has **no GitHub login**,
> so no Issue, pull request, or Release has been created on GitHub yet.
> Everything below is prepared text — copy-paste it on github.com.

**Time needed:** about 20–30 minutes (push 2 min, Issues 10 min,
PRs 5 min, Release 5 min).

Note: pull requests should be opened on GitHub *before* merging, so each PR page exists before the merge.

**Note about the git email:** this repo was built with the local git
identity `Muhammad Ubaidullah <muhammadubaidullah229@users.noreply.github.com>`.
That is GitHub's private "noreply" email for your username
`muhammadubaidullah229`, so your commits show your GitHub profile
without exposing your real email. If you want your real email on the
commits instead, change it before pushing with:
`git config user.email "your-real-email@example.com"` — but then the
already-made commits keep the old email; that is fine, do not rewrite
history for this.

## Before you start

On your PC, open a terminal (PowerShell or Git Bash) in the project
folder — the folder that has `main.py` and `.git` in it. Check:

```bash
git log --oneline | wc -l
git branch -a
git tag -l
```

You should see 23 commits, 6 branches
(main + feature/addtask + feature/completetask + feature/deletetask +
conflict/status-in-progress + conflict/status-completed) and tag `v1.0.0`.

## (a) Create the empty repo on GitHub

1. Go to https://github.com and sign in.
2. Click **+** (top right) → **New repository**.
3. Repository name: `student-task-manager`
4. Description (optional): `Simple console Student Task Manager — CSC418 Lab Assignment 4`
5. Choose **Public**.
6. **Do NOT tick** "Add a README file". Do NOT add a .gitignore or a
   license. The repo must be completely empty.
7. Click **Create repository**. GitHub shows you a page with push
   commands — ignore those, use the commands in step (b) below.

## (b) Push the repo

In your terminal, in the project folder, run these commands exactly:

```bash
git remote add origin https://github.com/muhammadubaidullah229/student-task-manager.git
git push -u origin main
git push --all
git push --tags
```

What each line does:

- `git remote add origin ...` — connects your local repo to the new
  empty GitHub repo.
- `git push -u origin main` — uploads `main` (all 23 commits) and makes
  `main` the default branch to push to.
- `git push --all` — uploads all the other branches too (the 3 feature
  branches and the 2 conflict branches).
- `git push --tags` — uploads the release tag `v1.0.0`.

Check on GitHub: open
`https://github.com/muhammadubaidullah229/student-task-manager` — you
should see the README, and the branch dropdown should list all
6 branches. Click **Actions** — the "Tests" workflow should run and
go green (it runs the 8 unit tests).

## (c) Create the 4 Issues

On the repo page, click **Issues** → **New issue**. Copy-paste each
title, body, and label exactly as below. Create one, then repeat.

### Issue 1

- **Title:** `Add-task validation: reject empty titles`
- **Labels:** `enhancement`
- **Body:**

```text
## Problem
A task with an empty title (or only spaces) should not be saved.
An empty task is meaningless in the list and confusing to read.

## Expected behaviour
- `add_task("")` raises `ValueError`
- `add_task("   ")` raises `ValueError`
- No task is added to the list in either case

## Done when
- The validation is in `task_manager.py`
- A unit test `test_add_empty_title_rejected` passes
- The work is merged from branch `feature/addtask` (PR #1)
```

### Issue 2

- **Title:** `Complete-task feature: mark a task as completed`
- **Labels:** `enhancement`
- **Body:**

```text
## What is needed
A way to mark a task as completed by its ID, so finished tasks
show as [Done] in the list.

## Expected behaviour
- `complete_task(1)` returns `True` and the task becomes completed
- `complete_task(99)` returns `False` when no task has that ID
- `complete_task(0)` or a negative ID raises `ValueError`

## Done when
- `complete_task` is in `task_manager.py`
- Menu option 3 works in `main.py`
- Unit tests `test_complete_task` and `test_complete_invalid_id` pass
- The work is merged from branch `feature/completetask` (PR #2)
```

### Issue 3

- **Title:** `Delete-task by valid ID`
- **Labels:** `enhancement`
- **Body:**

```text
## What is needed
A way to delete a task by its ID, so old tasks can be removed
from the list.

## Expected behaviour
- `delete_task(2)` returns `True` and the task is gone from the list
- `delete_task(99)` returns `False` when no task has that ID
- `delete_task(0)` or a negative ID raises `ValueError`
- Deleting one task must not delete any other task

## Done when
- `delete_task` is in `task_manager.py`
- Menu option 4 works in `main.py`
- Unit tests `test_delete_task` and `test_delete_invalid_id` pass
- The work is merged from branch `feature/deletetask` (PR #3)
```

### Issue 4

- **Title:** `Documentation: user guide for the Task Manager`
- **Labels:** `documentation`
- **Body:**

```text
## What is needed
A short user guide so a new user can run the app without asking
the developer.

## Done when
- `docs/user-guide.md` explains: install, run `python main.py`,
  each menu option (1-5) with an example, where tasks are stored
  (`tasks.json`), and troubleshooting for common errors
- README links to the user guide
```

## (d) The 5 pull requests — read this carefully, it is honest

**The truth:** the 5 pull requests were merged **locally** in this repo
with `git merge --no-ff`. You can see them in the history — run
`git log --oneline --graph --all` and you will see these 5 merge commits:

1. `Merge pull request #1 from feature/addtask — Closes #1`
2. `Merge pull request #2 from feature/completetask — Closes #2`
3. `Merge pull request #3 from feature/deletetask — Closes #3`
4. `Merge pull request #4 from conflict/status-in-progress`
5. `Merge pull request #5 from conflict/status-completed — resolve merge conflict (kept In Progress)`

Those merge commits are real and they prove the branches were reviewed
and merged. **No pull request pages exist on GitHub yet**, because a
pull request page can only be created on github.com. Do not tell the
teacher that GitHub PRs exist until you have done one of the two
options below.

### Option A (recommended for this submission) — show the local merges

- Do nothing extra. In the viva, show `git log --oneline --graph --all`
  and the 5 merge commits above, and explain: "The PRs were merged
  locally with --no-ff, so each merge commit is the PR record, and
  each one closes its Issue."
- This is the normal way a small local project records PRs, and the
  history is complete and verifiable.

### Option B (only if the teacher wants PR pages on github.com)

- Push all branches first (`git push --all` — already done in step b).
- On GitHub, go to **Pull requests** → **New pull request**, pick
  `base: main` and `compare: feature/addtask`, and create it. Repeat
  for the other 4 branches.
- **Warning, be honest about this:** because these branches are
  already merged into `main`, GitHub will show each PR as already
  merged / with no new changes to merge. The PR page still shows the
  branch, the files, and the discussion — but you cannot "merge it
  again" on GitHub. A truly fresh GitHub PR (with a Merge button) only
  happens if you open the PR *before* merging, so for a future project,
  push the branch first, open the PR, then merge on GitHub.

## (e) Create Release v1.0.0

1. On the repo page, click **Releases** (right side) → **Draft a new release**.
2. **Choose a tag:** type `v1.0.0` and select the existing tag
   (you pushed it in step b — do NOT create a new tag).
3. **Release title:** `v1.0.0 — Student Task Manager`
4. **Description:** copy-paste the text from `RELEASE_NOTES_v1.0.0.md`
   in this repo (the full text, exactly as it is).
5. Click **Publish release**.

## (f) What to show in the viva

1. The app running: `python main.py` — add a task, list, complete it,
   delete it (or show `labevidence/07-app-demo.png`).
2. The tests: `python -m unittest discover -s tests -v` — 8 tests, OK
   (or `labevidence/03-test-run-passed.png`).
3. The history: `git log --oneline --graph --all` — 23 commits,
   6 branches, 5 merge commits (or `labevidence/01-git-log-graph.png`).
4. The conflict: `labevidence/05-merge-conflict-before.png` (markers)
   and `06-merge-conflict-after.png` (resolved), and explain why
   "In Progress" was kept — the project was not finished yet.
5. On GitHub: the repo page, the 4 Issues, the green Actions run,
   and Release v1.0.0.
6. `LABREPORT.md` — your Part G answers.

## Part H checklist — ACTUAL counts

| Requirement | Required | Actual |
|---|---|---|
| Commits | >= 12 | **23** |
| Feature branches | 3 | **3** |
| Merged PRs (merge commits) | 5 | **5** |
| Resolved merge conflict | 1 | **1** |
| Unit tests | >= 3 | **8**, all passing |
| GitHub Actions workflow | 1 | **1** |
| Release tag | 1 | **1** — `v1.0.0` |

**DONE locally:** everything in the table above.
**Still needs github.com (by you):** the 4 Issues, the 5 GitHub PR
pages (see option A/B above), and publishing Release v1.0.0.
