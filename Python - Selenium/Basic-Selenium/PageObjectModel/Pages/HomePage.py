from selenium.webdriver.common.by import By

class HomePage:
    
    dropDown=(By.XPATH,"//*[@id='top-links']/ul/li[2]/a")
    login=(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[2]/a")
    register=(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[1]/a")