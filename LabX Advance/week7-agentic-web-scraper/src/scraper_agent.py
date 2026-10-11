# agentic-web-scraper/src/scraper_agent.py
import time
from dataclasses import asdict

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By

from src.data_models import Product
from src.driver_manager import DriverManager
from src.utils import safe_click, wait_for_element


class ScraperAgent:
    """
    "Agent" ที่ทำงานตามคำสั่งจากไฟล์ configuration:
    เปิดหน้าเว็บ -> รอให้สินค้าโหลด -> ดึงข้อมูลตาม selector -> กดหน้าถัดไป จนครบ max_pages
    """

    def __init__(self, config: dict, browser: str = "chrome", headless: bool = True):
        self.config = config
        self.max_retries = config.get("max_retries", 3)
        self.driver_manager = DriverManager(browser_type=browser, headless=headless)
        self.driver = self.driver_manager.get_driver()

    def _load_with_retry(self, url: str = None) -> bool:
        """
        Retry mechanism: โหลดหน้า (หรือรอหน้าปัจจุบัน) แล้วรอ item container ด้วย Explicit Wait
        หากล้มเหลวจากข้อผิดพลาดชั่วคราวจะลองใหม่สูงสุด max_retries ครั้ง (backoff 2, 4, 6 วินาที)
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                if url:
                    self.driver.get(url)
                wait_for_element(self.driver, self.config["item_container_selector"], timeout=15)
                return True
            except (TimeoutException, WebDriverException) as e:
                print(f"  [Retry {attempt}/{self.max_retries}] Page not ready: {type(e).__name__}")
                if attempt < self.max_retries:
                    time.sleep(2 * attempt)
                    if not url:
                        self.driver.refresh()
        return False

    def run(self) -> list:
        results = []
        try:
            if not self._load_with_retry(self.config["start_url"]):
                print("Could not load start page after retries. Stopping.")
                return results
            current_page = 1

            while current_page <= self.config["max_pages"]:
                print(f"Scraping page {current_page}...")
                # หน่วงเวลาระหว่างหน้า (rate limiting / anti-blocking)
                time.sleep(self.config["delay_between_pages"])

                items = self.driver.find_elements(By.CSS_SELECTOR, self.config["item_container_selector"])
                for item in items:
                    product_data = self._parse_item(item)
                    results.append(asdict(product_data))
                print(f"  -> found {len(items)} items on page {current_page}")

                # Handle Pagination
                pagination_selector = self.config.get("pagination_selector")
                if pagination_selector and current_page < self.config["max_pages"]:
                    next_buttons = self.driver.find_elements(By.CSS_SELECTOR, pagination_selector)
                    if next_buttons:
                        safe_click(self.driver, next_buttons[0])
                        if not self._load_with_retry():
                            print("Next page did not load. Stopping.")
                            break
                        current_page += 1
                    else:
                        print("No next page button found. Stopping.")
                        break
                else:
                    break

        finally:
            self.driver_manager.close_driver()

        return results

    def _parse_item(self, item) -> Product:
        selectors = self.config["item_data_selectors"]

        def get_text(selector):
            if not selector:
                return None
            try:
                return item.find_element(By.CSS_SELECTOR, selector).text.strip()
            except Exception:
                return None

        def get_attr(selector, attr):
            if not selector:
                return None
            try:
                return item.find_element(By.CSS_SELECTOR, selector).get_attribute(attr)
            except Exception:
                return None

        # ชื่อหนังสือบนหน้า list ถูกตัดเป็น "..." จึงใช้ attribute title ก่อน หากไม่มีจึงใช้ข้อความ
        name = get_attr(selectors.get("name"), "title") or get_text(selectors.get("name"))

        return Product(
            name=name,
            price=get_text(selectors.get("price")),
            description=get_text(selectors.get("description")),
            url=get_attr(selectors.get("url"), "href"),
            image_url=get_attr(selectors.get("image_url"), "src")
        )
