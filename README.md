# Quotes Scraper

This project is a simple web scraper written in Python that extracts quotes and their authors from [Quotes to Scrape](https://quotes.toscrape.com/) and saves the data into a CSV file.

## Features

- **Web Scraping**: Uses `requests` to fetch the webpage content and `BeautifulSoup` to parse the HTML.
- **Data Extraction**: Extracts quotes and their corresponding authors.
- **CSV Export**: Saves the extracted data into a CSV file for easy access and analysis.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/quotes-scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd quotes-scraper
    ```
3. Install the required libraries:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

Run the script to scrape quotes and authors from the website and save them to a CSV file:
```bash
python scrape_quotes.py
