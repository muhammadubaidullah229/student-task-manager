# Release v1.0.0 — Student Task Manager

**Tag:** `v1.0.0`
**Date:** 18 November 2026
**Author:** Muhammad Ubaidullah (SP23-BSE-131)

## What is in this release

A simple console Student Task Manager written in Python (standard
library only, no packages to install).

- Add a task with a title (empty titles are rejected)
- List all tasks with their status (Pending / Done)
- Mark a task as completed by its ID
- Delete a task by its ID
- Tasks are saved automatically to `tasks.json`

## Quality

- 8 unit tests, all passing (`python -m unittest discover -s tests -v`)
- GitHub Actions runs the tests on every push and pull request to `main`
- 23 commits, 3 feature branches, 5 merged pull requests, 1 merge
  conflict resolved (README status line — kept "In Progress")

## How to run

```bash
python main.py
```

See `docs/user-guide.md` for the full user guide.
