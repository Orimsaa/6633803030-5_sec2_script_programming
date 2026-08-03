# สรุปเนื้อหาบทเรียน สัปดาห์ที่ 2: Variables, Operators, Conditions & String Operations

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## 1. ตัวแปรและชนิดข้อมูลพื้นฐาน (Variables & Data Types)

ในการเขียนโปรแกรมภาษา Python ตัวแปร (Variables) ทำหน้าที่เป็นส่วนอ้างอิงตำแหน่งหน่วยความจำที่จัดเก็บข้อมูล โดยมีโครงสร้างข้อมูลพื้นฐานที่ใช้บ่อยในสัปดาห์นี้ ดังนี้
- **String (`str`):** ข้อมูลประเภทอักขระหรือข้อความ เช่น `"Script Programming"`
- **Integer (`int`):** ข้อมูลประเภทจำนวนเต็ม เช่น `25`, `-10`
- **Float (`float`):** ข้อมูลประเภทจำนวนจริงหรือทศนิยม เช่น `3.14159`
- **Boolean (`bool`):** ข้อมูลประเภทค่าความจริงทางตรรกศาสตร์ มีค่าเป็น `True` หรือ `False`

### 1.1 การตรวจสอบและแปลงชนิดข้อมูล (Type Checking and Type Casting)
- ฟังก์ชัน `type()` ใช้สำหรับตรวจสอบชนิดข้อมูลของตัวแปรหรือนิพจน์
- การแปลงชนิดข้อมูล (Type Casting) สามารถกระทำผ่านฟังก์ชัน `int()`, `float()`, `str()` และต้องคำนึงถึงข้อจำกัดของข้อมูลตั้งต้นเพื่อหลีกเลี่ยงข้อผิดพลาดประเภท `ValueError`

---

## 2. ตัวดำเนินการ (Operators)

| หมวดหมู่ | ตัวดำเนินการ | ความหมายและการทำงาน | ตัวอย่าง | ผลลัพธ์ |
|:---|:---:|:---|:---|:---:|
| **Arithmetic** | `+`, `-`, `*`, `/` | การบวก ลบ คูณ และการหารทศนิยม | `10 / 4` | `2.5` |
| | `//` | การหารปัดเศษทิ้ง (Floor Division) | `10 // 4` | `2` |
| | `%` | การหารเอาเศษ (Modulo) | `10 % 3` | `1` |
| | `**` | การยกกำลัง (Exponentiation) | `2 ** 3` | `8` |
| **Comparison** | `==`, `!=` | ตรวจสอบความเท่ากัน และไม่เท่ากัน | `5 == 5` | `True` |
| | `>`, `<`, `>=`, `<=` | ตรวจสอบความสัมพันธ์มากกว่า น้อยกว่า หรือเท่ากับ | `10 < 5` | `False` |
| **Logical** | `and` | ให้ค่าเป็น True เมื่อเงื่อนไขเป็นจริงทั้งหมด | `True and False` | `False` |
| | `or` | ให้ค่าเป็น True เมื่อมีเงื่อนไขใดเงื่อนไขหนึ่งเป็นจริง | `True or False` | `True` |
| | `not` | ปฏิเสธค่าความจริง (นิเสธ) | `not True` | `False` |

---

## 3. การจัดการสตริงและข้อความ (String Operations)

- **String Concatenation & Repetition:** การเชื่อมข้อความด้วยเครื่องหมาย `+` และการทำซ้ำข้อความด้วยเครื่องหมาย `*`
- **String Indexing & Slicing:** การเข้าถึงตำแหน่งตัวอักษรด้วยดัชนี (`s[index]`) และการตัดสตริงบางช่วง (`s[start:stop:step]`) โดยตำแหน่งแรกเริ่มต้นที่ 0 และตำแหน่งสุดท้ายสามารถอ้างอิงจากด้านหลังด้วยค่าติดลบ เช่น `-1`
- **String Methods:** เมธอดสำคัญสำหรับจัดการข้อความ เช่น `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.find()`, `.count()`
- **Formatted String Literals (f-string):** การจัดรูปแบบข้อความด้วย `f"{variable}"` ซึ่งช่วยเพิ่มความอ่านง่ายในการประมวลผลข้อความร่วมกับค่าของตัวแปร

```python
# ตัวอย่างการใช้งาน String Operations และ f-string
course_name = "Script Programming"
formatted_output = f"Welcome to {course_name.upper()}"
print(formatted_output)  # ผลลัพธ์: Welcome to SCRIPT PROGRAMMING
```

---

## 4. โครงสร้างเงื่อนไขและการควบคุมทิศทาง (Conditional Statements)

โครงสร้างเงื่อนไขในภาษา Python ใช้สำหรับการกำหนดเส้นทางการประมวลผลตามค่าความจริงทางตรรกศาสตร์ของนิพจน์ โดยยึดหลักการย่อหน้า (Indentation) ในการกำหนดขอบเขตคำสั่ง

```python
temperature = 25
is_raining = True

if temperature > 20 and not is_raining:
    print("Perfect day for outdoor activities.")
elif temperature <= 20 or is_raining:
    print("Stay indoors or carry an umbrella.")
else:
    print("Weather conditions are undefined.")
```

---

## 5. สรุปไฟล์ปฏิบัติการประจำสัปดาห์

| ไฟล์ปฏิบัติการ | คำอธิบายสาระสำคัญ |
|:---|:---|
| `activity2_1.ipynb` | **Evaluation Check & Vectorized Filter:** การฝึกวิเคราะห์ลำดับการประมวลผลของเงื่อนไข if / elif / else ร่วมกับการใช้ Set Comprehension ในการคัดกรองพยัญชนะจากข้อความ |
| `activity2_2.ipynb` | **Choose Your Own Adventure:** การออกแบบเกมผจญภัยแบบโต้ตอบ (Interactive Fiction) ที่ใช้โครงสร้าง if / elif / else ซ้อนกัน (Nested Conditionals) |
| `lab2_1.py` | **Number Parity and Sign Checker:** การตรวจสอบคุณสมบัติของตัวเลขว่าเป็นจำนวนบวก ลบ หรือศูนย์ และตรวจสอบความเป็นจำนวนคู่หรือคี่ |
| `lab2_2.py` | **Movie Recommendation by Age:** การสร้างระบบแนะนำเกณฑ์ภาพยนตร์ตามช่วงอายุผู้ใช้งาน ร่วมกับคำถามทางเลือก |
