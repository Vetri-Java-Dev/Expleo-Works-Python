import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup_teardown(request):

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(180)

    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver

    yield

    driver.quit()