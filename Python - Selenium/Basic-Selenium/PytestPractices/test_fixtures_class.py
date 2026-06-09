import pytest
import pytest_check as check
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestSearch:

    def test_valid_product(self):
        wait=WebDriverWait(self.driver, 10)

        search=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='search']")))
        search.send_keys("HP")
        search.send_keys(Keys.ENTER)

        result=wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='HP LP3065']")))

        check.is_true(result.is_displayed())

    def test_invalid_product(self):
        wait=WebDriverWait(self.driver, 10)

        search=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='search']")))
        search.clear()
        search.send_keys("Honda")
        search.send_keys(Keys.ENTER)

        msg=wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'no product')]")))

        check.is_true(msg.is_displayed())

    def test_no_product(self):
        wait = WebDriverWait(self.driver, 10)

        search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='search']")))
        search.clear()
        search.send_keys("")
        search.send_keys(Keys.ENTER)

        msg=wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'no product')]")))

        check.is_true(msg.is_displayed())