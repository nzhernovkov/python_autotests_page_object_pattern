from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_added_product(self):
        self.should_match_product_name()
        self.should_match_product_price()

    def should_match_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert name == alert_name, f"Alert product name '{alert_name}' not match actual product name '{name}"

    def should_match_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert price == alert_price, f"Alert product price '{alert_price}' not match actual product price '{price}'"
