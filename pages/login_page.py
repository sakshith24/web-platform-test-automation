from playwright.sync_api import Page, expect
from utils.test_data import BASE_UI_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']") # Specific data-test attribute for error message
        self.products_title = page.locator(".title").get_by_text("Products") # Locator for products page title

    def open(self):
        """
        Navigates to the SauceDemo login page.
        """
        self.page.goto(BASE_UI_URL)

    def login(self, username, password):
        """
        Performs the login action with provided credentials.
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """
        Returns the text of the login error message.
        """
        return self.error_message.text_content()

    def is_products_page_visible(self):
        """
        Checks if the Products page title is visible after login.
        """
        expect(self.products_title).to_be_visible()
