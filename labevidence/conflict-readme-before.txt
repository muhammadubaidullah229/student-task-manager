=== git status (during merge conflict) ===
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	labevidence/

no changes added to commit (use "git add" and/or "git commit -a")

=== conflicted README.md (with conflict markers) ===
# Student Task Manager

A simple console app to manage your daily tasks — add a task, list tasks,
mark a task as completed, or delete a task. Tasks are saved in `tasks.json`
so they are still there the next time you run the app.

## Features

- Add a task with a title
- List all tasks with their status
- Mark a task as completed
- Delete a task by its ID

## Setup

You need Python 3.10 or newer. No extra packages are needed — the app
uses only the Python standard library.

```bash
python main.py
```

## Author

Muhammad Ubaidullah — SP23-BSE-131

<<<<<<< HEAD
Project status: In Progress
=======
Project status: Completed
>>>>>>> conflict/status-completed
