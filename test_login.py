from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_failed_login_wrong_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wrong_user", "wrong_password")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match")

def test_login_with_empty_fields(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login_button.click()
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username is required")