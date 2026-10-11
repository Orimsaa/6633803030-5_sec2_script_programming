# email-sms-automator/src/utils.py
import logging
import os

from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env ในโฟลเดอร์โปรเจกต์ (ไฟล์นี้อยู่ใน .gitignore ห้าม commit)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"))


def setup_logging(name, level=logging.INFO):
    """สร้าง logger ที่ไม่เพิ่ม handler ซ้ำเมื่อถูกเรียกหลายครั้ง"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        logger.propagate = False
    return logger


def get_env_variable(var_name):
    """อ่าน environment variable; ถ้าไม่มีให้ raise ValueError พร้อมข้อความที่เข้าใจง่าย"""
    value = os.getenv(var_name)
    if value is None or value.strip() == "":
        raise ValueError(f"Environment variable '{var_name}' not set")
    return value.strip()


def ensure_directory_exists(path):
    os.makedirs(path, exist_ok=True)
