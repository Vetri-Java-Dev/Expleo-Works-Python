from selenium.webdriver.common.by import By

class HomePage:

    #Login Locators
    dropDown=(By.XPATH,"//*[@id='top-links']/ul/li[2]/a")
    login=(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[2]/a")
    register=(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[1]/a")

    #Search Locators
    searchField=(By.XPATH,"//*[@id='search']/input")
    searchEnter=(By.XPATH,"//*[@id='search']/span/button")