from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Cart page locators
        self.checkout_button = page.locator("#checkout")

        # Checkout Step One (Your Information) locators
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

        # Checkout Step Two (Overview) locators
        self.checkout_overview_title = page.locator(".title").get_by_text("Checkout: Overview")
        self.finish_button = page.locator("#finish")
        self.cart_item_label = page.locator(".cart_item_label") # To verify product on overview page

        # Checkout Complete locators
        self.checkout_complete_header = page.locator(".complete-header")
        self.checkout_complete_text = page.locator(".complete-text")

    def click_checkout_from_cart(self):
        """
        Clicks the 'Checkout' button on the cart page.
        Assumes we are already on the cart page.
        """
        expect(self.checkout_button).to_be_visible()
        self.checkout_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str):
        """
        Enters customer information on the checkout step one page.
        """
        expect(self.first_name_input).to_be_visible()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    def verify_checkout_overview_displayed(self, product_name: str):
        """
        Verifies that the checkout overview page is displayed and contains the product.
        """
        expect(self.checkout_overview_title).to_be_visible()
        expect(self.page.locator(f".cart_item_label:has-text('{product_name}')")).to_be_visible()
        expect(self.finish_button).to_be_visible()

    def finish_order(self):
        """
        Clicks the 'Finish' button to complete the order.
        """
        expect(self.finish_button).to_be_visible()
        self.finish_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    def verify_order_complete(self):
        """
        Verifies that the order confirmation page is displayed.
        """
        expect(self.checkout_complete_header).to_be_visible()
        expect(self.checkout_complete_header).to_have_text("Thank you for your order!")
        expect(self.checkout_complete_text).to_be_visible()
        expect(self.checkout_complete_text).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
