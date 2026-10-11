# my-oop-task-manager/tests/test_task_manager.py
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from task import Task  # noqa: E402
from task_manager import TaskManager  # noqa: E402


class TestTask(unittest.TestCase):
    def test_init_defaults(self):
        t = Task(1, "Read OOP chapter")
        self.assertEqual((t.id, t.description, t.completed), (1, "Read OOP chapter", False))

    def test_mark_complete_and_to_dict(self):
        t = Task(2, "Refactor CLI")
        t.mark_complete()
        self.assertEqual(t.to_dict(), {"id": 2, "description": "Refactor CLI", "completed": True})

    def test_str_and_repr(self):
        t = Task(3, "Write tests")
        self.assertEqual(str(t), "ID: 3 | Description: Write tests | Status: Pending")
        self.assertEqual(repr(t), "Task(id=3, description='Write tests', completed=False)")


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.path = os.path.join(self.tmp, "tasks.json")
        self.manager = TaskManager(self.path)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_add_complete_delete(self):
        self.manager.add_task("A")
        self.manager.add_task("B")
        self.assertEqual(self.manager.next_id, 3)
        self.assertTrue(self.manager.complete_task(1))
        self.assertTrue(self.manager.tasks[0].completed)
        self.assertFalse(self.manager.complete_task(99))
        self.assertTrue(self.manager.delete_task(1))
        self.assertEqual([t.id for t in self.manager.tasks], [2])
        self.assertFalse(self.manager.delete_task(1))

    def test_persistence_reloads_task_objects(self):
        self.manager.add_task("Persist me")
        self.manager.complete_task(1)
        reloaded = TaskManager(self.path)
        self.assertIsInstance(reloaded.tasks[0], Task)
        self.assertTrue(reloaded.tasks[0].completed)
        self.assertEqual(reloaded.next_id, 2)

    def test_corrupted_file(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("not json")
        self.assertEqual(TaskManager(self.path).tasks, [])


if __name__ == '__main__':
    unittest.main()
