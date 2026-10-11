# final_task_manager_project/main.py
"""Application entry point: สร้าง TaskManager และ CLIInterface แล้วเริ่มลูปการทำงาน"""
import sys

from src.cli_interface import CLIInterface
from src.task_manager import TaskManager


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # แสดงภาษาไทยได้ถูกต้องบน Windows
    manager = TaskManager("data/tasks.json")
    cli = CLIInterface(manager)
    try:
        cli.run()
    except (KeyboardInterrupt, EOFError):
        print("\n[Info] Program interrupted. All changes were already saved. Goodbye!")


if __name__ == "__main__":
    main()
