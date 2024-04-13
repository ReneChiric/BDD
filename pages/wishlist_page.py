from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishlistPage(BasePage):
    base_Url = "https://demo.nopcommerce.com/"
    URL_WISHLIST = "https://demo.nopcommerce.com/wishlist"
    EMPTY_WISHLIST_MESSAGE = (By.CLASS_NAME, 'no-data')
    PRODUCT_NAME = (By.CLASS_NAME, 'product-name')
    REMOVE_PRODUCT_BUTTON = (By.NAME, 'updatecart')


    def navigate_to_wishlist_page(self):
        self.driver.get(self.URL_WISHLIST)

    def is_empty_wishlist_message_displayed(self):
        return self.is_element_displayed(self.EMPTY_WISHLIST_MESSAGE)

    def get_empty_wishlist_message_text(self):
        return self.get_element_text(self.EMPTY_WISHLIST_MESSAGE)

    def add_to_wishlist(self):
        self.driver.get(self.base_Url)
        self.click(self.ADD_TO_WISHLIST)

    def verify_wishlist_message_displayed(self):
        assert self.is_element_displayed(self.EMPTY_WISHLIST_MESSAGE), "Mesajul nu este afisat"




