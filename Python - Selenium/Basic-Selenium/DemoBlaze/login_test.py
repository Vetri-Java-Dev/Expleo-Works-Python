import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_valid_login(self):

        wait=WebDriverWait(self.driver,15)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='login2']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='loginusername']"))).send_keys(ConfigReader.getData("TestData","username"))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='loginpassword']"))).send_keys(ConfigReader.getData("TestData","password"))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]"))).click()
    
        assert wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='nameofuser']"))).is_displayed()