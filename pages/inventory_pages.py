from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item_to_cart(self, item_id: str):
        self.page.locator(f"#add-to-cart-{item_id}").click()

    def remove_item_from_cart(self, item_id: str):
        self.page.locator(f"#remove-{item_id}").click()