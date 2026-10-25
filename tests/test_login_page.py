from pages.login_page import LoginPage
from config.config import TestData
import pytest
from tests.basetest import BaseTest



class TestLogin(BaseTest):

    @pytest.mark.sanity
    @pytest.mark.order(1)
    def test_login_Page_username(self):
        print("verifying username field")
        login_page = LoginPage(self.driver)
        # self.driver.get(TestData.BASE_URL)
        login_page.verify_login_page_usernam()


    @pytest.mark.sanity
    @pytest.mark.order(2)
    def test_login_Page_password(self):
        print("verifying password field")
        login_page = LoginPage(self.driver)
        login_page.verify_login_page_password()
    
    @pytest.mark.sanity
    @pytest.mark.order(3)
    @pytest.mark.regression
    def test_login_Page_button(self):
        print("verifying login button")
        login_page = LoginPage(self.driver)
        login_page.verify_login_button_visibility()

    @pytest.mark.funcational
    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_validate_login_functionality(self):
        print("Logging on to the application")
        login_page = LoginPage(self.driver)
        login_page.login_to_application()
        print("verifying the navigated url after logging in")
        login_page.verify_the_application_url_after_logging()


