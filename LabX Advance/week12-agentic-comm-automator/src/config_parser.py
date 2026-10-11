# agentic-comm-automator/src/config_parser.py
import json
import os

from utils import setup_logging

logger = setup_logging(__name__)

REQUIRED_PARAMS = {
    "send_email": ["recipients", "subject_template", "body_template"],
    "send_sms": ["phone_numbers", "message_template"],
    "process_inbox": ["search_criteria", "rules"],
}


class ConfigParser:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in config file: {e}")
        self._validate_config()
        logger.info(f"Configuration loaded successfully from {os.path.basename(self.config_path)}")
        return self.config

    def _validate_config(self):
        if not isinstance(self.config.get("tasks"), list):
            raise ValueError("Config must contain a 'tasks' list.")
        for i, task in enumerate(self.config["tasks"], 1):
            for field in ("name", "type"):
                if field not in task:
                    raise ValueError(f"Task {i} is missing '{field}' field.")
            if task["type"] not in REQUIRED_PARAMS:
                raise ValueError(f"Task {i} has unsupported type '{task['type']}'.")
            params = task.get("parameters", {})
            missing = [p for p in REQUIRED_PARAMS[task["type"]] if p not in params]
            if missing:
                raise ValueError(f"Task {i} ({task['type']}) is missing parameter(s): {missing}")
            if task["type"] == "send_email" and "to" not in params["recipients"]:
                raise ValueError(f"Task {i} (send_email) 'recipients' must contain a 'to' list.")
        logger.info(f"Configuration validated ({len(self.config['tasks'])} tasks).")
