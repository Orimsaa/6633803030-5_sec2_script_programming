# agentic-document-automator/src/config_parser.py
import json
import os

from utils import setup_logging

logger = setup_logging(__name__)

REQUIRED_TASK_FIELDS = {
    "generate_word_report": ["template_path", "output_path"],
    "apply_pdf_watermark": ["input_pdf", "output_pdf", "watermark_text"],
    "merge_pdfs": ["input_pdfs", "output_pdf"],
    "extract_pdf_text": ["input_pdf", "output_text_file"],
    "extract_word_text": ["input_docx", "output_text_file"],
}


class ConfigParser:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        if not os.path.exists(self.config_path):
            logger.critical(f"Configuration file not found: {self.config_path}")
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except json.JSONDecodeError as e:
            logger.critical(f"Invalid JSON format in config file: {e}")
            raise ValueError(f"Invalid JSON format in config file: {e}")
        self._validate_config()
        logger.info(f"Configuration loaded successfully from {self.config_path}")
        return self.config

    def _validate_config(self):
        for field in ["global_data", "tasks"]:
            if field not in self.config:
                raise ValueError(f"Missing required field in config: '{field}'")
        if not isinstance(self.config["tasks"], list):
            raise ValueError("Config field 'tasks' must be a list.")
        for i, task in enumerate(self.config["tasks"], 1):
            if "type" not in task:
                raise ValueError(f"Task {i} is missing 'type' field.")
            if task["type"] not in REQUIRED_TASK_FIELDS:
                raise ValueError(f"Task {i} has unsupported type '{task['type']}'.")
            missing = [f for f in REQUIRED_TASK_FIELDS[task["type"]] if f not in task]
            if missing:
                raise ValueError(f"Task {i} ({task['type']}) is missing field(s): {missing}")
        logger.info(f"Configuration validated ({len(self.config['tasks'])} tasks).")
