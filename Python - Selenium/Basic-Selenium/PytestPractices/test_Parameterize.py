from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
import time

@pytest.mark.search
@pytest.mark.parametrize("search",[("springboot"),("selenium"),("django")])
def test_search(search):
    driver=webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com/")

    driver.find_element(By.XPATH,"//*[@id='APjFqb']").send_keys(search)


@pytest.mark.parametrize("Browser",["chrome"])
@pytest.mark.parametrize("Url",["https://www.flipkart.com/","https://www.amazon.in/"])
def test_URL(Browser, Url):

    if(Browser=="chrome"):
        # options=ChromeOptions()
        # options.add_argument("--headless=new")
        # driver=webdriver.Chrome(options=options)
        driver=webdriver.Chrome()

    elif(Browser=="firefox"):
        # options=FirefoxOptions()
        # options.add_argument("--headless")
        # driver=webdriver.Firefox(options=options)
        driver=webdriver.Firefox()


    driver.maximize_window()
    
    driver.get(Url)

    time.sleep(5)

    print(driver.title)

    driver.close()
