# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 8: Automating with CSV and JSON Data

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 8)
- **LO 8.1:** สามารถอ่าน/เขียนไฟล์ CSV ด้วย `csv.DictReader` / `csv.DictWriter` และประมวลผล (สรุป กรอง รวมกลุ่ม) ได้
- **LO 8.2:** สามารถอ่าน/แก้ไข/เขียน JSON ที่มีโครงสร้างซ้อน (nested) ด้วย `json.load` / `json.dump` ได้
- **LO 8.3:** สามารถแปลงข้อมูลระหว่าง CSV และ JSON พร้อมแปลงชนิดข้อมูล (string → int/float/bool) ได้
- **LO 8.4:** สามารถออกแบบ Data Agent ที่ทำงานตาม pipeline ใน config, ส่งต่อข้อมูลระหว่าง task และบันทึก audit report ได้

---

## 1. CSV

```python
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))          # [{'OrderID': '101', 'Amount': '1200.50', ...}, ...]
with open(out, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader(); writer.writerows(rows)
```
ค่าทุกตัวที่อ่านจาก CSV เป็น string ต้องแปลง `float()` ภายใน `try/except ValueError`

## 2. JSON

| ฟังก์ชัน | ใช้กับ |
|:---|:---|
| `json.load(f)` / `json.dump(obj, f, indent=2, ensure_ascii=False)` | ไฟล์ |
| `json.loads(s)` / `json.dumps(obj)` | สตริง |

การอ้างถึงข้อมูลซ้อนด้วย dot-path เช่น `"0.details.brand"` → `data[0]["details"]["brand"]`

## 3. Agentic Data Pipeline
`DataAgent` อ่าน task ทีละตัว (`load_csv` → `transform_csv_aggregate` → `save_csv` → `csv_to_json_conversion` → ...)
เก็บผลลัพธ์ใน `data_store[output_data_key]` และให้ task ถัดไปอ่านผ่าน `input_data_key` ทุกขั้นตอนถูกบันทึกใน audit log

---

## ไฟล์ปฏิบัติการ
| งาน | โฟลเดอร์ | ผลลัพธ์ |
|:---|:---|:---|
| LabX BASIC: Automating with CSV and JSON Data | [data-processor](../LabX%20Basic/week8-data-processor) | `output_filtered_sales.csv`, `output_updated_inventory.json` |
| LabX ADV: Agentic Data Processing | [agentic-data-processor](../LabX%20Advance/week8-agentic-data-processor) | `processed_sales_by_customer.csv`, `sales_data.json`, `updated_inventory.json`, audit report |
