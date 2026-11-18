# Student Task Manager

A simple console app to manage your daily tasks — add a task, list tasks,
mark a task as completed, or delete a task. Tasks are saved in `tasks.json`
so they are still there the next time you run the app.

## Features

- Add a task with a title (empty titles are rejected)
- List all tasks with their status (Pending / Done)
- Mark a task as completed by its ID (completed tasks stay in the list marked [Done])
- Delete a task by its ID
- Tasks are saved automatically to `tasks.json`
- Invalid menu choices and IDs are handled without crashing

## Setup

You need Python 3.10 or newer. No extra packages are needed — the app
uses only the Python standard library, so there is nothing to install.

```bash
python main.py
```

(On some computers the command is `python3 main.py`.)

## Usage

When the app starts you see this menu:

```text
--- Student Task Manager ---
1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit
```

Example session:

```text
Enter your choice (1-5): 1
Enter task title: Revise DevOps notes
Task added: Revise DevOps notes

Enter your choice (1-5): 2
1. [Pending] Revise DevOps notes

Enter your choice (1-5): 3
Enter task ID to complete: 1
Task 1 marked as completed.

Enter your choice (1-5): 5
Goodbye! Your tasks are saved.
```

See `docs/user-guide.md` for the full user guide.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

All 8 unit tests should pass. Tests use temporary files, so they never
touch your real `tasks.json`.

## Project structure

```text
student-task-manager/
├── main.py                  # Console menu (add / display / complete / delete / exit)
├── task_manager.py          # Task dataclass + TaskManager (add, list, complete, delete, save/load)
├── tests/
│   └── test_task_manager.py # 8 unit tests
├── .github/workflows/
│   └── tests.yml            # GitHub Actions: run tests on push and PR to main
├── docs/
│   └── user-guide.md       # User guide
├── LABREPORT.md             # Answers to the Part G questions
├── GITHUB_STEPS.md          # Steps to push this repo to GitHub (helper, not graded)
├── LICENSE                  # MIT License
└── README.md                # This file
```

## Git workflow summary

- `main` is the stable branch. Work is done on short feature branches
  (`feature/addtask`, `feature/completetask`, `feature/deletetask`)
  and merged back with `--no-ff` merge commits, like pull requests.
- Every push and pull request to `main` runs the unit tests through
  GitHub Actions (`.github/workflows/tests.yml`).
- Releases are tagged, e.g. `v1.0.0`.

## Author

Muhammad Ubaidullah — SP23-BSE-131

Project status: In Progress
Merge conflict resolved: kept In Progress; Completed was premature.
