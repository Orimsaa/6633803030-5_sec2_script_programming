# enhanced-task-manager-design/src/cli_interface.py
"""Presentation layer: เมนู รับข้อมูล และตรวจสอบความถูกต้องของ input (ไม่มี business logic)"""
import datetime


class CLIInterface:
    def __init__(self, task_manager):
        self.manager = task_manager

    @staticmethod
    def display_menu():
        print("\n" + "=" * 45)
        print("     Enhanced Task Manager (Week 11)")
        print("=" * 45)
        print("1. เพิ่มงานทั่วไป (Add Normal Task)")
        print("2. เพิ่มงานที่มีวันครบกำหนด (Add Due Date Task)")
        print("3. เพิ่มงานที่มีระดับความสำคัญ (Add Priority Task)")
        print("4. แสดงรายการงานทั้งหมด (List All Tasks)")
        print("5. เปลี่ยนสถานะงานเป็นเสร็จสิ้น (Complete Task)")
        print("6. ลบงาน (Delete Task)")
        print("7. ค้นหางาน (Search Tasks)")
        print("8. กรองงาน (Filter Tasks)")
        print("9. เรียงลำดับงาน (Sort Tasks)")
        print("0. ออกจากโปรแกรม (Exit)")
        print("-" * 45)

    @staticmethod
    def show(tasks, title):
        if not tasks:
            print(f"\n[แจ้งเตือน]: ไม่พบงาน ({title})")
            return
        print(f"\n--- {title} ({len(tasks)} รายการ) ---")
        for task in tasks:
            print(f"- {task}")
        print("-" * 35)

    @staticmethod
    def get_description():
        while True:
            text = input("กรอกรายละเอียดงาน (Description): ").strip()
            if text:
                return text
            print("ข้อผิดพลาด: รายละเอียดงานต้องไม่เป็นค่าว่าง กรุณาลองใหม่อีกครั้ง")

    @staticmethod
    def get_date(prompt, allow_blank=False):
        while True:
            text = input(prompt).strip()
            if allow_blank and not text:
                return None
            try:
                datetime.datetime.strptime(text, "%Y-%m-%d")
                return text
            except ValueError:
                print("รูปแบบวันที่ไม่ถูกต้อง! กรุณาใช้รูปแบบ YYYY-MM-DD (เช่น 2026-10-30)")

    @staticmethod
    def get_priority(prompt="กรอกระดับความสำคัญ (High / Medium / Low): ", allow_blank=False):
        while True:
            text = input(prompt).strip().capitalize()
            if allow_blank and not text:
                return None
            if text in ("High", "Medium", "Low"):
                return text
            print("ระดับความสำคัญไม่ถูกต้อง! กรุณากรอก 'High', 'Medium', หรือ 'Low'")

    @staticmethod
    def get_tags():
        text = input("กรอกป้ายกำกับ (Tags คั่นด้วยจุลภาค เช่น work,urgent - หรือเว้นว่าง): ").strip()
        return [t.strip() for t in text.split(",") if t.strip()]

    @staticmethod
    def get_id(prompt):
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("ข้อผิดพลาด: ID ต้องเป็นตัวเลขจำนวนเต็มเท่านั้น")
            return None

    def run(self):
        print("ยินดีต้อนรับสู่ระบบ Enhanced Task Manager!")
        while True:
            self.display_menu()
            choice = input("เลือกเมนู (0-9): ").strip()
            if choice == "1":
                task = self.manager.add_normal_task(self.get_description(), self.get_tags())
                print(f"[สำเร็จ]: เพิ่มงานทั่วไป ID {task.id} เรียบร้อยแล้ว")
            elif choice == "2":
                desc, due = self.get_description(), self.get_date("กรอกวันครบกำหนด (YYYY-MM-DD): ")
                task = self.manager.add_due_date_task(desc, due, self.get_tags())
                print(f"[สำเร็จ]: เพิ่มงานครบกำหนด ID {task.id} (ครบกำหนด: {task.due_date}) เรียบร้อยแล้ว")
            elif choice == "3":
                desc, prio = self.get_description(), self.get_priority()
                task = self.manager.add_priority_task(desc, prio, self.get_tags())
                print(f"[สำเร็จ]: เพิ่มงานความสำคัญ ID {task.id} (ระดับ: {task.priority}) เรียบร้อยแล้ว")
            elif choice == "4":
                self.show(self.manager.get_all_tasks(), "รายการงานทั้งหมด")
            elif choice in ("5", "6"):
                task_id = self.get_id("กรอก ID ของงาน: ")
                if task_id is not None:
                    action = self.manager.complete_task if choice == "5" else self.manager.delete_task
                    ok, message = action(task_id)
                    print(f"{'[สำเร็จ]' if ok else '[แจ้งเตือน]'}: {message}")
            elif choice == "7":
                keyword = input("กรอกคำค้นหา (Keyword): ").strip()
                if keyword:
                    self.show(self.manager.search_tasks(keyword), f"ผลการค้นหา '{keyword}'")
                else:
                    print("ข้อผิดพลาด: กรุณากรอกคำค้นหา")
            elif choice == "8":
                print("\nตัวเลือกการกรอง (เว้นว่างได้หากไม่ต้องการกรองเงื่อนไขนั้น):")
                status_in = input("กรองตามสถานะ (completed/pending/เว้นว่าง): ").strip().lower()
                status = {"completed": True, "pending": False}.get(status_in)
                due = self.get_date("กรองงานครบกำหนดก่อนวันที่ (YYYY-MM-DD/เว้นว่าง): ", allow_blank=True)
                prio = self.get_priority("กรองตามความสำคัญ (High/Medium/Low/เว้นว่าง): ", allow_blank=True)
                tag = input("กรองตาม Tag (เว้นว่างได้): ").strip() or None
                self.show(self.manager.filter_tasks(status, due, prio, tag), "ผลการกรองงาน")
            elif choice == "9":
                criterion = input("เรียงตาม (id / due_date / priority) [id]: ").strip().lower() or "id"
                if criterion not in ("id", "due_date", "priority"):
                    print("ข้อผิดพลาด: เกณฑ์ไม่ถูกต้อง ใช้ค่าเริ่มต้น id")
                    criterion = "id"
                reverse = input("เรียงจากมากไปน้อย (y/n) [n]: ").strip().lower() in ("y", "yes")
                self.show(self.manager.sort_tasks(criterion, reverse), f"รายการงานที่จัดเรียงแล้ว (เกณฑ์: {criterion})")
            elif choice == "0":
                print("\nขอบคุณที่ใช้งาน Enhanced Task Manager! ลาก่อน")
                break
            else:
                print("ตัวเลือกไม่ถูกต้อง! กรุณากรอกหมายเลขระหว่าง 0 ถึง 9")
