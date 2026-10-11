# agentic-comm-automator/create_sample_attachments.py
"""สร้างไฟล์แนบตัวอย่าง data/reports/sales_report.pdf และ data/reports/summary_data.xlsx"""
import datetime
import os

import openpyxl
from openpyxl.styles import Font
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "data", "reports")

SALES = [("Laptop", 2, 1200.50), ("Monitor", 3, 300.00), ("Keyboard", 10, 75.99),
         ("Mouse", 25, 25.00), ("Headset", 8, 99.99)]


def create_pdf(path):
    c = canvas.Canvas(path, pagesize=A4)
    _, height = A4
    c.setFont("Helvetica-Bold", 18)
    c.drawString(72, height - 72, "Daily Sales Report")
    c.setFont("Helvetica", 11)
    c.drawString(72, height - 96, f"Date: {datetime.date.today().isoformat()}")
    y = height - 140
    c.setFont("Helvetica-Bold", 11)
    for x, title in zip((72, 250, 330, 430), ("Product", "Qty", "Unit Price", "Total")):
        c.drawString(x, y, title)
    c.setFont("Helvetica", 11)
    grand = 0
    for name, qty, price in SALES:
        y -= 20
        total = qty * price
        grand += total
        for x, value in zip((72, 250, 330, 430), (name, str(qty), f"{price:,.2f}", f"{total:,.2f}")):
            c.drawString(x, y, value)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(330, y - 28, "Grand Total")
    c.drawString(430, y - 28, f"{grand:,.2f}")
    c.save()


def create_xlsx(path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Summary"
    ws.append(["Product", "Quantity", "Unit Price", "Total"])
    for cell in ws[1]:
        cell.font = Font(bold=True)
    for i, (name, qty, price) in enumerate(SALES, start=2):
        ws.append([name, qty, price, f"=B{i}*C{i}"])
    ws.append(["Grand Total", None, None, f"=SUM(D2:D{len(SALES) + 1})"])
    wb.save(path)


if __name__ == "__main__":
    os.makedirs(REPORTS_DIR, exist_ok=True)
    create_pdf(os.path.join(REPORTS_DIR, "sales_report.pdf"))
    create_xlsx(os.path.join(REPORTS_DIR, "summary_data.xlsx"))
    print("Created data/reports/sales_report.pdf and data/reports/summary_data.xlsx")
