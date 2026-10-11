# agentic-web-scraper/src/utils.py
import json
import os
import time
from typing import Any, Dict, List

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def save_data_to_json(data: List[Dict[str, Any]], filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def wait_for_element(driver, selector: str, timeout: int = 10, by: By = By.CSS_SELECTOR):
    """Explicit wait: รอจนกว่า element จะปรากฏบนหน้า (เหมาะกับเนื้อหาไดนามิก)"""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )


def safe_click(driver, element):
    """เลื่อนหน้าไปยัง element ก่อนคลิก เพื่อลดปัญหา element ถูกบัง"""
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)
    element.click()
