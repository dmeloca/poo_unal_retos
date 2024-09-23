# Web Scraper

This web scraper fetches content from a specified website and extracts data based on a given CSS selector. It supports pagination and outputs the scraped data in JSON or CSV format.

## Features

- Asynchronous fetching for improved performance
- CSS selector-based data extraction using BeautifulSoup
- Support for pagination
- Output in JSON or CSV format
- Command-line interface for easy usage

## Requirements

- Python 3.7 or higher
- `requests` library
- `beautifulsoup4` library
- `aiohttp` library

## Installation

Install the required libraries using pip:

```bash
pip install -r requirements.txt
``` 
## Usage
To run the scraper, use the following command:
```bash
python web_scraper.py <base_url> <target_element> <pages> [--output <output_format>]
```

## Parameters
- `<base_url>`: The base URL of the website to scrape.
- `<target_element>`: The CSS selector for the elements you want to extract (e.g., h1, p, .classname).
- `<pages>`: The number of pages to scrape (assuming pagination).
- --output `<output_format>: Optional parameter to specify the output format (json or csv). Default is json.
## Example
To scrape the first 5 pages of a website for h1 elements and save the results in CSV format:

```bash
python web_scraper.py "https://archlinux.org" "p" 5 --output "json"
```
