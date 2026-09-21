from playwright.sync_api import Page, Locator, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.products_title = page.locator(".title").get_by_text("Products")
        self.inventory_items = page.locator(".inventory_item")
        self.inventory_item_names = page.locator(".inventory_item_name")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

        # Cart page locators (for verification after opening cart)
        self.cart_item_names = page.locator(".cart_item_label .inventory_item_name")


    def is_products_page_displayed(self):
        """
        Verifies that the products page title is visible.
        """
        expect(self.products_title).to_be_visible()

    def get_product_count(self) -> int:
        """
        Returns the number of products currently displayed.
        """
        return self.inventory_items.count()

    def get_product_names(self) -> list[str]:
        """
        Returns a list of all displayed product names.
        """
        return self.inventory_item_names.all_text_contents()

    def add_product_to_cart(self, product_name: str):
        """
        Adds a specified product to the cart.
        Locates the product by its name and then clicks its 'Add to cart' button.
        """
        # Find the specific product item element that contains the product_name
        product_item_locator = self.page.locator(f".inventory_item:has-text('{product_name}')")
        expect(product_item_locator).to_be_visible() # Ensure the product is visible

        # Within that product item, find the 'Add to cart' button
        add_to_cart_button = product_item_locator.locator("button:has-text('Add to cart')")
        expect(add_to_cart_button).to_be_enabled() # Ensure the button is enabled
        add_to_cart_button.click()

    def open_cart(self):
        """
        Navigates to the shopping cart page.
        """
        expect(self.shopping_cart_link).to_be_visible()
        self.shopping_cart_link.click()

    def is_product_in_cart(self, product_name: str):
        """
        Checks if a product is present in the cart page.
        Assumes we are already on the cart page.
        """
        # We can locate by text content directly or use the previously defined cart_item_names
        expect(self.page.locator(f".cart_item_label:has-text('{product_name}')")).to_be_visible()
