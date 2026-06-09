from Utilities import ExcelReader, LogCreater
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("userName, password",ExcelReader.getData("ExcelFiles/loginData.xlsx","Sheet1"))
class TestLogin:

    logger=LogCreater.logGenerator()

    def test_login(self, userName, password):

        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.get("https://www.demoblaze.com/")

        self.logger.info("Page loaded")

        wait=WebDriverWait(self.driver, 15)

        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='login2']"))).click()
        self.logger.info("Login button clicked")

        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='loginusername']"))).send_keys(userName)
        self.logger.info("UserName entered")

        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='loginpassword']"))).send_keys(password)
        self.logger.info("Password entered")

        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]"))).click()
        self.logger.info("Page loaded")
    
        assert wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='nameofuser']"))).is_displayed()
        self.logger.info("Successfully completed")







