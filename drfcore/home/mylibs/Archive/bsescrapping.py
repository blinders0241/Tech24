from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the BSE website
html = driver.get("https://www.bseindia.com/stock-share-price/zee-entertainment-enterprises-ltd/zeel/505537/shareholding-pattern/")
print(html)
soup = BeautifulSoup(html, 'html.parser')

# Find the table element by its class name
table = soup.find('table', {'class': 'ng-scope'})

# Extract the table rows
rows = table.find_all('tr')

# Print the table rows
for row in rows:
    print(row.text)
# try:
#     # Find the table element by its class name
#     tables = driver.find_elements(by=By.CLASS_NAME, value="largetable")
#     print(tables)
#     if len(tables) > 0:
#         table = tables[0]
#         # Extract the table rows
#         rows = table.find_elements(by=By.TAG_NAME, value="tr")

#         # Print the table rows
#         for row in rows:
#             print(row.text)
#     else:
#         print("Error: Table not found")

# except NoSuchElementException as e:
#     print("Error: ", e)

# finally:
#     # Close the browser window
#     driver.quit()
