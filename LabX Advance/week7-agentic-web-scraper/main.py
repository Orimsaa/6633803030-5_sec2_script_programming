# agentic-web-scraper/main.py
import os
import sys

from src.config_parser import ConfigParser
from src.scraper_agent import ScraperAgent
from src.utils import save_data_to_json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    config_path = os.path.join(BASE_DIR, "configs", "example_site_config.json")
    output_path = os.path.join(BASE_DIR, "data", "scraped_products.json")

    # 1. Load and parse config
    parser = ConfigParser(config_path)
    config = parser.load_config()

    # 2. Initialize and run scraper agent
    # ปรับ headless=False หากต้องการเปิดเบราว์เซอร์ดูการทำงานจริง
    agent = ScraperAgent(config=config, browser="chrome", headless=True)
    results = agent.run()

    # 3. Save results
    save_data_to_json(results, output_path)
    print(f"Successfully scraped {len(results)} items and saved to {os.path.relpath(output_path, BASE_DIR)}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
