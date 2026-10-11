# my-task-manager/src/task_logic.py
"""Business logic: เพิ่ม แสดง ค้นหา ทำเครื่องหมายเสร็จ และลบงาน"""

PRIORITIES = ("Low", "Medium", "High")


def get_next_task_id(tasks):
    """Generates a unique ID for a new task."""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


def add_task(tasks, description, priority="Medium"):
    """Adds a new task to the list."""
    priority = priority.strip().capitalize() or "Medium"
    if priority not in PRIORITIES:
        print(f"[Warning] Unknown priority '{priority}', using 'Medium'.")
        priority = "Medium"
    task_id = get_next_task_id(tasks)
    tasks.append({"id": task_id, "description": description, "completed": False, "priority": priority})
    print(f"[OK] Task '{description}' [{priority}] added with ID {task_id}.")
    return tasks


def list_tasks(tasks, status=None):
    """
    Lists tasks as a table.
    status: None = ทั้งหมด, 'pending' = ยังไม่เสร็จ, 'completed' = เสร็จแล้ว
    """
    shown = tasks
    if status == "pending":
        shown = [t for t in tasks if not t['completed']]
    elif status == "completed":
        shown = [t for t in tasks if t['completed']]
    if not shown:
        print("\nNo tasks found.")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<6}| {'Status':<12}| {'Priority':<10}| Description")
    print("-" * 60)
    for task in shown:
        status_text = "[DONE]" if task['completed'] else "[PENDING]"
        print(f"{'#' + str(task['id']):<6}| {status_text:<12}| {task.get('priority', 'Medium'):<10}| {task['description']}")
    print("=" * 60)
    done = sum(1 for t in tasks if t['completed'])
    print(f"Summary: {done}/{len(tasks)} task(s) completed.")


def search_tasks(tasks, keyword):
    """Shows tasks whose description contains the keyword (case-insensitive)."""
    matches = [t for t in tasks if keyword.lower() in t['description'].lower()]
    if not matches:
        print(f"No tasks match '{keyword}'.")
        return
    print(f"\nSearch results for '{keyword}':")
    list_tasks(matches)


def complete_task(tasks, task_id):
    """Marks a task as completed."""
    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print(f"Task ID {task_id} is already completed.")
            else:
                task['completed'] = True
                print(f"[OK] Task ID {task_id} marked as completed.")
            return tasks
    print(f"Error: Task with ID {task_id} not found.")
    return tasks


def delete_task(tasks, task_id):
    """Deletes a task from the list."""
    original_len = len(tasks)
    tasks[:] = [task for task in tasks if task['id'] != task_id]  # แก้ไข list เดิมแบบ in-place
    if len(tasks) < original_len:
        print(f"[OK] Task ID {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")
    return tasks
