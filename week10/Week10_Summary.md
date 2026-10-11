# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 10: Automating Spreadsheets (Excel & Google Sheets)

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 10)
- **LO 10.1:** สามารถอ่าน สร้าง และบันทึกไฟล์ `.xlsx` ด้วย `openpyxl` (Workbook, Worksheet, Cell) ได้
- **LO 10.2:** สามารถจัดรูปแบบเซลล์ (Font, Fill, Border, Alignment, number format, merge cells) ได้
- **LO 10.3:** สามารถใส่สูตร Excel, Conditional Formatting, Data Validation และสร้างกราฟด้วยโปรแกรมได้
- **LO 10.4:** สามารถออกแบบ Spreadsheet Agent ที่ทำงานตาม config พร้อมชีต Audit Log ได้
- **LO 10.5:** สามารถอธิบายแนวคิดการทำงานกับ Google Sheets API (`gspread`, Service Account) ได้

---

## 1. openpyxl พื้นฐาน

```python
wb = openpyxl.load_workbook("data/input_sales.xlsx")
ws = wb.active
for name, qty, price in ws.iter_rows(min_row=2, values_only=True):
    ...
out = openpyxl.Workbook(); sheet = out.create_sheet("Sales Report", 0)
cell = sheet.cell(row=1, column=1, value="Product Name")
cell.font = Font(bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", start_color="4CAF50")
sheet.merge_cells(start_row=7, start_column=1, end_row=7, end_column=3)
out.save("data/output_sales_report.xlsx")
```

## 2. ฟีเจอร์ขั้นสูง

| ฟีเจอร์ | โค้ด |
|:---|:---|
| สูตร | `ws["D2"] = "=B2*C2"` (คำนวณเมื่อเปิดใน Excel; อ่านค่าผลลัพธ์ด้วย `load_workbook(data_only=True)` หลัง Excel บันทึก) |
| Color Scale | `ColorScaleRule(start_type="min", ..., end_type="max", ...)` |
| Expression rule | `Rule(type="expression", formula=['$E2="High Value"'], dxf=DifferentialStyle(...))` |
| Dropdown | `DataValidation(type="list", formula1='"Pending,Approved,Rejected"')` |
| กราฟ | `BarChart()` + `Reference` + `chart.set_categories()` + `ws.add_chart(chart, "H2")` |

## 3. Google Sheets (แนวคิด)
`gspread` เรียก API บนคลาวด์ (เหมาะกับงานแชร์ร่วมกัน) ยืนยันตัวตนด้วย Service Account หรือ OAuth ส่วน `openpyxl` ทำงานกับไฟล์ในเครื่อง

---

## ไฟล์ปฏิบัติการ
| งาน | โฟลเดอร์ | ผลลัพธ์ |
|:---|:---|:---|
| LabX BASIC: Automating Spreadsheets | [spreadsheet-automator](./spreadsheet-automator) | `output_sales_report.xlsx` (Grand Total 3,203.97) |
| LabX ADV: Advanced Spreadsheet Automation & Agentic Workflows | [agentic-spreadsheet-processor](./agentic-spreadsheet-processor) | `output_report.xlsx` ชีต Audit Log / SalesData / Raw Data / Summary |
