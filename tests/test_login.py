from pages.login_page import LoginPage
from utils.test_data import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    """
    Test successful login with valid credentials.
    """
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    # Assert successful navigation to the products page by checking URL and an element
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    login_page.is_products_page_visible()
    print("\nValid login test PASSED.")


def test_invalid_login(page: Page):
    """
    Test unsuccessful login with invalid credentials.
    """
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    
    # Assert that the error message is displayed
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    expect(login_page.error_message).to_be_visible()
    assert login_page.get_error_message() == expected_error_message
    print("\nInvalid login test PASSED.")
