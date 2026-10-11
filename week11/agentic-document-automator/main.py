# agentic-document-automator/main.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'src'))

from config_parser import ConfigParser
from document_agent import DocumentAgent
from utils import ensure_directory_exists, setup_logging

logger = setup_logging("main")

PATH_KEYS = ["template_path", "output_path", "input_pdf", "output_pdf", "input_docx", "output_text_file"]


def resolve_paths(config):
    """แปลง path (relative กับโฟลเดอร์โปรเจกต์) ใน config ให้เป็น absolute path"""
    for key, value in config.get('output_files', {}).items():
        config['output_files'][key] = os.path.normpath(os.path.join(BASE_DIR, value))
    for task in config['tasks']:
        for k in PATH_KEYS:
            if k in task:
                task[k] = os.path.normpath(os.path.join(BASE_DIR, task[k]))
        if 'input_pdfs' in task:
            task['input_pdfs'] = [os.path.normpath(os.path.join(BASE_DIR, p)) for p in task['input_pdfs']]


def check_required_files(config):
    """
    ตรวจสอบไฟล์ input ทุกไฟล์ก่อนเริ่ม (ไม่นับไฟล์ที่ task ก่อนหน้าจะสร้างขึ้นเอง
    เช่น extract_word_text อ่าน generated_report.docx ที่ task แรกสร้าง)
    """
    produced = set()
    missing = []
    for task in config['tasks']:
        inputs = [task[k] for k in ('template_path', 'input_pdf', 'input_docx') if k in task]
        inputs += task.get('input_pdfs', [])
        missing += [p for p in inputs if p not in produced and not os.path.exists(p)]
        produced.update(task[k] for k in ('output_path', 'output_pdf') if k in task)
    for p in missing:
        logger.critical(f"Missing required input file: {os.path.relpath(p, BASE_DIR)}")
    return not missing


def main():
    config_file_path = os.path.join(BASE_DIR, 'configs', 'document_automation_config.json')
    ensure_directory_exists(os.path.join(BASE_DIR, 'documents'))
    ensure_directory_exists(os.path.join(BASE_DIR, 'templates'))

    try:
        config = ConfigParser(config_file_path).load_config()
    except (FileNotFoundError, ValueError) as e:
        logger.critical(f"Configuration error: {e}")
        return

    resolve_paths(config)
    if not check_required_files(config):
        logger.critical("Run 'python create_sample_documents.py' to create the template and sample PDFs.")
        return

    agent = DocumentAgent(config, reports_dir=os.path.join(BASE_DIR, 'documents', 'reports'))
    if agent.run():
        logger.info("Document automation process completed successfully.")
    else:
        logger.warning("Document automation finished with errors. Check the audit report.")


if __name__ == "__main__":
    main()
