from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.maximize_window

searchField=driver.find_element(By.XPATH,value="//*[@id='APjFqb']")

if(searchField.is_enabled):
    searchField.send_keys("Python Selenium")
    searchField.submit()

time.sleep(5)