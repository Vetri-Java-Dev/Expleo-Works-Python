import pytest
import pytest_check as check
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("driver")
class TestSearch :
    def test_valid_product(self):
        self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys("HP")
        self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)

        check.is_true(self.soft_assert(self.assertTrue, self.driver.find_element(By.XPATH, "//a[text() = \"HP LP3065\"]").is_displayed()))

    def test_invalid_product(self):
        self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
        
        check.is_true(self.assertTrue, self.driver.find_element(By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]").is_displayed())

    def test_no_product(self):
        self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
        
        check.is_true(self.assertTrue, self.driver.find_element(By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]").is_displayed())