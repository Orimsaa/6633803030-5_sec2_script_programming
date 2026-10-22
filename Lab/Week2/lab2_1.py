# lab2_1.py
# ชื่อ: อัษฎาวุธ เรือนแก้ว
# รหัสนักศึกษา: 663380303-5

# Step 1: รับตัวเลขจำนวนเต็มจากผู้ใช้
num = int(input("Enter an integer: "))

# Step 2: ตรวจสอบบวก / ลบ / ศูนย์
if num > 0:
    sign = "positive"
elif num < 0:
    sign = "negative"
else:
    sign = "zero"

# Step 3: ตรวจสอบคู่ / คี่
if num % 2 == 0:
    parity = "even"
else:
    parity = "odd"

# Step 4 (Challenge): รวมผลลัพธ์ทั้งสองในประโยคเดียว
print(f"The number is {sign} and {parity}.")
