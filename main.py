from google_image_scraper import GoogleImageScraper
import json

with open("config.json") as config_file:
    config = json.load(config_file)

scraper = GoogleImageScraper(config)
scraper.find_image_urls()
