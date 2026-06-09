import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def setUp(function):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(12)
    driver.get("https://tutorialsninja.com/demo/")

def teardown(function):
    driver.quit


def test_validProduct():
    driver.find_element(By.NAME,value="search").send_keys("Hp")
    driver.find_element(By.XPATH,"//*[@id='search']/span/button").click()

    assert driver.find_element(By.XPATH,value="//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a").is_displayed()

