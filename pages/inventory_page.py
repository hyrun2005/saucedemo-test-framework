class InventoryPage:
    _product_sort = "select[data-test='product-sort-container']"
    _inventory_item = "div[data-test='inventory-item']"
    _add_to_cart_button = "button[data-test='add-to-cart-sauce-labs-backpack']"
    _product_price = "div[data-test='inventory_item_price']"

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.locator(".inventory_list").is_visible()

    def add_to_cart(self):
        self.page.locator(self._add_to_cart_button).click()

    def sort_low_to_high(self):
        self.page.locator(self._product_sort).select_option("lohi")

    def sort_high_to_low(self):
        self.page.locator(self._product_sort).select_option("hilo")

    def sort_a_to_z(self):
        self.page.locator(self._product_sort).select_option("az")

    def sort_z_to_a(self):
        self.page.locator(self._product_sort).select_option("za")

    def get_amount_of_products(self):
        return self.page.locator(self._inventory_item).count()

    def get_product_prices(self):
        product_price_list = self.page.locator(self._product_price).all_text_contents()
        return [float(price.replace("$", "")) for price in product_price_list]