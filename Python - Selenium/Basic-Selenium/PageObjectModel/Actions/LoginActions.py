from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Actions.BaseActions import BaseActions

class LoginActions(BaseActions):

    def __init__(self,driver):
        super().__init__(driver)

    def login(self,email, password):

        self.click(HomePage.dropDown)
        self.click(HomePage.login)

        self.sendKeys(LoginPage.emailField, email)
        self.sendKeys(LoginPage.passwordField, password)

    
    def isLoggedIn(self):
        return "account" in self.driver.current_url
    

        
        