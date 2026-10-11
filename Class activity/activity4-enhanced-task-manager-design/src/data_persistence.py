# enhanced-task-manager-design/src/data_persistence.py
"""Data layer: รวมศูนย์การอ่าน/เขียน JSON และการแปลงกลับเป็น object ตาม _type"""
import json
import os

try:
    from .task import DueDateTask, PriorityTask, Task
except ImportError:
    from task import DueDateTask, PriorityTask, Task

CLASSES = {"Task": Task, "DueDateTask": DueDateTask, "PriorityTask": PriorityTask}


class DataPersistence:
    def __init__(self, data_file="data/tasks.json"):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = data_file if os.path.isabs(data_file) else os.path.join(root, data_file)

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
        except json.JSONDecodeError:
            print("Warning: tasks.json ว่างเปล่าหรือรูปแบบไม่ถูกต้อง เริ่มด้วยรายการงานว่าง")
            return []
        tasks = []
        for item in raw:
            task_type = item.pop("_type", "Task")
            item.setdefault("tags", [])
            cls = CLASSES.get(task_type)
            if cls is None:
                print(f"Warning: ไม่รู้จัก task type '{task_type}' (ID {item.get('id')}) ข้ามรายการนี้")
                continue
            try:
                tasks.append(cls(**item))
            except (TypeError, ValueError) as e:
                print(f"Warning: ข้อมูลงาน ID {item.get('id')} ไม่ถูกต้อง ({e}) ข้ามรายการนี้")
        return tasks

    def save_tasks(self, tasks):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=4, ensure_ascii=False)
