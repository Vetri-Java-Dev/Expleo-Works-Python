from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitForElement(locator):
    return wait.until(EC.visibility_of_element_located(locator))

def waitForClickable(locator):
    return wait.until(EC.element_to_be_clickable(locator))

def jsClick(element):
    driver.execute_script("arguments[0].click();",element)


driver=webdriver.Chrome()

driver.get("https://letcode.in/frame")
driver.switch_to.frame(0)

wait=WebDriverWait(driver,15)

firstName=waitForElement((By.XPATH,"//input[@name='fname']"))
lastName=waitForElement((By.XPATH,"//input[@name='lname']"))

driver.switch_to.frame("//iframe")

email=waitForElement((By.XPATH,"//input[@name='email']"))

firstName.send_keys("Vetri")
lastName.send_keys("b")
email.send_keys("vetri@gmail.com")

