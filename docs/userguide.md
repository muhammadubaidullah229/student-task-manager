# Student Task Manager — User Guide

## Install

You need Python 3.10 or newer. No extra packages are needed — the app
uses only the Python standard library, so there is nothing to install.

```bash
python main.py
```

(On some computers the command is `python3 main.py`.)

## Menu options

When the app starts you see this menu:

```text
--- Student Task Manager ---
1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit
```

### 1. Add Task

Type the title of your task and press Enter.

Example:

```text
Enter task title: Revise DevOps notes
Task added: Revise DevOps notes
```

An empty title is not accepted — the app tells you the title cannot
be empty and asks again. A title with only spaces is rejected the same way.

### 2. Display Tasks

Shows all your tasks with their number, status and title.

Example:

```text
1. [Pending] Revise DevOps notes
2. [Done] Submit assignment
```

If you have no tasks yet, the app says so.

### 3. Complete Task

Enter the ID (number) of the task you finished.

Example:

```text
Enter task ID to complete: 1
Task 1 marked as completed.
```

If no task has that ID, the app says "No task found with ID ...".
If you type something that is not a number, it asks for a valid ID
instead of crashing.

### 4. Delete Task

Enter the ID of the task you want to remove.

Example:

```text
Enter task ID to delete: 2
Task 2 deleted.
```

Like Complete, a wrong ID just shows "No task found", it does not
delete anything else.

### 5. Exit

Closes the app. Your tasks are already saved, so they will still be
there next time.

## Where are tasks stored?

In a file called `tasks.json` in the same folder as `main.py`. It is
created automatically the first time you add a task. You do not need
to open or edit it — the app does that for you. It is not committed
to git (see `.gitignore`).

## Troubleshooting

- **`python: command not found`** — try `python3 main.py` instead.
- **Menu shows "Invalid choice"** — type only a number from 1 to 5.
- **"Please enter a valid task ID"** — type the task number shown by
  option 2, not the task title.
- **Tasks disappeared** — check you are running the app from the same
  folder that holds `tasks.json`. Running it from another folder
  creates a new, empty `tasks.json` there.
- **Tests fail after editing the code** — run
  `python -m unittest discover -s tests -v` and read which test
  failed; the test name tells you which behaviour broke.
