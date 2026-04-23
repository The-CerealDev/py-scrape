# Python Scraper for automation of manual data collection tasks

## Overview

This project is a web scraping tool designed to automate the collection of financial data from the London Stock Exchange (LSE). It uses Selenium to navigate the website, extract relevant information from market news articles, and store the data in a structured format.

## Features

- **Multi-threaded Scraping**: Uses `multiprocessing` to run link discovery and data scraping concurrently for better performance.
- **Shadow DOM Support**: Utilizes `pyshadow` to extract data from web pages that use Shadow DOM.
- **Configurable**: Easily switch between different companies and date ranges via `config.py`.
- **Error Handling**: Includes retry logic for failed scrapes and logs skipped links.
- **Data Validation**: Checks if the discloser matches the target company and validates security data.

## Prerequisites

- Python 3.6+
- Required libraries: `selenium`, `webdriver-manager`, `pandas`, `pyshadow`

Install dependencies:
```bash
pip install selenium webdriver-manager pandas pyshadow
```

## Configuration

Edit `config/config.py` to set the target company and date range:

```python
COMPANY = "Blackrock"
START_DATE = '20250101'
END_DATE = '20260101'
```

The script will automatically generate the following files:
- `{COMPANY}-links.txt`: List of URLs to scrape.
- `{COMPANY}-scraped.csv`: Extracted data.
- `{COMPANY}-skipped.txt`: Links that failed to scrape.
- `{COMPANY}-links-cleaned.txt`: De-duplicated link list.

## Usage

1. **Run the scraper**:
   ```bash
   python link_flow.py
   ```

2. **Remove duplicate links** (before running the scraper):
   ```bash
   python dupli-remove.py
   ```

## File Structure

```
py-scrape/
├── config/
│   └── config.py
├── link_flow.py
├── link_analyser.py
├── linkscrape_v2.py
├── pyscrape.py
├── dupli-remove.py
├── Blackrock-links.txt
├── Blackrock-scraped.csv
├── Blackrock-skipped.txt
└── README.md
```

## License

MIT
