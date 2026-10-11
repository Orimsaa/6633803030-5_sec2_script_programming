# enhanced-task-manager-design/src/task.py
"""Domain models: Task (มี tags), DueDateTask และ PriorityTask (Inheritance + Method overriding)"""
import datetime


class Task:
    def __init__(self, id, description, completed=False, tags=None):
        self.id = id
        self.description = description
        self.completed = completed
        self.tags = []
        for tag in tags or []:
            self.add_tag(tag)

    def mark_complete(self):
        self.completed = True

    def add_tag(self, tag):
        cleaned = tag.strip()
        if cleaned and cleaned not in self.tags:
            self.tags.append(cleaned)

    def remove_tag(self, tag):
        if tag.strip() in self.tags:
            self.tags.remove(tag.strip())

    def to_dict(self):
        return {"id": self.id, "description": self.description, "completed": self.completed,
                "tags": self.tags, "_type": "Task"}

    def _details(self):
        return ""

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        tags = f" | Tags: {', '.join(self.tags)}" if self.tags else ""
        return f"ID: {self.id} | Description: {self.description} | Status: {status}{self._details()}{tags}"

    def __repr__(self):
        return f"{type(self).__name__}(id={self.id}, description={self.description!r})"


class DueDateTask(Task):
    def __init__(self, id, description, due_date, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        if isinstance(due_date, str):
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        self.due_date = due_date

    def to_dict(self):
        data = super().to_dict()
        data.update({"due_date": self.due_date.strftime("%Y-%m-%d"), "_type": "DueDateTask"})
        return data

    def _details(self):
        return f" | Due: {self.due_date.strftime('%Y-%m-%d')}"


class PriorityTask(Task):
    def __init__(self, id, description, priority, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        self.priority = priority.capitalize()

    def to_dict(self):
        data = super().to_dict()
        data.update({"priority": self.priority, "_type": "PriorityTask"})
        return data

    def _details(self):
        return f" | Priority: {self.priority}"
