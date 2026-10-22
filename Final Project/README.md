# Final Project — WeatherAQI Sense

> งาน Final Project ถูกเก็บไว้ใน repository แยก จึงทำเป็นไฟล์ลิงก์ตามที่ข้อกำหนดอนุญาต

**Repository:** https://github.com/Orimsaa/Ui_weather

## รายละเอียด

เว็บแดชบอร์ดติดตามสภาพอากาศและคุณภาพอากาศของประเทศไทยแบบเรียลไทม์ พร้อมแผนที่ GIS ครบ 77 จังหวัด และเรดาร์ฝน Doppler แบบสด

- **แผนที่ GIS 77 จังหวัด** — ขอบเขตจังหวัดอย่างเป็นทางการ, หมุดจังหวัดคำนวณจุดศูนย์กลางเรขาคณิต (Green's theorem), mask ประเทศเพื่อนบ้าน, hover/click เชื่อมกันระหว่างแผนที่และหมุด
- **Live Doppler Rain Radar** — ข้อมูลจาก RainViewer API พร้อม Play/Pause ย้อนหลัง 2 ชั่วโมง, timeline scrubber และสเกลความแรงของฝน
- **ข้อมูลสภาพอากาศและคุณภาพอากาศ** — อุณหภูมิ, ความชื้น, ลม, UV, จุดน้ำค้าง, US AQI พร้อม PM2.5 / PM10 / O3 / NO2 / SO2 / CO, พยากรณ์รายชั่วโมง 24 ชม. และ 7 วัน
- **ดัชนีไลฟ์สไตล์** — แนะนำการวิ่ง ตากผ้า ล้างรถ และทาครีมกันแดด
- **รองรับสองภาษา (ไทย/อังกฤษ)** และแสดงผลได้ทุกขนาดหน้าจอ

## Tech Stack

| ส่วน | เทคโนโลยี |
|:---|:---|
| Framework | Next.js 16 (App Router + Turbopack), React 19, TypeScript |
| Styling | Tailwind CSS, Lucide React Icons |
| GIS / Mapping | Leaflet.js, GeoJSON (77 จังหวัด + ขอบเขตประเทศไทย), Esri / OpenStreetMap tiles |
| APIs | OpenWeatherMap, IQAir AirVisual, RainViewer |

## วิธีรัน

```bash
git clone https://github.com/Orimsaa/Ui_weather.git
cd Ui_weather
pnpm install   # หรือ npm install
pnpm dev       # หรือ npm run dev
```
