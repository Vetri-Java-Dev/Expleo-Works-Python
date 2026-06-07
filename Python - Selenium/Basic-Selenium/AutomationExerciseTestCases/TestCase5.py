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

try:
    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 10)

    driver.maximize_window();
    driver.get("https://automationexercise.com/")

    assert driver.title == "Automation Exercise", "Home page is not reached."
    
    print("Home page is reached.")

    jsClick(waitForClickable((By.XPATH, "//a[@href = \"/login\"]")))

    assert waitForElement((By.XPATH, "//h2[text() = \"New User Signup!\"]")).is_displayed(), "Sign up message is not available."
    
    print("Sign up text is verified")

    waitForElement((By.XPATH, "//input[@name = \"name\"]")).send_keys("Vetri")
    waitForElement((By.XPATH, "//input[@data-qa = \"signup-email\"]")).send_keys("bvetrivel1@gmail.com7")
    jsClick(waitForClickable((By.XPATH,"//button[@data-qa = \"signup-button\"]")))

    assert waitForElement((By.XPATH, "//p[text() = \"Email Address already exist!\"]")).is_displayed(), "Error message is not displayed."
    
    print("Error message displayed.")
    print("Test case passed.")
    
except Exception as e:
    print(e)

finally:
    driver.quit()