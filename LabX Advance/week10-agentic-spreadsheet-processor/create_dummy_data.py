# agentic-spreadsheet-processor/create_dummy_data.py
"""สร้างไฟล์ data/input_data.xlsx (ชีต SalesData) ตามตัวอย่างในเอกสาร Lab"""
import os

import openpyxl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE_DIR, "data", "input_data.xlsx")

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "SalesData"  # ต้องตรงกับ source_sheet ใน config

ws.append(["Product Name", "Quantity", "Unit Price"])
data = [
    ["Laptop", 2, 1200.50], ["Mouse", 5, 25.00], ["Keyboard", 3, 75.99],
    ["Monitor", 1, 300.00], ["Projector", 1, 850.00], ["Webcam", 10, 45.00],
    ["Headset", 4, 99.99], ["SSD", 2, 180.00], ["Router", 1, 70.00],
]
for row in data:
    ws.append(row)
ws.column_dimensions["A"].width = 16
ws.column_dimensions["B"].width = 10
ws.column_dimensions["C"].width = 12

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
wb.save(OUTPUT)
print(f"Created {os.path.relpath(OUTPUT, BASE_DIR)} with {len(data)} products")
