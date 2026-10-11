# final_task_manager_project/src/cli_interface.py
"""Presentation layer: เมนู, รับ input พร้อม validation และแสดงผล (ไม่มี business logic)"""
import datetime


class CLIInterface:
    def __init__(self, task_manager):
        self.manager = task_manager

    # ------------------------------------------------------------------ display
    @staticmethod
    def display_menu():
        print("\n==================================")
        print("--- Enhanced Task Manager Menu ---")
        print("==================================")
        print("1. Add Normal Task")
        print("2. Add Due Date Task")
        print("3. Add Priority Task")
        print("4. List All Tasks")
        print("5. Complete Task")
        print("6. Delete Task")
        print("7. Search Tasks")
        print("8. Filter Tasks")
        print("9. Sort Tasks")
        print("0. Exit")
        print("----------------------------------")

    @staticmethod
    def display_tasks(tasks, title="Your Tasks"):
        if not tasks:
            print(f"\n[Info] No tasks to show ({title}).")
            return
        print(f"\n--- {title} (Total: {len(tasks)}) ---")
        for task in tasks:
            print(f"  * {task}")
        print("------------------------------------------")

    # ------------------------------------------------------------------ input helpers
    @staticmethod
    def ask_description():
        while True:
            text = input("Enter task description: ").strip()
            if text:
                return text
            print("[Error] Task description cannot be empty. Please try again.")

    @staticmethod
    def ask_date(prompt, allow_blank=False):
        while True:
            text = input(prompt).strip()
            if not text and allow_blank:
                return None
            try:
                return datetime.datetime.strptime(text, "%Y-%m-%d").date()
            except ValueError:
                print("[Error] Invalid date format. Please use YYYY-MM-DD (e.g., 2026-12-31).")

    @staticmethod
    def ask_priority(prompt="Enter priority (High/Medium/Low): ", allow_blank=False):
        while True:
            text = input(prompt).strip().capitalize()
            if not text and allow_blank:
                return None
            if text in ("High", "Medium", "Low"):
                return text
            print("[Error] Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

    @staticmethod
    def ask_tags(prompt="Enter tags (comma-separated, e.g., study,project,urgent - optional): "):
        text = input(prompt).strip()
        return [t.strip().lower() for t in text.split(",") if t.strip()] if text else []

    @staticmethod
    def ask_task_id(prompt):
        text = input(prompt).strip().lstrip("#")
        try:
            value = int(text)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print(f"[Error] '{text}' is not a valid task ID. Please enter a positive number.")
            return None

    @staticmethod
    def ask_yes_no(prompt):
        return input(prompt).strip().lower() in ("y", "yes")

    # ------------------------------------------------------------------ actions
    def _filter_flow(self):
        print("\nFilter options (press Enter to skip a condition):")
        while True:
            status_in = input("Completed status (completed/pending): ").strip().lower()
            if status_in in ("", "completed", "pending"):
                break
            print("[Error] Please type 'completed', 'pending' or leave it blank.")
        status = {"completed": True, "pending": False}.get(status_in)
        before = self.ask_date("Due date before (YYYY-MM-DD): ", allow_blank=True)
        after = self.ask_date("Due date after (YYYY-MM-DD): ", allow_blank=True)
        priority = self.ask_priority("Priority (High/Medium/Low): ", allow_blank=True)
        tags = self.ask_tags("Must have tags (comma-separated): ")
        result = self.manager.filter_tasks(status=status, due_date_before=before, due_date_after=after,
                                           priority_level=priority, contains_tags=tags)
        self.display_tasks(result, "Filtered Tasks")

    def _sort_flow(self):
        criteria = "/".join(self.manager.SORT_CRITERIA)
        while True:
            criterion = input(f"Sort by ({criteria}) [id]: ").strip().lower() or "id"
            if criterion in self.manager.SORT_CRITERIA:
                break
            print(f"[Error] Unknown criterion. Choose one of: {criteria}.")
        reverse = self.ask_yes_no("Descending order? (y/n) [n]: ")
        order = "descending" if reverse else "ascending"
        self.display_tasks(self.manager.sort_tasks(criterion, reverse), f"Tasks sorted by {criterion} ({order})")

    def run(self):
        for warning in self.manager.load_warnings:
            print(f"[Warning] {warning}")
        print(f"Loaded {len(self.manager.tasks)} task(s) from data/tasks.json")

        while True:
            self.display_menu()
            choice = input("Enter your choice (0-9): ").strip()
            try:
                if choice == "1":
                    task = self.manager.add_normal_task(self.ask_description(), self.ask_tags())
                    print(f"[Success] Normal Task '{task.description}' added with ID {task.id}.")
                elif choice == "2":
                    desc = self.ask_description()
                    due = self.ask_date("Enter due date (YYYY-MM-DD): ")
                    task = self.manager.add_due_date_task(desc, due, self.ask_tags())
                    print(f"[Success] Due Date Task '{task.description}' (due {task.due_date}) added with ID {task.id}.")
                elif choice == "3":
                    desc = self.ask_description()
                    priority = self.ask_priority()
                    task = self.manager.add_priority_task(desc, priority, self.ask_tags())
                    print(f"[Success] Priority Task '{task.description}' ({task.priority}) added with ID {task.id}.")
                elif choice == "4":
                    self.display_tasks(self.manager.get_all_tasks())
                elif choice == "5":
                    task_id = self.ask_task_id("Enter ID of task to complete: ")
                    if task_id is not None:
                        ok, msg = self.manager.complete_task(task_id)
                        print(f"[{'Success' if ok else 'Info'}] {msg}")
                elif choice == "6":
                    task_id = self.ask_task_id("Enter ID of task to delete: ")
                    if task_id is not None:
                        if self.ask_yes_no(f"Delete task ID {task_id}? (y/n): "):
                            ok, msg = self.manager.delete_task(task_id)
                            print(f"[{'Success' if ok else 'Info'}] {msg}")
                        else:
                            print("[Info] Deletion cancelled.")
                elif choice == "7":
                    keyword = input("Enter keyword to search (description or tag): ").strip()
                    if not keyword:
                        print("[Error] Keyword cannot be empty.")
                    else:
                        self.display_tasks(self.manager.search_tasks(keyword), f"Search results for '{keyword}'")
                elif choice == "8":
                    self._filter_flow()
                elif choice == "9":
                    self._sort_flow()
                elif choice == "0":
                    print("All changes are saved. Goodbye!")
                    break
                else:
                    print("[Error] Invalid choice. Please enter a number from 0 to 9.")
            except (ValueError, TypeError) as e:
                print(f"[Error] {e}")
            except OSError as e:
                print(f"[Error] Could not save tasks: {e}")
