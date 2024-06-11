from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

def get_stock_listings(url):
    # Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(r'C:\SIMPLY_Official\2024\DRF\drfcore\home\mylibs\EdgeDriver\msedgedriver.exe')
    print(webdriver_service)

    # Choose Chrome Browser
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    driver.get(url)

    time.sleep(5)  # wait for the page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the table with the stock listings
    table = soup.find('table')
    if table is None:
        print("No table found in the webpage.")
        return None

    # Get the table headers
    headers = [header.text for header in table.find_all('th')]

    # Get the table rows
    rows = table.find_all('tr')

    # Get the data from each row
    data = []
    for row in rows[1:]:  # Skip the first row (headers)
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(dict(zip(headers, cols)))

    driver.quit()

    return data

url = "https://www.nseindia.com/market-data/new-stock-exchange-listings-recent"
data = get_stock_listings(url)
if data is not None:
    print(data)
