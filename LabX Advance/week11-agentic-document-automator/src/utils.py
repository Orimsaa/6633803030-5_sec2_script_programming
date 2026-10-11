# agentic-document-automator/src/utils.py
import datetime
import logging
import os


def setup_logging(name, level=logging.INFO, filename=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        if filename:
            fh = logging.FileHandler(filename, encoding="utf-8")
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        logger.propagate = False
    return logger


_logger = setup_logging("audit")


def ensure_directory_exists(path):
    if path:
        os.makedirs(path, exist_ok=True)


def log_audit_entry(audit_log_list, status, message, task_type="N/A", details=None):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "status": status,
        "task_type": task_type,
        "message": message,
        "details": details if details else {}
    }
    audit_log_list.append(log_entry)
    if status in ["ERROR", "CRITICAL"]:
        _logger.error(f"AUDIT LOG - {status}: {message} | Task: {task_type}")
    else:
        _logger.info(f"AUDIT LOG - {status}: {message} | Task: {task_type}")
