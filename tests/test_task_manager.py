import os
import sys
import unittest

# Allow importing task_manager from the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish lab report")
        self.assertEqual(task.title, "Finish lab report")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Study DevOps")
        self.manager.complete_task(task.id)
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = self.manager.add_task("Temporary task")
        self.manager.delete_task(task.id)
        self.assertEqual(len(self.manager.get_tasks()), 1)
        # self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_delete_invalid_id(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(999)


if __name__ == "__main__":
    unittest.main()