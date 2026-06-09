import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


class TestLoginSmoke:

    @pytest.mark.smoke
    def test_login_success(self, page):
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        expect(page.locator("[data-test='title']")).to_have_text(
            "Products"
        )

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "username,password,error_text",
        [
            (
                "invalid_user",
                "invalid_password",
                "Epic sadface: Username and password do not match any user in this service"
            ),
            (
                "",
                "",
                "Epic sadface: Username is required"
            )
        ]
    )
    def test_login_validation(
        self,
        page,
        username,
        password,
        error_text
    ):
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(username, password)

        error = page.locator("[data-test='error']")

        expect(error).to_be_visible()
        expect(error).to_have_text(error_text)