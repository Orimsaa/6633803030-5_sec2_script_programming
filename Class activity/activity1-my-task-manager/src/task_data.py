# my-task-manager/src/task_data.py
"""Persistence layer: โหลด/บันทึกรายการงานเป็นไฟล์ JSON"""
import json
import os

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'tasks.json')


def load_tasks():
    """Loads tasks from the JSON file. คืนค่า list ว่างถ้าไม่มีไฟล์ ไฟล์ว่าง หรือไฟล์เสีย"""
    if not os.path.exists(TASKS_FILE):
        os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting with an empty task list.")
        return []
    except OSError as e:
        print(f"Warning: could not read tasks.json ({e}). Starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Saves tasks to the JSON file. คืนค่า True เมื่อบันทึกสำเร็จ"""
    try:
        os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"[Error] Could not save tasks: {e}")
        return False
