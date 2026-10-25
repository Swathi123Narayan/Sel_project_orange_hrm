import pytest
from pages.admin_page import AdminPage
from tests.basetest import BaseTest


class TestAdmin(BaseTest):

    @pytest.mark.sanity
    @pytest.mark.order(5)
    def test_admin_page_navigation_for_smoke(self,logged_in_user):
        admin_page = AdminPage(self.driver)
        admin_page.navigate_to_admin_section()

    @pytest.mark.funcational
    @pytest.mark.order(6)
    @pytest.mark.regression
    def test_admin_page_navigation_for_regression(self,logged_in_user):
        admin_page = AdminPage(self.driver)
        admin_page.navigate_to_admin_section()

    @pytest.mark.parametrize("req, res",[("hi","hello"),("how are you?","Fine!")])
    @pytest.mark.order(7)
    @pytest.mark.sanity
    def test_with_multiple_values(self, req,res):
        print(req, res)
