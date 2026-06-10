import pytest
from Actions.LoginActions import LoginActions
from Utilities.excel_reader import get_data
from Utilities.logger import get_logger

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("email,password",get_data("login_data.xlsx", "ValidLoginData"))
    def test_valid_login(self,email,password):

        logger=get_logger()

        loginActions=LoginActions(self.driver)
        logger.info("Test starts")
        loginActions.login(email,password)
        logger.info(f"{email} and {password} is entered")

        assert loginActions.isLoggedIn()
        logger.info("Test case completed")
