from selenium.webdriver.common.by import By

class LoginPage:
    
    emailField=(By.XPATH,"//input[@id='input-email']")
    passwordField=(By.XPATH,"//input[@id='input-password']")
    login=(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input")