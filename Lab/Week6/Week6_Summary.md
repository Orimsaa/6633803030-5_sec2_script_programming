# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 6: Functions & Modules

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 6)
- **LO 6.1:** สามารถนิยามและเรียกใช้ฟังก์ชัน (Functions) เพื่อส่งเสริมการใช้โค้ดซ้ำ (Code Reusability) และความเป็นโมดูล (Modularity) ได้
- **LO 6.2:** สามารถเข้าใจแนวคิดของพารามิเตอร์ (Parameters), อาร์กิวเมนต์ (Arguments), ค่าเริ่มต้น (Default Values) และค่าส่งกลับ (Return Values) ได้
- **LO 6.3:** สามารถแยกแยะขอบเขตตัวแปร (Variable Scope) ระหว่าง Local และ Global และนำเข้าใช้งานฟังก์ชันจากโมดูลมาตรฐานและโมดูลที่สร้างขึ้นเองได้

---

## 1. ฟังก์ชัน (Functions)

ฟังก์ชันคือบล็อกของโค้ดที่ถูกจัดกลุ่มไว้เพื่อทำงานเฉพาะอย่างหนึ่ง สามารถเรียกใช้ซ้ำได้ตลอดทั้งโปรแกรม ช่วยลดความซ้ำซ้อนตามหลักการ **DRY (Don't Repeat Yourself)**

### 1.1 การนิยามและเรียกใช้ฟังก์ชัน

```python
def greet(name):
    """Greets the user by their provided name."""
    print(f"Hello, {name}!")

greet("Alice")    # เรียกใช้ฟังก์ชัน
greet("Bob")      # เรียกใช้ซ้ำ (Code Reuse!)
```

### 1.2 พารามิเตอร์และอาร์กิวเมนต์

| ประเภท | คำอธิบาย | ตัวอย่าง |
|:---|:---|:---|
| **Positional Arguments** | อาร์กิวเมนต์จับคู่ตามตำแหน่ง | `describe_pet("dog", "Buddy")` |
| **Keyword Arguments** | ระบุชื่อพารามิเตอร์ (ลำดับอิสระ) | `describe_pet(pet_name="Buddy", animal_type="dog")` |
| **Default Parameters** | ค่าเริ่มต้นหากไม่ส่งอาร์กิวเมนต์ | `def power(base, exponent=2)` |
| **`*args`** | รับอาร์กิวเมนต์ positional จำนวนไม่จำกัด | `def add(*args): return sum(args)` |

```python
# ฟังก์ชันกับ Default Parameter
def make_coffee(size="regular", type="latte"):
    """Describes a coffee order with default values."""
    print(f"Making a {size} {type} coffee.")

make_coffee()                                    # regular latte
make_coffee("large")                             # large latte
make_coffee(type="espresso", size="small")       # small espresso
```

### 1.3 ค่าส่งกลับ (Return Values)

```python
def add_numbers(num1, num2):
    """Adds two numbers and returns their sum."""
    return num1 + num2

result = add_numbers(10, 5)     # result = 15

# คืนค่าหลายค่า (Python คืนเป็น Tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = get_min_max([3, 1, 4, 1, 5])   # lo=1, hi=5
```

---

## 2. ขอบเขตตัวแปร (Variable Scope)

### 2.1 Local vs Global Variables

- **Local Variable:** ตัวแปรที่สร้างภายในฟังก์ชัน เข้าถึงได้เฉพาะภายในฟังก์ชันนั้น
- **Global Variable:** ตัวแปรที่สร้างนอกฟังก์ชัน เข้าถึงได้จากทุกส่วนของโปรแกรม
- **`global` keyword:** ใช้ภายในฟังก์ชันเพื่อแก้ไขตัวแปร Global (ควรใช้อย่างระมัดระวัง)

```python
global_message = "I am global"     # Global variable

def show_scope():
    local_message = "I am local"   # Local variable
    print(local_message)           # ✅ เข้าถึง local ได้
    print(global_message)          # ✅ อ่าน global ได้

show_scope()
print(global_message)              # ✅ เข้าถึง global ได้
# print(local_message)             # ❌ NameError: ตัวแปร local ไม่อยู่ในขอบเขต
```

### 2.2 กฎ LEGB (Local → Enclosing → Global → Built-in)
Python ค้นหาตัวแปรตามลำดับ: ฟังก์ชันภายใน → ฟังก์ชันครอบ → ระดับ Global → ฟังก์ชัน Built-in

---

## 3. โมดูล (Modules)

โมดูลคือไฟล์ `.py` ที่บรรจุโค้ด Python (ฟังก์ชัน, คลาส, ตัวแปร) สามารถนำเข้า (import) มาใช้ในไฟล์อื่นได้

### 3.1 วิธีการนำเข้าโมดูล

| รูปแบบการ import | ตัวอย่าง | การเรียกใช้ |
|:---|:---|:---|
| `import module` | `import math` | `math.sqrt(25)` |
| `import module as alias` | `import random as rnd` | `rnd.randint(1, 100)` |
| `from module import func` | `from math import sqrt, pi` | `sqrt(25)` (ไม่ต้องใช้ prefix) |
| `from module import *` | `from math import *` | ⚠️ ไม่แนะนำ (อาจชื่อชน) |

### 3.2 การสร้างโมดูลเอง (Custom Module)

```python
# my_utils.py (Custom Module)
def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def is_prime(number):
    """Returns True if the number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
```

```python
# main_program.py (Import custom module)
import my_utils
import math
import random

my_utils.greet("Alice")                    # Hello, Alice!
print(my_utils.is_prime(7))                # True
print(math.sqrt(16))                       # 4.0
print(random.randint(1, 100))              # Random number
```

### 3.3 โมดูลมาตรฐานที่สำคัญ (Standard Library)

| โมดูล | ฟังก์ชันตัวอย่าง | ประโยชน์ |
|:---|:---|:---|
| `math` | `sqrt()`, `pi`, `ceil()`, `floor()` | การคำนวณทางคณิตศาสตร์ |
| `random` | `randint()`, `choice()`, `shuffle()` | การสุ่มข้อมูล |
| `datetime` | `datetime.now()`, `timedelta()` | การจัดการวันที่และเวลา |
| `os` | `listdir()`, `path.exists()` | การจัดการไฟล์และระบบ |
| `collections` | `Counter()`, `defaultdict()` | โครงสร้างข้อมูลพิเศษ |

---

## 4. สรุปไฟล์ปฏิบัติการประจำสัปดาห์

| หัวข้อปฏิบัติการ | สาระสำคัญทางเทคนิค |
|:---|:---|
| **Lab 6.1** | **Simple Calculator Functions:** การนิยามฟังก์ชัน `add()`, `subtract()`, `multiply()`, `divide()` พร้อม Docstring, การจัดการ Division by Zero, และ Challenge: ฟังก์ชัน `power(base, exponent=2)` ที่ใช้ Default Parameter เพื่อยกกำลังสอง |
| **Lab 6.2** | **Custom Module and Standard Library Usage:** การสร้างโมดูลเอง (`my_utils.py`) ที่บรรจุฟังก์ชัน `greet()` และ `is_prime()` จากนั้นนำเข้าใช้งานใน `main_program.py` ร่วมกับโมดูลมาตรฐาน `math.sqrt()` และ `random.randint()` |
| **Activity 6.1** | **Refactoring a Previous Lab Assignment:** การ Refactor โค้ดจาก Week 2 Lab 2.1 (Number Classifier) โดยแยกตรรกะออกเป็นฟังก์ชัน `classify_sign()`, `classify_parity()`, `classify_number()` เพื่อเพิ่ม Readability และ Reusability |
| **Activity 6.2** | **Benefits of Modular Programming & Standard Library Exploration:** การอภิปรายประโยชน์ของ Modularity (Code Reuse, Debugging, Teamwork, Readability) และการสำรวจโมดูล `datetime`, `os`, `collections` จาก Standard Library |
