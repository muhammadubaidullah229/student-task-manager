# Lab Evidence — Student Task Manager (CSC418 Lab Assignment 4)

**Student:** Muhammad Ubaidullah — SP23-BSE-131
**Date:** 18 November 2026

Every file here is real output from this project — terminal logs saved
directly, and PNG screenshots rendered from those exact logs (black
terminal, monospace text). Nothing here is typed by hand or faked.

Note on screenshots 01 and 06: they were rendered from `git log` when the
history had 21 commits (ending at the LABREPORT commit). The final two
commits after that are documentation only ("Add lab evidence..." and
"Add GitHub steps and release notes v1.0.0"); the branch and merge
structure they show is unchanged. The complete final log is in
`GIT_HISTORY.txt` in the submission zip.

## Index

| File | What it proves | Assignment part |
|---|---|---|
| `test-run-passed.txt` | `python -m unittest discover -s tests -v` — **8 tests, all OK** | Part D (testing) |
| `03-test-run-passed.png` | Screenshot of the passing run | Part D |
| `test-run-failed.txt` | The same suite with **1 deliberate failure** (see below) — `FAILED (failures=1)` | Part D |
| `04-test-run-failed.png` | Screenshot of the failing run | Part D |
| `app-demo.txt` | Real run of `python main.py`: add 2 tasks, list, complete 1, list, delete 2, list, exit | Part D / demo |
| `07-app-demo.png` | Screenshot of the app demo | Part D / demo |
| `conflict-readme-before.txt` | `git status` + README **during** the merge conflict, with `<<<<<<<`, `=======`, `>>>>>>>` markers | Part C (conflict) |
| `05-merge-conflict-before.png` | Screenshot of the conflicted README | Part C |
| `06-merge-conflict-after.png` | Resolved README (`Project status: In Progress` + resolution note) and `git log` showing the conflict merge commit | Part C |
| `01-git-log-graph.png` | `git log --oneline --graph --all` — all branches and 5 merge commits | Part B / H |
| `02-git-branches.png` | `git branch -a` + `git status` — main + 3 feature + 2 conflict branches | Part B / H |
| `08-workflow-file.png` | `.github/workflows/tests.yml` content | Part E (Actions) |

## The deliberate failing test run (honest note)

`test-run-failed.txt` was produced on purpose, to show what a failing
test looks like:

- A copy of the project was made in `/tmp/stm-fail-demo` (a scratch
  folder, NOT the real repo).
- In that scratch copy only, one line in `tests/test_task_manager.py`
  was changed: in `test_complete_task`, the check
  `assertTrue(...completed)` was changed to `assertFalse(...completed)`,
  so the test expected the opposite of what the code correctly does.
- The suite was run there: 7 passed, `test_complete_task` FAILED with
  `AssertionError: True is not false`, exit code 1.
- The scratch folder was then deleted. The real repo was never changed,
  no broken code was ever committed, and the suite was re-run in the
  real repo straight after: **8 tests, OK**.

## Part H checklist — ACTUAL counts (verified in this repo)

| Requirement | Required | Actual | Status |
|---|---|---|---|
| Commits | >= 12 | **23** (`git log --oneline \| wc -l`) | DONE locally |
| Feature branches | 3 | **3** — `feature/addtask`, `feature/completetask`, `feature/deletetask` | DONE locally |
| Merged pull requests (`--no-ff` merge commits) | 5 | **5** — #1 addtask, #2 completetask, #3 deletetask, #4 status-in-progress, #5 status-completed | DONE locally |
| Resolved merge conflict | 1 | **1** — README status line, kept "In Progress" | DONE locally |
| Unit tests | >= 3 | **8**, all passing | DONE locally |
| GitHub Actions workflow | 1 | **1** — `.github/workflows/tests.yml` (Python 3.12, runs on push + PR to main) | DONE locally |
| Release tag | 1 | **1** — `v1.0.0` (annotated) | DONE locally |

## What is DONE locally vs what still needs github.com

DONE locally (in this repo, ready to push):

- All code, tests, docs, 23 commits, 6 branches, 5 merge commits,
  1 resolved conflict, workflow file, tag `v1.0.0`.

STILL TO DO on github.com (by Muhammad, on his own PC — this machine
has no GitHub login, so nothing below was created there):

- Push the repo to github.com (see `GITHUB_STEPS.md`).
- Create the 4 Issues (exact titles/labels/bodies in `GITHUB_STEPS.md`).
- Open the 5 pull requests on GitHub — the 5 merges already exist
  locally as `--no-ff` merge commits; see `GITHUB_STEPS.md` for the
  two honest options (show the merged branches + merge commits, or
  push the branches first and open real PRs on GitHub).
- Publish Release v1.0.0 from the tag (release notes in
  `RELEASE_NOTES_v1.0.0.md`).

No GitHub Issue, pull request, or Release exists yet — do not claim
otherwise in the viva. Show the local `git log --graph` instead.
