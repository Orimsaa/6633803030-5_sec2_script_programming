# agentic-document-automator/src/pdf_tasks.py
import io
import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.pdfgen import canvas

from utils import ensure_directory_exists, setup_logging

logger = setup_logging(__name__)


class PDFTasks:
    """PDF operations for the Document Agent: watermark, merge, extract text."""

    def __init__(self):
        logger.info("PDFTasks initialized.")

    @staticmethod
    def _create_text_watermark(watermark_text, width, height, font_size=50, color=(0, 0, 0, 0.2), angle=45):
        """สร้างหน้า PDF (ในหน่วยความจำ) ขนาดเท่าหน้าเอกสาร ที่มีข้อความลายน้ำหมุนเอียงกลางหน้า"""
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=(width, height))
        r, g, b, a = color
        c.setFillColor(Color(r, g, b, alpha=a))
        c.setFont("Helvetica-Bold", font_size)
        c.translate(width / 2, height / 2)
        c.rotate(angle)
        text_width = c.stringWidth(watermark_text, "Helvetica-Bold", font_size)
        c.drawString(-text_width / 2, -font_size / 4, watermark_text)
        c.showPage()
        c.save()
        buffer.seek(0)
        return PdfReader(buffer).pages[0]

    def apply_watermark(self, input_pdf_path, output_pdf_path, watermark_text, font_size=50,
                        color=(0.5, 0.5, 0.5, 0.2), angle=45):
        if not os.path.exists(input_pdf_path):
            logger.error(f"Input PDF for watermarking not found: {input_pdf_path}")
            return False
        ensure_directory_exists(os.path.dirname(output_pdf_path))
        try:
            reader = PdfReader(input_pdf_path)
            writer = PdfWriter()
            cache = {}
            for page in reader.pages:
                size = (float(page.mediabox.width), float(page.mediabox.height))
                if size not in cache:  # ลายน้ำ 1 แบบต่อขนาดหน้า
                    cache[size] = self._create_text_watermark(watermark_text, *size, font_size, color, angle)
                page.merge_page(cache[size])
                writer.add_page(page)
            with open(output_pdf_path, "wb") as f:
                writer.write(f)
            logger.info(f"Watermark '{watermark_text}' applied to {len(reader.pages)} page(s) -> '{output_pdf_path}'.")
            return True
        except Exception as e:
            logger.error(f"Error applying watermark to '{input_pdf_path}': {e}")
            return False

    def merge_pdfs(self, pdf_paths, output_path):
        if not pdf_paths:
            logger.warning("No PDF paths provided for merging.")
            return False
        writer = PdfWriter()
        ensure_directory_exists(os.path.dirname(output_path))
        for pdf_path in pdf_paths:
            if not os.path.exists(pdf_path):
                logger.warning(f"Skipping non-existent PDF: {pdf_path}")
                continue
            try:
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    writer.add_page(page)
                logger.info(f"Added '{os.path.basename(pdf_path)}' ({len(reader.pages)} page(s)) to merge queue.")
            except Exception as e:
                logger.error(f"Error reading PDF '{pdf_path}': {e}")
        if len(writer.pages) == 0:
            logger.warning("No pages were added; merged PDF not created.")
            return False
        try:
            with open(output_path, "wb") as f:
                writer.write(f)
            logger.info(f"Merged {len(writer.pages)} page(s) into '{output_path}'.")
            return True
        except Exception as e:
            logger.error(f"Error writing merged PDF: {e}")
            return False

    def extract_text_from_pdf(self, pdf_path):
        if not os.path.exists(pdf_path):
            logger.error(f"PDF file not found: {pdf_path}")
            return None
        try:
            reader = PdfReader(pdf_path)
            text_content = ""
            for page in reader.pages:
                text_content += (page.extract_text() or "") + "\n--- Page End ---\n"
            logger.info(f"Extracted text from {len(reader.pages)} page(s) of '{os.path.basename(pdf_path)}'.")
            return text_content
        except Exception as e:
            logger.error(f"Error extracting text: {e}")
            return None
