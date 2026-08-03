# 📝 Week 2 Summary — Variables, Operators & Conditions

**วิชา:** Script Programming (Sec 2)  
**ชื่อ:** อัษฎาวุธ เรือนแก้ว | **รหัส:** 663380303-5

---

## 📌 หัวข้อที่เรียนในสัปดาห์นี้

### 1. ตัวแปรและชนิดข้อมูล (Variables & Data Types)
- **String (`str`):** ข้อความ เช่น `"Hello"`
- **Integer (`int`):** จำนวนเต็ม เช่น `25`
- **Float (`float`):** ทศนิยม เช่น `3.14`
- **Boolean (`bool`):** ค่าความจริง `True` / `False`
- ใช้ `type()` เพื่อตรวจสอบชนิดข้อมูล
- **Type Casting:** แปลงชนิดด้วย `int()`, `float()`, `str()`

### 2. Operators (ตัวดำเนินการ)

| ประเภท | ตัวอย่าง |
|--------|---------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| **Logical** | `and`, `or`, `not` |

### 3. String Operations (การจัดการสตริง)
- **Concatenation:** `"Hello" + " World"`
- **Repetition:** `"Ha" * 3` → `"HaHaHa"`
- **Indexing & Slicing:** `s[0]`, `s[-1]`, `s[1:4]`
- **Methods:** `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.find()`, `.count()`
- **f-string:** `f"Name is {name}"`
- **len():** หาความยาวสตริง

### 4. Input Function
- `input()` รับค่าจากผู้ใช้ (ได้ค่าเป็น `str` เสมอ)
- ต้อง cast เป็น `int()` หรือ `float()` ถ้าต้องการตัวเลข

### 5. Conditional Statements (เงื่อนไข)
```python
if เงื่อนไข:
    # ทำเมื่อเป็น True
elif เงื่อนไขอื่น:
    # ทำเมื่อเงื่อนไขแรกเป็น False แต่เงื่อนไขนี้เป็น True
else:
    # ทำเมื่อไม่ตรงเงื่อนไขใดเลย
```

---

## 📂 ไฟล์ในสัปดาห์นี้

| ไฟล์ | คำอธิบาย |
|------|---------|
| `activity2_1.ipynb` | Evaluation Check — ฝึกวิเคราะห์ลำดับการทำงานของ if/elif/else และ Set Comprehension |
| `activity2_2.ipynb` | Choose Your Own Adventure — เกมผจญภัยแบบเลือกทาง ใช้ if/elif/else ซ้อนกัน |
| `lab2_1.py` | ตรวจสอบตัวเลข บวก/ลบ/ศูนย์ และ คู่/คี่ |
| `lab2_2.py` | แนะนำประเภทภาพยนตร์ตามช่วงอายุ |

---

## 💡 สิ่งที่ได้เรียนรู้
- การใช้ Logical Operators (`and`, `or`, `not`) ร่วมกับ if/elif/else เพื่อสร้างเงื่อนไขซับซ้อน
- Set Comprehension สำหรับกรองข้อมูลแบบไม่ซ้ำ
- การออกแบบโปรแกรมแบบ Interactive ด้วย `input()` ร่วมกับ conditional branching
- การใช้ f-string เพื่อแสดงผลลัพธ์อย่างเป็นระเบียบ
