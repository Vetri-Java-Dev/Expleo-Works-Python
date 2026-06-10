from Actions.BaseActions import BaseActions
from Pages.HomePage import HomePage

class SearchActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, key):
        self.sendKeys(HomePage.searchField,key)
        self.click(HomePage.searchEnter)
    
    def isProductDisplayed(self):
        
    
    