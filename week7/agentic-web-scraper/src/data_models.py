# agentic-web-scraper/src/data_models.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    """โครงสร้างข้อมูลสินค้า 1 รายการที่ scrape ได้"""
    name: str
    price: str
    description: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
