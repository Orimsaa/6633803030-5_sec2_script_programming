# agentic-web-scraper/src/config_parser.py
import json
import os


class ConfigParser:
    """อ่านและตรวจสอบไฟล์ configuration ที่ใช้ควบคุมพฤติกรรมของ Scraper Agent"""

    REQUIRED_KEYS = [
        "start_url",
        "max_pages",
        "delay_between_pages",
        "item_container_selector",
        "item_data_selectors"
    ]

    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_config(self) -> dict:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        self._validate_config(config)
        return config

    def _validate_config(self, config: dict):
        for key in self.REQUIRED_KEYS:
            if key not in config:
                raise KeyError(f"Missing required configuration key: '{key}'")
        if not isinstance(config["max_pages"], int) or config["max_pages"] < 1:
            raise ValueError("'max_pages' must be a positive integer")
        if not isinstance(config["item_data_selectors"], dict):
            raise ValueError("'item_data_selectors' must be an object of field -> CSS selector")
