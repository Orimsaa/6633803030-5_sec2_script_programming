# final_task_manager_project/src/data_persistence.py
"""Data layer: อ่าน/เขียนรายการงานเป็นไฟล์ JSON และแปลงกลับเป็น object ตามชนิด (_type)"""
import json
import os

try:
    from .task import DueDateTask, PriorityTask, Task
except ImportError:
    from task import DueDateTask, PriorityTask, Task

TASK_TYPES = {"Task": Task, "DueDateTask": DueDateTask, "PriorityTask": PriorityTask}
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DataPersistence:
    def __init__(self, data_file="data/tasks.json"):
        # path แบบ relative อ้างอิงจากโฟลเดอร์โปรเจกต์ ทำให้รันจากโฟลเดอร์ไหนก็ได้
        self.file_path = data_file if os.path.isabs(data_file) else os.path.join(PROJECT_ROOT, data_file)
        self.warnings = []

    def load_tasks(self):
        """โหลดงานจากไฟล์ คืนค่า list ว่างถ้าไม่มีไฟล์หรือไฟล์เสีย (ไม่ทำให้โปรแกรม crash)"""
        self.warnings = []
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
            raw_tasks = json.loads(content) if content else []
        except json.JSONDecodeError as e:
            self.warnings.append(f"tasks.json is corrupted (line {e.lineno}); starting with an empty list.")
            return []
        except OSError as e:
            self.warnings.append(f"Could not read tasks file: {e}")
            return []

        if not isinstance(raw_tasks, list):
            self.warnings.append("tasks.json does not contain a list; starting with an empty list.")
            return []

        tasks = []
        for item in raw_tasks:
            try:
                data = dict(item)
                task_type = data.pop("_type", "Task")
                data.setdefault("tags", [])           # รองรับไฟล์เวอร์ชันเก่าที่ไม่มี tags
                cls = TASK_TYPES[task_type]
                tasks.append(cls(**data))
            except KeyError:
                self.warnings.append(f"Unknown task type '{task_type}' (id={item.get('id')}); skipped.")
            except (TypeError, ValueError) as e:
                self.warnings.append(f"Invalid task entry (id={item.get('id') if isinstance(item, dict) else '?'}): {e}; skipped.")
        return tasks

    def save_tasks(self, tasks):
        """บันทึกทุกงานด้วย to_dict() (polymorphism) แบบเขียนไฟล์ชั่วคราวก่อนแล้วค่อยแทนที่ ป้องกันไฟล์เสีย"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        tmp_path = self.file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4, ensure_ascii=False)
        os.replace(tmp_path, self.file_path)
