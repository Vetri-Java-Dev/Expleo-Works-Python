import pytest
from Actions.LoginActions import LoginActions
from Actions.SearchActions import SearchActions
from Utilities.excel_reader import get_data
from Utilities.logger import get_logger

@pytest.mark.usefixtures("setup")
class TestSearch:

    def test_valid_search(self):

        logger=get_logger()

        searchAction=SearchActions(self.driver)

        searchAction.search("HP")
        assert searchAction.isProductDisplayed("HP")

        print("Test successfull")
