# my-task-manager/main.py
import os
import sys

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import task_data
import task_logic


def display_menu():
    """Displays the main menu options to the user."""
    print("\n" + "=" * 32)
    print("        TASK MANAGER CLI")
    print("=" * 32)
    print("  1. Add New Task")
    print("  2. List All Tasks")
    print("  3. List Pending Tasks")
    print("  4. List Completed Tasks")
    print("  5. Search Tasks by Keyword")
    print("  6. Mark Task as Completed")
    print("  7. Delete Task")
    print("  8. Save and Exit")
    print("=" * 32)


def read_task_id(prompt):
    """อ่าน ID จากผู้ใช้ คืนค่า None ถ้าไม่ใช่ตัวเลข (ไม่ให้โปรแกรม crash)"""
    raw = input(prompt).strip().lstrip('#')
    try:
        return int(raw)
    except ValueError:
        print("Invalid input. Please enter a number for Task ID.")
        return None


def main():
    """Main function to run the Task Manager application."""
    tasks = task_data.load_tasks()  # Load tasks at startup
    try:
        while True:
            display_menu()
            choice = input("Enter choice (1-8): ").strip()

            if choice == '1':
                description = input("Enter task description: ").strip()
                if not description:
                    print("Task description cannot be empty.")
                    continue
                priority = input("Enter priority (Low/Medium/High) [Medium]: ")
                tasks = task_logic.add_task(tasks, description, priority)
                task_data.save_tasks(tasks)
            elif choice == '2':
                task_logic.list_tasks(tasks)
            elif choice == '3':
                task_logic.list_tasks(tasks, status="pending")
            elif choice == '4':
                task_logic.list_tasks(tasks, status="completed")
            elif choice == '5':
                keyword = input("Enter keyword: ").strip()
                if keyword:
                    task_logic.search_tasks(tasks, keyword)
                else:
                    print("Keyword cannot be empty.")
            elif choice == '6':
                task_id = read_task_id("Enter ID of task to complete: ")
                if task_id is not None:
                    tasks = task_logic.complete_task(tasks, task_id)
                    task_data.save_tasks(tasks)
            elif choice == '7':
                task_id = read_task_id("Enter ID of task to delete: ")
                if task_id is not None:
                    tasks = task_logic.delete_task(tasks, task_id)
                    task_data.save_tasks(tasks)
            elif choice == '8':
                print("Saving tasks and exiting. Goodbye!")
                task_data.save_tasks(tasks)  # Save tasks before exiting
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
    except (KeyboardInterrupt, EOFError):
        # กด Ctrl+C: บันทึกก่อนออก ข้อมูลไม่หาย
        print("\nInterrupted. Saving tasks before exit...")
        task_data.save_tasks(tasks)


if __name__ == "__main__":
    main()
