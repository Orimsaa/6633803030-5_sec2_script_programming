# agentic-web-scraper/test_setup.py
# ทดสอบว่า Selenium + ChromeDriver ติดตั้งและเปิดเบราว์เซอร์ได้ก่อนรัน main.py
from src.driver_manager import DriverManager

manager = DriverManager(browser_type="chrome", headless=True)
driver = manager.get_driver()
driver.get("https://books.toscrape.com/")
print("Title:", driver.title)
manager.close_driver()
