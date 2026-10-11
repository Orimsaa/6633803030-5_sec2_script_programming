# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 11: Automating PDFs & Word Documents

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 11)
- **LO 11.1:** สามารถดึงข้อความ รวม และแยกไฟล์ PDF ด้วย `PyPDF2` (`PdfReader`, `PdfWriter`) ได้
- **LO 11.2:** สามารถสร้างเอกสาร Word ด้วย `python-docx` (heading, paragraph formatting, table, picture) ได้
- **LO 11.3:** สามารถสร้างรายงานจาก template ด้วยการแทนที่ placeholder และแทรกตารางตามตำแหน่งได้
- **LO 11.4:** สามารถใส่ลายน้ำ PDF โดยสร้างหน้าลายน้ำด้วย `reportlab` แล้ว `merge_page` ได้
- **LO 11.5:** สามารถออกแบบ Document Agent ที่ทำงานตาม config และบันทึก audit report ได้

---

## 1. PDF ด้วย PyPDF2

```python
reader = PdfReader("input_article.pdf")
text = "".join(page.extract_text() for page in reader.pages)
writer = PdfWriter()
for path in ["dummy_doc1.pdf", "dummy_doc2.pdf"]:
    for page in PdfReader(path).pages:
        writer.add_page(page)
with open("merged_output.pdf", "wb") as f:
    writer.write(f)
```

## 2. Word ด้วย python-docx

| งาน | โค้ด |
|:---|:---|
| หัวข้อ | `doc.add_heading("Report", level=1)` |
| ย่อหน้า + รูปแบบ | `run = doc.add_paragraph(text).runs[0]; run.bold = True; run.font.size = Pt(12)` |
| ตาราง | `table = doc.add_table(rows, cols); table.style = "Table Grid"` |
| แทนที่ placeholder | ต้องรวมข้อความทุก `run` ก่อน เพราะ Word อาจแบ่ง `{{KEY}}` เป็นหลายส่วน |

## 3. ลายน้ำ
สร้าง PDF หน้าเดียวที่มีข้อความเอียงโปร่งใสด้วย `reportlab.pdfgen.canvas` (`setFillColor(Color(r, g, b, alpha))`, `rotate()`) แล้ว `page.merge_page(watermark_page)` ทุกหน้า

## 4. ข้อจำกัด
PDF แบบสแกนต้องใช้ OCR, ข้อความที่ดึงจาก PDF อาจตัดบรรทัดไม่ตรงต้นฉบับ, ควรตรวจไฟล์ input ก่อนเริ่มเสมอ

---

## ไฟล์ปฏิบัติการ
| งาน | โฟลเดอร์ | ผลลัพธ์ |
|:---|:---|:---|
| LabX BASIC: Automating PDFs & Word Documents | [document-automator](../LabX%20Basic/week11-document-automator) | `output_report.docx`, `merged_output.pdf` |
| LabX ADV: Agentic Document Automation | [agentic-document-automator](../LabX%20Advance/week11-agentic-document-automator) | `generated_report.docx`, `watermarked_document.pdf`, `merged_docs.pdf` |
