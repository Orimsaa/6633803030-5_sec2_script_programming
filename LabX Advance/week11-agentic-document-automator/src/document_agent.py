# agentic-document-automator/src/document_agent.py
import datetime
import json
import os

from pdf_tasks import PDFTasks
from utils import ensure_directory_exists, log_audit_entry, setup_logging
from word_tasks import WordTasks

logger = setup_logging(__name__)


class DocumentAgent:
    """
    Agent ที่ทำงานเอกสารตามลำดับ task ใน config:
    สร้างรายงาน Word จาก template, ใส่ลายน้ำ PDF, รวม PDF และดึงข้อความจาก PDF/Word
    แล้วสรุปผลเป็น audit report (JSON)
    """

    def __init__(self, config, reports_dir):
        self.config = config
        self.reports_dir = reports_dir
        self.audit_log = []
        self.start_time = datetime.datetime.now()
        self.pdf_processor = PDFTasks()
        self.word_processor = WordTasks()
        self.handlers = {
            "generate_word_report": self._generate_word_report,
            "apply_pdf_watermark": self._apply_pdf_watermark,
            "merge_pdfs": self._merge_pdfs,
            "extract_pdf_text": self._extract_pdf_text,
            "extract_word_text": self._extract_word_text,
        }

    # --- task handlers ---------------------------------------------------
    def _generate_word_report(self, task):
        placeholders = {**self.config.get("global_data", {}), **task.get("data", {})}
        return self.word_processor.generate_report_from_template(
            task["template_path"], task["output_path"], placeholders, task.get("table_data"))

    def _apply_pdf_watermark(self, task):
        return self.pdf_processor.apply_watermark(
            task["input_pdf"], task["output_pdf"], task["watermark_text"],
            task.get("font_size", 50), tuple(task.get("color", [0.5, 0.5, 0.5, 0.2])), task.get("angle", 45))

    def _merge_pdfs(self, task):
        return self.pdf_processor.merge_pdfs(task["input_pdfs"], task["output_pdf"])

    @staticmethod
    def _write_text(path, text):
        ensure_directory_exists(os.path.dirname(path))
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True

    def _extract_pdf_text(self, task):
        text = self.pdf_processor.extract_text_from_pdf(task["input_pdf"])
        return bool(text) and self._write_text(task["output_text_file"], text)

    def _extract_word_text(self, task):
        text = self.word_processor.extract_text_from_word(task["input_docx"])
        return bool(text) and self._write_text(task["output_text_file"], text)

    # --- run -----------------------------------------------------------------
    def _process_task(self, task):
        task_type = task.get("type")
        task_name = task.get("name", task_type)
        log_audit_entry(self.audit_log, "INFO", f"Starting task '{task_name}'", task_type)
        try:
            success = self.handlers[task_type](task)
        except Exception as e:
            log_audit_entry(self.audit_log, "ERROR", f"Error in '{task_name}': {e}", task_type)
            return False
        if success:
            log_audit_entry(self.audit_log, "SUCCESS", f"Task '{task_name}' completed.", task_type)
        else:
            log_audit_entry(self.audit_log, "ERROR", f"Task '{task_name}' failed.", task_type)
        return success

    def _generate_audit_report(self):
        ensure_directory_exists(self.reports_dir)
        report_path = os.path.join(self.reports_dir,
                                   f"audit_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(self.audit_log, f, indent=4, ensure_ascii=False)
        logger.info(f"Audit report saved to: {report_path}")
        return report_path

    def run(self):
        log_audit_entry(self.audit_log, "INFO", "Document Agent started.", "agent_run")
        results = [self._process_task(task) for task in self.config.get("tasks", [])]
        duration = (datetime.datetime.now() - self.start_time).total_seconds()
        log_audit_entry(self.audit_log, "INFO",
                        f"Finished {sum(results)}/{len(results)} task(s) successfully in {duration:.2f}s.",
                        "agent_run_summary")
        self._generate_audit_report()
        return all(results)
