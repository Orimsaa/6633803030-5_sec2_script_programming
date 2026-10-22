# mini Project — My Simple Task Manager CLI

> งาน mini project ถูกเก็บไว้ใน repository แยก จึงทำเป็นไฟล์ลิงก์ตามที่ข้อกำหนดอนุญาต

**Repository:** https://github.com/Orimsaa/my-task-manager

## รายละเอียด

โปรแกรมจัดการงาน (Task Manager) แบบ Command-Line Interface เขียนด้วย Python

- **Add Tasks** — เพิ่มงานใหม่พร้อมคำอธิบาย
- **List Tasks** — แสดงรายการงานทั้งหมด พร้อม ID, คำอธิบาย และสถานะ
- **Complete Tasks** — ทำเครื่องหมายว่างานเสร็จแล้วด้วย ID
- **Delete Tasks** — ลบงานด้วย ID
- **Persistence** — บันทึกงานลง `data/tasks.json` และโหลดกลับอัตโนมัติ

## โครงสร้างโปรเจกต์

```
my-task-manager/
├── main.py            # จุดเริ่มต้นโปรแกรม (เมนู CLI)
├── requirements.txt
└── src/
    ├── task_data.py   # อ่าน/เขียนข้อมูลงานจากไฟล์ JSON
    └── task_logic.py  # ตรรกะการเพิ่ม แสดง ทำเสร็จ และลบงาน
```

## วิธีรัน

```bash
git clone https://github.com/Orimsaa/my-task-manager.git
cd my-task-manager
python main.py
```
