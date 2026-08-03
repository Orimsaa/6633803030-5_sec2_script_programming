# 📝 Week 4 Summary — Data Structures: Lists & Tuples

**วิชา:** Script Programming (Sec 2)  
**ชื่อ:** อัษฎาวุธ เรือนแก้ว | **รหัส:** 663380303-5

---

## 📌 หัวข้อที่เรียนในสัปดาห์นี้

### 1. Lists (ลิสต์)
- สร้าง List: `my_list = [1, 2, 3]`
- เข้าถึงสมาชิก: `my_list[0]`, `my_list[-1]`
- **Mutable** — แก้ไขค่าได้

#### Methods ที่สำคัญ

| Method | การทำงาน | ตัวอย่าง |
|--------|---------|---------|
| `append(x)` | เพิ่มสมาชิกที่ท้าย list | `lst.append("Alice")` |
| `insert(i, x)` | แทรกที่ตำแหน่ง i | `lst.insert(0, "Bob")` |
| `remove(x)` | ลบสมาชิกตัวแรกที่ตรงกับ x | `lst.remove("Alice")` |
| `pop(i)` | ลบและคืนค่าที่ตำแหน่ง i | `lst.pop(0)` |
| `sort()` | เรียงลำดับ (in-place) | `lst.sort()` |
| `reverse()` | กลับลำดับ | `lst.reverse()` |
| `index(x)` | หาตำแหน่งของ x | `lst.index("Alice")` |
| `count(x)` | นับจำนวน x ที่มี | `lst.count("Alice")` |

#### ตรวจสอบสมาชิก
```python
if "Alice" in student_names:
    print("พบแล้ว!")
```

#### List Slicing
```python
lst[1:4]   # ตำแหน่ง 1 ถึง 3
lst[:3]    # ตำแหน่ง 0 ถึง 2
lst[2:]    # ตำแหน่ง 2 ถึงสุดท้าย
```

### 2. Tuples (ทูเพิล)
- สร้าง Tuple: `my_tuple = (1, 2, 3)`
- **Immutable** — แก้ไขค่าไม่ได้หลังสร้าง
- ใช้เมื่อต้องการข้อมูลที่ไม่เปลี่ยนแปลง (เช่น พิกัด, วันในสัปดาห์)

#### Tuple Packing & Unpacking
```python
# Packing
point = (10, 20)

# Unpacking
x, y = point
print(x)  # 10
print(y)  # 20
```

### 3. เปรียบเทียบ List vs Tuple

| คุณสมบัติ | List | Tuple |
|----------|------|-------|
| สร้างด้วย | `[ ]` | `( )` |
| แก้ไขได้ (Mutable) | ✅ ได้ | ❌ ไม่ได้ |
| เร็วกว่า | ช้ากว่า | เร็วกว่า |
| ใช้เมื่อ | ข้อมูลเปลี่ยนแปลงได้ | ข้อมูลคงที่ |

---

## 📂 ไฟล์ในสัปดาห์นี้

| ไฟล์ | คำอธิบาย |
|------|---------|
| `Lab_4_Script_.ipynb` | Student Management System — ระบบจัดการรายชื่อนักศึกษาด้วย List |

### Lab 4.1: Student Management System
ระบบ CRUD สำหรับจัดการรายชื่อนักศึกษา:
1. **Add** — เพิ่มนักศึกษาด้วย `append()`
2. **Find** — ค้นหาด้วย `in` และ `index()`
3. **Remove** — ลบด้วย `remove()` (เช็คก่อนลบเพื่อกัน error)
4. **Sort** — เรียงตามตัวอักษรด้วย `sort()`
5. **Count** — นับจำนวนด้วย `len()`

---

## 💡 สิ่งที่ได้เรียนรู้
- List เป็นโครงสร้างข้อมูลพื้นฐานที่ใช้บ่อยที่สุดใน Python — เก็บข้อมูลแบบลำดับ (ordered) และแก้ไขได้ (mutable)
- ต้องเช็คก่อนลบด้วย `in` เพื่อป้องกัน `ValueError`
- Tuple เหมาะสำหรับข้อมูลที่ไม่ต้องการเปลี่ยน เช่น พิกัด, ค่าคงที่
- การรวม loop + list operations สามารถสร้างระบบ CRUD แบบง่ายได้
