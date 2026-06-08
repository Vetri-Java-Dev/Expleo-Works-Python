from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome()
driver.maximize_window()

wait=WebDriverWait(driver,15)

driver.get("https://www.leafground.com/alert.xhtml;jsessionid=node010o81fl6edrzl1u72619roi7lx17897398.node0")

simpleAlertInvokeButton=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='j_idt88:j_idt93']")))
simpleAlertInvokeButton.click()

alert=Alert(driver=driver)

print("Alert text : ",alert.text)

alert.accept()
print("Alert accepted")