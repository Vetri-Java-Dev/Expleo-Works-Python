from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseActions:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(self.find(locator))).click()

    def jsClick(self,locator):
        self.driver.execute_script("arguments[0].click();",self.find(locator))

    def sendKeys(self, locator, text):
        self.find(locator).send_keys(text)

    