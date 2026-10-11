# agentic-spreadsheet-processor/src/config_parser.py
import json
import os

from utils import setup_logging

logger = setup_logging(__name__)

# ฟิลด์ที่ task แต่ละประเภทต้องมี
REQUIRED_TASK_FIELDS = {
    "copy_data": ["source_sheet", "dest_sheet"],
    "calculate_column": ["sheet", "target_column", "formula"],
    "conditional_format": ["sheet", "range", "rule_type"],
    "chart": ["sheet", "chart_type", "data_range"],
    "summary_sheet": ["source_sheet", "metrics"],
    "data_validation": ["sheet", "target_column", "options"],
}


class ConfigParser:
    """
    Parses and validates the spreadsheet automation configuration from a JSON file.
    """

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        """Loads the configuration from the specified JSON file."""
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
        """Validates required top-level fields and per-task parameters."""
        for field in ["input_file", "output_file", "tasks"]:
            if field not in self.config:
                raise ValueError(f"Missing required field in config: '{field}'")
        if not isinstance(self.config["tasks"], list):
            raise ValueError("Config field 'tasks' must be a list.")
        for i, task in enumerate(self.config["tasks"], 1):
            if "type" not in task:
                raise ValueError(f"Task {i} is missing 'type' field.")
            missing = [f for f in REQUIRED_TASK_FIELDS.get(task["type"], []) if f not in task]
            if missing:
                raise ValueError(f"Task {i} ({task['type']}) is missing field(s): {missing}")
        logger.info(f"Configuration validated ({len(self.config['tasks'])} tasks).")
