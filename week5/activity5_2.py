# ============================================================
# Activity 5.2: Word Frequency Counter (using Dictionary)
# ------------------------------------------------------------
# รับข้อความจากผู้ใช้ แล้วนับจำนวนความถี่ของแต่ละคำโดยใช้ Dictionary
# Challenge: จัดการเครื่องหมายวรรคตอน
# ============================================================

# รับข้อความประโยคจากผู้ใช้
sentence = input("Please Enter a sentence: ").lower()

# แยกประโยคออกเป็นคำ
words = sentence.split()

# กำหนด Dictionary เปล่า
word_counts = {}

# วนลูปอ่านคำแต่ละคำ
for word in words:
    # Challenge: ลบเครื่องหมายวรรคตอนออก
    word = word.strip('.,!?"')

    # ข้ามคำว่าง (กรณีที่คำเป็นแค่เครื่องหมายวรรคตอนล้วนๆ)
    if not word:
        continue

    # เช็กว่าคำนั้นมีอยู่ใน Key ของ Dictionary แล้วหรือยัง
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# แสดงผลลัพธ์
print(word_counts)
