"""Student Task Manager — core task logic.

Uses only the Python standard library. Tasks are stored in a JSON file
(tasks.json by default) so they survive between runs.
"""

import json
import os
from dataclasses import asdict, dataclass


@dataclass
class Task:
    """One task: an id, a title, and whether it is done."""

    id: int
    title: str
    completed: bool = False


class TaskManager:
    """Keeps the list of tasks and saves/loads them from a JSON file."""

    def __init__(self, storage_path="tasks.json"):
        self.storage_path = storage_path
        self.tasks = []
        self.load()

    def add_task(self, title):
        """Add a task and return it. Empty or blank titles are rejected."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task_id = max((t.id for t in self.tasks), default=0) + 1
        task = Task(id=task_id, title=title.strip())
        self.tasks.append(task)
        self.save()
        return task

    def list_tasks(self):
        """Return all tasks in the order they were added."""
        return list(self.tasks)

    def save(self):
        """Write all tasks to the JSON storage file."""
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump([asdict(t) for t in self.tasks], f, indent=2)

    def load(self):
        """Load tasks from the JSON file. A missing file means no tasks yet."""
        if not os.path.exists(self.storage_path):
            self.tasks = []
            return
        with open(self.storage_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [Task(**item) for item in data]
