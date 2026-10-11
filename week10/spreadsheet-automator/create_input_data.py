# spreadsheet-automator/create_input_data.py
"""สร้างไฟล์ตัวอย่าง data/input_sales.xlsx ตามเนื้อหาในเอกสาร Lab (มีแถวว่าง 1 แถวเพื่อทดสอบการข้ามแถว)"""
import os

import openpyxl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE_DIR, "data", "input_sales.xlsx")

rows = [
    ["Product Name", "Quantity", "Unit Price"],
    ["Laptop", 2, 1200.50],
    ["Mouse", 5, 25.00],
    ["Keyboard", 3, 75.99],
    ["Monitor", 1, 300.00],
    [None, None, None],          # แถวว่าง: สคริปต์ต้องข้ามได้
    ["Printer", 1, 150.00],
]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sheet1"
for row in rows:
    ws.append(row)

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
wb.save(OUTPUT)
print(f"Created {os.path.relpath(OUTPUT, BASE_DIR)}")
