# 📝 Week 1 Summary — Introduction to Python & Basic Syntax

**วิชา:** CP352301 Script Programming (Sec 2)  
**ชื่อ:** อัษฎาวุธ เรือนแก้ว | **รหัส:** 663380303-5  
**วันเรียน:** SEC2 Onsite วันอังคาร 23/6/69 เวลา 8:30-12:30 ห้อง SC9226

---

## 📌 กิจกรรมสัปดาห์นี้
1. แนะนำรายวิชา
2. บรรยายเรื่อง Getting Started with Python
3. ทำ Class Activities (Week 1: Python พื้นฐาน)

---

## 📋 ข้อมูลรายวิชาโดยรวม

**รหัสวิชา:** CP352301 Script Programming ภาคเรียน 1/2569  
**รูปแบบ:** self-paced, hybrid, online, project-based พร้อมใบรับรอง  
**ผู้สอน:** ผศ.บุญสืบ ไวคำ

### โครงสร้างวิชา 3 ส่วน

| ส่วนที่ | เนื้อหา | รายละเอียด |
|:-------:|---------|-----------|
| 1 | **Basics of Python** | บรรยาย + เรียนออนไลน์ด้วยตนเอง: Intro & Syntax, Strings & Console Output, Conditionals, Functions, Lists & Dictionaries, Loops, Advanced Topics, Classes, File I/O |
| 2 | **Application of Python** | Lab & Experiment: Systems/Network Programming, Python สำหรับแอปสมัยใหม่ |
| 3 | **Project & Conclusion** | Mini Project (midterm), Term Project (final), Final Exam |

### การให้คะแนน

| หมวด | สัดส่วน |
|------|:-------:|
| เข้าเรียน | 10% |
| เรียนออนไลน์รายบุคคล | 15% |
| งานกลุ่ม | 20% |
| Mini Project | 15% |
| Final Project | 20% |
| Final Exam | 20% |

### เกณฑ์เกรด
- **ผ่านขั้นต่ำ (D):** Codecademy/Datacamp ≥ 90%, Netacad Exam ≥ 50% (สำหรับใบรับรอง CISCO)
- **เกรด A:** ต้องได้ > 80% ใน **ทุกหมวด** (เข้าเรียน, งานรายสัปดาห์, Lab, Mini/Final Project, Final Exam)

### นโยบายสำคัญ
- ⚠️ **ความซื่อสัตย์ทางวิชาการ** — ห้ามคัดลอกโค้ดกัน, ห้ามส่งโค้ดทางอีเมล/แชท/โพสต์บนเว็บ → โทษ: 0 คะแนนโปรเจกต์, ลดเกรดเฉลี่ย 10%, รายงานต่อคณะกรรมการวินัย
- 🎓 **มารยาทในห้องเรียน** — ตรงเวลา, ไม่คุยระหว่างบรรยาย, ปิดเสียงมือถือ, ใช้แล็ปท็อปอย่างเหมาะสม

### เครื่องมือแนะนำ
- **Generative AI:** Gemini, ChatGPT, DeepSeek, Copilot — ช่วยเรียนรู้/เขียนโค้ด
- **Google Colab** — สำหรับ lab พื้นฐาน
- **GitHub** — สำหรับ lab ขั้นสูง/portfolio
- **NotebookLM** — สำหรับสรุปบทเรียน

---

## 📖 เนื้อหา Getting Started with Python

### 1. ปรัชญาของ Python (Zen of Python)
> - สวยงาม ดีกว่า อัปลักษณ์ *(Beautiful is better than ugly)*
> - ชัดเจน ดีกว่า กำกวม *(Explicit is better than implicit)*
> - เรียบง่าย ดีกว่า ซับซ้อน *(Simple is better than complex)*
> - **ความอ่านง่ายสำคัญที่สุด** *(Readability counts)*

### 2. ลักษณะทั่วไปของ Python
- **Dynamic typing** — ไม่ต้องประกาศชนิดข้อมูลล่วงหน้า
- **จัดการหน่วยความจำอัตโนมัติ** (Garbage Collection)
- รองรับหลายรูปแบบการเขียนโปรแกรม: **OOP, Imperative, Functional, Procedural**
- มี **Standard Library** ครอบคลุมหลากหลาย
- **Python 2.x** = เวอร์ชันเก่า (EOL) / **Python 3.x** = เวอร์ชันปัจจุบัน

### 3. การเริ่มต้นใช้งาน

```bash
# ตรวจสอบเวอร์ชัน
python --version

# เข้าสู่ Interactive Shell (REPL)
python
# หรือ
python3

# รันโค้ดแบบ string
python -c 'print("Hello")'

# ติดตั้งแพ็กเกจ
pip install <ชื่อแพ็กเกจ>
```

**วิธีเขียนโปรแกรม:**
- เขียนด้วย IDLE หรือสร้างไฟล์ `.py` แล้วรันผ่าน terminal
- ใช้ **interactive shell (REPL)** สำหรับทดสอบโค้ดสั้นๆ
- **Online Shell:** python.org/shell, repl.it, ideone.com

### 4. ตัวแปรและการตั้งชื่อ (Variables & Naming)

```python
# สร้างตัวแปร (ซ้ายไปขวาเท่านั้น)
name = "Tonkla"
age = 20
pi = 3.14

# กำหนดค่าหลายตัวแปรพร้อมกัน
x, y, z = 1, 2, 3

# Cascading assignment
a = b = c = 0
```

**กฎการตั้งชื่อตัวแปร:**
| กฎ | ตัวอย่าง |
|----|---------|
| ต้องขึ้นต้นด้วยตัวอักษรหรือ `_` | `name`, `_count` ✅ / `1name` ❌ |
| ตามด้วยตัวอักษร, ตัวเลข, `_` ได้ | `my_var2` ✅ |
| **case-sensitive** | `Name` ≠ `name` |
| ห้ามใช้ keyword ของ Python | `if`, `for`, `class` ❌ |

> ⚡ **ตัวแปรใน Python เปลี่ยนชนิดข้อมูลได้ตลอดเวลา** (Dynamic Typing)

### 5. Block Indentation

Python ใช้ **การเว้นวรรค (indentation)** แทนวงเล็บปีกกา `{ }` ในการกำหนดขอบเขตของ block:

```python
if age >= 18:
    print("Adult")      # ← ย่อหน้า 4 spaces = อยู่ใน if block
    print("Can vote")   # ← ย่อหน้า 4 spaces = อยู่ใน if block
print("Done")           # ← ไม่ย่อหน้า = อยู่นอก if block
```

> 📏 **PEP 8** แนะนำให้ใช้ **4 spaces** แทน tab

### 6. ชนิดข้อมูลพื้นฐาน (Built-in Types)

#### Primitive Types

| ชนิด | คำอธิบาย | ตัวอย่าง |
|------|---------|---------|
| `bool` | ค่าความจริง (subclass ของ int) | `True`, `False` |
| `int` | จำนวนเต็ม (ขนาดไม่จำกัด) | `42`, `-10`, `999999999999` |
| `float` | ทศนิยม | `3.14`, `-0.5` |
| `complex` | จำนวนเชิงซ้อน | `3+4j` |
| `str` | สตริง (ข้อความ) | `"Hello"`, `'World'` |

#### Collection Types

| ชนิด | ลักษณะ | Mutable? | ตัวอย่าง |
|------|--------|:--------:|---------|
| `list` | ลำดับ, ซ้ำได้ | ✅ | `[1, 2, 3]` |
| `tuple` | ลำดับ, ซ้ำได้ | ❌ | `(1, 2, 3)` |
| `set` | ไม่ซ้ำ, ไม่มีลำดับ | ✅ | `{1, 2, 3}` |
| `dict` | key-value pairs | ✅ | `{"a": 1, "b": 2}` |

#### Built-in Constants
- `True`, `False` — ค่าความจริง
- `None` — ค่าว่าง (ไม่มีค่า)
- `Ellipsis` (`...`) — ใช้ใน slicing ขั้นสูง
- `NotImplemented` — ใช้ใน operator overloading

#### ตรวจสอบชนิดข้อมูล
```python
type(42)           # <class 'int'>
type("Hello")      # <class 'str'>
isinstance(42, int)  # True
```

### 7. การแปลงชนิดข้อมูล (Type Conversion)

```python
# string → int
int("42")        # 42

# string → float
float("3.14")    # 3.14

# int → string
str(42)          # "42"

# float string → int (ต้องแปลง 2 ขั้น!)
int(float("3.14"))  # 3    ← ต้องทำแบบนี้
# int("3.14")       # ❌ ValueError!

# แปลงเป็น list/set
list("abc")      # ['a', 'b', 'c']
set([1, 2, 2, 3])  # {1, 2, 3}
```

### 8. ชนิดสตริงพิเศษ

| Prefix | ชนิด | ใช้งาน |
|:------:|------|-------|
| `b'...'` | bytes | ข้อมูลแบบ byte |
| `u'...'` | unicode | สตริง unicode (default ใน Python 3) |
| `r'...'` | raw string | ไม่ escape อักขระพิเศษ เช่น `r'\n'` แสดงเป็น `\n` จริงๆ |

### 9. Mutable vs Immutable

| Immutable (แก้ไขไม่ได้) | Mutable (แก้ไขได้) |
|:-----------------------:|:-----------------:|
| `int`, `float`, `str` | `list`, `dict`, `set` |
| `tuple`, `frozenset` | `bytearray` |

```python
# ใช้ id() ตรวจสอบว่าเป็น object เดียวกันหรือไม่
x = "hello"
y = x
print(id(x) == id(y))  # True — ชี้ไปที่ object เดียวกัน

x = "world"             # สร้าง object ใหม่
print(id(x) == id(y))  # False — x ชี้ไปที่ object ใหม่แล้ว
```

### 10. Collection Types แบบละเอียด

#### List
```python
fruits = ["apple", "banana", "cherry"]
fruits[0]          # "apple"
fruits[-1]         # "cherry"
fruits.append("date")
fruits.insert(1, "blueberry")
fruits.remove("banana")
fruits.pop(0)      # ลบและคืนค่าที่ตำแหน่ง 0
len(fruits)        # จำนวนสมาชิก
```

#### Tuple
```python
point = (10, 20)
point[0]           # 10
# point[0] = 99    # ❌ TypeError — immutable!
```

#### Dictionary
```python
student = {"name": "Tonkla", "age": 20}
student["name"]     # "Tonkla"
student["gpa"] = 3.5  # เพิ่ม key ใหม่

# iterate
for key in student.keys():
    print(key, student[key])
```

#### Set
```python
nums = {1, 2, 3, 3, 2}  # {1, 2, 3} — ไม่ซ้ำ
3 in nums               # True — ตรวจสอบสมาชิกเร็วกว่า list
```

#### defaultdict
```python
from collections import defaultdict
dd = defaultdict(int)    # ค่าเริ่มต้น = 0
dd["count"] += 1         # ไม่ต้องเช็คว่า key มีอยู่หรือไม่ — ป้องกัน KeyError
```

### 11. การรับข้อมูลจากผู้ใช้ (Interactive Input)

```python
# Python 3
name = input("Enter your name: ")    # ได้ค่าเป็น str เสมอ
age = int(input("Enter your age: "))  # ต้องแปลงเป็น int ก่อนคำนวณ

# Python 2 (ไม่ใช้แล้ว)
# name = raw_input("Enter your name: ")
```

> ⚠️ `input()` คืนค่าเป็น **string เสมอ** — ต้อง cast ก่อนนำไปคำนวณ!

---

## 📖 เนื้อหา Week 1: Introduction to Python & Basic Syntax

### เป้าหมายการเรียนรู้
1. เข้าใจบทบาทของ Python ใน scripting
2. เขียน/รันสคริปต์พื้นฐานได้
3. แยกแยะชนิดข้อมูลพื้นฐานได้

**เกณฑ์ประเมิน:** ความอ่านง่ายของโค้ด, ไวยากรณ์ที่ถูกต้อง, การรันสคริปต์สำเร็จ

### Python คืออะไร?
- ภาษาระดับสูงแบบ **interpreted**
- อ่านง่ายคล้าย pseudo-code
- ใช้ในงาน: **Automation, Web Development, Data Analysis, AI/ML**

### การติดตั้งสภาพแวดล้อม

| เครื่องมือ | รายละเอียด |
|-----------|-----------|
| **Anaconda** | ชุดติดตั้งสำหรับ data science (มี Python + library พร้อมใช้) |
| **VS Code** | พร้อม Python extension และเลือก interpreter |
| **Google Colab** | ใช้งานผ่านเบราว์เซอร์ ไม่ต้องติดตั้ง เหมาะกับผู้เริ่มต้น |

### ไวยากรณ์พื้นฐาน

#### print()
```python
print("Hello, World!")
print("A", "B", "C", sep="-")  # A-B-C
print("Hello", end=" ")
print("World")                  # Hello World (ไม่ขึ้นบรรทัดใหม่)
```

#### Comments
```python
# Comment บรรทัดเดียว

'''
Comment
หลายบรรทัด
(หรือ docstring)
'''
```

#### ตัวแปร & ชนิดข้อมูล
```python
name = "Tonkla"      # str
age = 20             # int
gpa = 3.75           # float
is_student = True    # bool

# f-string
print(f"ชื่อ {name} อายุ {age} ปี GPA {gpa}")
```

#### Input/Output
```python
name = input("ชื่อ: ")           # ได้ str
age = int(input("อายุ: "))       # แปลงเป็น int
height = float(input("ส่วนสูง: "))  # แปลงเป็น float
```

---

## 📂 Labs & Activities

### Lab 1.1: Hello World
ติดตั้ง Python/VS Code หรือใช้ Colab แล้วรันสคริปต์ "Hello World"

```python
print("Hello, World!")
```

### Lab 1.2: ตัวแปร, เลขคณิต, f-string & Input
เขียนสคริปต์ประกาศตัวแปรหลายชนิด, คำนวณเลขคณิตพื้นฐาน, ต่อสตริงด้วย f-string, รับค่าจากผู้ใช้พร้อมแปลงชนิดข้อมูล

```python
# ประกาศตัวแปร
name = "Tonkla"
age = 20
pi = 3.14159

# เลขคณิต
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")  # หารปัดลง
print(f"{a} % {b} = {a % b}")    # เศษจากการหาร
print(f"{a} ** {b} = {a ** b}")  # ยกกำลัง

# Input + แปลงชนิด
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old!")
```

### Activity 1.1: อภิปรายกลุ่ม
- การประยุกต์ใช้ scripting ในชีวิตจริง
- ตัวอย่าง: Automation, Web Scraping, Data Analysis ฯลฯ

### Activity 1.2: Python Puzzlers
ดูโค้ดสั้นๆ แล้วทายผลลัพธ์และชนิดข้อมูล:

```python
# Puzzle 1: int + float = ?
result = 10 + 3.14
print(type(result))   # <class 'float'>  ← int + float ได้ float

# Puzzle 2: string + string (ที่ดูเหมือนตัวเลข)
result = "10" + "20"
print(result)          # "1020"  ← ไม่ใช่ 30! เป็นการต่อ string

# Puzzle 3: input() ที่ไม่แปลงชนิด
x = input("Enter number: ")  # ผู้ใช้พิมพ์ 5
y = x + 10                    # ❌ TypeError! — str + int ไม่ได้
```

---

## 💡 Error Messages ที่ควรรู้

| Error | สาเหตุ | ตัวอย่าง |
|-------|--------|---------|
| `SyntaxError` | ไวยากรณ์ผิด | ลืมปิดวงเล็บ, ลืม `:` หลัง if |
| `TypeError` | ใช้ชนิดข้อมูลผิด | `"5" + 10` (str + int) |
| `NameError` | ใช้ตัวแปรที่ยังไม่ได้สร้าง | `print(x)` โดยไม่เคยสร้าง x |
| `ValueError` | ค่าไม่ถูกต้อง | `int("hello")` |

---

## 💡 สิ่งที่ได้เรียนรู้ในสัปดาห์นี้

1. **Python** เป็นภาษา interpreted ระดับสูง ที่เน้นความอ่านง่ายและเรียบง่าย
2. **Dynamic Typing** — ตัวแปรเปลี่ยนชนิดข้อมูลได้ตลอด ไม่ต้องประกาศชนิดล่วงหน้า
3. **Indentation** คือหัวใจของ Python — ใช้ 4 spaces แทน `{ }` ตาม PEP 8
4. **Built-in Types** มีหลากหลาย: bool, int, float, str, list, tuple, set, dict
5. ต้องเข้าใจ **Mutable vs Immutable** — เป็นพื้นฐานสำคัญสำหรับการจัดการข้อมูล
6. `input()` คืนค่าเป็น **string เสมอ** — ลืมแปลงชนิดจะ error
7. Python ใช้ในงานจริงหลากหลาย: **Automation, Web Dev, Data Analysis, AI/ML**
8. เครื่องมือที่ใช้ในวิชา: **Anaconda, VS Code, Google Colab, GitHub, NotebookLM**
