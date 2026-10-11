# enhanced-task-manager-design/main.py
"""Orchestrator: สร้าง TaskManager (logic + persistence) แล้วส่งให้ CLIInterface"""
import sys

from src.cli_interface import CLIInterface
from src.task_manager import TaskManager

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    CLIInterface(TaskManager()).run()
