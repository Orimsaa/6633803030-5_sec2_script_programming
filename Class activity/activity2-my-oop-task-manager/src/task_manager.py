# my-oop-task-manager/src/task_manager.py
import json
import os

try:
    from .task import Task
except ImportError:
    from task import Task

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TaskManager:
    """
    จัดการ collection ของ Task objects: โหลด/บันทึก JSON และ add / list / complete / delete
    """

    def __init__(self, data_file="data/tasks.json"):
        self.data_file = data_file if os.path.isabs(data_file) else os.path.join(PROJECT_ROOT, data_file)
        self.tasks = self.load_tasks()
        self.next_id = self._get_next_task_id()

    def _get_next_task_id(self):
        return max((task.id for task in self.tasks), default=0) + 1

    def load_tasks(self):
        """Loads tasks from JSON and converts each dict back into a Task object."""
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
            return [Task.from_dict(item) for item in json.loads(content)] if content else []
        except (json.JSONDecodeError, KeyError, TypeError):
            print("Warning: tasks.json is empty or corrupted. Starting with an empty task list.")
            return []

    def save_tasks(self):
        """Converts Task objects to dicts and saves them to JSON."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4, ensure_ascii=False)

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task '{description}' added with ID {task.id}.")
        return task

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n--- Your Tasks ---")
        for task in self.tasks:
            print(task)  # เรียก Task.__str__
        print("------------------")

    def find_task(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            return False
        if task.completed:
            print(f"Task ID {task_id} is already completed.")
            return True
        task.mark_complete()
        self.save_tasks()
        print(f"Task ID {task_id} marked as completed.")
        return True

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            return False
        self.tasks.remove(task)
        self.save_tasks()
        print(f"Task ID {task_id} deleted successfully.")
        return True
