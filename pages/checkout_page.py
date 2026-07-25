from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.zip_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.confirmation_message = page.locator(".complete-header")

    def go_to_cart(self):
        self.cart_icon.click()

    def start_checkout(self):
        self.checkout_button.click()

    def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_input.fill(zip_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()