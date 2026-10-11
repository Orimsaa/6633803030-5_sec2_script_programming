# agentic-web-scraper/src/driver_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


class DriverManager:
    """สร้างและปิด Selenium WebDriver (Chrome / Firefox) พร้อมตั้งค่า headless และ User-Agent"""

    def __init__(self, browser_type: str = "chrome", headless: bool = True):
        self.browser_type = browser_type.lower()
        self.headless = headless
        self.driver = None

    def _chrome_service(self):
        """ใช้ webdriver-manager ดาวน์โหลด ChromeDriver หากล้มเหลวให้ Selenium Manager จัดการเอง"""
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            return ChromeService(ChromeDriverManager().install())
        except Exception as e:
            print(f"[DriverManager] webdriver-manager failed ({e}); falling back to Selenium Manager.")
            return ChromeService()

    def _firefox_service(self):
        try:
            from webdriver_manager.firefox import GeckoDriverManager
            return FirefoxService(GeckoDriverManager().install())
        except Exception as e:
            print(f"[DriverManager] webdriver-manager failed ({e}); falling back to Selenium Manager.")
            return FirefoxService()

    def get_driver(self):
        if self.browser_type == "chrome":
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument(f"user-agent={USER_AGENT}")
            self.driver = webdriver.Chrome(service=self._chrome_service(), options=options)

        elif self.browser_type == "firefox":
            options = webdriver.FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=self._firefox_service(), options=options)

        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

        # Implicit wait: เวลารอสูงสุดเมื่อค้นหา element ทั่วไป
        self.driver.implicitly_wait(10)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
