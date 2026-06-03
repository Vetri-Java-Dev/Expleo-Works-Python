from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.maximize_window

print(driver.title)

time.sleep(3)

driver.quit()