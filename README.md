# CP352301 Script Programming

**ภาคเรียน:** 1/2569  
**รหัสวิชา:** CP352301  
**ชื่อรายวิชา:** การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2  

---

## สารบัญผลลัพธ์การเรียนรู้รายสัปดาห์ (Weekly Learning Outcomes)

| สัปดาห์ที่ | หัวข้อบทเรียน | ผลลัพธ์การเรียนรู้และสรุปเนื้อหา | โฟลเดอร์ปฏิบัติการ |
|:---:|:---|:---|:---:|
| 1 | Introduction to Python & Basic Syntax | [Learning Outcomes Week 1](./Week1/Week1_Summary.md) | [Week1](./Week1) |
| 2 | Variables, Operators, Conditions & String Operations | [Learning Outcomes Week 2](./Week2/Week2_Summary.md) | [Week2](./Week2) |
| 3 | Loops in Python (for / while) & Control Flow | [Learning Outcomes Week 3](./Week3/Week3_Summary.md) | [Week3](./Week3) |
| 4 | Data Structures: Lists & Tuples | [Learning Outcomes Week 4](./Week4/Week4_Summary.md) | [Week4](./Week4) |

---

## ผลลัพธ์การเรียนรู้รายสัปดาห์ (Key Learning Outcomes)

### สัปดาห์ที่ 1: Introduction to Python & Basic Syntax
- **LO 1.1:** สามารถอธิบายปรัชญาของภาษา Python (Zen of Python) ลักษณะเด่น และโครงสร้างไวยากรณ์พื้นฐานได้
- **LO 1.2:** สามารถติดตั้งและตั้งค่าสภาพแวดล้อมการพัฒนาโปรแกรม (Visual Studio Code, Google Colab) และทดสอบรันสคริปต์ได้
- **LO 1.3:** สามารถจำแนกและแปลงชนิดข้อมูลพื้นฐาน (Primitive & Collection Types) รวมถึงอธิบายความแตกต่างของ Mutable และ Immutable ได้
- **LO 1.4:** สามารถเขียนโปรแกรมรับข้อมูลจากผู้ใช้ (`input`) ประมวลผลนิพจน์คณิตศาสตร์ และจัดรูปแบบการแสดงผลด้วย `f-string` ได้
- **เอกสารผลลัพธ์การเรียนรู้:** [Week1_Summary.md](./Week1/Week1_Summary.md)

### สัปดาห์ที่ 2: Variables, Operators, Conditions & String Operations
- **LO 2.1:** สามารถเลือกใช้ตัวแปรและดำเนินการแปลงชนิดข้อมูล (Type Casting) เพื่อการประมวลผลข้อมูลที่ถูกต้อง
- **LO 2.2:** สามารถประยุกต์ใช้ตัวดำเนินการทางคณิตศาสตร์ การเปรียบเทียบ และตรรกศาสตร์ (`and`, `or`, `not`) ในการแก้ปัญหาได้
- **LO 2.3:** สามารถจัดการข้อความด้วย String Methods และ Slicing ร่วมกับการควบคุมทิศทางโปรแกรมด้วยเงื่อนไข (`if / elif / else`) ได้
- **LO 2.4:** สามารถออกแบบโปรแกรมเชิงโต้ตอบแบบมีเงื่อนไข (Interactive Fiction) และโปรแกรมแนะนำข้อมูลตามเงื่อนไขผู้ใช้งานได้
- **ไฟล์ปฏิบัติการ:** activity2_1.ipynb, activity2_2.ipynb, lab2_1.py, lab2_2.py
- **เอกสารผลลัพธ์การเรียนรู้:** [Week2_Summary.md](./Week2/Week2_Summary.md)

### สัปดาห์ที่ 3: Loops in Python (for / while) & Control Flow
- **LO 3.1:** สามารถออกแบบและเขียนโปรแกรมโครงสร้างวนซ้ำด้วยคำสั่ง `for` ร่วมกับ `range()` และคำสั่ง `while` ได้อย่างมีประสิทธิภาพ
- **LO 3.2:** สามารถใช้วงวนซ้อน (Nested Loops) และคำสั่งควบคุมการทำงาน (`break`, `continue`, `while-else`) ในการจัดการข้อมูลซับซ้อนได้
- **LO 3.3:** สามารถพัฒนาระบบอัตโนมัติและเกมจำลอง เช่น ตารางสูตรคูณ 2 มิติ ระบบนับถอยหลัง และเกมทายตัวเลขแบบจำกัดรอบได้
- **ไฟล์ปฏิบัติการ:** Lab3.ipynb
- **เอกสารผลลัพธ์การเรียนรู้:** [Week3_Summary.md](./Week3/Week3_Summary.md)

### สัปดาห์ที่ 4: Data Structures: Lists & Tuples
- **LO 4.1:** สามารถวิเคราะห์ความแตกต่างและเลือกใช้งานระหว่างโครงสร้างข้อมูลแบบรายการ (List) และทูเพิล (Tuple) ได้อย่างเหมาะสม
- **LO 4.2:** สามารถดำเนินการจัดการข้อมูลใน List (เพิ่ม, แทรก, ลบ, ค้นหา, เรียงลำดับ) และ Tuple (Packing, Unpacking) ได้
- **LO 4.3:** สามารถพัฒนาระบบจัดการข้อมูลนักศึกษาแบบ CRUD (Create, Read, Update, Delete) โดยประยุกต์ใช้ List และวงวนควบคุมได้
- **ไฟล์ปฏิบัติการ:** Lab_4_Script_.ipynb
- **เอกสารผลลัพธ์การเรียนรู้:** [Week4_Summary.md](./Week4/Week4_Summary.md)
