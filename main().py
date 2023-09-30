from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('/Users/nitin/Downloads/chromedriver_mac64/chromedriver')
def get_drvier():
    # Set options to make browsing easier
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    options = webdriver.ChromeOptions()
    options.add_argument("disable_infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service,options=options)
    # driver=webdriver.Edge()
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_drvier()
    time.sleep(4)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


print(main())