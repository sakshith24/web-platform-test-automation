from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.test_data import VALID_USERNAME, VALID_PASSWORD, STANDARD_PRODUCT_NAME

def test_products_page_loads(page: Page):
    """
    Test to verify that the products page loads successfully after login.
    """
    print("\nRunning test_products_page_loads...")
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # Verify products page is displayed using its unique title
    products_page.is_products_page_displayed()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("test_products_page_loads PASSED.")


def test_products_are_displayed(page: Page):
    """
    Test to verify that products are listed on the products page.
    """
    print("\nRunning test_products_are_displayed...")
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    products_page.is_products_page_displayed() # Ensure we are on the products page

    # Verify at least one product is displayed
    product_count = products_page.get_product_count()
    assert product_count > 0, f"Expected at least one product, but found {product_count}"

    # Optionally, verify specific product names if needed (less brittle check)
    product_names = products_page.get_product_names()
    print(f"Found products: {product_names}")
    assert STANDARD_PRODUCT_NAME in product_names, \
        f"Expected '{STANDARD_PRODUCT_NAME}' not found in displayed products."
    print("test_products_are_displayed PASSED.")


def test_add_product_to_cart(page: Page):
    """
    Test to verify adding a product to the cart and checking its presence in the cart.
    """
    print(f"\nRunning test_add_product_to_cart for '{STANDARD_PRODUCT_NAME}'...")
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    products_page.is_products_page_displayed()

    # Add a specific product to the cart
    products_page.add_product_to_cart(STANDARD_PRODUCT_NAME)

    # Verify cart badge updates
    expect(products_page.shopping_cart_badge).to_have_text("1")

    # Open the cart
    products_page.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    # Verify the selected product is present in the cart
    products_page.is_product_in_cart(STANDARD_PRODUCT_NAME)
    print(f"Product '{STANDARD_PRODUCT_NAME}' successfully added to cart and verified. PASSED.")
