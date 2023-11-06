from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def save_html(driver, url):
    """
    Save the HTML content of a web page.

    Parameters:
        driver (WebDriver): The WebDriver instance to use for interacting with the web page.
        url (str): The URL of the web page to save.

    Returns:
        None
    """
    driver.get(url)
    time.sleep(2)  # wait for the page to load
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # save the html file or do whatever you need to do
    with open(f"{url.split('/')[-1]}.html", 'w', encoding='utf-8') as file:
        file.write(str(soup))


def get_links(driver):
    """
    Get all the links from a web page using the given Selenium driver.

    Parameters:
        driver (WebDriver): The Selenium driver object used to interact with the web page.

    Returns:
        list: A list of URLs of all the links found on the web page.
    """
    links = driver.find_elements(By.TAG_NAME, 'a')
    link_urls = [link.get_attribute('href') for link in links if link.get_attribute('href')]
    return link_urls


def main():
    """
    Function to crawl a website and save the HTML of each page.

    This function uses Selenium to control a Chrome web browser and crawl a given website. It initializes a Selenium webdriver and accesses the specified website. The function then starts crawling the website by saving the HTML of each page it visits. It also saves all the links found on each page and adds them to the list of pages to crawl. The function continues crawling until there are no more pages to crawl.

    Parameters:
    - None

    Return:
    - None
    """
    chromedriver_path = '/usr/local/bin/chromedriver'

    # Setup Selenium service
    service = Service(chromedriver_path)

    # Initialize Selenium webdriver
    driver = webdriver.Chrome(service=service)

    # Access the website
    url = "https://netexservices.netexlearning.com/support/solutions/"
    driver.get(url)
    time.sleep(5)  # Esperar a que el JavaScript cargue

    pages_to_crawl = {url}
    crawled_pages = set()

    while pages_to_crawl:
        current_url = pages_to_crawl.pop()
        if current_url not in crawled_pages:
            save_html(driver, current_url)
            crawled_pages.add(current_url)

            # Get all the links on the current page
            new_links = get_links(driver)
            pages_to_crawl.update([link for link in new_links if link.startswith(url)])

    # close the driver
    driver.quit()


if __name__ == "__main__":
    main()
