from playwright.sync_api import Page, expect
from pages.inventory_pages import InventoryPage

def test_add_item_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

def test_add_multiple_items_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.add_item_to_cart("sauce-labs-bike-light")
    expect(inventory_page.cart_badge).to_have_text("2")

def test_remove_item_from_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")
    inventory_page.remove_item_from_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_be_hidden()