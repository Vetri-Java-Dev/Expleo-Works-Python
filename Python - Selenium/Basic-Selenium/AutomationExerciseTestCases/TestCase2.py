from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com")
time.sleep(3)

driver.find_element(By.XPATH,"//a[contains(text(),'Signup / Login')]").click()
time.sleep(3)

loginText=driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
assert loginText.is_displayed()

driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("bvetivel1@gmail.com1")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Vetri@1234")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
time.sleep(5)

loggedInText=driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
assert loggedInText.is_displayed()

print("Test Case 2 Passed succesfully")

driver.quit()