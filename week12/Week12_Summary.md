# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 12: Final Project & Agentic Communication (Email & SMS)

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 12)
- **LO 12.1:** สามารถพัฒนาโปรแกรมหลายโมดูลแบบ OOP (Inheritance, Overriding, Polymorphism, Encapsulation) แยกชั้น UI / Logic / Data ได้
- **LO 12.2:** สามารถเขียน Search, Multi-criteria Filter และ Polymorphic Sort สำหรับ object ต่างชนิดกันได้
- **LO 12.3:** สามารถเขียน Unit Test ด้วย `unittest` ที่ครอบคลุมทั้ง logic และ persistence ได้
- **LO 12.4:** สามารถส่งอีเมล (SMTP, HTML, CC/BCC, ไฟล์แนบ) และอ่าน/จัดการกล่องจดหมาย (IMAP) ได้
- **LO 12.5:** สามารถออกแบบ Communication Agent ที่ใช้ context, template และกฎ if-then พร้อมจัดการ credentials อย่างปลอดภัยด้วย `.env` ได้

---

## 1. Final Project: Enhanced Task Manager
- `Task` → `DueDateTask`, `PriorityTask` (override `to_dict()` และส่วนแสดงผล)
- โหลดกลับเป็นคลาสเดิมด้วยฟิลด์ `_type`
- Sort ตาม priority ใช้ `{"High": 1, "Medium": 2, "Low": 3}` และแยกงานที่ไม่มีค่าไว้ท้ายเสมอ
- รันทดสอบ: `python -m unittest discover tests` → 12 tests OK

## 2. Email & SMS

| งาน | ไลบรารี / คำสั่ง |
|:---|:---|
| ส่งอีเมล | `smtplib.SMTP("smtp.gmail.com", 587)` → `starttls()` → `login(email, app_password)` → `send_message()` |
| สร้างข้อความ | `email.message.EmailMessage` (`set_content`, `add_alternative(html)`, `add_attachment`) |
| ค้นหาอีเมล | `imaplib.IMAP4_SSL` → `uid("search", None, "UNSEEN", "SUBJECT", '"Data Request"')` |
| SMS | อีเมลถึง gateway เช่น `number@txt.att.net` (ในไทยควรใช้ SMS API เช่น Twilio) |
| ความปลอดภัย | เก็บรหัสใน `.env` + `python-dotenv` และใส่ `.env` ใน `.gitignore`, ใช้ Gmail App Password |

---

## ไฟล์ปฏิบัติการ
| งาน | โฟลเดอร์ |
|:---|:---|
| Lab 12: Final Project Development | [final_task_manager_project](./final_task_manager_project) |
| LabX ADV: Agentic Communication Workflows | [agentic-comm-automator](./agentic-comm-automator) |
