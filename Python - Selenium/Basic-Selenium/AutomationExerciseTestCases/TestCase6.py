from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def waitForElement(locator):
    return wait.until(EC.visibility_of_element_located(locator))

def waitForClickable(locator):
    return wait.until(EC.element_to_be_clickable(locator))

def jsClick(element):
    driver.execute_script("arguments[0].click();",element)

try:
    driver=webdriver.Chrome();
    wait=WebDriverWait(driver, 10)
    
    driver.maximize_window();
    driver.get("https://automationexercise.com/")

    assert driver.title=="Automation Exercise", "Home page title mismatch"
    print("Home page is reached.")

    contactUs=waitForElement((By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[8]/a"))
    jsClick(contactUs)

    print("Debug")

    assert waitForElement((By.XPATH,"//*[@id='contact-page']/div[2]/div[1]/div/h2")).text == "GET IN TOUCH"
    print("Redirected to Get in touch page")

    name=waitForElement((By.XPATH,"//*[@id='contact-us-form']/div[1]/input"))
    email=waitForElement((By.XPATH,"//*[@id='contact-us-form']/div[2]/input"))
    subject=waitForElement((By.XPATH,"//*[@id='contact-us-form']/div[3]/input"))
    message=waitForElement((By.XPATH,"//*[@id='message']"))

    name.send_keys("Vetri")
    email.send_keys("vetri@gmail.com")
    subject.send_keys("Automation test cases")
    message.send_keys("Automation test case 6 completed")

    submitBtn=waitForClickable((By.NAME, "submit"))
    submitBtn.click()

    alert=Alert(driver=driver)

    assert alert.text=="Press OK to proceed!"
    alert.accept()

    print("Test case completed")



except Exception as e:
    print(e)