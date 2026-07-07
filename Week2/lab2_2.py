# lab2_2.py
# ชื่อ: อัษฎาวุธ เรือนแก้ว
# รหัสนักศึกษา: 663380303-5

# Step 1: รับอายุจากผู้ใช้ แปลงเป็นจำนวนเต็ม
age = int(input("Enter your age: "))

# Step 2: แนะนำประเภทภาพยนตร์ตามช่วงอายุ
if age < 5:
    print("You're too young for movies! Enjoy cartoons.")
elif 5 <= age <= 12:
    print("Recommended: G-rated or PG-rated movies.")
elif 13 <= age <= 17:
    print("Recommended: PG-13 or R-rated (with parental guidance).")
else:
    print("Recommended: Any movie rating.")

    # Challenge: ถามเพิ่มเติมเฉพาะเมื่ออายุ 18 ปีขึ้นไป
    like_action = input("Do you like action movies? (yes/no): ").strip().lower()

    if like_action == "yes":
        print("You might enjoy the latest action blockbuster!")
