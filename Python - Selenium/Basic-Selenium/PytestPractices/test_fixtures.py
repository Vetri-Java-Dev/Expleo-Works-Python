from selenium.webdriver.common.by import By
import time

def test_ValidProductSearch(test_setup_teardown):

    driver=test_setup_teardown

    time.sleep(4)

    searchField = driver.find_element(By.XPATH, "//*[@id='search']/input")
    searchField.send_keys("mac")

    driver.find_element(By.XPATH, "//*[@id='search']/span/button").click()

    assert driver.find_element(By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a").text == "iMac"