# document-automator/create_sample_pdfs.py
"""
สร้างไฟล์ PDF ตัวอย่างในโฟลเดอร์ documents/ สำหรับใช้ทดสอบ Lab
- input_article.pdf : บทความ 2 หน้า (ใช้ดึงข้อความไปสร้างรายงาน Word)
- dummy_doc1.pdf    : เอกสาร 1 หน้า (ใช้ทดสอบการรวม PDF)
- dummy_doc2.pdf    : เอกสาร 2 หน้า (ใช้ทดสอบการรวม PDF)
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "documents")
styles = getSampleStyleSheet()


def build_pdf(filename, pages):
    """pages = list of (heading, [paragraph, ...]) ; หนึ่ง tuple ต่อหนึ่งหน้า"""
    path = os.path.join(DOCS_DIR, filename)
    story = []
    for i, (heading, paragraphs) in enumerate(pages):
        story.append(Paragraph(heading, styles["Title"] if i == 0 else styles["Heading1"]))
        story.append(Spacer(1, 12))
        for text in paragraphs:
            story.append(Paragraph(text, styles["BodyText"]))
            story.append(Spacer(1, 8))
        if i < len(pages) - 1:
            story.append(PageBreak())
    SimpleDocTemplate(path, pagesize=A4, title=filename).build(story)
    print(f"Created documents/{filename} ({len(pages)} page(s))")


if __name__ == "__main__":
    os.makedirs(DOCS_DIR, exist_ok=True)
    build_pdf("input_article.pdf", [
        ("Automating Office Documents with Python", [
            "Office workers spend many hours every week copying text between PDF files and Word "
            "documents. Python can automate this kind of repetitive document work with a few "
            "well-known libraries.",
            "PyPDF2 reads PDF files page by page. It can extract text, merge several files into one, "
            "split a large file into smaller parts and rotate pages.",
            "python-docx creates and edits Word documents. It supports headings, paragraphs with "
            "bold or italic text, tables with styles and pictures.",
        ]),
        ("Challenges and Best Practices", [
            "Text extraction depends on how the PDF was created. Scanned PDFs contain images instead "
            "of text and need OCR tools such as Tesseract.",
            "Always check that input files exist, handle exceptions for corrupted files, and keep "
            "generated documents in a separate output folder.",
        ]),
    ])
    build_pdf("dummy_doc1.pdf", [
        ("Dummy Document 1", [
            "This is the first document used to test the PDF merge feature.",
            "It contains a single page.",
        ]),
    ])
    build_pdf("dummy_doc2.pdf", [
        ("Dummy Document 2", ["This is page 1 of the second document used to test the PDF merge feature."]),
        ("Dummy Document 2 - Page 2", ["This is page 2 of the second document. After merging, the output "
                                       "file should contain 3 pages in total."]),
    ])
