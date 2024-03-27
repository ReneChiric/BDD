from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishlistPage(BasePage):
    base_Url = "https://demo.nopcommerce.com/"
    URL_WISHLIST = "https://demo.nopcommerce.com/wishlist"
    EMPTY_WISHLIST_MESSAGE = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div')
    POPULATED_WISHLIST = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/form/div[1]/table/thead/tr/th[4]')
    REMOVE_PRODUCT_BUTTON = (By.NAME, 'updatecart')
    ADD_TO_WISHLIST = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div/div[4]/div[2]/div[2]/div/div[2]/div[3]/div[2]/button[3]')

    def navigate_to_wishlist_page(self):
        self.driver.get(self.URL_WISHLIST)

    def is_empty_wishlist_message_displayed(self):
        return self.is_element_displayed(self.EMPTY_WISHLIST_MESSAGE)

    def get_empty_wishlist_message_text(self):
        return self.get_element_text(self.EMPTY_WISHLIST_MESSAGE)

    def add_to_wishlist(self):
        self.driver.get(self.base_Url)
        self.click(self.ADD_TO_WISHLIST)

    def is_wishlist_populated(self):
        return self.is_element_displayed(self.POPULATED_WISHLIST)




