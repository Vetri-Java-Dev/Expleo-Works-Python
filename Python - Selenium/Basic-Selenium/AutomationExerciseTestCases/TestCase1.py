from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/")

header=driver.find_element(By.XPATH, "//*[@id='header']/div/div/div")

if(header.is_displayed()):
    print("Home displayed")
else:
    print("Home not displayed")

time.sleep(2)

signupButton=driver.find_element(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
signupButton.click()

time.sleep(2)

name=driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[2]")

email=driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[3]")

if(name.is_enabled()):
    name.send_keys("Vetri")
    email.send_keys("bvetrivel1@gmail.com6")

driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/button").click()

password=driver.find_element(By.XPATH,value="//*[@id='password']")

firstName=driver.find_element(By.XPATH,value="//*[@id='first_name']")
lastName=driver.find_element(By.XPATH,value="//*[@id='last_name']")

state=driver.find_element(By.XPATH,value="//*[@id='state']")
city=driver.find_element(By.XPATH,value="//*[@id='city']")
zipCode=driver.find_element(By.XPATH,value="//*[@id='zipcode']")
phone=driver.find_element(By.XPATH,value="//*[@id='mobile_number']")
address=driver.find_element(By.XPATH,value="//*[@id='address1']")

firstName.send_keys("Vetri")
lastName.send_keys("B")
password.send_keys("Vetri@1234")
state.send_keys("TamilNadu")
city.send_keys("Ammapet")
address.send_keys("Jothi school frontSide")
zipCode.send_keys("636003")
phone.send_keys("9677558855")

driver.find_element(By.XPATH,value="//*[@id='form']/div/div/div/div[1]/form/button").click()

time.sleep(5)

if(driver.find_element(By.XPATH, "//b[text() = \"Account Created!\"]").is_displayed()):
    print("Account created.")
else:
    print("Account didnt created.")

driver.find_element(By.XPATH,value="//*[@id='form']/div/div/div/div/a").click()

time.sleep(3)
driver.find_element(By.XPATH,value="//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a").click()

time.sleep(3)
if(driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2").is_displayed()):
    print("Account Deleted.")
else:
    print("Account didnt Deleted.")


