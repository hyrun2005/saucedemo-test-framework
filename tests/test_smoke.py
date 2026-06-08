import pytest

from pages.login_page import LoginPage


class TestLoginSmoke:
    @pytest.mark.smoke
    def test_login_success(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        assert page.url == "https://www.saucedemo.com/inventory.html"
