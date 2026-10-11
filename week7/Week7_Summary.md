# สรุปผลลัพธ์การเรียนรู้ สัปดาห์ที่ 7: Web Scraping (Basic & Advanced)

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (Script Programming)  
**ภาคเรียน:** 1/2569  
**ผู้สอน:** ผู้ช่วยศาสตราจารย์บุญสืบ ไวคำ  
**นักศึกษา:** อัษฎาวุธ เรือนแก้ว (รหัสนักศึกษา 663380303-5)  
**กลุ่มเรียน (Section):** 2

---

## Key Learning Outcomes (ผลลัพธ์การเรียนรู้ประจำสัปดาห์ที่ 7)
- **LO 7.1:** สามารถดาวน์โหลดหน้าเว็บด้วย `requests` และแยกข้อมูลจาก HTML ด้วย `BeautifulSoup4` (`find`, `select`) ได้
- **LO 7.2:** สามารถจัดการข้อผิดพลาดของเครือข่าย (`HTTPError`, `ConnectionError`, `Timeout`) และกำหนด `User-Agent` ได้
- **LO 7.3:** สามารถควบคุมเบราว์เซอร์ด้วย Selenium (headless, implicit/explicit wait, คลิกเปลี่ยนหน้า) เพื่อดึงข้อมูลจากหลายหน้าได้
- **LO 7.4:** สามารถออกแบบ scraper แบบขับเคลื่อนด้วยไฟล์ configuration (agentic approach) พร้อม retry mechanism ได้
- **LO 7.5:** สามารถอธิบายข้อพิจารณาด้านจริยธรรมและกฎหมาย (robots.txt, ToS, rate limiting, ลิขสิทธิ์) ได้

---

## 1. Static Scraping: requests + BeautifulSoup

```python
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 ..."}, timeout=30)
response.raise_for_status()                    # 4xx/5xx -> HTTPError
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("article").find("header").find("h1").get_text(strip=True)
chapters = [a.get_text(strip=True) for a in soup.find("div", class_="content-body").select("ul li a")]
```

| เมธอด | ความหมาย |
|:---|:---|
| `find(tag, class_=...)` | คืนค่า element แรกที่ตรง (หรือ `None` ต้องเช็กก่อนใช้) |
| `find_all()` / `select(css)` | คืนค่าทุก element ที่ตรง |
| `get_text(strip=True)` | ข้อความภายใน element ตัดช่องว่าง |
| `get("href")` | อ่านค่า attribute |

## 2. Dynamic Scraping: Selenium

| หัวข้อ | โค้ด |
|:---|:---|
| เปิดเบราว์เซอร์แบบไม่มีหน้าต่าง | `options.add_argument("--headless=new")` |
| Implicit wait | `driver.implicitly_wait(10)` |
| Explicit wait | `WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, sel)))` |
| หา element | `driver.find_elements(By.CSS_SELECTOR, "article.product_pod")` |
| คลิกหน้าถัดไป | `driver.execute_script("arguments[0].scrollIntoView(true);", btn); btn.click()` |

## 3. Agentic Design
ไฟล์ `configs/example_site_config.json` กำหนด `start_url`, `max_pages`, `delay_between_pages`, `max_retries`
และ CSS selector ของแต่ละฟิลด์ — เปลี่ยนเว็บเป้าหมายได้โดยไม่แก้โค้ด ข้อมูลถูกเก็บเป็น `dataclass Product` แล้วบันทึก JSON

## 4. จริยธรรม
ตรวจ `robots.txt` และ ToS, หน่วงเวลาระหว่าง request, ไม่เก็บข้อมูลส่วนบุคคล, ใช้ API แทนถ้ามี (รายละเอียดใน `LabX Advance/week7-agentic-web-scraper/docs/ETHICS.md`)

---

## ไฟล์ปฏิบัติการ
| งาน | โฟลเดอร์ | ผลลัพธ์ |
|:---|:---|:---|
| LabX BASIC 1: Introduction to Web Scraping | [web-scraping-intro](../LabX%20Basic/week7-web-scraping-intro) | ชื่อหนังสือ + 27 บทจาก automatetheboringstuff.com |
| LabX ADV 1: Advanced Web Scraping & Automated Agents | [agentic-web-scraper](../LabX%20Advance/week7-agentic-web-scraper) | 40 รายการหนังสือจาก 2 หน้า → `data/scraped_products.json` |
