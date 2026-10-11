# agentic-comm-automator/src/utils.py
import datetime
import logging
import os

from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env (อยู่ที่โฟลเดอร์โปรเจกต์) เข้า environment variables
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"))


def setup_logging(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(ch)
        logger.propagate = False
    return logger


_audit_logger = setup_logging("audit")


def get_env_variable(var_name, default=None):
    """อ่าน environment variable ถ้าไม่มีและไม่มีค่า default จะ raise ValueError"""
    value = os.getenv(var_name, default)
    if value is None or value == "":
        raise ValueError(f"Environment variable '{var_name}' not set. Please check your .env file.")
    return value


def ensure_directory_exists(path):
    if path:
        os.makedirs(path, exist_ok=True)


def log_audit_entry(audit_log_list, status, message, task_type="N/A", details=None):
    audit_log_list.append({
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "status": status,
        "task_type": task_type,
        "message": message,
        "details": details if details else {},
    })
    if status in ("ERROR", "CRITICAL"):
        _audit_logger.error(f"AUDIT LOG - {status}: {message} | Task: {task_type}")
    else:
        _audit_logger.info(f"AUDIT LOG - {status}: {message} | Task: {task_type}")
