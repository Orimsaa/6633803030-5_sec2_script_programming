# my-api-fetcher/main.py
"""Interactive CLI สำหรับดึงและประมวลผลข้อมูล JSON จาก Web API (Week 10)"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # ภาษาไทยบน Windows Console

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "src"))

from api_client import APIClient, export_to_json_file


def display_menu():
    print("\n" + "=" * 50)
    print("   Web API Data Fetcher CLI (Week 10)")
    print("=" * 50)
    print("  1. ดึงข้อมูลงานเดี่ยว (Fetch Single TODO)")
    print("  2. ดึงรายการโพสต์ทั้งหมด (Fetch All Posts)")
    print("  3. ดึงรายการ TODO ตามรหัสผู้ใช้ (Fetch User TODOs)")
    print("  4. ดึงข้อมูลโปรไฟล์ผู้ใช้ (Fetch User Profile)")
    print("  5. ดึงคอมเมนต์ของโพสต์ (Fetch Post Comments)")
    print("  6. ดึงข้อมูลแล้วบันทึกเป็นไฟล์ JSON (Fetch & Export)")
    print("  7. ออกจากโปรแกรม (Exit)")
    print("=" * 50)


def ask_positive_int(prompt):
    """Input validation: รับเฉพาะจำนวนเต็มบวก คืนค่า None ถ้าไม่ถูกต้อง"""
    raw = input(prompt).strip()
    try:
        value = int(raw)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print(f"[ERROR] '{raw}' ไม่ใช่จำนวนเต็มบวก กรุณาป้อนตัวเลข เช่น 1, 2, 3")
        return None


def show_single_todo(client):
    todo_id = ask_positive_int("ป้อน TODO ID (เช่น 1, 5, 10): ")
    if todo_id is None:
        return
    todo = client.fetch_single_todo(todo_id)
    if not todo:
        print(f"ไม่พบข้อมูล TODO ID {todo_id}")
        return
    print("\n--- ข้อมูลงาน TODO ---")
    print(f"  ID       : {todo['id']}")
    print(f"  User ID  : {todo['userId']}")
    print(f"  Title    : {todo['title']}")
    print(f"  Status   : {'Completed' if todo['completed'] else 'Pending'}")


def show_all_posts(client, limit=5):
    posts = client.fetch_all_posts()
    if not posts:
        print("ไม่สามารถดึงรายการโพสต์ได้")
        return
    print(f"\n--- แสดง {limit} โพสต์แรก (จากทั้งหมด {len(posts)} โพสต์) ---")
    for i, post in enumerate(posts[:limit], start=1):
        body = post["body"].replace("\n", " ")
        print(f"[{i}] Post ID: {post['id']} | User ID: {post['userId']}")
        print(f"    Title: {post['title']}")
        print(f"    Body : {body[:60]}...")
    print(f"... และอีก {len(posts) - limit} โพสต์")


def show_user_todos(client):
    user_id = ask_positive_int("ป้อน User ID (เช่น 1, 2, 3): ")
    if user_id is None:
        return
    todos = client.fetch_user_todos(user_id)
    if todos is None:
        return
    if not todos:
        print(f"ไม่พบ TODO ของ User ID {user_id}")
        return
    done = sum(1 for t in todos if t["completed"])
    print(f"\n--- TODO ของ User ID {user_id} ({len(todos)} รายการ) ---")
    for t in todos:
        print(f"  [{t['id']:03d}] {'[x]' if t['completed'] else '[ ]'} {t['title']}")
    print(f"สรุป: เสร็จแล้ว {done}/{len(todos)} งาน | ค้างอยู่ {len(todos) - done} งาน")


def show_user_profile(client):
    user_id = ask_positive_int("ป้อน User ID (1-10): ")
    if user_id is None:
        return
    user = client.fetch_user_profile(user_id)
    if not user:
        print(f"ไม่พบผู้ใช้ ID {user_id}")
        return
    # เข้าถึง nested dictionary อย่างปลอดภัยด้วย .get(..., {})
    print("\n--- โปรไฟล์ผู้ใช้ ---")
    print(f"  ชื่อ-นามสกุล : {user.get('name', '-')}")
    print(f"  Username    : {user.get('username', '-')}")
    print(f"  อีเมล        : {user.get('email', '-')}")
    print(f"  โทรศัพท์     : {user.get('phone', '-')}")
    print(f"  บริษัท       : {user.get('company', {}).get('name', '-')}")
    print(f"  เมือง        : {user.get('address', {}).get('city', '-')}")


def show_post_comments(client, limit=3):
    post_id = ask_positive_int("ป้อน Post ID (1-100): ")
    if post_id is None:
        return
    comments = client.fetch_post_comments(post_id)
    if comments is None:
        return
    print(f"\n--- คอมเมนต์ของโพสต์ {post_id}: พบทั้งหมด {len(comments)} คอมเมนต์ ---")
    for i, c in enumerate(comments[:limit], start=1):
        print(f"[{i}] {c['name']} <{c['email']}>")
        print(f"    {c['body'].replace(chr(10), ' ')[:80]}...")


def fetch_and_export(client):
    print("เลือกข้อมูลที่จะบันทึก: 1) TODO ของผู้ใช้  2) โปรไฟล์ผู้ใช้  3) คอมเมนต์ของโพสต์")
    kind = input("เลือก (1-3): ").strip()
    if kind not in ("1", "2", "3"):
        print("[ERROR] กรุณาเลือก 1, 2 หรือ 3")
        return
    item_id = ask_positive_int("ป้อน ID: ")
    if item_id is None:
        return
    fetchers = {
        "1": (client.fetch_user_todos, f"user_{item_id}_todos.json"),
        "2": (client.fetch_user_profile, f"user_{item_id}_profile.json"),
        "3": (client.fetch_post_comments, f"post_{item_id}_comments.json"),
    }
    fetch, filename = fetchers[kind]
    data = fetch(item_id)
    if data:
        export_to_json_file(os.path.join(BASE_DIR, "exports", filename), data)
    else:
        print("ไม่มีข้อมูลให้บันทึก")


def main():
    client = APIClient()
    actions = {"1": show_single_todo, "2": show_all_posts, "3": show_user_todos,
               "4": show_user_profile, "5": show_post_comments, "6": fetch_and_export}
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-7): ").strip()
        if choice == "7":
            print("ขอบคุณที่ใช้งานโปรแกรม!")
            break
        action = actions.get(choice)
        if action:
            action(client)
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาป้อนตัวเลข 1 ถึง 7")


if __name__ == "__main__":
    main()
