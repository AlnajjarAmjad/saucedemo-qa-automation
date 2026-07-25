from playwright.sync_api import Page, expect
from pages.inventory_pages import InventoryPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout_flow(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.go_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_order()
    
    expect(checkout_page.confirmation_message).to_have_text("Thank you for your order!")

def test_checkout_missing_first_name(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.go_to_cart()
    checkout_page.start_checkout()
    
    # Αφήνουμε το first name κενό
    checkout_page.last_name_input.fill("Doe")
    checkout_page.zip_input.fill("12345")
    checkout_page.continue_button.click()
    
    error_message = logged_in_page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("First Name is required")    