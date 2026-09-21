from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from utils.test_data import VALID_USERNAME, VALID_PASSWORD, STANDARD_PRODUCT_NAME, CUSTOMER_INFO

def test_complete_checkout(page: Page):
    """
    End-to-end test for a complete checkout workflow.
    """
    print("\nRunning test_complete_checkout...")

    # Initialize Page Objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Login
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    products_page.is_products_page_displayed() # Verify login success

    # 2. Add Product to Cart
    products_page.add_product_to_cart(STANDARD_PRODUCT_NAME)
    expect(products_page.shopping_cart_badge).to_have_text("1")

    # 3. Open Cart & Verify Product
    products_page.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    products_page.is_product_in_cart(STANDARD_PRODUCT_NAME) # Important pre-checkout verification

    # 4. Click Checkout
    checkout_page.click_checkout_from_cart()

    # 5. Enter Customer Information
    checkout_page.enter_customer_information(
        CUSTOMER_INFO["first_name"],
        CUSTOMER_INFO["last_name"],
        CUSTOMER_INFO["postal_code"]
    )

    # 6. Verify Checkout Overview
    checkout_page.verify_checkout_overview_displayed(STANDARD_PRODUCT_NAME)
    # Additional verification: Check that the URL is correct for the overview page
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # 7. Finish Order
    checkout_page.finish_order()

    # 8. Verify Order Confirmation
    checkout_page.verify_order_complete()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    print("test_complete_checkout PASSED.")
