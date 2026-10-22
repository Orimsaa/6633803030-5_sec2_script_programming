# ============================================================
# Lab 5.2: Course Enrollment & Collaboration (Set Focus)
# ------------------------------------------------------------
# จำลองการลงทะเบียนเรียนและใช้ Set Operations เปรียบเทียบรายชื่อ
# ============================================================

# กำหนดเซตของนักศึกษาในแต่ละรายวิชา
python_students = {"S001", "S003", "S005", "S007", "S009"}
java_students = {"S002", "S003", "S006", "S007", "S010"}

print(f"Python Students: {python_students}")
print(f"Java Students:   {java_students}\n")


# --- ข้อที่ 3: หานักศึกษาที่เรียนทั้ง 2 วิชา (Intersection) ---
both_courses = python_students.intersection(java_students)
print(f"Students in Both Courses: {both_courses}")


# --- ข้อที่ 4: หานักศึกษาทั้งหมดแบบไม่ซ้ำกัน (Union) ---
all_unique_students = python_students.union(java_students)
print(f"All Unique Students: {all_unique_students}")


# --- ข้อที่ 5: หานักศึกษาที่เรียนเฉพาะวิชา Python เท่านั้น (Difference) ---
only_python = python_students.difference(java_students)
print(f"Students Only in Python: {only_python}")


# --- ข้อที่ 6: หานักศึกษาที่เรียนเพียงวิชาใดวิชาหนึ่ง (Symmetric Difference) ---
exclusive_students = python_students.symmetric_difference(java_students)
print(f"Students in Only One Course: {exclusive_students}\n")


# --- ข้อที่ 7: การลบข้อมูลซ้ำออกจาก List ---
all_students_list = ["S001", "S003", "S005", "S001", "S002"]
print(f"Original List (with duplicates): {all_students_list}")

# แปลง list -> set -> list เพื่อลบตัวซ้ำ
unique_students_list = list(set(all_students_list))
print(f"Unique List (after removing duplicates): {unique_students_list}")
