import logging
import time
import argparse
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import json
import csv
from functools import wraps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_fetching(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        url = args[0]  # Adjusted to get the URL correctly
        start_time = time.time()
        response = await func(self, *args, **kwargs)
        elapsed_time = time.time() - start_time
        logging.info(f"Fetched {url} in {elapsed_time:.2f} seconds")
        return response
    return wrapper

class WebScraper:
    def __init__(self, base_url, target_element, pages, output_format='json'):
        self.base_url = base_url
        self.target_element = target_element
        self.pages = pages
        self.output_format = output_format
        self.scraped_data = []

    @log_fetching
    async def fetch_url(self, session, url):
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

    async def url_generator(self):
        async with aiohttp.ClientSession() as session:
            for url in self.generate_urls():
                yield await self.fetch_url(session, url)

    def parse_html(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return [element.get_text(strip=True) for element in soup.select(self.target_element)]

    def generate_urls(self):
        return [f"{self.base_url}?page={i}" for i in range(1, self.pages + 1)]

    def save_to_file(self):
        if self.output_format == 'json':
            with open('output.json', 'w') as json_file:
                json.dump(self.scraped_data, json_file, indent=4)
        elif self.output_format == 'csv':
            with open('output.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Scraped Data'])
                for item in self.scraped_data:
                    writer.writerow([item])

    async def scrape(self):
        async for content in self.url_generator():
            data = self.parse_html(content)
            self.scraped_data.extend(data)

        self.save_to_file()

def main(base_url, target_element, pages, output_format='json'):
    scraper = WebScraper(base_url, target_element, pages, output_format)
    asyncio.run(scraper.scrape())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web Scraper')
    parser.add_argument('base_url', type=str, help='Base URL of the site to scrape')
    parser.add_argument('target_element', type=str, help='CSS selector for target elements')
    parser.add_argument('pages', type=int, help='Number of pages to scrape')
    parser.add_argument('--output', type=str, default='json', help='Output format (json/csv)')

    args = parser.parse_args()
    
    main(args.base_url, args.target_element, args.pages, args.output)

