# final_task_manager_project/src/task_manager.py
"""Business logic: CRUD, Search, Filter (หลายเงื่อนไข) และ Sort (polymorphic)"""
import datetime

try:
    from .data_persistence import DataPersistence
    from .task import DueDateTask, PriorityTask, Task, normalize_tag
except ImportError:
    from data_persistence import DataPersistence
    from task import DueDateTask, PriorityTask, Task, normalize_tag


def _to_date(value):
    """รับ 'YYYY-MM-DD' หรือ datetime.date แล้วคืนค่า datetime.date (None ถ้าไม่ได้ระบุ)"""
    if value is None or value == "":
        return None
    if isinstance(value, datetime.date):
        return value
    return datetime.datetime.strptime(str(value).strip(), "%Y-%m-%d").date()


class TaskManager:
    PRIORITY_MAP = {"High": 1, "Medium": 2, "Low": 3}
    SORT_CRITERIA = ("id", "description", "completed", "due_date", "priority")

    def __init__(self, data_file="data/tasks.json"):
        self.persistence = DataPersistence(data_file)
        self.tasks = self.persistence.load_tasks()
        self.next_id = self._get_next_task_id()

    @property
    def load_warnings(self):
        return self.persistence.warnings

    def _get_next_task_id(self):
        return max((task.id for task in self.tasks), default=0) + 1

    def _add(self, task):
        self.tasks.append(task)
        self.next_id += 1
        self.persistence.save_tasks(self.tasks)
        return task

    # ------------------------------------------------------------------ CRUD
    def add_normal_task(self, description, tags=None):
        return self._add(Task(self.next_id, description, tags=tags))

    def add_due_date_task(self, description, due_date, tags=None):
        return self._add(DueDateTask(self.next_id, description, due_date, tags=tags))

    def add_priority_task(self, description, priority, tags=None):
        return self._add(PriorityTask(self.next_id, description, priority, tags=tags))

    def get_task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def get_all_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task is None:
            return False, f"Task ID {task_id} not found."
        if task.completed:
            return False, f"Task ID {task_id} is already completed."
        task.mark_complete()
        self.persistence.save_tasks(self.tasks)
        return True, f"Task ID {task_id} marked as completed."

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task is None:
            return False, f"Task ID {task_id} not found."
        self.tasks.remove(task)
        self.persistence.save_tasks(self.tasks)
        return True, f"Task ID {task_id} ('{task.description}') deleted."

    # ------------------------------------------------------------------ Search / Filter / Sort
    def search_tasks(self, keyword):
        """ค้นหาแบบ partial match ไม่สนตัวพิมพ์เล็ก-ใหญ่ ทั้งใน description และ tags"""
        kw = (keyword or "").strip().lower()
        if not kw:
            return []
        return [t for t in self.tasks
                if kw in t.description.lower() or any(kw in tag for tag in t.tags)]

    def filter_tasks(self, status=None, due_date_before=None, due_date_after=None,
                     priority_level=None, contains_tags=None):
        """
        กรองหลายเงื่อนไขพร้อมกัน (AND)
        status: True=เสร็จแล้ว / False=ยังไม่เสร็จ / None=ไม่กรอง
        due_date_before / due_date_after: เฉพาะ DueDateTask ที่ due_date <= before และ >= after
        priority_level: เฉพาะ PriorityTask ที่ระดับตรงกัน
        contains_tags: งานต้องมีแท็ก "ครบทุกตัว" ที่ระบุ (list หรือ str คั่นด้วย comma)
        """
        before, after = _to_date(due_date_before), _to_date(due_date_after)
        if isinstance(contains_tags, str):
            contains_tags = contains_tags.split(",")
        wanted_tags = [normalize_tag(t) for t in contains_tags or [] if normalize_tag(t)]

        result = list(self.tasks)
        if status is not None:
            result = [t for t in result if t.completed == status]
        if before:
            result = [t for t in result if isinstance(t, DueDateTask) and t.due_date <= before]
        if after:
            result = [t for t in result if isinstance(t, DueDateTask) and t.due_date >= after]
        if priority_level:
            level = str(priority_level).strip().capitalize()
            result = [t for t in result if isinstance(t, PriorityTask) and t.priority == level]
        if wanted_tags:
            result = [t for t in result if all(tag in t.tags for tag in wanted_tags)]
        return result

    def sort_tasks(self, criterion="id", reverse=False):
        """
        เรียงงานตาม id / description / completed / due_date / priority
        งานที่ไม่มีค่าสำหรับเกณฑ์นั้น (เช่น Task ทั่วไปเมื่อเรียงตาม due_date) จะอยู่ท้ายสุดเสมอ
        ไม่ว่าจะเรียงจากน้อยไปมากหรือมากไปน้อย
        """
        if criterion not in self.SORT_CRITERIA:
            raise ValueError(f"Unknown sort criterion '{criterion}'. Use one of {', '.join(self.SORT_CRITERIA)}.")

        if criterion == "due_date":
            keyed = [t for t in self.tasks if isinstance(t, DueDateTask)]
            rest = [t for t in self.tasks if not isinstance(t, DueDateTask)]
            keyed.sort(key=lambda t: (t.due_date, t.id), reverse=reverse)
            return keyed + sorted(rest, key=lambda t: t.id)
        if criterion == "priority":
            keyed = [t for t in self.tasks if isinstance(t, PriorityTask)]
            rest = [t for t in self.tasks if not isinstance(t, PriorityTask)]
            # reverse=False: High -> Medium -> Low
            keyed.sort(key=lambda t: (self.PRIORITY_MAP[t.priority], t.id), reverse=reverse)
            return keyed + sorted(rest, key=lambda t: t.id)

        key_funcs = {
            "id": lambda t: t.id,
            "description": lambda t: (t.description.lower(), t.id),
            "completed": lambda t: (t.completed, t.id),
        }
        return sorted(self.tasks, key=key_funcs[criterion], reverse=reverse)
