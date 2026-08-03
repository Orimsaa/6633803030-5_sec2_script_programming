# 📝 Week 3 Summary — Loops in Python (for / while)

**วิชา:** Script Programming (Sec 2)  
**ชื่อ:** อัษฎาวุธ เรือนแก้ว | **รหัส:** 663380303-5

---

## 📌 หัวข้อที่เรียนในสัปดาห์นี้

### 1. For Loop
- ใช้วนซ้ำตามจำนวนรอบที่กำหนด
- ใช้ร่วมกับ `range(start, stop, step)`
```python
for i in range(1, 13):
    print(i)
```

### 2. While Loop
- ใช้วนซ้ำจนกว่าเงื่อนไขจะเป็น `False`
```python
count = 5
while count >= 0:
    print(count)
    count -= 1
```

### 3. While-Else
- บล็อก `else` ทำงานเมื่อลูปจบตามปกติ (ไม่ถูก `break`)
- ถ้าลูปถูก `break` → `else` จะ **ไม่ทำงาน**
```python
while attempts < max_attempts:
    # ทาย...
    if ถูก:
        break
else:
    print("หมดโควตา!")
```

### 4. Nested Loops (ลูปซ้อนกัน)
- ลูปนอก (Outer) ควบคุมแถว, ลูปใน (Inner) ควบคุมคอลัมน์
- ใช้สร้างตารางสูตรคูณ 12×12

### 5. break & continue
- `break` — หยุดลูปทันที
- `continue` — ข้ามรอบปัจจุบัน ไปรอบถัดไป

### 6. String Formatting ขั้นสูง
- `f"{value:4d}"` — จัดความกว้างตัวเลข
- `end=""` — ไม่ขึ้นบรรทัดใหม่หลัง print

---

## 📂 ไฟล์ในสัปดาห์นี้

| ไฟล์ | คำอธิบาย |
|------|---------|
| `Lab3.ipynb` | รวม Lab 3.1 และ Lab 3.2 พร้อม Challenge |

### Lab 3.1: Multiplication Table Generator
- **Part 1:** สูตรคูณเลขเดียว (for loop + range)
- **Part 2:** ตาราง 12×12 (Nested loops)
- **Challenge:** ตาราง 12×12 พร้อม Header และเส้นแบ่ง

### Lab 3.2: Countdown & Guessing Game
- **Part 1:** Countdown Timer (while loop)
- **Part 2:** เกมทายตัวเลข (while True + break)
- **Challenge 1:** Guessing Game จำกัดรอบ (while-else + random)
- **Challenge 2:** Countdown พร้อม Progress Bar (time.sleep)

---

## 💡 สิ่งที่ได้เรียนรู้
- ความแตกต่างระหว่าง `for` loop (รู้จำนวนรอบ) กับ `while` loop (ไม่รู้จำนวนรอบ)
- การใช้ `while-else` เป็นรูปแบบเฉพาะของ Python ที่ภาษาอื่นไม่ค่อยมี
- การใช้ `import random` และ `import time` เพื่อเพิ่มความสมจริงให้โปรแกรม
- Nested Loops สำหรับสร้างตาราง 2 มิติ
- การใช้ String Formatting (`f-string` ร่วม format spec) เพื่อจัดข้อมูลให้สวยงาม
