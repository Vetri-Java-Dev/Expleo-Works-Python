import pytest
from selenium import webdriver
import ConfigReader

@pytest.fixture(params=["Chrome"])
def driver(request):

    browser=request.param

    if browser == "Chrome":
        driver = webdriver.Chrome()

    elif browser == "Edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
    driver.get(ConfigReader.getData("Basic info", "url"))

    yield driver

    driver.quit()