# enhanced-task-manager-design/src/task_manager.py
"""Business logic: CRUD + search / filter / sort (ส่วนที่เป็น assignment ของนักศึกษา)"""
import datetime

try:
    from .data_persistence import DataPersistence
    from .task import DueDateTask, PriorityTask, Task
except ImportError:
    from data_persistence import DataPersistence
    from task import DueDateTask, PriorityTask, Task


class TaskManager:
    PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}

    def __init__(self, data_file="data/tasks.json"):
        self.persistence = DataPersistence(data_file)
        self.tasks = self.persistence.load_tasks()
        self.next_id = max((t.id for t in self.tasks), default=0) + 1

    def _save_changes(self):
        self.persistence.save_tasks(self.tasks)

    def _add(self, task):
        self.tasks.append(task)
        self.next_id += 1
        self._save_changes()
        return task

    # ---------------------------------------------------------------- CRUD
    def add_normal_task(self, description, tags=None):
        return self._add(Task(self.next_id, description, tags=tags))

    def add_due_date_task(self, description, due_date_str, tags=None):
        return self._add(DueDateTask(self.next_id, description, due_date_str, tags=tags))

    def add_priority_task(self, description, priority, tags=None):
        return self._add(PriorityTask(self.next_id, description, priority, tags=tags))

    def get_task_by_id(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task is None:
            return False, f"ไม่พบงาน ID {task_id} ในระบบ"
        if task.completed:
            return False, f"งาน ID {task_id} มีสถานะเสร็จสมบูรณ์อยู่แล้ว"
        task.mark_complete()
        self._save_changes()
        return True, f"งาน ID {task_id} ถูกเปลี่ยนสถานะเป็น 'เสร็จสมบูรณ์ (Completed)' แล้ว"

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task is None:
            return False, f"ไม่พบงาน ID {task_id} ในระบบ"
        self.tasks.remove(task)
        self._save_changes()
        return True, f"ลบงาน ID {task_id} เรียบร้อยแล้ว"

    def get_all_tasks(self):
        return list(self.tasks)

    # ---------------------------------------------------------------- Assignment
    def search_tasks(self, keyword):
        """ค้นหา keyword ใน description หรือ tags (ไม่สนตัวพิมพ์เล็ก/ใหญ่)"""
        kw = keyword.lower()
        return [t for t in self.tasks
                if kw in t.description.lower() or any(kw in tag.lower() for tag in t.tags)]

    def filter_tasks(self, status=None, due_date_before=None, priority=None, tags=None):
        """
        กรองตามเงื่อนไขที่ระบุ (ทุกเงื่อนไขต้องเป็นจริง)
        status: True/False/None, due_date_before: 'YYYY-MM-DD' หรือ date,
        priority: 'High'/'Medium'/'Low', tags: str หรือ list (ต้องมีครบทุกแท็ก)
        """
        filtered = list(self.tasks)
        if status is not None:
            filtered = [t for t in filtered if t.completed == status]
        if due_date_before:
            if isinstance(due_date_before, str):
                due_date_before = datetime.datetime.strptime(due_date_before, "%Y-%m-%d").date()
            filtered = [t for t in filtered if isinstance(t, DueDateTask) and t.due_date <= due_date_before]
        if priority:
            filtered = [t for t in filtered
                        if isinstance(t, PriorityTask) and t.priority.lower() == priority.lower()]
        if tags:
            wanted = [tags] if isinstance(tags, str) else list(tags)
            wanted = [w.strip().lower() for w in wanted if w.strip()]
            filtered = [t for t in filtered if all(w in [tg.lower() for tg in t.tags] for w in wanted)]
        return filtered

    def sort_tasks(self, criterion="id", reverse=False):
        """
        เรียงตาม id / due_date / priority
        งานที่ไม่มี due_date หรือ priority ถูกกำหนดค่าให้อยู่ท้ายสุด (date.max / 99)
        """
        if criterion == "due_date":
            key = lambda t: (t.due_date if isinstance(t, DueDateTask) else datetime.date.max, t.id)  # noqa: E731
        elif criterion == "priority":
            key = lambda t: (self.PRIORITY_ORDER.get(t.priority, 99) if isinstance(t, PriorityTask) else 99, t.id)  # noqa: E731
        else:
            key = lambda t: t.id  # noqa: E731
        return sorted(self.tasks, key=key, reverse=reverse)
