# web-scraping-intro/main.py
import json
import os
import sys

# เพิ่มไดเรกทอรี 'src' เข้าไปใน Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scraper import SimpleWebScraper

# ไฟล์สำหรับบันทึกผลลัพธ์ (Optional ตามโครงสร้างใน Lab)
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'scraped_output.json')


def save_to_json(data, file_path):
    """บันทึกข้อมูลที่ scrape ได้ลงไฟล์ JSON (รองรับภาษาไทย)"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    """
    จุดเริ่มต้นหลักสำหรับแอปพลิเคชัน web scraping อย่างง่าย
    """
    target_url = "https://automatetheboringstuff.com/3e/"
    scraper = SimpleWebScraper(target_url)

    scraped_data = scraper.scrape_main_titles()

    if scraped_data:
        print("\n--- ข้อมูลที่ Scrape ได้ ---")
        print(f"ชื่อหนังสือ: {scraped_data['book_title']}")
        print("\nชื่อบทต่างๆ:")
        if scraped_data['chapter_titles']:
            for i, title in enumerate(scraped_data['chapter_titles']):
                print(f"{i+1}. {title}")
        else:
            print("ไม่พบชื่อบทใดๆ")
        print("--------------------")
        save_to_json(scraped_data, OUTPUT_FILE)
        print(f"บันทึกผลลัพธ์ไว้ที่: data/scraped_output.json")
    else:
        print("ไม่สามารถ scrape ข้อมูลได้")


if __name__ == "__main__":
    # แสดงผลภาษาไทยได้ถูกต้องบน Windows Console
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
