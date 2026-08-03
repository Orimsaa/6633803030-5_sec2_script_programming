# สรุปเนื้อหาบทเรียน สัปดาห์ที่ 1: Introduction to Python & Basic Syntax

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2 (เรียน Onsite วันอังคาร 23/6/69 เวลา 08:30 - 12:30 น. ห้อง SC9226)

---

## 1. ข้อมูลภาพรวมรายวิชาและการประเมินผล

### 1.1 โครงสร้างรายวิชา (3 ส่วนหลัก)
| ส่วนที่ | ชื่อหัวข้อหลัก | รายละเอียดเนื้อหา |
|:---:|:---|:---|
| 1 | **Basics of Python** | ภาคบรรยายและการเรียนรู้ด้วยตนเอง: Introduction & Syntax, Strings & Console Output, Conditionals, Functions, Lists & Dictionaries, Loops, Advanced Topics, Classes, File I/O |
| 2 | **Application of Python** | ภาคปฏิบัติการ (Lab & Experiment): Systems and Network Programming, การพัฒนา Python สำหรับแอปพลิเคชันสมัยใหม่ |
| 3 | **Project & Conclusion** | การทำโครงงานและบทสรุป: Mini Project (Midterm), Term Project (Final), Final Exam |

### 1.2 สัดส่วนการให้คะแนน
| หมวดหมู่การประเมิน | สัดส่วนคะแนน |
|:---|:---:|
| การเข้าชั้นเรียนและส่วนร่วม | 10% |
| การเรียนรู้ออนไลน์รายบุคคล | 15% |
| กิจกรรมและงานกลุ่ม | 20% |
| โครงงานย่อย (Mini Project) | 15% |
| โครงงานปลายภาค (Final Project) | 20% |
| การสอบปลายภาค (Final Exam) | 20% |

### 1.3 เกณฑ์การประเมินผลการเรียน
- **เกณฑ์ผ่านขั้นต่ำ (D):** ผลการเรียนใน Codecademy / Datacamp ไม่ต่ำกว่า 90% และผลสอบ Netacad Exam ไม่ต่ำกว่า 50% (สำหรับใบรับรอง CISCO)
- **เกณฑ์ผลการเรียนดีเยี่ยม (A):** ต้องได้คะแนนมากกว่า 80% ในทุกหมวดหมู่การประเมิน (เข้าเรียน, งานรายสัปดาห์, ปฏิบัติการ, โครงงาน และการสอบปลายภาค)

### 1.4 นโยบายทางวิชาการและระเบียบปฏิบัติ
- **ความซื่อสัตย์ทางวิชาการ:** ห้ามคัดลอกรหัสต้นฉบับ (Code) หรือส่งต่อไฟล์งานทางอีเมล/สื่อสังคมออนไลน์ หากตรวจสอบพบการทุจริต จะถูกปรับคะแนนโครงงานเป็น 0 คะแนน หักเกรดเฉลี่ยรายวิชาลง 10% และรายงานต่อคณะกรรมการวินัยนักศึกษา
- **มารยาทในชั้นเรียน:** เข้าเรียนตรงเวลา ไม่ส่งเสียงดังรบกวนระหว่างการบรรยาย ปิดเสียงโทรศัพท์มือถือ และใช้อุปกรณ์คอมพิวเตอร์เฉพาะประโยชน์ต่อการเรียนการสอนเท่านั้น

---

## 2. ภาคทฤษฎี: Getting Started with Python

### 2.1 ปรัชญาของภาษา Python (Zen of Python)
Python ให้ความสำคัญกับโครงสร้างที่อ่านง่ายและตรงไปตรงมา ตามแนวคิดของ Tim Peters ดังนี้
- ความสวยงามย่อมดีกว่าความอัปลักษณ์ (Beautiful is better than ugly)
- ความชัดเจนย่อมดีกว่าความกำกวม (Explicit is better than implicit)
- ความเรียบง่ายย่อมดีกว่าความซับซ้อน (Simple is better than complex)
- **ความอ่านง่ายคือสิ่งสำคัญที่สุด (Readability counts)**

### 2.2 คุณลักษณะทางเทคนิคของภาษา Python
- **Dynamic Typing:** กำหนดชนิดข้อมูลและเปลี่ยนแปลงได้ในระหว่างเวลาประมวลผล (Runtime) โดยไม่ต้องประกาศชนิดข้อมูลล่วงหน้า
- **Automatic Memory Management:** จัดการหน่วยความจำอัตโนมัติด้วยระบบ Garbage Collection
- **Multi-paradigm:** รองรับการเขียนโปรแกรมเชิงวัตถุ (OOP), เชิงคำสั่ง (Imperative), เชิงฟังก์ชัน (Functional) และเชิงกระบวนการ (Procedural)
- **Standard Library:** มีไลบรารีมาตรฐานที่ครอบคลุมการทำงานด้านเครือข่าย วิทยาศาสตร์ข้อมูล และระบบปฏิบัติการ

### 2.3 การตั้งชื่อและจัดการตัวแปร (Variables & Naming Conventions)
- **หลักการตั้งชื่อ:** ต้องขึ้นต้นด้วยตัวอักษรภาษาอังกฤษหรือเครื่องหมาย `_` ตามด้วยตัวอักษร ตัวเลข หรือ `_` โดยมีความไวต่ออักษรตัวพิมพ์เล็ก-ใหญ่ (Case-sensitive) และห้ามใช้คำสงวน (Keywords)
- **การกำหนดค่า (Assignment):** นิพจน์ด้านขวาจะถูกประมวลผลก่อนนำไปเก็บในตัวแปรด้านซ้าย รองรับ Multiple Assignment และ Cascading Assignment

```python
# ตัวอย่างการประกาศและกำหนดค่าตัวแปร
student_name = "Tonkla"
student_age = 20
is_enrolled = True

# การกำหนดค่าแบบหลายตัวแปรพร้อมกัน (Multiple Assignment)
x, y, z = 10, 20, 30

# การกำหนดค่าแบบต่อเนื่อง (Cascading Assignment)
first_counter = second_counter = third_counter = 0
```

### 2.4 การย่อหน้าและขอบเขตคำสั่ง (Block Indentation)
Python ใช้การย่อหน้า (Indentation) เพื่อระบุขอบเขตของชุดคำสั่ง (Block scope) แทนการใช้วงเล็บปีกกา โดยมีเครื่องหมายทวิภาค `:` เป็นตัวนำหน้ากลุ่มคำสั่งตามมาตรฐาน PEP 8 ซึ่งแนะนำให้ใช้ช่องว่าง 4 ตัวอักษร (4 Spaces)

```python
score = 85

if score >= 80:
    print("Grade: A")        # อยู่ภายในขอบเขตเงื่อนไข if
    print("Status: Passed")  # อยู่ภายในขอบเขตเงื่อนไข if
print("Evaluation Completed") # อยู่ภายนอกขอบเขตเงื่อนไข if
```

### 2.5 ชนิดข้อมูลพื้นฐาน (Built-in Data Types)

| ชนิดข้อมูล | หมวดหมู่ | ลักษณะและความหมาย | ตัวอย่าง |
|:---|:---|:---|:---|
| `int` | Numeric | จำนวนเต็มที่มีขนาดไม่จำกัด (Arbitrary-precision) | `42`, `-150`, `999999999` |
| `float` | Numeric | จำนวนจริงหรือทศนิยมมาตรฐาน IEEE 754 | `3.14159`, `-0.005` |
| `complex` | Numeric | จำนวนเชิงซ้อน (ส่วนจริง + ส่วนจินตภาพ) | `3+4j` |
| `bool` | Boolean | ค่าทางตรรกศาสตร์ (Subclass ของ int) | `True`, `False` |
| `str` | Sequence | อักขระหรือข้อความแบบ Unicode (Immutable) | `"Python"`, `'Script'` |
| `list` | Sequence | รายการข้อมูลแบบเรียงลำดับและแก้ไขค่าได้ | `[10, 20, 30]` |
| `tuple` | Sequence | รายการข้อมูลแบบเรียงลำดับแต่แก้ไขค่าไม่ได้ | `(10, 20, 30)` |
| `dict` | Mapping | การจับคู่คีย์และค่า (Key-Value Pairs) | `{"name": "Tonkla", "gpa": 3.75}` |
| `set` | Set | เซตของข้อมูลที่ไม่ซ้ำกันและไม่มีลำดับ | `{1, 2, 3}` |

### 2.6 ความแตกต่างระหว่าง Mutable และ Immutable
- **Immutable Types:** ออบเจกต์ที่สร้างแล้วไม่สามารถแก้ไขข้อมูลภายในได้ ได้แก่ `int`, `float`, `str`, `tuple`, `bool`, `frozenset` หากทำการเปลี่ยนแปลงค่า ระบบจะสร้างออบเจกต์ใหม่ในหน่วยความจำ
- **Mutable Types:** ออบเจกต์ที่สามารถเปลี่ยนแปลงหรือปรับปรุงค่าภายในหน่วยความจำตำแหน่งเดิมได้ ได้แก่ `list`, `dict`, `set`, `bytearray`

```python
# การตรวจสอบตำแหน่งหน่วยความจำด้วยฟังก์ชัน id()
text_value = "Script"
first_id = id(text_value)

text_value += " Programming"  # สำหรับ str จะสร้างออบเจกต์ใหม่
second_id = id(text_value)

print(first_id == second_id)  # ผลลัพธ์: False (ชี้ไปยังคนละตำแหน่งหน่วยความจำ)
```

### 2.7 การแปลงชนิดข้อมูล (Type Conversion)
- **Implicit Conversion:** การแปลงชนิดข้อมูลอัตโนมัติของตัวแปลภาษา เช่น การบวก `int` กับ `float` ผลลัพธ์จะกลายเป็น `float`
- **Explicit Conversion (Casting):** การแปลงชนิดข้อมูลโดยคำสั่งของผู้เขียนโปรแกรม เช่น `int()`, `float()`, `str()`, `list()`, `set()`

```python
# การแปลงข้อมูลข้อความที่เป็นเลขทศนิยมให้กลายเป็นจำนวนเต็ม
value_str = "45.89"
value_int = int(float(value_str))  # ต้องแปลงเป็น float ก่อนแล้วจึงแปลงเป็น int
print(value_int)                   # ผลลัพธ์: 45
```

---

## 3. ภาคปฏิบัติการ (Labs & Activities)

### 3.1 Lab 1.1: Environment Setup and Hello World
การทดสอบสภาพแวดล้อมการทำงานผ่าน Visual Studio Code หรือ Google Colab ด้วยการเรียกใช้คำสั่งพื้นฐาน

```python
# Lab 1.1: Hello World Script
print("Hello, World!")
print("CP352301", "Script", "Programming", sep=" - ")
```

### 3.2 Lab 1.2: Variables, Arithmetic, f-string and Input Conversion
การเขียนโปรแกรมรับข้อมูลผู้ใช้ คำนวณนิพจน์ทางคณิตศาสตร์ และจัดรูปแบบการแสดงผลด้วย f-string

```python
# Lab 1.2: Student Data Processing Script
student_name = input("Enter Student Name: ")
birth_year = int(input("Enter Birth Year (A.D.): "))
current_year = 2026

age = current_year - birth_year

print(f"Student Profile: {student_name}")
print(f"Calculated Age: {age} years old")
```

### 3.3 Activity 1.2: Python Puzzlers
การวิเคราะห์พฤติกรรมและการทำงานของภาษา Python จากข้อคำถามทางเทคนิค

```python
# Puzzler 1: การดำเนินการระหว่างตัวเลขและสตริง
result_str = "10" + "20"
print(result_str)  # ผลลัพธ์: "1020" (String Concatenation ไม่ใช่การบวกทางคณิตศาสตร์)

# Puzzler 2: การตรวจสอบชนิดข้อมูลผลลัพธ์ของ Input
raw_data = input("Enter number: ")  # หากผู้ใช้กรอก 50 ค่าที่ได้คือ 'str'
# total = raw_data + 10             # จะเกิด TypeError เนื่องจากไม่สามารถบวก str กับ int ได้
```

---

## 4. สรุปข้อผิดพลาดที่พบบ่อย (Common Error Messages)

| ชื่อข้อผิดพลาด | สาเหตุของการเกิดข้อผิดพลาด | วิธีการแก้ไข |
|:---|:---|:---|
| `SyntaxError` | โครงสร้างไวยากรณ์ไม่ถูกต้องตามกฎของภาษา | ตรวจสอบวงเล็บ เครื่องหมายทวิภาค `:` หรือเครื่องหมายอัญประกาศ |
| `TypeError` | การกระทำระหว่างชนิดข้อมูลที่ไม่รองรับกัน | ใช้ฟังก์ชันแปลงชนิดข้อมูล เช่น `int()`, `str()`, `float()` |
| `NameError` | การเรียกใช้ตัวแปรที่ยังไม่ได้ประกาศในขอบเขต | ตรวจสอบการสะกดชื่อตัวแปรและการกำหนดค่าก่อนเรียกใช้ |
| `ValueError` | ข้อมูลมีรูปแบบไม่เหมาะสมกับการแปลงค่า | ตรวจสอบเนื้อหาข้อมูลก่อนทำการ Casting เช่น ไม่ใช้ `int("abc")` |
| `IndentationError` | การเว้นวรรคและการย่อหน้าไม่ถูกต้องหรือไม่สม่ำเสมอ | ตรวจสอบการใช้ Space 4 ช่อง และหลีกเลี่ยงการผสมระหว่าง Space และ Tab |
