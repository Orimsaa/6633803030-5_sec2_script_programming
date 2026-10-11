# final_task_manager_project/src/task.py
"""
Domain models ของ Task Manager
- Task         : งานทั่วไป (id, description, completed, tags)
- DueDateTask  : สืบทอดจาก Task เพิ่มวันกำหนดส่ง (due_date)
- PriorityTask : สืบทอดจาก Task เพิ่มระดับความสำคัญ (High / Medium / Low)
"""
import datetime

DATE_FORMAT = "%Y-%m-%d"
VALID_PRIORITIES = ("High", "Medium", "Low")


def normalize_tag(tag):
    """ตัดช่องว่างและแปลงเป็นตัวพิมพ์เล็ก เพื่อให้ 'Study ' กับ 'study' เป็นแท็กเดียวกัน"""
    return str(tag).strip().lower()


class Task:
    """งานทั่วไปในระบบ"""

    def __init__(self, id, description, completed=False, tags=None):
        if not str(description).strip():
            raise ValueError("Task description cannot be empty.")
        self.id = int(id)
        self.description = str(description).strip()
        self.completed = bool(completed)
        self.tags = []
        for tag in tags or []:
            self.add_tag(tag)

    def mark_complete(self):
        self.completed = True

    def add_tag(self, tag):
        """เพิ่มแท็ก (normalize แล้ว) โดยไม่ให้ซ้ำ คืนค่า True ถ้าเพิ่มสำเร็จ"""
        cleaned = normalize_tag(tag)
        if cleaned and cleaned not in self.tags:
            self.tags.append(cleaned)
            return True
        return False

    def remove_tag(self, tag):
        """ลบแท็ก คืนค่า True ถ้าพบและลบแล้ว"""
        cleaned = normalize_tag(tag)
        if cleaned in self.tags:
            self.tags.remove(cleaned)
            return True
        return False

    def has_tag(self, tag):
        return normalize_tag(tag) in self.tags

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "tags": list(self.tags),
            "_type": "Task",
        }

    def _extra_info(self):
        """ส่วนข้อมูลเฉพาะของคลาสลูก (override เพื่อแทรกก่อน Tags)"""
        return ""

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        text = f"ID: {self.id} | Description: {self.description} | Status: {status}{self._extra_info()}"
        if self.tags:
            text += f" | Tags: {', '.join(self.tags)}"
        return text

    def __repr__(self):
        return (f"{type(self).__name__}(id={self.id}, description={self.description!r}, "
                f"completed={self.completed}, tags={self.tags})")


class DueDateTask(Task):
    """งานที่มีวันกำหนดส่ง"""

    def __init__(self, id, description, due_date, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        if isinstance(due_date, datetime.datetime):
            due_date = due_date.date()
        if isinstance(due_date, datetime.date):
            self.due_date = due_date
        elif isinstance(due_date, str):
            try:
                self.due_date = datetime.datetime.strptime(due_date.strip(), DATE_FORMAT).date()
            except ValueError:
                raise ValueError(f"Invalid due date '{due_date}'. Use YYYY-MM-DD.")
        else:
            raise TypeError("due_date must be a 'YYYY-MM-DD' string or datetime.date")

    def is_overdue(self, today=None):
        today = today or datetime.date.today()
        return not self.completed and self.due_date < today

    def to_dict(self):
        data = super().to_dict()
        data["due_date"] = self.due_date.strftime(DATE_FORMAT)
        data["_type"] = "DueDateTask"
        return data

    def _extra_info(self):
        overdue = " (OVERDUE)" if self.is_overdue() else ""
        return f" | Due: {self.due_date.strftime(DATE_FORMAT)}{overdue}"


class PriorityTask(Task):
    """งานที่มีระดับความสำคัญ"""

    def __init__(self, id, description, priority, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        value = str(priority).strip().capitalize()
        if value not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Choose from {', '.join(VALID_PRIORITIES)}.")
        self.priority = value

    def to_dict(self):
        data = super().to_dict()
        data["priority"] = self.priority
        data["_type"] = "PriorityTask"
        return data

    def _extra_info(self):
        return f" | Priority: {self.priority}"
