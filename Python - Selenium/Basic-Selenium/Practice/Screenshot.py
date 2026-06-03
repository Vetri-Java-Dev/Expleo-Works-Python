from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.maximize_window

driver.save_screenshot("googleHome.png")