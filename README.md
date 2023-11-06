# Web Crawler with Selenium and BeautifulSoup

This Python script utilizes Selenium and BeautifulSoup to crawl a website, save the HTML content of each page, and collect all page links for further crawling.

## Key Features

- **Dynamic Content Handling**: Seamlessly interacts with web pages that require JavaScript to load, ensuring comprehensive crawling of modern web applications.
- Automated browser interactions using Selenium.
- Extraction and preservation of HTML content.
- Collection of hyperlinks from web pages for recursive crawling.
- Utilization of BeautifulSoup for advanced HTML parsing.
- Smart crawl management to avoid redundancy.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Pipenv (Install it using `pip install pipenv` if not already installed)

## Installation

1. Clone the repository:
git clone <repository-url>
2. Navigate to the cloned project's directory:
cd <project-directory>
3. Use Pipenv to install the dependencies and create a virtual environment:
```bash
pipenv install
```
4. Activate the Pipenv shell:
```bash
pipenv shell
```

## Usage

Run the crawler using the following command within the Pipenv shell:

```bash
python crawler.py
```
