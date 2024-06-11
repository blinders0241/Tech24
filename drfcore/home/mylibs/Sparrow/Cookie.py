from selenium import webdriver
import json
url = "https://www.nseindia.com"
# Create a new instance of the Firefox driver
# Save the cookies to a file
class Cookie:
    def __init__(self):
        pass
    def get_cookies(self):
        driver = webdriver.Firefox()

        # Send a GET request to the website to receive cookies
        driver.get(url)
        try:
            cookies = driver.get_cookies()
            cookie_dict = {}
            with open("cookies.txt", 'w') as fp:
                for cokie in cookies:
                    cookie_dict[cokie['name']] = cokie['value']
                fp.write(json.dumps(cookie_dict))
            driver.quit()
            return cookie_dict
        except Exception as e:
            message = f"Error saving cookies: {e}"
            path = None
            return None

# Cookie().get_cookies()