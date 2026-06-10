from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SearchPage:
    
    result=(By.XPATH,"//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a")
