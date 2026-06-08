from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def waitForElement(locator):
    return wait.until(EC.visibility_of_element_located(locator))

def waitForElements(locator):
    return wait.until(EC.presence_of_all_elements_located(locator))

def waitForClickable(locator):
    return wait.until(EC.element_to_be_clickable(locator))

def jsClick(element):
    driver.execute_script("arguments[0].click();",element)

def moveToElement(element):
    action=ActionChains(driver)
    action.move_to_element(element).perform()

def moveToElementAndClick(element):
    action=ActionChains(driver)
    action.move_to_element(element).click().perform()

def click(element):
    action=ActionChains(driver)
    action.click(element).perform()

driver=webdriver.Chrome()
driver.maximize_window()

wait=WebDriverWait(driver, 15)

driver.set_page_load_timeout(180)
driver.implicitly_wait(10)

driver.get("https://automationexercise.com/")

header=waitForElement((By.XPATH, "//*[@id='header']"))

if (header.is_displayed()):
    print("Home displayed")
else:
    print("Home not displayed")


products=waitForClickable((By.XPATH,"//a[contains(text(),'Products')]"))
click(products)

assert waitForElement((By.XPATH,"//h2[contains(text(),'All Products')]")).is_displayed()

elements=driver.find_elements(By.XPATH,"//*[@class='productinfo text-center']")

for i in range(2):

    addToCart = elements[i].find_element(By.XPATH,".//a[contains(@class,'add-to-cart')]")

    jsClick(addToCart)
    continueShopping=waitForClickable((By.XPATH,"//*[@id='cartModal']//button"))
    jsClick(continueShopping)

moveToElementAndClick(waitForElement((By.LINK_TEXT,"Cart")))

cartElements=waitForElements((By.XPATH,"//*[contains(@id,'product-')]"))

assert len(cartElements)==2
print("Products added to cart succesfully")
print("Test case successfully executed")

driver.quit()