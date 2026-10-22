# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 5: Data Structures: Dictionaries & Sets

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 5)
- **LO 5.1:** สามารถจัดระเบียบข้อมูลด้วยโครงสร้างคู่กุญแจ-ค่า (Dictionaries) เพื่อการดึงข้อมูลที่รวดเร็วระดับ O(1) ได้
- **LO 5.2:** สามารถจัดการชุดข้อมูลที่ไม่ซ้ำกัน (Sets) และดำเนินการทางคณิตศาสตร์เชิงเซต (Union, Intersection, Difference, Symmetric Difference) ได้
- **LO 5.3:** สามารถเลือกใช้โครงสร้างข้อมูลที่เหมาะสม (List, Tuple, Dictionary, Set) สำหรับปัญหาที่กำหนดได้

---

## 1. โครงสร้างข้อมูลแบบดิกชันนารี (Dictionaries)

Dictionary คือโครงสร้างข้อมูลที่จับคู่ระหว่าง **Key** และ **Value** โดย Key ต้องเป็นวัตถุที่ไม่สามารถเปลี่ยนแปลงค่าได้ (Immutable และ Hashable) เช่น สตริง ตัวเลข หรือทูเพิล ส่วน Value สามารถเป็นข้อมูลประเภทใดก็ได้

### 1.1 การสร้างและเข้าถึงข้อมูล

```python
# การสร้าง Dictionary
student_profile = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.7
}

# การเข้าถึงแบบปกติ vs แบบปลอดภัย
print(student_profile["name"])                          # Direct access
print(student_profile.get("city", "Not Specified"))     # Safe access with default
```

### 1.2 เมธอดสำหรับการจัดการ Dictionary

| ชื่อเมธอด | หน้าที่การทำงาน | ตัวอย่างคำสั่ง | ผลลัพธ์จากการดำเนินการ |
|:---|:---|:---|:---|
| `dict[key] = value` | เพิ่มหรือแก้ไขค่า | `d["city"] = "Bangkok"` | เพิ่มคีย์ใหม่หรืออัปเดตค่าเดิม |
| `.get(key, default)` | เข้าถึงค่าอย่างปลอดภัย | `d.get("city", "N/A")` | คืนค่า default หากไม่พบคีย์ |
| `.pop(key)` | ลบคีย์และคืนค่า | `d.pop("major")` | คืนค่าและลบคีย์ออก |
| `.popitem()` | ลบคู่สุดท้ายที่เพิ่มเข้า | `d.popitem()` | คืนค่า tuple ของคู่ key-value |
| `.keys()` | ดึงคีย์ทั้งหมด | `d.keys()` | View object ของคีย์ทั้งหมด |
| `.values()` | ดึงค่าทั้งหมด | `d.values()` | View object ของค่าทั้งหมด |
| `.items()` | ดึงคู่ key-value ทั้งหมด | `d.items()` | View object ของ tuple คู่ key-value |
| `del dict[key]` | ลบรายการ | `del d["age"]` | ลบคีย์ที่ระบุออกจาก Dictionary |

### 1.3 การวนลูปเข้าถึงข้อมูล

```python
my_book = {"title": "The Python Journey", "author": "A. Coder", "pages": 350}

# วนลูปผ่าน key-value pairs
for key, value in my_book.items():
    print(f"{key}: {value}")
```

---

## 2. โครงสร้างข้อมูลแบบเซต (Sets)

Set คือโครงสร้างข้อมูลที่ **ไม่เรียงลำดับ (Unordered)** และสมาชิกทุกตัวต้อง **ไม่ซ้ำกัน (Unique)** เหมาะสำหรับการลบข้อมูลซ้ำซ้อนและการดำเนินการทางคณิตศาสตร์เชิงเซต

### 2.1 การสร้างและจัดการ Set

```python
# สร้าง Set จาก List (ลบตัวซ้ำอัตโนมัติ)
unique_numbers = set([1, 2, 2, 3, 4, 4, 5])  # ผลลัพธ์: {1, 2, 3, 4, 5}

# สร้าง Set ว่าง (ต้องใช้ set() เพราะ {} สร้าง Dictionary)
empty_set = set()

# เพิ่ม/ลบสมาชิก
vowels = {"a", "e", "i", "o", "u"}
vowels.add("y")        # เพิ่มสมาชิก
vowels.discard("z")    # ลบอย่างปลอดภัย (ไม่มี error ถ้าไม่พบ)
```

### 2.2 ตัวดำเนินการทางคณิตศาสตร์เชิงเซต

| ตัวดำเนินการ | เมธอด | ความหมาย | ตัวอย่าง (A={1,2,3}, B={3,4,5}) | ผลลัพธ์ |
|:---:|:---|:---|:---|:---|
| `\|` | `.union()` | รวมสมาชิกทั้งหมด | `A \| B` | `{1, 2, 3, 4, 5}` |
| `&` | `.intersection()` | สมาชิกร่วมกัน | `A & B` | `{3}` |
| `-` | `.difference()` | สมาชิกใน A แต่ไม่อยู่ใน B | `A - B` | `{1, 2}` |
| `^` | `.symmetric_difference()` | สมาชิกที่ไม่ซ้ำกัน | `A ^ B` | `{1, 2, 4, 5}` |

### 2.3 ความปลอดภัยในการลบสมาชิก

- **`.remove(item)`:** หากไม่พบสมาชิก จะเกิดข้อผิดพลาด `KeyError` ทำให้โปรแกรมหยุดทำงาน
- **`.discard(item)`:** หากไม่พบสมาชิก จะข้ามผ่านโดยไม่เกิดข้อผิดพลาด (Safe operation)

---

## 3. การเปรียบเทียบโครงสร้างข้อมูลทั้ง 4 ประเภท

| เกณฑ์ | List | Tuple | Dictionary | Set |
|:---|:---|:---|:---|:---|
| **ไวยากรณ์** | `[ ]` | `( )` | `{ key: value }` | `{ }` หรือ `set()` |
| **ลำดับ** | Ordered | Ordered | Ordered (3.7+) | Unordered |
| **Mutability** | Mutable | Immutable | Mutable | Mutable |
| **ข้อมูลซ้ำ** | อนุญาต | อนุญาต | Key ซ้ำไม่ได้ | ไม่อนุญาต |
| **การค้นหา** | O(n) | O(n) | O(1) | O(1) |
| **Use Case** | ข้อมูลลำดับ | ค่าคงที่ | แมปข้อมูล key-value | ข้อมูลไม่ซ้ำ |

---

## 4. สรุปไฟล์ปฏิบัติการประจำสัปดาห์

| หัวข้อปฏิบัติการ | สาระสำคัญทางเทคนิค |
|:---|:---|
| **Lab 5.1** | **Simple Contact Book Manager (Dictionary Focus):** การสร้างระบบจัดการสมุดโทรศัพท์ด้วย Dictionary ประกอบด้วย CRUD operations ใช้เมธอด `.get()` สำหรับการเข้าถึงอย่างปลอดภัย, `.items()` สำหรับการวนลูป, `.pop()` สำหรับการลบ พร้อม Challenge: case-insensitive keys ด้วย `.lower()` |
| **Lab 5.2** | **Course Enrollment & Collaboration (Set Focus):** การจำลองระบบลงทะเบียนเรียนด้วย Set Operations ใช้ `.intersection()` หานักศึกษาที่เรียนทั้ง 2 วิชา, `.union()` หารายชื่อทั้งหมด, `.difference()` หานักศึกษาเฉพาะวิชา, `.symmetric_difference()` หานักศึกษาที่เรียนวิชาเดียว และการแปลง List → Set → List เพื่อลบข้อมูลซ้ำ |
| **Activity 5.1** | **Real-World Applications of Dictionaries and Sets:** การระดมความคิดยกตัวอย่างการประยุกต์ใช้ Dictionary (Inventory, Character Stats, Product Database) และ Set (User Permissions, Unique Visitors, Blocked IPs) |
| **Activity 5.2** | **Word Frequency Counter:** การสร้างโปรแกรมนับความถี่คำด้วย Dictionary วนลูปตรวจสอบ key existence แล้วเพิ่ม/สร้างค่า พร้อม Challenge: ลบเครื่องหมายวรรคตอนด้วย `word.strip('.,!?"')` |
