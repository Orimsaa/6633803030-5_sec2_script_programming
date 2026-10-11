# agentic-comm-automator/main.py
import argparse
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'src'))

from communication_agent import CommunicationAgent
from config_parser import ConfigParser
from utils import ensure_directory_exists, setup_logging

logger = setup_logging("main")


def check_attachments(config):
    """แจ้งเตือนไฟล์แนบที่ไม่มีอยู่จริง (agent จะข้ามไฟล์นั้นแต่ยังส่งอีเมลได้)"""
    missing = []
    for task in config["tasks"]:
        for path in task.get("parameters", {}).get("attachments", []):
            if "{" not in path and not os.path.exists(os.path.join(BASE_DIR, path)):
                missing.append(path)
    for path in missing:
        logger.warning(f"Attachment not found: {path} (run 'python create_sample_attachments.py')")
    return missing


def main():
    parser = argparse.ArgumentParser(description="Agentic Communication Workflow (Email & SMS)")
    parser.add_argument("--dry-run", action="store_true",
                        help="do not connect to Gmail; save emails as .eml files in outbox/ and mock_inbox/")
    args = parser.parse_args()
    dry_run = args.dry_run or os.getenv("DRY_RUN", "false").lower() == "true"

    config_file_path = os.path.join(BASE_DIR, 'configs', 'comm_pipeline_config.json')
    try:
        ensure_directory_exists(os.path.join(BASE_DIR, 'data', 'reports'))
        ensure_directory_exists(os.path.join(BASE_DIR, 'data', 'incoming_attachments'))
        logger.info(f"Loading configuration from: {os.path.relpath(config_file_path, BASE_DIR)}")
        config = ConfigParser(config_file_path).load_config()
        check_attachments(config)

        logger.info(f"Initializing Communication Agent (mode: {'DRY-RUN' if dry_run else 'LIVE'})...")
        agent = CommunicationAgent(config, BASE_DIR, dry_run=dry_run)

        logger.info("Running Communication Agent workflow...")
        if agent.run():
            logger.info("Communication automation process completed successfully.")
        else:
            logger.warning("Communication automation finished with errors. See the audit report.")
    except ValueError as e:
        logger.critical(f"{e}")
        logger.info("Copy .env.example to .env and fill in your Gmail address + App Password, "
                    "or run 'python main.py --dry-run' to test without sending.")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"An unexpected critical error occurred: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
