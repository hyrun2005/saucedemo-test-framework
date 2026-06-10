import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    @pytest.mark.smoke
    def test_page_visibility(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        assert inventory_page.is_loaded()

    @pytest.mark.smoke
    def test_product_amount(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        amount = inventory_page.get_amount_of_products()
        assert amount > 0

    @pytest.mark.smoke
    def test_sort_low_to_high(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        inventory_page.sort_low_to_high()
        prices = inventory_page.get_product_prices()
        assert prices == sorted(prices)
