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
| 5 | Data Structures: Dictionaries & Sets | [Learning Outcomes Week 5](./week5/Week5_Summary.md) | [week5](./week5) |
| 6 | Functions & Modules | [Learning Outcomes Week 6](./week6/Week6_Summary.md) | [week6](./week6) |
| 7 | Web Scraping (LabX Basic & Advanced) | [Learning Outcomes Week 7](./Summary/Week7_Summary.md) | [LabX Basic](./LabX%20Basic) · [LabX Advance](./LabX%20Advance) |
| 8 | Automating with CSV and JSON Data (LabX Basic & Advanced) | [Learning Outcomes Week 8](./Summary/Week8_Summary.md) | [LabX Basic](./LabX%20Basic) · [LabX Advance](./LabX%20Advance) |
| 10 | Automating Spreadsheets (LabX Basic & Advanced) | [Learning Outcomes Week 10](./Summary/Week10_Summary.md) | [LabX Basic](./LabX%20Basic) · [LabX Advance](./LabX%20Advance) |
| 11 | Automating PDFs & Word Documents (LabX Basic & Advanced) | [Learning Outcomes Week 11](./Summary/Week11_Summary.md) | [LabX Basic](./LabX%20Basic) · [LabX Advance](./LabX%20Advance) |
| 12 | Final Project & Automating Communications (Email & SMS) | [Learning Outcomes Week 12](./Summary/Week12_Summary.md) | [Lab](./Lab) · [LabX Advance](./LabX%20Advance) |
| – | Class Activity 1–4 (คะแนนเสริม) | [รายการกิจกรรม](./Class%20activity/README.md) | [Class activity](./Class%20activity) |

### โครงสร้างโฟลเดอร์งานสัปดาห์ที่ 7–12

| โฟลเดอร์ | เนื้อหา |
|:---|:---|
| [LabX Basic](./LabX%20Basic) | LabX BASIC สัปดาห์ที่ 7, 8, 10, 11, 12 |
| [LabX Advance](./LabX%20Advance) | LabX ADV สัปดาห์ที่ 7, 8, 10, 11, 12 |
| [Lab](./Lab) | Lab 12: Final Project Development |
| [Class activity](./Class%20activity) | Class Activity 1–4 |
| [Summary](./Summary) | เอกสารสรุปผลลัพธ์การเรียนรู้สัปดาห์ที่ 7–12 |

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

### สัปดาห์ที่ 5: Data Structures: Dictionaries & Sets
- **LO 5.1:** สามารถจัดระเบียบข้อมูลด้วยโครงสร้างคู่กุญแจ-ค่า (Dictionaries) เพื่อการดึงข้อมูลที่รวดเร็วระดับ O(1) ได้
- **LO 5.2:** สามารถจัดการชุดข้อมูลที่ไม่ซ้ำกัน (Sets) และดำเนินการทางคณิตศาสตร์เชิงเซต (Union, Intersection, Difference, Symmetric Difference) ได้
- **LO 5.3:** สามารถเลือกใช้โครงสร้างข้อมูลที่เหมาะสม (List, Tuple, Dictionary, Set) สำหรับปัญหาที่กำหนดได้
- **ไฟล์ปฏิบัติการ:** Sec2_week5_6633803030-5.ipynb, lab5_1.py, lab5_2.py, activity5_2.py
- **เอกสารผลลัพธ์การเรียนรู้:** [Week5_Summary.md](./week5/Week5_Summary.md)

### สัปดาห์ที่ 6: Functions & Modules
- **LO 6.1:** สามารถนิยามและเรียกใช้ฟังก์ชัน (Functions) เพื่อส่งเสริมการใช้โค้ดซ้ำ (Code Reusability) และความเป็นโมดูล (Modularity) ได้
- **LO 6.2:** สามารถเข้าใจแนวคิดของพารามิเตอร์ (Parameters), อาร์กิวเมนต์ (Arguments), ค่าเริ่มต้น (Default Values) และค่าส่งกลับ (Return Values) ได้
- **LO 6.3:** สามารถแยกแยะขอบเขตตัวแปร (Variable Scope) ระหว่าง Local และ Global และนำเข้าใช้งานฟังก์ชันจากโมดูลมาตรฐานและโมดูลที่สร้างขึ้นเองได้
- **ไฟล์ปฏิบัติการ:** Sec2_week6_6633803030-5.ipynb, lab6_1.py, my_utils.py, main_program.py, activity6_1.py
- **เอกสารผลลัพธ์การเรียนรู้:** [Week6_Summary.md](./week6/Week6_Summary.md)

### สัปดาห์ที่ 7: Web Scraping
- **LO 7.1:** สามารถดึงและแยกข้อมูลจาก HTML ด้วย `requests` และ `BeautifulSoup4` พร้อมจัดการข้อผิดพลาดของเครือข่ายได้
- **LO 7.2:** สามารถควบคุมเบราว์เซอร์ด้วย Selenium (headless, explicit wait, pagination) และออกแบบ scraper แบบ config-driven พร้อม retry ได้
- **LO 7.3:** สามารถอธิบายข้อพิจารณาด้านจริยธรรมและกฎหมายของการทำ web scraping ได้
- **ไฟล์ปฏิบัติการ:** [LabX Basic/week7-web-scraping-intro](./LabX%20Basic/week7-web-scraping-intro), [LabX Advance/week7-agentic-web-scraper](./LabX%20Advance/week7-agentic-web-scraper)
- **เอกสารผลลัพธ์การเรียนรู้:** [Week7_Summary.md](./Summary/Week7_Summary.md)

### สัปดาห์ที่ 8: Automating with CSV and JSON Data
- **LO 8.1:** สามารถอ่าน เขียน กรอง และรวมกลุ่มข้อมูล CSV ด้วยโมดูล `csv` ได้
- **LO 8.2:** สามารถจัดการ JSON แบบซ้อน (อัปเดต เพิ่ม ค้นด้วย dot-path) และแปลง CSV ↔ JSON ได้
- **LO 8.3:** สามารถสร้าง Data Agent ที่ทำงานตาม pipeline ใน config พร้อม audit report ได้
- **ไฟล์ปฏิบัติการ:** [LabX Basic/week8-data-processor](./LabX%20Basic/week8-data-processor), [LabX Advance/week8-agentic-data-processor](./LabX%20Advance/week8-agentic-data-processor)
- **เอกสารผลลัพธ์การเรียนรู้:** [Week8_Summary.md](./Summary/Week8_Summary.md)

### สัปดาห์ที่ 10: Automating Spreadsheets
- **LO 10.1:** สามารถอ่าน/สร้าง/จัดรูปแบบไฟล์ Excel ด้วย `openpyxl` ได้
- **LO 10.2:** สามารถใช้สูตร, Conditional Formatting, Data Validation และกราฟผ่านโค้ดได้
- **LO 10.3:** สามารถสร้าง Spreadsheet Agent ที่บันทึกการทำงานลงชีต Audit Log และอธิบายแนวคิด Google Sheets API ได้
- **ไฟล์ปฏิบัติการ:** [LabX Basic/week10-spreadsheet-automator](./LabX%20Basic/week10-spreadsheet-automator), [LabX Advance/week10-agentic-spreadsheet-processor](./LabX%20Advance/week10-agentic-spreadsheet-processor)
- **เอกสารผลลัพธ์การเรียนรู้:** [Week10_Summary.md](./Summary/Week10_Summary.md)

### สัปดาห์ที่ 11: Automating PDFs & Word Documents
- **LO 11.1:** สามารถดึงข้อความ รวม และใส่ลายน้ำไฟล์ PDF ด้วย `PyPDF2` และ `reportlab` ได้
- **LO 11.2:** สามารถสร้างเอกสาร Word และรายงานจาก template ด้วย `python-docx` ได้
- **LO 11.3:** สามารถสร้าง Document Agent ที่ทำงานตาม config พร้อม audit report ได้
- **ไฟล์ปฏิบัติการ:** [LabX Basic/week11-document-automator](./LabX%20Basic/week11-document-automator), [LabX Advance/week11-agentic-document-automator](./LabX%20Advance/week11-agentic-document-automator)
- **เอกสารผลลัพธ์การเรียนรู้:** [Week11_Summary.md](./Summary/Week11_Summary.md)

### สัปดาห์ที่ 12: Final Project & Agentic Communication
- **LO 12.1:** สามารถพัฒนา Task Manager แบบ OOP หลายโมดูล พร้อม Search / Filter / Sort และ Unit Tests ได้
- **LO 12.2:** สามารถส่งอีเมล/SMS แบบ template และประมวลผลอีเมลขาเข้าด้วยกฎ if-then โดยจัดการ credentials ผ่าน `.env` ได้
- **ไฟล์ปฏิบัติการ:** [Lab/week12-final-task-manager-project](./Lab/week12-final-task-manager-project), [LabX Basic/week12-email-sms-automator](./LabX%20Basic/week12-email-sms-automator), [LabX Advance/week12-agentic-comm-automator](./LabX%20Advance/week12-agentic-comm-automator)
- **เอกสารผลลัพธ์การเรียนรู้:** [Week12_Summary.md](./Summary/Week12_Summary.md)

### Class Activity (คะแนนเสริม)
- Activity 1–4: Simple CLI Task Manager, OOP Refactoring, Web API Fetcher, Project Planning & Design
- **โฟลเดอร์:** [Class activity](./Class%20activity)
