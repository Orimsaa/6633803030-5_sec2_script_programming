# Presentation Outline (5–7 นาที)

1. **Introduction** — แนะนำตัว (อัษฎาวุธ เรือนแก้ว 663380303-5) และเป้าหมาย: Task Manager CLI ที่ใช้ OOP เต็มรูปแบบ
2. **Problem Solved** — จดงานหลายแบบ (มีกำหนดส่ง/มีความสำคัญ) แล้วหา/กรอง/เรียงงานที่ต้องทำก่อนได้เร็ว ข้อมูลไม่หายเมื่อปิดโปรแกรม
3. **Live Demo** (ใช้ข้อมูลตัวอย่างใน `data/tasks.json`)
   - `4` แสดงทั้งหมด → `2` เพิ่ม "Final Project Submission" due `2026-10-15` tags `study, urgent, final`
   - `7` ค้นหา `urgent` → `8` กรอง due ก่อน `2026-10-31` + tag `study` → `9` เรียงตาม `priority`
   - ทดสอบ input ผิด: วันที่ `31/12/2026`, priority `urgent`, ID `abc`
   - สำรอง: ภาพใน `screenshots/` กรณี demo มีปัญหา
4. **Software Architecture** — แผนภาพใน `PLAN.md`: CLI → TaskManager → DataPersistence, คลาสลูก DueDateTask/PriorityTask
5. **Technical Challenges** — Polymorphic sort (งานไม่มีวันส่งต้องอยู่ท้ายทั้งสองทิศทาง), การโหลด `_type`, atomic save
6. **Lessons Learned** — แยกชั้นทำให้ทดสอบง่าย, validate สองชั้น, คิดถึงค่าว่างตั้งแต่ออกแบบ
7. **Future Work & Q&A** — RecurringTask, แจ้งเตือน, SQLite, GUI
