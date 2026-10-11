# agentic-spreadsheet-processor/main.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Add the 'src' directory to the Python path
sys.path.append(os.path.join(BASE_DIR, 'src'))

from config_parser import ConfigParser
from spreadsheet_agent import SpreadsheetAgent
from utils import setup_logging

logger = setup_logging("main")


def main():
    """
    Main entry point for the Agentic Spreadsheet Processor.
    Loads config and runs the agent.
    """
    # paths ใน config เป็น relative กับโฟลเดอร์โปรเจกต์
    os.chdir(BASE_DIR)
    config_file_path = os.path.join('configs', 'example_spreadsheet_config.json')

    try:
        os.makedirs('data', exist_ok=True)
        logger.info(f"Loading configuration from: {config_file_path}")
        config = ConfigParser(config_file_path).load_config()

        input_file_path = config.get("input_file")
        if not os.path.exists(input_file_path):
            logger.critical(f"Input Excel file not found: '{input_file_path}'. "
                            "Run 'python create_dummy_data.py' first.")
            return

        logger.info("Initializing Spreadsheet Agent...")
        agent = SpreadsheetAgent(config)

        logger.info("Running Spreadsheet Agent...")
        if agent.run():
            logger.info("All tasks completed successfully.")
        else:
            logger.warning("Agent finished with errors. See the 'Audit Log' sheet for details.")

    except FileNotFoundError as e:
        logger.critical(f"File system error: {e}")
    except ValueError as e:
        logger.critical(f"Configuration error: {e}")
        logger.info("Please check the format and required fields in your config file.")
    except Exception as e:
        logger.critical(f"An unexpected critical error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
