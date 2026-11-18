"""Unit tests for the Student Task Manager.

Run with:  python -m unittest discover -s tests -v
"""

import os
import tempfile
import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # A fresh temporary file for every test, so tests never touch
        # the real tasks.json.
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.tmp.close()
        os.unlink(self.tmp.name)
        self.manager = TaskManager(storage_path=self.tmp.name)

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.unlink(self.tmp.name)

    def test_add_task(self):
        task = self.manager.add_task("Revise DevOps notes")
        self.assertEqual(task.title, "Revise DevOps notes")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_list_tasks_empty_at_start(self):
        self.assertEqual(self.manager.list_tasks(), [])

    def test_save_and_load(self):
        self.manager.add_task("Prepare lab report")
        reloaded = TaskManager(storage_path=self.tmp.name)
        titles = [t.title for t in reloaded.list_tasks()]
        self.assertEqual(titles, ["Prepare lab report"])


if __name__ == "__main__":
    unittest.main()
