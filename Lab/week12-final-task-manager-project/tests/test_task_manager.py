# final_task_manager_project/tests/test_task_manager.py
import datetime
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.task import DueDateTask, PriorityTask, Task  # noqa: E402
from src.task_manager import TaskManager  # noqa: E402


class TestTaskModels(unittest.TestCase):
    def test_tags_are_normalized_and_unique(self):
        t = Task(1, "Read", tags=[" Study", "study", "URGENT", ""])
        self.assertEqual(t.tags, ["study", "urgent"])
        self.assertFalse(t.add_tag("Study "))
        self.assertTrue(t.remove_tag("URGENT"))
        self.assertEqual(t.tags, ["study"])
        self.assertFalse(t.remove_tag("missing"))

    def test_str_shows_type_specific_info_before_tags(self):
        due = DueDateTask(2, "Submit", "2099-01-31", tags=["uni"])
        prio = PriorityTask(3, "Slides", "high")
        self.assertEqual(str(due), "ID: 2 | Description: Submit | Status: Pending | Due: 2099-01-31 | Tags: uni")
        self.assertEqual(str(prio), "ID: 3 | Description: Slides | Status: Pending | Priority: High")

    def test_validation_errors(self):
        with self.assertRaises(ValueError):
            Task(1, "   ")
        with self.assertRaises(ValueError):
            DueDateTask(1, "x", "31-12-2026")
        with self.assertRaises(ValueError):
            PriorityTask(1, "x", "urgent")

    def test_to_dict_contains_type_and_fields(self):
        self.assertEqual(DueDateTask(5, "x", "2026-10-15").to_dict()["_type"], "DueDateTask")
        self.assertEqual(DueDateTask(5, "x", "2026-10-15").to_dict()["due_date"], "2026-10-15")
        self.assertEqual(PriorityTask(6, "y", "Low").to_dict()["priority"], "Low")

    def test_overdue_flag(self):
        task = DueDateTask(1, "old", "2000-01-01")
        self.assertTrue(task.is_overdue())
        task.mark_complete()
        self.assertFalse(task.is_overdue())


class TestTaskManagerLogic(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.path = os.path.join(self.tmp, "tasks.json")
        self.m = TaskManager(self.path)
        self.m.add_normal_task("Write README", ["docs", "final"])                      # 1
        self.m.add_due_date_task("Final Project Submission", "2026-10-15",
                                 ["study", "urgent", "final"])                          # 2
        self.m.add_due_date_task("Midterm review", "2026-09-20", ["study", "exam"])     # 3
        self.m.add_priority_task("Prepare slides", "High", ["presentation", "urgent"])  # 4
        self.m.add_priority_task("Refactor code", "Low", ["code"])                      # 5
        self.m.add_priority_task("Fix PEP 8 issues", "Medium")                          # 6

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_crud_and_ids(self):
        self.assertEqual([t.id for t in self.m.tasks], [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.m.complete_task(3), (True, "Task ID 3 marked as completed."))
        self.assertFalse(self.m.complete_task(3)[0])          # already completed
        self.assertFalse(self.m.complete_task(99)[0])         # not found
        self.assertTrue(self.m.delete_task(6)[0])
        self.assertFalse(self.m.delete_task(6)[0])
        self.assertEqual(self.m.add_normal_task("New").id, 7)  # ids are never reused

    def test_search_description_and_tags_case_insensitive(self):
        self.assertEqual({t.id for t in self.m.search_tasks("URGENT")}, {2, 4})
        self.assertEqual({t.id for t in self.m.search_tasks("final")}, {1, 2})
        self.assertEqual({t.id for t in self.m.search_tasks("pep")}, {6})
        self.assertEqual(self.m.search_tasks("   "), [])

    def test_filter_single_and_combined(self):
        self.m.complete_task(3)
        self.assertEqual({t.id for t in self.m.filter_tasks(status=True)}, {3})
        self.assertEqual({t.id for t in self.m.filter_tasks(due_date_before="2026-10-01")}, {3})
        self.assertEqual({t.id for t in self.m.filter_tasks(due_date_after=datetime.date(2026, 10, 1))}, {2})
        self.assertEqual({t.id for t in self.m.filter_tasks(priority_level="high")}, {4})
        self.assertEqual({t.id for t in self.m.filter_tasks(contains_tags=["study", "final"])}, {2})
        self.assertEqual({t.id for t in self.m.filter_tasks(contains_tags="urgent")}, {2, 4})
        combined = self.m.filter_tasks(status=False, due_date_before="2026-12-31", contains_tags=["study"])
        self.assertEqual([t.id for t in combined], [2])
        self.assertEqual(len(self.m.filter_tasks()), 6)

    def test_sort_due_date_keeps_undated_last(self):
        self.assertEqual([t.id for t in self.m.sort_tasks("due_date")], [3, 2, 1, 4, 5, 6])
        self.assertEqual([t.id for t in self.m.sort_tasks("due_date", reverse=True)], [2, 3, 1, 4, 5, 6])

    def test_sort_priority_and_others(self):
        self.assertEqual([t.id for t in self.m.sort_tasks("priority")], [4, 6, 5, 1, 2, 3])
        self.assertEqual([t.id for t in self.m.sort_tasks("priority", reverse=True)], [5, 6, 4, 1, 2, 3])
        self.assertEqual([t.id for t in self.m.sort_tasks("id", reverse=True)], [6, 5, 4, 3, 2, 1])
        self.assertEqual(self.m.sort_tasks("description")[0].description, "Final Project Submission")
        self.m.complete_task(1)
        self.assertEqual(self.m.sort_tasks("completed")[-1].id, 1)
        with self.assertRaises(ValueError):
            self.m.sort_tasks("color")

    def test_persistence_round_trip_restores_types(self):
        self.m.complete_task(2)
        reloaded = TaskManager(self.path)
        self.assertEqual(len(reloaded.tasks), 6)
        self.assertIsInstance(reloaded.get_task_by_id(2), DueDateTask)
        self.assertIsInstance(reloaded.get_task_by_id(4), PriorityTask)
        self.assertEqual(type(reloaded.get_task_by_id(1)), Task)
        self.assertTrue(reloaded.get_task_by_id(2).completed)
        self.assertEqual(reloaded.get_task_by_id(2).due_date, datetime.date(2026, 10, 15))
        self.assertEqual(reloaded.get_task_by_id(4).tags, ["presentation", "urgent"])
        self.assertEqual(reloaded.next_id, 7)

    def test_corrupted_and_legacy_files_do_not_crash(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("{ not valid json")
        broken = TaskManager(self.path)
        self.assertEqual(broken.tasks, [])
        self.assertTrue(broken.load_warnings)

        legacy = [{"id": 1, "description": "old task without tags", "completed": False},
                  {"id": 2, "description": "bad", "completed": False, "_type": "Alien"},
                  {"id": 3, "description": "bad date", "completed": False, "_type": "DueDateTask",
                   "due_date": "tomorrow"}]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(legacy, f)
        m = TaskManager(self.path)
        self.assertEqual([t.id for t in m.tasks], [1])
        self.assertEqual(m.tasks[0].tags, [])
        self.assertEqual(len(m.load_warnings), 2)


if __name__ == "__main__":
    unittest.main()
