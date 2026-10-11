# my-oop-task-manager/src/task.py


class Task:
    """
    แทนงาน 1 รายการ (Single Task)

    Attributes:
        id (int): รหัสงานที่ไม่ซ้ำกัน
        description (str): รายละเอียดงาน
        completed (bool): True = เสร็จแล้ว, False = ยังไม่เสร็จ
    """

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

    def to_dict(self):
        """แปลง object เป็น dictionary สำหรับบันทึกลง JSON"""
        return {"id": self.id, "description": self.description, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        """สร้าง Task กลับจาก dictionary ที่อ่านจาก JSON"""
        return cls(data["id"], data["description"], data.get("completed", False))

    def __str__(self):
        """User-friendly representation (ใช้กับ print)"""
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id} | Description: {self.description} | Status: {status}"

    def __repr__(self):
        """Developer-friendly representation (ใช้ตอน debug)"""
        return f"Task(id={self.id}, description='{self.description}', completed={self.completed})"
